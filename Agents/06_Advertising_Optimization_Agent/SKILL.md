---
name: sop-ecom-ads
description: >-
  Skill tầng ra quyết định quảng cáo cho thương mại điện tử xuyên biên giới, chuyên Shopee Brazil và Mercado Livre.
  Đọc báo cáo xuất từ quảng cáo → tính toán chính xác đến từng con số (ROAS hòa vốn / CPC chịu được / đóng góp ròng,
  có tính thuế phí Brazil) → danh sách hành động phân cấp P0/P1/P2.
  Chỉ đề xuất, không thực thi — không sửa trên trang quản trị, không tự động chỉnh giá thầu. Dùng khi người dùng muốn
  chẩn đoán quảng cáo, xem ROAS/ACOS, hạ ngân sách hạ giá thầu, phân tích quảng cáo lỗ, tổng kết sau đợt sale lớn.
  Các cụm tiếng Việt「chẩn đoán quảng cáo / quảng cáo lỗ / chỉnh ngân sách thế nào」và tiếng Trung
  「广告诊断 / 广告亏钱 / 预算怎么调」cũng kích hoạt Skill này.
  NOT for bot tự động chỉnh giá thầu, ghi thẳng vào trang quản trị của sàn, sản xuất creative video quảng cáo.
allowed-tools:
  - Bash(python *)
  - Read
  - Write
metadata:
  version: 0.4.0
  category: e-commerce/advertising-optimization
  license: MIT
---

# 06 · Advertising Optimization Skill (tầng ra quyết định)

> **Định vị**: **tầng ra quyết định** của quảng cáo, không phải bot. Nằm trên nguồn dữ liệu của bạn (báo cáo quảng cáo xuất từ sàn),
> tạo ra danh sách hành động「sửa gì, sửa thành bao nhiêu, căn cứ vào đâu」. **Việc thực thi do con người quyết định.**

---

## Ba nguyên tắc nền

1. **Không thực thi** — Skill này không bao giờ trực tiếp sửa ngân sách/giá thầu trên trang quản trị, danh sách hành động phải được người duyệt
2. **Không đoán số** — mọi chỉ số do `scripts/ad_metrics.py` tính, Agent chỉ diễn giải; nghi ngờ con số → `[METRIC_SUSPECT]`
3. **Không tạm dừng quảng cáo** — cách cắt lỗ là hạ ngân sách, hạ giá thầu; tạm dừng làm đứt tính liên tục và giảm điểm quảng cáo (xem nguyên tắc sắt trong [actions.md](references/actions.md))

---

## Bắt đầu nhanh (hai lệnh)

```bash
# 1) Tính ngưỡng hòa vốn và CPC chịu được — dùng preset sàn (dùng chung platform_fees.json với 02, có phí cố định theo bậc giá)
python scripts/ad_metrics.py calc --platform shopee_br --price 113.40 --product-cost 55 \
    --target-acos 25 --cvr 0.44

#    hoặc nhập tay (tham số tường minh được ưu tiên)
python scripts/ad_metrics.py calc --price 113.40 --product-cost 55 \
    --commission 14 --return 2 --tax 0 --target-acos 25 --cvr 0.44

# 2) Đọc báo cáo xuất từ quảng cáo → chẩn đoán toàn bộ + hành động phân cấp P0/P1/P2
python scripts/ad_metrics.py diagnose --file examples/sample-ad-report.csv \
    --price 113.40 --product-cost 55 --commission 14 --return 2 --tax 0 --target-acos 25
```

`--tax` là **thuế suất hiệu dụng tổng hợp** (ICMS/PIS/COFINS/Simples Nacional của Brazil quy đổi thành % trên giá bán).
Với thuế suất 8%, ROAS hòa vốn tăng từ 2.82 lên 3.64 — **ngưỡng hòa vốn không tính thuế là ngưỡng ảo**.

---

## Quy trình

```text
① calc      cấu trúc chi phí → ACoS/ROAS hòa vốn, CPC chịu được
② diagnose  CSV xuất từ quảng cáo → chỉ số phễu theo từng nhóm + phân cấp
③ đọc phân cấp → mở playbook tương ứng (references/playbooks.md)
④ tạo danh sách hành động (kèm danh sách「vòng này không động vào」)
⑤ người duyệt → thực thi → kiểm tra lại (retest) sau 3–7 ngày
```

---

## Thứ tự chẩn đoán (cố định, không được bỏ bước)

```text
Tầng 0 Độ đủ dữ liệu (hiển thị <1,000 → không động vào) → Tầng 1 Không có chi phí → Tầng 2 CTR<2% (quay vòng về 04)
→ Tầng 3 Click≥30 mà 0 đơn (quay vòng về 03, phía quảng cáo cắt lỗ) → Tầng 4 Phân cấp ROAS:
   < 0.5×hòa vốn = P0 cắt lỗ ｜ < hòa vốn = P1 cải thiện ｜ < mục tiêu = P1 giữ nguyên ｜ ≥ mục tiêu = P2 scale
```

Bảng quy tắc đầy đủ xem [references/diagnosis.md](references/diagnosis.md);
công thức và ánh xạ tên cột xem [references/metrics.md](references/metrics.md);
8 playbook theo tình huống xem [references/playbooks.md](references/playbooks.md);
thư viện hành động (điều kiện/mức độ/tần suất/rollback + nhịp ngân sách Shopee và nguyên tắc sắt "không tạm dừng") xem
[references/actions.md](references/actions.md).

---

## Ràng buộc riêng của Shopee BR (bắt buộc biết khi tự động hóa)

| Quy tắc | Nội dung |
|---|---|
| Nhịp ngân sách | 11:00 giờ Bắc Kinh → ngủ đông ở R$10; 23:30 giờ Bắc Kinh → khôi phục mức kích hoạt |
| Đã tiêu thì chỉ được tăng | Trong ngày đã phát sinh chi phí thì ngân sách **không được giảm** (đợi hôm sau reset) |
| Popup xác nhận lần hai | Bấm xác nhận xong còn bước「Vui lòng xác nhận trước khi sửa → Tiếp tục sửa」 |

---

## Giới hạn đã biết

| Giới hạn | Giải thích |
|---|---|
| **Không thực thi** | Danh sách hành động để người duyệt; ghi vào trang quản trị thuộc hướng B, chưa triển khai |
| Chưa nối báo cáo từ khóa tìm kiếm | Phân tích từ khóa tìm kiếm/từ khóa phủ định cần file xuất từ sàn (khung sqp còn thiếu, xem ROADMAP) |
| Ngưỡng là giá trị kinh nghiệm của Shopee Brazil | Các chuẩn như CTR 3–5% lấy từ SOP và thực chiến, mỗi ngành hàng cần hiệu chỉnh lại |
| Thuế suất là cách tính đơn giản hóa | Gộp thành một tham số thuế suất hiệu dụng, không phản ánh chi tiết thuế thực tế |
| Sàn không có API công khai | Shopee không có API quảng cáo cho người bán → dữ liệu dựa vào xuất tay hoặc tự động hóa trình duyệt |
