# Template đầu vào · Brief chiến lược sản phẩm

> **Điều kiện tiên quyết**:
> 1. Đã chạy xong [01 Market Research](../../01_Market_Research_Agent/) (cung cấp kết luận thị trường)
> 2. Đã có người xác nhận "sản phẩm này đã quyết định làm" (`decision_approved`)

---

## 0. Xác nhận quyết định ★ Mục chặn

```yaml
decision_approved*: false      # ⚠️ bắt buộc do người đổi thành true
approved_by: ""                # người ra quyết định
approved_date: ""              # YYYY-MM-DD
decision_notes: ""             # ghi chú căn cứ quyết định
```

> **Vì sao đây là mục chặn**: module này **không ra quyết định chọn sản phẩm**, chỉ làm "chuẩn hóa thông số cho sản phẩm đã được quyết định".
> Chưa xác nhận mà vẫn chạy tiếp, tức là để Agent ra quyết định kinh doanh thay bạn —— việc này liên quan đến chiến lược công ty, vốn và khẩu vị rủi ro, Agent không làm thay được.

---

## 1. Cấu hình tác vụ

```yaml
platform*: shopee
target_market*: Brazil
category*: ""
```

---

## 2. Trường upstream · bàn giao từ 01 ★ Mục chặn

```yaml
# ── Dán thẳng từ khối «Các trường giao cho 02 Product Strategy» trong đầu ra của 01 ──

target_price_range*: [0, 0]
main_price_zone: [0, 0]
cost_floor_price: 0.00         # giá khả thi theo giá vốn do 01 tính ngược (không có thì điền null)

recommended_config*: {}
mainstream_config: {}
opportunity_config: {}

brand_barrier: ""              # low | medium | high
seller_barrier: ""             # low | medium | high
competitor_weakness*: []
competitor_review_insights: []

benchmark_for_launch:
  days_to_ramp: null
  reviews_needed_before_ramp: null
  sales_needed_before_ramp: null
  ad_dependency: null

pending_confirmations: []
```

---

## 3. Cấu trúc chi phí ★ Mục chặn

> **Cấu hình khác nhau thì giá vốn khác nhau, hãy điền từng SKU.** Dùng một giá vốn cho mọi SKU sẽ tính sai biên lợi nhuận.

```yaml
cost_structure*:
  commission_rate: 0.14        # ⚠️ tra theo ngành hàng thực tế
  return_rate: 0.02            # SOP quy định 2%
  ad_rate: 0.05                # hàng cồng kềnh ~5% / hàng nhỏ 5–10%
  target_margin_rate: 0.32     # hàng cồng kềnh 30–35% / hàng nhỏ 25–30%
  tax_rate: 0.00               # ⚠️ thuế Brazil; điền 0 thì báo cáo sẽ ghi chú "chưa gồm thuế"

sku_costs*:
  - sku_role: "SKU kéo traffic"
    product_cost: 0.00
    shipping: 0.00
    warehouse: 0.00
  - sku_role: "SKU chủ lực"
    product_cost: 0.00
    shipping: 0.00
    warehouse: 0.00
  - sku_role: "SKU cấu hình cao"
    product_cost: 0.00
    shipping: 0.00
    warehouse: 0.00
  - sku_role: "SKU combo"
    product_cost: 0.00          # gồm bộ phụ kiện
    shipping: 0.00
    warehouse: 0.00
```

---

## 4. Năng lực và ràng buộc của công ty

```yaml
company_capabilities:
  can_do_config: true           # có làm được cấu hình thị trường đề xuất không
  config_limitations: ""        # cấu hình không làm được, vd. "nhà cung cấp khung chịu lực chỉ hỗ trợ tối đa 150kg"
  supply_lead_time_days: 0
  moq: 0                        # số lượng đặt hàng tối thiểu

after_sales_capacity*:          # quyết định được ghi cam kết hậu mãi gì
  can_repair: false
  can_replace: true
  has_local_warranty_point: false
  can_provide_parts: true
  warranty_months: 0
  notes: ""
```

> ⚠️ `after_sales_capacity` quyết định trực tiếp đoạn 5 (cam kết hậu mãi) trên trang chi tiết được ghi gì.
> **Ngoài năng lực thì tuyệt đối không ghi** —— ghi vào là tự rước đánh giá tiêu cực.

---

## 5. Ràng buộc vận hành (ảnh hưởng chiến lược giá)

```yaml
cash_flow_constraint: ""        # ràng buộc dòng tiền, vd. "giai đoạn đầu chịu được tối đa 4 tuần biên lợi nhuận thấp"
inventory_level: 0              # tồn kho hiện tại
can_stock_for_promo: true       # có chuẩn bị hàng cho chương trình khuyến mãi được không
# ⚠️ Chương trình Shopee đã đăng ký thì không rút ra được, khi đăng ký phải đối chiếu tồn kho
```

---

## 6. Điểm neo giá đối thủ (tùy chọn)

```yaml
competitor_price_points:
  - label: "A"
    price: 0.00
    config: ""
  - label: "B"
    price: 0.00
    config: ""
```

---

## Tự kiểm tra khi điền

- [ ] `decision_approved` đã được người xác nhận và đổi thành true
- [ ] Các trường bàn giao của 01 đã dán đầy đủ (nhất là `opportunity_config` và `cost_floor_price`)
- [ ] `sku_costs` đã điền **từng SKU**, không dùng chung một giá vốn
- [ ] `commission_rate` tra theo ngành hàng thực tế, không áp mặc định 14%
- [ ] Thuế đã được tính vào (nếu chưa thì chấp nhận ghi chú "chưa gồm thuế" trong báo cáo)
- [ ] `after_sales_capacity` điền đúng thực tế (cái này quyết định cam kết hậu mãi được ghi gì)
- [ ] Tôi hiểu: **quyết định thu mua do tôi làm**, Agent chỉ xuất thông số và căn cứ
