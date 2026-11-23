# ROADMAP

## Lộ trình phiên bản

| Phiên bản | Chủ đề | Nội dung | Trạng thái |
|---|---|---|---|
| **v0.1** | Cụm sáng tạo | 03 Listing / 04 Image / 05 Video + tài liệu phương pháp + thư viện case study | ✅ Đã hoàn thành |
| **v0.2** | Cụm vận hành | 06 Advertising / 07 Review + case study vòng khép kín | ✅ Đã hoàn thành |
| **v0.3** | Cụm phân tích | 01 Market Research (kèm script) / 02 Product Strategy | ✅ Đã hoàn thành |
| v1.0 | Nối chuỗi | Chạy trọn vẹn toàn bộ workflow chỉ với một lệnh, xuất gói nội dung để đăng bán | 📋 Đang lên kế hoạch |
| V2 | API | Kết nối API của sàn Shopee / Mercado Livre | 📋 Đang lên kế hoạch |
| V3 | Web | Ứng dụng web, workflow trực quan | 📋 Đang lên kế hoạch |
| V4 | Tự động hóa | Chạy theo lịch + tối ưu vòng khép kín | 📋 Đang lên kế hoạch |

✅ **Cả 7 module Agent đã hoàn thành.**

---

## v0.1 · Cụm sáng tạo ✅

| Module | Nội dung |
|---|---|
| 03 Listing Creative | Tách từ khóa thành 7 loại · công thức tiêu đề 5 đoạn · trang chi tiết 7 phần · phân tầng điểm bán hàng · kiểm tra nhất quán thông số |
| 04 Product Image | Lên kế hoạch 9 ảnh · Prompt tạo ảnh cho từng ảnh · thư viện Negative Prompt · lớp bảo vệ tuân thủ cho ảnh |
| 05 Product Video | Kịch bản 2 phiên bản 15s/30s · bảng storyboard · Prompt video AI · bản lồng tiếng · phụ đề · kiểm tra khả năng đọc khi tắt tiếng |

---

## v0.2 · Cụm vận hành ✅

### 06 Advertising Optimization Agent

- [x] Template đầu vào: dữ liệu quảng cáo + cấu trúc chi phí (kèm ngưỡng chất lượng dữ liệu: lượt hiển thị < 1,000 thì từ chối phân tích)
- [x] Chẩn đoán phễu 4 loại (xét nghiêm ngặt theo thứ tự CTR → tỷ lệ thêm vào giỏ → tỷ lệ chuyển đổi → ROAS)
- [x] Tính ROAS hòa vốn + bảng độ nhạy ROAS + phân tích khoảng cách tới ngưỡng đạt
- [x] Mô hình 2 biến ngân sách × ROI + mục tiêu theo giai đoạn + nhịp ngân sách theo khung giờ
- [x] Case study đầy đủ: 4 nhóm quảng cáo sạc dự phòng, đủ cả 4 loại triệu chứng, ROAS tổng 1,84 đang lỗ

### 07 Review Analysis Agent

- [x] Quy nguyên nhân đánh giá tiêu cực theo 8 nhóm + phân tích đánh giá tích cực theo 5 chiều
- [x] **Nhận diện đánh giá tiêu cực loại hiểu lầm** (3 kiểu xác định: thiếu giải thích / giải thích không nổi bật / người mua không đọc)
- [x] Đề xuất vá trang chi tiết + đúc kết lằn ranh đỏ về thông số + xếp hạng điểm bán hàng theo tần suất × cường độ cảm xúc
- [x] Case study đầy đủ: xe scooter điện, đánh giá tiêu cực sửa được 84,6%, loại hiểu lầm chiếm 38,5%

### Case study vòng khép kín

- [x] `Examples/03_Closed_Loop/`: demo đầy đủ hai đường quay vòng về từ phía quảng cáo + phía đánh giá

---

## v0.3 · Cụm phân tích ✅

### 01 Market Research Agent

**Nút thắt của đợt này là "dữ liệu đưa vào bằng cách nào", nên làm luôn cả script.**

- [x] `scripts/shaduola_parser.py`: chuẩn hóa định dạng (làm sạch ký hiệu tiền tệ / dấu phân cách hàng nghìn / đơn vị 万 (vạn) / giá trị rỗng / ngày tháng / tính bù GMV)
- [x] `scripts/market_metrics.py`: quy mô thị trường / CR3·CR10·HHI / chia khoảng giá / **phát hiện vùng trũng** / bảng chéo cấu hình
- [x] `scripts/make_sample.py` + `samples/`: dữ liệu mẫu tái hiện được (kèm kết quả kỳ vọng, dùng để kiểm tra môi trường)
- [x] Prompt đánh giá sơ bộ (SOP 1.1, **không đạt thì dừng, không làm tiếp phía hạ nguồn**)
- [x] Prompt phân tích thị trường (SOP 1.2–1.6, kèm yêu cầu cứng "dữ liệu không đủ thì phải nói thẳng")
- [x] Case study đầy đủ: xe scooter điện (mọi con số đều tái hiện được bằng ba lệnh)
- [x] **Nguyên tắc thiết kế**: cái gì tính được thì đừng để model đoán —— tính toán tất định giao cho script, phán đoán giao cho Agent

**Ba điểm triển khai chính của phát hiện vùng trũng** (rút ra sau khi dính lỗi):
1. Phát hiện trên đường cong gốc, **mặc định không làm mượt** (trung bình trượt 3 điểm sẽ xóa mất các vùng trũng dốc)
2. Lọc theo mức độ đáng kể của độ sụt (mặc định 15%)
3. Giới hạn số dải giá (mặc định 5, vượt quá thì lấy các dải có độ sụt lớn nhất)

### 02 Product Strategy Agent

- [x] Prompt định vị sản phẩm (1.7 + 3.1, kèm 8 câu hỏi trước khi đăng bán)
- [x] Prompt định giá và SKU (1.9 + 3.2, kèm kiểm tra lại biên lợi nhuận gộp từng SKU + ngưỡng hòa vốn)
- [x] **Cơ chế chặn `decision_approved`** —— không ra quyết định chọn sản phẩm, chỉ chuẩn hóa thông số
- [x] Cấu trúc 4 vai trò SKU + kiểm tra bậc giá hai chiều (quá lớn/quá nhỏ) + thiết kế voucher
- [x] Case study đầy đủ: xe scooter điện (vòng khép kín giữa dư địa lợi nhuận gộp R$ 98,95 và voucher dự kiến R$ 100)

---

## v1.0 · Nối chuỗi 📋

- [ ] `workflow.md`: định nghĩa thứ tự thực hiện đầy đủ và điều kiện dừng (01→02→03→04/05→đăng bán→06/07→quay vòng về)
- [ ] Xuất cấu trúc thư mục「gói nội dung đăng bán」thống nhất
- [ ] Script một lệnh (nối Prompt và script của các module theo thứ tự)
- [ ] Kiểm chứng tái hiện case study end-to-end

## V2 · Kết nối API 📋

- [ ] Shopee Open Platform API (dữ liệu sản phẩm / đơn hàng / quảng cáo)
- [ ] Mercado Livre API (items / orders / ads)
- [ ] Tự động kéo dữ liệu từ khóa (thay cho nhập thủ công 3 bảng xếp hạng)
- [ ] **Tự động kéo dữ liệu ngành hàng** (thay cho xuất thủ công, nối thẳng vào lớp script của 01)
- [ ] Tự động kéo dữ liệu quảng cáo (cho 06 dùng, bỏ bước điền bảng thủ công)
- [ ] Tự động kéo dữ liệu đánh giá (cho 07 dùng)

## V3 · Ứng dụng web 📋

- [ ] Giao diện workflow trực quan
- [ ] Trực quan hóa báo cáo chỉ số (đường cong giá, đánh dấu vùng trũng, bảng chéo cấu hình)
- [ ] Xem trước và quản lý nội dung sáng tạo (creative)
- [ ] Chuyển đổi nhiều shop / nhiều sàn

## V4 · Hệ thống Agent tự động 📋

- [ ] Chạy theo lịch (thu thập dữ liệu hằng ngày → chẩn đoán → đề xuất)
- [ ] Tối ưu vòng khép kín (thực hiện hành động → thu lại dữ liệu → kiểm chứng hiệu quả)
- [ ] Cảnh báo bất thường (CTR tụt mạnh / ROAS rơi xuống dưới ngưỡng hòa vốn / đánh giá tiêu cực tăng vọt)

---

## Việc tồn đọng đã biết (nợ kỹ thuật)

| # | Hạng mục | Ảnh hưởng | Cách xử lý |
|---|---|---|---|
| 1 | ~~Chưa trích xuất được danh sách gốc「logic tạo 9 ảnh」trong SOP~~ | ✅ **Đã chốt dùng khung 9 ảnh do repo này tự suy ra** | Đã đóng, xem [`04 README`](./Agents/04_Product_Image_Agent/README.md) |
| 2 | Bản gốc SOP nói trang chi tiết có "8 phần" nhưng chỉ liệt kê 7 mục | Repo này làm theo 7 phần | Chờ xác nhận có thiếu sót hay không |
| 3 | Quy định số ký tự / trường của sàn có thể đã lỗi thời | Tài liệu ghi theo quy định công khai tại thời điểm biên soạn | Đã ghi chú "kiểm tra lại trước khi đăng" ở nhiều chỗ; sau này có thể thêm kiểm tra tự động |
| 4 | ~~Hệ thống đánh số không khớp với kế hoạch ban đầu~~ | ✅ **Đã chốt** (sắp xếp lại theo cụm công việc) | Đã đóng, xem [`CHANGELOG`](./CHANGELOG.md) |
| 5 | Đầu vào của 06/07 phụ thuộc vào điền bảng thủ công | Dữ liệu quảng cáo và đánh giá phải xuất và chỉnh lý thủ công | Sẽ hết khi V2 kết nối API |
| 6 | Dữ liệu review lại kết quả chưa tự quay vòng về được | Chế độ `iterate` cần người dán output của 06/07 về 03/04 | Sẽ hết khi v1.0 nối chuỗi |
| 7 | Nguồn dữ liệu của 01 phụ thuộc vào xuất thủ công | Định dạng xuất của Shaduola có thể thay đổi, cần bảo trì `--mapping` | Sẽ hết khi V2 kết nối API |
| 8 | Script chưa tính thuế Brazil | Cả lớp chỉ số lẫn lớp định giá đều chưa có thuế, biên lợi nhuận gộp thực tế sẽ thấp hơn | Phải tự bổ sung khoản thuế khi sử dụng, đã ghi chú trong tài liệu |
| 9 | Trích xuất chiều cấu hình mang tính heuristic | Khi cấu hình chỉ nằm trong tiêu đề thì dựa vào regex, tỷ lệ trích xuất có thể thấp | Báo cáo sẽ ghi số lần thất bại; khuyến nghị tách cấu hình thành cột riêng |

---

## Những việc không định làm

Để không gây hiểu lầm cho người dùng, liệt kê rõ những việc **bộ công cụ này không làm**:

| Không làm | Lý do |
|---|---|
| Công cụ buff đơn ảo / review ảo | Sàn cấm rõ ràng, xem [`docs/03_Compliance_Guard.md`](./docs/03_Compliance_Guard.md) |
| Công cụ tổ chức report đối thủ | Cạnh tranh không lành mạnh |
| Tự động giành suất đăng ký / lách hệ thống kiểm soát rủi ro | Dùng thủ thuật kỹ thuật để né quy định sàn |
| Cào dữ liệu đối thủ và dùng lại nguyên nội dung sáng tạo | Rủi ro bản quyền |
| Tính năng cam kết lợi nhuận / đảm bảo ra đơn | Không thể chịu trách nhiệm |
| **Ra quyết định chọn sản phẩm thay người** | Module 02 cần người xác nhận `decision_approved`; chọn sản phẩm liên quan đến chiến lược công ty, vốn và khẩu vị rủi ro, Agent không làm thay được |

---

**Quay lại**: [Trang chủ dự án](./README.md) · [Tách kiến trúc](./docs/00_Architecture_SOP_to_Agent.md)
