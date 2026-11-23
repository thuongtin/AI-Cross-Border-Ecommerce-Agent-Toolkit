---
name: sop-ecom-pricing
description: >-
  Skill tính toán định giá SKU cho Shopee Brazil / Mercado Livre. Từ giá vốn về kho (landed cost) →
  biên lợi nhuận ròng / giá hòa vốn / tính ngược giá mục tiêu / bậc giá / dư địa voucher (có tính
  các khoản thuế Brazil). Dùng khi người dùng cần tính lợi nhuận gộp, định giá, giá hòa vốn, nên
  phát voucher bao nhiêu, cấu trúc SKU có hợp lý không. Các cụm «tính lãi / định giá / giá hòa vốn /
  phát voucher» cũng kích hoạt Skill này.
  NOT for khảo sát giá đối thủ, phân tích dải giá thị trường (đó là việc của 01).
allowed-tools:
  - Bash(python *)
  - Read
metadata:
  version: 0.4.0
  category: e-commerce/pricing
  license: MIT
---

# 02 · Product Strategy Skill (tầng tính toán định giá)

> **Định vị**: biến «giá vốn về kho + các mức phí + biên lợi nhuận mục tiêu» thành **những con số kiểm chứng được**.
> **Quyết định** định giá do người làm; Skill này chỉ đảm bảo tính đúng.

---

## Bắt đầu nhanh

```bash
# Preset theo sàn (khuyên dùng): mức phí lấy từ scripts/platform_fees.json, có hoa hồng/phí cố định chia bậc theo giá
# Các sàn có sẵn: shopee_br / mercadolivre_br / mercadolivre_br_premium / amazon_br / tiktok_br
python scripts/sku_pricing.py calc --platform shopee_br --cost 935 --price 2199
python scripts/sku_pricing.py --list-platforms          # xem toàn bộ preset và nguồn mức phí

# Ma trận nhiều SKU + bậc giá + dư địa voucher (đọc CSV)
python scripts/sku_pricing.py matrix --file examples/sample-skus.csv --platform mercadolivre_br

# Nhập tay (tương thích cách dùng cũ, tham số truyền rõ luôn được ưu tiên hơn preset)
python scripts/sku_pricing.py calc --cost 935 --price 2199 \
    --commission 14 --return 2 --ad 5 --tax 0 --target-margin 32

# Ma trận nhiều SKU: bảng biên lợi nhuận ròng + bậc giá + dư địa voucher + cảnh báo cấu trúc
python scripts/sku_pricing.py matrix --file examples/sample-skus.csv \
    --commission 14 --return 2 --ad 5 --tax 0 --target-margin 32
```

---

## Đọc kết quả (năm chỉ số)

| Đầu ra | Dùng thế nào |
|---|---|
| `net_rate` biên lợi nhuận ròng | So với `target_margin`: thấp hơn = trượt mục tiêu (SKU kéo traffic có thể cố ý thấp hơn, nhưng phải trên giá hòa vốn) |
| `break_even_price` giá hòa vốn | **Giá sàn tuyệt đối** —— giá sau khuyến mãi/voucher mà thủng mức này là lỗ thật |
| `target_price` giá mục tiêu | Giá tham chiếu tính ngược từ biên lợi nhuận mục tiêu (kiểu giá vốn ÷ 0.47) |
| `coupon_headroom` dư địa voucher | Phần biên lợi nhuận ròng vượt mục tiêu × giá bán = **hạn mức voucher phát ra mà không thủng mục tiêu** |
| `price_ladder` bậc giá | Chênh giá giữa các SKU liền kề: chênh quá ít thì tự ăn thịt lẫn nhau, chênh quá nhiều thì chừa khoảng trống cho đối thủ |

---

## Quy tắc và cách tính

- Công thức, cách tính thuế (thuế suất hiệu dụng tổng hợp), giải thích tham số → [references/pricing-rules.md](references/pricing-rules.md)
- Dữ liệu case study (xe scooter điện, bốn SKU) → [examples/sample-skus.csv](examples/sample-skus.csv)

## Ba lưu ý

1. **SKU kéo traffic có biên lợi nhuận ròng thấp hơn mục tiêu là chiến lược chứ không phải sự cố** —— nhưng script sẽ nhắc bạn xác nhận, và giá của nó bắt buộc phải cao hơn giá hòa vốn
2. **SKU cấu hình cao thường có biên lợi nhuận ròng thấp hơn SKU chủ lực** (giá vốn tăng nhanh hơn giá bán) —— script sẽ nhắc kiểm tra
3. **Đừng quên thuế** —— chỉ cần `--tax 8` là giá hòa vốn đã bị đẩy lên gần 30%; hãy quy đổi theo chế độ thuế Brazil của bạn rồi điền vào
