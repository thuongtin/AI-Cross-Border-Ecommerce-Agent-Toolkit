# 01 · Market Research Agent

**Agent phân tích thị trường** · Đầu vào là dữ liệu ngành hàng, đầu ra là nhận định **"sản phẩm này có nên làm không, làm ở mức giá nào, làm cấu hình gì"**.

---

## 1. Nó giải quyết vấn đề gì

Chương 1 của SOP có 10 mục nhỏ, tiêu chí đánh giá rất đầy đủ. Nhưng khi thực thi lại vướng ở hai chỗ:

| Điểm nghẽn | Biểu hiện | Module này giải quyết thế nào |
|---|---|---|
| **Dữ liệu không vào được** | File xuất đủ kiểu định dạng, lần nào cũng phải chỉnh tay | **`scripts/` có hai script**: chuẩn hóa định dạng + tính chỉ số |
| **Chỉ số tính không chuẩn / mỗi lần một khác** | Tự tính mức độ tập trung, vẽ đường cong giá, làm bảng chéo cấu hình bằng tay | Script tính (tất định), Agent chỉ diễn giải |
| **Tính xong không biết nghĩa là gì** | Một đống con số, không biết số nào cho thấy "làm được" | Prompt có sẵn ngưỡng đánh giá và quy tắc phán định của SOP |

**Sản phẩm đầu ra**: kết luận sàng lọc sơ bộ ngành hàng → nhận định quy mô thị trường và mức độ tập trung → chọn dải giá → khuyến nghị tổ hợp cấu hình → insight về đối thủ và đánh giá.

---

## 2. Các chương SOP được bao phủ

| SOP | Nội dung | Nằm ở đâu |
|---|---|---|
| **1.1** | Sàng lọc sơ bộ ngành hàng (có hợp nguồn hàng công ty không / có phải ngành hàng rủi ro cao không) | `prompts/01_category_precheck.md` |
| **1.2** | Phân tích quy mô thị trường và lượng bán | `prompts/02_market_analysis.md` |
| **1.3** | Mức độ tập trung thương hiệu và mức độ tập trung người bán | `prompts/02_market_analysis.md` |
| **1.4** | Phân tích giá (chia dải giá) | `prompts/02_market_analysis.md` + `scripts/market_metrics.py` |
| **1.5** | Phân tích loại sản phẩm và tổ hợp cấu hình | `prompts/02_market_analysis.md` + `scripts/market_metrics.py` |
| **1.6** | Phân tích đối thủ và phân tích đánh giá | `prompts/02_market_analysis.md` (phân tích đánh giá chuyên sâu giao cho [`07`](../07_Review_Analysis_Agent/)) |
| 1.7 | Chốt sản phẩm chủ lực | → giao cho [`02 Product Strategy`](../02_Product_Strategy_Agent/) |
| 1.8 | Bảng từ khóa | → giao cho [`03 Listing Creative`](../03_Listing_Creative_Agent/) |
| 1.9 | Định giá | → giao cho [`02 Product Strategy`](../02_Product_Strategy_Agent/) |
| 1.10 | Kế hoạch quảng bá | → giao cho [`06 Advertising`](../06_Advertising_Optimization_Agent/) |

> **Ranh giới của module này**: chỉ trả lời "**có làm không, làm ở mức giá và cấu hình nào**". Không trả lời "làm thành sản phẩm thế nào" (02), "viết thế nào" (03), "chạy quảng cáo thế nào" (06).

---

## 3. Workflow

```text
① Xuất dữ liệu ngành hàng (Shaduola / Seller Center / công cụ bên thứ ba)
              ▼
   ┌──────────────────────────────────────┐
   │ scripts/shaduola_parser.py           │  Chuẩn hóa định dạng: lọc ký hiệu
   │                                      │  tiền tệ/dấu nghìn/đơn vị 万/
   │                                      │  giá trị rỗng/ngày → JSON thống nhất
   └──────────────┬───────────────────────┘
                  ▼
   ┌──────────────────────────────────────┐
   │ scripts/market_metrics.py            │  Tính chỉ số (tất định, không LLM):
   │                                      │  quy mô / CR3·CR10·HHI / chia bin giá
   │                                      │  + dò vùng trũng / bảng chéo cấu hình
   └──────────────┬───────────────────────┘
                  ▼  metrics.md + metrics.json
        ┌─────────────────────────┐
        │ prompts/00_system.md    │  Vai trò + ngưỡng SOP + bảo vệ tuân thủ
        └───────────┬─────────────┘
                    ▼
        ┌─────────────────────────┐
        │ 01_category_precheck.md │  Step 1  Sàng lọc sơ bộ (làm được không)
        │                         │  → Không phù hợp thì **dừng ngay**, không phân tích tiếp
        └───────────┬─────────────┘
                    ▼
        ┌─────────────────────────┐
        │ 02_market_analysis.md   │  Step 2  Quy mô + mức độ tập trung + dải giá
        │                         │  Step 3  Tổ hợp cấu hình + đối thủ/đánh giá
        └───────────┬─────────────┘
                    ▼
        Đầu ra: gói trường dữ liệu bàn giao cho 02 Product Strategy
```

### Vì sao Step 1 phải "dừng" được

Nhận định cốt lõi của SOP 1.1 là:

> Nếu công ty không có chuỗi cung ứng, không có năng lực hậu mãi, không có lợi thế về giá, **thì dù thị trường tốt cũng chưa chắc nên làm**.

Vì vậy vai trò của sàng lọc sơ bộ là **lọc**, không phải "làm cho đủ thủ tục". Nếu một ngành hàng rủi ro cao (như dễ vỡ, cần chứng nhận, dễ khai khống thông số) không có lợi nhuận cao gánh đỡ, Prompt sẽ xuất thẳng 「không khuyến nghị sang bước tiếp theo」 thay vì tiếp tục tính quy mô và giá —— **tránh để các bước sau làm việc vô ích**.

---

## 4. Lớp script: cái gì tính được thì đừng để mô hình đoán

Đây là điểm khác biệt lớn nhất giữa module này và các "Prompt phân tích thị trường" khác.

| | Giao cho script | Giao cho Agent |
|---|---|---|
| Mức độ tập trung CR3/CR10/HHI | ✅ Tính tất định | — |
| Thống kê chia bin giá | ✅ | — |
| Dò vùng trũng (ranh giới dải giá) | ✅ Có lọc mức độ đáng kể | — |
| Bảng chéo cấu hình (thống kê bốn chiều) | ✅ | — |
| "Thị trường này có đáng vào không" | — | ✅ Nhận định |
| "Chọn dải giá nào" | — | ✅ Nhận định dựa trên chi phí và đối thủ |
| "Khuyến nghị tổ hợp cấu hình nào" | — | ✅ Nhận định dựa trên năng lực công ty |

**Căn cứ phân chia**: kết quả duy nhất (tính 100 lần vẫn như nhau) → script; cần cân nhắc đánh đổi (phụ thuộc nguồn lực công ty, chi phí, khẩu vị rủi ro) → Agent.

Chi tiết xem [`scripts/README.md`](./scripts/README.md).

### Chạy thử nhanh

```bash
cd scripts
python make_sample.py                                    # Tạo dữ liệu mẫu (dữ liệu tổng hợp)
python shaduola_parser.py ../samples/sample_patinete_eletrico.csv
python market_metrics.py ../samples/sample_patinete_eletrico.normalized.json \
    --bins 10 --config-fields "công suất,tải trọng"
```

Đầu ra là `metrics.md` (cho người đọc) và `metrics.json` (cho các bước sau sử dụng).

---

## 5. Cấu trúc file

| File | Tác dụng |
|---|---|
| [`scripts/shaduola_parser.py`](./scripts/shaduola_parser.py) | Chuẩn hóa định dạng: dữ liệu bẩn → JSON thống nhất |
| [`scripts/market_metrics.py`](./scripts/market_metrics.py) | Tính chỉ số: quy mô / mức độ tập trung / dải giá / bảng chéo cấu hình |
| [`scripts/make_sample.py`](./scripts/make_sample.py) | Tạo dữ liệu mẫu (có định dạng dữ liệu bẩn) |
| [`scripts/README.md`](./scripts/README.md) | Cách dùng script và giải thích thuật toán |
| [`prompts/00_system.md`](./prompts/00_system.md) | System Prompt: vai trò + ngưỡng SOP + bảo vệ tuân thủ |
| [`prompts/01_category_precheck.md`](./prompts/01_category_precheck.md) | Task Prompt: sàng lọc sơ bộ ngành hàng (1.1) |
| [`prompts/02_market_analysis.md`](./prompts/02_market_analysis.md) | Task Prompt: quy mô/mức độ tập trung/dải giá/cấu hình/đối thủ (1.2–1.6) |
| [`templates/input_category_research.md`](./templates/input_category_research.md) | Đầu vào chuẩn |
| [`templates/output_market_analysis.md`](./templates/output_market_analysis.md) | Đầu ra chuẩn |
| [`examples/patinete_eletrico_market.md`](./examples/patinete_eletrico_market.md) | Case study thực tế: ngành hàng xe trượt điện |
| [`samples/`](./samples/) | Dữ liệu mẫu và kết quả kỳ vọng |

---

## 6. Ngưỡng đánh giá do SOP đưa ra (có sẵn trong Prompt)

| Chiều | Ngưỡng | Nguồn |
|---|---|---|
| Mức độ tập trung thương hiệu | **< 50%** → hàng no-brand vẫn còn cơ hội; **> 50%** → thận trọng khi vào | SOP 1.3 |
| Mức độ tập trung người bán | Xem **CR10** (tỷ trọng lượng bán của 10 người bán đầu) | SOP 1.3 |
| Chọn dải giá | Tìm phân khúc **lượng bán cao + lượng bán trung bình cao + có lãi + đối thủ không mạnh**, không phải tìm đỉnh cao nhất | SOP 1.4 |
| Cách chia dải giá | Trục ngang là khoảng giá, trục dọc là lượng bán, chia **từ vùng trũng đến vùng trũng** | SOP 1.4 |
| Đánh giá cấu hình | Bốn chiều: tổng lượng bán / lượng bán trung bình / tỷ trọng số lượng / hiệu suất mỗi SKU | SOP 1.5 |
| Mẫu dữ liệu | **50** sản phẩm đầu; nếu sau vị trí 50 lượng bán không giảm đột ngột thì mở rộng lên **100** | SOP 1.4 |
| Ngành hàng rủi ro cao | **Ngành hàng rủi ro cao cần lợi nhuận cao mới gánh được** | SOP 1.1 |
| Hiệu quả sản phẩm mới | Sản phẩm mới có ra đơn được không là tín hiệu cốt lõi cho cơ hội của listing mới (⚠️ dữ liệu này của Shaduola không chính xác, cần đối chiếu thủ công) | SOP 1.2 |

---

## 7. Hạn chế đã biết

| Hạn chế | Giải thích |
|---|---|
| **Không thu thập dữ liệu** | Nguồn dữ liệu phải tự xuất. Bản V2 kết nối API thì có thể tự động hóa |
| **Không tính thuế phí** | Thuế phí ở Brazil phức tạp, không xử lý ở lớp chỉ số |
| **Độ chính xác của "lượng bán sản phẩm mới" có hạn** | Bản gốc SOP đã ghi chú "dữ liệu Shaduola không chính xác", script chỉ dùng `listing_age_days` để phân tầng sơ bộ, **bắt buộc đối chiếu thủ công** |
| **Trích xuất cấu hình mang tính heuristic** | Khi cấu hình chỉ nằm trong tiêu đề thì dựa vào regex để trích, tỷ lệ trích được có thể thấp (báo cáo sẽ ghi rõ số lỗi) |
| **HHI không có chuẩn ngành** | Script chỉ đưa giá trị gốc, việc đánh giá giao cho Agent |
| **Không ra quyết định chọn sản phẩm** | Chỉ xuất kết luận phân tích. **Quyết định cuối cùng bắt buộc do con người đưa ra** — liên quan đến nguồn lực công ty, chuỗi cung ứng và khẩu vị rủi ro, Agent không làm thay được |
| **Đánh giá của đối thủ chỉ ở mức sơ bộ** | Module này chỉ đánh giá sơ bộ "đối thủ bán được nhờ đâu"; quy nguyên nhân chuyên sâu giao cho [`07`](../07_Review_Analysis_Agent/) |

---

**Quay lại**: [Mục lục Agents](../README.md) · **Bước sau**: [02 Product Strategy](../02_Product_Strategy_Agent/) · **Tài liệu**: [Phân rã SOP](../../docs/00_Architecture_SOP_to_Agent.md) · [Checklist tự kiểm tra](../../docs/04_Result_Checklist.md)
