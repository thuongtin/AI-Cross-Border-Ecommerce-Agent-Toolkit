# Case study 02 · Bolsa Térmica 20L (túi giữ nhiệt) · Vòng khép kín chỉnh sửa lại ở chế độ iterate

> ⚠️ **Cập nhật quy định (2026-10)**: 「ảnh chính ML nền trắng tinh」trong case study là quy định cũ.
> Hiện hành: nền trắng/màu trơn/bối cảnh thật **tùy theo ngành hàng**, nhưng nền phải sạch, ảnh đầu tiên cấm chữ khuyến mãi.
> Xem [`../Agents/04_Product_Image_Agent/references/platform-mercadolivre.md`](../../Agents/04_Product_Image_Agent/references/platform-mercadolivre.md).

> **Loại case study**: Sản phẩm thật · Đã ẩn danh hóa
> **Module bao phủ**: 03 Listing Creative (`mode = iterate`) + 06 Advertising (chạy thử)
> **Thị trường**: Shopee Brazil
> **SOP tương ứng**: 3.6 Logic điều chỉnh quảng cáo · 3.5 Nhịp độ quảng cáo và đánh giá

---

## I. Case study này khác gì case study 01

Case study 01 minh họa **từ 0 đến 1** (`mode = single`). Case study này minh họa **chạy rồi mới phát hiện vấn đề, quay lại sửa** (`mode = iterate`).

| | Case study 01 | Case study 02 |
|---|---|---|
| Tình huống kích hoạt | Đăng bán sản phẩm mới | Đã đăng bán, số liệu quảng cáo không khỏe |
| Đầu vào | Trống | **Listing hiện có + mô tả triệu chứng** |
| Đầu ra | Gói nội dung sáng tạo đầy đủ | **Chỉ sửa phần cần thiết**, phần còn lại giữ nguyên |
| Năng lực cốt lõi | Tạo mới | **Chẩn đoán + thay đổi tối thiểu** |

> **Vì sao cần chế độ iterate**: SOP 3.6 đã viết các hiện tượng như "có hiển thị mà không có click", "có click mà không thêm vào giỏ" thành quy tắc có thể phán định. Nghĩa là **sửa lại không nên dựa vào cảm tính** — triệu chứng chẩn đoán được, chỗ cần sửa xác định được.

---

## II. Bối cảnh sản phẩm

| Mục | Nội dung |
|---|---|
| Sản phẩm | Túi giữ nhiệt 20L, vải chống nước, lót giấy bạc nhôm dày, gấp gọn được, quai xách bản rộng gia cố |
| Thị trường | Brazil (Shopee BR) |
| Ngành hàng | Túi xách & vali |
| Định vị | SKU kéo traffic |
| Thời gian đã đăng bán | 3 tuần |

**Vì sao chọn sản phẩm này**: ngưỡng chuẩn khỏe mạnh mà SOP 3.6 đưa ra là「CTR 3–5%」. Với ngành hàng **ảnh chính ít khác biệt** như túi giữ nhiệt, vấn đề dễ gặp nhất chính là "có hiển thị mà không có click" — ảnh chính nhìn na ná nhau, người mua lấy lý do gì để click vào bạn? Đây là tình huống iterate điển hình nhất và cũng dễ kiểm chứng nhất.

---

## III. Ngưỡng chuẩn khỏe mạnh của SOP 3.6

Đặt ngưỡng chuẩn ra trước, vì **chẩn đoán cần có chuẩn**:

| Chỉ số | Chuẩn (SOP) | Thực tế case study | Đánh giá |
|---|---|---|---|
| CTR | **3–5%** | **1,4%** | ❌ Thấp hơn mức dưới quá một nửa |
| Tỷ lệ chuyển đổi (CVR) | Ổn định **trên 1%** | 2,1% | ✅ Đạt |
| Tỷ lệ thêm vào giỏ | **> 8%** | 11,3% | ✅ Đạt |

**Xác định triệu chứng**: **có hiển thị mà không có click** (lượt hiển thị bình thường, CTR thấp nghiêm trọng, nhưng chuyển đổi và thêm vào giỏ đều khỏe).

> Tổ hợp này cực kỳ quan trọng: **tỷ lệ chuyển đổi bình thường chứng tỏ bản thân sản phẩm không có vấn đề, giá cũng không có vấn đề** — vấn đề nằm ở "khâu trước khi người mua click vào", tức là **ảnh chính và tiêu đề**. Nếu tỷ lệ chuyển đổi cũng thấp, lúc đó mới phải xem xét trang chi tiết và giá.

---

## IV. Quy tắc chẩn đoán của SOP 3.6

Danh sách ưu tiên kiểm tra mà SOP đưa ra cho trường hợp "có hiển thị mà không có click":

| Mục ưu tiên kiểm tra | Hiện trạng case study | Chẩn đoán |
|---|---|---|
| Ảnh chính | Một ảnh sản phẩm nền trắng, không có chữ, **gần như không phân biệt được** với ảnh chính của đối thủ | 🔴 **Nguyên nhân chính** |
| Tiêu đề | Đủ thông số nhưng thiếu "lý do để click vào" | 🟡 Nguyên nhân phụ |
| Cách hiển thị giá | Ngang với sản phẩm cùng loại | ✅ Không vấn đề |
| Điểm bán hàng lõi | Trang chi tiết có, nhưng **ảnh chính hoàn toàn không có** | 🔴 **Nguyên nhân chính** |
| Có ưu đãi rõ ràng không | Không | 🟡 Tối ưu tùy chọn |

**Hướng tối ưu SOP đưa ra**: đổi ảnh chính → tối ưu từ khóa tiêu đề → làm nổi bật lợi thế giá → thêm điểm bán hàng lên ảnh chính → điều chỉnh từ khóa quảng cáo

---

## V. Đầu vào của chế độ iterate

```yaml
platform: shopee
target_market: Brazil
mode: iterate                  # ← Then chốt: chỉ sửa phần cần thiết

# ── Hiện trạng ──
existing_title: "Bolsa Térmica 20L Impermeável para Delivery e Supermercado com Alça Reforçada"
                                    # 77 ký tự

existing_main_image_desc: "Bolsa térmica em fundo branco puro, vista frontal 3/4,
                           sem texto, sem elementos gráficos, produto centralizado"

symptom: "Có hiển thị mà không có click. CTR 1,4% (chuẩn SOP 3–5%). Lượt hiển thị bình thường 12.400/tuần,
          tỷ lệ chuyển đổi 2,1% và tỷ lệ thêm vào giỏ 11,3% đều đạt."

# ── Ràng buộc ──
constraints: "Không thay đổi định vị sản phẩm và giá. Ảnh chính cần sửa, tiêu đề được phép tối ưu nhẹ.
              Trang chi tiết và video giữ nguyên (tỷ lệ chuyển đổi đã đạt, không cần động vào)."

# ── Kế thừa từ đầu ra gốc của 03 (giữ tính nhất quán) ──
core_selling_point: "Conserva a temperatura por até 8 horas com forro de alumínio duplo"
spec_table:
  capacidade: "20 L"
  material_externo: "Poliéster 600D impermeável"
  forro: "Alumínio duplo"
  tempo_conservacao: "até 8 horas"
  carga_suportada: "até 15 kg"
  dimensoes: "40 × 30 × 22 cm"
  medida_fechada: "40 × 30 × 6 cm"
  peso: "620 g"
forbidden_words: ["100% Impermeável", "A Melhor do Mercado", "Vedação Absoluta", "Termo Rei"]
usage_scope_confirmed: ["Transporte de compras do supermercado", "Entrega de comida por entregadores", "Transporte de bebidas geladas para eventos"]
```

---

## VI. Phương án chỉnh sửa lại

### 6.1 Iterate ảnh chính (thay đổi cốt lõi)

**Chẩn đoán**: vấn đề của ảnh chính gốc không phải "chụp xấu", mà là **"không thấy khác gì so với các túi giữ nhiệt khác"**. Trong danh sách tìm kiếm có 20 tấm túi giữ nhiệt nền trắng gần như y hệt nhau, người mua không có lý do gì để click vào tấm của bạn.

```markdown
## Phương án iterate ảnh chính

- Hiện trạng: nền trắng tinh + không chữ + góc chính diện 3/4
- Triệu chứng: CTR 1,4% (chuẩn 3–5%), lượt hiển thị bình thường
- Chẩn đoán: ảnh chính「không có độ khác biệt」trong kết quả tìm kiếm. Tỷ lệ chuyển đổi và thêm vào giỏ đều đạt → sản phẩm và giá không có vấn đề,
        vấn đề ở khâu click. Tương ứng SOP 3.6「có hiển thị mà không có click → ưu tiên kiểm tra ảnh chính」.
- Điểm sửa (tối thiểu hóa):
    1. Giữ nền trắng và góc chụp sản phẩm (không chụp lại từ đầu)
    2. Thêm **yếu tố khác biệt thị giác**: đặt sản phẩm ở「trạng thái mở hé」, lộ lớp giấy bạc nhôm bên trong + một chai nước lạnh
    3. Thêm **một dòng chữ điểm bán hàng**: `8h de conservação` (không quá 20 ký tự, Shopee cho phép chữ trên ảnh)
- Không thay đổi: bản thân sản phẩm, góc chụp, màu nền, cách hiển thị giá
- Hiệu quả kỳ vọng: trong danh sách tìm kiếm xuất hiện「điểm khác biệt nhìn là hiểu」, mục tiêu CTR tăng lên trên 3%
```

**Vì sao sửa như vậy**:
- **Lộ lớp lót + chai nước lạnh** = một tấm ảnh trả lời cùng lúc "đây là gì" và "nó làm được gì", điều mà ảnh chính gốc không làm được
- **`8h de conservação`** lấy trực tiếp từ `core_selling_point`, và là thông tin đối thủ chỉ nói trong trang chi tiết, không nói trên ảnh chính — **đưa điểm khác biệt từ trang chi tiết lên ảnh chính là cách trực tiếp nhất để tăng CTR**

### 6.2 Prompt ảnh chính sau iterate (bản Shopee)

```text
[SUBJECT] A grey and navy thermal delivery bag, 20L, partially unzipped and open
to about 40 degrees, revealing a shiny silver aluminum-lined interior.
A chilled glass bottle with visible condensation stands beside the bag's base.

[MATERIAL] Water-resistant 600D polyester outer with visible fine weave texture,
matte finish; bright reflective silver aluminum foil lining inside,
slightly wrinkled to show thickness and flexibility.

[COMPOSITION] Three-quarter front view, bag centered occupying 65% of frame,
slightly elevated camera angle looking down into the open bag,
empty space on the top right reserved for text overlay.

[LIGHTING] Clean studio lighting from upper-left with large softbox,
crisp specular highlights on the aluminum lining to convey the insulation property,
neutral white temperature (5500K).

[BACKGROUND] Pure seamless white background, RGB 255,255,255, no shadow outside
the product and bottle area.

[STYLE] Commercial product photography, photorealistic, high detail,
crisp focus across bag and bottle, category-leading clarity.

[PARAMETERS] 1:1 square aspect ratio, 1024x1024, reserve top-right 30% for text overlay.
```

**Negative Prompt**

```text
text rendered by the model, watermark, logo, brand names, melted ice, water puddle,
wet fabric, visible human hands, food items other than the bottle,
cluttered background, low resolution, distorted proportions, dark or moody lighting
```

> **Bắt buộc thêm `melted ice, water puddle, wet fabric`**: sản phẩm là "chống nước bắn" chứ không phải "chống nước hoàn toàn" (`forbidden_words` đã cấm rõ `100% Impermeável`). Trong ảnh mà có vệt nước hay đá tan là ngầm ý khả năng chống nước vượt quá thực tế.

### 6.3 Tinh chỉnh tiêu đề

**Nguyên tắc**: ở `mode = iterate`, tiêu đề chỉ **tối ưu nhẹ**, không viết lại. Vì tỷ lệ chuyển đổi đã đạt, chứng tỏ chất lượng traffic do tiêu đề mang lại không có vấn đề, vấn đề nằm ở CTR — **vai trò của tiêu đề là "để đúng người tìm thấy bạn", chứ không phải "khiến người ta muốn click vào bạn"**.

| | Tiêu đề | Số ký tự |
|---|---|---|
| Hiện trạng | `Bolsa Térmica 20L Impermeável para Delivery e Supermercado com Alça Reforçada` | **77/120** |
| Sau iterate | `Bolsa Térmica 20L Impermeável 8 Horas de Conservação para Delivery e Supermercado` | **81/120** |

**Giải thích thay đổi**:
- **Thêm** `8 Horas de Conservação` (điểm bán hàng tạo khác biệt cốt lõi, đồng thời là ý định tìm kiếm thật của người mua)
- **Bỏ** `com Alça Reforçada` (tính năng phụ, đã nói trong trang chi tiết)
- Vị trí từ khóa chính `Bolsa Térmica` giữ nguyên, vẫn ở đầu
- Mức thay đổi: tăng ròng 4 ký tự, **cấu trúc không đổi**

### 6.4 Những phần chắc chắn không thay đổi

| Mục | Không động vào | Lý do |
|---|---|---|
| Trang chi tiết | ❌ Không động | Tỷ lệ chuyển đổi 2,1% đã đạt → trang chi tiết đang hiệu quả |
| Giá | ❌ Không động | Chuyển đổi và thêm vào giỏ đạt → giá không phải điểm nghẽn |
| Video | ❌ Không động | Như trên |
| 8 ảnh còn lại | ❌ Không động | CTR chỉ liên quan đến ảnh chính |
| Cấu trúc SKU | ❌ Không động | Tỷ lệ thêm vào giỏ 11,3% đạt → thiết kế SKU hiệu quả |

> **Giá trị lớn nhất của `mode = iterate` nằm ở đây: nói rõ "không sửa gì".** Nhiều người vận hành khi CTR thấp hay tiện tay sửa giá, sửa trang chi tiết, thêm voucher — làm hỏng những khâu vốn không có vấn đề, rồi lại không biết thao tác nào mới thực sự có tác dụng.

---

## VII. Một đề xuất khác của SOP 3.6

SOP còn nhắc đến một mẹo gỡ "bug" quảng cáo:

> Khi quảng cáo không chạy được, đừng chỉ điều chỉnh ROI và ngân sách, lúc này hãy sửa nhẹ ảnh chính, tiêu đề, trang chi tiết, thường chỉ cần sửa ảnh chính là gỡ được bug quảng cáo, quảng cáo sẽ chạy lại được.

**Đánh giá mức độ áp dụng cho case study này**:

| Tình huống | Có áp dụng không |
|---|---|
| Quảng cáo **không chạy được** (không tiêu được tiền, không có hiển thị) | ✅ Áp dụng — sửa ảnh chính thường gỡ được |
| Quảng cáo **chạy được nhưng không có click** (case study này) | ✅ Cũng áp dụng — sửa ảnh chính là thao tác đầu tiên |
| Quảng cáo **chạy được, có click, không có chuyển đổi** | ❌ Không áp dụng — vấn đề ở trang chi tiết và giá |

**Quan sát thêm từ case study này**: thao tác sửa ảnh chính được SOP dùng cùng lúc cho hai mục đích — **gỡ bug quảng cáo** và **tăng CTR**. Điều này cho thấy ảnh chính có trọng số cực cao trong bộ phương pháp luận này: **nó vừa là cửa ngõ traffic, vừa là "công tắc kích hoạt" ở tầng kỹ thuật**.

---

## VIII. Cách kiểm chứng

Sửa xong bắt buộc phải kiểm chứng, nếu không sẽ không biết thay đổi có hiệu quả không.

| Mục kiểm chứng | Cách làm | Chu kỳ quan sát |
|---|---|---|
| CTR có tăng không | So sánh CTR cùng kỳ sau khi đổi ảnh chính | **7 ngày** (khoảng thời gian test của SOP) |
| Lượt hiển thị có thay đổi không | Xác nhận lượt hiển thị không giảm do thay đổi | 7 ngày |
| Tỷ lệ chuyển đổi có giữ được không | Xác nhận 2,1% không tụt (tránh traffic từ click mới bị kém đi) | 7 ngày |
| Quảng cáo có tiêu tiền bình thường không | Xác nhận ngân sách tiêu bình thường | 3 ngày |

**Nguyên tắc đối chứng**: **mỗi lần chỉ thay đổi một biến**. Case study này sửa cùng lúc ảnh chính và tiêu đề, nếu CTR tăng thì không xác định được cái nào có tác dụng.

> ⚠️ **Đây là một khiếm khuyết phương pháp luận đã biết**, cũng là lời thú nhận thẳng thắn của case study này: để rút gọn độ dài, ở đây sửa ảnh chính và tiêu đề cùng lúc.
> **Khi làm thực tế nên chia hai bước**: sửa ảnh chính trước (7 ngày) → có cải thiện thì dừng; không cải thiện thì mới tối ưu thêm tiêu đề (thêm 7 ngày). Như vậy hiệu quả của mỗi bước đều quy nguyên nhân được.
> Nguyên tắc này cùng logic với câu "mô hình quảng cáo phải chạy đủ 7 ngày test" trong SOP — **thay đổi cần có khoảng thời gian test, không được động vào nhiều biến cùng lúc**.

---

## IX. Đề xuất tối ưu

| # | Đề xuất | Căn cứ |
|---|---|---|
| 1 | **Lần làm thực tế này nên chia hai bước**: sửa ảnh chính trước → quan sát 7 ngày → rồi mới quyết định có sửa tiêu đề không | Sửa hai biến cùng lúc thì không quy nguyên nhân được |
| 2 | Đạo cụ chai nước lạnh trên ảnh chính phải **chụp thật hoặc ghép từ ảnh thật**, đừng vẽ ra | Chai nước vẽ ra sẽ làm giảm độ tin cậy |
| 3 | Nếu sau 7 ngày CTR vẫn chưa đạt 3%, cân nhắc **phương án B**: đặt túi giữ nhiệt vào bối cảnh sử dụng thật (shipper giao đồ ăn đeo trên lưng) | Ảnh chính nền trắng ở ngành hàng túi xách bị đồng nhất nghiêm trọng, ảnh chính theo bối cảnh là một hướng khác |
| 4 | Bổ sung **một ảnh chính đối chứng ở trạng thái mở để A/B test** | Kiểm chứng "lộ lớp lót" có phải yếu tố then chốt giúp tăng click không |
| 5 | Trang chi tiết giữ nguyên, nhưng phải **ghi lại mốc thời gian trước khi thay đổi** | Tiện truy ngược sau này xem lần thay đổi nào mang lại cải thiện |
| 6 | Nếu CTR tăng mà tỷ lệ chuyển đổi tụt, nghĩa là ảnh chính mới đã hút nhầm người | Cần hiệu chỉnh lại cách thể hiện điểm bán hàng |

---

## X. Case study này chứng minh điều gì

| Kết luận | Bằng chứng |
|---|---|
| **Chẩn đoán cần có ngưỡng chuẩn** | Không có chuẩn「CTR 3–5%」của SOP thì con số 1,4% chẳng có ý nghĩa gì |
| **Tổ hợp chỉ số khoanh vùng được khâu có vấn đề** | CTR thấp nhưng chuyển đổi/thêm vào giỏ đạt → vấn đề ở khâu click, không phải sản phẩm và giá |
| **Cốt lõi của iterate là "không sửa gì"** | Liệt kê rõ 4 mục trang chi tiết/giá/video/SKU không động vào, tránh làm hỏng khâu không có vấn đề |
| **Đầu ra của `mode = iterate` là tập thay đổi tối thiểu** | Ảnh chính sửa 3 chỗ, tiêu đề sửa 2 cụm từ, còn lại giữ nguyên toàn bộ |
| **Thay đổi bắt buộc phải quy nguyên nhân được** | Việc sửa hai biến cùng lúc được ghi rõ là khiếm khuyết, kèm phương án chia bước |
| **Từ cấm sẽ ràng buộc ngược lại hình ảnh** | Cấm `100% Impermeável` → Negative Prompt của ảnh chính bắt buộc thêm `water puddle, wet fabric` |
| **Một thao tác phục vụ hai mục đích** | Sửa ảnh chính vừa tăng CTR, vừa là cách gỡ bug quảng cáo trong SOP |

---

**Case study liên quan**: [Case study 01 · Patinete Elétrico end-to-end](../01_Patinete_Eletrico_500W/) · [Power Bank](../../Agents/03_Listing_Creative_Agent/examples/powerbank_20000mah.md) · [Pet Carrier](../../Agents/04_Product_Image_Agent/examples/pet_carrier.md) · [Air Fryer](../../Agents/05_Product_Video_Agent/examples/air_fryer.md)

**Tài liệu liên quan**: [Phân rã kiến trúc](../../docs/00_Architecture_SOP_to_Agent.md) · [06 Advertising Agent](../../Agents/06_Advertising_Optimization_Agent/) (Phase 2) · [Checklist tự kiểm tra](../../docs/04_Result_Checklist.md)
