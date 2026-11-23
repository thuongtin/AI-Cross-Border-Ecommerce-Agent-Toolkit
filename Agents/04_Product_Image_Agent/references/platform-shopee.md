# Shopee Brazil · Thẻ quy tắc ảnh sản phẩm

> Nguồn: PDF chính thức của Shopee "Quy chuẩn đăng bán Shopee Mall" + thực tiễn của người bán năm 2026.
> **Kiểm tra lại trên Seller Center trước khi đăng**, quy tắc sẽ thay đổi.

---

## I. Quy cách bắt buộc

| Mục | Yêu cầu |
|---|---|
| Số lượng | Mỗi listing tối đa **9 ảnh** (gồm ảnh đầu) |
| Kích thước | Tối thiểu 500×500; **khuyến nghị từ 1024×1024 trở lên** (người bán top thường dùng 1500–2000) |
| Tỷ lệ | **Vuông 1:1** —— ảnh không vuông sẽ bị tự động cắt, có thể cắt mất sản phẩm |
| Định dạng | JPG (khuyến nghị) / PNG |
| Dung lượng mỗi ảnh | **≤ 2 MB** (một số ngành hàng 5MB) —— khắt khe nhất trong ba sàn, ra ảnh xong bắt buộc nén |
| Không gian màu | sRGB |
| Ảnh mô tả | Thêm tối đa 12 ảnh, tối thiểu 900×900 |

---

## II. Quy tắc ảnh đầu (ảnh bìa)

| Mục | Yêu cầu |
|---|---|
| Nền | **Màu trơn, ưu tiên trắng**; bối cảnh thật làm mờ tông sáng có thể chấp nhận |
| Tỷ lệ chiếm khung của sản phẩm | ≥ **60%** (bắt buộc với Shopee Mall); vùng tối ưu thực chiến **70–85%** |
| Khung viền | ❌ Cấm (không được có viền trắng/viền đen/khung trang trí) |
| Ảnh ghép | ❌ Cấm (một ảnh một sản phẩm, nhiều biến thể dùng tính năng variation) |
| Người | ❌ Ảnh đầu cấm người mẫu/người (**ngoại lệ: thời trang, trang sức, đồ đeo**) |
| Watermark | Chỉ được đặt ở bốn góc, không được che phủ diện rộng lên sản phẩm |

### Về chữ —— hoàn toàn ngược với Amazon ⚠️

| Quy tắc | Nội dung |
|---|---|
| Người bán thông thường | **Cho phép và khuyến nghị** chèn chữ: hình minh họa/chữ/phụ kiện **không được lớn hơn chủ thể sản phẩm** và **dưới 20% khung hình** |
| Shopee Mall | Ảnh bìa **cấm** chữ, watermark, đồ họa |

**Gu thẩm mỹ của Shopee Brazil** (khác nhiều so với các site Đông Nam Á, không dùng chung một bộ ảnh được):

| Mục | Sở thích của thị trường Brazil |
|---|---|
| Ngôn ngữ chữ | **Tiếng Bồ Đào Nha** |
| Phong cách | Nhiệt tình, táo bạo, **độ bão hòa cao, tông màu ấm** |
| Yếu tố điển hình | Chữ to phần trăm giảm giá, câu ngắn điểm bán hàng, nhãn góc quà tặng |

---

## III. Chuỗi 9 ảnh khuyến nghị (hướng tới chuyển đổi)

| Vị trí ảnh | Nội dung | Chữ |
|---|---|---|
| 1 Ảnh đầu | Ảnh chính diện nền trắng, sản phẩm chiếm 70% | ✅ Chữ to PT-BR (≤20% khung hình) |
| 2 | Góc nghiêng/mặt sau/45° | Được, ít |
| 3 | Cận cảnh chất liệu/chi tiết | Được chú thích điểm bán hàng |
| 4 | Ảnh bối cảnh/đời sống | Được |
| 5 | **So sánh kích thước** (bàn tay/đồng xu/ghi kích thước) | ✅ Ghi số |
| 6 | Infographic điểm bán hàng (2–3 điểm bán hàng) | ✅ |
| 7 | Biến thể/tùy chọn màu | ✅ |
| 8 | Danh sách đóng gói (có/không có phụ kiện) | ✅ Ghi `Não incluso` |
| 9 | Yếu tố tạo niềm tin (chứng nhận/bảo hành/đập hộp) | Được |

> Ảnh 5 và ảnh 8 là **vị trí phòng ngừa đánh giá tiêu cực**: hiểu lầm kích thước và hiểu lầm phụ kiện là hai nguồn đánh giá tiêu cực lớn nhất (xem case study ở module 07).

---

## IV. Thông số kiểm tra pixel (tương ứng scripts/check_main_image.py)

```bash
python scripts/check_main_image.py anh.png --platform shopee
```

| Kiểm tra | Ngưỡng | Căn cứ |
|---|---|---|
| Kích thước tối thiểu | ≥ 500px, **<1024 cảnh báo** | Mức tối thiểu / khuyến nghị chính thức |
| Hình vuông | Tỷ lệ rộng/cao 1:1 (±1%) | Ảnh không vuông bị tự động cắt |
| Tỷ lệ chiếm khung của chủ thể | ≥ 60% (Mall) / **khuyến nghị 70–85%** | Chính thức + thực chiến |
| Độ sạch của nền | Tỷ lệ pixel gần trắng ở dải viền ≥ 98% (khi dùng nền trắng) | Ảnh đầu ưu tiên màu trơn trắng |
| Dung lượng file | ≤ 2 MB | Giới hạn chính thức |
| Tỷ lệ chữ trong ảnh | ≤ 20% khung hình | **Người xác nhận** (script không chạy OCR) |
