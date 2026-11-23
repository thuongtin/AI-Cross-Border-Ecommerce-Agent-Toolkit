# Examples · Thư viện case study thực tế

Các case study ở đây **xâu chuỗi nhiều module**: một sản phẩm đi trọn từ đầu đến cuối, minh họa toàn bộ luồng 03 → 04 → 05.

Case study tập trung vào từng module riêng lẻ nằm trong thư mục `examples/` của từng Agent; thư mục này chỉ chứa case study **end-to-end**.

---

## Danh mục case study

| # | Sản phẩm | Thị trường | Module bao phủ | Điểm minh họa chính |
|---|---|---|---|---|
| **01** | [Patinete Elétrico 500W](./01_Patinete_Eletrico_500W/) (xe scooter điện) | Shopee BR + Mercado Livre | 03 → 04 → 05 | **Xâu chuỗi toàn luồng** · Rút gọn tiêu đề giữa các sàn (120→60 ký tự) · Nhất quán thông số giữa các module |
| **02** | [Bolsa Térmica](./02_Thermal_Bag/) (túi giữ nhiệt) | Shopee BR | 03 (iterate) | **Chế độ iterate**: vòng khép kín chỉnh sửa lại khi quảng cáo không chạy được |
| **03** | [Closed Loop](./03_Closed_Loop/) (case study vòng khép kín) | Shopee BR | 03 → 06 → 03 → 04 → 07 → kiểm tra lại | Vòng khép kín đầy đủ **chẩn đoán → quay vòng về → kiểm tra lại** · Những cái bẫy ngược trực giác · Chọn chỉ số khi retest |

---

## Luồng tiền đề (nằm trong examples/ của từng module)

Luồng tiền đề đầy đủ 01 → 02 → 03 nằm rải rác ở ba module và nối tiếp nhau:

| Khâu | Vị trí | Đầu ra |
|---|---|---|
| **01 Phân tích thị trường** | [`01/examples/patinete_eletrico_market.md`](../Agents/01_Market_Research_Agent/examples/patinete_eletrico_market.md) | Dải giá R$ 1.989–2.966 · Cấu hình cơ hội 200kg · Giá khả thi theo giá vốn R$ 1.989,36 |
| **02 Chiến lược sản phẩm** | [`02/examples/patinete_eletrico_strategy.md`](../Agents/02_Product_Strategy_Agent/examples/patinete_eletrico_strategy.md) | Điểm bán hàng chủ lực「500W + 200kg」· SKU 4 bậc · Giá SKU chủ lực R$ 2.199 · Ngưỡng hòa vốn ROAS 2,41 |
| **03–05 Nội dung sáng tạo** | [`01_Patinete_Eletrico_500W/`](./01_Patinete_Eletrico_500W/) | Tiêu đề (Shopee 89 ký tự / ML 54 ký tự) · 9 ảnh · Video 30s |

**Điểm đặc biệt đáng xem của luồng này**: hai điểm kiểm chứng mà "hai cách suy luận độc lập cùng dẫn đến một kết quả" ——

1. Cận dưới dải giá do phát hiện vùng trũng (valley) tìm ra là **R$ 1.989,13**, còn giá khả thi theo giá vốn tính ngược từ công thức định giá là **R$ 1.989,36**, chênh nhau **R$ 0,23**
2. Biên lãi gộp còn dư của SKU chủ lực **R$ 98,95** so với mệnh giá voucher dự kiến phát **R$ 100**, chênh nhau **R$ 1,05**

> Một bên là toán thuần túy (đường cong doanh số), một bên là tài chính thuần túy (cơ cấu chi phí). **Hai bên khớp nhau, chứng tỏ bộ phương pháp luận này nhất quán từ bên trong.**

---

## Mức độ bao phủ 5 sản phẩm case study mà Toolkit đã lên kế hoạch

5 sản phẩm case study được chỉ định trong `AI_Cross_Border_Ecommerce_Agent_Toolkit_制作说明` (tài liệu hướng dẫn xây dựng):

| Sản phẩm | Nằm ở đâu | Module |
|---|---|---|
| **Electric Scooter** | [`01_Patinete_Eletrico_500W/`](./01_Patinete_Eletrico_500W/) + [`01/examples`](../Agents/01_Market_Research_Agent/examples/patinete_eletrico_market.md) + [`02/examples`](../Agents/02_Product_Strategy_Agent/examples/patinete_eletrico_strategy.md) + [`07/examples`](../Agents/07_Review_Analysis_Agent/examples/electric_scooter_reviews.md) | **Toàn luồng 01 + 02 + 03 + 04 + 05 + 07** |
| **Power Bank** | [`03/examples`](../Agents/03_Listing_Creative_Agent/examples/powerbank_20000mah.md) + [`06/examples`](../Agents/06_Advertising_Optimization_Agent/examples/powerbank_20000mah_ads.md) | 03 · 06 Chẩn đoán quảng cáo |
| **Pet Carrier** | [`04/examples`](../Agents/04_Product_Image_Agent/examples/pet_carrier.md) | 04 |
| **Air Fryer** | [`05/examples`](../Agents/05_Product_Video_Agent/examples/air_fryer.md) | 05 |
| **Thermal Bag** | [`02_Thermal_Bag/`](./02_Thermal_Bag/) | 03 iterate · 06 chạy thử |

✅ Đã bao phủ đủ cả 5 sản phẩm, trong đó **Electric Scooter đi hết toàn bộ 7 module** (01→02→03→04→05→đăng bán→07).

---

## Cấu trúc case study (đối chiếu yêu cầu của tài liệu hướng dẫn xây dựng)

Tài liệu hướng dẫn quy định cấu trúc case study là: **Bối cảnh sản phẩm → Phân tích thị trường → Quy trình xử lý bằng AI → Kết quả tạo ra → Đề xuất tối ưu**.

Các case study trong repo này bổ sung thêm hai phần:

| Phần | Nguồn | Vì sao cần thêm |
|---|---|---|
| Bối cảnh sản phẩm | Tài liệu hướng dẫn | — |
| Phân tích thị trường | Tài liệu hướng dẫn | — |
| Quy trình xử lý bằng AI | Tài liệu hướng dẫn | — |
| Kết quả tạo ra | Tài liệu hướng dẫn | — |
| **Các trường bàn giao cho module hạ nguồn** | Repo này bổ sung | Để case study **thực sự tái lập được**, chứ không chỉ để đọc |
| **Case study này chứng minh điều gì** | Repo này bổ sung | Nêu rõ kết luận của case study, tiện so sánh chéo giữa các case study |

---

## Đóng góp case study mới

Rất hoan nghênh! Yêu cầu:

1. **Bắt buộc ẩn danh hóa**: không có tên shop thật, tài khoản, thông tin người mua, từ khóa thương hiệu chưa được cấp phép
2. **Thông số phải là thật**: thông số ví dụ phải có bằng chứng, không được bịa
3. **Bắt buộc có phần "Các trường bàn giao cho module hạ nguồn"** (xem [`Templates/product_brief_template.md`](../Templates/product_brief_template.md))
4. **Bắt buộc rà qua** [`docs/04_Result_Checklist.md`](../docs/04_Result_Checklist.md)
5. Nếu có case study về ảnh/video, **không được chứa logo chứng nhận giả, ảnh chụp đánh giá giả, nhãn số lượng đã bán giả**

Định dạng tham khảo các case study hiện có. Chi tiết xem [`CONTRIBUTING.md`](../CONTRIBUTING.md).

---

**Quay lại**: [Trang chủ dự án](../README.md) · [Phân rã kiến trúc](../docs/00_Architecture_SOP_to_Agent.md)
