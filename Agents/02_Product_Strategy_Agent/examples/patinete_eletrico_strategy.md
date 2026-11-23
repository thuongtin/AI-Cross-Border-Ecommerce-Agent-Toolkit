# Case study · Chiến lược sản phẩm Patinete Elétrico (Shopee Brazil)

> **Loại case study**: case study tái hiện được · nối tiếp đầu ra phân tích thị trường của 01
> **Module sử dụng**: 02 Product Strategy Agent
> **SOP tương ứng**: 1.7 Xác nhận sản phẩm chủ lực · 1.9 Định giá · 3.1 Chuẩn bị trước khi đăng bán · 3.2 Chiến lược SKU
> **Trọng tâm minh họa**: **dư địa lợi nhuận vừa đủ để phát một voucher** —— định giá và cấu trúc SKU nhất quán với nhau

---

## 1. Đầu vào upstream (01 Market Research)

Xem [`01/.../examples/patinete_eletrico_market.md`](../../01_Market_Research_Agent/examples/patinete_eletrico_market.md). Các trường then chốt:

```yaml
target_price_range: [1989.13, 2966.21]
main_price_zone: [2100, 2300]
cost_floor_price: 1989.36        # 01 tính ngược: giá khả thi thấp nhất với biên LN 32% + quảng cáo 5%

brand_barrier: low               # CR3 74.1% nhưng top 3 đều là hàng no-brand → người mua không quan tâm thương hiệu
seller_barrier: medium           # CR10 71.5%, nhưng nhóm đuôi vẫn hoạt động sôi nổi

recommended_config: {power: "500W", load: "200kg", capacity: "12Ah"}
mainstream_config: {power: "500W", load: "150kg", capacity: "12Ah"}

opportunity_config:
  value: "200kg"
  evidence: "Chỉ có 4 sản phẩm đối thủ, doanh số trung bình 212.0 (gấp 1.80 lần trung bình chung), top 3 người bán chỉ chiếm 2/4, doanh số cao nhất đến từ người bán vừa và nhỏ"

competitor_weakness:
  - "Phân khúc 800W có nhiều sản phẩm nhất nhưng doanh số trung bình thấp nhất (0.49 lần) → cấu hình giá cao bán không chạy"
  - "Đối thủ thường không ghi điều kiện test quãng đường/tải trọng → bên ta ghi rõ điều kiện để tạo niềm tin"
```

**Xác nhận quyết định**: `decision_approved = true` (trưởng bộ phận vận hành, 2026-10-13)

---

## 2. Step 1 · Định vị loại sản phẩm

| Khía cạnh | Định vị | Căn cứ |
|---|---|---|
| Vai trò trong shop | **SKU lợi nhuận** | Ngành hàng rủi ro cao (4 mục) cần biên lợi nhuận cao để gánh; biên LN sau rủi ro 32,4% vẫn đứng vững |
| Mức độ khác biệt | **SKU khác biệt hóa** | Có `opportunity_config` rõ ràng (200kg) và chưa bị nhóm dẫn đầu độc chiếm |
| Vai trò quảng bá | **SKU chủ lực** | Khác biệt hóa đủ gánh ROI, phù hợp test quảng cáo |

**Lý do định vị**

【Căn cứ】Rào cản thương hiệu thấp (top 3 theo CR3 đều là hàng no-brand) → không cần trả tiền cho premium thương hiệu, có thể đánh vào khác biệt sản phẩm
【Căn cứ】Rào cản người bán trung bình (CR10 71,5%) → chỉ bán theo (copy) thì khó, bắt buộc phải có khác biệt
【Đề xuất】Chọn **SKU khác biệt hóa + SKU lợi nhuận**: lấy tải trọng 200kg làm điểm tựa khác biệt, né cuộc chiến giá ở phân khúc phổ thông 150kg

---

## 3. Step 2 · Xác nhận cấu hình cốt lõi

| Khía cạnh cấu hình | Giá trị thị trường đề xuất | Giá trị bên ta chốt | Khớp | Giải thích |
|---|---|---|---|---|
| Công suất | 500W | **500W** | ✅ | Chiếm 61,4% doanh số, doanh số trung bình gấp 1,62 lần trung bình chung |
| **Tải trọng** | **200kg** | **200kg** | ✅ | ★Cấu hình cơ hội, doanh số trung bình gấp 1,80 lần trung bình chung |
| Dung lượng pin | 12Ah | **12Ah** | ✅ | Chiếm 78% doanh số |
| Gấp gọn | — | Gấp gọn được | — | Trang bị tiêu chuẩn phổ biến, không có thì mất sức cạnh tranh |

**Đối chiếu cấu hình với năng lực công ty**

| Cấu hình | Công ty làm được không | Giải thích |
|---|---|---|
| Động cơ 500W | ✅ | Nhà cung cấp hiện tại hỗ trợ |
| **Tải trọng 200kg** | ⚠️ | **Cần xác nhận**: cần gia cố kết cấu khung, nhà cung cấp có hỗ trợ được không |
| Pin 12Ah | ✅ | Nhà cung cấp hiện tại hỗ trợ |

> ⚠️ **Tải trọng 200kg là điểm tựa cốt lõi của phương án này, nhưng cũng là mục năng lực duy nhất còn chờ xác nhận.**
> Nếu nhà cung cấp không làm được 200kg, toàn bộ logic khác biệt hóa sụp đổ —— khi đó phải quay lại 01 chọn lại cấu hình (ví dụ đổi sang khác biệt bằng 「gấp gọn + giảm xóc kép」), **chứ không cố ghi 200kg**.

### Một lựa chọn đánh đổi cấu hình then chốt

Dữ liệu thị trường cho thấy:

| Công suất | Tỷ trọng số sản phẩm | Tỷ trọng doanh số | Doanh số trung bình | Diễn giải |
|---|---|---|---|---|
| 500W | 38,0% | **61,4%** | **190,1** | Phổ thông + hiệu quả → **SKU chủ lực** |
| **800W** | **34,0%** (nhiều nhất) | 16,6% | **57,4** | Nhiều sản phẩm nhất nhưng **hiệu quả thấp nhất** |

> **800W là cái bẫy dễ dính nhất**: theo trực giác "cấu hình càng cao càng tốt", nhưng dữ liệu cho thấy phân khúc 800W có nhiều sản phẩm nhất (17 sản phẩm) mà doanh số trung bình chỉ 57,4, bằng **0.49 lần** trung bình chung.
> **Kết luận: không lấy 800W làm SKU chủ lực.** Nó chỉ nên làm 「SKU cấu hình cao」 để tăng AOV; lấy nó làm chủ lực chẳng khác nào dùng cấu hình cạnh tranh khốc liệt nhất để đánh trận thảm nhất.

---

## 4. Step 3 · Thu gọn điểm bán hàng chủ lực

### 4.1 Nguồn điểm bán hàng

| Nguồn | Nội dung | Mức khả dụng |
|---|---|---|
| **Cấu hình cơ hội** | Tải trọng 200kg (chỉ 4 sản phẩm đối thủ) | ✅ **Khác biệt hóa cốt lõi** |
| Cấu hình phổ thông | Động cơ 500W + 12Ah | ⭕ Nền tảng (bắt buộc có, nhưng không phải điểm bán hàng) |
| Điểm yếu của đối thủ | Không ghi điều kiện test | ✅ Khác biệt hóa về độ tin cậy |
| Mối quan tâm thường gặp của người mua | Khả năng leo dốc (xem case study đánh giá của 07: đứng thứ 1 trong đánh giá tích cực, 38 lượt nhắc đến) | ✅ nhưng cần thêm giới hạn |

### 4.2 Phân tầng điểm bán hàng

| Tầng | Điểm bán hàng | Căn cứ hỗ trợ | Dùng cho |
|---|---|---|---|
| **Điểm bán hàng chính (duy nhất)** | **`Motor 500W com capacidade de 200 kg`** (động cơ 500W + tải trọng 200kg) | 500W chiếm 61,4% doanh số; 200kg chỉ có 4 sản phẩm đối thủ và doanh số trung bình gấp 1,80 lần | Copy chính trên ảnh chính / hook video / từ thông số trong tiêu đề |
| Điểm bán hàng phụ 1 | Giảm xóc kép (trước sau) | Đứng thứ 3 trong đánh giá tích cực (27 lượt nhắc đến) | Trang chi tiết / ảnh 6 / cảnh quay video |
| Điểm bán hàng phụ 2 | Gấp gọn trong 3 giây | Đứng thứ 2 trong đánh giá tích cực (31 lượt nhắc đến) | Ảnh 5 / cảnh quay video |
| Điểm bán hàng phụ 3 | Phanh kép phanh đĩa + phanh điện | Cấu hình có thật | Ảnh 6 / trang chi tiết |
| Điểm bán hàng phụ 4 | Minh bạch điều kiện test quãng đường | Đối thủ thường không ghi | Chú thích đoạn 4 trang chi tiết |
| Điểm bán hàng nền | Pin 12Ah / đèn LED / yên chỉnh được | Trang bị tiêu chuẩn phổ biến | Bảng thông số đoạn 4 trang chi tiết |
| **Cách diễn đạt bị cấm** | `200kg ngồi hai người thoải mái` / `mọi con dốc` / `quãng đường 60km` / `chiếu sáng ban đêm` / bảo hành một năm | Không đúng thông số hoặc vượt giới hạn | ⛔ `forbidden_words` |

### 4.3 Kết luận một câu

> **Sản phẩm này của chúng ta bán cho** người dùng trưởng thành cần chở tải trọng lớn (kể cả đồ đạc) khi đi lại trong thành phố**,
> đánh vào **động cơ 500W + tải trọng 200kg** (trên thị trường chỉ có 4 đối thủ, và sản phẩm có doanh số cao nhất đến từ người bán vừa và nhỏ),
> dùng cấu hình **gấp gọn + giảm xóc kép + phanh đĩa**,
> ở mức **R$ 2.199** (nằm trong vùng hai đỉnh 2.100–2.300 của dải giá #2),
> né ba loại rủi ro hậu mãi: **khai khống quãng đường, dùng vượt tải trọng, khó lắp ráp**.

---

## 5. Step 4 · Danh sách phòng tránh rủi ro

| # | Loại rủi ro | Rủi ro cụ thể | Cách phòng tránh | Đặt ở đâu |
|---|---|---|---|---|
| 1 | **Không khai khống thông số** | Quãng đường (tăng tải thì quãng đường giảm), tốc độ (30km/h là tối đa chứ không phải trung bình) | Ghi đầy đủ điều kiện test (cân nặng người lái/mặt đường/tốc độ) | Chú thích thông số đoạn 4 của 03 |
| 2 | **Không ghi từ thương hiệu** | Danh sách từ của đối thủ có thương hiệu chưa được ủy quyền như `Xiaomi` | Đưa vào `forbidden_words`, chặn cứng toàn chuỗi | 03/04/05 |
| 3 | Nói trước vấn đề hậu mãi | Tưởng có kèm mũ bảo hiểm / bơm (case study 07 thực tế có 2 đánh giá tiêu cực loại này) | Ảnh danh sách đóng gói ghi rõ `Não incluso` | 03 đoạn 6 + 04 ảnh 8 |
| 4 | **Ghi rõ giới hạn chức năng** | Tưởng leo được dốc đứng / chở được hai người | Ghi rõ "dốc thoải, một người lái, tải trọng gồm cả hành lý" | 03 đoạn 6 |
| 5 | Không cam kết bừa | Không có điểm sửa chữa tại địa phương | Chỉ cam kết đổi hàng, không ghi dịch vụ sửa chữa | 03 đoạn 5 |

### Giới hạn cam kết hậu mãi (bị ràng buộc bởi năng lực thực tế)

| Năng lực hậu mãi | Cam kết không được ghi |
|---|---|
| ✅ Đổi hàng được | — |
| ❌ Không sửa chữa được | **Không ghi "có dịch vụ sửa chữa"** |
| ❌ Không có điểm bảo hành tại địa phương | **Không ghi "bảo hành tại địa phương"** |
| ✅ Cung cấp được phụ kiện | Có thể ghi "phụ kiện có thể mua riêng" |
| Bảo hành 6 tháng (động cơ + pin) | Không ghi "bảo hành toàn bộ xe" |

**Copy cam kết hậu mãi đoạn 5 chốt theo đó** (giao cho 03):

```text
Garantia de 6 meses para motor e bateria.
Atendimento pelo chat com resposta em até 24 horas.
Peças de reposição disponíveis para compra separada.
```

> ⚠️ **Chú ý câu thứ ba**: vì **không sửa chữa được**, năng lực hậu mãi chỉ cho phép cam kết "cung cấp phụ kiện".
> Nếu chép nguyên "assistência técnica completa" (hỗ trợ kỹ thuật toàn diện) của đối thủ, tức là ghi điều mình không làm được vào Listing —— tự tạo ra đánh giá tiêu cực.

---

## 6. Step 5 · 8 câu hỏi trước khi đăng bán

| # | Câu hỏi | Trả lời | Trạng thái |
|---|---|---|---|
| 1 | Bán cho ai | Người dùng trưởng thành đi lại trong thành phố, gồm cả nhóm cần chở đồ | ✅ |
| 2 | Điểm bán hàng cốt lõi | Động cơ 500W + tải trọng 200kg | ✅ |
| 3 | Đối thủ chính | 4 sản phẩm đối thủ 200kg (sản phẩm có doanh số cao nhất đến từ người bán vừa và nhỏ) | ✅ |
| 4 | Khoảng giá | R$ 2.100–2.300 (giá chủ lực R$ 2.199) | ✅ |
| 5 | SKU chủ lực | 500W / 200kg / 12Ah | ✅ |
| 6 | Mức lợi nhuận sàn | Giá hòa vốn **R$ 1.113,10** (thấp hơn mức này là lỗ mỗi đơn) | ✅ |
| 7 | Có phù hợp test quảng cáo không | **✅ Phù hợp**——có khác biệt hóa và chưa bị độc chiếm, đủ gánh ROI | ✅ |
| 8 | Rủi ro hậu mãi | Chênh lệch kỳ vọng về quãng đường/tải trọng, khó lắp ráp, hiểu lầm về phụ kiện | ✅ |

> **Câu trả lời của câu 6 đáng chú ý**: giá hòa vốn chỉ **R$ 1.113,10**, trong khi giá chủ lực là R$ 2.199 —— ở giữa có khoảng đệm an toàn gần **1.086 real**.
> Điều này có nghĩa là **dư địa hạ giá nuôi trọng số giai đoạn đầu rất lớn** (chi tiết xem mục 9), nhưng cũng cho thấy **bản thân mức giá đã có dư địa dồi dào**, không cần dựa vào giá thấp để khởi động.

---

## 7. Step 6–7 · Định giá và cấu trúc SKU

### 7.1 Cấu trúc chi phí từng SKU

| SKU | Cấu hình | Giá vốn sản phẩm | Vận chuyển chặng cuối | Phí lưu kho | Tổng giá vốn |
|---|---|---|---|---|---|
| SKU kéo traffic | 350W / 100kg / 10Ah | R$ 700 | R$ 125 | R$ 25 | **R$ 850** |
| **SKU chủ lực** | **500W / 200kg / 12Ah** | R$ 780 | R$ 130 | R$ 25 | **R$ 935** |
| SKU cấu hình cao | 800W / 150kg / 12Ah | R$ 1.080 | R$ 150 | R$ 30 | **R$ 1.260** |
| SKU combo | Chủ lực + bộ phụ kiện | R$ 900 | R$ 150 | R$ 30 | **R$ 1.080** |

**Mức phí**: hoa hồng 14% ｜ quảng cáo 5% (hàng cồng kềnh) ｜ hoàn hàng 2% ｜ biên LN mục tiêu 32%

⚠️ **Chưa tính thuế** (cấu trúc thuế Brazil phức tạp, cần bổ sung theo phương án thực tế). **Biên lợi nhuận trước thuế sẽ cao hơn thực tế.**

### 7.2 Công thức định giá và tính ngược

```
Giá bán mục tiêu = tổng giá vốn ÷ (1 − % hoa hồng − % quảng cáo − % hoàn hàng − % biên lợi nhuận mục tiêu)
```

Lấy SKU chủ lực làm ví dụ (thay số đầy đủ):

```
Tử số = 780 + 130 + 25 = 935
Mẫu số = 1 − 0,14 − 0,05 − 0,02 − 0,32 = 0,47

Giá bán mục tiêu = 935 ÷ 0,47 = R$ 1.989,36
```

| SKU | Tổng giá vốn | Mẫu số | Giá bán mục tiêu tính ngược | Giá bán thực tế | Chênh lệch |
|---|---|---|---|---|---|
| SKU kéo traffic | R$ 850 | 0,47 | R$ 1.808,51 | **R$ 1.649,00** | **−R$ 159,51** |
| SKU chủ lực | R$ 935 | 0,47 | R$ 1.989,36 | **R$ 2.199,00** | **+R$ 209,64** |
| SKU cấu hình cao | R$ 1.260 | 0,47 | R$ 2.680,85 | **R$ 2.699,00** | +R$ 18,15 |
| SKU combo | R$ 1.080 | 0,47 | R$ 2.297,87 | **R$ 2.599,00** | **+R$ 301,13** |

### 7.3 ⭐ Kiểm chứng chéo với 01

| Hạng mục | Giá trị |
|---|---|
| Giá khả thi theo giá vốn do 01 tính ngược | **R$ 1.989,36** |
| Giá bán mục tiêu của SKU chủ lực tính ngược ở bước này | **R$ 1.989,36** |
| Chênh lệch | **R$ 0,00** |

**Kết luận**: ✅ **Hoàn toàn khớp.**

> Hai con số đến từ **cùng một bộ giá vốn và mức phí**, nên tất nhiên phải khớp —— nhưng chính điều đó xác nhận `cost_floor_price` của 01 và mô hình định giá của 02 dùng **cùng một bộ giả định**, không mắc lỗi phổ biến "phân tích thị trường dùng một bộ mức phí, định giá dùng bộ khác".
>
> Đáng chú ý hơn: mức R$ 1.989,36 này chỉ lệch **R$ 0,23** so với cận dưới dải giá **R$ 1.989,13** mà 01 suy ra độc lập bằng **phát hiện vùng trũng (valley)**.
> **Một con đường thuần toán học (đường cong doanh số), một con đường thuần tài chính (cấu trúc chi phí), cùng chỉ về một mức giá.**

---

## 8. Phương án giá và kiểm tra biên lợi nhuận

| SKU | Giá bán | LN gộp khả dụng trước QC | Tỷ trọng | LN sau QC | Biên LN ròng | Đạt (≥32%) | ROAS hòa vốn |
|---|---|---|---|---|---|---|---|
| SKU kéo traffic | R$ 1.649,00 | R$ 535,16 | 32,5% | R$ 452,71 | **27,5%** | ❌ | **3,08** |
| **SKU chủ lực** | **R$ 2.199,00** | **R$ 912,16** | **41,5%** | **R$ 802,21** | **36,5%** | ✅ | **2,41** |
| SKU cấu hình cao | R$ 2.699,00 | R$ 1.007,16 | 37,3% | R$ 872,21 | **32,3%** | ✅ | **2,68** |
| SKU combo | R$ 2.599,00 | R$ 1.103,16 | 42,4% | R$ 973,21 | **37,4%** | ✅ | **2,36** |

**Công thức kiểm tra (từng dòng kiểm lại được)**

```
LN gộp khả dụng trước QC = giá bán − tổng giá vốn − giá bán×0,14 − giá bán×0,02
LN sau QC                = LN gộp khả dụng trước QC − giá bán×0,05
Biên LN ròng             = LN sau QC ÷ giá bán
ROAS hòa vốn             = giá bán ÷ LN gộp khả dụng trước QC
```

**Lấy SKU chủ lực làm ví dụ**:
```
Trước QC = 2199 − 935 − 307,86 − 43,98 = 912,16   (41,5%)
Sau QC   = 912,16 − 109,95 = 802,21              (36,5%)
ROAS hòa vốn = 2199 ÷ 912,16 = 2,41
```

### 8.1 Cấu trúc biên lợi nhuận bốn bậc có đúng thiết kế vai trò của SOP không

| Vai trò | Định vị biên lợi nhuận theo SOP | Biên LN ròng thực tế của case study | Có đúng không |
|---|---|---|---|
| SKU kéo traffic giá thấp | Mỏng nhất | **27,5%** | ✅ Thấp nhất |
| SKU chủ lực | Biên LN mục tiêu | 36,5% | ✅ Cao hơn mục tiêu |
| SKU cấu hình cao | Cao hơn | 32,3% | ⚠️ **Thấp hơn SKU chủ lực** |
| SKU combo | **Cao nhất** | **37,4%** | ✅ Cao nhất |

> ⚠️ **Phát hiện một điểm không khớp với kỳ vọng của SOP: biên LN ròng của SKU cấu hình cao (32,3%) thấp hơn SKU chủ lực (36,5%).**
>
> **Nguyên nhân**: giá vốn vật tư của 800W tăng mạnh (giá vốn từ 935 → 1.260, tăng 34,8%), nhưng giá bán chỉ tăng 22,7% (2.199 → 2.699), mức tăng giá vốn vượt mức tăng giá bán.
>
> **Đây là một vấn đề cấu trúc có thật**. Dữ liệu thị trường đã báo trước: phân khúc 800W có nhiều sản phẩm nhất nhưng doanh số trung bình chỉ bằng 0.49 lần trung bình chung —— cho thấy dòng sản phẩm 800W này **nhìn chung có cấu trúc chi phí kém, không phải vấn đề riêng của bên ta**.
>
> **Cách xử lý**: SKU cấu hình cao không gánh nhiệm vụ lợi nhuận, chỉ gánh nhiệm vụ "tăng AOV + làm điểm neo giá cho SKU chủ lực". **Đây là điều chỉnh vai trò có chủ đích, không phải sơ suất.** Đã ghi rõ nhiệm vụ trong bảng SKU.

### 8.2 Phân tích dư địa lợi nhuận

| SKU | Biên LN ròng thực tế | Mục tiêu | **Dư địa** | Mức voucher dư địa gánh được |
|---|---|---|---|---|
| SKU kéo traffic | 27,5% | 32% | **−4,5%** | ❌ Không có dư địa, không được phát voucher |
| **SKU chủ lực** | **36,5%** | 32% | **+4,5%** | ✅ **R$ 98,95/đơn** |
| SKU cấu hình cao | 32,3% | 32% | +0,3% | Gần như không có dư địa |
| SKU combo | 37,4% | 32% | **+5,4%** | ✅ R$ 140,35/đơn |

### 8.3 ⭐ Sự trùng khớp giữa dư địa lợi nhuận và mệnh giá voucher

```
Dư địa lợi nhuận SKU chủ lực = R$ 2.199 × 4,5% = R$ 98,95
Mệnh giá voucher dự kiến     = R$ 100,00
Chênh lệch                   = R$ 1,05
```

> **4,5 điểm vượt biên LN mục tiêu của SKU chủ lực, quy ra tiền là R$ 98,95 —— vừa đủ để phát một voucher R$ 100.**
>
> Đây không phải con số tôi gò cho đẹp, mà là kết quả **cùng quyết định** bởi hai yếu tố "khoảng giá (thị trường cho 2.100–2.300) + cấu trúc chi phí (935)":
> thị trường sẵn sàng trả 2.199, còn giá vốn chỉ cần 1.989 là đạt biên LN 32% → ở giữa tự nhiên dư ra khoảng R$ 99.
>
> **R$ 99 này nên dùng thế nào?** SOP đã có câu trả lời: tác dụng của voucher là "**thu hẹp chênh lệch giá**". Vì vậy nên dùng nó để kéo SKU chủ lực lại gần SKU kéo traffic, chứ không để nằm trên sổ sách.

### 8.4 Xử lý SKU kéo traffic

| Hạng mục | Giá trị |
|---|---|
| Giá bán | R$ 1.649,00 |
| Biên LN mục tiêu | 32% |
| Biên LN ròng thực tế | **27,5%** |
| ROAS hòa vốn | 3,08 |
| **Có nằm trên ngưỡng hòa vốn không** | ✅ **Có** (giá hòa vốn chỉ R$ 1.113,10) |
| **Vai trò chiến lược** | SKU kéo traffic thông thường, **không phải lỗ chiến lược** |

> ✅ **Đây là một SKU kéo traffic lành mạnh**: biên lợi nhuận thấp hơn mục tiêu 4,5 điểm, nhưng **vẫn có lãi**.
> Không cần ghi chú lỗ chiến lược, cũng không cần đặt điều kiện thoát —— nó chỉ "lãi ít hơn một chút", không phải "chịu lỗ để đổi lấy lượng".
>
> **Tiêu chí phán đoán**: thấp hơn biên LN mục tiêu nhưng cao hơn ngưỡng hòa vốn = định giá theo vai trò bình thường; thấp hơn ngưỡng hòa vốn = lỗ chiến lược, bắt buộc ghi chú riêng cùng điều kiện thoát.

---

## 9. Cấu trúc SKU

| Vai trò | Nội dung | Khác biệt cấu hình | Giá bán | Biên LN ròng | Nhiệm vụ |
|---|---|---|---|---|---|
| **Kéo traffic giá thấp** | 350W / 100kg / 10Ah | Công suất thấp + tải trọng thấp | **R$ 1.649,00** | 27,5% | Kéo click, tăng hiệu quả quảng cáo |
| **Chủ lực** ⭐ | **500W / 200kg / 12Ah** | **Cấu hình khác biệt hóa** | **R$ 2.199,00** | **36,5%** | **Chịu trách nhiệm chốt đơn** |
| **Cấu hình cao** | 800W / 150kg / 12Ah | Công suất cao | **R$ 2.699,00** | 32,3% | Tăng AOV + làm điểm neo giá (**không gánh lợi nhuận**) |
| **Combo** | Chủ lực + bộ phụ kiện (mũ bảo hiểm/khóa xe/bơm) | Máy chính + phụ kiện | **R$ 2.599,00** | **37,4%** | **Tăng lợi nhuận** |

### 9.1 Kiểm tra bậc giá

| Hai bậc liền kề | Chênh giá | Biên độ | Kiểm tra |
|---|---|---|---|
| Kéo traffic → chủ lực | R$ 550 | **33,4%** | ⚠️ Hơi cao (gần ngưỡng cảnh báo 40%) → **cần dùng voucher để thu hẹp** |
| Chủ lực → cấu hình cao | R$ 500 | 22,7% | ✅ Hợp lý |
| Chủ lực → combo | R$ 400 | 18,2% | ✅ Hợp lý (combo rẻ hơn bản cấu hình cao, thắng nhờ "tặng thêm đồ" chứ không phải "giảm giá") |

> **Khoảng chênh 33,4% từ kéo traffic → chủ lực là điểm yếu duy nhất trong cấu trúc SKU này.**
> Chênh 550 real, người mua có thể dừng ở SKU kéo traffic R$ 1.649 mà không nâng cấp. **Đây chính là vấn đề voucher cần giải quyết.**

### 9.2 Thiết kế voucher

| Voucher | SKU áp dụng | Mệnh giá | Giá sau voucher | Chênh lệch được thu hẹp | Nguồn chi phí |
|---|---|---|---|---|---|
| Voucher riêng cho SKU chủ lực | **SKU chủ lực** | **R$ 100** | **R$ 2.099,00** | Kéo traffic↔chủ lực từ R$ 550 xuống **R$ 450** (27,3%) | Dư địa lợi nhuận của SKU chủ lực R$ 98,95 |

**Kiểm tra ngưỡng hòa vốn sau voucher**

| SKU | Giá sau voucher | LN gộp khả dụng trước QC | Biên LN ròng sau voucher | Có > 0 không |
|---|---|---|---|---|
| SKU chủ lực | R$ 2.099,00 | R$ 828,16 | **34,5%** | ✅ |

```
Kiểm tra sau voucher: 2099 − 935 − 2099×0,14 − 2099×0,02 = 828,16  (39,4%)
                      828,16 − 2099×0,05 = 723,21                  (34,5%)
```

**Sau voucher vẫn cao hơn biên LN mục tiêu 32%** → voucher an toàn.

> **Vì sao phát voucher cho SKU chủ lực mà không phải SKU kéo traffic?**
> - Biên LN ròng của SKU kéo traffic chỉ 27,5%, **không có dư địa**, phát voucher là thủng mục tiêu
> - SKU chủ lực có dư địa R$ 98,95, **voucher lấy đúng từ phần dư địa này**
> - Quan trọng hơn: SOP nói tác dụng của voucher là "thu hẹp chênh lệch giá" —— **thứ được thu hẹp là khoảng cách "SKU kéo traffic đến SKU chủ lực", mục đích là đẩy người mua từ SKU kéo traffic lên SKU chủ lực**. Phát voucher cho SKU kéo traffic chẳng khác nào giữ người đáng lẽ nâng cấp ở lại bậc rẻ hơn, đi ngược hướng.

---

## 10. Chiến lược giá giai đoạn đầu (SOP 1.9)

| Giai đoạn | Giá bán | Biên LN ròng | Mục đích | Điều kiện kích hoạt nâng giá lại |
|---|---|---|---|---|
| Cold start (tuần 1–4) | **R$ 1.999** | 32,2% | Nằm gần cận dưới dải giá, giành click ban đầu | Doanh số tháng ổn định ≥ 30 đơn |
| Giai đoạn nâng giá lại (tuần 5–8) | **R$ 2.099** | 34,5% | Quan sát tỷ lệ chuyển đổi có giữ được không | Tỷ lệ chuyển đổi ≥ 1% (chuẩn SOP) |
| Giai đoạn ổn định | **R$ 2.199** | 36,5% | Giá mục tiêu | — |

**Kiểm tra ràng buộc**

| Hạng mục | Giải thích |
|---|---|
| Giá giai đoạn đầu có thấp hơn ngưỡng hòa vốn không | ✅ **Không**——LN gộp trước QC ở mức R$ 1.999 vẫn còn R$ 744,16 |
| Giá hòa vốn | **R$ 1.113,10** (thấp hơn rất nhiều so với giá của mọi giai đoạn) |
| Dòng tiền có chịu được không | `【Cần xác nhận】` biên LN ròng giai đoạn đầu 32,2% vẫn nằm trên đường mục tiêu, **thực tế không phải là "hạ biên lợi nhuận nuôi trọng số"** |
| Chỉ số xác định thời điểm nâng giá lại | Dùng **khung test 7 ngày** của SOP để quan sát tỷ lệ chuyển đổi |

> **Một phát hiện đáng chú ý**: "hạ giá giai đoạn đầu" trong case study này thực ra **không thật sự hạ biên lợi nhuận** —— biên LN ròng ở mức R$ 1.999 vẫn là 32,2%, vừa đúng đường mục tiêu.
>
> Nguyên nhân là **bản thân mức giá đã có dư địa dồi dào** (thị trường trả tới 2.199, giá vốn chỉ cần 1.989 là đạt chuẩn).
> Vì vậy với sản phẩm này, động tác "hạ nhẹ biên lợi nhuận giai đoạn đầu để nuôi trọng số" **có thể làm thong thả hơn** —— có khoảng đệm an toàn gần 1.086 real, dư địa hạ giá lớn hơn nhiều so với dùng voucher.
>
> **Ngược lại**: nếu `cost_floor_price` của một sản phẩm đã sát giá thị trường (dư địa rất ít), thì "hạ giá giai đoạn đầu" sẽ thật sự ăn vào biên lợi nhuận, bắt buộc phải thận trọng. **Dư địa nhiều hay ít quyết định mức độ tự do của chiến lược nuôi trọng số.**

---

## 11. Các trường giao cho 06 Advertising

| SKU | Giá bán | LN gộp khả dụng trước QC | **ROAS hòa vốn** | % quảng cáo đề xuất | Chạy quảng cáo được |
|---|---|---|---|---|---|
| **SKU chủ lực** | R$ 2.199,00 | R$ 912,16 | **2,41** | 5% | ✅ |
| SKU cấu hình cao | R$ 2.699,00 | R$ 1.007,16 | **2,68** | 5% | ✅ |
| SKU combo | R$ 2.599,00 | R$ 1.103,16 | **2,36** | 5% | ✅ |
| SKU kéo traffic | R$ 1.649,00 | R$ 535,16 | **3,08** | 5% | ⚠️ Ngưỡng hòa vốn cao nhất, khuyến nghị ngân sách thấp |

**Lưu ý then chốt cho 06**:

> **Khoảng ROAS hòa vốn của sản phẩm này là 2,36–3,08, nằm ở phía thấp của khoảng ROI quảng cáo thường gặp (3–8).**
> Điều này có nghĩa là **sản phẩm có dư địa quảng cáo lành mạnh** —— ngưỡng hòa vốn thấp cho thấy biên lợi nhuận dày, quảng cáo dù ROI không cao cũng khó lỗ.
>
> **So sánh**: sản phẩm nhỏ (như sạc dự phòng 20000mAh) có ngưỡng hòa vốn **2,82**, nhìn có vẻ gần; nhưng ROAS của hàng nhỏ thực tế rất khó vượt 3, còn hàng cồng kềnh có AOV và dư địa lợi nhuận lớn hơn, ROAS dễ đạt trên 3 hơn.
> **Vì vậy con số "ROAS hòa vốn" phải xem cùng với "ngành hàng đó chạy được ROAS bao nhiêu"** —— chỉ nhìn ngưỡng hòa vốn cao hay thấp sẽ đánh giá sai.

---

## 12. Quét tuân thủ đề xuất

`Quét tuân thủ đề xuất: không có vi phạm`

(Không khai khống thông số, không đề xuất lách chứng nhận, không đề xuất bán dưới giá vốn lâu dài để đẩy lượng, không cam kết hiệu quả, không ra quyết định thu mua thay con người.)

---

## 13. Các trường bàn giao

```yaml
product_type: {role: "SKU lợi nhuận", differentiation: "SKU khác biệt hóa", promo_role: "SKU chủ lực"}

final_config:
  power: "500W"
  load: "200kg"          # ★ điểm tựa khác biệt hóa
  capacity: "12Ah"
  foldable: true

core_selling_point: "Motor 500W com capacidade de 200 kg"

secondary_points:
  - "Suspensão dianteira e traseira"
  - "Dobra em 3 segundos"
  - "Freio a disco + freio elétrico"
  - "Autonomia com condições de teste declaradas"

forbidden_words_seed:
  - "200 kg para 2 pessoas"
  - "qualquer ladeira"
  - "60 km"
  - "iluminação noturna"
  - "garantia de 1 ano"
  - "Xiaomi"
  - "assistência técnica completa"     # không có năng lực sửa chữa

after_sales_commitment: |
  Garantia de 6 meses para motor e bateria.
  Atendimento pelo chat com resposta em até 24 horas.
  Peças de reposição disponíveis para compra separada.

risk_mitigation:
  - {type: "Khai khống thông số", action: "Ghi điều kiện test cho quãng đường/tốc độ", target: "03 đoạn 4"}
  - {type: "Từ thương hiệu", action: "Đưa vào forbidden_words", target: "03/04/05"}
  - {type: "Hiểu lầm về phụ kiện", action: "Ảnh danh sách đóng gói ghi Não incluso", target: "04 ảnh 8"}
  - {type: "Giới hạn chức năng", action: "Ghi rõ dốc thoải/một người lái/tải trọng gồm hành lý", target: "03 đoạn 6"}
  - {type: "Cam kết sai sự thật", action: "Chỉ cam kết đổi hàng và phụ kiện, không ghi sửa chữa", target: "03 đoạn 5"}

sku_structure:
  - {role: "SKU kéo traffic", config: "350W/100kg/10Ah", price: 1649.00, net_rate: 0.275, duty: "Kéo click"}
  - {role: "SKU chủ lực", config: "500W/200kg/12Ah", price: 2199.00, net_rate: 0.365, duty: "Chốt đơn"}
  - {role: "SKU cấu hình cao", config: "800W/150kg/12Ah", price: 2699.00, net_rate: 0.323, duty: "Tăng AOV + điểm neo giá"}
  - {role: "SKU combo", config: "Chủ lực + bộ phụ kiện", price: 2599.00, net_rate: 0.374, duty: "Tăng lợi nhuận"}

main_sku: "SKU chủ lực 500W / 200kg / 12Ah"

pricing_table:
  SKU kéo traffic: {price: 1649.00, pre_ad_margin: 535.16, net_rate: 0.275}
  SKU chủ lực: {price: 2199.00, pre_ad_margin: 912.16, net_rate: 0.365}
  SKU cấu hình cao: {price: 2699.00, pre_ad_margin: 1007.16, net_rate: 0.323}
  SKU combo: {price: 2599.00, pre_ad_margin: 1103.16, net_rate: 0.374}

breakeven_roas_by_sku:
  SKU kéo traffic: 3.08
  SKU chủ lực: 2.41
  SKU cấu hình cao: 2.68
  SKU combo: 2.36

coupon_plan:
  - {sku: "SKU chủ lực", amount: 100.00, after_price: 2099.00, closes_gap: "550 -> 450", funded_by: "Dư địa lợi nhuận R$98.95"}

ramp_up_plan:
  week_1_4:  {price: 1999.00, net_rate: 0.322}
  week_5_8:  {price: 2099.00, net_rate: 0.345}
  stable:    {price: 2199.00, net_rate: 0.365}
  breakeven_floor_price: 1113.10

strategic_loss_sku: null      # biên LN của SKU kéo traffic 27.5% vẫn dương, không phải lỗ chiến lược

prelaunch_checklist:
  target_buyer: "Người dùng trưởng thành đi lại trong thành phố (có nhu cầu chở đồ)"
  core_point: "Động cơ 500W + tải trọng 200kg"
  main_competitor: "4 sản phẩm đối thủ 200kg"
  price_zone: "2100-2300"
  main_sku: "SKU chủ lực"
  profit_floor: 1113.10
  ad_suitable: true
  after_sales_risk: "Chênh lệch kỳ vọng về quãng đường/tải trọng, khó lắp ráp, hiểu lầm về phụ kiện"

pending_confirmations:
  - "Nhà cung cấp có hỗ trợ khung chịu tải 200kg không (điểm tựa khác biệt hóa, quan trọng nhất)"
  - "Thuế Brazil đã được tính vào giá bán chưa"
  - "Giá vốn thực tế của bộ phụ kiện"
```

---

## 14. Case study này chứng minh điều gì

| Kết luận | Bằng chứng |
|---|---|
| **Sự trùng khớp giữa dư địa lợi nhuận và mệnh giá voucher phản ánh cấu trúc nhất quán** | Dư địa SKU chủ lực R$ 98,95, voucher dự kiến R$ 100, chênh R$ 1,05 |
| **Voucher phải phát cho SKU có dư địa, và hướng là "thu hẹp khoảng cách tới bậc kế tiếp"** | SKU chủ lực có dư địa nên phát voucher; SKU kéo traffic 27,5% không có dư địa nên không phát |
| **"Cấu hình cao" chưa chắc biên lợi nhuận cao** | Giá vốn 800W tăng 34,8% nhưng giá bán chỉ tăng 22,7% → biên LN ròng bản cấu hình cao 32,3% **thấp hơn SKU chủ lực 36,5%** |
| **Cấu hình có cấu trúc chi phí kém không nên làm SKU chủ lực** | 800W nhiều sản phẩm nhất nhưng doanh số trung bình chỉ 0.49 lần trung bình chung → chỉ làm điểm neo giá |
| **"Hạ biên lợi nhuận giai đoạn đầu để nuôi trọng số" phụ thuộc vào dư địa** | Biên LN ròng ở R$ 1.999 vẫn 32,2% (chưa thật sự hạ); giá hòa vốn R$ 1.113 thấp hơn rất xa mọi mức giá |
| **SKU kéo traffic thấp hơn biên LN mục tiêu ≠ lỗ chiến lược** | 27,5% thấp hơn mục tiêu 32% nhưng vẫn trên ngưỡng hòa vốn → không cần ghi chú lỗ và điều kiện thoát |
| **Cam kết hậu mãi phải suy ngược từ năng lực** | Không có năng lực sửa chữa → không ghi `assistência técnica`, chỉ cam kết đổi hàng và phụ kiện |
| **ROAS hòa vốn phải xem cùng ROAS mà ngành hàng đạt được** | Sản phẩm này 2,36–3,08 nhìn có vẻ hơi cao, nhưng hàng cồng kềnh AOV cao, ROAS dễ đẩy lên hơn, thuộc khoảng lành mạnh |
| **Điểm tựa khác biệt hóa phải dựa trên năng lực** | 200kg là điểm tựa của toàn bộ logic khác biệt hóa, cũng là mục năng lực duy nhất chờ xác nhận → không làm được thì phải quay lại 01 chọn lại cấu hình |

---

**Tệp liên quan**: [Giới thiệu module](../README.md) · [Prompt định vị sản phẩm](../prompts/01_product_decision.md) · [Prompt định giá và SKU](../prompts/02_pricing_and_sku.md) · [Template bảng yêu cầu sản phẩm](../templates/output_product_requirement.md) · **Upstream**: [Case study phân tích thị trường 01](../../01_Market_Research_Agent/examples/patinete_eletrico_market.md) · **Downstream**: [03 Listing](../../03_Listing_Creative_Agent/) · [06 Advertising](../../06_Advertising_Optimization_Agent/)
