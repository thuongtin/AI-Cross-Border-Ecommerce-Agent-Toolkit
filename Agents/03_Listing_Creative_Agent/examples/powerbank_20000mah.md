# Case study · Carregador Portátil 20000mAh 45W (Shopee Brazil)

> **Loại case study**: sản phẩm thật · đã ẩn danh (không có tên shop, không có tài khoản, không có tên thương hiệu chưa ủy quyền)
> **Module sử dụng**: 03 Listing Creative Agent
> **SOP tương ứng**: 1.8 Bảng từ khóa · 3.3 Xây dựng Listing · 3.6 Sửa lại khi quảng cáo không chạy

---

## 1. Bối cảnh sản phẩm

| Mục | Nội dung |
|---|---|
| Sản phẩm | Sạc dự phòng sạc nhanh 20000mAh 45W, có màn hình số, 3 cổng ra |
| Thị trường | Brazil (Shopee BR) |
| Ngành hàng | Pin / sạc |
| Định vị | SKU kéo traffic, sản phẩm chủ lực chạy quảng cáo |
| Bối cảnh đăng bán | Khởi động sản phẩm mới, cần một bộ Listing đủ sức kéo CTR |

**Vì sao chọn case study này**: ngành hàng sạc dự phòng trên Shopee Brazil cạnh tranh gay gắt, là ngành hàng điển hình mà "khác biệt trong cách viết tiêu đề thể hiện trực tiếp lên CTR"; đồng thời sản phẩm có **đánh giá tiêu cực loại hiểu lầm** rõ ràng (người mua tưởng có kèm cáp sạc), có thể dùng để minh họa vòng khép kín (closed loop) "đánh giá → trang chi tiết".

---

## 2. Phía đầu vào (trích)

Template đầy đủ xem tại [`../templates/input_product_brief.md`](../templates/input_product_brief.md).

```yaml
platform: shopee
target_market: Brazil
mode: single

product_name: "Carregador Portátil"
category: "Pin / sạc"
```

### spec_table (trích)

| Key thông số | Giá trị |
|---|---|
| `capacidade` | `20000 mAh` |
| `potencia_saida` | `45 W` |
| `portas` | `2× USB-A + 1× USB-C` |
| `voltagem_entrada` | `100–240 V` |
| `peso` | `380 g` |
| `dimensoes` | `14,2 × 6,8 × 2,8 cm` |
| `display` | `Display digital de bateria` |
| `tempo_recarga` | `≈ 4 h com carregador de 45 W` |
| `garantia` | `6 meses (defeito de fabricação)` |
| `certificacoes` | `(để trống — chưa có ANATEL, không điền thì không bịa)` |

### package_content

```yaml
- "1× Carregador Portátil 20000mAh 45W"
- "1× Cabo USB-C 30 cm"
- "1× Manual de instruções em português"
```

### usage_scope

```yaml
- "Viagem e deslocamentos diários"
- "Trabalho remoto / home office"
- "Emergência durante o dia fora de casa"
```

### selling_points_input (có cách nói phóng đại, chờ viết lại)

```yaml
- "Bateria gigante, dura dias inteiros sem precisar de tomada"
- "Carrega ultra rápido, mais rápido que carregador comum"
- "Serve para qualquer celular"
- "Design moderno e compacto, cabe no bolso"
- "Seguro, não esquenta nem incha"
```

### review_insights

```yaml
- type: loại hiểu lầm
  content: "Đánh giá của người mua có câu 'esperava que viesse o cabo longo', tưởng có kèm cáp dài"
  action: "Ghi rõ cabo incluso tem 30 cm trong đoạn Lưu ý của trang chi tiết"
- type: loại hiểu lầm
  content: "Người mua tưởng sạc được cho laptop"
  action: "Ghi rõ scope ở đoạn Lưu ý và đoạn thông số: celular e tablet"
```

### brand_authorization

```yaml
brand_authorization: []      # không có bất kỳ ủy quyền thương hiệu nào
```

---

## 3. Quy trình AI xử lý

```text
[Step 1] 00_system.md                    → nạp vai trò, quy tắc sàn (120 ký tự), quy tắc đầu ra PT-BR, chốt chặn tuân thủ
[Step 2] 01_keyword_to_title.md          → gộp và loại trùng 84 từ của 3 bảng → chia 7 nhóm → 3 tiêu đề dự phòng
[Step 3] 02_description_builder.md       → trang chi tiết 7 đoạn + phân tầng điểm bán hàng + kiểm tra nhất quán thông số
[Step 4] 03_compliance_guard.md          → quét tuân thủ → dính 3 mục → viết lại → quét lần hai xác nhận không dính
[Step 5] Xuất output_listing_pack.md     → bàn giao core_selling_point / forbidden_words cho 04, 05
```

**Lưu ý khi chuyển tiếp**: bảng phân loại từ khóa của Step 2 đưa thẳng vào Step 3 (để cài từ khóa ở đoạn 7 của trang chi tiết), không tạo lại.

---

## 4. Kết quả tạo ra

### 4.1 Phân loại từ khóa (trích)

| Nhóm | Số từ | Từ tiêu biểu |
|---|---|---|
| Từ cốt lõi | 3 | `Carregador Portátil`, `Bateria Externa`, `Power Bank` |
| Từ thông số | 11 | `20000mAh`, `45W`, `3 Saídas`, `USB-C` |
| Từ nhóm khách hàng | 4 | `Unissex`, `Viagem`, `Trabalho`, `Estudante` |
| Từ tính năng | 8 | `Turbo Carga Rápida`, `Display Digital`, `Carregamento Simultâneo` |
| Từ ngữ cảnh | 6 | `Viagem`, `Trabalho Remoto`, `Camping`, `Emergência` |
| Từ phụ kiện | 5 | `com Cabo USB-C`, `com Manual`, `Bateria` |
| **Từ rủi ro** | **6** | ⛔ `iPhone` (thương hiệu chưa ủy quyền), `100% Original`, `À Prova de Água` (thông số không khớp)... |

> **Xử lý từ rủi ro**: cả 6 từ rủi ro đều được cách ly, **không được xuất hiện trong bất kỳ đầu ra nào**, nhưng được bàn giao đầy đủ cho 04/05 để chặn.
> Lưu ý riêng: `iPhone` là tên thương hiệu chưa được ủy quyền, còn `Celular` là từ thông dụng, dùng bình thường được — hai cái này không giống nhau.

### 4.2 Tiêu đề (3 bản dự phòng, số ký tự đã đo thực tế)

| # | Tiêu đề | Số ký tự | Hướng trọng tâm |
|---|---|---|---|
| **A** | `Carregador Portátil 20000mAh 45W Turbo Carga Rápida 3 Saídas com Display Digital para Celular Viagem` | **100/120** | Thông số dẫn dắt |
| **B** | `Carregador Portátil 20000mAh 45W com Display Digital 3 Saídas para Viagem e Trabalho Remoto` | **91/120** | Ngữ cảnh dẫn dắt |
| **C** | `Carregador Portátil 20000mAh 45W Bateria Externa com Display Digital 3 Saídas para Celular Viagem` | **97/120** | Tính năng dẫn dắt |

**Đề xuất A**, lý do: từ khóa chính `Carregador Portátil` nằm ở ký tự 1–19, `20000mAh 45W` nằm trong 30 ký tự đầu, mật độ thông số cao nhất, phù hợp giai đoạn khởi động sản phẩm mới để giành traffic tìm kiếm chính xác.

> **Không cố nhồi cho đủ 120 ký tự**. SOP có nhắc "tiêu đề viết đủ ký tự sẽ có lợi hơn ở điểm độ hoàn thiện", nhưng **điều kiện tiên quyết là mỗi từ đều phải là từ người mua sẽ tìm**. Thêm những từ như `Hot Sale`, `Novo` chỉ để đủ số ký tự là hành vi nhồi từ khóa bị sàn cấm rõ ràng.

### 4.3 Trang chi tiết (trích)

**Đoạn 1 · Lời chào**
```text
Carregador portátil de 20000mAh com saída de 45W e display digital.
Ideal para quem passa o dia fora de casa e não pode ficar sem bateria.
```

**Đoạn 2 · Điểm bán hàng cốt lõi** (kèm đối chiếu trước/sau khi viết lại)

| Đầu vào (phóng đại) | Đầu ra (kiểm chứng được) |
|---|---|
| Bateria gigante, dura dias | `Capacidade de 20000 mAh — recarrega um celular comum cerca de 4 vezes` |
| Carrega ultra rápido | `Saída de 45W, recarga completa de um celular em cerca de 40 minutos*` |
| Serve para qualquer celular | `Compatível com celulares e tablets via USB-A ou USB-C` |
| Design moderno e compacto | `Corpo em ABS de 14,2 × 6,8 × 2,8 cm e 380 g` |
| Seguro, não esquenta | `Proteção contra sobrecarga, sobrecorrente e curto-circuito` |

> `*` cần bổ sung điều kiện test ở đoạn 6.

**Đoạn 3 · Ngữ cảnh sử dụng** (toàn bộ nằm trong `usage_scope`)

| Ngữ cảnh | Cách dùng cụ thể |
|---|---|
| Viagem e deslocamentos | Carregue o celular no aeroporto, no ônibus ou no carro |
| Trabalho remoto | Mantenha o celular carregado durante o dia de reuniões |
| Emergência durante o dia | Saia de casa sem se preocupar com a bateria baixa |

**Đoạn 6 · Lưu ý** (được tạo dựa trên `review_insights`)

```text
- O cabo incluso (USB-C) tem 30 cm. Não é um cabo longo.
- O produto carrega celulares e tablets. Não é indicado para notebooks.
- A recarga completa em cerca de 40 minutos foi medida com um celular de
  4.500 mAh em temperatura ambiente de 25 °C.
- Nunca use o aparelho molhado ou sobre superfícies inflamáveis.
```

> Đoạn này là **đầu ra mang lại hiệu quả cao nhất của case study**. Hai đánh giá tiêu cực loại hiểu lầm → hai lời giải thích đặt trước, giảm trực tiếp trả hàng và đánh giá tiêu cực về sau.

### 4.4 Phân tầng điểm bán hàng

| Tầng | Điểm bán hàng | Căn cứ chứng minh |
|---|---|---|
| **Điểm bán hàng chính** | `Kết hợp sạc nhanh 45W + dung lượng 20000mAh` | `spec_table`: `45 W` / `20000 mAh` |
| Điểm bán hàng phụ | Màn hình số; 3 cổng ra; dải điện áp rộng 100–240V | `display` / `portas` / `voltagem_entrada` |
| Điểm bán hàng dự phòng | 380 g gọn nhẹ; bảo hành 6 tháng | `peso` / `garantia` |
| Điểm bán hàng bị cấm | `100% original`, `à prova d'água`, `serve para tudo` | Thương hiệu chưa ủy quyền / thông số không khớp / tuyệt đối hóa |

### 4.5 Kết quả quét tuân thủ

| Quy tắc | Số lần dính | Xử lý |
|---|---|---|
| R1 Từ ngữ tuyệt đối hóa | 1 | `mais rápido que carregador comum` → đổi thành cách diễn đạt định lượng kèm điều kiện test |
| R2 Tên thương hiệu chưa được ủy quyền | 1 | `iPhone` → đổi thành từ thông dụng `Celular` |
| R3 Khai khống thông số | 0 | — |
| R4 Từ khuyến mãi trong tiêu đề | 1 | `Promoção` trong tiêu đề đã chuyển sang đoạn 1 của trang chi tiết |
| R5 Nội dung nhạy cảm | 0 | — |
| R6 Ngữ cảnh vượt phạm vi | 1 | `Camping` ở đầu vào không nằm trong `usage_scope` → xóa và ghi `[SCENE_DROPPED]` |
| R7 Chứng cứ giả mạo | 0 | — |

**Kết luận**: dính 4 mục (R2 nguy cơ cao), đã xử lý toàn bộ, **quét lần hai không dính mục nào**, có thể đăng.

---

## 5. Bàn giao cho module phía sau

```yaml
core_selling_point: "20000mAh com saída de 45W — recarga completa do celular em cerca de 40 minutos"
secondary_points:
  - "Display digital de bateria"
  - "3 saídas (2× USB-A + 1× USB-C) para carregamento simultâneo"
  - "Entrada 100–240V, funciona em qualquer tomada do Brasil"
spec_table: { ... }          # giống input
forbidden_words:
  - "iPhone"
  - "100% Original"
  - "À Prova de Água"
  - "mais rápido do mercado"
  - "Serve para tudo"
  - "Promoção"
keyword_classified: { ... }
title_final: "Carregador Portátil 20000mAh 45W Turbo Carga Rápida 3 Saídas com Display Digital para Celular Viagem"
visual_tone_hint: "Tecnológico e limpo — fundo claro, tons de cinza e azul, sem elementos infantis"
usage_scope_confirmed:
  - "Viagem e deslocamentos diários"
  - "Trabalho remoto / home office"
  - "Emergência durante o dia fora de casa"
```

`visual_tone_hint` được cả 04 (hình ảnh) và 05 (video) cùng đọc, đảm bảo phong cách hình ảnh của hai bên thống nhất.

---

## 6. Phiên bản cho sàn khác (cùng sản phẩm)

### Mercado Livre (giới hạn 60 ký tự, cần rút gọn mạnh)

| # | Tiêu đề | Số ký tự |
|---|---|---|
| A | `Carregador Portátil 20000mAh 45W 3 Saídas Display Digital` | **57/60** |

**Quá trình cắt từ**: `Viagem` (từ ngữ cảnh, bị cắt đầu tiên) → `Turbo Carga Rápida` (từ tính năng, trùng nghĩa với 45W) → giữ lại `Carregador Portátil` (từ cốt lõi) + `20000mAh 45W` (thông số) + `3 Saídas Display Digital` (tính năng).
**Không cắt bất kỳ từ khóa chính hay thông số cốt lõi nào** — đúng quy tắc ưu tiên cắt từ của ML.

⚠️ **Quy chuẩn hình ảnh của ML xung đột với Shopee**: ảnh chính trên ML cấm mọi chữ và watermark, trong khi ảnh chính trên Shopee thường chèn chữ nêu điểm bán hàng. Vì vậy 04 Product Image Agent cần xuất **hai bộ phương án ảnh chính**, không dùng chung được.

---

## 7. Gợi ý tối ưu (bước tiếp theo cho người dùng)

| # | Gợi ý | Căn cứ |
|---|---|---|
| 1 | Dùng tiêu đề A/B/C để **A/B test 3 link** (SOP 3.4 cách hai) | Ba tiêu đề có hướng trọng tâm khác nhau, nhanh chóng biết hướng nào có CTR cao hơn |
| 2 | Ưu tiên chụp ảnh lúc **màn hình số đang sáng** | Đây là điểm bán hàng trực quan nhất, đối thủ phần lớn chụp kém |
| 3 | Chụp bổ sung một ảnh **trải phẳng các món trong hộp** | Đối phó trực tiếp với đánh giá tiêu cực loại hiểu lầm "tưởng có kèm cáp dài" |
| 4 | Quảng cáo không chạy thì sửa ảnh chính trước, rồi mới động tới ROI (SOP 3.6) | Sửa ảnh chính thường gỡ được "bug" quảng cáo, hiệu quả hơn chỉnh giá mù quáng |
| 5 | Sau khi đoạn 6 của trang chi tiết lên sóng thì **theo dõi biến động đánh giá tiêu cực** | Kiểm chứng "giải thích trước cho đánh giá tiêu cực loại hiểu lầm" có thực sự giảm trả hàng không |
| 6 | Có chứng nhận ANATEL rồi mới bổ sung ảnh chứng nhận | Hiện để trống là đúng — bịa chứng nhận là vi phạm nguy cơ cao |

---

## 8. Case study này chứng minh điều gì

| Kết luận | Bằng chứng |
|---|---|
| **Agent giữ được mức sàn về tính xác thực của thông số** | Toàn bộ quá trình 0 lần `[PARAM_DROPPED]`, vì mọi giá trị số đều lấy từ `spec_table` |
| **Chốt chặn tuân thủ có hiệu quả** | Chặn 4 mục, trong đó có 1 tên thương hiệu chưa ủy quyền nguy cơ cao |
| **Đánh giá có thể sửa ngược lại Listing** | 2 đánh giá tiêu cực loại hiểu lầm → 2 lời giải thích đặt trước, và hai lời giải thích này được xếp là mục hiệu quả cao nhất trong phần gợi ý tối ưu |
| **Không thể sao chép đơn giản giữa các sàn** | Cùng một sản phẩm, Shopee 100 ký tự vs ML 57 ký tự; hơn nữa quy chuẩn ảnh chính xung đột trực tiếp |
| **Mức trần nằm ở người chứ không ở model** | Agent chỉ đảm bảo được "đầu ra = đầu vào", bản thân thông số có đúng sự thật hay không là trách nhiệm của người dùng |

---

**File liên quan**: [Mô tả module](../README.md) · [Template đầu vào](../templates/input_product_brief.md) · [Template đầu ra](../templates/output_listing_pack.md) · [Lằn ranh đỏ tuân thủ](../../../docs/03_Compliance_Guard.md)
