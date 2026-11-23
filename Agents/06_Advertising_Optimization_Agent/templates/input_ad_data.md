# Template đầu vào · Dữ liệu quảng cáo và cấu trúc chi phí

> **Chất lượng dữ liệu quyết định chất lượng chẩn đoán.** Dữ liệu có lượt hiển thị dưới 1,000 hoặc chu kỳ dưới 3 ngày sẽ bị Agent từ chối phân tích thẳng — không phải làm khó, mà vì khi thiếu mẫu, dao động của chỉ số sẽ lớn hơn tín hiệu.

---

## 0. Cấu hình nhiệm vụ

```yaml
platform*: shopee              # shopee | mercadolivre
ad_type*: keyword              # keyword | product | shop (Shopee) / Mercado Ads
test_window_days*: 7           # số ngày dữ liệu bao phủ
target_market: Brazil
target_market_timezone: "UTC-3"

# Tùy chọn nhưng nên điền
current_title: ""
current_main_image_desc: ""
```

---

## 1. Định giá và cấu trúc chi phí ★ Hạng mục chặn

> **Thiếu phần này, Agent từ chối xuất mọi kết luận ROI** — vì không tính được ngưỡng hòa vốn thì mọi phán đoán "ROI tốt hay không" đều là nói suông.

```yaml
price*: 0.00                   # giá bán

cost_structure*:
  unit_cost: 0.00              # giá vốn (gồm phần phân bổ vận chuyển chặng đầu)
  shipping: 0.00               # vận chuyển chặng cuối (giá trị đo thực tế)
  warehouse: 0.00              # phí kho / phí xử lý
  commission_rate: 0.14        # tỷ lệ hoa hồng sàn (⚠️ tra theo ngành hàng thực tế)
  return_rate: 0.02            # tỷ lệ hao hụt hoàn hàng (SOP quy định 2%)
  # Lưu ý cho Shopee Brazil: thuế phí chưa gồm ở đây, nếu có thuế suất riêng hãy thêm trường khác

target_margin_rate: 0.28       # biên lợi nhuận gộp mục tiêu (hàng lớn 30–35% / hàng nhỏ 25–30%)
ad_cost_rate_assumed: 0.075    # tỷ lệ chi phí quảng cáo dự trù khi định giá (hàng nhỏ 5–10%)
```

---

## 2. Dữ liệu nhóm quảng cáo

> **Mỗi nhóm quảng cáo một dòng.** Cách tính chỉ số phải khớp với trang quản trị của sàn — đặc biệt là cách tính "thêm vào giỏ".

```yaml
ad_groups:
  - keyword_or_target*: ""     # từ khóa / sản phẩm / tên shop
    match_type*: ""            # amplo(khớp rộng) | exato(khớp chính xác) | concorrente(từ khóa đối thủ) | cenario(từ khóa ngữ cảnh) | produto(sản phẩm)
    impressions*: 0
    clicks*: 0
    add_to_cart*: 0
    orders*: 0
    spend*: 0.00
    # Các trường sau do Agent tính, không cần điền (điền rồi cũng sẽ bị tính lại)
    # ctr / atc_rate / cvr / cpc / cpa / roas

  - keyword_or_target*: ""
    match_type*: ""
    impressions*: 0
    clicks*: 0
    add_to_cart*: 0
    orders*: 0
    spend*: 0.00
```

### Lưu ý khi điền dữ liệu

| Hạng mục | Lưu ý |
|---|---|
| `impressions` | Dùng **lượt hiển thị trên trang quản trị của sàn**, đừng dùng "lượt hiển thị ước tính" |
| `add_to_cart` | ⚠️ **Xác nhận cách tính thêm vào giỏ của sàn** — là "số sản phẩm được thêm vào giỏ" hay "số người thêm vào giỏ"? Mỗi sàn mỗi khác |
| `orders` | Dùng **đơn được quy cho quảng cáo**, không phải tổng đơn |
| `spend` | Dùng **số tiền bị trừ thực tế**, không phải ngân sách |
| Nhóm quảng cáo bất thường | Nếu một nhóm có lượt hiển thị cực thấp (không tiêu được tiền), vẫn **điền bình thường** — Agent sẽ nhận diện và đi quy trình gỡ bug |

---

## 3. Hiện trạng ngân sách

```yaml
daily_budget_current: 0.00     # ngân sách ngày hiện tại
budget_mode: "manual"          # manual | auto (ML 7 ngày đầu nên dùng manual)
roi_setting_current: 0.00      # cài đặt ROI hiện tại (nếu có)
bid_strategy: ""               # mô tả chiến lược giá thầu
```

---

## 4. Dữ liệu quảng bá của đối thủ (tùy chọn, dùng để suy ngược mục tiêu theo giai đoạn)

> Nguồn: SOP 1.10. Điền phần này, Agent sẽ suy ngược "link mới bao lâu thì lên đơn, trước khi lên đơn cần bao nhiêu đánh giá".

```yaml
competitor_benchmark:
  - name: ""                   # ký hiệu đối thủ (đừng điền tên shop thật, dùng A/B/C)
    listing_age_days: 0        # số ngày đã đăng bán
    monthly_sales: 0
    last_30d_sales: 0
    review_count: 0
    review_with_image_count: 0
    has_ad_slot: false         # có xuất hiện ở vị trí quảng cáo không
```

---

## 5. Khai báo nhiễu bên ngoài (tùy chọn nhưng nên điền)

> Mục đích: khi kiểm tra lại, phân biệt thay đổi chỉ số là **do hành động mang lại** hay **do yếu tố bên ngoài**.

```yaml
external_events:
  - date: ""
    event: ""                  # vd: "tham gia đợt sale lớn của sàn" / "đối thủ giảm giá 15%" / "hết hàng 2 ngày"
```

---

## Tự kiểm tra khi điền

- [ ] Cấu trúc chi phí đầy đủ (thiếu thì không tính được ngưỡng hòa vốn)
- [ ] `commission_rate` được tra theo **ngành hàng thực tế**, không áp cứng 14%
- [ ] Mỗi nhóm quảng cáo đã điền đủ hiển thị/click/thêm giỏ/đơn/chi phí
- [ ] Đã xác nhận cách tính "thêm vào giỏ" của sàn
- [ ] Chu kỳ test ≥ 3 ngày, tổng lượt hiển thị ≥ 1,000
- [ ] Các nhóm quảng cáo có lượt hiển thị thấp bất thường cũng đã điền (đừng xóa bỏ)
- [ ] Ký hiệu đối thủ đã ẩn danh (dùng A/B/C, không dùng tên shop thật)
- [ ] Đã khai báo các sự kiện nhiễu bên ngoài
