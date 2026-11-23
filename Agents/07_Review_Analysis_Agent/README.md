# 07 · Review Analysis Agent

**Agent phân tích đánh giá** · Từ nguyên văn đánh giá, tìm ra **điều người mua thực sự quan tâm**, rồi chỉ ra Listing cần sửa câu nào.

> **v0.4 Skill hóa**: bổ sung [`SKILL.md`](./SKILL.md) (ranh giới phân công: **phân loại giao cho mô hình, đếm số giao cho script**) +
> [`scripts/review_stats.py`](./scripts/review_stats.py) (**tổng hợp xác định**:
> phân bố đánh giá tích cực / trung lập / tiêu cực, số lượng và tỷ trọng theo 8 nhóm nguyên nhân, **tự báo lỗi khi tổng đã quy nguyên nhân ≠ số đánh giá tiêu cực**,
> tỷ lệ khắc phục được, xếp hạng điểm bán hàng theo tần suất × trọng số cảm xúc; tên cột tự nhận diện Việt / Trung / Anh / Bồ Đào Nha, số liệu tương thích định dạng Brazil).
> Kết quả chạy thực tế: 128 đánh giá / 13 tiêu cực / 11 khắc phục được = 84,6%, khớp hoàn toàn với tài liệu case study.

---

## I. Nó giải quyết vấn đề gì

SOP 1.6 có một câu, và đó là toàn bộ nền tảng lập luận của module này:

> **Phân tích đánh giá phải được tách riêng, vì đánh giá là nơi gần nhất với nhu cầu thật của người mua.**

Nhưng cách đội vận hành thường đọc đánh giá rất kém hiệu quả: lướt một lượt, nhớ vài cái, "thấy chất lượng cũng ổn". Vấn đề thật sự là **thông tin trong đánh giá chưa được cấu trúc hóa** — nên không thể quay vòng về Listing.

| Điểm đau | Biểu hiện | Module này giải quyết thế nào |
|---|---|---|
| **Đọc đánh giá nhưng không dùng được** | Biết có đánh giá tiêu cực nhưng không biết nên sửa câu nào trên trang chi tiết | Bắt buộc xuất ánh xạ «đánh giá tiêu cực → hành động trên trang chi tiết» |
| **Không phân biệt được lỗi của ai** | Gộp vận chuyển chậm, người mua hiểu lầm, lỗi sản phẩm vào một nhóm | Quy nguyên nhân theo 8 nhóm của SOP, **tách riêng loại hiểu lầm** |
| **Xếp điểm bán hàng theo cảm tính** | "Tôi thấy sạc nhanh là điểm bán hàng" | Xếp hạng định lượng theo tần suất nhắc đến × mức độ cảm xúc |
| **Không thấy lằn ranh đỏ về thông số** | Liên tục bị phàn nàn thông số không khớp nhưng chưa rút ra thành từ cấm | Xuất danh sách ứng viên `forbidden_words` |

**Sản phẩm đầu ra**: phân loại và quy nguyên nhân đánh giá tích cực / tiêu cực → danh sách đánh giá tiêu cực loại hiểu lầm → xếp hạng tần suất điểm bán hàng → lằn ranh đỏ thông số → đề xuất vá trang chi tiết.

---

## II. Các mục SOP được bao phủ

| SOP | Nội dung | Nằm ở Prompt nào |
|---|---|---|
| **1.6** | Đánh giá tích cực xem gì (5 mục) / Đánh giá tiêu cực xem gì (8 mục) | `01_classify_and_attribute.md` |
| **1.6** | Mục tiêu phân tích (7 câu hỏi) | `01_classify_and_attribute.md` |
| **3.7** | Duy trì đánh giá và hậu mãi / quy nguyên nhân đánh giá tiêu cực / xử lý khách hỏi trước khi mua | `02_misunderstanding_detector.md` |
| **1.5 / 1.7** | Căn cứ chọn cấu hình và điểm bán hàng | `01_classify_and_attribute.md` (xếp hạng điểm bán hàng) |
| Toàn chương | Lằn ranh đỏ tuân thủ | COMPLIANCE GUARD trong `00_system.md` |

---

## III. Quy trình

```text
Đầu vào: lô nguyên văn đánh giá (phía mình + đối thủ)
                         ▼
        ┌──────────────────────────────────┐
        │ 00_system.md                     │  Vai trò + định nghĩa 8 nhóm + chốt chặn tuân thủ
        └──────────────┬───────────────────┘
                       ▼
        ┌──────────────────────────────────┐
        │ 01_classify_and_attribute.md     │  Step 1  Phân loại tích cực/tiêu cực
        │                                  │  Step 2  Quy nguyên nhân 8 nhóm
        │                                  │  Step 3  Xếp hạng tần suất điểm bán hàng
        └──────────────┬───────────────────┘
                       ▼
        ┌──────────────────────────────────┐
        │ 02_misunderstanding_detector.md  │  Step 4  Nhận diện loại hiểu lầm (cốt lõi)
        │                                  │  Step 5  Đề xuất vá trang chi tiết
        │                                  │  Step 6  Rút lằn ranh đỏ thông số
        └──────────────┬───────────────────┘
                       ▼
        Đầu ra: output_review_insights.md
              ├── review_patch_suggestions[]  ──► quay về 03 Listing (bổ sung đoạn Lưu ý)
              ├── forbidden_words_candidates[] ──► 04/05 chặn cứng
              └── selling_points_ranked[]     ──► 03 chọn điểm bán hàng cho tiêu đề/ảnh chính
```

**Đây là module quay vòng (feedback loop)**: đầu ra của nó quay về 03/04, tạo thành vòng khép kín "phân tích lại dữ liệu → tối ưu ngược bốn khâu phía trước" mà SOP nói tới.

---

## IV. 8 nhóm nguyên nhân đánh giá tiêu cực (SOP 1.6)

SOP liệt kê rõ đánh giá tiêu cực cần xem gì. Chuyển nó thành phân loại có thể phán định:

| # | Nhóm nguyên nhân | Dấu hiệu nhận biết | Bên chịu trách nhiệm | Cách khắc phục |
|---|---|---|---|---|
| 1 | **Hiểu lầm** ⭐ | Sản phẩm không có vấn đề, do mô tả chưa rõ | **Phía mình (trang chi tiết)** | **Sửa trang chi tiết / đoạn Lưu ý** |
| 2 | Lỗi chất lượng sản phẩm | Thực sự có khuyết tật, lỗi gia công | Nhà cung cấp / phía mình | Đổi nhà cung cấp / cải tiến sản phẩm |
| 3 | Thông số không như kỳ vọng | Mô tả và hàng thật có chênh lệch | Phía mình | Sửa mô tả thông số / thông số đồng nhất ở 3 nơi |
| 4 | Thiếu phụ kiện | Người mua tưởng có kèm một phụ kiện nào đó | **Phía mình (ảnh danh sách đóng gói)** | Bổ sung ảnh danh sách đóng gói + ghi rõ "không kèm gì" |
| 5 | Giao hàng chậm | Vấn đề thời gian vận chuyển | Đơn vị vận chuyển / phía mình | Sửa cam kết giao hàng / đổi đơn vị vận chuyển |
| 6 | Khó sử dụng | Khó làm quen, sách hướng dẫn không rõ | **Phía mình (sách hướng dẫn / trang chi tiết)** | Bổ sung ảnh hướng dẫn sử dụng |
| 7 | Hậu mãi kém | CSKH phản hồi chậm, phương án xử lý không thỏa đáng | Phía mình | Sửa mẫu câu CSKH / quy trình |
| 8 | Hư hỏng / lỗi / trả hàng | Hư hỏng khi vận chuyển hoặc lỗi chức năng | Đơn vị vận chuyển / nhà cung cấp | Cải tiến đóng gói / đổi nhà cung cấp |

### Vì sao phải tách riêng «loại hiểu lầm»

| | Loại hiểu lầm | Bảy nhóm còn lại |
|---|---|---|
| Sửa được bằng nội dung không | ✅ **Được** | ❌ Không (phải sửa sản phẩm / vận chuyển / quy trình) |
| Chi phí khắc phục | **Gần bằng 0** (sửa một câu trên trang chi tiết) | Cao (đổi nhà cung cấp, đổi vận chuyển, sửa sản phẩm) |
| Thời gian khắc phục | **Sửa xong có hiệu lực ngay** | Vài tuần đến vài tháng |
| ROI | **Cao nhất** | Giảm dần |

> **Đánh giá tiêu cực loại hiểu lầm là nhóm duy nhất "sửa một câu là hết".** Nó không chiếm đa số, nhưng là **hạng mục khắc phục đáng tiền nhất** — nên module này lấy nó làm đầu ra cốt lõi, thay vì trộn lẫn vào tổng số đánh giá tiêu cực.

**Phân biệt then chốt**: một đánh giá tiêu cực rốt cuộc là "lỗi chất lượng sản phẩm" hay "hiểu lầm"?

- `A bateria dura pouco` (pin không bền) → cần hỏi thêm: sản phẩm thật sự không bền, hay người mua tưởng 20000mAh sạc được laptop? **Trường hợp sau là hiểu lầm.**
- `Não veio o cabo` (không có cáp) → nếu sản phẩm vốn không kèm cáp, **đây là hiểu lầm**, không phải thiếu hàng.

> **Tiêu chí phán định**: nếu giao hàng 100% đúng mô tả, sản phẩm không lỗi mà người mua vẫn không hài lòng, thì đó là **vấn đề của mô tả**, xếp vào loại hiểu lầm.

---

## V. Ba loại quay vòng về Listing

Đây là lý do module này tồn tại. **Phân tích không phải để ra báo cáo, mà để sửa Listing.**

| Loại quay vòng | Nội dung | Bên sử dụng | Hành động cụ thể |
|---|---|---|---|
| **A. Đề xuất vá trang chi tiết** | Vấn đề từ đánh giá tiêu cực → các mục đề xuất viết vào đoạn 6 (Lưu ý) của trang chi tiết | **03 Listing** | Viết bổ sung đoạn Lưu ý |
| **B. Lằn ranh đỏ thông số** | Thông số bị phàn nàn "không như kỳ vọng" nhiều lần → ứng viên từ cấm | **03 / 04 / 05** | Thêm vào `forbidden_words`, chặn cứng toàn chuỗi |
| **C. Xếp hạng điểm bán hàng** | Điểm bán hàng xếp theo tần suất nhắc đến × mức độ cảm xúc | **03 / 04** | Quyết định nội dung cốt lõi trên ảnh chính và từ khóa tiêu đề |

### Ví dụ quay vòng

```text
Đầu vào: đánh giá nhắc "esperava que viesse o cabo longo" 7 lần
        ↓
Quy nguyên nhân: loại hiểu lầm (sản phẩm không lỗi, người mua tưởng có kèm cáp dài)
        ↓
Quay vòng A: đoạn Lưu ý trang chi tiết thêm "O cabo incluso (USB-C) tem 30 cm"
Quay vòng B: đưa "cabo longo" vào forbidden_words (tránh tiêu đề/ảnh ngầm ý có kèm cáp dài)
Quay vòng C: ảnh danh sách đóng gói phải ghi rõ chiều dài cáp
```

---

## VI. Các file Prompt

| File | Vai trò |
|---|---|
| [`prompts/00_system.md`](./prompts/00_system.md) | System Prompt: vai trò + định nghĩa 8 nhóm nguyên nhân + chốt chặn tuân thủ |
| [`prompts/01_classify_and_attribute.md`](./prompts/01_classify_and_attribute.md) | Task Prompt: phân loại tích cực/tiêu cực + quy nguyên nhân 8 nhóm + xếp hạng điểm bán hàng |
| [`prompts/02_misunderstanding_detector.md`](./prompts/02_misunderstanding_detector.md) | Task Prompt: nhận diện loại hiểu lầm + đề xuất vá trang chi tiết + lằn ranh đỏ thông số |

## VII. Template và case study

| File | Mô tả |
|---|---|
| [`templates/input_review_batch.md`](./templates/input_review_batch.md) | Đầu vào chuẩn: định dạng nhập lô đánh giá |
| [`templates/output_review_insights.md`](./templates/output_review_insights.md) | Đầu ra chuẩn: báo cáo insight đánh giá |
| [`examples/electric_scooter_reviews.md`](./examples/electric_scooter_reviews.md) | Case study thực tế: xe scooter điện, kiểm chứng ba dự báo đã cài sẵn trong case study flagship |

---

## VIII. Tuân thủ: đâu là ranh giới chính đáng khi "xử lý đánh giá tiêu cực"

Quy trình xử lý đánh giá tiêu cực trong SOP 3.7 có một số hành động mà repo này **không triển khai**. Ranh giới ở đây phải nói rõ:

| Nguyên văn SOP | Tính chất | Module này xử lý |
|---|---|---|
| Báo cáo đánh giá tiêu cực, có cơ hội xóa được | Khiếu nại được sàn cho phép, nhưng **báo cáo có tổ chức** là lạm dụng | ⚠️ Giữ "đánh giá vi phạm rõ ràng thì khiếu nại bình thường từng cái", **bỏ "tổ chức báo cáo"** |
| Liên hệ khách xóa đánh giá tiêu cực, hứa xóa xong sẽ hoàn tiền nhanh và bồi thường | **Dùng lợi ích dụ dỗ xóa đánh giá** | ❌ Loại bỏ |
| Sản phẩm khai khống thông số thì nói là đóng nhầm sách hướng dẫn, sản phẩm có mấy phiên bản | **Dùng lý do sai sự thật để giải thích thông số không khớp** | ❌ Loại bỏ |
| Trả lời đánh giá tiêu cực trước, phủi trách nhiệm và thể hiện thái độ | Tùy trường hợp, trả lời kiểu phủi trách nhiệm làm mất niềm tin | ⚠️ Đổi thành "nói đúng sự thật + đưa ra phương án giải quyết" |
| **Tối ưu ngược trang chi tiết, mẫu câu CSKH hoặc sản phẩm** | ✅ **Hoàn toàn chính đáng** | ✅ **Giữ và nâng lên thành cốt lõi của module** |

> **Mục đích chính đáng của quy nguyên nhân là cải thiện sản phẩm và mô tả của chính mình, không phải xóa bỏ thông tin bất lợi.**
> Đây cũng là lý do module lấy "đánh giá tiêu cực loại hiểu lầm → vá trang chi tiết" làm đầu ra cốt lõi — **nó biến mong muốn "xóa đánh giá tiêu cực" thành một việc thực sự nên làm.**

---

## IX. Ranh giới và giới hạn

| Hạng mục | Mô tả |
|---|---|
| ✅ Chịu trách nhiệm | Phân loại và quy nguyên nhân đánh giá, nhận diện loại hiểu lầm, xếp hạng điểm bán hàng, lằn ranh đỏ thông số, đề xuất vá trang chi tiết, đề xuất mẫu câu CSKH |
| ❌ Không chịu trách nhiệm | Trực tiếp sửa Listing (giao 03/04), thao tác trong Seller Center, liên hệ người mua |
| ⚠️ Cỡ mẫu | Khi < 20 đánh giá, xếp hạng tần suất không có ý nghĩa thống kê — Agent sẽ ghi chú "chỉ để tham khảo" |
| ⚠️ Không xác minh được thật/giả | Không thể phán đoán đánh giá đến từ người mua thật hay buff đánh giá ảo, **quy nguyên nhân dựa trên nội dung văn bản, không dựa trên phán đoán tính xác thực** |
| ⚠️ Vấn đề ngôn ngữ | Đánh giá tiếng Bồ Đào Nha / Tây Ban Nha nhiều văn nói và lỗi chính tả, có thể ảnh hưởng độ chính xác phân loại |
| ⚠️ Rủi ro đánh giá bị xóa | Sàn sẽ xóa một phần đánh giá, khiến mẫu không đầy đủ |

---

**Quay lại**: [Mục lục Agents](../README.md) · **Thượng nguồn**: [06 Advertising](../06_Advertising_Optimization_Agent/) · **Hạ nguồn**: [03 Listing Creative](../03_Listing_Creative_Agent/) · **Tài liệu**: [Lằn ranh đỏ tuân thủ](../../docs/03_Compliance_Guard.md) · [Checklist tự kiểm tra](../../docs/04_Result_Checklist.md)
