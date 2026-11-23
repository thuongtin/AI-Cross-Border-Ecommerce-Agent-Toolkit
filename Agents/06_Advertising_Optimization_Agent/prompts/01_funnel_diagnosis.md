# TASK · Chẩn đoán phễu bốn loại và danh sách hành động

> Dùng kèm: `00_system.md` + `templates/input_ad_data.md` (dữ liệu quảng cáo đã điền)
> Tương ứng SOP **3.6 Logic điều chỉnh quảng cáo**

---

# INPUT

| Trường | Giải thích | Ảnh hưởng khi thiếu |
|---|---|---|
| `platform` | Sàn mục tiêu | Không áp dụng được quy tắc khác biệt giữa các sàn |
| `test_window_days` | Chu kỳ test (ngày) | Không xác định được dữ liệu đã ổn định chưa |
| `price` | Giá bán | Không tính được ROAS và ngưỡng hòa vốn |
| `ad_groups[]` | Mảng nhóm quảng cáo | — |
| `ad_groups[].keyword_or_target` | Đối tượng quảng cáo (từ khóa/sản phẩm/shop) | Không đưa ra được hành động cụ thể |
| `ad_groups[].match_type` | Kiểu khớp (rộng/chính xác/đối thủ/ngữ cảnh) | Ảnh hưởng trọng tâm chẩn đoán |
| `ad_groups[].impressions` | Lượt hiển thị | Bắt buộc |
| `ad_groups[].clicks` | Click | Bắt buộc |
| `ad_groups[].add_to_cart` | Thêm vào giỏ | Bắt buộc (thiếu thì không xét được khâu 2) |
| `ad_groups[].orders` | Đơn | Bắt buộc |
| `ad_groups[].spend` | Chi phí | Bắt buộc |
| `cost_structure` | Cấu trúc chi phí (giá vốn/vận chuyển/kho/tỷ lệ hoa hồng/tỷ lệ hoàn hàng) | Thiếu thì **từ chối xuất kết luận ROI** |
| `existing_main_image` | Mô tả ảnh chính hiện tại (tùy chọn) | Khi CTR không đạt, không đưa ra được đề xuất đổi ảnh cụ thể |
| `existing_title` | Tiêu đề hiện tại (tùy chọn) | Khi CTR không đạt, không đưa ra được đề xuất sửa tiêu đề cụ thể |

---

# STEP 1 · Tổng quan

Tính các chỉ số tổng trước, đưa ra **đánh giá tổng một câu**.

```markdown
## 1. Tổng quan

| Chỉ số | Giá trị | Chuẩn | Đánh giá |
|---|---|---|---|
| Tổng lượt hiển thị | | — | — |
| Tổng click | | — | — |
| **CTR tổng** | | 3–5% | ✅ / ❌ |
| Tổng thêm vào giỏ | | — | — |
| **Tỷ lệ thêm vào giỏ tổng** | | > 8% | ✅ / ❌ |
| Tổng đơn | | — | — |
| **Tỷ lệ chuyển đổi tổng** | | > 1% | ✅ / ❌ |
| Tổng chi phí | | — | — |
| Tổng GMV | | — | — |
| **ROAS tổng** | | ≥ ngưỡng hòa vốn `<giá trị>` | ✅ / ❌ |
| **Lợi nhuận gộp đóng góp ròng** | | > 0 | ✅ / ❌ |

**Đánh giá tổng một câu**: <tổng thể đang ở trạng thái nào, việc nên làm nhất là gì>

**Ghi chú độ tin cậy dữ liệu**: <cỡ mẫu có đủ không / chu kỳ test có đạt không>
```

**Công thức tính** (bắt buộc trình bày để dễ kiểm tra lại):

```
CTR               = Click ÷ Lượt hiển thị
Tỷ lệ thêm giỏ    = Thêm vào giỏ ÷ Click
Tỷ lệ chuyển đổi  = Đơn ÷ Click
CPC               = Chi phí ÷ Click
CPA               = Chi phí ÷ Đơn
GMV               = Đơn × Giá bán
ROAS              = GMV ÷ Chi phí
Đóng góp ròng     = Lợi nhuận gộp khả dụng trước quảng cáo × Đơn − Chi phí
```

---

# STEP 2 · Xét phễu theo từng nhóm quảng cáo

Đây là phần cốt lõi của nhiệm vụ. **Mỗi nhóm quảng cáo đi riêng một lượt bốn bước xét**.

```markdown
## 2. Chẩn đoán theo từng nhóm quảng cáo

### Nhóm quảng cáo A · <từ khóa/đối tượng> (<kiểu khớp>)

**Dữ liệu gốc**

| Hiển thị | Click | CTR | Thêm giỏ | Tỷ lệ thêm giỏ | Đơn | Tỷ lệ chuyển đổi | Chi phí | CPC | CPA | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

**Xét phễu**

| Bước | Hạng mục kiểm tra | Chuẩn | Thực tế | Đạt | Kết luận |
|---|---|---|---|---|---|
| 1 | CTR | 3–5% | | ✅/❌ | |
| 2 | Tỷ lệ thêm giỏ | > 8% | | ✅/❌ | |
| 3 | Tỷ lệ chuyển đổi | > 1% | | ✅/❌ | |
| 4 | ROAS | ≥ ngưỡng hòa vốn | | ✅/❌ | |

**Kết luận**: <một trong bốn loại hoặc đơn vị khỏe>

**Phân tích nguyên nhân**: <vì sao xuất hiện triệu chứng này, chỉ tới khâu cụ thể nào>

**Danh sách hành động**

| # | Hành động | Đối tượng | Căn cứ | Hiệu quả kỳ vọng | Ưu tiên |
|---|---|---|---|---|---|
| 1 | | | | | 🔴 Cao |

**Vòng này dứt khoát không động vào**: <liệt kê các khâu của nhóm này không cần sửa, và giải thích vì sao>
```

> **"Vòng này dứt khoát không động vào" là mục bắt buộc của nhiệm vụ này.** Nó ngăn người vận hành tiện tay làm hỏng khâu B khi đang sửa khâu A — tình huống điển hình "sửa tới cuối không biết hành động nào có tác dụng".

---

# STEP 3 · Tổng hợp hành động và ưu tiên

```markdown
## 3. Tổng hợp hành động

Sắp xếp theo「phạm vi ảnh hưởng × mức khẩn cấp」:

| Ưu tiên | Hành động | Nhóm quảng cáo liên quan | Tỷ trọng ngân sách bị ảnh hưởng | Hiệu quả kỳ vọng | Chu kỳ kiểm tra lại |
|---|---|---|---|---|---|
| 🔴 P0 | | | | | 7 ngày |
| 🟡 P1 | | | | | 7 ngày |
| ⚪ P2 | | | | | 7 ngày |

### Mỗi lần chỉ sửa một việc

Số thay đổi đề xuất trong vòng này: <n> hạng mục
<nếu > 1 hạng mục, giải thích vì sao bắt buộc sửa cùng lúc / hoặc đề xuất tách thành mấy vòng>
```

**Về "mỗi lần chỉ sửa một việc"**:

Lý tưởng là mỗi vòng chỉ sửa một biến, để hiệu quả có thể quy nguyên nhân. Nhưng thực tế nếu một khâu nào đó không đạt nghiêm trọng (như CTR chỉ có 1,4%, chưa tới một nửa mức sàn của chuẩn) và chiếm phần lớn ngân sách, thì có thể đồng thời đổi ảnh chính và cắt từ khóa kém hiệu quả — vì hai việc này chỉ tới **cùng một nguyên nhân gốc** (khâu click), không phải hai biến độc lập.

**Tiêu chí phán đoán**: thay đổi có chỉ tới **cùng một nguyên nhân gốc** không. Có → có thể sửa cùng đợt; không → bắt buộc tách vòng.

---

# STEP 4 · Quy trình gỡ bug khi quảng cáo không chạy

**Chỉ xuất mục này khi đầu vào có nhóm quảng cáo "thiếu hiển thị / không tiêu được tiền".**

```markdown
## 4. Xử lý quảng cáo không chạy

Nhóm kích hoạt: <liệt kê các nhóm có lượt hiển thị thấp bất thường>

| Nhóm | Hiển thị | Đánh giá |
|---|---|---|
| | | Thiếu hiển thị, chưa thể vào chẩn đoán phễu |

**Quy trình xử lý** (SOP 3.6)

| Bước | Hành động | Giải thích | Chu kỳ theo dõi |
|---|---|---|---|
| 1 | Đổi ảnh chính | SOP: thường chỉ cần đổi ảnh chính là gỡ được bug quảng cáo | 1–2 ngày |
| 2 | Tinh chỉnh tiêu đề đồng thời | Ưu tiên thấp hơn ảnh chính, chỉ làm khi đổi ảnh chính không hiệu quả | 1–2 ngày |
| 3 | Tìm CSKH mở ticket | Dùng khi hai bước trên không hiệu quả | Theo thời gian phản hồi của sàn |

**Lưu ý**: đừng dùng "tăng giá thầu" làm biện pháp đầu tiên. SOP chỉ rõ nên sửa creative trước.
```

---

# STEP 5 · Phương án kiểm tra lại

```markdown
## 5. Phương án kiểm tra lại

| Hạng mục | Nội dung |
|---|---|
| Thời điểm kiểm tra lại | Ngày thứ **7** sau khi thay đổi (khoảng test của SOP) |
| Dữ liệu cần thu | Cùng các trường của vòng này (hiển thị/click/thêm giỏ/đơn/chi phí) |
| Tiêu chí đạt | Chỉ số của mọi khâu được sửa quay về trên đường chuẩn, và ROAS ≥ ngưỡng hòa vốn |
| Xử lý khi không đạt | Quay lại Step 2 chẩn đoán lại, **đừng tiếp tục tăng liều cùng một hành động** |
| Cần xác nhận đồng thời | Trong thời gian thay đổi có chương trình, chỉnh giá, động thái đối thủ hay nhiễu bên ngoài nào không |
```

> **"Đừng tiếp tục tăng liều cùng một hành động" rất quan trọng**: nếu đổi ảnh chính 7 ngày mà CTR không lên, đổi thêm một ảnh chính nữa thường cũng vô ích — nghĩa là vấn đề không nằm ở ảnh chính. Phải quay lại chẩn đoán, xác định lại khâu.

---

# FINAL OUTPUT STRUCTURE

```markdown
## 1. Tổng quan
## 2. Chẩn đoán theo từng nhóm quảng cáo
   (mỗi nhóm gồm: dữ liệu gốc / xét phễu / kết luận / phân tích nguyên nhân / danh sách hành động / phần vòng này không động vào)
## 3. Tổng hợp hành động
## 4. Xử lý quảng cáo không chạy      (xuất có điều kiện)
## 5. Phương án kiểm tra lại
## 6. Quét tuân thủ đề xuất
   (xuất theo G1–G5 của 00_system.md; không vi phạm thì bắt buộc ghi "không vi phạm")
## 7. Các trường bàn giao cho module khác
   - symptom_by_group: {}          # triệu chứng từng nhóm → chuyển cho 03/04 làm đầu vào sửa đổi
   - ctr_fail_groups: []           # nhóm CTR không đạt → 03 sửa tiêu đề / 04 đổi ảnh chính
   - atc_fail_groups: []           # nhóm thêm giỏ không đạt → 03 sửa trang chi tiết
   - cvr_fail_groups: []           # nhóm chuyển đổi không đạt → 03 sửa cách hiển thị giá / 07 phân tích đánh giá
   - breakeven_roas: <giá trị>     # ngưỡng hòa vốn, dùng để đối chiếu khi kiểm tra lại
   - review_needed: true/false     # có cần 07 vào phân tích đánh giá không
```

---

# SELF-CHECK

- [ ] Mỗi nhóm quảng cáo đều đi riêng đủ bốn bước xét, không bỏ bước
- [ ] Mỗi nhóm đều có kết luận rõ ràng (một trong bốn loại / đơn vị khỏe / thiếu dữ liệu)
- [ ] Mỗi nhóm đều xuất phần "vòng này dứt khoát không động vào"
- [ ] Không đề xuất chỉnh giá thầu khi phần đầu phễu chưa đạt
- [ ] Mỗi dòng trong danh sách hành động đều có đối tượng và con số cụ thể
- [ ] Đã trình bày công thức tính các chỉ số
- [ ] Đã tính ROAS hòa vốn (khi thiếu cấu trúc chi phí đã từ chối rõ ràng việc xuất kết luận ROI)
- [ ] Đã ghi chú trường hợp thiếu mẫu / thiếu chu kỳ
- [ ] Đã giải thích các thay đổi có chỉ tới cùng một nguyên nhân gốc không (quyết định có sửa cùng đợt được không)
- [ ] Đã xuất phương án kiểm tra lại
- [ ] Cuối đầu ra đã kèm quét tuân thủ đề xuất + các trường cho hạ nguồn
