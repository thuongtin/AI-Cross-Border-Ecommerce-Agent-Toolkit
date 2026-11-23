# Báo cáo chỉ số ngành hàng

Nguồn dữ liệu: `sample_patinete_eletrico.csv` · Cỡ mẫu: 50 sản phẩm

## 1. Quy mô thị trường

| Chỉ số | Giá trị |
|---|---|
| Số sản phẩm trong mẫu | 50 |
| Tổng lượng bán tháng | 5,886.0 |
| Tổng doanh thu tháng | R$ 12,700,584.22 |
| Giá trung bình | R$ 2,238.56 |
| Giá trung vị | R$ 2,252.03 |
| Khoảng giá | R$ 1,500.59 – R$ 3,129.06 |
| Lượng bán tháng trung bình mỗi sản phẩm | 117.7 |
| Giá trung bình ngầm định (GMV÷lượng bán) | R$ 2,157.76 |
| Tỷ trọng doanh thu của top 10 | 71.5% |

## 2. Mức độ tập trung thương hiệu

- Số thương hiệu: **6**
- **CR3 (doanh thu): 74.1%** · CR10: 100.0% · CR10 theo lượng bán: 100.0%
- HHI: **2219.7** (0–10000, càng cao càng tập trung)

> ⚠️ Số chủ thể (6) ≤ n (10), CR10 luôn bằng 100%, không có giá trị tham khảo. Hãy dùng CR3 (74.1%) và HHI (2219.7) để đánh giá mức độ tập trung.

| # | Thương hiệu | Doanh thu | Tỷ trọng doanh thu | Tỷ trọng lượng bán | Số sản phẩm |
|---|---|---|---|---|---|
| 1 | Generic | R$ 3,800,602.19 | 29.9% | 30.5% | 12 |
| 2 | Sem marca | R$ 3,639,985.53 | 28.7% | 27.4% | 15 |
| 3 | Outras | R$ 1,969,251.04 | 15.5% | 15.3% | 10 |
| 4 | MarcaA | R$ 1,586,133.21 | 12.5% | 13.5% | 6 |
| 5 | MarcaB | R$ 1,215,716.22 | 9.6% | 8.5% | 4 |
| 6 | MarcaC | R$ 488,896.03 | 3.9% | 4.9% | 3 |

> **Đánh giá** (SOP 1.3): mức độ tập trung thương hiệu < 50% → hàng no-brand vẫn còn cơ hội; > 50% → thương hiệu top đầu chi phối mạnh, cần thận trọng.

## 3. Mức độ tập trung người bán

- Số người bán: **34**
- **CR3 (doanh thu): 46.8%** · **CR10 (doanh thu): 71.5%** · CR10 theo lượng bán: 70.6%
- HHI: **951.5**

| # | Người bán | Tỷ trọng doanh thu | Tỷ trọng lượng bán | Số sản phẩm |
|---|---|---|---|---|
| 1 | LojaGrande1 | 21.3% | 21.4% | 8 |
| 2 | LojaGrande3 | 17.0% | 16.1% | 5 |
| 3 | LojaGrande2 | 8.5% | 9.7% | 6 |
| 4 | LojaPequena15 | 5.3% | 5.5% | 1 |
| 5 | LojaPequena07 | 5.3% | 5.0% | 1 |
| 6 | LojaPequena17 | 3.4% | 3.1% | 1 |
| 7 | LojaPequena28 | 2.9% | 2.5% | 1 |
| 8 | LojaPequena18 | 2.9% | 2.5% | 1 |
| 9 | LojaPequena29 | 2.6% | 2.2% | 1 |
| 10 | LojaPequena26 | 2.5% | 2.6% | 1 |

## 4. Phân tích dải giá

- Khoảng giá: R$ 1,500.59 – R$ 3,129.06 · Độ rộng bin: R$ 162.85

### 4.1 Chia bin đều (đường cong lượng bán)

| Bin | Khoảng giá | Số sản phẩm | Tổng lượng bán | Đường cong | Tổng doanh thu | Lượng bán TB/sản phẩm |
|---|---|---|---|---|---|---|
| 1 | R$ 1,500.59–1,663.44 | 7 | 499 | ████████ | R$ 795,781.82 | 71.3 |
| 2 | R$ 1,663.44–1,826.28 | 7 | 799 | ██████████████ | R$ 1,409,872.23 | 114.1 |
| 3 | R$ 1,826.28–1,989.13 | 4 | 618 | ███████████ | R$ 1,214,826.45 | 154.5 |
| 4 | R$ 1,989.13–2,151.98 | 5 | 1,120 | ████████████████████ | R$ 2,347,217.48 | 224.0 |
| 5 | R$ 2,151.98–2,314.83 | 5 | 999 | █████████████████ | R$ 2,256,349.47 | 199.8 |
| 6 | R$ 2,314.82–2,477.67 | 5 | 875 | ███████████████ | R$ 2,070,575.57 | 175.0 |
| 7 | R$ 2,477.67–2,640.52 | 5 | 552 | █████████ | R$ 1,404,915.60 | 110.4 |
| 8 | R$ 2,640.52–2,803.37 | 5 | 241 | ████ | R$ 655,057.19 | 48.2 |
| 9 | R$ 2,803.37–2,966.21 | 2 | 56 | █ | R$ 158,402.98 | 28.0 |
| 10 | R$ 2,966.21–3,129.06 | 5 | 127 | ██ | R$ 387,585.43 | 25.4 |

### 4.2 Dò vùng trũng

Ngưỡng xác định: mức giảm tối thiểu của vùng trũng so với hai bin bên cạnh **≥ 15.0%** (thấp hơn thì coi là nhiễu)

| Bin số | Ranh giới giá | Mức giảm | Dùng làm ranh giới dải giá |
|---|---|---|---|
| 3 | R$ 1,989.13 | 22.7% | ✅ |
| 9 | R$ 2,966.21 | 55.9% | ✅ |

### 4.3 Dải giá đề xuất (cắt theo vùng trũng)

| Dải giá | Khoảng giá | Số sản phẩm | Tổng lượng bán | Tổng doanh thu | Lượng bán TB/sản phẩm |
|---|---|---|---|---|---|
| #1 | R$ 1,500.59–1,989.13 | 18 | 1,916 | R$ 3,420,480.50 | 106.4 |
| #2 | R$ 1,989.13–2,966.21 | 27 | 3,843 | R$ 8,892,518.29 | 142.3 |
| #3 | R$ 2,966.21–3,129.06 | 5 | 127 | R$ 387,585.43 | 25.4 |

> ⚠️ Cắt theo vùng trũng chỉ là **gợi ý toán học**. SOP 1.4 yêu cầu kết luận cuối cùng phải xét thêm: sản phẩm của công ty có lãi không, đối thủ có quá mạnh không. Bước này do Agent làm dựa trên cấu trúc chi phí.

## 5. Bảng chéo tổ hợp cấu hình

### Chiều: công suất

- Số giá trị: 3 · Lượng bán TB mỗi SKU toàn bộ: 117.7 · Mốc chia đều (1/n): 33.3%

| Giá trị cấu hình | Số sản phẩm | Tỷ trọng số lượng | Tổng lượng bán | Tỷ trọng lượng bán | Lượng bán TB | Đánh giá |
|---|---|---|---|---|---|---|
| 500W | 19 | 38.0% | 3,612 | 61.4% | 190.1 | Tổng lượng bán cao→nhu cầu lớn; Hiệu suất mỗi SKU cao |
| 350W | 14 | 28.0% | 1,298 | 22.1% | 92.7 | Bình thường |
| 800W | 17 | 34.0% | 976 | 16.6% | 57.4 | Bình thường |

### Chiều: tải trọng

- Số giá trị: 3 · Lượng bán TB mỗi SKU toàn bộ: 117.7 · Mốc chia đều (1/n): 33.3%

| Giá trị cấu hình | Số sản phẩm | Tỷ trọng số lượng | Tổng lượng bán | Tỷ trọng lượng bán | Lượng bán TB | Đánh giá |
|---|---|---|---|---|---|---|
| 150kg | 32 | 64.0% | 3,740 | 63.5% | 116.9 | Tổng lượng bán cao→nhu cầu lớn; Cấu hình phổ biến→cạnh tranh gắt; Thị trường lớn nhưng cạnh tranh gắt |
| 100kg | 14 | 28.0% | 1,298 | 22.1% | 92.7 | Bình thường |
| 200kg | 4 | 8.0% | 848 | 14.4% | 212.0 | Hiệu suất mỗi SKU cao; ★Cấu hình cơ hội (ít sản phẩm nhưng hiệu suất cao) |

### Chiều: dung lượng

- Số giá trị: 2 · Lượng bán TB mỗi SKU toàn bộ: 117.7 · Mốc chia đều (1/n): 50.0%

| Giá trị cấu hình | Số sản phẩm | Tỷ trọng số lượng | Tổng lượng bán | Tỷ trọng lượng bán | Lượng bán TB | Đánh giá |
|---|---|---|---|---|---|---|
| 12Ah | 36 | 72.0% | 4,588 | 78.0% | 127.4 | Tổng lượng bán cao→nhu cầu lớn |
| 10Ah | 14 | 28.0% | 1,298 | 22.1% | 92.7 | Bình thường |

> **Quy tắc đánh giá** (SOP 1.5): tổng lượng bán cao = nhu cầu lớn (tỷ trọng lượng bán ≥30%); lượng bán TB cao = hiệu suất mỗi SKU cao (gấp trên 1.2 lần mức TB chung); tỷ trọng số lượng cao = phổ biến nhưng cạnh tranh gắt (gấp trên 1.5 lần mức chia đều); **ít sản phẩm nhưng lượng bán TB cao = cấu hình cơ hội tiềm năng** (dưới 0.6 lần mức chia đều và hiệu suất cao, cần xác nhận thêm có bị nhóm top đầu chiếm không); tổng lượng bán cao nhưng lượng bán TB thấp = thị trường lớn nhưng cạnh tranh gắt.
