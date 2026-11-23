---
name: review-analysis
description: 'Skill phân tích đánh giá cho thương mại điện tử xuyên biên giới (Shopee BR / Mercado Livre, PT-BR). Phân loại đánh giá giao cho mô hình, đếm số giao cho script: quy nguyên nhân đánh giá tiêu cực theo 8 nhóm, tỷ lệ khắc phục được, xếp hạng điểm bán hàng từ đánh giá tích cực theo tần suất × trọng số, xuất đề xuất vá trang chi tiết. Dùng khi người dùng muốn "phân tích đánh giá tiêu cực / quy nguyên nhân đánh giá / rút ra điểm bán hàng / vì sao trang chi tiết chuyển đổi thấp".'
---

# Skill phân tích đánh giá (07 Review Analysis Agent)

## Khi nào dùng

- Đã tích lũy được một lượng đánh giá (nên ≥ 20 đánh giá), cần biết **đánh giá tiêu cực rốt cuộc đến từ đâu, cái nào sửa được**
- Cần rút ra **bảng xếp hạng điểm bán hàng thật** từ đánh giá tích cực, quay vòng về trang chi tiết và ảnh chính
- CVR quảng cáo thấp, nghi ngờ vấn đề nằm ở đánh giá / trang chi tiết (dùng kết hợp với 06)

## Ranh giới phân công (thiết kế cốt lõi của Skill này)

```text
Việc của mô hình                Việc của script
─────────────                   ─────────────
Đọc từng đánh giá               Tổng hợp, đếm số
→ Quy 8 nhóm (phán đoán ngữ nghĩa) → Tỷ trọng / tỷ lệ khắc phục được / kiểm tra tổng
→ Rút điểm bán hàng + chấm mức độ  → Xếp hạng tần suất × trọng số
→ Viết nội dung vá (PT-BR)       → Xuất báo cáo thống kê
```

**Phân loại là việc của mô hình, script không đoán; đếm số là việc của script, mô hình không được nhẩm.**

## Ba nguyên tắc bất di bất dịch

1. **Tổng số đã quy nguyên nhân phải bằng số đánh giá tiêu cực** — script tự kiểm tra, không khớp = sửa dữ liệu trước rồi mới kết luận
2. **Nội dung vá phải là PT-BR chuẩn người bản xứ, dán thẳng được** (≤ 600 ký tự, cùng quy chuẩn với mẫu câu CSKH)
3. **Chỉ đưa hành động theo "bên chịu trách nhiệm / khả năng khắc phục"** — không liệt kê theo hiện tượng; cùng một hiện tượng (như "không nhận được phụ kiện")
   có thể là lỗi đóng gói (sửa được) hoặc lỗi vận chuyển (không sửa được)

## 8 nhóm nguyên nhân và tiêu chí khắc phục mặc định

| Nhóm | Khắc phục được | Cách khắc phục |
|---|---|---|
| **Hiểu lầm** (sản phẩm không sai, người mua hiểu sai) | ✅ | Bổ sung giải thích / thêm ảnh trên trang chi tiết — **ROI cao nhất** |
| Thông số không như kỳ vọng | ✅ | Ánh xạ điểm bán hàng sát thực tế / đưa thông số chính lên đầu |
| Thiếu phụ kiện (không đọc bảng thông số) | ✅ | Ảnh bày phẳng ghi rõ `Não incluso` (**gửi bù phụ kiện là sai**) |
| Khó sử dụng | ✅ | Bổ sung hướng dẫn sử dụng / video hướng dẫn |
| Giao hàng chậm | ❌ | Giải quyết ở khâu vận chuyển |
| Lỗi chất lượng sản phẩm | ❌ | Giải quyết ở khâu chuỗi cung ứng |
| Hư hỏng/lỗi/trả hàng | ❌ | Giải quyết ở khâu đóng gói / QC |
| Hậu mãi kém | ❌ | Giải quyết ở quy trình CSKH |

Tiêu chí khắc phục được có thể chỉnh bằng `--fixable` (mặc định: Hiểu lầm,Thông số không như kỳ vọng,Thiếu phụ kiện,Khó sử dụng).

## Quy trình

```text
[Step 1] Xuất CSV đánh giá (bắt buộc rating; nên có cột category / has_image)
[Step 2] Mô hình phân loại từng đánh giá (tiêu cực → 8 nhóm; tích cực → điểm bán hàng + mức độ)
[Step 3] Chạy scripts/review_stats.py để tổng hợp và kiểm tra
         → 🔴 Kiểm tra tổng thất bại: quay lại Step 2 bổ sung các dòng chưa quy nguyên nhân
[Step 4] Dựa vào "tỷ lệ khắc phục được" để quyết định thứ tự ưu tiên, xuất nội dung vá
[Step 5] Quay vòng về: nội dung vá → 03 (iterate) / 04 (bổ sung ảnh)
```

## Tra nhanh lệnh

```bash
# Thống kê cơ bản (kèm kiểm tra tổng)
python scripts/review_stats.py --file danh_gia.csv

# Bản đầy đủ: chỉ định tiêu chí khắc phục được + xếp hạng điểm bán hàng
python scripts/review_stats.py --file danh_gia.csv \
    --fixable "Hiểu lầm,Thông số không như kỳ vọng,Thiếu phụ kiện,Khó sử dụng" \
    --points diem_ban_hang.csv
```

Tên cột tự nhận diện tiếng Việt / Trung / Anh / Bồ Đào Nha: `rating|số sao|评分|avaliacao`, `category|nguyên nhân|归因|categoria`,
`has_image|có ảnh|带图|com_imagem`; số liệu tương thích định dạng Brazil. Tên nhóm và mức độ bằng tiếng Trung (`误解型`, `强/中/弱`…) được tự quy đổi sang tiếng Việt.

## Tiêu chí xếp hạng điểm bán hàng

Điểm tổng hợp = tần suất nhắc đến × trọng số cảm xúc (mạnh=3 / vừa=2 / yếu=1).
**Bảng xếp hạng định hướng thứ tự ưu tiên điểm bán hàng, không xác nhận tính xác thực** — tính xác thực vẫn phải đối chiếu với `spec_table`.

## Ranh giới

- Không trả lời đánh giá thay, không liên hệ người mua, không xóa đánh giá (việc sàn cấm thì không làm)
- Khi tổng số đánh giá < 20, kết luận nhiều nhiễu; script vẫn chạy nhưng báo cáo phải ghi chú "mẫu chưa đủ"
