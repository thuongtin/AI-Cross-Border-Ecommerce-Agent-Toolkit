# Mercado Livre · Thẻ quy tắc ảnh sản phẩm (bản quy định mới 2026)

> Nguồn: Seller Center chính thức của ML (cbt.mercadolibre.com/pictures và trung tâm học tập global-selling).
> **⚠️ Quy tắc đã thay đổi**: không còn yêu cầu nền trắng tinh cho mọi ngành hàng. Trước khi đăng hãy vào Seller Center kiểm tra lại theo ngành hàng.

---

## I. 🔴 Thay đổi quan trọng nhất: nền phân biệt theo ngành hàng

Nguyên văn chính thức: **"You can now choose between white, solid or real-life backgrounds for your
listings — depending on the category."**

| Ngành hàng | Yêu cầu về nền |
|---|---|
| **Technology / Beauty / Health / Supermarket** | **Vẫn yêu cầu nền trắng** (trắng tinh là an toàn nhất) |
| **Fashion / Home / Sports / Toys / Auto / Tools / Entertainment** | **Cho phép nền bối cảnh thật/tình huống** (sản phẩm trong môi trường sử dụng thực tế) |

**Mức sàn chung (áp dụng cho mọi ngành hàng)**:

> **Nền phải sạch** —— dù là nền trắng hay bối cảnh thật, "Avoid messy or busy backgrounds",
> sản phẩm phải là nhân vật chính tuyệt đối của bức ảnh.

---

## II. Quy cách bắt buộc

| Mục | Yêu cầu |
|---|---|
| Kích thước tối thiểu | 500×500 (sản phẩm dài mảnh như bút, cạnh ngắn ≥250) |
| **Kích thước khuyến nghị** | **1200×1200** (hỗ trợ zoom) |
| Kích thước tối đa | 1920×1920 |
| Tỷ lệ | **Vuông 1:1** ("width and height must be the same") |
| Định dạng | JPG / PNG, **không gian màu RGB** (không dùng CMYK) |
| Dung lượng file | ≤ 10 MB |
| Số ảnh | Không giới hạn cứng, khuyến nghị 6–8 ảnh |

---

## III. Tỷ lệ chiếm khung —— yêu cầu cao nhất trong ba sàn ⚠️

Nguyên văn chính thức: **"the product takes up 95% of the entire image"** (sản phẩm chiếm 95% khung hình, tránh để trống).

| Mục | Giá trị |
|---|---|
| Mức chính thức | ~95% |
| Vùng tối ưu thực chiến | **80–92%** (95% gần như sát viền, chừa 8% dư an toàn hơn) |

> So sánh: Amazon ≥85%, Shopee ≥60%. **Yêu cầu tỷ lệ chiếm khung của ML là khắt khe nhất.**

---

## IV. Các mục cấm ở ảnh đầu (ảnh bìa) —— dễ dính lỗi hơn cả nền

Những nội dung sau **không được xuất hiện trong bất kỳ trường hợp nào** (chính thức liệt kê từng mục):

| Mục cấm | Mô tả |
|---|---|
| ❌ Từ thuộc tính của sàn | `Mais vendido`(Bestseller), `Full`, `MercadoLíder`, `Oferta relâmpago` |
| ❌ Watermark | Logo/chữ/chữ ký bán trong suốt |
| ❌ Khung viền | Bất kỳ khung viền trang trí nào |
| ❌ Logo không phải của chính sản phẩm | Logo shop của người bán, logo nhà cung cấp |
| ❌ Banner khuyến mãi | Nhãn góc sale lớn, đồng hồ đếm ngược |
| ❌ Ảnh ghép nhiều sản phẩm | Các chú thích kiểu "different colors and models" |
| ❌ Mã QR / thông tin liên hệ / link mạng xã hội | — |
| ❌ Chữ không thuộc sản phẩm | Bất kỳ chữ nào không liên quan đến sản phẩm |

**Chỉ từ ảnh thứ hai trở đi** mới được: nhiều góc chụp, bối cảnh sử dụng, trưng bày bao bì.

---

## V. Tóm tắt quy tắc chữ (đối chiếu Shopee)

| Vị trí | Shopee BR | Mercado Livre |
|---|---|---|
| Ảnh đầu | ✅ Khuyến nghị chèn chữ (≤20% khung hình) | ❌ Cấm chữ không liên quan |
| Ảnh phụ | ✅ Khuyến nghị | ✅ Được chú thích điểm bán hàng (không phải từ thuộc tính của sàn) |

**Kết luận: một bộ ảnh không thể dùng chung cho Shopee và ML, ảnh đầu bắt buộc làm riêng.**

---

## VI. Thông số kiểm tra pixel (tương ứng scripts/check_main_image.py)

```bash
python scripts/check_main_image.py anh.png --platform mercadolivre
```

| Kiểm tra | Ngưỡng | Căn cứ |
|---|---|---|
| Kích thước tối thiểu | ≥ 500px, **<1200 cảnh báo** | Mức tối thiểu / khuyến nghị chính thức |
| Hình vuông | Tỷ lệ rộng/cao 1:1 (±1%) | "width and height must be the same" |
| Tỷ lệ chiếm khung của chủ thể | ≥ 80%, **khuyến nghị 85–95%** | Mức ~95% chính thức |
| Độ đồng đều của nền | Tỷ lệ màu chủ đạo ở dải viền ≥ 90% (**mục thông tin**) | Nền bối cảnh thật được phép không đồng đều, chỉ nhắc "có thể lộn xộn" |
| Dung lượng file | ≤ 10 MB | Giới hạn chính thức |

> Khác biệt với Amazon: ML **không bắt buộc** nền gần trắng —— script kiểm tra với ML chỉ đo "nền có đồng đều, sạch hay không",
> không đo "có trắng tinh hay không". Nếu ngành hàng của bạn thuộc Technology/Beauty/Health/Supermarket, hãy chạy lại thêm một lượt
> theo chuẩn nền trắng của `--platform amazon`.
