# 05 · Bảng đăng ký chênh lệch so với SOP (các hạng mục không triển khai)

> **Bản chất của tài liệu này: đăng ký, không phải hướng dẫn.**
>
> Nó trả lời một câu hỏi: **"Vì sao một số nội dung trong SOP gốc không tìm thấy trong repo này?"**
>
> Dự án mã nguồn mở bỏ đi nội dung của người khác mà không giải thích thì sẽ bị hiểu nhầm là bỏ sót. Vì vậy tài liệu này đăng ký từng mục: **SOP gốc nhắc đến điều gì → vì sao không triển khai → có phương án thay thế tuân thủ không → phương án thay thế nằm ở module nào**.
>
> ⚠️ **Tài liệu này chỉ đăng ký đến mức "kết luận", không thuật lại chi tiết thao tác.** Cần các bước thao tác gốc thì hãy tra bản SOP gốc. Đây là thiết kế có chủ ý —— mục đích của việc đăng ký là minh bạch, không phải lan truyền.

---

## I. Vì sao không "triển khai từng mục"

Ba lý do thực tế:

| Lý do | Giải thích |
|---|---|
| **Rủi ro từ sàn** | Những thao tác này là vi phạm ở mức cao nhất của sàn, hình phạt gồm xóa đánh giá / bóp traffic / trừ điểm / khóa shop, và một số hành vi **không được khiếu nại** |
| **Rủi ro pháp lý** | Khai khống thông số tại Brazil thuộc phạm vi điều chỉnh của «Bộ luật Bảo vệ Người tiêu dùng»; báo cáo ác ý đối thủ có thể cấu thành cạnh tranh không lành mạnh |
| **Rủi ro cho dự án** | Repo mã nguồn mở chứa hướng dẫn thao tác vi phạm sẽ bị hệ thống kiểm soát rủi ro của sàn nhận diện, đồng thời khiến người dùng bị liên đới thiệt hại |

**Nguyên tắc xử lý**: **giữ mục tiêu kinh doanh, thay thủ đoạn thực hiện.**

> Đây là ranh giới giữa repo này và các "tuyển tập mẹo vận hành" khác: chúng tôi không chép lại SOP, mà **đánh giá phần nào tự động hóa được, phần nào không, phần không được thì đổi thành cách làm được ra sao**.

---

## II. Bảng đăng ký

### 2.1 Nhóm dữ liệu và đánh giá

| # | Nội dung SOP nhắc đến | Tính chất theo quy định sàn | Cách repo xử lý | Thay thế tuân thủ | Nằm ở đâu |
|---|---|---|---|---|---|
| 1 | Tổ chức giao dịch bằng cách tự tạo SKU, điều chỉnh quy cách, kiểm soát khung giờ đặt hàng v.v. để tích lũy doanh số và đánh giá | **Giao dịch ảo** —— vi phạm ở mức cao nhất của sàn | ❌ Không triển khai | Khuyến mãi giá thấp có thật để nhanh chóng phá mốc 0 đơn; dùng kênh mời đánh giá chính thức của sàn; voucher không công khai để thu hút người mua thật | [`03` trang chi tiết phần 5](../Agents/03_Listing_Creative_Agent/prompts/02_description_builder.md) · [`07` đề xuất quay vòng về](../Agents/07_Review_Analysis_Agent/) |
| 2 | Dùng voucher dụ dỗ người mua đánh giá; khi dùng lại hình ảnh của người khác thì sửa đặc trưng file để lách kiểm tra | **Lách kiểm soát rủi ro + xâm phạm bản quyền** | ❌ Không triển khai | Công cụ mời đánh giá chính thức của sàn; nội dung sáng tạo tự chụp hoặc mua bản quyền | [`docs/04` tự kiểm tra mục D](./04_Result_Checklist.md) |
| 3 | Tổ chức người báo cáo tập trung vào đánh giá của đối thủ | **Lạm dụng cơ chế báo cáo + cạnh tranh không lành mạnh** | ❌ Không triển khai | Quy nguyên nhân đánh giá tiêu cực của đối thủ → chuyển thành **phần giải thích phòng ngừa** trên trang chi tiết của mình | [`07` so sánh đối thủ](../Agents/07_Review_Analysis_Agent/prompts/01_classify_and_attribute.md) |
| 4 | Thương lượng với người mua để xóa đánh giá tiêu cực với điều kiện hoàn tiền / bồi thường | **Tác động không chính đáng đến đánh giá** | ❌ Không triển khai | Giải thích trung thực + đưa ra phương án giải quyết; đưa vấn đề trong đánh giá tiêu cực quay vòng về thành bản vá trang chi tiết | [`07` nhận diện loại hiểu lầm](../Agents/07_Review_Analysis_Agent/prompts/02_misunderstanding_detector.md) |

> ⚠️ Mục 3 cần phân rõ ranh giới: **khiếu nại thông thường với một đánh giá vi phạm rõ ràng là điều sàn cho phép** ("báo cáo trước thì có cơ hội được gỡ" mà SOP nhắc đến thuộc loại này). Thứ repo loại bỏ là "báo cáo tập trung **có tổ chức**", không phải phủ nhận quyền khiếu nại thông thường.

### 2.2 Nhóm nội dung và thông số

| # | Nội dung SOP nhắc đến | Tính chất theo quy định sàn | Cách repo xử lý | Thay thế tuân thủ | Nằm ở đâu |
|---|---|---|---|---|---|
| 5 | Tiêu đề viết "quảng cáo sai sự thật trong phạm vi kiểm soát được" để tăng CTR | **Quảng cáo sai sự thật** (quy định sàn + luật tiêu dùng Brazil) | ❌ Không triển khai | **Bảng ánh xạ điểm bán hàng về sự thật**: cách nói phóng đại → cách nói kiểm chứng được (`A Bateria Mais Forte do Mercado` → `Bateria de 20000mAh com saída de 45W`) | [`docs/03` mục III](./03_Compliance_Guard.md) · [`03` phần 2](../Agents/03_Listing_Creative_Agent/prompts/02_description_builder.md) |
| 6 | Khi có khai khống thông số, giải thích với người mua là "đóng gói nhầm sách hướng dẫn", "sản phẩm có mấy phiên bản" | **Gian lận** | ❌ Không triển khai | **Kiểm tra tính nhất quán thông số ở ba chỗ**: `spec_table` đầu vào = tiêu đề = trang chi tiết, khớp từng ký tự | [`03` kiểm tra thông số](../Agents/03_Listing_Creative_Agent/prompts/02_description_builder.md) · [`07` lằn ranh đỏ thông số](../Agents/07_Review_Analysis_Agent/prompts/02_misunderstanding_detector.md) |
| 7 | Dùng từ thương hiệu lớn, từ nhạy cảm của sàn để cài từ khóa vào tiêu đề | **Xâm phạm quyền + vi phạm quy định sàn** | ❌ Không triển khai | Thương hiệu chưa ủy quyền đều thay bằng `Compatível com <marca>` hoặc xóa; từ rủi ro được tách riêng thành `forbidden_words` | [`docs/03` quy tắc R2](./03_Compliance_Guard.md) · [`03` cô lập từ rủi ro](../Agents/03_Listing_Creative_Agent/prompts/01_keyword_to_title.md) |
| 8 | Khi thứ hạng đối thủ tăng, cân nhắc đánh giá tiêu cực đối thủ | **Cạnh tranh ác ý** | ❌ Không triển khai | Phân tích nguyên nhân quảng cáo và chuyển đổi của đối thủ; tăng cường khác biệt hóa trên trang chi tiết của mình | [`01` phân tích đối thủ](../Agents/01_Market_Research_Agent/) |

### 2.3 Nhóm nhịp độ vận hành

| # | Nội dung SOP nhắc đến | Tính chất | Cách repo xử lý | Thay thế tuân thủ |
|---|---|---|---|---|
| 9 | Dùng giá chốt đơn quá thấp (ví dụ voucher giá trị lớn) để tạo dữ liệu đơn hàng trong thời gian ngắn | **Giao dịch bất thường** —— mục hay bị kiểm soát rủi ro với shop mới | ⚠️ Giữ lại một phần | Giữ **cảnh báo rủi ro** "giai đoạn đầu shop mới đừng để lượng đơn biến động quá lớn"; loại bỏ cách làm "dùng voucher giá trị lớn để tạo đơn". Khuyến nghị scale theo nhịp đẩy sản phẩm bình thường | 
| 10 | Sàn sẽ xóa một phần đánh giá; sau khi có vấn đề thì đánh giá chỉ được sửa một lần | **Sự thật về sàn** | ✅ Giữ lại | Giữ làm lưu ý vận hành, để nhấn mạnh "xây dựng đánh giá phải làm đúng ngay từ đầu" |

> Ranh giới của mục 9: **bản thân khuyến mãi giá thấp là hoạt động kinh doanh bình thường**, repo không phản đối. Thứ bị loại bỏ là "giá thấp cực đoan nhằm tạo dữ liệu đơn hàng giả, không khớp với nhu cầu thật". Tiêu chuẩn phán đoán là **mục đích có phải để đánh lừa thuật toán của sàn hay không**.

---

## III. Repo này đã **bổ sung** những gì

Ngoài phần đăng ký chênh lệch, còn vài chỗ SOP không có mà repo đã bổ sung. Liệt kê ra để tiện đối chiếu:

| # | Nội dung bổ sung | Vì sao thêm | Nằm ở đâu |
|---|---|---|---|
| 1 | **Tính ROAS hòa vốn** | SOP đưa ra ngưỡng chuẩn cho chỉ số sức khỏe, nhưng không có đường phân định "có lãi hay không". Hai thứ này khác nhau —— phễu đạt chuẩn toàn bộ vẫn có thể lỗ | [`06`](../Agents/06_Advertising_Optimization_Agent/) |
| 2 | **Phân loại riêng đánh giá tiêu cực loại hiểu lầm** | SOP liệt kê đánh giá tiêu cực theo hiện tượng, không phân biệt "vấn đề do mô tả" và "vấn đề do sản phẩm". Tách ra rồi mới thấy 84,6% đánh giá tiêu cực có thể giải quyết bằng cách sửa nội dung | [`07`](../Agents/07_Review_Analysis_Agent/) |
| 3 | **Nguồn thông số duy nhất (`spec_table`)** | SOP không bắt buộc thống nhất nguồn giá trị số, bảng từ khóa lẫn cả thông số của đối thủ (ví dụ đối thủ ghi quãng đường 60km) rất dễ biến thành khai khống thông số | [`03`](../Agents/03_Listing_Creative_Agent/) · [`Templates`](../Templates/product_brief_template.md) |
| 4 | **Hợp đồng giao tiếp giữa các module + trường chặn** | Tránh mất thông tin và mô hình tự suy đoán khi truyền giữa các module | [`Templates/product_brief_template.md`](../Templates/product_brief_template.md) |
| 5 | **«Phần giữ nguyên trong vòng này»** | Tránh việc sửa khâu A tiện tay làm hỏng khâu B, dẫn đến không quy được nguyên nhân | [`06` chẩn đoán phễu](../Agents/06_Advertising_Optimization_Agent/prompts/01_funnel_diagnosis.md) |
| 6 | **Nguyên tắc chọn chỉ số kiểm tra lại** | Chọn chỉ số "mà thay đổi kiểm soát được" (quảng cáo xem ROAS, nội dung xem tỷ lệ loại hiểu lầm), không xem tổng doanh số | [`Examples/03`](../Examples/03_Closed_Loop/) |
| 7 | **Prompt phủ định như một công cụ tuân thủ** | Ảnh bối cảnh của sản phẩm không chống nước bắt buộc loại trừ `rain / water / swimming pool`, nếu không thì bản thân hình ảnh đã là một lời ám chỉ | [`04` Prompt tạo ảnh](../Agents/04_Product_Image_Agent/prompts/02_image_prompt_generator.md) |

---

## IV. Lời khuyên cho người dùng

Nếu trong tay bạn chính là bản SOP đầy đủ đó:

1. **Tài liệu này là căn cứ để phán đoán, không phải danh sách cấm.** Thứ chúng tôi loại bỏ là "thủ đoạn", còn mục tiêu kinh doanh (tăng doanh số, xây dựng đánh giá, lên thứ hạng) đều được giữ lại, chỉ là đổi cách làm.
2. **Gặp nội dung không có trong tài liệu này**, hãy tự kiểm tra bằng ba câu hỏi:
   - Nếu **kể đúng sự thật** thao tác này cho người khác nghe, tôi có thấy khó chịu không?
   - Nếu sàn biết tôi đang làm thế này, có bị phạt không?
   - Đổi sang cách làm tuân thủ, **mục tiêu kinh doanh còn đạt được không**? Được → thì đổi; không được → chứng tỏ bản thân mục tiêu đó không đứng vững.
3. **Khi không chắc có tuân thủ hay không**, hãy đối chiếu với bảng đối chiếu viết lại trong [`docs/03_Compliance_Guard.md`](./03_Compliance_Guard.md) —— nó bao quát phần lớn các tình huống thường gặp.

---

## V. Đóng góp

Nếu bạn phát hiện repo bỏ sót chưa đăng ký một nội dung nào đó của SOP, hoặc không đồng ý với cách xử lý một mục:

- Mở Issue, nêu rõ **vị trí trong SOP gốc + nhận định của bạn + đề xuất xử lý**
- **Đừng dán các bước thao tác vi phạm cụ thể vào Issue / PR** —— chỉ cần đăng ký đến mức "kết luận"

Xem chi tiết tại [`CONTRIBUTING.md`](../CONTRIBUTING.md).

---

**Tài liệu liên quan**: [03 Lằn ranh đỏ tuân thủ và đối chiếu viết lại](./03_Compliance_Guard.md) · [00 Phân rã kiến trúc](./00_Architecture_SOP_to_Agent.md) · [04 Checklist tự kiểm tra](./04_Result_Checklist.md)
