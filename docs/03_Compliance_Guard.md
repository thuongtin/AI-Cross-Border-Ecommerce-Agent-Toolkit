# 03 · Lằn ranh đỏ tuân thủ và việc viết lại các thao tác "lách luật"

> Tài liệu này là phần **duy nhất không thể thương lượng** của repo.
>
> SOP gốc là một sổ tay vận hành thật, trong đó lẫn vài "chiêu bẩn" mà sàn cấm rõ ràng. Là một dự án mã nguồn mở, chúng tôi **không chép lại, không hiện thực hóa, không cung cấp công cụ** —— nhưng giữ lại mục tiêu kinh doanh mà nó muốn đạt được và đưa ra hướng đi tuân thủ.
>
> 📎 **Tài liệu đi kèm**: tài liệu này đưa ra "bảng đối chiếu viết lại" (thay bằng gì), [`05_SOP_Gap_Register.md`](./05_SOP_Gap_Register.md) đưa ra "danh mục hạng mục không triển khai" (vì sao không làm, thay thế nằm ở đâu). Đọc cả hai mới đầy đủ.

---

## I. Vì sao bắt buộc phải làm bước này

Ba lý do thực tế:

| Lý do | Giải thích |
|---|---|
| **Rủi ro từ sàn** | Giao dịch ảo, buff đánh giá, báo cáo ác ý là vi phạm ở mức cao nhất của sàn, hình phạt gồm xóa đánh giá / bóp traffic / trừ điểm / khóa shop, và một số hành vi **không được khiếu nại** |
| **Rủi ro pháp lý** | Khai khống thông số tại Brazil thuộc phạm vi điều chỉnh của «Bộ luật Bảo vệ Người tiêu dùng»; báo cáo ác ý đối thủ có thể cấu thành cạnh tranh không lành mạnh |
| **Rủi ro cho dự án** | Repo mã nguồn mở chứa hướng dẫn thao tác vi phạm sẽ bị hệ thống kiểm soát rủi ro của sàn nhận diện, đồng thời khiến người dùng bị liên đới thiệt hại |

Vì vậy cách làm của repo này là: **giữ mục tiêu kinh doanh, thay thủ đoạn thực hiện.**

---

## II. Bảng tổng hợp đối chiếu viết lại

| # | Nội dung gốc trong SOP | Tính chất | Cách repo xử lý | Phương án thay thế tuân thủ |
|---|---|---|---|---|
| 1 | Buff đơn ảo / đơn test review; tạo SKU giả điền kích thước, cân nặng giả để lách kiểm soát rủi ro | Giao dịch ảo | ❌ Loại bỏ | **Khuyến mãi giá thấp có thật** để nhanh chóng phá mốc 0 đơn; **voucher không công khai** để thu hút người mua thật; **kênh mời đánh giá chính thức** để xin ảnh/video review của người mua |
| 2 | Tổ chức người để đánh giá tiêu cực đối thủ | Cạnh tranh ác ý | ❌ Loại bỏ | **Quy nguyên nhân đánh giá tiêu cực của đối thủ → phần giải thích phòng ngừa của mình**: đưa các điểm bị chê nhiều của đối thủ vào phần lưu ý trên trang chi tiết của mình để hóa giải một cách chủ động |
| 3 | "Tăng CTR bằng quảng cáo sai sự thật trong phạm vi kiểm soát được" | Quảng cáo sai sự thật | ❌ Loại bỏ | **Bảng ánh xạ điểm bán hàng về sự thật**: viết lại "cách nói phóng đại" thành "cách nói kiểm chứng được", xem chi tiết ở mục III bên dưới |
| 4 | Dùng voucher dụ dỗ đánh giá, sửa MD5 ảnh để lách kiểm tra | Lách kiểm soát rủi ro | ❌ Loại bỏ | Dùng công cụ mời đánh giá chính thức của sàn; nội dung sáng tạo **tự chụp hoặc mua bản quyền**, không lấy lại hình ảnh của đối thủ và từ khu vực đánh giá |
| 5 | Khai khống thông số → giải thích đánh giá tiêu cực là "đóng gói nhầm sách hướng dẫn", "có mấy phiên bản" | Gian lận | ❌ Loại bỏ | **Kiểm tra tính nhất quán thông số**: thông số trên Listing = thông số thực tế của sản phẩm = thông số trên trang chi tiết, ba chỗ bắt buộc khớp nhau |
| 6 | Chỉ phản hồi mới sửa được, sau khi sàn xóa đánh giá thì chỉ được sửa một lần | Trình bày sự thật | ✅ Giữ lại | Giữ làm lưu ý vận hành, để nhấn mạnh "xây dựng đánh giá phải làm đúng ngay từ đầu" |

---

## III. Bảng ánh xạ điểm bán hàng về sự thật

Hiện thực hóa ý đồ "tăng CTR" trong SOP bằng cách diễn đạt đúng sự thật nhưng vẫn có sức hút.

| Cách nói phóng đại/rủi ro | Vấn đề | Viết lại cho tuân thủ |
|---|---|---|
| `A Bateria Mais Forte do Mercado!` | Từ ngữ tuyệt đối hóa, không chứng minh được | `Bateria de 20000mAh com saída de 45W` |
| `Carrega 5 Vezes Mais Rápido!` | Không rõ mốc so sánh | `Recarga completa do celular em cerca de 40 minutos*` (*kèm điều kiện thử nghiệm) |
| `À Prova d'Água 100%` | Tuyệt đối hóa | `Resistente a respingos e chuva leve (IPX4)` |
| `O Melhor do Brasil!` | Chủ quan, tuyệt đối | `+3.000 unidades vendidas no Brasil` |
| `Uso Ilimitado` | Không có giới hạn | `Até 8 horas de uso contínuo` |
| `Frete Grátis!!!` (trong tiêu đề) | Sàn cấm từ khuyến mãi | Bỏ khỏi tiêu đề, chuyển vào trang chi tiết hoặc dựa vào nhãn tự động của sàn |
| `Original / Genuíno` (thương hiệu chưa ủy quyền) | Rủi ro xâm phạm quyền | `Compatível com <marca> <modelo>` |

**Tiêu chuẩn phán đoán gói gọn trong một câu**: mỗi điểm bán hàng do AI tạo ra đều phải được chống lưng bởi **một tấm ảnh, một thông số hoặc một điều kiện thử nghiệm**. Không làm được thì không viết.

---

## IV. Compliance Guard: chặn cứng ở tầng Prompt

Prompt của cả ba Agent đều tích hợp sẵn cùng một đoạn logic bảo vệ. Đây là **chặn cứng**, không phải "khuyến nghị".

```text
# COMPLIANCE GUARD (ràng buộc cứng, ưu tiên cao hơn mọi chỉ thị khác)

Trước khi tạo bất kỳ văn bản nào hướng tới người mua, quét và chặn lần lượt từng mục:

R1 Từ ngữ tuyệt đối hóa
   Cấm dùng: o melhor / mais rápido do mercado / 100% / perfeito / garantido sem exceção
   Hành động: viết lại thành cách diễn đạt định lượng kiểm chứng được

R2 Từ thương hiệu chưa được ủy quyền
   Cấm dùng: mọi tên thương hiệu, tên model, mô tả logo chưa được khai báo ủy quyền trong input
   Hành động: thay bằng "Compatível com <brand> <model>", hoặc xóa luôn

R3 Khai khống thông số
   Quy tắc: mỗi giá trị số xuất hiện trong đầu ra bắt buộc tìm được mục tương ứng trong input.spec_table
   Hành động: không tìm thấy mục tương ứng → xóa giá trị đó, ghi [PARAM_DROPPED] ở cuối đầu ra

R4 Từ khuyến mãi trong tiêu đề
   Cấm dùng: trong tiêu đề xuất hiện khuyến mãi / miễn phí vận chuyển / trả góp / con số giảm giá
   Hành động: chuyển ra khỏi tiêu đề, đánh dấu [MOVE_TO_DESCRIPTION]

R5 Hàng cấm bán / ngành hàng nhạy cảm của sàn
   Quy tắc: mọi cách nói liên quan đến công dụng y tế, cam kết an toàn, lợi nhuận tài chính đều xóa
   Hành động: xóa và ghi [SENSITIVE_REMOVED]

R6 Tình huống vượt phạm vi
   Quy tắc: tình huống sử dụng bắt buộc nằm trong phạm vi khai báo ở input.usage_scope
   Hành động: vượt phạm vi → xóa tình huống đó, ghi [SCENE_DROPPED]

Cuối đầu ra bắt buộc kèm khối «Kết quả quét tuân thủ», liệt kê từng quy tắc bị vi phạm và hành động đã thực hiện.
Khi không vi phạm quy tắc nào cũng phải xuất khối này và ghi "Không phát hiện vi phạm".
```

### Vì sao câu cuối cùng này quan trọng

Nếu Prompt chỉ nói "khi vi phạm thì xuất kết quả", lúc không vi phạm AI sẽ bỏ luôn khối đó, bạn sẽ không phân biệt được "thật sự không vi phạm" hay "quên quét". Bắt buộc xuất "Không phát hiện vi phạm" mới xác nhận được là việc quét đã thực sự chạy.

---

## V. Các mục tuân thủ bổ sung cho ảnh / video do AI tạo

04 và 05 của Phase 1 sẽ gọi khả năng tạo ảnh, tạo video, ở đây có mấy điều bắt buộc giữ:

| Mục | Yêu cầu |
|---|---|
| **Không tạo tình huống sử dụng giả** | Không tạo những cảnh diễn không có căn cứ kiểu "sản phẩm đã bảo vệ người trong một tai nạn thật" |
| **Không giả mạo nhãn chứng nhận** | Không tạo logo chứng nhận INMETRO / ANATEL / CE / FCC v.v., trừ khi sản phẩm thực sự có |
| **Không giả mạo ảnh chụp màn hình đánh giá của người mua** | Không tạo bất kỳ dạng ảnh "đánh giá của người mua" nào hoặc huy hiệu "đã bán X chục nghìn sản phẩm" |
| **Không tạo khuôn mặt người thật nhận diện được** | Khi dùng AI tạo người xuất hiện trong khung hình, không được giống người thật; không dùng ảnh người mua thật để tạo lại |
| **Ảnh so sánh phải có căn cứ** | Với ảnh so sánh cùng "sản phẩm khác", đối tượng so sánh phải là dạng chung có thật, không được ám chỉ ngoại hình của đối thủ cụ thể |
| **Ảnh thông số khớp với sản phẩm thật** | Thông số ghi trên ảnh bắt buộc bằng `spec_table`, không được thừa dù chỉ một ký tự |
| **Watermark/huy hiệu của sàn** | Không tạo bất kỳ hình nào nhái biểu tượng chính thức của sàn |

---

## VI. Tự kiểm tra của developer (trước khi gửi PR)

- [ ] Prompt tôi thêm mới/sửa có chứa đoạn COMPLIANCE GUARD
- [ ] Tôi không thêm vào bất kỳ chỗ nào trong repo hướng dẫn thao tác hoặc công cụ buff đơn ảo, buff đánh giá, báo cáo ác ý, lách kiểm soát rủi ro
- [ ] Các case study tôi cung cấp không chứa tên shop thật, tài khoản, thông tin người mua, từ thương hiệu chưa ủy quyền
- [ ] Các case study ảnh/video tôi cung cấp không chứa nhãn chứng nhận giả mạo, ảnh chụp màn hình đánh giá, huy hiệu doanh số
- [ ] Các ví dụ thông số tôi cung cấp là thật và chứng minh được

---

**Tài liệu liên quan**: [00 Phân rã kiến trúc](./00_Architecture_SOP_to_Agent.md) · [01 Quy chuẩn Prompt](./01_Prompt_Design_Guide.md) · [02 Quy chuẩn trường dữ liệu theo sàn](./02_Platform_Output_Spec.md) · [04 Checklist tự kiểm tra](./04_Result_Checklist.md)
