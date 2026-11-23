---
name: sop-ecom-image
description: >-
  Skill tạo ảnh sản phẩm cho thương mại điện tử xuyên biên giới, chuyên Shopee Brazil và Mercado Livre. Lên kế hoạch theo khung 9 ảnh, khóa nhận diện sản phẩm,
  tích hợp sẵn quy tắc sàn (quy định mới của ML: nền trắng/màu trơn/bối cảnh thật theo ngành hàng), kiểm tra tuân thủ cấp pixel và tự động sửa lỗi.
  Dùng khi người dùng cần làm ảnh chính, ảnh bối cảnh, ảnh chi tiết, ảnh nền trắng, bộ 9 ảnh, kiểm tra tuân thủ ảnh, đổi nền, đổi màu theo SKU.
  Các câu tiếng Việt "làm ảnh / ảnh chính / ảnh bối cảnh / ảnh chi tiết / kiểm tra tuân thủ" cũng kích hoạt (tiếng Trung 「做图 / 主图 / 场景图 / 详情图 / 合规检查」 cũng vậy).
  NOT for dựng/cắt video, chuyển đổi định dạng thuần túy, nén hàng loạt.
allowed-tools:
  - Bash(python *)
  - Read
  - Write
metadata:
  version: 0.4.0
  category: e-commerce/image-generation
  license: MIT
---

# 04 · Product Image Skill (chuyên Shopee BR / Mercado Livre)

Biến một ảnh sản phẩm + một bảng thông số thành **trọn bộ ảnh sản phẩm đúng quy chuẩn sàn, có thể đăng bán ngay**.

**Khác biệt so với các Skill tạo ảnh thương mại điện tử khác trên GitHub**: tất cả chúng đều nhắm tới Amazon / Taobao / Xiaohongshu / TikTok Shop.
Skill này chuyên về hai sàn —— **Mercado Livre (quy tắc đặc thù nhất: phân biệt nền theo ngành hàng, ảnh đầu cấm chữ không liên quan)**
và **Shopee Brazil (ảnh đầu khuyến nghị chèn chữ, phong cách poster chữ to tiếng Bồ Đào Nha với độ bão hòa cao)**, đồng thời giữ khung kế hoạch 9 ảnh.

---

## Ba lằn ranh đỏ (đọc trước, không thương lượng)

1. **Không gỡ bỏ watermark ẩn như C2PA / SynthID**
2. **Không xúi giục lách quy định gắn nhãn AI của sàn** (ví dụ "sửa qua bằng PS là khỏi phải khai ảnh AI")
3. **Không giả mạo ảnh chụp thật** —— ảnh do AI tạo không được mạo danh "100% ảnh chụp thật"

Yêu cầu tái tạo người thật có thể nhận diện → từ chối (liên quan right-of-publicity, không liên quan đến watermark).

---

## Khóa nhận diện sản phẩm (Product Identity Lock) —— bắt buộc trước mỗi lần ra ảnh

Sự cố lớn nhất khi tạo ảnh không phải "ảnh xấu", mà là **sản phẩm bị vẽ không còn giống nữa** (Logo sai chính tả, lệch màu, biến dạng hình dáng).
Vì vậy trước khi ra bất kỳ ảnh nào, phải cố định nhận diện sản phẩm và **đưa nguyên văn vào mọi prompt**.

| Trường | Mô tả | Ví dụ |
|---|---|---|
| `product_type` | Loại sản phẩm + hình dạng | Sạc dự phòng (khối chữ nhật bo góc) |
| `shape` | Mô tả hình dạng, càng cụ thể càng tốt | Thân hình chữ nhật bo góc, bán kính bốn góc khoảng 8mm |
| `color` | **Mã màu hex**, không dùng tính từ | Thân `#1C1C1E`, nút bấm `#3A3A3C` |
| `logo_text` | Chữ trên sản phẩm, ghi đúng từng ký tự | `HX-20000` (hiển thị trên màn hình) |
| `materials` | Chất liệu và xử lý bề mặt | Nhựa nhám + tấm nhôm anod hóa |
| `ports_layout` | Vị trí cổng/bộ phận | Mặt trên: USB-C×1 + USB-A×2 |
| `must_not_change` | Những điểm tuyệt đối không được đổi | Số trên màn hình, vị trí Logo, số lượng nút bấm |

> **Quy tắc**: mỗi mục trong `must_not_change` phải được lặp lại trong danh sách phủ định của **mọi** prompt về sau.
> Đây là cách hiệu quả duy nhất để tránh tình trạng "càng vẽ càng không giống".

---

## Đầu vào tối thiểu

```text
1. 1 ảnh sản phẩm (chụp vội bằng điện thoại cũng được, nền trắng/bối cảnh thật đều được)
2. Bảng thông số spec_table (kích thước/dung lượng/chất liệu, lấy từ đầu ra của 03 Listing Agent)
3. Sàn mục tiêu: shopee | mercadolivre | amazon
4. Ngành hàng (quyết định quy tắc nền của ML, xem bảng định tuyến sàn)
```

---

## Tổng quan quy trình

```text
① Khóa nhận diện → ② Định tuyến quy tắc sàn → ③ Lên kế hoạch chuỗi ảnh → ④ Lắp Prompt cho từng ảnh
→ ⑤ Ra ảnh (chọn một trong ba kênh) → ⑥ Kiểm tra tuân thủ cấp pixel (--fix tự sửa) → ⑦ Giao
```

---

## ① Định tuyến quy tắc sàn (đọc thẻ quy tắc tương ứng, đừng dựa vào trí nhớ)

| platform | Thẻ quy tắc | Khác biệt chính |
|---|---|---|
| `shopee` | [references/platform-shopee.md](references/platform-shopee.md) | Ảnh đầu **khuyến nghị chèn chữ** (poster chữ to PT-BR), độ bão hòa cao, tối đa 9 ảnh, mỗi ảnh ≤2MB |
| `mercadolivre` | [references/platform-mercadolivre.md](references/platform-mercadolivre.md) | **Nền không còn bắt buộc trắng tinh** (trắng/màu trơn/bối cảnh thật theo ngành hàng), nhưng ảnh đầu cấm chữ khuyến mãi; yêu cầu tỷ lệ chiếm khung cao nhất (~95%) |
| `amazon` | [references/platform-amazon.md](references/platform-amazon.md) | Khắt khe nhất: bắt buộc trắng tinh RGB(255,255,255) + chủ thể ≥85% + cấm mọi loại chữ |

**Lưu ý**: câu trả lời của ba sàn cho câu hỏi "ảnh đầu có được có chữ không" **mâu thuẫn nhau**, một bộ ảnh không thể dùng lại trực tiếp ——
đây chính là lý do Skill này làm thẻ quy tắc riêng cho từng sàn.

---

## ② Lên kế hoạch chuỗi ảnh

Việc lên kế hoạch đi theo **khung 9 ảnh** của repo này (Shopee tối đa 9 ảnh, vừa đúng để lên kế hoạch từng ô).

Từng vị trí ảnh (mục đích / bố cục / khung prompt / khác biệt sàn) xem
[references/scenarios-9grid.md](references/scenarios-9grid.md).

ML không giới hạn số ảnh (khuyến nghị 6–8 ảnh), 5 ảnh đầu tuân theo quy tắc ảnh đầu của ML, các ảnh còn lại có thể dùng ảnh bối cảnh.

---

## ③ Lắp Prompt: năm slot + bảy nguyên tắc sắt

Mỗi prompt ra ảnh được lắp theo năm slot:

```text
[Nhận diện sản phẩm] + [Bối cảnh và bố cục] + [Ánh sáng] + [Thông số kỹ thuật của sàn] + [Danh sách phủ định]
```

Bảy nguyên tắc sắt (đúc kết từ thực chiến, thực hiện bắt buộc từng điều):

1. **Màu dùng mã hex**, không dùng tính từ —— `#1C1C1E`, không viết "xám đậm"
2. **Tỷ lệ chiếm khung của sản phẩm phải là con số** —— `product occupies 82% of frame height`
3. **Khoảng trắng phải khai báo rõ** —— `even 9% margin on all sides`
4. **Không được bỏ danh sách phủ định** —— và phải chứa toàn bộ mục trong `must_not_change`
5. **Chừa chỗ theo sàn** —— ảnh đầu Shopee chừa 12% góc trên bên phải cho nhãn giá; ảnh đầu ML chừa khoảng trắng bốn cạnh
6. **Chữ trong ảnh theo kiến trúc ba lớp** —— slogan chính ≤4 từ / điểm bán hàng ≤7 từ / nhãn góc chỉ có số (**chỉ Shopee**; ảnh đầu ML cấm)
7. **Ra ảnh hàng loạt tốt hơn chỉnh thông số liên tục** —— một lần ra 5 bản chọn 1, đừng chỉnh tỉ mỉ từng ảnh

---

## ④ Kênh ra ảnh (chọn một trong ba, tự hạ cấp theo môi trường)

| Kênh | Điều kiện | Cách dùng |
|---|---|---|
| **A. Tạo ảnh tích hợp trong Agent** | Môi trường AI của bạn có sẵn công cụ vẽ | Giao thẳng prompt đã lắp cho công cụ tạo ảnh |
| **B. API tương thích OpenAI** | Có `$IMAGE_API_BASE` + `$IMAGE_API_KEY` | Gọi `/v1/images/edits`, ảnh tham chiếu truyền qua `image_urls` |
| **C. Chỉ xuất gói prompt** | Không có gì cả | Xuất `prompt.txt` + link công cụ online, dán thủ công |

**Định tuyến model** (nếu có):
- Ảnh bối cảnh / ảnh đời sống / thử nhiều phiên bản → model nhanh (loại Flare)
- Cần giữ Logo / chữ trên màn hình / chỉnh sửa cục bộ → model mạnh (loại Sunburst)

---

## ⑤ Sau khi ra ảnh bắt buộc qua kiểm tra pixel (không phải "nhìn qua")

```bash
python scripts/check_main_image.py anh_da_tao.png --platform mercadolivre
python scripts/check_main_image.py anh_da_tao.png --platform shopee --fix anh_da_sua.png
```

Script sẽ kiểm tra **từng pixel**: kích thước, hình vuông, tỷ lệ chiếm khung của chủ thể, độ sạch/độ đồng đều của nền, dung lượng file;
các mục lỗi được liệt kê trực tiếp; những lỗi `--fix` tự sửa được (nền trắng không tinh, khoảng trắng quá nhiều, không vuông) sẽ được sửa luôn.

**Tiêu chuẩn kiểm tra lấy từ thẻ quy tắc sàn, không phải tự nghĩ ra.** Ảnh không qua kiểm tra không được giao.

**Tự test**: [`tests/`](tests/README.md) có sẵn 5 ảnh mẫu tổng hợp (gồm cả lỗi cố ý cài vào) và kết quả mong đợi,
clone về chạy một lượt là kiểm chứng được script có hoạt động bình thường không.

---

## Hạn chế đã biết

| Hạn chế | Mô tả |
|---|---|
| **Không render thực tế** | Skill này xuất ra "kế hoạch + Prompt + kiểm tra", việc vẽ giao cho model tạo ảnh (kênh A/B/C) |
| **Không tự động phát hiện chữ trong ảnh** | Có chèn chữ vi phạm hay không cần người xác nhận (OCR phụ thuộc nặng, tạm chưa tích hợp) |
| **Quy tắc nền theo ngành hàng của ML sẽ thay đổi** | Nền trắng/bối cảnh thật chia theo ngành hàng, trước khi làm catalog lớn hãy vào Seller Center của ML đối chiếu ngành hàng hiện tại |
| **Quy tắc sàn là giá trị công khai tại thời điểm viết** | Bắt buộc kiểm tra lại trên Seller Center trước khi đăng |
| **Không thay thế retouch** | Retouch các khuyết điểm phức tạp của sản phẩm vẫn cần người làm |

---

**Quay lại**: [README module 04](README.md) · **Thẻ quy tắc**: [Shopee](references/platform-shopee.md) · [Mercado Livre](references/platform-mercadolivre.md) · [Thư viện bối cảnh 9 ảnh](references/scenarios-9grid.md)
