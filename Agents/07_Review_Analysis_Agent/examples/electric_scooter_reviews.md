# Case study · Phân tích đánh giá Patinete Elétrico 500W (Shopee Brazil)

> **Loại case study**: dữ liệu thật · đã ẩn danh hóa
> **Module sử dụng**: 07 Review Analysis Agent
> **SOP tương ứng**: 1.6 Phân tích đối thủ và phân tích đánh giá · 3.7 Duy trì đánh giá và hậu mãi
> **Trọng tâm minh họa**: **84,6% đánh giá tiêu cực có thể giải quyết bằng cách sửa nội dung** · điểm bán hàng lớn nhất đồng thời là nguồn hiểu lầm lớn nhất

**Vì sao chọn case này**: đây là "phục bút" đã cài sẵn trong [case study flagship](../../../Examples/01_Patinete_Eletrico_500W/) — đoạn Lưu ý trên trang chi tiết của case đó đã dự báo ba nhóm đánh giá tiêu cực (tải trọng, quãng đường, lắp ráp). Case này **dùng dữ liệu đánh giá thật để kiểm chứng dự báo đó chính xác đến đâu**, và đưa ra phương án vá. Nó minh họa **vòng khép kín quay vòng** của toàn bộ quy trình.

---

## I. Tổng quan dữ liệu

| Hạng mục | Giá trị | Tỷ trọng |
|---|---|---|
| Tổng số đánh giá | **128** | 100% |
| Tích cực (4–5 sao) | 104 | **81,2%** |
| Trung lập (3 sao) | 11 | 8,6% |
| Tiêu cực (1–2 sao) | **13** | **10,2%** |
| Số đánh giá có ảnh | 31 | **24,2%** |

**Đánh giá cỡ mẫu**: ✅ Đủ (≥ 50 đánh giá)

**Giới hạn dữ liệu**: sàn đã xóa một phần đánh giá (SOP có nhắc sàn sẽ xóa đánh giá quá sơ sài, trùng lặp nhiều hoặc vi phạm), mẫu thực tế có thể không đầy đủ.

---

## II. Kiểm chứng dự báo của case study flagship trước

Case study flagship đã viết bốn mục giải thích trước trong đoạn Lưu ý của trang chi tiết. Giờ xem đánh giá tiêu cực thật có rơi vào phạm vi dự báo không:

| Dự báo của case study flagship | Đánh giá tiêu cực thực tế có xuất hiện không | Trúng |
|---|---|---|
| Khai khống quãng đường ("35 km đo thực tế không đúng") | ✅ Có (xem Thông số không như kỳ vọng #1) | ✅ |
| Tải trọng không như kỳ vọng ("tưởng chở được hai người") | ✅ Có (xem Hiểu lầm #1) | ✅ |
| Khó lắp ráp | ✅ Có (xem Khó sử dụng #1) | ✅ |
| Cần kiểm tra luật giao thông địa phương | ❌ Không xuất hiện | — |

> **Trúng 3 trên 4 dự báo.**
>
> Điều này cho thấy đoạn Lưu ý mà case study flagship viết dựa trên `review_insights` và `usage_scope` là đúng hướng. **Nhưng 3 mục trúng vẫn phát sinh đánh giá tiêu cực — chứng tỏ "đã viết" không có nghĩa là "hiệu quả".** Đây chính là vấn đề cốt lõi case này cần giải quyết.

---

## III. Phân tích đánh giá tích cực

### 3.1 Vì sao người mua hài lòng

| # | Lý do hài lòng | Số lần nhắc | Tỷ trọng | Nguyên văn tiêu biểu |
|---|---|---|---|---|
| 1 | Khả năng leo dốc | 38 | 36,5% | `Sobe ladeira sem esforço, achei que ia travar mas subiu tranquilo` |
| 2 | Gấp gọn tiện lợi | 31 | 29,8% | `Dobro em segundos e coloco no porta-malas do carro` |
| 3 | Giảm xóc tốt | 27 | 26,0% | `Passei em cima de buraco e nem senti` |
| 4 | Thời lượng pin | 22 | 21,2% | `Ando 25 km por dia e ainda sobra bateria` |
| 5 | Thiết kế ngoại hình | 18 | 17,3% | `Muito bonito, parece de marca cara` |
| 6 | Đáng tiền | 14 | 13,5% | `Pelo preço, valeu muito` |
| 7 | CSKH của người bán | 9 | 8,7% | `Vendedor respondeu rápido e ajudou na montagem` |

> ⚠️ **Mục 4 đáng chú ý**: đánh giá tích cực nói "đi 25 km vẫn còn pin", đánh giá tiêu cực nói "chỉ chạy được 20 km". **Cùng một cục pin, hai kết luận — khác biệt đến từ tải trọng.** Phép đối chiếu này là manh mối then chốt để nhận diện đánh giá tiêu cực về quãng đường ở phần sau.

### 3.2 Đối chiếu hiệu quả điểm bán hàng

| Điểm bán hàng | Số lần nhắc | Listing hiện tại có làm nổi bật không | Đề xuất |
|---|---|---|---|
| Khả năng leo dốc | 38 | ⚠️ **Tiêu đề có `500W`, nhưng ảnh chính không làm nổi bật khả năng leo dốc** | Ảnh chính + video tăng cường cảnh leo dốc |
| Gấp gọn tiện lợi | 31 | ✅ Tiêu đề có `Dobrável`, ảnh 5 là ảnh riêng | Giữ nguyên |
| Giảm xóc tốt | 27 | ✅ Tiêu đề có `e Suspensão`, ảnh 6 cận cảnh | Giữ nguyên |
| Thời lượng pin | 22 | ⚠️ Chỉ có trong bảng thông số, xếp thứ 3 trên ảnh thông số | Đưa lên đầu ảnh thông số + ghi điều kiện thử nghiệm |
| **Phản hồi CSKH** | **9** | ❌ **Listing hoàn toàn không nhắc** | ⚠️ **Đây là cơ hội bỏ ngỏ** |

> **CSKH được 9 đánh giá tích cực chủ động khen, nhưng Listing không nhắc một chữ nào.**
> Ít đánh giá, độ tin cậy chưa đủ là lực cản chính với tỷ lệ chuyển đổi (xem kết luận trong [case study quảng cáo 06](../../06_Advertising_Optimization_Agent/examples/powerbank_20000mah_ads.md)), mà **"người bán phản hồi nhanh" lại đúng là một trong những điều người mua muốn xác nhận nhất trước khi đặt hàng**. Viết điểm này vào trang chi tiết là hành động chi phí bằng 0.

### 3.3 Vận chuyển và hậu mãi

| Khía cạnh | Nhắc tích cực | Nhắc tiêu cực | Cảm xúc ròng |
|---|---|---|---|
| Tốc độ giao hàng | 12 | 1 | ✅ Tích cực |
| Độ nguyên vẹn của đóng gói | 8 | 1 | ✅ Tích cực |
| Phản hồi CSKH | 9 | 0 | ✅ Tích cực |

### 3.4 Cảm nhận về giá

| Loại | Số lần nhắc | Nguyên văn tiêu biểu |
|---|---|---|
| Thấy đáng tiền | 14 | `Custo-benefício excelente para o que entrega` |
| Thấy hơi đắt | 2 | `Achei um pouco caro, mas a qualidade compensa` |

---

## IV. Quy nguyên nhân đánh giá tiêu cực

### 4.1 Phân bố nguyên nhân

| # | Nhóm nguyên nhân | Số lượng | Tỷ trọng | Bên chịu trách nhiệm | Sửa được bằng nội dung không |
|---|---|---|---|---|---|
| 1 | **Hiểu lầm** ⭐ | **5** | **38,5%** | Phía mình (trang chi tiết) | ✅ Được |
| 2 | Lỗi chất lượng sản phẩm | 0 | 0,0% | Nhà cung cấp | ❌ |
| 3 | Thông số không như kỳ vọng | **3** | 23,1% | Phía mình | ✅ Được |
| 4 | Thiếu phụ kiện | **2** | 15,4% | Phía mình (danh sách đóng gói) | ✅ Được |
| 5 | Giao hàng chậm | 1 | 7,7% | Đơn vị vận chuyển | ❌ |
| 6 | Khó sử dụng | **1** | 7,7% | Phía mình (sách hướng dẫn) | ✅ Được |
| 7 | Hậu mãi kém | 0 | 0,0% | Phía mình | ✅ Được |
| 8 | Hư hỏng / lỗi / trả hàng | 1 | 7,7% | Đơn vị vận chuyển / nhà cung cấp | ❌ |
| | **Tổng** | **13** | 100% | | |

### 4.2 ⭐ Con số quan trọng nhất của case này

```
Mục khắc phục được = Hiểu lầm 5 + Thông số không khớp 3 + Thiếu phụ kiện 2 + Khó sử dụng 1 + Hậu mãi kém 0
                   = 11 đánh giá

Chiếm tổng đánh giá tiêu cực = 11 ÷ 13 = 84,6%
```

> ### **84,6% đánh giá tiêu cực có thể giải quyết bằng cách sửa nội dung và hình ảnh, không cần động vào sản phẩm, không cần đổi nhà cung cấp, không cần đổi đơn vị vận chuyển.**
>
> Hơn nữa, kiểu khắc phục này có **chi phí gần bằng 0, thời gian là "sửa xong có hiệu lực ngay"**.
>
> So sánh với 15,4% còn lại: một đánh giá là giao hàng chậm (phải đổi vận chuyển), một là hư hỏng/lỗi (phải cải tiến đóng gói hoặc đổi nhà cung cấp) — hai nhóm này mất vài tuần đến vài tháng mới khắc phục được.
>
> **Vì vậy thứ tự hành động đúng là: dành một ngày sửa nội dung để xử lý 11 đánh giá trước, rồi mới xử lý 2 đánh giá còn lại.**

### 4.3 Chi tiết từng nhóm

#### Hiểu lầm (5 đánh giá)

| # | Nguyên văn | Người mua tưởng | Thực tế | Phán định |
|---|---|---|---|---|
| 1 | `Pensei que dava para duas pessoas, mas é só para uma mesmo` | Chở được hai người | `capacidade_carga = 150 kg` (không ghi rõ "chỉ một người") | Giải thích không nổi bật |
| 2 | `Não sobe ladeira forte como no vídeo, aqui tem um morro íngreme` | Leo được mọi loại dốc | `usage_scope` chỉ gồm `vias planas e pavimentadas` | Giải thích không nổi bật |
| 3 | `Imaginai que fosse mais leve, é difícil de subir no ônibus` | Nhẹ hơn | `peso_produto = 18 kg` (ghi ở dòng 12 bảng thông số) | Giải thích không nổi bật |
| 4 | `O farol é fraco à noite, quase não ilumina a rua` | Dùng làm đèn chiếu sáng ban đêm được | Không ghi rõ đèn chỉ dùng để báo hiệu, giúp người khác nhìn thấy | **Thiếu giải thích** |
| 5 | `Pensei que a garantia era de 1 ano, mas é 6 meses` | Bảo hành 1 năm | `warranty = 6 meses (motor e bateria)` | Giải thích không nổi bật |

#### Thông số không như kỳ vọng (3 đánh giá)

| # | Nguyên văn | Người mua kỳ vọng | Giá trị thực tế | Phán định |
|---|---|---|---|---|
| 1 | `Diz 35 km mas só fez 20 km comigo` | 35 km | `autonomia = até 35 km` (điều kiện thử nghiệm: người lái 70 kg) | **Mô tả chưa rõ** — cân nặng người mua cao hơn hẳn điều kiện thử nghiệm |
| 2 | `A velocidade não chega a 30 km/h nem no plano` | 30 km/h | `velocidade_max = 30 km/h` | **Mô tả chưa rõ** — không ghi rõ là "tốc độ tối đa" chứ không phải "tốc độ duy trì" |
| 3 | `Demorou mais de 7 horas para carregar` | 5–6 h | `tempo_recarga = 5 a 6 horas` (với sạc chính hãng) | **Mô tả chưa rõ** — người mua dùng sạc không chính hãng |

> **Cả ba đều không phải khai khống thông số, mà là "chưa ghi rõ điều kiện thử nghiệm".** Cả ba nên xếp vào "mô tả chưa rõ" chứ không phải "mô tả sai" — **cách xử lý là bổ sung điều kiện, không phải sửa con số.**
>
> Đây là một phép phân biệt rất quan trọng: nếu phán định nhầm thành "mô tả sai" rồi sửa giá trị công bố thành 20 km, thì chẳng khác nào tự bỏ đi một lợi thế có thật (khi tải nhẹ đúng là chạy được 35 km).

#### Thiếu phụ kiện (2 đánh giá)

| # | Nguyên văn | Người mua tưởng có kèm | Thực tế trong `package_content` | Phán định |
|---|---|---|---|---|
| 1 | `Achei que vinha com capacete` | Mũ bảo hiểm | **Không kèm** | Hiểu lầm → cần ghi rõ |
| 2 | `Não veio a bomba de ar para os pneus` | Bơm hơi | **Không kèm** | Hiểu lầm → cần ghi rõ |

> ⚠️ **Cả hai đều là hiểu lầm, không phải thiếu hàng.** Đối chiếu `package_content` xác nhận sản phẩm vốn không kèm hai món này.
> **Hành động đúng là ghi rõ "không kèm gì" trên ảnh danh sách đóng gói, không phải gửi bù phụ kiện.**
> Gửi bù phụ kiện là sai — chi phí sẽ tăng, mà lô người mua tiếp theo vẫn hiểu lầm như cũ.

#### Giao hàng chậm (1 đánh giá)

| # | Nguyên văn | Vấn đề |
|---|---|---|
| 1 | `Demorou 12 dias para chegar` | Thời gian vận chuyển |

**Không sửa được bằng nội dung**. Hành động: kiểm tra xem có cần điều chỉnh cách diễn đạt cam kết giao hàng không, hoặc trao đổi với đơn vị vận chuyển.

#### Khó sử dụng (1 đánh giá)

| # | Nguyên văn | Vấn đề |
|---|---|---|
| 1 | `Difícil de montar, o manual não explica bem a parte do guidão` | Sách hướng dẫn giải thích phần tay lái chưa rõ |

**Sửa được bằng nội dung**. Hành động: bổ sung một ảnh hướng dẫn lắp ráp (quay về 04).

#### Hư hỏng / lỗi / trả hàng (1 đánh giá)

| # | Nguyên văn | Vấn đề |
|---|---|---|
| 1 | `Veio com um risco na carenagem e a lanterna traseira não acende` | Trầy xước khi vận chuyển + đèn hậu hỏng |

**Không sửa được bằng nội dung**. Hành động: cải tiến đóng gói (chống trầy) + kiểm tra đèn hậu trước khi xuất kho.

---

## V. ⭐ Phát hiện then chốt nhất: điểm bán hàng lớn nhất = nguồn hiểu lầm lớn nhất

Đặt xếp hạng điểm bán hàng từ đánh giá tích cực cạnh kết quả quy nguyên nhân đánh giá tiêu cực:

| Điểm bán hàng | Nhắc trong đánh giá tích cực | Hạng | Đánh giá tiêu cực liên quan | Nguyên nhân đánh giá tiêu cực |
|---|---|---|---|---|
| **Khả năng leo dốc** | **38 lần** | **🥇 Hạng 1** | **1 đánh giá** | Hiểu lầm #2 (tưởng leo được dốc gắt) |
| Gấp gọn tiện lợi | 31 lần | 🥈 Hạng 2 | 0 đánh giá | — |
| Giảm xóc tốt | 27 lần | 🥉 Hạng 3 | 0 đánh giá | — |
| **Thời lượng pin** | 22 lần | Hạng 4 | **1 đánh giá** | Thông số không khớp #1 (đo thực tế thấp hơn công bố) |
| Thiết kế ngoại hình | 18 lần | Hạng 5 | 0 đánh giá | — |

> ### **Điểm bán hàng hạng 1 đồng thời cũng là một nguồn đánh giá tiêu cực.**
>
> Đây không phải ngẫu nhiên, mà là một **quy luật**:
>
> **Điểm bán hàng càng được nhấn mạnh trên trang chi tiết và video, kỳ vọng của người mua càng cao; kỳ vọng càng cao, khả năng hụt hẫng càng lớn.**
>
> Case study flagship quay "cảnh leo dốc" trong video, ghi `500W` trong tiêu đề, đặt `Motor 500W` trên ảnh 2 — biến khả năng leo dốc thành điểm bán hàng số 1. Người mua vì thế kỳ vọng "xe này dốc nào cũng leo được", rồi thất vọng ngay trên con dốc gắt trước cửa nhà.

### Không phải "không nên nhấn mạnh", mà là "nhấn mạnh thì phải kèm giới hạn"

| Cách làm | Kết quả |
|---|---|
| ❌ Giảm quảng bá khả năng leo dốc | Mất điểm bán hàng số 1, được không bù mất |
| ❌ Không ghi bất kỳ giới hạn nào | Đánh giá tiêu cực tiếp tục phát sinh |
| ✅ **Tăng cường khả năng leo dốc + đồng thời ghi rõ giới hạn** | **Vừa giữ sức thuyết phục của điểm bán hàng, vừa kiểm soát được kỳ vọng** |

**Hành động cụ thể**:

```text
Trước đây (hiện trạng case study flagship): ảnh 2 chỉ ghi "Motor 500W"
Đổi thành: ảnh 2 ghi "Motor 500W" + chữ nhỏ "Indicado para ladeiras leves"
```

> **Một dòng chữ nhỏ, vừa giữ được điểm bán hàng, vừa xóa được hiểu lầm.** Đây là thủ pháp cốt lõi của module — **không phải làm mô tả dè dặt hơn, mà là làm mô tả chính xác hơn.**

Logic tương tự áp dụng cho quãng đường:

```text
Ảnh thông số trước đây: "Autonomia: até 35 km"
Đổi thành:              "Autonomia: até 35 km (piloto de 70 kg, piso plano)"
```

---

## VI. Đề xuất vá trang chi tiết

### 6.1 Mục thêm mới / chỉnh sửa (→ 03 Listing)

| # | Đánh giá tiêu cực tương ứng | Vị trí viết | Nội dung (PT-BR) | Giải thích (tiếng Việt) |
|---|---|---|---|---|
| 1 | Hiểu lầm #1 | Đoạn 6 · **mục đầu** | `Indicado para 1 pessoa. Capacidade máxima de 150 kg (piloto + bagagem).` | Ghi rõ chỉ một người đi |
| 2 | Hiểu lầm #2 | Đoạn 6 · mục đầu | `Indicado para vias planas e pavimentadas e ladeiras leves.` | Đưa từ `usage_scope` lên đầu |
| 3 | Hiểu lầm #3 | Đoạn 6 | `Peso do produto: 18 kg. Recomendamos duas pessoas para transportá-lo em escadas ou ônibus.` | Trọng lượng + gợi ý sử dụng |
| 4 | Hiểu lầm #4 | Đoạn 6 | `O farol LED é para sinalização e visibilidade. Não substitui iluminação de via pública.` | Giải thích giới hạn công dụng của đèn |
| 5 | Hiểu lầm #5 | Đoạn 5 · Hậu mãi | `Garantia de 6 meses para motor e bateria.` | Đưa bảo hành vào đoạn 5 (trước đây chỉ có trong bảng thông số) |
| 6 | Thông số không khớp #1 | Đoạn 4 · Ghi chú thông số | `Autonomia de até 35 km medida com piloto de 70 kg, em piso plano, a 20 km/h.` | Bổ sung đủ điều kiện thử nghiệm |
| 7 | Thông số không khớp #2 | Đoạn 4 · Ghi chú thông số | `Velocidade máxima de 30 km/h. A velocidade média de uso é menor.` | Phân biệt tốc độ tối đa và trung bình |
| 8 | Thông số không khớp #3 | Đoạn 4 · Ghi chú thông số | `Tempo de recarga de 5 a 6 horas com o carregador original incluso.` | Giới hạn ở sạc chính hãng |
| 9 | Khó sử dụng #1 | Đoạn 6 | `A montagem do guidão leva cerca de 15 minutos. Veja o guia ilustrado abaixo.` | Hướng dẫn lắp ráp |

### 6.2 Ảnh cần bổ sung (→ 04 Product Image)

| # | Đánh giá tiêu cực tương ứng | Vị trí ảnh | Chữ trên ảnh (PT-BR) | Mô tả |
|---|---|---|---|---|
| 1 | Thiếu phụ kiện #1 #2 | Ảnh 8 · Ảnh danh sách đóng gói | `Não incluso: capacete, bomba de ar` | **Dùng ảnh thay cho chữ** — giải thích bằng chữ sẽ bị lướt qua |
| 2 | Khó sử dụng #1 | Thêm ảnh 10 · Ảnh hướng dẫn lắp ráp | Ảnh từng bước `1 · 2 · 3` | ML cho phép 12 ảnh, Shopee cần thay ảnh giá trị thấp |
| 3 | Hiểu lầm #2 | Ảnh 4 · Ảnh tình huống | Chữ nhỏ `Vias pavimentadas` | Thêm giải thích giới hạn trên ảnh tình huống |
| 4 | Thông số không khớp #1 | Ảnh 3 · Ảnh thông số | Thêm `(piloto 70 kg, piso plano)` dưới mục quãng đường | Bổ sung điều kiện thử nghiệm trên ảnh thông số |

> **Mục 1 là giải pháp tối ưu**: hiểu lầm về phụ kiện **viết chữ thế nào cũng không rõ**, vì người mua không đọc bảng thông số cũng không đọc đoạn Lưu ý. Nhưng **một dòng `Não incluso` trên ảnh bày phẳng thì không ai bỏ sót.**

### 6.3 Điểm bán hàng cần bổ sung (→ 03)

| # | Phát hiện | Hành động |
|---|---|---|
| 1 | Phản hồi CSKH được 9 đánh giá tích cực chủ động khen, nhưng Listing không nhắc | Thêm vào cam kết hậu mãi ở đoạn 5: `Atendimento pelo chat com resposta em até 24 horas` |

> **Đây là yếu tố tạo niềm tin chi phí bằng 0**: trước khi đặt hàng, người mua muốn biết nhất "có vấn đề thì tìm ai", và đây lại đúng là điểm mạnh đã được người mua thật xác nhận. **Giá trị lớn nhất của phân tích đánh giá chính là phát hiện những "ưu điểm đã được kiểm chứng nhưng chưa viết vào Listing" như thế này.**

---

## VII. Lằn ranh đỏ thông số

| # | Thông số bị phàn nàn | Người mua kỳ vọng | Giá trị thực tế | Ứng viên từ cấm | Lý do |
|---|---|---|---|---|---|
| 1 | Quãng đường | 60 km | 35 km | `60 km` `autonomia longa` `dura o dia todo` | Bảng từ khóa của đối thủ có 60km, lấy dùng là khai khống thông số |
| 2 | Tải trọng | 200 kg | 150 kg | `200 kg` | Quá tải có rủi ro an toàn |
| 3 | Leo dốc | Mọi loại dốc | Dốc thoải | `qualquer ladeira` `sobe tudo` `off-road` | Diễn đạt không giới hạn sẽ bị hiểu là mọi tình huống |
| 4 | Chiếu sáng ban đêm | Thay thế đèn đường | Chỉ để báo hiệu | `iluminação noturna` `farol potente` | Liên quan cam kết an toàn |
| 5 | Tốc độ | 60 km/h | 30 km/h | `60 km/h` `alta velocidade` | Lẫn từ bảng từ khóa của đối thủ |
| 6 | Bảo hành | 1 năm | 6 tháng | `garantia de 1 ano` | Tránh hụt hẫng kỳ vọng |

```yaml
forbidden_words_candidates:
  - "60 km"
  - "60 km/h"
  - "200 kg"
  - "autonomia longa"
  - "dura o dia todo"
  - "qualquer ladeira"
  - "sobe tudo"
  - "off-road"
  - "iluminação noturna"
  - "farol potente"
  - "garantia de 1 ano"
```

> **Lằn ranh đỏ 1 và 5 đặc biệt đáng chú ý**: `60 km` `60 km/h` rất có thể xuất hiện trong **bảng từ khóa của đối thủ** (đối thủ công bố quãng đường 60 km, tốc độ tối đa 60 km/h). Nếu theo hướng SEO mà viết những từ này vào tiêu đề, thì chẳng khác nào chủ động khai khống thông số.
> **Phân tích đánh giá là con đường trực tiếp nhất để phát hiện những lằn ranh đỏ như vậy** — vì người mua sẽ cầm thông số của đối thủ ra chất vấn bạn.

---

## VIII. Xếp hạng điểm bán hàng (kèm mức độ cảm xúc)

| Hạng | Điểm bán hàng | Số lần nhắc | Mức độ cảm xúc | Điểm tổng hợp | Hành động đề xuất |
|---|---|---|---|---|---|
| 1 | Khả năng leo dốc | 38 | Mạnh (×3) | **114** | Ảnh chính + video (**đồng thời thêm giải thích giới hạn**) |
| 2 | Gấp gọn tiện lợi | 31 | Mạnh (×3) | **93** | Đã nổi bật, giữ nguyên |
| 3 | Giảm xóc tốt | 27 | Vừa (×2) | **54** | Đã nổi bật, giữ nguyên |
| 4 | Thời lượng pin | 22 | Vừa (×2) | **44** | Đưa lên đầu ảnh thông số + bổ sung điều kiện thử nghiệm |
| 5 | Thiết kế ngoại hình | 18 | Vừa (×2) | **36** | Giữ trên trang chi tiết |
| 6 | Đáng tiền | 14 | Vừa (×2) | **28** | Tăng cường trong điểm bán hàng ở đoạn 2 |
| 7 | **CSKH của người bán** | 9 | Mạnh (×3) | **27** | ⭐ **Thêm mới vào đoạn 5 trang chi tiết** |

**Tiêu chí phán định mức độ cảm xúc**: Mạnh (`excelente` / `perfeito` / `superou` / `recomendo`, trọng số 3) · Vừa (`bom` / `funciona bem` / `satisfeito`, trọng số 2) · Yếu (`ok` / `razoável`, trọng số 1)

> **Đối chiếu hiện trạng Listing**:
> - 2 điểm bán hàng hạng đầu (leo dốc, gấp gọn) đều có trong tiêu đề hoặc ảnh chính ✅
> - **CSKH** hạng 7 hoàn toàn không được nhắc ⚠️ → đây là **điểm tối ưu mới phát hiện**, chi phí bằng 0
> - **Quãng đường** hạng 4 chỉ nằm ở dòng 3 bảng thông số → có thể đưa lên đầu

---

## IX. Trả lời mục tiêu phân tích (bảy câu hỏi của SOP 1.6)

| # | Câu hỏi | Kết luận | Căn cứ |
|---|---|---|---|
| 1 | Đối thủ bán được nhờ đâu | (Case này phạm vi `own`, chưa nhập đánh giá đối thủ) | — |
| 2 | Người mua thực sự quan tâm điều gì | **Khả năng leo dốc** (38 lần, hạng 1) > gấp gọn tiện lợi > giảm xóc | 128 đánh giá |
| 3 | **Điểm bán hàng nào bắt buộc phải viết** | Khả năng leo dốc, gấp gọn, giảm xóc, quãng đường, **phản hồi CSKH** | Xếp hạng tần suất đánh giá tích cực |
| 4 | **Thông số nào không được viết bừa** | Quãng đường (điều kiện giới hạn 35 km), tải trọng (150 kg một người), tốc độ (tối đa 30 km/h), bảo hành (6 tháng) | 3 đánh giá quy nguyên nhân thông số + 2 đánh giá hiểu lầm |
| 5 | **Vấn đề nào cần giải thích trước** | Chỉ một người đi / giới hạn leo dốc / trọng lượng 18 kg / công dụng của đèn / thời hạn bảo hành / điều kiện thử nghiệm quãng đường / thời gian lắp ráp | 11 đánh giá tiêu cực khắc phục được |
| 6 | Phía mình nên làm nổi bật khác biệt gì | Khả năng leo dốc (đối thủ ít nhấn mạnh và phía mình đã được kiểm chứng hiệu quả) + **phản hồi CSKH** (đã được kiểm chứng nhưng chưa quảng bá) | Xếp hạng đánh giá tích cực |
| 7 | Phía mình cần tránh rủi ro hậu mãi gì | Hụt hẫng kỳ vọng về quãng đường, hụt hẫng kỳ vọng về leo dốc, hiểu lầm về phụ kiện, hiểu lầm về công dụng của đèn | Quy nguyên nhân đánh giá tiêu cực |

---

## X. Đánh giá khả năng khắc phục

| Hạng mục | Số lượng | Tỷ trọng |
|---|---|---|
| Tổng đánh giá tiêu cực | 13 | 100% |
| **Khắc phục được bằng sửa mô tả / sửa ảnh** | **11** | **84,6%** |
| Cần sửa sản phẩm / nhà cung cấp | 0 | 0% |
| Cần sửa vận chuyển / đóng gói | 2 | 15,4% |

**Thứ tự ưu tiên khắc phục** (xếp theo «tần suất xuất hiện ÷ chi phí khắc phục»):

| Thứ tự | Hành động | Đánh giá tiêu cực bao phủ | Chi phí | Hiệu lực |
|---|---|---|---|---|
| 1 | Ảnh danh sách đóng gói ghi rõ `Não incluso` | 2 đánh giá (15,4%) | 1 ảnh | Ngay lập tức |
| 2 | Bổ sung 5 mục giải thích giới hạn ở đoạn 6 | 5 đánh giá (38,5%) | Sửa nội dung | Ngay lập tức |
| 3 | Bổ sung điều kiện thử nghiệm ở đoạn thông số | 3 đánh giá (23,1%) | Sửa nội dung | Ngay lập tức |
| 4 | Bổ sung ảnh hướng dẫn lắp ráp | 1 đánh giá (7,7%) | 1 ảnh | Ngay lập tức |
| 5 | Cải tiến đóng gói / kiểm tra trước khi xuất kho | 1 đánh giá (7,7%) | Cần chuỗi cung ứng | Vài tuần |
| 6 | Trao đổi với đơn vị vận chuyển | 1 đánh giá (7,7%) | Cần bên ngoài | Vài tuần |

> **4 hành động đầu bao phủ 11 đánh giá tiêu cực (84,6%), toàn bộ là "sửa nội dung + bổ sung hai ảnh", làm xong trong một ngày.**

---

## XI. Quét tuân thủ phân tích

`Quét tuân thủ phân tích: không vi phạm`

(Case này không liên quan đến: dụ dỗ xóa đánh giá, báo cáo có tổ chức, đánh giá giả, tự suy đoán thật/giả của đánh giá, làm lộ thông tin riêng tư của người mua. Mọi kết luận dựa trên nội dung văn bản và đối chiếu trường dữ liệu, không phán đoán tính xác thực của đánh giá.)

---

## XII. Các trường bàn giao cho module khác

```yaml
selling_points_ranked:
  - {rank: 1, point: "Khả năng leo dốc", mentions: 38, strength: "mạnh", score: 114, action: "Ảnh chính + video (thêm giải thích giới hạn)"}
  - {rank: 2, point: "Gấp gọn tiện lợi", mentions: 31, strength: "mạnh", score: 93, action: "Giữ nguyên"}
  - {rank: 3, point: "Giảm xóc tốt", mentions: 27, strength: "vừa", score: 54, action: "Giữ nguyên"}
  - {rank: 4, point: "Thời lượng pin", mentions: 22, strength: "vừa", score: 44, action: "Đưa lên đầu ảnh thông số + bổ sung điều kiện thử nghiệm"}
  - {rank: 7, point: "CSKH của người bán", mentions: 9, strength: "mạnh", score: 27, action: "⭐ Thêm mới vào đoạn 5"}

forbidden_words_candidates:
  ["60 km", "60 km/h", "200 kg", "autonomia longa", "dura o dia todo",
   "qualquer ladeira", "sobe tudo", "off-road", "iluminação noturna",
   "farol potente", "garantia de 1 ano"]

review_patch_suggestions:             # → 03 trang chi tiết
  - {location: "Đoạn 6 mục đầu", copy: "Indicado para 1 pessoa. Capacidade máxima de 150 kg (piloto + bagagem)."}
  - {location: "Đoạn 6 mục đầu", copy: "Indicado para vias planas e pavimentadas e ladeiras leves."}
  - {location: "Đoạn 6", copy: "Peso do produto: 18 kg. Recomendamos duas pessoas para transportá-lo em escadas ou ônibus."}
  - {location: "Đoạn 6", copy: "O farol LED é para sinalização e visibilidade. Não substitui iluminação de via pública."}
  - {location: "Đoạn 5 hậu mãi", copy: "Garantia de 6 meses para motor e bateria."}
  - {location: "Đoạn 5 hậu mãi", copy: "Atendimento pelo chat com resposta em até 24 horas."}
  - {location: "Đoạn 4 ghi chú thông số", copy: "Autonomia de até 35 km medida com piloto de 70 kg, em piso plano, a 20 km/h."}
  - {location: "Đoạn 4 ghi chú thông số", copy: "Velocidade máxima de 30 km/h. A velocidade média de uso é menor."}
  - {location: "Đoạn 4 ghi chú thông số", copy: "Tempo de recarga de 5 a 6 horas com o carregador original incluso."}
  - {location: "Đoạn 6", copy: "A montagem do guidão leva cerca de 15 minutos. Veja o guia ilustrado abaixo."}

packaging_clarity_needed: true         # → 04 bổ sung ảnh danh sách đóng gói (ghi rõ Não incluso)
scene_limit_image_needed: true         # → 04 thêm giải thích giới hạn trên ảnh tình huống

# Chỉ số chính (để đối chiếu khi kiểm tra lại)
negative_review_count: 13
misunderstanding_count: 5
fixable_count: 11
fixable_ratio: 0.846
image_review_ratio: 0.242
```

---

## XIII. Phương án kiểm tra lại (retest)

| Hạng mục | Nội dung |
|---|---|
| Mốc kiểm tra lại | **14–30 ngày** sau khi thay đổi có hiệu lực (đánh giá cần thời gian tích lũy, chu kỳ dài hơn kiểm tra lại quảng cáo) |
| **Chỉ số quan sát chính** | **Tỷ trọng đánh giá tiêu cực loại hiểu lầm trong tổng đánh giá tiêu cực** (hiện tại 38,5%) |
| Chỉ số phụ | Số đánh giá tiêu cực nhóm thiếu phụ kiện (hiện tại 2), nhóm thông số không khớp (hiện tại 3) |
| Tiêu chuẩn đạt | Tỷ trọng loại hiểu lầm giảm xuống **dưới 20%** |
| Xử lý khi không đạt | Kiểm tra xem là "phán định sai loại" (nên dùng ảnh lại dùng chữ) hay "vị trí không nổi bật" |
| Yếu tố nhiễu cần loại trừ | Có đổi đơn vị vận chuyển / đổi lô hàng / trùng đợt sale lớn kéo theo tệp khách mới không |

> **Vì sao chỉ số chính chọn "tỷ trọng loại hiểu lầm" mà không phải "số đánh giá tiêu cực"?**
> Vì tổng số đánh giá tiêu cực chịu ảnh hưởng của doanh số, vận chuyển, sale lớn và các yếu tố bên ngoài khác, **không phải thứ nội dung kiểm soát được**. Còn tỷ trọng loại hiểu lầm gần như hoàn toàn do nội dung quyết định — **đó là chỉ số sạch nhất để kiểm chứng "sửa nội dung có tác dụng hay không".**

---

## XIV. Case này chứng minh điều gì

| Kết luận | Bằng chứng |
|---|---|
| **Phần lớn đánh giá tiêu cực là vấn đề nội dung, không phải vấn đề sản phẩm** | 84,6% (11/13) đánh giá tiêu cực khắc phục được bằng sửa mô tả / sửa ảnh |
| **Điểm bán hàng lớn nhất đồng thời là nguồn hiểu lầm lớn nhất** | Khả năng leo dốc xếp hạng 1 trong đánh giá tích cực (38 lần), đồng thời sinh ra 1 đánh giá tiêu cực loại hiểu lầm |
| **"Đã viết" không có nghĩa là "hiệu quả"** | Case study flagship đã dự báo 3 nhóm đánh giá tiêu cực và đã viết giải thích, nhưng vẫn phát sinh đủ cả 3 → vị trí / hình thức giải thích chưa đúng |
| **Hiểu lầm về phụ kiện không thể giải thích rõ bằng chữ** | Cả 2 đánh giá về phụ kiện đều do người mua không đọc bảng thông số → bắt buộc dùng ảnh bày phẳng + `Não incluso` |
| **"Mô tả chưa rõ" ≠ "mô tả sai"** | Cả 3 đánh giá về thông số đều do thiếu điều kiện thử nghiệm, **không phải khai khống** → bổ sung điều kiện chứ không sửa con số |
| **Đánh giá tích cực giúp phát hiện ưu điểm bị chìm** | Phản hồi CSKH được 9 đánh giá tích cực khen nhưng Listing không nhắc → điểm tối ưu chi phí bằng 0 |
| **Thông số của đối thủ có thể thành lằn ranh đỏ của chính mình** | `60 km` `60 km/h` đến từ bảng từ khóa của đối thủ → bắt buộc đưa vào `forbidden_words` |
| **Làm mô tả chính xác hơn, không phải dè dặt hơn** | Thêm giải thích giới hạn "dốc thoải", vừa giữ được điểm bán hàng số 1 vừa kiểm soát kỳ vọng |
| **Chỉ số kiểm tra lại phải chọn cái mà nội dung kiểm soát được** | Dùng "tỷ trọng loại hiểu lầm" thay vì "tổng đánh giá tiêu cực" |
| **Vòng khép kín được xác lập** | 03 viết đoạn Lưu ý → đăng bán → 07 phân tích đánh giá → quay về 03 sửa nội dung → kiểm tra lại |

---

**File liên quan**: [Giới thiệu module](../README.md) · [Prompt nhận diện loại hiểu lầm](../prompts/02_misunderstanding_detector.md) · [Prompt phân loại và quy nguyên nhân](../prompts/01_classify_and_attribute.md) · [Case study flagship](../../../Examples/01_Patinete_Eletrico_500W/) · [Case study vòng khép kín](../../../Examples/03_Closed_Loop/) · [Case study chẩn đoán quảng cáo](../../06_Advertising_Optimization_Agent/examples/powerbank_20000mah_ads.md)
