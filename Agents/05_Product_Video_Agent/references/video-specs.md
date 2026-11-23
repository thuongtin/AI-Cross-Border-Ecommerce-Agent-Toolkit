# Thẻ quy chuẩn video của sàn (Shopee BR / Mercado Livre)

> ⚠️ Dưới đây là tổng hợp quy định công khai tại thời điểm biên soạn (2026-10). Quy định của sàn sẽ thay đổi,
> **trước khi đăng bắt buộc kiểm tra lại văn bản gốc trên Seller Center**.

## Shopee Brazil (video ảnh chính / video sản phẩm)

| Hạng mục | Yêu cầu |
|---|---|
| Thời lượng | **≤ 30s** (video ảnh chính của sản phẩm; video dài tính riêng) |
| Khung hình | Dọc 9:16 hoặc 1:1 (1:1 khớp với vị trí ảnh chính là an toàn nhất) |
| Định dạng | MP4 (H.264), khuyến nghị ≤ 30MB |
| Khung đầu | **Bắt buộc là sản phẩm** (quy tắc 3 giây vàng: 0–3s là hook) |
| Phụ đề | **Nên burn-in** (rất nhiều người mua lướt Feed khi tắt tiếng), PT-BR, mỗi dòng ≤ 42 ký tự |
| Ngân sách lời thoại | 30s ≈ 65 từ / 15s ≈ 30 từ (2,5 từ/giây, chừa khoảng lặng 3–4s) |
| Cấm | Nhồi từ khóa khuyến mãi, quảng cáo phóng đại (dùng chung bộ kiểm soát tuân thủ với Listing) |

## Mercado Livre

| Hạng mục | Yêu cầu |
|---|---|
| Thời lượng | Khuyến nghị ≤ 30s |
| Tính nhất quán | Cách thể hiện sản phẩm trong video phải dùng **cùng một bộ identity** với ảnh chính/ảnh chi tiết (màu sắc/phụ kiện/góc chụp không bị lệch) |
| Phụ đề | PT-BR; yêu cầu đọc được khi tắt tiếng vẫn áp dụng |
| Lằn ranh đỏ | Cùng nguồn với ảnh chính: không demo sai sự thật (tính năng được demo phải có thật) |

## Áp dụng chung cho cả hai sàn

- **Kiểm tra khả năng đọc khi tắt tiếng**: tắt âm thanh, chỉ xem hình + phụ đề, chuỗi điểm bán hàng vẫn phải trọn vẹn
- **Thẻ thông số**: các con số trên thẻ thông số cuối video phải khớp từng ký tự với `spec_table` (dùng
  `spec_consistency.py` của 03 để rà lại con số trong lời thoại và phụ đề)
- **BGM**: chọn thư viện nhạc được phép dùng thương mại; âm lượng không lấn giọng đọc
- **Tính chân thực của demo**: chỉ demo tính năng sản phẩm thực sự có (kiểm soát tuân thủ: không dàn dựng hiệu ứng giả)

## 3 giây vàng (hook 0–3s)

- Câu thoại đầu tiên ≤ **8 từ** (ở tốc độ 2,5 từ/giây ≈ đọc xong trong 3,2s)
- Hình ảnh phải có chuyển động (đồng hồ hẹn giờ nhảy số / ra thành phẩm / thao tác mở ra), không dùng ảnh sản phẩm tĩnh
- Cách viết câu hook: **câu hỏi nỗi đau** hoặc **đưa kết quả lên trước** (chọn một, không chồng cả hai)
