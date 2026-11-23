---
name: sop-ecom-listing-lint
description: >-
  Skill kiểm tra tuân thủ Listing: đo thực tế số ký tự tiêu đề (ký tự chứ không phải byte), dính từ cấm, độ phủ từ khóa cốt lõi,
  phát hiện từ khuyến mãi / emoji / nhồi từ khóa, truy nguồn tính nhất quán thông số (mọi con số trong nội dung phải khớp với spec_table).
  Dùng khi người dùng muốn kiểm tra tiêu đề, kiểm tra vượt giới hạn ký tự, kiểm tra từ cấm, kiểm tra lệch thông số, tự kiểm tra trước khi đăng bán.
  Câu tiếng Việt như "kiểm tra tiêu đề giúp / check tuân thủ / thông số đúng chưa" cũng kích hoạt.
  NOT for viết tiêu đề, viết trang chi tiết (việc của luồng chính 03), tạo ảnh (04).
allowed-tools:
  - Bash(python *)
  - Read
metadata:
  version: 0.4.0
  category: e-commerce/listing-compliance
  license: MIT
---

# 03 · Listing Compliance Skill (chốt chặn mức sàn)

> **Định vị**: giữ **mức sàn** của Listing — không vượt số ký tự, không bị cắt chữ, không dính từ cấm, thông số không bị lệch.
> **Mức trần** (có kéo được click hay không) không thuộc phạm vi Skill này, cái đó phải đăng bán rồi xem CTR thực tế.

---

## Bắt đầu nhanh

```bash
# Kiểm tra tiêu đề (số ký tự là giá trị đo thực tế)
python scripts/title_lint.py "Nội dung tiêu đề" --platform shopee \
    --forbidden "iPhone,Samsung" --keywords "carregador,20000mah,45w"

# Tính nhất quán thông số: mọi con số trong nội dung phải truy được về spec_table
python scripts/spec_consistency.py --spec examples/spec_table.csv --text noi_dung_trang_chi_tiet.md

# Kiểm tra tiêu đề + trang chi tiết cùng lúc
python scripts/spec_consistency.py --spec examples/spec_table.csv \
    --title "Tiêu đề" --text noi_dung_trang_chi_tiet.md
```

---

## Các mục kiểm tra

### title_lint.py (theo bảng quy tắc của từng sàn)

| Kiểm tra | Shopee | Mercado Livre | Amazon |
|---|---|---|---|
| Giới hạn ký tự | 120 | **60** | 200 |
| 30 ký tự đầu | ✅ Xuất riêng (đoạn có trọng số cao nhất) | — | — |
| Từ khuyến mãi | ⚠️ Cẩn trọng | ⚠️ Khuyến cáo rõ là không dùng | ⚠️ |
| Emoji | ❌ Cấm | ⚠️ | ⚠️ |
| Viết hoa toàn bộ tràn lan | ⚠️ | ⚠️ | ⚠️ |
| Từ lặp ≥3 lần | ❌ Nhồi từ khóa bị giảm thứ hạng | ❌ | ⚠️ |
| Lẫn ký tự tiếng Trung | ❌ (sàn PT-BR) | ❌ | ❌ |
| Từ cấm | ❌ (tự chuẩn bị danh sách: thương hiệu chưa ủy quyền / từ ngữ tuyệt đối hóa) | ❌ | ❌ |
| Độ phủ từ khóa cốt lõi | ⚠️ Nhắc thiếu từ | ⚠️ | ⚠️ |

### spec_consistency.py

| Kiểm tra | Mô tả |
|---|---|
| **Lệch thông số** | Mọi con số trong nội dung phải truy được về spec_table; không truy được = gõ nhầm / bịa ra / không thống nhất cách tính |
| **Bỏ sót thông số** | Thông số có số trong spec_table nhưng chưa từng xuất hiện trong nội dung → nhắc bổ sung |

Hỗ trợ định dạng số kiểu Brazil (`20.000` = 20000) và miễn kiểm tra bằng `--allow` (năm và các hằng số không liên quan).

---

## Bảng quy tắc

- [references/platform-title-rules.md](references/platform-title-rules.md) — nguồn gốc và ngưỡng của quy tắc số ký tự / mục cấm / nhồi từ khóa
- Dữ liệu ví dụ: [examples/spec_table.csv](examples/spec_table.csv) (bảng thông số sạc dự phòng)

## Giới hạn đã biết

| Giới hạn | Mô tả |
|---|---|
| Không kiểm tra chữ trong ảnh | Tuân thủ chữ chèn trên ảnh chính / ảnh chi tiết thuộc về `check_main_image.py` của 04 (cấp độ pixel) |
| Phải tự chuẩn bị danh sách từ cấm | Sàn không công khai đầy đủ danh sách từ vi phạm; lấy đầu ra của Prompt quét tuân thủ 03 đưa vào `--forbidden` |
| Chỉ kiểm tra, không tạo nội dung | Muốn viết tiêu đề hãy quay lại Prompt luồng chính 03; Skill này là chốt chặn cuối cùng trước khi đăng |
