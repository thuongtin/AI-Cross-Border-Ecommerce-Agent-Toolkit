# actions.md · Thư viện hành động (điều kiện / mức độ / tần suất / rollback)

> Mỗi hành động có bốn yếu tố: **điều kiện kích hoạt · mức độ thực hiện · giới hạn tần suất · cách rollback**.
> Skill này chỉ **đề xuất** hành động, không thực thi — việc thực thi do con người quyết định.

---

## Nhóm P0 cắt lỗ

| Hành động | Kích hoạt | Mức độ | Tần suất | Rollback |
|---|---|---|---|---|
| **Hạ giá thầu** | ROAS < 0.5×BE, hoặc click≥30 mà 0 đơn | Hạ xuống dưới CPC chịu được; mỗi lần hạ ≤ 30% | Cùng nhóm không lặp lại trong 3 ngày | Đưa giá thầu về mức cũ |
| **Hạ nấc ngân sách** | ROAS < 0.5×BE kéo dài 2 chu kỳ chẩn đoán | Hạ về mức thấp nhất (hoặc 30% ngân sách ngày) | Mỗi tuần ≤ 1 lần | Đưa ngân sách về mức cũ |

### ❗ Nguyên tắc sắt: không tạm dừng quảng cáo

Tạm dừng làm đứt tính liên tục của quảng cáo, giảm điểm quảng cáo và điểm chất lượng, giai đoạn khôi phục lại còn tốn hơn.
**Cách cắt lỗ = hạ ngân sách + hạ giá thầu**, để quảng cáo vẫn chạy nhưng gần như không tốn tiền.
(Ngoại lệ: vi phạm chính sách sàn / hết hàng / đặt sai ngành hàng — những trường hợp này bắt buộc phải dừng.)

---

## Nhóm P1 cải thiện

| Hành động | Kích hoạt | Mức độ | Tần suất | Rollback |
|---|---|---|---|---|
| **Tinh chỉnh giá thầu** | BE ≤ ROAS < mục tiêu, CPC > CPC chịu được | Mỗi lần ≤ 20% | Cùng nhóm 3 ngày một lần | Đưa về mức cũ |
| **Thêm từ khóa phủ định** | Báo cáo từ khóa tìm kiếm có click không liên quan ≥ 10 lần | Thêm từng từ | Mỗi tuần một lần khi xuất báo cáo | Có thể gỡ bỏ |
| **Quay vòng về 03** (trang chi tiết) | CVR < 1% và click ≥ 30 | Chế độ iterate, chỉ sửa đoạn mà triệu chứng chỉ tới | Mỗi vòng 1 lần | — |
| **Quay vòng về 04** (đổi ảnh chính) | CTR < 2% | Chế độ iterate, chỉ đổi ảnh đầu | Mỗi vòng 1 lần | — |
| **Quay vòng về 07** (quy nguyên nhân đánh giá tiêu cực) | CVR thấp + đánh giá tiêu cực tăng vọt gần đây | Chạy một lần quy nguyên nhân | Mỗi tháng một lần | — |

---

## Nhóm P2 scale

| Hành động | Kích hoạt | Mức độ | Tần suất | Rollback |
|---|---|---|---|---|
| **Tăng nấc ngân sách** | ROAS ≥ mục tiêu | **+20~30%** (mỗi lần chỉ tăng một nấc) | Theo dõi 3 ngày rồi mới tăng nấc tiếp | Giảm lại |
| **Mở rộng kiểu khớp** | Đạt P2 và tăng ngân sách tối đa vẫn có lãi | Chính xác → mở rộng từ đồng nghĩa | Mỗi tuần một lần | Tạm dừng nhóm mới |
| **Nhân bản cấu trúc đang chạy** | P2 ổn định 2 tuần | Nhóm mới cùng giá thầu, cùng ngân sách | Hai tuần một lần | Tạm dừng |

> **Kỷ luật scale**: mỗi lần chỉ tăng một nấc. Tăng hai nấc cùng lúc thì không thể quy nguyên nhân「tăng bao nhiêu là nhờ bước nào」.

---

## Quy tắc riêng theo sàn

### Shopee BR (gồm các ràng buộc thực chiến khi nối với tự động hóa trên máy)

| Quy tắc | Giải thích |
|---|---|
| **Nhịp ngân sách** | 11:00 giờ Bắc Kinh (0:00 giờ Brazil) → cho ngân sách ngủ đông ở **R$ 10**; 23:30 giờ Bắc Kinh (khoảng 12:30 giờ Brazil) → khôi phục mức kích hoạt |
| **Đã tiêu thì chỉ được tăng** | Sau khi quảng cáo trong ngày đã phát sinh chi phí, **ngân sách chỉ được tăng, không được giảm**; muốn giảm phải đợi sang ngày hôm sau theo giờ Brazil khi chi phí reset về 0 |
| **Popup xác nhận lần hai** | Bấm「Xác nhận」xong sẽ hiện popup「Vui lòng xác nhận trước khi sửa」, phải bấm「Tiếp tục sửa」— bắt buộc biết khi tự động hóa |
| Vị trí chủ lực | Carregador 20000mAh Turbo 45W (R$30/ngày) và Trilho Elétrico (R$50/ngày) là SKU chủ lực đang chạy quảng cáo |

### Mercado Livre

| Quy tắc | Giải thích |
|---|---|
| Sản phẩm quảng cáo | Publicidad (Product Ads), thao tác tay trong trung tâm người bán |
| Không có API ghi công khai | Người bán không có API quảng cáo công khai → hành động phải làm tay trên trang quản trị (hoặc tự động hóa trình duyệt, cẩn thận) |
| Cách tính chỉ số | Báo cáo ML dùng cách tính ACoS (invertido), là nghịch đảo của ROAS |

---

## Quy tắc kiểm tra lại (sửa xong thế nào là thành công)

| Vòng này sửa gì | Kiểm tra lại chỉ số nào | Chu kỳ |
|---|---|---|
| Giá thầu/ngân sách | ROAS và đóng góp ròng | 3–7 ngày |
| Ảnh chính (quay vòng về 04) | CTR | 3–5 ngày |
| Trang chi tiết (quay vòng về 03) | CVR | 7 ngày |
| Xử lý đánh giá tiêu cực (quay vòng về 07) | Tỷ trọng đánh giá tiêu cực loại hiểu lầm | 2–4 tuần |

**Không nhìn tổng doanh số** (bị ảnh hưởng bởi đợt sale lớn/mùa vụ/đối thủ, không thể quy nguyên nhân).
