# platform-title-rules.md · Bảng quy tắc tiêu đề (nguồn gốc ngưỡng)

> Ngưỡng lấy từ quy tắc chính thức của từng sàn và SOP, **trước khi đăng phải vào Seller Center kiểm tra lại**.

---

## Shopee (giới hạn 120 ký tự)

| Quy tắc | Nội dung | Mức |
|---|---|---|
| Giới hạn ký tự | 120 ký tự (30 ký tự đầu có trọng số cao nhất, từ khóa chính bắt buộc đặt lên đầu) | Cứng |
| Emoji | Cấm dùng trong tiêu đề | Cứng |
| Viết hoa toàn bộ | Cấm viết hoa tràn lan (chấp nhận tên viết tắt thương hiệu) | Mềm |
| Nhồi từ khóa | Cùng một từ lặp ≥3 lần là nhồi từ khóa | Cứng |
| Từ khuyến mãi | Cẩn trọng (frete grátis... là thông tin khuyến mãi, nên đưa vào ảnh / mô tả) | Mềm |
| Ngôn ngữ | PT-BR (xuất hiện tiếng Trung = sai ngay) | Cứng |
| Tỷ lệ sử dụng | Khuyến nghị ≥80% (viết không đủ là lãng phí traffic miễn phí) | Mềm |

## Mercado Livre (giới hạn 60 ký tự)

| Quy tắc | Nội dung | Mức |
|---|---|---|
| Giới hạn ký tự | **60 ký tự** — chặt nhất, thứ tự cắt từ: từ ngữ cảnh → từ nhóm khách hàng → **không bao giờ cắt từ khóa chính và thông số cốt lõi** | Cứng |
| Từ khuyến mãi | Khuyến cáo rõ là không dùng (envío/frete grátis...) | Mềm |
| Ngôn ngữ | PT-BR | Cứng |

## Amazon (giới hạn 200 ký tự)

| Quy tắc | Nội dung | Mức |
|---|---|---|
| Giới hạn ký tự | 200 (trên mobile nên đặt thông tin chính trong 80 ký tự) | Cứng |
| Thương hiệu đứng đầu | Tiêu đề bắt đầu bằng tên thương hiệu | Mềm |

---

## Ghi chú về cách kiểm tra (title_lint.py)

- **Số ký tự = `len()`**, không phải số byte. `á`/`ç` của PT-BR chiếm 2 byte trong UTF-8 —
  tính theo byte sẽ báo nhầm tiêu đề chuẩn là vượt giới hạn. Đây chính là nguồn gốc chênh lệch giữa "đo thực tế và ước lượng".
- So khớp từ cấm **không phân biệt hoa thường**, xuất kết quả theo nguyên từ (không tách iPhone thành từng chữ cái).
- Danh sách từ khuyến mãi có sẵn 17 từ thường gặp (PT/EN/CN/VI), có thể dùng `--forbidden` để thêm danh sách riêng.
