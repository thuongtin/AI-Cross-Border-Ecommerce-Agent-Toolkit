# TASK · Kịch bản và storyboard

> Dùng kèm: `00_system.md` + đầu ra của 03 Listing Creative Agent

---

# INPUT

| Trường | Nguồn | Ghi chú |
|---|---|---|
| `platform` | Nhập tay | Quyết định thời lượng và tỷ lệ khung hình |
| `target_market` | Nhập tay | Quyết định ngôn ngữ |
| `mode` | Nhập tay | `standard` / `variant` |
| `durations` | Nhập tay | `[15]` / `[30]` / `[15,30]` (mặc định hai bản) |
| `product_name` | 03 | |
| `core_selling_point` | **03 (mục chặn)** | Hook và mạch chính |
| `secondary_points[]` | **03 (mục chặn)** | Phần điểm bán hàng |
| `spec_table` | **03 (mục chặn)** | Phần thông số |
| `forbidden_words[]` | **03 (mục chặn)** | Chặn từ cấm trong phụ đề |
| `usage_scope_confirmed[]` | **03 (mục chặn)** | Cảnh bối cảnh |
| `title_final` | 03 | CTA cuối video |
| `visual_tone_confirmed` | 04 (tùy chọn) | Thống nhất phong cách toàn video |
| `hero_visual` | 04 (tùy chọn) | Tham chiếu khung hình đầu |
| `key_visual_moments[]` | 04 (tùy chọn) | Ưu tiên khi lên storyboard |
| `production_mode` | Nhập tay | `ai_generated` (tạo hoàn toàn bằng AI) / `real_shoot` (quay thật) / `mixed` (kết hợp) |

---

# STEP 1 · Thiết kế hook

Xuất trước nhiều phương án hook, sau đó chọn một:

```markdown
## 1. Phương án hook (0–3s)

| # | Loại | Câu hook | Hình ảnh | Chọn |
|---|---|---|---|---|
| A | Đánh thẳng nỗi đau | `<tiếng bản ngữ>` | `<mô tả hình ảnh>` | |
| B | Đưa kết quả lên trước | `<tiếng bản ngữ>` | `<mô tả hình ảnh>` | ✅ Đã chọn |
| C | Phản trực giác | `<tiếng bản ngữ>` | `<mô tả hình ảnh>` | |

**Lý do chọn**: <một câu>
```

## Quy tắc cứng cho hook

| Quy tắc | Ghi chú |
|---|---|
| ❌ Cấm tự giới thiệu | `Olá pessoal` / `Bem-vindos ao canal` / `Hoje vou mostrar` |
| ❌ Cấm mở đầu bằng animation Logo | Đưa Logo vào 3 giây đầu = phí 3 giây |
| ❌ Cấm rào đón | `Antes de começar, deixe seu like` |
| ✅ Nguồn ưu tiên | Lời phàn nàn trong đánh giá tiêu cực → hook nỗi đau; điểm hài lòng trong đánh giá tích cực → hook kết quả |
| ✅ Hình ảnh phải có chuyển động | Mở đầu bằng ảnh sản phẩm tĩnh = bị lướt qua |

---

# STEP 2 · Cấu trúc kịch bản

## Khi durations có 15

```markdown
## 2. Kịch bản bản 15s

| Phân đoạn | Thời gian | Mục tiêu | Nội dung |
|---|---|---|---|
| Hook | 0–3s | Giữ chân sự chú ý | <câu hook + hình ảnh> |
| Điểm bán hàng cốt lõi | 3–9s | Nói rõ một điều | <hình ảnh hóa core_selling_point> |
| Bối cảnh | 9–13s | Nhập vai | <bối cảnh usage_scope[0]> |
| CTA | 13–15s | Kêu gọi hành động | <khớp với title_final> |
```

## Khi durations có 30

```markdown
## 3. Kịch bản bản 30s

| Phân đoạn | Thời gian | Mục tiêu | Nội dung |
|---|---|---|---|
| Hook | 0–3s | Giữ chân sự chú ý | <giống hook bản 15s> |
| Điểm bán hàng 1 | 3–9s | Điểm bán hàng chính | <core_selling_point> |
| Điểm bán hàng 2 | 9–16s | Điểm bán hàng phụ | <secondary_points[0]> |
| Bối cảnh | 16–23s | Nhập vai | <usage_scope[0] + [1]> |
| Thông số / Niềm tin | 23–28s | Xóa băn khoăn | <thông số chính + bảo hành> |
| CTA | 28–30s | Kêu gọi hành động | <giống CTA bản 15s> |
```

> **Nguyên tắc cấu trúc**: **hook và CTA của bản 15s và bản 30s phải giống nhau**. Bản 30s không phải là bản 15s kéo dài ra, mà là chèn thêm các đoạn lập luận——hook và phần kết cùng phục vụ một ý.

---

# STEP 3 · Bảng storyboard

Đây là **đầu ra cốt lõi nhất** của nhiệm vụ này——bảng storyboard phải giao thẳng cho editor được.

```markdown
## 4. Bảng storyboard (bản <n>s)

| Cảnh số | Thời lượng | Nội dung hình ảnh | Chuyển động máy | Phụ đề (xem khi tắt tiếng) | Hiệu ứng âm thanh / Giọng đọc |
|---|---|---|---|---|---|
| 1 | 0–3s | <mô tả hình ảnh cụ thể, ghi rõ chủ thể/hành động/môi trường> | <máy tĩnh / push-in / bám theo / góc từ trên xuống> | `<tiếng bản ngữ, ≤20 ký tự>` | <giọng đọc / âm thanh môi trường / hiệu ứng âm thanh> |
| 2 | 3–6s | | | | |
| ... | | | | | |
```

## Yêu cầu cứng cho bảng storyboard

| Hạng mục | Yêu cầu |
|---|---|
| **Nội dung hình ảnh** | Phải cụ thể đến mức quay được ngay. Không viết "giới thiệu sản phẩm", mà viết "tay cầm sạc dự phòng, màn hình hiển thị 87%, cắm dây cáp vào" |
| **Chuyển động máy** | Mỗi cảnh đều phải ghi, kể cả chỉ ghi "máy tĩnh" |
| **Phụ đề (xem khi tắt tiếng)** | **Bắt buộc điền**. Đây là kênh truyền tải thông tin khi người xem tắt tiếng |
| **Số dòng phụ đề** | Mỗi màn hình ≤ 2 dòng, mỗi dòng ≤ 20 ký tự (tiếng Bồ Đào Nha) |
| **Hiệu ứng âm thanh** | Chỉ phục vụ **nhấn mạnh hành động trong hình**, không nhồi nhét |
| **Số cảnh** | Bản 15s 4–6 cảnh; bản 30s 7–10 cảnh. Ít quá thì lê thê, nhiều quá thì rối mắt |

## Khác biệt theo production_mode

| Chế độ | Cách xử lý bảng storyboard |
|---|---|
| `ai_generated` | Mỗi cảnh phải tạo được bằng mô hình video AI (tránh tương tác người phức tạp, động tác tay chính xác) |
| `real_shoot` | Viết chỉ dẫn quay thật bình thường, ghi rõ nhu cầu đạo cụ và địa điểm |
| `mixed` | Ghi `[AI]` hoặc `[Quay thật]` cho từng cảnh |

> **Quy tắc đặc biệt cho cảnh người thật**: dù ở chế độ nào, cảnh có người thật xuất hiện **chỉ viết chỉ dẫn quay** (vị trí máy, động tác, cỡ cảnh), **không xuất Prompt tạo bằng AI**. Lý do xem V6 trong `00_system.md`.

---

# STEP 4 · Đối chiếu thời lượng

```markdown
## 5. Đối chiếu thời lượng

| Phiên bản | Thời lượng mục tiêu | Cộng dồn storyboard | Ước tính lồng tiếng | Khớp không |
|---|---|---|---|---|
| 15s | 15s | <n>s | <n>s | ✅ / ❌ |
| 30s | 30s | <n>s | <n>s | ✅ / ❌ |
```

**Quy tắc ước tính thời lượng lồng tiếng** (áp dụng cho TTS và người đọc thật ở đa số ngôn ngữ):

| Ngôn ngữ | Tốc độ đọc tham khảo |
|---|---|
| Tiếng Bồ Đào Nha (Brazil) | Khoảng **2.5 từ/giây** (nhịp quảng cáo văn nói) |
| Tiếng Tây Ban Nha | Khoảng **2.5 từ/giây** |
| Tiếng Anh | Khoảng **2.8 từ/giây** |

> Ví dụ: video 15s, trừ khoảng lặng thì phần đọc hiệu quả khoảng 12s → kịch bản lồng tiếng giữ trong khoảng **30 từ**.
> Thừa thì cắt, đừng tăng tốc độ đọc——đọc nhanh lên là người mua Brazil cảm thấy ngay "cái này không giống quảng cáo bản địa".

---

# Cấu trúc đầu ra

```markdown
## 1. Phương án hook
## 2. Kịch bản bản 15s        (nếu durations có 15)
## 3. Kịch bản bản 30s        (nếu durations có 30)
## 4. Bảng storyboard
## 5. Đối chiếu thời lượng
## 6. Yêu cầu nhạc nền và hiệu ứng âm thanh
   - Cảm xúc BGM: <...> (⚠️ phải dùng nội dung được phép dùng thương mại)
   - Hiệu ứng âm thanh chính: <...>
## 7. Quét tuân thủ video
(Xuất theo V1–V8 trong 00_system.md; không có vi phạm thì bắt buộc ghi "không có vi phạm")
## 8. Các trường bàn giao cho module tiếp theo
- hook_final:
- shot_count:
- subtitle_lines: []
- cta_line:
```

---

# mode = variant

Tương ứng với việc tạo khác biệt cho nhiều shop hoặc nhiều link ở SOP 2.3 / 3.4, xuất **2 bộ kịch bản có góc tiếp cận khác nhau**:

| Biến thể | Góc tiếp cận | Loại hook | Phù hợp |
|---|---|---|---|
| 1 | Tiếp cận từ nỗi đau | Loại phàn nàn từ đánh giá tiêu cực | Thị trường trưởng thành, người mua đã biết mình cần gì |
| 2 | Tiếp cận từ kết quả | Loại hài lòng từ đánh giá tích cực | Thị trường mới nổi, cần xây dựng nhận thức về nhu cầu trước |

Hai bộ phải khác nhau thực chất về **hook, thứ tự điểm bán hàng, lựa chọn bối cảnh**, không được chỉ đổi câu chữ.

---

# SELF-CHECK

- [ ] 3 giây đầu là hook, không phải tự giới thiệu
- [ ] Bản 15s chỉ nói một điểm bán hàng cốt lõi
- [ ] Mỗi dòng của bảng storyboard đều có đủ bốn cột hình ảnh/chuyển động máy/phụ đề/hiệu ứng âm thanh, không bỏ trống
- [ ] Phụ đề mỗi màn hình ≤2 dòng, mỗi dòng ≤20 ký tự
- [ ] Số từ lồng tiếng khớp với ước tính tốc độ đọc, không vượt thời lượng
- [ ] Mọi giá trị số khớp với `spec_table`
- [ ] Mọi bối cảnh đều nằm trong `usage_scope_confirmed`
- [ ] Cảnh người thật chỉ có chỉ dẫn quay, không có Prompt tạo bằng AI
- [ ] BGM đã ghi chú yêu cầu được phép dùng thương mại
- [ ] Hook và CTA của bản 15s và 30s giống nhau
- [ ] Cuối đầu ra đã kèm quét tuân thủ video + các trường bàn giao
