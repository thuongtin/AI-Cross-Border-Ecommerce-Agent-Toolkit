# Template đầu vào · Brief tạo video

> **Điều kiện tiên quyết**: module này **phụ thuộc vào đầu ra của 03 Listing Creative Agent**; có thêm đầu ra của 04 thì hiệu quả tốt hơn (thống nhất phong cách).

---

## 0. Cấu hình nhiệm vụ

```yaml
platform*: shopee              # shopee | mercadolivre | amazon | tiktokshop | shopify
target_market*: Brazil
durations*: [15, 30]           # Tùy chọn [15] / [30] / [15, 30]
mode*: standard                # standard | variant
production_mode*: mixed        # ai_generated | real_shoot | mixed
prompt_language: en            # en | zh
```

---

## 1. Trường thượng nguồn · bàn giao từ 03 (mục chặn)

```yaml
# ── Dán trực tiếp từ khối「Các trường bàn giao cho module phía sau」trong đầu ra của 03 ──

core_selling_point*: ""        # Hook và mạch chính của video

secondary_points*: []          # Nội dung phần điểm bán hàng

spec_table*: {}                # Phần thông số

forbidden_words*: []           # Chặn cứng trong phụ đề

usage_scope_confirmed*: []     # Phạm vi cảnh bối cảnh

title_final*: ""               # CTA cuối video bắt buộc khớp với trường này
```

## 2. Trường thượng nguồn · bàn giao từ 04 (tùy chọn nhưng nên có)

```yaml
# ── Dán từ khối handoff_to_video trong đầu ra của 04 ──

visual_tone_confirmed: ""      # Thống nhất phong cách toàn video
hero_visual: ""                # Tham chiếu khung hình đầu
key_visual_moments: []         # Ưu tiên khi lên storyboard
```

> Có hai trường này, phong cách hình ảnh của video sẽ nhất quán với bộ 9 ảnh. **Thống nhất thị giác xuyên module là thể hiện độ chuyên nghiệp của quy trình này**——ảnh một phong cách, video một phong cách, người mua sẽ thấy như chắp vá.

---

## 3. Thông tin sản phẩm

```yaml
product_name*: ""
category*: ""
appearance:
  color: ""
  material: ""
  key_features: []
```

---

## 4. Nguồn hook (rất nên điền)

> SOP 1.6: **review là nơi gần nhất với nhu cầu thật của người mua.** Nguồn hook tốt nhất nằm ở đây.

```yaml
hook_material:
  pain_points: []              # Từ lời phàn nàn trong đánh giá tiêu cực, VD:
    # - "Người mua phàn nàn sạc dự phòng bị đè trong túi là mất điện"
  satisfaction_points: []      # Từ điểm hài lòng trong đánh giá tích cực, VD:
    # - "Người mua nhắc đi nhắc lại màn hình hiển thị dung lượng còn lại rất tiện"
  competitor_weakness: []      # Điểm yếu của đối thủ, VD:
    # - "Đối thủ phổ biến 18W, sản phẩm này 45W"
```

---

## 5. Ràng buộc sản xuất

```yaml
constraints:
  has_real_product: true       # Có sản phẩm thật để quay không
  can_shoot_people: false      # Có quay được người thật xuất hiện không (false thì toàn bộ dùng phương án không lộ mặt hoặc hoàn toàn bằng AI)
  available_props: []          # Đạo cụ có sẵn
  location_available: []       # Địa điểm có sẵn
  budget_level: ""             # low | medium | high (ảnh hưởng độ phức tạp của storyboard)
```

---

## 6. Sở thích lồng tiếng (tùy chọn)

```yaml
voice_style:
  gender: ""                   # Giọng nam / Giọng nữ / Không giới hạn
  tone: ""                     # Thân thiện / Chuyên nghiệp / Năng động / Điềm đạm
  accent: "Português (Brasil)"
  reference: ""                # Mô tả phong cách quảng cáo muốn tham khảo
```

---

## 7. mode = variant

```yaml
variant_angles: []             # Để trống thì Agent tự phân bổ
  # VD: ["Tiếp cận từ nỗi đau", "Tiếp cận từ kết quả"]
```

---

## Tự kiểm tra khi điền

- [ ] Đã dán sáu trường chặn từ 03
- [ ] Đã điền `title_final` (nếu không CTA sẽ lệch với tiêu đề)
- [ ] `production_mode` khớp với thực tế
- [ ] `can_shoot_people` điền đúng thực tế (false sẽ kích hoạt phương án không lộ mặt)
- [ ] Tôi hiểu: **cảnh người thật sẽ không có AI Prompt**, thay bằng chỉ dẫn quay (tuân thủ về chân dung)
- [ ] Tôi hiểu: **nội dung BGM / hiệu ứng âm thanh phải tự lo bản quyền**
- [ ] Tôi hiểu: thời lượng storyboard là giá trị đề xuất, thực tế cần căn theo audio lồng tiếng
