#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
video_timing.py — lớp tính toán tất định (deterministic) của 05 Product Video Agent.

Chỉ tính toán, không đánh giá "viết hay hay dở":
  1. Số từ lồng tiếng từng câu → thời lượng ước tính (mặc định tốc độ đọc PT-BR 2,5 từ/giây, chỉnh bằng --wps)
  2. Timeline (thời điểm bắt đầu/kết thúc từng câu + cộng dồn)
  3. Độ dài dòng phụ đề (mặc định cảnh báo khi > 42 ký tự/dòng)
  4. Kiểm tra hook (câu đầu ≤ 8 từ, đảm bảo đọc xong trong 3 giây)
  5. Tổng thời lượng so với mục tiêu (15s / 30s, dung sai ±15%)

Đầu vào: kịch bản lồng tiếng dạng text thuần, một dòng = một câu thoại (một cảnh trong storyboard). Bỏ qua dòng trống và dòng chú thích bắt đầu bằng #.
Không phụ thuộc thư viện bên thứ ba, Python 3.9+.

Cách dùng:
  python video_timing.py --script kich_ban_long_tieng.txt --target 15
  python video_timing.py --script kich_ban_long_tieng.txt --target 30 --wps 2.4 --subtitle-max 40 --format json
"""
from __future__ import annotations

import argparse
import json
import sys
import unicodedata
from pathlib import Path

# ---------------------------------------------------------------- Hằng số

DEFAULT_WPS = 2.5          # Tốc độ đọc PT-BR: khoảng 150 từ/phút
DEFAULT_SUBTITLE_MAX = 42  # Giới hạn ký tự mỗi dòng phụ đề (giá trị kinh nghiệm cho khả năng đọc trên mobile)
HOOK_MAX_WORDS = 8         # Giới hạn số từ của câu hook đầu tiên (≈3 giây)
TOLERANCE = 0.15           # Sai lệch cho phép của tổng thời lượng so với mục tiêu ±15%

PLATFORM_TARGETS = {
    "shopee15": 15, "shopee30": 30,
    "mercadolivre15": 15, "mercadolivre30": 30,
    "15": 15, "30": 30,
}


# ---------------------------------------------------------------- Tiện ích

def _out(msg: str) -> None:
    print(msg, flush=True)


def _fmt_sec(t: float) -> str:
    return f"{t:.1f}s"


def _load_lines(path: str) -> list[str]:
    p = Path(path)
    if not p.exists():
        sys.exit(f"[INPUT_MISSING] Không tìm thấy file kịch bản lồng tiếng: {path}")
    lines: list[str] = []
    for i, raw in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        lines.append((i, line))  # Giữ số dòng gốc để dễ định vị
    if not lines:
        sys.exit(f"[INPUT_MISSING] {path} không có câu thoại hợp lệ nào (không tính dòng trống/dòng chú thích).")
    return lines


def _emoji_hit(text: str) -> bool:
    """Kiểm tra sơ bộ: chuỗi có chứa emoji / ký tự ký hiệu hay không (phụ đề không nên có)."""
    for ch in text:
        cat = unicodedata.category(ch)
        if cat in ("So", "Sk") or ord(ch) >= 0x1F000:
            return True
    return False


# ---------------------------------------------------------------- Tính toán cốt lõi

def analyze(lines: list[tuple[int, str]], wps: float, subtitle_max: int) -> dict:
    rows, t = [], 0.0
    issues: list[str] = []
    for idx, (src_no, text) in enumerate(lines, 1):
        words = len(text.split())
        dur = words / wps if wps > 0 else 0.0
        start, end = t, t + dur
        t = end
        row = {
            "index": idx,
            "source_line": src_no,
            "text": text,
            "words": words,
            "est_seconds": round(dur, 2),
            "timeline": f"{_fmt_sec(start)} → {_fmt_sec(end)}",
            "subtitle_chars": len(text),
        }
        # Độ dài dòng phụ đề
        if len(text) > subtitle_max:
            row["flag"] = f"Phụ đề {len(text)} ký tự > giới hạn {subtitle_max} (nên tách thành hai dòng hoặc rút gọn)"
            issues.append(f"Câu {idx}: {row['flag']}")
        if _emoji_hit(text):
            row["flag"] = "Nghi có emoji/ký tự đặc biệt, có thể lỗi hiển thị khi xuất phụ đề"
            issues.append(f"Câu {idx}: {row['flag']}")
        rows.append(row)

    # Kiểm tra hook (câu đầu tiên)
    hook_note = None
    if rows and rows[0]["words"] > HOOK_MAX_WORDS:
        hook_note = (
            f"Câu đầu {rows[0]['words']} từ > {HOOK_MAX_WORDS} từ, "
            f"với {wps} từ/giây cần {_fmt_sec(rows[0]['est_seconds'])}, "
            f"vượt khung 3 giây vàng mở đầu, nên rút gọn hook"
        )
        issues.append(hook_note)

    return {"rows": rows, "total_seconds": round(t, 2), "issues": issues,
            "hook_note": hook_note}


def target_check(total: float, target: float | None) -> dict | None:
    if not target:
        return None
    lo, hi = target * (1 - TOLERANCE), target * (1 + TOLERANCE)
    ok = lo <= total <= hi
    return {
        "target": target,
        "window": f"{_fmt_sec(lo)} – {_fmt_sec(hi)}",
        "delta": round(total - target, 2),
        "pass": ok,
        "verdict": ("✅ Đạt thời lượng" if ok else
                    (f"❌ Thiếu {abs(total - target):.1f}s (chưa đủ nội dung, cần thêm câu điểm bán hàng hoặc giãn nhịp)"
                     if total < lo else
                     f"❌ Vượt {total - target:.1f}s (cần bỏ câu hoặc tăng tốc, cắt số từ thoại theo trần {target}s×{DEFAULT_WPS} từ/giây ≈ {int(target * DEFAULT_WPS)} từ)")),
    }


# ---------------------------------------------------------------- Xuất kết quả

def to_markdown(res: dict, chk: dict | None, wps: float, subtitle_max: int) -> str:
    L = ["# Báo cáo kiểm tra thời lượng lồng tiếng và phụ đề\n"]
    L.append(f"- Giả định tốc độ đọc: **{wps} từ/giây** (giá trị kinh nghiệm cho giọng đọc PT-BR, chỉnh bằng --wps)")
    L.append(f"- Giới hạn mỗi dòng phụ đề: **{subtitle_max} ký tự**")
    L.append(f"- Tổng số câu: **{len(res['rows'])}**")
    L.append(f"- Tổng thời lượng ước tính: **{_fmt_sec(res['total_seconds'])}**")
    if chk:
        L.append(f"- Thời lượng mục tiêu: {chk['target']}s (cho phép {chk['window']}) → **{chk['verdict']}**")
    L.append("")
    L.append("| # | Timeline | Số từ | Thời lượng ước tính | Ký tự phụ đề | Câu thoại |")
    L.append("|---|---|---|---|---|---|")
    for r in res["rows"]:
        flag = f" ⚠️{r['flag']}" if "flag" in r else ""
        L.append(f"| {r['index']} | {r['timeline']} | {r['words']} | "
                 f"{_fmt_sec(r['est_seconds'])} | {r['subtitle_chars']} | "
                 f"{r['text'][:40]}{'…' if len(r['text']) > 40 else ''}{flag} |")
    L.append("")
    if res["hook_note"]:
        L.append(f"> 🪝 {res['hook_note']}\n")
    if res["issues"]:
        L.append(f"## Cần xử lý ({len(res['issues'])} mục)\n")
        for x in res["issues"]:
            L.append(f"- {x}")
    else:
        L.append("## Cần xử lý\n\n- Không có ✅ (thời lượng và phụ đề đều đạt)")
    L.append("")
    L.append("> ⚠️ Thời lượng ước tính dựa trên mô hình tốc độ đọc đều, **không thay thế được việc nghe thử bản đọc thật/công cụ lồng tiếng**. "
             "Trước khi bàn giao, hãy nghe lại bản lồng tiếng thực tế để tinh chỉnh.")
    return "\n".join(L)


def main() -> None:
    ap = argparse.ArgumentParser(description="Kiểm tra thời lượng lồng tiếng và phụ đề (tính toán tất định)")
    ap.add_argument("--script", required=True, help="File kịch bản lồng tiếng: một dòng = một câu thoại")
    ap.add_argument("--target", help="Số giây mục tiêu (15 / 30) hoặc khóa sàn shopee15/shopee30, v.v.")
    ap.add_argument("--wps", type=float, default=DEFAULT_WPS, help=f"Tốc độ đọc, từ/giây (mặc định {DEFAULT_WPS})")
    ap.add_argument("--subtitle-max", type=int, default=DEFAULT_SUBTITLE_MAX,
                    help=f"Giới hạn ký tự mỗi dòng phụ đề (mặc định {DEFAULT_SUBTITLE_MAX})")
    ap.add_argument("--format", choices=["md", "json", "both"], default="md")
    ap.add_argument("-o", "--output", help="Tiền tố file đầu ra (mặc định chỉ in ra màn hình)")
    args = ap.parse_args()

    lines = _load_lines(args.script)
    target = None
    if args.target:
        key = str(args.target).strip().lower()
        target = PLATFORM_TARGETS.get(key)
        if target is None:
            try:
                target = float(key)
            except ValueError:
                sys.exit(f"[INPUT_MISSING] Không nhận diện được thời lượng mục tiêu: {args.target} "
                         f"(dùng được: {', '.join(sorted(PLATFORM_TARGETS))} hoặc số giây bất kỳ)")

    res = analyze(lines, args.wps, args.subtitle_max)
    chk = target_check(res["total_seconds"], target)

    md = to_markdown(res, chk, args.wps, args.subtitle_max)
    payload = {
        "meta": {"wps": args.wps, "subtitle_max": args.subtitle_max,
                 "target": target, "total_seconds": res["total_seconds"],
                 "lines": len(res["rows"])},
        "timeline": res["rows"],
        "target_check": chk,
        "issues": res["issues"],
    }

    if args.format in ("md", "both"):
        _out(md)
    if args.format in ("json", "both"):
        js = json.dumps(payload, ensure_ascii=False, indent=2)
        if args.format == "json":
            _out(js)
    if args.output:
        pref = Path(args.output)
        if args.format in ("md", "both"):
            pref.with_suffix(".md").write_text(md, encoding="utf-8")
        if args.format in ("json", "both"):
            pref.with_suffix(".json").write_text(
                json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        _out(f"\nĐã ghi: {pref.with_suffix('.md')}" +
             (f" / {pref.with_suffix('.json')}" if args.format in ("json", "both") else ""))


if __name__ == "__main__":
    main()
