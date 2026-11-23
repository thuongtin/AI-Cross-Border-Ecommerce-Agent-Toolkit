# TASK · Phân loại đánh giá, quy nguyên nhân và xếp hạng điểm bán hàng

> Dùng kèm: `00_system.md` + `templates/input_review_batch.md`
> Tương ứng SOP **1.6 Phân tích đối thủ và phân tích đánh giá**

---

# INPUT

| Trường | Mô tả |
|---|---|
| `platform` / `target_market` / `product_name` | Thông tin cơ bản |
| `spec_table` | **Mục chặn** (cần để phán định đánh giá tiêu cực nhóm thông số không khớp) |
| `package_content[]` | **Mục chặn** (phán định thiếu phụ kiện là thiếu thật hay hiểu lầm) |
| `usage_scope[]` | Phạm vi tình huống sử dụng |
| `warranty` | Thông tin bảo hành |
| `reviews[]` | Mảng đánh giá, gồm `text` / `rating` / `has_image` / `source` |
| `analysis_scope` | `own` (chỉ phía mình) / `competitor` (chỉ đối thủ) / `both` (so sánh) |

---

# STEP 1 · Tổng quan dữ liệu

```markdown
## 1. Tổng quan dữ liệu

| Hạng mục | Giá trị |
|---|---|
| Tổng số đánh giá | |
| Số đánh giá tích cực (4–5 sao) | |
| Số đánh giá trung lập (3 sao) | |
| Số đánh giá tiêu cực (1–2 sao) | |
| Tỷ lệ đánh giá tích cực | |
| Số đánh giá có ảnh / tỷ trọng | |
| Nguồn dữ liệu | <phía mình / đối thủ A / đối thủ B> |
| **Đánh giá cỡ mẫu** | <đủ / hơi nhỏ / chưa đủ (chỉ để tham khảo)> |

**Giới hạn dữ liệu**: <ảnh hưởng do sàn xóa đánh giá / sai lệch hiểu ngôn ngữ / mẫu chưa đủ…>
```

---

# STEP 2 · Phân tích đánh giá tích cực

Phân tích theo 5 khía cạnh của SOP.

```markdown
## 2. Phân tích đánh giá tích cực

### 2.1 Vì sao người mua hài lòng

| # | Lý do hài lòng | Số lần nhắc | Tỷ trọng | Nguyên văn tiêu biểu |
|---|---|---|---|---|
| 1 | | | | `<nguyên văn>` |

### 2.2 Tính năng được nhắc đi nhắc lại

| Tính năng | Số lần nhắc | Sắc thái cảm xúc | Nguyên văn tiêu biểu |
|---|---|---|---|
| | | Tích cực / trung tính | |

### 2.3 Điểm bán hàng nào thực sự hiệu quả

| Điểm bán hàng | Số lần nhắc | Có được làm nổi bật trong Listing hiện tại không | Đề xuất |
|---|---|---|---|
| | | ✅ / ❌ | Nổi bật trên ảnh chính / tăng cường trên trang chi tiết / đưa vào tiêu đề |

> **"Có được làm nổi bật trong Listing hiện tại không" là phán đoán then chốt**:
> Nếu một điểm bán hàng được người mua khen đi khen lại mà Listing không làm nổi bật — **đây là cơ hội tối ưu trực tiếp nhất**, ROI cực cao.

### 2.4 Mức hài lòng về vận chuyển và hậu mãi

| Khía cạnh | Nhắc tích cực | Nhắc tiêu cực | Cảm xúc ròng |
|---|---|---|---|
| Tốc độ giao hàng | | | |
| Độ nguyên vẹn của đóng gói | | | |
| Phản hồi CSKH | | | |

### 2.5 Cảm nhận về giá

| Loại | Số lần nhắc | Nguyên văn tiêu biểu |
|---|---|---|
| Thấy đáng tiền | | |
| Thấy hơi đắt | | |
| So giá với sản phẩm khác | | |
```

---

# STEP 3 · Quy nguyên nhân đánh giá tiêu cực (8 nhóm)

**Đây là cốt lõi của task này.**

```markdown
## 3. Quy nguyên nhân đánh giá tiêu cực

### 3.1 Phân bố nguyên nhân

| # | Nhóm nguyên nhân | Số lượng | Tỷ trọng | Bên chịu trách nhiệm | Sửa được bằng nội dung không |
|---|---|---|---|---|---|
| 1 | **Hiểu lầm** ⭐ | | | Phía mình (trang chi tiết) | ✅ Được |
| 2 | Lỗi chất lượng sản phẩm | | | Nhà cung cấp | ❌ Không |
| 3 | Thông số không như kỳ vọng | | | Phía mình | ✅ Được |
| 4 | Thiếu phụ kiện | | | Phía mình (danh sách đóng gói) | ✅ Được (nếu là hiểu lầm) |
| 5 | Giao hàng chậm | | | Đơn vị vận chuyển | ⚠️ Một phần |
| 6 | Khó sử dụng | | | Phía mình (sách hướng dẫn) | ✅ Được |
| 7 | Hậu mãi kém | | | Phía mình | ✅ Được |
| 8 | Hư hỏng / lỗi / trả hàng | | | Đơn vị vận chuyển / nhà cung cấp | ❌ Không |

**Tổng các mục khắc phục được**: <tổng nhóm 1, 3, 4, 6, 7> đánh giá, chiếm <%> tổng số đánh giá tiêu cực

> Con số tổng này là một trong những đầu ra quan trọng nhất của module:
> **Nó cho biết "bao nhiêu đánh giá tiêu cực có thể giải quyết bằng cách sửa mô tả" mà không cần động vào sản phẩm.**

### 3.2 Chi tiết từng nhóm

#### Nhóm 1 · Hiểu lầm (<n> đánh giá)

| # | Nguyên văn | Người mua tưởng | Thực tế | Vị trí thiếu giải thích |
|---|---|---|---|---|
| 1 | `<nguyên văn>` | | | Trang chi tiết / ảnh danh sách đóng gói / sách hướng dẫn |

#### Nhóm 2 · Lỗi chất lượng sản phẩm (<n> đánh giá)

| # | Nguyên văn | Mô tả vấn đề | Tần suất xuất hiện | Có cần đổi nhà cung cấp không |
|---|---|---|---|---|

#### Nhóm 3 · Thông số không như kỳ vọng (<n> đánh giá)

| # | Nguyên văn | Người mua kỳ vọng | Giá trị thực tế trong `spec_table` | Phán định |
|---|---|---|---|---|
| | | | | Mô tả chưa rõ / mô tả sai / người mua đọc nhầm |

> **Phán định "mô tả chưa rõ / mô tả sai / người mua đọc nhầm" rất quan trọng**:
> - Mô tả sai → phải sửa ngay (rủi ro tuân thủ)
> - Mô tả chưa rõ → đổi cách diễn đạt
> - Người mua đọc nhầm → thêm giải thích ở vị trí đầu

#### Nhóm 4 · Thiếu phụ kiện (<n> đánh giá)

| # | Nguyên văn | Người mua tưởng có kèm | Thực tế trong `package_content` | Phán định |
|---|---|---|---|---|
| | | | | Thiếu thật (sự cố chất lượng) / hiểu lầm (cần ghi rõ) |

> ⚠️ **Bắt buộc đối chiếu `package_content` để phán định.** Nếu sản phẩm vốn không kèm phụ kiện đó mà người mua vẫn phàn nàn "không có" — đây là **hiểu lầm**, cần ghi rõ "không kèm gì" trên ảnh danh sách đóng gói, không phải gửi bù phụ kiện.

#### Nhóm 5–8 (lược, cùng định dạng)
```

---

# STEP 4 · Xếp hạng tần suất điểm bán hàng

Dùng **tần suất nhắc đến × mức độ cảm xúc** để xếp thứ tự ưu tiên điểm bán hàng.

```markdown
## 4. Xếp hạng điểm bán hàng

| Hạng | Điểm bán hàng | Số lần được nhắc | Mức độ cảm xúc | Điểm tổng hợp | Hành động đề xuất |
|---|---|---|---|---|---|
| 1 | | | Mạnh / vừa / yếu | | Cốt lõi ảnh chính / từ khóa tiêu đề / trang chi tiết |
```

### Tiêu chí phán định mức độ cảm xúc

| Mức độ | Từ đặc trưng (ví dụ tiếng Bồ Đào Nha) | Trọng số |
|---|---|---|
| **Mạnh** | `excelente` / `perfeito` / `superou` / `melhor que esperava` / `recomendo` | 3 |
| **Vừa** | `bom` / `funciona bem` / `atende` / `satisfeito` | 2 |
| **Yếu** | `ok` / `razoável` / `normal` | 1 |

**Điểm tổng hợp = số lần được nhắc × trọng số mức độ cảm xúc**

> **Kết quả xếp hạng phải đối chiếu được với Listing**:
> 2 điểm bán hàng đứng đầu phải xuất hiện trên **ảnh chính**; hạng 3–5 phải xuất hiện trong **tiêu đề hoặc đoạn 2 của trang chi tiết**.
> Nếu một điểm bán hàng xếp hạng cao mà không tìm thấy trong Listing — đó chính là điểm cần tối ưu rõ ràng.

---

# STEP 5 · So sánh đối thủ (xuất khi `analysis_scope` có competitor)

```markdown
## 5. So sánh đối thủ

### 5.1 Đối thủ bán được nhờ đâu

| Đối thủ | Điểm tập trung đánh giá tích cực | Điểm tập trung đánh giá tiêu cực | Lợi thế cạnh tranh (moat) |
|---|---|---|---|
| A | | | |
| B | | | |

### 5.2 Phía mình vs đối thủ

| Khía cạnh | Phía mình | Đối thủ A | Đối thủ B | Ưu/nhược điểm của phía mình |
|---|---|---|---|---|
| Điểm hay được khen | | | | |
| Điểm hay bị chê | | | | |
| Tỷ trọng đánh giá có ảnh | | | | |
| Cảm nhận về giá | | | | |

### 5.3 Cơ hội bỏ ngỏ

| Cơ hội | Căn cứ | Hành động cụ thể |
|---|---|---|
| Đối thủ bị chê nhiều nhưng người mua quan tâm | <mục đối thủ hay bị chê> | Trang chi tiết + ảnh chính của mình chủ động nhấn mạnh điểm đó |
| Đối thủ thường không viết nhưng người mua hay hỏi | <mục người mua hay hỏi trong đánh giá> | Giải thích ngay đầu trang chi tiết của mình |
```

> **"Đánh giá tiêu cực của đối thủ = điểm bán hàng của mình"** — đây là ứng dụng trực tiếp phần "cơ hội của phía mình" trong SOP 1.6.
> Nhưng lưu ý: **chỉ dùng làm căn cứ tự cải thiện, không dùng để cạnh tranh không lành mạnh.** Cách làm cụ thể là giải thích rõ trên trang chi tiết của mình những vấn đề đối thủ bị chê, chứ không phải đi báo cáo hay bôi nhọ.

---

# STEP 6 · Bảy mục tiêu phân tích

Bảy câu hỏi SOP yêu cầu trả lời, trả lời lần lượt từng câu:

```markdown
## 6. Trả lời mục tiêu phân tích

| # | Câu hỏi | Kết luận | Căn cứ (cỡ mẫu) |
|---|---|---|---|
| 1 | Đối thủ bán được nhờ đâu | | |
| 2 | Người mua thực sự quan tâm điều gì | | |
| 3 | **Điểm bán hàng nào bắt buộc phải viết** | | |
| 4 | **Thông số nào không được viết bừa** | | |
| 5 | **Vấn đề nào cần giải thích trước trên trang chi tiết** | | |
| 6 | Phía mình nên làm nổi bật khác biệt gì | | |
| 7 | Phía mình cần tránh rủi ro hậu mãi gì | | |
```

---

# FINAL OUTPUT STRUCTURE

```markdown
## 1. Tổng quan dữ liệu
## 2. Phân tích đánh giá tích cực
## 3. Quy nguyên nhân đánh giá tiêu cực
## 4. Xếp hạng điểm bán hàng
## 5. So sánh đối thủ            (xuất có điều kiện)
## 6. Trả lời mục tiêu phân tích
## 7. Quét tuân thủ phân tích
   (theo C1–C5 của 00_system.md; không vi phạm thì bắt buộc ghi "không vi phạm")
## 8. Các trường bàn giao cho module khác
   - selling_points_ranked: []        # → 03 chọn điểm bán hàng cho tiêu đề/ảnh chính
   - forbidden_words_candidates: []   # → 03/04/05 chặn cứng
   - review_patch_suggestions: []     # → 03 viết bổ sung đoạn Lưu ý
   - packaging_clarity_needed: true/false  # → 04 ảnh danh sách đóng gói
   - fixable_ratio: <tỷ trọng đánh giá tiêu cực khắc phục được>
```

---

# SELF-CHECK

- [ ] Mọi đánh giá đã ẩn danh hóa
- [ ] Đánh giá tích cực và tiêu cực được phân tích riêng
- [ ] 8 nhóm nguyên nhân đều có số lượng và tỷ trọng (kể cả nhóm bằng 0)
- [ ] Mỗi lần quy nguyên nhân đều trích dẫn nguyên văn
- [ ] Đã phân biệt nghiêm ngặt loại hiểu lầm và lỗi chất lượng sản phẩm
- [ ] Nhóm thiếu phụ kiện đã đối chiếu `package_content` để phán định
- [ ] Đã tính tổng các mục khắc phục được
- [ ] Xếp hạng điểm bán hàng có tần suất và mức độ cảm xúc, đã đối chiếu với hiện trạng Listing
- [ ] Bảy mục tiêu phân tích đều có câu trả lời
- [ ] Đề xuất quay vòng có nội dung cụ thể bằng ngôn ngữ bản địa
- [ ] Cuối đầu ra đã kèm Quét tuân thủ phân tích + các trường bàn giao
