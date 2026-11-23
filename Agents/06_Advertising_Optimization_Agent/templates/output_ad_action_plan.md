# Template đầu ra · Danh sách hành động quảng cáo

> Cấu trúc đầu ra chuẩn của 06 Advertising Optimization Agent.
> **Đơn vị tiêu thụ ở hạ nguồn**: 03 Listing Creative (sửa tiêu đề/trang chi tiết), 04 Product Image (đổi ảnh chính), 07 Review Analysis (phân tích đánh giá).

---

```markdown
# Ad Action Plan · <product_name> · <platform> / <market>

Thời gian tạo: <YYYY-MM-DD>
Phiên bản Prompt: 06-Advertising-Optimization v0.2
Chu kỳ test: <n> ngày
Nguồn dữ liệu: <xuất từ trang quản trị của sàn / tổng hợp thủ công>

---

## 1. Tổng quan

| Chỉ số | Giá trị | Chuẩn | Đánh giá |
|---|---|---|---|
| Tổng lượt hiển thị | | — | — |
| Tổng click | | — | — |
| **CTR tổng** | | 3–5% | |
| Tổng thêm vào giỏ | | — | — |
| **Tỷ lệ thêm vào giỏ tổng** | | > 8% | |
| Tổng đơn | | — | — |
| **Tỷ lệ chuyển đổi tổng** | | > 1% | |
| Tổng chi phí | | — | — |
| Tổng GMV | | — | — |
| **ROAS tổng** | | ≥ ngưỡng hòa vốn | |
| **Lợi nhuận gộp đóng góp ròng** | | > 0 | |

**ROAS hòa vốn**: <giá trị>

**Đánh giá tổng một câu**:

**Độ tin cậy dữ liệu**: <mẫu / chu kỳ có đủ không>

**Công thức tính**
```
CTR = Click ÷ Lượt hiển thị
Tỷ lệ thêm giỏ = Thêm vào giỏ ÷ Click
Tỷ lệ chuyển đổi = Đơn ÷ Click
ROAS = (Đơn × Giá bán) ÷ Chi phí
Đóng góp ròng = Lợi nhuận gộp khả dụng trước quảng cáo × Đơn − Chi phí
```

---

## 2. Chẩn đoán theo từng nhóm quảng cáo

### Nhóm quảng cáo <A> · <từ khóa> (<kiểu khớp>)

**Dữ liệu gốc**

| Hiển thị | Click | CTR | Thêm giỏ | Tỷ lệ thêm giỏ | Đơn | Tỷ lệ chuyển đổi | Chi phí | CPC | CPA | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

**Xét phễu**

| Bước | Hạng mục kiểm tra | Chuẩn | Thực tế | Đạt |
|---|---|---|---|---|
| 1 | CTR | 3–5% | | |
| 2 | Tỷ lệ thêm giỏ | > 8% | | |
| 3 | Tỷ lệ chuyển đổi | > 1% | | |
| 4 | ROAS | ≥ <ngưỡng hòa vốn> | | |

**Kết luận**: <Có hiển thị không có click / Có click không thêm vào giỏ / Có thêm vào giỏ không chuyển đổi / Chi phí cao ROI thấp / Đơn vị khỏe / Thiếu dữ liệu>

**Phân tích nguyên nhân**:

**Danh sách hành động**

| # | Hành động | Đối tượng | Căn cứ | Hiệu quả kỳ vọng | Ưu tiên |
|---|---|---|---|---|---|
| 1 | | | | | |

**Vòng này dứt khoát không động vào**

| Khâu | Lý do không động vào |
|---|---|
| | |

---

(lặp lại mục này cho các nhóm quảng cáo khác)

---

## 3. Tổng hợp hành động

| Ưu tiên | Hành động | Nhóm quảng cáo liên quan | Tỷ trọng ngân sách bị ảnh hưởng | Hiệu quả kỳ vọng | Chu kỳ kiểm tra lại |
|---|---|---|---|---|---|
| 🔴 P0 | | | | | 7 ngày |
| 🟡 P1 | | | | | 7 ngày |
| ⚪ P2 | | | | | 7 ngày |

**Số thay đổi**: <n> hạng mục
**Có chỉ tới cùng một nguyên nhân gốc không**: Có / Không
**Thực hiện cùng đợt / tách vòng**: <kết luận và lý do>

---

## 4. Xử lý quảng cáo không chạy        (xuất có điều kiện)

| Nhóm | Hiển thị | Đánh giá |
|---|---|---|
| | | Thiếu hiển thị, chưa thể vào chẩn đoán phễu |

| Bước | Hành động | Chu kỳ theo dõi |
|---|---|---|
| 1 | Đổi ảnh chính | 1–2 ngày |
| 2 | Tinh chỉnh tiêu đề | 1–2 ngày |
| 3 | Tìm CSKH mở ticket | Theo thời gian phản hồi của sàn |

---

## 5. Tính ngưỡng hòa vốn

### 5.1 Lợi nhuận gộp khả dụng trước quảng cáo

| Hạng mục | Số tiền | % giá bán |
|---|---|---|
| Giá bán | | 100% |
| − Giá vốn | | |
| − Vận chuyển chặng cuối | | |
| − Phí kho/phí xử lý | | |
| − Hoa hồng sàn | | |
| − Hao hụt hoàn hàng | | |
| **= Lợi nhuận gộp khả dụng trước quảng cáo** | | |

### 5.2 Độ nhạy ROAS

| ROAS | Phí QC/đơn | Lợi nhuận gộp còn lại/đơn | % giá bán | Đánh giá |
|---|---|---|---|---|
| | | | | |

### 5.3 Đề xuất hướng xử lý

---

## 6. Mô hình ngân sách

| Hạng mục | Giá trị | Căn cứ |
|---|---|---|
| Ngân sách ngày tối đa đề xuất | | |
| Khoảng ROI mục tiêu đề xuất | | |
| Khoảng test | 7 ngày | SOP |
| Mục tiêu giai đoạn hiện tại | | |

### Nhịp ngân sách theo khung giờ

| Khung giờ (thị trường mục tiêu) | Giờ Bắc Kinh tương ứng | Ngân sách | Lý do |
|---|---|---|---|
| | | | |

---

## 7. Phương án kiểm tra lại

| Hạng mục | Nội dung |
|---|---|
| Thời điểm kiểm tra lại | Ngày thứ 7 sau khi thay đổi |
| Dữ liệu cần thu | Hiển thị/click/thêm giỏ/đơn/chi phí |
| Tiêu chí đạt | Khâu được sửa quay về trên đường chuẩn và ROAS ≥ ngưỡng hòa vốn |
| Xử lý khi không đạt | Quay lại chẩn đoán phễu, **không tiếp tục tăng liều cùng một hành động** |
| Xác nhận nhiễu bên ngoài | |

---

## 8. Quét tuân thủ đề xuất

| Quy tắc | Vi phạm | Xử lý |
|---|---|---|
| G1 Dữ liệu giả | | |
| G2 Cạnh tranh không lành mạnh | | |
| G3 Lách thuật toán | | |
| G4 Đề xuất không thực thi được | | |
| G5 Cam kết thiếu căn cứ | | |

(Khi không vi phạm: `Quét tuân thủ đề xuất: không vi phạm`)

---

## 9. Các trường bàn giao cho module khác

```yaml
breakeven_roas: 0.00
target_roas_range: [0.00, 0.00]
max_daily_budget: 0.00
test_window_days: 7
budget_schedule: {}
symptom_by_group:
  A: ""                        # triệu chứng → chuyển cho 03/04
  B: ""
ctr_fail_groups: []            # → 03 sửa tiêu đề / 04 đổi ảnh chính
atc_fail_groups: []            # → 03 sửa trang chi tiết
cvr_fail_groups: []            # → 03 sửa cách hiển thị giá / 07 phân tích đánh giá
review_needed: false           # → có cần 07 vào cuộc không
```

---

## 10. Nhắc nhở trước khi thực thi

- [ ] Đã xác nhận cách tính chỉ số trên trang quản trị của sàn khớp với bảng này
- [ ] Trước khi thay đổi đã ghi lại dữ liệu baseline (nếu không sẽ không quy nguyên nhân được)
- [ ] Đã xác nhận quan hệ giữa số thay đổi và nguyên tắc "mỗi lần chỉ sửa một việc"
- [ ] Đã kiểm tra quy đổi múi giờ của nhịp ngân sách
- [ ] Đã đưa thời điểm kiểm tra lại vào lịch (ngày thứ 7)
```

---

## Các module hạ nguồn sử dụng thế nào

| Trường | Đơn vị sử dụng | Mục đích |
|---|---|---|
| `ctr_fail_groups` | **03** (`mode = iterate`) | Sửa từ khóa trong tiêu đề |
| `ctr_fail_groups` | **04** (`mode = iterate`) | Đổi ảnh chính |
| `atc_fail_groups` | **03** (`mode = iterate`) | Tối ưu trang chi tiết / chỉnh SKU |
| `cvr_fail_groups` | **03 + 07** | Sửa cách hiển thị giá / phân tích chất lượng đánh giá |
| `breakeven_roas` | Đối chiếu khi kiểm tra lại | Xác định vòng sau có lãi không |
| `review_needed` | **07** | Có khởi động phân tích đánh giá không |

> **Quy tắc vòng khép kín**: 03/04 ở `mode = iterate` bắt buộc nhận `symptom_by_group`, và **chỉ sửa khâu mà triệu chứng chỉ tới**, không được tiện tay sửa phần khác.
