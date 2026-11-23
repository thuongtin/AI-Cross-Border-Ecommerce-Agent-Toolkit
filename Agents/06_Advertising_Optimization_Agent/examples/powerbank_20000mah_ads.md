# Case study · Chẩn đoán quảng cáo Carregador Portátil 20000mAh 45W (Shopee Brazil)

> **Loại case**: dữ liệu thật · đã ẩn danh
> **Module sử dụng**: 06 Advertising Optimization Agent
> **SOP tương ứng**: 3.5 Logic chạy quảng cáo · 3.6 Logic điều chỉnh quảng cáo
> **Điểm minh họa chính**: đủ cả bốn loại triệu chứng phễu · **"sửa CTR lại càng lỗ"** · tính ngưỡng hòa vốn

**Vì sao chọn case này**: trong bộ dữ liệu thật này, bốn nhóm quảng cáo vừa khéo bao phủ **toàn bộ bốn loại triệu chứng** của SOP 3.6 — một mẫu chuẩn sách giáo khoa hiếm có. Quan trọng hơn, nó lật đổ một trực giác mà gần như người vận hành nào cũng có: **nhóm quảng cáo có CTR tệ nhất chưa chắc là nhóm nên sửa nhất.**

---

## I. Bối cảnh sản phẩm và chi phí

Cùng sản phẩm với [`Agents/03.../examples/powerbank_20000mah.md`](../../03_Listing_Creative_Agent/examples/powerbank_20000mah.md).

| Hạng mục | Giá trị |
|---|---|
| Sản phẩm | Sạc dự phòng sạc nhanh 20000mAh 45W, có màn hình hiển thị số, 3 cổng ra |
| Giá bán | `R$ 113,40` |
| Chu kỳ test | 7 ngày |
| Sàn | Shopee Brazil |

### Cấu trúc chi phí (dùng để tính ngưỡng hòa vốn)

| Hạng mục | Số tiền | % giá bán |
|---|---|---|
| Giá bán | `R$ 113,40` | 100% |
| Giá vốn + vận chuyển chặng cuối + phí kho | `R$ 55,00` | 48,5% |
| Hoa hồng sàn (14%) | `R$ 15,88` | 14,0% |
| Hao hụt hoàn hàng (2%) | `R$ 2,27` | 2,0% |
| **Lợi nhuận gộp khả dụng trước quảng cáo** | **`R$ 40,26`** | **35,5%** |

```
ROAS hòa vốn = 113,40 ÷ 40,26 = 2,82
```

> **Nói con số này trước**: nhóm quảng cáo nào có ROAS dưới **2,82** thì bán mỗi đơn là lỗ một đơn — dù CTR và tỷ lệ chuyển đổi của nó đẹp tới đâu.

---

## II. Dữ liệu gốc

| Nhóm QC | Từ khóa | Khớp | Hiển thị | Click | CTR | Thêm giỏ | Tỷ lệ thêm giỏ | Đơn | Tỷ lệ chuyển đổi | Chi phí | CPC | CPA | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **A** | `carregador portátil` | Rộng | 48.200 | 675 | **1,40%** | 42 | **6,22%** | 3 | **0,44%** | R$ 210,60 | 0,31 | 70,20 | **1,62** |
| **B** | `carregador 20000mah 45w` | Chính xác | 15.400 | 672 | 4,36% | 29 | **4,32%** | 2 | **0,30%** | R$ 168,00 | 0,25 | 84,00 | **1,35** |
| **C** | `bateria externa viagem` | Ngữ cảnh | 9.150 | 393 | 4,30% | 39 | 9,92% | 2 | **0,51%** | R$ 133,62 | 0,34 | 66,81 | **1,70** |
| **D** | `power bank turbo` | Đối thủ | 6.300 | 277 | 4,40% | 31 | 11,19% | 4 | 1,44% | R$ 166,20 | **0,60** | 41,55 | 2,73 |
| **Tổng** | — | — | **79.050** | **2.017** | **2,55%** | **141** | **6,99%** | **11** | **0,55%** | **R$ 678,42** | 0,34 | 61,67 | **1,84** |

**Đối chiếu đường chuẩn**

| Chỉ số | Thực tế | Chuẩn | Đánh giá |
|---|---|---|---|
| CTR tổng | 2,55% | 3–5% | ❌ Hơi thấp hơn mức sàn |
| Tỷ lệ thêm giỏ tổng | 6,99% | > 8% | ❌ Thấp hơn chuẩn |
| **Tỷ lệ chuyển đổi tổng** | **0,55%** | **> 1%** | ❌ **Chỉ bằng một nửa chuẩn** |
| ROAS tổng | 1,84 | ≥ 2,82 | ❌ Lỗ |

**Đóng góp ròng tổng**: `R$ 40,26 × 11 − R$ 678,42 = **−R$ 235,56**`

> Một tuần lỗ **R$ 235,56**.

---

## III. Chẩn đoán bốn nhóm quảng cáo

### Nhóm quảng cáo A · `carregador portátil` (khớp rộng)

| Bước | Hạng mục kiểm tra | Chuẩn | Thực tế | Đạt |
|---|---|---|---|---|
| 1 | CTR | 3–5% | 1,40% | ❌ |
| 2 | Tỷ lệ thêm giỏ | > 8% | 6,22% | ❌ |
| 3 | Tỷ lệ chuyển đổi | > 1% | 0,44% | ❌ |
| 4 | ROAS | ≥ 2,82 | 1,62 | ❌ |

**Kết luận**: **cả ba khâu đều không đạt** — không khớp với bất kỳ loại đơn lẻ nào trong bốn loại.

**Đây là tình huống khung bốn loại không bao phủ được.** Khi CTR, tỷ lệ thêm giỏ, tỷ lệ chuyển đổi **cùng lúc** không đạt, nguyên nhân không nằm ở một tài sản đơn lẻ nào (không phải ảnh chính kém, cũng không phải trang chi tiết kém), mà nằm ở **chính traffic**:

> **Nguyên nhân gốc: từ khóa khớp rộng quá rộng, traffic mang về không khớp với sản phẩm.**
> Người được dẫn vào vốn dĩ không phải người muốn mua sạc dự phòng sạc nhanh 20000mAh — nên họ không click (CTR thấp), click vào cũng không thấy hấp dẫn (thêm giỏ thấp), thêm giỏ rồi cũng không mua (chuyển đổi thấp).

**Hành động**:

| # | Hành động | Đối tượng | Căn cứ | Kỳ vọng | Ưu tiên |
|---|---|---|---|---|---|
| 1 | **Thu hẹp kiểu khớp**: đổi `carregador portátil` từ khớp rộng sang khớp chính xác, hoặc thêm từ khóa phủ định để loại các từ không mục tiêu như `cabo` `fonte` `adaptador` | Nhóm A | Cả ba khâu cùng thấp = traffic không chính xác | Lượng click giảm nhưng chất lượng tăng | 🔴 P0 |
| 2 | Chuyển ngân sách nhóm A sang nhóm D (nhóm duy nhất có phễu khỏe) | Phân bổ ngân sách | Xem phần phân bổ lại ngân sách bên dưới | Xem bên dưới | 🔴 P0 |
| 3 | Tối ưu ảnh chính (thứ yếu) | Module 04 | CTR 1,40% đúng là cũng thấp | CTR tăng nhẹ | 🟡 P1 |

**Vòng này dứt khoát không động vào**: trang chi tiết (bản thân traffic của nhóm A đã không chính xác, lúc này tối ưu trang chi tiết là tối ưu cho một vấn đề vốn không đón được đúng traffic).

---

### Nhóm quảng cáo B · `carregador 20000mah 45w` (khớp chính xác)

| Bước | Hạng mục kiểm tra | Chuẩn | Thực tế | Đạt |
|---|---|---|---|---|
| 1 | CTR | 3–5% | 4,36% | ✅ |
| 2 | Tỷ lệ thêm giỏ | > 8% | 4,32% | ❌ |
| 3 | Tỷ lệ chuyển đổi | > 1% | 0,30% | ❌ |
| 4 | ROAS | ≥ 2,82 | 1,35 | ❌ |

**Kết luận**: **có click không thêm vào giỏ** (CTR đạt, tỷ lệ thêm giỏ không đạt).

**Phân tích nguyên nhân**: đây là nhóm đáng ngẫm nghĩ nhất. CTR 4,36% cho thấy **người tìm từ khóa này có ý định cực kỳ rõ ràng** (người tìm `carregador 20000mah 45w` chính là đang tìm sản phẩm này); nhưng tỷ lệ thêm giỏ chỉ có 4,32% — **người click vào không bị trang chi tiết thuyết phục**.

> **CTR cao của từ khóa chính xác là một tín hiệu mạnh**: nó chứng minh "tiêu đề viết đúng, thu hút được đúng người".
> Tỷ lệ thêm giỏ thấp lại là một tín hiệu mạnh khác: **trang chi tiết không đỡ được nhóm người đúng này**.
>
> Giá trị của nhóm này nằm ở chỗ: **nó loại trừ được vấn đề traffic.** Nếu ngay cả nhóm traffic chính xác nhất này cũng không đỡ được, thì vấn đề đúng là nằm ở trang chi tiết.

**Hành động**:

| # | Hành động | Đối tượng | Căn cứ | Kỳ vọng | Ưu tiên |
|---|---|---|---|---|---|
| 1 | Tối ưu đoạn 2 (điểm bán hàng cốt lõi) và đoạn 4 (thông số) của trang chi tiết: nói rõ **hiệu quả thực tế** của sạc nhanh 45W (như "đầy trong 40 phút"), chứ không chỉ ghi thông số | Module 03 (iterate) | Tỷ lệ thêm giỏ 4,32% < 8% | Tỷ lệ thêm giỏ tăng | 🔴 P0 |
| 2 | Chỉnh cấu trúc SKU: hiện có thể đang thiếu một phân khúc giữa đủ hấp dẫn | Module 03 | SOP: SKU là để người mua tự so sánh | Tỷ lệ thêm giỏ tăng | 🟡 P1 |
| 3 | Kiểm tra có voucher không | Vận hành | SOP liệt kê rõ là hướng tối ưu cho "có click không thêm vào giỏ" | — | 🟡 P1 |
| 4 | Bổ sung phản hồi thật của người mua | Vận hành | SOP liệt kê rõ là hướng tối ưu | — | 🟡 P1 |

**Vòng này dứt khoát không động vào**: ảnh chính và tiêu đề (CTR 4,36% đã đạt, động vào là không có căn cứ).

---

### Nhóm quảng cáo C · `bateria externa viagem` (ngữ cảnh)

| Bước | Hạng mục kiểm tra | Chuẩn | Thực tế | Đạt |
|---|---|---|---|---|
| 1 | CTR | 3–5% | 4,30% | ✅ |
| 2 | Tỷ lệ thêm giỏ | > 8% | 9,92% | ✅ |
| 3 | Tỷ lệ chuyển đổi | > 1% | 0,51% | ❌ |
| 4 | ROAS | ≥ 2,82 | 1,70 | ❌ |

**Kết luận**: **có thêm vào giỏ không chuyển đổi** (hai khâu đầu đạt, tỷ lệ chuyển đổi không đạt).

**Phân tích nguyên nhân**:
- CTR 4,30% ✅ + tỷ lệ thêm giỏ 9,92% ✅ → **ảnh chính, tiêu đề, trang chi tiết đều hiệu quả**
- Tỷ lệ chuyển đổi 0,51% ❌ → người mua đã thêm giỏ, đã thích, **nhưng do dự ở bước cuối cùng**

Các hạng mục SOP ưu tiên kiểm tra cho "có thêm vào giỏ không chuyển đổi": sức cạnh tranh về giá / mức voucher / chất lượng đánh giá / cam kết giao hàng / giá đối thủ / cam kết hậu mãi.

> **Nhóm này có giá trị chẩn đoán cao nhất**: nó chứng minh "trang chi tiết không có vấn đề". Tỷ lệ thêm giỏ 9,92% cho thấy trang chi tiết đã thuyết phục được về sản phẩm.
> Kẹt ở bước cuối, gần như chắc chắn là **lực cản ra quyết định** — điển hình nhất là **số lượng đánh giá không đủ** (SOP: giai đoạn đầu của link mới nhất định phải liên hệ khách để có ảnh review của người mua).

**Hành động**:

| # | Hành động | Đối tượng | Căn cứ | Kỳ vọng | Ưu tiên |
|---|---|---|---|---|---|
| 1 | **Xây dựng đánh giá**: liên hệ khách đã mua để xin đánh giá có ảnh | Vận hành | SOP chỉ rõ tới "chất lượng đánh giá" | Tỷ lệ chuyển đổi tăng | 🔴 P0 |
| 2 | Kiểm tra thông tin cam kết giao hàng có rõ ràng không | Module 03 | SOP liệt kê rõ là hướng tối ưu | — | 🟡 P1 |
| 3 | Đặt ưu đãi giới hạn thời gian hoặc tăng mức voucher | Vận hành | SOP liệt kê rõ là hướng tối ưu | — | 🟡 P1 |
| 4 | Khởi động **07 Review Analysis** để phân tích chất lượng đánh giá | Module 07 | `review_needed = true` | Tìm ra điểm cản cụ thể | 🟡 P1 |

**Vòng này dứt khoát không động vào**: ảnh chính, tiêu đề, trang chi tiết (hai khâu đầu đều đạt, **động vào là phá phần đã được kiểm chứng là hiệu quả**).

---

### Nhóm quảng cáo D · `power bank turbo` (từ khóa đối thủ)

| Bước | Hạng mục kiểm tra | Chuẩn | Thực tế | Đạt |
|---|---|---|---|---|
| 1 | CTR | 3–5% | 4,40% | ✅ |
| 2 | Tỷ lệ thêm giỏ | > 8% | 11,19% | ✅ |
| 3 | Tỷ lệ chuyển đổi | > 1% | 1,44% | ✅ |
| 4 | ROAS | ≥ 2,82 | 2,73 | ❌ |

**Kết luận**: **chi phí cao ROI thấp** (cả ba chỉ số phễu đều đạt, nhưng ROAS vẫn dưới ngưỡng hòa vốn).

**Phân tích nguyên nhân**: nhóm này là phát hiện quan trọng nhất của toàn bộ tài liệu.

- Ba khâu phễu **đều khỏe, thậm chí xuất sắc**: CTR 4,40% (đạt), tỷ lệ thêm giỏ 11,19% (vượt xa 8%), tỷ lệ chuyển đổi 1,44% (vượt chuẩn 44%)
- Nhưng ROAS chỉ có **2,73**, vẫn dưới ngưỡng hòa vốn **2,82** → **mỗi đơn lỗ R$ 1,3**

Nguyên nhân gốc: **CPC 0,60 gần gấp 2 lần các nhóm khác.**

| Nhóm | CPC |
|---|---|
| A | R$ 0,31 |
| B | R$ 0,25 |
| C | R$ 0,34 |
| **D** | **R$ 0,60** ← từ khóa đối thủ cạnh tranh giá thầu gay gắt, giá thầu bị đẩy lên |

> **Nhóm này lật đổ giả định "phễu đạt chuẩn là quảng cáo tốt".**
>
> Nhóm D là **nhóm duy nhất có phễu hoàn toàn khỏe** trong bốn nhóm, cũng là nhóm có CPA thấp nhất (R$ 41,55), nhưng nó vẫn đang lỗ — vì nó **mua traffic quá đắt**.
>
> Ngược trực giác hơn nữa: từ khóa quảng cáo của nhóm D là **từ khóa đối thủ** (người tìm thương hiệu của đối thủ). Loại từ khóa này tự nhiên có tỷ lệ chuyển đổi cao nhất (ý định rõ nhất), nhưng cũng đắt nhất. **Nhóm có tỷ lệ chuyển đổi cao nhất chưa chắc là nhóm có lãi nhất.**

**Hành động**:

| # | Hành động | Đối tượng | Căn cứ | Kỳ vọng | Ưu tiên |
|---|---|---|---|---|---|
| 1 | **Hạ giá thầu**: CPC từ R$ 0,60 xuống khoảng R$ 0,45 | Nhóm D | CPC là hạng mục bất thường duy nhất | Xem phần tính toán bên dưới | 🔴 P0 |
| 2 | Chỉnh hệ số giá thầu theo vị trí hiển thị: trang kết quả tìm kiếm giữ hệ số cao hơn, trang chi tiết hạ xuống | Nhóm D | ML/Shopee đều hỗ trợ hệ số theo vị trí hiển thị | Giảm chi phí ở vị trí kém hiệu quả | 🟡 P1 |
| 3 | Giữ từ khóa cốt lõi của nhóm, cắt các từ khóa đuôi dài không liên quan | Nhóm D | Tránh giá thầu tràn ra ngoài | — | ⚪ P2 |

**Vòng này dứt khoát không động vào**: ảnh chính, tiêu đề, trang chi tiết, giá (cả ba khâu phễu đều đạt, **không có căn cứ nào để động vào chúng**).

---

## IV. Tính toán then chốt: sửa CTR lại càng lỗ

Đây là đoạn đáng nhớ nhất của case này.

### Kịch bản 1 · Chỉ sửa CTR của nhóm A (1,40% → 3,0%)

Giả sử chỉ đổi ảnh chính của nhóm A, CTR tăng lên mức chuẩn 3,0%, các chỉ số còn lại (tỷ lệ thêm giỏ 6,22%, tỷ lệ chuyển đổi 0,44%) không đổi:

| Hạng mục | Trước khi sửa | Sau khi sửa |
|---|---|---|
| Click nhóm A | 675 | **1.446** |
| Chi phí nhóm A | R$ 210,60 | **R$ 448,26** |
| Đơn nhóm A | 3 | **6,4** |
| Tổng chi phí | R$ 678,42 | **R$ 916,08** |
| Tổng đơn | 11 | **14,4** |
| ROAS tổng | 1,84 | **1,79** ⬇️ |
| **Đóng góp ròng tổng** | **−R$ 235,56** | **−R$ 335,26** ⬇️ |

> ### ❌ Lỗ nhiều hơn.
>
> Vì tỷ lệ chuyển đổi của nhóm A chỉ có 0,44%. Tăng CTR chỉ khiến **nhiều traffic không đạt chuẩn click vào hơn**, tốn thêm tiền mua thêm những click không ra đơn.
>
> **Bản thân hành động "đẩy CTR lên" là trung tính.** Chỉ khi tỷ lệ chuyển đổi không giảm thì tăng CTR mới có ý nghĩa.

### Kịch bản 2 · Chỉ sửa tỷ lệ chuyển đổi tổng (0,55% → 1,0%)

Giả sử lượng click và chi phí hoàn toàn không đổi, chỉ nâng tỷ lệ chuyển đổi lên mức chuẩn SOP 1,0%:

| Hạng mục | Trước khi sửa | Sau khi sửa |
|---|---|---|
| Đơn | 11 | **20,2** |
| GMV | R$ 1.247,40 | **R$ 2.287,28** |
| ROAS tổng | 1,84 | **3,37** ✅ |
| **Đóng góp ròng tổng** | **−R$ 235,56** | **+R$ 133,62** ✅ |

> ### ✅ Vượt ngưỡng hòa vốn, chuyển lỗ thành lãi.

**Độ nhạy theo tỷ lệ chuyển đổi**

| Tỷ lệ chuyển đổi | Đơn | ROAS | Đóng góp ròng | Đánh giá |
|---|---|---|---|---|
| 0,55% (hiện tại) | 11,1 | 1,85 | −R$ 235,56 | ❌ |
| 0,75% | 15,1 | 2,53 | −R$ 69,39 | ❌ |
| **1,00%** | **20,2** | **3,37** | **+R$ 133,62** | ✅ **Vượt ngưỡng hòa vốn** |
| 1,25% | 25,2 | 4,21 | +R$ 336,64 | ✅ |
| 1,50% | 30,3 | 5,06 | +R$ 539,65 | ✅ |

**Giá trị tới hạn của tỷ lệ chuyển đổi khoảng 0,83%** (khi ROAS đạt 2,82).

### Kịch bản 3 · Nâng tỷ lệ chuyển đổi nhóm C lên 1% (có thêm vào giỏ không chuyển đổi)

| Hạng mục | Trước khi sửa | Sau khi sửa |
|---|---|---|
| Đơn | 2 | 3,9 |
| Chi phí | R$ 133,62 | R$ 133,62 |
| ROAS | 1,70 | **3,34** ✅ |
| Đóng góp ròng | −R$ 53,11 | **+R$ 24,60** ✅ |

> Nhóm C chỉ chiếm 20% ngân sách, sửa xong đóng góp R$ 24,60. **Vấn đề của nhóm C nằm ở "lực cản ra quyết định", thứ cần sửa là đánh giá và cam kết, không phải traffic.**

### Kịch bản 4 · CPC nhóm D giảm từ 0,60 xuống 0,45 (phễu đã khỏe)

| Hạng mục | Trước khi sửa | Sau khi sửa |
|---|---|---|
| Chi phí | R$ 166,20 | R$ 124,65 |
| ROAS | 2,73 | **3,64** ✅ |
| Đóng góp ròng | −R$ 5,18 | **+R$ 36,39** ✅ |

> **Nhóm D là nhóm dễ sửa nhất**: phễu đã khỏe, chỉ cần ép phần mua đắt xuống.

### Đối chiếu bốn kịch bản

| Kịch bản | Hành động | Thay đổi đóng góp ròng | Kết luận |
|---|---|---|---|
| 1 | Sửa CTR nhóm A | −R$ 235,56 → **−R$ 335,26** | ❌ **Xấu đi** |
| 2 | Sửa tỷ lệ chuyển đổi tổng lên 1% | −R$ 235,56 → **+R$ 133,62** | ✅ Chuyển lỗ thành lãi |
| 3 | Sửa tỷ lệ chuyển đổi nhóm C lên 1% | −R$ 53,11 → **+R$ 24,60** | ✅ |
| 4 | Sửa CPC nhóm D | −R$ 5,18 → **+R$ 36,39** | ✅ |

> **Thứ tự ưu tiên đúng là 2 → 4 → 3, còn 1 xếp cuối cùng.**
> Trong khi nếu xếp theo trực giác "nhóm nào CTR tệ nhất", đáp án sẽ là 1 ưu tiên — **đây chính là cái bẫy mà trực giác sẽ giẫm phải.**

---

## V. Kết luận chẩn đoán và tổng hợp hành động

### Đánh giá tổng một câu

> **Mô hình quảng cáo hiện tại của sản phẩm này không đứng được, nút thắt là tỷ lệ chuyển đổi (0,55%, chỉ bằng một nửa chuẩn), chứ không phải CTR.**
> Trước khi tỷ lệ chuyển đổi được sửa lên 1%, mọi hành động tăng hiển thị hay nâng CTR đều sẽ khuếch đại khoản lỗ.

### Tổng hợp hành động (xếp theo phạm vi ảnh hưởng)

| Ưu tiên | Hành động | Đối tượng | Căn cứ | Kỳ vọng | Chu kỳ kiểm tra lại |
|---|---|---|---|---|---|
| 🔴 **P0** | **Xây dựng đánh giá**: liên hệ khách đã mua để xin đánh giá có ảnh | Vận hành | Tỷ lệ chuyển đổi tổng 0,55% là nút thắt cứng duy nhất; SOP chỉ thẳng tới "chất lượng đánh giá" | Tỷ lệ chuyển đổi → 1% → chuyển lỗ thành lãi | 7 ngày |
| 🔴 **P0** | **Nhóm D hạ giá thầu**: CPC 0,60 → 0,45 | Quảng cáo nhóm D | Phễu đã khỏe, hạng mục bất thường duy nhất là CPC | Đóng góp ròng +R$ 36,39 | 7 ngày |
| 🔴 **P0** | **Nhóm A thu hẹp kiểu khớp**: rộng → chính xác + thêm từ khóa phủ định | Quảng cáo nhóm A | Cả ba khâu cùng thấp = traffic không chính xác | Giảm chi phí vô ích | 7 ngày |
| 🟡 P1 | **Nhóm B tối ưu đoạn 2/4 của trang chi tiết**: nói 45W thành hiệu quả | Module 03 (iterate) | Tỷ lệ thêm giỏ 4,32% < 8% | Tỷ lệ thêm giỏ tăng | 7 ngày |
| 🟡 P1 | **Nhóm C khởi động 07 Review Analysis** | Module 07 | Thêm giỏ đạt nhưng chuyển đổi không đạt = lực cản ra quyết định | Xác định điểm cản cụ thể | 7 ngày |
| 🟡 P1 | Bổ sung voucher / tối ưu hiển thị thông tin giao hàng và bảo hành | Vận hành + 03 | Hướng tối ưu của SOP cho "có thêm vào giỏ không chuyển đổi" | — | 7 ngày |
| ⚪ P2 | Tối ưu ảnh chính nhóm A | Module 04 | CTR 1,40% thấp (nhưng không phải nút thắt hiện tại) | — | 7 ngày |

### Có thể thực hiện cùng đợt không

**Ba hạng mục P0 chỉ tới các nguyên nhân gốc khác nhau, nhưng không ảnh hưởng lẫn nhau**:

| Hành động | Nguyên nhân gốc | Có ảnh hưởng lẫn nhau không |
|---|---|---|
| Xây dựng đánh giá | Lực cản ra quyết định | Không |
| Nhóm D hạ giá thầu | Chi phí | Không |
| Nhóm A thu hẹp kiểu khớp | Chất lượng traffic | Không |

**Kết luận**: có thể thực hiện cùng đợt. Lý do là mục tiêu của vòng này là **cắt lỗ** — cả ba hạng mục đều là cắt giảm chi phí vô ích hoặc giảm lực cản ra quyết định, không dính tới việc đánh đổi để "nâng một chỉ số nào đó".

**Điều duy nhất cần lưu ý**: sau khi nhóm A thu hẹp kiểu khớp, lượng click sẽ giảm, **đừng đánh giá nhầm đây là "hành động thất bại"**. Chỉ số cần xem là **CPA và ROAS**, không phải lượng click.

---

## VI. Tính ngưỡng hòa vốn

### Lợi nhuận gộp khả dụng trước quảng cáo

| Hạng mục | Số tiền | % giá bán |
|---|---|---|
| Giá bán | R$ 113,40 | 100% |
| − Giá vốn + vận chuyển chặng cuối + phí kho | R$ 55,00 | 48,5% |
| − Hoa hồng sàn (14%) | R$ 15,88 | 14,0% |
| − Hao hụt hoàn hàng (2%) | R$ 2,27 | 2,0% |
| **= Lợi nhuận gộp khả dụng trước quảng cáo** | **R$ 40,26** | **35,5%** |

```
ROAS hòa vốn = 113,40 ÷ 40,26 = 2,82
```

### Độ nhạy ROAS

| ROAS | Phí QC/đơn | Lợi nhuận gộp còn lại/đơn | % giá bán | Đánh giá |
|---|---|---|---|---|
| 2,0 | R$ 56,70 | −R$ 16,44 | −14,5% | ❌ |
| 2,5 | R$ 45,36 | −R$ 5,10 | −4,5% | ❌ |
| **2,82** | R$ 40,21 | R$ 0,04 | ~0% | ⚠️ Hòa vốn |
| 3,37 | R$ 33,65 | R$ 6,61 | 5,8% | ✅ Mục tiêu sửa hiện tại |
| 5,0 | R$ 22,68 | R$ 17,58 | 15,5% | ✅ |
| 8,0 | R$ 14,18 | R$ 26,08 | 23,0% | ✅ |
| **13,33** | R$ 8,50 | R$ 31,76 | **28,0%** | 🎯 Mục tiêu của mô hình định giá |

### ⚠️ Một khoảng chênh bắt buộc phải nhìn rõ

Khi định giá, theo tỷ lệ chi phí quảng cáo SOP giả định **7,5%** đã dự trù `R$ 8,51/đơn`, tương ứng **ROAS 13,33**. Trong khi ROAS chạy thực tế là **1,84**, mục tiêu sửa cũng chỉ là **3,37**.

| | ROAS | Biên lợi nhuận gộp |
|---|---|---|
| Giả định của mô hình định giá | 13,33 | 28,0% |
| Mục tiêu sửa | 3,37 | 5,8% |
| Chạy thực tế | 1,84 | Lỗ |

> **Kết luận: định giá của sản phẩm này chưa chừa chỗ cho chi phí quảng cáo thật.**
> Kể cả khi sửa tỷ lệ chuyển đổi về mức chuẩn, biên lợi nhuận gộp cũng chỉ có **5,8%** — thấp xa so với 28% mà mô hình định giá hình dung.
>
> **Cách làm đúng là ở giai đoạn định giá, dự trù chi phí quảng cáo 12–15% chứ không phải 7,5%.** Đây không phải vấn đề chạy quảng cáo giải quyết được, mà là vấn đề định giá.

### Đề xuất hướng xử lý

| # | Hướng | Giải thích | Đề xuất cho case này |
|---|---|---|---|
| 1 | Nâng mức dự trù chi phí quảng cáo khi định giá | Từ 7,5% lên 12–15%, tính lại giá bán | ⚠️ Giá bán cần tăng từ R$ 113,40, có thể ảnh hưởng chuyển đổi |
| 2 | Chấp nhận biên lợi nhuận thấp, dựa vào traffic tự nhiên | Quảng cáo chỉ làm lực đẩy khởi động lạnh | ✅ **Khuyến nghị** — sản phẩm này là SKU kéo traffic, định vị vốn là kéo traffic, không nên kỳ vọng quảng cáo trực tiếp có lãi |
| 3 | Tối ưu cấu trúc chi phí | Đàm phán phí vận chuyển tốt hơn, đổi nhà cung cấp | Làm song song |
| 4 | Tăng giá trị đơn hàng | Đẩy SKU combo (như 20000mAh × 2) | ✅ Nên làm đồng thời |
| 5 | Bỏ sản phẩm này | Cấu trúc lợi nhuận không đứng được | Tạm chưa xét — nhiệm vụ của SKU kéo traffic không phải là kiếm tiền |

> **Hướng 2 + 4 là lựa chọn hợp lý nhất cho sản phẩm này**: là SKU kéo traffic, nhiệm vụ của nó là kéo traffic vào shop, kéo theo SKU lợi nhuận; chi phí quảng cáo nên được **nhìn như "chi phí có khách" chứ không phải "khoản trừ vào lợi nhuận"**.
> Nhưng tiền đề là chi phí có khách này phải nằm trong mức chịu được — `R$ 61,67/đơn` (CPA hiện tại) rõ ràng quá cao, `R$ 33,65/đơn` (mục tiêu sửa) cũng không thấp.

---

## VII. Mô hình ngân sách và nhịp

### Mức trần ngân sách tối đa

| Căn cứ phán đoán | Tình hình case này | Ảnh hưởng |
|---|---|---|
| Quy mô thị trường của ngành hàng | Sạc dự phòng là ngành hàng cạnh tranh cao ở Shopee Brazil, quy mô lớn | Có thể gánh ngân sách tương đối lớn |
| Lượng nhu cầu tìm kiếm | `carregador portátil` có lượng tìm kiếm lớn | Gánh được |
| Mức doanh số của đối thủ | Đối thủ top đầu có doanh số cao | Cạnh tranh phân khúc gay gắt |
| **Điểm uy tín hiện tại của link bên mình** | **Link mới, ít đánh giá** | ⚠️ **Đây mới là ràng buộc trần thật sự** |

> **Quy mô thị trường lớn ≠ bạn gánh được ngân sách lớn.** Ràng buộc thật sự hiện tại không phải thị trường, mà là **khả năng chuyển đổi** của link bên mình (0,55%).
> **Trước khi tỷ lệ chuyển đổi được sửa, khuyến nghị giữ nguyên ngân sách hiện tại, không tăng thêm.**

### Khoảng ROI mục tiêu

| Chiều | Hiện trạng | Ảnh hưởng tới mức trần ROI |
|---|---|---|
| Ảnh chính | Đã tối ưu (xem case 03) | Trung tính |
| Giá | R$ 113,40, ngang các sản phẩm cùng loại | Trung tính |
| **Số lượng đánh giá** | **Ít** | ⬇️ **Kìm hãm nghiêm trọng mức trần ROI** |
| Trang chi tiết | Đủ 7 đoạn | Tích cực |
| Cam kết hậu mãi | Bảo hành 6 tháng | Tích cực |

**Khoảng ROI mục tiêu đề xuất**: `2,50` – `3,40`

- `2,50` hơi thấp hơn ngưỡng hòa vốn, làm giá trị chuyển tiếp trong giai đoạn sửa (ưu tiên lấy mẫu)
- `3,40` là đường mục tiêu sau khi sửa xong

⚠️ **Đừng ngay từ đầu đặt ROI ở 2,82 (ngưỡng hòa vốn).** ROI đặt càng sát ngưỡng hòa vốn, quảng cáo càng khó chạy, mẫu càng ít, càng không xác định được mô hình thật. **Chạy lấy mẫu ở 2,50 trước, rồi siết dần.**

### Nhịp ngân sách theo khung giờ (Shopee Brazil)

| Khung giờ (giờ Brazil BRT) | Giờ Bắc Kinh tương ứng | Ngân sách | Lý do |
|---|---|---|---|
| 00:00 – 09:00 (Brazil từ khuya tới sáng sớm) | **11:00 – 20:00** | **R$ 10 (ngủ đông)** | Vùng trũng chuyển đổi, ép chi phí |
| 09:00 – 24:00 (Brazil từ ban ngày tới khuya) | **20:00 – 11:00 hôm sau** | **Ngân sách mục tiêu** | Cửa sổ chuyển đổi |

> **Dùng "hạ thấp" chứ không phải "tạm dừng"**: SOP chỉ rõ tạm dừng thường xuyên sẽ lãng phí hạn mức miễn phí sàn cấp cho link mới. Ép ngân sách về R$ 10 chỉ giảm chi tiêu, không kích hoạt việc mất hạn mức.
>
> **Đã kiểm tra quy đổi múi giờ**: giờ Brazil (BRT, UTC−3) **chậm hơn giờ Bắc Kinh (UTC+8) 11 tiếng**. Vì vậy 00:00 Brazil = 11:00 Bắc Kinh.

---

## VIII. Phương án kiểm tra lại

| Hạng mục | Nội dung |
|---|---|
| Thời điểm kiểm tra lại | Ngày thứ **7** sau khi thay đổi |
| Dữ liệu cần thu | Hiển thị / click / thêm giỏ / đơn / chi phí của từng nhóm |
| **Chỉ số theo dõi chính** | **Tỷ lệ chuyển đổi tổng** (mục tiêu ≥ 0,83%, lý tưởng ≥ 1,0%), **ROAS tổng** (mục tiêu ≥ 2,82), **CPA** (mục tiêu ≤ R$ 45) |
| **Chỉ số không nên theo dõi** | Lượng click nhóm A (thu hẹp kiểu khớp thì chắc chắn giảm, không phải tín hiệu thất bại) |
| Tiêu chí đạt | ROAS tổng ≥ 2,82 và đóng góp ròng > 0 |
| Xử lý khi không đạt | Quay lại chẩn đoán phễu, **đừng tiếp tục tăng liều cùng một hành động** |
| Nhiễu bên ngoài cần loại trừ | Có đợt sale lớn của sàn, đối thủ chỉnh giá, hết hàng không |

> **Điều "đừng theo dõi lượng click nhóm A" rất then chốt.** Thu hẹp kiểu khớp rồi lượng click giảm là **kết quả dự kiến**, không phải vấn đề. Nếu người vận hành cứ nhìn chằm chằm vào lượng click, sẽ đánh giá nhầm là "hành động vô dụng" rồi đổi kiểu khớp về lại khớp rộng — sửa ngược lại đúng vấn đề vừa sửa xong.

---

## IX. Quét tuân thủ đề xuất

`Quét tuân thủ đề xuất: không vi phạm`

(Case này không liên quan tới: tạo dữ liệu giả, cạnh tranh không lành mạnh, lách thuật toán, đề xuất không thực thi được, cam kết hiệu quả thiếu căn cứ. Mọi hiệu quả kỳ vọng đều đã ghi rõ điều kiện tiền đề.)

---

## X. Các trường bàn giao cho module khác

```yaml
breakeven_roas: 2.82
target_roas_range: [2.50, 3.40]     # giai đoạn sửa → sau khi sửa
max_daily_budget: "Giữ nguyên mức hiện tại, không tăng thêm — chưa nên scale khi tỷ lệ chuyển đổi chưa được sửa"
test_window_days: 7

budget_schedule:
  BRT_00_09: 10.00                  # ngủ đông
  BRT_09_24: "target"

symptom_by_group:
  A: "Cả ba khâu đều không đạt → nguyên nhân gốc: traffic khớp rộng không chính xác (không phải vấn đề ảnh chính)"
  B: "Có click không thêm vào giỏ → nguyên nhân gốc: trang chi tiết không đỡ được traffic chính xác"
  C: "Có thêm vào giỏ không chuyển đổi → nguyên nhân gốc: lực cản ra quyết định (đánh giá/cam kết/giá)"
  D: "Chi phí cao ROI thấp → nguyên nhân gốc: CPC 0.60 giá thầu quá cao (bản thân phễu khỏe)"

ctr_fail_groups: [A]                # → 03 sửa tiêu đề / 04 đổi ảnh chính (ưu tiên thấp nhất)
atc_fail_groups: [A, B]             # → 03 sửa trang chi tiết
cvr_fail_groups: [A, B, C]          # → 03 sửa cách hiển thị giá / 07 phân tích đánh giá
review_needed: true                 # → khởi động 07

# Chỉ số then chốt (để đối chiếu khi kiểm tra lại)
baseline_cvr: 0.0055
target_cvr: 0.0100
cvr_threshold_for_breakeven: 0.0083 # tỷ lệ chuyển đổi đạt mức này là vượt ngưỡng hòa vốn
baseline_roas: 1.84
baseline_cpa: 61.67
```

---

## XI. Case này chứng minh điều gì

| Kết luận | Bằng chứng |
|---|---|
| **Sửa CTR có thể làm khoản lỗ lớn hơn** | Kịch bản 1: CTR nhóm A 1,40%→3,0%, đóng góp ròng xấu đi từ −235,56 xuống −335,26 |
| **Khung bốn loại có tình huống không bao phủ được** | Nhóm A cả ba khâu cùng không đạt → nguyên nhân gốc là "từ khóa quá rộng", không thuộc loại đơn lẻ nào trong bốn loại |
| **Phễu đạt hết ≠ có lãi** | Nhóm D cả ba khâu CTR/thêm giỏ/chuyển đổi đều khỏe, ROAS 2,73 vẫn dưới ngưỡng hòa vốn 2,82 |
| **Nhóm có tỷ lệ chuyển đổi cao nhất chưa chắc có lãi nhất** | Nhóm D là nhóm từ khóa đối thủ, tỷ lệ chuyển đổi 1,44% cao nhất, nhưng CPC cũng cao nhất (R$ 0,60) |
| **Ngưỡng hòa vốn quan trọng hơn đường chuẩn** | Đường chuẩn cho biết "khâu nào không khỏe", ngưỡng hòa vốn cho biết "có lãi hay không". Phải xem cả hai |
| **Giả định định giá có thể đánh giá thấp nghiêm trọng chi phí quảng cáo** | Dự trù 7,5% tương ứng ROAS 13,33, mục tiêu sửa thực tế chỉ có 3,37 → đây là vấn đề định giá, không phải vấn đề chạy quảng cáo |
| **Nguyên nhân gốc khác nhau có thể sửa cùng đợt, cùng một nguyên nhân gốc phải tách vòng** | Ba hạng mục P0 vòng này có nguyên nhân gốc khác nhau, không ảnh hưởng lẫn nhau → có thể cùng đợt; nếu đều chỉ tới CTR thì phải tách bước để giữ khả năng quy nguyên nhân |
| **Sửa xong phải đổi chỉ số theo dõi** | Nhóm A thu hẹp kiểu khớp thì lượng click chắc chắn giảm, lúc này nên xem CPA/ROAS chứ không phải lượng click |
| **SKU kéo traffic không nên đo bằng tiêu chuẩn của SKU lợi nhuận** | Sản phẩm này định vị kéo traffic, chi phí quảng cáo nên được nhìn như "chi phí có khách" (hướng 2) |

---

**File liên quan**: [Giới thiệu module](../README.md) · [Prompt chẩn đoán phễu](../prompts/01_funnel_diagnosis.md) · [Prompt mô hình ngân sách ROI](../prompts/02_budget_roi_model.md) · [Mô hình định giá](../../../Templates/cost_pricing_template.md) · [Case Listing cùng sản phẩm](../../03_Listing_Creative_Agent/examples/powerbank_20000mah.md) · [Case vòng khép kín](../../../Examples/03_Closed_Loop/)
