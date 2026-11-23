# Template đầu vào · Brief tạo ảnh

> **Điều kiện tiên quyết**: module này **phụ thuộc vào đầu ra của 03 Listing Creative Agent**.
> Chưa chạy 03 mà chạy 04 thì Agent sẽ báo lỗi ngay —— thiết kế vốn như vậy, không phải bug.

---

## 0. Cấu hình task

```yaml
platform*: shopee              # shopee | mercadolivre | amazon | tiktokshop | shopify
target_market*: Brazil
mode*: standard                # standard | variant | iterate
prompt_language: en            # en (model phổ thông) | zh (model tiếng Trung như Jimeng/Tongyi Wanxiang)
has_product_photo*: true       # Có ảnh chụp thật làm tham chiếu hay không
```

---

## 1. Các trường từ upstream (dán từ đầu ra của 03)

> ⚠️ **Năm trường này là mục chặn, thiếu thì Agent từ chối thực thi.**

```yaml
# ── Quan trọng: dán thẳng từ khối "Các trường giao cho module downstream" trong đầu ra của 03 ──

core_selling_point*: ""        # Ví dụ: "20000mAh com saída de 45W — recarga completa em cerca de 40 minutos"

secondary_points*: []          # Ví dụ:
  # - "Display digital de bateria"
  # - "3 saídas (2× USB-A + 1× USB-C)"

spec_table*: {}                # Dán thẳng spec_table của 03

forbidden_words*: []           # Ví dụ: ["iPhone", "100% Original", "À Prova de Água"]

usage_scope_confirmed*: []     # Ví dụ:
  # - "Viagem e deslocamentos diários"
  # - "Trabalho remoto / home office"
```

---

## 2. Thông tin sản phẩm và hình ảnh

```yaml
product_name*: ""              # Ví dụ: "Carregador Portátil"
category*: ""                  # Ví dụ: "Pin / sạc"
visual_tone_hint: ""           # Kế thừa từ 03, ví dụ: "Tecnológico e limpo — fundo claro, tons de cinza e azul"
```

### Mô tả ngoại hình (giúp ra ảnh chính xác hơn)

```yaml
appearance:
  color: ""                    # Ví dụ: "Preto fosco com detalhes em cinza"
  material: ""                 # Ví dụ: "ABS + PC com acabamento antichamas"
  shape: ""                    # Ví dụ: "Retangular com cantos arredondados"
  key_features: []             # Ví dụ: ["Display LED frontal", "3 portas na face superior"]
```

---

## 3. Khai báo chứng nhận ★ Then chốt về tuân thủ

```yaml
certifications: []             # ⚠️ Chỉ điền chứng nhận [thực sự có], không có thì để trống []
                               # Ví dụ: ["ANATEL"]  ← chỉ điền khi thật sự đã có
                               # Để trống = Agent sẽ không tạo bất kỳ ảnh chứng nhận nào
```

> **Để trống mục này hoàn toàn không sao, điền sai mới là vấn đề.** Làm giả dấu chứng nhận là vi phạm nguy cơ cao trên sàn.

---

## 4. Đóng gói và bảo hành (dùng cho ảnh 8 / ảnh 9)

```yaml
package_content*: []           # Kế thừa từ 03, liệt kê đầy đủ
  # - "1× Carregador Portátil 20000mAh 45W"
  # - "1× Cabo USB-C 30 cm"
  # - "(Não incluso: adaptador de tomada)"   ← ghi rõ "không có gì"

warranty*: ""                  # Ví dụ: "6 meses contra defeito de fabricação"
warranty_scope: ""             # Ví dụ: "Não cobre danos por mau uso ou queda"
support_channel: ""            # Ví dụ: "Atendimento pelo chat do Shopee"
```

---

## 5. Tham chiếu hình ảnh (tùy chọn)

```yaml
reference:
  competitor_image_notes: ""   # Nhận xét về ảnh của đối thủ (đừng bê nguyên creative về dùng!)
  style_reference: ""          # Ví dụ: "Phong cách chụp sản phẩm tối giản giống website chính thức của Anker"
  avoid: []                    # Ví dụ: ["Nền lòe loẹt", "Yếu tố hoạt hình", "Quá nhiều slogan tiếng Anh"]
```

> ⚠️ **Đừng dán link ảnh của đối thủ làm đầu vào image-to-image** —— liên quan đến bản quyền, và có thể bị coi là ăn cắp ảnh.

---

## 6. Các trường riêng theo mode

### mode = variant

```yaml
variant_directions: []
  # Ví dụ: ["Điểm bán hàng của ảnh chính là công suất", "Điểm bán hàng của ảnh chính là dung lượng"]
  # Để trống thì Agent tự phân bổ hai hướng khác biệt hóa
```

### mode = iterate (tương ứng SOP 3.6 quảng cáo không có click → đổi ảnh chính)

```yaml
existing_main_image_desc: ""   # Mô tả khung hình của ảnh chính hiện tại
symptom: ""                    # Ví dụ: "Có lượt hiển thị nhưng không có click, CTR 1.2% (thấp hơn mức chuẩn 3–5%)"
change_scope: "main_image_only"  # Chỉ sửa ảnh chính, 8 ảnh còn lại giữ nguyên
```

---

## Tự kiểm tra khi điền

- [ ] Năm trường chặn (`core_selling_point` / `secondary_points` / `spec_table` / `forbidden_words` / `usage_scope_confirmed`) đã được dán từ 03
- [ ] `certifications` để trống hoặc chỉ điền chứng nhận thực sự có
- [ ] `package_content` có ghi "không có gì"
- [ ] Không dán ảnh của đối thủ làm creative cho image-to-image
- [ ] Tôi hiểu: **ảnh 8 (danh sách đóng gói) bắt buộc chụp thật**, AI tạo ra sẽ gây đánh giá tiêu cực về thiếu phụ kiện
- [ ] Tôi hiểu: **chữ trong ảnh do công cụ thiết kế chèn ở hậu kỳ**, không dựa vào model tạo ảnh để render
