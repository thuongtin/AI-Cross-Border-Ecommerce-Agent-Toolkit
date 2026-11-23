# TASK · Định vị sản phẩm, cấu hình, điểm bán hàng và rủi ro

> Dùng kèm: `00_system.md` + đầu ra của 01 Market Research
> Tương ứng SOP **1.7 Chốt sản phẩm chủ lực** + **3.1 Chuẩn bị trước khi đăng bán từng sản phẩm**

---

# INPUT

| Trường | Giải thích |
|---|---|
| `decision_approved` | **Mục chặn**, bắt buộc là `true` |
| `platform` / `target_market` / `category` | Thông tin cơ bản |
| `market_analysis` | Toàn bộ đầu ra của 01 (gồm `target_price_range` / `recommended_config` / `opportunity_config` / `brand_barrier` / `seller_barrier` / `competitor_weakness`) |
| `company_capabilities` | Công ty có làm được cấu hình này không |
| `after_sales_capacity` | Xử lý được hậu mãi gì (có sửa chữa được không / chỉ đổi hàng / có cung cấp phụ kiện được không) |
| `cost_structure` | Dùng để kiểm chứng cấu hình có dư địa lợi nhuận không |
| `planned_specs[]` (tùy chọn) | Cấu hình đã chốt, dùng để so sánh khi mâu thuẫn với đề xuất của thị trường |

---

# STEP 1 · Định vị loại sản phẩm

```markdown
## 1. Loại sản phẩm

| Khía cạnh | Định vị | Căn cứ |
|---|---|---|
| Vai trò trong shop | SKU kéo traffic / SKU lợi nhuận / SKU test / SKU long-tail | |
| Mức độ khác biệt | SKU phổ thông / SKU khác biệt hóa | |
| Vai trò quảng bá | SKU chủ lực / SKU test | |

**Lý do định vị**:
【Căn cứ】<từ phân tích thị trường: rào cản thương hiệu / rào cản người bán / cấu hình cơ hội>
【Đề xuất】<vì sao chọn vai trò này>
```

### Tham khảo chọn vai trò

| Đặc điểm thị trường | Định vị đề xuất |
|---|---|
| Rào cản thương hiệu cao (CR3 cao và top đầu là thương hiệu) | **SKU khác biệt hóa**——tránh đối đầu chiến giá trực diện |
| Rào cản thương hiệu thấp (top đầu là hàng no-brand) | SKU phổ thông vẫn khả thi, cạnh tranh bằng giá vốn và hiệu suất |
| Rào cản người bán cao (CR10 > 70%) | Ưu tiên tìm `opportunity_config` để khác biệt hóa |
| Có `opportunity_config` rõ ràng và chưa bị top đầu chiếm | **SKU chủ lực + SKU khác biệt hóa** |
| Dòng tiền eo hẹp / cần kiểm chứng nhanh | **SKU test**, chạy lô nhỏ trước |

---

# STEP 2 · Chốt cấu hình cốt lõi

```markdown
## 2. Cấu hình cốt lõi

| Khía cạnh cấu hình | Giá trị thị trường đề xuất | Giá trị bên ta chốt | Có khớp không | Giải thích |
|---|---|---|---|---|
| | | | ✅ / ⚠️ | |

**Kiểm tra mức khớp giữa cấu hình và năng lực công ty**

| Cấu hình | Công ty làm được không | Giải thích |
|---|---|---|
| | ✅ / ⚠️ / ❌ | |

⚠️ **Nếu có cấu hình công ty không làm được**: đừng cố ghi vào, hãy ghi chú rõ và trả khía cạnh đó về cho phân tích thị trường chọn lại cấu hình.
```

### Ba nguyên tắc chốt cấu hình

| Nguyên tắc | Giải thích |
|---|---|
| **Traffic chính giữ nhu cầu** | Cấu hình cốt lõi đi theo dòng chính của thị trường (vd. công suất), đảm bảo quy mô nhu cầu |
| **Cấu hình cơ hội tạo khác biệt** | Khía cạnh khác biệt hóa chọn theo `opportunity_config`, vị trí cạnh tranh thấp mà nhu cầu cao |
| **Không chồng thông số** | Đẩy lên cấu hình cao nhất không có nghĩa là bán chạy nhất——dữ liệu thị trường có thể cho thấy phân khúc cấu hình cao có doanh số trung bình thấp nhất |

> **Lưu ý then chốt**: nếu phân tích thị trường cho thấy một phân khúc cấu hình cao (vd. 800W) "nhiều sản phẩm nhất nhưng doanh số trung bình thấp nhất", thì nó **không hợp làm chủ lực**, chỉ hợp làm SKU cấu hình cao.
> **Căn cứ phán đoán là dữ liệu, không phải trực giác "cấu hình càng cao càng tốt".**

---

# STEP 3 · Hội tụ điểm bán hàng chủ lực (cốt lõi của SOP 1.7)

```markdown
## 3. Điểm bán hàng chủ lực

### 3.1 Nguồn điểm bán hàng

| Nguồn | Nội dung | Mức dùng được |
|---|---|---|
| Cấu hình cơ hội | | ✅ Khác biệt hóa cốt lõi |
| Điểm yếu của đối thủ | | ✅ Căn cứ khác biệt hóa |
| Cấu hình phổ biến | | ⭕ Mức tối thiểu (bắt buộc có, nhưng không phải điểm bán hàng) |
| Điều người mua quan tâm nhiều | | ✅ |

### 3.2 Phân tầng điểm bán hàng

| Tầng | Điểm bán hàng | Căn cứ hỗ trợ | Dùng cho |
|---|---|---|---|
| **Điểm bán hàng chính (1 điểm)** | | | Copy chính trên ảnh chính / hook video / từ khóa tiêu đề |
| Điểm bán hàng phụ (3–5 điểm) | | | Trang chi tiết / 5 bullet point mô tả / đoạn điểm bán hàng trong video |
| Điểm bán hàng tối thiểu | | | Trang chi tiết (đảm bảo đủ thông tin) |
| **Cách diễn đạt bị cấm** | | | ⛔ Đưa vào `forbidden_words` |

### 3.3 Kết luận một câu

> **Sản phẩm này của chúng ta bán cho <ai>, đánh vào <điểm bán hàng nào>, dùng <cấu hình nào>, ở mức <giá nào>, tránh <rủi ro nào>.**
```

### Tiêu chí chọn điểm bán hàng chính (theo thứ tự ưu tiên)

1. Đối thủ phần lớn **không có** hoặc **làm kém**
2. Được **nhắc đi nhắc lại** trong đánh giá (review) của người mua
3. Nói rõ được bằng **một con số hoặc một hình ảnh**
4. Liên quan trực tiếp nhất đến giá

> **Điểm bán hàng chính chỉ được có một.** Hai điểm ngang hàng bằng không điểm——người mua không nhớ nổi.
> Điểm bán hàng phụ có thể nhiều, nhưng điểm bán hàng chính quyết định ảnh chính in chữ gì, video mở đầu bằng cảnh nào.

---

# STEP 4 · Danh sách phòng tránh rủi ro (SOP 1.7)

```markdown
## 4. Phòng tránh rủi ro

| # | Loại rủi ro | Rủi ro cụ thể | Cách phòng tránh | Nằm ở đâu |
|---|---|---|---|---|
| 1 | Không được khai khống thông số | | Ghi theo giá trị thực + ghi chú điều kiện test | 03 đoạn thông số |
| 2 | Không được ghi từ khóa thương hiệu | | Đưa vào forbidden_words | 03/04/05 |
| 3 | Vấn đề hậu mãi phải nói trước | | Ghi vào đoạn lưu ý trên trang chi tiết | 03 đoạn 6 |
| 4 | Giới hạn chức năng phải ghi rõ | | Nêu rõ phạm vi khả năng, không dùng cách nói "không làm được" | 03 đoạn 6 |
| 5 | Không được cam kết bừa | | Khớp với năng lực hậu mãi | 03 đoạn 5 |

**Ràng buộc cụ thể dựa trên năng lực hậu mãi**

| Năng lực hậu mãi | Cam kết tương ứng không được ghi |
|---|---|
| Chỉ đổi hàng, không sửa chữa được | ❌ Không ghi "có dịch vụ sửa chữa" |
| Không có điểm bảo hành tại địa phương | ❌ Không ghi "bảo hành tại địa phương" |
| Không hỗ trợ tận nơi | ❌ Không ghi "dịch vụ tận nhà" |
```

> **Phần này là đầu vào của 03 Listing.** Nội dung cụ thể của đoạn cam kết hậu mãi (đoạn 5) và đoạn lưu ý (đoạn 6) lấy thẳng từ đây.

---

# STEP 5 · Tự kiểm tra 8 câu trước khi đăng bán (SOP 3.1)

```markdown
## 5. 8 câu hỏi trước khi đăng bán

| # | Câu hỏi | Câu trả lời | Trạng thái |
|---|---|---|---|
| 1 | Sản phẩm này bán cho ai | | ✅ / ⚠️ |
| 2 | Điểm bán hàng cốt lõi là gì | | |
| 3 | Đối thủ chính là ai | | |
| 4 | Giá đánh vào khoảng nào | | |
| 5 | SKU chủ lực là SKU nào | | |
| 6 | Lợi nhuận tối thiểu là bao nhiêu | | |
| 7 | Có phù hợp để test quảng cáo không | | |
| 8 | Rủi ro hậu mãi có thể gặp là gì | | |

**Xử lý câu chưa trả lời**: với các mục ⚠️, liệt kê hành động cần xác nhận tương ứng, không đăng bán khi còn câu chưa trả lời.
```

**Căn cứ phán đoán câu 7**:

| Tình huống | Có phù hợp test quảng cáo không |
|---|---|
| Có `opportunity_config` rõ ràng và chưa bị độc chiếm | ✅ Phù hợp——khác biệt hóa đủ để gánh ROI |
| Chỉ bán theo mẫu phổ biến, không có khác biệt | ⚠️ Cần xác nhận lợi thế giá vốn trước |
| Tồn kho không đủ | ❌ Không phù hợp——quảng cáo lên sẽ đứt hàng |
| Rủi ro hậu mãi cao mà năng lực không đủ | ❌ Không phù hợp——khuếch đại hoàn hàng |

---

# FINAL OUTPUT STRUCTURE

```markdown
## 1. Loại sản phẩm
## 2. Cấu hình cốt lõi
## 3. Điểm bán hàng chủ lực
## 4. Phòng tránh rủi ro
## 5. 8 câu hỏi trước khi đăng bán
## 6. Quét tuân thủ đề xuất
   (theo S1–S5 trong 00_system.md; không có vi phạm phải ghi "không có vi phạm")
## 7. Các trường giao cho downstream
   - product_type: {role, differentiation, promo_role}
   - final_config: {}
   - core_selling_point: ""              # → 03/04/05
   - secondary_points: []                # → 03/04/05
   - forbidden_words_seed: []            # → 03/04/05
   - risk_mitigation: []                 # → 03 đoạn 5/6
   - after_sales_commitment: ""          # → 03 đoạn 5 (bị ràng buộc bởi năng lực hậu mãi)
   - prelaunch_checklist: {}             # 8 câu hỏi trước khi đăng bán
```

---

# SELF-CHECK

- [ ] `decision_approved` là true
- [ ] Loại sản phẩm đã được định vị đủ cả ba khía cạnh
- [ ] Cấu hình cốt lõi đã được đối chiếu từng mục với đề xuất của thị trường
- [ ] Cấu hình công ty không làm được đã ghi chú, không cố ghi vào
- [ ] Không lấy phân khúc cấu hình cao làm chủ lực (nếu dữ liệu cho thấy cấu hình cao có doanh số trung bình thấp)
- [ ] Điểm bán hàng chính **chỉ có một**, và đạt bốn tiêu chí chọn
- [ ] Kết luận một câu có đủ năm yếu tố (bán cho ai/đánh vào gì/cấu hình nào/giá nào/tránh gì)
- [ ] Phòng tránh rủi ro đủ 5 loại, và khớp với năng lực hậu mãi
- [ ] 8 câu hỏi trước khi đăng bán đều có câu trả lời, mục ⚠️ có hành động tương ứng
- [ ] Không khai khống thông số
- [ ] Cuối đầu ra đã kèm quét tuân thủ đề xuất + các trường giao cho downstream
