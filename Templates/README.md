# Templates · Thư viện template dùng chung giữa các module

Các template ở đây **không gắn với một Agent cụ thể** và có thể được nhiều module dùng chung.

| File | Công dụng | Đối tượng dùng chính |
|---|---|---|
| [`product_brief_template.md`](./product_brief_template.md) | **Sản phẩm trung gian chuẩn** — hợp đồng giao tiếp giữa ba module | 03 / 04 / 05 |
| [`keyword_analysis_template.md`](./keyword_analysis_template.md) | Bảng phân tích từ khóa theo 3 bảng xếp hạng (SOP 1.8) | 03 (đầu vào có thể lấy từ 01) |
| [`cost_pricing_template.md`](./cost_pricing_template.md) | Mô hình tính giá (SOP 1.9 / 3.2) | 02 (Phase 2) |
| [`output_qa_checklist.md`](./output_qa_checklist.md) | Checklist tự kiểm tra trước khi bàn giao (bản in) | Tất cả |

---

## Khác biệt so với template bên trong Agent

| | `Templates/` cấp gốc | `templates/` bên trong Agent |
|---|---|---|
| Phạm vi | Dùng chung giữa các module | Riêng cho một module |
| Độ ổn định | Sửa sẽ ảnh hưởng nhiều module | Sửa chỉ ảnh hưởng module đó |
| Ví dụ | `product_brief_template` | `input_image_brief` |

> **Quy tắc**: nếu một template chỉ được một Agent dùng, để nó trong thư mục của Agent đó; nếu có từ hai Agent trở lên dùng, chuyển lên đây.

---

## Hợp đồng sản phẩm trung gian

Ba module Phase 1 giao tiếp với nhau qua các trường được định nghĩa trong `product_brief_template.md`:

```text
03 Listing Creative ──► product_brief ──► 04 Product Image
                                      └──► 05 Product Video
```

**Quy tắc chặn**: khi `core_selling_point` hoặc `forbidden_words` để trống, module phía sau bắt buộc từ chối chạy và báo lỗi, không được tự suy đoán.

---

**Quay lại**: [Trang chủ dự án](../README.md) · [Phân rã kiến trúc](../docs/00_Architecture_SOP_to_Agent.md)
