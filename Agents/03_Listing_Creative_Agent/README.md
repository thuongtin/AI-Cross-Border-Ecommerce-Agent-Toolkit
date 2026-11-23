# 03 · Listing Creative Agent

**Agent tạo nội dung sản phẩm** · Từ một mớ từ khóa lộn xộn thành một bộ Listing có thể đăng bán ngay.

> **Skill hóa (v0.4)**: bổ sung script kiểm tra tuân thủ trước khi đăng và điểm vào cho Agent
> [`SKILL.md`](SKILL.md). **Số ký tự là giá trị `len()` đo thực tế** (chữ `á` trong PT-BR chiếm 2 byte,
> tính theo byte sẽ báo nhầm là vượt giới hạn):
>
> ```bash
> # Tuân thủ tiêu đề (vượt giới hạn / từ cấm / từ khuyến mãi / nhồi từ khóa / độ phủ từ khóa cốt lõi)
> python scripts/title_lint.py "Tiêu đề" --platform shopee --forbidden "iPhone,Samsung"
> # Tính nhất quán thông số (mọi con số trong nội dung phải truy được về spec_table)
> python scripts/spec_consistency.py --spec examples/spec_table.csv --text chi_tiet.md
> ```
>
> Bảng quy tắc xem tại [`references/platform-title-rules.md`](references/platform-title-rules.md).

---

## 1. Nó giải quyết vấn đề gì

SOP 3.3 nói mục tiêu của Listing là "giúp trang sản phẩm có khả năng kéo click và chuyển đổi". Nhưng thực tế, người vận hành hay bị kẹt ở ba chỗ:

| Điểm đau | Biểu hiện | Module này giải quyết thế nào |
|---|---|---|
| **Không biết phân loại từ khóa** | Cào về 90 từ từ ba bảng xếp hạng, nhét hết vào tiêu đề, nhồi từ khóa nên ngược lại bị giảm thứ hạng | Bắt buộc chia 7 nhóm từ, tách riêng từ rủi ro |
| **Tiêu đề không có cấu trúc** | Nghĩ gì viết nấy, từ khóa chính bị chôn ở giữa | Công thức 5 đoạn cố định, bắt buộc đặt từ khóa chính trong 30 ký tự đầu |
| **Trang chi tiết không viết ra được điểm bán hàng** | Chép đối thủ, viết toàn tính từ, sót thông số | Cấu trúc 7 đoạn + ánh xạ điểm bán hàng về sự thật + kiểm tra tính nhất quán thông số |

**Sản phẩm đầu ra**: 2–3 tiêu đề dự phòng, trang chi tiết hoàn chỉnh, danh sách điểm bán hàng, bảng thông số, bảng phân loại từ khóa, kết quả quét tuân thủ.

---

## 2. Các chương SOP được bao phủ

| SOP | Nội dung | Nằm ở Prompt nào |
|---|---|---|
| **1.8** | Bảng từ khóa: trích từ ba bảng xếp hạng → từ tần suất cao → chia 7 nhóm → ghép tiêu đề | `01_keyword_to_title.md` |
| **3.3** | Xây dựng Listing: lưu ý khi viết tiêu đề + cấu trúc trang chi tiết | `01_keyword_to_title.md` / `02_description_builder.md` |
| **2.3** | Khởi động shop mới: cùng sản phẩm trên nhiều shop bắt buộc phải khác biệt hóa | `01_keyword_to_title.md` (chế độ biến thể) |
| **3.4** | Khởi động một sản phẩm nhiều link: test nhiều bộ tiêu đề / ảnh chính / trang chi tiết | `01_keyword_to_title.md` (chế độ biến thể) |
| **3.6** | Quảng cáo "có hiển thị nhưng không có click" → quay lại sửa tiêu đề | `01_keyword_to_title.md` (chế độ lặp) |
| **Toàn bộ** | Lằn ranh đỏ tuân thủ | `03_compliance_guard.md` |

---

## 3. Quy trình làm việc

```text
┌─────────────────────────────────────────────────────────┐
│ Đầu vào: input_product_brief.md (hồ sơ SP + 3 bảng từ)  │
└────────────────────────┬────────────────────────────────┘
                         ▼
        ┌────────────────────────────────┐
        │ 00_system.md                   │  Vai trò + quy tắc sàn + chốt chặn tuân thủ
        └────────────────┬───────────────┘
                         ▼
        ┌────────────────────────────────┐
        │ 01_keyword_to_title.md         │  Step 1  Chia từ khóa thành 7 nhóm
        │                                │  Step 2  Tạo tiêu đề (2–3 bản dự phòng)
        └────────────────┬───────────────┘
                         ▼
        ┌────────────────────────────────┐
        │ 02_description_builder.md      │  Step 3  Trang chi tiết 7 đoạn
        │                                │  Step 4  Danh sách điểm bán hàng + bảng thông số
        └────────────────┬───────────────┘
                         ▼
        ┌────────────────────────────────┐
        │ 03_compliance_guard.md         │  Step 5  Quét tuân thủ → chặn cứng
        └────────────────┬───────────────┘
                         ▼
        Đầu ra: output_listing_pack.md
              ├── core_selling_point     ──► bàn giao cho 04 / 05
              ├── secondary_points[]
              ├── spec_table
              ├── keyword_classified
              └── forbidden_words[]
```

> **Step 5 không phải tùy chọn.** Đầu ra của bước quét tuân thủ (`forbidden_words[]`) là danh sách chặn cứng của 04 và 05, bỏ qua bước này đồng nghĩa với đẩy rủi ro xuống khâu sau.

---

## 4. Cách sử dụng

### Lộ trình tối thiểu (3 bước)

```text
1. Sao chép templates/input_product_brief.md, điền hồ sơ sản phẩm + 3 bảng từ khóa
2. Chạy lần lượt: 00_system → 01_keyword_to_title → 02_description_builder → 03_compliance_guard
3. Dùng phần B trong docs/04_Result_Checklist.md để tự kiểm tra từng mục
```

### Ba chế độ làm việc

Cùng một Agent hỗ trợ ba chế độ, chuyển đổi bằng trường `mode` trong template đầu vào:

| Chế độ | Mục đích | Khác biệt |
|---|---|---|
| `single` | Đăng bán một link thông thường | Xuất 1 bộ phương án hoàn chỉnh + 2–3 tiêu đề dự phòng |
| `variant` | **A/B test nhiều link** (SOP 3.4) | Xuất 2–4 bộ phương án **khác biệt hóa**, tiêu đề / điểm bán hàng / ngữ cảnh mỗi bộ đi một hướng |
| `iterate` | **Sửa lại khi quảng cáo không chạy** (SOP 3.6) | Nhập phương án hiện có + triệu chứng, chỉ sửa phần được chỉ định, phần còn lại giữ nguyên |

### Chuyển sàn

Trường `platform` quyết định giới hạn ký tự và cấu trúc:

| platform | Giới hạn tiêu đề | Cấu trúc trang chi tiết |
|---|---|---|
| `shopee` | 120 ký tự (30 ký tự đầu có trọng số cao nhất) | Cấu trúc đầy đủ 7 đoạn |
| `mercadolivre` | **60 ký tự** | Características principais + Ficha Técnica |
| `amazon` | 200 ký tự | 5 bullet point + cấu trúc A+ |
| `tiktokshop` | Theo từng thị trường | Mô tả ngắn + đưa điểm bán hàng lên đầu |
| `shopify` | Khuyến nghị 70 | Mô tả dài + đoạn SEO |

---

## 5. Các file Prompt

| File | Vai trò |
|---|---|
| [`prompts/00_system.md`](./prompts/00_system.md) | System Prompt: vai trò + quy tắc sàn + quy tắc ngôn ngữ + chốt chặn tuân thủ (dùng chung cho ba task) |
| [`prompts/01_keyword_to_title.md`](./prompts/01_keyword_to_title.md) | Task Prompt: chia từ khóa 7 nhóm → trích từ tần suất cao → tạo tiêu đề |
| [`prompts/02_description_builder.md`](./prompts/02_description_builder.md) | Task Prompt: trang chi tiết 7 đoạn + danh sách điểm bán hàng + bảng thông số |
| [`prompts/03_compliance_guard.md`](./prompts/03_compliance_guard.md) | Task Prompt: quét tuân thủ độc lập (cũng có thể dùng riêng để rà soát lại Listing có sẵn) |

---

## 6. Template và case study

| File | Mô tả |
|---|---|
| [`templates/input_product_brief.md`](./templates/input_product_brief.md) | Đầu vào chuẩn: hồ sơ sản phẩm + 3 bảng từ khóa + cam kết tuân thủ |
| [`templates/output_listing_pack.md`](./templates/output_listing_pack.md) | Đầu ra chuẩn: cấu trúc bộ nội dung sáng tạo hoàn chỉnh |
| [`examples/powerbank_20000mah.md`](./examples/powerbank_20000mah.md) | Case study thực tế: Carregador Portátil 20000mAh 45W (Shopee Brazil) |

---

## 7. Giới hạn đã biết

| Giới hạn | Mô tả |
|---|---|
| **Không tự sinh từ khóa** | Từ khóa phải do bạn xuất từ 虾多拉 (Xiaduola) / công cụ từ khóa tìm kiếm của sàn. Agent chỉ phân loại và ghép, **không tự bịa từ** |
| **Không quyết định chọn sản phẩm** | Đây là việc của 01 Market Research |
| **Không định giá** | Đây là việc của 02 Product Strategy |
| **Không kiểm chứng thông số thật** | Agent chỉ đảm bảo được "đầu ra khớp với đầu vào", không thể biết bản thân đầu vào có đúng sự thật hay không. **Bạn chịu trách nhiệm về tính xác thực của thông số** |
| **Quy tắc sàn có thể đã cũ** | Giới hạn ký tự trong repo là quy tắc công khai tại thời điểm viết, **trước khi đăng phải vào Seller Center kiểm tra lại** |
| **Chất lượng ngôn ngữ bản địa có giới hạn** | Chất lượng đầu ra PT-BR phụ thuộc vào model; listing giá trị cao nên nhờ người bản xứ duyệt lại |

---

## 8. Một ví dụ thực tế

Xem [`examples/powerbank_20000mah.md`](./examples/powerbank_20000mah.md). Tóm tắt:

```text
Đầu vào: sạc dự phòng 20000mAh 45W, Shopee Brazil, 3 bảng từ khóa tổng cộng 84 từ
  ↓
Phân loại từ khóa: từ cốt lõi 3 / từ thông số 11 / từ nhóm khách hàng 4 /
            từ tính năng 8 / từ ngữ cảnh 6 / từ phụ kiện 5 / từ rủi ro 6 (đã cách ly)
  ↓
Tiêu đề (Shopee BR, 115/120 ký tự, đo thực tế bằng `title_lint.py`):
  Carregador Portátil 20000mAh 45W Turbo Carga Rápida 3 Saídas
  com Display Digital para Celular iPhone Android Viagem
  ↓
Quy nguyên nhân đánh giá tiêu cực phát hiện "tưởng có kèm cáp sạc" là hiểu lầm phổ biến
  → thêm " cabo não incluso " vào đoạn 6 của trang chi tiết
  ↓
Quét tuân thủ: dính 2 mục (1 từ ngữ tuyệt đối hóa, 1 tên thương hiệu chưa ủy quyền), đã viết lại
```

---

**Quay lại**: [Danh mục Agents](../README.md) · **Tài liệu**: [Phân rã SOP](../../docs/00_Architecture_SOP_to_Agent.md) · [Chuẩn viết Prompt](../../docs/01_Prompt_Design_Guide.md) · [Lằn ranh đỏ tuân thủ](../../docs/03_Compliance_Guard.md)
