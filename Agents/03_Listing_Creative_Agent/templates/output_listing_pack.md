# Template đầu ra · Bộ nội dung Listing

> Cấu trúc đầu ra chuẩn của Agent. **Các module phía sau (04 Product Image / 05 Product Video) phụ thuộc vào các trường ở đoạn 5**, không được bỏ.

---

```markdown
# Listing Pack · <product_name> · <platform> / <target_market>

Thời gian tạo: <YYYY-MM-DD>
Phiên bản Prompt: 03-Listing-Creative v0.1
Chế độ: <single | variant | iterate>

---

## 1. Bảng phân loại từ khóa

### 1.1 Trích từ tần suất cao

| Từ | Số bảng xuất hiện | Xuất hiện ở bảng nào | Thuộc nhóm |
|---|---|---|---|
| | /3 | | |

### 1.2 Tổng hợp phân loại

| Nhóm | Số từ | Danh sách từ | Dùng ở đâu |
|---|---|---|---|
| Từ cốt lõi | | | 30 ký tự đầu của tiêu đề |
| Từ thông số | | | Tiêu đề + đoạn thông số của trang chi tiết |
| Từ nhóm khách hàng | | | Đoạn nhóm khách hàng của tiêu đề |
| Từ tính năng | | | Đoạn tính năng của tiêu đề + đoạn điểm bán hàng của trang chi tiết |
| Từ ngữ cảnh | | | Đoạn ngữ cảnh của trang chi tiết |
| Từ phụ kiện | | | Đoạn thông số của trang chi tiết |
| Từ rủi ro | | | ⛔ Cấm dùng |

### 1.3 Danh sách cách ly từ rủi ro

| Từ rủi ro | Loại rủi ro | Lý do |
|---|---|---|
| | Vi phạm thương hiệu / Thông số không khớp / Nhạy cảm | |

---

## 2. Phương án tiêu đề

| # | Tiêu đề | Số ký tự | Hướng trọng tâm |
|---|---|---|---|
| A | | /120 | |
| B | | /120 | |
| C | | /120 | |

**Đề xuất**: <A/B/C> — <lý do>

---

## 3. Nội dung trang chi tiết

### Đoạn 1 · Lời chào
### Đoạn 2 · Điểm bán hàng cốt lõi
| # | Điểm bán hàng | Số liệu chứng minh |
|---|---|---|

### Đoạn 3 · Ngữ cảnh sử dụng
| # | Ngữ cảnh | Cách dùng cụ thể |
|---|---|---|

### Đoạn 4 · Thông số chi tiết
| Thông số | Giá trị |
|---|---|

**Danh sách hàng trong hộp**:
- 

### Đoạn 5 · Cam kết hậu mãi và CSKH
### Đoạn 6 · Lưu ý
### Đoạn 7 · Khu vực tag từ khóa
`tag1, tag2, ...`

---

## 4. Phân tầng điểm bán hàng

| Tầng | Điểm bán hàng | Căn cứ chứng minh | Dùng cho |
|---|---|---|---|
| **Điểm bán hàng chính** | | | Chữ chính trên ảnh chính / hook video / tiêu đề |
| Điểm bán hàng phụ | | | Ảnh chi tiết / đoạn điểm bán hàng trong video |
| Điểm bán hàng dự phòng | | | A/B test |
| Điểm bán hàng bị cấm | | | ⛔ |

---

## 5. Các trường bàn giao cho module phía sau ★

```yaml
core_selling_point: ""          # điểm bán hàng chính trong một câu → chữ chính trên ảnh chính của 04 / hook video của 05
secondary_points: []            # danh sách điểm bán hàng phụ → chữ trên ảnh chi tiết của 04 / đoạn điểm bán hàng của 05
spec_table: {}                  # bảng thông số → ảnh thông số của 04 / chú thích thông số của 05
forbidden_words: []             # từ cấm → 04/05 chặn cứng
keyword_classified: {}          # phân loại từ khóa → điểm bán hàng trên ảnh chính của 04 / phụ đề của 05
title_final: ""                 # tiêu đề cuối cùng → CTA cuối video của 05
visual_tone_hint: ""            # gợi ý tông hình ảnh → 04/05 thống nhất phong cách
usage_scope_confirmed: []       # các ngữ cảnh đã xác nhận được dùng
```

---

## 6. Kiểm tra tính nhất quán thông số

| Thông số | spec_table | Trang chi tiết | Tiêu đề | Nhất quán |
|---|---|---|---|---|
| | | | | ✅ |

---

## 7. Tự kiểm tra khi tạo

### Tự kiểm tra tiêu đề
| Mục kiểm tra | Kết quả |
|---|---|
| Số ký tự ≤ giới hạn | |
| Từ khóa chính nằm trong 30 ký tự đầu | |
| Không có từ khuyến mãi / emoji / ký tự đặc biệt / viết hoa toàn bộ | |
| Không nhồi từ lặp lại | |
| Không có tên thương hiệu chưa ủy quyền | |
| Mọi giá trị số đều truy được nguồn | |

### Quét tuân thủ
| Quy tắc | Số lần dính | Xử lý |
|---|---|---|
| R1 Từ ngữ tuyệt đối hóa | | |
| R2 Tên thương hiệu chưa được ủy quyền | | |
| R3 Khai khống thông số | | |
| R4 Từ khuyến mãi trong tiêu đề | | |
| R5 Nội dung nhạy cảm | | |
| R6 Ngữ cảnh vượt phạm vi | | |
| R7 Chứng cứ giả mạo | | |

**Chi tiết các mục dính**:
| # | Quy tắc | Bản gốc | Vấn đề | Sau khi viết lại |
|---|---|---|---|---|

(Khi không dính: `Quét tuân thủ: không dính`)

### Tự kiểm tra cấu trúc
| Mục kiểm tra | Kết quả |
|---|---|
| Cấu trúc 7 đoạn đầy đủ | |
| Mọi ngữ cảnh đều trong phạm vi | |
| Danh sách hàng trong hộp đầy đủ | |
| Thông tin bảo hành đầy đủ | |
| Cuối đầu ra đã kèm các trường cho module phía sau | |

---

## 8. Nhắc nhở trước khi đăng

- [ ] Đã vào Seller Center kiểm tra lại quy tắc hiện hành của sàn (số ký tự / trường thông tin / hình ảnh)
- [ ] Đã đối chiếu tính xác thực của thông số (Agent không kiểm chứng được bản thân đầu vào)
- [ ] Khi đăng bán trên nhiều shop đã làm khác biệt hóa
- [ ] Đã ghi lại số phiên bản Prompt lần này
```

---

## Module phía sau sử dụng như thế nào

### 04 Product Image Agent cần

| Trường | Mục đích |
|---|---|
| `core_selling_point` | Chữ chính trên ảnh chính |
| `secondary_points[]` | Chữ trên ảnh chi tiết |
| `spec_table` | Ảnh thông số |
| `forbidden_words[]` | Chặn cứng chữ trong ảnh |
| `visual_tone_hint` | Thống nhất phong cách |

### 05 Product Video Agent cần

| Trường | Mục đích |
|---|---|
| `core_selling_point` | Hook 3 giây đầu |
| `secondary_points[]` | Kịch bản đoạn điểm bán hàng |
| `spec_table` | Chú thích thông số |
| `forbidden_words[]` | Chặn cứng phụ đề |
| `title_final` | CTA cuối video |
| `usage_scope_confirmed[]` | Cảnh quay theo ngữ cảnh |

> **Quy tắc chặn**: khi `core_selling_point` hoặc `forbidden_words` trống, 04/05 bắt buộc từ chối thực hiện và báo lỗi, chứ không được tự suy đoán.
