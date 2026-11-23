#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
market_metrics.py — Tầng tính chỉ số cho dữ liệu ngành hàng

Nguyên tắc thiết kế: **cái gì tính được thì đừng để model đoán.**
Mức độ tập trung, tỷ trọng, chia bin, bảng chéo đều là phép tính tất định, giao cho script;
Agent chỉ phụ trách diễn giải "những con số này nghĩa là gì, bước tiếp theo làm gì".

Phụ thuộc: chỉ thư viện chuẩn.

Cách dùng:
    python market_metrics.py <normalized.json> [--bins 10] [--top 10]
                             [--config-fields "công suất,tải trọng"] [--format md|json]
    python market_metrics.py data.normalized.json --config-fields "potencia,peso_max"
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
import unicodedata
from typing import Any

# ---------------------------------------------------------------------------
# Tiện ích
# ---------------------------------------------------------------------------
def _get(item: dict, key: str) -> Any:
    return item.get(key)


def _safe_div(a: float, b: float) -> float:
    return (a / b) if b else 0.0


def _fmt_money(v: float) -> str:
    return f"{v:,.2f}"


def _fmt_pct(v: float) -> str:
    return f"{v * 100:.1f}%"


# ---------------------------------------------------------------------------
# 1. Quy mô thị trường
# ---------------------------------------------------------------------------
def market_capacity(items: list[dict]) -> dict:
    prices = [i["price"] for i in items if i.get("price")]
    sales = [i["monthly_sales"] for i in items if i.get("monthly_sales") is not None]
    revs = [i["monthly_revenue"] for i in items if i.get("monthly_revenue")]

    total_sales = sum(sales)
    total_rev = sum(revs)
    return {
        "item_count": len(items),
        "total_monthly_sales": total_sales,
        "total_monthly_revenue": round(total_rev, 2),
        "avg_price": round(statistics.mean(prices), 2) if prices else 0,
        "median_price": round(statistics.median(prices), 2) if prices else 0,
        "price_min": round(min(prices), 2) if prices else 0,
        "price_max": round(max(prices), 2) if prices else 0,
        "avg_monthly_sales_per_item": round(_safe_div(total_sales, len(items)), 1),
        "implied_avg_price": round(_safe_div(total_rev, total_sales), 2),
        "rev_share_top10": 0.0,  # được điền lại từ concentration
    }


# ---------------------------------------------------------------------------
# 2. Mức độ tập trung (thương hiệu / người bán)
# ---------------------------------------------------------------------------
def _concentration(items: list[dict], key: str, top_n: int = 10) -> dict:
    """Gộp doanh thu và lượng bán theo key, tính CR-n và HHI."""
    agg: dict[str, dict[str, float]] = {}
    for i in items:
        name = (i.get(key) or "").strip() or "(chưa điền)"
        slot = agg.setdefault(name, {"revenue": 0.0, "sales": 0.0, "items": 0})
        slot["revenue"] += i.get("monthly_revenue") or 0.0
        slot["sales"] += i.get("monthly_sales") or 0.0
        slot["items"] += 1

    total_rev = sum(v["revenue"] for v in agg.values())
    total_sales = sum(v["sales"] for v in agg.values())
    total_items = sum(v["items"] for v in agg.values())

    ranked = sorted(agg.items(), key=lambda kv: -kv[1]["revenue"])
    cr = _safe_div(sum(v["revenue"] for _, v in ranked[:top_n]), total_rev)

    # HHI: tổng bình phương tỷ trọng doanh thu của từng chủ thể × 10000 (0–10000, càng cao càng tập trung)
    hhi = round(sum((_safe_div(v["revenue"], total_rev) ** 2) for _, v in ranked) * 10000, 1)

    # ⚠️ Khi số chủ thể ≤ top_n, CR-n luôn bằng 100%, không có giá trị tham khảo → đưa CR3 kèm cảnh báo rõ ràng
    cr_note = None
    cr3 = round(_safe_div(sum(v["revenue"] for _, v in ranked[:3]), total_rev), 4)
    if len(agg) <= top_n:
        cr_note = (
            f"Số chủ thể ({len(agg)}) ≤ n ({top_n}), CR{top_n} luôn bằng 100%, không có giá trị tham khảo. "
            f"Hãy dùng CR3 ({cr3 * 100:.1f}%) và HHI ({hhi}) để đánh giá mức độ tập trung."
        )

    top_list = [
        {
            "rank": idx + 1,
            "name": name,
            "revenue": round(v["revenue"], 2),
            "revenue_share": round(_safe_div(v["revenue"], total_rev), 4),
            "sales": int(v["sales"]),
            "sales_share": round(_safe_div(v["sales"], total_sales), 4),
            "item_count": int(v["items"]),
            "item_share": round(_safe_div(v["items"], total_items), 4),
        }
        for idx, (name, v) in enumerate(ranked[:top_n])
    ]

    return {
        "subject_count": len(agg),
        f"cr{top_n}": round(cr, 4),
        f"cr{top_n}_by_sales": round(
            _safe_div(sum(v["sales"] for _, v in ranked[:top_n]), total_sales), 4
        ),
        "cr3": cr3,
        "hhi": hhi,
        "cr_note": cr_note,
        "top_list": top_list,
    }


# ---------------------------------------------------------------------------
# 3. Chia bin dải giá + dò vùng trũng
# ---------------------------------------------------------------------------
def price_bands(items: list[dict], n_bins: int = 10, valley_min_drop: float = 0.15,
                max_bands: int = 5) -> dict:
    """
    SOP 1.4: trục hoành là khoảng giá, trục tung là lượng bán, chia dải giá từ vùng trũng đến vùng trũng.

    Cách làm: chia bin đều → thống kê lượng bán → dò cực tiểu cục bộ (vùng trũng) **trên đường cong gốc** → cắt dải giá theo vùng trũng.

    Hai tham số chính:
      valley_min_drop  mức giảm tối thiểu của vùng trũng so với hai bin bên cạnh, thấp hơn thì coi là nhiễu (mặc định 0.15 = 15%)
      max_bands        số dải giá tối đa được giữ, vượt quá thì lấy các vùng trũng sâu nhất (mặc định 5)

    Lưu ý: **luồng mặc định không làm mượt (smoothing)**. Trung bình trượt 3 điểm sẽ san phẳng các vùng trũng cục bộ dốc
    (ví dụ vùng trũng 799 → 618 → 1120 sẽ bị trung bình hóa mất), khiến bỏ sót ranh giới dải giá thật.
    Cần làm mượt thì dùng --smooth.
    """
    pts = [(i["price"], i.get("monthly_sales") or 0, i.get("monthly_revenue") or 0)
           for i in items if i.get("price")]
    if not pts:
        return {"bins": [], "valleys": [], "suggested_bands": []}

    prices = sorted(p for p, _, _ in pts)
    lo, hi = prices[0], prices[-1]
    if hi <= lo:
        return {"bins": [], "valleys": [], "suggested_bands": [], "note": "Giá không có chênh lệch, không chia bin được"}

    width = (hi - lo) / n_bins
    bins = []
    for k in range(n_bins):
        b_lo = lo + k * width
        b_hi = b_lo + width if k < n_bins - 1 else hi + 1e-9
        sel = [(p, s, r) for p, s, r in pts if b_lo <= p < b_hi]
        bins.append({
            "index": k + 1,
            "price_lo": round(b_lo, 2),
            "price_hi": round(b_hi, 2),
            "item_count": len(sel),
            "total_sales": int(sum(s for _, s, _ in sel)),
            "total_revenue": round(sum(r for _, _, r in sel), 2),
            "avg_sales_per_item": round(_safe_div(sum(s for _, s, _ in sel), len(sel)), 1),
        })

    raw = [b["total_sales"] for b in bins]

    # Dò vùng trũng: cực tiểu cục bộ + lọc theo mức giảm tương đối có ý nghĩa
    candidates = []
    for i in range(1, len(raw) - 1):
        if raw[i] < raw[i - 1] and raw[i] < raw[i + 1]:
            drops = []
            if raw[i - 1]:
                drops.append((raw[i - 1] - raw[i]) / raw[i - 1])
            if raw[i + 1]:
                drops.append((raw[i + 1] - raw[i]) / raw[i + 1])
            drop = min(drops) if drops else 0.0
            # Khi bin bên phải là bin đầu tiên của xu hướng tăng, mức giảm bên phải tự nhiên rất lớn → dùng mức giảm bên trái làm tiêu chí chính
            candidates.append({"bin_index": i + 1, "price": round(bins[i]["price_hi"], 2),
                               "drop": round(drop, 4)})

    significant = [c for c in candidates if c["drop"] >= valley_min_drop]
    noise_count = len(candidates) - len(significant)

    # Khi có quá nhiều vùng trũng, lấy (max_bands - 1) vùng sâu nhất theo mức giảm
    trimmed = []
    if len(significant) > max_bands - 1:
        ordered = sorted(significant, key=lambda c: -c["drop"])
        keep = {c["bin_index"] for c in ordered[: max_bands - 1]}
        trimmed = [c for c in significant if c["bin_index"] not in keep]
        significant = [c for c in significant if c["bin_index"] in keep]

    significant.sort(key=lambda c: c["bin_index"])

    boundaries = [lo] + [v["price"] for v in significant] + [hi]
    bands = []
    for k in range(len(boundaries) - 1):
        a, b = boundaries[k], boundaries[k + 1]
        sel = [(p, s, r) for p, s, r in pts if a <= p <= b]
        bands.append({
            "band_index": k + 1,
            "price_from": round(a, 2),
            "price_to": round(b, 2),
            "item_count": len(sel),
            "total_sales": int(sum(s for _, s, _ in sel)),
            "total_revenue": round(sum(r for _, _, r in sel), 2),
            "avg_sales_per_item": round(_safe_div(sum(s for _, s, _ in sel), len(sel)), 1),
        })

    return {
        "price_range": [round(lo, 2), round(hi, 2)],
        "bin_width": round(width, 2),
        "bins": bins,
        "valleys": significant,
        "noise_valleys": noise_count,
        "trimmed_valleys": trimmed,
        "valley_min_drop": valley_min_drop,
        "suggested_bands": bands,
    }


# ---------------------------------------------------------------------------
# 4. Bảng chéo tổ hợp cấu hình
# ---------------------------------------------------------------------------
def _extract_dim(item: dict, field: str) -> str | None:
    """Trích giá trị cấu hình từ trường hoặc title. Trường không tồn tại thì thử trích từ tiêu đề bằng regex."""
    if item.get(field):
        return str(item[field]).strip()

    title = item.get("title") or ""
    # Số + đơn vị thường gặp (tên chiều hỗ trợ tiếng Trung / tiếng Việt / tiếng Anh / tiếng Bồ Đào Nha)
    if re.search(r"(?i)(power|watt|potência|potencia|công suất|cong suat)", field) or field == "功率":
        m = re.search(r"(\d{2,4})\s*(?:w|W|瓦)", title)
        if m:
            return f"{m.group(1)}W"
    if re.search(r"(?i)(weight|peso|承重|carga|tải trọng|tai trong)", field) or field == "承重":
        m = re.search(r"(\d{2,3})\s*(?:kg|KG|公斤)", title)
        if m:
            return f"{m.group(1)}kg"
    if re.search(r"(?i)(capacit|容量|dung lượng|dung luong|ah|mah|litro|L\b)", field) or field == "容量":
        m = re.search(r"(\d+(?:[.,]\d+)?)\s*(?:mah|mAh|Ah|ah|L|L\b|litros)", title)
        if m:
            return m.group(0)
    return None


def config_matrix(items: list[dict], fields: list[str]) -> dict:
    """
    SOP 1.5: với mỗi chiều cấu hình, thống kê "số sản phẩm / tỷ trọng số lượng / lượng bán trung bình / tổng lượng bán"
    và đưa ra đánh giá bốn chiều:
      - Tổng lượng bán cao → nhu cầu lớn
      - Lượng bán trung bình cao → hiệu suất mỗi SKU cao
      - Tỷ trọng số lượng cao → cấu hình phổ biến (nhưng cạnh tranh có thể gắt hơn)
      - Số lượng ít nhưng lượng bán trung bình cao → cấu hình cơ hội tiềm năng
    """
    out: dict[str, Any] = {}
    total_items = len(items)

    for field in fields:
        agg: dict[str, dict[str, float]] = {}
        unparsed = 0
        for i in items:
            val = _extract_dim(i, field)
            if not val:
                unparsed += 1
                continue
            slot = agg.setdefault(val, {"items": 0, "sales": 0.0, "revenue": 0.0})
            slot["items"] += 1
            slot["sales"] += i.get("monthly_sales") or 0
            slot["revenue"] += i.get("monthly_revenue") or 0

        if not agg:
            out[field] = {"error": "Không trích được giá trị nào cho chiều này. Hãy để cấu hình ở cột riêng, hoặc chỉ định bằng --mapping.",
                          "unparsed": unparsed}
            continue

        total_sales = sum(v["sales"] for v in agg.values())
        rows = []
        for val, v in agg.items():
            rows.append({
                "value": val,
                "item_count": int(v["items"]),
                "item_share": round(_safe_div(v["items"], total_items), 4),
                "total_sales": int(v["sales"]),
                "sales_share": round(_safe_div(v["sales"], total_sales), 4),
                "avg_sales": round(_safe_div(v["sales"], v["items"]), 1),
            })
        rows.sort(key=lambda r: -r["total_sales"])

        n_values = len(rows)
        avg_sales_all = _safe_div(total_sales, sum(r["item_count"] for r in rows))
        # Mốc chia đều: nếu một giá trị chiếm 1/n, nghĩa là các giá trị "ngang ngửa nhau"
        equal_share = 1.0 / n_values if n_values else 1.0

        for r in rows:
            flags = []
            # ① Tổng lượng bán cao → nhu cầu thị trường lớn
            if r["sales_share"] >= 0.30:
                flags.append("Tổng lượng bán cao→nhu cầu lớn")
            # ② Hiệu suất mỗi SKU cao: lượng bán trung bình cao hơn hẳn mức chung
            if avg_sales_all and r["avg_sales"] > avg_sales_all * 1.2:
                flags.append("Hiệu suất mỗi SKU cao")
            # ③ Cấu hình phổ biến: tỷ trọng số lượng cao hơn hẳn mức chia đều (→ cạnh tranh gắt hơn)
            if r["item_share"] >= equal_share * 1.5:
                flags.append("Cấu hình phổ biến→cạnh tranh gắt")
            # ④ Cấu hình cơ hội tiềm năng: tỷ trọng số lượng thấp hơn hẳn mức chia đều, nhưng hiệu suất mỗi SKU cao
            if r["item_share"] <= equal_share * 0.6 and avg_sales_all \
                    and r["avg_sales"] > avg_sales_all * 1.2:
                flags.append("★Cấu hình cơ hội (ít sản phẩm nhưng hiệu suất cao)")
            # ⑤ Thị trường lớn nhưng cạnh tranh gắt: tổng lượng bán cao mà hiệu suất mỗi SKU thấp
            if r["sales_share"] >= 0.30 and avg_sales_all and r["avg_sales"] < avg_sales_all:
                flags.append("Thị trường lớn nhưng cạnh tranh gắt")
            r["judgement"] = flags or ["Bình thường"]

        out[field] = {
            "value_count": n_values,
            "unparsed_items": unparsed,
            "avg_sales_all_values": round(avg_sales_all, 1),
            "equal_share_reference": round(equal_share, 4),
            "rows": rows,
        }

    return out


# ---------------------------------------------------------------------------
# Render báo cáo
# ---------------------------------------------------------------------------
def render_md(payload: dict) -> str:
    cap = payload["market_capacity"]
    L: list[str] = []
    L.append("# Báo cáo chỉ số ngành hàng\n")
    L.append(f"Nguồn dữ liệu: `{payload['meta'].get('source_file', '—')}` · "
             f"Cỡ mẫu: {cap['item_count']} sản phẩm\n")

    L.append("## 1. Quy mô thị trường\n")
    L.append("| Chỉ số | Giá trị |")
    L.append("|---|---|")
    L.append(f"| Số sản phẩm trong mẫu | {cap['item_count']} |")
    L.append(f"| Tổng lượng bán tháng | {cap['total_monthly_sales']:,} |")
    L.append(f"| Tổng doanh thu tháng | R$ {_fmt_money(cap['total_monthly_revenue'])} |")
    L.append(f"| Giá trung bình | R$ {_fmt_money(cap['avg_price'])} |")
    L.append(f"| Giá trung vị | R$ {_fmt_money(cap['median_price'])} |")
    L.append(f"| Khoảng giá | R$ {_fmt_money(cap['price_min'])} – R$ {_fmt_money(cap['price_max'])} |")
    L.append(f"| Lượng bán tháng trung bình mỗi sản phẩm | {cap['avg_monthly_sales_per_item']} |")
    L.append(f"| Giá trung bình ngầm định (GMV÷lượng bán) | R$ {_fmt_money(cap['implied_avg_price'])} |")
    L.append(f"| Tỷ trọng doanh thu của top 10 | {_fmt_pct(cap.get('rev_share_top10', 0))} |")
    L.append("")

    br = payload.get("brand_concentration")
    if br:
        L.append("## 2. Mức độ tập trung thương hiệu\n")
        L.append(f"- Số thương hiệu: **{br['subject_count']}**")
        L.append(f"- **CR3 (doanh thu): {_fmt_pct(br['cr3'])}** · CR10: {_fmt_pct(br['cr10'])}"
                 f" · CR10 theo lượng bán: {_fmt_pct(br['cr10_by_sales'])}")
        L.append(f"- HHI: **{br['hhi']}** (0–10000, càng cao càng tập trung)")
        if br.get("cr_note"):
            L.append(f"\n> ⚠️ {br['cr_note']}")
        L.append("")
        L.append("| # | Thương hiệu | Doanh thu | Tỷ trọng doanh thu | Tỷ trọng lượng bán | Số sản phẩm |")
        L.append("|---|---|---|---|---|---|")
        for r in br["top_list"][:10]:
            L.append(f"| {r['rank']} | {r['name']} | R$ {_fmt_money(r['revenue'])} | "
                     f"{_fmt_pct(r['revenue_share'])} | {_fmt_pct(r['sales_share'])} | {r['item_count']} |")
        L.append("")
        L.append("> **Đánh giá** (SOP 1.3): mức độ tập trung thương hiệu < 50% → hàng no-brand vẫn còn cơ hội; > 50% → thương hiệu top đầu chi phối mạnh, cần thận trọng.\n")

    sl = payload.get("seller_concentration")
    if sl:
        L.append("## 3. Mức độ tập trung người bán\n")
        L.append(f"- Số người bán: **{sl['subject_count']}**")
        L.append(f"- **CR3 (doanh thu): {_fmt_pct(sl['cr3'])}** · "
                 f"**CR10 (doanh thu): {_fmt_pct(sl['cr10'])}** · CR10 theo lượng bán: {_fmt_pct(sl['cr10_by_sales'])}")
        L.append(f"- HHI: **{sl['hhi']}**")
        if sl.get("cr_note"):
            L.append(f"\n> ⚠️ {sl['cr_note']}")
        L.append("")
        L.append("| # | Người bán | Tỷ trọng doanh thu | Tỷ trọng lượng bán | Số sản phẩm |")
        L.append("|---|---|---|---|---|")
        for r in sl["top_list"][:10]:
            L.append(f"| {r['rank']} | {r['name']} | {_fmt_pct(r['revenue_share'])} | "
                     f"{_fmt_pct(r['sales_share'])} | {r['item_count']} |")
        L.append("")

    pb = payload.get("price_bands")
    if pb and pb.get("bins"):
        L.append("## 4. Phân tích dải giá\n")
        L.append(f"- Khoảng giá: R$ {_fmt_money(pb['price_range'][0])} – R$ {_fmt_money(pb['price_range'][1])}"
                 f" · Độ rộng bin: R$ {_fmt_money(pb['bin_width'])}")
        L.append("")
        L.append("### 4.1 Chia bin đều (đường cong lượng bán)\n")
        L.append("| Bin | Khoảng giá | Số sản phẩm | Tổng lượng bán | Đường cong | Tổng doanh thu | Lượng bán TB/sản phẩm |")
        L.append("|---|---|---|---|---|---|---|")
        peak = max((b["total_sales"] for b in pb["bins"]), default=0)
        for b in pb["bins"]:
            bar = "█" * int(_safe_div(b["total_sales"], peak) * 20) if peak else ""
            L.append(f"| {b['index']} | R$ {_fmt_money(b['price_lo'])}–{_fmt_money(b['price_hi'])} | "
                     f"{b['item_count']} | {b['total_sales']:,} | {bar} | "
                     f"R$ {_fmt_money(b['total_revenue'])} | {b['avg_sales_per_item']} |")
        L.append("")
        L.append("### 4.2 Dò vùng trũng\n")
        if pb.get("valleys"):
            L.append(f"Ngưỡng xác định: mức giảm tối thiểu của vùng trũng so với hai bin bên cạnh **≥ {_fmt_pct(pb.get('valley_min_drop', 0))}**"
                     f" (thấp hơn thì coi là nhiễu)\n")
            L.append("| Bin số | Ranh giới giá | Mức giảm | Dùng làm ranh giới dải giá |")
            L.append("|---|---|---|---|")
            for v in pb["valleys"]:
                L.append(f"| {v['bin_index']} | R$ {_fmt_money(v['price'])} | {_fmt_pct(v['drop'])} | ✅ |")
            L.append("")
            if pb.get("noise_valleys"):
                L.append(f"> Ngoài ra có {pb['noise_valleys']} vùng trũng ứng viên có mức giảm dưới ngưỡng đã bị lọc như nhiễu.\n")
            if pb.get("trimmed_valleys"):
                names = ", ".join(f"bin {v['bin_index']} (R$ {_fmt_money(v['price'])})"
                                for v in pb["trimmed_valleys"])
                L.append(f"> Bị cắt bỏ do vượt số dải giá tối đa ({pb.get('max_bands', 5)}): {names}. "
                         f"Muốn giữ lại thì tăng `--max-bands`.\n")
        else:
            L.append("Không phát hiện vùng trũng đáng kể. Nguyên nhân có thể: cỡ mẫu nhỏ (nên ≥ 50), "
                     "phân bố giá quá liên tục, hoặc đường cong lượng bán đơn điệu.\n")
        if pb.get("suggested_bands"):
            L.append("### 4.3 Dải giá đề xuất (cắt theo vùng trũng)\n")
            L.append("| Dải giá | Khoảng giá | Số sản phẩm | Tổng lượng bán | Tổng doanh thu | Lượng bán TB/sản phẩm |")
            L.append("|---|---|---|---|---|---|")
            for b in pb["suggested_bands"]:
                L.append(f"| #{b['band_index']} | R$ {_fmt_money(b['price_from'])}–{_fmt_money(b['price_to'])} | "
                         f"{b['item_count']} | {b['total_sales']:,} | "
                         f"R$ {_fmt_money(b['total_revenue'])} | {b['avg_sales_per_item']} |")
            L.append("")
            L.append("> ⚠️ Cắt theo vùng trũng chỉ là **gợi ý toán học**. SOP 1.4 yêu cầu kết luận cuối cùng phải xét thêm: "
                     "sản phẩm của công ty có lãi không, đối thủ có quá mạnh không. Bước này do Agent làm dựa trên cấu trúc chi phí.\n")

    cm = payload.get("config_matrix")
    if cm:
        L.append("## 5. Bảng chéo tổ hợp cấu hình\n")
        for field, data in cm.items():
            L.append(f"### Chiều: {field}\n")
            if "error" in data:
                L.append(f"⚠️ {data['error']}\n")
                continue
            L.append(f"- Số giá trị: {data['value_count']} · Lượng bán TB mỗi SKU toàn bộ: {data['avg_sales_all_values']}"
                     f" · Mốc chia đều (1/n): {_fmt_pct(data.get('equal_share_reference', 0))}")
            if data.get("unparsed_items"):
                L.append(f"- ⚠️ Số sản phẩm không trích được chiều này: {data['unparsed_items']}")
            L.append("")
            L.append("| Giá trị cấu hình | Số sản phẩm | Tỷ trọng số lượng | Tổng lượng bán | Tỷ trọng lượng bán | Lượng bán TB | Đánh giá |")
            L.append("|---|---|---|---|---|---|---|")
            for r in data["rows"]:
                L.append(f"| {r['value']} | {r['item_count']} | {_fmt_pct(r['item_share'])} | "
                         f"{r['total_sales']:,} | {_fmt_pct(r['sales_share'])} | {r['avg_sales']} | "
                         f"{'; '.join(r['judgement'])} |")
            L.append("")
        L.append("> **Quy tắc đánh giá** (SOP 1.5): tổng lượng bán cao = nhu cầu lớn (tỷ trọng lượng bán ≥30%); "
                 "lượng bán TB cao = hiệu suất mỗi SKU cao (gấp trên 1.2 lần mức TB chung); "
                 "tỷ trọng số lượng cao = phổ biến nhưng cạnh tranh gắt (gấp trên 1.5 lần mức chia đều); "
                 "**ít sản phẩm nhưng lượng bán TB cao = cấu hình cơ hội tiềm năng** (dưới 0.6 lần mức chia đều và hiệu suất cao, cần xác nhận thêm có bị nhóm top đầu chiếm không); "
                 "tổng lượng bán cao nhưng lượng bán TB thấp = thị trường lớn nhưng cạnh tranh gắt.\n")

    return "\n".join(L)


# ---------------------------------------------------------------------------
def main() -> None:
    ap = argparse.ArgumentParser(description="Tính chỉ số ngành hàng (mức độ tập trung / dải giá / bảng chéo cấu hình)")
    ap.add_argument("input", help="File normalized.json do shaduola_parser.py tạo ra")
    ap.add_argument("--bins", type=int, default=10, help="Số bin chia giá (mặc định 10)")
    ap.add_argument("--top", type=int, default=10, help="n của CR-n và độ dài bảng Top (mặc định 10)")
    ap.add_argument("--config-fields", default="", help="Các trường chiều cấu hình, phân tách bằng dấu phẩy, ví dụ \"công suất,tải trọng\"")
    ap.add_argument("--valley-min-drop", type=float, default=0.15,
                    help="Mức giảm tối thiểu của vùng trũng so với hai bin bên cạnh, thấp hơn thì coi là nhiễu (mặc định 0.15)")
    ap.add_argument("--max-bands", type=int, default=5, help="Số dải giá tối đa được giữ (mặc định 5)")
    ap.add_argument("--brand-field", default="brand", help="Tên trường thương hiệu (mặc định brand)")
    ap.add_argument("--seller-field", default="seller", help="Tên trường người bán (mặc định seller)")
    ap.add_argument("--format", choices=["md", "json", "both"], default="both", help="Định dạng đầu ra (mặc định both)")
    ap.add_argument("-o", "--output", help="Tiền tố file đầu ra (mặc định <tên_đầu_vào>.metrics)")
    args = ap.parse_args()

    with open(args.input, encoding="utf-8") as f:
        data = json.load(f)
    items = data.get("items", [])
    if not items:
        sys.exit("[ERROR] JSON đầu vào không có items. Hãy chuyển đổi bằng shaduola_parser.py trước.")

    cap = market_capacity(items)
    brand = _concentration(items, args.brand_field, args.top)
    seller = _concentration(items, args.seller_field, args.top)
    cap["rev_share_top10"] = seller[f"cr{args.top}"]

    pb = price_bands(items, args.bins, args.valley_min_drop, args.max_bands)
    pb["max_bands"] = args.max_bands

    payload: dict[str, Any] = {
        "meta": data.get("meta", {}),
        "market_capacity": cap,
        "brand_concentration": brand,
        "seller_concentration": seller,
        "price_bands": pb,
    }

    fields = [unicodedata.normalize("NFC", f.strip()) for f in args.config_fields.split(",") if f.strip()]
    if fields:
        payload["config_matrix"] = config_matrix(items, fields)

    prefix = args.output or (args.input.rsplit(".", 1)[0] + ".metrics")
    if args.format in ("json", "both"):
        with open(prefix + ".json", "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        print(f"✅ JSON → {prefix}.json")
    if args.format in ("md", "both"):
        md = render_md(payload)
        with open(prefix + ".md", "w", encoding="utf-8") as f:
            f.write(md)
        print(f"✅ Markdown → {prefix}.md")
        print()
        print(md)

    print("\n" + "=" * 60)
    print("Đầu vào cho Agent: gửi báo cáo chỉ số ở trên (JSON hoặc MD) kèm "
          "templates/input_category_research.md.")
    print("Agent chỉ diễn giải, không tính lại. Nếu nghi ngờ con số, quay lại chỉnh tham số script.")


if __name__ == "__main__":
    main()
