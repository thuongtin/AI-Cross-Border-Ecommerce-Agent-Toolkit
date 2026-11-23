# CHANGELOG

File này ghi lại các thay đổi về cấu trúc và nội dung của bộ công cụ.

---

## [v0.3] — 2026-10-13

Bổ sung **cụm phân tích (chuỗi tiền đề)**: 01 Phân tích thị trường, 02 Chiến lược sản phẩm. **Cả 7 module Agent đã hoàn thành.**

Đợt này cũng chốt ba quyết định trước đó được đánh dấu "chờ xác nhận", đồng thời thêm tài liệu sổ đăng ký khác biệt.

### Xác nhận quyết định

| # | Hạng mục | Kết luận |
|---|---|---|
| 1 | **Sắp xếp lại mã số Agent** | ✅ **Chấp nhận**. Theo cụm công việc: `01-02` cụm phân tích → `03-04-05` cụm sáng tạo → `06-07` cụm vận hành |
| 2 | **Danh sách gốc「logic tạo 9 ảnh」trong SOP** | ✅ **Dùng khung 9 ảnh do repo này tự suy ra**, không chờ bản gốc nữa. Logic suy ra (ba bước) đã được viết vào mục 2 của [`04 README`](./Agents/04_Product_Image_Agent/README.md) |
| 3 | **Có giữ phần "xám" của SOP làm phụ lục không** | ✅ **Giữ, nhưng làm thành "sổ đăng ký" chứ không phải "hướng dẫn thao tác"**. Xem tài liệu mới bên dưới |

### Tài liệu mới

#### `docs/05_SOP_Gap_Register.md` — Sổ đăng ký khác biệt so với SOP

Ghi lại những nội dung trong SOP gốc không được triển khai: **bản gốc đề cập gì → vì sao không triển khai → có phương án thay thế tuân thủ không → phương án thay thế nằm ở đâu**.

- Bao quát 10 mục, chia ba nhóm: dữ liệu và đánh giá / nội dung và thông số / nhịp độ vận hành
- Liệt kê thêm **7 chỗ "cộng thêm"** của repo này (SOP không có, chúng tôi bổ sung)
- Đồng thời đưa ra cách tự kiểm tra cho người dùng (ba câu hỏi để xác định có nên làm một hành động hay không)

> ⚠️ **Quyết định thiết kế an toàn**: tài liệu này chỉ ghi ở "**mức kết luận**", **không thuật lại chi tiết thao tác**.
> Lý do: repo mã nguồn mở chứa hướng dẫn thao tác vi phạm sẽ bị hệ thống kiểm soát rủi ro của sàn nhận diện, và cũng khiến người dùng bị liên đới thiệt hại. **Mục đích của việc đăng ký là minh bạch, không phải phát tán.**

### Module mới

#### `Agents/01_Market_Research_Agent`

⚠️ **Module này khác với năm module trước: nó có kèm script.**

Nhận định trước đó là "nút thắt của 01 nằm ở việc lấy dữ liệu, không nằm ở Prompt". Đã chấp nhận nhận định này thì làm luôn cả script —— nếu không thì chỉ là đẩy cái khó sang cho người dùng.

| File | Nội dung |
|---|---|
| `scripts/shaduola_parser.py` | Chuẩn hóa định dạng: ký hiệu tiền tệ / dấu phân cách hàng nghìn / số thập phân kiểu châu Âu / đơn vị số lượng tiếng Trung (万/亿) / ký hiệu giá trị rỗng / ngày tháng → JSON thống nhất; khớp mờ tên cột + chỉ định thủ công bằng `--mapping`; `--profile` chỉ xem kết quả nhận diện |
| `scripts/market_metrics.py` | Tính chỉ số: quy mô thị trường / mức độ tập trung thương hiệu và người bán (CR3·CR10·HHI) / chia khoảng giá + **phát hiện vùng trũng** / bảng chéo cấu hình (phán đoán 4 chiều) |
| `scripts/make_sample.py` | Tạo dữ liệu mẫu có lẫn dữ liệu bẩn, để người dùng vừa clone về là chạy trọn vẹn được |
| `scripts/README.md` | Cách dùng + giải thích thuật toán (kèm lý do không làm mượt) |
| `samples/` | CSV mẫu + JSON đã chuẩn hóa + báo cáo chỉ số (kèm **bảng kết quả kỳ vọng**, dùng để kiểm tra môi trường) |
| `prompts/00_system.md` | Vai trò + ngưỡng phán đoán của SOP + lớp bảo vệ tuân thủ M1–M5 |
| `prompts/01_category_precheck.md` | Đánh giá sơ bộ SOP 1.1 (kèm **kiểm tra sức chịu lợi nhuận** cho ngành hàng rủi ro cao) |
| `prompts/02_market_analysis.md` | SOP 1.2–1.6 (quy mô thị trường / mức độ tập trung / dải giá / cấu hình / đối thủ) |
| `templates/` | input_category_research · output_market_analysis |
| `examples/patinete_eletrico_market.md` | Case study tái hiện được (ba lệnh đối chiếu từng con số) |

**Bốn thiết kế cốt lõi**:

1. **Cái gì tính được thì đừng để model đoán** —— mức độ tập trung/chia khoảng/bảng chéo là tính toán tất định, giao cho script; Agent chỉ diễn giải "những con số này có ý nghĩa gì"
2. **Phát hiện vùng trũng không làm mượt** —— trung bình trượt 3 điểm sẽ xóa mất các vùng trũng dốc (trong dữ liệu mẫu, vùng trũng `799→618→1120` bị làm trung bình thành `639→846→912`, vùng trũng biến mất)
3. **Đánh giá sơ bộ có quyền dừng** —— SOP 1.1 nói "không có năng lực chuỗi cung ứng/hậu mãi hay lợi thế giá thì dù thị trường tốt cũng chưa chắc nên làm", nên khi không đạt thì **dừng, không làm phân tích hạ nguồn**
4. **Tự động cảnh báo bẫy CR-n** —— khi số chủ thể ≤ n thì CR-n luôn bằng 100%, script tự động nhắc chuyển sang dùng CR3 và HHI

#### `Agents/02_Product_Strategy_Agent`

| File | Nội dung |
|---|---|
| `prompts/00_system.md` | Vai trò + quy tắc định giá và SKU + lớp bảo vệ tuân thủ S1–S5 |
| `prompts/01_product_decision.md` | SOP 1.7 + 3.1: định vị / cấu hình / **chốt điểm bán hàng chủ lực (duy nhất)** / né rủi ro / 8 câu hỏi trước khi đăng bán |
| `prompts/02_pricing_and_sku.md` | SOP 1.9 + 3.2: công thức định giá + kiểm tra lại từng SKU + 4 vai trò SKU + thiết kế voucher + ngưỡng hòa vốn |
| `templates/` | input_strategy_brief · output_product_requirement |
| `examples/patinete_eletrico_strategy.md` | Case study đầy đủ (nối tiếp output của 01) |

**Ba thiết kế cốt lõi**:

1. **Cơ chế chặn `decision_approved`** —— module này **không ra quyết định chọn sản phẩm**, chỉ "chuẩn hóa thông số cho sản phẩm đã được quyết định". Chạy tiếp khi chưa có người xác nhận = để Agent ra quyết định kinh doanh thay bạn
2. **Điểm bán hàng chính phải là duy nhất** —— hai điểm ngang hàng nhau cũng như không có điểm nào. Điểm bán hàng chính quyết định ảnh chính in chữ gì, video mở đầu bằng cảnh nào
3. **4 vai trò SKU + kiểm tra bậc giá hai chiều** —— chênh giá quá lớn thì người mua không nâng cấp, quá nhỏ thì SKU kéo traffic mất ý nghĩa

### Hai "sự trùng hợp nhất quán" trong case study

Khi làm case study cho 01, 02, xuất hiện hai điểm kiểm chứng mà **hai cách suy luận độc lập cùng dẫn tới một kết quả**, cả hai đều được giữ lại trong case study:

| Sự trùng hợp phát hiện được | Ý nghĩa |
|---|---|
| Cận dưới dải giá do phát hiện vùng trũng tìm ra là **R$ 1.989,13** vs giá khả thi theo chi phí tính ngược từ công thức định giá là **R$ 1.989,36**, chênh **R$ 0,23** | Một bên thuần toán học (đường cong doanh số), một bên thuần tài chính (cấu trúc chi phí) → mức giá này vừa khớp cấu trúc thị trường vừa khả thi về chi phí |
| Dư địa lợi nhuận gộp của SKU chủ lực **R$ 98,95** vs mệnh giá voucher dự kiến **R$ 100**, chênh **R$ 1,05** | Khoảng cách giữa giá thị trường chấp nhận (2.199) và yêu cầu chi phí (1.989) vừa đủ để phát một voucher "thu hẹp chênh lệch giá" |

> Hai con số này không phải gán ghép, mà là kết quả cùng quyết định bởi "thị trường sẵn sàng trả bao nhiêu + chi phí cần bao nhiêu". **Việc chúng xuất hiện cho thấy phương pháp này nhất quán từ bên trong.**

### Nhận thức mới

| # | Nhận thức | Bằng chứng |
|---|---|---|
| 1 | **CR cao ≠ độc quyền** | Trong case study, CR3 thương hiệu = 74,1% trông rất cao, nhưng **cả ba vị trí đầu đều là hàng no-brand** → người mua không quan tâm thương hiệu, shop mới vẫn còn đất |
| 2 | **Phải xem tỷ lệ giữa thị phần và số sản phẩm** | Một người bán chiếm 8,5% doanh số nhưng chiếm 12% số sản phẩm → **kiểu chiếm chỗ chứ không phải kiểu hiệu quả**, là đối tượng có thể vượt qua |
| 3 | **"Cấu hình cao" chưa chắc lợi nhuận gộp cao** | Bản 800W chi phí tăng 34,8% nhưng giá bán chỉ tăng 22,7% → biên lợi nhuận ròng bản cấu hình cao 32,3% **thấp hơn SKU chủ lực 36,5%** |
| 4 | **Mức tự do của "giai đoạn đầu giảm lợi nhuận gộp để nuôi trọng số" phụ thuộc vào dư địa** | Trong case study, ở R$ 1.999 biên lợi nhuận ròng vẫn còn 32,2%, thực ra chưa hề giảm thật —— vì bản thân mức định giá đã có dư địa dồi dào |
| 5 | **SKU kéo traffic thấp hơn lợi nhuận gộp mục tiêu ≠ lỗ chiến lược** | 27,5% thấp hơn mục tiêu 32% nhưng vẫn trên ngưỡng hòa vốn (giá tới hạn R$ 1.113) → không cần ghi chú lỗ và điều kiện rút lui |

### Cập nhật tài liệu

- `README.md`: bảng toàn cảnh Agent (hoàn thành 7/7) · cây thư mục (kèm `scripts/`, `samples/`) · sơ đồ mermaid vòng khép kín (kèm 01/02) · lộ trình · badge → v0.3 · tuyên bố tuân thủ thêm đường dẫn tới sổ đăng ký khác biệt
- `Agents/README.md`: danh sách hoàn thành v0.3 + **bảng hợp đồng xuôi chiều** (ai phải đưa gì cho ai, thiếu thì báo lỗi gì)
- `docs/00`: thêm ranh giới module của cụm phân tích + "làm gì/không làm gì" của từng module
- `docs/03`: thêm ở đầu phần giải thích phân công với `05` (tài liệu này nói "thay thế thế nào", 05 nói "vì sao không làm")
- `docs/04` / `Templates/output_qa_checklist.md`: bổ sung phần tự kiểm tra cho 01/02 (chờ bổ sung)
- `ROADMAP.md`: đánh dấu v0.3 hoàn thành, đóng nợ kỹ thuật #1, #4, thêm #7–#9
- `Examples/README.md`: cập nhật mục lục case study

---

## [v0.2] — 2026-10-13

Hoàn thành **cụm vận hành Phase 2**: thêm hai module 06 Tối ưu quảng cáo, 07 Phân tích đánh giá, và khép toàn bộ quy trình thành vòng.

### Module mới

#### `Agents/06_Advertising_Optimization_Agent`

| File | Nội dung |
|---|---|
| `README.md` | Bảng chẩn đoán phễu 4 loại · đường chuẩn sức khỏe · **thuật toán ROAS hòa vốn** · hai mẹo thực chiến trong SOP (không tạm dừng quảng cáo / đổi ảnh chính để gỡ bug) |
| `prompts/00_system.md` | Vai trò + đường chuẩn + thứ tự xét phễu (quy tắc cứng: phần trước chưa đạt thì cấm chỉnh giá thầu) + lớp bảo vệ tuân thủ G1–G5 |
| `prompts/01_funnel_diagnosis.md` | Xét 4 bước cho từng nhóm quảng cáo → danh sách hành động (**bắt buộc xuất "phần vòng này chắc chắn không đụng tới"**) + quy trình gỡ bug + phương án kiểm tra lại |
| `prompts/02_budget_roi_model.md` | Tính ngưỡng hòa vốn + bảng độ nhạy ROAS + phân tích khoảng cách tới ngưỡng đạt + mô hình 2 biến ngân sách×ROI + nhịp theo khung giờ |
| `templates/input_ad_data.md` | Dữ liệu quảng cáo + cấu trúc chi phí (kèm ngưỡng chất lượng dữ liệu) |
| `templates/output_ad_action_plan.md` | Danh sách hành động (hạ nguồn: 03/04/07) |
| `examples/powerbank_20000mah_ads.md` | Case study thật: 4 nhóm quảng cáo bao phủ đủ 4 loại triệu chứng, ROAS tổng 1,84 đang lỗ |

**Ba thiết kế cốt lõi**:

1. **Không được nhảy cóc thứ tự xét phễu**: CTR → tỷ lệ thêm vào giỏ → tỷ lệ chuyển đổi → ROAS. **Chỉ khi các phần trước đều đạt mới được đề xuất chỉnh giá thầu.**
2. **Ngưỡng hòa vốn đặt trên đường chuẩn**: đường chuẩn cho biết "khâu nào không khỏe", ngưỡng hòa vốn cho biết "có lãi hay không". Phải xem cả hai —— vì **phễu đạt hết vẫn có thể lỗ**.
3. **Ngưỡng chất lượng dữ liệu**: lượt hiển thị < 1,000 thì từ chối phân tích; thiếu cấu trúc chi phí thì từ chối xuất bất kỳ kết luận ROI nào.

#### `Agents/07_Review_Analysis_Agent`

| File | Nội dung |
|---|---|
| `README.md` | Quy nguyên nhân đánh giá tiêu cực theo 8 nhóm · **vì sao tách riêng loại hiểu lầm** · 3 loại quay vòng về (vá trang chi tiết / lằn ranh đỏ thông số / xếp hạng điểm bán hàng) · ranh giới tuân thủ |
| `prompts/00_system.md` | Vai trò + định nghĩa quy nguyên nhân 8 nhóm + tiêu chuẩn xác định loại hiểu lầm ("mô tả không sai mà khách vẫn không hài lòng = lỗi của mô tả") + lớp bảo vệ tuân thủ C1–C5 |
| `prompts/01_classify_and_attribute.md` | 5 chiều đánh giá tích cực + quy nguyên nhân 8 nhóm đánh giá tiêu cực + xếp hạng điểm bán hàng theo tần suất×cường độ cảm xúc + so sánh đối thủ + 7 câu hỏi của SOP |
| `prompts/02_misunderstanding_detector.md` | **Ba kiểu xác định loại hiểu lầm** (thiếu giải thích / giải thích không nổi bật / người mua không đọc) + copy vá trang chi tiết + lằn ranh đỏ thông số |
| `templates/input_review_batch.md` | Nhập đánh giá hàng loạt (kèm ngưỡng cỡ mẫu ≥ 20) |
| `templates/output_review_insights.md` | Báo cáo insight đánh giá (hạ nguồn: 03/04) |
| `examples/electric_scooter_reviews.md` | Case study thật: 128 đánh giá, **đánh giá tiêu cực sửa được 84,6%**, loại hiểu lầm chiếm 38,5% |

**Ba thiết kế cốt lõi**:

1. **Tách riêng đánh giá tiêu cực loại hiểu lầm**: đây là loại duy nhất "sửa một câu là hết" —— chi phí gần bằng 0, sửa xong có hiệu lực ngay, ROI cao nhất.
2. **Ba kiểu xác định**: thiếu giải thích → thêm mục mới; giải thích không nổi bật → đưa lên đầu; người mua không đọc → **chuyển thành ảnh** (chữ sẽ bị lướt qua, ảnh thì không).
3. **Hiểu lầm về phụ kiện bắt buộc dùng ảnh**: cả 2 đánh giá tiêu cực về phụ kiện đều do người mua không đọc bảng thông số —— gửi bù phụ kiện là sai, hành động đúng là dùng ảnh danh sách đóng gói ghi rõ "không bao gồm những gì".

### Case study vòng khép kín mới

#### `Examples/03_Closed_Loop/`

Demo cơ chế đầy đủ của chương 3 SOP "review dữ liệu → quay lại tối ưu bốn khâu phía trước":

- **Quay vòng về từ phía quảng cáo** (Power Bank): 06 chẩn đoán → xác định nút thắt là tỷ lệ chuyển đổi chứ không phải CTR → can thiệp → kiểm tra lại sau 7 ngày → **đóng góp ròng −R$ 235,56 → +R$ 83,90**
- **Quay vòng về từ phía đánh giá** (Electric Scooter): 07 chẩn đoán → 84,6% đánh giá tiêu cực sửa được → quay về 03/04 → kiểm tra lại sau 14–30 ngày
- **Cái bẫy ngược trực giác**: sửa nhóm có CTR tệ nhất → lỗ mở rộng tới −R$ 335,26; tăng lượt hiển thị → lỗ tăng theo cùng tỷ lệ
- **Nguyên tắc chọn chỉ số kiểm tra lại**: phải chọn chỉ số "thay đổi kiểm soát được" (quảng cáo xem ROAS, copy xem tỷ lệ loại hiểu lầm, đều không xem tổng doanh số)

### Cơ chế thiết kế mới

| Cơ chế | Mô tả |
|---|---|
| **ROAS hòa vốn** | Mẫu số trừ đi bốn tỷ lệ phần trăm phí hoa hồng/quảng cáo/hoàn hàng/lợi nhuận gộp; `ROAS < ngưỡng hòa vốn` tức là mỗi đơn đều lỗ |
| **Ngưỡng đạt vs ngưỡng hòa vốn** | Chỉ rõ khoảng cách "định giá chừa chi phí quảng cáo 7.5% tương ứng ROAS 13,33, trong khi chạy quảng cáo thực tế thường chỉ 3–8" |
| **Thứ tự xét phễu là quy tắc cứng** | Phần trước chưa đạt mà đã chỉnh giá thầu = đề xuất vi phạm, Prompt bắt buộc phải từ chối |
| **"Phần vòng này chắc chắn không đụng tới"** | Mục bắt buộc xuất của 06 —— tránh việc sửa khâu A rồi tiện tay làm hỏng khâu B |
| **Ba kiểu loại hiểu lầm** | Biến mong muốn "muốn xóa đánh giá tiêu cực" thành ba hành động làm được: "bổ sung giải thích / đưa lên đầu / chuyển thành ảnh" |
| **Chỉ số kiểm tra lại quy được nguyên nhân** | Chọn chỉ số mà thay đổi kiểm soát được: quảng cáo xem ROAS, copy xem tỷ lệ loại hiểu lầm |

### Cập nhật tài liệu

- `README.md`: cập nhật bảng toàn cảnh Agent (5 module đã hoàn thành) · cây thư mục · sơ đồ mermaid vòng khép kín · lộ trình
- `Agents/README.md`: tách danh sách hoàn thành v0.1/v0.2 + thêm bảng **hợp đồng quay vòng về**
- `docs/04_Result_Checklist.md`: thêm ba phần tự kiểm tra F (06) / G (07) / H (vòng khép kín)
- `Templates/output_qa_checklist.md`: đồng bộ thêm các phần F/G/H
- `Examples/README.md`: thêm mục lục case study vòng khép kín + bảng bao phủ năm sản phẩm (hiện mỗi sản phẩm đã được ít nhất hai module phân tích)
- `ROADMAP.md`: đánh dấu v0.1/v0.2 hoàn thành, thêm nợ kỹ thuật mục 5, 6

### Xử lý tuân thủ (tiếp nối nguyên tắc v0.1)

Module 07 liên quan tới quy trình xử lý đánh giá tiêu cực ở SOP 3.7, trong đó các hành động sau **không được đưa vào**:

| Diễn đạt gốc trong SOP | Xử lý |
|---|---|
| Liên hệ khách xóa đánh giá tiêu cực, nói xóa xong sẽ hoàn tiền nhanh và bồi thường thêm | ❌ Loại bỏ (dùng lợi ích để dụ xóa đánh giá) |
| Nếu sản phẩm khai khống thông số thì có thể nói là đóng gói nhầm sách hướng dẫn | ❌ Loại bỏ (dùng lý do sai sự thật để giải thích thông số không khớp) |
| Report đánh giá tiêu cực trước, có cơ hội xóa được | ⚠️ Giữ "từng đánh giá vi phạm rõ ràng có thể khiếu nại bình thường", loại bỏ "report có tổ chức" |
| **Tối ưu ngược lại trang chi tiết, kịch bản CSKH hoặc sản phẩm** | ✅ **Giữ lại và nâng thành output cốt lõi của 07** |

Chi tiết xem [`docs/03_Compliance_Guard.md`](./docs/03_Compliance_Guard.md).

### Vấn đề đã biết

| # | Vấn đề | Trạng thái |
|---|---|---|
| 7 | Đầu vào của 06/07 phụ thuộc điền bảng thủ công (dữ liệu quảng cáo / đánh giá phải xuất thủ công) | Sẽ hết khi V2 kết nối API |
| 8 | Dữ liệu review chưa tự quay vòng về được, `iterate` cần dán thủ công | Sẽ hết khi v1.0 nối chuỗi |

---

## [v0.1] — 2026-10-13

Phiên bản đầu tiên. Hoàn thành ba Agent cụm sáng tạo của **Phase 1**.

### Thêm mới

**Module cốt lõi (Phase 1)**

| Module | Nội dung |
|---|---|
| `Agents/03_Listing_Creative_Agent` | Tách từ khóa thành 7 loại · công thức tiêu đề 5 đoạn · trang chi tiết 7 phần · phân tầng điểm bán hàng · kiểm tra nhất quán thông số |
| `Agents/04_Product_Image_Agent` | Lên kế hoạch nội dung 9 ảnh · Prompt tạo ảnh cho từng ảnh · thư viện Negative Prompt · lớp bảo vệ tuân thủ cho ảnh |
| `Agents/05_Product_Video_Agent` | Kịch bản 2 phiên bản 15s/30s · bảng storyboard · Prompt video AI · bản lồng tiếng · phụ đề · kiểm tra khả năng đọc khi tắt tiếng |

**Ghi chú module giữ chỗ (Phase 2)**

`01 Market Research` · `02 Product Strategy` · `06 Advertising Optimization` · `07 Review Analysis`

**Tài liệu phương pháp**

| File | Nội dung |
|---|---|
| `docs/00_Architecture_SOP_to_Agent.md` | Bảng tách đầy đủ 38 trang SOP → 7 Agent (kèm phương pháp phân 3 cấp) |
| `docs/01_Prompt_Design_Guide.md` | Chuẩn 5 thành phần của Prompt + 4 quy tắc cứng + chiến lược ngôn ngữ output |
| `docs/02_Platform_Output_Spec.md` | Chỉ tiêu cứng về trường của Shopee / ML / Amazon / TikTok Shop / Shopify |
| `docs/03_Compliance_Guard.md` | Lằn ranh đỏ tuân thủ + bảng đối chiếu viết lại thao tác "xám" + bảng ánh xạ chân thực hóa điểm bán hàng |
| `docs/04_Result_Checklist.md` | Checklist tự kiểm tra khi bàn giao gồm 6 phần |

**Thư viện template** (`Templates/` cấp trên cùng)

`product_brief_template.md` (hợp đồng giao tiếp giữa các module) · `keyword_analysis_template.md` · `cost_pricing_template.md` (kèm công thức định giá kiểm tra lại được) · `output_qa_checklist.md` (bản in được)

**Thư viện case study**

| Case study | Module bao phủ | Trọng tâm |
|---|---|---|
| `Examples/01_Patinete_Eletrico_500W` | 03 → 04 → 05 | Nối chuỗi end-to-end · nén 120→60 ký tự khi chuyển sàn · kiểm tra nhất quán liên module |
| `Examples/02_Thermal_Bag` | 03 (iterate) | Chẩn đoán dữ liệu quảng cáo → vòng khép kín sửa lại với thay đổi tối thiểu |
| `Agents/03.../examples/powerbank_20000mah.md` | 03 | Dùng đánh giá để sửa ngược lại Listing |
| `Agents/04.../examples/pet_carrier.md` | 04 | Xử lý xung đột quy chuẩn ảnh chính giữa ML và Shopee |
| `Agents/05.../examples/air_fryer.md` | 05 | Hook lấy từ đánh giá tiêu cực · khả năng đọc khi tắt tiếng |

### Thay đổi cấu trúc

**Sắp xếp lại mã số Agent.** Kế hoạch ban đầu (từ bản hướng dẫn thực hiện) là:

```
01 Market Research → 02 Product Strategy → 03 Listing Creative
→ 04 Advertising → 05 Review → 06 Product Video
```

v0.1 đổi sang đánh số theo **cụm công việc**:

```
03 Listing Creative ─┐
04 Product Image     ├─ Cụm sáng tạo (copy → ảnh → video, vốn nối tiếp nhau)
05 Product Video     ┘

06 Advertising ─┐
07 Review      ─┴─ Cụm vận hành (quảng cáo → đánh giá)
```

**Lý do điều chỉnh**: để các module vốn nối tiếp nhau có mã số liền mạch, dễ tham chiếu; cụm sáng tạo và cụm vận hành không chồng chéo về quan hệ phụ thuộc.
**Ảnh hưởng**: `Product Video` từ `06` thành `05`; `Advertising` từ `04` thành `06`; `Review` từ `05` thành `07`; thêm `04 Product Image` (trong kế hoạch ban đầu không có mã số riêng).

### Cơ chế thiết kế mới

| Cơ chế | Mô tả |
|---|---|
| **Hợp đồng giao tiếp giữa các module** | 03 → 04/05 truyền các trường có cấu trúc qua `product_brief`, tránh thất thoát thông tin |
| **Trường chặn** | Khi `core_selling_point` / `forbidden_words`, v.v. để trống, module hạ nguồn bắt buộc báo lỗi, không được suy đoán |
| **Tách ngôn ngữ nội bộ / tiếng mẹ đẻ** | Văn bản người mua nhìn thấy dùng tiếng mẹ đẻ của thị trường mục tiêu, ghi chú nội bộ dùng tiếng Việt, Prompt bắt buộc phân biệt |
| **Nguồn thông số duy nhất** | Mọi giá trị số trong output phải truy được nguồn về `spec_table`, nếu không thì xóa và ghi `[PARAM_DROPPED]` |
| **Bắt buộc xuất khối quét tuân thủ** | Không có kết quả trùng khớp cũng phải ghi "không có kết quả trùng khớp", để xác nhận việc quét đã thực sự được chạy |
| **Negative Prompt làm công cụ tuân thủ** | Ảnh bối cảnh của sản phẩm không chống nước bắt buộc có từ phủ định `rain, water, swimming pool` |

### Xử lý tuân thủ

Các nội dung sau trong SOP gốc **không được đưa vào, không được triển khai**, kèm phương án thay thế tuân thủ:

| Diễn đạt gốc trong SOP | Xử lý |
|---|---|
| Buff đơn ảo / review ảo / tạo SKU giả để lách kiểm soát rủi ro | ❌ Loại bỏ → khuyến mãi giá thấp thật + voucher không công khai + mời đánh giá qua kênh chính thức |
| Tổ chức để lại đánh giá tiêu cực cho đối thủ | ❌ Loại bỏ → quy nguyên nhân đánh giá tiêu cực của đối thủ → giải thích phòng thủ cho mình |
| "Quảng cáo sai sự thật trong phạm vi kiểm soát được" | ❌ Loại bỏ → bảng ánh xạ chân thực hóa điểm bán hàng |
| Dùng voucher dụ dỗ đánh giá / đổi MD5 ảnh | ❌ Loại bỏ → kênh mời đánh giá chính thức |
| Khai khống thông số rồi giải thích là "đóng gói nhầm sách hướng dẫn" | ❌ Loại bỏ → kiểm tra nhất quán thông số ở ba nơi |

Chi tiết xem [`docs/03_Compliance_Guard.md`](./docs/03_Compliance_Guard.md).

### Vấn đề đã biết

| # | Vấn đề | Trạng thái |
|---|---|---|
| 1 | Danh sách cụ thể「logic tạo 9 ảnh thương mại điện tử」của SOP nằm ở dạng hình ảnh trong PDF, trích xuất văn bản không khôi phục được; khung 9 ảnh hiện tại là **bản suy ra** dựa trên cấu trúc trang chi tiết | Chờ tác giả SOP bổ sung rồi hiệu chỉnh |
| 2 | Bản gốc SOP ghi trang chi tiết có "8 phần" nhưng chỉ liệt kê 7 mục | Repo này làm theo 7 phần, chờ xác nhận |
| 3 | Quy định số ký tự / trường của sàn là quy định công khai tại thời điểm biên soạn, có thể đã lỗi thời | Đã ghi chú "kiểm tra lại trước khi đăng" ở nhiều chỗ |
| 4 | Trong `Examples/02_Thermal_Bag` đã đổi cùng lúc cả ảnh chính lẫn tiêu đề, không quy được nguyên nhân | Đã ghi rõ trong case study là điểm yếu của phương pháp và đưa ra phương án làm từng bước |

---

## Chờ phát hành

### v0.2 (kế hoạch)

- `06 Advertising Optimization Agent`: chẩn đoán phễu 4 loại + đối chiếu đường chuẩn + nhịp ngân sách
- `07 Review Analysis Agent`: quy nguyên nhân đánh giá + nhận diện đánh giá tiêu cực loại hiểu lầm → đề xuất vá trang chi tiết

### v0.3 (kế hoạch)

- `01 Market Research Agent`: cần giải quyết việc lấy dữ liệu trước (script phân tích + tính chỉ số)
- `02 Product Strategy Agent`: phụ thuộc 01

Chi tiết xem [`ROADMAP.md`](./ROADMAP.md).
