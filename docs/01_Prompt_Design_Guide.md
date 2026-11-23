# 01 · Quy chuẩn thiết kế Prompt

> Mọi Prompt trong repo này bắt buộc tuân theo cấu trúc ở phần này. PR không đạt sẽ không được merge.

---

## I. Cấu trúc năm thành phần

Mỗi Prompt tác vụ gồm năm phần, thiếu một phần là Prompt không đạt.

| # | Thành phần | Tác dụng | Ví dụ sai |
|---|---|---|---|
| 1 | **Vai trò ROLE** | Giới hạn góc nhìn chuyên môn và tiêu chuẩn phán đoán | "Bạn là một trợ lý AI" ← quá chung chung |
| 2 | **Ngữ cảnh CONTEXT** | Cung cấp quy định sàn, đặc thù ngành hàng, ràng buộc kinh doanh | Thiếu phần này thì AI sẽ lấy kiến thức thương mại điện tử chung chung đè lên quy định của sàn |
| 3 | **Hợp đồng đầu vào INPUT** | Khai báo các trường bắt buộc, thiếu trường thì từ chối trả lời | Thiếu phần này thì AI sẽ tự bịa thông số |
| 4 | **Hợp đồng đầu ra OUTPUT** | Cố định cấu trúc để module phía sau dễ phân tích | Thiếu phần này thì phía sau không nối tự động được |
| 5 | **Tự kiểm tra SELF-CHECK** | Kiểm tra từng mục trước khi xuất, không đạt thì viết lại | Thiếu phần này thì độ ổn định của đầu ra giảm một nửa |

---

## II. Khung chuẩn

```text
# ROLE
Bạn là <vai trò cụ thể>, phục vụ cho <sàn/thị trường cụ thể>. Tiêu chuẩn phán đoán của bạn là <tiêu chuẩn 1, tiêu chuẩn 2, tiêu chuẩn 3>.

# CONTEXT
<Quy định cứng của sàn: số ký tự/trường dữ liệu/mục bị cấm>
<Đặc thù ngành hàng: người mua hay hỏi gì, hay hoàn hàng vì gì>
<Ràng buộc kinh doanh: biên lợi nhuận, tồn kho, năng lực hậu mãi>

# INPUT
Bắt buộc có các trường sau, thiếu bất kỳ trường nào thì dừng lại và liệt kê các mục còn thiếu, không được đoán:
- field_a: <mô tả>
- field_b: <mô tả>

# OUTPUT
Xuất đúng theo cấu trúc sau, không thêm bớt mục:
## 1. <tên mục>
...

# SELF-CHECK (kiểm tra từng mục trước khi xuất, bất kỳ mục nào không đạt thì viết lại)
- [ ] Mục kiểm tra 1
- [ ] Mục kiểm tra 2
```

---

## III. Bốn quy tắc cứng

### Quy tắc 1: Thiếu trường thì phải báo lỗi, không được đoán

**Đây là quy tắc quan trọng nhất.** Trong vận hành xuyên biên giới, thiệt hại do "AI bịa một thông số" lớn hơn nhiều so với "AI từ chối trả lời".

```text
❌ Ví dụ sai
Đầu vào không có dung lượng pin → AI tự viết "20000mAh" → sau khi đăng bán bị khiếu nại sai thông số

✅ Ví dụ đúng
Đầu vào không có dung lượng pin → AI xuất:
   [INPUT_MISSING] Thiếu trường: battery_capacity
   Ảnh hưởng: không thể tạo bảng thông số và từ khóa thông số trong tiêu đề
   Vui lòng bổ sung rồi gửi lại
```

### Quy tắc 2: Quy định sàn viết ở CONTEXT, không viết ở OUTPUT

Đặt quy định trong phần OUTPUT thì AI dễ "quên" lúc sinh nội dung. Đặt trong CONTEXT thì mô hình sẽ coi đó là ràng buộc tiền đề.

### Quy tắc 3: Cấu trúc đầu ra dùng tiêu đề Markdown cố định

Chúng tôi dùng tiêu đề đánh số kiểu `## 1. xxx` thay vì văn xuôi tự do. Lý do: module 04/05 phía sau phải dựa vào tiêu đề để lấy trường dữ liệu, văn xuôi thì không lấy được.

### Quy tắc 4: Checklist tự kiểm tra viết thành các mục đánh dấu được

Mỗi mục tự kiểm tra bắt buộc là **phán đoán nhị phân** (đạt/không đạt), không được là yêu cầu mơ hồ kiểu "cố gắng", "chú ý".

```text
❌ - [ ] Tiêu đề cố gắng thu hút
✅ - [ ] Tiêu đề ≤ 120 ký tự, không chứa từ khuyến mãi, emoji, từ viết hoa toàn bộ
```

---

## IV. Chiến lược ngôn ngữ đầu ra

Đây là cái bẫy đặc thù của bán hàng xuyên biên giới.

| Tình huống | Ngôn ngữ đầu ra | Lý do |
|---|---|---|
| Tiêu đề / trang chi tiết / chữ trên ảnh / phụ đề | **Tiếng bản địa của thị trường mục tiêu** (Shopee Brazil = PT-BR) | Listing dịch thẳng từ tiếng Anh có CTR thấp về mặt cấu trúc |
| Trường giải thích, ghi chú nội bộ, ý nghĩa thông số | Tiếng Việt | Để đội vận hành dễ đối chiếu |
| Chữ trên ảnh | Tiếng bản địa + ghi rõ giới hạn số ký tự | Chữ trên ảnh quá dài sẽ chèn ép hình ảnh |

**Trong Prompt bắt buộc ghi rõ**:

```text
# LANGUAGE RULE
- Mọi văn bản hướng tới người mua (tiêu đề, mô tả, chữ trên ảnh, phụ đề) bắt buộc dùng <PT-BR tiếng Bồ Đào Nha Brazil>.
- Cấm viết tiếng Anh trước rồi dịch, phải trực tiếp nghĩ và diễn đạt bằng <ngôn ngữ mục tiêu>.
- Đơn vị thông số dùng hệ mét (kg / cm / W / V / mAh), cấm dùng hệ Anh (lb / inch).
- Các trường ghi chú nội bộ dùng tiếng Việt.
```

> Vì sao nhấn mạnh "không viết tiếng Anh trước rồi dịch": mô hình kích hoạt theo cách khác nhau với "tác vụ dịch" và "tác vụ sáng tạo". Viết thành tác vụ dịch sẽ cho ra nội dung đúng ngữ pháp nhưng đọc lên như người nước ngoài viết (người mua Brazil cảm nhận rất rõ). Viết thành tác vụ sáng tạo thì mô hình mới dùng đến thói quen diễn đạt của người bản xứ.

---

## V. Cách viết tham số hóa

Những chỗ trong Prompt cần thay biến thì đánh dấu bằng `<ngoặc nhọn>`, và đưa giá trị ví dụ trong file mẫu:

```text
# CONTEXT
Sàn: <Shopee / Mercado Livre>
Thị trường mục tiêu: <Brazil / Mexico / Philippines>
Ngành hàng: <Patinete Elétrico / Carregador Portátil>
```

Đừng dùng `{var}` hay `$VAR` —— dễ xung đột với template code, và dễ bị mô hình hiểu nhầm là chuỗi literal cần giữ nguyên.

---

## VI. Tái sử dụng và lắp ghép

Một lần gọi hoàn chỉnh = **Prompt hệ thống + Prompt tác vụ + mẫu đầu vào đã điền**.

```text
┌─────────────────────────────┐
│ 00_system.md                │  ← vai trò + ràng buộc chung, mọi tác vụ dùng chung
├─────────────────────────────┤
│ 0X_<task>.md                │  ← tác vụ cụ thể: hợp đồng đầu vào + hợp đồng đầu ra + tự kiểm tra
├─────────────────────────────┤
│ templates/input_*.md (đã điền)│  ← dữ liệu thật
└─────────────────────────────┘
```

Lợi ích của thiết kế này: sửa quy định sàn chỉ cần sửa một chỗ là `00_system.md`; thêm tác vụ mới chỉ cần thêm một Prompt tác vụ.

---

## VII. Cách debug

Khi chất lượng đầu ra không ổn định, rà soát theo thứ tự này (từ dưới lên):

| # | Hạng mục rà soát | Triệu chứng điển hình |
|---|---|---|
| 1 | Cấu trúc đầu ra đã cố định chưa | Mỗi lần xuất số lượng mục lại khác nhau |
| 2 | Checklist tự kiểm tra có thực thi được không | Tự kiểm tra đã tick nhưng nội dung vẫn không đạt |
| 3 | Hợp đồng đầu vào có được tuân thủ không | AI bắt đầu bịa thông số không được cung cấp |
| 4 | CONTEXT có bị ghi đè không | AI dùng kiến thức thương mại điện tử chung chung thay cho quy định sàn |
| 5 | Thiết lập vai trò có quá chung chung không | Đầu ra giống bách khoa toàn thư, không giống phán đoán của người vận hành lâu năm |

**Kinh nghiệm thực tế**: 90% vấn đề đầu ra không ổn định nằm ở mục 3 và mục 4.

---

**Tài liệu liên quan**: [00 Phân rã kiến trúc](./00_Architecture_SOP_to_Agent.md) · [02 Quy chuẩn trường dữ liệu theo sàn](./02_Platform_Output_Spec.md) · [03 Lằn ranh đỏ tuân thủ](./03_Compliance_Guard.md)
