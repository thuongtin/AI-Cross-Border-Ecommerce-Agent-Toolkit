#!/usr/bin/env python3
"""Kiểm tra tính nhất quán thông số — tự động hóa nguyên tắc "thông số chỉ có một nguồn duy nhất".

  python spec_consistency.py --spec spec_table.csv --text noi_dung.txt --allow 2026,110
  python spec_consistency.py --spec spec_table.csv --title "Tiêu đề" --text chi_tiet.md

Quy tắc: **mọi con số xuất hiện trong nội dung đều phải truy được về spec_table**.
  Truy được = trùng với một con số trong giá trị thông số (20000 của 20000mAh, 45 của 45W, 3 của 3 Saídas).
  Số không truy được = lệch thông số (gõ nhầm / bịa ra / không thống nhất cách tính), liệt kê từng số kèm ngữ cảnh.

Kiểm tra ngược: con số trong spec_table chưa từng xuất hiện trong nội dung = thông số chưa được nhắc tới, nhắc bổ sung nội dung.
"""
import argparse
import csv
import json
import re
import sys

NUM_RE = re.compile(r"(?<![\w.])(\d{1,3}(?:[.,]\d{3})+|\d+(?:[.,]\d+)?)(?![\w]*\d)(?=[^\d]|$)")


def load_spec(path):
    """spec_table: CSV (2 cột Thông số,Giá trị) hoặc JSON (dict). Trả về [(thông số, giá trị gốc, tập các con số)]."""
    specs = []
    if path.endswith(".json"):
        with open(path, encoding="utf-8") as f:
            for k, v in json.load(f).items():
                specs.append((k, str(v), _nums_in(str(v))))
        return specs
    with open(path, encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    for row in rows:
        if len(row) < 2 or not row[1].strip():
            continue
        if row[0].strip().lower() in ("参数", "param", "key", "项目", "thông số", "tham số", "hạng mục"):
            continue
        val = row[1].strip()
        specs.append((row[0].strip(), val, _nums_in(val)))
    return specs


def _nums_in(s):
    """Tách số từ chuỗi: hỗ trợ 20.000 (dấu phân cách hàng nghìn kiểu Brazil), 20,000, 20000, 1.5."""
    out = set()
    for m in re.finditer(r"\d{1,3}(?:[.,]\d{3})+(?!\d)|\d+(?:[.,]\d+)?", s):
        t = m.group()
        if re.fullmatch(r"\d{1,3}(?:[.,]\d{3})+", t):
            t = t.replace(".", "").replace(",", "")
        else:
            t = t.replace(",", ".")
        try:
            f = float(t)
            out.add(int(f) if f == int(f) else round(f, 4))
        except ValueError:
            pass
    return out


def check(text, specs, allow):
    allow_nums = _nums_in(",".join(allow)) if allow else set()
    spec_nums = {}
    for name, raw, nums in specs:
        for n in nums:
            spec_nums.setdefault(n, []).append(name)

    text_norm = text.replace("\u00a0", " ")
    # Các con số trong nội dung (kèm ngữ cảnh)
    found, untraceable = [], []
    for m in re.finditer(r"\d{1,3}(?:[.,]\d{3})+(?!\d)|\d+(?:[.,]\d+)?", text_norm):
        raw = m.group()
        t = raw
        if re.fullmatch(r"\d{1,3}(?:[.,]\d{3})+", t):
            t = t.replace(".", "").replace(",", "")
        else:
            t = t.replace(",", ".")
        try:
            n = float(t)
            n = int(n) if n == int(n) else round(n, 4)
        except ValueError:
            continue
        ctx = text_norm[max(0, m.start() - 25): m.end() + 25].replace("\n", " ")
        found.append((n, raw, ctx))
        if n in spec_nums or n in allow_nums:
            continue
        untraceable.append(dict(number=raw, context=f"…{ctx}…",
                                hint="Không truy được về spec_table — gõ nhầm / bịa ra / không thống nhất cách tính?"))

    # Kiểm tra ngược: thông số chưa từng xuất hiện (chỉ xét thông số có chứa số; thông số không có số như "Display Digital" thì không đối chiếu được)
    missing = []
    for name, raw, nums in specs:
        if not nums:
            continue
        hit = any(re.search(rf"(?<![\d.,]){re.escape(str(n))}(?![\d])", text_norm) for n in nums)
        if not hit:
            missing.append(f"{name} ({raw})")

    ok = not untraceable
    return dict(ok=ok, spec_count=len(specs),
                numbers_in_text=len(found),
                untraceable=untraceable,
                missing_specs=missing)


def main():
    ap = argparse.ArgumentParser(description="Kiểm tra tính nhất quán thông số (nguyên tắc thông số chỉ có một nguồn duy nhất)")
    ap.add_argument("--spec", required=True, help="spec_table: CSV (Thông số,Giá trị) hoặc JSON")
    ap.add_argument("--text", help="File nội dung (tốt nhất là kiểm tra tiêu đề + trang chi tiết cùng lúc)")
    ap.add_argument("--title", help="Nội dung tiêu đề (có thể truyền cùng --text để kiểm tra gộp)")
    ap.add_argument("--allow", help="Các số được miễn kiểm tra, phân tách bằng dấu phẩy (năm, hằng số không liên quan...)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if not args.text and not args.title:
        sys.exit("[ERROR] Cần truyền file --text hoặc nội dung --title")
    text = ""
    if args.title:
        text += args.title + "\n"
    if args.text:
        try:
            with open(args.text, encoding="utf-8") as f:
                text += f.read()
        except OSError as e:
            sys.exit(f"[ERROR] Không đọc được file: {e}")

    specs = load_spec(args.spec)
    if not specs:
        sys.exit("[ERROR] spec_table không có thông số nào dùng được")
    allow = [a.strip() for a in args.allow.split(",")] if args.allow else []

    rep = check(text, specs, allow)
    if args.json:
        print(json.dumps(rep, ensure_ascii=False, indent=2))
    else:
        print(f"\nThông số: {rep['spec_count']} mục | Số trong nội dung: {rep['numbers_in_text']} chỗ | "
              f"Kết luận: {'✅ Truy được toàn bộ' if rep['ok'] else '❌ Có lệch thông số'}")
        for u in rep["untraceable"]:
            print(f"  ❌ {u['number']}: {u['context']}")
        if rep["missing_specs"]:
            print(f"  ⚠️ Các thông số sau chưa từng xuất hiện trong nội dung (nên bổ sung): {', '.join(rep['missing_specs'])}")
    sys.exit(0 if rep["ok"] else 1)


if __name__ == "__main__":
    main()
