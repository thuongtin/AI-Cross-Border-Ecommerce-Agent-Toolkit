# TASK · Mô hình định giá và cấu trúc SKU

> Dùng kèm: `00_system.md` + đầu ra của `01_product_decision.md`
> Tương ứng SOP **1.9 Định giá** + **3.2 Chiến lược định giá và SKU**

---

# INPUT

| Trường | Giải thích | Ảnh hưởng khi thiếu |
|---|---|---|
| `decision_approved` | **Mục chặn** | Chưa xác nhận thì dừng |
| `cost_structure` | Cấu trúc chi phí (gồm chênh lệch giá vốn giữa các SKU) | **Chặn**——không định giá được |
| `target_price_range` | Phân tích dải giá của 01 | Không có điểm neo thị trường |
| `main_price_zone` | Mức giá chủ lực của 01 | Không chốt được giá SKU chủ lực |
| `cost_floor_price` | Giá khả thi theo giá vốn do 01 tính ngược (nếu có) | Không kiểm chứng chéo được |
| `target_margin_rate` | Biên lợi nhuận mục tiêu (hàng cồng kềnh 30–35% / hàng nhỏ 25–30%) | Không tính ngược được |
| `final_config` | Đầu ra của 01_product_decision | Không thiết kế được khác biệt giữa các SKU |
| `competitor_price_points[]` | Mức giá của đối thủ (tùy chọn) | Không neo giá được |
| `cash_flow_constraint` | Ràng buộc dòng tiền (tùy chọn) | Không đánh giá được có nuôi trọng số lâu dài được không |
| `inventory_level` | Mức tồn kho | Không đánh giá được rủi ro tồn kho khi chạy chương trình |

---

# STEP 1 · Cấu trúc chi phí từng SKU

**Cấu hình khác nhau thì giá vốn khác nhau, bắt buộc liệt kê từng SKU.** Dùng một giá vốn để tính cho mọi SKU là lỗi phổ biến nhất.

```markdown
## 1. Cấu trúc chi phí

| SKU | Giá vốn sản phẩm | Vận chuyển chặng cuối | Phí lưu kho | Tổng giá vốn | Giải thích |
|---|---|---|---|---|---|
| SKU kéo traffic | | | | | |
| SKU chủ lực | | | | | |
| SKU cấu hình cao | | | | | |
| SKU combo | | | | | |

**Giả định về mức phí**

| Hạng mục | Giá trị | Nguồn |
|---|---|---|
| % hoa hồng sàn | | Tra theo ngành hàng thực tế |
| % quảng cáo | | Hàng cồng kềnh ~5% / hàng nhỏ 5–10% (SOP) |
| % hao hụt hoàn hàng | | 2% (SOP) |
| **% biên lợi nhuận mục tiêu** | | Hàng cồng kềnh 30–35% / hàng nhỏ 25–30% (SOP) |
| Thuế | | ⚠️ Thuế Brazil cần tự tính vào; nếu chưa tính phải ghi chú trong báo cáo |
```

---

# STEP 2 · Công thức định giá và tính ngược

```markdown
## 2. Tính giá

### 2.1 Công thức giá bán

    Giá bán mục tiêu = (giá vốn sản phẩm + vận chuyển chặng cuối + phí lưu kho) ÷ (1 − % hoa hồng − % quảng cáo − % hoàn hàng − % biên lợi nhuận mục tiêu)

**Lấy SKU chủ lực làm ví dụ (bắt buộc trình bày đầy đủ bước thay số)**:

    Tử số = <giá vốn> + <vận chuyển> + <lưu kho> = <tổng>
    Mẫu số = 1 − <% hoa hồng> − <% quảng cáo> − <% hoàn hàng> − <% biên lợi nhuận mục tiêu> = <giá trị>

    Giá bán mục tiêu = <tử số> ÷ <mẫu số> = R$ <kết quả>

### 2.2 Kết quả tính ngược từng SKU

| SKU | Tổng giá vốn | Mẫu số | **Giá bán mục tiêu tính ngược** | Điểm neo thị trường | Chênh lệch |
|---|---|---|---|---|---|
| SKU kéo traffic | | | | | |
| SKU chủ lực | | | | | |
| SKU cấu hình cao | | | | | |
| SKU combo | | | | | |
```

### 2.3 Kiểm chứng chéo then chốt (bắt buộc)

```markdown
### 2.3 Kiểm chứng chéo với phân tích thị trường

| Hạng mục | Giá trị |
|---|---|
| **Giá khả thi theo giá vốn** do phân tích thị trường đề xuất (01 tính ngược) | |
| Giá bán mục tiêu tính ngược ở bước này | |
| Chênh lệch | |

**Kết luận**: <khớp / có chênh lệch, chênh lệch có nghĩa là gì>
```

**Vì sao bước này bắt buộc**:

| Tình huống | Ý nghĩa | Cách xử lý |
|---|---|---|
| Hai giá trị gần nhau | ✅ Dải tối ưu của cấu trúc thị trường khớp với vùng khả thi theo giá vốn | Định giá theo kế hoạch |
| Dải tối ưu của thị trường **thấp hơn** giá khả thi theo giá vốn | ⚠️ Phân khúc giá dễ bán lại không ra lợi nhuận | Bắt buộc giảm giá vốn, đổi cấu hình, hoặc bỏ mức giá đó |
| Dải tối ưu của thị trường **cao hơn** giá khả thi theo giá vốn | ✅ Có dư địa lợi nhuận gộp | Phần dư dùng cho voucher/chương trình khuyến mãi |

---

# STEP 3 · Chốt giá và kiểm tra biên lợi nhuận

```markdown
## 3. Phương án giá và kiểm tra

| SKU | Giá bán | LN gộp khả dụng trước QC | Tỷ trọng | LN sau QC | Biên LN ròng | Đạt (≥ mục tiêu) | ROAS hòa vốn |
|---|---|---|---|---|---|---|---|
| SKU kéo traffic | | | | | | | |
| SKU chủ lực | | | | | | | |
| SKU cấu hình cao | | | | | | | |
| SKU combo | | | | | | | |

**Công thức kiểm tra (mỗi dòng đều phải kiểm lại được)**

    LN gộp khả dụng trước QC = giá bán − tổng giá vốn − giá bán×% hoa hồng − giá bán×% hoàn hàng
    LN sau QC                = LN gộp khả dụng trước QC − giá bán×% quảng cáo
    Biên LN ròng             = LN sau QC ÷ giá bán
    ROAS hòa vốn             = giá bán ÷ LN gộp khả dụng trước QC
```

### 3.1 Phân tích dư địa lợi nhuận

```markdown
### 3.1 Dư địa lợi nhuận

| SKU | Biên LN ròng thực tế | Biên LN mục tiêu | Dư địa | Mức voucher dư địa gánh được |
|---|---|---|---|---|
| SKU chủ lực | | 32% | | R$ <n> |

**Ý nghĩa**: SKU có dư địa > 0 mới đủ sức phát voucher; SKU có dư địa ≤ 0 phát voucher là lỗ.
```

> **Cách dùng dư địa**: SOP nói tác dụng của voucher là "**thu hẹp chênh lệch giá**".
> Vì vậy dư địa nên ưu tiên dùng cho **SKU chủ lực hoặc SKU cấu hình cao** (kéo giá chốt thực tế của chúng lại gần SKU kéo traffic), chứ không phát voucher cho SKU kéo traffic (biên lợi nhuận của nó mỏng nhất).

### 3.2 Xử lý đặc biệt cho SKU kéo traffic

```markdown
### 3.2 Giải thích vai trò chiến lược của SKU kéo traffic

| Hạng mục | Giá trị |
|---|---|
| Giá SKU kéo traffic | |
| Biên LN mục tiêu | |
| Biên LN ròng thực tế | |
| ROAS hòa vốn | |
| **Có nằm trên ngưỡng hòa vốn không** | ✅ / ⚠️ |
| **Ghi chú vai trò chiến lược** | |
```

⚠️ **Nếu SKU kéo traffic thấp hơn ngưỡng hòa vốn (lỗ mỗi đơn)**: bắt buộc ghi rõ vai trò chiến lược và khối lượng chịu được:

```
[SKU kéo traffic lỗ chiến lược]
- Lỗ mỗi đơn R$ <n>
- Mục đích: <kéo click / tăng hiệu quả quảng cáo / có đơn đầu tiên>
- Khối lượng chịu được: <tối đa n đơn mỗi tháng, hoặc ≤ n% tổng lượng>
- Điều kiện thoát: <sau khi SKU chủ lực đạt n đơn/tháng thì gỡ xuống hoặc tăng giá>
```

**Không được phép** đưa ra đề xuất giá dưới giá vốn khi chưa có ghi chú này.

---

# STEP 4 · Thiết kế cấu trúc SKU bốn vai trò

```markdown
## 4. Cấu trúc SKU

| Vai trò | Nội dung | Khác biệt cấu hình | Giá bán | Biên LN ròng | Nhiệm vụ |
|---|---|---|---|---|---|
| **Kéo traffic giá thấp** | | Cấu hình thấp | | | Kéo click, tăng hiệu quả quảng cáo |
| **Chủ lực** | | **Cấu hình khác biệt hóa** | | | **Chịu trách nhiệm chốt đơn** |
| **Cấu hình cao** | | Cấu hình cao | | | Tăng AOV |
| **Combo** | | Máy chính + phụ kiện | | | **Tăng lợi nhuận** |

### 4.1 Kiểm tra bậc giá

| Hai bậc liền kề | Chênh giá | Biên độ chênh | Có hợp lý không |
|---|---|---|---|
| Kéo traffic → chủ lực | | | Chênh không nên quá lớn (nếu không người mua sẽ không nâng cấp) |
| Chủ lực → cấu hình cao | | | |
| Chủ lực → combo | | | |

⚠️ **Vấn đề khi chênh giá quá lớn**: nếu SKU kéo traffic và SKU chủ lực chênh hơn 40%, người mua sẽ dừng ở SKU kéo traffic, SKU chủ lực không có đơn.
⚠️ **Vấn đề khi chênh giá quá nhỏ**: nếu chỉ chênh 5%, người mua sẽ chọn hết bản cấu hình cao, SKU kéo traffic mất ý nghĩa.

### 4.2 Thiết kế voucher (SOP: thu hẹp chênh lệch giá)

| Voucher | SKU áp dụng | Mệnh giá | Giá sau voucher | Chênh lệch được thu hẹp | Nguồn chi phí |
|---|---|---|---|---|---|
| | SKU chủ lực | | | Kéo traffic ↔ chủ lực từ R$ <a> xuống R$ <b> | Dư địa lợi nhuận của SKU chủ lực R$ <n> |

**Kiểm tra**: giá sau voucher vẫn phải nằm trên ngưỡng hòa vốn.

| SKU | Giá sau voucher | Biên LN ròng sau voucher | Có > 0 không |
|---|---|---|---|
| | | | ✅ / ❌ |
```

### 4.3 Logic thiết kế bốn vai trò (dùng để kiểm tra cấu trúc của bạn có đúng không)

```
SKU cấu hình thấp hút click  →  nên nó phải đủ rẻ để tạo ra sự so sánh
SKU chủ lực chốt đơn         →  nên nó phải là bậc "thêm chút tiền là nâng cấp rõ rệt"
SKU cấu hình cao kéo AOV     →  nên nó phải có chênh lệch giá trị thật, không phải đội giá
SKU combo tăng lợi nhuận     →  nên mức tăng giá vốn của nó phải nhỏ hơn mức tăng giá bán
Voucher thu hẹp chênh lệch   →  nên nó phải phát cho SKU chủ lực/cấu hình cao, không phải SKU kéo traffic
```

> **Cách tự kiểm tra**: biến năm câu trên thành câu hỏi và lần lượt tự hỏi. Bậc nào trả lời không được, bậc đó là chỗ thiết kế có vấn đề.

---

# STEP 5 · Chiến lược nuôi trọng số giai đoạn đầu (SOP 1.9)

```markdown
## 5. Chiến lược giá giai đoạn đầu

| Giai đoạn | Giá bán | Biên LN | Mục đích | Điều kiện kích hoạt nâng giá lại |
|---|---|---|---|---|
| Cold start (tuần 1–4) | | | Nuôi trọng số | |
| Giai đoạn nâng giá lại (tuần 5–8) | | | Khôi phục biên LN mục tiêu | |
| Giai đoạn ổn định | Giá mục tiêu | Biên LN mục tiêu | — | — |

**Kiểm tra ràng buộc**

| Hạng mục | Giải thích |
|---|---|
| Dòng tiền có chịu được việc hạ biên lợi nhuận giai đoạn đầu không | `【Cần xác nhận】` cần người đánh giá |
| Giá giai đoạn đầu có thấp hơn ngưỡng hòa vốn không | ✅ / ⚠️ |
| Chỉ số xác định thời điểm nâng giá lại | Khuyến nghị quan sát theo khung test 7 ngày của SOP |
```

> ⚠️ **Hạ biên lợi nhuận giai đoạn đầu không có nghĩa là bán lỗ.** SOP nói "giai đoạn đầu tỷ suất lợi nhuận có thể thấp hơn một chút"——hạ vài điểm thì được, **thủng ngưỡng hòa vốn lại là chuyện khác** (đó là lỗ chiến lược của SKU kéo traffic, cần ghi chú riêng).
> **Tiêu chí phán đoán**: hạ xuống dưới biên lợi nhuận mục tiêu nhưng vẫn trên ngưỡng hòa vốn → nuôi trọng số bình thường; thấp hơn ngưỡng hòa vốn → lỗ chiến lược, cần ghi rõ cùng điều kiện thoát.

---

# STEP 6 · Chỉ số giao cho 06

```markdown
## 6. Các trường giao cho 06 Advertising

| SKU | Giá bán | LN gộp khả dụng trước QC | **ROAS hòa vốn** | Biên LN mục tiêu | % quảng cáo đề xuất | Có chạy quảng cáo được không |
|---|---|---|---|---|---|---|
| SKU chủ lực | | | | | | ✅ |
| SKU cấu hình cao | | | | | | |
| SKU kéo traffic | | | | | | ⚠️ xem ghi chú lỗ chiến lược |

**Giải thích**:
- `ROAS hòa vốn` là đường chuẩn để 06 đánh giá "quảng cáo có lãi không"
- Nếu ROAS hòa vốn của một SKU cao hơn khoảng ROI thường gặp của ngành hàng đó (thường 3–8), **tức là mô hình quảng cáo của nó không đứng vững**, phải nhìn ra ngay từ giai đoạn định giá chứ không đợi chạy quảng cáo rồi mới phát hiện
```

---

# FINAL OUTPUT STRUCTURE

```markdown
## 1. Cấu trúc chi phí
## 2. Tính giá
   ### 2.1 Công thức giá bán
   ### 2.2 Kết quả tính ngược từng SKU
   ### 2.3 Kiểm chứng chéo với phân tích thị trường
## 3. Phương án giá và kiểm tra
   ### 3.1 Phân tích dư địa lợi nhuận
   ### 3.2 Xử lý đặc biệt cho SKU kéo traffic
## 4. Cấu trúc SKU
   ### 4.1 Kiểm tra bậc giá
   ### 4.2 Thiết kế voucher
## 5. Chiến lược giá giai đoạn đầu
## 6. Chỉ số giao cho 06
## 7. Quét tuân thủ đề xuất
   (theo S1–S5 trong 00_system.md; không có vi phạm phải ghi "không có vi phạm")
## 8. Các trường bàn giao
   - sku_structure: []
   - main_sku: ""
   - pricing_table: {}
   - breakeven_roas_by_sku: {}       # → 06
   - coupon_plan: []
   - ramp_up_plan: {}
   - strategic_loss_sku: null        # bắt buộc điền khi SKU kéo traffic thấp hơn ngưỡng hòa vốn, kèm điều kiện thoát
```

---

# SELF-CHECK

- [ ] Giá vốn từng SKU được liệt kê riêng, không dùng một giá vốn cho mọi SKU
- [ ] Hoa hồng/quảng cáo/hoàn hàng trong công thức định giá được tính theo **phần trăm giá bán** và đặt ở mẫu số
- [ ] Đã trình bày đầy đủ quá trình thay số (kiểm lại được)
- [ ] Đã kiểm chứng chéo với `cost_floor_price` của 01 và giải thích ý nghĩa của chênh lệch
- [ ] Mỗi SKU đều đã tính LN gộp trước QC / LN sau QC / biên LN ròng / ROAS hòa vốn
- [ ] Đã tính dư địa lợi nhuận và giải thích mức voucher mà dư địa gánh được
- [ ] Voucher phát cho SKU chủ lực/cấu hình cao (không phải SKU kéo traffic), và giá sau voucher vẫn trên ngưỡng hòa vốn
- [ ] Bậc giá đã được kiểm tra cả hai chiều "quá lớn/quá nhỏ"
- [ ] Khi SKU kéo traffic thấp hơn ngưỡng hòa vốn đã ghi rõ vai trò chiến lược, khối lượng chịu được, điều kiện thoát
- [ ] Giá giai đoạn đầu không thủng ngưỡng hòa vốn; nếu đã thủng thì đã ghi chú là lỗ chiến lược
- [ ] Đã xuất ROAS hòa vốn của từng SKU cho 06
- [ ] Không khai khống thông số, không đề xuất lách chứng nhận, không cam kết hiệu quả, không ra quyết định thu mua thay con người
- [ ] Cuối đầu ra đã kèm quét tuân thủ đề xuất + các trường bàn giao
