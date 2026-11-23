# TASK · Xây dựng trang chi tiết và chắt lọc điểm bán hàng / thông số

> Dùng kèm: `00_system.md` (System Prompt) + đầu ra của `01_keyword_to_title.md` (bảng phân loại từ khóa) + `templates/input_product_brief.md`

Tương ứng SOP **3.3 Xây dựng Listing (cấu trúc trang chi tiết)**.

> ⚠️ **Vấn đề đánh số trong bản gốc SOP**: bản gốc viết "có thể chia thành 8 phần sau", nhưng thực tế chỉ liệt kê 7 mục (lời chào / điểm bán hàng cốt lõi / ngữ cảnh sử dụng / thông số chi tiết / hậu mãi và CSKH / lưu ý / khu vực tag từ khóa). Module này thực hiện theo **7 đoạn**. Nếu sau này bổ sung đoạn thứ 8, hãy cập nhật ở đây và trong `docs/02_Platform_Output_Spec.md`.

---

# INPUT

Trường bắt buộc:

| Trường | Mô tả |
|---|---|
| `platform` | Sàn mục tiêu (quyết định cấu trúc: Shopee 7 đoạn / ML 5 ý + Ficha Técnica) |
| `target_market` | Thị trường mục tiêu (quyết định ngôn ngữ đầu ra) |
| `product_name` | Tên gọi chung của sản phẩm |
| `category` | Ngành hàng |
| `spec_table` | Bảng thông số (cặp key-value) |
| `usage_scope[]` | Các ngữ cảnh sử dụng được phép nêu |
| `selling_points_input[]` | Điểm bán hàng đã biết (cách diễn đạt gốc, có thể phóng đại, Agent sẽ viết lại) |
| `warranty` | Thông tin bảo hành (**bắt buộc với Shopee Brazil**, ML cũng yêu cầu) |
| `package_content[]` | Danh sách hàng trong hộp (**đây là mục hay bị đánh giá tiêu cực nhất, nhất định phải điền đủ**) |
| `notes_required` | Có cần tạo đoạn "Lưu ý" hay không (`true` / `false`) |
| `keyword_classified` | Lấy từ đoạn 5 của `01_keyword_to_title.md` |

Trường tùy chọn:
- `review_insights`: kết quả quy nguyên nhân đánh giá tiêu cực từ 07 Review Analysis Agent (nếu có thì dùng để bổ sung đoạn 6)
- `competitor_weakness[]`: điểm yếu của đối thủ (dùng cho cách diễn đạt khác biệt hóa)

---

# Cấu trúc đầu ra (platform = shopee)

Đúng 7 đoạn, thứ tự cố định:

```markdown
## 1. Nội dung trang chi tiết

### Đoạn 1 · Lời chào (Boas-vindas)
### Đoạn 2 · Điểm bán hàng cốt lõi (Diferenciais)
### Đoạn 3 · Ngữ cảnh sử dụng (Cenários de Uso)
### Đoạn 4 · Thông số chi tiết (Especificações)
### Đoạn 5 · Cam kết hậu mãi và CSKH (Garantia e Atendimento)
### Đoạn 6 · Lưu ý (Observações Importantes)  ← chỉ tạo khi notes_required = true
### Đoạn 7 · Khu vực tag từ khóa (Tags de Busca)
```

---

## Đoạn 1 · Lời chào

**Nội dung**: một câu tự giới thiệu + thông tin khuyến mãi.
**Độ dài**: 2–3 câu, không quá 200 ký tự.
**Lưu ý**: không viết kiểu xã giao không có thông tin như "Cảm ơn đã ghé shop". Viết "chúng tôi bán gì + vì sao đáng để đọc tiếp".

---

## Đoạn 2 · Điểm bán hàng cốt lõi

**Nội dung**: sản phẩm giải quyết vấn đề gì, có ưu điểm gì.
**Số lượng**: 3–5 ý.
**Định dạng**: mỗi ý một dòng, `tiêu đề điểm bán hàng — số liệu chứng minh`.

### Ánh xạ điểm bán hàng về sự thật (bắt buộc thực hiện)

Điểm bán hàng ở đầu vào nếu là cách nói phóng đại, **bắt buộc viết lại thành cách diễn đạt kiểm chứng được**:

| Đầu vào (phóng đại) | Đầu ra (kiểm chứng được) |
|---|---|
| Bateria mais forte do mercado | Bateria de 20000mAh |
| Carrega super rápido | Saída de 45W, recarrega um celular em cerca de 40 minutos* |
| Qualidade premium | Carcaça em ABS + PC com acabamento antichamas |
| Durável | Suporta mais de 500 ciclos de carga |
| Design moderno | Corpo de 14,2 cm × 6,8 cm × 2,8 cm, 380 g |
| Serve para tudo | Compatível com smartphones, tablets e fones com entrada USB-C ou USB-A |

> **Quy tắc viết lại**: thay "tính từ" bằng "danh từ + con số". Câu nào không chứng minh được bằng một tấm ảnh, một thông số hoặc một điều kiện test thì xóa hết.
> Giá trị có dấu `*` cần bổ sung điều kiện test ở đoạn 6.

---

## Đoạn 3 · Ngữ cảnh sử dụng

**Nội dung**: giúp người mua hình dung bản thân trong tình huống, kích thích mong muốn mua.

> ⚠️ **Đây là vùng dễ quảng cáo sai sự thật nhất.** Bản gốc SOP cũng đã đánh dấu điểm này. Khi thực hiện, ràng buộc bắt buộc:
> Mỗi ngữ cảnh **bắt buộc** nằm trong danh sách `input.usage_scope`. Ngữ cảnh vượt phạm vi đều bị xóa, và ghi `[SCENE_DROPPED]`.

**Định dạng**: 3–5 ngữ cảnh, mỗi ngữ cảnh ghi `tên ngữ cảnh + cách dùng cụ thể` (không viết câu sáo rỗng kiểu "giúp cuộc sống tốt đẹp hơn").

---

## Đoạn 4 · Thông số chi tiết

**Nội dung**: các thông tin quy cách như màu sắc, chất liệu, kích thước, dung lượng, đóng gói.

**Định dạng**: bảng. Cột trái là tên thông số (ngôn ngữ bản địa), cột phải là giá trị (kèm đơn vị).

**Ràng buộc cứng**:
- Mỗi giá trị **bắt buộc** khớp từng ký tự với mục tương ứng trong `spec_table`
- `package_content[]` bắt buộc **liệt kê đầy đủ**, không được thiếu một món nào (đây là nguồn đánh giá tiêu cực số một)
- Đơn vị toàn bộ là hệ mét, số thập phân dùng dấu phẩy

---

## Đoạn 5 · Cam kết hậu mãi và CSKH

**Nội dung**: giảm nỗi lo trả hàng.

**Yêu cầu**:
- Cam kết phải khớp với `input.warranty`
- **Shopee Brazil**: thông tin bảo hành là yêu cầu của luật bảo vệ người tiêu dùng, bắt buộc ghi rõ thời hạn và phạm vi
- **Cấm** cam kết điều không làm được (ví dụ "đổi trả vô điều kiện" nếu quy tắc sàn không hỗ trợ)

---

## Đoạn 6 · Lưu ý (tạo có điều kiện)

**Điều kiện kích hoạt**: `notes_required = true`, **hoặc** trong `review_insights` có "đánh giá tiêu cực loại hiểu lầm".

**Nguồn nội dung** (theo thứ tự ưu tiên):
1. **Đánh giá tiêu cực loại hiểu lầm** trong `review_insights` → chuyển thành lời giải thích phòng ngừa (đây là cách dùng có ROI cao nhất)
2. Giới hạn sử dụng vốn có của sản phẩm (điện áp, khả năng tương thích, cách vệ sinh)
3. Điều kiện test của các mục có dấu `*` ở đoạn 2

**Cấm**: chép lại quy tắc chung của sàn cho đủ số lượng.

---

## Đoạn 7 · Khu vực tag từ khóa

**Nội dung**: cài từ khóa để tối ưu lượt hiển thị tìm kiếm.

**Nguồn**: **từ cốt lõi + từ tính năng + từ ngữ cảnh + từ phụ kiện** trong `keyword_classified`.
**Cấm**: đưa vào từ rủi ro, từ không liên quan, từ lặp. Số tag giữ trong khoảng 10–15.

---

# Cấu trúc đầu ra (platform = mercadolivre)

Cấu trúc khác, đổi thành:

```markdown
## 1. Nội dung trang chi tiết

### 1.1 Características principais (mô tả 5 ý)
Mỗi ý = kết hợp thông số kỹ thuật + ngữ cảnh phù hợp + bảo đảm hậu mãi. 5 ý, mỗi ý không quá 120 ký tự.

### 1.2 Ficha Técnica (bảng thông số kỹ thuật)
"Điền được bao nhiêu điền hết bấy nhiêu" — sàn ưu tiên xếp hạng cho listing điền đầy đủ.
Bắt buộc có: Marca / Modelo / Cor / Material / Peso / Dimensões /
         Voltagem / Potência / Garantia / Itens incluídos

### 1.3 Observações
(tạo có điều kiện, giống đoạn 6 của Shopee)
```

---

# STEP 2 · Chắt lọc điểm bán hàng theo tầng

Sau khi viết xong nội dung trang chi tiết, xuất thêm một **bảng phân tầng điểm bán hàng** — đây là đầu vào trực tiếp của module 04 và 05.

```markdown
## 2. Phân tầng điểm bán hàng

| Tầng | Điểm bán hàng | Căn cứ chứng minh | Dùng cho |
|---|---|---|---|
| **Điểm bán hàng chính** (1 ý) | <điểm khác biệt cốt lõi> | <thông số / kết quả test / chất liệu> | Chữ chính trên ảnh chính, hook video, từ khóa tiêu đề |
| **Điểm bán hàng phụ** (3–5 ý) | <từng ý> | <căn cứ> | Chữ trên ảnh chi tiết, đoạn điểm bán hàng trong video, mô tả 5 ý |
| **Điểm bán hàng dự phòng** (một số) | <từng ý> | <căn cứ> | A/B test, nội dung sáng tạo theo ngữ cảnh |
| **Điểm bán hàng bị cấm** | <cách nói phóng đại bị loại> | <vì sao không dùng được> | ⛔ Đưa vào forbidden_words |
```

**Tiêu chí chọn điểm bán hàng chính** (theo thứ tự ưu tiên):
1. Thứ mà đối thủ phần lớn **không có** hoặc **làm kém**
2. Thứ được **nhắc đi nhắc lại** trong đánh giá của người mua
3. Thứ nói rõ được bằng **một con số**
4. Thứ liên quan trực tiếp nhất tới giá

---

# STEP 3 · Kiểm tra tính nhất quán thông số

```markdown
## 3. Kiểm tra tính nhất quán thông số

| Thông số | input.spec_table | Nội dung trang chi tiết | Tiêu đề | Nhất quán |
|---|---|---|---|---|
| <key> | <giá trị> | <giá trị> | <giá trị> | ✅ / ❌ |

Kết quả kiểm tra: <nhất quán toàn bộ / phát hiện N chỗ không nhất quán, đã sửa>
```

> Ba nơi (đầu vào / tiêu đề / trang chi tiết) phải khớp nhau từng ký tự. Đây là tuyến phòng thủ đầu tiên chống lệch thông số giữa các module.

---

# FINAL OUTPUT STRUCTURE

```markdown
## 1. Nội dung trang chi tiết
(xuất cấu trúc tương ứng theo platform)

## 2. Phân tầng điểm bán hàng

## 3. Kiểm tra tính nhất quán thông số

## 4. Quét tuân thủ
(xuất theo 00_system.md; không dính cũng phải ghi "không dính")

## 5. Các trường bàn giao cho module phía sau
- core_selling_point:
- secondary_points: [...]
- spec_table: {...}
- forbidden_words: [...]
- visual_tone_hint:     ← gợi ý tông hình ảnh, để 04/05 thống nhất phong cách
- usage_scope_confirmed: [...]
```

---

# SELF-CHECK

- [ ] Cấu trúc 7 đoạn đầy đủ (khi `notes_required = false` và không có đánh giá tiêu cực loại hiểu lầm, có thể bỏ đoạn 6 và ghi rõ lý do)
- [ ] Mọi ngữ cảnh sử dụng đều nằm trong `usage_scope`
- [ ] `package_content[]` đã liệt kê đầy đủ, không sót
- [ ] Đoạn 2 không có từ ngữ tuyệt đối hóa, mọi cách nói phóng đại đã được viết lại
- [ ] Mỗi giá trị số ở đoạn 4 khớp từng ký tự với `spec_table`
- [ ] Nội dung đoạn 6 có nguồn rõ ràng (quy nguyên nhân đánh giá / giới hạn sản phẩm / điều kiện test), không phải câu sáo rỗng chung chung
- [ ] Đoạn 7 không chứa từ rủi ro
- [ ] Thông tin bảo hành đầy đủ (bắt buộc với Shopee Brazil và ML)
- [ ] Cuối đầu ra đã kèm các trường cho module phía sau + quét tuân thủ
