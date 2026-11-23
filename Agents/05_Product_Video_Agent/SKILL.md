---
name: shopee-br-product-video
description: Skill sản xuất video sản phẩm cho thương mại điện tử xuyên biên giới (Shopee BR / Mercado Livre, PT-BR). Bao gồm kịch bản 15s/30s, bảng storyboard, Prompt video AI, kịch bản lồng tiếng và phụ đề, đồng thời dùng script tất định để kiểm tra thời lượng và độ dài dòng phụ đề. Dùng khi người dùng muốn "làm video sản phẩm / video ngắn bán hàng / lên storyboard / kịch bản lồng tiếng và phụ đề".
---

# Skill video sản phẩm (05 Product Video Agent)

## Khi nào dùng

- Cần làm video ngắn 15s hoặc 30s cho sản phẩm trên Shopee BR / Mercado Livre
- Đã có kịch bản/bản lồng tiếng, cần **kiểm tra thời lượng có đạt không, phụ đề có vượt dòng không**
- Cần chuyển kịch bản thành bảng storyboard + Prompt video AI + gói lồng tiếng và phụ đề

## Ba nguyên tắc cứng (không thương lượng)

1. **Không bịa thông số** —— mọi con số xuất hiện trong lời thoại phải lấy từ `spec_table`;
   đối chiếu nguồn bằng [`../03_Listing_Creative_Agent/scripts/spec_consistency.py`](../03_Listing_Creative_Agent/scripts/spec_consistency.py).
2. **Thời lượng và phụ đề giao cho script** —— việc quy đổi số từ → thời lượng, kiểm tra độ dài dòng phụ đề **không được tự nhẩm**,
   luôn chạy `scripts/video_timing.py`. Quá giờ thì **cắt bớt từ, không được tăng tốc độ đọc**.
3. **Mọi văn bản người mua nhìn thấy phải là PT-BR bản ngữ** —— cấm viết tiếng Anh trước rồi dịch sang.

## Quy trình

```text
[Step 1] Đọc references/video-specs.md (quy chuẩn video của sàn)
[Step 2] Viết kịch bản (hai bản 15s / 30s, mỗi câu thoại = một cảnh storyboard)
[Step 3] Chạy scripts/video_timing.py --target 15 / 30 để kiểm tra
         → ❌ Quá giờ/thiếu giờ: cắt từ hoặc thêm câu điểm bán hàng, sửa xong chạy lại cho đến khi ✅
[Step 4] Chạy spec_consistency.py của 03 để kiểm tra các con số trong lời thoại
[Step 5] Xuất bảng storyboard + Prompt video AI + file phụ đề (SRT)
```

## Tra nhanh lệnh

```bash
# Kiểm tra thời lượng + phụ đề (dùng nhiều nhất)
python scripts/video_timing.py --script kich_ban_long_tieng.txt --target 30

# Chỉ định tốc độ đọc và độ rộng dòng phụ đề
python scripts/video_timing.py --script kich_ban_long_tieng.txt --target 15 --wps 2.4 --subtitle-max 40
```

Đầu ra: timeline từng câu (giây bắt đầu/kết thúc), tổng thời lượng so với mục tiêu (dung sai ±15%), cảnh báo phụ đề vượt dòng,
kiểm tra hook (câu đầu > 8 từ = vượt 3 giây vàng mở đầu, sẽ cảnh báo).

## Chuẩn tốc độ đọc

Giọng đọc PT-BR **2,5 từ/giây** (≈150 từ/phút) là mức trung vị theo kinh nghiệm:
- Bản 30s: ngân sách lời thoại ≈ **65 từ** (chừa 4s cho khoảng lặng và chuyển cảnh)
- Bản 15s: ngân sách lời thoại ≈ **30 từ** (chừa 3s khoảng lặng)

> Tốc độ đọc thay đổi theo công cụ lồng tiếng/người đọc, trước khi bàn giao chính thức hãy nghe lại bản lồng tiếng thực tế để tinh chỉnh `--wps`.

## Ghi nhớ nhanh theo sàn (chi tiết xem references/video-specs.md)

| Sàn | Thời lượng khuyến nghị | Ràng buộc chính |
|---|---|---|
| Shopee BR | ≤ 30s (video ảnh chính) | Khung đầu là sản phẩm, phụ đề burn-in, dọc 9:16 hoặc 1:1 |
| Mercado Livre | ≤ 30s | Nhất quán với quy chuẩn ảnh chính; phụ đề PT-BR |

Các thông số của sàn là quy định công khai tại thời điểm biên soạn, **trước khi đăng hãy kiểm tra lại văn bản gốc trên Seller Center**.

## Phạm vi

- Skill này **không phụ trách render** (giao cho công cụ video AI/phần mềm dựng) và mua bản quyền BGM
- Chỉ sản xuất: kịch bản, bảng storyboard, Prompt, kịch bản lồng tiếng, phụ đề
