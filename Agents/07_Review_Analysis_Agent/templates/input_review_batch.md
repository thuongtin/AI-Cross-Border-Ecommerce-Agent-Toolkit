# Template đầu vào · Nhập lô đánh giá

> ⚠️ **Bắt buộc ẩn danh hóa trước khi nhập**: xóa nickname người mua, mã đơn hàng, URL avatar, thông tin cá nhân có thể định danh.
> Nguyên văn đánh giá **giữ ngôn ngữ gốc** (tiếng Bồ Đào Nha / Tây Ban Nha), không dịch trước — dịch sẽ làm mất manh mối diễn đạt (như từ đặc trưng của loại hiểu lầm "esperava que").

---

## 0. Cấu hình task

```yaml
platform*: shopee
target_market*: Brazil
product_name*: ""
analysis_scope*: own          # own (chỉ phía mình) | competitor (chỉ đối thủ) | both (so sánh)
```

---

## 1. Dữ liệu chuẩn ★ Mục chặn

> **Thiếu hai phần này, Agent không thể phán định "thông số không khớp" và "thiếu phụ kiện" là vấn đề thật hay hiểu lầm.** Agent sẽ từ chối chạy.

```yaml
# ── Dán từ đầu ra của 03 Listing Creative ──

spec_table*: {}
# Ví dụ:
#   autonomia: "até 35 km"
#   capacidade_carga: "150 kg"
#   peso_produto: "18 kg"
#   tempo_recarga: "5 a 6 horas"

package_content*: []
# Ví dụ:
#   - "1× Patinete Elétrico"
#   - "1× Carregador 42V"
#   - "1× Manual em português"
#   - "(Não incluso: capacete)"     ← ghi rõ "không kèm gì" là cực kỳ quan trọng

usage_scope*: []
# Ví dụ:
#   - "Deslocamento urbano em vias planas e pavimentadas"
#   - "Lazer em parques e ciclovias"
#   - "Trajeto casa-trabalho em distâncias curtas"

warranty*: ""                 # Ví dụ: "6 meses (motor e bateria)"
```

---

## 2. Listing hiện tại (để phán định "thiếu giải thích" hay "giải thích không nổi bật")

```yaml
current_title: ""
current_description: ""        # Toàn văn trang chi tiết (hoặc dán theo đoạn, ghi số thứ tự đoạn)
current_image_plan: []         # Kế hoạch 9 ảnh của 04 (tùy chọn)
# Ví dụ:
#   - {slot: 1, role: "Ảnh chính"}
#   - {slot: 8, role: "Ảnh danh sách đóng gói"}
```

> Có hai mục này, Agent mới phân biệt được:
> - Hoàn toàn không nhắc → **thiếu giải thích** → thêm mục mới
> - Có nhắc nhưng bị chìm → **giải thích không nổi bật** → đưa lên đầu
> - Rất nổi bật mà vẫn bị hiểu lầm → **người mua không đọc** → đổi cách diễn đạt (chuyển thành ảnh)

---

## 3. Dữ liệu đánh giá

> **Định dạng**: dùng mảng JSON hoặc CSV. Mỗi đánh giá tối thiểu có `text` / `rating` / `source`.

```json
[
  {
    "id": "R001",
    "text": "<nguyên văn, giữ ngôn ngữ gốc>",
    "rating": 5,
    "has_image": true,
    "source": "own",
    "date": "2026-09-15"
  },
  {
    "id": "R002",
    "text": "",
    "rating": 1,
    "has_image": false,
    "source": "own",
    "date": "2026-09-20"
  }
]
```

### Mô tả trường

| Trường | Bắt buộc | Mô tả |
|---|---|---|
| `id` | ✅ | Mã tự đặt (**không dùng ID đánh giá của sàn**, tránh truy ngược được) |
| `text` | ✅ | Nguyên văn đánh giá, **giữ ngôn ngữ gốc và lỗi chính tả** |
| `rating` | ✅ | Số sao (dùng để chia nhóm tích cực/tiêu cực) |
| `has_image` | ✅ | Có ảnh hay không (dùng để đánh giá chất lượng đánh giá, chính là "số đánh giá có ảnh" mà SOP nhắc tới) |
| `source` | ✅ | `own` / `competitor_A` / `competitor_B` (**dùng mã, không dùng tên shop thật**) |
| `date` | ⭕ | Tiện xem xu hướng theo thời gian (như một vấn đề có tập trung ở một lô hàng nào không) |

### Gợi ý chọn đánh giá

| Gợi ý | Lý do |
|---|---|
| **Ưu tiên nhập toàn bộ đánh giá tiêu cực** | Mật độ thông tin của đánh giá tiêu cực cao hơn hẳn đánh giá tích cực |
| Đánh giá tích cực có thể lấy mẫu (ví dụ 50 cái gần nhất) | Đánh giá tích cực khá đồng nhất, lấy đủ mẫu là xác định được điểm hay được khen |
| Đừng bỏ đánh giá trung lập (3 sao) | Đánh giá trung lập phản ánh rõ nhất khoảng hụt cụ thể kiểu "chỉ thiếu chút nữa là hài lòng" |
| Đánh giá đối thủ nhập từ shop top đầu cùng ngành hàng | Dùng để so sánh "đối thủ bán được nhờ đâu" |
| Giữ nguyên lỗi chính tả | Cách viết `nao` / `não` phản ánh thói quen ngôn ngữ của người mua |

---

## 4. Trọng tâm phân tích (tùy chọn)

```yaml
focus:
  - "Vì sao đánh giá tiêu cực tập trung vào khả năng leo dốc"     # Điền khi có câu hỏi cụ thể, Agent sẽ trả lời riêng
  - ""
```

---

## Tự kiểm tra khi điền

- [ ] Đã ẩn danh hóa (không nickname, mã đơn hàng, URL avatar)
- [ ] Đã điền `spec_table` và `package_content` (thiếu thì Agent từ chối chạy)
- [ ] Đã điền `usage_scope` (dùng để phán định hiểu lầm về tình huống sử dụng)
- [ ] Nguyên văn đánh giá **giữ ngôn ngữ gốc**, không dịch trước
- [ ] Nguồn đối thủ dùng mã (`competitor_A`), không điền tên shop thật
- [ ] Đã nhập toàn bộ đánh giá tiêu cực, đánh giá tích cực có thể lấy mẫu
- [ ] Không bỏ đánh giá trung lập (3 sao)
- [ ] Mỗi đánh giá đều có `rating` và `has_image`
- [ ] Tổng số đánh giá ≥ 20 (dưới mức này Agent sẽ ghi chú "mẫu chưa đủ")
