# TASK · Lên kế hoạch nội dung 9 ảnh và text trong ảnh

> Dùng kèm: `00_system.md` + đầu ra của 03 Listing Creative Agent
> Tương ứng SOP **3.3 "Logic tạo 9 ảnh thương mại điện tử"**

---

# INPUT

Trường bắt buộc:

| Trường | Nguồn | Mô tả |
|---|---|---|
| `platform` | Người nhập | Quyết định quy chuẩn ảnh |
| `target_market` | Người nhập | Quyết định ngôn ngữ text trong ảnh |
| `mode` | Người nhập | `standard` / `variant` / `iterate` |
| `product_name` | 03 | Tên chung của sản phẩm |
| `category` | 03 | Dùng để xác định tông hình ảnh |
| `core_selling_point` | **03 (mục chặn)** | Thông tin cốt lõi của ảnh chính |
| `secondary_points[]` | **03 (mục chặn)** | Nội dung ảnh chi tiết |
| `spec_table` | **03 (mục chặn)** | Ảnh thông số / ảnh kích thước |
| `package_content[]` | **03 (mục chặn)** | Ảnh danh sách đóng gói |
| `warranty` | **03 (mục chặn)** | Ảnh bảo hành |
| `usage_scope_confirmed[]` | **03 (mục chặn)** | Ảnh bối cảnh |
| `forbidden_words[]` | **03 (mục chặn)** | Chặn từ cấm trong text ảnh |
| `visual_tone_hint` | 03 | Thống nhất phong cách |
| `certifications` | Người nhập | ⚠️ Chỉ điền chứng nhận **thực sự có**, để trống thì không tạo ảnh chứng nhận |

---

# STEP 1 · Lên kế hoạch nội dung 9 ảnh

Xuất theo 9 vị trí ảnh cố định. Mỗi vị trí ảnh bắt buộc điền các trường sau:

```markdown
## 1. Kế hoạch nội dung 9 ảnh

| # | Vị trí ảnh | Thông tin truyền tải | Loại thông tin | Thành phần khung hình | Text trong ảnh | Số ký tự |
|---|---|---|---|---|---|---|
| 1 | Ảnh chính | <nhìn một cái là biết đây là gì> | Nhận diện | <mô tả bố cục> | <text hoặc "Không có chữ"> | <n ký tự> |
| 2 | Ảnh điểm bán hàng chủ lực | <core_selling_point> | Thuyết phục | | | |
| 3 | Ảnh thông số kỹ thuật | <trực quan hóa spec_table> | Thông tin | | | |
| 4 | Ảnh bối cảnh sử dụng A | <usage_scope[0]> | Nhập vai | | | |
| 5 | Ảnh bối cảnh sử dụng B | <usage_scope[1]> | Nhập vai | | | |
| 6 | Ảnh cận cảnh chi tiết | <mục then chốt trong secondary_points> | Thuyết phục | | | |
| 7 | Ảnh kích thước/so sánh | <thông số kích thước> | Xóa nghi ngờ | | | |
| 8 | Ảnh danh sách đóng gói | <package_content> | Ngăn tranh chấp | | | |
| 9 | Ảnh hậu mãi/bảo hành | <warranty> | Niềm tin | | | |
```

## Yêu cầu bắt buộc cho từng vị trí ảnh

### Ảnh 1 · Ảnh chính

- **ML**: text trong ảnh bắt buộc ghi `Không có chữ` (sàn cấm rõ ràng)
- **Shopee**: được thêm một câu điểm bán hàng, nhưng **không quá 2 dòng, mỗi dòng không quá 20 ký tự**
- Khung hình: nền trắng tinh, sản phẩm một góc chính diện duy nhất, thể hiện trọn vẹn, không có phụ kiện (trừ khi phụ kiện là sản phẩm chính được bán)
- ⚠️ **Ảnh này bắt buộc phải phán đoán khác biệt giữa các sàn**, xem `platform_variant` bên dưới

### Ảnh 2 · Ảnh điểm bán hàng chủ lực

- Chỉ được thể hiện **1** điểm bán hàng (chính là `core_selling_point`)
- Các yếu tố trong khung hình phải **trực tiếp chứng minh** cho câu điểm bán hàng đó. Điểm bán hàng nói 45W thì khung hình phải có ký hiệu công suất hoặc so sánh sạc nhanh

### Ảnh 3 · Ảnh thông số kỹ thuật

- Con số khớp **từng ký tự** với `spec_table`
- Đơn vị hệ mét, số thập phân dùng dấu phẩy (`14,2 cm`)
- Không quá **6** mục thông số, nhiều hơn sẽ khó đọc trên điện thoại, tách sang ảnh thứ 7

### Ảnh 4 / 5 · Ảnh bối cảnh sử dụng

- Bối cảnh phải lấy từ `usage_scope_confirmed`, **thứ tự chính là mức ưu tiên**
- ⚠️ **Vùng hay dính quảng cáo sai sự thật**: cách sử dụng trong khung hình phải là điều sản phẩm thực sự làm được
  (ví dụ: sản phẩm không chống nước thì ảnh bối cảnh không được có cảnh trong mưa, bên hồ bơi, trên thuyền)

### Ảnh 6 · Ảnh cận cảnh chi tiết

- Chọn mục **có sức hút thị giác nhất** trong `secondary_points`
- Ví dụ: màn hình hiển thị số, bố trí cổng kết nối, đường may khóa kéo

### Ảnh 7 · Ảnh kích thước/so sánh

- Bắt buộc có **con số cụ thể + vật tham chiếu** (bàn tay, đồ vật thông dụng, tỷ lệ cơ thể người)
- ⚠️ Đối tượng so sánh phải là hình dạng chung, không được chỉ đích danh ngoại hình của đối thủ

### Ảnh 8 · Ảnh danh sách đóng gói

- **Bày phẳng đầy đủ**, không sót món nào
- **Ghi rõ "không có gì"** —— đây là ảnh hiệu quả nhất để phòng ngừa đánh giá tiêu cực loại hiểu lầm
- Ví dụ: `Não incluso: adaptador de tomada`

### Ảnh 9 · Ảnh hậu mãi/bảo hành

- **Shopee Brazil rất nên có** (yếu tố tạo niềm tin trong bối cảnh luật bảo vệ người tiêu dùng)
- Nội dung: thời hạn bảo hành + phạm vi + kênh CSKH
- **Không được tạo đồ họa nhái biểu tượng chính thức của sàn**

---

# STEP 2 · Xử lý khác biệt giữa các sàn (platform_variant)

**Nếu `platform = mercadolivre` hoặc `amazon`**, xuất hai phương án ảnh chính:

```markdown
## 2. Phương án theo khác biệt sàn

| Phương án | Sàn áp dụng | Đặc điểm ảnh chính | Ghi chú |
|---|---|---|---|
| A | Mercado Livre / Amazon | **Nền trắng tinh + không có chữ nào** | Sàn bắt buộc |
| B | Shopee / TikTok Shop | Nền trắng + chữ điểm bán hàng (≤2 dòng) | Tăng CTR trên sàn |

⚠️ **Cùng một bộ creative ảnh chính không được dùng lại giữa các sàn.**
```

Lý do: trên Shopee, ảnh chính có điểm bán hàng là cách làm phổ biến và hiệu quả, còn Mercado Livre cấm rõ ràng. **Đây là xung đột cứng, không phải khác biệt về sở thích.**

---

# STEP 3 · Viết text trong ảnh

Với mỗi ảnh có chữ, xuất:

```markdown
## 3. Chi tiết text trong ảnh

### Ảnh <n> · <vị trí ảnh>
- Text chính: `<ngôn ngữ bản địa>`
- Text phụ: `<ngôn ngữ bản địa>` (tùy chọn)
- Số ký tự: `<n>` ký tự / giới hạn `<m>`
- Dễ đọc trên mobile: ✅ cỡ chữ text chính ≥ 4% chiều cao ảnh
- Kiểm tra tuân thủ: ✅ không có từ cấm / con số khớp spec_table
```

**Ba quy tắc cứng khi viết text**:

1. **Text trong ảnh không phải slogan quảng cáo.** Viết thông tin, không viết cảm xúc.
   - ❌ `Incrível! O melhor carregador do Brasil!`
   - ✅ `20000 mAh · 45 W · 3 saídas`
2. **Con số phải khớp hoàn toàn với `spec_table`**, kể cả dấu thập phân và dấu phân cách hàng nghìn.
3. **Mỗi câu chỉ nói một việc.** Một ảnh có hai điểm bán hàng thì coi như không có điểm bán hàng nào.

---

# Ba chế độ

| mode | Khác biệt đầu ra |
|---|---|
| `standard` | Phương án 9 ảnh tiêu chuẩn |
| `variant` | Xuất **2 bộ** phương án 9 ảnh khác biệt hóa (hướng điểm bán hàng của ảnh chính khác nhau, bối cảnh khác nhau), dùng cho test nhiều link theo SOP 3.4 / khác biệt hóa nhiều shop theo SOP 2.3 |
| `iterate` | Tương ứng SOP 3.6: nhập mô tả ảnh chính hiện tại + triệu chứng (ví dụ "CTR 1.2% thấp hơn mức chuẩn 3%"), **chỉ sửa ảnh chính**, các ảnh khác giữ nguyên |

Khi `mode = iterate` thì xuất:

```markdown
## 2. Phương án cải tiến ảnh chính
- Mô tả ảnh chính hiện tại: <...>
- Triệu chứng: <...>
- Chẩn đoán: <vì sao CTR thấp, ứng với quy tắc nào>
- Điểm cần sửa: <chỉ liệt kê mục thay đổi>
- Phương án ảnh chính sau cải tiến: <...>
- Hiệu quả kỳ vọng: <một câu>
```

---

# FINAL OUTPUT STRUCTURE

```markdown
## 1. Kế hoạch nội dung 9 ảnh
(bảng 9 dòng)

## 2. Phương án theo khác biệt sàn
(chỉ xuất khi là ML / Amazon; sàn khác ghi "Không có xung đột giữa các sàn")

## 3. Chi tiết text trong ảnh
(từng ảnh)

## 4. Quét tuân thủ hình ảnh
(xuất theo I1–I8 của 00_system.md; không vi phạm cũng phải ghi "không vi phạm")

## 5. Các trường giao cho 05 Product Video
- visual_tone_confirmed:     # Tông hình ảnh được xác nhận cuối cùng
- hero_visual:               # Mô tả khung hình ảnh chính → tham chiếu khung hình đầu của video
- key_visual_moments: []     # 2–3 khung hình có sức hút thị giác nhất → mục ưu tiên cho storyboard video
```

---

# SELF-CHECK

- [ ] Điền đủ cả 9 vị trí ảnh, không có "chờ xác định"
- [ ] Mỗi ảnh chỉ mang một thông tin rõ ràng
- [ ] Quy chuẩn ảnh chính đúng với sàn mục tiêu (ML không có chữ)
- [ ] Text trong ảnh không quá 3 dòng, mỗi dòng không vượt giới hạn
- [ ] Mọi con số khớp từng ký tự với `spec_table`
- [ ] Mọi bối cảnh đều nằm trong `usage_scope_confirmed`
- [ ] Ảnh 8 đã ghi rõ "không có gì"
- [ ] Khi `certifications` trống thì không tạo bất kỳ ảnh chứng nhận nào
- [ ] Cuối đầu ra đã kèm quét tuân thủ hình ảnh + các trường cho downstream
