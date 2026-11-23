# Case study · Phân tích ngành hàng Patinete Elétrico (Shopee Brazil)

> **Loại case study**: case study tái lập được · dữ liệu do script mẫu của repo này tạo ra
> **Module sử dụng**: 01 Market Research Agent (gồm toàn bộ quy trình `scripts/`)
> **SOP tương ứng**: 1.1 – 1.6
> **Trọng tâm minh họa**: **chỉ số do script tính, Agent chỉ diễn giải** · tính nhất quán giữa việc cắt theo vùng trũng và giá khả thi theo chi phí

**Điểm đặc biệt của case study này**: dữ liệu **hoàn toàn do script của repo này tạo ra**, nên mỗi bước bạn đều tái lập được trên máy mình và đối chiếu được từng con số. Không phải "case study kiểu kể chuyện".

---

## 1. Cách tái lập

```bash
cd Agents/01_Market_Research_Agent/scripts
python make_sample.py                                              # ① Tạo dữ liệu mẫu
python shaduola_parser.py ../samples/sample_patinete_eletrico.csv   # ② Chuẩn hóa định dạng
python market_metrics.py ../samples/sample_patinete_eletrico.normalized.json \
    --bins 10 --config-fields "công suất,tải trọng,dung lượng"       # ③ Tính chỉ số
```

Toàn bộ đầu ra nằm trong `samples/`. **Mọi con số bên dưới đều đối chiếu được từng mục trong `sample_patinete_eletrico.metrics.md`.**

> ⚠️ Mẫu là **dữ liệu tổng hợp** (`random.seed(20261013)`), dùng để minh họa phương pháp và quy trình tái lập, **không đại diện cho thị trường thật**.

---

## 2. Bối cảnh sản phẩm

| Hạng mục | Nội dung |
|---|---|
| Ngành hàng | Xe trượt điện (dành cho người lớn) |
| Thị trường | Brazil (Shopee BR) |
| Nguồn lực công ty | Có hàng sẵn, có nhà cung cấp ổn định, xử lý được đổi hàng (không sửa chữa) |
| Cấu trúc chi phí | Giá vốn sản phẩm `R$ 780` + vận chuyển chặng cuối `R$ 130` + kho bãi `R$ 25` = **`R$ 935`** |
| Biên lợi nhuận gộp mục tiêu | 32% (hàng cồng kềnh 30–35%) |
| Dự phòng quảng cáo | 5% (hàng cồng kềnh) |

---

## 3. Step 1 · Sàng lọc sơ bộ ngành hàng (SOP 1.1)

### 3.1 Mức độ phù hợp với nguồn hàng

| Hạng mục kiểm tra | Kết luận | Căn cứ |
|---|---|---|
| Có hàng sẵn hoặc hàng sắp về không | ✅ | Có hàng sẵn |
| Có nhà cung cấp ổn định không | ✅ | — |
| Giá vốn có lợi thế không | ⚠️ | **Cần xác nhận**: phải so với giá nhập của người bán top đầu cùng ngành hàng |
| Có hợp với thị trường mục tiêu không | ✅ | Nhu cầu đi lại trong đô thị ở Brazil mạnh |
| Kích thước, cân nặng có hợp với kho bãi và vận chuyển không | ⚠️ | Mỗi chiếc 18 kg / 90×25×110 cm, thuộc hàng cồng kềnh, **cần xác nhận dư chỗ cho hàng cồng kềnh trong kho hiện tại** |
| Có năng lực xử lý hậu mãi / phụ kiện / đổi trả không | ⚠️ | Đổi hàng được, **không sửa chữa** → hậu mãi do lỗi kỹ thuật sẽ chuyển thành trả hàng |

### 3.2 Xác định ngành hàng rủi ro

| # | Chiều đánh giá | Kết luận | Giải thích |
|---|---|---|---|
| 1 | Dễ phát sinh vấn đề khi sử dụng | 🔴 Có | Lắp ráp, sạc pin, chỉnh phanh đều cần thời gian làm quen |
| 2 | Dễ dẫn đến khiếu nại | 🔴 Có | Quãng đường đi được và tải trọng là điểm tranh cãi phổ biến nhất |
| 3 | Chi phí trả hàng cao | 🔴 Có | Hàng cồng kềnh, phí vận chuyển trả hàng cao |
| 4 | Dễ khai khống thông số | 🔴 Có | Quãng đường/tốc độ/tải trọng đều dễ bị thổi phồng |
| 5 | Liên quan sở hữu trí tuệ / rủi ro cấm bán | 🟡 Trung bình | Không bị cấm bán, nhưng cần chú ý từ khóa thương hiệu |
| 6 | Dễ bị phạt điểm | 🟡 Trung bình | Rủi ro tỷ lệ hư hỏng và giao hàng trễ |

**Mức độ rủi ro: 🔴 Rủi ro cao (dính 4 mục)**

### 3.3 Kiểm tra khả năng gánh rủi ro bằng lợi nhuận (bắt buộc với ngành hàng rủi ro cao)

| Hạng mục | Giá trị |
|---|---|
| Giá bán mục tiêu | `R$ 2.200` |
| Lợi nhuận gộp khả dụng trước quảng cáo | `R$ 913,00` (41,5%) |
| Tỷ lệ trả hàng ước tính | 6% |
| Chi phí hậu mãi ước tính / đơn (gồm phân bổ hao hụt do trả hàng) | `R$ 90` |
| **Lợi nhuận gộp ròng sau rủi ro** | `R$ 913 − R$ 110(quảng cáo) − R$ 90 = R$ 713` |
| Biên lợi nhuận gộp sau rủi ro | **32,4%** |
| Có đủ bù rủi ro không | ✅ Có (≥ mục tiêu 32%) |

### 3.4 Kết luận sàng lọc sơ bộ

| # | Hạng mục kết luận | Nội dung |
|---|---|---|
| 1 | Có hợp với nguồn hàng hiện tại của công ty không | ⚠️ Cần xác nhận (lợi thế giá vốn + chỗ kho cho hàng cồng kềnh) |
| 2 | Có lợi thế chuỗi cung ứng không | ⚠️ Cần xác nhận |
| 3 | Có vấn đề về vận chuyển hoặc kho bãi không | ⚠️ Cần xác nhận chỗ kho cho hàng cồng kềnh |
| 4 | Mức độ rủi ro | 🔴 Rủi ro cao (4 mục) |
| 5 | Khả năng gánh rủi ro bằng lợi nhuận của ngành hàng rủi ro cao | ✅ Đủ (32,4%) |
| 6 | Hạn chế của sàn | Không cấm bán; chú ý từ khóa thương hiệu; nên xác nhận có cần chứng nhận không |
| 7 | **Có sang bước phân tích quy mô thị trường không** | ⚠️ **Sang bước tiếp có điều kiện** |

> **Nhận định**: với tiền đề hai điều kiện 「lợi thế giá vốn xác nhận được」 và 「chỗ kho cho hàng cồng kềnh đảm bảo được」 đều thỏa, dữ liệu ủng hộ sang bước tiếp theo.
> Nhờ biên lợi nhuận gộp sau rủi ro đạt 32,4%, khả năng gánh rủi ro bằng lợi nhuận của ngành hàng rủi ro cao này là có —— **đây là lý do duy nhất để làm một ngành hàng rủi ro cao**.

**Danh sách cần xác nhận**
- [ ] So sánh giá nhập với người bán top đầu cùng ngành hàng
- [ ] Dư chỗ cho hàng cồng kềnh trong kho hiện tại
- [ ] Yêu cầu chứng nhận và quy định lưu thông đối với xe trượt điện tại Brazil

---

## 4. Step 2 · Quy mô thị trường (SOP 1.2)

### 4.1 Quy mô

| Chỉ số | Giá trị | Nhận định |
|---|---|---|
| Số sản phẩm trong mẫu | 50 | Đạt cỡ mẫu cơ bản theo SOP |
| Tổng lượng bán tháng | **5.886** | Quy mô đủ lớn |
| Tổng doanh thu tháng | **R$ 12.700.584** | Quy mô đủ lớn |
| Giá trung bình | `R$ 2.238,56` | — |
| Giá trung vị | `R$ 2.252,03` | Gần giá trung bình → **phân bố không lệch** |
| Giá trung bình ngầm định (GMV÷lượng bán) | `R$ 2.157,76` | Thấp hơn giá trung bình số học → phân khúc giá thấp đóng góp nhiều lượng bán hơn |
| Lượng bán tháng trung bình mỗi sản phẩm | **117,7** | Mức độ sôi động của ngành hàng lành mạnh |

**【Nhận định】Quy mô thị trường đủ để chống đỡ khoản đầu tư.**
Tín hiệu bổ sung: giá trung vị ≈ giá trung bình (2.252 vs 2.239) cho thấy phân bố giá đối xứng, không có giá cực thấp hay cực cao kéo lệch giá trung bình; nhưng giá trung bình ngầm định (2.158) thấp hơn giá trung bình → **lượng bán tập trung hơn ở phân khúc giá hơi thấp**, tín hiệu này sẽ được dùng ở Step 4.

### 4.2 Xu hướng bán hàng

⚠️ **Case study này chỉ có dữ liệu chụp nhanh một kỳ, không đánh giá được xu hướng.** 

SOP yêu cầu dựa vào lượng bán tháng và doanh thu tháng để đánh giá "đang trong giai đoạn tăng trưởng/suy giảm", việc này cần so sánh ≥2 kỳ dữ liệu (nên cách nhau 30 ngày). **Dữ liệu một kỳ cho biết "hiện tại lớn cỡ nào", không cho biết "đang lớn lên hay nhỏ đi".**

| Câu hỏi | Kết luận |
|---|---|
| Có ra đơn đều đặn không | Không đủ dữ liệu (chụp nhanh một kỳ) |
| Tăng trưởng / suy giảm | **Không đủ dữ liệu, cần bổ sung dữ liệu kỳ thứ hai** |
| Có phải bùng nổ ngắn hạn không | Không đánh giá được |
| Có theo mùa không | Không đánh giá được |

### 4.3 Hiệu quả sản phẩm mới

| Câu hỏi | Kết luận |
|---|---|
| Sản phẩm mới có ra đơn được không | ⚠️ **Dữ liệu không đáng tin** |

**Nguyên nhân**: bản gốc SOP đã ghi chú "phần này dữ liệu Shaduola không chính xác". `listing_age_days` trong mẫu này do script sinh ngẫu nhiên, chỉ để minh họa định dạng trường, **không có giá trị phân tích** → khối này cần đối chiếu thủ công thời gian đăng bán thực tế.

> **Mục này minh họa một nguyên tắc thiết kế của module**: dữ liệu không đủ thì nói "không đủ dữ liệu", đừng dùng những câu mơ hồ kiểu "cơ hội thị trường chưa rõ ràng" để che lấp vấn đề.

---

## 5. Step 3 · Mức độ tập trung (SOP 1.3)

### 5.1 Mức độ tập trung thương hiệu

| Chỉ số | Giá trị | Ngưỡng | Phán định |
|---|---|---|---|
| Số thương hiệu | **6** | — | — |
| CR3 (doanh thu) | **74,1%** | — | — |
| CR10 | 100,0% | — | ⚠️ **Vô nghĩa** (số chủ thể 6 ≤ 10) |
| HHI | **2.219,7** | > 1800 coi là tập trung cao | 🔴 Tập trung |

> ⚠️ **Script tự động nhắc**: Số chủ thể (6) ≤ n (10), CR10 luôn bằng 100%, không có giá trị tham khảo. Nên chuyển sang dùng CR3 và HHI.
> **Đây là cái bẫy dễ vấp nhất của module này**: thấy "CR10 = 100%" là tưởng "độc quyền hoàn toàn", thực ra chỉ vì không đủ 10 thương hiệu.

**Tỷ trọng số sản phẩm của thương hiệu top đầu**

| Thương hiệu | Tỷ trọng doanh thu | Tỷ trọng lượng bán | Tỷ trọng số sản phẩm | Phân loại |
|---|---|---|---|---|
| Generic | 29,9% | 30,5% | 24,0% | No-brand, dựa vào số lượng sản phẩm |
| Sem marca | 28,7% | 27,4% | 30,0% | No-brand, dựa vào số lượng sản phẩm |
| Outras | 15,5% | 15,3% | 20,0% | No-brand |
| MarcaA | 12,5% | 13,5% | 12,0% | Có thương hiệu, tỷ trọng tương đương |
| MarcaB | 9,6% | 8,5% | 8,0% | Có thương hiệu |
| MarcaC | 3,9% | 4,9% | 6,0% | Có thương hiệu |

**【Nhận định】Không có độc quyền thương hiệu.**

CR3 = 74,1% trông có vẻ rất cao, nhưng tách ra mà xem: **ba vị trí đầu đều là hàng no-brand (Generic / Sem marca / Outras), cộng lại chiếm 74,1% doanh thu.** Các thương hiệu thật sự (MarcaA/B/C) cộng lại chỉ 26%.

> **Đây là ví dụ điển hình của "CR cao nhưng không tạo thành rào cản thương hiệu".** Nếu chỉ nhìn CR3 = 74,1% mà kết luận "mức độ tập trung thương hiệu quá cao, cần thận trọng khi vào" thì sẽ đánh giá sai hoàn toàn.
> **Cách đọc đúng**: CR cao chỉ cho thấy "thị phần nhóm top đầu tập trung", còn phải xem **nhóm top đầu là ai** —— là thương hiệu hay no-brand. No-brand chiếm nhóm đầu → người mua không chuộng thương hiệu, mà chuộng sản phẩm và giá → **shop mới vẫn còn dư địa**.

No-brand cộng lại chiếm 74,1% và tỷ trọng số sản phẩm cũng cao → thị trường đang ở trạng thái **cạnh tranh giữa hàng no-brand**, rào cản thương hiệu thấp.

### 5.2 Mức độ tập trung người bán

| Chỉ số | Giá trị | Phán định |
|---|---|---|
| Số người bán | **34** | Số lượng người bán dồi dào |
| CR3 (doanh thu) | **46,8%** | Trung bình |
| **CR10 (doanh thu)** | **71,5%** | 🟡 Hơi cao |
| CR10 (lượng bán) | 70,6% | Khớp với tính theo doanh thu |
| HHI | **951,5** | < 1500 → tập trung trung bình thấp |

| # | Người bán | Tỷ trọng doanh thu | Tỷ trọng lượng bán | Tỷ trọng số sản phẩm | Loại |
|---|---|---|---|---|---|
| 1 | LojaGrande1 | 21,3% | 21,4% | 16,0% | Loại hiệu suất (thị phần > tỷ trọng số sản phẩm) |
| 2 | LojaGrande3 | 17,0% | 16,1% | 10,0% | Loại hiệu suất |
| 3 | LojaGrande2 | 8,5% | 9,7% | 12,0% | **Loại chiếm chỗ** (tỷ trọng số sản phẩm > tỷ trọng doanh thu) |
| 4–10 | Người bán vừa và nhỏ | Cộng lại 24,7% | — | Mỗi bên 2% | Một người một sản phẩm |

**【Nhận định】Có mức độ tập trung người bán trung bình, nhưng chưa tạo thành độc quyền.**

Chỉ số đọc then chốt: **tỷ lệ giữa tỷ trọng doanh thu và tỷ trọng số sản phẩm**:

| Người bán | Tỷ trọng doanh thu ÷ tỷ trọng số sản phẩm | Diễn giải |
|---|---|---|
| LojaGrande1 | 21,3 / 16,0 = **1,33** | Hiệu suất cao hơn mức trung bình |
| LojaGrande3 | 17,0 / 10,0 = **1,70** | **Hiệu suất cao nhất** |
| LojaGrande2 | 8,5 / 12,0 = **0,71** | **Dựa vào phủ sản phẩm để chiếm chỗ, hiệu suất mỗi SKU thấp** |

> **LojaGrande2 là người bán đáng chú ý nhất**: tỷ trọng doanh thu 8,5% trông không nhỏ, nhưng tỷ trọng số sản phẩm lên tới 12% —— cho thấy đây là **thị phần chồng lên nhờ số lượng**, hiệu suất mỗi SKU lại thấp hơn mức trung bình.
> **Loại người bán này không phải rào cản, mà là "đối tượng có thể vượt qua"**. Ngược lại, LojaGrande3 dùng 10% số sản phẩm để lấy 17% doanh thu, đó mới là đối thủ thật sự cần nghiên cứu.

**CR10 = 71,5% nhưng phần đuôi có rất nhiều người bán một người một sản phẩm** → phần đuôi dài vẫn sôi động, sản phẩm mới vào sẽ không bị chèn ép ra ngoài.

---

## 6. Step 4 · Dải giá (SOP 1.4)

### 6.1 Chia bin và dò vùng trũng

| Khoảng | Phân khúc giá | Số sản phẩm | Tổng lượng bán | Đường cong | Lượng bán TB mỗi sản phẩm |
|---|---|---|---|---|---|
| 1 | R$ 1.500,59–1.663,44 | 7 | 499 | ████████ | 71,3 |
| 2 | R$ 1.663,44–1.826,28 | 7 | 799 | ██████████████ | 114,1 |
| **3** | **R$ 1.826,28–1.989,13** | 4 | **618** | ███████████ | 154,5 |
| 4 | R$ 1.989,13–2.151,98 | 5 | **1.120** | ████████████████████ | **224,0** |
| 5 | R$ 2.151,98–2.314,83 | 5 | 999 | █████████████████ | 199,8 |
| 6 | R$ 2.314,82–2.477,67 | 5 | 875 | ███████████████ | 175,0 |
| 7 | R$ 2.477,67–2.640,52 | 5 | 552 | █████████ | 110,4 |
| 8 | R$ 2.640,52–2.803,37 | 5 | 241 | ████ | 48,2 |
| **9** | **R$ 2.803,37–2.966,21** | 2 | **56** | █ | 28,0 |
| 10 | R$ 2.966,21–3.129,06 | 5 | 127 | ██ | 25,4 |

**Kết quả dò vùng trũng** (ngưỡng: mức giảm ≥ 15%)

| Thứ tự bin | Ranh giới giá | Mức giảm | Dùng làm ranh giới dải giá |
|---|---|---|---|
| **3** | **R$ 1.989,13** | 22,7% | ✅ |
| **9** | **R$ 2.966,21** | 55,9% | ✅ |

> **Về câu hỏi "vì sao không làm mượt"**: bin 3 (618) là một điểm thấp cục bộ rõ rệt so với bin 2 (799) và bin 4 (1.120), mức giảm 22,7%.
> Nhưng nếu làm trung bình trượt 3 điểm, bin 3 sẽ thành (799+618+1120)/3 = **846**, bin 2 thành 639, bin 4 thành 912 —— đường cong biến thành tăng đơn điệu, **vùng trũng này bị xóa sạch**, ranh giới dải giá cũng mất luôn.
> Đây là lý do script mặc định không làm mượt, chi tiết xem [`scripts/README.md`](../scripts/README.md).

### 6.2 Dải giá đề xuất (cắt theo vùng trũng)

| Dải giá | Khoảng giá | Số sản phẩm | Tổng lượng bán | Lượng bán TB mỗi sản phẩm |
|---|---|---|---|---|
| #1 | R$ 1.500,59–1.989,13 | 18 | 1.916 | 106,4 |
| **#2** | **R$ 1.989,13–2.966,21** | 27 | **3.843** | **142,3** |
| #3 | R$ 2.966,21–3.129,06 | 5 | 127 | 25,4 |

### 6.3 Đánh giá chéo bốn điều kiện cho dải giá mục tiêu

| Điều kiện | Nhận định | Căn cứ |
|---|---|---|
| **① Lượng bán cao** | ✅ | Dải #2 chiếm **65,3%** tổng lượng bán (3.843 ÷ 5.886) |
| **② Lượng bán trung bình cao** | ✅ | Lượng bán TB **142,3** vs trung bình chung 117,7 → **gấp 1,21 lần** |
| **③ Sản phẩm của công ty có lãi** | ✅ | Xem phần tính toán bên dưới |
| **④ Đối thủ không quá mạnh** | ⚠️ Một phần | Dải #2 có 27 sản phẩm (chiếm 54%), cạnh tranh không yếu; nhưng CR3 chỉ 46,8%, không có ai độc quyền |

#### Tính toán cho điều kiện ③

Dùng công thức định giá để tính ngược "cận dưới của mức giá mục tiêu":

```
P = (giá vốn sản phẩm + vận chuyển chặng cuối + phí kho) ÷ (1 − tỷ lệ hoa hồng − tỷ lệ quảng cáo − tỷ lệ trả hàng − biên lợi nhuận gộp mục tiêu)
  = 935 ÷ (1 − 0,14 − 0,05 − 0,02 − 0,32)
  = 935 ÷ 0,47
  = R$ 1.989,36
```

**Còn cận dưới của dải giá #2 do dò vùng trũng đưa ra là R$ 1.989,13 —— hai con số chênh nhau R$ 0,23.**

> **Sự trùng khớp 0,23 real này không phải cố tình làm cho khớp, mà là kiểm chứng chéo của hai cách suy luận độc lập:**
> - Dò vùng trũng: thuần toán học (điểm thấp cục bộ của đường cong lượng bán)
> - Công thức định giá: thuần tài chính (chi phí + các loại phí + biên lợi nhuận gộp mục tiêu)
>
> **Hai con đường cùng chỉ về một mức giá, cho thấy lựa chọn dải giá này đồng thời thỏa "cấu trúc thị trường" và "khả thi về chi phí".**
> Đây là một tín hiệu rất có giá trị —— khi hai bên chênh lệch lớn (ví dụ dải tối ưu về toán học là R$ 1.600, nhưng giá khả thi theo chi phí là R$ 2.100), nghĩa là **phân khúc giá bán chạy nhất trên thị trường thì bạn không làm ra lãi**, khi đó bắt buộc phải xem lại cấu hình sản phẩm (giảm chi phí) hoặc bỏ cuộc.

#### Lý do loại dải giá #3

Dải #3 (R$ 2.966–3.129) tuy số liệu lượng bán trung bình không đẹp (25,4), nhưng cần lưu ý **cỡ mẫu của nó chỉ có 5 sản phẩm**. SOP có nói "nếu sau vị trí 50 lượng bán không giảm đột ngột thì có thể mở rộng mẫu lên 100" —— phân khúc giá cao có ít sản phẩm, **kết luận dễ bị ảnh hưởng bởi trường hợp cá biệt**.

**【Nhận định】Loại #3 khỏi vai trò chiến trường chính, nhưng có thể dùng làm tham chiếu giá cho SKU cấu hình cao.**

### 6.4 Khoảng giá mục tiêu

| Hạng mục | Gợi ý |
|---|---|
| **Khoảng giá mục tiêu khuyến nghị** | **`R$ 1.989 – R$ 2.966`** (dải #2) |
| **Mức giá chủ lực** | **`R$ 2.100 – R$ 2.300`** (bin 4+5, cộng lại 2.119 lượng bán, là hai đỉnh lượng bán trong dải này) |
| Giá bán thường ngày | `R$ 2.199` |
| Giá chương trình | `R$ 1.999` |
| Giá sau voucher | `R$ 1.949` (sát cận dưới dải giá, không phá vỡ ngưỡng chi phí R$ 1.989) |
| Biên lợi nhuận gộp mục tiêu | 32% |
| SKU kéo traffic | Nên đặt mẫu cấu hình thấp 350W ở R$ 1.799 (rơi vào dải #1, dùng để kéo click) |

> **Chú ý quan hệ giữa giá chương trình và ngưỡng chi phí**: giá chương trình R$ 1.999 đã ép sát ngưỡng khả thi theo chi phí 1.989, **giá sau voucher 1.949 sẽ thấp hơn 1.989** —— nghĩa là đơn dùng voucher có thể không có lãi.
> **Điều này chấp nhận được**: voucher là công cụ kéo chuyển đổi, không phải giá thường ngày. Nhưng nếu giá sau voucher là trạng thái **lâu dài**, nghĩa là mô hình định giá không đứng vững, cần tính lại chi phí hoặc điều chỉnh cấu hình.

---

## 7. Step 5 · Tổ hợp cấu hình (SOP 1.5)

### 7.1 Công suất

| Giá trị cấu hình | Số sản phẩm | Tỷ trọng số lượng | Tổng lượng bán | Tỷ trọng lượng bán | Lượng bán TB | Đánh giá |
|---|---|---|---|---|---|---|
| **500W** | 19 | 38,0% | **3.612** | **61,4%** | **190,1** | Tổng lượng bán cao→nhu cầu lớn; Hiệu suất mỗi SKU cao |
| 350W | 14 | 28,0% | 1.298 | 22,1% | 92,7 | Bình thường |
| 800W | 17 | 34,0% | 976 | 16,6% | 57,4 | Bình thường |

> **800W là dòng ngược trực giác nhất**: số sản phẩm nhiều nhất (17 sản phẩm, 34%), nhưng tỷ trọng lượng bán thấp nhất (16,6%), lượng bán TB chỉ 57,4 (bằng 0,49 lần trung bình chung).
> **Cho thấy thị trường coi 800W là "cấu hình giá cao" chứ không phải "nhu cầu hiệu năng"** —— bán không chạy không phải vì công suất không đủ, mà vì đắt.
> **Kết luận**: đừng lấy 800W làm SKU chủ lực, nó là ứng viên cho "SKU cấu hình cao để nâng giá trị đơn hàng", không phải chiến trường chính.

### 7.2 Tải trọng

| Giá trị cấu hình | Số sản phẩm | Tỷ trọng số lượng | Tổng lượng bán | Tỷ trọng lượng bán | Lượng bán TB | Đánh giá |
|---|---|---|---|---|---|---|
| 150kg | 32 | **64,0%** | 3.740 | 63,5% | 116,9 | Tổng lượng bán cao→nhu cầu lớn; Cấu hình phổ biến→cạnh tranh gắt; Thị trường lớn nhưng cạnh tranh gắt |
| 100kg | 14 | 28,0% | 1.298 | 22,1% | 92,7 | Bình thường |
| **200kg** | **4** | **8,0%** | 848 | 14,4% | **212,0** | Hiệu suất mỗi SKU cao; **★Cấu hình cơ hội (ít sản phẩm nhưng hiệu suất cao)** |

### 7.3 ⭐ Kiểm tra then chốt cho cấu hình cơ hội: có bị nhóm top đầu chiếm không?

SOP yêu cầu rõ: "**Ít sản phẩm nhưng lượng bán trung bình cao, cho thấy có thể là cấu hình cơ hội, nhưng phải xem tiếp có bị một số ít người bán top đầu chiếm không.**"

**Chủ sở hữu 4 sản phẩm 200kg:**

| Người bán sở hữu | Giá | Lượng bán tháng | Có phải người bán Top3 không |
|---|---|---|---|
| LojaGrande1 | R$ 1.985,12 | 138 | ✅ Có (doanh thu hạng 1) |
| LojaGrande2 | R$ 1.984,19 | 249 | ✅ Có (doanh thu hạng 3) |
| LojaPequena05 | R$ 1.944,98 | 138 | ❌ Không |
| **LojaPequena15** | R$ 2.069,39 | **323** | ❌ Không |

**【Nhận định】Cấu hình cơ hội là có thật, chưa bị nhóm top đầu độc quyền.**

Ba căn cứ:

1. **Trong 4 sản phẩm chỉ có 2 sản phẩm nằm trong tay người bán Top3** —— nhóm đầu chiếm một nửa, nhưng chưa chiếm hết
2. **Listing có lượng bán cao nhất (323) đến từ người bán vừa và nhỏ LojaPequena15** —— cho thấy cấu hình này thắng **nhờ bản thân cấu hình, không nhờ trọng số của shop**
3. **Nhóm đầu chỉ chiếm một nửa số sản phẩm** —— cho thấy họ không phủ hàng loạt cấu hình này, đây là **khoảng trống cấu hình chứ không phải cuộc chiến giá**

> **Căn cứ thứ 2 là bằng chứng then chốt.** Nếu toàn bộ sản phẩm top đầu của cấu hình 200kg đều thuộc LojaGrande1, thì đó có thể là kết quả "nhóm đầu dùng trọng số shop để đẩy cứng", shop mới không sao chép được.
> Nhưng lượng bán cao nhất lại xuất hiện ở một người bán nhỏ một người một sản phẩm —— **điều này chứng minh thị trường có nhu cầu với chính cấu hình này**, chứ không phải ưu ái một shop nào đó.
>
> **Đây chính là khác biệt giữa "cấu hình cơ hội" và "cái bẫy trông giống cơ hội" mà SOP nói tới.**

### 7.4 Dung lượng

| Giá trị cấu hình | Số sản phẩm | Tỷ trọng số lượng | Tổng lượng bán | Tỷ trọng lượng bán | Lượng bán TB | Đánh giá |
|---|---|---|---|---|---|---|
| 12Ah | 36 | 72,0% | 4.588 | 78,0% | 127,4 | Tổng lượng bán cao→nhu cầu lớn |
| 10Ah | 14 | 28,0% | 1.298 | 22,1% | 92,7 | Bình thường |

> **Chiều này có lượng thông tin thấp nhất** (chỉ có 2 giá trị, và gần như trùng khớp với các nấc giá). **Khi chiều cấu hình có quá ít giá trị, giá trị của bảng chéo sẽ giảm** —— khi nhận định phải ý thức được điều này, đừng cố đọc ra ý nghĩa.

### 7.5 Tổ hợp cấu hình khuyến nghị

| Chiều | Giá trị khuyến nghị | Căn cứ |
|---|---|---|
| Công suất | **500W** | Tỷ trọng lượng bán 61,4% + lượng bán TB 190,1 (gấp 1,62 lần trung bình) |
| **Tải trọng** | **200kg** ⭐ | **Cấu hình cơ hội**: chỉ 4 sản phẩm nhưng lượng bán TB 212,0 (gấp 1,80 lần trung bình), và chưa bị nhóm top đầu độc quyền |
| Dung lượng pin | 12Ah | Tỷ trọng lượng bán 78%, là cấu hình phổ biến |
| Giá | R$ 2.100–2.300 | Hai đỉnh lượng bán trong dải giá #2 |

**Đối chiếu năm điều kiện**

| Điều kiện | Có thỏa không | Giải thích |
|---|---|---|
| Tổng lượng bán cao | ✅ | 500W chiếm 61,4% lượng bán; dải #2 chiếm 65,3% |
| Lượng bán trung bình cao | ✅ | Lượng bán TB của cấu hình cơ hội 212,0 = gấp 1,80 lần trung bình chung |
| Công ty làm được | ⚠️ | **Cần xác nhận nhà cung cấp linh kiện chịu lực có hỗ trợ quy cách 200kg không** |
| Lợi nhuận chấp nhận được | ✅ | Biên lợi nhuận gộp sau rủi ro 32,4% (cùng phân khúc giá) |
| Hậu mãi kiểm soát được | ⚠️ | Tăng tải trọng sẽ làm tăng rủi ro hậu mãi liên quan đến an toàn, cần xác nhận năng lực hậu mãi |

> **Tổ hợp "500W + 200kg" là đầu ra cốt lõi của case study này.**
> Logic của nó là: **dùng cấu hình phổ biến (500W) để đảm bảo nhu cầu, dùng cấu hình cơ hội (200kg) để tạo khác biệt.**
> Điều này trả lời đúng một nửa câu kết luận mà SOP 1.7 cần —— "điểm bán hàng chủ lực là gì": **"động cơ 500W + tải trọng 200kg"**.
> Mà 200kg trên thị trường chỉ có 4 sản phẩm cạnh tranh, là vị trí **cạnh tranh thấp nhu cầu cao** hiếm có.

---

## 8. Step 6 · Đối thủ và nhịp độ đẩy sản phẩm

(Case study này dùng dữ liệu do script tạo ra, không có link đối thủ thật. Mục này đưa ra **phương pháp và cấu trúc cần điền**.)

| Hạng mục | Kết luận suy ngược |
|---|---|
| Listing mới mất bao lâu để lên đơn | Cần điền (cần so sánh thời gian đăng bán của đối thủ + lượng bán hiện tại) |
| Cần bao nhiêu đánh giá nền trước khi lên đơn | Cần điền (SOP: giai đoạn đầu của listing mới nhất định phải liên hệ khách để lại đánh giá kèm ảnh) |
| Cần bao nhiêu lượng bán làm nền trước khi lên đơn | Tham khảo: lượng bán TB của dải #2 là 142,3/tháng, mục tiêu đạt 50% tức **khoảng 71 đơn/tháng** |
| Có dựa vào quảng cáo để scale không | Cần điền |

**Điểm cơ hội của bên mình**

| Điểm cơ hội | Căn cứ |
|---|---|
| **Khác biệt hóa bằng tải trọng 200kg** | Chỉ 4 sản phẩm cạnh tranh, lượng bán TB gấp 1,80 lần mức chung, và chưa bị nhóm top đầu độc quyền |
| **Trực quan hóa khả năng leo dốc** | Đánh giá tiêu cực/đối thủ thường không ghi điều kiện thử nghiệm → bên mình chủ động ghi rõ giới hạn lại tạo được niềm tin |

**Điểm rủi ro của bên mình**

| Điểm rủi ro | Căn cứ |
|---|---|
| Hụt kỳ vọng về quãng đường đi được | Sau khi tăng tải trọng, quãng đường thực tế sẽ giảm, **bắt buộc ghi rõ điều kiện thử nghiệm** (cân nặng/mặt đường/tốc độ) |
| Hậu mãi liên quan đến an toàn | Tải trọng 200kg liên quan đến an toàn, **nội dung listing và hướng dẫn sử dụng bắt buộc nêu giới hạn** (dốc thoải, một người lái) |
| Rào cản lắp ráp | Lắp ráp hàng cồng kềnh là nguyên nhân trả hàng thường gặp, cần bổ sung hướng dẫn lắp ráp |

> Hai mục sau tương ứng trực tiếp với phát hiện "đánh giá tiêu cực khắc phục được 84,6%" trong [`07 Review Analysis`](../../07_Review_Analysis_Agent/examples/electric_scooter_reviews.md) —— **điểm rủi ro phải được chặn bằng nội dung ngay khi đăng bán, chứ không đợi đánh giá tiêu cực xuất hiện rồi mới vá.**

---

## 9. Quét tuân thủ phân tích

`Quét tuân thủ phân tích: không vi phạm`

(Không bịa dữ liệu, không thổi phồng cơ hội, không quyết định thay con người, không gợi ý lách quy định, không phỏng đoán thật giả của dữ liệu đối thủ. Mọi giá trị đều lấy từ đầu ra của script và tái lập được.)

---

## 10. Các trường bàn giao cho 02 Product Strategy

```yaml
target_price_range: [1989.13, 2966.21]
main_price_zone: [2100, 2300]

price_band_analysis:
  band_1: {range: [1500.59, 1989.13], items: 18, sales: 1916, avg_sales: 106.4, role: "Phân khúc kéo traffic"}
  band_2: {range: [1989.13, 2966.21], items: 27, sales: 3843, avg_sales: 142.3, role: "Chiến trường chính"}
  band_3: {range: [2966.21, 3129.06], items: 5,  sales: 127,  avg_sales: 25.4,  role: "Tham chiếu cấu hình cao, mẫu chỉ có 5 sản phẩm"}

cost_floor_price: 1989.36          # Giá khả thi thấp nhất tính ngược từ biên lợi nhuận gộp 32% + quảng cáo 5%
note_convergence: "Cận dưới vùng trũng 1989.13 và giá khả thi theo chi phí 1989.36 chênh 0.23, hai cách suy luận độc lập trùng khớp"

recommended_config:
  power: "500W"                     # Tỷ trọng lượng bán 61.4%, lượng bán TB gấp 1.62 lần trung bình
  load: "200kg"                     # ★Cấu hình cơ hội, lượng bán TB gấp 1.80 lần trung bình
  capacity: "12Ah"
mainstream_config: {power: "500W", load: "150kg", capacity: "12Ah"}
opportunity_config:
  value: "200kg"
  evidence: "4 sản phẩm, lượng bán TB 212.0 (gấp 1.80 lần trung bình chung), người bán Top3 chỉ chiếm 2/4, lượng bán cao nhất đến từ người bán vừa và nhỏ"
  differentiation: "Động cơ 500W + tải trọng 200kg —— vị trí cạnh tranh thấp nhu cầu cao"

brand_barrier: low                  # CR3 74.1% nhưng ba vị trí đầu đều là no-brand → người mua không chuộng thương hiệu
seller_barrier: medium              # CR10 71.5%, nhưng phần đuôi sôi động, LojaGrande2 thuộc loại chiếm chỗ

competitor_weakness:
  - "Phân khúc 800W có nhiều sản phẩm nhất nhưng lượng bán TB thấp nhất (0.49 lần), cho thấy cấu hình giá cao bán không chạy"
  - "Đối thủ thường không ghi điều kiện thử nghiệm quãng đường/tải trọng → bên mình ghi rõ điều kiện sẽ tạo được niềm tin"

competitor_review_insights: []      # Cần kết nối đánh giá thật, giao cho 07

benchmark_for_launch:
  days_to_ramp: null                # Cần điền
  reviews_needed_before_ramp: null  # Cần điền
  sales_needed_before_ramp: 71      # 50% lượng bán TB của dải #2
  ad_dependency: null               # Cần điền

pending_confirmations:
  - "So sánh giá nhập với người bán top đầu"
  - "Dư chỗ kho cho hàng cồng kềnh"
  - "Nhà cung cấp linh kiện chịu lực có hỗ trợ 200kg không"
  - "Yêu cầu chứng nhận và quy định lưu thông xe trượt điện tại Brazil"
  - "Dữ liệu kỳ thứ hai (để đánh giá xu hướng)"
  - "Link đối thủ thật và dữ liệu quảng bá"
```

---

## 11. Case study này chứng minh điều gì

| Kết luận | Bằng chứng |
|---|---|
| **Chỉ số do script tính, Agent chỉ diễn giải** | Mọi con số đều tái lập được bằng ba lệnh; đầu ra của Agent là nhận định chứ không phải tính toán |
| **CR cao ≠ độc quyền** | CR3 thương hiệu = 74,1% trông cao, nhưng ba vị trí đầu đều là no-brand → người mua không chuộng thương hiệu, shop mới vẫn còn dư địa |
| **Phải xem tỷ lệ giữa thị phần và số sản phẩm** | LojaGrande2 có doanh thu 8,5% nhưng số sản phẩm chiếm 12% → **loại chiếm chỗ chứ không phải loại hiệu suất**, là đối tượng có thể vượt qua |
| **Vùng trũng không được làm mượt** | Vùng trũng ở bin 3 (mức giảm 22,7%) biến mất sau trung bình trượt 3 điểm → mất ranh giới dải giá |
| **Dải tối ưu về toán học và giá khả thi theo chi phí cần được kiểm chứng chéo** | Cận dưới vùng trũng 1.989,13 và giá khả thi theo chi phí 1.989,36 chênh R$ 0,23 —— hai con đường độc lập trùng khớp |
| **"Cấu hình cơ hội" bắt buộc kiểm tra nhóm top đầu có nắm giữ không** | 200kg chỉ có 4 sản phẩm cạnh tranh, và **listing có lượng bán cao nhất đến từ người bán vừa và nhỏ** → thắng nhờ cấu hình chứ không nhờ trọng số shop |
| **Chiều có quá ít giá trị thì giá trị thấp** | Chiều dung lượng chỉ có 2 giá trị và trùng khớp với nấc giá → lượng thông tin thấp nhất, không nên cố đọc |
| **Dữ liệu một kỳ không đánh giá được xu hướng** | SOP yêu cầu xem tăng trưởng/suy giảm, nhưng ảnh chụp nhanh chỉ cho biết "hiện tại lớn cỡ nào" |
| **Thiếu dữ liệu thì phải nói thẳng** | Hai mục hiệu quả sản phẩm mới và xu hướng bán hàng đều ghi rõ "không đủ dữ liệu", không dùng câu mơ hồ để che lấp |
| **Phải chặn rủi ro đã biết ngay trước khi đăng bán** | Ba điểm rủi ro quãng đường/tải trọng/lắp ráp được nhận diện ngay ở giai đoạn phân tích, đưa vào nội dung listing thay vì đợi đánh giá tiêu cực |

---

**File liên quan**: [Giới thiệu module](../README.md) · [Giải thích script](../scripts/README.md) · [Giải thích dữ liệu mẫu](../samples/README.md) · [Prompt sàng lọc sơ bộ](../prompts/01_category_precheck.md) · [Prompt phân tích thị trường](../prompts/02_market_analysis.md) · **Bước sau**: [02 Product Strategy](../../02_Product_Strategy_Agent/)
