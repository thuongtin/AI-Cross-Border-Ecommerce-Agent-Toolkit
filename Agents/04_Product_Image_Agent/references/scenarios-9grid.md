# Thư viện bối cảnh 9 ảnh (chuỗi Shopee × khác biệt giữa các sàn)

> Mỗi vị trí ảnh đều có: **mục đích / bố cục / khung prompt / khác biệt giữa các sàn**.
> Cách dùng: chọn chuỗi theo `planning_mode` → áp template cho từng vị trí ảnh → điền các trường "khóa nhận diện sản phẩm" vào
> `[PRODUCT]` → phần khác biệt giữa các sàn quyết định chèn chữ và nền.
>
> Tỷ lệ chiếm khung, màu sắc, khoảng trắng trong prompt **bắt buộc phải là con số** (xem bảy nguyên tắc sắt trong SKILL.md).

---

## Khung Prompt chung (năm slot)

```text
[Khối nhận diện PRODUCT]
{product_type}, {shape}, body color {hex}, {materials},
logo/text "{logo_text}" rendered exactly as in reference image,
{ports_layout}

[Bối cảnh và bố cục]
{scene}, {camera_angle}, product occupies {n}% of frame,
{margin} even margin on all sides

[Ánh sáng]
{lighting}, soft shadows, accurate colors, sRGB

[Thông số kỹ thuật của sàn]
square 1:1, {min_px}px or larger, clean {background_type} background

[Danh sách phủ định]
no text overlay (except {allowed_text}), no watermark, no border, no collage,
no extra objects, keep {must_not_change} unchanged
```

---

## Vị trí ảnh 1 · Ảnh đầu / ảnh chính diện nền trắng

| Mục | Nội dung |
|---|---|
| Mục đích | CTR trên kết quả tìm kiếm —— tấm ảnh duy nhất quyết định sống còn |
| Bố cục | Chính diện ngang tầm mắt, sản phẩm chiếm **Shopee 70–85% / ML 85–95%**, căn giữa |
| Khung | `studio packshot of [PRODUCT], front view, on {bg}, soft studio lighting` |
| **Shopee** | Nền trắng + **chèn chữ PT-BR** (slogan chính ≤4 từ, tổng chữ ≤20% khung hình, chừa 12% góc trên bên phải cho nhãn góc) |
| **ML** | Nền **chỉ cần sạch** (trắng/màu trơn/bối cảnh thật theo ngành hàng), ❌ cấm mọi chữ không liên quan |
| Amazon | Trắng tinh `#FFFFFF`, không có chữ |

**Template chèn chữ Shopee BR**:

```text
top banner text "{slogan chính ≤4 từ}" in bold {color} PT-BR typography,
occupying less than 20% of the image area, never covering the product
```

---

## Vị trí ảnh 2 · Nhiều góc chụp

| Mục | Nội dung |
|---|---|
| Mục đích | Để người mua xác nhận hình dáng —— giảm hoàn hàng vì "nhận hàng không giống" |
| Bố cục | Mặt bên / mặt sau / 45°, **cùng ánh sáng cùng nền** với ảnh đầu |
| Khung | `[PRODUCT], {angle} view, same studio setup as packshot` |
| Khác biệt | Ba sàn như nhau, nền trắng |

> ⚠️ Mấu chốt của tính nhất quán: **hướng sáng, nhiệt độ màu, màu nền phải giống hệt ảnh đầu**, nếu không sẽ trông như ảnh chắp vá.

---

## Vị trí ảnh 3 · Cận cảnh chất liệu / chi tiết

| Mục | Nội dung |
|---|---|
| Mục đích | Chứng minh cảm giác chất lượng —— làm chỗ dựa cho mức giá |
| Bố cục | Macro, lấy nét vào {điểm chất liệu then chốt} (cổng kết nối / vân dệt / lớp phủ) |
| Khung | `extreme close-up macro of [PRODUCT] {detail_point}, shallow depth of field` |
| Khác biệt | Ba sàn như nhau; Shopee có thể chèn một từ điểm bán hàng |

---

## Vị trí ảnh 4 · Ảnh bối cảnh / đời sống

| Mục | Nội dung |
|---|---|
| Mục đích | Giúp người mua hình dung khi đã sở hữu sản phẩm |
| Bố cục | Sản phẩm trong môi trường sử dụng thật, chiếm 55–70%, môi trường là phụ |
| Khung | `[PRODUCT] placed on {scene}, contextual photography, natural lighting` |
| **ML** | ✅ **Với ngành hàng Fashion/Home/Sports, ảnh này có thể dùng thẳng làm ảnh đầu** (quy định mới cho phép bối cảnh thật) |
| Shopee | ✅ Vị trí ảnh phụ |

> Bối cảnh phải **đáng tin**: phối cảnh, tỷ lệ, bóng tiếp xúc, phản chiếu đều phải đúng —— sofa không được lơ lửng trong phòng.

---

## Vị trí ảnh 5 · So sánh kích thước ⭐ Vị trí phòng ngừa đánh giá tiêu cực

| Mục | Nội dung |
|---|---|
| Mục đích | Chống hiểu lầm kích thước —— thuốc đặc trị cho đánh giá tiêu cực về kích thước |
| Bố cục | Sản phẩm + vật tham chiếu (bàn tay / đồng xu / giấy A4) hoặc nền trắng có đường ghi kích thước |
| Khung | `[PRODUCT] with size annotation, {reference_object} for scale, clean background` |
| Chữ | ✅ Ghi số (`19cm` / `20000mAh`), **dùng cm không dùng inch** (Brazil dùng hệ mét) |
| Khác biệt | Shopee ✅ / ML ✅ (ảnh phụ được phép chú thích) |

---

## Vị trí ảnh 6 · Infographic điểm bán hàng

| Mục | Nội dung |
|---|---|
| Mục đích | Biến `secondary_points[]` của Agent 03 thành hình ảnh |
| Bố cục | Sản phẩm một bên + danh sách icon điểm bán hàng (tối đa 3 mục) |
| Khung | `infographic style, [PRODUCT] on one side, {n} benefit callouts with icons on the other` |
| Chữ | ✅ Mỗi điểm bán hàng ≤7 từ PT-BR (ví dụ: `Carrega 3 aparelhos ao mesmo tempo`) |
| Khác biệt | Shopee ✅ / ML ✅ (ảnh phụ) |

---

## Vị trí ảnh 7 · Biến thể / đổi màu theo SKU

| Mục | Nội dung |
|---|---|
| Mục đích | Một ảnh thể hiện toàn bộ biến thể, dẫn người mua vào link biến thể |
| Bố cục | Ảnh lớn biến thể chính + hàng ô màu các biến thể |
| Khung | `[PRODUCT] in {color_1} as main, smaller thumbnails showing {color_2}, {color_3}` |
| Lưu ý | **Đổi màu thì chỉ đổi màu, hình dáng/Logo/vị trí cổng không được động vào bất cứ thứ gì** (`must_not_change` của khóa nhận diện) |
| ML | Nhiều màu thì dùng tính năng variation để tạo link riêng, trên ảnh không ghi "có màu khác" |

---

## Vị trí ảnh 8 · Danh sách đóng gói ⭐ Vị trí phòng ngừa đánh giá tiêu cực

| Mục | Nội dung |
|---|---|
| Mục đích | Chống hiểu lầm kiểu "tưởng là có kèm cáp sạc" (case study module 07: đánh giá tiêu cực loại hiểu lầm chiếm 38.5%) |
| Bố cục | Ảnh flat lay: bày hết mọi thứ trong hộp ra, có gì chụp nấy |
| Khung | `flat lay of package contents: [PRODUCT], {included_items}, on neutral background` |
| Chữ | ✅ **Bắt buộc ghi `Não incluso`** (mục không kèm theo) —— chỉ một dòng này là cắt luôn đánh giá tiêu cực về phụ kiện |
| Khác biệt | Shopee ✅ / ML ✅ |

---

## Vị trí ảnh 9 · Yếu tố tạo niềm tin

| Mục | Nội dung |
|---|---|
| Mục đích | Xóa băn khoăn cuối cùng (bảo hành / chứng nhận / đập hộp) |
| Bố cục | Nhãn bảo hành / chứng nhận ANATEL / quá trình đập hộp |
| Khung | `[PRODUCT] with warranty badge "{text}", trust signal composition` |
| Chữ | ✅ `1 ano de garantia` / `ANATEL homologado` |
| Lưu ý | Dấu chứng nhận phải là **thực sự có**, không được làm giả (lằn ranh đỏ tuân thủ) |

---

## Quy tắc nhất quán (trường bắt buộc của Campaign Style Lock)

Trước khi ra cả bộ ảnh, điền bảng này trước, **mọi prompt đều mang theo nguyên văn**:

```yaml
campaign_style_lock:
  light_direction: "top-left"        # Thống nhất cho cả bộ
  color_temperature: "5200K neutral"
  background_family: "white studio"  # hoặc "warm lifestyle"
  saturation: "accurate, no oversaturation"
  camera_height: "eye-level"
  must_not_change:
    - "screen digits"
    - "logo position"
    - "port count"
```

**Không được đổi dù một chữ** —— khi người mua lướt qua 9 ảnh, phong cách nhảy lung tung trông như ảnh ăn cắp.
