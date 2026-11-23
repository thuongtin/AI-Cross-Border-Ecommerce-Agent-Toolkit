# scripts · Lấy dữ liệu và tính chỉ số

> **Lý do lớp này tồn tại: cái gì tính được thì đừng để mô hình đoán.**
>
> Mức độ tập trung, tỷ trọng, chia bin, bảng chéo đều là **phép tính tất định** — script tính 100 lần vẫn ra cùng kết quả, mô hình tính thì mỗi lần có thể khác.
> Agent chỉ phụ trách bước cuối: "những con số này nghĩa là gì, bước tiếp theo làm gì."

Phụ thuộc: **chỉ thư viện chuẩn của Python** (XLSX cần `openpyxl`, tùy chọn; CSV không cần thư viện nào).

---

## Ba bước chạy trọn vẹn

```bash
# 1) Chạy thử với dữ liệu mẫu trước (kiểm tra môi trường, dữ liệu là tổng hợp)
python make_sample.py

# 2) Xem tình trạng nhận diện cột (bắt buộc làm khi lần đầu dùng nguồn dữ liệu mới)
python shaduola_parser.py ../samples/sample_patinete_eletrico.csv --profile

# 3) Chuyển đổi + tính toán
python shaduola_parser.py ../samples/sample_patinete_eletrico.csv
python market_metrics.py ../samples/sample_patinete_eletrico.normalized.json \
    --bins 10 --config-fields "công suất,tải trọng"
```

Tạo ra hai file:
- `<tên>.metrics.json` — cho Agent / script phía sau sử dụng
- `<tên>.metrics.md` — cho người đọc, cũng là tài liệu chính nộp cho Agent

---

## `shaduola_parser.py` — Chuẩn hóa định dạng

Gom đủ kiểu định dạng xuất từ các sàn về một Schema cố định.

### Lọc được những loại dữ liệu bẩn nào

Dữ liệu xuất ra thường trông như dưới đây, logic làm sạch đều đã bao phủ:

| Trường hợp | Ví dụ | Kết quả xử lý |
|---|---|---|
| Ký hiệu tiền tệ | `R$ 2.199,90` / `¥1,234.56` / `USD 99.9` / `1.299.000₫` | `2199.90` |
| Dấu phân cách hàng nghìn (dấu chấm) | `1.234` | `1234` |
| Dấu phân cách hàng nghìn (dấu phẩy) | `1,234` | `1234` |
| Số thập phân kiểu châu Âu | `1.234,56` | `1234.56` |
| Đơn vị số lượng tiếng Trung / tiếng Việt | `1.2万` / `1,5 triệu` / `3000+` | `12000` / `1500000` / `3000` |
| Ký hiệu giá trị rỗng | `-` / `N/A` / `暂无` / `không có` / `null` | `None` |
| Thời gian đăng bán | `30天` / `30 ngày` / `2个月` / `2 tháng` / `2025-06-15` / `365` | Số ngày (số nguyên) |
| Thiếu doanh thu tháng | — | Tính bù bằng `giá × lượng bán tháng` |

### Nhận diện tên cột

Bảng ánh xạ có sẵn bao phủ các tên cột phổ biến bằng tiếng Trung / tiếng Việt / tiếng Anh / tiếng Bồ Đào Nha (xem `DEFAULT_MAPPING` trong script). **Cột nào không nhận diện được thì chỉ định thủ công bằng `--mapping`**:

```bash
# mapping.json
{"price": ["Cột giá của tôi", "Preço Final"], "monthly_sales": ["Lượng bán 30 ngày"]}

python shaduola_parser.py data.xlsx --mapping mapping.json
```

### Schema đầu ra

```json
{
  "meta": {
    "source_file": "data.csv",
    "row_count_raw": 50,
    "row_count_kept": 50,
    "column_map": { "price": "Giá", "monthly_sales": "Lượng bán tháng" }
  },
  "items": [
    {
      "title": "...", "price": 2199.0, "monthly_sales": 210,
      "monthly_revenue": 461790.0,
      "seller": "...", "brand": "...", "rating": 4.6,
      "review_count": 126, "listing_age_days": 420,
      "url": "...", "category": null
    }
  ]
}
```

---

## `market_metrics.py` — Tính chỉ số

### Tính những chỉ số nào (ứng với chương SOP)

| Khối đầu ra | Chỉ số | SOP tương ứng |
|---|---|---|
| Quy mô thị trường | Tổng lượng bán / tổng doanh thu / giá trung bình / giá trung vị / lượng bán TB mỗi sản phẩm / giá trung bình ngầm định | 1.2 |
| Mức độ tập trung thương hiệu | Số thương hiệu / **CR3** / CR10 / **HHI** / bảng xếp hạng Top | 1.3 |
| Mức độ tập trung người bán | Số người bán / CR3 / CR10 / HHI / bảng xếp hạng Top | 1.3 |
| Dải giá | Đường cong lượng bán chia bin đều / **dò vùng trũng** / dải giá đề xuất | 1.4 |
| Bảng chéo cấu hình | Mỗi giá trị cấu hình: số sản phẩm / tỷ trọng số lượng / tổng lượng bán / tỷ trọng lượng bán / lượng bán trung bình + đánh giá bốn chiều | 1.5 |

### Dò vùng trũng thế nào (triển khai SOP 1.4)

Nguyên văn SOP:

> Quan sát đỉnh và đáy của đường cong, **chia một dải giá tương đối trọn vẹn từ vùng trũng này đến vùng trũng kia**.

Có ba điểm chính khi triển khai, đều được sửa ra sau khi vấp lỗi:

| # | Điểm chính | Vì sao |
|---|---|---|
| 1 | **Dò trên đường cong gốc, mặc định không làm mượt** | Trung bình trượt 3 điểm sẽ xóa phẳng vùng trũng cục bộ dốc. Vùng trũng `799 → 618 → 1120` trong mẫu, sau trung bình trượt thành `638 → 845 → 912` (tăng đơn điệu), vùng trũng biến mất luôn |
| 2 | **Lọc mức giảm đáng kể** (mặc định 15%) | Nếu không, nhiễu sẽ tạo ra rất nhiều vùng trũng giả. Mức giảm = mức giảm **nhỏ hơn** của vùng trũng so với hai điểm lân cận |
| 3 | **Giới hạn số dải giá** (mặc định 5) | Khi có quá nhiều vùng trũng thì lấy vài vùng sâu nhất theo mức giảm, phần còn lại ghi vào `trimmed_valleys`, có thể chỉnh lại bằng `--max-bands` |

```bash
# Điều chỉnh tham số
python market_metrics.py data.normalized.json --bins 12 --valley-min-drop 0.20 --max-bands 6
```

### Một cái bẫy của CR-n

**Khi số chủ thể ≤ n, CR-n luôn bằng 100%, hoàn toàn vô nghĩa.**
Script sẽ tự phát hiện trường hợp này và nhắc chuyển sang dùng CR3 và HHI:

```
> ⚠️ Số chủ thể (6) ≤ n (10), CR10 luôn bằng 100%, không có giá trị tham khảo. Hãy dùng CR3 (74.1%) và HHI (2219.7) để đánh giá mức độ tập trung.
```

### Khai báo chiều cấu hình thế nào

Có hai cách:

1. **Cấu hình nằm ở cột riêng** → dùng `--config-fields <tên cột>`, script đọc trực tiếp
2. **Cấu hình chỉ nằm trong tiêu đề** → script sẽ thử trích số + đơn vị từ title bằng regex (`500W` / `150kg` / `20000mAh`), hỗ trợ từ khóa tiếng Trung, tiếng Việt, tiếng Anh, tiếng Bồ Đào Nha

```bash
--config-fields "công suất,tải trọng" # kích hoạt trích xuất từ tiêu đề (cũng nhận 功率,承重)
--config-fields "potencia,peso_max"   # đọc trực tiếp khi cột có tồn tại
```

Số mục trích xuất lỗi sẽ được ghi trong báo cáo (`Số sản phẩm không trích được chiều này: N`) — **phải để mắt đến con số này**, tỷ lệ trích được quá thấp nghĩa là định dạng tiêu đề không thống nhất hoặc tên chiều không đúng.

---

## Logic đánh giá bốn chiều (SOP 1.5)

Script tự động gắn nhãn cho từng giá trị cấu hình:

| Nhãn | Điều kiện | Ý nghĩa |
|---|---|---|
| `Tổng lượng bán cao→nhu cầu lớn` | Tỷ trọng lượng bán ≥ 25% | Nhu cầu thị trường tập trung ở đây |
| `Hiệu suất mỗi SKU cao` | Lượng bán trung bình > trung bình chung × 1.2 | Sản phẩm cấu hình này bán chạy |
| `Cấu hình phổ biến→cạnh tranh gắt` | Tỷ trọng số lượng > tỷ trọng chung × 1.5 | Nguồn cung nhiều, chắc chắn cạnh tranh gắt |
| `★Cấu hình cơ hội` | Số sản phẩm ≤ 30% và lượng bán trung bình > trung bình chung × 1.2 | **Ít sản phẩm nhưng hiệu suất cao** — cần xác nhận thêm có bị nhóm top đầu chiếm không |

> Tiêu chuẩn cuối cùng của SOP là: **tổng lượng bán cao + lượng bán trung bình cao + công ty làm được + lợi nhuận chấp nhận được + hậu mãi kiểm soát được**.
> Script chỉ bao phủ được hai mục đầu (có dữ liệu), ba mục sau bắt buộc do Agent đánh giá dựa trên nguồn lực công ty và cấu trúc chi phí.

---

## Vì sao không dùng BI / Pivot Table Excel có sẵn

| | Script này | Pivot Table Excel |
|---|---|---|
| Tái lập được | ✅ Tham số cố định thì kết quả cố định | ❌ Phụ thuộc thao tác tay, khó tái lập |
| Truy vết được | ✅ Xuất JSON, mọi con số đều truy ngược được | ⚠️ Công thức giấu trong ô |
| Tự động hóa được | ✅ Bản V2 kết nối API là nối thẳng vào được | ❌ |
| Dò vùng trũng | ✅ Có sẵn lọc mức độ đáng kể | ❌ Phải nhìn biểu đồ bằng mắt |
| Thân thiện với Agent | ✅ JSON có cấu trúc | ❌ |

**Khác biệt cốt lõi**: Excel là để người xem, script là để **quy trình** dùng.

---

## Hạn chế đã biết

| Hạn chế | Giải thích |
|---|---|
| **Không thu thập dữ liệu** | Chỉ chuyển đổi định dạng và tính toán. Nguồn dữ liệu phải tự xuất (Shaduola / Seller Center / công cụ bên thứ ba) |
| **Không tính thuế phí** | Cơ cấu thuế phí của Brazil phức tạp (thuế bang/thuế liên bang/thuế nhập khẩu), không xử lý ở lớp chỉ số; giai đoạn định giá cần bổ sung riêng |
| **Không tính "hiệu quả sản phẩm mới"** | SOP 1.2 đặc biệt nhắc đến "tình hình lượng bán sản phẩm mới", và ghi chú "dữ liệu Shaduola không chính xác". Cần trường `listing_age_days` mới làm được, độ chính xác có hạn, nên đối chiếu thủ công |
| **Không đánh giá thật giả** | Không kiểm tra bản thân dữ liệu lượng bán có đáng tin hay không |
| **Trích xuất cấu hình mang tính heuristic** | Định dạng tiêu đề muôn hình vạn trạng, tỷ lệ trích được có thể thấp, báo cáo sẽ ghi rõ số lỗi |
| **HHI chưa hiệu chỉnh theo ngành** | Ngưỡng HHI khác nhau theo ngành, script chỉ đưa giá trị gốc, việc đánh giá giao cho Agent |

---

**Quay lại**: [Giới thiệu module 01](../README.md) · **Bước tiếp theo**: nộp `<tên>.metrics.md` cùng [`templates/input_category_research.md`](../templates/input_category_research.md) cho Agent
