# TASK · Tính ngưỡng hòa vốn và mô hình ngân sách / ROI

> Dùng kèm: `00_system.md` + đầu ra của `01_funnel_diagnosis.md`
> Tương ứng SOP **3.5 Logic nền của chạy quảng cáo** + **3.6 Cách bật/tắt quảng cáo** + **1.10 Kế hoạch đẩy sản phẩm**

---

# INPUT

| Trường | Giải thích | Ảnh hưởng khi thiếu |
|---|---|---|
| `platform` | Sàn mục tiêu | Không áp dụng được quy tắc nhịp ngân sách |
| `price` | Giá bán | Không tính được ngưỡng hòa vốn |
| `cost_structure` | Cấu trúc chi phí | **Hạng mục chặn** — thiếu thì từ chối thực hiện |
| `cost_structure.unit_cost` | Giá vốn | Chặn |
| `cost_structure.shipping` | Vận chuyển chặng cuối | Chặn |
| `cost_structure.warehouse` | Phí kho/phí xử lý | Chặn |
| `cost_structure.commission_rate` | Tỷ lệ hoa hồng sàn | Chặn |
| `cost_structure.return_rate` | Tỷ lệ hao hụt hoàn hàng | Chặn |
| `target_margin_rate` | Biên lợi nhuận gộp mục tiêu (tùy chọn, mặc định theo SOP: hàng lớn 30–35% / hàng nhỏ 25–30%) | Ảnh hưởng đường đạt chuẩn |
| `current_roas` | ROAS hiện tại (tùy chọn) | Không đưa ra được biên độ cải thiện |
| `daily_budget_current` | Ngân sách ngày hiện tại (tùy chọn) | Không đưa ra được đề xuất ngân sách |
| `competitor_benchmark` | Dữ liệu quảng bá của đối thủ (tùy chọn, từ SOP 1.10) | Không đưa ra được mục tiêu theo giai đoạn |
| `target_market_timezone` | Múi giờ thị trường mục tiêu (tùy chọn) | Không đưa ra được nhịp theo khung giờ |

---

# PART A · Tính ngưỡng hòa vốn

## A1 · Tính lợi nhuận gộp khả dụng trước quảng cáo

```markdown
## 1. Tính ngưỡng hòa vốn

### 1.1 Lợi nhuận gộp khả dụng trước quảng cáo

| Hạng mục | Số tiền | % giá bán |
|---|---|---|
| Giá bán | R$ <P> | 100% |
| − Giá vốn | R$ <c> | <%> |
| − Vận chuyển chặng cuối | R$ <s> | <%> |
| − Phí kho/phí xử lý | R$ <w> | <%> |
| − Hoa hồng sàn (<r>%) | R$ <P×r> | <r>% |
| − Hao hụt hoàn hàng (<rr>%) | R$ <P×rr> | <rr>% |
| **= Lợi nhuận gộp khả dụng trước quảng cáo** | **R$ <M>** | **<M/P>%** |

Quá trình tính:
M = <P> − <c> − <s> − <w> − <P>×<r> − <P>×<rr>
  = <P> − <c> − <s> − <w> − <P×r> − <P×rr>
  = **R$ <M>**
```

> ⚠️ **Hoa hồng và hao hụt hoàn hàng bắt buộc tính theo % giá bán**. Coi chúng là số tiền cố định là kiểu tính sai phổ biến nhất.

## A2 · Tính ROAS hòa vốn

```markdown
### 1.2 ROAS hòa vốn

ROAS hòa vốn = Giá bán ÷ Lợi nhuận gộp khả dụng trước quảng cáo
             = <P> ÷ <M>
             = **<giá trị>**

Ý nghĩa: khi ROAS thấp hơn <giá trị>, nhóm quảng cáo này bán mỗi đơn là lỗ một đơn, dù chỉ số phễu đẹp tới đâu.
```

## A3 · ROAS đạt chuẩn

```markdown
### 1.3 ROAS đạt chuẩn (cần để đạt biên lợi nhuận gộp mục tiêu)

Chi phí quảng cáo dự trù khi định giá = Giá bán × Tỷ lệ chi phí quảng cáo
                                     = <P> × <ad_rate>
                                     = R$ <giá trị>

ROAS đạt chuẩn = Giá bán ÷ Chi phí quảng cáo dự trù = <giá trị>
```

> **Chỗ này thường xuất hiện một khoảng chênh khó chịu**:
> ROAS đạt chuẩn tính theo tỷ lệ chi phí quảng cáo SOP giả định khi định giá (hàng nhỏ 5–10%) thường ở mức **trên 10 lần**,
> trong khi khoảng ROAS thường gặp khi chạy thực tế là **3–8 lần**.
>
> **Đây không phải tính sai, đây là cấu trúc lợi nhuận thật.** Bắt buộc chỉ rõ khoảng chênh này và đưa ra hướng xử lý (xem A4).

## A4 · Bảng độ nhạy ROAS (bắt buộc xuất)

```markdown
### 1.4 Phân tích độ nhạy ROAS

| ROAS | Phí QC/đơn | Lợi nhuận gộp còn lại/đơn | % giá bán | Đánh giá |
|---|---|---|---|---|
| <hòa vốn−0.5> | | **Số âm** | | ❌ Lỗ |
| **<hòa vốn>** | | ~0 | ~0% | ⚠️ Hòa vốn |
| <hòa vốn+0.7> | | | | ✅ Lãi mỏng |
| 5,0 | | | | ✅ |
| 8,0 | | | | ✅ |
| <đạt chuẩn> | | | <mục tiêu%> | 🎯 Đạt mục tiêu định giá |

**Kết luận then chốt**: <ROAS hiện tại đang ở nấc nào, muốn có lãi tối thiểu cần đạt bao nhiêu>
```

## A5 · Hướng xử lý (bắt buộc xuất)

```markdown
### 1.5 Nếu「chi phí quảng cáo dự trù khi định giá」và「ROAS thực tế」chênh nhau quá lớn, các hướng có thể chọn

| # | Hướng | Cách làm | Cái giá |
|---|---|---|---|
| 1 | **Nâng mức dự trù chi phí quảng cáo khi định giá** | Nâng tỷ lệ dự trù từ <%> lên **12–15%**, tính lại giá bán | Giá bán tăng, có thể ảnh hưởng click và chuyển đổi |
| 2 | **Chấp nhận biên lợi nhuận thấp, dựa vào traffic tự nhiên** | Quảng cáo chỉ làm lực đẩy khởi động lạnh, có traffic tự nhiên rồi thì giảm dần ngân sách | Chu kỳ lên đơn dài hơn, cần kiên nhẫn hơn |
| 3 | **Tối ưu cấu trúc chi phí** | Đổi nhà cung cấp / đổi đơn vị vận chuyển / đàm phán phí tốt hơn | Cần thượng nguồn phối hợp, chu kỳ dài |
| 4 | **Tăng giá trị đơn hàng** | Thêm SKU cấu hình cao, SKU combo (tương ứng SOP 3.2) | Cần sản phẩm hỗ trợ |
| 5 | **Bỏ sản phẩm này** | Nếu các hướng trên đều không khả thi, nghĩa là cấu trúc lợi nhuận không đứng được | Khoản đầu tư ban đầu thành chi phí chìm |

**Đề xuất cho case này**: <chọn hướng nào, vì sao>
```

---

# PART B · Mô hình hai biến ngân sách × ROI

Phán đoán cốt lõi của SOP 3.5:

> Mỗi sản phẩm đều có một mô hình quảng cáo tương đối phù hợp với chính nó. Mô hình này chủ yếu do hai biến then chốt quyết định: **ngân sách tối đa** và **ROI mục tiêu**.

## B1 · Xác định ngân sách tối đa

```markdown
## 2. Mô hình ngân sách

### 2.1 Mức trần ngân sách tối đa

Ngân sách tối đa phụ thuộc vào **quy mô traffic của thị trường** và **sức chứa của phân khúc**, không phải càng cao càng tốt.

| Căn cứ phán đoán | Tình hình case này | Ảnh hưởng tới ngân sách |
|---|---|---|
| Quy mô thị trường của ngành hàng | <lớn / vừa / nhỏ> | |
| Lượng nhu cầu tìm kiếm | | |
| Mức doanh số của đối thủ | | |
| Điểm uy tín hiện tại của link bên mình | | |

**Phán đoán mức trần ngân sách**:
- Nếu quy mô thị trường lớn + nhu cầu tìm kiếm mạnh + doanh số đối thủ cao → có thể gánh ngân sách lớn hơn
- Nếu bản thân thị trường nhỏ → **tiếp tục tăng ngân sách chỉ làm tăng chi phí, không mang lại thêm đơn một cách ổn định**

**Ngân sách ngày tối đa đề xuất**: R$ <giá trị> — <lý do>
```

## B2 · Xác định ROI mục tiêu

```markdown
### 2.2 Khoảng ROI mục tiêu

Mức trần ROI phụ thuộc vào **sức cạnh tranh của sản phẩm** (ảnh chính / giá / đánh giá / trang chi tiết / cam kết hậu mãi).

| Chiều cạnh tranh | Hiện trạng | Ảnh hưởng tới mức trần ROI |
|---|---|---|
| Ảnh chính | | |
| Giá | | |
| Số lượng và chất lượng đánh giá | | |
| Trang chi tiết | | |
| Cam kết hậu mãi | | |

**Phán đoán**:
- Sức cạnh tranh mạnh → có thể có chuyển đổi hiệu quả ở mức ROI tương đối cao
- Sức cạnh tranh yếu → **đẩy ROI quá cao sẽ khiến quảng cáo không tiêu được tiền, không có đủ lượt hiển thị và mẫu**

**Khoảng ROI mục tiêu đề xuất**: `<mức sàn>` – `<mức trần>` (mức sàn = ngưỡng hòa vốn + biên an toàn)

⚠️ **Đừng ngay từ đầu đặt ROI sát ngưỡng hòa vốn**. ROI đặt càng sát ngưỡng hòa vốn, quảng cáo càng khó chạy, mẫu càng ít, càng không xác định được mô hình thật. Cách làm đúng: **chạy ra mẫu trước, rồi siết ROI dần**.
```

## B3 · Chu kỳ test và mục tiêu theo giai đoạn

```markdown
### 2.3 Chu kỳ test

| Hạng mục | Giá trị |
|---|---|
| Chu kỳ ổn định mô hình theo sàn chính thức | 14 ngày |
| **Khoảng test khuyến nghị khi thực chiến** | **7 ngày** |
| Khi chạy đang lỗ có thể rút xuống | 3–5 ngày (ưu tiên cắt lỗ) |
| Khoảng test vòng này | <n> ngày |

### 2.4 Mục tiêu theo giai đoạn (mỗi 7 ngày là một giai đoạn)

| Giai đoạn | Ngày | Mục tiêu | Điều kiện đạt | Xử lý khi không đạt |
|---|---|---|---|---|
| Tuần 1 | 1–7 | Chạy ra mẫu | Hiển thị ≥ <n> / click ≥ <n> / đơn ≥ <n> | Kiểm tra ngân sách có quá thấp, từ khóa có quá hẹp không |
| Tuần 2 | 8–14 | Xét phễu | Chỉ số các khâu về lại đường chuẩn | Quay về `01_funnel_diagnosis.md` xác định lại |
| Tuần 3 | 15–21 | Hội tụ ROI | ROAS ≥ ngưỡng hòa vốn | Cắt các nhóm lâu ngày không đạt, dồn ngân sách vào nhóm khỏe |
| Tuần 4 | 22–28 | Scale | Tăng ngân sách trong khi giữ được ROAS | Scale dần, mỗi lần tăng 20–30% rồi theo dõi |
```

> **"Mỗi giai đoạn chỉ đẩy một việc"**: đừng trong cùng một giai đoạn vừa muốn chạy ra mẫu vừa muốn hội tụ ROI. Mẫu và hiệu suất là hai mục tiêu xung đột, bắt buộc tách giai đoạn.

## B4 · Suy ngược từ đối thủ (SOP 1.10)

**Xuất khi đầu vào có `competitor_benchmark`.**

```markdown
### 2.5 Suy ngược nhịp quảng bá của đối thủ

| Đối thủ | Thời gian đăng bán | Doanh số tháng | Doanh số 30 ngày gần nhất | Số đánh giá | Số đánh giá có ảnh | Vị trí quảng cáo |
|---|---|---|---|---|---|---|
| | | | | | | |

**Kết luận suy ngược**

| Câu hỏi | Câu trả lời rút ra từ dữ liệu đối thủ |
|---|---|
| Link mới trong ngành hàng này mất khoảng bao lâu thì lên đơn | |
| Trước khi lên đơn cần bao nhiêu đánh giá nền | |
| Giai đoạn đầu cần bao nhiêu doanh số làm nền | |
| Chủ yếu được đẩy bằng giá rẻ / quảng cáo / chương trình / đánh giá | |
| Đối thủ có scale nhanh bằng quảng cáo không | |

**Căn chỉnh mục tiêu của bên mình**

| Chỉ số giai đoạn | Giá trị mục tiêu | Căn cứ |
|---|---|---|
| CTR | ≥ 3% | Chuẩn SOP |
| Lượt truy cập | | Suy ngược từ đối thủ |
| Tỷ lệ chuyển đổi đơn | ≥ 1% | Chuẩn SOP |
| ROI thực | ≥ <ngưỡng hòa vốn> | Tính ngưỡng hòa vốn |
| Chi tiêu quảng cáo | | Suy ngược từ đối thủ |
| Tổng số đánh giá có ảnh | | Suy ngược từ đối thủ (**SOP: giai đoạn đầu của link mới nhất định phải liên hệ khách để có ảnh review của người mua**) |
```

> **SOP nói rõ**: giai đoạn đầu của link mới nhất định phải chủ động liên hệ khách, tìm cách có được ảnh review của người mua, việc này giảm rủi ro cho các khoản đầu tư sau. Điều này nên được chuyển thành một **hành động vận hành cụ thể**, chứ không chỉ nằm trên tài liệu.

---

# PART C · Nhịp ngân sách theo khung giờ

SOP 3.6 nói rõ:

> Khi điều chỉnh quảng cáo Shopee đừng thường xuyên tạm dừng, sẽ lãng phí hạn mức miễn phí, cách tốt nhất là ngoài khung giờ vàng thì chỉnh về khoảng 10, tới khung giờ vàng lại chỉnh về ngân sách bình thường.

## C1 · Vì sao là "hạ thấp" chứ không phải "tạm dừng"

| Cách làm | Hậu quả |
|---|---|
| Tạm dừng quảng cáo | **Mất hạn mức traffic hỗ trợ mà sàn cấp cho link mới** |
| Ép ngân sách về mức tối thiểu vẫn chạy được | Chỉ giảm chi tiêu, không kích hoạt việc mất hạn mức |

## C2 · Template phương án nhịp

```markdown
## 3. Nhịp ngân sách theo khung giờ

| Khung giờ (giờ địa phương thị trường mục tiêu) | Giờ Bắc Kinh tương ứng | Cài đặt ngân sách | Lý do |
|---|---|---|---|
| <khung giờ vàng> | | Ngân sách mục tiêu R$ <giá trị> | <đỉnh chuyển đổi> |
| <ngoài khung giờ vàng> | | Mức tối thiểu vẫn chạy được R$ 10 | <ép chi phí, giữ hạn mức> |

**Múi giờ thị trường mục tiêu**: <UTC−3 Brazil / khác>
**Căn cứ xác định khung giờ vàng**: <dữ liệu sàn / kinh nghiệm / quan sát đối thủ>
```

## C3 · Cấu hình tham khảo (Shopee Brazil)

```markdown
### Cấu hình tham khảo · Shopee Brazil

| Khung giờ (giờ Brazil BRT) | Giờ Bắc Kinh tương ứng | Ngân sách |
|---|---|---|
| 00:00 – 09:00 (Brazil từ khuya tới sáng sớm) | 11:00 – 20:00 | R$ 10 (ngủ đông) |
| 09:00 – 24:00 (Brazil từ ban ngày tới khuya) | 20:00 – 11:00 hôm sau | Ngân sách mục tiêu R$ <giá trị> |
```

> ⚠️ **Quy đổi múi giờ bắt buộc phải xác nhận, đừng dựa vào ấn tượng.** Giờ Brazil **chậm hơn giờ Bắc Kinh 11 tiếng** (trong thời gian giờ mùa hè của Brazil là 10 tiếng — Brazil đã bỏ giờ mùa hè từ năm 2019, nhưng vẫn khuyến nghị kiểm tra thực tế).
> Logic quy đổi: 11:00 Bắc Kinh = 00:00 Brazil. Vì vậy "Brazil bắt đầu ngủ đông lúc 0 giờ" tương ứng với "bắt đầu hạ ngân sách lúc 11:00 giờ Bắc Kinh".

## C4 · Quy tắc bổ sung của Mercado Livre

SOP không bao phủ ML, nhưng Mercado Ads của ML có những đặc tính của sàn cần lưu ý:

| Đặc tính | Cách xử lý |
|---|---|
| Ngân sách ngày tối thiểu từ R$ 10 | Mức ngủ đông không được thấp hơn R$ 10 |
| 7 ngày đầu thuật toán có xu hướng tiêu quá tay vào từ khóa rộng | 7 ngày đầu bắt buộc theo dõi thủ công, **đừng đặt "tự động"** |
| Không có từ khóa phủ định ở cấp chiến dịch | Từ khóa phủ định quản lý ở **cấp nhóm quảng cáo** |
| Hỗ trợ hệ số giá thầu theo vị trí hiển thị | Trang kết quả tìm kiếm vs trang chi tiết có thể đặt hệ số riêng |
| Hỗ trợ dayparting | Đặt giá thầu theo khung giờ ngay trên sàn, không cần sửa ngân sách thủ công |

> **Với ML, dùng dayparting của sàn ổn định hơn sửa ngân sách thủ công** — sửa thủ công dễ quên khôi phục.

---

# FINAL OUTPUT STRUCTURE

```markdown
## 1. Tính ngưỡng hòa vốn
### 1.1 Lợi nhuận gộp khả dụng trước quảng cáo
### 1.2 ROAS hòa vốn
### 1.3 ROAS đạt chuẩn
### 1.4 Phân tích độ nhạy ROAS
### 1.5 Hướng xử lý

## 2. Mô hình ngân sách
### 2.1 Mức trần ngân sách tối đa
### 2.2 Khoảng ROI mục tiêu
### 2.3 Chu kỳ test
### 2.4 Mục tiêu theo giai đoạn
### 2.5 Suy ngược nhịp quảng bá của đối thủ        (xuất có điều kiện)

## 3. Nhịp ngân sách theo khung giờ

## 4. Quét tuân thủ đề xuất
(theo G1–G5 của 00_system.md; không vi phạm thì ghi "không vi phạm")

## 5. Các trường bàn giao
- breakeven_roas:
- target_roas_range: []
- max_daily_budget:
- test_window_days: 7
- budget_schedule: {}
- stage_targets: []
```

---

# SELF-CHECK

- [ ] Hoa hồng và hao hụt hoàn hàng tính theo % giá bán, không coi là giá trị cố định
- [ ] Quá trình tính được trình bày đầy đủ, có thể kiểm tra lại
- [ ] Đã tính ROAS hòa vốn và nêu rõ ý nghĩa
- [ ] Đã tính ROAS đạt chuẩn, và **chỉ rõ khoảng chênh so với ngưỡng hòa vốn**
- [ ] Đã xuất bảng độ nhạy ROAS
- [ ] Đã đưa ra đề xuất hướng xử lý
- [ ] Căn cứ phán đoán ngân sách tối đa là quy mô thị trường chứ không phải trực giác
- [ ] ROI mục tiêu không bị đặt sát ngưỡng hòa vốn ngay từ đầu
- [ ] Chu kỳ test là 7 ngày (hoặc đã giải thích vì sao rút ngắn)
- [ ] Mục tiêu theo giai đoạn được đặt tách giai đoạn, không trộn mẫu và hiệu suất vào cùng một giai đoạn
- [ ] Đã kiểm tra quy đổi múi giờ của nhịp theo khung giờ
- [ ] Với tình huống ML đã nhắc dùng dayparting của sàn
- [ ] Cuối đầu ra đã kèm quét tuân thủ đề xuất + các trường bàn giao
