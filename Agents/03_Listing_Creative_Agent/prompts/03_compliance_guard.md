# TASK · Quét tuân thủ (task độc lập)

> Dùng kèm: `00_system.md`
>
> Prompt này có thể **dùng riêng** — không nhất thiết phải chạy 01/02, có thể lấy thẳng một Listing có sẵn (tự viết, tham khảo đối thủ, tồn đọng từ trước) đưa vào để rà soát tuân thủ.

---

# Ngữ cảnh sử dụng

| Ngữ cảnh | Đầu vào | Đầu ra |
|---|---|---|
| **Trong luồng** | Sản phẩm đầu ra của 01/02 | Kết quả chặn + bản đã viết lại + `forbidden_words[]` |
| **Rà soát riêng** | Bất kỳ văn bản Listing có sẵn | Danh sách rủi ro + gợi ý viết lại từng mục |
| **Chốt cuối trước khi đăng bán** | Bộ nội dung sáng tạo hoàn chỉnh | Đạt / Không đạt + các mục chặn |

---

# INPUT

Trường bắt buộc:

| Trường | Mô tả |
|---|---|
| `scan_target` | Văn bản cần quét (tiêu đề / mô tả / chữ trong ảnh / phụ đề / cả bộ nội dung sáng tạo) |
| `platform` | Sàn mục tiêu |
| `target_market` | Thị trường mục tiêu |
| `spec_table` | **Chuẩn thông số** — dùng để kiểm tra tính xác thực của mọi giá trị số (R3) |
| `brand_authorization` | Danh sách thương hiệu đã được ủy quyền (có thể là mảng rỗng) |
| `usage_scope[]` | Các ngữ cảnh sử dụng được phép nêu (R6) |
| `mode` | `in_flow` (trong luồng, cần xuất bản viết lại) / `audit_only` (chỉ xuất báo cáo) |

---

# SCAN RULES

Quét lần lượt bảy loại dưới đây. **Mỗi mục phải có kết luận rõ ràng**, không được viết "có vẻ", "có thể".

```
R1 Từ ngữ tuyệt đối hóa
   Kho từ cấm: o melhor / mais rápido / 100% / perfeito / garantido /
            incomparável / único / nº1 / à prova de tudo / indestrutível
   Phạm vi kiểm tra: toàn bộ văn bản người mua nhìn thấy (gồm chữ trong ảnh, phụ đề)
   Xử lý: viết lại thành cách diễn đạt định lượng, kiểm chứng được

R2 Tên thương hiệu chưa được ủy quyền
   Quy tắc: mọi tên thương hiệu / tên model xuất hiện trong văn bản phải có trong brand_authorization
   Phạm vi kiểm tra: tiêu đề, mô tả, bảng thông số, chữ trong ảnh, phụ đề
   Xử lý: thay bằng "Compatível com <marca> <modelo>", hoặc xóa

R3 Khai khống thông số
   Quy tắc: mọi giá trị số (con số + đơn vị) xuất hiện trong văn bản phải tìm được mục tương ứng trong spec_table
   Phạm vi kiểm tra: tiêu đề, mô tả, bảng thông số, chữ trong ảnh, phụ đề
   Xử lý: không có mục tương ứng → xóa giá trị đó + ghi [PARAM_DROPPED]
        có mục tương ứng nhưng giá trị khác → sửa về giá trị trong spec_table + ghi [PARAM_FIXED]

R4 Từ khuyến mãi trong tiêu đề
   Cấm: tiêu đề xuất hiện khuyến mãi / miễn phí vận chuyển / trả góp / con số giảm giá / giới hạn thời gian
   Xử lý: chuyển ra khỏi tiêu đề + ghi [MOVE_TO_DESCRIPTION]

R5 Nội dung nhạy cảm
   Cấm: công dụng y tế (cura / previne / trata),
        cam kết an toàn tuyệt đối (não causa nenhum risco / seguro para todos),
        lợi nhuận tài chính (lucro garantido / renda extra garantida)
   Xử lý: xóa + ghi [SENSITIVE_REMOVED]

R6 Ngữ cảnh vượt phạm vi
   Quy tắc: ngữ cảnh sử dụng trong mô tả phải nằm trong usage_scope
   Xử lý: vượt phạm vi → xóa ngữ cảnh đó + ghi [SCENE_DROPPED]

R7 Chứng cứ giả mạo
   Cấm: dấu chứng nhận bịa đặt (INMETRO / ANATEL / CE / FCC / RoHS),
        số lượng bán bịa đặt (+10.000 vendidos), đánh giá bịa đặt (ảnh chụp màn hình / trích dẫn),
        ủy quyền chính hãng bịa đặt (loja oficial / autorizado, nếu không có ủy quyền)
   Xử lý: xóa + ghi [FAKE_PROOF_REMOVED]
```

---

# Cấu trúc đầu ra

## mode = in_flow

```markdown
## 1. Tổng quan kết quả quét

| Quy tắc | Số lần dính | Mức độ nghiêm trọng | Trạng thái xử lý |
|---|---|---|---|
| R1 Từ ngữ tuyệt đối hóa | 2 | Trung bình | Đã viết lại |
| R2 Tên thương hiệu chưa được ủy quyền | 1 | **Cao** | Đã thay thế |
| R3 Khai khống thông số | 0 | — | — |
| R4 Từ khuyến mãi trong tiêu đề | 1 | Trung bình | Đã chuyển ra |
| R5 Nội dung nhạy cảm | 0 | — | — |
| R6 Ngữ cảnh vượt phạm vi | 1 | Trung bình | Đã xóa |
| R7 Chứng cứ giả mạo | 0 | — | — |

**Kết luận**: dính 5 mục, trong đó 1 mục nguy cơ cao. Tất cả đã được xử lý.

## 2. Chi tiết từng mục

| # | Quy tắc | Vị trí trong bản gốc | Đoạn trích gốc | Vấn đề | Sau khi viết lại |
|---|---|---|---|---|---|
| 1 | R2 | Tiêu đề | `... iPhone 15 ...` | Tên thương hiệu chưa được ủy quyền | `Compatível com iPhone` |
| ... | | | | | |

## 3. Toàn văn sau khi viết lại
(xuất khi mode = in_flow; khi mode = audit_only thì ghi "(Chỉ rà soát, không xuất bản viết lại)")

## 4. forbidden_words (để 04 / 05 chặn cứng)
["<từ 1>", "<từ 2>", ...]

## 5. Phán định đạt

| Mục kiểm tra | Kết quả |
|---|---|
| Đã loại bỏ toàn bộ mục nguy cơ cao (R2 / R3 / R7) | ✅ / ❌ |
| Tiêu đề không có từ khuyến mãi, không có từ ngữ tuyệt đối hóa | ✅ / ❌ |
| Mọi giá trị số đều truy được nguồn | ✅ / ❌ |
| Mọi ngữ cảnh đều trong phạm vi | ✅ / ❌ |
| **Có thể đăng hay không** | ✅ Có thể đăng / ❌ Có mục chặn: <liệt kê> |
```

---

# Định nghĩa mức độ nghiêm trọng

| Mức | Quy tắc | Ý nghĩa |
|---|---|---|
| **Nguy cơ cao** | R2 / R3 / R7 | Sàn sẽ phán là vi phạm, có thể dẫn tới bị gỡ sản phẩm, bị trừ điểm, bị khiếu nại vi phạm bản quyền. **Bắt buộc loại bỏ mới được đăng** |
| Nguy cơ trung bình | R1 / R4 / R6 | Ảnh hưởng hiệu quả chuyển đổi hoặc có rủi ro tuân thủ tiềm ẩn, sàn có thể không chủ động phạt nhưng rủi ro sẽ tích tụ |
| Nguy cơ thấp | R5 | Tùy mức độ diễn đạt, nội dung liên quan y tế / an toàn thì xử lý như nguy cơ cao |

---

# Quy tắc ranh giới

1. **Chỉ báo cáo, không phỏng đoán.** Chỉ đánh dấu vấn đề có bằng chứng rõ ràng trong văn bản. Không suy diễn kiểu "câu này có thể ngụ ý…".
2. **Không đánh giá thẩm mỹ.** Quét tuân thủ không đánh giá câu chữ hay hay dở, có hấp dẫn hay không.
3. **Viết lại phải tối thiểu.** Chỉ sửa phần vi phạm, phần còn lại giữ nguyên. Đừng nhân tiện viết lại cả đoạn.
4. **Sau khi viết lại phải quét lại.** Văn bản viết lại có thể phát sinh vấn đề mới (ví dụ thay tên thương hiệu xong lại tạo ra cách diễn đạt mới). Trước khi xuất, chạy lại một lần trên kết quả viết lại để xác nhận không dính mục nào.
5. **Không dính mục nào vẫn phải xuất đủ cấu trúc**, bảng ở đoạn 1 điền toàn số 0, đoạn 5 phán định là "✅ Có thể đăng".

---

# SELF-CHECK

- [ ] Đã quét đủ bảy quy tắc, mỗi quy tắc đều có số lần dính (kể cả 0)
- [ ] Mỗi mục dính đều có đoạn trích gốc rõ ràng làm bằng chứng
- [ ] Văn bản sau khi viết lại đã được **quét lần hai** xác nhận không dính mục nào
- [ ] Đã xuất danh sách `forbidden_words`, định dạng là mảng
- [ ] Đã xuất phán định "Có thể đăng hay không" rõ ràng, kèm các mục chặn có lý do
- [ ] Không chỉnh sửa câu chữ vượt quá phạm vi tuân thủ
