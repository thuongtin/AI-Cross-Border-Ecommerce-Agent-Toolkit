# Template · Bảng phân tích từ khóa theo 3 bảng xếp hạng

> Bảng làm việc chuẩn cho **SOP 1.8 Bảng từ khóa**.
> **Nguồn dữ liệu**: Xiaduola / công cụ từ khóa tìm kiếm của sàn / mục phân tích từ khóa trong Seller Center.

---

## 1. Vì sao phải xem riêng từng bảng

SOP nói rất rõ:

> Đừng gộp ba chiều dữ liệu lại để xem chung, vì mỗi chiều mang ý nghĩa khác nhau.

| Bảng xếp hạng | Phản ánh điều gì | Nếu chỉ xem riêng dễ hiểu sai thành |
|---|---|---|
| **Top 30 lượng tìm kiếm** | Quy mô nhu cầu — có bao nhiêu người đang tìm | "Nhiều người tìm = dễ bán" (nhưng có thể đã cạnh tranh đến mức hết lời) |
| **Top 30 tỷ lệ cung cầu** | Mức độ cạnh tranh — nhu cầu chia cho nguồn cung | "Ít cạnh tranh = cơ hội" (nhưng có thể chỉ vì nhu cầu cũng nhỏ) |
| **Top 30 tốc độ tăng trưởng** | Xu hướng — nhu cầu đang tăng hay giảm | "Tăng nhanh = phải làm" (nhưng có thể chỉ là trend ngắn hạn) |

**Đối chiếu 3 bảng**: chỉ những từ xuất hiện cùng lúc ở cả ba bảng mới là từ "nhu cầu lớn + còn dư địa cạnh tranh + vẫn đang tăng" — đó mới là từ khóa cơ hội thực sự.

---

## 2. Bảng làm việc

### 2.1 Ba bảng xếp hạng gốc (mỗi bảng 30 từ)

**Bảng 1 · Top 30 lượng tìm kiếm**

| # | Từ khóa | Lượng tìm kiếm | Ghi chú |
|---|---|---|---|
| 1 | | | |
| ... | | | |

**Bảng 2 · Top 30 tỷ lệ cung cầu**

| # | Từ khóa | Tỷ lệ cung cầu | Ghi chú |
|---|---|---|---|
| 1 | | | |
| ... | | | |

**Bảng 3 · Top 30 tốc độ tăng trưởng**

| # | Từ khóa | Tốc độ tăng trưởng | Ghi chú |
|---|---|---|---|
| 1 | | | |
| ... | | | |

---

### 2.2 Lọc từ tần suất cao (đối chiếu 3 bảng)

**Tách từ khóa** của cả ba bảng **thành từ gốc**, rồi đếm số lần lặp lại.

| Từ gốc | Số bảng xuất hiện | Vị trí ở bảng 1 | Vị trí ở bảng 2 | Vị trí ở bảng 3 | Mức ưu tiên |
|---|---|---|---|---|---|
| | **3/3** | | | | 🔴 Cao nhất |
| | 2/3 | | | | 🟡 Cao |
| | 1/3 | | | | ⚪ Bình thường |

> **Tách từ gốc**: `Patinete Elétrico Adulto` tách thành 3 từ gốc `Patinete`, `Elétrico`, `Adulto`, rồi đếm riêng từng từ.

---

### 2.3 Phân loại từ khóa theo 7 nhóm (theo định nghĩa của SOP)

| Nhóm | Định nghĩa | Danh sách từ | Số từ | Dùng ở đâu |
|---|---|---|---|---|
| **Từ cốt lõi** | Cho biết sản phẩm là gì | | | 30 ký tự đầu của tiêu đề |
| **Từ thông số** | Cấu hình như công suất / tải trọng / dung tích | | | Phần thông số trong tiêu đề + phần thông số trong trang chi tiết |
| **Từ đối tượng** | Phù hợp cho người lớn / trẻ em / nam / nữ | | | Phần đối tượng trong tiêu đề |
| **Từ tính năng** | Có yên / gấp gọn được / có giảm xóc | | | Phần tính năng trong tiêu đề + phần điểm bán hàng trong trang chi tiết |
| **Từ ngữ cảnh** | Đi làm / địa hình / di chuyển trong thành phố | | | Phần ngữ cảnh sử dụng trong trang chi tiết |
| **Từ phụ kiện** | Motor / pin / yên / mũ bảo hiểm | | | Phần thông số trong trang chi tiết |
| **Từ rủi ro** | ⛔ Tên thương hiệu / từ vi phạm bản quyền / từ thông số không đúng thực tế | | | **Cấm dùng**, đưa vào `forbidden_words` |

**Ba dạng từ rủi ro điển hình**:

| Dạng | Ví dụ | Vì sao không được dùng |
|---|---|---|
| Từ vi phạm thương hiệu | Tên thương hiệu chưa được ủy quyền | Rủi ro bị khiếu nại vi phạm bản quyền |
| Từ sai thông số | Sản phẩm 18W nhưng có người tìm `65W` | Ghi `65W` vào tiêu đề = khai khống thông số |
| Từ nhạy cảm với sàn | Y tế, chứng nhận, cách nói tuyệt đối | Vi phạm chính sách sàn |

---

### 2.4 Ghép tiêu đề

**Công thức** (SOP 1.8):

```
Từ sản phẩm cốt lõi + Từ đối tượng/ngữ cảnh + Từ thông số chính + Từ tính năng/điểm bán hàng + Từ khóa bổ sung
```

**Ví dụ gốc trong SOP**:

```
Patinete Elétrico Adulto 500W 150kg com Banco Dobrável para Mobilidade Urbana
```

| Thành phần | Từ |
|---|---|
| Từ cốt lõi | `Patinete Elétrico` |
| Từ đối tượng | `Adulto` |
| Từ thông số | `500W` `150kg` |
| Từ tính năng | `com Banco` `Dobrável` |
| Từ ngữ cảnh | `Mobilidade Urbana` |

**Tiêu đề dự phòng** (SOP yêu cầu cuối cùng ra được 2–3 phương án):

| # | Tiêu đề | Số ký tự | Hướng nhấn mạnh | Dùng cho |
|---|---|---|---|---|
| A | | /120 | Nhấn thông số | Link chính |
| B | | /120 | Nhấn ngữ cảnh | Test nhiều link |
| C | | /120 | Nhấn tính năng | Test nhiều link |

---

### 2.5 Phân bổ vị trí cài từ khóa

| Vị trí | Đặt những từ nào | Không đặt những từ nào |
|---|---|---|
| Tiêu đề | Từ cốt lõi + từ thông số tần suất cao + 1–2 từ tính năng | Từ rủi ro, từ tần suất thấp, từ đuôi dài về ngữ cảnh |
| Đoạn 3 trang chi tiết (ngữ cảnh) | Từ ngữ cảnh | Từ thông số (để ở đoạn 4) |
| Đoạn 4 trang chi tiết (thông số) | Từ thông số | Từ ngữ cảnh |
| Đoạn 7 trang chi tiết (tag) | Từ cốt lõi + từ tính năng + từ ngữ cảnh + từ phụ kiện | Từ rủi ro (**tuyệt đối không đặt**) |
| Từ khóa chạy quảng cáo | Từ cốt lõi tần suất cao + từ tính năng chuyển đổi cao | Từ chung chung, từ không có chuyển đổi |

---

## 3. Tự kiểm tra khi điền

- [ ] Mỗi bảng đủ 30 từ, tổng 90 từ, không sót
- [ ] Đã tách từ gốc để thống kê, đánh dấu các từ tần suất cao trùng ở cả 3 bảng
- [ ] Mỗi từ đều được xếp vào một trong 7 nhóm, không có nhóm "khác"
- [ ] Đã liệt kê đầy đủ từ rủi ro và đánh dấu cấm dùng
- [ ] Đủ 5 thành phần của công thức tiêu đề
- [ ] Đã đưa ra 2–3 tiêu đề dự phòng với hướng nhấn mạnh khác nhau
- [ ] Mỗi tiêu đề đều ghi **số ký tự đo thực tế** (không phải ước lượng)
- [ ] Đã phân bổ vị trí cài từ khóa, từ rủi ro không xuất hiện ở bất kỳ vị trí nào được đăng công khai

---

**Tài liệu liên quan**: [Phân rã SOP→Agent](../docs/00_Architecture_SOP_to_Agent.md) · [Quy chuẩn trường dữ liệu theo sàn](../docs/02_Platform_Output_Spec.md) · [03 Listing Creative Agent](../Agents/03_Listing_Creative_Agent/)
