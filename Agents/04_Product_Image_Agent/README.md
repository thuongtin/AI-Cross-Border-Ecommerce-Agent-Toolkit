# 04 · Product Image Agent

**Agent tạo ảnh chính và ảnh chi tiết** · Từ một câu điểm bán hàng đến 9 Prompt sẵn sàng để ra ảnh.

---

## I. Nó giải quyết vấn đề gì

Hình ảnh là đòn bẩy lớn nhất lên tỷ lệ chuyển đổi — nhưng cũng là phần dễ làm sai nhất.

| Vấn đề | Biểu hiện | Module này giải quyết thế nào |
|---|---|---|
| **Không biết 9 ảnh nên đặt gì** | Chụp cả đống ảnh, chức năng trùng lặp, thiếu thông tin quan trọng | Khung phân vai 9 ảnh cố định, mỗi ảnh có nhiệm vụ rõ ràng |
| **Dính lỗi quy chuẩn ảnh chính của sàn** | ML: ảnh chính chèn chữ bị gỡ; Shopee: ảnh chính không có điểm bán hàng nên CTR thấp | Thông số `platform_variant`, xuất ra hai phương án |
| **Viết Prompt ra ảnh không ra hiệu quả** | Ném cho AI một câu, ảnh ra không dùng được | Prompt có cấu trúc: chủ thể + chất liệu + vị trí ánh sáng + bố cục + thông số + negative prompt |
| **Text trong ảnh quá dài** | Chữ trên ảnh chen chúc, người mua không đọc được | Mỗi ảnh ghi rõ giới hạn số từ + số từ thực tế |

**Đầu ra**: bảng kế hoạch nội dung 9 ảnh + Prompt ra ảnh cho từng ảnh (kèm negative prompt) + text trong ảnh + kiểm tra tuân thủ (compliance).

---

## II. Nguồn gốc khung 9 ảnh (đã xác nhận áp dụng)

SOP 3.3 có viết một câu:

> **Logic tạo 9 ảnh thương mại điện tử**: "9 ảnh nên được tạo theo thứ tự sau:"

**Danh sách cụ thể sau câu này trong file PDF gốc ở dạng hình ảnh, trích xuất văn bản không khôi phục được.** Vì vậy khung 9 ảnh của module này được **suy ra từ cấu trúc 7 phần của trang chi tiết trong SOP + quy chuẩn hình ảnh của sàn**.

> ✅ **Đã xác nhận ngày 2026-10-13: áp dụng khung 9 ảnh do repo này suy ra.** Không chờ bổ sung bản gốc SOP nữa.
> Căn cứ suy luận và phân vai xem phần V bên dưới. Nếu sau này có được danh sách gốc của SOP mà không khớp với khung này, hãy hiệu chỉnh theo bản gốc SOP và cập nhật [`CHANGELOG`](../../CHANGELOG.md).

**Logic suy luận** (ba bước, có thể kiểm chứng lại):

| Bước | Căn cứ | Kết quả |
|---|---|---|
| 1 | Cấu trúc 7 phần trang chi tiết trong SOP (lời chào/điểm bán hàng/bối cảnh/thông số/hậu mãi/lưu ý/tag) | Chuyển thành các "vị trí ảnh dạng thông tin": ảnh điểm bán hàng, ảnh thông số, ảnh bối cảnh, ảnh hậu mãi |
| 2 | Quy chuẩn cứng của sàn (ảnh chính Shopee được có chữ / ML cấm chữ; ML cần ảnh bảo hành) | Bổ sung "ảnh chính" và "ảnh hậu mãi/bảo hành", đồng thời đánh dấu khác biệt giữa các sàn |
| 3 | Các nguyên nhân đánh giá tiêu cực hay gặp (thiếu phụ kiện, kích thước không như mong đợi) | Bổ sung "ảnh kích thước/so sánh" và "ảnh danh sách đóng gói" |

> Bước 3 là điểm khác biệt giữa khung này và "mẫu 9 ảnh phổ thông": **nó coi việc "phòng ngừa đánh giá tiêu cực" là một trong các mục tiêu thiết kế vị trí ảnh**, chứ không chỉ nghĩ đến "trưng bày sản phẩm".

---

## III. Các chương SOP được bao phủ

| SOP | Nội dung | Nằm ở Prompt nào |
|---|---|---|
| **3.3** | Logic tạo 9 ảnh thương mại điện tử | `01_image_plan_9grid.md` |
| **3.3** | Khung nội dung trang chi tiết (dùng làm nguồn thông tin cho ảnh) | `01_image_plan_9grid.md` |
| **2.3** | Shop mới chạy nhiều shop cùng mẫu cần làm khác biệt hóa hình ảnh | `01_image_plan_9grid.md` (chế độ variant) |
| **3.6** | Quảng cáo không có click → đổi ảnh chính | `02_image_prompt_generator.md` (chế độ iterate) |
| Toàn chương | Tuân thủ hình ảnh | IMAGE COMPLIANCE GUARD trong `00_system.md` |

---

## IV. Quy trình làm việc

```text
Đầu vào: đầu ra của 03 Listing Creative (core_selling_point / secondary_points / spec_table / forbidden_words)
        ▲
        └── [Quy tắc chặn] core_selling_point hoặc forbidden_words rỗng → từ chối thực thi, báo lỗi
                         ▼
        ┌──────────────────────────────────┐
        │ 00_system.md                     │  Vai trò + quy chuẩn ảnh của sàn + bộ chặn tuân thủ hình ảnh
        └──────────────┬───────────────────┘
                       ▼
        ┌──────────────────────────────────┐
        │ 01_image_plan_9grid.md           │  Step 1  Lên kế hoạch nội dung 9 ảnh (mỗi ảnh đặt gì)
        │                                  │  Step 2  Viết text trong ảnh (kiểm soát số từ)
        └──────────────┬───────────────────┘
                       ▼
        ┌──────────────────────────────────┐
        │ 02_image_prompt_generator.md     │  Step 3  Tạo Prompt ra ảnh cho từng ảnh
        │                                  │  Step 4  Negative Prompt + kiểm tra tuân thủ
        └──────────────┬───────────────────┘
                       ▼
        Đầu ra: output_image_prompt_pack.yaml  →  giao cho ImageGen / Midjourney / Jimeng... để render thực tế
```

**Ranh giới của module**: chỉ phụ trách "toàn bộ công việc thiết kế trước khi ra ảnh", **không phụ trách render**. Render giao cho công cụ tạo ảnh, kiểm soát chất lượng sau render do phần C của [`docs/04_Result_Checklist.md`](../../docs/04_Result_Checklist.md) đảm nhận.

---

## IV.5. Dạng Skill (mới ở v0.4)

Module này đã được tổ chức theo cấu trúc Skill chuẩn của cộng đồng (đối chiếu với các Skill tạo ảnh thương mại điện tử hàng đầu trên GitHub),
**có thể được cài đặt và gọi trực tiếp bởi bất kỳ Agent nào đọc `SKILL.md` như Claude Code / Codex / Cursor / WorkBuddy**:

```text
04_Product_Image_Agent/
├── SKILL.md                        # Điểm vào cho Agent: nhận diện ý định → định tuyến quy tắc → ra ảnh → kiểm tra
├── references/
│   ├── platform-shopee.md          # Thẻ quy tắc Shopee Brazil (ảnh đầu khuyến nghị chèn chữ / tối đa 2MB / 9 ảnh)
│   ├── platform-mercadolivre.md    # Thẻ quy tắc ML (quy định mới 2026: nền theo ngành hàng / chiếm 95% / ảnh đầu cấm chữ khuyến mãi)
│   ├── platform-amazon.md          # Thẻ đối chiếu Amazon (chuẩn nền trắng khắt khe nhất)
│   └── scenarios-9grid.md          # Thư viện bối cảnh 9 ảnh (mỗi vị trí: mục đích/bố cục/khung prompt/khác biệt sàn)
├── scripts/
│   └── check_main_image.py         # Kiểm tra tuân thủ cấp pixel + --fix tự sửa (thuần Pillow) ⭐
├── tests/
│   ├── README.md                   # 5 ảnh mẫu tổng hợp + kết quả mong đợi (clone về là tự test được) ⭐
│   └── *.png                       # ml_pass · amazon_fail · shopee_fix/fixed · ml_chaotic
├── prompts/ templates/ examples/   # Bộ bốn thành phần sẵn có
```

**Cách dùng**:

```bash
# Kiểm tra tuân thủ bắt buộc sau khi ra ảnh (cấp pixel, không phải "nhìn qua")
python scripts/check_main_image.py anh_da_tao.png --platform mercadolivre
python scripts/check_main_image.py anh_da_tao.png --platform shopee --fix anh_da_sua.png
```

Ảnh không qua kiểm tra **không được giao**; những lỗi `--fix` tự sửa được (nền trắng không tinh, khoảng trắng quá nhiều, không vuông) sẽ được sửa luôn và kiểm tra lại.

---

## V. Khung 9 ảnh

| # | Vị trí ảnh | Nhiệm vụ | Nguồn thông tin | Khác biệt giữa các sàn |
|---|---|---|---|---|
| 1 | **Ảnh chính** | Nhìn một cái là biết "đây là gì" | `product_name` + thẻ quy tắc sàn | ⚠️ ML: ảnh đầu cấm chữ khuyến mãi; Shopee: khuyến nghị chèn chữ |
| 2 | **Ảnh điểm bán hàng chủ lực** | Hình ảnh hóa điểm bán hàng chính trong một câu | `core_selling_point` | Chung |
| 3 | **Ảnh thông số kỹ thuật** | Trực quan hóa `spec_table` | `spec_table` | Chung |
| 4 | **Ảnh bối cảnh sử dụng A** | Đưa người xem vào bối cảnh chính | `usage_scope[0]` | Chung |
| 5 | **Ảnh bối cảnh sử dụng B** | Bối cảnh phụ / đối tượng người dùng | `usage_scope[1]` | Chung |
| 6 | **Ảnh cận cảnh chi tiết** | Chất liệu, tay nghề, bộ phận quan trọng | `secondary_points` | Chung |
| 7 | **Ảnh kích thước/so sánh** | Xóa bỏ "kích thước không như mong đợi" | Mục kích thước trong `spec_table` | ML nên có |
| 8 | **Ảnh danh sách đóng gói** | Làm rõ "có gì / không có gì" | `package_content` | **Ảnh then chốt phòng ngừa đánh giá tiêu cực** |
| 9 | **Ảnh hậu mãi/bảo hành** | Giảm băn khoăn khi mua | `warranty` | **Shopee Brazil rất nên có** |

> Ảnh số 8 và 9 là hai ảnh dễ bị bỏ qua nhất nhưng mang lại lợi ích trực tiếp nhất: **ảnh số 8 phòng ngừa đánh giá tiêu cực loại hiểu lầm kiểu "tưởng là có kèm X", ảnh số 9 là yếu tố tạo niềm tin trong bối cảnh luật bảo vệ người tiêu dùng Brazil.**

---

## VI. File Prompt

| File | Chức năng |
|---|---|
| [`prompts/00_system.md`](./prompts/00_system.md) | System Prompt: vai trò + quy chuẩn ảnh của sàn + IMAGE COMPLIANCE GUARD |
| [`prompts/01_image_plan_9grid.md`](./prompts/01_image_plan_9grid.md) | Task Prompt: kế hoạch 9 ảnh + text trong ảnh |
| [`prompts/02_image_prompt_generator.md`](./prompts/02_image_prompt_generator.md) | Task Prompt: Prompt ra ảnh cho từng ảnh + negative prompt |

## VII. Template và case study

| File | Mô tả |
|---|---|
| [`templates/input_image_brief.md`](./templates/input_image_brief.md) | Đầu vào chuẩn |
| [`templates/output_image_prompt_pack.yaml`](./templates/output_image_prompt_pack.yaml) | Đầu ra chuẩn |
| [`examples/pet_carrier.md`](./examples/pet_carrier.md) | Case study thực tế: túi đựng thú cưng đi ra ngoài (kế hoạch 9 ảnh đầy đủ) |

---

## VIII. Hạn chế đã biết

| Hạn chế | Mô tả |
|---|---|
| **Không render ảnh** | Chỉ tạo Prompt và đặc tả thiết kế, ra ảnh thực tế dùng công cụ tạo ảnh |
| **Khung 9 ảnh là bản suy luận** | Chưa trích xuất được danh sách gốc của SOP, đã xác nhận dùng bản suy luận của repo này (xem phần II); sau này có bản gốc thì hiệu chỉnh |
| **Không tự phán đoán ảnh đã tạo có tuân thủ hay không** | Kiểm soát chất lượng sau render cần người thực hiện theo checklist phần C |
| **Không tạo dấu chứng nhận** | Sản phẩm không có chứng nhận tuyệt đối không ra ảnh chứng nhận, đây là chặn cứng |
| **Có ràng buộc khi dùng người thật** | Người do AI tạo không được giống cá nhân thật có thể nhận diện; không được dùng ảnh người mua thật để tạo lại |
| **Quy chuẩn sàn sẽ thay đổi** | Quy tắc ảnh chính thay đổi thường xuyên, **bắt buộc kiểm tra lại trước khi đăng** |

---

**Quay lại**: [Mục lục Agents](../README.md) · **Thượng nguồn**: [03 Listing Creative](../03_Listing_Creative_Agent/) · **Tài liệu**: [Quy chuẩn trường dữ liệu sàn](../../docs/02_Platform_Output_Spec.md) · [Lằn ranh đỏ tuân thủ](../../docs/03_Compliance_Guard.md)
