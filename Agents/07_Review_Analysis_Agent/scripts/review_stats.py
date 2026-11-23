#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
review_stats.py — lớp tính toán xác định (deterministic) của 07 Review Analysis Agent.

Ranh giới phân công: **phân loại giao cho mô hình, đếm số giao cho script.**
  Việc của mô hình: xếp từng đánh giá vào 8 nhóm nguyên nhân đánh giá tiêu cực /
                    điểm bán hàng từ đánh giá tích cực (phán đoán ngữ nghĩa)
  Việc của script:  tổng hợp, tỷ trọng, tỷ lệ khắc phục được, kiểm tra tổng,
                    xếp hạng điểm bán hàng (tính toán xác định)

Đầu vào 1: CSV đánh giá (bắt buộc cột rating; dòng tiêu cực nên có cột category;
           cột has_image tùy chọn)
Đầu vào 2 (tùy chọn): CSV điểm bán hàng (cột: điểm bán hàng, tần suất, mức độ
           [mạnh/vừa/yếu]) → xếp hạng theo tần suất × trọng số
Đầu ra: phân bố đánh giá tích cực / trung lập / tiêu cực, số lượng và tỷ trọng
        theo 8 nhóm nguyên nhân, tỷ lệ khắc phục được (kèm kiểm tra tổng),
        bảng xếp hạng điểm tổng hợp của điểm bán hàng, danh sách dòng chưa quy
        nguyên nhân / chưa phân loại.

Không cần thư viện bên thứ ba, Python 3.9+.

Cách dùng:
  python review_stats.py --file danh_gia.csv --fixable "Hiểu lầm,Thông số không như kỳ vọng,Thiếu phụ kiện,Khó sử dụng"
  python review_stats.py --file danh_gia.csv --points diem_ban_hang.csv --format json

Tên nhóm nguyên nhân và mức độ bằng tiếng Trung (误解型, 强/中/弱 …) vẫn được
nhận diện và tự động quy đổi sang tên tiếng Việt.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

WEIGHT = {"mạnh": 3, "vừa": 2, "yếu": 1}
STRENGTH_ALIASES = {
    "强": "mạnh", "strong": "mạnh", "forte": "mạnh",
    "中": "vừa", "medium": "vừa", "médio": "vừa", "medio": "vừa", "trung bình": "vừa",
    "弱": "yếu", "weak": "yếu", "fraco": "yếu",
}
DEFAULT_STRENGTH = "vừa"

CATEGORY_ALIASES = {
    "误解型": "Hiểu lầm",
    "产品质量问题": "Lỗi chất lượng sản phẩm",
    "参数不符合预期": "Thông số không như kỳ vọng",
    "配件缺失": "Thiếu phụ kiện",
    "发货慢": "Giao hàng chậm",
    "使用困难": "Khó sử dụng",
    "售后差": "Hậu mãi kém",
    "破损/故障/退货": "Hư hỏng/lỗi/trả hàng",
    "破损 / 故障 / 退货": "Hư hỏng/lỗi/trả hàng",
}
DEFAULT_FIXABLE = "Hiểu lầm,Thông số không như kỳ vọng,Thiếu phụ kiện,Khó sử dụng"

RATING_COLS = ["rating", "评分", "星级", "đánh giá", "số sao", "điểm",
               "avaliacao", "estrelas", "stars"]
CATEGORY_COLS = ["category", "归因", "分类", "差评归因", "nguyên nhân",
                 "phân loại", "quy nguyên nhân", "categoria"]
IMAGE_COLS = ["has_image", "带图", "有图", "có ảnh", "com_imagem", "com_foto", "image"]
POINT_COLS = ["卖点", "điểm bán hàng", "selling_point", "point"]
FREQ_COLS = ["频次", "次数", "tần suất", "số lần", "frequency", "count"]
STRENGTH_COLS = ["强度", "情感强度", "mức độ", "mức độ cảm xúc", "strength", "weight"]


def _out(msg: str) -> None:
    print(msg, flush=True)


def _norm_category(v: str) -> str:
    v = v.strip()
    return CATEGORY_ALIASES.get(v, v)


def _norm_strength(v: str) -> str:
    v = v.strip()
    return STRENGTH_ALIASES.get(v, STRENGTH_ALIASES.get(v.lower(), v.lower()))


def _pick(row_cols: list[str], candidates: list[str], label: str,
          required: bool) -> str | None:
    lowered = {c.strip().lower(): c for c in row_cols}
    for c in candidates:
        if c in row_cols:
            return c
        if c.lower() in lowered:
            return lowered[c.lower()]
    if required:
        sys.exit(f"[INPUT_MISSING] Không tìm thấy cột {label}. Các cột hiện có: {', '.join(row_cols)}"
                 f" (tên cột được nhận diện: {', '.join(candidates)})")
    return None


def _num(v, default=0.0):
    if v is None:
        return default
    s = str(v).strip().replace("%", "").replace(" ", "")
    if s in ("", "-", "—", "暂无", "chưacó", "N/A", "nan"):
        return default
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".")
    elif "," in s:
        parts = s.split(",")
        s = parts[0] + "." + parts[1] if len(parts) == 2 and len(parts[1]) != 3 \
            else s.replace(",", "")
    try:
        return float(s)
    except ValueError:
        return default


def _truthy(v) -> bool:
    return str(v).strip().lower() in ("1", "1.0", "true", "yes", "y", "是", "有", "có", "sim")


# ---------------------------------------------------------------- Tính toán chính

def analyze_reviews(path: str, fixable: set[str]) -> dict:
    p = Path(path)
    if not p.exists():
        sys.exit(f"[INPUT_MISSING] Không tìm thấy file đánh giá: {path}")
    with p.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        sys.exit(f"[INPUT_MISSING] {path} không có dòng dữ liệu nào.")
    cols = list(rows[0].keys())

    rc = _pick(cols, RATING_COLS, "số sao (rating)", required=True)
    cc = _pick(cols, CATEGORY_COLS, "nguyên nhân (category)", required=False)
    ic = _pick(cols, IMAGE_COLS, "có ảnh (has_image)", required=False)

    total = len(rows)
    good = mid = bad = imgs = 0
    unrate = 0
    attr: dict[str, int] = {}
    unattributed: list[str] = []

    for i, r in enumerate(rows, 2):
        val = _num(r.get(rc), default=None)
        if val is None or val < 1 or val > 5:
            unrate += 1
            continue
        if val >= 4:
            good += 1
        elif val == 3:
            mid += 1
        else:
            bad += 1
            cat = _norm_category(r.get(cc) or "") if cc else ""
            if cat:
                attr[cat] = attr.get(cat, 0) + 1
            else:
                unattributed.append(f"dòng {i}")
        if ic and _truthy(r.get(ic)):
            imgs += 1

    rated = good + mid + bad
    attr_total = sum(attr.values())
    mismatch = attr_total - bad  # phải bằng 0
    fixable_count = sum(v for k, v in attr.items() if k in fixable)
    unknown_cats = sorted(set(attr) - fixable - set())  # toàn bộ nhóm

    return {
        "total": total, "unrated": unrate,
        "good": good, "mid": mid, "bad": bad,
        "good_rate": round(good / rated, 4) if rated else 0,
        "mid_rate": round(mid / rated, 4) if rated else 0,
        "bad_rate": round(bad / rated, 4) if rated else 0,
        "image_count": imgs,
        "image_rate": round(imgs / total, 4) if total else 0,
        "attribution": dict(sorted(attr.items(), key=lambda kv: -kv[1])),
        "attribution_total": attr_total,
        "attribution_mismatch": mismatch,
        "unattributed": unattributed,
        "fixable_set": sorted(fixable),
        "fixable_count": fixable_count,
        "fixable_rate": round(fixable_count / bad, 4) if bad else 0,
        "all_categories": unknown_cats,
    }


def analyze_points(path: str) -> dict | None:
    p = Path(path)
    if not p.exists():
        sys.exit(f"[INPUT_MISSING] Không tìm thấy file điểm bán hàng: {path}")
    with p.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        return None
    cols = list(rows[0].keys())
    pc = _pick(cols, POINT_COLS, "điểm bán hàng", required=True)
    fc = _pick(cols, FREQ_COLS, "tần suất", required=True)
    sc = _pick(cols, STRENGTH_COLS, "mức độ", required=False)

    out = []
    for r in rows:
        name = (r.get(pc) or "").strip()
        if not name:
            continue
        freq = int(_num(r.get(fc)))
        s_raw = (r.get(sc) or DEFAULT_STRENGTH).strip() if sc else DEFAULT_STRENGTH
        s_norm = _norm_strength(s_raw)
        w = WEIGHT.get(s_norm)
        if w is None:
            sys.exit(f"[INPUT_MISSING] Không nhận diện được mức độ: {s_raw!r}"
                     f" (giá trị hợp lệ: mạnh/vừa/yếu)")
        out.append({"point": name, "freq": freq, "strength": s_norm,
                    "weight": w, "score": freq * w})
    out.sort(key=lambda x: -x["score"])
    for i, x in enumerate(out, 1):
        x["rank"] = i
    return {"rows": out}


# ---------------------------------------------------------------- Xuất kết quả

def to_markdown(res: dict, pts: dict | None, fixable: set[str]) -> str:
    L = ["# Báo cáo thống kê đánh giá (tổng hợp xác định)\n"]
    L.append("## 1. Phân bố tổng thể\n")
    L.append(f"- Tổng số đánh giá: **{res['total']}**"
             + (f" (đã loại {res['unrated']} đánh giá thiếu số sao)" if res["unrated"] else ""))
    L.append(f"- Tích cực (4–5★): **{res['good']}** ({res['good_rate']:.1%})")
    L.append(f"- Trung lập (3★): **{res['mid']}** ({res['mid_rate']:.1%})")
    L.append(f"- Tiêu cực (1–2★): **{res['bad']}** ({res['bad_rate']:.1%})")
    if res["image_count"]:
        L.append(f"- Đánh giá có ảnh: {res['image_count']} ({res['image_rate']:.1%})")
    L.append("")

    L.append("## 2. Quy nguyên nhân đánh giá tiêu cực\n")
    if res["attribution_mismatch"] != 0:
        L.append(f"> 🔴 **Kiểm tra tổng thất bại**: tổng đã quy nguyên nhân {res['attribution_total']}"
                 f" ≠ số đánh giá tiêu cực {res['bad']} (lệch {res['attribution_mismatch']:+d}). "
                 f"**Sửa dữ liệu trước rồi mới kết luận**, {len(res['unattributed'])} dòng chưa quy nguyên nhân: "
                 f"{', '.join(res['unattributed'][:6])}"
                 f"{'…' if len(res['unattributed']) > 6 else ''}\n")
    L.append("| Nhóm | Số lượng | Tỷ trọng trong tiêu cực | Khắc phục được |")
    L.append("|---|---|---|---|")
    bad = res["bad"] or 1
    for k, v in res["attribution"].items():
        mark = "✅" if k in fixable else "❌"
        L.append(f"| {k} | {v} | {v / bad:.1%} | {mark} |")
    L.append(f"| **Tổng** | **{res['attribution_total']}** | "
             f"{res['attribution_total'] / bad:.1%} | "
             f"**{res['fixable_count']} đánh giá khắc phục được = {res['fixable_rate']:.1%}** |")
    L.append("")
    L.append(f"> Tiêu chí khắc phục được (chỉ định bằng --fixable): {', '.join(res['fixable_set'])}. "
             f"Khắc phục được = chỉ cần sửa nội dung / bổ sung ảnh / bổ sung giải thích, chi phí gần bằng 0; "
             f"không khắc phục được = nhóm vận chuyển / chất lượng, mất hàng tuần đến hàng tháng.\n")

    if pts:
        L.append("## 3. Xếp hạng điểm bán hàng từ đánh giá tích cực (tần suất × trọng số cảm xúc)\n")
        L.append("| # | Điểm bán hàng | Tần suất nhắc đến | Mức độ | Trọng số | Điểm tổng hợp |")
        L.append("|---|---|---|---|---|---|")
        for r in pts["rows"]:
            L.append(f"| {r['rank']} | {r['point']} | {r['freq']} | "
                     f"{r['strength']} | {r['weight']} | **{r['score']}** |")
        L.append("")
        L.append("> Điểm tổng hợp = tần suất × trọng số (mạnh=3 / vừa=2 / yếu=1). "
                 "Bảng xếp hạng định hướng thứ tự ưu tiên điểm bán hàng trên trang chi tiết và ảnh chính, "
                 "**không xác nhận tính xác thực** — tính xác thực vẫn phải đối chiếu với spec_table.\n")
    return "\n".join(L)


def main() -> None:
    ap = argparse.ArgumentParser(description="Tổng hợp thống kê đánh giá (tính toán xác định)")
    ap.add_argument("--file", required=True,
                    help="CSV đánh giá (bắt buộc rating, category/has_image tùy chọn)")
    ap.add_argument("--fixable", default=DEFAULT_FIXABLE,
                    help="Các nhóm khắc phục được, phân tách bằng dấu phẩy")
    ap.add_argument("--points", help="CSV điểm bán hàng (điểm bán hàng, tần suất, mức độ), tùy chọn")
    ap.add_argument("--format", choices=["md", "json", "both"], default="md")
    ap.add_argument("-o", "--output", help="Tiền tố file đầu ra")
    args = ap.parse_args()

    fixable = {_norm_category(x) for x in args.fixable.split(",") if x.strip()}
    res = analyze_reviews(args.file, fixable)
    pts = analyze_points(args.points) if args.points else None

    md = to_markdown(res, pts, fixable)
    if args.format in ("md", "both"):
        _out(md)
    if args.format in ("json", "both"):
        payload = {"reviews": res, "selling_points": pts}
        _out("\n" + json.dumps(payload, ensure_ascii=False, indent=2))
    if args.output:
        pref = Path(args.output)
        if args.format in ("md", "both"):
            pref.with_suffix(".md").write_text(md, encoding="utf-8")
        if args.format in ("json", "both"):
            pref.with_suffix(".json").write_text(
                json.dumps({"reviews": res, "selling_points": pts},
                           ensure_ascii=False, indent=2), encoding="utf-8")
        _out(f"\nĐã ghi: {pref.with_suffix('.md')}")


if __name__ == "__main__":
    main()
