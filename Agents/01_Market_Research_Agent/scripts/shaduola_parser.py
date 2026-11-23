#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
shaduola_parser.py — Chuẩn hóa dữ liệu xuất ngành hàng (CSV / XLSX) thành JSON

Mục đích: giải quyết khâu "đưa dữ liệu vào thế nào". Agent chỉ nhận JSON đã chuẩn hóa,
          không nhận các định dạng xuất đủ kiểu của từng sàn.

Phụ thuộc: chỉ thư viện chuẩn. Đọc XLSX cần openpyxl (tùy chọn, thiếu sẽ có thông báo).

Cách dùng:
    python shaduola_parser.py <file_đầu_vào> [-o đầu_ra.json] [--mapping ánh_xạ.json]
    python shaduola_parser.py data.csv -o out.json
    python shaduola_parser.py data.csv --profile     # chỉ in các cột nhận diện được, không chuyển đổi
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import unicodedata
from typing import Any

# ---------------------------------------------------------------------------
# Ánh xạ tên cột: khóa = tên trường chuẩn, giá trị = các tên cột có thể gặp
# (không phân biệt hoa thường, so khớp sau khi bỏ khoảng trắng).
# Giữ alias tiếng Trung (file xuất từ Shaduola/công cụ Trung Quốc) và thêm alias tiếng Việt.
# ---------------------------------------------------------------------------
DEFAULT_MAPPING: dict[str, list[str]] = {
    "title":        ["商品名称", "商品名", "标题", "产品名称", "tên sản phẩm", "tên sp", "tiêu đề",
                     "product name", "title", "nome do produto"],
    "price":        ["价格", "售价", "均价", "商品价格", "giá", "giá bán", "giá sản phẩm",
                     "price", "preço", "preco"],
    "monthly_sales": ["月销量", "月销", "30天销量", "近30天销量", "lượng bán tháng", "lượt bán tháng",
                      "đã bán tháng", "đã bán 30 ngày", "monthly sales", "vendas mensais"],
    "monthly_revenue": ["月销售额", "月销售额(元)", "销售额", "月gmv", "doanh thu tháng", "doanh thu",
                        "gmv tháng", "revenue", "faturamento"],
    "total_sales":  ["总销量", "累计销量", "tổng lượng bán", "tổng đã bán", "total sales", "vendas totais"],
    "seller":       ["卖家", "店铺", "店铺名称", "卖家名称", "người bán", "tên shop", "shop",
                     "seller", "loja", "vendedor"],
    "brand":        ["品牌", "品牌名", "thương hiệu", "brand", "marca"],
    "rating":       ["评分", "商品评分", "điểm đánh giá", "rating", "avaliação", "avaliacao"],
    "review_count": ["评价数", "评论数", "评价数量", "số đánh giá", "lượt đánh giá", "review count", "avaliações"],
    "listing_age_days": ["上架天数", "上架时间", "已上架", "thời gian đăng bán", "số ngày đăng bán",
                         "ngày đăng bán", "listing age"],
    "url":          ["商品链接", "链接", "link sản phẩm", "url", "link"],
    "category":     ["类目", "分类", "ngành hàng", "danh mục", "category", "categoria"],
}

# Các trường số trong đầu ra đã chuẩn hóa
NUMERIC_FIELDS = [
    "price", "monthly_sales", "monthly_revenue", "total_sales",
    "rating", "review_count", "listing_age_days",
]

# Đơn vị số lượng (tiếng Trung / tiếng Việt / tiếng Anh)
_CN_UNITS = {
    "万": 10_000, "亿": 100_000_000,
    "nghìn": 1_000, "ngàn": 1_000, "triệu": 1_000_000, "tr": 1_000_000, "tỷ": 1_000_000_000,
    "k": 1_000, "K": 1_000, "m": 1_000_000, "M": 1_000_000,
}


def _norm_key(s: str) -> str:
    """Chuẩn hóa tên cột: chuẩn Unicode NFC, bỏ khoảng trắng và dấu ngoặc, chuyển chữ thường."""
    if s is None:
        return ""
    s = unicodedata.normalize("NFC", str(s))
    s = s.replace("\u3000", " ").replace("\xa0", " ")
    s = re.sub(r"[\s\(\)（）\[\]【】:：]", "", s)
    return s.strip().lower()


def _to_number(raw: Any) -> float | None:
    """
    Chuyển dữ liệu "bẩn" thành số.

    Xử lý: ký hiệu tiền tệ (R$ / $ / ¥ / BRL / ₫ / VND), dấu phân cách hàng nghìn (phẩy/chấm/khoảng trắng),
           đơn vị số lượng (万 / 亿 / nghìn / triệu / tỷ / k / M), phần trăm, hậu tố "+",
           giá trị rỗng, '-' / 'N/A'.
    """
    if raw is None:
        return None
    if isinstance(raw, (int, float)):
        try:
            return float(raw)
        except (TypeError, ValueError):
            return None

    s = unicodedata.normalize("NFC", str(raw)).strip()
    if s == "" or s.lower() in {"-", "--", "n/a", "na", "não", "nao", "null", "none", "无", "暂无",
                                "không có", "chưa có"}:
        return None

    # Bỏ ký hiệu và chữ chỉ tiền tệ
    s = re.sub(r"(?i)(R\$|BRL|USD|VNĐ|VND|\$|¥|€|£|₫|đ|元|雷亚尔)", "", s)
    s = s.replace("%", "").strip().rstrip("+").strip()

    # Đơn vị số lượng tiếng Trung / tiếng Việt / tiếng Anh
    mult = 1.0
    for unit, factor in _CN_UNITS.items():
        if s.endswith(unit):
            mult = float(factor)
            s = s[: -len(unit)].strip()
            break

    # Bỏ dấu phân cách hàng nghìn (trường hợp dấu cuối cùng là dấu thập phân sẽ xét bên dưới)
    s = s.replace(" ", "")
    if "," in s and "." in s:
        # Có cả hai: dấu xuất hiện sau cùng là dấu thập phân  1.234,56 → 1234.56 / 1,234.56 → 1234.56
        if s.rfind(",") > s.rfind("."):
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    elif "," in s:
        # Chỉ có dấu phẩy: 1,234 coi là phân cách hàng nghìn; 1,5 coi là dấu thập phân
        head, _, tail = s.rpartition(",")
        s = (head.replace(",", "") + "." + tail) if len(tail) == 1 else s.replace(",", "")
    elif s.count(".") > 1:
        # Nhiều dấu chấm (kiểu Việt Nam 1.234.567) → đều là phân cách hàng nghìn
        s = s.replace(".", "")

    try:
        return float(s) * mult
    except ValueError:
        return None


def _to_days(raw: Any) -> int | None:
    """Thời gian đăng bán → số ngày. Hỗ trợ '30 ngày' / '2 tháng' / '1 năm' / '30天' / '2个月' / '2026-01-15' / '365'."""
    if raw is None:
        return None
    s = unicodedata.normalize("NFC", str(raw)).strip()
    if not s or s.lower() in {"n/a", "-", "无", "không có"}:
        return None

    m = re.search(r"(\d+(?:\.\d+)?)\s*(天|日|ngày)", s, re.IGNORECASE)
    if m:
        return int(float(m.group(1)))
    m = re.search(r"(\d+(?:\.\d+)?)\s*(?:个?\s*月|tháng)", s, re.IGNORECASE)
    if m:
        return int(float(m.group(1)) * 30)
    m = re.search(r"(\d+(?:\.\d+)?)\s*(?:年|năm)", s, re.IGNORECASE)
    if m:
        return int(float(m.group(1)) * 365)
    m = re.match(r"^\d{4}[-/](\d{1,2})[-/](\d{1,2})", s)
    if m:
        # Tính gần đúng: đếm từ ngày 1/1 của năm đó, tránh vấn đề múi giờ của datetime
        return int((int(m.group(1)) - 1) * 30 + int(m.group(2)))
    n = _to_number(s)
    return int(n) if n is not None else None


# ---------------------------------------------------------------------------
# Tầng đọc dữ liệu
# ---------------------------------------------------------------------------
def read_rows(path: str) -> list[dict[str, Any]]:
    """Đọc CSV / TSV / XLSX thành list[dict]. Tự dò encoding và dấu phân cách."""
    ext = os.path.splitext(path)[1].lower()

    if ext in {".xlsx", ".xlsm", ".xls"}:
        try:
            import openpyxl  # type: ignore
        except ImportError:
            sys.exit(
                "[ERROR] Đọc XLSX cần openpyxl. Hãy cài trước:\n"
                "        pip install openpyxl\n"
                "        hoặc lưu bảng tính thành CSV rồi chạy lại."
            )
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        ws = wb.active
        rows_iter = ws.iter_rows(values_only=True)
        try:
            header = [str(c) if c is not None else "" for c in next(rows_iter)]
        except StopIteration:
            return []
        out = []
        for r in rows_iter:
            if r is None or all(c is None or str(c).strip() == "" for c in r):
                continue
            out.append({header[i]: (r[i] if i < len(r) else None) for i in range(len(header))})
        wb.close()
        return out

    # File văn bản: dò encoding
    text = None
    for enc in ("utf-8-sig", "utf-8", "gbk", "gb18030", "latin-1"):
        try:
            with open(path, "r", encoding=enc, newline="") as f:
                text = f.read()
            break
        except UnicodeDecodeError:
            continue
    if text is None:
        sys.exit(f"[ERROR] Không nhận diện được encoding của file: {path}")

    sample = text[:4096]
    delim = "\t" if sample.count("\t") > sample.count(",") else ","
    reader = csv.DictReader(text.splitlines(), delimiter=delim)
    return [dict(r) for r in reader]


def build_column_map(header: list[str], custom: dict | None = None) -> dict[str, str]:
    """Ánh xạ trường chuẩn sang tên cột thực tế. Trả về {trường_chuẩn: tên_cột_thực_tế}."""
    mapping = dict(DEFAULT_MAPPING)
    if custom:
        for k, v in custom.items():
            mapping[k] = v if isinstance(v, list) else [v]

    norm_header = {_norm_key(h): h for h in header if h is not None}
    resolved: dict[str, str] = {}
    for field, aliases in mapping.items():
        for alias in aliases:
            key = _norm_key(alias)
            if key in norm_header:
                resolved[field] = norm_header[key]
                break
        else:
            # So khớp mờ: alias là chuỗi con của tên cột
            for alias in aliases:
                key = _norm_key(alias)
                hit = next((orig for nk, orig in norm_header.items() if key and key in nk), None)
                if hit:
                    resolved[field] = hit
                    break
    return resolved


# ---------------------------------------------------------------------------
# Tầng chuyển đổi
# ---------------------------------------------------------------------------
def normalize(rows: list[dict[str, Any]], colmap: dict[str, str]) -> list[dict[str, Any]]:
    """Trích trường theo ánh xạ + làm sạch số + bỏ các dòng không có cả giá lẫn lượng bán."""
    out: list[dict[str, Any]] = []
    dropped = 0

    for r in rows:
        item: dict[str, Any] = {}
        for field, src in colmap.items():
            raw = r.get(src)
            if field in NUMERIC_FIELDS:
                item[field] = (
                    _to_days(raw) if field == "listing_age_days" else _to_number(raw)
                )
            else:
                item[field] = (str(raw).strip() if raw is not None else None) or None

        # Thiếu doanh thu tháng thì tính bù bằng giá × lượng bán tháng
        if item.get("monthly_revenue") is None and item.get("price") and item.get("monthly_sales"):
            item["monthly_revenue"] = round(item["price"] * item["monthly_sales"], 2)

        # Bỏ các dòng hoàn toàn không có tín hiệu giá trị
        if item.get("price") is None and item.get("monthly_sales") is None:
            dropped += 1
            continue
        out.append(item)

    if dropped:
        print(f"[warn] Bỏ {dropped} dòng (thiếu cả giá lẫn lượng bán tháng)", file=sys.stderr)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="Dữ liệu xuất ngành hàng → JSON chuẩn hóa")
    ap.add_argument("input", help="File đầu vào (CSV / TSV / XLSX)")
    ap.add_argument("-o", "--output", help="Đường dẫn JSON đầu ra (mặc định <tên_đầu_vào>.normalized.json)")
    ap.add_argument("--mapping", help="JSON ánh xạ tên cột tùy chỉnh, dạng {\"price\": [\"Cột giá của tôi\"]}")
    ap.add_argument("--profile", action="store_true", help="Chỉ in kết quả nhận diện cột, không chuyển đổi")
    args = ap.parse_args()

    rows = read_rows(args.input)
    if not rows:
        sys.exit("[ERROR] Không đọc được dòng dữ liệu nào. Hãy kiểm tra file không rỗng và dòng đầu tiên là tiêu đề cột.")

    header = list(rows[0].keys())
    custom = json.load(open(args.mapping, encoding="utf-8")) if args.mapping else None
    colmap = build_column_map(header, custom)

    if args.profile:
        print(f"File: {args.input}\nSố dòng dữ liệu: {len(rows)}\n")
        print("Các cột nhận diện được:")
        for h in header:
            print(f"  - {h}")
        print("\nKết quả ánh xạ trường:")
        for field in DEFAULT_MAPPING:
            src = colmap.get(field)
            print(f"  {'✅' if src else '❌'}  {field:20} <- {src if src else '(chưa nhận diện, có thể chỉ định bằng --mapping)'}")
        missing = [f for f in ("title", "price", "monthly_sales") if f not in colmap]
        if missing:
            print(f"\n[Gợi ý] Chưa nhận diện được trường quan trọng: {missing}. Nên chỉ định thủ công bằng --mapping.")
        return

    for required in ("price", "monthly_sales"):
        if required not in colmap:
            sys.exit(
                f"[ERROR] Không nhận diện được trường bắt buộc `{required}`.\n"
                f"        Dùng --profile để xem kết quả nhận diện, hoặc --mapping để chỉ định tên cột."
            )

    items = normalize(rows, colmap)
    out_path = args.output or os.path.splitext(args.input)[0] + ".normalized.json"

    payload = {
        "meta": {
            "source_file": os.path.basename(args.input),
            "row_count_raw": len(rows),
            "row_count_kept": len(items),
            "column_map": colmap,
        },
        "items": items,
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"✅ Đã ghi {out_path}")
    print(f"   Giữ lại {len(items)} / {len(rows)} dòng")
    print(f"   Nhận diện {len(colmap)} trường: {', '.join(sorted(colmap))}")


if __name__ == "__main__":
    main()
