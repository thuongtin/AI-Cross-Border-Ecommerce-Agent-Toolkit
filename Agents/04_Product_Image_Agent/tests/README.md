# 04 · Bộ ảnh test cho check_main_image.py

5 ảnh tổng hợp, **mỗi ảnh đều cài sẵn các mục tuân thủ và vi phạm đã biết**.
Clone về chạy một lượt, kết quả khớp với bảng dưới = script kiểm tra hoạt động bình thường.

```bash
cd Agents/04_Product_Image_Agent/scripts

python check_main_image.py ../tests/ml_pass.png       --platform mercadolivre   # Mong đợi ✅
python check_main_image.py ../tests/amazon_fail.png   --platform amazon         # Mong đợi ❌ coverage
python check_main_image.py ../tests/shopee_fix.png    --platform shopee  --fix ../tests/shopee_fixed.png
python check_main_image.py ../tests/ml_chaotic.png    --platform mercadolivre   # Mong đợi ❌ square
python check_main_image.py ../tests/shopee_fixed.png  --platform shopee         # Mong đợi ✅
```

---

## Danh sách ảnh test và kết quả mong đợi (giá trị đo thực tế)

| Ảnh test | Cách dựng | Sàn | Kết luận mong đợi |
|---|---|---|---|
| `ml_pass.png` | 1200×1200 nền be sạch `#F5F0E8`, chủ thể chiếm 88% | mercadolivre | **✅ Đạt** |
| `amazon_fail.png` | 2000×2000 nền trắng tinh, chủ thể chỉ chiếm **60%** | amazon | **❌ coverage** 60% < 85% |
| `shopee_fix.png` | 900×900 nền trắng ngà `#FAFAF8` (không phải trắng tinh), chủ thể chiếm **56%** | shopee | **❌ white_bg 0%** + **❌ coverage** |
| `shopee_fixed.png` | Đầu ra của ảnh trên sau khi chạy `--fix` | shopee | **✅ Đạt** (1024px / nền trắng 100% / chiếm khung 80%) |
| `ml_chaotic.png` | **1100×1000 không vuông** + nền nhiễu ngẫu nhiên ở viền | mercadolivre | **❌ square** + **⚠️ bg_uniformity** + **⚠️ coverage 100%*** |

### Ghi nhận đo thực tế (2026-10-16)

| Ảnh test | Đầu ra chính |
|---|---|
| ml_pass | ✅ size 1200px · ✅ square · ⚠️ coverage 100% (>97% giới hạn trên, cảnh báo đúng) · ✅ bg_uniformity 100% |
| amazon_fail | ❌ coverage 60% < 85% · ✅ white_bg 100% · ✅ square |
| shopee_fix | ❌ white_bg 0.0% < 90% · ❌ coverage 56% < 60% · ⚠️ size 900 < 1024 |
| shopee_fixed | ✅ 1024px · ✅ white_bg 100% · ✅ coverage 80% (`--fix` đạt chuẩn chính xác) |
| ml_chaotic | ❌ square 1100×1000 · ⚠️ bg_uniformity 84% (nền hơi rối) · ⚠️ size 1000 < 1200 · ⚠️ coverage 100%* |

> **\* Về coverage=100% của ml_chaotic**: tỷ lệ chiếm khung được đo bằng "khung bao các pixel không phải nền",
> mà bản thân pixel nhiễu cũng không phải nền → khung bao bị kéo phủ kín toàn ảnh. **Với nền lộn xộn, phương pháp đo tỷ lệ bằng bbox chắc chắn mất tác dụng**
> —— đây không phải bug, mà chính là lý do script đồng thời đưa ra cảnh báo `bg_uniformity`:
> ảnh có nền rối thì con số tỷ lệ chiếm khung không đáng tin, làm sạch nền trước rồi mới bàn đến tỷ lệ.

---

## Bộ ảnh test này bao phủ những gì

| Năng lực | Được kiểm chứng bởi ảnh nào |
|---|---|
| ML "nền chỉ cần sạch, không yêu cầu trắng tinh" (quy định mới 2026) | `ml_pass` (nền be vẫn đạt) |
| Độ tinh nền trắng Amazon + lằn ranh đỏ tỷ lệ chiếm khung 85% | `amazon_fail` |
| `--fix` kéo pixel gần trắng về trắng tinh + sắp xếp lại tỷ lệ chiếm khung | `shopee_fix` → `shopee_fixed` |
| Phát hiện ảnh không vuông | `ml_chaotic` |
| Nhắc nền lộn xộn + giới hạn mất tác dụng của phương pháp đo bằng bbox khi nền lộn xộn | `ml_chaotic` |
| Cảnh báo tỷ lệ chiếm khung vượt giới hạn trên (>97%) | `ml_pass` (100% sát viền) |

**Không bao phủ**: tỷ lệ chữ trong ảnh (cần OCR, xếp vào mục người xác nhận), ảnh sản phẩm thật (ảnh test là ảnh tổng hợp, chỉ kiểm tra hình học và màu sắc).

---

**Script**: [`scripts/check_main_image.py`](../scripts/check_main_image.py) · **Thẻ quy tắc**: [Shopee](../references/platform-shopee.md) · [Mercado Livre](../references/platform-mercadolivre.md) · [Amazon](../references/platform-amazon.md)
