# Case study 01 · Patinete Elétrico 500W (xe scooter điện) · Toàn luồng end-to-end

> **Loại case study**: Case study chủ lực · Sản phẩm thật · Đã ẩn danh hóa
> **Module bao phủ**: 03 Listing Creative → 04 Product Image → 05 Product Video
> **Thị trường**: Shopee Brazil (chính) + Mercado Livre (đối chiếu)
> **SOP tương ứng**: 1.8 Bảng từ khóa · 3.3 Listing + 9 ảnh + cấu trúc trang chi tiết · 3.4 Khởi chạy nhiều link

**Vì sao đây là case study chủ lực**: SOP 1.8 dùng nó làm sản phẩm ví dụ cho công thức tiêu đề (nguyên văn: `Patinete Elétrico Adulto 500W 150kg com Banco Dobrável para Mobilidade Urbana`), tài liệu hướng dẫn xây dựng xếp nó vào 5 sản phẩm case study (Electric Scooter), và nó **tự nhiên trải dài qua cả ba module** — nhiều thông số (hợp làm ảnh thông số), có bối cảnh sử dụng mạnh (hợp làm video bối cảnh), có rủi ro an toàn rõ ràng (hợp để minh họa lớp bảo vệ tuân thủ).

---

## I. Bối cảnh sản phẩm

| Mục | Nội dung |
|---|---|
| Sản phẩm | Xe scooter điện 500W, dòng cho người lớn, có yên, gấp gọn được, giảm xóc trước sau |
| Thị trường | Brazil (Shopee BR là chủ lực, ML để đối chiếu) |
| Ngành hàng | Phương tiện di chuyển điện |
| Định vị | SKU chủ lực |
| Tông hình ảnh | Mạnh mẽ, năng động kiểu đô thị, tông lạnh |

**Đặc thù ngành hàng** (quyết định toàn bộ chiến lược nội dung):

| Đặc thù | Ảnh hưởng |
|---|---|
| Nhiều thông số (công suất/quãng đường/tải trọng/lốp/giảm xóc…) | Bắt buộc làm ảnh thông số, và không được dồn hết vào một chỗ |
| Người mua sợ nhất "khai khống tải trọng", "khai khống quãng đường" | Trang chi tiết bắt buộc giải thích điều kiện thử nghiệm |
| Liên quan an toàn (phanh, đèn, đi đêm) | **Ngành hàng dày đặc lằn ranh đỏ về tuân thủ nhất** |
| Brazil có quy định địa phương về việc xe scooter điện lưu thông trên đường | Mô tả bối cảnh không được cam kết "được phép lưu thông hợp pháp" |

---

## II. Phân tích thị trường (bản rút gọn)

Bản chi tiết do 01 Market Research Agent đảm nhận (Phase 2). Ở đây chỉ đưa kết luận cần cho case study:

| Khía cạnh | Kết luận | Ảnh hưởng đến nội dung |
|---|---|---|
| Dải giá | Khoảng mục tiêu `R$ 1.800 – R$ 2.600` | Từ khóa thông số trong tiêu đề được cấu hình theo phân khúc giá này |
| Cấu hình phổ biến | 350–500W, 10–15Ah, lốp 8–10 inch, tải trọng 100–150kg | Tiêu đề bắt buộc chứa `500W` `150kg` (tạo khác biệt với đối thủ 350W) |
| Điểm yếu của đối thủ | Đa số đối thủ **không ghi điều kiện thử quãng đường**, không ghi chi tiết giảm xóc | Trang chi tiết của mình nói thật kỹ hai điểm này |
| Nguyên nhân hoàn hàng cao | Tải trọng/quãng đường không như kỳ vọng, khó lắp ráp | Đoạn lưu ý trên trang chi tiết bắt buộc phải bao quát |
| Từ khóa | Từ khóa tần suất cao tập trung ở `Patinete Elétrico` + `Adulto` + công suất + `Dobrável` + `Mobilidade Urbana` | Cấu trúc tiêu đề bám thẳng theo công thức SOP |

---

## III. Module 03 · Listing Creative

### 3.1 Đầu vào (trích)

```yaml
platform: shopee
target_market: Brazil
mode: single
product_name: "Patinete Elétrico"
category: "Phương tiện di chuyển điện"

spec_table:
  potencia: "500 W"
  bateria: "12 Ah / 48 V"
  autonomia: "até 35 km"
  velocidade_max: "30 km/h"
  capacidade_carga: "150 kg"
  pneu: "8 polegadas, câmara de ar"
  freio: "Freio a disco dianteiro + freio elétrico traseiro"
  suspensao: "Suspensão dianteira e traseira"
  banco: "Banco removível com haste ajustável"
  dobravel: "Sim — sistema de dobra em 3 segundos"
  tempo_recarga: "5 a 6 horas"
  iluminacao: "Farol LED dianteiro + lanterna traseira"
  peso_produto: "18 kg"
  peso_max_usuario: "150 kg"
  garantia: "6 meses (motor e bateria)"

usage_scope_confirmed:
  - "Deslocamento urbano em vias planas e pavimentadas"
  - "Lazer em parques e ciclovias"
  - "Trajeto casa-trabalho em distâncias curtas"

forbidden_words:            # Do bước quét tuân thủ tạo ra
  - "Anda a 60 km/h"        # Sai thông số (thực tế 30 km/h)
  - "Autonomia de 60 km"    # Sai thông số (thực tế 35 km)
  - "Pode Andar em Qualquer Via"  # Rủi ro tuân thủ: quy định lưu thông khác nhau theo địa phương, không được cam kết
  - "O Melhor Patinete do Brasil" # Từ ngữ tuyệt đối hóa
  - "Xiaomi"                # Thương hiệu chưa được cấp phép
```

### 3.2 Phân loại từ khóa thành 7 nhóm (trích)

| Nhóm | Số từ | Từ tiêu biểu |
|---|---|---|
| Từ khóa lõi | 4 | `Patinete Elétrico`, `Scooter Elétrico`, `Patinete Adulto` |
| Từ khóa thông số | 12 | `500W`, `150kg`, `12Ah`, `8 Polegadas`, `30 km/h` |
| Từ khóa nhóm khách hàng | 4 | `Adulto`, `Unissex`, `Iniciante` |
| Từ khóa tính năng | 10 | `Dobrável`, `com Banco`, `com Suspensão`, `Freio a Disco` |
| Từ khóa bối cảnh | 6 | `Mobilidade Urbana`, `Ciclovia`, `Parque`, `Casa-Trabalho` |
| Từ khóa phụ kiện | 5 | `Bateria`, `Carregador`, `Banco Removível` |
| **Từ khóa rủi ro** | **5** | ⛔ Xem `forbidden_words` |

### 3.3 Tiêu đề (số ký tự đo thực tế)

| # | Tiêu đề | Số ký tự | Trọng tâm |
|---|---|---|---|
| **A** | `Patinete Elétrico Adulto 500W 150kg com Banco Dobrável e Suspensão para Mobilidade Urbana` | **89/120** | Dẫn dắt bằng thông số ✅ Đề xuất |
| B | `Patinete Elétrico Adulto 500W 150kg Dobrável com Banco para Mobilidade Urbana e Lazer` | **85/120** | Dẫn dắt bằng bối cảnh |
| C | `Patinete Elétrico Adulto 500W 150kg com Banco Dobrável Pneus 8 Polegadas Mobilidade Urbana` | **90/120** | Dẫn dắt bằng tính năng |

**Khác biệt so với ví dụ gốc trong SOP**:

| | Tiêu đề | Số ký tự |
|---|---|---|
| Ví dụ gốc SOP | `Patinete Elétrico Adulto 500W 150kg com Banco Dobrável para Mobilidade Urbana` | **77** |
| Phương án A của case study | Thêm `e Suspensão` vào ví dụ gốc (điểm bán hàng tạo khác biệt mà ví dụ gốc SOP chưa có) | **89** |

> Ví dụ gốc SOP chỉ dùng 77/120 ký tự, **còn 43 ký tự chưa dùng**. Phương án A của case study này bổ sung điểm「giảm xóc kép」— điểm mà đối thủ thường không nhấn mạnh — vào tiêu đề. **Bổ sung điểm bán hàng thật mà không nhồi nhét mới là cách tối ưu tiêu đề đúng; thêm `Novo` `Promoção` cho đủ ký tự mới là nhồi từ khóa.**

### 3.4 Trang chi tiết 7 đoạn (sơ đồ cấu trúc)

| Đoạn | Nội dung chính | Xử lý đặc thù của case study |
|---|---|---|
| 1 · Lời chào | Định vị sản phẩm trong một câu | — |
| 2 · Điểm bán hàng lõi | 5 điểm, mỗi điểm có số liệu chứng minh | Lõi: `động cơ 500W + tải trọng 150kg` |
| 3 · Bối cảnh sử dụng | 3 bối cảnh | ⚠️ **Chỉ ghi "vias planas e pavimentadas"**, không cam kết đi được mọi loại đường |
| 4 · Thông số chi tiết | Bảng, 14 mục | Quãng đường bắt buộc ghi điều kiện thử nghiệm |
| 5 · Hậu mãi | 6 tháng (động cơ + pin) | Ghi rõ phạm vi |
| 6 · Lưu ý | Dựa trên `review_insights` | Xem bên dưới |
| 7 · Thẻ từ khóa | 10–15 thẻ | Không dính từ khóa rủi ro nào |

**Nguồn nội dung của đoạn 6 · Lưu ý** (đoạn then chốt):

```text
- A autonomia de até 35 km foi medida com piloto de 70 kg, em piso plano,
  velocidade média de 20 km/h e temperatura de 25 °C. Autonomia varia com
  peso do piloto, relevo, velocidade e calibragem dos pneus.
- A capacidade máxima é de 150 kg (piloto + bagagem).
- O tempo de recarga completo é de 5 a 6 horas.
- Regras de circulação de patinetes elétricos variam por cidade e estado.
  Verifique a legislação local antes de circular em vias públicas.
- É obrigatório o uso de capacete.
- O produto vem parcialmente montado; a montagem final leva cerca de 15 minutos.
```

> **Ba mục cuối là phần giá trị nhất của case study này**:
> -「Quy định lưu thông khác nhau theo địa phương, vui lòng tự kiểm tra」— **vừa né được rủi ro tuân thủ, vừa trông chuyên nghiệp**. Ghi thẳng "được phép lưu thông hợp pháp" là nguy hiểm.
> -「Bắt buộc đội mũ bảo hiểm」— nhắc nhở an toàn, đồng thời giảm tranh chấp hậu mãi.
> -「Cần tự lắp ráp một phần」— **khó lắp ráp là nguyên nhân hoàn hàng tần suất cao của loại sản phẩm này**, nói trước giúp giảm hoàn hàng trực tiếp.
>
> Hai mục đầu thì trực tiếp chặn trước hai loại đánh giá tiêu cực hay gặp là "khai khống quãng đường" và "khai khống tải trọng".

### 3.5 Phân tầng điểm bán hàng và các trường bàn giao

```yaml
core_selling_point: "Motor de 500W com capacidade para 150 kg — sobe ladeiras leves com estabilidade"

secondary_points:
  - "Suspensão dianteira e traseira — menos impacto em piso irregular"
  - "Dobrável em 3 segundos — cabe no porta-malas"
  - "Banco removível com haste ajustável"
  - "Freio a disco dianteiro + freio elétrico traseiro"
  - "Farol LED dianteiro e lanterna traseira"
  - "Autonomia de até 35 km (condições de teste no item 6 da descrição)"

forbidden_words: [giống 5 mục phía trên trong spec_table]

visual_tone_hint: "Urbano e dinâmico — luz natural de fim de tarde, asfalto e ciclovia, tons frios com destaque no produto"

usage_scope_confirmed:
  - "Deslocamento urbano em vias planas e pavimentadas"
  - "Lazer em parques e ciclovias"
  - "Trajeto casa-trabalho em distâncias curtas"

title_final: "Patinete Elétrico Adulto 500W 150kg com Banco Dobrável e Suspensão para Mobilidade Urbana"
```

### 3.6 Kết quả quét tuân thủ

| Quy tắc | Số lần dính | Xử lý |
|---|---|---|
| R1 Từ ngữ tuyệt đối hóa | 1 | `O Melhor Patinete do Brasil` → xóa |
| R2 Từ khóa thương hiệu chưa cấp phép | 1 | `Xiaomi` → xóa |
| R3 Khai khống thông số | **3** | `60 km/h` `quãng đường 60 km` `lẫn model 350W` → xóa hết và ghi `[PARAM_DROPPED]` |
| R4 Từ khuyến mãi trong tiêu đề | 1 | Bản nháp tiêu đề có `Promoção` → chuyển xuống đoạn 1 của trang chi tiết |
| R5 Diễn đạt nhạy cảm | 1 | `Pode Andar em Qualquer Via` → đổi thành "vui lòng kiểm tra quy định địa phương" |
| R6 Bối cảnh vượt phạm vi | 1 | Đầu vào có `Trilhas e Off-Road` không nằm trong `usage_scope` → xóa và ghi `[SCENE_DROPPED]` |
| R7 Bằng chứng giả | 0 | — |

**Kết luận**: dính 8 mục, trong đó R3 có 3 mục rủi ro cao. Đã xử lý hết, quét lần hai không dính mục nào.

> **R3 dính 3 lần là điểm đáng chú ý nhất của case study này.** Khai khống thông số thường không phải cố tình bịa, mà là do **bảng từ khóa lẫn từ khóa thông số của đối thủ** (đối thủ ghi 60km/h, quãng đường 60km); nếu lấy dùng thẳng thì thành khai khống. Điều này chứng minh `spec_table` cần thiết phải là nguồn số liệu duy nhất.

---

## IV. Module 04 · Product Image

### 4.1 Kế hoạch nội dung 9 ảnh

| # | Vị trí ảnh | Thông tin truyền tải | Chữ trên ảnh | Số ký tự |
|---|---|---|---|---|
| 1 | **Ảnh chính** | Toàn thân xe, góc 3/4 chếch trước | **Không chữ** (bản ML) / `500W · 150kg` (bản Shopee) | 0 / 14 |
| 2 | Ảnh điểm bán hàng lõi | Động cơ 500W + tải trọng 150kg | `Motor 500W · Suporta 150 kg` | 28 |
| 3 | Ảnh thông số | Trực quan hóa thông số chính | Công suất/pin/quãng đường/tốc độ/tải trọng | — |
| 4 | Ảnh bối cảnh A | Đi lại trong thành phố | `Mobilidade urbana` | 17 |
| 5 | Ảnh bối cảnh B | Gấp gọn cho vào cốp xe | `Dobra em 3 segundos` | 19 |
| 6 | Ảnh chi tiết | Cận cảnh giảm xóc + phanh đĩa | `Suspensão + freio a disco` | 25 |
| 7 | Ảnh kích thước/so sánh | Kích thước cả xe + kích thước khi gấp | Ghi chú số đo | — |
| 8 | Ảnh danh sách đóng gói | **Chụp thật** bày phẳng | `Não incluso: capacete` | 21 |
| 9 | Ảnh hậu mãi/bảo hành | 6 tháng động cơ và pin | `6 meses · motor e bateria` | 26 |

### 4.2 Xử lý xung đột giữa các sàn

| Phương án | Sàn | Ảnh chính |
|---|---|---|
| **A** | Mercado Livre / Amazon | Nền trắng tinh + **không chữ** (ML cấm chữ trên ảnh chính) |
| **B** | Shopee / TikTok Shop | Nền trắng + `500W · 150kg` (tăng CTR trong sàn) |

⚠️ **Không dùng chung được**. Ảnh chính ML có chữ sẽ bị tính là vi phạm.

### 4.3 Prompt tạo ảnh (ảnh 2 · ảnh điểm bán hàng lõi)

```text
[SUBJECT] A black and dark-grey adult electric scooter with a removable padded
seat, standing upright on flat asphalt. A slender LED headlight is on.
The deck is wide and textured with grip tape; 8-inch pneumatic tires are clearly visible.

[MATERIAL] Matte powder-coated aluminum frame with subtle brushed metal accents
on the folding hinge; rubber tires with visible tread; textured grip tape on the deck.

[COMPOSITION] Three-quarter front-left view, scooter occupying 70% of frame height,
slightly low camera angle to emphasize stability and power, clean empty space on the
right third reserved for text overlay.

[LIGHTING] Late afternoon directional natural light from camera-right, long soft
shadow cast to the left on the asphalt, warm-neutral tone (4800K).

[BACKGROUND] Smooth clean asphalt with a subtle cyclist lane line blurred in the
far background, shallow depth of field, horizon line below the frame center.

[STYLE] Commercial e-mobility advertising photography, photorealistic, crisp focus
on the scooter, dynamic but stable mood.

[PARAMETERS] 1:1 square aspect ratio, 1024x1024, reserve right 35% for text overlay.
```

**Negative Prompt**

```text
text rendered by the model, watermark, logo, brand names, rider, human figure,
helmet, exaggerated speed blur, sparks, off-road mud, wet road, rain,
damaged scooter, broken parts, low resolution, distorted proportions,
cluttered background, traffic, visible license plate
```

> **`rider, human figure` là bắt buộc phải thêm**: nếu ảnh chính có người, sự chú ý sẽ bị kéo khỏi sản phẩm, và trên ML có thể bị coi là "hiển thị thứ không được bán".

### 4.4 Quét tuân thủ hình ảnh (các mục dính trong case study này)

| Quy tắc | Số lần dính | Xử lý |
|---|---|---|
| I1 Logo chứng nhận giả | **1** | Bản nháp ảnh 9 định thêm logo `INMETRO` → sản phẩm chưa có chứng nhận, **xóa**, đổi thành chữ mô tả bảo hành |
| I2 Đánh giá / số lượng đã bán giả | 0 | — |
| I3 Thương hiệu chưa cấp phép | 1 | Thêm `logo, brand names` vào Negative Prompt để chặn `Xiaomi` |
| I4 Thông số không nhất quán | **2** | Bản nháp ảnh 3 ghi `35km` / `30km/h` (không có dấu cách) → thống nhất thành `35 km` / `30 km/h` |
| I5 Bối cảnh vượt phạm vi | **1** | Phương án gốc ảnh 4 là "bối cảnh đường núi off-road" → không nằm trong `usage_scope`, đổi thành bối cảnh đi lại trong thành phố |
| I6 Chân dung người thật | 0 | Ảnh bối cảnh dùng bóng/lưng người lái, không lộ khuôn mặt nhận diện được |
| I7 Từ ngữ tuyệt đối hóa | 0 | — |
| I8 Ràng buộc ảnh so sánh | **1** | Bản nháp ảnh 7 định so sánh chung khung với một đối thủ → đổi thành so sánh với **đường viền kích thước thân xe chung chung** |

**Kết luận**: dính 6 mục, đã xử lý hết.

> **I1 và I5 là hai mục thể hiện rõ nhất giá trị của lớp bảo vệ tuân thủ**: một mục suýt tạo ra logo chứng nhận giả, một mục suýt dùng "bối cảnh off-road" để ngầm ý sản phẩm làm được điều nó không làm được. **Hai loại vấn đề này cực kỳ phổ biến ở ngành hàng phương tiện di chuyển điện, và đều thuộc nhóm rủi ro cao.**

---

## V. Module 05 · Product Video

### 5.1 Chọn hook

| # | Loại | Hook | Lựa chọn |
|---|---|---|---|
| A | Đánh thẳng vào nỗi đau | `Trânsito parado e você ainda de ônibus?` | ✅ Chọn |
| B | Ngược thường thức | `Chega ao trabalho sem suar.` | |
| C | Nhập vai bối cảnh | `Seis quilômetros. Doze minutos.` | |

### 5.2 Storyboard (bản 30s, trích)

| Cảnh | Thời lượng | Hình ảnh | Chuyển động máy | Phụ đề (xem không tiếng) |
|---|---|---|---|---|
| 1 | 0–3s | Làn xe kẹt cứng, máy quay lia từ dòng xe sang làn xe đạp trống bên cạnh | Lia ngang | `Trânsito parado?` |
| 2 | 3–7s | Scooter lướt vào làn xe đạp từ bên phải khung hình, chạy đều | Bám theo bên hông | `Patinete Elétrico 500W` |
| 3 | 7–12s | Đoạn lên dốc, xe leo ổn định, tiếng động cơ êm | Bám theo góc thấp | `Sobe ladeiras leves` |
| 4 | 12–17s | Minh họa tải trọng: người lái (lưng/bóng) + phụ đề ghi `150 kg` | Trung cảnh cố định | `Suporta 150 kg` |
| 5 | 17–22s | Thao tác gấp: xong trong 3 giây, cho vào cốp ô tô | Cố định từ trên xuống | `Dobra em 3 segundos` |
| 6 | 22–26s | Cận cảnh giảm xóc và phanh đĩa | Macro cố định | `Suspensão + freio a disco` |
| 7 | 26–30s | Dừng hình sản phẩm + thẻ thông số | Tĩnh | `Confira o link` |

**7 cảnh / 30s** ✅

### 5.3 Xử lý cảnh quay người thật (cảnh 4)

```markdown
### Cảnh 4 · 12–17s · [Cảnh quay người thật — không tạo AI Prompt]

**Chỉ dẫn quay**
- Vị trí máy: góc thấp, trung cảnh, hơi ngước lên
- Bố cục: **lưng hoặc bóng người lái, không lộ mặt**
- Động tác: chạy thẳng đều, thân trên thẳng
- Lưu ý: **bắt buộc đội mũ bảo hiểm** (tuân thủ an toàn + nội dung chân thực), cần ký giấy cho phép sử dụng hình ảnh hoặc dùng bóng người
- Thời lượng: 5s

**Phương án AI thay thế**
- Dùng bố cục bóng người ngược sáng
- Prompt: Silhouette of an adult riding an electric scooter from behind at dusk,
  wearing a helmet, riding on a flat asphalt bike lane, low camera angle,
  warm golden backlight, no facial features visible, photorealistic, gentle forward motion
```

### 5.4 Kịch bản lồng tiếng (thời lượng đo thực tế)

| Cảnh | Lời lồng tiếng | Số từ | Lũy kế | Thời lượng ước tính |
|---|---|---|---|---|
| 1 | `Trânsito parado e você ainda de ônibus?` | 7 | 7 | 2,8s |
| 2 | `Este patinete tem motor de quinhentos watts.` | 7 | 14 | 5,6s |
| 3 | `Sobe ladeiras leves sem esforço.` | 5 | 19 | 7,6s |
| 4 | `Suporta até cento e cinquenta quilos.` | 6 | 25 | 10,0s |
| 5 | `Dobra em três segundos e cabe no porta-malas.` | 8 | 33 | 13,2s |
| 6 | `Suspensão nas duas rodas e freio a disco na frente.` | 9 | 42 | 16,8s |
| 7 | `Patinete Elétrico 500W. Confira o link.` | 6 | **48** | **19,2s** |

> Bản 30s chỉ dùng 48 từ (19,2s) → **để lại nhiều khoảng lặng**. Với ngành hàng phương tiện di chuyển điện thì điều này phù hợp: **lời thoại dồn dập sẽ làm giảm cảm giác "ổn định, đáng tin cậy"**, nhịp chậm + khoảng lặng hợp với tông sản phẩm hơn.
> Nếu sàn yêu cầu lấp đầy thời lượng, hãy bổ sung **hình ảnh** chứ đừng bổ sung **lời thoại**.

### 5.5 Quét tuân thủ video (các mục dính trong case study này)

| Quy tắc | Số lần dính | Xử lý |
|---|---|---|
| V1 Bằng chứng giả | 0 | — |
| V2 Thông số không nhất quán | **1** | Bản nháp phụ đề ghi `500W` không có dấu cách → đổi thành `500 W` |
| V3 Bối cảnh vượt phạm vi | **1** | Cảnh 3 ban đầu là "leo dốc off-road" → không nằm trong `usage_scope`, đổi thành "dốc thoải đường đô thị (urban)" |
| V4 Từ ngữ tuyệt đối hóa | 0 | — |
| V5 Thương hiệu chưa cấp phép | 0 | — |
| V6 Chân dung người thật | **1** | Cảnh 4 quay chính diện → đổi thành lưng/bóng người |
| V7 Minh họa hành vi nguy hiểm | **1** | Bản nháp có "buông hai tay để khoe thăng bằng" → **xóa** (thao tác nguy hiểm) |
| V8 Bản quyền âm thanh | 0 | Đã ghi chú yêu cầu được phép dùng thương mại |

> **V7 cần đặc biệt chú ý**: cảnh thao tác nguy hiểm là thứ dễ bị "tiện tay thêm vào" nhất trong loại nội dung này — người làm video sẽ thấy "buông hai tay" rất ngầu, dễ viral. Nhưng nó vừa vi phạm vừa truyền đi hình mẫu nguy hiểm. **Quy tắc này bắt buộc phải chặn cứng.**

---

## VI. Đối chiếu giữa các sàn: rút tiêu đề từ 120 ký tự xuống 60 ký tự

| Sàn | Tiêu đề | Số ký tự |
|---|---|---|
| Shopee | `Patinete Elétrico Adulto 500W 150kg com Banco Dobrável e Suspensão para Mobilidade Urbana` | **89/120** |
| **Mercado Livre** | `Patinete Elétrico Adulto 500W 150kg com Banco Dobrável` | **54/60** |

**Quá trình cắt từ cho ML** (theo thứ tự ưu tiên cắt từ của ML: từ khóa bối cảnh → từ khóa nhóm khách hàng → từ khóa chính và thông số lõi không bao giờ cắt):

| Bước | Thao tác | Thành phần bị cắt | Số ký tự còn lại |
|---|---|---|---|
| 1 | Điểm xuất phát | — | 89 |
| 2 | Cắt từ khóa bối cảnh | `Mobilidade Urbana`, `para` | 69 |
| 3 | Cắt từ khóa tính năng đi kèm | `e Suspensão` | 57 |
| 4 | Thêm lại từ nối cần thiết | Giữ `com` | **54** |

**Được giữ lại**: `Patinete Elétrico` (từ khóa lõi) + `Adulto` (từ khóa nhóm khách hàng, cần thiết trên ML) + `500W` `150kg` (thông số lõi) + `com Banco Dobrável` (tính năng lõi).
**Không cắt bất kỳ thông số lõi nào** — đúng với nguyên tắc cắt từ của SOP.

---

## VII. Kiểm tra tính nhất quán giữa các module

Đây là bước đáng sao chép nhất của case study này.

| Trường | 03 Listing | 04 Image | 05 Video | Nhất quán |
|---|---|---|---|---|
| Công suất | `500 W` | `500 W` | `500 W` | ✅ |
| Tải trọng | `150 kg` | `150 kg` | `150 kg` | ✅ |
| Quãng đường | `até 35 km` | `35 km` | Không nhắc đến | ✅ |
| Thời gian gấp | `3 segundos` | `3 segundos` | `3 segundos` | ✅ |
| Bảo hành | `6 meses (motor e bateria)` | `6 meses · motor e bateria` | Không nhắc đến | ✅ |
| Điểm bán hàng lõi | `Motor de 500W … 150 kg` | Chữ trên ảnh 2 cùng nguồn | Cảnh 2/4 cùng nguồn | ✅ |
| Tông hình ảnh | `Urbano e dinâmico` | Từ ngữ trong Prompt ở 4.3 nhất quán | Hình ảnh storyboard nhất quán | ✅ |
| Từ cấm bị dính | 5 mục | 5 mục chung + 1 mục bối cảnh | Như trên | ✅ |

**Phát hiện 4 chỗ không nhất quán (đã sửa)**:

| # | Vấn đề | Vị trí | Sửa |
|---|---|---|---|
| 1 | `35km` không có dấu cách | Bản nháp ảnh 3 | → `35 km` |
| 2 | `500W` không có dấu cách | Bản nháp phụ đề video | → `500 W` |
| 3 | Cách diễn đạt bảo hành không thống nhất | Ảnh 9 so với trang chi tiết | Thống nhất thành `6 meses · motor e bateria` |
| 4 | Mô tả tông hình ảnh không nhất quán | 04 ghi "tông ấm", storyboard 05 ghi "tông lạnh" | Thống nhất theo `Urbano e dinâmico` của 03 (tông lạnh + ánh sáng ấm) |

> **Mục 4 nói lên vấn đề rõ nhất**: cùng một sản phẩm, ảnh dùng tông ấm, video dùng tông lạnh, nhìn riêng thì đều đẹp, đặt cạnh nhau thì thấy chắp vá. **Tông hình ảnh bắt buộc do 03 định nghĩa, 04 và 05 cùng tuân theo.**

---

## VIII. Đề xuất tối ưu

| # | Đề xuất | Căn cứ |
|---|---|---|
| 1 | Dùng 3 tiêu đề A/B/C để **test nhiều link** (SOP 3.4 cách 2) | Ba tiêu đề có trọng tâm khác nhau, nhanh chóng biết hướng nào có CTR cao hơn |
| 2 | Ưu tiên quay **cảnh lên dốc** làm nội dung sáng tạo chủ lực cho video | "Leo được dốc" là bằng chứng trực quan khó bị đối thủ bắt chước nhất của loại sản phẩm này |
| 3 | Quay bổ sung **một cảnh dài trọn vẹn 3 giây quá trình gấp xe** | Dựng được nhiều phiên bản, làm được bản dọc, và cũng là ảnh bổ sung cho trang chi tiết |
| 4 | Đưa cả「điều kiện thử quãng đường」vào ảnh thông số số 3 | Chặn trước trực tiếp loại đánh giá tiêu cực "khai khống quãng đường" |
| 5 | Sau khi lên sàn, theo dõi 3 loại đánh giá tiêu cực「tải trọng」「quãng đường」「lắp ráp」 | Kiểm chứng phần nói trước ở đoạn 6 có thực sự giảm hoàn hàng không |
| 6 | **Điền đầy đủ từng mục** `Ficha Técnica` trên ML (nhập hết 14 thông số) | Listing điền đầy đủ được ưu tiên xếp hạng |
| 7 | Có chứng nhận INMETRO rồi mới bổ sung ảnh chứng nhận | Hiện tại không tạo là đúng — chứng nhận bịa đặt là vi phạm rủi ro cao |

---

## IX. Case study này chứng minh điều gì

| Kết luận | Bằng chứng |
|---|---|
| **Xâu chuỗi end-to-end là khả thi** | `core_selling_point` của 03 được 04 và 05 dùng trực tiếp, không thất thoát thông tin |
| **`spec_table` là nguồn số liệu duy nhất là cần thiết** | R3 dính 3 lần — bảng từ khóa lẫn thông số 60km/h, 60km của đối thủ, không có `spec_table` sẽ thành khai khống |
| **Lớp bảo vệ tuân thủ dính nhiều nhất ở ngành hàng phương tiện di chuyển điện** | 03 dính 8 mục, 04 dính 6 mục, 05 dính 4 mục, trong đó nhiều mục rủi ro cao |
| **Công thức tiêu đề SOP dùng được ngay** | Ví dụ gốc SOP 77 ký tự, case study này bổ sung điểm bán hàng thật nâng lên 89 ký tự, không nhồi nhét |
| **Sang sàn khác bắt buộc rút gọn lại** | 89 → 54 ký tự, cắt từ có thứ tự ưu tiên rõ ràng, không mất thông số lõi nào |
| **Tông hình ảnh bắt buộc do thượng nguồn định nghĩa** | Chỗ không nhất quán thứ 4 phát hiện được chính là do 04 và 05 tự đặt tông riêng |
| **Cảnh nguy hiểm sẽ bị tiện tay thêm vào** | "Buông hai tay" bị V7 chặn là ví dụ điển hình về xung đột giữa sức hút nội dung và tuân thủ |
| **Đoạn lưu ý là đầu ra có lợi nhất** | Điều kiện thử quãng đường, giải thích tải trọng, hướng dẫn lắp ráp, nhắc đội mũ bảo hiểm — cả bốn đều trực tiếp chặn trước các nguyên nhân hoàn hàng cao |

---

**Case study liên quan**: [Case study 02 · Thermal Bag](../02_Thermal_Bag/) (vòng khép kín chỉnh sửa lại ở chế độ iterate) · [Power Bank](../../Agents/03_Listing_Creative_Agent/examples/powerbank_20000mah.md) · [Pet Carrier](../../Agents/04_Product_Image_Agent/examples/pet_carrier.md) · [Air Fryer](../../Agents/05_Product_Video_Agent/examples/air_fryer.md)

**Tài liệu liên quan**: [Phân rã kiến trúc](../../docs/00_Architecture_SOP_to_Agent.md) · [Quy chuẩn trường theo sàn](../../docs/02_Platform_Output_Spec.md) · [Lằn ranh đỏ tuân thủ](../../docs/03_Compliance_Guard.md) · [Checklist tự kiểm tra](../../docs/04_Result_Checklist.md)
