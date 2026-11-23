# CONTRIBUTING

Cảm ơn bạn đã tham gia. Mục tiêu của repo này là **biến kinh nghiệm vận hành xuyên biên giới thành thứ có thể tái sử dụng** —— vì vậy người đóng góp chỉ cần đáp ứng ba yêu cầu: **thật, ẩn danh, tái hiện được**.

---

## 1. Có thể đóng góp những gì

| Loại | Ví dụ | Mức ưu tiên |
|---|---|---|
| **Case study mới** | Bản ghi chạy trọn vẹn cho một ngành hàng | 🔴 Cao nhất |
| **Bảng chiều cấu hình theo ngành hàng** | Ngành hàng đó cần tách những thông số cấu hình nào (như 12 chiều của xe scooter trong SOP 1.5) | 🔴 Cao |
| **Quy định sàn cho thị trường mới** | Quy chuẩn trường của site Mexico / Chile / Colombia | 🟡 Trung bình |
| **Cải tiến Prompt** | Prompt hiện có cho output ổn định hơn / khớp quy định sàn hơn | 🟡 Trung bình |
| **Module Agent mới** | Bổ sung đủ bốn module của Phase 2 | 🟡 Trung bình |
| **Chỉnh sửa tài liệu** | Sửa lỗi, bổ sung giải thích | ⚪ Bình thường |
| **Báo lỗi (bug)** | Output Prompt bất thường, định nghĩa trường mâu thuẫn | ⚪ Bình thường |

## Không chấp nhận những gì

| Không chấp nhận | Lý do |
|---|---|
| Hướng dẫn thao tác hoặc công cụ buff đơn ảo / buff review / lách hệ thống kiểm soát rủi ro | Sàn cấm rõ ràng, và sẽ khiến cả repo lẫn người dùng gánh rủi ro |
| Cách report ác ý đối thủ | Cạnh tranh không lành mạnh |
| Case study chứa tên shop thật / tài khoản / thông tin người mua | Quyền riêng tư |
| "Ví dụ" chứa từ khóa thương hiệu chưa được cấp phép | Vi phạm quyền sở hữu |
| Nội dung sáng tạo (creative) bê nguyên của đối thủ (ảnh / video / copy) | Bản quyền |
| Nội dung cam kết lợi nhuận, đảm bảo ra đơn | Không thể chịu trách nhiệm |

> **Nếu bạn không chắc một nội dung có tuân thủ hay không**, hãy đọc [`docs/03_Compliance_Guard.md`](./docs/03_Compliance_Guard.md) trước. Ở đó có bảng đối chiếu viết lại đầy đủ —— **mục tiêu kinh doanh của nhiều thao tác "xám" vốn hợp lý, chỉ là cách làm cần được thay thế**.

---

## 2. Tiêu chuẩn gửi case study

Case study là đóng góp giá trị nhất cho repo này. Yêu cầu:

### Bắt buộc có

1. **Bối cảnh sản phẩm** — sản phẩm gì, thị trường nào, định vị ra sao
2. **Đầu vào** — toàn bộ đầu vào (`spec_table` / `forbidden_words` / `usage_scope`, v.v.)
3. **Quy trình xử lý của AI** — đã chạy những Prompt nào, theo thứ tự nào
4. **Kết quả tạo ra** — output thực tế (có thể trích một phần, nhưng phải thấy được chất lượng)
5. **Các trường bàn giao cho module hạ nguồn** — theo định nghĩa trong [`Templates/product_brief_template.md`](./Templates/product_brief_template.md)
6. **Đề xuất tối ưu** — bước tiếp theo nên làm gì
7. **Case study này chứng minh được điều gì** — nêu rõ kết luận

### Bắt buộc đạt

- [ ] **Ẩn danh**: không có tên shop thật, tài khoản, thông tin người mua, từ khóa thương hiệu chưa được cấp phép
- [ ] **Thông số thật**: thông số trong ví dụ phải có bằng chứng, không bịa
- [ ] **Đếm ký tự thực tế**: độ dài tiêu đề, phụ đề, v.v. phải đếm thực tế (có thể dùng script), không ước lượng
- [ ] **Con số tái hiện được**: quá trình tính thời lượng, số từ, giá, v.v. người đọc phải kiểm tra lại được
- [ ] **Đã qua checklist tự kiểm tra**: [`docs/04_Result_Checklist.md`](./docs/04_Result_Checklist.md)
- [ ] **Case study ảnh / video không chứa** logo chứng nhận giả, ảnh chụp đánh giá, badge số lượng đã bán

### Điểm cộng

- Tự chỉ ra lỗi của mình và giải thích cách sửa (**điều này giá trị hơn một case study hoàn hảo**)
- Ghi chú các điểm yếu đã biết của phương pháp
- Đưa ra phản ví dụ (cách làm nào là sai)

---

## 3. Tiêu chuẩn gửi cải tiến Prompt

- [ ] Tuân theo cấu trúc 5 thành phần trong [`docs/01_Prompt_Design_Guide.md`](./docs/01_Prompt_Design_Guide.md)
- [ ] **Giữ nguyên đoạn COMPLIANCE GUARD** (không được xóa, không được làm yếu đi)
- [ ] Khai báo hợp đồng đầu vào đầy đủ (thiếu trường phải báo lỗi, không được đoán)
- [ ] Hợp đồng đầu ra dùng cấu trúc heading Markdown cố định
- [ ] Checklist tự kiểm tra là **phán đoán nhị phân** tick được, không phải kiểu "cố gắng", "chú ý"
- [ ] Giải thích đã sửa gì, vì sao sửa, so sánh trước và sau khi sửa

---

## 4. Quy ước thư mục

```text
Agents/<NN>_<Name>_Agent/
├── README.md          Bắt buộc: trách nhiệm / đầu vào đầu ra / cách dùng / giới hạn đã biết
├── prompts/           Bắt buộc: 00_system.md + các Task Prompt
├── templates/         Bắt buộc: input_* + output_*
└── examples/          Bắt buộc: ít nhất 1 case study thật
```

- **Template chỉ một Agent dùng** → đặt trong `templates/` của Agent đó
- **Từ hai Agent trở lên dùng** → đưa lên [`Templates/`](./Templates/) ở cấp trên cùng
- **Case study một module** → đặt trong `examples/` của Agent đó
- **Case study end-to-end liên module** → đặt trong [`Examples/`](./Examples/) ở cấp trên cùng

---

## 5. Quy chuẩn commit message

```
<type>: <mô tả ngắn>

type:
  feat     Thêm Agent / module / case study mới
  fix      Sửa lỗi
  docs     Chỉnh sửa tài liệu
  prompt   Cải tiến Prompt
  chore    Việc lặt vặt (thư mục, cấu hình)
```

Ví dụ:
```
feat: thêm bảng chiều cấu hình cho ngành hàng Drill / máy khoan điện
fix: sửa mô tả giới hạn số ký tự tiêu đề Shopee
prompt: Prompt tạo tiêu đề của 03 thêm bước "kiểm tra vị trí từ khóa chính"
```

---

## 6. Kiểm tra lần cuối trước khi gửi

- [ ] Thay đổi của tôi **không có** nội dung buff đơn ảo / buff review / report ác ý / lách hệ thống kiểm soát rủi ro
- [ ] Case study của tôi **đã ẩn danh** (tên shop, tài khoản, thông tin người mua, thương hiệu chưa được cấp phép)
- [ ] Prompt của tôi **giữ nguyên COMPLIANCE GUARD**
- [ ] Thông số trong ví dụ của tôi **có bằng chứng**
- [ ] Các con số của tôi **tái hiện được** (đặc biệt là số ký tự, thời lượng, giá)
- [ ] Case study ảnh / video tôi gửi **không có chứng nhận, đánh giá, số lượng đã bán giả mạo**
- [ ] Tôi đã đọc [`docs/03_Compliance_Guard.md`](./docs/03_Compliance_Guard.md)

---

**Tài liệu liên quan**: [Tách kiến trúc](./docs/00_Architecture_SOP_to_Agent.md) · [Chuẩn Prompt](./docs/01_Prompt_Design_Guide.md) · [Lằn ranh đỏ tuân thủ](./docs/03_Compliance_Guard.md) · [Lộ trình](./ROADMAP.md)
