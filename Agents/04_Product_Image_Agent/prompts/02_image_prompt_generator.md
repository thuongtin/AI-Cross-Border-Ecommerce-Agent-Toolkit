# TASK · Tạo Prompt ra ảnh

> Dùng kèm: `00_system.md` + đầu ra của `01_image_plan_9grid.md` (kế hoạch 9 ảnh + text trong ảnh)

Đầu ra của task này là Prompt **có thể dán thẳng vào công cụ tạo ảnh**.

---

# INPUT

| Trường | Nguồn | Mô tả |
|---|---|---|
| `platform` | Người nhập | Quyết định quy chuẩn ảnh chính |
| `target_market` | Người nhập | Quyết định ngôn ngữ text trong ảnh |
| `prompt_language` | Người nhập | `en` (mặc định, model phổ thông) / `zh` (model tiếng Trung như Jimeng, Tongyi Wanxiang) |
| `image_plan` | **Đầu ra của 01** | Bảng kế hoạch 9 ảnh |
| `image_copy` | **Đầu ra của 01** | Chi tiết text trong ảnh |
| `visual_tone_confirmed` | **Đầu ra của 01** | Tông hình ảnh |
| `spec_table` | 03 | Dùng để đối chiếu thông số |
| `forbidden_words[]` | 03 | Chặn từ cấm trong chữ trên ảnh |
| `has_product_photo` | Người nhập | `true` / `false` —— có ảnh chụp thật làm tham chiếu hay không |

---

# Công thức cấu trúc Prompt

Prompt của mỗi ảnh gồm **bảy slot**, thiếu một cũng không được:

```
[SUBJECT]     Chủ thể: là gì, hình dạng thế nào, màu sắc chất liệu ra sao
[MATERIAL]    Chất liệu và xử lý bề mặt: nhám/bóng/kim loại/vải, chi tiết vân bề mặt
[COMPOSITION] Bố cục: góc chụp, vị trí, tỷ lệ chiếm khung, vùng khoảng trắng
[LIGHTING]    Vị trí ánh sáng: hướng đèn chính, mềm/cứng, nhiệt độ màu, bóng đổ
[BACKGROUND]  Nền: trắng tinh/bối cảnh/gradient, mô tả cụ thể
[STYLE]       Phong cách: chân thực/chụp ảnh sản phẩm/render 3D, chất cảm tham chiếu
[PARAMETERS]  Thông số kỹ thuật: tỷ lệ, kích thước, (khi render chân thực) thông số máy ảnh
```

## Nguyên tắc then chốt

| Nguyên tắc | Mô tả |
|---|---|
| **Càng cụ thể càng dễ kiểm soát** | `nền trắng` → `nền trắng tinh liền mạch, RGB 255,255,255, không đổ bóng` |
| **Đừng nói "đẹp"** | Dùng mô tả thị giác có thể thực thi thay cho đánh giá chủ quan |
| **Chữ trong ảnh xử lý riêng** | **Không** viết chữ vào Prompt ra ảnh, mà đánh dấu là "chèn chữ hậu kỳ". Lý do: model tạo ảnh hiện nay render chữ vẫn chưa ổn định, đặc biệt dấu tiếng Bồ Đào Nha (ã ç õ é) rất dễ sai |
| **Một Prompt ra một khung hình** | Đừng cố để một Prompt tạo ra "ảnh ghép" |

> **Khuyến nghị xử lý chữ trong ảnh**: module này xuất **Prompt khung hình sản phẩm không có chữ** + **text trong ảnh riêng biệt**, rồi dùng công cụ thiết kế (Figma / Canva / Photoshop) chèn chữ ở hậu kỳ. Như vậy chữ chắc chắn chính xác, chắc chắn rõ nét, chắc chắn không sai dấu.

---

# Định dạng đầu ra

Xuất lần lượt cho 9 ảnh:

```markdown
### Ảnh <n> · <vị trí ảnh>

**Prompt ra ảnh (<prompt_language>)**
```text
<Prompt đầy đủ, đủ bảy slot>
```

**Negative Prompt**
```text
<các yếu tố cần loại bỏ>
```

**Text trong ảnh (chèn chữ hậu kỳ)**
- Text chính: `<ngôn ngữ bản địa>`
- Text phụ: `<ngôn ngữ bản địa>`
- Vị trí: <giữa lệch lên trên / góc dưới bên trái / ...>
- Gợi ý cỡ chữ: <chiều cao text chính ≥ 4% chiều cao ảnh>

**Thông số render**
- Tỷ lệ: 1:1 (hoặc theo sàn)
- Kích thước khuyến nghị: <1024×1024 / 1000×1000 / 1080×1920>
- Nhu cầu ảnh tham chiếu: <cần / không cần>

**Kiểm tra**
- Tính nhất quán của con số: ✅ / ❌ <từng mục>
- Từ cấm: ✅ không vi phạm / ❌ <liệt kê>
- Phạm vi bối cảnh: ✅ trong phạm vi / ❌ <vượt phạm vi>
```

---

# Thư viện negative Prompt chuẩn

Ghép theo sàn và theo tình huống:

## Negative prompt chung

```text
text, watermark, logo, signature, stamp, border, frame, label,
low resolution, blurry, jpeg artifacts, oversaturated,
distorted proportions, extra objects, cluttered background,
plastic look, cartoon, illustration, 3d render (unless intended)
```

## Dành riêng cho ảnh chính Mercado Livre (bắt buộc thêm)

```text
text of any kind, letters, numbers printed on the image, watermark,
logo, badge, ribbon, colored block, frame, border, background gradient,
additional props, accessories not included in the package
```

## Ảnh chính Shopee (được giữ nhãn của chính sản phẩm)

```text
watermark, extra props, cluttered background, distracting elements
```

## Dành riêng cho ảnh bối cảnh

```text
indoors with wrong context, rain, water, swimming pool (for non-waterproof items),
medical setting, exaggerated dramatic lighting, unrealistic physics
```

> Dòng cuối đặc biệt quan trọng với **sản phẩm không chống nước** —— trong khung hình có nước tức là ngầm ám chỉ sản phẩm chống nước, thuộc quảng cáo sai sự thật.

---

# Trọng tâm Prompt theo từng vị trí ảnh

| Vị trí ảnh | Trọng tâm Prompt |
|---|---|
| Ảnh 1 ảnh chính | `[BACKGROUND]` bắt buộc trắng tinh liền mạch; không có đạo cụ nào; bố cục khắt khe nhất |
| Ảnh 2 ảnh điểm bán hàng | Cần **làm nổi yếu tố thị giác ứng với điểm bán hàng** (ví dụ sạc nhanh → hiệu ứng ánh sáng dòng năng lượng, cận cảnh cổng sạc) |
| Ảnh 3 ảnh thông số | Thường là **ảnh dàn trang thiết kế**, không phải ảnh AI tạo —— xuất "đặc tả layout" thay vì Prompt ra ảnh |
| Ảnh 4/5 ảnh bối cảnh | Cần **người/môi trường**, chú ý ràng buộc chân dung I6 (khuyến nghị không lộ mặt: bàn tay, bóng lưng, cảnh xa) |
| Ảnh 6 ảnh chi tiết | Cần **chất cảm macro**, Prompt nhấn mạnh chất liệu và vân bề mặt |
| Ảnh 7 ảnh kích thước | Thường là **ảnh chụp thật hoặc ảnh thiết kế có vật tham chiếu** —— xuất "đặc tả layout" |
| Ảnh 8 ảnh danh sách đóng gói | **Bắt buộc chụp thật**, AI tạo danh sách đóng gói sẽ khiến người mua nhận hàng không đúng mô tả |
| Ảnh 9 ảnh hậu mãi | **Ảnh dàn trang thiết kế** —— xuất "đặc tả layout" |

> ⚠️ **Phán đoán quan trọng**: ảnh 3, 7, 8, 9 về bản chất là **ảnh dàn trang thông tin**, không phải ảnh AI. Với các vị trí này, xuất "đặc tả layout" (kích thước, font chữ, phân cấp, phối màu) hữu ích hơn xuất Prompt ra ảnh.
> **Ảnh 8 đặc biệt bắt buộc chụp thật** —— danh sách đóng gói do AI tạo không khớp thực tế sẽ trực tiếp gây ra đánh giá tiêu cực "thiếu phụ kiện".

---

# Cấu trúc đầu ra

```markdown
## 1. Danh sách Prompt ra ảnh
### Ảnh 1 · Ảnh chính
### Ảnh 2 · Ảnh điểm bán hàng chủ lực
...
### Ảnh 9 · Ảnh hậu mãi/bảo hành

## 2. Đặc tả layout cho các vị trí ảnh không dùng AI
(ảnh 3 / 7 / 9, và ảnh 8 cần chụp thật)

## 3. Gợi ý quy trình ra ảnh
- Thứ tự ra ảnh hàng loạt
- Quy trình chèn chữ hậu kỳ
- Các điểm kiểm soát chất lượng

## 4. Quét tuân thủ hình ảnh
(xuất theo I1–I8 của 00_system.md; không vi phạm thì ghi "không vi phạm")

## 5. Các trường giao cho downstream
- hero_visual:
- key_visual_moments: []
- visual_tone_confirmed:
```

---

# SELF-CHECK

- [ ] Mỗi Prompt ra ảnh AI đều đủ bảy slot
- [ ] Mỗi ảnh đều kèm negative Prompt
- [ ] Negative prompt của Prompt ảnh chính ML / Amazon có chứa `text of any kind`
- [ ] Negative prompt của Prompt bối cảnh cho sản phẩm không chống nước có chứa `rain, water, swimming pool`
- [ ] Chữ trong ảnh **không được viết vào** Prompt ra ảnh, mà đánh dấu là chèn chữ hậu kỳ
- [ ] Ảnh 8 đã đánh dấu "bắt buộc chụp thật"
- [ ] Ảnh 3 / 7 / 9 đã xuất "đặc tả layout" thay vì Prompt ra ảnh
- [ ] Bố cục người trong ảnh bối cảnh đã tránh khuôn mặt có thể nhận diện
- [ ] Mọi con số khớp với `spec_table`
- [ ] Cuối đầu ra đã kèm quét tuân thủ hình ảnh
