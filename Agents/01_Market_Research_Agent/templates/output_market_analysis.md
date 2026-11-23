# Mẫu đầu ra · Báo cáo phân tích thị trường

> Cấu trúc đầu ra chuẩn của 01 Market Research Agent.
> **Bên sử dụng phía sau**: [02 Product Strategy](../../02_Product_Strategy_Agent/) (nhu cầu chính), [06 Advertising](../../06_Advertising_Optimization_Agent/) (suy ngược nhịp độ đẩy sản phẩm).

---

```markdown
# Market Analysis · <category> · <platform> / <market>

Thời gian tạo: <YYYY-MM-DD>
Phiên bản Prompt: 01-Market-Research v0.3
Nguồn dữ liệu: <file / sàn>
Cỡ mẫu: <n>
Ngày dữ liệu: <YYYY-MM-DD>

---

## 0. Kết luận sàng lọc sơ bộ (từ 01_category_precheck)

| # | Hạng mục kết luận | Nội dung |
|---|---|---|
| 1 | Có hợp với nguồn hàng hiện tại của công ty không | |
| 2 | Có lợi thế chuỗi cung ứng không | |
| 3 | Có vấn đề về vận chuyển hoặc kho bãi không | |
| 4 | Mức độ rủi ro | 🟢 / 🟡 / 🔴 |
| 5 | Khả năng gánh rủi ro bằng lợi nhuận của ngành hàng rủi ro cao | |
| 6 | Hạn chế của sàn | |
| 7 | **Có sang bước phân tích quy mô thị trường không** | |

(Khi `precheck_pass = false`, báo cáo kết thúc tại đây)

---

## 1. Độ tin cậy của dữ liệu

| Hạng mục | Giá trị | Kết luận |
|---|---|---|
| Cỡ mẫu | | |
| Ngày dữ liệu | | |
| Số sản phẩm không trích được chiều cấu hình | | |
| Số kỳ dữ liệu | | Một kỳ → không đánh giá được xu hướng |

**Kết luận**:

---

## 2. Quy mô thị trường

### 2.1 Quy mô

| Chỉ số | Giá trị | Nhận định |
|---|---|---|
| Tổng lượng bán tháng | | |
| Tổng doanh thu tháng | | |
| Giá trung bình / giá trung vị | | |
| Giá trung bình ngầm định | | |
| Lượng bán tháng trung bình mỗi sản phẩm | | |

【Nhận định】

### 2.2 Xu hướng bán hàng

| Câu hỏi | Kết luận | Căn cứ |
|---|---|---|
| Có ra đơn đều đặn không | | |
| Tăng trưởng / suy giảm | | |
| Có phải bùng nổ ngắn hạn không | | |
| Có theo mùa không | | |

### 2.3 Hiệu quả sản phẩm mới

| Câu hỏi | Kết luận | Căn cứ |
|---|---|---|

**Ghi chú độ tin cậy của dữ liệu**:

---

## 3. Phân tích mức độ tập trung

### 3.1 Mức độ tập trung thương hiệu

| Chỉ số | Giá trị | Ngưỡng | Kết luận |
|---|---|---|---|
| Số thương hiệu | | — | |
| CR3 | | — | |
| CR10 | | — | |
| HHI | | — | |

**Tỷ trọng số sản phẩm của thương hiệu top đầu** (phân biệt chiếm chỗ vs hiệu suất):

| Thương hiệu | Tỷ trọng doanh thu | Tỷ trọng lượng bán | Tỷ trọng số sản phẩm | Phân loại |
|---|---|---|---|---|

【Nhận định】

### 3.2 Mức độ tập trung người bán

| Chỉ số | Giá trị |
|---|---|
| Số người bán | |
| CR3 / CR10 | |
| HHI | |

| # | Người bán | Tỷ trọng doanh thu | Tỷ trọng lượng bán | Tỷ trọng số sản phẩm | Loại |
|---|---|---|---|---|---|

【Nhận định】

---

## 4. Phân tích dải giá

### 4.1 Đọc đường cong lượng bán

- Hình dạng đường cong:
- Khoảng đỉnh:
- Tỷ trọng trong tổng lượng bán:

### 4.2 Dải giá đề xuất

| Dải giá | Khoảng giá | Số sản phẩm | Tổng lượng bán | Lượng bán TB/sản phẩm | Mức cạnh tranh |
|---|---|---|---|---|---|
| #1 | | | | | |
| #2 | | | | | |
| #3 | | | | | |

### 4.3 Đánh giá chéo bốn điều kiện cho dải giá mục tiêu

| Điều kiện | Nhận định | Căn cứ |
|---|---|---|
| ① Lượng bán cao | | |
| ② Lượng bán trung bình cao | | |
| ③ Sản phẩm của công ty có lãi | | |
| ④ Đối thủ không quá mạnh | | |

**Khoảng giá mục tiêu khuyến nghị**: R$ <n> – R$ <n>
**Lý do**:
**Cần xác nhận**:

### 4.4 Gợi ý định giá ban đầu

| Hạng mục | Gợi ý |
|---|---|
| Giá bán thường ngày | |
| Giá chương trình | |
| Giá sau voucher | |
| Biên lợi nhuận mục tiêu | |
| SKU kéo traffic | |

---

## 5. Tổ hợp cấu hình

### Chiều: <X>

| Giá trị cấu hình | Số sản phẩm | Tỷ trọng số lượng | Tổng lượng bán | Tỷ trọng lượng bán | Lượng bán TB | Đánh giá |
|---|---|---|---|---|---|---|

- **Cấu hình phổ biến**:
- **Cấu hình nhiều cơ hội**:
- **Cấu hình cơ hội có bị nhóm top đầu chiếm không**:

### 5.1 Tổ hợp cấu hình khuyến nghị

| Chiều | Giá trị khuyến nghị | Căn cứ |
|---|---|---|

### 5.2 Đối chiếu năm điều kiện

| Điều kiện | Có thỏa không | Giải thích |
|---|---|---|
| Tổng lượng bán cao | | |
| Lượng bán trung bình cao | | |
| Công ty làm được | | |
| Lợi nhuận chấp nhận được | | |
| Hậu mãi kiểm soát được | | |

---

## 6. Phân tích đối thủ

### 6.1 Tổng quan đối thủ

| Đối thủ | Giá | Lượng bán tháng | Doanh thu tháng | Tốc độ tăng | Số ngày đăng bán | Cấu hình chính | Điểm/số đánh giá |
|---|---|---|---|---|---|---|---|

### 6.2 Điểm bán hàng của đối thủ

| Đối thủ | Cấu trúc tiêu đề | Điểm bán hàng trên ảnh chính | Đặc điểm trang chi tiết | Điểm bán hàng cốt lõi |
|---|---|---|---|---|

### 6.3 Đánh giá tích cực và đánh giá tiêu cực (mức sơ bộ)

| Đối thủ | Điểm khen tập trung | Điểm chê tập trung | Loại đánh giá tiêu cực hay gặp |
|---|---|---|---|

### 6.4 Điểm cơ hội và điểm rủi ro

| Loại | Nội dung | Căn cứ |
|---|---|---|
| Điểm cơ hội | | |
| Điểm rủi ro | | |

### 6.5 Suy ngược nhịp độ đẩy sản phẩm

| Hạng mục | Đối thủ A | Đối thủ B | Kết luận suy ngược |
|---|---|---|---|
| Thời gian đăng bán | | | |
| Lượng bán tháng | | | |
| Số đánh giá / số đánh giá có ảnh | | | |
| Vị trí quảng cáo | | | |

---

## 7. Quét tuân thủ phân tích

| Quy tắc | Vi phạm | Xử lý |
|---|---|---|
| M1 Bịa dữ liệu thị trường | | |
| M2 Thổi phồng cơ hội thị trường | | |
| M3 Quyết định thay con người | | |
| M4 Gợi ý lách quy định của sàn | | |
| M5 Phỏng đoán thật giả của dữ liệu đối thủ | | |

(Khi không vi phạm: `Quét tuân thủ phân tích: không vi phạm`)

---

## 8. Các trường bàn giao cho 02 Product Strategy

```yaml
target_price_range: [0.00, 0.00]
price_band_analysis: {}
recommended_config: {}
mainstream_config: {}
opportunity_config: {}
brand_barrier: low          # low | medium | high
seller_barrier: low
competitor_weakness: []
competitor_review_insights: []
benchmark_for_launch:
  days_to_ramp: null
  reviews_needed_before_ramp: null
  sales_needed_before_ramp: null
  ad_dependency: false
pending_confirmations: []
```

---

## 9. Nhắc việc khi thực thi

- [ ] Các mục cần xác nhận đã được con người bổ sung đủ
- [ ] Khi chỉ có dữ liệu một kỳ đã chấp nhận "không đánh giá được xu hướng"
- [ ] Dữ liệu đối thủ đã được kiểm tra thủ công ngẫu nhiên (mẫu có thể sai)
- [ ] Quyết định chọn sản phẩm cuối cùng do con người đưa ra, báo cáo này chỉ cung cấp căn cứ
```

---

## Các bước sau sử dụng thế nào

| Trường | Bên sử dụng | Mục đích |
|---|---|---|
| `target_price_range` | 02 | Đầu vào của mô hình định giá |
| `recommended_config` | 02 | Quyết định cấu hình sản phẩm |
| `opportunity_config` | 02 | Hướng khác biệt hóa |
| `brand_barrier` / `seller_barrier` | 02 | Quyết định có cần định vị khác biệt không |
| `competitor_weakness` | 02 / 03 | Diễn đạt điểm bán hàng khác biệt |
| `benchmark_for_launch` | **06** | Suy ngược mục tiêu lượng bán và đánh giá khi ra mắt sản phẩm mới |
| `pending_confirmations` | Con người | Các mục bắt buộc bổ sung trước khi quyết định |

> **Lưu ý**: kết luận của báo cáo này là "**dữ liệu ủng hộ / không ủng hộ**", không phải "khuyến nghị làm".
> Quyết định cuối cùng liên quan đến nguồn lực công ty, chuỗi cung ứng và khẩu vị rủi ro, bắt buộc do con người đưa ra.
