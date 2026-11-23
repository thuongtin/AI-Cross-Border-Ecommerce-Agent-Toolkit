---
name: sop-market-research
description: Skill nghiên cứu thị trường cho thương mại điện tử xuyên biên giới (Shopee BR / Mercado Livre). Làm sạch file CSV ngành hàng xuất từ Shaduola và các công cụ khác thành dữ liệu chuẩn, tính quy mô thị trường, mức độ tập trung thương hiệu/người bán (CR3/CR10/HHI), chia bin dải giá và dò vùng trũng, bảng chéo cấu hình, rồi diễn giải "ngành hàng này có đáng vào không". Dùng khi người dùng muốn "xem ngành hàng / phân tích thị trường / dải giá / mức độ tập trung đối thủ / nghiên cứu trước khi chọn sản phẩm".
allowed-tools:
  - Bash(python *)
  - Read
  - Write
metadata:
  version: 0.4.0
  category: e-commerce/market-research
  license: MIT
---

# 01 · Market Research Skill (nghiên cứu thị trường)

**Ranh giới phân công: con số do script tính, "nghĩa là gì, bước tiếp theo làm gì" do bạn (Agent) diễn giải.**
Đừng tự tính lại chỉ số — các con số trong báo cáo là kết quả tất định do script tính; nghi ngờ con số có vấn đề thì xuất
`[METRIC_SUSPECT]` để người dùng kiểm tra tham số script.

## Đầu vào tối thiểu

```text
1. File CSV/Excel dữ liệu sản phẩm của ngành hàng (xuất từ Shaduola và các công cụ khác: tên sản phẩm/giá/lượng bán tháng/doanh thu tháng/người bán/thương hiệu…)
2. Tên ngành hàng + sàn
3. (Tùy chọn) Tên trường chiều cấu hình, ví dụ: công suất,tải trọng
```

## Ba nguyên tắc nền

1. **Không bịa dữ liệu** — trường nào không có trong đầu vào thì không được đoán, thiếu cột quan trọng thì báo `[INPUT_MISSING]` và liệt kê các cột có sẵn
2. **Không thay thế quyết định chọn sản phẩm** — đầu ra là kết luận phân tích và gợi ý bước tiếp theo, quyết định cuối cùng bắt buộc do con người đưa ra
3. **Con số phải truy được nguồn** — mọi con số trích dẫn trong phần diễn giải đều phải chỉ ra được xuất xứ trong báo cáo của script

## Quy trình

```text
[Step 1] Chạy shaduola_parser.py để làm sạch dữ liệu (định dạng bẩn → JSON chuẩn hóa)
         Hỗ trợ R$ 1.234,56 / 1,234 / 1.2万 / 1,5 triệu / 4 tháng / thiếu doanh thu tháng thì tính bù bằng giá×lượng bán
[Step 2] Chạy market_metrics.py để ra báo cáo chỉ số (quy mô / CR3·CR10·HHI / vùng trũng dải giá / bảng chéo cấu hình)
[Step 3] Diễn giải theo prompts/02_market_analysis.md:
         → Ngành hàng này có đáng vào không (quy mô, mức độ tập trung, cận dưới dải giá vs giá khả thi theo chi phí)
         → Cấu hình phổ biến là gì, cấu hình cơ hội nằm ở đâu
         → Kết luận chuyển tiếp cho 02 Product Strategy
```

## Tra cứu nhanh lệnh

```bash
# ① Làm sạch dữ liệu (nhận cả CSV/Excel; --profile chỉ xem nhận diện cột, không xuất file)
python scripts/shaduola_parser.py file_xuat_nganh_hang.csv -o data.normalized.json

# ② Tính chỉ số (--config-fields đổi theo ngành hàng)
python scripts/market_metrics.py data.normalized.json \
    --bins 10 --config-fields "công suất,tải trọng,dung lượng" --format md -o report

# ③ Chưa có dữ liệu thật thì tạo mẫu có dữ liệu bẩn để kiểm tra môi trường trước
python scripts/make_sample.py
```

## Ngưỡng đánh giá khi diễn giải (có sẵn trong SOP, đưa vào phân tích của bạn)

- CR3 thương hiệu cao nhưng **top 3 đều là hàng no-brand** → người mua không chuộng thương hiệu, shop mới vẫn còn dư địa
- Người bán có "tỷ trọng doanh thu < tỷ trọng số sản phẩm" → loại chiếm chỗ chứ không phải loại hiệu suất, là đối tượng có thể vượt qua
- Ranh giới vùng trũng của dải giá ≈ giá khả thi theo chi phí → cấu trúc thị trường khớp với cấu trúc chi phí, mức giá đó đáng tin
- Cấu hình "nhiều sản phẩm nhưng lượng bán trung bình thấp" → phân khúc cạnh tranh gắt nhất, chỉ dùng làm mỏ neo giá, không làm SKU chủ lực
- Dò vùng trũng **mặc định không làm mượt** (làm mượt sẽ xóa mất vùng trũng dốc); khi số chủ thể ≤ n thì CR-n vô nghĩa, chuyển sang xem CR3 + HHI

## Hạn chế đã biết

- Bản thân việc thu thập dữ liệu không nằm trong Skill này (file xuất từ Shaduola/Seller Center do người dùng cung cấp)
- Các chỉ số đều **chưa tính thuế phí của Brazil**, khi đánh giá lợi nhuận hãy nhắc người dùng tự bổ sung thuế suất
- Dữ liệu lượng bán là số hiển thị của sàn, có nhiễu do buff đơn ảo, kết luận phải ghi rõ nguồn và thời điểm dữ liệu
