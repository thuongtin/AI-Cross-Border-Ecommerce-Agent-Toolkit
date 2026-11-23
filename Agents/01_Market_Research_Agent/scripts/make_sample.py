#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_sample.py — Tạo một bảng xuất ngành hàng mẫu có chứa "dữ liệu bẩn"

Mục đích: giúp người dùng vừa lấy repo về là chạy trọn vẹn được ngay hai script trong scripts/ để kiểm tra môi trường.
Dữ liệu là **dữ liệu tổng hợp (synthetic)**, dùng để minh họa định dạng và khả năng làm sạch, không đại diện cho thị trường thật nào.

Cách dùng: python make_sample.py [-o ../samples/sample_patinete_eletrico.csv]
"""

import argparse
import csv
import random
from pathlib import Path

random.seed(20261013)

# Thương hiệu: 2 thương hiệu top đầu + một loạt hàng no-brand (mô phỏng thị trường "no-brand vẫn còn cơ hội")
BRANDS = (
    ["MarcaA"] * 6 + ["MarcaB"] * 4 + ["MarcaC"] * 3
    + ["Generic"] * 12 + ["Sem marca"] * 15 + ["Outras"] * 10
)

# Người bán: CR10 hình thành tự nhiên từ dữ liệu (3 shop lớn + một loạt shop nhỏ)
SELLERS = (
    ["LojaGrande1"] * 8 + ["LojaGrande2"] * 6 + ["LojaGrande3"] * 5
    + [f"LojaPequena{i:02d}" for i in range(1, 32)]
)

POWERS = ["350W", "500W", "500W", "500W", "800W"]      # 500W là phổ biến nhất
LOADS = ["100kg", "120kg", "150kg", "150kg", "150kg"]  # 150kg là phổ biến nhất
FOLDABLE = ["Dobrável", "Dobrável", "Dobrável", "Não dobrável"]

# Thiết kế dải giá: 1500–3200, lượng bán tập trung ở 1800–2400 (chừa cấu trúc dễ nhận ra cho việc dò vùng trũng)
PRICE_ANCHORS = [
    (1550, 40), (1700, 90), (1850, 160), (2000, 210), (2150, 230),
    (2300, 190), (2450, 120), (2600, 70), (2800, 40), (3050, 20),
]


def price_for(i: int) -> float:
    lo, _ = PRICE_ANCHORS[i % len(PRICE_ANCHORS)]
    return round(lo + random.uniform(-90, 90), 2)


def sales_for(price: float) -> int:
    # Tìm điểm neo gần nhất, lấy lượng bán của nó + nhiễu
    best = min(PRICE_ANCHORS, key=lambda a: abs(a[0] - price))
    base = best[1]
    return max(0, int(random.gauss(base, base * 0.45)))


def config_for(price: float) -> tuple[str, str, str]:
    """
    Gán cấu hình theo mức giá — điểm này rất quan trọng.

    Nếu cấu hình và lượng bán ngẫu nhiên độc lập, "cấu hình cơ hội" tính ra từ bảng chéo cấu hình chỉ là nhiễu.
    Ở thị trường thật, cấu hình tương quan mạnh với giá (công suất cao → đắt), nên dữ liệu mẫu cũng phải dựng như vậy,
    nếu không sẽ không minh họa được công dụng thật của bảng chéo.
    """
    if price < 1900:
        return "350W", "100kg", "10Ah"
    if price < 2400:
        return "500W", "150kg", "12Ah"
    return "800W", "150kg", "12Ah"


def dirty(v) -> str:
    """Làm "bẩn" định dạng số một cách ngẫu nhiên, để kiểm tra khả năng làm sạch của parser."""
    style = random.choice(["plain", "thousands_dot", "thousands_comma", "currency", "currency_comma_dot"])
    if isinstance(v, float):
        if style == "plain":
            return f"{v:.2f}"
        if style == "currency":
            return f"R$ {v:,.2f}"
        if style == "currency_comma_dot":
            return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        return f"{v:.2f}"
    # int
    if style == "thousands_dot":
        return f"{v:,}".replace(",", ".")
    if style == "thousands_comma":
        return f"{v:,}"
    if style == "currency":
        return f"R$ {v:,}".replace(",", ".")
    if style == "plain":
        return str(v)
    return str(v)


def age_dirty(days: int) -> str:
    style = random.choice(["days", "months", "date", "plain"])
    if style == "days":
        return f"{days} ngày"
    if style == "months":
        return f"{max(1, days // 30)} tháng"
    if style == "date":
        return f"2025-{(days % 12) + 1:02d}-15"
    return str(days)


def main() -> None:
    ap = argparse.ArgumentParser(description="Tạo bảng xuất ngành hàng mẫu (dữ liệu tổng hợp, có dữ liệu bẩn)")
    default_out = Path(__file__).resolve().parent.parent / "samples" / "sample_patinete_eletrico.csv"
    ap.add_argument("-o", "--output", default=str(default_out), help="Đường dẫn CSV đầu ra")
    ap.add_argument("-n", "--rows", type=int, default=50, help="Số dòng (mặc định 50)")
    args = ap.parse_args()

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)

    header = [
        "Tên sản phẩm", "Giá", "Lượng bán tháng", "Doanh thu tháng", "Người bán", "Thương hiệu",
        "Điểm đánh giá", "Số đánh giá", "Thời gian đăng bán", "Link sản phẩm",
    ]

    # Cấu hình cơ hội: đặt 4 dòng cấu hình "tải trọng cao" vào dải giá đỉnh (số lượng ít, xem có lợi thế hiệu suất mỗi SKU không)
    opportunity_slots = {3, 13, 23, 33}

    with open(args.output, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        for i in range(args.rows):
            p = price_for(i)
            s = sales_for(p)
            brand = BRANDS[i % len(BRANDS)]
            seller = SELLERS[i % len(SELLERS)]
            power, load, cap = config_for(p)
            fold = FOLDABLE[i % len(FOLDABLE)]

            # Đổi một số ít dòng sang cấu hình khác biệt (tải trọng cao) để minh họa việc đánh giá "cấu hình cơ hội"
            if i in opportunity_slots and 1900 <= p < 2400:
                load = "200kg"

            title = (f"Patinete Elétrico Adulto {power} {load} Bateria {cap} "
                     f"com Banco {fold} para Mobilidade Urbana")
            if brand not in ("Generic", "Sem marca", "Outras"):
                title = f"{brand} {title}"

            rating = round(random.uniform(4.0, 5.0), 1)
            reviews = int(random.gauss(s * 0.6, s * 0.3)) if s else 0
            reviews = max(0, reviews)
            age = random.randint(20, 900)

            w.writerow([
                title,
                dirty(p),
                dirty(s),
                dirty(round(p * s, 2)) if random.random() > 0.25 else "",  # Thiếu 25%, để kiểm tra tính bù
                seller,
                brand,
                f"{rating}",
                dirty(reviews),
                age_dirty(age),
                f"https://example.com/item/{100000 + i}",
            ])

    print(f"✅ Đã tạo dữ liệu mẫu: {args.output} ({args.rows} dòng, có cố ý trộn các định dạng dữ liệu bẩn)")


if __name__ == "__main__":
    main()
