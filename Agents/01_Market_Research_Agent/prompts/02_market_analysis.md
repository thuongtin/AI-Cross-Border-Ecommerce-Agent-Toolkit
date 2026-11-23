# TASK · Phân tích quy mô thị trường, mức độ tập trung, dải giá, tổ hợp cấu hình và đối thủ

> Dùng kèm: `00_system.md` + đầu ra của `01_category_precheck.md` + kết quả của `scripts/market_metrics.py`
> Tương ứng SOP **1.2 – 1.6**

**Điều kiện tiên quyết**: khi `precheck_pass = false` trong `01_category_precheck.md` thì **không được thực hiện task này**.

---

# INPUT

| Trường | Nguồn | Mô tả |
|---|---|---|
| `platform` / `target_market` / `category` | Người dùng | — |
| `metrics_report` | **`scripts/market_metrics.py`** | **Mục chặn** — gồm quy mô thị trường / mức độ tập trung / dải giá / bảng chéo cấu hình |
| `sample_size` / `data_date` | Như trên | Dùng để đánh giá độ tin cậy của dữ liệu |
| `cost_structure` | Người dùng | Căn cứ để đánh giá "công ty có lãi không" khi chọn dải giá |
| `company_capabilities` | Người dùng | Căn cứ để đánh giá "công ty làm được không" khi chọn tổ hợp cấu hình |
| `competitors[]` | Người dùng | 2–3 đối thủ (giá/cấu hình/tệp khách gần giống, lượng bán khá cao, gần đây vẫn ra đơn) |
| `competitor_reviews[]` | Người dùng (tùy chọn) | Nguyên văn đánh giá (review) của đối thủ; quy nguyên nhân chuyên sâu giao cho 07 |

> ⚠️ **Không tự tính lại chỉ số.** Các con số trong metrics_report là kết quả tất định do script tính, nhiệm vụ của bạn là **diễn giải**. Nếu nghi ngờ con số có vấn đề, xuất `[METRIC_SUSPECT]` kèm lý do để người dùng quay lại kiểm tra tham số script, chứ không tự sửa thành "giá trị ước tính".

---

# STEP 1 · Tuyên bố độ tin cậy của dữ liệu

```markdown
## 1. Độ tin cậy của dữ liệu

| Hạng mục | Giá trị | Kết luận |
|---|---|---|
| Cỡ mẫu | <n> | Đủ (≥50) / Hơi nhỏ (30–49) / Không đủ (<30) |
| Ngày dữ liệu | | Có đủ mới không |
| Số sản phẩm không trích được chiều cấu hình | <n> | Ghi chú khi tỷ lệ > 30% |
| Nguồn dữ liệu | | — |

**Kết luận**: <mức độ tin cậy của kết luận lần phân tích này, và những phần nào bị hạn chế do thiếu dữ liệu>
```

---

# STEP 2 · Quy mô thị trường và lượng bán (SOP 1.2)

```markdown
## 2. Quy mô thị trường

### 2.1 Đánh giá quy mô

| Chỉ số | Giá trị | Nhận định |
|---|---|---|
| Tổng lượng bán tháng | | |
| Tổng doanh thu tháng | | |
| Giá trung bình / giá trung vị | | Hai giá trị chênh nhiều → phân bố lệch, cần xem giá trung bình ngầm định |
| Giá trung bình ngầm định (GMV÷lượng bán) | | Phản ánh mức giá chốt đơn thực tế |
| Lượng bán tháng trung bình mỗi sản phẩm | | |

【Nhận định】Quy mô thị trường có đủ để bỏ vốn đầu tư không?

### 2.2 Xu hướng bán hàng (SOP: đánh giá qua lượng bán tháng và doanh thu tháng)

| Câu hỏi | Kết luận | Căn cứ |
|---|---|---|
| Sản phẩm có ra đơn đều đặn không | | |
| Đang trong giai đoạn tăng trưởng / suy giảm | | ⚠️ **Dữ liệu chụp nhanh một kỳ không đánh giá được xu hướng**, cần ≥2 kỳ dữ liệu |
| Có phải chỉ bùng nổ ngắn hạn không | | |
| Có khả năng là sản phẩm theo mùa không | | |

⚠️ **Nếu chỉ có dữ liệu một kỳ**: ghi rõ "dữ liệu chụp nhanh một kỳ không đánh giá được xu hướng, cần so sánh từ 2 kỳ trở lên (nên cách nhau 30 ngày)", không suy đoán tăng hay giảm.

### 2.3 Hiệu quả sản phẩm mới

| Câu hỏi | Kết luận | Căn cứ |
|---|---|---|
| Sản phẩm mới đăng bán có ra đơn không | | |
| Lượng bán tháng của sản phẩm mới có lọt nhóm đầu không | | |
| Sản phẩm mới có tốc độ tăng trưởng không | | |
| Sản phẩm mới có phải dựa vào giá thấp, quảng cáo hay chương trình để lên đơn không | | |

**Logic đánh giá** (nguyên văn SOP):

```
Nếu sản phẩm mới cũng bán được          → link mới còn cơ hội
Nếu lượng bán tập trung ở link cũ       → link mới rất khó lên đơn
Nếu sản phẩm mới chỉ sống nhờ giá cực thấp → thị trường có thể đã rất cạnh tranh
```

⚠️ **SOP ghi chú riêng "phần dữ liệu này của Shaduola không chính xác"**. Nếu thiếu `listing_age_days` hoặc độ chính xác kém, ghi thẳng "dữ liệu phần này không đáng tin, cần kiểm tra thủ công", không cố đưa kết luận.
```

---

# STEP 3 · Mức độ tập trung thương hiệu và người bán (SOP 1.3)

```markdown
## 3. Phân tích mức độ tập trung

### 3.1 Mức độ tập trung thương hiệu

| Chỉ số | Giá trị | Ngưỡng | Kết luận |
|---|---|---|---|
| Số thương hiệu | | — | — |
| CR3 (doanh thu) | | — | — |
| CR10 (doanh thu) | | — | ⚠️ Vô nghĩa khi số chủ thể ≤10 |
| HHI | | — | — |

**Đánh giá theo ngưỡng** (SOP 1.3): mức độ tập trung thương hiệu < 50% → hàng no-brand vẫn còn cơ hội; > 50% → cần thận trọng.

【Nhận định】Có thương hiệu độc chiếm không? Hàng no-brand vào khó đến đâu?

**Tỷ trọng số sản phẩm của thương hiệu top đầu** (nhận định bổ sung then chốt):
- Nếu một thương hiệu lớn chiếm phần lớn lượng bán **và tỷ trọng số sản phẩm cũng cao** → họ đang dùng chiến lược phủ sản phẩm để chiếm chỗ, dư địa của shop mới bị thu hẹp
- Nếu một thương hiệu bán nhiều nhưng **ít sản phẩm** → thắng nhờ hiệu suất mỗi SKU, nghĩa là sức mạnh sản phẩm có thể sao chép được, shop mới vẫn còn cơ hội

### 3.2 Mức độ tập trung người bán

| Chỉ số | Giá trị | Kết luận |
|---|---|---|
| Số người bán | | |
| CR3 / CR10 (doanh thu) | | |
| CR10 (lượng bán) | | |
| HHI | | |

**Danh sách người bán top đầu** (top 10, theo doanh thu)

【Nhận định】Có người bán độc chiếm không? Shop mới vào khó đến đâu?
```

> **Một điểm dễ hiểu sai**: CR là "tỷ trọng doanh thu", nhưng **người bán có thể dựa vào số lượng sản phẩm phủ ra để đẩy CR lên cao**. Đánh giá mức độ độc chiếm phải xem **so sánh giữa CR và Item Share** — script đã đưa đồng thời `revenue_share`, `sales_share`, `item_share` trong bảng Top. Nếu `item_share` của một người bán cao hơn hẳn `revenue_share`, nghĩa là họ **chiếm chỗ bằng số lượng** chứ không phải **lợi thế hiệu suất**.

---

# STEP 4 · Phân tích dải giá (SOP 1.4)

```markdown
## 4. Phân tích dải giá

### 4.1 Đọc đường cong lượng bán

(trích bảng chia bin trong metrics_report)

**Hình dạng đường cong**: <tăng đơn điệu / một đỉnh / hai đỉnh / đuôi dài>

**Khoảng đỉnh**: R$ <n> – R$ <n>, chiếm <n>% tổng lượng bán

### 4.2 Dải giá đề xuất (cắt theo vùng trũng)

(trích suggested_bands trong metrics_report)

| Dải giá | Khoảng giá | Số sản phẩm | Tổng lượng bán | Lượng bán TB/sản phẩm | Mức cạnh tranh | Nhận định |
|---|---|---|---|---|---|---|
| #1 | | | | | Nhiều/ít sản phẩm | |
| #2 | | | | | | |
| #3 | | | | | | |

**Tham khảo mức cạnh tranh**: lượng bán TB/sản phẩm cao và ít sản phẩm → cạnh tranh không gắt; nhiều sản phẩm và lượng bán TB/sản phẩm thấp → biển đỏ (red ocean)

### 4.3 ⭐ Đánh giá chéo bốn điều kiện cho dải giá mục tiêu

SOP yêu cầu rõ dải giá được chọn cuối cùng phải **đồng thời** thỏa bốn điều kiện:

| Điều kiện | Nhận định | Căn cứ |
|---|---|---|
| ① Lượng bán cao | | Tỷ trọng tổng lượng bán của dải đó |
| ② Lượng bán trung bình cao | | Lượng bán TB/sản phẩm của dải đó vs mức TB chung |
| ③ Sản phẩm của công ty có lãi | | Tính ngược từ `cost_structure`: ở mức giá này biên lợi nhuận gộp có đạt mục tiêu ngành hàng không |
| ④ Đối thủ không quá mạnh | | Số sản phẩm của dải đó và tỷ trọng của người bán top đầu |

【Nhận định】**Khoảng giá mục tiêu khuyến nghị**: R$ <n> – R$ <n>
【Lý do】<đối chiếu từng điều kiện trong bốn điều kiện trên>

⚠️ **Nếu không đánh giá được ③ hoặc ④** (thiếu cấu trúc chi phí hoặc dữ liệu đối thủ) → ghi `【Cần xác nhận】`, không lướt qua bằng câu "chắc không vấn đề gì".

### 4.4 Gợi ý định giá ban đầu

| Hạng mục | Gợi ý |
|---|---|
| Giá bán thường ngày | |
| Giá chương trình | |
| Giá sau voucher | |
| Biên lợi nhuận mục tiêu | |
| Có cần SKU giá thấp để kéo traffic không | |
```

> **Lỗi thường gặp**: chỉ nhìn "dải giá bán nhiều nhất" là chọn luôn. SOP yêu cầu rõ phải thỏa đồng thời bốn điều kiện — dải bán nhiều nhất thường cũng là dải cạnh tranh gắt nhất.

---

# STEP 5 · Phân tích tổ hợp cấu hình (SOP 1.5)

```markdown
## 5. Tổ hợp cấu hình

(trích config_matrix trong metrics_report theo từng chiều)

### Chiều: <X>

| Giá trị cấu hình | Số sản phẩm | Tỷ trọng số lượng | Tổng lượng bán | Tỷ trọng lượng bán | Lượng bán TB | Đánh giá |
|---|---|---|---|---|---|---|

**Cấu hình phổ biến**: <giá trị> — tỷ trọng số lượng <n>%, tỷ trọng lượng bán <n>%
**Cấu hình nhiều cơ hội**: <giá trị> — chỉ <n> sản phẩm nhưng lượng bán TB <n> (mức TB chung <n>)

**Cấu hình cơ hội có bị nhóm top đầu chiếm không?**
<đối chiếu chéo với bảng Top của mức độ tập trung người bán: người bán nắm cấu hình này có tập trung ở nhóm top đầu không>

### 5.1 Tổ hợp cấu hình khuyến nghị

| Chiều | Giá trị khuyến nghị | Căn cứ |
|---|---|---|

**Đối chiếu năm điều kiện** (tiêu chuẩn cuối cùng của SOP):

| Điều kiện | Có thỏa không | Giải thích |
|---|---|---|
| Tổng lượng bán cao | | |
| Lượng bán trung bình cao | | |
| Công ty làm được | | Dựa trên `company_capabilities` |
| Lợi nhuận chấp nhận được | | Dựa trên `cost_structure` |
| Hậu mãi kiểm soát được | | |
```

> **Lưu ý then chốt**: `Ít sản phẩm nhưng lượng bán trung bình cao` chỉ cho thấy "có thể là cấu hình cơ hội", **bắt buộc kiểm tra thêm có bị một số ít người bán top đầu chiếm không** (nguyên văn SOP). Nếu cấu hình nhiều cơ hội này lại đúng là địa bàn của người bán top đầu thì đó không phải cơ hội mà là cái bẫy.

---

# STEP 6 · Đối thủ và đánh giá (SOP 1.6)

```markdown
## 6. Phân tích đối thủ

### 6.1 Chọn đối thủ

Tiêu chí lọc của SOP: khoảng giá gần / cấu hình gần / người dùng mục tiêu gần / lượng bán khá cao / nhiều đánh giá / gần đây vẫn có lượng bán / có **quan hệ cạnh tranh trực tiếp** với sản phẩm bên mình định làm.

| Đối thủ | Giá | Lượng bán tháng | Doanh thu tháng | Tốc độ tăng lượng bán | Thời gian đăng bán | Cấu hình chính | Điểm/số đánh giá |
|---|---|---|---|---|---|---|---|
| A | | | | | | | |
| B | | | | | | | |
| C | | | | | | | |

### 6.2 Điểm bán hàng (selling point) cốt lõi của đối thủ

| Đối thủ | Cấu trúc tiêu đề | Điểm bán hàng trên ảnh chính | Đặc điểm trang chi tiết | Điểm bán hàng cốt lõi |
|---|---|---|---|---|

### 6.3 Đánh giá tích cực và đánh giá tiêu cực (mức sơ bộ)

| Đối thủ | Điểm khen tập trung | Điểm chê tập trung | Loại đánh giá tiêu cực hay gặp |
|---|---|---|---|
| | | | Loại hiểu lầm / sai thông số / thiếu phụ kiện / chất lượng / vận chuyển / khó sử dụng |

> **Quy nguyên nhân đánh giá chuyên sâu giao cho [`07 Review Analysis Agent`](../../07_Review_Analysis_Agent/).** Bước này chỉ đánh giá sơ bộ "đối thủ bán được nhờ đâu".

### 6.4 Điểm cơ hội và điểm rủi ro của bên mình

| Loại | Nội dung | Căn cứ |
|---|---|---|
| Điểm cơ hội | | Điểm đối thủ bị chê nhiều mà người mua quan tâm / điểm đối thủ thường không ghi mà người mua hay hỏi |
| Điểm rủi ro | | Điểm đối thủ hay bị chê và bên mình cũng có thể gặp |

### 6.5 Nhịp độ đẩy sản phẩm của đối thủ

| Hạng mục | Đối thủ A | Đối thủ B | Kết luận suy ngược |
|---|---|---|---|
| Thời gian đăng bán | | | Link mới mất khoảng bao lâu để lên đơn |
| Lượng bán tháng / lượng bán 30 ngày gần nhất | | | Cần bao nhiêu lượng bán làm nền trước khi lên đơn |
| Số đánh giá / số đánh giá có ảnh | | | **Cần bao nhiêu đánh giá nền trước khi lên đơn** |
| Có nằm ở vị trí quảng cáo không | | | Có dựa vào quảng cáo để scale không |
```

> **Đầu ra của 6.5 sẽ được đưa thẳng vào kế hoạch đẩy sản phẩm của [`06 Advertising`](../../06_Advertising_Optimization_Agent/).** Đặc biệt là "cần bao nhiêu đánh giá nền trước khi lên đơn" — SOP nói rõ giai đoạn đầu của link mới nhất định phải liên hệ khách để xin đánh giá kèm ảnh thực tế, con số này quyết định cần xây bao nhiêu đánh giá.

---

# FINAL OUTPUT STRUCTURE

```markdown
## 1. Độ tin cậy của dữ liệu
## 2. Quy mô thị trường
## 3. Phân tích mức độ tập trung
## 4. Phân tích dải giá
## 5. Tổ hợp cấu hình
## 6. Phân tích đối thủ
## 7. Quét tuân thủ phân tích
   (theo M1–M5 trong 00_system.md; không vi phạm thì bắt buộc ghi "không vi phạm")
## 8. Các trường bàn giao cho 02 Product Strategy
   - target_price_range: [min, max]
   - price_band_analysis: {}
   - recommended_config: {}
   - mainstream_config: {}
   - opportunity_config: {}
   - brand_barrier: low/medium/high
   - seller_barrier: low/medium/high
   - competitor_weakness: []
   - competitor_review_insights: []
   - benchmark_for_launch: {          # → dùng cho kế hoạch đẩy sản phẩm của 06
       days_to_ramp: null,
       reviews_needed_before_ramp: null,
       sales_needed_before_ramp: null,
       ad_dependency: true/false
     }
   - pending_confirmations: []
```

---

# SELF-CHECK

- [ ] Mọi con số lấy từ `metrics_report`, không bịa
- [ ] Khi chỉ có dữ liệu một kỳ đã nói rõ "không đánh giá được xu hướng", không suy đoán tăng/giảm
- [ ] "Hiệu quả sản phẩm mới" đã ghi chú khi dữ liệu không đáng tin, không cố đưa kết luận
- [ ] Đánh giá mức độ tập trung thương hiệu đã xem cả CR và **tỷ trọng số sản phẩm** (phân biệt chiếm chỗ vs hiệu suất)
- [ ] Đánh giá mức độ tập trung người bán đã xem cả `revenue_share` và `item_share`
- [ ] Khi số chủ thể ≤10 không dùng CR10 làm căn cứ
- [ ] Dải giá mục tiêu đã qua **đánh giá chéo bốn điều kiện** (lượng bán/lượng bán TB/lợi nhuận/mức mạnh của đối thủ)
- [ ] Cấu hình cơ hội đã được đối chiếu chéo xem có bị nhóm top đầu chiếm không
- [ ] Ba điều kiện "công ty làm được / lợi nhuận chấp nhận được / hậu mãi kiểm soát được" của cấu hình khuyến nghị đã được đánh giá dựa trên đầu vào nghiệp vụ
- [ ] Đã chọn 2–3 đối thủ thỏa tiêu chí lọc của SOP
- [ ] Đã xuất các trường suy ngược nhịp độ đẩy sản phẩm
- [ ] Cuối đầu ra đã kèm quét tuân thủ phân tích + các trường bàn giao
