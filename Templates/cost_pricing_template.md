# Template · Mô hình tính giá

> SOP **1.9 Định giá** + **3.2 Định giá từng sản phẩm và chiến lược SKU**.
> Tài liệu này đưa ra **công thức tính được ngay**, thay vì "nhìn chừng chừng rồi định".

---

## 1. Quy tắc định giá trong SOP

| Mục | Quy tắc (nguyên văn SOP) |
|---|---|
| Biên lợi nhuận gộp hàng cồng kềnh | **30–35%** |
| Biên lợi nhuận gộp hàng nhỏ | **25–30%** |
| Tỷ trọng chi phí quảng cáo | Hàng cồng kềnh **~5%** / hàng nhỏ **5–10%** |
| Hao hụt do hoàn hàng | **2%** |
| Phí hoa hồng sàn | Tra theo ngành hàng thực tế (Mercado Livre thường 8–16%) |
| Vận chuyển chặng cuối | Đo theo sản phẩm thực tế (SOP gọi là "phí chặng cuối của sản phẩm") |
| Phí thao tác kho | Theo bậc kích thước sản phẩm |
| Nhịp điều chỉnh giá | **Giai đoạn đầu có thể giảm nhẹ biên lợi nhuận để nuôi trọng số (ranking), khi trọng số đã lên thì nâng lại** |

---

## 2. Công thức cốt lõi

> **Từ 2026-10**: phần tính tay trong template này đã được tự động hóa bằng script `Agents/02_Product_Strategy_Agent/scripts/sku_pricing.py`,
> có sẵn preset biểu phí cho 5 sàn (Shopee BR / ML Clássico / ML Premium / Amazon BR / TikTok Shop BR,
> bao gồm hoa hồng theo bậc giá và phí cố định theo từng sản phẩm):
>
> ```bash
> python Agents/02_Product_Strategy_Agent/scripts/sku_pricing.py calc --platform shopee_br --cost 935 --price 2199
> python Agents/02_Product_Strategy_Agent/scripts/sku_pricing.py --list-platforms
> ```
>
> Cách tính và nguồn biểu phí xem tại `Agents/02_Product_Strategy_Agent/references/pricing-rules.md`;
> **sàn nào không có nguồn biểu phí đáng tin cậy thì không làm preset** (Magalu / Temu / Shein, v.v.), phải tự truyền tham số.
> Các công thức tính tay bên dưới được giữ lại để hiểu nguyên lý và đối chiếu kết quả của script.

### Công thức giá bán

```
        Giá vốn sản phẩm + Vận chuyển chặng cuối + Phí thao tác kho
P = ──────────────────────────────────────────────────────────────────────────────
      1 − Tỷ lệ hoa hồng − Tỷ lệ quảng cáo − Tỷ lệ hao hụt hoàn hàng − Biên LN gộp mục tiêu
```

**Vì sao mẫu số phải trừ nhiều như vậy?** Vì hoa hồng, quảng cáo, hao hụt hoàn hàng và lợi nhuận gộp đều phát sinh **theo tỷ lệ phần trăm trên giá bán**, chứ không phải số tiền tuyệt đối cố định. Nếu cộng thẳng vào tử số thì sẽ tính thiếu.

### Ngưỡng hòa vốn (giá bán thấp nhất khi lợi nhuận gộp = 0)

```
          Giá vốn sản phẩm + Vận chuyển chặng cuối + Phí thao tác kho
P₀ = ─────────────────────────────────────────────────────────────────
            1 − Tỷ lệ hoa hồng − Tỷ lệ quảng cáo − Tỷ lệ hoàn hàng
```

> P₀ là **mức giá tuyệt đối không được thấp hơn**. Thấp hơn P₀ là bán đơn nào lỗ đơn đó (chưa tính chi phí cố định). Khi làm khuyến mãi, tham gia campaign hay tính mức voucher, phải vạch ra ngưỡng này trước.

### Giá sàn theo biên lợi nhuận gộp

```
Pmin = Công thức của P₀, nhưng mẫu số trừ thêm "biên LN gộp thấp nhất có thể chấp nhận"
```

---

## 3. Ví dụ A · Hàng nhỏ (sạc dự phòng)

### Đầu vào

| Mục | Giá trị | Ghi chú |
|---|---|---|
| Giá vốn sản phẩm | `R$ 40,00` | Gồm giá nhập + phân bổ vận chuyển chặng đầu |
| Vận chuyển chặng cuối | `R$ 12,00` | Đo theo cân nặng, thể tích thực tế của sản phẩm |
| Phí thao tác kho | `R$ 3,00` | Theo bậc thể tích |
| Tỷ lệ hoa hồng sàn | `14%` | ⚠️ Tra theo ngành hàng thực tế |
| Tỷ lệ quảng cáo | `7,5%` | Hàng nhỏ 5–10%, lấy giá trị giữa |
| Tỷ lệ hao hụt hoàn hàng | `2%` | Giá trị quy định trong SOP |
| Biên LN gộp mục tiêu | `28%` | Hàng nhỏ 25–30%, lấy giá trị giữa |

### Tính toán

```
Mẫu số = 1 − 0,14 − 0,075 − 0,02 − 0,28 = 0,485
Tử số  = 40 + 12 + 3 = 55

P = 55 ÷ 0,485 = R$ 113,40
```

### Tính ngược để kiểm tra

| Mục | Số tiền | % trên giá bán |
|---|---|---|
| Giá vốn sản phẩm | R$ 40,00 | 35,3% |
| Vận chuyển chặng cuối | R$ 12,00 | 10,6% |
| Phí thao tác kho | R$ 3,00 | 2,6% |
| Hoa hồng sàn (14%) | R$ 15,88 | 14,00% |
| Quảng cáo (7,5%) | R$ 8,51 | 7,50% |
| Hao hụt hoàn hàng (2%) | R$ 2,27 | 2,00% |
| **Lợi nhuận gộp (28%)** | **R$ 31,75** | **28,00%** |
| **Tổng** | **R$ 113,40** | **100%** |

✅ Tổng = giá bán, mô hình tự khớp.

### Giá sàn

| Ngưỡng | Giá | Ý nghĩa |
|---|---|---|
| **Ngưỡng hòa vốn P₀** | **R$ 71,90** | Thấp hơn giá này là đơn nào cũng lỗ |
| Giá sàn theo biên LN gộp (23%) | R$ 102,80 | Biên LN gộp thấp nhất có thể chấp nhận |

---

## 4. Ví dụ B · Hàng cồng kềnh (nồi chiên không dầu)

### Đầu vào

| Mục | Giá trị |
|---|---|
| Giá vốn sản phẩm | `R$ 120,00` |
| Vận chuyển chặng cuối | `R$ 45,00` |
| Phí thao tác kho | `R$ 8,00` |
| Tỷ lệ hoa hồng sàn | `14%` |
| Tỷ lệ quảng cáo | `5%` (hàng cồng kềnh) |
| Tỷ lệ hao hụt hoàn hàng | `2%` |
| Biên LN gộp mục tiêu | `32%` (hàng cồng kềnh 30–35%, lấy giá trị giữa) |

### Tính toán

```
Mẫu số = 1 − 0,14 − 0,05 − 0,02 − 0,32 = 0,47
Tử số  = 120 + 45 + 8 = 173

P = 173 ÷ 0,47 = R$ 368,09
```

### Tính ngược để kiểm tra

| Mục | Số tiền | % trên giá bán |
|---|---|---|
| Giá vốn sản phẩm | R$ 120,00 | 32,6% |
| Vận chuyển chặng cuối | R$ 45,00 | 12,2% |
| Phí thao tác kho | R$ 8,00 | 2,2% |
| Hoa hồng sàn (14%) | R$ 51,53 | 14,00% |
| Quảng cáo (5%) | R$ 18,40 | 5,00% |
| Hao hụt hoàn hàng (2%) | R$ 7,36 | 2,00% |
| **Lợi nhuận gộp (32%)** | **R$ 117,79** | **32,00%** |
| **Tổng** | **R$ 368,09** | **100%** |

### Giá sàn

| Ngưỡng | Giá |
|---|---|
| **Ngưỡng hòa vốn P₀** | **R$ 218,99** |
| Giá sàn theo biên LN gộp (27%) | R$ 332,69 |

---

## 5. Định giá theo cấu trúc SKU (SOP 3.2)

Nhận định cốt lõi của SOP:

> SKU không phải muốn thêm là thêm, mà là để người mua có sự so sánh.

| Vai trò SKU | Định vị giá | Biên LN gộp | Tác dụng |
|---|---|---|---|
| **SKU kéo traffic (cấu hình thấp)** | Giá thấp nhất, sát giá sàn theo biên LN gộp | **Mỏng nhất** (có thể thấp hơn mục tiêu 5–8 điểm %) | Tăng hiệu quả quảng cáo, nâng CTR |
| **SKU chủ lực** | Giá mục tiêu | Biên LN gộp mục tiêu | Chốt đơn |
| **SKU cấu hình cao** | Cao hơn SKU chủ lực 20–40% | Cao hơn | Tăng giá trị đơn hàng trung bình (AOV) |
| **SKU combo** | Thường đắt nhất | **Cao nhất** | Tăng lợi nhuận |

**Công cụ phối hợp**: dùng voucher để **thu hẹp chênh lệch giá giữa các SKU** — cho người mua cảm giác "thêm chút tiền là được nâng cấp", từ đó kéo họ về SKU chủ lực và SKU cấu hình cao.

### Ví dụ định giá SKU (sạc dự phòng)

| SKU | Nội dung | Giá bán | Biên LN gộp | Ghi chú |
|---|---|---|---|---|
| Kéo traffic (cấu hình thấp) | 10000mAh, 1 cổng | `R$ 79,90` | ~20% | ⚠️ **Cao hơn ngưỡng hòa vốn R$ 71,90**, an toàn |
| **Chủ lực** | **20000mAh, 3 cổng** | **`R$ 113,40`** | **28%** | Giá mục tiêu |
| Cấu hình cao | 20000mAh + sạc không dây | `R$ 149,90` | ~32% | — |
| Combo | 20000mAh × 2 | `R$ 199,90` | ~34% | — |

> **Giá của SKU cấu hình thấp bắt buộc phải qua bước kiểm tra ngưỡng hòa vốn.** Rất nhiều người bán đặt giá SKU kéo traffic quá thấp, nhìn biên LN gộp thì có vẻ ổn, nhưng thực tế đã thấp hơn P₀ và đang lỗ.

---

## 6. Tra nhanh biểu phí tham khảo

| Mục | Giá trị tham khảo | Ghi chú |
|---|---|---|
| Hoa hồng sàn | 8–16% | **Bắt buộc tra theo ngành hàng thực tế**, chênh lệch rất lớn |
| Chi phí quảng cáo · hàng cồng kềnh | ~5% | SOP |
| Chi phí quảng cáo · hàng nhỏ | 5–10% | SOP |
| Hao hụt hoàn hàng | 2% | SOP |
| Vận chuyển chặng đầu | Theo thực tế | Phân bổ cho từng sản phẩm |
| Vận chuyển chặng cuối | Theo thực tế | Bắt buộc cân, đo thể tích thực tế |
| Phí thao tác kho | Theo bậc thể tích | Bắt buộc theo báo giá thực tế |
| Phí thanh toán | Theo sàn | Một số sàn tính riêng, cần xác nhận đã gồm trong hoa hồng hay chưa |

> ⚠️ **Lưu ý riêng cho thị trường Mỹ Latinh**: cơ cấu thuế khi bán sang Brazil khá phức tạp (thuế bang, thuế liên bang, thuế nhập khẩu), **mô hình này chưa tính thuế**. Khi định giá thực tế, bắt buộc bổ sung khoản thuế theo phương án thuế thực tế của bạn, nếu không biên LN gộp tính ra sẽ bị cao hơn thực tế.
> Nên thêm một khoản `Tỷ lệ thuế` vào mẫu số, công thức trở thành:
> ```
> P = Tử số ÷ (1 − Tỷ lệ hoa hồng − Tỷ lệ quảng cáo − Tỷ lệ hoàn hàng − Tỷ lệ thuế − Biên LN gộp mục tiêu)
> ```

---

## 7. Tự kiểm tra khi điền

- [ ] Tỷ lệ hoa hồng được **tra theo ngành hàng thực tế**, không lấy luôn giá trị tham khảo
- [ ] Vận chuyển chặng cuối là số **đo thực tế**, không phải ước lượng
- [ ] Đã bổ sung khoản thuế theo phương án thuế thực tế tại Brazil (hoặc thị trường khác)
- [ ] Đã tính **ngưỡng hòa vốn P₀** và xác nhận giá của mọi SKU đều cao hơn P₀
- [ ] Đã kiểm tra kỹ ngưỡng hòa vốn cho SKU kéo traffic (chỗ dễ lỗ nhất)
- [ ] Đã phân tầng biên LN gộp theo vai trò SKU, tạo cấu trúc "dẫn người mua lên mức giá cao hơn"
- [ ] Đã ghi lại mức giảm giá trong giai đoạn nuôi trọng số ban đầu và thời điểm nâng giá lại
- [ ] Mọi mức giá đều dùng `R$` và dấu phẩy thập phân (`R$ 113,40`)

---

**Tài liệu liên quan**: [Phân rã SOP→Agent](../docs/00_Architecture_SOP_to_Agent.md) · [Quy chuẩn trường dữ liệu theo sàn](../docs/02_Platform_Output_Spec.md) · [02 Product Strategy Agent](../Agents/02_Product_Strategy_Agent/) (Phase 2)
