# Template đầu vào · Hồ sơ sản phẩm và 3 bảng từ khóa

> **Cách dùng**: sao chép file này → điền thông tin → gửi cho LLM cùng `prompts/00_system.md` + Task Prompt tương ứng.
> **Trường có dấu `*` là bắt buộc**, thiếu sẽ khiến phần đầu ra tương ứng không tạo được (chi tiết xem INPUT CONTRACT của từng Prompt).

---

## 0. Cấu hình task

```yaml
platform*: shopee              # shopee | mercadolivre | amazon | tiktokshop | shopify
target_market*: Brazil         # quyết định ngôn ngữ đầu ra: Brazil→PT-BR / Mexico→ES
mode*: single                  # single | variant | iterate
variant_count: 3               # bắt buộc khi mode=variant, 2–4
```

---

## 1. Thông tin cơ bản của sản phẩm

```yaml
product_name*: "Carregador Portátil"        # tên gọi chung của sản phẩm (ngôn ngữ mục tiêu)
category*: "Pin / sạc"
sku_internal: ""                            # mã SKU nội bộ (tùy chọn)
```

---

## 2. Bảng thông số (spec_table) ★ Quan trọng nhất

> **Mọi giá trị số xuất hiện trong đầu ra đều phải tìm được mục tương ứng trong bảng này.** Bảng này là nguồn số liệu duy nhất.
> **Thông số chưa chắc chắn: để trống, đừng bịa.** Để trống chỉ mất một điểm bán hàng, bịa sai sẽ dẫn tới trả hàng và bị phạt điểm.

| Key thông số | Giá trị (kèm đơn vị) | Ghi chú |
|---|---|---|
| `marca` | | Không có ủy quyền thương hiệu thì để trống |
| `modelo` | | |
| `cor` | | |
| `material` | | |
| `peso` | | Hệ mét: `380 g` |
| `dimensoes` | | Hệ mét: `14,2 × 6,8 × 2,8 cm` |
| `capacidade` | | Ví dụ `20000 mAh` |
| `potencia_saida` | | Ví dụ `45 W` |
| `voltagem_entrada` | | Ví dụ `100–240 V` |
| `portas` | | Ví dụ `2× USB-A + 1× USB-C` |
| `tempo_recarga` | | Ghi rõ điều kiện test |
| `garantia` | | **Bắt buộc với Shopee Brazil** |
| `certificacoes` | | ⚠️ Chỉ điền chứng nhận **thực sự đang có**, bịa đặt là vi phạm nguy cơ cao |
| `_custom_1` | | Thông số riêng của ngành hàng, thêm bớt tùy nhu cầu |
| `_custom_2` | | |

**Danh sách hàng trong hộp** (`package_content`) — ⚠️ **nguồn đánh giá tiêu cực số một, nhất định phải điền đủ**:

```yaml
package_content*:
  - "1× Carregador Portátil 20000mAh"
  - "1× Cabo USB-C"
  # Những gì không kèm theo cũng phải ghi rõ, ví dụ:
  # - "(Lưu ý: Adaptador de tomada NÃO incluso)"
```

---

## 3. Phạm vi ngữ cảnh sử dụng (usage_scope) ★ Bắt buộc để tuân thủ

> Chỉ những ngữ cảnh được liệt kê ở đây mới được phép xuất hiện trong đoạn "Ngữ cảnh sử dụng" của trang chi tiết. Ngữ cảnh vượt phạm vi sẽ bị xóa.

```yaml
usage_scope*:
  - "Viagem e deslocamentos diários"
  - "Trabalho remoto / home office"
  - "Camping e atividades ao ar livre"
  # Đừng ghi ngữ cảnh mà sản phẩm không làm được
```

**Đừng ghi những ngữ cảnh như sau** (ví dụ): sản phẩm không chống nước thì đừng ghi "hoạt động dưới nước"; sản phẩm không dùng cho y tế thì đừng ghi "sơ cứu y tế".

---

## 4. Điểm bán hàng đầu vào (có thể phóng đại)

> Phần này viết thoải mái, thậm chí viết phóng đại cũng được. Agent sẽ viết lại thành cách diễn đạt kiểm chứng được theo "bảng ánh xạ điểm bán hàng về sự thật".
> Nhưng **mỗi điểm bán hàng đều phải có căn cứ thật**, nếu không sẽ không viết lại được.

```yaml
selling_points_input:
  - "Turbo carga: carrega muito mais rápido que carregador comum"
  - "Bateria gigante, dura dias"
  - "Serve para qualquer celular"
  - "Design compacto e moderno"
  - "Seguro, não esquenta"
```

---

## 5. Thương hiệu và cam kết tuân thủ ★

```yaml
brand_authorization: []      # danh sách thương hiệu đã được ủy quyền. Không có ủy quyền thì ghi []
                             # ví dụ: ["Anker"]  ← chỉ điền khi thực sự đã có ủy quyền

competitor_weakness: []      # điểm yếu của đối thủ (dùng cho cách diễn đạt khác biệt hóa, tùy chọn)
  # ví dụ: ["Đối thủ phần lớn chỉ có đầu ra 18W", "Đối thủ không có màn hình số"]

review_insights: []          # kết quả quy nguyên nhân đánh giá tiêu cực từ 07 Review Analysis (tùy chọn, rất nên có)
  # ví dụ:
  # - type: loại hiểu lầm
  #   content: "Người mua tưởng có kèm cáp sạc"
  #   action: "Ghi rõ cabo não incluso trong đoạn Lưu ý của trang chi tiết"

notes_required*: true        # có tạo đoạn "Lưu ý" hay không
                             # khi có đánh giá tiêu cực loại hiểu lầm nên đặt là true
```

---

## 6. Ba bảng từ khóa ★ Bắt buộc

> Nguồn: 虾多拉 (Xiaduola) / công cụ từ khóa tìm kiếm của sàn / phân tích từ khóa trong Seller Center.
> **Định dạng**: mỗi bảng một từ một dòng, hoặc phân tách bằng dấu phẩy.
> ⚠️ Agent **không tự sinh từ khóa**, chỉ phân loại và ghép. Thiếu ba bảng thì không thực hiện được phân loại từ khóa.

### 6.1 Top 30 theo lượng tìm kiếm

```text
<từ 1>
<từ 2>
...
```

### 6.2 Top 30 theo tỷ lệ cung cầu

```text
<từ 1>
<từ 2>
...
```

### 6.3 Top 30 theo tốc độ tăng trưởng

```text
<từ 1>
<từ 2>
...
```

---

## 7. Tham khảo đối thủ (tùy chọn nhưng nên có)

| Đối thủ | Giá | Doanh số tháng | Tiêu đề | Đặc điểm ảnh chính | Điểm bán hàng cốt lõi | Điểm hay bị đánh giá tiêu cực |
|---|---|---|---|---|---|---|
| | | | | | | |

> Điền phần này thì phần "diễn đạt khác biệt hóa" của Agent sẽ cụ thể hơn; không điền cũng không ảnh hưởng đầu ra cơ bản.

---

## 8. Trường riêng theo mode

### mode = variant

```yaml
variant_directions: []       # để trống thì Agent tự phân bổ theo ba hướng
  # ví dụ: ["Thông số dẫn dắt", "Ngữ cảnh dẫn dắt", "Nhóm khách hàng dẫn dắt"]
```

### mode = iterate (tương ứng SOP 3.6 sửa lại khi quảng cáo không chạy)

```yaml
existing_title: ""
symptom: ""                  # ví dụ: "Có hiển thị nhưng không có click, CTR 1.2% (thấp hơn chuẩn 3%)"
constraints: ""              # ví dụ: "Chỉ sửa từ khóa ở vị trí đầu tiêu đề, không động vào phần thông số"
```

---

## Tự kiểm tra khi điền

- [ ] Đã điền mọi trường bắt buộc có dấu `*`
- [ ] Mọi giá trị số trong `spec_table` đều là **giá trị thật mà tôi chứng minh được**
- [ ] `package_content` đã liệt kê đầy đủ, gồm cả "những gì không kèm theo"
- [ ] Các ngữ cảnh trong `usage_scope` là những gì sản phẩm **thực sự làm được**
- [ ] `brand_authorization` không chứa thương hiệu chưa được ủy quyền
- [ ] `certificacoes` chỉ điền chứng nhận **thực sự đang có**
- [ ] Đã điền ba bảng từ khóa (tổng 90 từ)
- [ ] Tôi hiểu rằng: **tôi chịu trách nhiệm về tính xác thực của thông số**, Agent chỉ đảm bảo được "đầu ra khớp với đầu vào"
