# Mẫu đầu vào · Nghiên cứu ngành hàng

> **Bước tiên quyết**: chạy hai script trong `scripts/` để tạo `metrics_report` trước, rồi mới điền mẫu này.
> Khi script không chạy được / dữ liệu không vào được, **đừng tự ước tính chỉ số bằng tay** — đó chính là điều module này muốn tránh nhất.

---

## 0. Cấu hình task

```yaml
platform*: shopee
target_market*: Brazil
category*: ""                  # Tên ngành hàng
sample_size: 0                 # Số sản phẩm trong mẫu (đọc từ metrics_report)
data_date: ""                  # Ngày dữ liệu YYYY-MM-DD
```

---

## 1. Báo cáo chỉ số ★ Mục chặn

> Do `market_metrics.py` tạo ra. **Dán thẳng nội dung file `.md` vào đây, hoặc đưa đường dẫn file `.json`.**

```yaml
metrics_report_source: ""      # Đường dẫn file, hoặc ghi "xem nội dung dán bên dưới"
metrics_json_path: ""
```

```text
(Dán toàn bộ nội dung metrics.md vào đây, hoặc ghi đường dẫn JSON)
```

### Tùy chọn: dữ liệu nhiều kỳ (để đánh giá xu hướng)

SOP 1.2 yêu cầu đánh giá "đang trong giai đoạn tăng trưởng/suy giảm". **Dữ liệu chụp nhanh một kỳ không đánh giá được**, cần từ 2 kỳ trở lên:

| Kỳ | Ngày dữ liệu | Tổng lượng bán tháng | Tổng doanh thu tháng | Ghi chú |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

---

## 2. Năng lực nguồn lực công ty ★ Mục chặn (bắt buộc cho bước sàng lọc sơ bộ)

> Thiếu phần này thì không thực hiện được bước sàng lọc sơ bộ — Agent không được phép tự giả định năng lực thay công ty.

```yaml
company_capabilities:
  has_stock_or_incoming: false        # Có hàng sẵn hoặc hàng sắp về không
  has_stable_supplier: false          # Có nhà cung cấp ổn định không
  has_cost_advantage: false           # Giá vốn có lợi thế không
  fits_target_market: false           # Có hợp với thị trường mục tiêu không
  fits_warehouse_logistics: false     # Kích thước, cân nặng có hợp với kho bãi và vận chuyển hiện tại không
  can_handle_after_sales: false       # Có năng lực xử lý hậu mãi/sửa chữa/phụ kiện/đổi trả không
  after_sales_notes: ""               # Ghi chú thêm (ví dụ "chỉ xử lý đổi hàng, không sửa chữa")
```

### Hồ sơ sản phẩm (để xác định rủi ro)

```yaml
product_profile:
  weight_kg: 0
  volume_cm: ""                       # Ví dụ "90 × 25 × 110"
  is_fragile: false                   # Có dễ vỡ không
  needs_certification: []             # Chứng nhận cần có, ví dụ ["ANATEL", "INMETRO"]
  contains_battery: false
  is_liquid_or_magnet: false
  high_virtual_spec_risk: false       # Có dễ bị khai khống thông số không
  ip_risk: ""                         # Mô tả rủi ro sở hữu trí tuệ
```

---

## 3. Cấu trúc chi phí (bắt buộc để đánh giá dải giá "có lãi không")

```yaml
cost_structure:
  unit_cost: 0.00
  shipping: 0.00
  warehouse: 0.00
  commission_rate: 0.14
  return_rate: 0.02
  after_sales_cost_per_unit: 0.00     # Ngành hàng rủi ro cao phải điền (phân bổ chi phí sửa chữa/phụ kiện/phạt điểm)
target_margin_rate: 0.30              # Hàng cồng kềnh 30–35% / hàng nhỏ 25–30%
```

---

## 4. Dữ liệu đối thủ (SOP 1.6 yêu cầu 2–3 đối thủ)

> Tiêu chí lọc: khoảng giá gần / cấu hình gần / người dùng mục tiêu gần / lượng bán khá cao / nhiều đánh giá / gần đây vẫn có lượng bán / **có quan hệ cạnh tranh trực tiếp với sản phẩm bên mình định làm**.

```yaml
competitors:
  - label: "A"                        # ⚠️ Dùng mã hiệu, không điền tên shop thật
    price: 0.00
    monthly_sales: 0
    monthly_revenue: 0.00
    sales_growth_rate: 0.00
    listing_age_days: 0
    rating: 0.0
    review_count: 0
    review_with_image_count: 0
    core_config: ""                   # Cấu hình chính
    title: ""
    main_image_points: []             # Điểm bán hàng thể hiện trên ảnh chính
    detail_page_notes: ""             # Đặc điểm trang chi tiết
    in_ad_slot: false                 # Có xuất hiện ở vị trí quảng cáo không
  - label: "B"
    # ... cùng cấu trúc
```

### Đánh giá của đối thủ (tùy chọn, mức sơ bộ là đủ)

```yaml
competitor_reviews:
  - competitor: "A"
    text: ""                          # Giữ nguyên ngôn ngữ gốc
    rating: 0
```

> **Quy nguyên nhân đánh giá chuyên sâu giao cho [`07 Review Analysis`](../../07_Review_Analysis_Agent/).** Ở đây chỉ cần điền lượng đủ để thấy "đối thủ bán được nhờ đâu".

---

## 5. Chiều cấu hình (để script trích xuất)

```yaml
config_dimensions: []
# Ví dụ: ["công suất", "tải trọng", "dung lượng pin", "có gấp được không"]
# Đã chỉ định bằng --config-fields khi chạy script, ở đây chỉ để ghi lại
```

---

## Tự kiểm tra khi điền

- [ ] `metrics_report` lấy từ script, không phải ước tính bằng tay
- [ ] Đã điền đủ sáu mục của `company_capabilities` (kèm `after_sales_notes`)
- [ ] `product_profile` đã điền kích thước, cân nặng và nhu cầu chứng nhận
- [ ] Ngành hàng rủi ro cao đã điền `after_sales_cost_per_unit`
- [ ] Đối thủ dùng mã hiệu (A/B/C), không điền tên shop thật
- [ ] Đánh giá giữ nguyên ngôn ngữ gốc, không dịch
- [ ] Nếu chỉ có dữ liệu một kỳ, đã sẵn sàng chấp nhận kết luận "không đánh giá được xu hướng"
- [ ] Tôi hiểu: **quyết định chọn sản phẩm cuối cùng do tôi đưa ra**, Agent chỉ xuất phân tích và căn cứ
