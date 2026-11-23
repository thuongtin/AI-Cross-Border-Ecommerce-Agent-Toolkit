# playbooks.md · Playbook theo tình huống

> 8 tình huống thường gặp nhất. Mỗi playbook có năm phần: **Triệu chứng → Thứ tự chẩn đoán → Hành động → Vòng này không động vào → Kiểm tra lại**.
> Chạy `scripts/ad_metrics.py diagnose` để lấy phân cấp trước, rồi mới mở playbook tương ứng.

---

## Playbook 1 · Sản phẩm mới khởi động lạnh (chưa có dữ liệu)

**Triệu chứng**: nhóm quảng cáo vừa tạo, lượt hiển thị < 1,000.
**Chẩn đoán**: tất cả các nhóm rơi vào tầng 0 (INFO), không sinh ra hành động nào.
**Hành động**: chỉ làm hai việc — ① xác nhận ngân sách đủ mua lượng hiển thị tối thiểu; ② tự kiểm tra điểm cơ bản của Listing trước (tiêu đề/ảnh chính/dải giá, dùng checklist tự kiểm tra của 03/04).
**Không động vào**: giá thầu (chưa có dữ liệu để làm căn cứ cho bất kỳ điều chỉnh nào).
**Kiểm tra lại**: chạy lại diagnose khi lượt hiển thị vượt 1,000.

---

## Playbook 2 · Lỗ toàn bộ (ROAS tổng < ngưỡng hòa vốn)

**Triệu chứng**: diagnose cho đóng góp ròng tổng < 0.
**Thứ tự chẩn đoán**: trước hết xem **có nhóm nào đạt chuẩn không** (có P2 = cấu trúc không có vấn đề, vấn đề nằm ở giá/ngân sách);
sau đó xem tỷ trọng chi phí của các nhóm P0 (>50% = ưu tiên cắt lỗ).
**Hành động**: cắt lỗ toàn bộ nhóm P0 → nhóm P1 hạ giá thầu về CPC chịu được → chạy lại calc xem bản thân ngưỡng hòa vốn có hợp lý không
(**nếu ngưỡng hòa vốn sau thuế cao vô lý, hãy sửa định giá trước, đừng sửa quảng cáo** — xem ví dụ thuế trong metrics.md).
**Không động vào**: các nhóm đã đạt chuẩn (chúng không phải là vấn đề, đừng quậy luôn cả chúng).
**Kiểm tra lại**: chạy diagnose sau 3 ngày, xem tốc độ đóng góp ròng tiến về 0.

---

## Playbook 3 · Cắt lỗ một nhóm (P0)

**Triệu chứng**: một nhóm có ROAS < 0.5 × ngưỡng hòa vốn.
**Hành động**: hạ giá thầu xuống dưới CPC chịu được + hạ nấc ngân sách; **không tạm dừng** (xem nguyên tắc sắt trong actions.md).
**Không động vào**: creative và Listing (giai đoạn cắt lỗ mỗi lần chỉ sửa một nguyên nhân gốc).
**Kiểm tra lại**: 3 ngày. ROAS vẫn < 0.5×BE → hạ ngân sách thêm một nấc; lên tới 0.5–1.0×BE → chuyển sang playbook 4.

---

## Playbook 4 · Nhóm sát ngưỡng hòa vốn (P1 cải thiện)

**Triệu chứng**: 0.5×BE ≤ ROAS < BE, các khâu của phễu về cơ bản khỏe.
**Hành động**: **chỉ hạ giá thầu** xuống dưới CPC chịu được. Vấn đề của nhóm này gần như luôn là「mua đắt」chứ không phải「mua sai」.
**Không động vào**: ngân sách, creative, Listing.
**Kiểm tra lại**: 3 ngày. ROAS vượt ngưỡng hòa vốn → theo dõi xem có chạm mục tiêu không; không vượt → kiểm tra CPC đã về tới mức chịu được chưa (về tới rồi mà vẫn lỗ = bản thân ngưỡng hòa vốn tính sai hoặc sản phẩm hết cứu, quay lại phần kiểm tra định giá ở playbook 2).

---

## Playbook 5 · Đạt chuẩn thì scale (P2)

**Triệu chứng**: ROAS ≥ mục tiêu.
**Hành động**: ngân sách +20~30%, theo dõi 3 ngày, ổn định thì tăng nấc tiếp; tăng ngân sách tối đa mà vẫn có lãi → nhân bản cấu trúc sang nhóm mới.
**Không động vào**: giá thầu (giai đoạn scale mà tăng giá thầu là dễ kéo ROAS tụt lại nhất).
**Kiểm tra lại**: sau mỗi nấc tăng 3 ngày, xem ROAS có giữ được không.

---

## Playbook 6 · CTR thấp (hiển thị nhiều, click ít)

**Triệu chứng**: CTR < 2%, lượng click không đủ.
**Chẩn đoán**: đây là **vấn đề creative**, chỉnh giá thầu/ngân sách phía quảng cáo không giải quyết được.
**Hành động**: quay vòng về 04 (chế độ iterate, chỉ đổi ảnh đầu) → sau khi ảnh đầu mới lên, kiểm tra lại CTR trong 3–5 ngày.
**Không động vào**: mọi tham số phía quảng cáo.
**Kiểm tra lại**: CTR; nếu CTR đã sửa xong mà ROAS vẫn lỗ → quay lại playbook 2/4.

---

## Playbook 7 · CVR thấp (click nhiều, đơn ít)

**Triệu chứng**: click ≥ 30 và CVR < 1%.
**Chẩn đoán**: vấn đề ở trang đích/giá/số lượng đánh giá. Kiểm tra số đánh giá nền trước (link mới chưa có đánh giá thì xây đánh giá nền trước rồi mới bàn chuyện chuyển đổi).
**Hành động**: quay vòng về 03 (đoạn lưu ý trên trang chi tiết) + quay vòng về 07 (quy nguyên nhân đánh giá tiêu cực để tìm điểm hiểu lầm); phía quảng cáo chỉ ép giá thầu về mức chịu được.
**Không động vào**: ngân sách.
**Kiểm tra lại**: CVR, 7 ngày.

---

## Playbook 8 · Tổng kết sau đợt sale lớn (như Black Friday)

**Triệu chứng**: trong đợt sale lớn ROAS dao động mạnh, ngưỡng thường ngày mất tác dụng.
**Chẩn đoán**: trong đợt sale lớn **không dùng** ngưỡng hòa vốn để đánh giá (sale lớn vốn dĩ là đổi lợi nhuận lấy traffic và thứ hạng).
**Hành động**: trong đợt sale chỉ giữ hai điều — ① ngân sách không bị tiêu cạn sớm (thực hiện theo nhịp); ② cấm mọi hành động cắt lỗ P0 (giá trị traffic của đợt sale nằm ở sau sale).
**Không động vào**: mọi hành động tối ưu, dời hết sang 7 ngày sau đợt sale mới chạy diagnose thường lệ.
**Kiểm tra lại**: ngày thứ 7 sau đợt sale chạy một lần diagnose thường lệ, xem thay đổi về điểm quảng cáo và traffic tự nhiên.
