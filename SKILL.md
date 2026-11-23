---
name: sop-ecom-toolkit
description: >-
  Điểm vào tổng của bộ công cụ AI vận hành thương mại điện tử xuyên biên giới (chuyên sâu Shopee Brazil / Mercado Livre, PT-BR).
  Bao quát 7 workflow: nghiên cứu thị trường, chiến lược sản phẩm và định giá, copy Listing, ảnh sản phẩm (khung 9 ảnh),
  nội dung video ngắn, chẩn đoán quảng cáo, phân tích đánh giá, cùng vòng khép kín "chẩn đoán→sửa lại→kiểm tra lại".
  Dùng khi người dùng muốn "xem ngành hàng / định giá / viết tiêu đề / viết trang chi tiết / làm ảnh chính / làm ảnh chi tiết / 9 ảnh /
  làm video / storyboard / lồng tiếng phụ đề / chẩn đoán quảng cáo / ROAS / ACOS / phân tích đánh giá tiêu cực / đúc kết điểm bán hàng /
  tối ưu chuyển đổi". Câu lệnh tiếng Việt「làm ảnh / làm video / xem ngành hàng / tính giá / phân tích đánh giá」cũng kích hoạt.
  NOT for thao tác tài khoản, buff đơn ảo/review ảo và các hành vi sàn cấm khác, hay pivot Excel thuần túy.
allowed-tools:
  - Bash(python *)
  - Read
  - Write
metadata:
  version: 0.4.0
  category: e-commerce/operations
  license: MIT
---

# AI Cross Border Ecommerce Agent Toolkit (điểm vào tổng)

Thư mục này là một **Skill dạng ô dù**: trước tiên dựa vào bảng định tuyến bên dưới để xác định người dùng muốn làm việc gì,
**sau đó mở SKILL.md của module con tương ứng và làm theo đúng từng bước** —— mỗi module con có thẻ quy tắc,
script tính toán và ràng buộc tối thiểu riêng; file này chỉ lo định tuyến, không thay thế chi tiết của module con.

## Ba nguyên tắc nền tảng chung (mọi module con đều kế thừa)

1. **Không bịa dữ liệu** —— đầu vào thiếu trường thì báo `[INPUT_MISSING]` và liệt kê các cột đang có, không được đoán;
   mọi chỉ số đều phải chạy script trong `scripts/`, Agent không tính nhẩm
2. **Tuân thủ là ưu tiên số một** —— không làm các hành vi sàn cấm như buff đơn ảo/dụ dỗ đánh giá/quảng cáo sai sự thật/report ác ý
   (xem `docs/03_Compliance_Guard.md`, `docs/05_SOP_Gap_Register.md`)
3. **Văn bản người mua nhìn thấy = tiếng mẹ đẻ của thị trường mục tiêu (PT-BR)**, ghi chú nội bộ dùng tiếng Việt;
   mọi con số phải truy được nguồn về `spec_table`

## Bảng định tuyến

| Việc người dùng muốn làm | Mở module con nào |
|---|---|
| Xem ngành hàng / quy mô thị trường / mức độ tập trung / dải giá / cơ hội cấu hình | [Agents/01_Market_Research_Agent/SKILL.md](Agents/01_Market_Research_Agent/SKILL.md) |
| Định giá / cấu trúc SKU / hạn mức voucher / tính ngược từ biên lợi nhuận gộp mục tiêu | [Agents/02_Product_Strategy_Agent/SKILL.md](Agents/02_Product_Strategy_Agent/SKILL.md) |
| Tiêu đề / trang chi tiết / đúc kết điểm bán hàng / phân loại từ khóa / quét tuân thủ | [Agents/03_Listing_Creative_Agent/SKILL.md](Agents/03_Listing_Creative_Agent/SKILL.md) |
| Ảnh chính / ảnh nền trắng / ảnh bối cảnh / 9 ảnh / kiểm tra tuân thủ ảnh | [Agents/04_Product_Image_Agent/SKILL.md](Agents/04_Product_Image_Agent/SKILL.md) |
| Video / storyboard / Prompt video AI / lồng tiếng / phụ đề | [Agents/05_Product_Video_Agent/SKILL.md](Agents/05_Product_Video_Agent/SKILL.md) |
| Chẩn đoán quảng cáo / ROAS / ngưỡng hòa vốn / hành động ngân sách | [Agents/06_Advertising_Optimization_Agent/SKILL.md](Agents/06_Advertising_Optimization_Agent/SKILL.md) |
| Quy nguyên nhân đánh giá tiêu cực / thống kê đánh giá / xếp hạng điểm bán hàng / copy vá lỗi | [Agents/07_Review_Analysis_Agent/SKILL.md](Agents/07_Review_Analysis_Agent/SKILL.md) |

**Vòng khép kín liên module** (nhắc người dùng về chuỗi này khi họ làm vận hành trọn bộ):

```text
01 Nghiên cứu sơ bộ → 02 Chốt chiến lược → 03 Viết Listing → 04 Ảnh + 05 Video → Đăng bán
→ 06 Chẩn đoán quảng cáo + 07 Phân tích đánh giá → Quay về 03/04 (iterate: chỉ sửa phần mà triệu chứng chỉ tới) → Kiểm tra lại
```

Kỷ luật vòng khép kín: **mỗi lần chỉ sửa một nguyên nhân gốc; khâu nào không thuộc triệu chứng thì không đụng tới; chưa đạt thì không tăng liều cùng một hành động, mà quay lại chẩn đoán để xác định lại.**

## Thứ tự thực hiện chung

```text
1. Đọc bảng định tuyến → mở SKILL.md của module con
2. Theo「đầu vào tối thiểu」của module con, xin dữ liệu từ người dùng (CSV xuất ra / ảnh sản phẩm / bảng thông số)
3. Chạy script trong scripts/ của module con để ra con số tất định (lệnh đều có trong bảng tra nhanh của SKILL.md con)
4. Tạo nội dung theo quy tắc trong prompts/
5. Có script kiểm tra thì bắt buộc phải qua, không qua thì không bàn giao
6. Nếu liên quan đến đăng bán, nhắc người dùng: quy định sàn là giá trị công khai tại thời điểm biên soạn, trước khi đăng phải kiểm tra lại trong Seller Center;
   mô hình định giá chưa bao gồm thuế Brazil, tự bổ sung thuế suất trước khi dùng
```

## Giới hạn đã biết

- **Không làm thay**: không thao tác Seller Center, không đổi giá/đổi ngân sách thay người dùng (danh sách hành động giao cho người duyệt)
- **Không bao gồm thu thập dữ liệu**: dữ liệu xuất ngành hàng/quảng cáo/đánh giá do người dùng cung cấp
- **Không bao gồm render**: ảnh và video do model tạo ảnh/công cụ dựng video tạo ra, bộ công cụ này chỉ xuất kế hoạch và Prompt
- Không làm bất kỳ hành vi nào sàn cấm; khi yêu cầu dính tới thì từ chối và đưa phương án thay thế tuân thủ

---

**Tài liệu**: [README](README.md) · [Tách kiến trúc](docs/00_Architecture_SOP_to_Agent.md) ·
[Lằn ranh đỏ tuân thủ](docs/03_Compliance_Guard.md) · [Lộ trình](ROADMAP.md)
