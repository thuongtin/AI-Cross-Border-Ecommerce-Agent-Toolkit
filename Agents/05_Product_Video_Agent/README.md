# 05 · Product Video Agent

**Agent tạo video ngắn cho sản phẩm** · Từ một câu điểm bán hàng đến một kịch bản storyboard quay được ngay.

> **v0.4 chuyển thành Skill**: bổ sung [`SKILL.md`](./SKILL.md) (điểm vào của Agent) +
> [`references/video-specs.md`](./references/video-specs.md) (thẻ quy chuẩn video của sàn) +
> [`scripts/video_timing.py`](./scripts/video_timing.py) (**kiểm tra tất định thời lượng và phụ đề**:
> quy đổi số từ → thời lượng, timeline từng câu, độ dài dòng phụ đề, kiểm tra hook, tổng thời lượng so với mục tiêu 15s/30s dung sai ±15%).
> Kiểm tra thời lượng thực tế: 65 từ ÷ 2,5 từ/giây = 26,0s, khớp hoàn toàn với số liệu ghi trong case study.

---

## I. Nó giải quyết vấn đề gì

Video là khâu **có rào cản cao nhất, dễ bỏ dở giữa chừng nhất** trong ba module sáng tạo.

| Nỗi đau | Biểu hiện | Module này giải quyết thế nào |
|---|---|---|
| **Không biết 3 giây đầu đặt gì** | Mở đầu bằng "Xin chào mọi người, hôm nay mình giới thiệu…", người xem đã lướt qua | Quy tắc hook bắt buộc: 3 giây đầu phải là sản phẩm/kết quả/nỗi đau, không phải tự giới thiệu |
| **Không viết được storyboard** | Chỉ có một đoạn mô tả, đến lúc quay/dựng không biết bắt đầu từ đâu | Xuất bảng storyboard có cấu trúc: số cảnh / thời lượng / hình ảnh / chuyển động máy / lời thoại / hiệu ứng âm thanh |
| **Prompt video AI không hiệu quả** | Ném một câu cho mô hình video, hình ra không dùng được | Xuất Prompt có cấu trúc theo từng cảnh: chủ thể + hành động + chuyển động máy + ánh sáng + phong cách |
| **Lời lồng tiếng như văn viết** | Đọc lên rất cứng, TTS ra kém | Bắt buộc viết lại theo văn nói + ước tính thời lượng đọc |

**Đầu ra**: kịch bản hai bản 15s / 30s + bảng storyboard + Prompt video AI từng cảnh + kịch bản lồng tiếng + phụ đề.

---

## II. Các chương SOP được bao phủ

SOP không có chương "video" riêng——**đây là module mở rộng của repo này**, SOP chỉ cung cấp nền tảng về mặt nội dung sáng tạo:

| Nguồn SOP | Nội dung trích xuất | Cách dùng |
|---|---|---|
| **3.3 Khung nội dung trang chi tiết** | Cấu trúc 7 phần (lời chào / điểm bán hàng / bối cảnh / thông số / hậu mãi / lưu ý / từ khóa) | Chuyển thành khung tự sự video: hook → điểm bán hàng → bối cảnh → thông số → niềm tin → CTA |
| **3.3 Cách viết tiêu đề** | Từ khóa chính + đối tượng + thông số + công năng + bối cảnh | CTA cuối video nhất quán với tiêu đề |
| **1.6 Phân tích review** | Người mua thực sự quan tâm điều gì | Quyết định ưu tiên nói điểm bán hàng nào trong video |
| **2.3 Tạo khác biệt** | Nhiều shop bán cùng mẫu cần tạo khác biệt | Chế độ `variant` xuất nhiều bộ kịch bản với góc tiếp cận khác nhau |

> **Nói thẳng**: phương pháp luận của module video phần lớn đến từ thực tiễn video ngắn nói chung, không phải từ bộ SOP này. SOP cung cấp **chất liệu và ràng buộc** (điểm bán hàng, thông số, phạm vi bối cảnh, từ cấm), module này lo việc tổ chức chúng thành ngôn ngữ video.

---

## III. Quy trình

```text
Đầu vào: đầu ra của 03 Listing Creative + (tùy chọn) hero_visual của 04 Product Image
        ▲
        └── 【Quy tắc chặn】core_selling_point hoặc forbidden_words rỗng → từ chối thực thi
                         ▼
        ┌────────────────────────────────┐
        │ 00_system.md                   │  Vai trò + quy chuẩn video sàn + kiểm soát tuân thủ phụ đề
        └──────────────┬─────────────────┘
                       ▼
        ┌────────────────────────────────┐
        │ 01_script_and_storyboard.md    │  Step 1  Kịch bản 15s / 30s
        │                                │  Step 2  Bảng storyboard
        └──────────────┬─────────────────┘
                       ▼
        ┌────────────────────────────────┐
        │ 02_ai_video_and_voice.md       │  Step 3  Prompt video AI từng cảnh
        │                                │  Step 4  Lồng tiếng + phụ đề + đối chiếu thời lượng
        └──────────────┬─────────────────┘
                       ▼
        Đầu ra: output_video_pack.yaml  →  giao cho VideoGen / Jimeng / Runway / Kling / CapCut
```

---

## IV. Chiến lược hai phiên bản

| Phiên bản | Mục đích | Cấu trúc |
|---|---|---|
| **15s** | Video vị trí ảnh chính, quảng cáo trong Feed, màn hình đầu TikTok | Hook(0–3s) → Điểm bán hàng cốt lõi(3–9s) → Bối cảnh(9–13s) → CTA(13–15s) |
| **30s** | Video trang chi tiết, nhúng trong trang sản phẩm | Hook(0–3s) → Điểm bán hàng 1(3–9s) → Điểm bán hàng 2(9–16s) → Bối cảnh(16–23s) → Thông số/Niềm tin(23–28s) → CTA(28–30s) |

**Vì sao bắt buộc làm bản 15s**: video ở vị trí ảnh chính và màn hình đầu TikTok giữ chân traffic đều trong khoảng **3 giây đầu đến 15 giây đầu**. Bản 30s làm hay đến mấy mà 15s đầu không ổn thì vẫn là video bỏ đi——bản 15s về bản chất là ép bạn nén thông tin hiệu quả nhất lên trước.

---

## V. Thiết kế hook (3 giây đầu)

SOP không nói trực tiếp về hook video, nhưng SOP 1.6 có nói một điều: **review là nơi gần nhất với nhu cầu thật của người mua**. Nguồn hook tốt nhất chính là đây:

| Loại hook | Nguồn | Ví dụ (Brazil / sạc dự phòng) |
|---|---|---|
| **Đánh thẳng nỗi đau** | Lời phàn nàn hay gặp trong đánh giá tiêu cực | `Seu celular acaba antes do fim do dia?` |
| **Đưa kết quả lên trước** | Điểm hài lòng hay gặp trong đánh giá tích cực | `Carrega o celular 4 vezes sem tomada.` |
| **Phản trực giác** | Điểm bất ngờ trong thông số | `20.000 mAh e ainda cabe no bolso.` |
| **Đối chiếu gây sốc** | Điểm yếu của đối thủ | `45W. Não 18W.` |
| **Nhập vai bối cảnh** | Bối cảnh chính trong `usage_scope` | `Domingo inteiro fora de casa. Sem tomada.` |

❌ **Cấm**: `Olá pessoal, bem-vindos ao meu canal`, `Hoje vou apresentar para vocês`, mọi kiểu tự giới thiệu.

---

## VI. Các file Prompt

| File | Vai trò |
|---|---|
| [`prompts/00_system.md`](./prompts/00_system.md) | System Prompt: vai trò + quy chuẩn video sàn + kiểm soát tuân thủ phụ đề/hình ảnh |
| [`prompts/01_script_and_storyboard.md`](./prompts/01_script_and_storyboard.md) | Task Prompt: kịch bản + bảng storyboard |
| [`prompts/02_ai_video_and_voice.md`](./prompts/02_ai_video_and_voice.md) | Task Prompt: Prompt video AI từng cảnh + kịch bản lồng tiếng + phụ đề |

## VII. Template và case study

| File | Mô tả |
|---|---|
| [`templates/input_video_brief.md`](./templates/input_video_brief.md) | Đầu vào chuẩn |
| [`templates/output_video_pack.yaml`](./templates/output_video_pack.yaml) | Đầu ra chuẩn |
| [`examples/air_fryer.md`](./examples/air_fryer.md) | Case study thực tế: nồi chiên không dầu, hai bản 15s + 30s |

---

## VIII. Hạn chế đã biết

| Hạn chế | Mô tả |
|---|---|
| **Không render video** | Chỉ xuất kịch bản, storyboard và Prompt, việc tạo video thực tế dùng công cụ video |
| **Không có căn cứ trực tiếp từ SOP** | Một phần phương pháp luận của module này đến từ thực tiễn video ngắn nói chung, đã ghi chú ở trên |
| **Đồng bộ hình và tiếng cần làm thủ công** | Thời lượng storyboard là giá trị đề xuất, thực tế cần căn theo audio lồng tiếng |
| **Tự lo bản quyền BGM** | Module chỉ đưa ra "cần nhạc mang cảm xúc gì", không cung cấp nhạc |
| **Không hỗ trợ phương án người thật xuất hiện** | Cảnh quay người thật chỉ có chỉ dẫn quay, không tạo Prompt video người thật (rủi ro tuân thủ về chân dung) |
| **Không đánh giá được chất lượng thành phẩm** | Kiểm soát chất lượng sau khi render cần người thực hiện theo checklist mục D |

---

**Quay lại**: [Mục lục Agents](../README.md) · **Thượng nguồn**: [03 Listing Creative](../03_Listing_Creative_Agent/) · [04 Product Image](../04_Product_Image_Agent/) · **Tài liệu**: [Quy chuẩn trường dữ liệu theo sàn](../../docs/02_Platform_Output_Spec.md) · [Lằn ranh đỏ tuân thủ](../../docs/03_Compliance_Guard.md)
