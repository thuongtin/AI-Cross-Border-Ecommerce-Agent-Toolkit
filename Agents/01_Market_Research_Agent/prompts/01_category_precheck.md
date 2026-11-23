# TASK · Sàng lọc sơ bộ ngành hàng

> Dùng kèm: `00_system.md` + `templates/input_category_research.md`
> Tương ứng SOP **1.1 Sàng lọc sơ bộ ngành hàng**

**Mục đích của bước này không phải là chọn sản phẩm hoàn chỉnh, mà là trước khi tốn tiền phân tích quy mô thị trường, đánh giá xem ngành hàng này có đáng phân tích tiếp hay không.**

---

# INPUT

Trường bắt buộc:

| Trường | Mô tả | Ảnh hưởng khi thiếu |
|---|---|---|
| `category` | Tên ngành hàng | — |
| `platform` / `target_market` | Sàn và thị trường | Không áp dụng được quy tắc hạn chế của sàn |
| `company_capabilities` | Nguồn lực công ty: hàng sẵn / nhà cung cấp / lợi thế chi phí / kho bãi vận chuyển / năng lực hậu mãi | **Chặn** |
| `product_profile` | Hồ sơ sản phẩm: kích thước / cân nặng / dễ vỡ không / cần chứng nhận không / có pin không | **Chặn** |
| `cost_structure` | Cấu trúc chi phí (để đánh giá biên lợi nhuận) | Không đánh giá được "ngành hàng rủi ro cao có đủ lợi nhuận để gánh không" |
| `metrics_report` | Báo cáo chỉ số (tùy chọn) | Thiếu thì bước này chỉ đánh giá định tính |

---

# STEP 1 · Có hợp với nguồn hàng hiện tại của công ty không

Kiểm tra từng mục, **mỗi mục bắt buộc ghi ✅ / ❌ / ⚠️ (thiếu thông tin)**:

```markdown
## 1. Mức độ phù hợp với nguồn hàng

| Hạng mục kiểm tra | Kết luận | Căn cứ / Nội dung cần xác nhận |
|---|---|---|
| Công ty có hàng sẵn hoặc hàng sắp về không | ✅ / ❌ / ⚠️ | |
| Có nhà cung cấp ổn định không | | |
| Giá vốn sản phẩm có lợi thế không | | |
| Sản phẩm có hợp với thị trường mục tiêu không | | |
| Kích thước, cân nặng có hợp với kho bãi và vận chuyển hiện tại không | | |
| Có năng lực xử lý hậu mãi, sửa chữa, phụ kiện, đổi trả không | | |

**Kết luận**:
- Từ ba mục ❌ trở lên → **không khuyến nghị vào**, xuất kết luận và dừng lại
- Có mục ⚠️ → liệt kê danh sách cần xác nhận, ghi chú "cần con người xác nhận rồi mới đánh giá"
- Tất cả ✅ → sang Step 2
```

**Logic đánh giá** (nguyên văn SOP):

> Nếu công ty có hàng, có lợi thế chi phí, có năng lực chuỗi cung ứng thì có thể sang bước phân tích tiếp theo;
> nếu công ty không có chuỗi cung ứng, không có năng lực hậu mãi, không có lợi thế giá thì **dù thị trường tốt cũng chưa chắc đã nên làm**.

---

# STEP 2 · Có thuộc ngành hàng tỷ lệ hoàn cao / hậu mãi nhiều / rủi ro cao không

SOP liệt kê 6 chiều đánh giá:

```markdown
## 2. Xác định ngành hàng rủi ro

| # | Chiều đánh giá | Kết luận | Giải thích cụ thể |
|---|---|---|---|
| 1 | Sản phẩm có dễ phát sinh lỗi khi sử dụng không | | |
| 2 | Sản phẩm có dễ gây khiếu nại từ người mua không | | |
| 3 | Chi phí hoàn hàng của sản phẩm có cao không | | |
| 4 | Sản phẩm có dễ bị khai khống thông số không | | |
| 5 | Sản phẩm có rủi ro về sở hữu trí tuệ, từ khóa thương hiệu, hàng cấm bán trên sàn không | | |
| 6 | Sản phẩm có dễ khiến shop bị phạt điểm do giao hàng, vỡ hỏng, sửa chữa không | | |

### 2.1 Mức độ rủi ro

| Mức | Số mục dính | Ý nghĩa |
|---|---|---|
| 🟢 Rủi ro thấp | 0–1 | Vận hành bình thường |
| 🟡 Rủi ro trung bình | 2–3 | Cần dự phòng năng lực hậu mãi và nội dung phòng thủ trong mô tả |
| 🔴 Rủi ro cao | ≥ 4 | **Cần lợi nhuận cao mới gánh được** |
```

### 2.2 Kiểm tra khả năng gánh rủi ro bằng lợi nhuận của ngành hàng rủi ro cao

**SOP nói rõ: ngành hàng rủi ro cao cần lợi nhuận cao mới gánh được.** Vì vậy khi dính rủi ro cao, bắt buộc làm bước kiểm tra này:

```markdown
### 2.2 Kiểm tra khả năng gánh rủi ro bằng lợi nhuận

| Hạng mục | Giá trị |
|---|---|
| Giá bán mục tiêu | |
| Lợi nhuận gộp khả dụng trước quảng cáo | |
| Biên lợi nhuận gộp | |
| Tỷ lệ hoàn dự kiến | |
| Chi phí hậu mãi dự kiến/đơn | |
| **Lợi nhuận gộp ròng sau rủi ro** | |
| Có đủ bù rủi ro không | ✅ / ❌ |

**Kết luận**:
- Lợi nhuận gộp ròng sau rủi ro > 0 và biên lợi nhuận gộp ≥ mục tiêu của ngành hàng → gánh được rủi ro
- Lợi nhuận gộp ròng sau rủi ro ≤ 0 → **không khuyến nghị vào** (biên thấp mà làm ngành hàng rủi ro cao = chắc chắn lỗ)
```

> ⚠️ **Đây là bước mà rất nhiều người bán bỏ qua.** Vấn đề thường gặp ở ngành hàng rủi ro cao là: nhìn biên lợi nhuận gộp thấy cũng được, nhưng tính cả rủi ro hoàn hàng, hậu mãi, sửa chữa, phạt điểm vào thì chẳng còn bao nhiêu.
> Nếu thiếu `cost_structure`, bước này **không thực hiện được**, bắt buộc xuất `[INPUT_MISSING]` chứ không được bỏ qua.

---

# STEP 3 · Kiểm tra hạn chế của sàn và tuân thủ (compliance)

```markdown
## 3. Kiểm tra hạn chế của sàn

| Hạng mục kiểm tra | Kết luận | Giải thích |
|---|---|---|
| Có nằm trong danh sách hàng cấm bán của sàn không | | |
| Có thuộc ngành hàng hạn chế (cần xin quyền bán) không | | |
| Có cần chứng nhận không (ví dụ ANATEL / INMETRO của Brazil) | | |
| Có liên quan đăng ký thương hiệu hoặc ủy quyền không | | |
| Có thuộc tính nhạy cảm khi vận chuyển như pin / chất lỏng / nam châm không | | |
| Kích thước, cân nặng có vượt giới hạn vận chuyển của sàn không | | |

**Nếu có mục cần chứng nhận/quyền bán**: xuất rõ "cần có X trước mới đăng bán được", không gợi ý bất kỳ cách lách nào.
```

---

# STEP 4 · Kết luận sàng lọc sơ bộ

```markdown
## 4. Kết luận sàng lọc sơ bộ ngành hàng

| # | Hạng mục kết luận | Nội dung |
|---|---|---|
| 1 | Có hợp với nguồn hàng hiện tại của công ty không | ✅ Phù hợp / ❌ Không phù hợp / ⚠️ Cần xác nhận |
| 2 | Có lợi thế chuỗi cung ứng không | |
| 3 | Có vấn đề về vận chuyển hoặc kho bãi không | |
| 4 | Có thuộc ngành hàng tỷ lệ hoàn cao, hậu mãi nhiều, rủi ro cao không | 🟢 / 🟡 / 🔴 (dính n mục) |
| 5 | Lợi nhuận của ngành hàng rủi ro cao có đủ gánh không | ✅ Đủ / ❌ Không đủ / ⚠️ Thiếu dữ liệu |
| 6 | Có hạn chế của sàn không | |
| 7 | **Có sang bước phân tích quy mô thị trường tiếp theo không** | ✅ Sang / ❌ Không sang |
```

## Kết luận phải viết thành "một câu + điều kiện"

```markdown
**Nhận định**:
Với điều kiện <điều kiện A> và <điều kiện B> được đáp ứng, dữ liệu ủng hộ việc sang bước phân tích quy mô thị trường tiếp theo.
Ngược lại, nếu <điều kiện C> không đáp ứng thì không khuyến nghị vào.

**Danh sách cần xác nhận** (con người bổ sung xong mới quyết định cuối cùng):
- [ ] ...
- [ ] ...
```

**Không viết kết luận vô điều kiện kiểu "nhìn chung khuyến nghị vào".**

---

# FINAL OUTPUT STRUCTURE

```markdown
## 1. Mức độ phù hợp với nguồn hàng
## 2. Xác định ngành hàng rủi ro
   ### 2.1 Mức độ rủi ro
   ### 2.2 Kiểm tra khả năng gánh rủi ro bằng lợi nhuận      (bắt buộc khi rủi ro cao)
## 3. Kiểm tra hạn chế của sàn
## 4. Kết luận sàng lọc sơ bộ ngành hàng
## 5. Quét tuân thủ phân tích
   (theo M1–M5 trong 00_system.md; không vi phạm thì bắt buộc ghi "không vi phạm")
## 6. Các trường bàn giao cho bước sau
   - precheck_pass: true/false
   - risk_level: low/medium/high
   - risk_items: []
   - platform_restrictions: []
   - pending_confirmations: []
   - carry_to_next_step: []    # các mục bước sau cần đặc biệt lưu ý
```

---

# SELF-CHECK

- [ ] 6 mục phù hợp nguồn hàng đều có kết luận từng mục, không bỏ sót
- [ ] 6 chiều rủi ro đều có kết luận từng mục, không bỏ sót
- [ ] Khi rủi ro cao đã kiểm tra khả năng gánh bằng lợi nhuận; thiếu cấu trúc chi phí thì đã báo lỗi chứ không bỏ qua
- [ ] Hạn chế của sàn (cấm bán/hạn chế bán/chứng nhận/nhạy cảm vận chuyển) đã kiểm tra từng mục
- [ ] Khi kết luận "không sang" đã **dừng lại**, không làm tiếp phân tích quy mô và giá
- [ ] Kết luận là "có điều kiện", không phải vô điều kiện
- [ ] Đã xuất danh sách cần xác nhận
- [ ] Không gợi ý bất kỳ cách lách quy định của sàn nào
- [ ] Cuối đầu ra đã kèm quét tuân thủ phân tích + các trường bàn giao
