# 06 · Advertising Optimization Agent

**Agent tối ưu quảng cáo** · Nhập dữ liệu quảng cáo, xuất ra **danh sách hành động** — không phải "đề xuất tối ưu" chung chung, mà là "tắt từ khóa nào, đổi ảnh chính nào, chỉnh ROI về bao nhiêu".

> **Đóng gói thành Skill (v0.4)**: module này đã có entry để Agent gọi trực tiếp [`SKILL.md`](SKILL.md),
> và bổ sung script tính toán xác định [`scripts/ad_metrics.py`](scripts/ad_metrics.py)
> (`calc` tính ngưỡng hòa vốn/CPC chịu được, `diagnose` đọc CSV xuất từ quảng cáo và xuất hành động phân cấp P0/P1/P2,
> chỉ dùng thư viện chuẩn, hỗ trợ tên cột tiếng Trung/Việt/Anh/Bồ Đào Nha, có tính thuế phí Brazil).
> Quy tắc và cách tính xem bộ bốn tài liệu trong [`references/`](references/): [metrics](references/metrics.md) ·
> [diagnosis](references/diagnosis.md) · [playbooks](references/playbooks.md) · [actions](references/actions.md).
> **Skill này chỉ đề xuất, không thực thi** — ghi vào trang quản trị thuộc hướng B, chưa triển khai.

---

## I. Nó giải quyết vấn đề gì

SOP 3.5 nói vai trò của quảng cáo là "mua lượt hiển thị, test dữ liệu, giành thứ hạng, khuếch đại link". Nhưng khi chạy quảng cáo thực tế, lỗi người vận hành dễ mắc nhất là **thấy ROI kém là đi chỉnh ROI và ngân sách** — chỉnh ba vòng vẫn lỗ.

Lý do: **ROI kém là kết quả, không phải nguyên nhân.** Nguyên nhân thật nằm ở các khâu phía trước trong phễu. Việc module này làm là **đi ngược phễu để tìm ra gốc bệnh**.

| Nỗi đau | Biểu hiện | Module này giải quyết thế nào |
|---|---|---|
| **Không biết vấn đề nằm ở khâu nào** | ROI kém thì chỉnh ROI, càng chỉnh càng tệ | Chẩn đoán phễu bốn loại: hiển thị→click→thêm vào giỏ→chuyển đổi, xét từng khâu |
| **Không có đường chuẩn, toàn dựa vào cảm giác** | "CTR 1.4% hình như cũng ổn" | Bắt buộc đối chiếu đường chuẩn SOP (CTR 3–5% / chuyển đổi >1% / thêm vào giỏ >8%) |
| **Không biết nên chi bao nhiêu** | Ngân sách đặt tùy hứng, tiêu hết là dừng | Mô hình hai biến ngân sách tối đa × ROI mục tiêu + tính ROAS hòa vốn |
| **Quảng cáo không chạy là bó tay** | Không tiêu được tiền, chỉ biết tăng giá thầu | Cách gỡ bug của SOP: đổi ảnh chính trước, rồi mới tìm CSKH mở ticket |

**Đầu ra**: kết quả chẩn đoán phễu bốn loại + danh sách hành động theo từng nhóm quảng cáo + khoảng mục tiêu ngân sách/ROI + tính ngưỡng hòa vốn + phương án nhịp ngân sách.

---

## II. Các chương SOP được bao phủ

| SOP | Nội dung | Nằm ở Prompt nào |
|---|---|---|
| **3.5** | Logic nền của chạy quảng cáo: hai biến ngân sách tối đa × ROI mục tiêu | `02_budget_roi_model.md` |
| **3.5** | Khoảng test 7 ngày (sàn chính thức là 14 ngày) | `02_budget_roi_model.md` |
| **3.6** | Chẩn đoán phễu bốn loại + hướng tối ưu | `01_funnel_diagnosis.md` |
| **3.6** | Đường chuẩn chỉ số khỏe (CTR 3–5% / chuyển đổi >1% / thêm vào giỏ >8%) | `01_funnel_diagnosis.md` |
| **3.6** | Gỡ bug quảng cáo: đổi ảnh chính | `01_funnel_diagnosis.md` (mục riêng cuối file) |
| **3.6** | Cách bật/tắt quảng cáo: ngoài khung giờ vàng thì hạ ngân sách thay vì tạm dừng | `02_budget_roi_model.md` |
| **1.10** | Kế hoạch đẩy sản phẩm: xem đối thủ bao lâu thì lên đơn → suy ngược nhịp cho sản phẩm mới | `02_budget_roi_model.md` (mục tiêu theo giai đoạn) |

---

## III. Quy trình

```text
Đầu vào: bảng dữ liệu quảng cáo (hiển thị/click/thêm giỏ/đơn/chi phí) + cấu trúc chi phí
                         ▼
        ┌────────────────────────────────────┐
        │ 00_system.md                       │  Vai trò + đường chuẩn + thuật toán hòa vốn + tuân thủ
        └──────────────┬─────────────────────┘
                       ▼
        ┌────────────────────────────────────┐
        │ 01_funnel_diagnosis.md             │  Step 1  Xét phễu bốn loại cho từng nhóm QC
        │                                    │  Step 2  Xuất danh sách hành động (có ưu tiên)
        └──────────────┬─────────────────────┘
                       ▼
        ┌────────────────────────────────────┐
        │ 02_budget_roi_model.md             │  Step 3  Tính ROAS hòa vốn
        │                                    │  Step 4  Khoảng mục tiêu ngân sách × ROI
        │                                    │  Step 5  Nhịp ngân sách theo khung giờ
        └──────────────┬─────────────────────┘
                       ▼
        Đầu ra: output_ad_action_plan.md  →  thực thi hành động → sau 7 ngày thu dữ liệu để kiểm tra lại
```

**Đây là một module vòng khép kín (closed loop)**: sau khi thực thi hành động bắt buộc phải thu dữ liệu để kiểm tra lại, nếu không sẽ không biết hành động có hiệu quả hay không. Khoảng cách kiểm tra lại dùng **khoảng test 7 ngày** của SOP.

---

## IV. Chẩn đoán phễu bốn loại (cốt lõi)

SOP 3.6 chia vấn đề quảng cáo thành bốn loại. **Mỗi loại ứng với nguyên nhân khác nhau và hành động khác nhau** — đây là bảng phán đoán quan trọng nhất của module:

| Triệu chứng | Điều kiện xác định | Khâu chứa nguyên nhân | Ưu tiên kiểm tra | Hành động tối ưu |
|---|---|---|---|---|
| **Có hiển thị không có click** | CTR < 3% | Trước click (ảnh chính/tiêu đề) | Ảnh chính / tiêu đề / cách hiển thị giá / điểm bán hàng cốt lõi / có ưu đãi rõ ràng không | Đổi ảnh chính, tối ưu từ khóa trong tiêu đề, nhấn mạnh lợi thế giá, thêm điểm bán hàng vào ảnh chính, chỉnh từ khóa quảng cáo |
| **Có click không thêm vào giỏ** | CTR đạt và tỷ lệ thêm vào giỏ < 8% | Trang chi tiết | Trang chi tiết / cấu trúc SKU / giá / số lượng đánh giá / cam kết hậu mãi / mô tả rõ ràng | Tối ưu trang chi tiết, chỉnh SKU, thêm voucher, nhấn mạnh điểm bán hàng cốt lõi, bổ sung phản hồi thật của người mua |
| **Có thêm vào giỏ không chuyển đổi** | Tỷ lệ thêm vào giỏ đạt và tỷ lệ chuyển đổi < 1% | Khâu ra quyết định | Sức cạnh tranh về giá / mức voucher / chất lượng đánh giá / cam kết giao hàng / giá đối thủ / cam kết hậu mãi | Ưu đãi giới hạn thời gian, tối ưu hiển thị đánh giá, tối ưu thông tin giao hàng và bảo hành, chỉnh giá, tham gia chương trình |
| **Chi phí cao ROI thấp** | Cả ba chỉ số phễu đều đạt, nhưng ROAS < ngưỡng hòa vốn | Khâu chi phí (giá thầu/chất lượng từ khóa) | Từ khóa có quá rộng không / giá thầu quá cao / ảnh chính click kém hiệu quả / sản phẩm chuyển đổi yếu / giá không cạnh tranh | Giảm ngân sách cho từ khóa kém hiệu quả, tắt từ khóa không chuyển đổi, tối ưu ảnh chính và trang chi tiết, chỉnh giá và voucher, test lại khoảng ROI |

### Thứ tự xét rất quan trọng

**Bắt buộc xét theo thứ tự CTR → tỷ lệ thêm vào giỏ → tỷ lệ chuyển đổi → ROAS, không được bỏ bước.**

Lý do: nếu CTR không đạt nghĩa là người mua còn chưa bấm vào — lúc này xem tỷ lệ thêm vào giỏ chẳng có ý nghĩa gì, mẫu đã lệch ngay từ gốc.

```text
CTR không đạt → nguyên nhân ở trước click → sửa ảnh chính/tiêu đề, lúc này đừng động vào ROI và ngân sách
CTR đạt, thêm giỏ không đạt → nguyên nhân ở trang chi tiết → sửa trang chi tiết/SKU, lúc này đừng động vào ảnh chính
CTR và thêm giỏ đều đạt, chuyển đổi không đạt → nguyên nhân ở khâu ra quyết định → sửa giá/đánh giá/cam kết
Cả ba đều đạt nhưng ROAS kém → nguyên nhân ở khâu chi phí → lúc này mới tới lượt chỉnh giá thầu và ROI
```

> **Đây là kỷ luật cốt lõi nhất của module**: **chỉ khi các khâu phía trước đều đạt mới được phép động vào giá thầu.** Khâu phía trước chưa sửa xong mà đã chỉnh giá thầu thì chẳng khác gì trả thêm tiền mua traffic cho một link không chuyển đổi nổi.

---

## V. Đường chuẩn sức khỏe (SOP 3.6)

| Chỉ số | Chuẩn | Ý nghĩa khi thấp hơn chuẩn |
|---|---|---|
| CTR | **3–5%** | Ảnh chính/tiêu đề không hấp dẫn |
| Tỷ lệ chuyển đổi | Ổn định **trên 1%** | Khâu ra quyết định có lực cản |
| Tỷ lệ thêm vào giỏ | **> 8%** | Trang chi tiết thiếu sức thuyết phục |

⚠️ **Đường chuẩn là điểm neo để phán đoán, không phải mục tiêu.** SOP đưa ra "điểm đạt" — dùng để xác định "khâu nào không khỏe", chứ không phải "làm tới đây là đủ". Mục tiêu thật do **ngưỡng hòa vốn** quyết định (xem bên dưới).

---

## VI. Điều quan trọng hơn đường chuẩn: ROAS hòa vốn

Chỉ số phễu đạt hết **không có nghĩa là có lãi**. Đây là quan điểm cốt lõi thứ hai mà module này muốn nhấn mạnh.

### Cách tính ROAS hòa vốn

```
Lợi nhuận gộp khả dụng trước quảng cáo = Giá bán − Giá vốn − Vận chuyển chặng cuối − Phí kho − Hoa hồng sàn − Hao hụt hoàn hàng

ROAS hòa vốn = Giá bán ÷ Lợi nhuận gộp khả dụng trước quảng cáo
```

**ROAS < ngưỡng hòa vốn là mỗi đơn đều lỗ**, dù chỉ số phễu đẹp tới đâu.

### Ví dụ tính đầy đủ (tiếp nối ví dụ hàng nhỏ trong [`Templates/cost_pricing_template.md`](../../Templates/cost_pricing_template.md))

| Hạng mục | Số tiền |
|---|---|
| Giá bán | `R$ 113,40` |
| Giá vốn + vận chuyển chặng cuối + phí kho | `R$ 55,00` |
| Hoa hồng sàn (14%) | `R$ 15,88` |
| Hao hụt hoàn hàng (2%) | `R$ 2,27` |
| **Lợi nhuận gộp khả dụng trước quảng cáo** | **`R$ 40,26`** |

```
ROAS hòa vốn = 113,40 ÷ 40,26 = 2,82
```

### Biên lợi nhuận thực tế ở các mức ROAS khác nhau

| ROAS | Phí QC/đơn | Lợi nhuận gộp còn lại | % giá bán |
|---|---|---|---|
| 2,0 | R$ 56,70 | **−R$ 16,44** | **−14,5%** ❌ lỗ |
| 2,5 | R$ 45,36 | −R$ 5,10 | −4,5% ❌ lỗ |
| **2,82** | R$ 40,21 | R$ 0,04 | ~0% ⚠️ **hòa vốn** |
| 3,5 | R$ 32,40 | R$ 7,86 | 6,9% ✅ |
| 5,0 | R$ 22,68 | R$ 17,58 | 15,5% ✅ |
| 8,0 | R$ 14,18 | R$ 26,08 | 23,0% ✅ |
| 13,33 | R$ 8,50 | R$ 31,76 | 28,0% 🎯 đạt mục tiêu định giá |

### ⚠️ Một bảng bắt buộc phải nhìn rõ

Chi phí quảng cáo dự trù trong mô hình định giá là **7,5%** (SOP cho hàng nhỏ khoảng 5–10%), tương ứng `R$ 8,51/đơn`, tức **ROAS 13,33**.

**Trong khi ROAS khi chạy quảng cáo thực tế thường nằm trong khoảng 3–8.**

| So sánh | ROAS | Biên lợi nhuận gộp tương ứng |
|---|---|---|
| Giả định trong mô hình định giá | 13,33 | 28,0% |
| Khoảng thường gặp khi chạy thực tế | 3,5 – 8,0 | 6,9% – 23,0% |

> **Điều này nghĩa là: với sản phẩm hàng nhỏ chạy số lượng, quảng cáo thực tế sẽ ăn mất lợi nhuận gộp nhiều hơn đáng kể so với ngân sách dự trù lúc định giá.**
> Khoảng chênh này phải được nhìn rõ ngay **ở giai đoạn định giá** — chứ không phải đợi chạy quảng cáo rồi mới phát hiện.
> Hai hướng xử lý: ① khi định giá, dự trù chi phí quảng cáo **12–15%** thay vì 7,5%; ② chấp nhận biên lợi nhuận thấp, dựa vào việc tăng **tỷ trọng traffic tự nhiên** để nâng lợi nhuận tổng thể (quảng cáo chỉ làm lực đẩy khởi động lạnh).

---

## VII. Hai mẹo thực chiến từ SOP

### Mẹo 1 · Đừng tạm dừng quảng cáo thường xuyên

Nguyên văn SOP:

> Khi điều chỉnh quảng cáo Shopee đừng thường xuyên tạm dừng, sẽ lãng phí hạn mức miễn phí, cách tốt nhất là ngoài khung giờ vàng thì chỉnh về khoảng 10, tới khung giờ vàng lại chỉnh về ngân sách bình thường.

**Cách làm**: đổi "bật/tắt" thành "cao/thấp". Ngoài khung giờ vàng ép ngân sách về mức tối thiểu vẫn chạy được (như `R$ 10`), khung giờ vàng thì khôi phục ngân sách mục tiêu.

**Vì sao**: tạm dừng sẽ mất hạn mức traffic hỗ trợ link mới mà sàn cấp; còn hạ ngân sách chỉ giảm chi tiêu, không kích hoạt khoản mất này.

### Mẹo 2 · Quảng cáo không chạy thì đổi ảnh chính trước

Nguyên văn SOP:

> Khi quảng cáo bị tình trạng không chạy thì không chỉ đơn thuần chỉnh ROI và ngân sách, lúc này sửa nhẹ ảnh chính, tiêu đề, trang chi tiết, thường chỉ cần sửa ảnh chính là đủ, gỡ được bug của quảng cáo thì quảng cáo sẽ chạy lại, đây là cách gỡ bug…… thứ hai là tìm CSKH giải quyết, CSKH sẽ mở ticket để gỡ bug.

**Thứ tự hành động**: đổi ảnh chính → theo dõi 1–2 ngày → vẫn không chạy → tìm CSKH mở ticket.

> **Lưu ý**: mẹo này và "chẩn đoán phễu bốn loại" ở chương IV là quan hệ **bổ sung**, không phải thay thế:
> - **Chẩn đoán phễu** xử lý tình huống thông thường (dữ liệu phản ánh được nguyên nhân)
> - **Đổi ảnh chính để gỡ bug** xử lý tình huống bất thường (bản thân dữ liệu không chạy ra, không đủ mẫu để xác định nguyên nhân)
>
> Căn cứ phán đoán: **có lượt hiển thị hay không.** Có hiển thị → đi chẩn đoán phễu; không tiêu được tiền, không có hiển thị → đi quy trình gỡ bug.

---

## VIII. File Prompt

| File | Vai trò |
|---|---|
| [`prompts/00_system.md`](./prompts/00_system.md) | System Prompt: vai trò + đường chuẩn + thuật toán hòa vốn + quy tắc ngôn ngữ + chốt chặn tuân thủ |
| [`prompts/01_funnel_diagnosis.md`](./prompts/01_funnel_diagnosis.md) | Task Prompt: xét phễu bốn loại cho từng nhóm quảng cáo + danh sách hành động |
| [`prompts/02_budget_roi_model.md`](./prompts/02_budget_roi_model.md) | Task Prompt: tính ngưỡng hòa vốn + khoảng mục tiêu ngân sách/ROI + nhịp ngân sách theo khung giờ |

## IX. Template và case study

| File | Giải thích |
|---|---|
| [`templates/input_ad_data.md`](./templates/input_ad_data.md) | Đầu vào chuẩn: bảng dữ liệu quảng cáo + cấu trúc chi phí |
| [`templates/output_ad_action_plan.md`](./templates/output_ad_action_plan.md) | Đầu ra chuẩn: danh sách hành động |
| [`examples/powerbank_20000mah_ads.md`](./examples/powerbank_20000mah_ads.md) | Case study thật: sạc dự phòng với 4 nhóm quảng cáo, đủ cả bốn loại triệu chứng, ROAS tổng 1,84 đang lỗ |

---

## X. Phạm vi và giới hạn

| Hạng mục | Giải thích |
|---|---|
| ✅ Phụ trách | Chẩn đoán phễu, danh sách hành động, tính ngưỡng hòa vốn, mục tiêu ngân sách và ROI, nhịp ngân sách, phương án kiểm tra lại |
| ❌ Không phụ trách | Thực sự sửa giá sửa ảnh (giao cho 03/04), thao tác trên trang quản trị của sàn, thuật toán đấu thầu thời gian thực |
| ⚠️ Phụ thuộc dữ liệu | **Bắt buộc có dữ liệu quảng cáo thật**. Dữ liệu kiểu "một tuần 100 lượt hiển thị" không có giá trị chẩn đoán, Agent sẽ từ chối phân tích |
| ⚠️ Cỡ mẫu | Khi một nhóm quảng cáo có < 5 đơn, chẩn đoán chỉ mang tính tham khảo — mẫu quá nhỏ, dao động chỉ số lớn hơn tín hiệu |
| ⚠️ Phí | Tỷ lệ hoa hồng, chi phí vận chuyển phải điền theo giá trị thực tế, nếu không ngưỡng hòa vốn sẽ tính sai |
| ⚠️ Khác biệt giữa các sàn | Định nghĩa chỉ số trên trang quản trị quảng cáo của mỗi sàn khác nhau (như cách tính "thêm vào giỏ"), **trước khi điền dữ liệu hãy xác nhận cách tính thống nhất** |

---

**Quay lại**: [Danh mục Agents](../README.md) · **Thượng nguồn**: [03 Listing Creative](../03_Listing_Creative_Agent/) · [04 Product Image](../04_Product_Image_Agent/) · **Hạ nguồn**: [07 Review Analysis](../07_Review_Analysis_Agent/) · **Tài liệu**: [Checklist tự kiểm tra](../../docs/04_Result_Checklist.md)
