# samples · Dữ liệu mẫu

> ⚠️ **Toàn bộ là dữ liệu tổng hợp (synthetic)**, dùng để kiểm tra môi trường chạy script và minh họa khả năng làm sạch định dạng, **không đại diện cho bất kỳ thị trường thật nào**.
> Được tạo bởi [`scripts/make_sample.py`](../scripts/make_sample.py) (`random.seed(20261013)`, tái lập được).

---

## Các file

| File | Mô tả |
|---|---|
| `sample_patinete_eletrico.csv` | Bảng xuất gốc (50 dòng), **cố ý trộn đủ kiểu định dạng dữ liệu bẩn** |
| `sample_patinete_eletrico.normalized.json` | Đầu ra của `shaduola_parser.py` |
| `sample_patinete_eletrico.metrics.md` | Báo cáo của `market_metrics.py` (cho người đọc) |
| `sample_patinete_eletrico.metrics.json` | Như trên (cho máy đọc) |

---

## Vì sao dữ liệu mẫu phải "bẩn"

Bảng xuất ngành hàng thực tế không bao giờ sạch sẽ. Mẫu này cố ý trộn các định dạng dưới đây để kiểm tra logic làm sạch:

| Dạng dữ liệu bẩn | Vị trí xuất hiện | Kết quả mong đợi |
|---|---|---|
| `R$ 2.199,90` | Giá | Phân cách hàng nghìn + thập phân kiểu châu Âu → `2199.9` |
| `R$ 2,199.90` | Giá | Định dạng kiểu Mỹ → `2199.9` |
| `1.234` | Lượng bán | Dấu chấm làm phân cách hàng nghìn → `1234` |
| `4 tháng` / `2025-06-15` / `420 ngày` / `420` | Thời gian đăng bán | Quy về số ngày |
| Chuỗi rỗng | Doanh thu tháng (25% số dòng) | Tính bù bằng `giá × lượng bán tháng` |

Chạy xong, `meta.row_count_kept` phải bằng `row_count_raw` (50 = 50), tức là không có dòng nào bị bỏ nhầm.

---

## Cách tái lập

```bash
cd ../scripts
python make_sample.py                    # tạo lại CSV (kết quả giống file trong repo)
python shaduola_parser.py ../samples/sample_patinete_eletrico.csv
python market_metrics.py ../samples/sample_patinete_eletrico.normalized.json \
    --bins 10 --config-fields "công suất,tải trọng,dung lượng" \
    -o ../samples/sample_patinete_eletrico.metrics
```

---

## Kết quả chính bạn sẽ thấy khi chạy trọn vẹn

| Chỉ số | Giá trị | Ghi chú |
|---|---|---|
| Số sản phẩm trong mẫu | 50 | — |
| Số thương hiệu | 6 | Chỉ có 6 → **kích hoạt cảnh báo CR10 vô nghĩa**, nên chuyển sang CR3 |
| CR3 thương hiệu | 74.1% | Mức độ tập trung khá cao (trong dữ liệu tổng hợp, thương hiệu top đầu có nhiều sản phẩm) |
| Số người bán | 34 | CR10 = 71.5% |
| Khoảng giá | R$ 1,500.59 – 3,129.06 | Độ rộng bin R$ 162.85 |
| **Vùng trũng phát hiện được** | **2** (R$ 1,989.13 / R$ 2,966.21) | Nằm ở bin 3 và bin 9 |
| **Dải giá đề xuất** | **3** | Tương ứng với "chia từ vùng trũng đến vùng trũng" của SOP 1.4 |
| Chiều cấu hình | công suất 3 giá trị / tải trọng 3 giá trị | 500W và 150kg là cấu hình phổ biến (mỗi loại 30 sản phẩm, 60%) |

> **Nếu số vùng trũng không phải là 2**, nghĩa là môi trường Python hoặc tham số của bạn khác với tài liệu này — hãy kiểm tra đã dùng `--bins 10`, `--valley-min-drop 0.15` chưa.

---

**Quay lại**: [Hướng dẫn scripts](../scripts/README.md) · [Mô tả module 01](../README.md)
