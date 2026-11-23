# Template · Sản phẩm trung gian chuẩn (Product Brief)

> **Đây là hợp đồng giao tiếp giữa ba module.** 03 tạo ra nó, 04 và 05 dùng nó.
> Nó không phải "template đầu vào của một Agent nào đó", mà là **định nghĩa giao diện dữ liệu giữa các module**.

---

## Vì sao cần nó

Nếu không có sản phẩm trung gian thì chuyện gì xảy ra:

```text
❌ Không có hợp đồng
Người vận hành chạy xong 03, được một đống nội dung
→ Đưa cho 04 làm ảnh, 04 tự "hiểu" lại điểm bán hàng một lần (hiểu lệch)
→ Đưa cho 05 làm video, 05 lại tự hiểu thêm một lần nữa (lại lệch tiếp)
→ Điểm bán hàng ở ba nơi không khớp nhau, người xem thấy như ghép nhặt
```

```text
✅ Có hợp đồng
03 xuất ra product_brief có cấu trúc
→ 04 đọc thẳng core_selling_point (không hao hụt do diễn giải)
→ 05 đọc thẳng cùng một core_selling_point
→ Ba nơi khớp nhau hoàn toàn
```

---

## Định nghĩa trường

### Trường bắt buộc (mục chặn)

| Trường | Kiểu | Định nghĩa | Ai tạo ra | Ai sử dụng |
|---|---|---|---|---|
| `product_name` | string | Tên gọi chung của sản phẩm (bằng ngôn ngữ thị trường mục tiêu) | Người làm | 03/04/05 |
| `target_market` | string | Thị trường mục tiêu | Người làm | 03/04/05 |
| `platform` | enum | Sàn mục tiêu | Người làm | 03/04/05 |
| **`core_selling_point`** | string | **Điểm bán hàng chủ lực trong một câu**, bắt buộc kiểm chứng được | 03 | **04/05** |
| **`secondary_points[]`** | array | 3–5 điểm bán hàng phụ | 03 | **04/05** |
| **`spec_table`** | object | Bảng thông số (nguồn số liệu duy nhất) | Người làm → 03 kiểm tra | **04/05** |
| **`forbidden_words[]`** | array | Danh sách từ cấm | 03 (quét tuân thủ) | **04/05** |
| **`usage_scope_confirmed[]`** | array | Các ngữ cảnh sử dụng đã xác nhận | Người làm → 03 xác nhận | **04/05** |
| `package_content[]` | array | Danh sách trong hộp (kèm "không bao gồm gì") | Người làm | 04 |
| `warranty` | string | Thông tin bảo hành | Người làm | 04/05 |

> **Khi một trong sáu trường in đậm để trống, 04/05 bắt buộc từ chối chạy.** Đây không phải "khuyến nghị", mà là chặn cứng.

### Trường tùy chọn

| Trường | Kiểu | Định nghĩa | Công dụng |
|---|---|---|---|
| `title_final` | string | Tiêu đề cuối cùng | CTA kết video của 05 |
| `keyword_classified` | object | Kết quả phân loại từ khóa 7 nhóm | Điểm bán hàng trên ảnh chính của 04, cài từ khóa vào phụ đề của 05 |
| `visual_tone_hint` | string | Tông hình ảnh | Thống nhất phong cách giữa 04/05 |
| `review_insights[]` | array | Quy nguyên nhân đánh giá tiêu cực | Đoạn lưu ý của 03, chọn ngữ cảnh cho 05 |
| `brand_authorization[]` | array | Thương hiệu đã được ủy quyền | Mốc chuẩn để chặn vi phạm tuân thủ |

---

## Template

```yaml
# ─────────────────────────────────────────────
# PRODUCT BRIEF · Hợp đồng giao tiếp giữa các module
# ─────────────────────────────────────────────
meta:
  brief_id: ""                 # để tiện truy vết, vd: PB-20261013-001
  created_at: ""               # YYYY-MM-DD
  source_agent: "03-Listing-Creative"
  version: "v0.1"

# ── Thông tin cơ bản ──
identity:
  product_name*: ""
  product_name_local: ""       # phiên bản theo ngôn ngữ thị trường mục tiêu
  category*: ""
  platform*: ""                # shopee | mercadolivre | amazon | tiktokshop | shopify
  target_market*: ""

# ── Đầu ra cốt lõi (mục chặn cho module phía sau) ──
core:
  core_selling_point*: ""      # một câu, bắt buộc kiểm chứng được
  secondary_points*: []        # 3–5 điểm
  usage_scope_confirmed*: []   # whitelist ngữ cảnh sử dụng

# ── Thông số (nguồn số liệu duy nhất) ──
params:
  spec_table*: {}              # mọi con số trong đầu ra đều phải lấy từ đây
  package_content*: []
  warranty*: ""

# ── Tuân thủ ──
compliance:
  forbidden_words*: []
  brand_authorization: []
  certifications: []           # ⚠️ chỉ điền chứng nhận thực sự đang có

# ── Hình ảnh & từ khóa ──
creative:
  keyword_classified: {}
  title_final: ""
  visual_tone_hint: ""

# ── Insight từ đánh giá ──
insights:
  review_insights: []
  # - type: loại hiểu lầm | loại chất lượng | loại vận chuyển | loại thông số
  #   content: ""
  #   action: ""
```

---

## Cách sử dụng

### 03 tạo ra nó như thế nào

Sau khi chạy xong `02_description_builder.md` + `03_compliance_guard.md`, copy thẳng từ khối "Trường bàn giao cho module phía sau" trong đầu ra.

### 04 / 05 sử dụng nó như thế nào

**Kiểm tra phụ thuộc trước khi chạy** (bắt buộc):

```text
1. Đọc product_brief
2. Kiểm tra sáu trường chặn có khác rỗng hay không
3. Bất kỳ trường nào rỗng → báo lỗi và dừng:

   [UPSTREAM_MISSING]
   Trường bị thiếu: <tên trường>
   Ảnh hưởng: <phần nào không thể hoàn thành>
   Vui lòng chạy xong 03 Listing Creative Agent và bổ sung đủ các trường trên trước.
```

**Tuyệt đối không được** dùng giá trị suy đoán để điền khi thiếu trường chặn.

---

## Kiểm tra tính nhất quán dữ liệu

Sau khi ba module chạy xong, đối chiếu ngang một lượt:

| Trường | Đầu ra 03 | Đầu ra 04 | Đầu ra 05 | Khớp |
|---|---|---|---|---|
| Con số trong `core_selling_point` | | | | ✅ / ❌ |
| Thông số chính trong `spec_table` | | | | ✅ / ❌ |
| Số lần dính `forbidden_words` | | | | ✅ / ❌ |
| Mô tả tông hình ảnh | | | | ✅ / ❌ |

> **Lệch thông số là lỗi hay gặp nhất của quy trình này.** 03 ghi `20000mAh`, ảnh của 04 ghi thành `20.000mAh`, lồng tiếng của 05 lại đọc "hai mươi nghìn mi-li-ampe giờ" — từng cái riêng lẻ đều không sai, nhưng đặt cạnh nhau thì thấy rõ cảm giác ghép nhặt. Chạy xong bắt buộc đối chiếu một lần.

---

**Tài liệu liên quan**: [Phân rã kiến trúc](../docs/00_Architecture_SOP_to_Agent.md) · [Checklist tự kiểm tra](../docs/04_Result_Checklist.md)
