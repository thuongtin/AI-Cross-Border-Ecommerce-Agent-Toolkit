# TASK · Phân loại từ khóa và tạo tiêu đề

> Dùng kèm: `00_system.md` (System Prompt) + `templates/input_product_brief.md` (đầu vào đã điền)

Tương ứng SOP **1.8 Bảng từ khóa** + **3.3 Xây dựng Listing** + **3.4 Khởi động một sản phẩm nhiều link**.

---

# INPUT

Bắt buộc có các trường sau, thiếu bất kỳ trường nào thì dừng và báo lỗi theo INPUT CONTRACT của `00_system.md`:

| Trường | Mô tả | Ảnh hưởng khi thiếu |
|---|---|---|
| `platform` | Sàn mục tiêu | Không xác định được giới hạn ký tự và cấu trúc |
| `target_market` | Thị trường mục tiêu | Không xác định được ngôn ngữ đầu ra |
| `mode` | `single` / `variant` / `iterate` | Không xác định được số bộ đầu ra |
| `product_name` | Tên gọi chung của sản phẩm (ngôn ngữ bản địa) | Không tạo được tiêu đề |
| `category` | Ngành hàng | Không áp dụng được kiến thức ngành hàng |
| `keyword_top30_by_search_volume[]` | Top 30 theo lượng tìm kiếm | Phân loại từ khóa thiếu một chiều |
| `keyword_top30_by_supply_demand[]` | Top 30 theo tỷ lệ cung cầu | Phân loại từ khóa thiếu một chiều |
| `keyword_top30_by_growth[]` | Top 30 theo tốc độ tăng trưởng | Phân loại từ khóa thiếu một chiều |
| `spec_table` | Bảng thông số (cặp key-value) | **Không xuất được bất kỳ giá trị số nào, tiêu đề sẽ thiếu toàn bộ từ thông số** |
| `usage_scope[]` | Các ngữ cảnh sử dụng được phép nêu | Không đánh giá được tính hợp lệ của từ ngữ cảnh |
| `brand_authorization` | Thương hiệu đã được ủy quyền (có thể để trống) | Không chạy được bước chặn tên thương hiệu R2 |

Trường tùy chọn:
- Khi `mode = variant` cần `variant_count` (2–4, mặc định 3)
- Khi `mode = iterate` cần `existing_title` + `symptom` (mô tả triệu chứng)

---

# STEP 1 · Chia từ khóa thành 7 nhóm

**Gộp và loại trùng** từ khóa của ba bảng xếp hạng, sau đó phân loại lần lượt theo 7 nhóm SOP định nghĩa.

## Định nghĩa các nhóm

| Nhóm | Định nghĩa | Ví dụ (Brazil / xe scooter điện) |
|---|---|---|
| **Từ cốt lõi** | Cho biết sản phẩm là gì, là cửa vào tìm kiếm đầu tiên của người mua | `Patinete Elétrico`, `Scooter Elétrico` |
| **Từ thông số** | Cho biết cấu hình như công suất, tải trọng, dung lượng, kích thước | `500W`, `150kg`, `10Ah` |
| **Từ nhóm khách hàng** | Cho biết sản phẩm phù hợp với ai | `Adulto`, `Infantil`, `Unissex` |
| **Từ tính năng** | Cho biết sản phẩm có tính năng gì | `Dobrável`, `com Banco`, `com Suspensão` |
| **Từ ngữ cảnh** | Cho biết dùng trong ngữ cảnh nào | `Mobilidade Urbana`, `Off Road`, `Viagem` |
| **Từ phụ kiện** | Cho biết kèm theo / đi cùng những gì | `com Carregador`, `com Capacete`, `Bateria` |
| **Từ rủi ro** | **Cấm dùng**: tên thương hiệu, từ vi phạm bản quyền, từ thông số không khớp với hàng thật | Tên thương hiệu chưa được ủy quyền, giá trị số mâu thuẫn với `spec_table` |

## Định dạng đầu ra

```markdown
## 1. Bảng phân loại từ khóa

### 1.1 Trích từ tần suất cao

| Từ | Số bảng xuất hiện | Xuất hiện ở bảng nào | Thuộc nhóm |
|---|---|---|---|
| <từ> | 3/3 | Lượng tìm kiếm / Tỷ lệ cung cầu / Tốc độ tăng trưởng | Từ cốt lõi |
| ... | | | |

> Từ xuất hiện ở ≥2 bảng là "từ tần suất cao", có độ ưu tiên cao nhất.

### 1.2 Tổng hợp phân loại

| Nhóm | Số từ | Danh sách từ | Dùng ở đâu |
|---|---|---|---|
| Từ cốt lõi | 3 | ... | 30 ký tự đầu của tiêu đề |
| Từ thông số | 11 | ... | Đoạn thông số của tiêu đề + đoạn thông số của trang chi tiết |
| Từ nhóm khách hàng | 4 | ... | Đoạn nhóm khách hàng của tiêu đề |
| Từ tính năng | 8 | ... | Đoạn tính năng của tiêu đề + đoạn điểm bán hàng của trang chi tiết |
| Từ ngữ cảnh | 6 | ... | Đoạn ngữ cảnh của trang chi tiết |
| Từ phụ kiện | 5 | ... | Đoạn thông số của trang chi tiết |
| Từ rủi ro | 6 | ... | ⛔ Cấm dùng, đưa vào forbidden_words |

### 1.3 Danh sách cách ly từ rủi ro (để 04/05 phía sau chặn cứng)

| Từ rủi ro | Loại rủi ro | Lý do |
|---|---|---|
| <từ> | Vi phạm thương hiệu | Chưa được khai báo trong brand_authorization |
| <từ> | Thông số không khớp | Mâu thuẫn với spec_table (thực tế là X, từ này ngụ ý Y) |
```

**Quy tắc**: từ rủi ro **không được xuất hiện trong bất kỳ nội dung đầu ra nào**, nhưng phải được **liệt kê đầy đủ** trong bảng 1.3 — vì 04/05 cần nó để chặn.

---

# STEP 2 · Tạo tiêu đề

## Công thức ghép (SOP 1.8)

```
Từ sản phẩm cốt lõi + từ nhóm khách hàng/ngữ cảnh + từ thông số cốt lõi + từ điểm bán hàng tính năng + từ khóa bổ sung
```

Ví dụ gốc trong SOP:

```
Patinete Elétrico Adulto 500W 150kg com Banco Dobrável para Mobilidade Urbana
```
Phân tích: từ cốt lõi `Patinete Elétrico` / từ nhóm khách hàng `Adulto` / từ thông số `500W` `150kg` / từ tính năng `com Banco` `Dobrável` / từ ngữ cảnh `Mobilidade Urbana`

## Yêu cầu khi tạo

1. **Tuân thủ nghiêm giới hạn ký tự của input.platform**, khi xuất phải **ghi rõ số ký tự thực tế** (định dạng: `116/120`)
2. **Từ khóa chính đặt lên đầu** (Shopee: trong 30 ký tự đầu; ML: đứng đầu tiên)
3. **Từ thông số chỉ được dùng giá trị thật trong `spec_table`**
4. **Không lặp nghĩa** (`Patinete Elétrico Patinete Elétrico Scooter` ❌)
5. **Không nhồi từ không liên quan**
6. Khi `mode = single` xuất **3 bản dự phòng**, mỗi bản một hướng trọng tâm khác nhau
7. Khi `mode = variant` xuất **variant_count bộ phương án khác biệt hóa**, **hướng trọng tâm của mỗi bộ phải khác nhau** (chi tiết bên dưới)
8. Khi `mode = iterate` **chỉ xuất 1 bộ phương án sửa**, và yêu cầu: chỉ rõ đã sửa ở vị trí nào, vì sao sửa như vậy

## Khác biệt đầu ra giữa ba chế độ

### mode = single

```markdown
## 2. Phương án tiêu đề (3 bản dự phòng)

| # | Tiêu đề | Số ký tự | Hướng trọng tâm | Phù hợp khi |
|---|---|---|---|---|
| A | <tiêu đề> | 116/120 | Thông số dẫn dắt | Muốn traffic tìm kiếm chính xác |
| B | <tiêu đề> | 112/120 | Ngữ cảnh dẫn dắt | Mở rộng traffic rộng |
| C | <tiêu đề> | 118/120 | Tính năng dẫn dắt | Làm nổi bật điểm bán hàng khác biệt |

**Đề xuất**: A (lý do: <một câu>)
```

### mode = variant (tương ứng SOP 3.4 test nhiều link / SOP 2.3 khác biệt hóa giữa nhiều shop)

Mỗi bộ đi một **hướng trọng tâm khác nhau** để test riêng:

| Biến thể | Hướng trọng tâm | Điểm khác của tiêu đề | Mục đích test |
|---|---|---|---|
| 1 | Thông số dẫn dắt | Thông số đặt lên đầu, mật độ con số cao | Test CTR của từ khóa tìm kiếm chính xác |
| 2 | Ngữ cảnh dẫn dắt | Từ ngữ cảnh đặt lên đầu, giảm nhấn thông số | Test tỷ lệ chuyển đổi của traffic rộng |
| 3 | Nhóm khách hàng dẫn dắt | Từ nhóm khách hàng đặt lên đầu | Test mức độ đồng cảm của nhóm khách hàng cụ thể |

**Yêu cầu cứng**: giữa các biến thể phải có **khác biệt thực chất**, không được chỉ đổi thứ tự từ. Nếu hai biến thể giống nhau quá 70%, bắt buộc viết lại một trong hai và giải thích.

### mode = iterate (tương ứng SOP 3.6 sửa lại khi quảng cáo không chạy)

```markdown
## 2. Phương án sửa tiêu đề

- Hiện trạng: <existing_title>
- Triệu chứng: <symptom>
- Nhận định: <vì sao xuất hiện triệu chứng này, ứng với quy tắc nào trong SOP>
- Điểm sửa: <cụ thể sửa ở đâu> (chỉ sửa vị trí cần thiết, phần còn lại giữ nguyên)
- Sau khi sửa: <new_title> (<số ký tự>)
- Hiệu quả kỳ vọng: <một câu>
```

---

# STEP 3 · Tự kiểm tra tuân thủ tiêu đề

```markdown
## 3. Tự kiểm tra tiêu đề

| Mục kiểm tra | Kết quả | Ghi chú |
|---|---|---|
| Số ký tự ≤ <giới hạn> | ✅ / ❌ | Thực tế <n> ký tự |
| Từ khóa chính nằm trong 30 ký tự đầu | ✅ / ❌ | Vị trí: bắt đầu từ ký tự thứ <n> |
| Không có từ khuyến mãi | ✅ / ❌ | |
| Không có emoji / ký tự đặc biệt | ✅ / ❌ | |
| Không có từ viết hoa toàn bộ | ✅ / ❌ | |
| Không nhồi từ lặp lại | ✅ / ❌ | |
| Không có tên thương hiệu chưa ủy quyền | ✅ / ❌ | |
| Mọi giá trị số đều truy được về spec_table | ✅ / ❌ | Liệt kê từng mục |
| Đơn vị hệ mét | ✅ / ❌ | |
| Viết hoa chữ cái đầu đúng quy cách | ✅ / ❌ | |
```

---

# FINAL OUTPUT STRUCTURE

Xuất nghiêm theo thứ tự này, không thêm bớt chương:

```markdown
## 1. Bảng phân loại từ khóa
### 1.1 Trích từ tần suất cao
### 1.2 Tổng hợp phân loại
### 1.3 Danh sách cách ly từ rủi ro

## 2. Phương án tiêu đề
(xuất định dạng tương ứng theo mode)

## 3. Tự kiểm tra tiêu đề

## 4. Quét tuân thủ
(xuất theo COMPLIANCE GUARD của 00_system.md; không dính cũng phải ghi "không dính")

## 5. Các trường bàn giao cho module phía sau
- core_selling_point:
- keyword_classified: { từ cốt lõi: [...], từ thông số: [...], ... }
- forbidden_words: [...]
- title_final:
```

> Đoạn 5 là hợp đồng đầu vào (input contract) của 04 Product Image và 05 Product Video, **không được bỏ**.

---

# SELF-CHECK

- [ ] Từ khóa của ba bảng đã được gộp và loại trùng toàn bộ, không sót
- [ ] Mỗi từ đều được xếp vào một trong 7 nhóm, không có nhóm "khác"
- [ ] Từ rủi ro đã được liệt kê đầy đủ và không xuất hiện trong tiêu đề
- [ ] Số ký tự tiêu đề là **giá trị đo thực tế**, không phải ước lượng
- [ ] Khi `mode = variant`, độ giống nhau giữa các biến thể < 70%
- [ ] Mọi giá trị số trong tiêu đề đều tìm được trong `spec_table`
- [ ] Cuối đầu ra đã kèm quét tuân thủ + các trường cho module phía sau
