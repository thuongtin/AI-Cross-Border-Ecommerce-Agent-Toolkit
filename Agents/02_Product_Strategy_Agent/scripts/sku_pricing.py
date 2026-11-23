#!/usr/bin/env python3
"""Script tính toán định giá SKU —— chỉ tính, không đoán, không tự định giá (quyết định định giá do người làm).

  # Preset theo sàn (khuyên dùng): mức phí lấy từ scripts/platform_fees.json
  python sku_pricing.py calc --platform shopee_br --cost 935 --price 2199
  python sku_pricing.py calc --platform mercadolivre_br --cost 935 --price 2199
  python sku_pricing.py calc --platform amazon_br --cost 935 --price 2199
  python sku_pricing.py calc --platform tiktok_br --cost 935 --price 2199
  python sku_pricing.py --list-platforms

  # Nhập tay (tương thích cách dùng cũ, mức phí tự đặt tương đương preset)
  python sku_pricing.py calc --cost 935 --price 2199 --commission 14 --return 2 \
      --ad 5 --tax 0 --target-margin 32
  python sku_pricing.py matrix --file examples/sample-skus.csv --platform shopee_br

Công thức (có các khoản thuế Brazil và phí cố định mỗi sản phẩm của sàn):
  Lợi nhuận gộp trước QC = giá bán − giá vốn về kho − giá bán×(%hoa hồng+%hoàn hàng+%thuế+%phụ phí sàn) − phí cố định mỗi sản phẩm
  Biên lợi nhuận ròng    = (lợi nhuận gộp trước QC − giá bán×%quảng cáo) ÷ giá bán
  Giá hòa vốn / giá mục tiêu: khi mức phí chia bậc theo giá thì giải bằng lặp điểm bất động (hội tụ sau 12 vòng)
"""
import argparse
import csv
import json
import sys
from pathlib import Path

PLATFORMS_FILE = Path(__file__).with_name("platform_fees.json")

# Mặc định cũ dùng khi không chỉ định --platform (= hành vi bản cũ, fixed fee bằng 0)
LEGACY = dict(commission=14.0, return_rate=2.0, ad=5.0, tax=0.0,
              extra_pct=0.0, target_margin=32.0)


def load_platforms() -> dict:
    try:
        with open(PLATFORMS_FILE, encoding="utf-8") as f:
            return json.load(f)
    except OSError as e:
        sys.exit(f"[ERROR] Không đọc được bảng phí sàn {PLATFORMS_FILE.name}: {e}")


def _tier_lookup(price: float, tiers: list, default: float) -> float:
    """tiers: [{"max": 79.99, "fee"/"pct": v}, ..., {"max": null, ...}], lấy bậc đầu tiên khớp theo thứ tự."""
    for t in tiers or []:
        mx = t.get("max")
        if mx is None or price <= float(mx):
            v = t.get("pct", t.get("fee", default))
            return float(v)
    return default


class FeeModel:
    """Mô hình phí: tham số CLI truyền rõ > preset theo sàn > mặc định cũ. Hoa hồng/phí cố định có thể chia bậc theo giá."""

    def __init__(self, preset: dict | None = None, *, commission=None,
                 return_rate=None, ad=None, tax=None, target_margin=None,
                 extra_pct=None, fixed_fee=None):
        self.p = preset or {}
        self.o = dict(commission=commission, return_rate=return_rate, ad=ad,
                      tax=tax, target_margin=target_margin,
                      extra_pct=extra_pct, fixed_fee=fixed_fee)

    def _scalar(self, key: str, preset_key: str) -> float:
        if self.o[key] is not None:
            return float(self.o[key])
        if preset_key in self.p:
            return float(self.p[preset_key])
        return LEGACY[key]

    def commission_pct(self, price: float) -> float:
        if self.o["commission"] is not None:
            return float(self.o["commission"])
        if self.p.get("commission_tiers"):
            return _tier_lookup(price, self.p["commission_tiers"],
                                self.p.get("commission_pct", LEGACY["commission"]))
        return float(self.p.get("commission_pct", LEGACY["commission"]))

    def fixed_fee(self, price: float) -> float:
        if self.o["fixed_fee"] is not None:
            return float(self.o["fixed_fee"])
        if self.p.get("fixed_fee_tiers"):
            return _tier_lookup(price, self.p["fixed_fee_tiers"], 0.0)
        return 0.0

    def return_pct(self) -> float: return self._scalar("return_rate", "return_pct")
    def tax_pct(self) -> float:    return self._scalar("tax", "tax_pct")
    def extra_pct(self) -> float:  return self._scalar("extra_pct", "extra_pct")
    def ad_pct(self) -> float:     return self._scalar("ad", "ad_pct")
    def target_margin(self) -> float: return self._scalar("target_margin", "target_margin_pct")

    def margin(self, price: float, cost: float, ad_pct: float | None = None) -> dict:
        ad = self.ad_pct() if ad_pct is None else ad_pct
        cp = self.commission_pct(price)
        ff = self.fixed_fee(price)
        pct = cp + self.return_pct() + self.tax_pct() + self.extra_pct()
        pre = price - cost - price * pct / 100 - ff
        net = pre - price * ad / 100
        return dict(pre_ad_margin=round(pre, 2),
                    pre_ad_rate=round(pre / price, 4) if price else 0,
                    net_margin=round(net, 2),
                    net_rate=round(net / price, 4) if price else 0,
                    commission_pct_applied=cp,
                    fixed_fee_applied=round(ff, 2))

    def _solve(self, cost: float, ad_pct: float, tm_pct: float) -> float | None:
        """Giá hòa vốn/giá mục tiêu: p = (cost + fixed_fee(p)) / (1 − Σpct(p)/100), lặp điểm bất động."""
        p = max(cost, 1.0)
        for _ in range(12):
            pct = (self.commission_pct(p) + self.return_pct() + self.tax_pct()
                   + self.extra_pct() + ad_pct + tm_pct) / 100
            denom = 1 - pct
            if denom <= 0:
                return None
            p = (cost + self.fixed_fee(p)) / denom
        return round(p, 2)

    def break_even_price(self, cost: float) -> float | None:
        return self._solve(cost, 0.0, 0.0)

    def target_price(self, cost: float) -> float | None:
        return self._solve(cost, self.ad_pct(), self.target_margin())


def _model_from_args(args, plats: dict) -> FeeModel:
    preset = None
    if getattr(args, "platform", None):
        key = args.platform.strip()
        if key not in plats:
            # Cho phép bỏ hậu tố khu vực (vd. --platform mercadolivre → mercadolivre_br)
            matches = [k for k in plats
                       if not k.startswith("_") and (k == key or k.startswith(key + "_"))]
            if len(matches) == 1:
                key = matches[0]
            else:
                keys = ", ".join(k for k in plats if not k.startswith("_"))
                hint = f" ({key!r} khớp nhiều preset: {', '.join(matches)}, hãy ghi tên đầy đủ)" \
                       if len(matches) > 1 else ""
                sys.exit(f"[INPUT_MISSING] Không rõ sàn {args.platform!r}. Có sẵn: {keys}{hint}")
        preset = plats[key]
    return FeeModel(preset,
                    commission=getattr(args, "commission", None),
                    return_rate=getattr(args, "return_rate", None),
                    ad=getattr(args, "ad", None),
                    tax=getattr(args, "tax", None),
                    target_margin=getattr(args, "target_margin", None),
                    extra_pct=getattr(args, "extra_pct", None),
                    fixed_fee=getattr(args, "fixed_fee", None))


def cmd_calc(args, plats) -> int:
    fm = _model_from_args(args, plats)
    m = fm.margin(args.price, args.cost)
    be = fm.break_even_price(args.cost)
    tp = fm.target_price(args.cost)
    tm = fm.target_margin() / 100
    out = dict(mode="calc", platform=getattr(args, "platform", None) or "custom",
               price=args.price, cost=args.cost, **m,
               extra_pct_applied=fm.extra_pct(),
               break_even_price=be, target_price=tp,
               target_margin=fm.target_margin(),
               coupon_headroom=round((m["net_rate"] - tm) * args.price, 2)
               if m["net_rate"] > tm else 0,
               break_even_roas=round(args.price / m["pre_ad_margin"], 2)
               if m["pre_ad_margin"] > 0 else None)
    if fm.ad_pct() > 0 and m["pre_ad_margin"] > 0:
        out["break_even_roas_at_this_ad"] = round(
            args.price / (args.price * fm.ad_pct() / 100), 2)
    # Phí tháng của sàn/chi phí cố định khác chỉ để nhắc (không phân bổ vào từng sản phẩm)
    if fm.p.get("monthly_fee"):
        out["platform_monthly_fee"] = fm.p["monthly_fee"]
    print(json.dumps(out, ensure_ascii=False, indent=2))
    if not getattr(args, "json", False):
        print(f"\nSàn: {out['platform']} | Hoa hồng {m['commission_pct_applied']}% | "
              f"Phí cố định R$ {m['fixed_fee_applied']:.2f} | Phụ phí sàn {fm.extra_pct()}% | "
              f"Hoàn hàng {fm.return_pct()}% | Thuế {fm.tax_pct()}% | Quảng cáo {fm.ad_pct()}%")
        print(f"Biên LN ròng {m['net_rate']:.1%} | Giá hòa vốn R$ {be:,.2f} | "
              f"Giá mục tiêu R$ {tp:,.2f} | Dư địa voucher R$ {out['coupon_headroom']:,.2f}")
        for note in fm.p.get("notes", [])[:3]:
            print(f"  ℹ️  {note}")
    return 0


def cmd_matrix(args, plats) -> int:
    try:
        with open(args.file, encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
    except OSError as e:
        sys.exit(f"[ERROR] Không đọc được file: {e}")
    if not rows:
        sys.exit("[ERROR] CSV không có dòng dữ liệu nào")
    header = list(rows[0].keys())
    low = [h.strip().lower() for h in header]

    def col(*cands):
        for c in cands:
            if c in low:
                return header[low.index(c)]
        return None

    c_name = col("角色", "名称", "vai trò", "tên", "sku", "role", "name") or header[0]
    c_price = col("售价", "价格", "giá bán", "giá", "price")
    c_cost = col("到岸成本", "成本", "giá vốn về kho", "giá vốn", "landed cost", "cost")
    if not c_price or not c_cost:
        sys.exit(f"[ERROR] Không nhận ra cột giá bán/giá vốn (header: {header})")

    fm = _model_from_args(args, plats)
    tm = fm.target_margin() / 100
    results = []
    for r in rows:
        name = (r.get(c_name) or "?").strip()
        price = _num(r.get(c_price), kind="dec")
        cost = _num(r.get(c_cost), kind="dec")
        if price <= 0 or cost <= 0:
            results.append(dict(sku=name, error="Giá bán hoặc giá vốn không dương, bỏ qua"))
            continue
        m = fm.margin(price, cost)
        headroom = round((m["net_rate"] - tm) * price, 2)
        results.append(dict(
            sku=name, price=price, cost=cost,
            pre_ad_margin=m["pre_ad_margin"], net_rate=m["net_rate"],
            commission_pct_applied=m["commission_pct_applied"],
            fixed_fee_applied=m["fixed_fee_applied"],
            vs_target=round(m["net_rate"] - tm, 4),
            verdict=("Đạt mục tiêu" if m["net_rate"] >= tm else
                     f"Thấp hơn mục tiêu {(tm - m['net_rate']) * 100:.1f} điểm %"),
            coupon_headroom=max(headroom, 0),
            break_even_price=fm.break_even_price(cost)))

    ladder = []
    sorted_skus = sorted([r for r in results if "price" in r], key=lambda x: x["price"])
    for a, b in zip(sorted_skus, sorted_skus[1:]):
        gap = b["price"] - a["price"]
        ladder.append(dict(frm=a["sku"], to=b["sku"], gap=round(gap, 2),
                           gap_pct=round(gap / a["price"], 4)))

    notes = []
    by_net = sorted([r for r in results if "net_rate" in r], key=lambda x: -x["net_rate"])
    if len(by_net) >= 2 and by_net[0]["price"] < by_net[-1]["price"]:
        notes.append("SKU có biên lợi nhuận ròng cao nhất không phải SKU giá cao nhất —— nếu là chiến lược SKU kéo traffic thì bình thường; nếu không cố ý thiết kế vậy, hãy kiểm tra giá vốn SKU cấu hình cao")
    under = [r["sku"] for r in results if "net_rate" in r and r["net_rate"] < tm]
    if under:
        notes.append(f"SKU thấp hơn biên lợi nhuận mục tiêu {fm.target_margin():g}%: {(', '.join(under))} —— xác nhận có cố ý không (SKU kéo traffic có thể thấp hơn mục tiêu, nhưng phải trên giá hòa vốn)")

    out = dict(mode="matrix", platform=getattr(args, "platform", None) or "custom",
               target_margin=fm.target_margin(), skus=results,
               price_ladder=ladder, notes=notes)
    print(json.dumps(out, ensure_ascii=False, indent=2))

    if not args.json:
        plat_label = (fm.p.get("label") or out["platform"])
        print(f"\nSàn: {plat_label} | Biên LN mục tiêu {fm.target_margin():g}% | "
              f"Hoa hồng/phí cố định chia bậc theo giá | Quảng cáo {fm.ad_pct()}% | Hoàn hàng {fm.return_pct()}% | "
              f"Thuế {fm.tax_pct()}% | Phụ phí sàn {fm.extra_pct()}%\n")
        print(f"{'SKU':<30}{'Giá bán':>10}{'Hoa hồng%':>10}{'Phí CĐ':>8}{'LN ròng':>9}{'vs MT':>9}{'Dư voucher':>12}")
        for r in results:
            if "error" in r:
                print(f"{r['sku']:<30}  ⚠️ {r['error']}")
                continue
            mark = "✅" if r["vs_target"] >= 0 else "⚠️ "
            print(f"{r['sku']:<30}{r['price']:>10,.2f}{r['commission_pct_applied']:>10g}"
                  f"{r['fixed_fee_applied']:>8,.2f}{r['net_rate']:>9.1%}"
                  f"{r['vs_target']:>+9.1%}{r['coupon_headroom']:>12,.2f} {mark}")
        print()
        for l in ladder:
            print(f"  Bậc giá {l['frm']} → {l['to']}: chênh R$ {l['gap']:,.2f} ({l['gap_pct']:.0%})")
        for n in notes:
            print(f"  ℹ️  {n}")
        for note in fm.p.get("notes", [])[:2]:
            print(f"  📌 {note}")
    return 0


def _fmt_tiers(tiers: list, field: str, suffix: str = "") -> str:
    caps = [t["max"] for t in tiers if t.get("max") is not None]
    if not caps:
        return f"{tiers[0][field]}{suffix}"
    return "/".join(f"≤{t['max']}:{t[field]}{suffix}" if t.get("max") is not None
                    else f">{caps[-1]}:{t[field]}{suffix}" for t in tiers)


def cmd_list_platforms(plats) -> int:
    print(f"{'key':<28}{'Sàn':<34}{'Hoa hồng%':<24}{'Phí cố định':<44}{'Phụ phí%':<9}")
    print("-" * 139)
    for k, v in plats.items():
        if k.startswith("_"):
            continue
        ct = v.get("commission_tiers")
        if ct:
            comm = _fmt_tiers(ct, "pct", "%")
        else:
            comm = f"{v.get('commission_pct', '-')}%"
        ft = v.get("fixed_fee_tiers")
        if ft:
            fee = _fmt_tiers(ft, "fee")
        else:
            fee = "0"
        print(f"{k:<28}{v.get('label', k):<34}{comm:<24}{fee:<44}{v.get('extra_pct', 0):<9g}")
    print("\nMức phí là số liệu công khai tại thời điểm biên soạn (xem _meta.updated), trước khi đăng bán bắt buộc kiểm tra lại trên Seller Center của từng sàn;")
    print("tham số truyền rõ (--commission, v.v.) luôn được ưu tiên hơn preset.")
    return 0


def _num(v, default=0.0, kind="dec"):
    if v is None:
        return default
    s = str(v).strip().replace("R$", "").replace("%", "").replace(" ", "")
    if s in ("", "-", "—", "暂无", "chưa có", "N/A", "nan"):
        return default
    neg = s.startswith("-")
    s = s.lstrip("-")
    if kind == "int":
        digits = "".join(ch for ch in s if ch.isdigit())
        return (-1 if neg else 1) * int(digits) if digits else default
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".") if s.rfind(",") > s.rfind(".") else s.replace(",", "")
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


def _add_common(p):
    p.add_argument("--platform", help="key preset theo sàn (xem bằng --list-platforms); tham số phí nào không truyền sẽ lấy mặc định của preset")
    p.add_argument("--commission", type=float, default=None, help="%% hoa hồng sàn (ghi đè preset)")
    p.add_argument("--return", dest="return_rate", type=float, default=None, help="%% hao hụt hoàn hàng (ghi đè preset)")
    p.add_argument("--ad", type=float, default=None, help="%% ngân sách quảng cáo trên giá bán (ghi đè preset)")
    p.add_argument("--tax", type=float, default=None, help="%% thuế suất hiệu dụng tổng hợp (ghi đè preset)")
    p.add_argument("--extra-pct", type=float, default=None, help="%% phụ phí sàn (vd. chương trình freeship; ghi đè preset)")
    p.add_argument("--fixed-fee", type=float, default=None, help="Phí cố định mỗi sản phẩm R$ (ghi đè bậc phí của preset)")
    p.add_argument("--target-margin", type=float, default=None, help="%% lợi nhuận ròng mục tiêu (mặc định 32)")


def main():
    plats = load_platforms()
    ap = argparse.ArgumentParser(description="Tính toán định giá SKU (chỉ tính, không tự định giá)")
    ap.add_argument("--list-platforms", action="store_true", help="Liệt kê toàn bộ preset mức phí theo sàn")
    sub = ap.add_subparsers(dest="cmd")

    c = sub.add_parser("calc", help="Một SKU: biên lợi nhuận ròng / giá hòa vốn / giá mục tiêu / dư địa voucher")
    _add_common(c)
    c.add_argument("--cost", type=float, required=True, help="Giá vốn về kho (landed cost) R$")
    c.add_argument("--price", type=float, required=True, help="Giá bán R$")
    c.add_argument("--json", action="store_true", help="Chỉ xuất JSON")

    m = sub.add_parser("matrix", help="Ma trận nhiều SKU: đọc CSV, xuất bảng biên lợi nhuận ròng + bậc giá + dư địa voucher")
    _add_common(m)
    m.add_argument("--file", required=True)
    m.add_argument("--json", action="store_true")

    args = ap.parse_args()
    if args.list_platforms:
        sys.exit(cmd_list_platforms(plats))
    if not args.cmd:
        ap.print_help()
        sys.exit(2)
    sys.exit(cmd_calc(args, plats) if args.cmd == "calc" else cmd_matrix(args, plats))


if __name__ == "__main__":
    main()
