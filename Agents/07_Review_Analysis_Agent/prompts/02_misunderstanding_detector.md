# TASK · Nhận diện đánh giá tiêu cực loại hiểu lầm và vá trang chi tiết

> Dùng kèm: `00_system.md` + đầu ra của `01_classify_and_attribute.md`
> Tương ứng SOP **3.7 Duy trì đánh giá và hậu mãi** · **1.6 mục tiêu phân tích câu 3–5**

**Đây là task quan trọng nhất của module này.** Đầu ra của nó viết lại trực tiếp Listing, và là **hành động có ROI cao nhất trong toàn bộ quy trình** — sửa một câu, xóa sổ cả một nhóm đánh giá tiêu cực.

---

# INPUT

| Trường | Nguồn | Mô tả |
|---|---|---|
| `platform` / `target_market` | Người nhập | Quyết định ngôn ngữ đầu ra |
| `spec_table` | 03 | **Mục chặn** — chuẩn để phán định hiểu lầm về thông số |
| `package_content[]` | 03 | **Mục chặn** — chuẩn để phán định hiểu lầm về phụ kiện |
| `usage_scope[]` | 03 | **Mục chặn** — chuẩn để phán định hiểu lầm về tình huống sử dụng |
| `warranty` | 03 | Phán định hiểu lầm về hậu mãi |
| `reviews[]` | Dữ liệu đánh giá | Nguyên văn đánh giá tiêu cực |
| `attribution` | **Đầu ra của 01** | Kết quả quy nguyên nhân 8 nhóm đã hoàn tất |
| `current_description` | 03 | Nội dung trang chi tiết hiện tại (để xác định cần bổ sung ở đoạn nào) |
| `current_image_plan` | 04 (tùy chọn) | Kế hoạch 9 ảnh hiện tại (để phán đoán có cần bổ sung ảnh không) |

---

# STEP 1 · Phán định loại hiểu lầm

Với **từng** đánh giá tiêu cực được xếp vào "Hiểu lầm", đi qua chuỗi phán định:

```
1. Người mua phàn nàn cụ thể điều gì?
2. Thông tin đó nằm ở trường nào của input? (spec_table / package_content / usage_scope / warranty)
3. Listing hiện tại (current_description / current_image_plan) có nhắc điểm này không?
   ├─ Hoàn toàn không nhắc → phán định: thiếu giải thích
   ├─ Có nhắc nhưng bị chìm trong chi tiết → phán định: giải thích không nổi bật
   └─ Có nhắc và rất nổi bật → phán định: người mua không đọc (cần đổi vị trí hoặc cách diễn đạt)
4. Đưa ra hành động vá theo kết quả phán định
```

## Ba loại phán định và hành động tương ứng

| Phán định | Đặc điểm | Hành động vá | Chi phí |
|---|---|---|---|
| **Thiếu giải thích** | Listing hoàn toàn không nhắc | Thêm mục giải thích mới | Thấp |
| **Giải thích không nổi bật** | Có nhắc nhưng nằm sâu trong đoạn / chữ nhỏ | Đưa lên mục đầu tiên của đoạn Lưu ý / bổ sung ảnh | Trung bình |
| **Người mua không đọc** | Đã rất nổi bật mà vẫn bị hiểu lầm | Đổi cách diễn đạt: từ chữ chuyển sang **ảnh** | Trung bình |

> **"Chuyển thành ảnh" là cách hiệu quả nhất để xử lý "người mua không đọc".** Chữ sẽ bị lướt qua, ảnh thì không.
> Ví dụ: danh sách đóng gói viết bằng chữ "có X, không có Y" thì người mua không đọc; làm thành một ảnh bày phẳng và ghi `Não incluso` là giải quyết xong.

## Định dạng đầu ra

```markdown
## 1. Phán định đánh giá tiêu cực loại hiểu lầm

| # | Nguyên văn đánh giá tiêu cực | Người mua tưởng | Thực tế (trường căn cứ) | Listing hiện tại có nhắc không | Phán định | Hành động vá |
|---|---|---|---|---|---|---|
| 1 | `<nguyên văn>` | | `<spec_table.xxx = giá trị>` | Không nhắc | Thiếu giải thích | Thêm vào đoạn 6 trang chi tiết |
| 2 | `<nguyên văn>` | | `<package_content không có xxx>` | Có nhắc nhưng ở dòng cuối bảng đoạn 4 | Giải thích không nổi bật | Chuyển lên mục đầu đoạn 6 |
| 3 | `<nguyên văn>` | | `<usage_scope chỉ gồm dốc thoải>` | Đã viết nhưng người mua không để ý | Người mua không đọc | Bổ sung một ảnh giới hạn tình huống |
```

> ⚠️ **Phân biệt then chốt**: nếu đối chiếu `spec_table` / `package_content` mà thấy **thực tế đúng là không khớp mô tả**, thì đó không phải loại hiểu lầm mà là **thông số không như kỳ vọng**, phải đi theo hướng khác (sửa mô tả hoặc sửa sản phẩm), không được trộn vào đây.

---

# STEP 2 · Đề xuất vá trang chi tiết

Với mỗi kết quả phán định, xuất **nội dung bằng ngôn ngữ bản địa, dán thẳng được**.

```markdown
## 2. Đề xuất vá trang chi tiết

### 2.1 Mục thêm mới / chỉnh sửa

| # | Đánh giá tiêu cực tương ứng | Vị trí viết | Nội dung (<ngôn ngữ mục tiêu>) | Giải thích (tiếng Việt) |
|---|---|---|---|---|
| 1 | #1 | Đoạn 6 · Lưu ý (mục đầu) | `<nội dung bản địa>` | Ghi rõ không kèm mũ bảo hiểm |
| 2 | #2 | Đoạn 6 · Lưu ý | `<nội dung bản địa>` | Ghi rõ giới hạn khả năng leo dốc |

### 2.2 Ảnh cần bổ sung (quay về 04)

| # | Đánh giá tiêu cực tương ứng | Vị trí ảnh | Chữ trên ảnh | Mô tả |
|---|---|---|---|---|
| 1 | #1 | Ảnh 8 · Ảnh danh sách đóng gói | `Não incluso: capacete` | Dùng ảnh thay cho giải thích bằng chữ |

### 2.3 Cách diễn đạt cần sửa (quay về 03)

| # | Diễn đạt gốc | Vấn đề | Diễn đạt đề xuất |
|---|---|---|---|
| 1 | `<nguyên văn>` | Tạo kỳ vọng quá cao cho người mua | `<diễn đạt mới>` |
```

## Bốn quy tắc viết nội dung

| Quy tắc | Mô tả | Ví dụ |
|---|---|---|
| **Khẳng định trực diện, không biện minh** | Không viết kiểu ngầm trách "người mua không đọc kỹ" | ✅ `O capacete não está incluso.` |
| **Nêu giới hạn, không nói "không làm được"** | Nói rõ phạm vi khả năng, thay vì phủ định sản phẩm | ✅ `Indicado para ladeiras leves e vias pavimentadas.` ❌ `Não sobe ladeiras.` |
| **Đưa lên vị trí nổi bật** | Mục dễ bị hiểu lầm đặt ở **mục đầu** của đoạn Lưu ý | Đừng đặt giữa đoạn |
| **Kèm số liệu hoặc độ dài cụ thể** | Giải thích mơ hồ coi như không giải thích | ✅ `O cabo tem 30 cm.` ❌ `O cabo é curto.` |

---

# STEP 3 · Rút lằn ranh đỏ thông số

Rút các thông số bị phàn nàn "không như kỳ vọng" nhiều lần thành ứng viên `forbidden_words`.

```markdown
## 3. Lằn ranh đỏ thông số

| # | Thông số bị phàn nàn | Người mua kỳ vọng | Giá trị thực tế trong `spec_table` | Ứng viên từ cấm | Lý do |
|---|---|---|---|---|---|
| 1 | Quãng đường | 60 km | 35 km | `60 km` `autonomia longa` | Sẽ gây đánh giá tiêu cực về quãng đường |
| 2 | Tải trọng | 200 kg | 150 kg | `200 kg` | Dùng quá tải có rủi ro an toàn |
| 3 | Leo dốc | Mọi loại dốc | Dốc thoải | `qualquer ladeira` `sobe tudo` | Diễn đạt không giới hạn sẽ bị hiểu là mọi tình huống |

**Xuất thành `forbidden_words_candidates[]`** (để 03/04/05 chặn cứng)
```

> **Giá trị của lằn ranh đỏ là "phòng bệnh hơn chữa bệnh"**: những từ này thường xuất hiện trong bảng từ khóa của đối thủ (đối thủ có thể ghi quãng đường 60km), nếu lấy về dùng theo hướng SEO thì chẳng khác nào chủ động khai khống thông số. **Phân tích đánh giá là con đường trực tiếp nhất để phát hiện những lằn ranh đỏ như vậy.**

---

# STEP 4 · Đánh giá khả năng khắc phục

```markdown
## 4. Đánh giá khả năng khắc phục

| Hạng mục | Số lượng | Tỷ trọng |
|---|---|---|
| Tổng đánh giá tiêu cực | | 100% |
| **Khắc phục được bằng sửa mô tả / sửa ảnh** | | |
| Cần sửa sản phẩm / nhà cung cấp | | |
| Cần sửa vận chuyển | | |

**Kết luận**: <n>% đánh giá tiêu cực có thể giải quyết bằng cách sửa Listing, không cần động vào sản phẩm.

**Thứ tự ưu tiên khắc phục**: <xếp theo «tần suất xuất hiện ÷ chi phí khắc phục»>
```

---

# STEP 5 · Mẫu câu CSKH (tùy chọn)

**Chỉ xuất khi input có yêu cầu rõ ràng.**

```markdown
## 5. Đề xuất mẫu câu CSKH

| Tình huống | Mẫu câu (ngôn ngữ mục tiêu) | Mô tả |
|---|---|---|
| Khách hỏi trước khi mua: có kèm phụ kiện X không | | Trả lời đúng sự thật + gợi ý phụ kiện có thể mua |
| Trả lời đánh giá tiêu cực: thông số không khớp (đo thực tế không sai) | | Nói đúng điều kiện thử nghiệm, không biện minh |
| Trả lời đánh giá tiêu cực: lỗi chức năng | | Xin lỗi + phương án hậu mãi |
```

## Ba nguyên tắc bất di bất dịch của mẫu câu

| Nguyên tắc | Mô tả |
|---|---|
| ❌ Không dùng lợi ích dụ dỗ xóa đánh giá | Đây là hành động có trong SOP nhưng repo này không triển khai |
| ❌ Không dùng lý do sai sự thật để giải thích thông số không khớp | Như "đóng nhầm sách hướng dẫn" — là gian lận |
| ✅ Nói đúng sự thật + đưa ra phương án giải quyết | Con đường chính đáng duy nhất |

---

# FINAL OUTPUT STRUCTURE

```markdown
## 1. Phán định đánh giá tiêu cực loại hiểu lầm
## 2. Đề xuất vá trang chi tiết
   ### 2.1 Mục thêm mới / chỉnh sửa
   ### 2.2 Ảnh cần bổ sung (→ 04)
   ### 2.3 Cách diễn đạt cần sửa (→ 03)
## 3. Lằn ranh đỏ thông số
## 4. Đánh giá khả năng khắc phục
## 5. Đề xuất mẫu câu CSKH        (xuất có điều kiện)
## 6. Quét tuân thủ phân tích
   (theo C1–C5 của 00_system.md; không vi phạm thì bắt buộc ghi "không vi phạm")
## 7. Các trường bàn giao cho module khác
   - review_patch_suggestions: []      # → 03 đoạn Lưu ý trang chi tiết
   - forbidden_words_candidates: []    # → 03/04/05 chặn cứng
   - packaging_clarity_needed: true/false  # → 04 ảnh danh sách đóng gói
   - scene_limit_image_needed: true/false  # → 04 ảnh giới hạn tình huống
   - fixable_ratio: 0.00
```

---

# SELF-CHECK

- [ ] Mỗi đánh giá tiêu cực loại hiểu lầm đều đã đối chiếu trường cụ thể (spec_table / package_content / usage_scope)
- [ ] Đã phân biệt ba loại phán định "thiếu giải thích / giải thích không nổi bật / người mua không đọc"
- [ ] Trường hợp đúng là không khớp mô tả đã chuyển sang "thông số không như kỳ vọng", không trộn vào loại hiểu lầm
- [ ] Nội dung vá là **ngôn ngữ mục tiêu** và dán thẳng được
- [ ] Nội dung tuân theo bốn quy tắc (khẳng định trực diện / nêu giới hạn / đưa lên đầu / kèm số liệu)
- [ ] Trường hợp liên quan phụ kiện đã phán đoán có cần bổ sung ảnh không
- [ ] Lằn ranh đỏ thông số có ứng viên từ cấm
- [ ] Đã tính tỷ trọng khả năng khắc phục
- [ ] Mẫu câu CSKH không có dụ dỗ xóa đánh giá, không có giải thích sai sự thật
- [ ] Cuối đầu ra đã kèm Quét tuân thủ phân tích + các trường bàn giao
