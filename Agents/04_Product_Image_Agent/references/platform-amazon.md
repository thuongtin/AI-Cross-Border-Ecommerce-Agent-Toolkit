# Amazon · Thẻ quy tắc ảnh sản phẩm (dùng để đối chiếu)

> Amazon không phải chiến trường chính của Skill này, nhưng đây là sàn có **tiêu chuẩn kiểm tra khắt khe nhất** ——
> ảnh nền trắng đạt chuẩn Amazon thì dùng thẳng được cho các ngành hàng nền trắng của Shopee và ML.

---

## Quy cách bắt buộc

| Mục | Yêu cầu |
|---|---|
| Kích thước tối thiểu | Cạnh ngắn nhất **1000px** (thấp hơn thì tắt tính năng zoom) |
| Kích thước khuyến nghị | 2000×2000 |
| Tỷ lệ | 1:1 |
| Định dạng | JPG (ưu tiên) / PNG / GIF |
| **Nền** | **Trắng tinh RGB(255,255,255) —— bắt buộc** |
| **Tỷ lệ chiếm khung của chủ thể** | **≥ 85% khung hình** (khoảng trắng quá nhiều sẽ bị từ chối) |
| Chữ | ❌ Ảnh chính cấm mọi loại chữ, Logo, watermark |
| Số ảnh | 1 ảnh chính + tối đa 8 ảnh phụ |

---

## Khác biệt căn bản với hai sàn còn lại

| | Amazon | Shopee BR | Mercado Livre |
|---|---|---|---|
| Nền ảnh đầu | Trắng tinh **bắt buộc** | Ưu tiên màu trơn trắng | **Theo ngành hàng** (trắng/màu trơn/bối cảnh thật) |
| Chèn chữ ảnh đầu | ❌ Cấm | ✅ **Khuyến nghị** | ❌ Cấm |
| Tỷ lệ chiếm khung của chủ thể | ≥85% | ≥60% (Mall) | ~95% |
| Dung lượng tối đa mỗi ảnh | 10 MB | **2 MB** | 10 MB |

---

## Thông số kiểm tra

```bash
python scripts/check_main_image.py anh.png --platform amazon
```

| Kiểm tra | Ngưỡng |
|---|---|
| Độ tinh của nền trắng | Tỷ lệ pixel gần trắng ở dải viền ≥ 98% (dung sai 3) |
| Tỷ lệ chiếm khung của chủ thể | ≥ 85% |
| Kích thước tối thiểu | ≥ 1000px |
| `--fix` | Kéo pixel gần trắng về trắng tinh + cắt/bù viền về ~87% |
