# TASK · Prompt video AI và lồng tiếng

> Dùng kèm: `00_system.md` + đầu ra của `01_script_and_storyboard.md` (bảng storyboard)
> Nhiệm vụ này biến bảng storyboard thành **lệnh tạo nội dung thực thi được**: Prompt video, kịch bản lồng tiếng, phụ đề.

---

# INPUT

| Trường | Nguồn | Ghi chú |
|---|---|---|
| `platform` | Nhập tay | Quyết định tỷ lệ khung hình và vùng an toàn |
| `target_market` | Nhập tay | Quyết định ngôn ngữ |
| `prompt_language` | Nhập tay | `en` (mặc định) / `zh` |
| `storyboard` | **Đầu ra của 01** | Bảng storyboard |
| `production_mode` | Nhập tay | `ai_generated` / `real_shoot` / `mixed` |
| `spec_table` | 03 | Kiểm tra thông số |
| `forbidden_words[]` | 03 | Chặn từ cấm trong phụ đề |
| `visual_tone_confirmed` | 04 | Thống nhất phong cách |
| `hero_visual` | 04 | Tham chiếu khung hình đầu |
| `voice_style` | Nhập tay | Phong cách lồng tiếng mong muốn (tùy chọn) |

---

# PART A · Prompt video AI

## Công thức cấu trúc Prompt (sáu ô)

```
[SUBJECT]      Chủ thể: là gì, hình dáng ra sao, màu sắc chất liệu, đang ở trạng thái nào
[ACTION]       Hành động: chủ thể đang làm gì (đây là ô cốt lõi phân biệt video với ảnh)
[CAMERA]       Chuyển động máy: push-in / pull-out / lia / bám theo / quay vòng / máy tĩnh, kèm tốc độ
[LIGHTING]     Ánh sáng: hướng, mềm hay gắt, nhiệt độ màu
[ENVIRONMENT]  Môi trường: nền, bối cảnh, không khí
[STYLE]        Phong cách + thông số kỹ thuật: tả thực/quảng cáo thương mại/chất cảm vật liệu, tỷ lệ, thời lượng
```

## Ba yêu cầu đặc biệt cho Prompt video

| Yêu cầu | Ghi chú |
|---|---|
| **Hành động phải đơn nhất** | Mỗi cảnh chỉ làm một việc. Viết "vừa xoay, vừa phát sáng, vừa biến hình" → mô hình sẽ cho ra một mớ nhòe nhoẹt |
| **Tránh động tác tay tinh vi** | Mô hình video AI xử lý ngón tay vẫn chưa ổn định. Khi cần cầm sản phẩm, né bằng cách "tay ra khỏi khung hình/cận cảnh không lộ tay" |
| **Chuyển động máy phải chậm** | Ghi rõ `slow`, `gentle`. Chuyển động máy nhanh rất dễ gây méo, lệch hình trong mô hình tạo video |

## Định dạng đầu ra

```markdown
### Cảnh <n> · <khoảng thời gian>

**Prompt video (<prompt_language>)**
```text
<đủ sáu ô>
```

**Prompt tham chiếu khung hình đầu** (tùy chọn, khi cần image-to-video)
```text
<Prompt hình ảnh tĩnh>
```

**Negative Prompt**
```text
<các yếu tố cần loại trừ>
```

**Thông số kỹ thuật**
- Tỷ lệ: <1:1 / 9:16 / 16:9>
- Thời lượng: <n>s
- Cường độ chuyển động: <low / medium>
- Cách tạo: <text-to-video / image-to-video>

**Kiểm tra**
- Nhất quán số liệu: ✅ / ❌
- Phạm vi bối cảnh: ✅ / ❌
- Chân dung người thật: ✅ không có người thật / ⚠️ xem ghi chú đặc biệt bên dưới
```

## Xử lý đặc biệt cho cảnh người thật (quan trọng)

Nếu storyboard có người thật xuất hiện, **không xuất Prompt tạo bằng AI**, thay vào đó xuất chỉ dẫn quay:

```markdown
### Cảnh <n> · <khoảng thời gian> · [Cảnh người thật — không tạo AI Prompt]

**Lý do**: liên quan đến chân dung người thật, theo quy tắc V6 chuyển thành chỉ dẫn quay.

**Chỉ dẫn quay**
- Vị trí máy: <độ cao, góc máy, cỡ cảnh>
- Động tác: <thứ tự động tác cụ thể của nhân vật>
- Đạo cụ: <đồ cần chuẩn bị>
- Địa điểm: <yêu cầu môi trường>
- Thời lượng: <n>s
- Lưu ý: <VD: "tránh lộ khuôn mặt có thể nhận diện" hoặc "cần ký giấy đồng ý sử dụng hình ảnh">

**Phương án AI thay thế** (nếu cần làm hoàn toàn bằng AI)
- Dùng bố cục không lộ mặt: <bàn tay / bóng lưng / cảnh xa / bóng đen>
- Prompt tương ứng: <...>
```

---

# PART B · Kịch bản lồng tiếng

## Quy tắc viết kịch bản lồng tiếng

| Quy tắc | Ghi chú | Ví dụ sai |
|---|---|---|
| **Câu ngắn** | Mỗi câu ≤ 12 từ | ❌ Một câu lồng ba mệnh đề phụ |
| **Văn nói** | Viết "lời nói ra miệng", không phải "lời viết ra giấy" | ❌ `O dispositivo possui capacidade de…` |
| **Số theo cách đọc** | Viết theo cách đọc thành tiếng | ✅ `vinte mil mAh` / ❌ `20000mAh` |
| **Mỗi câu dùng độc lập được** | Tách riêng một câu ra vẫn nghe hiểu | — |
| **Đánh dấu ngắt hơi** | Dùng `|` để đánh dấu chỗ lấy hơi | — |
| **Đánh dấu nhấn giọng** | Dùng **in đậm** để đánh dấu từ đọc nhấn | — |

## Định dạng đầu ra

```markdown
## Kịch bản lồng tiếng (bản <n>s)

| Cảnh số | Thời gian | Lời lồng tiếng | Số từ | Số từ cộng dồn | Thời lượng ước tính |
|---|---|---|---|---|---|
| 1 | 0–3s | Você já ficou sem bateria no meio do dia? | 9 | 9 | 3,6s |
| 2 | 3–6s | Este carregador tem **vinte mil mAh** … | 11 | 20 | 8,0s |
```

**Tốc độ đọc tham khảo** (nhịp quảng cáo văn nói):

| Ngôn ngữ | Tốc độ đọc |
|---|---|
| Tiếng Bồ Đào Nha (Brazil) | Khoảng **2,5 từ/giây** |
| Tiếng Tây Ban Nha | Khoảng **2,5 từ/giây** |
| Tiếng Anh | Khoảng **2,8 từ/giây** |

> Thời lượng ước tính = số từ ÷ tốc độ đọc. Nếu thời lượng cộng dồn vượt khung thời gian của phân đoạn → **cắt từ, không tăng tốc độ đọc**.

## Gợi ý TTS

```markdown
**Gợi ý thông số TTS**
- Ngôn ngữ / giọng: Português (Brasil)
- Chất giọng: <giọng nam / giọng nữ>, <độ tuổi cảm nhận>, <ngữ điệu: thân thiện / chuyên nghiệp / năng động>
- Tốc độ: <1.0x> (không tăng quá 1.1x)
- Ngắt nghỉ: cuối câu 0,3s, chỗ chuyển cảnh 0,2s
- Kiểm tra dấu thanh: ✅ đã kiểm tra ã ç õ é ê í ó ú
```

> **Dấu thanh là điểm hay "toang" của TTS PT-BR.** Sau khi tạo xong bắt buộc kiểm tra chính tả thủ công một lượt, đặc biệt là `ã` `ç` `õ`. Đọc sai là nghe ra ngay.

---

# PART C · Phụ đề

## Quy tắc phụ đề

| Quy tắc | Giá trị |
|---|---|
| Số dòng mỗi màn hình | ≤ **2 dòng** |
| Số ký tự mỗi dòng | ≤ **20 ký tự** (tiếng Bồ Đào Nha) |
| Vị trí | Video dọc tránh 20% phía dưới / 15% phía trên; video ngang đặt giữa lệch xuống dưới |
| Cỡ chữ | Đọc được trên mobile, chiều cao tương đương ≥ 4% chiều cao video |
| Độ tương phản | Bắt buộc có viền chữ hoặc nền lót, tránh đè lên vùng hình sáng màu |
| Quan hệ với lồng tiếng | **Không yêu cầu khớp từng chữ**, có thể rút gọn——phụ đề phải ngắn, lồng tiếng có thể dài hơn một chút |
| Quan hệ với hình ảnh | Phụ đề không được che chủ thể sản phẩm |

## Định dạng đầu ra

```markdown
## Bảng phụ đề (bản <n>s)

| Cảnh số | Thời gian | Phụ đề (dòng 1) | Phụ đề (dòng 2) | Số ký tự | Vị trí |
|---|---|---|---|---|---|
| 1 | 0–3s | | | | |
| ... | | | | | |
```

## Kiểm tra khi tắt tiếng

Sau khi xuất xong bảng phụ đề, thực hiện một lượt **tự kiểm tra khi tắt tiếng**:

```markdown
## Kiểm tra khả năng hiểu khi tắt tiếng

| Mục kiểm tra | Kết quả |
|---|---|
| Tắt tiếng, có hiểu đây là sản phẩm gì không | ✅ / ❌ |
| Tắt tiếng, có hiểu điểm bán hàng cốt lõi không | ✅ / ❌ |
| Tắt tiếng, có hiểu cuối video cần làm gì không | ✅ / ❌ |
```

> Cả ba mục đều ✅ mới tính là đạt. Trên Shopee Brazil và trong bối cảnh video ngắn, **phần lớn người dùng xem khi tắt tiếng**——không qua được bước này thì lồng tiếng hay mấy cũng vô nghĩa.

---

# Xử lý theo production_mode

| Chế độ | Xử lý |
|---|---|
| `ai_generated` | Xuất Prompt video cho toàn bộ storyboard. Tránh động tác tay phức tạp và người thật xuất hiện |
| `real_shoot` | Không xuất Prompt video, toàn bộ xuất chỉ dẫn quay (vị trí máy/động tác/đạo cụ/địa điểm) |
| `mixed` | Ghi chú từng cảnh, cảnh AI xuất Prompt, cảnh người thật xuất chỉ dẫn quay |

---

# Cấu trúc đầu ra

```markdown
## 1. Prompt video AI
### Cảnh 1 · 0–3s
### Cảnh 2 · 3–6s
...

## 2. Kịch bản lồng tiếng
(Bảng + gợi ý thông số TTS)

## 3. Bảng phụ đề
(Bảng)

## 4. Kiểm tra khả năng hiểu khi tắt tiếng

## 5. Yêu cầu kỹ thuật và nội dung
- Tỷ lệ / độ phân giải
- Cảm xúc BGM: <...> (⚠️ phải dùng nội dung được phép dùng thương mại)
- Danh sách hiệu ứng âm thanh
- Các thành phần đồ họa cần chèn ở hậu kỳ (vị trí Logo, thẻ thông số)

## 6. Quét tuân thủ video
(Theo V1–V8 trong 00_system.md; không có vi phạm thì ghi "không có vi phạm")

## 7. Các trường bàn giao
- prompt_count:
- subtitle_lines: []
- voiceover_word_count:
- final_cta:
```

---

# SELF-CHECK

- [ ] Prompt của mỗi cảnh AI đều đủ sáu ô
- [ ] Hành động đơn nhất, không "làm nhiều việc cùng lúc"
- [ ] Chuyển động máy đã ghi tốc độ và hướng
- [ ] Cảnh người thật **không xuất** Prompt tạo bằng AI, thay bằng chỉ dẫn quay + phương án thay thế không lộ mặt
- [ ] Kịch bản lồng tiếng mỗi câu ≤12 từ, số đã viết theo cách đọc
- [ ] Số từ lồng tiếng cộng dồn khớp khung thời gian, không vượt giờ
- [ ] Phụ đề mỗi màn hình ≤2 dòng, mỗi dòng ≤20 ký tự
- [ ] Đã kiểm tra dấu thanh
- [ ] Ba mục kiểm tra khi tắt tiếng đều ✅
- [ ] Mọi giá trị số khớp với `spec_table`
- [ ] Phụ đề không chứa bất kỳ từ nào trong `forbidden_words[]`
- [ ] BGM đã ghi chú yêu cầu được phép dùng thương mại
- [ ] Cuối đầu ra đã kèm quét tuân thủ video
