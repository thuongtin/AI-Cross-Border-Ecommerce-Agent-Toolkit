# Agents · Mục lục module

7 module Agent, cấu trúc thống nhất:

```text
<NN>_<Name>_Agent/
├── README.md        # Giải quyết vấn đề gì / đầu vào đầu ra / cách dùng / giới hạn đã biết
├── prompts/         # System Prompt + Task Prompt
├── templates/       # Template đầu vào chuẩn + template đầu ra chuẩn
└── examples/        # Bản ghi chạy trọn vẹn trên sản phẩm thật
```

---

## Đã hoàn thành

### v0.1 · Cụm sáng tạo

| Mã số | Module | Trách nhiệm | Phụ thuộc | Thư mục |
|---|---|---|---|---|
| **03** | **Listing Creative Agent** | Phân loại từ khóa → tiêu đề → trang chi tiết → điểm bán hàng/thông số → tự kiểm tra tuân thủ | Không (module đầu vào) | [→](./03_Listing_Creative_Agent/) |
| **04** | **Product Image Agent** | Lên kế hoạch nội dung 9 ảnh + Prompt tạo ảnh cho từng ảnh + kiểm tra tuân thủ ảnh | **03** (cần `core_selling_point`) | [→](./04_Product_Image_Agent/) |
| **05** | **Product Video Agent** | Kịch bản 15s/30s → storyboard → Prompt video AI → lồng tiếng & phụ đề | **03** (cần `core_selling_point`) | [→](./05_Product_Video_Agent/) |

### v0.2 · Cụm vận hành

| Mã số | Module | Trách nhiệm | Phụ thuộc | Thư mục |
|---|---|---|---|---|
| **06** | **Advertising Optimization Agent** | Chẩn đoán phễu 4 loại (lượt hiển thị→click→thêm vào giỏ→chuyển đổi) + tính ngưỡng hòa vốn + mô hình ngân sách/ROI | Dữ liệu quảng cáo + cấu trúc chi phí | [→](./06_Advertising_Optimization_Agent/) |
| **07** | **Review Analysis Agent** | Phân loại đánh giá tích cực/tiêu cực → quy nguyên nhân theo 8 nhóm → nhận diện loại hiểu lầm → đề xuất vá trang chi tiết | Dữ liệu đánh giá + `spec_table` | [→](./07_Review_Analysis_Agent/) |

### v0.3 · Cụm phân tích (chuỗi tiền đề)

| Mã số | Module | Trách nhiệm | Phụ thuộc | Thư mục |
|---|---|---|---|---|
| **01** | **Market Research Agent** | Đánh giá sơ bộ ngành hàng / quy mô thị trường / mức độ tập trung / dải giá (kèm phát hiện vùng trũng) / tổ hợp cấu hình · **kèm script phân tích dữ liệu và tính chỉ số** | Dữ liệu xuất ngành hàng + nguồn lực công ty + cấu trúc chi phí | [→](./01_Market_Research_Agent/) |
| **02** | **Product Strategy Agent** | Định vị sản phẩm / cấu hình cốt lõi / chốt điểm bán hàng chủ lực / né rủi ro / mô hình định giá / cấu trúc 4 vai trò SKU | **01** + `decision_approved` | [→](./02_Product_Strategy_Agent/) |

✅ **Cả 7 module đã hoàn thành.**

---

## Giải thích cách đánh số

Kế hoạch ban đầu là `01` Thị trường → `02` Chiến lược sản phẩm → `03` Listing → `04` Quảng cáo → `05` Đánh giá → `06` Video.
Bản v0.1 đã sắp xếp lại theo **cụm công việc** thành `03-04-05` (cụm sáng tạo: copy→ảnh→video) và `06-07` (cụm vận hành: quảng cáo→đánh giá), để các module vốn nối tiếp nhau có mã số liền mạch. Lịch sử thay đổi xem tại [CHANGELOG.md](../CHANGELOG.md) ở thư mục gốc.

---

## Hợp đồng bàn giao

```text
01 Market Research ──► 02 Product Strategy ──► 03 Listing Creative
(có làm không, giá nào)  (làm thành ra sao)      (thể hiện thế nào)
                                                    │
                              ┌─────────────────────┼─────────────────────┐
                              ▼                     ▼                     ▼
                     04 Product Image      05 Product Video        Đăng bán → vận hành trên sàn
                                                                        │
                                          ┌─────────────────────────────┴──────────┐
                                          ▼                                        ▼
                                 06 Advertising                           07 Review Analysis
                                 (dữ liệu quảng cáo)                      (dữ liệu đánh giá)
                                          │                                        │
                                          └────────► Quay về 03/04 (iterate) ◄─────┘
                                                             │
                                                             ▼
                                                 Kiểm tra lại → đạt thì scale / chưa đạt thì chẩn đoán lại
```

### Hợp đồng xuôi chiều

| Thượng nguồn | Bắt buộc cung cấp | Hạ nguồn | Hành vi khi thiếu |
|---|---|---|---|
| 01 | `target_price_range` / `recommended_config` / `opportunity_config` / `cost_floor_price` | 02 | 02 không thể định giá và chốt cấu hình → báo lỗi |
| 02 | `core_selling_point` (duy nhất) / `secondary_points` / `forbidden_words_seed` / `after_sales_commitment` | 03 | 03 không thể chốt điểm bán hàng → báo lỗi |
| 02 | `breakeven_roas_by_sku` | 06 | 06 không thể đánh giá quảng cáo có lãi hay không → từ chối xuất kết luận ROI |
| 03 | `core_selling_point` / `spec_table` / `forbidden_words` / `title_final` | 04 / 05 | **Chặn lại**, 04/05 không được bắt đầu |

### Hợp đồng quay vòng về (06 / 07 → 03 / 04)

| Thượng nguồn | Trường đầu ra | Đích quay về | Ràng buộc |
|---|---|---|---|
| **06** | `symptom_by_group` / `ctr_fail_groups` / `atc_fail_groups` / `cvr_fail_groups` / `breakeven_roas` | 03 (iterate), 04 (iterate) | **Chỉ sửa khâu mà triệu chứng chỉ tới**, phần còn lại giữ nguyên |
| **07** | `review_patch_suggestions` / `forbidden_words_candidates` / `selling_points_ranked` / `packaging_clarity_needed` | 03 (iterate), 04 (iterate) | Copy vá lỗi phải viết bằng **tiếng mẹ đẻ của thị trường mục tiêu** và dán thẳng được |

**Kỷ luật vòng khép kín** (các module bên trên đã nhấn mạnh nhiều lần):
1. Mỗi lần chỉ sửa một **nguyên nhân gốc** (các hành động cùng chỉ về một nguyên nhân gốc có thể làm chung một đợt)
2. Khâu không thuộc triệu chứng **không được đụng tới**
3. Chưa đạt thì **không tăng liều cùng một hành động**, quay lại chẩn đoán để xác định lại

Demo vòng khép kín đầy đủ xem tại [`../Examples/03_Closed_Loop/`](../Examples/03_Closed_Loop/). Chuỗi tiền đề đầy đủ xem [`01`](./01_Market_Research_Agent/examples/patinete_eletrico_market.md) → [`02`](./02_Product_Strategy_Agent/examples/patinete_eletrico_strategy.md) → [`03`](./03_Listing_Creative_Agent/examples/powerbank_20000mah.md).

---

**Tài liệu**: [Tách SOP→Agent](../docs/00_Architecture_SOP_to_Agent.md) · [Chuẩn Prompt](../docs/01_Prompt_Design_Guide.md) · [Quy chuẩn trường theo sàn](../docs/02_Platform_Output_Spec.md) · [Lằn ranh đỏ tuân thủ](../docs/03_Compliance_Guard.md) · [Checklist tự kiểm tra](../docs/04_Result_Checklist.md)
