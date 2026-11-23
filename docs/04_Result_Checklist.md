# 04 · Checklist tự kiểm tra trước khi bàn giao

> Mỗi module chạy xong thì tick từng mục. **Chưa tick đủ thì không được đăng.**
> Lý do checklist này tồn tại: biến "cảm thấy cũng ổn" thành "kiểm chứng được từng mục".

---

## A. Chung (áp dụng cho mọi module)

- [ ] Mọi văn bản hướng tới người mua dùng **tiếng bản địa của thị trường mục tiêu** (Shopee Brazil = PT-BR), không phải văn dịch
- [ ] Mọi thông số dùng **đơn vị hệ mét** (kg / cm / W / V / mAh / L), không sót đơn vị hệ Anh
- [ ] Mỗi giá trị số xuất hiện trong đầu ra đều tìm được mục tương ứng trong `spec_table` của đầu vào
- [ ] Không chứa bất kỳ tên thương hiệu, tên model nào chưa được ủy quyền
- [ ] Không chứa từ ngữ tuyệt đối hóa (o melhor / 100% / mais rápido do mercado)
- [ ] Không chứa thông tin khuyến mãi (miễn phí vận chuyển / trả góp / con số giảm giá)
- [ ] Trường ghi chú nội bộ dùng tiếng Việt, trường người mua nhìn thấy dùng tiếng bản địa, **hai loại không bị lẫn**
- [ ] Cấu trúc đầu ra đầy đủ, không thiếu mục, không còn placeholder `TODO`

---

## B. 03 Listing Creative Agent

### Tiêu đề
- [ ] Shopee: số ký tự **≤ 120**, và từ khóa cốt lõi nằm trong **30 ký tự đầu**
- [ ] Mercado Livre: số ký tự **≤ 60**
- [ ] Đúng cấu trúc: từ khóa sản phẩm cốt lõi + từ chỉ đối tượng/tình huống + từ thông số + từ điểm bán hàng về tính năng + từ bổ sung
- [ ] Viết hoa chữ cái đầu đúng quy chuẩn (không viết hoa toàn bộ, không viết thường toàn bộ)
- [ ] Không emoji, không ký tự đặc biệt, không nhồi từ khóa lặp lại
- [ ] Đã đưa ra **2–3 tiêu đề dự phòng** (để test A/B nhiều link)
- [ ] Bản cho nhiều sàn đã được khác biệt hóa, không phải copy-paste đơn thuần

### Trang chi tiết
- [ ] Đủ cấu trúc 7 phần: lời chào / điểm bán hàng cốt lõi / tình huống sử dụng / thông số chi tiết / cam kết hậu mãi / (lưu ý) / tag từ khóa
- [ ] Mọi tình huống sử dụng đều nằm trong phạm vi khai báo ở `usage_scope`
- [ ] Phần thông số khớp từng mục với `spec_table`
- [ ] Cam kết hậu mãi tương xứng với năng lực thực tế (không hứa điều không làm được)
- [ ] Khi không có lưu ý đặc biệt, **không tạo** phần "Lưu ý"

### Từ khóa
- [ ] Đã tách từ theo bảy nhóm: từ cốt lõi / từ thông số / từ chỉ đối tượng / từ tính năng / từ tình huống / từ phụ kiện / từ rủi ro
- [ ] Từ rủi ro (từ thương hiệu, từ xâm phạm quyền, từ không khớp thông số) đã được liệt kê riêng và **đánh dấu cấm dùng**
- [ ] Đã đánh dấu các từ tần suất cao trùng nhau giữa ba bảng xếp hạng (lượng tìm kiếm / tỷ lệ cung-cầu / tốc độ tăng trưởng)

### Sản phẩm bàn giao
- [ ] Cuối đầu ra có khối «Kết quả quét tuân thủ» (không vi phạm thì ghi "Không phát hiện vi phạm")
- [ ] Đã xuất `core_selling_point` (cho module 04/05 sử dụng)

---

## C. 04 Product Image Agent

- [ ] **Phân công nội dung** của 9 ảnh rõ ràng, không trùng chức năng
- [ ] Ảnh 1 (ảnh chính) đúng quy chuẩn của sàn mục tiêu:
  - [ ] Mercado Livre: nền sạch (trắng/màu trơn/bối cảnh thật tùy ngành hàng), không chữ khuyến mãi/watermark/viền/từ chỉ thuộc tính của sàn, một góc duy nhất, chủ thể 85–95%, ≥1200×1200
  - [ ] Đã chạy `scripts/check_main_image.py --platform <sàn>` và không có mục FAIL
  - [ ] Shopee: nền trắng + chữ điểm bán hàng (nếu dùng)
- [ ] Mỗi ảnh đều có **Prompt tạo ảnh dùng được ngay** (tiếng Anh/tiếng bản địa)
- [ ] **Chữ trên ảnh** của mỗi ảnh đều ghi rõ giới hạn số ký tự, và không vượt quá
- [ ] Thông số ghi trên ảnh = `spec_table`, khớp từng ký tự
- [ ] Mỗi ảnh kèm **Prompt phủ định** (negative prompt)
- [ ] Không tạo nhãn chứng nhận / ảnh chụp màn hình đánh giá / huy hiệu doanh số giả mạo
- [ ] Đã xử lý các điểm xung đột giữa các sàn (ảnh đầu ML cấm chữ khuyến mãi vs Shopee khuyến khích chèn chữ, xuất hai phương án)
- [ ] Ảnh có người xuất hiện không giống cá nhân thật nhận diện được

---

## D. 05 Product Video Agent

- [ ] Đã có hai phiên bản **15s** (newsfeed/vị trí ảnh chính) và **30s** (trang chi tiết), hoặc giải thích vì sao chỉ làm một bản
- [ ] **3 giây đầu có hook**, và hook không phải kiểu "Xin chào mọi người, tôi là…"
- [ ] Bảng storyboard gồm: số cảnh / thời lượng / nội dung khung hình / chuyển động máy / chữ trên hình / hiệu ứng âm thanh
- [ ] Mỗi cảnh quay đều có **Prompt tạo video AI** tương ứng
- [ ] Nội dung lồng tiếng là bản văn nói bằng tiếng bản địa **đọc được ngay** (không phải văn viết), có ghi thời lượng dự kiến
- [ ] Phụ đề khớp từng câu với lồng tiếng, và **không vượt giới hạn số ký tự mỗi dòng**
- [ ] CTA cuối video nhất quán với tiêu đề/điểm bán hàng, không có cam kết nào mà tiêu đề không có
- [ ] Hiệu ứng âm thanh/BGM có ghi yêu cầu nguồn bản quyền (được dùng thương mại)
- [ ] Không tạo dữ liệu doanh số, nhãn chứng nhận, cảnh đánh giá của người mua giả mạo

---

## E. Tính nhất quán liên module (03 → 04 → 05)

- [ ] Điểm bán hàng được trích trong chữ trên ảnh của 04 lấy từ `secondary_points[]` do 03 xuất
- [ ] Thông điệp cốt lõi trong kịch bản của 05 lấy từ `core_selling_point` do 03 xuất
- [ ] **Con số thông số của ba module hoàn toàn khớp nhau** (cùng một `spec_table`, không lệch chút nào)
- [ ] Cùng một danh sách `forbidden_words[]` được cả 04 và 05 tuân thủ
- [ ] Phong cách hình ảnh thống nhất: mô tả phong cách ảnh của 04 khớp với mô tả phong cách storyboard của 05

> **Lệch thông số là lỗi "toang" thường gặp nhất của quy trình này**: 03 ghi 20000mAh, ảnh của 04 ghi thành 20.000mAh, lồng tiếng của 05 đọc thành "hai mươi nghìn mi-li-am-pe giờ" —— ba chỗ không khớp, người mua nhìn là thấy chắp vá. Chạy xong bắt buộc so khớp liên module một lần.

---

## F. 06 Advertising Optimization Agent

### Ngưỡng dữ liệu
- [ ] Chu kỳ thử nghiệm ≥ 3 ngày (khuyến nghị 7 ngày)
- [ ] Tổng lượt hiển thị ≥ 1,000 (thấp hơn mức này Agent nên từ chối phân tích)
- [ ] Cơ cấu chi phí đầy đủ (thiếu thì không tính được ngưỡng hòa vốn, **không được đưa ra kết luận ROI**)
- [ ] Đã xác nhận cách sàn thống kê "thêm vào giỏ"
- [ ] Đã khai báo các sự kiện nhiễu bên ngoài (mega sale / đối thủ đổi giá / hết hàng)

### Chẩn đoán
- [ ] Phán định phễu đi đúng thứ tự **CTR → tỷ lệ thêm vào giỏ → tỷ lệ chuyển đổi → ROAS**, không nhảy bước
- [ ] Mỗi nhóm quảng cáo đều có kết luận phán định rõ ràng (một trong bốn loại / đơn vị khỏe / chưa đủ dữ liệu)
- [ ] Khi cả ba khâu cùng không đạt, đã nhận diện là vấn đề "độ chính xác của traffic" chứ không phải vấn đề của một tài sản đơn lẻ
- [ ] **Không đề xuất điều chỉnh giá thầu hay ngân sách trước khi các khâu đầu phễu đạt chuẩn**
- [ ] Mỗi nhóm quảng cáo đều xuất «Phần giữ nguyên trong vòng này»

### Ngưỡng hòa vốn
- [ ] Phí hoa hồng và hao hụt hoàn hàng tính theo **phần trăm giá bán**, không coi là giá trị cố định
- [ ] Trình bày đầy đủ quá trình tính, có thể kiểm tra lại
- [ ] Đã tính cả ROAS hòa vốn và ROAS đạt chuẩn
- [ ] Đã chỉ rõ khoảng chênh giữa «chi phí quảng cáo dự trù trong giá bán» và «ROAS thực tế»
- [ ] Đã xuất bảng độ nhạy ROAS

### Hành động và kiểm tra lại
- [ ] Mỗi hành động đều có **đối tượng cụ thể** (từ khóa nào / ảnh nào / con số nào), không có kiểu "tối ưu một chút"
- [ ] Đã nêu các thay đổi có cùng một nguyên nhân gốc hay không (quyết định có làm cùng đợt được không)
- [ ] Đã xuất phương án kiểm tra lại, và nêu rõ "chưa đạt thì không tăng liều cùng một hành động"
- [ ] Đã nêu "các chỉ số trông sẽ xấu đi" (ví dụ thu hẹp đối sánh thì lượt click giảm)

---

## G. 07 Review Analysis Agent

### Chất lượng dữ liệu
- [ ] Tổng số đánh giá ≥ 20 (thấp hơn mức này đã ghi "chỉ để tham khảo")
- [ ] Đã nhập toàn bộ đánh giá tiêu cực, không bỏ đánh giá trung bình (3 sao)
- [ ] Nguyên văn đánh giá giữ **ngôn ngữ gốc**, không dịch trước
- [ ] Đã xác nhận đánh giá đã được ẩn danh (không có nickname / mã đơn hàng / thông tin nhận diện được)

### Quy nguyên nhân
- [ ] Tám nhóm nguyên nhân đều có số lượng và tỷ lệ (kể cả nhóm bằng 0)
- [ ] Mỗi nguyên nhân đều trích dẫn nguyên văn
- [ ] **Đã phân biệt nghiêm ngặt loại hiểu lầm với vấn đề chất lượng sản phẩm**
- [ ] Nhóm thiếu phụ kiện đã đối chiếu với `package_content` (thiếu thật vs hiểu lầm)
- [ ] Nhóm sai thông số đã phân biệt "mô tả không rõ / mô tả sai / người mua đọc nhầm"
- [ ] Đã tính tỷ lệ đánh giá tiêu cực có thể khắc phục

### Quay vòng về
- [ ] Nội dung vá là **tiếng bản địa của thị trường mục tiêu** và dán vào dùng được ngay
- [ ] Nội dung vá tuân theo bốn quy tắc: diễn đạt tích cực / nêu giới hạn chứ không nói "không làm được" / đưa lên vị trí dễ thấy / kèm con số cụ thể
- [ ] Đã đánh giá có cần bổ sung ảnh không (hiểu lầm về phụ kiện bắt buộc dùng ảnh, chữ không nói rõ được)
- [ ] Đã xuất `forbidden_words_candidates` (gồm cả các từ vượt thông số trong bảng từ khóa của đối thủ)
- [ ] Xếp hạng điểm bán hàng có tính tần suất × cường độ cảm xúc, và đã **đối chiếu** với hiện trạng Listing
- [ ] Đã kiểm tra các điểm bán hàng "được đánh giá tốt khen nhưng Listing chưa nhắc đến" (điểm tối ưu không tốn chi phí)

### Tuân thủ
- [ ] Không đưa ra phương án dụ dỗ xóa đánh giá
- [ ] Không đưa ra phương án báo cáo có tổ chức
- [ ] Không đề xuất đánh giá giả
- [ ] Không phỏng đoán đánh giá thật hay giả
- [ ] Kịch bản CSKH không dùng lý do sai sự thật để giải thích việc sai thông số

---

## H. Vòng khép kín (06 / 07 → 03 / 04)

- [ ] Trước khi thay đổi đã ghi lại **dữ liệu baseline** (nếu không thì không quy được nguyên nhân)
- [ ] 03/04 ở `mode = iterate` chỉ sửa phần mà triệu chứng chỉ ra, các phần còn lại giữ nguyên
- [ ] Mỗi lần chỉ sửa một **nguyên nhân gốc** (các thay đổi cùng chỉ về một nguyên nhân thì làm cùng đợt được)
- [ ] Chu kỳ kiểm tra lại phía quảng cáo là **7 ngày**
- [ ] Chu kỳ kiểm tra lại phía đánh giá là **14–30 ngày**
- [ ] Chỉ số kiểm tra lại là **chỉ số mà thay đổi đó kiểm soát được**
  - [ ] Hành động quảng cáo → xem ROAS, không xem tổng doanh số
  - [ ] Hành động nội dung → xem tỷ lệ loại hiểu lầm, không xem tổng số đánh giá tiêu cực
- [ ] Đã đánh dấu các chỉ số "trông sẽ xấu đi nhưng nằm trong dự kiến" (ví dụ lượt click)
- [ ] Khi chưa đạt thì **không tăng liều cùng một hành động**, mà quay lại chẩn đoán để định vị lại
- [ ] Đã xác nhận trong thời gian kiểm tra lại không có nhiễu bên ngoài (hoặc đã ghi lại)

> **Ba cách làm dễ gây hao tổn nhất trong vòng khép kín**: ① coi chỉ số "giảm trong dự kiến" là thất bại rồi sửa ngược lại; ② sửa nhiều nguyên nhân gốc cùng lúc khiến không quy được nguyên nhân; ③ chưa đạt đã tăng liều cùng một hành động.

---

## I. 01 Market Research Agent

### Tầng dữ liệu (script)
- [ ] Đã chạy `shaduola_parser.py`, và đã đối chiếu chênh lệch giữa `row_count_kept` và `row_count_raw`
- [ ] Nhận diện tên cột đầy đủ (khi thiếu trường quan trọng đã chỉ định bằng `--mapping`)
- [ ] Chỉ số do **script tạo ra**, không phải ước tính thủ công
- [ ] Cỡ mẫu ≥ 30 (khi < 30 đã ghi "kết luận chỉ để tham khảo")
- [ ] Đã xem tỷ lệ `unparsed_items` của chiều cấu hình (khi > 30% đã ghi kết luận bị hạn chế)
- [ ] Đã xác nhận tham số phát hiện vùng trũng (`--bins` / `--valley-min-drop` / `--max-bands`)
- [ ] Khi số chủ thể ≤ 10 không dùng CR-n làm căn cứ phán đoán (đã chuyển sang CR3 / HHI)

### Tầng phán đoán (Agent)
- [ ] Khi đánh giá sơ bộ không đạt **đã dừng lại**, không tiếp tục phân tích quy mô thị trường và giá
- [ ] Ngành hàng rủi ro cao **đã kiểm tra khả năng gánh lợi nhuận** (gồm cả chi phí hoàn hàng/hậu mãi)
- [ ] Đã kiểm tra từng hạn chế của sàn (cấm bán / hạn chế bán / chứng nhận / nhạy cảm về vận chuyển)
- [ ] Với dữ liệu chỉ có một kỳ, đã ghi rõ "không thể đánh giá xu hướng", không suy đoán tăng hay giảm
- [ ] Khi dữ liệu không đáng tin, "hiệu quả sản phẩm mới" đã được ghi chú, không cố đưa ra kết luận
- [ ] Đánh giá mức độ tập trung thương hiệu đã xem đồng thời **CR và tỷ lệ số lượng sản phẩm** (phân biệt chiếm chỗ vs hiệu quả)
- [ ] Đánh giá mức độ tập trung người bán đã xem đồng thời `revenue_share` và `item_share`
- [ ] Dải giá mục tiêu đã được **đánh giá chéo bốn mặt** (doanh số / doanh số trung bình / lợi nhuận / sức mạnh đối thủ)
- [ ] Cấu hình cơ hội đã được **đối chiếu chéo xem có bị nhóm dẫn đầu chiếm giữ không**
- [ ] Mọi kết luận đều phân biệt `【Dữ liệu】` / `【Nhận định】` / `【Cần xác nhận】`
- [ ] Không quyết định chọn sản phẩm thay cho người
- [ ] Cuối đầu ra đã kèm phần quét tuân thủ của phân tích + các trường bàn giao

---

## J. 02 Product Strategy Agent

- [ ] **`decision_approved` là true** (nếu không thì phải dừng)
- [ ] Loại sản phẩm đã được định vị theo cả ba chiều
- [ ] Cấu hình cốt lõi đã đối chiếu từng mục với khuyến nghị của thị trường, những gì công ty không làm được đã được ghi chú
- [ ] Không chọn phân khúc cấu hình cao "nhiều sản phẩm nhất nhưng doanh số trung bình thấp nhất" làm SKU chủ lực
- [ ] **Chỉ có một điểm bán hàng chủ lực**, và đáp ứng bốn tiêu chuẩn lựa chọn
- [ ] Câu kết luận gồm đủ năm yếu tố (bán cho ai / đánh vào đâu / cấu hình nào / giá bao nhiêu / tránh cái gì)
- [ ] Đã đưa ra lần lượt 5 nhóm phòng tránh rủi ro, và khớp với **năng lực hậu mãi**
- [ ] Cam kết hậu mãi không vượt năng lực thực tế (không ghi dịch vụ sửa chữa/bảo hành tại chỗ không làm được)
- [ ] 8 câu hỏi trước khi đăng bán đều đã có câu trả lời
- [ ] Giá vốn được liệt kê **theo từng SKU**, không dùng một giá vốn cho mọi SKU
- [ ] Phí hoa hồng/quảng cáo/hoàn hàng trong công thức định giá được đặt ở mẫu số theo **phần trăm giá bán**
- [ ] Đã trình bày đầy đủ quá trình thế số tính toán
- [ ] Đã kiểm tra chéo với `cost_floor_price` của 01 và giải thích ý nghĩa của chênh lệch
- [ ] Mỗi SKU đều đã tính lãi gộp trước quảng cáo / lãi gộp sau quảng cáo / biên lợi nhuận ròng / ROAS hòa vốn
- [ ] Đã tính dư địa lãi gộp, và nêu mức voucher có thể gánh được
- [ ] Voucher được áp cho **SKU còn dư địa** (không phải SKU kéo traffic), và sau voucher vẫn trên ngưỡng hòa vốn
- [ ] Bậc giá đã được kiểm tra hai chiều "quá lớn/quá nhỏ"
- [ ] Khi SKU kéo traffic thấp hơn ngưỡng hòa vốn đã ghi chú vai trò chiến lược và điều kiện rút lui
- [ ] Giảm giá giai đoạn đầu không xuống dưới ngưỡng hòa vốn (trường hợp xuống dưới đã ghi chú là lỗ chiến lược)
- [ ] Đã xuất ROAS hòa vốn của từng SKU cho 06
- [ ] Cuối đầu ra đã kèm phần quét tuân thủ của đề xuất + các trường bàn giao

---

## K. Chốt chặn cuối cùng trước khi đăng

- [ ] Đã vào **Seller Center kiểm tra lại** quy định hiện hành về số ký tự/trường dữ liệu/hình ảnh của sàn (quy định sẽ thay đổi, tài liệu của repo có thể bị chậm)
- [ ] Đã xác nhận tồn kho đủ, hoặc đã điều chỉnh ngân sách quảng cáo theo lượng tồn kho
- [ ] Đã xác nhận sản phẩm không nằm trong danh sách cấm bán/hạn chế bán của sàn
- [ ] Khi đăng bán cùng sản phẩm ở shop khác, tiêu đề/ảnh chính/trang chi tiết **đã được khác biệt hóa**
- [ ] Đã ghi lại phiên bản Prompt dùng lần này (để sau này so sánh cách nào hiệu quả hơn)

---

**Tài liệu liên quan**: [00 Phân rã kiến trúc](./00_Architecture_SOP_to_Agent.md) · [01 Quy chuẩn Prompt](./01_Prompt_Design_Guide.md) · [02 Quy chuẩn trường dữ liệu theo sàn](./02_Platform_Output_Spec.md) · [03 Lằn ranh đỏ tuân thủ](./03_Compliance_Guard.md)
