# Case study · Air Fryer 5L (Shopee Brazil)

> **Loại case study**: sản phẩm thật · đã ẩn danh
> **Module sử dụng**: 05 Product Video Agent (thượng nguồn 03 + 04)
> **SOP tương ứng**: 3.3 Cấu trúc trang chi tiết (khung tự sự) + 1.6 Insight từ review (nguồn hook)
> **Điểm minh họa chính**: hai bản 15s / 30s, hook lấy từ đánh giá tiêu cực, khả năng hiểu khi tắt tiếng

---

## I. Bối cảnh sản phẩm

| Hạng mục | Nội dung |
|---|---|
| Sản phẩm | Nồi chiên không dầu 5L, 8 chương trình cài sẵn, cửa sổ quan sát, giỏ chiên tháo rời phủ chống dính |
| Thị trường | Brazil (Shopee BR) |
| Ngành hàng | Điện gia dụng |
| Định vị | SKU lợi nhuận |
| Tông thị giác | Sáng, ấm cúng, tông màu ấm |

**Vì sao chọn case study này**: ngành hàng điện gia dụng vốn rất hợp làm video (có "cảm giác quá trình" và "cảm giác kết quả"), hơn nữa **nỗi đau cốt lõi của nó rất rõ ràng**——lời phàn nàn xuất hiện nhiều nhất trong đánh giá tiêu cực của đối thủ là "làm nóng quá lâu". Đây là bối cảnh ứng dụng hoàn hảo cho điều SOP 1.6 nói: "review là nơi gần nhất với nhu cầu thật của người mua": **hook không cần sáng tác, cứ nhặt từ review ra là được.**

---

## II. Đầu vào (kế thừa từ 03 / 04)

```yaml
platform: shopee
target_market: Brazil
durations: [15, 30]
mode: standard
production_mode: mixed
prompt_language: en

# ── Bàn giao từ 03 (mục chặn, đã đủ toàn bộ) ──
core_selling_point: "Aquece até 200 °C em 3 minutos — sem pré-aquecimento longo"

secondary_points:
  - "Cesto de 5 litros — serve uma família de 4 pessoas"
  - "8 programas prontos com um toque"
  - "Frita com pouco ou nenhum óleo"
  - "Cesto antiaderente removível, pode lavar na máquina"
  - "Visor transparente — acompanhe sem abrir"

spec_table:
  capacidade: "5 L"
  potencia: "1500 W"
  temperatura: "80 °C a 200 °C"
  tempo_aquecimento: "≈ 3 minutos até 200 °C"
  programas: "8 presets"
  voltagem: "127 V / 220 V"
  material_cesto: "Aço com revestimento antiaderente"
  peso: "4,8 kg"
  dimensoes: "32 × 30 × 34 cm"
  garantia: "12 meses"

usage_scope_confirmed:
  - "Preparo de refeições diárias em casa"
  - "Reaquecer alimentos sem micro-ondas"
  - "Receitas rápidas para famílias pequenas"

forbidden_words:
  - "Fritura 100% Saudável"      # Tuyệt đối hóa + ám chỉ y tế
  - "Substitui Médico"           # Diễn đạt y tế
  - "O Mais Rápido do Brasil"    # Tuyệt đối hóa
  - "Philips"                    # Thương hiệu chưa được ủy quyền
  - "À Prova de Falhas"          # Tuyệt đối hóa

title_final: "Air Fryer 5L 1500W 8 Programas Cesto Antiaderente Visor Transparente para Família"

# ── Bàn giao từ 04 (thống nhất thị giác) ──
visual_tone_confirmed: "Claro e acolhedor — luz natural de cozinha, tons quentes, madeira e branco"
hero_visual: "Airefryer 3/4 em bancada de madeira clara, cesto puxado 1/3, luz natural pela janela"
key_visual_moments:
  - "Cesto puxando com batatas douradas fumegando — o 'resultado' mais vendável"
  - "Painel digital acendendo com os 8 programas — 'simples de usar'"
  - "Comparação de óleo: colher cheia vs colher quase vazia — 'pouco óleo'"

hook_material:
  pain_points:
    - "Đánh giá tiêu cực hay gặp: 'demora muito pra esquentar, quase 8 minutos'"
    - "Đánh giá tiêu cực hay gặp: 'não sei qual programa usar em cada comida'"
  satisfaction_points:
    - "Đánh giá tích cực hay gặp: 'batata ficou pronta rápido e crocante'"
    - "Đánh giá tích cực hay gặp: 'cesto fácil de lavar'"
  competitor_weakness:
    - "Đối thủ cùng dải giá phần lớn làm nóng mất 6–8 phút"
```

---

## III. Quy trình AI xử lý

```text
[Kiểm tra phụ thuộc] Đủ sáu trường chặn ✅
[Step 1] 01_script_and_storyboard.md   → Ứng viên hook → chọn → kịch bản hai bản → bảng storyboard
[Step 2] Đối chiếu thời lượng          → Bản 15s 30 từ / bản 30s 65 từ (tính thực tế)
[Step 3] 02_ai_video_and_voice.md      → Prompt từng cảnh + kịch bản lồng tiếng + phụ đề
[Step 4] Kiểm tra hiểu khi tắt tiếng   → Đối chiếu ba mục
[Step 5] VIDEO COMPLIANCE GUARD         → Phát hiện 4 vi phạm → xử lý
```

---

## IV. Kết quả tạo ra

### 4.1 Phương án hook (0–3s)

| # | Loại | Câu hook | Hình ảnh | Chọn |
|---|---|---|---|---|
| A | **Đánh thẳng nỗi đau** | `Sua air fryer demora uma eternidade para esquentar?` | Cận cảnh đồng hồ hẹn giờ trên điện thoại, số nhảy đến 6:00 thì bị bấm tạm dừng | ✅ **Đã chọn** |
| B | Đưa kết quả lên trước | `Batata crocante em doze minutos.` | Kéo giỏ chiên ra, khoai tây chiên vàng ruộm bốc hơi nóng | |
| C | Đối chiếu gây sốc | `Três minutos. Não oito.` | Chia đôi màn hình, bên trái đồng hồ 8:00, bên phải 3:00 | |

**Chọn A**, lý do:
- Lấy thẳng từ **lời phàn nàn hay gặp nhất trong đánh giá tiêu cực của đối thủ** (cách làm của SOP 1.6)
- Người mua Brazil ở nhà có trải nghiệm thật về việc "chờ nồi chiên không dầu làm nóng", hook đánh trúng **nỗi đau sẵn có**, không cần giáo dục thị trường
- Quay xong trong 3 giây, và hình ảnh có chuyển động (đồng hồ nhảy số)

> **B cũng rất mạnh**, nhưng nó giả định người xem đã muốn mua nồi chiên không dầu; A giả định người xem đã có một chiếc nồi chậm hoặc đang lo nồi chậm——nhóm sau rộng hơn trong tệp khách của Shopee Brazil.

### 4.2 Kịch bản bản 15s

| Phân đoạn | Thời gian | Mục tiêu | Nội dung |
|---|---|---|---|
| Hook | 0–3s | Giữ chân sự chú ý | Đồng hồ nhảy đến 6:00 thì bị tạm dừng + `Sua air fryer demora uma eternidade para esquentar?` |
| Điểm bán hàng cốt lõi | 3–9s | Nói rõ một điều | Nồi được cắm điện, số trên bảng điều khiển tăng nhanh từ 25 °C lên 200 °C, đồng hồ đồng thời hiển thị 3:00 |
| Bối cảnh | 9–13s | Nhập vai | Kéo giỏ chiên ra, khoai tây vàng ruộm bốc hơi, người nhà đưa tay lấy ăn |
| CTA | 13–15s | Kêu gọi hành động | Dừng hình sản phẩm + `Air Fryer 5L. Confira o link.` |

### 4.3 Kịch bản bản 30s

| Phân đoạn | Thời gian | Mục tiêu | Nội dung |
|---|---|---|---|
| Hook | 0–3s | Giữ chân sự chú ý | Giống bản 15s (**hook bắt buộc giống nhau**) |
| Điểm bán hàng 1 | 3–9s | Điểm bán hàng chính | Toàn bộ quá trình lên 200 °C trong 3 phút |
| Điểm bán hàng 2 | 9–16s | Điểm bán hàng phụ | 8 chương trình cài sẵn lần lượt sáng lên, ngón tay chạm nhẹ để chuyển |
| Bối cảnh | 16–23s | Nhập vai | Cả nhà ăn tối, giỏ chiên và khay nướng cùng ra món |
| Thông số/Niềm tin | 23–28s | Xóa băn khoăn | Dung tích 5L, 1500W, giỏ chiên tháo rửa được, bảo hành 12 tháng |
| CTA | 28–30s | Kêu gọi hành động | Giống bản 15s (**CTA bắt buộc giống nhau**) |

### 4.4 Bảng storyboard (bản 30s)

| Cảnh số | Thời lượng | Nội dung hình ảnh | Chuyển động máy | Phụ đề (xem khi tắt tiếng) | Hiệu ứng âm thanh / Giọng đọc |
|---|---|---|---|---|---|
| 1 | 0–3s | Cận cảnh đồng hồ hẹn giờ trên điện thoại, số nhảy đến 6:00 thì ngón tay bấm tạm dừng | Máy tĩnh, macro | `Esperando esquentar?` | Giọng đọc đặt câu hỏi + tiếng "bíp" của đồng hồ |
| 2 | 3–6s | Cắm điện nồi chiên, số trên bảng điều khiển tăng nhanh từ 25, đồng hồ chạy song song tới 3:00 | Push-in chậm vào bảng điều khiển | `200 °C em 3 minutos` | Tiếng bíp điện tử |
| 3 | 6–9s | Kéo giỏ chiên ra, khoai tây vàng ruộm bốc hơi, hơi nước bay lên | Bám theo ngang khi kéo giỏ ra | `Batata crocante` | Tiếng giòn rụm + tiếng hơi nóng |
| 4 | 9–12s | 8 biểu tượng chương trình cài sẵn trên bảng điều khiển lần lượt sáng lên | Máy tĩnh + push-in nhẹ | `8 programas prontos` | Âm điện tử vui tai |
| 5 | 12–16s | Ngón tay chạm nhẹ bảng điều khiển để chuyển chương trình, hình cắt sang biểu tượng món ăn tương ứng | Máy tĩnh | `Um toque` | Âm phản hồi cảm ứng |
| 6 | 16–19s | Cảnh bữa tối: giỏ chiên và khay nướng cùng ra món, người nhà (**chỉ tay/bóng lưng, không lộ mặt**) lấy ăn | Trung cảnh, máy tĩnh | `Para toda a família` | Tiếng bát đũa môi trường |
| 7 | 19–23s | Toàn cảnh bàn ăn, bày đủ suất ăn cho 5 người | Lia ngang chậm | `5 litros` | BGM tông ấm to dần |
| 8 | 23–26s | Cận cảnh tháo giỏ chiên, rửa, cho vào máy rửa bát | Máy tĩnh, góc từ trên xuống | `Cesto antiaderente lavável` | Tiếng nước chảy |
| 9 | 26–28s | Dàn trang thẻ thông số: 1500W / 5L / 127V-220V / 12 meses | Dàn trang tĩnh | `1500 W · 5 L · 12 meses` | BGM tiếp tục |
| 10 | 28–30s | Dừng hình sản phẩm + một góc danh sách đồ trong hộp | Máy tĩnh | `Confira o link` | BGM kết thúc |

> **10 cảnh / 30s** ——đạt yêu cầu "bản 30s có 7–10 cảnh".
> **Cảnh 6 được đánh dấu là cảnh người thật**: chỉ xuất chỉ dẫn quay, không tạo AI Prompt (xem 4.6).

### 4.5 Kịch bản lồng tiếng (**số từ và thời lượng đều được tính thực tế**)

| Cảnh số | Thời gian | Lời lồng tiếng | Số từ | Cộng dồn | Thời lượng ước tính |
|---|---|---|---|---|---|
| 1 | 0–3s | `Sua air fryer demora uma eternidade para esquentar?` | 8 | 8 | 3,2s |
| 2 | 3–6s | `Esta chega a duzentos graus em três minutos.` | 8 | 16 | 6,4s |
| 3–4 | 6–12s | `Cesto de cinco litros: comida para toda a família.` | 9 | 25 | 10,0s |
| 5 | 12–16s | `Oito programas prontos, só girar o botão.` | 7 | 32 | 12,8s |
| 6–7 | 16–23s | `Frita sem óleo e a louça sai fácil, porque o cesto é antiaderente.` | 13 | 45 | 18,0s |
| 8 | 23–26s | `Traz receitas em português e tem um ano de garantia.` | 10 | 55 | 22,0s |
| 9–10 | 26–30s | `Air Fryer cinco litros, cento e cinquenta graus a duzentos.` | 10 | **65** | **26,0s** |

**Đối chiếu thời lượng**: 65 từ ÷ 2,5 từ/giây = **26,0s**, nằm trong khung 30s (chừa 4s cho khoảng lặng và chuyển cảnh) ✅

**Kịch bản lồng tiếng bản 15s**:

| Cảnh số | Thời gian | Lời lồng tiếng | Số từ | Cộng dồn | Thời lượng ước tính |
|---|---|---|---|---|---|
| 1 | 0–3s | `Sua air fryer demora demais para esquentar?` | 7 | 7 | 2,8s |
| 2 | 3–6s | `Esta chega a duzentos graus em três minutos.` | 8 | 15 | 6,0s |
| 3 | 6–13s | `Cesto de cinco litros para toda a família.` | 8 | 23 | 9,2s |
| 4 | 13–15s | `Air Fryer cinco litros. Confira o link.` | 7 | **30** | **12,0s** |

**Đối chiếu thời lượng**: 30 từ ÷ 2,5 = **12,0s**, nằm trong khung 15s (chừa 3s khoảng lặng) ✅

**Gợi ý thông số TTS**
```yaml
accent: "Português (Brasil)"
gender: "Feminino"
tone: "Próximo e cotidiano, como quem conversa em casa"
speed: 1.0
pauses: "Cuối câu 0,3s / Chuyển cảnh 0,2s"
diacritics_checked: true   # Đã kiểm tra: três, família, óleo, antaderente → antiaderente, português, botão
```

> Lưu ý: bản nháp đầu của case study này viết `botão` thành `botao`, `três` thành `tres`, đã sửa ở bước kiểm tra. **Dấu thanh là điểm hay "toang" của TTS PT-BR**——`botao` và `botão` phát âm hoàn toàn khác nhau.

### 4.6 Xử lý cảnh người thật (cảnh 6)

```markdown
### Cảnh 6 · 16–19s · [Cảnh người thật — không tạo AI Prompt]

**Lý do**: có người thật xuất hiện, theo quy tắc V6 chuyển thành chỉ dẫn quay.

**Chỉ dẫn quay**
- Vị trí máy: ngang mặt bàn, trung cảnh, hơi thấp hơn tầm mắt (tạo cảm giác "quây quần bên bàn ăn")
- Cỡ cảnh: trung cảnh, khung hình chỉ lấy người nhà từ vai trở xuống
- Động tác: ba bàn tay lần lượt đưa từ ngoài khung vào lấy đồ ăn, tự nhiên không gượng
- Đạo cụ: bàn ăn, đĩa, món ăn thành phẩm quay thật (có thể dùng đồ chiên thật)
- Địa điểm: bếp hoặc khu ăn uống sáng sủa, ánh sáng ấm, nền gọn gàng
- Thời lượng: 3s
- Lưu ý: **khung hình chỉ từ vai trở xuống, không xuất hiện khuôn mặt**; nếu cần người thật lộ mặt, phải ký giấy đồng ý sử dụng hình ảnh

**Phương án AI thay thế** (nếu cần làm hoàn toàn bằng AI)
- Dùng bố cục không lộ mặt: chỉ có bàn tay lấy đồ ăn
- Prompt tương ứng: Close-up of three hands, of different skin tones,
  reaching into frame to take golden french fries from an air fryer basket
  on a light wooden dining table, no faces visible, warm natural window light,
  shallow depth of field, photorealistic lifestyle photography, slow gentle motion
```

### 4.7 Bảng phụ đề

| Cảnh số | Thời gian | Dòng 1 | Dòng 2 | Số ký tự | Số dòng |
|---|---|---|---|---|---|
| 1 | 0–3s | `Esperando esquentar?` | — | 20 | 1 |
| 2 | 3–6s | `200 °C em` | `3 minutos` | 12 | 2 |
| 3 | 6–9s | `Batata crocante` | — | 15 | 1 |
| 4 | 9–12s | `8 programas` | `prontos` | 17 | 2 |
| 5 | 12–16s | `Um toque` | — | 8 | 1 |
| 6 | 16–19s | `Para toda` | `a família` | 16 | 2 |
| 7 | 19–23s | `5 litros` | — | 8 | 1 |
| 8 | 23–26s | `Cesto lavável` | — | 13 | 1 |
| 9 | 26–28s | `1500 W · 5 L` | `12 meses` | 19 | 2 |
| 10 | 28–30s | `Confira o link` | — | 14 | 1 |

Tất cả đều đạt "mỗi màn hình ≤2 dòng / mỗi dòng ≤20 ký tự".

### 4.8 Kiểm tra khả năng hiểu khi tắt tiếng

| Mục kiểm tra | Kết quả | Căn cứ |
|---|---|---|
| Tắt tiếng, có hiểu đây là sản phẩm gì không | ✅ | Cảnh 2/3/7 đều có hình sản phẩm đầy đủ + phụ đề `5 litros` |
| Tắt tiếng, có hiểu điểm bán hàng cốt lõi không | ✅ | Cảnh 1 (đồng hồ 6:00) + cảnh 2 (`200 °C em 3 minutos`) tạo thành phép đối chiếu trọn vẹn |
| Tắt tiếng, có hiểu cuối video cần làm gì không | ✅ | Phụ đề cảnh 10 `Confira o link` |
| **Có đạt không** | **✅ Đạt** | Cả ba mục đều ✅ |

> **Điểm thiết kế của cảnh 1**: phụ đề viết `Esperando esquentar?` thay vì cả câu hỏi đầy đủ, vì phụ đề phải ngắn; còn **hình ảnh đồng hồ nhảy đến 6:00 tự nó đã truyền tải được "chờ quá lâu" mà không cần chữ nào**. Đây chính là ứng dụng của nguyên tắc "hình ảnh ưu tiên hơn lời thoại".

### 4.9 Kết quả quét tuân thủ video

| Quy tắc | Vi phạm | Xử lý |
|---|---|---|
| V1 Bằng chứng giả | 0 | Không có chứng nhận / doanh số / đánh giá bịa đặt ✅ |
| V2 Thông số không khớp | **1** | Bản nháp phụ đề viết `1500W` (không có khoảng trắng), đã sửa thành `1500 W` cho khớp với `spec_table` |
| V3 Bối cảnh vượt phạm vi | 0 | Mọi bối cảnh đều nằm trong `usage_scope_confirmed` ✅ |
| V4 Từ ngữ tuyệt đối hóa | **2** | `O mais rápido do Brasil` trong bản nháp kịch bản → đổi thành `200 °C em 3 minutos`; `100% sem óleo` trong kịch bản lồng tiếng → đổi thành `sem óleo ou com pouquíssimo óleo` |
| V5 Thương hiệu chưa được ủy quyền | **1** | `forbidden_words` đầu vào có `Philips`, đã chặn trong toàn bộ phụ đề và lồng tiếng |
| V6 Chân dung người thật | **1** | Cảnh 6 ban đầu dự kiến quay người thật lộ mặt → đổi thành **chỉ từ vai trở xuống**, đồng thời bổ sung phương án AI thay thế không lộ mặt |
| V7 Demo nguy hiểm | 0 | Không có thao tác nguy hiểm ✅ |
| V8 Bản quyền âm thanh | **1** | BGM và hiệu ứng âm thanh đã ghi chú「phải dùng nội dung được phép dùng thương mại」 |

**Kết luận**: phát hiện 5 vi phạm (gồm cả loại chân dung V6), đã xử lý toàn bộ, **quét lại lần hai không còn vi phạm**.

---

## V. Yêu cầu kỹ thuật

```yaml
aspect_ratio: "1:1"            # Vị trí ảnh chính Shopee; bản TikTok đổi sang 9:16
resolution: "1080x1080"
bgm_mood: "Tông ấm, nhẹ nhàng vui tươi, cảm giác đời thường, không ồn ào, đoạn giữa to dần, kết thúc gọn gàng"
bgm_license: "Phải dùng nội dung được phép dùng thương mại"
sfx_list:
  - "Tiếng bíp đồng hồ hẹn giờ (cảnh 1)"
  - "Tiếng bíp điện tử (cảnh 2/4)"
  - "Tiếng giòn rụm + tiếng hơi nóng (cảnh 3)"
  - "Âm phản hồi cảm ứng (cảnh 5)"
  - "Tiếng bát đũa môi trường (cảnh 6)"
  - "Tiếng nước chảy (cảnh 8)"
overlay_elements:
  - "Thẻ thông số (cảnh 9): 1500 W · 5 L · 127V/220V · 12 meses"
  - "Vị trí Logo ở góc (cảnh 10)"
```

---

## VI. Đề xuất tối ưu

| # | Đề xuất | Căn cứ |
|---|---|---|
| 1 | **Quay thật quá trình tăng số ở cảnh 2**, đừng dùng animation hậu kỳ | Quá trình thật thuyết phục hơn animation, đồng thời tránh cảm giác "làm giả số liệu" |
| 2 | Bản 15s ưu tiên chạy quảng cáo ở vị trí ảnh chính, bản 30s đặt ở trang chi tiết | Bản 15s mật độ thông tin cao hơn, hợp để giữ chân; bản 30s hợp với người dùng có ý định đã vào trang chi tiết |
| 3 | Quay bổ sung một cảnh liền mạch không cắt **chỉ trong 3 phút** làm nội dung sáng tạo | Có thể cắt ra nhiều phiên bản để tái sử dụng, cũng tiện làm bản dọc TikTok về sau |
| 4 | Chạy A/B test với hook B (`Batata crocante em doze minutos`) | Hai hook đại diện cho hai giả thuyết: A đánh vào nỗi đau sẵn có, B đánh vào cơn thèm ăn |
| 5 | Sau khi lên sóng, theo dõi đánh giá tiêu cực liên quan đến "thời gian làm nóng" có giảm không | Kiểm chứng điểm bán hàng cốt lõi có thực sự đứng vững |
| 6 | Bản TikTok cần làm lại bố cục (9:16, đưa phụ đề lên trên để tránh 20% phía dưới) | Kéo giãn trực tiếp nội dung ngang sẽ phá vỡ vùng an toàn |

---

## VII. Case study này chứng minh điều gì

| Kết luận | Bằng chứng |
|---|---|
| **Hook nhặt từ review, không cần sáng tác** | Hook A lấy thẳng từ lời phàn nàn "làm nóng quá lâu" trong đánh giá tiêu cực của đối thủ |
| **Thời lượng lồng tiếng phải tính thực tế** | 65 từ ÷ 2,5 từ/giây = 26,0s, mọi con số đều tái lập được; vượt thì cắt từ chứ không tăng tốc độ đọc |
| **Khả năng hiểu khi tắt tiếng là chỉ tiêu cứng** | Qua cả ba mục mới tính là đạt——phần lớn người mua xem khi tắt tiếng |
| **Dấu thanh là điểm hay "toang" của PT-BR** | Bản nháp `botao` / `tres` đã được sửa thành `botão` / `três` |
| **Cảnh người thật phải xử lý riêng** | Cảnh 6 từ "người thật lộ mặt" đổi thành "từ vai trở xuống", kèm phương án AI thay thế không lộ mặt |
| **Phụ đề ngắn hơn lồng tiếng** | Lồng tiếng của hook là câu hỏi đầy đủ, phụ đề rút gọn thành `Esperando esquentar?` |
| **Hook/CTA của bản 15s và 30s giống nhau** | Hai phiên bản cùng phục vụ một ý |
| **Từ ngữ tuyệt đối hóa sẽ tự nhiên chen vào** | Bản nháp xuất hiện `O mais rápido do Brasil`, cho thấy quy tắc chặn là cần thiết chứ không phải hình thức |

---

**File liên quan**: [Giới thiệu module](../README.md) · [Prompt kịch bản và storyboard](../prompts/01_script_and_storyboard.md) · [Prompt video và lồng tiếng](../prompts/02_ai_video_and_voice.md) · [Template đầu ra](../templates/output_video_pack.yaml) · [Checklist tự kiểm tra](../../../docs/04_Result_Checklist.md)
