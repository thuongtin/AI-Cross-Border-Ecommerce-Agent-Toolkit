#!/usr/bin/env python3
"""Script tính toán cho tầng ra quyết định quảng cáo (quảng cáo Shopee / Mercado Livre) — chỉ tính, không đoán, không thực thi.

  python ad_metrics.py calc --price 113.40 --product-cost 55 --commission 14 \
      --return 2 --tax 0 --target-acos 25 --cvr 0.44
  python ad_metrics.py diagnose --file ../examples/sample-ad-report.csv \
      --price 113.40 --product-cost 55 --commission 14 --return 2 --tax 0 --target-acos 25

Nguyên tắc thiết kế (giống module 01): cái gì tính được thì đừng để mô hình đoán.
  Script này chỉ xuất ra con số xác định và đề xuất hành động theo cấp (P0 cắt lỗ / P1 cải thiện / P2 scale),
  **không sửa trên trang quản trị, không thực thi** — việc thực thi do con người quyết định (yêu cầu tuân thủ và kiểm soát rủi ro).

Công thức ngưỡng hòa vốn (có tính thuế phí Brazil):
  Đóng góp trước quảng cáo = Giá bán − Giá vốn − Vận chuyển chặng đầu − Vận chuyển chặng cuối − Giá bán×Hoa hồng% − Giá bán×Hao hụt hoàn hàng% − Giá bán×Thuế suất%
  ACoS hòa vốn = Đóng góp trước quảng cáo ÷ Giá bán      ROAS hòa vốn = 1 ÷ ACoS hòa vốn
  CPC chịu được = Giá bán × Tỷ lệ chuyển đổi × ACoS mục tiêu
Cách tính thuế: hệ thống thuế Brazil phức tạp (ICMS/PIS/COFINS/Simples Nacional), ở đây gộp thành một tham số
  「thuế suất hiệu dụng tổng hợp」 (tính theo % giá bán), người dùng tự điền theo chế độ thuế của mình.
"""
import argparse
import csv
import json
import sys
from pathlib import Path

# Dùng chung bộ preset phí sàn với module 02 (nguồn sự thật duy nhất)
PLATFORM_FEES = (Path(__file__).resolve().parents[2]
                 / "02_Product_Strategy_Agent" / "scripts" / "platform_fees.json")


def _tier_lookup(price, tiers, default=0.0):
    for t in tiers or []:
        mx = t.get("max")
        if mx is None or price <= float(mx):
            return float(t.get("pct", t.get("fee", default)))
    return default


def _resolve_fees(args):
    """Xác định phí: tham số CLI tường minh > preset sàn (--platform) > 0."""
    preset = None
    if getattr(args, "platform", None):
        try:
            plats = json.loads(PLATFORM_FEES.read_text(encoding="utf-8"))
        except OSError:
            sys.exit(f"[ERROR] Không đọc được bảng phí sàn: {PLATFORM_FEES}")
        key = args.platform.strip()
        if key not in plats:
            matches = [k for k in plats
                       if not k.startswith("_") and (k == key or k.startswith(key + "_"))]
            if len(matches) == 1:
                key = matches[0]
            else:
                keys = ", ".join(k for k in plats if not k.startswith("_"))
                sys.exit(f"[INPUT_MISSING] Sàn không xác định {args.platform!r}. Có thể dùng: {keys}")
        preset = plats[key]

    price = args.price
    if args.commission is not None:
        comm = args.commission
    elif preset:
        if "commission_pct" in preset:
            comm = float(preset["commission_pct"])
        elif preset.get("commission_tiers"):
            comm = _tier_lookup(price, preset["commission_tiers"])
        else:
            comm = 0.0
    else:
        comm = 0.0

    def scalar(flag, pkey):
        if flag is not None:
            return float(flag)
        if preset and pkey in preset:
            return float(preset[pkey])
        return 0.0

    if getattr(args, "fixed_fee", None) is not None:
        ff = float(args.fixed_fee)
    elif preset and preset.get("fixed_fee_tiers"):
        ff = _tier_lookup(price, preset["fixed_fee_tiers"])
    else:
        ff = 0.0

    return comm, scalar(args.return_rate, "return_pct"), scalar(args.tax, "tax_pct"), \
        scalar(getattr(args, "extra_pct", None), "extra_pct"), ff, \
        (preset or {}).get("label", getattr(args, "platform", None) or "custom")
import sys

# Tự động ánh xạ tên cột (Trung / Việt / Anh / Bồ Đào Nha)
COLUMN_MAP = {
    "name":    ["广告名称", "广告组", "计划名称", "tên quảng cáo", "nhóm quảng cáo", "tên chiến dịch",
                "chiến dịch", "campaign", "name", "ad_group", "campanha"],
    "impressions": ["曝光量", "曝光", "展示量", "lượt hiển thị", "hiển thị", "impressions", "imps", "impressoes"],
    "clicks":  ["点击量", "点击数", "点击", "lượt click", "lượt nhấp", "số lượt click", "clicks", "cliques"],
    "spend":   ["花费", "消耗", "花费金额", "chi phí", "chi tiêu", "spend", "cost", "gasto"],
    "orders":  ["订单数", "订单", "成交订单", "số đơn", "đơn hàng", "lượt chuyển đổi", "orders", "conversions", "pedidos"],
    "gmv":     ["销售额", "成交金额", "广告销售额", "doanh thu", "doanh số", "gmv", "sales", "receita"],
}


def _num(v, default=0.0, kind="dec"):
    """Chấp nhận 'R$ 1.234,56' / '1,234' / '1.500' / '12.3%' / '-' / chuỗi rỗng.

    kind="int" (hiển thị/click/đơn): dấu chấm, dấu phẩy đều coi là phân cách hàng nghìn, chỉ giữ chữ số.
    kind="dec" (chi phí/doanh thu):
      có cả , và .  → dấu nằm bên phải là dấu thập phân;
      chỉ có một dấu → phần sau dấu ≤2 chữ số thì là thập phân, ngược lại là hàng nghìn (Brazil '1.500'=1500).
    """
    if v is None:
        return default
    s = str(v).strip().replace("R$", "").replace("%", "").replace(" ", "")
    if s in ("", "-", "—", "暂无", "N/A", "nan"):
        return default
    neg = s.startswith("-")
    s = s.lstrip("-")
    if kind == "int":
        digits = "".join(ch for ch in s if ch.isdigit())
        if not digits:
            return default
        return (-1 if neg else 1) * int(digits)
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".") if s.rfind(",") > s.rfind(".") \
            else s.replace(",", "")
    elif "," in s:
        head, _, tail = s.rpartition(",")
        s = f"{head}.{tail}" if len(tail) <= 2 else head + tail
    elif "." in s:
        head, _, tail = s.rpartition(".")
        s = s if len(tail) <= 2 else head + tail
    try:
        return (-1 if neg else 1) * float(s)
    except ValueError:
        return default


def _pick(header, kind):
    low = [h.strip().lower() for h in header]
    for cand in COLUMN_MAP[kind]:
        if cand.lower() in low:
            return header[low.index(cand.lower())]
    return None


def cost_model(args):
    price = args.price
    comm, ret, tax, extra, ff, plat_label = _resolve_fees(args)
    contrib = (price - args.product_cost - args.first_leg - args.shipping
               - price * (comm + ret + tax + extra) / 100 - ff)
    be_acos = contrib / price if price else 0
    return dict(price=price, platform=plat_label,
                commission_pct_applied=comm, fixed_fee_applied=round(ff, 2),
                extra_pct_applied=extra,
                pre_ad_contribution=round(contrib, 2),
                break_even_acos=round(be_acos, 4),
                break_even_roas=round(1 / be_acos, 2) if be_acos > 0 else None)


def cmd_calc(args):
    m = cost_model(args)
    out = dict(mode="calc", **m)
    if args.target_acos:
        ta = args.target_acos / 100
        out["target_acos"] = args.target_acos
        out["target_roas"] = round(1 / ta, 2)
        if args.cvr:
            out["affordable_cpc"] = round(m["price"] * (args.cvr / 100) * ta, 2)
            out["affordable_cpc_note"] = "Giá bán × Tỷ lệ chuyển đổi × ACoS mục tiêu — đặt giá thầu cao hơn mức này là lỗ càng nhanh"
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


def _grade(row, m, args, be_roas, target_roas):
    """Phân cấp xác định: P0 cắt lỗ / P1 cải thiện / P2 scale / INFO thiếu dữ liệu. Trả về (cấp, danh sách hành động)."""
    acts = []
    name = row["name"]
    imp, clk, spend, orders = row["impressions"], row["clicks"], row["spend"], row["orders"]
    gmv = row["gmv"] if row["gmv"] else orders * m["price"]
    ctr = clk / imp if imp else 0
    cvr = orders / clk if clk else 0
    cpc = spend / clk if clk else 0
    roas = gmv / spend if spend else None
    affordable_cpc = m["price"] * cvr * (args.target_acos / 100) if cvr else None

    # 0) Độ đủ dữ liệu — thiếu dữ liệu thì không động vào (gom thêm dữ liệu, ra tay quá sớm = chạy theo nhiễu)
    if imp < args.min_impressions:
        return "INFO", [f"Lượt hiển thị {imp:,.0f} < {args.min_impressions:,}, thiếu dữ liệu, vòng này không động vào, tiếp tục gom dữ liệu"], dict(
            ctr=ctr, cvr=cvr, cpc=cpc, roas=roas, affordable_cpc=affordable_cpc, gmv=gmv)
    if not spend:
        return "INFO", ["Không có chi phí, vòng này không động vào"], dict(ctr=ctr, cvr=cvr, cpc=cpc, roas=roas,
                                                affordable_cpc=affordable_cpc, gmv=gmv)

    # 1) Kiểm tra CTR (chuẩn 3–5%, <2% là thấp rõ ràng) — triệu chứng chỉ về creative, quay vòng về 04
    if ctr < 0.02:
        acts.append(f"CTR {ctr:.2%} dưới 2% — quay vòng về 04 để đổi ảnh chính/ảnh đầu (đừng xử lý vấn đề creative ở phía quảng cáo)")
    elif ctr < 0.03:
        acts.append(f"CTR {ctr:.2%} nằm trong vùng theo dõi 2–3%, tạm chưa động vào creative")

    # 2) Không có đơn (đủ click = creative ổn, vấn đề nằm ở trang đích/giá/đánh giá)
    if orders == 0 and clk >= 30:
        acts.append(f"{clk:,.0f} click mà 0 đơn — quay vòng về 03 kiểm tra trang chi tiết và dải giá, phía quảng cáo chỉ hạ giá thầu để cắt lỗ")
        acts.append(f"Hạ giá thầu xuống dưới CPC chịu được {affordable_cpc:.2f} (CPC hiện tại {cpc:.2f})")
        return "P0", acts, dict(ctr=ctr, cvr=cvr, cpc=cpc, roas=roas,
                                affordable_cpc=affordable_cpc, gmv=gmv)

    # 3) Phân cấp ROAS (neo theo ngưỡng hòa vốn, không neo theo cảm giác)
    if roas is None:
        return "INFO", ["Không có dữ liệu chi phí"], dict(ctr=ctr, cvr=cvr, cpc=cpc, roas=None,
                                            affordable_cpc=affordable_cpc, gmv=gmv)
    if roas < 0.5 * be_roas:
        acts.append(f"ROAS {roas:.2f} < một nửa ngưỡng hòa vốn ({be_roas:.2f}) — P0 cắt lỗ")
        acts.append(f"Hạ ngân sách về mức thấp nhất, hạ giá thầu xuống dưới {affordable_cpc:.2f} (CPC hiện tại {cpc:.2f})")
        acts.append("❗ Đừng tạm dừng quảng cáo — tạm dừng làm đứt tính liên tục và giảm điểm quảng cáo (nên hạ ngân sách, hạ giá thầu, xem actions.md)")
    elif roas < be_roas:
        acts.append(f"ROAS {roas:.2f} dưới ngưỡng hòa vốn {be_roas:.2f} — P1 cải thiện")
        acts.append(f"Hạ giá thầu xuống dưới {affordable_cpc:.2f} (CPC hiện tại {cpc:.2f}), tạm giữ nguyên ngân sách")
        if cvr < 0.01:
            acts.append(f"Tỷ lệ chuyển đổi {cvr:.2%} < 1% — nút thắt ở chuyển đổi chứ không ở traffic, quay vòng về 03/07, phía quảng cáo không đẩy thêm")
    elif roas < target_roas:
        acts.append(f"ROAS {roas:.2f} nằm giữa ngưỡng hòa vốn và mục tiêu {target_roas:.2f} — P1 giữ nguyên")
        acts.append("Giữ nguyên cả ngân sách lẫn giá thầu; cải thiện tỷ lệ chuyển đổi là đòn bẩy duy nhất")
    else:
        acts.append(f"ROAS {roas:.2f} ≥ mục tiêu {target_roas:.2f} — P2 scale")
        acts.append("Ngân sách +20~30% (mỗi lần chỉ tăng một nấc), theo dõi 3 ngày rồi mới quyết định nấc tiếp theo")

    # 4) Kỷ luật iterate: xuất danh sách 「vòng này dứt khoát không động vào」
    keep = "cấu trúc ngân sách và giá thầu, creative, nội dung Listing" if roas >= be_roas else "nội dung Listing và creative"
    acts.append(f"Vòng này dứt khoát không động vào: {keep} (mỗi lần chỉ sửa một nguyên nhân gốc)")
    return ("P0" if roas < 0.5 * be_roas else
            "P2" if roas >= target_roas else "P1"), acts, dict(
        ctr=ctr, cvr=cvr, cpc=cpc, roas=roas, affordable_cpc=affordable_cpc, gmv=gmv)


def cmd_diagnose(args):
    m = cost_model(args)
    be_roas = m["break_even_roas"]
    target_roas = 1 / (args.target_acos / 100) if args.target_acos else be_roas * 1.5

    try:
        with open(args.file, encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
    except OSError as e:
        sys.exit(f"[ERROR] Không đọc được file: {e}")
    if not rows:
        sys.exit("[ERROR] File CSV không có dòng dữ liệu nào")

    header = list(rows[0].keys())
    col = {k: _pick(header, k) for k in COLUMN_MAP}
    missing = [k for k, v in col.items() if v is None and k != "gmv"]
    if missing:
        sys.exit(f"[ERROR] Không nhận ra các cột sau (xem bảng ánh xạ trong references/metrics.md): {missing}")

    results, totals = [], dict(spend=0.0, gmv=0.0, orders=0.0, clicks=0.0, impressions=0.0)
    for r in rows:
        row = dict(name=(r.get(col["name"]) or "?").strip(),
                   impressions=_num(r.get(col["impressions"]), kind="int"),
                   clicks=_num(r.get(col["clicks"]), kind="int"),
                   spend=_num(r.get(col["spend"]), kind="dec"),
                   orders=_num(r.get(col["orders"]), kind="int"),
                   gmv=_num(r.get(col["gmv"]), kind="dec") if col["gmv"] else 0.0)
        grade, acts, met = _grade(row, m, args, be_roas, target_roas)
        results.append(dict(campaign=row["name"], grade=grade,
                            impressions=row["impressions"], clicks=row["clicks"],
                            spend=round(row["spend"], 2), orders=row["orders"],
                            **{k: (round(v, 4) if isinstance(v, float) else v) for k, v in met.items()},
                            actions=acts))
        for k in totals:
            totals[k] += row[k] if k != "gmv" else (row["gmv"] or row["orders"] * m["price"])

    total_roas = totals["gmv"] / totals["spend"] if totals["spend"] else None
    out = dict(mode="diagnose", cost_model=m, target_acos=args.target_acos,
               target_roas=target_roas, total=dict(
                   campaigns=len(results), **{k: round(v, 2) for k, v in totals.items()},
                   roas=round(total_roas, 2) if total_roas else None,
                   net_contribution=round(m["pre_ad_contribution"] / m["price"] * totals["gmv"] - totals["spend"], 2)),
               campaigns=sorted(results, key=lambda x: (x["grade"], -(x["roas"] or 0))))
    print(json.dumps(out, ensure_ascii=False, indent=2))

    if not args.json:
        icon = {"P0": "🔴", "P1": "🟡", "P2": "🟢", "INFO": "⚪"}
        print(f"\nROAS hòa vốn {be_roas} ｜ ROAS mục tiêu {target_roas} ｜ "
              f"ROAS tổng {out['total']['roas']} ｜ Đóng góp ròng tổng R$ {out['total']['net_contribution']}\n")
        for c in out["campaigns"]:
            print(f"{icon[c['grade']]} [{c['grade']}] {c['campaign']}  "
                  f"ROAS {c['roas'] if c['roas'] else '-'}  Chi phí R$ {c['spend']}  Đơn {c['orders']:g}")
            for a in c["actions"]:
                print(f"     · {a}")
            print()
    return 0


def main():
    ap = argparse.ArgumentParser(description="Script tính toán cho tầng ra quyết định quảng cáo (chỉ tính, không thực thi)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("calc", help="Tính ngưỡng hòa vốn / CPC chịu được từ cấu trúc chi phí")
    c.add_argument("--price", type=float, required=True, help="Giá bán R$")
    c.add_argument("--product-cost", type=float, required=True)
    c.add_argument("--shipping", type=float, default=0, help="Phí vận chuyển chặng cuối")
    c.add_argument("--first-leg", type=float, default=0, help="Phí vận chuyển chặng đầu")
    c.add_argument("--platform", help="Key preset phí sàn (dùng chung platform_fees.json với 02 sku_pricing)")
    c.add_argument("--commission", type=float, default=None, help="Hoa hồng sàn %% (ghi đè preset)")
    c.add_argument("--return", dest="return_rate", type=float, default=None, help="Hao hụt hoàn hàng %% (ghi đè preset)")
    c.add_argument("--tax", type=float, default=None, help="Thuế suất hiệu dụng tổng hợp %% (tự quy đổi theo chế độ thuế Brazil)")
    c.add_argument("--extra-pct", type=float, default=None, help="Phụ phí sàn %% (vd. chương trình Freeship; ghi đè preset)")
    c.add_argument("--fixed-fee", type=float, default=None, help="Phí cố định mỗi đơn vị R$ (ghi đè bậc phí của preset)")
    c.add_argument("--target-acos", type=float, help="ACoS mục tiêu %%")
    c.add_argument("--cvr", type=float, help="Tỷ lệ chuyển đổi %% (dùng để tính CPC chịu được)")

    d = sub.add_parser("diagnose", help="Đọc file CSV xuất từ quảng cáo → chỉ số + hành động phân cấp P0/P1/P2")
    d.add_argument("--file", required=True)
    d.add_argument("--price", type=float, required=True)
    d.add_argument("--product-cost", type=float, required=True)
    d.add_argument("--shipping", type=float, default=0)
    d.add_argument("--first-leg", type=float, default=0)
    d.add_argument("--platform", help="Key preset phí sàn (dùng chung platform_fees.json với 02 sku_pricing)")
    d.add_argument("--commission", type=float, default=None)
    d.add_argument("--return", dest="return_rate", type=float, default=None)
    d.add_argument("--tax", type=float, default=None)
    d.add_argument("--extra-pct", type=float, default=None)
    d.add_argument("--fixed-fee", type=float, default=None)
    d.add_argument("--target-acos", type=float, default=25)
    d.add_argument("--min-impressions", type=int, default=1000, help="Ngưỡng đủ dữ liệu")
    d.add_argument("--json", action="store_true")

    args = ap.parse_args()
    sys.exit(cmd_calc(args) if args.cmd == "calc" else cmd_diagnose(args))


if __name__ == "__main__":
    main()
