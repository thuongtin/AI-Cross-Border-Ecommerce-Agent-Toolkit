# Checklist tự kiểm tra trước khi bàn giao · Bản in

> Bản rút gọn của [`docs/04_Result_Checklist.md`](../docs/04_Result_Checklist.md), tiện in ra hoặc dán ở bàn làm việc.
> Bản đầy đủ có giải thích từng mục, bản này chỉ giữ lại các ô đánh dấu.

**Sản phẩm**: ______________  **Sàn**: __________  **Ngày**: __________  **Phiên bản Prompt**: __________

---

## A. Chung (dùng cho cả ba module)

- [ ] Nội dung người mua nhìn thấy dùng **tiếng bản địa của thị trường mục tiêu**, không có giọng văn dịch máy
- [ ] Toàn bộ dùng **đơn vị hệ mét**, dấu phẩy thập phân
- [ ] Mỗi con số trong đầu ra đều tìm được mục tương ứng trong `spec_table`
- [ ] Không có tên thương hiệu / tên model chưa được ủy quyền
- [ ] Không có từ ngữ tuyệt đối (o melhor / 100% / mais rápido)
- [ ] Không có thông tin khuyến mãi (freeship / trả góp / con số giảm giá)
- [ ] Ghi chú nội bộ (tiếng Việt) không bị lẫn vào nội dung tiếng bản địa
- [ ] Không thiếu mục nào, không còn placeholder TODO

---

## B. 03 Listing Creative

**Tiêu đề**
- [ ] Shopee ≤ **120** ký tự, từ khóa cốt lõi nằm trong **30 ký tự đầu**
- [ ] Mercado Livre ≤ **60** ký tự
- [ ] Đủ cấu trúc 5 phần: từ cốt lõi + đối tượng/ngữ cảnh + thông số + tính năng + bổ sung
- [ ] Viết hoa chữ cái đầu đúng quy cách, không emoji / ký tự đặc biệt / nhồi từ khóa lặp lại
- [ ] Có **2–3 phương án dự phòng** với hướng khác nhau
- [ ] Phiên bản cho từng sàn đã được làm khác nhau

**Trang chi tiết**
- [ ] Đủ cấu trúc 7 đoạn
- [ ] Mọi ngữ cảnh sử dụng đều nằm trong `usage_scope`
- [ ] Thông số khớp từng mục với `spec_table`
- [ ] Cam kết hậu mãi đúng với năng lực thực tế
- [ ] Khi không có lưu ý đặc biệt thì **không tạo** đoạn "Lưu ý"

**Từ khóa**
- [ ] Đã phân loại từ khóa 7 nhóm
- [ ] Từ rủi ro đã được liệt kê riêng và đánh dấu cấm dùng
- [ ] Đã đánh dấu các từ tần suất cao trùng ở cả 3 bảng xếp hạng

**Bàn giao**
- [ ] Cuối bản có đính kèm "Kết quả quét tuân thủ" (không dính thì ghi "Không dính")
- [ ] Đã xuất `core_selling_point`

---

## C. 04 Product Image

- [ ] 9 ảnh có phân vai nội dung rõ ràng, không trùng chức năng
- [ ] Ảnh chính đúng quy chuẩn của sàn:
  - [ ] ML: nền trắng tinh, không chữ / watermark / mảng màu, một góc chụp duy nhất, ≥800×800
  - [ ] Shopee: nền trắng (+ chữ điểm bán hàng tùy chọn)
- [ ] Mỗi ảnh có **Prompt tạo ảnh dùng được ngay**
- [ ] Chữ trên ảnh có ghi giới hạn số ký tự và không vượt quá
- [ ] Thông số trên ảnh = `spec_table`, khớp từng ký tự
- [ ] Mỗi ảnh có kèm **Negative Prompt**
- [ ] Không tạo chứng nhận giả / ảnh chụp đánh giá giả / huy hiệu số lượng bán
- [ ] Đã xử lý xung đột giữa các sàn (ML không chữ / Shopee có điểm bán hàng — hai bộ phương án)
- [ ] Người xuất hiện trong ảnh không giống một cá nhân có thật, nhận diện được

---

## D. 05 Product Video

- [ ] Có cả hai bản 15s và 30s (hoặc giải thích vì sao chỉ làm một bản)
- [ ] **3 giây đầu là hook**, không phải tự giới thiệu
- [ ] Bảng storyboard gồm: số cảnh / thời lượng / hình ảnh / chuyển động máy quay / phụ đề / hiệu ứng âm thanh
- [ ] Mỗi cảnh đều có Prompt video AI
- [ ] Kịch bản lồng tiếng là văn nói **đọc được ngay**, có ghi thời lượng dự kiến
- [ ] Phụ đề khớp với lồng tiếng, mỗi dòng không vượt số ký tự
- [ ] CTA kết video khớp với tiêu đề, không có cam kết thêm
- [ ] BGM / hiệu ứng âm thanh có ghi yêu cầu được phép dùng thương mại
- [ ] Không tạo cảnh số lượng bán / chứng nhận / đánh giá giả
- [ ] Ở chế độ tắt tiếng vẫn hiểu được thông tin cốt lõi

---

## E. Nhất quán giữa các module (03 → 04 → 05)

- [ ] Chữ trên ảnh của 04 lấy từ `secondary_points[]` của 03
- [ ] Nội dung cốt lõi trong kịch bản của 05 lấy từ `core_selling_point` của 03
- [ ] **Con số thông số ở ba nơi khớp hoàn toàn** (không lệch)
- [ ] 04 và 05 cùng tuân thủ một bộ `forbidden_words[]`
- [ ] Tông hình ảnh thống nhất (do 03 định nghĩa, 04/05 tuân theo)

**Bảng đối chiếu thông số**

| Thông số | 03 | 04 | 05 | Khớp |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

---

## F. 06 Tối ưu quảng cáo

- [ ] Chu kỳ test ≥ 3 ngày, tổng lượt hiển thị ≥ 1,000
- [ ] Cơ cấu chi phí đầy đủ (thiếu thì không được đưa ra kết luận ROI)
- [ ] Đánh giá phễu theo đúng thứ tự **CTR → tỷ lệ thêm vào giỏ → CVR → ROAS**, không nhảy bước
- [ ] Mỗi nhóm đều có kết luận đánh giá rõ ràng + **"phần giữ nguyên ở vòng này"**
- [ ] Không đề xuất chỉnh giá thầu khi các bước phía trước chưa đạt
- [ ] Hoa hồng và hao hụt hoàn hàng được tính theo **% trên giá bán**
- [ ] Đã tính cả ROAS hòa vốn và ROAS đạt chuẩn, đã chỉ ra khoảng chênh
- [ ] Mỗi hành động đều có **đối tượng cụ thể**, không có kiểu "tối ưu một chút"
- [ ] Đã nói rõ các thay đổi có cùng nhắm vào một nguyên nhân gốc hay không
- [ ] Phương án kiểm tra lại có điều kiện "chưa đạt thì không tăng liều cùng một hành động"

---

## G. 07 Phân tích đánh giá

- [ ] ≥ 20 đánh giá, nhập đủ toàn bộ đánh giá tiêu cực, không bỏ sót đánh giá trung bình
- [ ] Giữ nguyên ngôn ngữ gốc của đánh giá, đã ẩn danh hóa
- [ ] Quy nguyên nhân đủ từng nhóm trong 8 nhóm (kể cả nhóm bằng 0)
- [ ] **Phân biệt rạch ròi loại hiểu lầm với lỗi chất lượng sản phẩm**
- [ ] Trường hợp thiếu phụ kiện đã đối chiếu với `package_content` để kết luận
- [ ] Đã tính tỷ lệ đánh giá tiêu cực có thể khắc phục
- [ ] Nội dung sửa là **tiếng bản địa** và dán vào dùng được ngay
- [ ] Hiểu lầm về phụ kiện đã được xác định là cần bổ sung ảnh (chữ không giải thích nổi)
- [ ] Đã xuất `forbidden_words_candidates`
- [ ] Đã kiểm tra các điểm bán hàng "được khen trong đánh giá tốt nhưng Listing chưa nhắc tới"
- [ ] Không có nội dung dụ dỗ xóa đánh giá / tổ chức report / đánh giá ảo / tự phán đoán thật giả

---

## H. Vòng khép kín (06 / 07 → 03 / 04)

- [ ] Đã ghi lại **dữ liệu baseline** trước khi thay đổi
- [ ] `iterate` chỉ sửa phần mà triệu chứng chỉ tới, phần còn lại giữ nguyên
- [ ] Mỗi lần chỉ sửa một **nguyên nhân gốc**
- [ ] Chu kỳ kiểm tra lại: quảng cáo **7 ngày** / đánh giá **14–30 ngày**
- [ ] Chỉ số kiểm tra lại là **chỉ số mà thay đổi kiểm soát được** (quảng cáo xem ROAS, nội dung xem tỷ lệ loại hiểu lầm)
- [ ] Đã đánh dấu những chỉ số "trông có vẻ xấu đi nhưng nằm trong dự kiến" (vd: lượt click)
- [ ] Chưa đạt thì **không tăng liều cùng một hành động**, quay về chẩn đoán để định vị lại

> Ba kiểu tự làm khó mình: ① Thấy chỉ số giảm như dự kiến lại tưởng là thất bại rồi sửa ngược lại; ② Sửa nhiều nguyên nhân gốc cùng lúc nên không quy được nguyên nhân; ③ Chưa đạt đã tăng liều cùng một hành động.

---

## I. 01 Phân tích thị trường

**Tầng dữ liệu (script)**
- [ ] Chỉ số do script tạo ra, không phải ước lượng thủ công
- [ ] Cỡ mẫu ≥ 30 (< 30 đã ghi chú chỉ để tham khảo)
- [ ] Đã xem tỷ trọng `unparsed_items` của chiều cấu hình (> 30% đã ghi chú bị hạn chế)
- [ ] Khi số chủ thể ≤ 10 thì không dùng CR-n làm căn cứ (chuyển sang CR3 / HHI)

**Tầng nhận định (Agent)**
- [ ] Khi nhận định tiền đề không đạt thì **đã dừng lại**
- [ ] Ngành hàng rủi ro cao đã làm **kiểm định khả năng gánh lợi nhuận**
- [ ] Kiểm tra từng hạn chế của sàn (cấm bán / hạn chế bán / chứng nhận / nhạy cảm vận chuyển)
- [ ] Khi chỉ có dữ liệu một kỳ thì ghi rõ "không đánh giá được xu hướng"
- [ ] Khi dữ liệu "hiệu suất sản phẩm mới" không đáng tin đã ghi chú
- [ ] Mức độ tập trung thương hiệu đã xem cả **CR lẫn tỷ trọng số lượng sản phẩm**
- [ ] Dải giá mục tiêu đã qua **đối chiếu chéo 4 tiêu chí** (doanh số / doanh số trung bình / lợi nhuận / sức mạnh đối thủ)
- [ ] Cấu hình cơ hội đã đối chiếu chéo xem **có bị top đầu chiếm giữ không**
- [ ] Kết luận có phân biệt `【Dữ liệu】` / `【Nhận định】` / `【Cần xác nhận】`
- [ ] Không thay con người ra quyết định chọn sản phẩm

---

## J. 02 Chiến lược sản phẩm

- [ ] **`decision_approved` là true**
- [ ] **Chỉ có một điểm bán hàng chủ lực**
- [ ] Kết luận một câu có đủ 5 yếu tố (bán cho ai / nhấn mạnh gì / cấu hình nào / giá bao nhiêu / tránh điều gì)
- [ ] Không chọn phân khúc cấu hình cao (nhiều sản phẩm nhưng doanh số trung bình thấp) làm SKU chủ lực
- [ ] Cam kết hậu mãi không vượt quá năng lực thực tế
- [ ] Đã trả lời đủ 8 câu hỏi trước khi đăng bán
- [ ] Liệt kê chi phí riêng **cho từng SKU**
- [ ] Trong công thức định giá, hoa hồng / quảng cáo / hoàn hàng nằm ở mẫu số dưới dạng **% trên giá bán**
- [ ] Đã đối chiếu chéo với `cost_floor_price` của 01
- [ ] Mỗi SKU đều đã tính biên lợi nhuận ròng và ROAS hòa vốn
- [ ] Voucher được áp cho **SKU còn dư địa voucher**, sau khi trừ voucher vẫn trên ngưỡng hòa vốn
- [ ] Bậc giá đã được kiểm tra cả hai chiều "quá lớn / quá nhỏ"
- [ ] SKU kéo traffic thấp hơn ngưỡng hòa vốn đã ghi rõ vai trò chiến lược và điều kiện rút lui

---

## K. Chốt chặn cuối trước khi đăng

- [ ] Đã vào **Seller Center kiểm tra lại** quy định hiện hành của sàn về số ký tự / trường / hình ảnh
- [ ] Đã xác nhận đủ tồn kho, hoặc đã điều chỉnh ngân sách quảng cáo theo tồn kho
- [ ] Đã xác nhận sản phẩm không nằm trong danh sách cấm bán / hạn chế bán
- [ ] Khi cùng sản phẩm được đăng bán ở shop khác đã làm **khác biệt tiêu đề / ảnh chính / trang chi tiết**
- [ ] Đã ghi lại số phiên bản Prompt của lần này

---

## Ký xác nhận

| | Họ tên | Ngày |
|---|---|---|
| Thực hiện | | |
| Kiểm duyệt | | |

> **Chưa tích đủ thì không cho qua.**

---

**Tài liệu liên quan**: [Checklist tự kiểm tra bản đầy đủ](../docs/04_Result_Checklist.md) · [Lằn ranh đỏ về tuân thủ](../docs/03_Compliance_Guard.md) · [Quy chuẩn trường dữ liệu theo sàn](../docs/02_Platform_Output_Spec.md)
