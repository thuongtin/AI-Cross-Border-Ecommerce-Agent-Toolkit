# metrics.md · Công thức và cách tính

> Mọi con số do `scripts/ad_metrics.py` tính, Agent **chỉ diễn giải, không tính lại** (cùng kỷ luật với module 01).
> Nghi ngờ con số có vấn đề → xuất `[METRIC_SUSPECT]` và yêu cầu người dùng kiểm tra lại tham số của script.

---

## I. Mô hình chi phí (nền móng của ngưỡng hòa vốn)

```text
Đóng góp trước quảng cáo = Giá bán − Giá vốn − Vận chuyển chặng đầu − Vận chuyển chặng cuối − Giá bán×Hoa hồng% − Giá bán×Hao hụt hoàn hàng% − Giá bán×Thuế suất%
ACoS hòa vốn = Đóng góp trước quảng cáo ÷ Giá bán
ROAS hòa vốn = 1 ÷ ACoS hòa vốn = Giá bán ÷ Đóng góp trước quảng cáo
```

| Tham số | Cờ CLI | Giải thích |
|---|---|---|
| Giá bán | `--price` | Giá bán đã gồm thuế, R$ |
| Giá vốn + vận chuyển | `--product-cost` | **Giá vốn về tới kho** (nếu đã gồm vận chuyển chặng đầu/chặng cuối thì tính hết ở đây, đừng điền thêm shipping để tránh tính trùng) |
| Hoa hồng sàn | `--commission` | Shopee BR khoảng 14% (gồm phí giao dịch), ML khoảng 13–17% tùy ngành hàng |
| Hao hụt hoàn hàng | `--return` | Cách tính đơn giản: tỷ lệ hoàn hàng × tổn thất giá trị hàng |
| **Thuế suất hiệu dụng tổng hợp** | `--tax` | Hệ thống thuế Brazil phức tạp (ICMS/PIS/COFINS/Simples Nacional), **quy đổi thành một tham số "% trên giá bán"**, điền theo chế độ thuế của mình |

### Ảnh hưởng của thuế đến ngưỡng hòa vốn (đo thực tế, case sạc dự phòng)

```text
Thuế suất 0%: Đóng góp trước quảng cáo R$ 40.26  → ROAS hòa vốn 2.82
Thuế suất 8%: Đóng góp trước quảng cáo R$ 31.18  → ROAS hòa vốn 3.64   ← ngưỡng tăng 29%
```

**Thuế suất không phải tùy chọn.** Ngưỡng hòa vốn tính mà không có thuế sẽ khiến bạn tưởng đơn không lỗ trong khi thực ra đang lỗ.

---

## II. Công thức giá thầu

```text
CPC chịu được = Giá bán × Tỷ lệ chuyển đổi × ACoS mục tiêu
ROAS mục tiêu = 1 ÷ ACoS mục tiêu
```

- ACoS mục tiêu do người dùng đặt (phải thấp hơn ngưỡng hòa vốn mới có lãi; thường 20–30%)
- CPC hiện tại **cao hơn** CPC chịu được → mỗi click đều đang làm lỗ nhanh hơn

---

## III. Định nghĩa chỉ số phễu

| Chỉ số | Công thức | Chuẩn (tham khảo Shopee BR, nguồn SOP 3.6) |
|---|---|---|
| CTR | Click ÷ Lượt hiển thị | 3–5%; **<2% là thấp rõ ràng** |
| CVR | Đơn ÷ Click | **≥1%** |
| CPC | Chi phí ÷ Click | So với CPC chịu được |
| ACoS | Chi phí ÷ Doanh thu quảng cáo | So với ngưỡng hòa vốn/mục tiêu |
| ROAS | Doanh thu quảng cáo ÷ Chi phí | = 1 ÷ ACoS |
| Đóng góp ròng | Đóng góp trước quảng cáo/Giá bán × GMV − Chi phí | **<0 = lỗ** |

> **Đường chuẩn và ngưỡng hòa vốn là hai chuyện khác nhau** (nhận thức cốt lõi của module này): đường chuẩn cho biết "khâu nào không khỏe",
> ngưỡng hòa vốn cho biết "có lãi hay không". Phễu đạt chuẩn hết vẫn có thể lỗ (mua CPC đắt).

---

## IV. Tự động ánh xạ tên cột CSV (dùng cho diagnose)

| Ý nghĩa | Tên cột nhận diện được (không phân biệt hoa thường) |
|---|---|
| Tên quảng cáo | Tên quảng cáo / Nhóm quảng cáo / Tên chiến dịch / Chiến dịch / 广告名称 / 广告组 / 计划名称 / campaign / name / campanha |
| Lượt hiển thị | Lượt hiển thị / Hiển thị / 曝光量 / 曝光 / impressions / imps / impressoes |
| Click | Lượt click / Lượt nhấp / 点击量 / 点击 / clicks / cliques |
| Chi phí | Chi phí / Chi tiêu / 花费 / 消耗 / spend / cost / gasto |
| Đơn | Số đơn / Đơn hàng / Lượt chuyển đổi / 订单数 / 订单 / orders / conversions / pedidos |
| Doanh thu (tùy chọn) | Doanh thu / Doanh số / 销售额 / 成交金额 / gmv / sales / receita |

- Cột không nhận ra sẽ **báo lỗi và liệt kê ra**, không đoán bừa
- Số chấp nhận định dạng bẩn như `R$ 1.234,56` / `1,234` / `12.3%` / `-`
- Khi thiếu doanh thu thì tính bù bằng `Đơn × Giá bán`

---

## V. Ngưỡng đủ dữ liệu

| Ngưỡng | Mặc định | Lý do |
|---|---|---|
| Lượt hiển thị | **≥ 1,000**/nhóm | Dưới ngưỡng này CTR/CVR toàn là nhiễu, ra tay quá sớm = chạy theo nhiễu |
| Click (để xét 0 đơn) | ≥ 30 | 30 click mà 0 đơn mới có ý nghĩa thống kê |
