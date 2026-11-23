# pricing-rules.md · Công thức định giá và cách tính

> Mọi con số đều do `scripts/sku_pricing.py` tính. Nghi ngờ con số → `[METRIC_SUSPECT]`.

---

## Công thức

```text
Lợi nhuận gộp trước QC = giá bán − giá vốn về kho − giá bán×% hoa hồng − giá bán×% hao hụt hoàn hàng − giá bán×% thuế
Biên lợi nhuận ròng    = (lợi nhuận gộp trước QC − giá bán×% quảng cáo) ÷ giá bán
Giá hòa vốn            = giá vốn về kho ÷ (1 − % hoa hồng − % hoàn hàng − % thuế)
Giá mục tiêu           = giá vốn về kho ÷ (1 − % hoa hồng − % hoàn hàng − % quảng cáo − % biên lợi nhuận mục tiêu)
Dư địa voucher         = giá bán × (biên lợi nhuận ròng thực tế − % biên lợi nhuận mục tiêu)
```

**Giá vốn về kho (landed cost)** = giá vốn sản phẩm + vận chuyển chặng đầu + vận chuyển chặng cuối + lưu kho (dồn hết vào một tham số `--cost`, đừng tách ra rồi tính trùng).

---

## Giá trị mặc định của tham số và nguồn

**Preset mức phí theo sàn (số liệu ngày 2026-10-18, nguồn và lưu ý kiểm tra lại xem `../scripts/platform_fees.json`)**:

| key | Sàn | Hoa hồng | Phí cố định mỗi sản phẩm | Phụ phí | Bẫy chính |
|---|---|---|---|---|---|
| `shopee_br` | Shopee Brazil | <R$80 → 20%; ≥R$80 → 14% | ≤79.99→4 / 80–99.99→16 / 100–199.99→20 / ≥200→26 | 0 | Chính sách mới 2026-03-01: phí cố định chia bậc + bỏ trần hoa hồng R$100 |
| `mercadolivre_br` | ML Clássico | 11% (10–14%) | <R$79→6.50 (từ 2026-03-02 chuyển thành chi phí vận chuyển biến đổi theo cân nặng/kích thước) | 0 | <R$79 là dải giá nguy hiểm nhất, nâng giá vượt ngưỡng để tiết kiệm phí mỗi sản phẩm |
| `mercadolivre_br_premium` | ML Premium | 16% (15–19%) | Như trên | 0 | Đắt hơn 5pp để đổi lấy trả góp không lãi + hiển thị cao |
| `amazon_br` | Amazon Brazil | 15% (Most categories, tùy ngành hàng 8–15%) | 0 (Professional; Individual R$2 mỗi sản phẩm) | 0 | Phí tháng R$19; phí xử lý đơn FBA tính riêng; referral tính trên tổng tiền người mua trả |
| `tiktok_br` | TikTok Shop | <R$50 → 10%; ≥R$50 → 6% | <R$50→4 / ≥R$50→6 | 6% (chương trình freeship, tự động tham gia) | Chia bậc theo giá sau chiết khấu của người bán —— voucher có thể làm nhảy bậc; giá trị đơn thấp thì khởi điểm đã 30% |

**Tham số CLI truyền rõ luôn được ưu tiên hơn preset.** Quy tắc của sàn sẽ thay đổi, hãy kiểm tra lại trên Seller Center trước khi đăng bán;
sàn chưa tìm được nguồn mức phí đáng tin cậy (Magalu / Temu / Shein, v.v.) thì **không làm preset**, hãy truyền tham số thủ công.

## Mặc định thủ công trước đây (khi nhập tay / không dùng --platform)

| Tham số | Mặc định | Nguồn |
|---|---|---|
| Hoa hồng | 14% | Mức phí tổng hợp phổ biến của Shopee BR (gồm phí giao dịch), ML tùy ngành hàng 13–17% —— nay đã được preset theo sàn ở trên thay thế |
| Hao hụt hoàn hàng | 2% | SOP 3.5 khuyến nghị dự phòng |
| Quảng cáo | 5% | Dự phòng trong mô hình định giá (lưu ý: chạy quảng cáo thực tế thường cao hơn mức này, xem phần đối chiếu ngưỡng hòa vốn ở 06) |
| Thuế | 0% | **Người dùng bắt buộc phải điền**: quy đổi Simples Nacional / ICMS / PIS+COFINS thành % trên giá bán |
| Biên lợi nhuận mục tiêu | 32% | Mục tiêu biên lợi nhuận của team (điền theo công ty) |

---

## Ba nhận định sai kinh điển (script sẽ cảnh báo)

**① SKU kéo traffic có biên lợi nhuận ròng thấp hơn mục tiêu = lỗ chiến lược?**
Chưa chắc. Đối chiếu với `break_even_price`: chỉ cần giá bán nằm trên giá hòa vốn là vẫn có lãi,
thấp hơn biên lợi nhuận mục tiêu chỉ là «chưa lãi được nhiều như mục tiêu». SKU kéo traffic 27.5% so với mục tiêu 32% là chiến lược bình thường.

**② SKU cấu hình cao bị SKU chủ lực vượt mặt về biên lợi nhuận ròng = định giá sai?**
Hiện tượng thường gặp: giá vốn tăng 34.8% nhưng giá bán chỉ tăng 22.7% (giá tăng theo cấu hình không tuyến tính).
Giá trị tồn tại của SKU cấu hình cao thường là **neo giá**, không nhất thiết là SKU lợi nhuận —— nhưng script sẽ nhắc bạn kiểm tra lại.

**③ Voucher muốn phát bao nhiêu thì phát?**
`coupon_headroom` chính là hạn mức: phần biên lợi nhuận ròng vượt mục tiêu × giá bán.
SKU chủ lực có biên lợi nhuận ròng 36.5%, mục tiêu 32% → dư địa R$ 98.52 → phát voucher R$100 là vừa sát vạch mục tiêu.

---

## Đọc bậc giá

| Chênh giá giữa hai bậc liền kề | Ý nghĩa |
|---|---|
| < 10% | Tự ăn thịt lẫn nhau —— người mua đều mua bản rẻ |
| 10–35% | Bậc giá lành mạnh (kéo traffic → chủ lực thường 30%+) |
| > 50% | Bỏ trống khoảng giữa cho đối thủ |
