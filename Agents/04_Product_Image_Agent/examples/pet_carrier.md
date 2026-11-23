# Case study · Bolsa Transportadora para Pets (Mercado Livre Brazil)

> ⚠️ **Ghi chú cập nhật quy tắc (2026-10)**: khi viết case study này, ML yêu cầu ảnh chính nền trắng tinh.
> **Quy tắc hiện hành đã nới lỏng** —— trắng/màu trơn/bối cảnh thật theo ngành hàng, nhưng "nền sạch + ảnh đầu cấm chữ khuyến mãi" vẫn giữ nguyên.
> Phương án nền trắng trong case study này vẫn là **lựa chọn an toàn nhất** cho ngành hàng đồ thú cưng, có thể tiếp tục dùng;
> quy tắc mới nhất xem [`../references/platform-mercadolivre.md`](../references/platform-mercadolivre.md).

> **Loại case study**: sản phẩm thật · đã ẩn danh
> **Module sử dụng**: 04 Product Image Agent (phụ thuộc upstream 03 Listing Creative)
> **SOP tương ứng**: 3.3 Logic tạo 9 ảnh thương mại điện tử
> **Trọng tâm minh họa**: xử lý **xung đột quy chuẩn ảnh chính** giữa ML và Shopee

---

## I. Bối cảnh sản phẩm

| Mục | Nội dung |
|---|---|
| Sản phẩm | Túi đựng thú cưng đi ra ngoài, dạng hộp mềm gấp gọn được, mặt lưới thoáng khí, đeo vai/xách tay hai kiểu |
| Thị trường | Brazil (sàn: Mercado Livre) |
| Ngành hàng | Mẹ & bé / thú cưng |
| Định vị | Sản phẩm phổ thông |
| Tông hình ảnh | Dịu dàng, chất liệu mềm, tông nhạt |

**Vì sao chọn case study này**: ngành hàng thú cưng là vùng điển hình hay bị đánh giá tiêu cực kiểu "kích thước không như mong đợi" —— người mua không hình dung được "đựng được chó/mèo cỡ nào", ảnh kích thước làm không tốt là bị hoàn hàng ngay. Đồng thời ML cấm chữ khuyến mãi và từ thuộc tính của sàn ở ảnh đầu (khắt khe hơn Shopee), xung đột trực tiếp với cách làm phổ biến trên Shopee, vừa đúng để minh họa `platform_variant`.

---

## II. Đầu vào (kế thừa từ 03)

```yaml
platform: mercadolivre
target_market: Brazil
mode: standard
prompt_language: en
has_product_photo: true

# ── Đầu ra của 03 (các mục chặn, đã đầy đủ) ──
core_selling_point: "Ventilação em 3 lados com tela reforçada — seu pet respira e enxerga durante todo o trajeto"

secondary_points:
  - "Dobrável e plana para guardar — ocupa pouco espaço"
  - "Alça de ombro ajustável + alça de mão"
  - "Base rígida removível e lavável"
  - "Mosquetão interno para prender a coleira"

spec_table:
  dimensoes_externas: "41 × 25 × 26 cm"
  dimensoes_internas: "38 × 23 × 23 cm"
  peso: "1,2 kg"
  capacidade_peso: "até 8 kg"
  material: "Poliéster 600D + tela de nylon respirável"
  cor: "Cinza mescla com detalhes em azul"
  fechamento: "Zíper duplo com trava de segurança"

usage_scope_confirmed:
  - "Transporte de pets de pequeno porte em consultas veterinárias"
  - "Deslocamentos curtos de carro e transporte público"
  - "Viagens de ônibus de curta distância"

forbidden_words:
  - "À Prova d'Água"          # Thông số không khớp: vải chỉ chống bắn nước, không phải chống nước
  - "Grau de Companhia Aérea"  # Không có chứng nhận, không được tuyên bố
  - "100% Seguro"
  - "Irresistível"
  - "Gucci"                    # Thương hiệu không được ủy quyền

visual_tone_hint: "Suave e acolhedor — fundo claro, tons pastel, sem elementos agressivos"
certifications: []             # Để trống → không tạo bất kỳ ảnh chứng nhận nào
```

---

## III. Quy trình xử lý của AI

```text
[Kiểm tra phụ thuộc] core_selling_point / secondary_points / spec_table / forbidden_words / usage_scope đều đầy đủ ✅
[Step 1] 01_image_plan_9grid.md        → kế hoạch 9 ảnh + text trong ảnh
[Step 2] Phát hiện platform = mercadolivre → kích hoạt platform_variant, xuất hai phương án ảnh chính
[Step 3] 02_image_prompt_generator.md  → Prompt ra ảnh từng ảnh + negative prompt
[Step 4] IMAGE COMPLIANCE GUARD I1–I8  → quét → vi phạm 3 mục → xử lý
```

---

## IV. Kết quả tạo ra

### 4.1 Kế hoạch nội dung 9 ảnh

| # | Vị trí ảnh | Thông tin truyền tải | Loại | Thành phần khung hình | Text trong ảnh | Số ký tự |
|---|---|---|---|---|---|---|
| **1** | Ảnh chính | Đây là một chiếc túi đựng thú cưng đi ra ngoài | Nhận diện | Nền trắng tinh, thân túi góc chính diện 3/4, dây đeo vai buông tự nhiên | **Không có chữ** (ML bắt buộc) | 0 |
| **2** | Ảnh điểm bán hàng chủ lực | Lưới thoáng khí ba mặt, thú cưng thở được và nhìn được | Thuyết phục | Trong túi có một chú chó nhỏ áp mặt nghiêng sát mặt lưới, ánh sáng xuyên qua lỗ lưới | `Ventilação em 3 lados` | 22 |
| **3** | Ảnh thông số kỹ thuật | Kích thước và tải trọng | Thông tin | Ảnh dàn trang nền trắng | Kích thước trong / tải trọng / trọng lượng / chất liệu vải | — |
| **4** | Ảnh bối cảnh A | Mang đi phòng khám thú y | Nhập vai | Chủ xách túi ở hành lang phòng khám, không lộ mặt (bàn tay + hậu cảnh) | (không có chữ) | 0 |
| **5** | Ảnh bối cảnh B | Đi lại ngắn bằng ô tô | Nhập vai | Túi đặt ở ghế sau ô tô, thú cưng trong túi thò đầu ra | (không có chữ) | 0 |
| **6** | Ảnh cận cảnh chi tiết | Móc khóa bên trong + khóa kéo hai đầu | Thuyết phục | Cận cảnh macro, móc kim loại và răng khóa kéo rõ nét | `Mosquetão interno incluso` | 25 |
| **7** | Ảnh kích thước/so sánh | 41×25×26 cm to cỡ nào | Xóa nghi ngờ | Đặt bàn tay và cẳng tay của một phụ nữ trưởng thành cạnh thân túi làm tham chiếu | Con số kích thước | — |
| **8** | Ảnh danh sách đóng gói | Có gì / không có gì | Ngăn tranh chấp | **Chụp thật** bày phẳng từ trên xuống | `Não incluso: comedouro` | 22 |
| **9** | Ảnh hậu mãi/bảo hành | Bảo hành và CSKH | Niềm tin | Ảnh dàn trang nền xám đậm | `3 meses · Garantia legal` | — |

**Phán đoán then chốt**: ảnh 1 trên ML bắt buộc **không có chữ nào** —— đây là khác biệt lớn nhất giữa case study này và bản Shopee.

### 4.2 Phương án theo khác biệt sàn

| Phương án | Sàn áp dụng | Ảnh chính | Ghi chú |
|---|---|---|---|
| **A** | **Mercado Livre** / Amazon | Nền trắng tinh, **không có chữ nào** | ✅ Case study này áp dụng |
| B | Shopee / TikTok Shop | Nền trắng + huy hiệu chữ (`3 Lados de Tela`) | Cách làm phổ biến để tăng CTR trên sàn |

⚠️ **Điểm xung đột**: nếu tải thẳng ảnh chính bản Shopee lên ML sẽ bị xử vi phạm (ảnh chính có chữ) → có thể bị gỡ hoặc bị yêu cầu chỉnh sửa. **Hai bộ creative bắt buộc quản lý riêng.**

### 4.3 Prompt ra ảnh (trích ba ảnh)

#### Ảnh 1 · Ảnh chính (bản ML, không có chữ)

```text
[SUBJECT] A soft-sided pet carrier bag, rectangular box shape with rounded corners,
light grey mélange polyester body with subtle blue trim accents,
carrying handle on top and adjustable shoulder strap draped naturally alongside.

[MATERIAL] 600D polyester with visible fine woven texture, matte finish,
two breathable mesh panels clearly distinguishable by their slight sheen,
metal zipper pulls with a slight brushed metallic reflection.

[COMPOSITION] Three-quarter front view, product centered, occupying approximately
70% of frame width, floating with no support, no props, generous even white margin
on all four sides.

[LIGHTING] Soft diffused studio lighting from upper-left at 45 degrees,
large softbox, minimal contact shadow directly beneath the product,
neutral white color temperature (5500K).

[BACKGROUND] Pure seamless white background, RGB 255,255,255,
completely shadowless outside the product area.

[STYLE] Professional e-commerce product photography, photorealistic,
high detail, sharp focus across the entire product, commercial catalog quality.

[PARAMETERS] 1:1 square aspect ratio, 1024x1024, no text or graphics anywhere.
```

**Negative Prompt**

```text
text of any kind, letters, numbers printed on the image, watermark, logo, badge,
ribbon, colored block, frame, border, background gradient, additional props,
accessories not included in the package, animals outside the carrier,
low resolution, blurry, oversaturated, distorted proportions, cluttered background
```

#### Ảnh 2 · Ảnh điểm bán hàng chủ lực

```text
[SUBJECT] The same grey and blue pet carrier bag with a small short-haired dog
(approximately 5 kg, brown and white) inside, head and front paws visible behind
the breathable mesh panel, looking calmly toward camera-left.

[MATERIAL] Mesh panel rendered with a visible hexagonal weave, light passing through
creating a soft glow; polyester body retains matte woven texture.

[COMPOSITION] Eye-level side view, slightly angled toward the viewer, carrier fills
75% of frame, dog's face positioned on the upper third, empty space on the right
reserved for text overlay.

[LIGHTING] Bright soft daylight, large window light from the right, gentle fill
from the left, soft natural shadows, warm-neutral tone (5200K).

[BACKGROUND] Seamless light beige studio background, subtle vertical gradient,
no visible floor line.

[STYLE] Warm lifestyle product photography, photorealistic, shallow depth of field
on background, crisp focus on the mesh and the dog's face.

[PARAMETERS] 1:1 square aspect ratio, 1024x1024, reserve right 35% for text overlay.
```

**Negative Prompt**

```text
watermark, logo, brand names, rain, water, wet fur, swimming pool, outdoor storm,
medical setting, hospital equipment, exaggerated dramatic lighting,
text rendered by the model, multiple animals, distressed animal, aggressive dog
```

> **`rain, water, wet fur` là bắt buộc phải thêm**: vải của sản phẩm này chỉ chống bắn nước, không chống nước. Trong khung hình có nước tức là ngầm ám chỉ sản phẩm chống nước —— thuộc quảng cáo sai sự thật (ứng với `À Prova d'Água` trong `forbidden_words`).

#### Ảnh 4 · Ảnh bối cảnh sử dụng A

```text
[SUBJECT] A person's hand and forearm carrying the grey pet carrier by its top
handle, walking through a bright veterinary clinic waiting area.
The carrier is the visual focus; the person is cropped at the shoulder — no face visible.

[MATERIAL] Same carrier as main image; clinic interior with light wood flooring,
white walls, simple bench seating blurred in the background.

[COMPOSITION] Over-the-shoulder perspective, carrier in sharp foreground at lower-left,
background corridor receding to upper-right, intentional blur on the surroundings.

[LIGHTING] Bright even indoor lighting, large windows out of frame to the left,
soft ambient bounce, neutral-cool tone (5000K).

[BACKGROUND] Clean modern veterinary clinic interior, uncluttered, no signage,
no readable text on walls.

[STYLE] Documentary lifestyle photography, photorealistic, natural candid feel,
moderate depth of field.

[PARAMETERS] 1:1 square aspect ratio, 1024x1024, no face visible, no text.
```

**Negative Prompt**

```text
visible human face, recognizable person, rain, water, swimming pool,
large breed dog, multiple animals, cluttered background, readable signage,
medical equipment, syringes, distressed pets, watermark
```

### 4.4 Đặc tả layout cho các vị trí ảnh không dùng AI

| Vị trí ảnh | Loại | Cách xử lý |
|---|---|---|
| Ảnh 3 | Ảnh dàn trang thông số | Làm bằng công cụ thiết kế. Nền trắng, 4 dòng thông số (`Dimensões internas 38 × 23 × 23 cm` / `Peso suportado até 8 kg` / `Peso do produto 1,2 kg` / `Poliéster 600D + tela respirável`), font không chân, chiều cao text chính ≥ 4% chiều cao ảnh |
| Ảnh 7 | Ảnh so sánh kích thước | **Chụp thật**: đặt bàn tay + cẳng tay của một phụ nữ trưởng thành cạnh thân túi, ghi `41 × 25 × 26 cm` (khớp từng ký tự với `spec_table.dimensoes_externas`) |
| Ảnh 8 | Ảnh danh sách đóng gói | **Bắt buộc chụp thật**: bày phẳng chụp từ trên xuống, gồm `1× Bolsa` / `1× Alça de ombro` / `1× Base rígida removível` / `1× Manual`, và ghi rõ ở góc ảnh **`Não incluso: comedouro e coleira`** |
| Ảnh 9 | Ảnh dàn trang hậu mãi | Làm bằng công cụ thiết kế. Nền xám đậm, gồm thời hạn bảo hành `3 meses`, phạm vi, kênh CSKH. **Không được tạo đồ họa nhái biểu tượng chính thức của ML** |

> **Vì sao ảnh 8 bắt buộc chụp thật**: ảnh danh sách đóng gói do AI tạo dễ "vẽ thừa một món" hoặc vẽ thiếu một món. Người mua nhận hàng, đối chiếu với ảnh thấy không khớp → đánh giá tiêu cực "thiếu phụ kiện" ngay. Đây là rủi ro dễ tránh nhất và cũng không đáng mạo hiểm nhất.

### 4.5 Kết quả quét tuân thủ hình ảnh

| Quy tắc | Vi phạm | Xử lý |
|---|---|---|
| I1 Giả mạo dấu chứng nhận | 0 | `certifications` trống, không tạo ảnh chứng nhận ✅ |
| I2 Giả mạo đánh giá / doanh số | 0 | Không có ảnh chụp màn hình đánh giá, nhãn góc doanh số nào ✅ |
| I3 Thương hiệu không được ủy quyền | **1** | `forbidden_words` đầu vào có `Gucci`, đã chặn trong toàn bộ Prompt và text trong ảnh; negative prompt của Prompt ảnh chính thêm `logo, brand names` |
| I4 Thông số không nhất quán | **1** | Bản nháp đầu của chú thích kích thước ảnh 7 ghi `41 x 25 x 26 cm` (chữ x nửa độ rộng), đã sửa thành `41 × 25 × 26 cm` (khớp từng ký tự với `spec_table`) |
| I5 Bối cảnh vượt phạm vi | **1** | Ảnh bối cảnh ban đầu dự kiến có "ký gửi hàng không", không nằm trong `usage_scope_confirmed` → xóa và ghi `[SCENE_DROPPED]` |
| I6 Chân dung người thật | 0 | Ảnh bối cảnh đều dùng bố cục không lộ mặt (bàn tay / bóng lưng) ✅ |
| I7 Từ ngữ tuyệt đối hóa | 0 | Text trong ảnh không có cách diễn đạt tuyệt đối hóa ✅ |
| I8 Ràng buộc ảnh so sánh | 0 | Vật tham chiếu của ảnh kích thước là bàn tay và cẳng tay (hình dạng chung) ✅ |

**Kết luận**: vi phạm 3 mục, đã xử lý xong toàn bộ, **quét lần hai không còn vi phạm**.

---

## V. Giao cho 05 Product Video Agent

```yaml
visual_tone_confirmed: "Suave e acolhedor — fundo claro, tons pastel, sem elementos agressivos"
hero_visual: "Thân túi góc chính diện 3/4, vải xám pha màu với chi tiết xanh dương, lưới thoáng khí ba mặt nhìn rõ"
key_visual_moments:
  - "Mặt nghiêng của thú cưng nhìn ra qua mặt lưới —— truyền tải trực quan 'thở được, nhìn được'"
  - "Cận cảnh móc kim loại bên trong —— truyền tải chi tiết an toàn"
  - "Trạng thái gấp phẳng —— truyền tải sự tiện lợi khi cất gọn"
forbidden_words:            # Chuyển tiếp cho 05, dùng để chặn cứng từ cấm trong phụ đề
  - "À Prova d'Água"
  - "Grau de Companhia Aérea"
  - "100% Seguro"
  - "Irresistível"
  - "Gucci"
```

---

## VI. Gợi ý tối ưu

| # | Gợi ý | Căn cứ |
|---|---|---|
| 1 | Ảnh 2 là ứng viên cho **khung hình đầu của video** | Thú cưng nhìn vào ống kính qua lớp lưới là khung hình giàu cảm xúc nhất của case study này |
| 2 | Đổi vật tham chiếu của ảnh 7 thành **vật thật đặt cùng khung** (ví dụ quả cân chuẩn 5 kg hoặc thú cưng phổ biến) | Tham chiếu bằng bàn tay ít giúp trả lời "đựng được chó cỡ nào", thắc mắc thật sự của người mua là tải trọng |
| 3 | Trường `Ficha Técnica` của ML **điền đầy đủ từng mục** | Dữ liệu thử nghiệm công khai cho thấy listing điền đầy đủ có xác suất nhận traffic tự nhiên cao hơn rõ rệt |
| 4 | Chụp bổ sung **ảnh trạng thái gấp gọn** làm ứng viên cho ảnh thứ 10 | ML cho phép 12 ảnh, gấp gọn cất giữ là điểm bán hàng khác biệt, hiện mới chỉ có trong text |
| 5 | Hai bộ creative ảnh chính **đặt tên và lưu riêng** (tiền tố `ML_` / `SP_`) | Tránh tải nhầm khiến ảnh chính ML vi phạm và bị gỡ |
| 6 | Sau khi lên sàn theo dõi đánh giá tiêu cực loại "kích thước không khớp" | Kiểm chứng ảnh 7 có thật sự xóa được nghi ngờ hay không |

---

## VII. Case study này chứng minh điều gì

| Kết luận | Bằng chứng |
|---|---|
| **Xung đột quy chuẩn giữa các sàn phải được xử lý tường minh** | ML không có chữ vs Shopee có điểm bán hàng, cùng một sản phẩm hai bộ ảnh chính |
| **Có những ảnh không thể tạo bằng AI** | Danh sách đóng gói ở ảnh 8 bắt buộc chụp thật, AI tạo = đánh giá tiêu cực thiếu phụ kiện |
| **Negative Prompt là công cụ phòng thủ** | `rain, water, wet fur` chặn đứng rủi ro quảng cáo sai sự thật kiểu "ám chỉ chống nước" |
| **Ảnh dàn trang thông tin ≠ ảnh AI** | Với ảnh 3/7/9, xuất "đặc tả layout" hữu ích hơn xuất Prompt |
| **Tính nhất quán của thông số phải đến cấp ký tự** | Chữ `x` nửa độ rộng và dấu `×` đều phải thống nhất —— người mua không để ý, nhưng nhất quán là mức sàn của sự chuyên nghiệp |
| **Cơ chế chặn thật sự được kích hoạt** | Bối cảnh "ký gửi hàng không" bị xóa vì không nằm trong `usage_scope_confirmed`, chứng minh bộ chặn R6/I5 có hiệu lực |

---

**File liên quan**: [Mô tả module](../README.md) · [Prompt kế hoạch 9 ảnh](../prompts/01_image_plan_9grid.md) · [Tạo Prompt ra ảnh](../prompts/02_image_prompt_generator.md) · [Template đầu ra](../templates/output_image_prompt_pack.yaml) · [Quy chuẩn trường dữ liệu sàn](../../../docs/02_Platform_Output_Spec.md)
