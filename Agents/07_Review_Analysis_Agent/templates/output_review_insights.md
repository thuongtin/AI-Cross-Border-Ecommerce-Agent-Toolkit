# Template đầu ra · Báo cáo insight đánh giá

> Cấu trúc đầu ra chuẩn của 07 Review Analysis Agent.
> **Bên sử dụng ở hạ nguồn**: 03 Listing Creative (bổ sung đoạn Lưu ý / sửa cách diễn đạt / chọn điểm bán hàng), 04 Product Image (bổ sung ảnh), 05 Product Video (chặn phụ đề).

---

```markdown
# Review Insights · <product_name> · <platform> / <market>

Thời gian tạo: <YYYY-MM-DD>
Phiên bản Prompt: 07-Review-Analysis v0.2
Phạm vi phân tích: <own / competitor / both>
Cỡ mẫu: <n> đánh giá

---

## 1. Tổng quan dữ liệu

| Hạng mục | Giá trị | Tỷ trọng |
|---|---|---|
| Tổng số đánh giá | | 100% |
| Tích cực (4–5 sao) | | |
| Trung lập (3 sao) | | |
| Tiêu cực (1–2 sao) | | |
| Số đánh giá có ảnh | | |
| Nguồn dữ liệu | <phía mình / đối thủ A / đối thủ B> | — |

**Đánh giá cỡ mẫu**: <đủ / hơi nhỏ / chưa đủ (chỉ để tham khảo)>

**Giới hạn dữ liệu**: <sàn xóa đánh giá / sai lệch hiểu ngôn ngữ / mẫu chưa đủ>

---

## 2. Phân tích đánh giá tích cực

### 2.1 Vì sao người mua hài lòng

| # | Lý do hài lòng | Số lần nhắc | Tỷ trọng | Nguyên văn tiêu biểu |
|---|---|---|---|---|
| | | | | |

### 2.2 Tính năng được nhắc đi nhắc lại

| Tính năng | Số lần nhắc | Sắc thái cảm xúc | Nguyên văn tiêu biểu |
|---|---|---|---|
| | | | |

### 2.3 Đối chiếu hiệu quả điểm bán hàng

| Điểm bán hàng | Số lần nhắc | Listing hiện tại có làm nổi bật không | Đề xuất |
|---|---|---|---|
| | | ✅ / ❌ | |

### 2.4 Mức hài lòng về vận chuyển và hậu mãi

| Khía cạnh | Nhắc tích cực | Nhắc tiêu cực | Cảm xúc ròng |
|---|---|---|---|
| Tốc độ giao hàng | | | |
| Độ nguyên vẹn của đóng gói | | | |
| Phản hồi CSKH | | | |

### 2.5 Cảm nhận về giá

| Loại | Số lần nhắc | Nguyên văn tiêu biểu |
|---|---|---|
| Thấy đáng tiền | | |
| Thấy hơi đắt | | |

---

## 3. Quy nguyên nhân đánh giá tiêu cực

### 3.1 Phân bố nguyên nhân

| # | Nhóm nguyên nhân | Số lượng | Tỷ trọng | Bên chịu trách nhiệm | Sửa được bằng nội dung không |
|---|---|---|---|---|---|
| 1 | **Hiểu lầm** ⭐ | | | Phía mình (trang chi tiết) | ✅ |
| 2 | Lỗi chất lượng sản phẩm | | | Nhà cung cấp | ❌ |
| 3 | Thông số không như kỳ vọng | | | Phía mình | ✅ |
| 4 | Thiếu phụ kiện | | | Phía mình (danh sách đóng gói) | ✅ |
| 5 | Giao hàng chậm | | | Đơn vị vận chuyển | ⚠️ |
| 6 | Khó sử dụng | | | Phía mình (sách hướng dẫn) | ✅ |
| 7 | Hậu mãi kém | | | Phía mình | ✅ |
| 8 | Hư hỏng / lỗi / trả hàng | | | Đơn vị vận chuyển / nhà cung cấp | ❌ |
| | **Tổng** | | 100% | | |

**Tổng các mục khắc phục được**: <n> đánh giá, chiếm **<%>** tổng đánh giá tiêu cực

### 3.2 Chi tiết từng nhóm

#### Nhóm <n> · <tên nhóm> (<n> đánh giá)

| # | Nguyên văn | Người mua kỳ vọng/tưởng | Thực tế | Phán định |
|---|---|---|---|---|
| | | | | |

---

## 4. Phán định đánh giá tiêu cực loại hiểu lầm

| # | Nguyên văn đánh giá tiêu cực | Người mua tưởng | Thực tế (trường căn cứ) | Listing hiện tại có nhắc không | Phán định | Hành động vá |
|---|---|---|---|---|---|---|
| | | | | | | |

**Tổng hợp loại phán định**

| Phán định | Số lượng |
|---|---|
| Thiếu giải thích | |
| Giải thích không nổi bật | |
| Người mua không đọc | |

---

## 5. Đề xuất vá trang chi tiết

### 5.1 Mục thêm mới / chỉnh sửa (→ 03)

| # | Đánh giá tiêu cực tương ứng | Vị trí viết | Nội dung (ngôn ngữ mục tiêu) | Giải thích (tiếng Việt) |
|---|---|---|---|---|
| | | | | |

### 5.2 Ảnh cần bổ sung (→ 04)

| # | Đánh giá tiêu cực tương ứng | Vị trí ảnh | Chữ trên ảnh | Mô tả |
|---|---|---|---|---|
| | | | | |

### 5.3 Cách diễn đạt cần sửa (→ 03)

| # | Diễn đạt gốc | Vấn đề | Diễn đạt đề xuất |
|---|---|---|---|
| | | | |

---

## 6. Lằn ranh đỏ thông số

| # | Thông số bị phàn nàn | Người mua kỳ vọng | Giá trị thực tế trong `spec_table` | Ứng viên từ cấm | Lý do |
|---|---|---|---|---|---|
| | | | | | |

---

## 7. Xếp hạng điểm bán hàng

| Hạng | Điểm bán hàng | Số lần nhắc | Mức độ cảm xúc | Điểm tổng hợp | Hành động đề xuất |
|---|---|---|---|---|---|
| | | | | | |

---

## 8. So sánh đối thủ            (xuất có điều kiện)

### 8.1 Đối thủ bán được nhờ đâu

| Đối thủ | Điểm tập trung đánh giá tích cực | Điểm tập trung đánh giá tiêu cực | Lợi thế cạnh tranh (moat) |
|---|---|---|---|
| | | | |

### 8.2 Phía mình vs đối thủ

| Khía cạnh | Phía mình | Đối thủ A | Đối thủ B |
|---|---|---|---|
| Điểm hay được khen | | | |
| Điểm hay bị chê | | | |
| Tỷ trọng đánh giá có ảnh | | | |

### 8.3 Cơ hội bỏ ngỏ

| Cơ hội | Căn cứ | Hành động cụ thể |
|---|---|---|
| | | |

---

## 9. Trả lời mục tiêu phân tích (bảy câu hỏi của SOP 1.6)

| # | Câu hỏi | Kết luận | Căn cứ |
|---|---|---|---|
| 1 | Đối thủ bán được nhờ đâu | | |
| 2 | Người mua thực sự quan tâm điều gì | | |
| 3 | **Điểm bán hàng nào bắt buộc phải viết** | | |
| 4 | **Thông số nào không được viết bừa** | | |
| 5 | **Vấn đề nào cần giải thích trước trên trang chi tiết** | | |
| 6 | Phía mình nên làm nổi bật khác biệt gì | | |
| 7 | Phía mình cần tránh rủi ro hậu mãi gì | | |

---

## 10. Đánh giá khả năng khắc phục

| Hạng mục | Số lượng | Tỷ trọng |
|---|---|---|
| Tổng đánh giá tiêu cực | | 100% |
| **Khắc phục được bằng sửa mô tả / sửa ảnh** | | |
| Cần sửa sản phẩm / nhà cung cấp | | |
| Cần sửa vận chuyển | | |

**Thứ tự ưu tiên khắc phục**: <xếp theo «tần suất xuất hiện ÷ chi phí khắc phục»>

---

## 11. Đề xuất mẫu câu CSKH        (xuất có điều kiện)

| Tình huống | Mẫu câu (ngôn ngữ mục tiêu) | Mô tả |
|---|---|---|
| | | |

**Kiểm tra nguyên tắc mẫu câu**
- [ ] Không dùng lợi ích dụ dỗ xóa đánh giá
- [ ] Không dùng lý do sai sự thật để giải thích thông số không khớp
- [ ] Đã nói đúng sự thật + đưa ra phương án giải quyết

---

## 12. Quét tuân thủ phân tích

| Quy tắc | Vi phạm | Xử lý |
|---|---|---|
| C1 Dụ dỗ xóa đánh giá | | |
| C2 Báo cáo có tổ chức | | |
| C3 Đánh giá giả | | |
| C4 Tự suy đoán thật/giả của đánh giá | | |
| C5 Làm lộ thông tin riêng tư của người mua | | |

(Khi không vi phạm: `Quét tuân thủ phân tích: không vi phạm`)

---

## 13. Các trường bàn giao cho module khác

```yaml
selling_points_ranked: []          # → 03 chọn điểm bán hàng cho tiêu đề/ảnh chính
forbidden_words_candidates: []     # → 03/04/05 chặn cứng
review_patch_suggestions: []       # → 03 đoạn Lưu ý trang chi tiết
packaging_clarity_needed: false    # → 04 ảnh danh sách đóng gói
scene_limit_image_needed: false    # → 04 ảnh giới hạn tình huống
fixable_ratio: 0.00

# Chỉ số chính (để đối chiếu khi kiểm tra lại)
negative_review_count: 0
misunderstanding_count: 0
fixable_count: 0
image_review_ratio: 0.00
```

---

## 14. Checklist thực thi

- [ ] Đã xác nhận mọi đánh giá đã ẩn danh hóa
- [ ] Nội dung vá đã giao 03 thực thi (`mode = iterate`)
- [ ] Ảnh cần bổ sung đã giao 04 thực thi
- [ ] Ứng viên từ cấm đã thêm vào `forbidden_words`
- [ ] Đã ghi lại baseline (số đánh giá tiêu cực / tỷ trọng loại hiểu lầm / tỷ trọng đánh giá có ảnh)
- [ ] Đã chốt mốc kiểm tra lại (đề xuất xem lại thay đổi cơ cấu đánh giá tiêu cực sau 14–30 ngày)
```

---

## Ghi chú quay vòng

Đầu ra của báo cáo này **không phải điểm kết thúc**. Giá trị của nó nằm ở việc sửa Listing:

```text
misunderstanding_count cao   → 03 bổ sung đoạn Lưu ý + 04 bổ sung ảnh danh sách đóng gói
forbidden_words_candidates   → 03/04/05 chặn cứng, tránh chủ động khai khống thông số
selling_points_ranked        → 03 quyết định nội dung cốt lõi trên ảnh chính và từ khóa tiêu đề
```

**Cách kiểm chứng**: 14–30 ngày sau khi thay đổi có hiệu lực, xem lại **cơ cấu đánh giá tiêu cực** có thay đổi không — đặc biệt là tỷ trọng loại hiểu lầm trong tổng đánh giá tiêu cực có giảm không. Tỷ trọng này là chỉ số kiểm chứng trực tiếp nhất, vì nó gần như hoàn toàn do nội dung quyết định.
