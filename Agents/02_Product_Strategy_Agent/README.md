# 02 · Product Strategy Agent

**Agent chiến lược sản phẩm** · Chuyển kết luận phân tích thị trường thành **bảng thông số sản phẩm có thể giao thẳng cho bộ phận thu mua, đăng bán, thiết kế ảnh và định giá**.

> **Skill hóa (v0.4)**: bổ sung script tính toán định giá và entry point cho Agent [`SKILL.md`](SKILL.md).
>
> ```bash
> # Một SKU: biên lợi nhuận ròng / giá hòa vốn / giá mục tiêu / dư địa voucher
> python scripts/sku_pricing.py calc --cost 935 --price 2199 --commission 14 --ad 5
> # Ma trận nhiều SKU: bảng biên lợi nhuận ròng + bậc giá + cảnh báo cấu trúc
> python scripts/sku_pricing.py matrix --file examples/sample-skus.csv --target-margin 32
> ```
>
> Công thức và cách tính thuế xem tại [`references/pricing-rules.md`](references/pricing-rules.md). **Có tính các khoản thuế Brazil.**

---

## 1. Module này giải quyết vấn đề gì

SOP 1.7 định vị bước này như sau:

> Bước này là đầu ra cuối cùng của phân tích thị trường, **không phải chỉ tóm tắt lại**, mà phải hình thành **yêu cầu sản phẩm** đủ để chỉ đạo thu mua, đăng bán, làm ảnh, định giá và quảng bá.

Đây chính là chỗ dễ "đứt gánh" nhất khi triển khai: phân tích thị trường làm rất kỹ, nhưng đến lúc chốt "làm sản phẩm gì" lại chỉ còn một câu mơ hồ.

| Vấn đề | Biểu hiện | Module này giải quyết thế nào |
|---|---|---|
| **Kết luận không triển khai được** | "Nên làm mẫu 500W" —— thu mua không biết cần thông số gì | Xuất đủ sáu hạng mục yêu cầu: loại sản phẩm / cấu hình / giá / SKU / điểm bán hàng / rủi ro |
| **Định giá cảm tính** | Nhìn giá đối thủ rồi trừ đi một chút | Dùng công thức định giá để tính ngược + kiểm tra biên lợi nhuận từng SKU + tính ngưỡng hòa vốn |
| **Thêm SKU tùy hứng** | Nghĩ ra gì thêm nấy | Thiết kế theo bốn vai trò «kéo traffic / chủ lực / cấu hình cao / combo», mỗi bậc có nhiệm vụ rõ ràng |
| **Điểm bán hàng không hội tụ** | Mười điểm bán hàng ngang hàng nhau, tức là không có điểm nào | Hội tụ từ `opportunity_config` của phân tích thị trường thành một câu điểm bán hàng chính |

**Sản phẩm đầu ra**: «Bảng yêu cầu sản phẩm» —— loại sản phẩm đề xuất / cấu hình cốt lõi / cấu trúc SKU / khoảng giá / điểm bán hàng chủ lực / phòng tránh rủi ro / yêu cầu triển khai tiếp theo.

---

## 2. Các chương SOP được bao phủ

| SOP | Nội dung | Nằm ở đâu |
|---|---|---|
| **1.7** | Chốt sản phẩm chủ lực: loại sản phẩm / cấu hình cốt lõi / giá mục tiêu / điểm bán hàng cốt lõi / phòng tránh rủi ro / yêu cầu triển khai tiếp theo | `prompts/01_product_decision.md` |
| **1.9** | Định giá: hàng cồng kềnh 30–35%, hàng nhỏ 25–30%, giai đoạn đầu có thể thấp hơn một chút để nuôi trọng số | `prompts/02_pricing_and_sku.md` |
| **3.1** | Chuẩn bị trước khi đăng bán từng sản phẩm (8 câu hỏi bắt buộc) | `prompts/01_product_decision.md` |
| **3.2** | Chiến lược định giá và SKU (cấu trúc bốn vai trò) | `prompts/02_pricing_and_sku.md` |

---

## 3. Luồng làm việc

```text
Đầu vào: đầu ra của 01 Market Research (target_price_range / recommended_config /
      opportunity_config / cost_structure / competitor_weakness)
                         ▼
        ┌────────────────────────────────┐
        │ prompts/00_system.md           │  Vai trò + quy tắc định giá + chốt chặn tuân thủ
        └──────────────┬─────────────────┘
                       ▼
        ┌────────────────────────────────┐
        │ 01_product_decision.md         │  Step 1  Định vị loại sản phẩm
        │                                │  Step 2  Chốt cấu hình cốt lõi
        │                                │  Step 3  Hội tụ điểm bán hàng chủ lực (một câu)
        │                                │  Step 4  Danh sách phòng tránh rủi ro
        │                                │  Step 5  Tự kiểm tra 8 câu trước khi đăng bán
        └──────────────┬─────────────────┘
                       ▼
        ┌────────────────────────────────┐
        │ 02_pricing_and_sku.md          │  Step 6  Mô hình định giá + kiểm tra từng SKU
        │                                │  Step 7  Cấu trúc SKU bốn vai trò
        │                                │  Step 8  ROAS hòa vốn (giao cho 06)
        └──────────────┬─────────────────┘
                       ▼
        Đầu ra: «Bảng yêu cầu sản phẩm» → giao cho 03 Listing / 04 Image / 05 Video / 06 Advertising
```

---

## 4. Quy tắc cốt lõi (SOP)

### Định giá

| Hạng mục | Quy tắc |
|---|---|
| Biên lợi nhuận mục tiêu · hàng cồng kềnh | **30–35%** |
| Biên lợi nhuận mục tiêu · hàng nhỏ | **25–30%** |
| Tỷ trọng chi phí quảng cáo | Hàng cồng kềnh ~**5%** / hàng nhỏ **5–10%** |
| Hao hụt do hoàn hàng | **2%** |
| Nhịp độ | **Giai đoạn đầu có thể hạ nhẹ biên lợi nhuận để nuôi trọng số, khi trọng số lên rồi thì nâng lại** |

**Công thức giá bán** (suy luận đầy đủ xem [`Templates/cost_pricing_template.md`](../../Templates/cost_pricing_template.md)):

```
P = (giá vốn sản phẩm + vận chuyển chặng cuối + phí lưu kho) ÷ (1 − % hoa hồng − % quảng cáo − % hoàn hàng − % biên lợi nhuận mục tiêu)
```

### Cấu trúc SKU (SOP 3.2)

**Nhận định cốt lõi**: SOP nói rõ —— **SKU không phải thêm tùy tiện, mà là để người mua có sự so sánh.**

| Vai trò SKU | Tác dụng | Định vị biên lợi nhuận |
|---|---|---|
| **SKU kéo traffic giá thấp** | Tăng hiệu quả quảng cáo, tăng CTR | Mỏng nhất (có thể thấp hơn mục tiêu 5–8 điểm %) |
| **SKU chủ lực** | Chịu trách nhiệm chốt đơn | Biên lợi nhuận mục tiêu |
| **SKU cấu hình cao** | Tăng giá trị đơn hàng trung bình (AOV) | Cao hơn |
| **SKU combo** | **Tăng lợi nhuận** | Cao nhất |
| (Phối hợp) voucher | **Thu hẹp chênh lệch giá** | — |

### 8 câu hỏi trước khi đăng bán (SOP 3.1)

Phải trả lời rõ trước khi đăng bán, thiếu một câu là coi như chưa sẵn sàng:

1. Sản phẩm này bán cho ai
2. Điểm bán hàng cốt lõi là gì
3. Đối thủ chính là ai
4. Giá đánh vào khoảng nào
5. SKU chủ lực là SKU nào
6. Lợi nhuận tối thiểu là bao nhiêu
7. Có phù hợp để test quảng cáo không
8. Rủi ro hậu mãi có thể gặp là gì

---

## 5. Cấu trúc file

| File | Vai trò |
|---|---|
| [`prompts/00_system.md`](./prompts/00_system.md) | System Prompt: vai trò + quy tắc định giá và SKU + chốt chặn tuân thủ |
| [`prompts/01_product_decision.md`](./prompts/01_product_decision.md) | Task Prompt: định vị sản phẩm / cấu hình / hội tụ điểm bán hàng / phòng tránh rủi ro / 8 câu trước khi đăng bán |
| [`prompts/02_pricing_and_sku.md`](./prompts/02_pricing_and_sku.md) | Task Prompt: mô hình định giá + SKU bốn vai trò + ngưỡng hòa vốn |
| [`templates/input_strategy_brief.md`](./templates/input_strategy_brief.md) | Đầu vào chuẩn |
| [`templates/output_product_requirement.md`](./templates/output_product_requirement.md) | Đầu ra chuẩn: «Bảng yêu cầu sản phẩm» |
| [`examples/patinete_eletrico_strategy.md`](./examples/patinete_eletrico_strategy.md) | Case study thực tế: xe scooter điện (nối tiếp đầu ra của 01) |

---

## 6. Một đánh đổi thiết kế quan trọng

**Module này không ra "quyết định chọn sản phẩm", chỉ làm "chuẩn hóa thông số cho sản phẩm đã được quyết định".**

Khác nhau ở đâu:

| | Quyết định chọn sản phẩm (người làm) | Chuẩn hóa thông số (module này làm) |
|---|---|---|
| Câu hỏi | "Có nên làm sản phẩm này không" | "Nếu làm thì làm thành như thế nào" |
| Phụ thuộc | Chiến lược công ty, vốn, khẩu vị rủi ro, đàm phán chuỗi cung ứng | Dữ liệu thị trường + cấu trúc chi phí |
| Kiểm chứng được không | Không (phải chờ vài tháng mới có kết quả) | Được (cấu hình có đúng không, giá có ra lợi nhuận không) |

Vì vậy trong đầu vào của module này, **trường `decision_approved` là bắt buộc** —— cần người xác nhận rõ "sản phẩm này đã quyết định làm" thì Agent mới bắt đầu chuẩn hóa thông số. **Agent sẽ không thay bạn nói "nên làm sản phẩm này".**

---

## 7. Giới hạn đã biết

| Giới hạn | Giải thích |
|---|---|
| **Không ra quyết định chọn sản phẩm** | Cần người xác nhận `decision_approved` |
| **Không thẩm định giá nhập** | Cấu trúc chi phí do người điền, Agent không thể kiểm chứng giá thu mua thật hay giả |
| **Không tính thuế** | Cấu trúc thuế Brazil phức tạp, cần tự đưa vào cấu trúc chi phí |
| **Không bao gồm quy tắc chương trình khuyến mãi của sàn** | Liên động giá khuyến mãi và tồn kho (chương trình Shopee đã đăng ký thì không rút ra được) thuộc phạm vi vận hành, module này chỉ đưa ra đề xuất giá |
| **Hội tụ điểm bán hàng phụ thuộc upstream** | Nếu chưa chạy 01, thiếu `opportunity_config` → chỉ đưa ra được điểm bán hàng chung chung, chất lượng khác biệt hóa giảm |
| **Mức hạ giá nuôi trọng số giai đoạn đầu cần người quyết** | SOP nói "giai đoạn đầu có thể thấp hơn một chút", hạ bao nhiêu điểm tùy dòng tiền và tồn kho, Agent chỉ đưa ra khoảng |

---

**Quay lại**: [Mục lục Agents](../README.md) · **Upstream**: [01 Market Research](../01_Market_Research_Agent/) · **Downstream**: [03 Listing](../03_Listing_Creative_Agent/) · [06 Advertising](../06_Advertising_Optimization_Agent/) · **Tài liệu**: [Mô hình định giá](../../Templates/cost_pricing_template.md)
