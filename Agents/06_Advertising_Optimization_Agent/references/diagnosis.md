# diagnosis.md · Quy tắc chẩn đoán (khớp một-một với logic của script)

> **Thứ tự chẩn đoán cố định, không được bỏ bước** — vấn đề ở tầng trên sẽ che lấp vấn đề ở tầng dưới.
> Mỗi nhóm quảng cáo đi từ trên xuống, tầng đầu tiên bị trúng sẽ quyết định hành động của vòng này.

```text
Tầng 0  Độ đủ dữ liệu (hiển thị < 1,000 → INFO, vòng này không động vào, gom thêm dữ liệu)
Tầng 1  Không có chi phí (→ INFO)
Tầng 2  CTR < 2% (→ vấn đề creative, quay vòng về 04 — không xử lý vấn đề creative ở phía quảng cáo)
Tầng 3  Click ≥ 30 mà 0 đơn (→ vấn đề trang đích/giá, quay vòng về 03; phía quảng cáo chỉ hạ giá thầu để cắt lỗ)
Tầng 4  Phân cấp ROAS (so với ngưỡng hòa vốn và mục tiêu, xem bảng dưới)
```

---

## Bảng phân cấp ROAS

Đặt ROAS hòa vốn = `BE`, ROAS mục tiêu = `T` (= 1 ÷ ACoS mục tiêu):

| Điều kiện | Cấp | Hành động cốt lõi |
|---|---|---|
| ROAS < 0.5 × BE | **P0 cắt lỗ** | Hạ ngân sách về mức thấp nhất + hạ giá thầu xuống dưới CPC chịu được; **❗ không tạm dừng** |
| 0.5 × BE ≤ ROAS < BE | **P1 cải thiện** | Hạ giá thầu xuống dưới CPC chịu được, **giữ nguyên ngân sách**; CVR<1% thì quay vòng về 03/07 |
| BE ≤ ROAS < T | **P1 giữ nguyên** | Giữ nguyên cả ngân sách lẫn giá thầu, cải thiện tỷ lệ chuyển đổi là đòn bẩy duy nhất |
| ROAS ≥ T | **P2 scale** | Ngân sách +20~30% (mỗi lần một nấc), theo dõi 3 ngày |

> Vì sao lấy **0.5 × BE** làm ngưỡng P0: ROAS còn chưa tới một nửa ngưỡng hòa vốn,
> nghĩa là không phải "mua đắt" mà là "sai hoàn toàn", tiếp tục tối ưu theo nhịp bình thường chỉ là lỗ rỉ rả kéo dài.

---

## Ba nhận thức nền tảng (mỗi điều đều có dữ liệu case study chứng minh)

**① Đường chuẩn và ngưỡng hòa vốn là hai chuyện khác nhau.**
Một nhóm quảng cáo có thể đạt hết CTR 4.4%, CVR 1.44%, tỷ lệ thêm vào giỏ 11.2%,
mà ROAS 2.73 vẫn dưới ngưỡng hòa vốn 2.82 — vì CPC gấp đôi các nhóm khác.
**Phễu khỏe ≠ có lãi.**

**② Sửa CTR có thể làm lỗ nặng hơn.**
CTR 1.4% → 3.0% (tỷ lệ chuyển đổi 0.44% không đổi):
đóng góp ròng −R$235 → **−R$335**. Cho thêm traffic không đạt chuẩn vào = tốn thêm tiền.
**Trước hết hỏi tỷ lệ chuyển đổi có đỡ nổi không, rồi mới tối ưu click.**

**③ Khi nút thắt nằm ở chuyển đổi, tăng hiển thị = tăng lỗ.**
Tỷ lệ chuyển đổi không đổi, click 2,017 → 3,000: đóng góp ròng −R$236 → **−R$218? Không,
là −R$353**. Lượt hiển thị không đổi ra tiền, chỉ đổi ra hóa đơn.

---

## Vòng này dứt khoát không động vào (kỷ luật iterate)

Mỗi lần chẩn đoán, đầu ra **bắt buộc có** danh sách「vòng này dứt khoát không động vào」:

| Trạng thái ROAS vòng này | Dứt khoát không động vào |
|---|---|
| Nhóm đang lỗ (P0/P1 cải thiện) | Nội dung Listing, creative — chỉ động vào giá thầu/ngân sách phía quảng cáo |
| Trên ngưỡng hòa vốn (P1 giữ nguyên / P2) | Ngân sách, cấu trúc giá thầu — chỉ tối ưu tỷ lệ chuyển đổi |

Mỗi lần chỉ sửa một nguyên nhân gốc; chỉ số kiểm tra lại = chỉ số mà khâu được sửa kiểm soát được (hành động quảng cáo thì xem ROAS,
hành động nội dung thì xem tỷ trọng đánh giá tiêu cực loại hiểu lầm), **không nhìn tổng doanh số**.
