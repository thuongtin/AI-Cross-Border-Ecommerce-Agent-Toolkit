# 00 · Từ SOP đến Agent: bảng tổng hợp phân rã kiến trúc

> Đây là **tài liệu gốc** của cả bộ công cụ (toolkit). Nó trả lời một câu hỏi: trong một bộ SOP vận hành thương mại điện tử xuyên biên giới dài 38 trang, phần nào giao được cho AI, phần nào không, và chia tách ra sao.

---

## I. Phương pháp phân rã: ba câu hỏi sàng lọc

Không phải nội dung SOP nào cũng hợp để làm thành AI Agent. Chúng tôi sàng lọc bằng ba câu hỏi:

| Tiêu chí | Câu hỏi | Kết luận |
|---|---|---|
| **① Dựa vào "phán đoán" hay dựa vào "dữ liệu"** | Kết luận của bước này do người cân nhắc đưa ra, hay do chạy số liệu? | Do người cân nhắc → hợp với Agent (Agent giỏi cấu trúc hóa quy tắc); do chạy số liệu → hợp với script/API, Agent chỉ diễn giải |
| **② Đầu vào có liệt kê hết được không** | Đầu vào cần thiết có điền hết vào một biểu mẫu được không? | Được → hợp với Agent; không được (cần dữ liệu toàn thị trường theo thời gian thực) → không hợp với Agent chạy độc lập |
| **③ Đầu ra có kiểm chứng được không** | Kết quả đúng hay sai, có nhìn qua là biết không? | Được → làm trước; không được → để sau |

Lọc 38 trang SOP qua ba tiêu chí này, ta có ba cấp phân loại:

| Cấp | Đặc điểm | Cách tiếp nhận | Tỷ trọng trong SOP |
|---|---|---|---|
| 🟢 **Cấp A: Agent hóa trực tiếp** | Đầu vào dạng biểu mẫu, đầu ra kiểm chứng được, sản phẩm thuần văn bản/nội dung sáng tạo (creative) | Module Agent hoàn chỉnh | ~30% |
| 🟡 **Cấp B: Agent hỗ trợ** | Phụ thuộc dữ liệu bên ngoài, AI chỉ diễn giải và đề xuất | Agent + người cung cấp dữ liệu | ~45% |
| 🔴 **Cấp C: Không Agent hóa được** | Cấu hình trong backend, thao tác vận chuyển, kiểm soát rủi ro tài khoản, giao tiếp giữa người với người | Giữ nguyên dạng sổ tay SOP | ~25% |

---

## II. Bảng ánh xạ chương SOP → Agent

### Chương 1: Phân tích thị trường (SOP 1.1 – 1.10)

| Mục SOP | Kinh nghiệm vận hành cốt lõi | Cấp | Agent tiếp nhận | Đầu vào | Đầu ra |
|---|---|---|---|---|---|
| 1.1 Đánh giá sơ bộ ngành hàng | Ngành hàng tỷ lệ hoàn hàng cao/hậu mãi nặng/rủi ro cao phải thận trọng; có hàng, có giá vốn mới nên vào | 🟡 B | **01 Market Research** | Bảng nguồn hàng, năng lực nhà cung cấp, năng lực hậu mãi | «Kết luận đánh giá sơ bộ ngành hàng» |
| 1.2 Quy mô thị trường và doanh số | Không nhìn một sản phẩm bán chạy (best-seller) đơn lẻ, mà nhìn tổng quy mô ngành hàng; sản phẩm mới có lên được đơn hay không là tín hiệu then chốt | 🟡 B | **01 Market Research** | Dữ liệu xuất từ Shaduola | «Bảng phân tích quy mô thị trường và doanh số» |
| 1.3 Mức độ tập trung thương hiệu/người bán | Mức độ tập trung thương hiệu >50% thì thận trọng; CR10 phản ánh độ khó cho shop mới | 🟡 B | **01 Market Research** | Tỷ trọng doanh số theo thương hiệu/người bán | «Bảng phân tích mức độ tập trung» |
| 1.4 Phân tích giá | Tìm dải giá **doanh số cao + cạnh tranh vừa phải + có lãi**, chứ không phải tìm đỉnh cao nhất | 🟡 B | **01 Market Research** | Giá và doanh số của top 50/100 sản phẩm | «Bảng phân tích khoảng giá» |
| 1.5 Loại sản phẩm và tổ hợp cấu hình | Tìm cấu hình "tổng doanh số cao + doanh số trung bình cao + làm được + có lãi + hậu mãi kiểm soát được" | 🟡 B | **01 Market Research** | Phân rã cấu hình của top 50 sản phẩm | «Bảng phân tích tổ hợp cấu hình» |
| 1.6 Phân tích đối thủ và đánh giá | Đánh giá (review) là nơi gần nhất với nhu cầu thật; đánh giá tốt để tìm điểm bán hàng, đánh giá tiêu cực để tìm rủi ro | 🟡 B | **01 + 07 Review** | 2–3 link đối thủ, nguyên văn đánh giá | «Bảng phân tích đối thủ» «Insight từ đánh giá» |
| 1.7 Chốt sản phẩm chủ lực | Một câu kết luận: làm gì, bán cho ai, giá bao nhiêu, đánh vào đâu, tránh cái gì | 🟢 A | **02 Product Strategy** | Đầu ra của các mục 1.2–1.6 ở trên | «Bảng yêu cầu sản phẩm của tôi» |
| **1.8 Bảng từ khóa** | So sánh ba bảng xếp hạng lượng tìm kiếm/tỷ lệ cung-cầu/tốc độ tăng trưởng → từ tần suất cao → tách từ theo bảy nhóm → ghép tiêu đề | 🟢 A | **03 Listing Creative** ⭐ | Danh sách từ khóa của ba bảng xếp hạng | Bảng phân loại từ khóa + 2–3 tiêu đề dự phòng |
| 1.9 Định giá | Hàng cồng kềnh lãi gộp 30–35%, hàng nhỏ 25–30%; giai đoạn đầu có thể để thấp hơn một chút để nuôi điểm (trọng số) tìm kiếm | 🟢 A | **02 Product Strategy** | Giá vốn, vận chuyển, phí hoa hồng, các loại phí | Bảng mô hình định giá |
| 1.10 Kế hoạch đẩy sản phẩm | Xem đối thủ đăng bán bao lâu thì lên đơn, cần bao nhiêu đánh giá trước khi lên đơn → suy ngược ra nhịp độ cho sản phẩm mới | 🟡 B | **06 Advertising** | Dữ liệu quảng cáo/đẩy sản phẩm của đối thủ | «Bảng kế hoạch đẩy sản phẩm mới» |

### Chương 2: Vận hành shop (SOP 2.1 – 2.5)

| Mục SOP | Kinh nghiệm vận hành cốt lõi | Cấp | Cách tiếp nhận |
|---|---|---|---|
| 2.1 Định vị shop và cơ cấu sản phẩm | Cơ cấu bốn loại: SKU kéo traffic/SKU lợi nhuận/SKU thử nghiệm/SKU long-tail | 🔴 C | Chiến lược do người làm; Agent có thể tạo đề xuất cơ cấu (02) |
| 2.2 Trang trí shop và phong cách | Thống nhất ngành hàng, thống nhất phong cách, phân nhóm rõ ràng, voucher theo dõi shop | 🟢 A | Tái sử dụng năng lực mô tả hình ảnh của **03 Listing** để viết nội dung giới thiệu shop |
| 2.3 Khởi động shop mới và phòng ngừa bất thường | Không đăng hàng loạt sản phẩm quá giống nhau; cùng một mẫu bán ở nhiều shop thì bắt buộc khác biệt hóa | 🟢 A | **03 Listing (chế độ khác biệt hóa nhiều link)** ⭐ |
| 2.4 Nhịp độ khởi động traffic | Ba tuần đầu: lượt truy cập cơ bản → thử nghiệm ổn định → lọc link trọng điểm để scale (tăng ngân sách) | 🔴 C | Bảng nhịp độ, người thực hiện |
| 2.5 Sức khỏe tài khoản và duy trì điểm phạt | Vi phạm hoàn tất đơn hàng có trọng số cao nhất; giao trễ, tỷ lệ hủy, không giao đúng hạn | 🔴 C | Sổ tay vận hành; **nội dung khiếu nại** có thể Agent hóa |

### Chương 3: Vận hành từng sản phẩm (SOP 3.1 – 3.9) ★ Trọng tâm

| Mục SOP | Kinh nghiệm vận hành cốt lõi | Cấp | Agent tiếp nhận |
|---|---|---|---|
| 3.1 Chuẩn bị trước khi đăng bán | Xác định rõ bán cho ai, điểm bán hàng, đối thủ, dải giá, mức lãi tối thiểu, rủi ro hậu mãi | 🟢 A | **02 Product Strategy** |
| 3.2 Chiến lược định giá và SKU | Bản cấu hình thấp kéo traffic / bản chủ lực chốt đơn / bản cấu hình cao tăng giá trị đơn / combo tăng lợi nhuận | 🟢 A | **02 Product Strategy** |
| **3.3 Xây dựng Listing** | Tiêu đề cấu trúc năm cụm từ; **logic tạo 9 ảnh thương mại điện tử**; trang chi tiết cấu trúc 7 phần | 🟢 A | **03 Listing** ⭐ + **04 Image** ⭐ |
| 3.4 Khởi động nhiều link cho một sản phẩm | Thử nghiệm riêng nhiều bộ tiêu đề/ảnh chính/trang chi tiết, tìm link tốt nhất rồi tập trung scale | 🟢 A | **03 Listing (chế độ biến thể A/B)** ⭐ |
| 3.5 Nhịp độ quảng cáo và đánh giá | Hai biến: ngân sách tối đa × ROI mục tiêu; khung thử nghiệm 7 ngày | 🟡 B | **06 Advertising** |
| 3.6 Logic điều chỉnh quảng cáo | Chẩn đoán phễu bốn loại: có hiển thị không có click / có click không thêm vào giỏ / có thêm vào giỏ không chuyển đổi / chi tiêu cao ROI thấp | 🟡 B | **06 Advertising** |
| 3.7 Duy trì đánh giá và hậu mãi | Mời người mua thật đánh giá, khuyến khích ảnh/video review của người mua, quy nguyên nhân đánh giá tiêu cực, chuyển đổi tin nhắn hỏi hàng | 🟡 B | **07 Review** |
| 3.8 Theo dõi đối thủ theo từng sản phẩm | Biến động giá/doanh số/ảnh chính/tiêu đề/trang chi tiết/voucher/đánh giá/thứ hạng | 🟡 B | **01 Market Research (chế độ giám sát)** |
| **3.9 Rà soát dữ liệu từng sản phẩm** | Báo cáo ngày 11 chỉ số / báo cáo tuần 4 chiều / báo cáo tháng 5 quyết định | 🟡 B | **06 + 07 cùng xuất** |

### Chương 4: Thao tác backend và hệ thống hằng ngày (SOP 4.1 – 4.3)

| Mục SOP | Cấp | Ghi chú |
|---|---|---|
| 4.1 Kiểm tra tồn kho và quản lý đơn hàng | 🔴 C | Dự báo sáng tối mỗi buổi một lần, chặn đơn trên TMS, quy trình xử lý hoàn hàng → giữ nguyên SOP, có thể dùng RPA |
| 4.2 Trả lời khách và hậu mãi | 🟡 B | **Kịch bản CSKH có thể Agent hóa** (kịch bản chuyển đổi tin nhắn hỏi hàng, kịch bản hoàn tiền một phần, kịch bản phản hồi đánh giá tiêu cực) |
| 4.3 Học và ghi chép quy định sàn | 🟢 A | Mẫu ghi chép quy định (chuyện gì xảy ra/vì sao/ảnh hưởng/cách tránh) có thể mẫu hóa |

---

## III. Ranh giới module

### Phase 1 · Cụm phân tích (chuỗi tiền đề của SOP)

**Nút thắt của cụm này không nằm ở Prompt mà ở việc lấy dữ liệu.** Vì vậy đây là cụm duy nhất có kèm script.

```
Dữ liệu xuất theo ngành hàng
    │
    ▼
scripts/shaduola_parser.py   ← chuẩn hóa định dạng (dữ liệu bẩn → JSON thống nhất)
scripts/market_metrics.py    ← tính chỉ số (quy mô/mức độ tập trung/dải giá/bảng chéo cấu hình)
    │
    ▼  metrics.md + metrics.json
01 Market Research Agent     ← chỉ diễn giải, không tính lại
    │ Đầu ra: có nên làm không / mức giá nào / cấu hình nào
    ▼
02 Product Strategy Agent    ← quy chuẩn hóa (không ra quyết định chọn sản phẩm)
    │ Đầu ra: bảng yêu cầu sản phẩm (một điểm bán hàng chủ lực duy nhất + cơ cấu SKU + định giá + danh sách rủi ro)
```

### Phase 2 · Cụm sáng tạo (các khâu 🟢 cấp A trong SOP và nối tiếp nhau)

Lý do chọn: **đầu vào dạng biểu mẫu, đầu ra kiểm chứng được, phụ thuộc lẫn nhau**.

```
product requirement của 02 ┐
SOP 1.8 bảng từ khóa       ├──►  03 Listing Creative Agent
SOP 3.3 Listing            │     │ Đầu ra: tiêu đề / trang chi tiết / điểm bán hàng / thông số / từ khóa
SOP 2.3 khác biệt hóa      ┘     ▼
                          04 Product Image Agent
                          │ Đầu ra: kế hoạch 9 ảnh + Prompt tạo ảnh cho từng ảnh
                          ▼
                          05 Product Video Agent
                            Đầu ra: kịch bản / storyboard / Prompt video AI / lồng tiếng và phụ đề
```

### Phase 3 · Cụm vận hành (phần "dữ liệu định lượng được, kết luận phán định được" trong 🟡 cấp B của SOP)

Lý do chọn: **SOP đã viết logic chẩn đoán thành quy tắc phán định được (điều kiện → hành động)**, đây là dạng Agent làm tốt nhất.

```
Dữ liệu quảng cáo ──► 06 Advertising Optimization Agent
             │ Đầu ra: phán định phễu bốn loại + danh sách hành động + ROAS hòa vốn + nhịp phân bổ ngân sách
             │
             │ Quay vòng về (triệu chứng → khâu → đối tượng cụ thể)
             ▼
          03 / 04 (iterate: chỉ sửa phần mà triệu chứng chỉ ra)

Dữ liệu đánh giá ──► 07 Review Analysis Agent
             │ Đầu ra: quy nguyên nhân tám nhóm + nhận diện loại hiểu lầm + lằn ranh đỏ thông số + xếp hạng điểm bán hàng
             │
             │ Quay vòng về (đánh giá tiêu cực → trường → nội dung)
             ▼
          03 / 04 (iterate: bổ sung phần lưu ý / bổ sung ảnh danh sách đóng gói)
```

### Quan hệ giữa ba cụm

```text
01 Phân tích thị trường ──► 02 Chiến lược sản phẩm ──► 03/04/05 Sản xuất creative ──► Đăng bán
(có nên làm không)          (làm thành ra sao)          (thể hiện thế nào)              │
                                                                                         │
                        ┌────────────────────────────────────────────────────────────────┘
                        ▼
        06 Chẩn đoán quảng cáo ─┐
        07 Chẩn đoán đánh giá ──┴──► Quay về 03/04 sửa ──► Kiểm tra lại ──► Đạt thì scale / chưa đạt thì quay lại chẩn đoán
```

**Đây là ranh giới giữa bộ công cụ này và các "công cụ tạo nội dung một lần"**: Listing được tạo ra sẽ ngày càng chuẩn hơn nhờ dữ liệu thật.
Bản demo vòng khép kín (closed loop) đầy đủ xem tại [`Examples/03_Closed_Loop/`](../Examples/03_Closed_Loop/).
Chuỗi tiền đề đầy đủ xem tại [`01`](../Agents/01_Market_Research_Agent/examples/patinete_eletrico_market.md) → [`02`](../Agents/02_Product_Strategy_Agent/examples/patinete_eletrico_strategy.md).

### Ranh giới của từng module (làm gì / không làm gì)

| Agent | ✅ Phụ trách | ❌ Không phụ trách |
|---|---|---|
| **01 Market Research** | Đánh giá sơ bộ, quy mô thị trường, mức độ tập trung, dải giá, tổ hợp cấu hình, phân tích đối thủ ở mức cơ bản, **script tính chỉ số** | Quyết định chọn sản phẩm, định giá, bảng từ khóa (giao cho 03), quy nguyên nhân đánh giá chuyên sâu (giao cho 07) |
| **02 Product Strategy** | Định vị sản phẩm, cấu hình cốt lõi, chốt điểm bán hàng chủ lực, phòng tránh rủi ro, mô hình định giá, bốn vai trò SKU | **Quyết định chọn sản phẩm (cần người xác nhận)**, thẩm định giá vốn, quy định chương trình của sàn, thu mua thực tế |
| **03 Listing Creative** | Phân loại từ khóa, tạo tiêu đề, trang chi tiết 7 phần, đúc kết điểm bán hàng, bảng thông số, tự kiểm tra tuân thủ | Quyết định chọn sản phẩm, định giá, đặt giá thầu quảng cáo |
| **04 Product Image** | Lên kế hoạch nội dung 9 ảnh, bố cục/chữ trên ảnh/Prompt tạo ảnh cho từng ảnh, kiểm tra nền trắng và tuân thủ | Render ảnh thực tế (giao cho ImageGen / Midjourney), kiểm tra chất lượng sau render |
| **05 Product Video** | Kịch bản 15s/30s, bảng storyboard, Prompt cho từng cảnh quay, kịch bản lồng tiếng, phụ đề | Dựng và ghép video thực tế, mua bản quyền BGM |
| **06 Advertising** | Chẩn đoán phễu, danh sách hành động, tính ngưỡng hòa vốn, ngân sách và ROI mục tiêu, nhịp phân bổ ngân sách | Thực sự sửa giá sửa ảnh, thao tác backend, đấu thầu theo thời gian thực |
| **07 Review Analysis** | Phân loại và quy nguyên nhân, nhận diện loại hiểu lầm, xếp hạng điểm bán hàng, lằn ranh đỏ thông số, đề xuất vá lỗi, kịch bản CSKH | Thực sự sửa Listing, thao tác backend, liên hệ người mua |

**Hợp đồng bàn giao rõ ràng**:

- 01 → 02: thiếu `opportunity_config` / `cost_floor_price` thì 02 không làm việc được
- 02 → 03: `core_selling_point` bắt buộc chỉ là **một câu duy nhất**, nếu không toàn bộ chuỗi phía sau của 03 sẽ mất trọng tâm
- 03 → 04/05: thiếu `core_selling_point` / `forbidden_words` thì 04/05 **không được bắt đầu**
- 06/07 → 03/04: đầu ra bắt buộc kèm "triệu chứng → khâu → đối tượng cụ thể", nếu không thì không được chạy `iterate`

---

## IV. Luồng dữ liệu liên module

Các module giao tiếp với nhau qua một **sản phẩm trung gian chuẩn** (định nghĩa xem tại [`Templates/product_brief_template.md`](../Templates/product_brief_template.md)):

| Trường | Nguồn | Bên sử dụng | Bắt buộc |
|---|---|---|---|
| `product_name` | Người nhập | 03/04/05 | ✅ |
| `target_market` | Người nhập | 03/04/05 | ✅ |
| `core_selling_point` | **Đầu ra 03** | 04/05 | ✅ **Mục chặn** |
| `secondary_points[]` | **Đầu ra 03** | 04/05 | ✅ |
| `spec_table` | **Đầu ra 03** | 04 | ✅ |
| `keyword_classified` | **Đầu ra 03** | 04 (điểm bán hàng trên ảnh chính) / 05 (phụ đề) | ✅ |
| `title_final` | **Đầu ra 03** | 05 (CTA cuối video) | ⭕ Khuyến nghị |
| `forbidden_words[]` | **Đầu ra tự kiểm tra tuân thủ của 03** | 04/05 chặn cứng | ✅ **Mục chặn** |

> Ý nghĩa của bộ hợp đồng này: giúp AI **không làm mất thông tin, không bịa thông tin khi truyền giữa các module**. 04 không nhận được `core_selling_point` thì báo lỗi, chứ không tự đoán bừa một cái.

### Các trường quay vòng về (mới ở v0.2)

Đầu ra của 06 và 07 bắt buộc kèm thông tin ba cấp "**triệu chứng → khâu → đối tượng cụ thể**", nếu không thì chế độ `iterate` của 03/04 không được chạy:

| Trường | Nguồn | Đích quay về | Mục đích |
|---|---|---|---|
| `symptom_by_group` | 06 | 03/04 | Nêu rõ triệu chứng, tránh sửa nhầm khâu |
| `ctr_fail_groups[]` | 06 | 03 / 04 | Sửa từ khóa trong tiêu đề / đổi ảnh chính |
| `atc_fail_groups[]` | 06 | 03 | Tối ưu trang chi tiết / điều chỉnh SKU |
| `cvr_fail_groups[]` | 06 | 03 / 07 | Sửa cách hiển thị giá / khởi động phân tích đánh giá |
| `breakeven_roas` | 06 | Mốc so sánh khi kiểm tra lại | Đánh giá vòng sau có lãi hay không |
| `review_patch_suggestions[]` | 07 | 03 | Viết bổ sung phần lưu ý trên trang chi tiết |
| `forbidden_words_candidates[]` | 07 | 03 / 04 / 05 | Thêm vào danh sách chặn cứng |
| `selling_points_ranked[]` | 07 | 03 / 04 | Quyết định nội dung chính trên ảnh chính và từ khóa trong tiêu đề |
| `packaging_clarity_needed` | 07 | 04 | Có cần bổ sung ảnh danh sách đóng gói không |

**Ràng buộc cứng của vòng quay về**: chế độ `iterate` **chỉ sửa khâu mà triệu chứng chỉ ra**, các phần còn lại giữ nguyên. Đây là tiền đề để "hiệu quả quy được nguyên nhân".

---

## V. Những nội dung SOP đã bị **viết lại**

SOP gốc có vài thao tác thuộc dạng "lách luật" mà sàn cấm rõ ràng. Là một dự án mã nguồn mở, chúng tôi **không chép lại, không hiện thực hóa**, nhưng giữ lại mục tiêu kinh doanh mà nó muốn đạt được và đưa ra hướng thay thế tuân thủ (compliance).

Bảng đối chiếu đầy đủ xem tại **[`03_Compliance_Guard.md`](./03_Compliance_Guard.md)**, danh mục từng hạng mục không triển khai xem tại **[`05_SOP_Gap_Register.md`](./05_SOP_Gap_Register.md)**. Tóm tắt:

| Nội dung gốc trong SOP | Xử lý | Thay thế tuân thủ |
|---|---|---|
| Buff đơn ảo / đơn test review / tạo SKU giả để lách kiểm soát rủi ro | ❌ Loại bỏ | Khuyến mãi giá thấp có thật để nhanh chóng phá mốc 0 đơn + voucher không công khai để mời đánh giá |
| Tổ chức nhóm để đánh giá tiêu cực đối thủ | ❌ Loại bỏ | Quy nguyên nhân đánh giá tiêu cực của đối thủ → chuyển thành phần giải thích phòng ngừa trên trang chi tiết của mình |
| "Quảng cáo sai sự thật trong phạm vi kiểm soát được", giải thích cho việc khai khống thông số | ❌ Loại bỏ | Bảng ánh xạ điểm bán hàng về sự thật + kiểm tra tính nhất quán thông số |
| Dùng voucher dụ dỗ đánh giá, sửa MD5 để lách kiểm tra | ❌ Loại bỏ | Kênh mời đánh giá chính thức được sàn cho phép |

---

## VI. Tình trạng hoàn thành và bước tiếp theo

| Ưu tiên | Module | Trạng thái | Ghi chú |
|---|---|---|---|
| P0 | 06 Advertising Optimization | ✅ **Hoàn thành v0.2** | Quy tắc chẩn đoán phễu trong SOP 3.5–3.6 đầy đủ nhất, chi phí chuyển đổi thấp nhất |
| P0 | 07 Review Analysis | ✅ **Hoàn thành v0.2** | Đầu vào là văn bản đánh giá, tác vụ thuần văn bản, Agent hợp sẵn |
| P1 | 01 Market Research | ✅ **Hoàn thành v0.3** | **Làm luôn cả script** —— lấy dữ liệu là bài toán kỹ thuật, không thể chỉ để lại một Prompt |
| P2 | 02 Product Strategy | ✅ **Hoàn thành v0.3** | Phụ thuộc 01, bàn giao cùng 01 |

✅ **Đã hoàn thành cả 7 module.**

### Năm nhận thức mới sau khi làm xong

Bốn nhận thức đầu là những phán đoán được điều chỉnh trong quá trình phân rã và hiện thực hóa, nhận thức thứ năm thuộc về phương pháp luận:

**Nhận thức 1 · Ngưỡng chuẩn và ngưỡng hòa vốn là hai chuyện khác nhau**

Ngưỡng chuẩn SOP đưa ra (CTR 3–5% / chuyển đổi >1% / thêm vào giỏ >8%) dùng để xác định "**khâu nào không khỏe**".
Nhưng **phễu đạt chuẩn toàn bộ vẫn có thể lỗ** —— trong case study của 06, một nhóm quảng cáo khỏe cả ba khâu nhưng ROAS 2,73 vẫn thấp hơn ngưỡng hòa vốn 2,82.

**Nhận thức 2 · "Đánh giá tiêu cực loại hiểu lầm" là hạng mục sửa có tỷ suất đầu tư/hiệu quả cao nhất**

SOP liệt kê đánh giá tiêu cực theo hiện tượng, nhưng không tách "**vấn đề do mô tả**" với "**vấn đề do sản phẩm**".
Tách ra rồi mới có kết luận bất ngờ: **84,6% đánh giá tiêu cực có thể giải quyết bằng cách sửa nội dung** (case study xe điện), và sửa xong là có hiệu lực ngay.

**Nhận thức 3 · Phân rã có ranh giới do con người làm thực dụng hơn một giải pháp kỹ thuật toàn diện**

Định vị của module 01 được đổi từ "làm một Agent phân tích thị trường" thành "**làm một pipeline dữ liệu + một Agent diễn giải**".
Lý do: mức độ tập trung, chia bin, bảng chéo là các phép tính tất định, **để mô hình tính lại sinh ra bất định**.
Hình thái cuối cùng là "script tính + Agent diễn giải", chứ không phải "giao hết cho Agent".

**Nhận thức 4 · Ràng buộc "không sửa gì" quan trọng ngang ràng buộc "sửa gì"**

Đầu ra của 06 bắt buộc có «Phần giữ nguyên trong vòng này», chế độ `iterate` của 03/04 chỉ sửa khâu mà triệu chứng chỉ ra.
Lý do: hao tổn lớn nhất trong vòng khép kín không phải là sửa chưa đúng, mà là **làm hỏng những khâu vốn đang hiệu quả**.

**Nhận thức 5 · "Kết quả tái lập được" phải là mức tối thiểu của một bộ công cụ mã nguồn mở**

Sau khi case study của 01 được làm thành "ba lệnh là tái lập được", đã lộ ra ba vấn đề trước đó không nhìn thấy:
- Trung bình trượt 3 điểm làm mất vùng trũng (valley) (mất ranh giới dải giá)
- Thiết kế của `item_share_all` khiến phán định "cấu hình chủ đạo" luôn là false
- CR10 luôn bằng 100% khi số chủ thể ≤ 10, dễ bị hiểu nhầm là "độc quyền hoàn toàn"

**Ba vấn đề này sẽ không bao giờ được phát hiện nếu chỉ có tài liệu mà không có code chạy được.**

> **Đây là bài học quan trọng nhất lần này**: viết phương pháp luận thành tài liệu thì dễ, viết thành thứ mà "người khác chạy trọn vẹn được và ra cùng kết quả" thì khó —— mà cái sau mới là giá trị của mã nguồn mở.

---

**Tài liệu liên quan**: [01 Quy chuẩn thiết kế Prompt](./01_Prompt_Design_Guide.md) · [02 Quy chuẩn trường dữ liệu theo sàn](./02_Platform_Output_Spec.md) · [03 Lằn ranh đỏ tuân thủ](./03_Compliance_Guard.md) · [04 Checklist tự kiểm tra trước khi bàn giao](./04_Result_Checklist.md)
