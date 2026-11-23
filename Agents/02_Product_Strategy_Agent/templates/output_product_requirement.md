# Template đầu ra · Bảng yêu cầu sản phẩm

> Đầu ra chuẩn của 02 Product Strategy Agent. Là sản phẩm bàn giao cuối cùng mà SOP 1.7 yêu cầu.
> **Bên sử dụng downstream**: 03 Listing / 04 Image / 05 Video (điểm bán hàng và thông số), 06 Advertising (ngưỡng hòa vốn), bộ phận thu mua (quy cách).

---

```markdown
# Product Requirement · <product_name> · <platform> / <market>

Thời gian tạo: <YYYY-MM-DD>
Phiên bản Prompt: 02-Product-Strategy v0.3
Xác nhận quyết định: <người ra quyết định / ngày>
Upstream: 01-Market-Research

---

## 0. Kết luận một câu (SOP 1.7 yêu cầu)

> **Sản phẩm này của chúng ta bán cho <ai>, đánh vào <điểm bán hàng nào>, dùng <cấu hình nào>,
> ở mức <giá nào>, né <rủi ro nào>.**

---

## 1. Loại sản phẩm

| Khía cạnh | Định vị | Căn cứ |
|---|---|---|
| Vai trò trong shop | SKU kéo traffic / SKU lợi nhuận / SKU test / SKU long-tail | |
| Mức độ khác biệt | SKU phổ thông / SKU khác biệt hóa | |
| Vai trò quảng bá | SKU chủ lực / SKU test | |

---

## 2. Cấu hình cốt lõi

| Khía cạnh cấu hình | Giá trị thị trường đề xuất | Giá trị bên ta chốt | Có khớp không | Công ty làm được không |
|---|---|---|---|---|
| | | | | |

**Giải thích cấu hình**:

⚠️ **Cấu hình công ty không làm được**:

---

## 3. Điểm bán hàng chủ lực

### 3.1 Phân tầng điểm bán hàng

| Tầng | Điểm bán hàng | Căn cứ hỗ trợ | Dùng cho |
|---|---|---|---|
| **Điểm bán hàng chính (duy nhất)** | | | Ảnh chính / hook video / tiêu đề |
| Điểm bán hàng phụ | | | Trang chi tiết / 5 gạch đầu dòng / video |
| Điểm bán hàng nền | | | Trang chi tiết |
| **Cách diễn đạt bị cấm** | | | ⛔ |

---

## 4. Phòng tránh rủi ro

| # | Loại rủi ro | Rủi ro cụ thể | Cách phòng tránh | Đặt ở đâu |
|---|---|---|---|---|
| 1 | Không khai khống thông số | | | 03 đoạn 4 |
| 2 | Không ghi từ thương hiệu | | | 03/04/05 |
| 3 | Nói trước vấn đề hậu mãi | | | 03 đoạn 6 |
| 4 | Ghi rõ giới hạn chức năng | | | 03 đoạn 6 |
| 5 | Không cam kết bừa | | | 03 đoạn 5 |

**Giới hạn cam kết hậu mãi** (bị ràng buộc bởi năng lực thực tế)

| Năng lực hậu mãi | Cam kết không được ghi |
|---|---|
| | |

---

## 5. 8 câu hỏi trước khi đăng bán

| # | Câu hỏi | Trả lời | Trạng thái |
|---|---|---|---|
| 1 | Bán cho ai | | |
| 2 | Điểm bán hàng cốt lõi | | |
| 3 | Đối thủ chính | | |
| 4 | Khoảng giá | | |
| 5 | SKU chủ lực | | |
| 6 | Mức lợi nhuận sàn | | |
| 7 | Có phù hợp test quảng cáo không | | |
| 8 | Rủi ro hậu mãi | | |

---

## 6. Cấu trúc chi phí

| SKU | Giá vốn sản phẩm | Vận chuyển chặng cuối | Phí lưu kho | Tổng |
|---|---|---|---|---|
| | | | | |

**Mức phí**: hoa hồng <n>% ｜ quảng cáo <n>% ｜ hoàn hàng <n>% ｜ biên LN mục tiêu <n>% ｜ thuế <n>%

⚠️ Ghi chú thuế: <đã tính vào chưa>

---

## 7. Tính giá

### 7.1 Công thức

```
Giá bán mục tiêu = tổng giá vốn ÷ (1 − % hoa hồng − % quảng cáo − % hoàn hàng − % biên lợi nhuận mục tiêu)
```

### 7.2 Tính ngược từng SKU

| SKU | Tổng giá vốn | Mẫu số | Giá bán mục tiêu tính ngược | Điểm neo thị trường | Chênh lệch |
|---|---|---|---|---|---|
| | | | | | |

### 7.3 Kiểm chứng chéo

| Hạng mục | Giá trị |
|---|---|
| Giá khả thi theo giá vốn do 01 tính ngược | |
| Giá bán mục tiêu tính ngược ở bước này | |
| Chênh lệch | |

**Kết luận**:

---

## 8. Phương án giá và kiểm tra

| SKU | Giá bán | LN gộp khả dụng trước QC | Tỷ trọng | LN sau QC | Biên LN ròng | Đạt | ROAS hòa vốn |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

### 8.1 Dư địa lợi nhuận

| SKU | Biên LN ròng thực tế | Mục tiêu | Dư địa | Mức voucher gánh được |
|---|---|---|---|---|

### 8.2 Vai trò chiến lược của SKU kéo traffic

| Hạng mục | Giá trị |
|---|---|
| Có nằm trên ngưỡng hòa vốn không | |
| Vai trò chiến lược | |
| Khối lượng chịu được | |
| Điều kiện thoát | |

---

## 9. Cấu trúc SKU

| Vai trò | Nội dung | Khác biệt cấu hình | Giá bán | Biên LN ròng | Nhiệm vụ |
|---|---|---|---|---|---|
| Kéo traffic | | | | | |
| **Chủ lực** | | | | | **Chốt đơn** |
| Cấu hình cao | | | | | Tăng AOV |
| Combo | | | | | **Tăng lợi nhuận** |

### 9.1 Bậc giá

| Hai bậc liền kề | Chênh giá | Biên độ | Kiểm tra |
|---|---|---|---|
| Kéo traffic → chủ lực | | | |
| Chủ lực → cấu hình cao | | | |
| Chủ lực → combo | | | |

### 9.2 Voucher

| Voucher | SKU áp dụng | Mệnh giá | Giá sau voucher | Chênh lệch được thu hẹp | Nguồn chi phí |
|---|---|---|---|---|---|

**Kiểm tra ngưỡng hòa vốn sau voucher**: ✅ / ❌

---

## 10. Chiến lược giá giai đoạn đầu

| Giai đoạn | Giá bán | Biên LN | Mục đích | Điều kiện nâng giá lại |
|---|---|---|---|---|
| Cold start | | | | |
| Giai đoạn nâng giá lại | | | | |
| Giai đoạn ổn định | | | | |

---

## 11. Các trường giao cho 06 Advertising

| SKU | Giá bán | LN gộp khả dụng trước QC | **ROAS hòa vốn** | % quảng cáo đề xuất | Chạy quảng cáo được |
|---|---|---|---|---|---|
| | | | | | |

**Giải thích**:

---

## 12. Quét tuân thủ đề xuất

| Quy tắc | Vi phạm | Xử lý |
|---|---|---|
| S1 Khai khống thông số | | |
| S2 Lách chứng nhận | | |
| S3 Chiến lược giá sai sự thật | | |
| S4 Cam kết hiệu quả | | |
| S5 Ra quyết định thu mua thay con người | | |

(Khi không có vi phạm: `Quét tuân thủ đề xuất: không có vi phạm`)

---

## 13. Các trường bàn giao

```yaml
product_type: {role: "", differentiation: "", promo_role: ""}
final_config: {}
core_selling_point: ""
secondary_points: []
forbidden_words_seed: []
risk_mitigation: []
after_sales_commitment: ""
sku_structure: []
main_sku: ""
pricing_table: {}
breakeven_roas_by_sku: {}
coupon_plan: []
ramp_up_plan: {}
strategic_loss_sku: null
prelaunch_checklist: {}
```

---

## 14. Nhắc nhở trước khi triển khai

- [ ] Thu mua đã xác nhận cấu hình sản xuất được (nhất là cấu hình khác biệt hóa)
- [ ] Đã kiểm tra thuế có được tính vào giá bán chưa
- [ ] Cam kết hậu mãi khớp với năng lực hậu mãi (không ghi điều làm không được)
- [ ] Đã đối chiếu tồn kho trước khi đăng ký chương trình (⚠️ chương trình Shopee đã đăng ký thì không rút ra được)
- [ ] Đã ghi lại số phiên bản Prompt của lần chạy này
```

---

## Downstream sử dụng thế nào

| Trường | Bên sử dụng | Mục đích |
|---|---|---|
| `core_selling_point` (điểm bán hàng chính duy nhất) | **03 / 04 / 05** | Copy chính trên ảnh chính, hook video, từ khóa tiêu đề |
| `secondary_points[]` | 03 / 04 / 05 | Trang chi tiết, 5 gạch đầu dòng, đoạn điểm bán hàng trong video |
| `forbidden_words_seed[]` | 03 / 04 / 05 | Danh sách chặn cứng |
| `after_sales_commitment` | 03 đoạn 5 | Cam kết hậu mãi (bị ràng buộc bởi năng lực) |
| `risk_mitigation[]` | 03 đoạn 6 | Đoạn lưu ý |
| `breakeven_roas_by_sku` | **06** | Đường chuẩn để đánh giá quảng cáo có lãi không |
| `strategic_loss_sku` | 06 / vận hành | Nếu có SKU lỗ chiến lược, khi chạy quảng cáo cần giới hạn trọng số của nó |

> **Chú ý tính duy nhất của `core_selling_point`**: toàn bộ chuỗi downstream của 03 đều dựa trên tiền đề "chỉ có một điểm bán hàng chính".
> Hai điểm bán hàng chính ngang hàng sẽ khiến ảnh chính có hai dòng chữ, đầu video nói hai chuyện —— cuối cùng người mua không nhớ được cái nào.
