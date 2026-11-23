#!/usr/bin/env python3
"""Kiểm tra tuân thủ tiêu đề (Shopee / Mercado Livre / Amazon) — số ký tự là giá trị đo thực tế, không phải ước lượng.

  python title_lint.py "Nội dung tiêu đề" --platform shopee
  python title_lint.py tieu_de.txt --platform mercadolivre --forbidden iPhone,Samsung
  python title_lint.py "Tiêu đề" --platform shopee --keywords carregador,20000mah,45w

Các mục kiểm tra (ngưỡng lấy từ bảng quy tắc references/platform-title-rules.md):
  length        : số ký tự (không phải số byte) có nằm trong giới hạn của sàn không; <90% thì gợi ý bổ sung từ khóa (Shopee)
  first30       : nội dung 30 ký tự đầu (đoạn có trọng số cao nhất trên Shopee, để người duyệt xác nhận từ khóa chính đã đặt lên đầu chưa)
  forbidden     : dính từ cấm (tên thương hiệu chưa được ủy quyền, từ ngữ tuyệt đối hóa...)
  keywords      : độ phủ từ khóa cốt lõi (thiếu những từ nào)
  emoji         : emoji / ký hiệu bất thường (Shopee cấm)
  all_caps      : từ viết hoa toàn bộ (Shopee cấm viết hoa tràn lan)
  promo_words   : từ khuyến mãi (Shopee: cẩn trọng / ML: khuyến cáo rõ là không dùng)
  duplicates    : nhồi từ khóa lặp lại (≥3 lần)
  locale        : lẫn ký tự tiếng Trung (sàn PT-BR phải dùng ngôn ngữ bản địa)
"""
import argparse
import json
import re
import sys

PLATFORMS = {
    "shopee": dict(limit=120, first_n=30, rec_fill=0.80, promo="warn"),
    "mercadolivre": dict(limit=60, first_n=None, rec_fill=None, promo="warn"),
    "amazon": dict(limit=200, first_n=None, rec_fill=None, promo="warn"),
}

PROMO_WORDS = [
    "frete grátis", "frete gratis", "promoção", "promocao", "oferta", "imperdível",
    "imperdivel", "brinde", "desconto", "promo", "sale", "免费", "促销", "特价",
    "miễn phí", "khuyến mãi", "giảm giá",
]

EMOJI_RE = re.compile("[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F900-\U0001F9FF]")
CJK_RE = re.compile(r"[\u4e00-\u9fff]")


def analyse(title, platform, args):
    p = PLATFORMS[platform]
    res = []   # (mức độ, mục kiểm tra, mô tả)
    t = title.strip()
    n = len(t)   # độ dài chuỗi Python = số ký tự (không phải byte)

    # 1) Độ dài
    if n > p["limit"]:
        res.append(("FAIL", "length", f"{n} ký tự > giới hạn của sàn {p['limit']} — phần vượt sẽ bị cắt"))
    elif p["rec_fill"] and n < p["limit"] * p["rec_fill"]:
        res.append(("WARN", "length", f"{n}/{p['limit']} ký tự (tỷ lệ sử dụng {n / p['limit']:.0%}), "
                                      f"nên bổ sung từ khóa lên 90%+"))
    else:
        res.append(("PASS", "length", f"{n}/{p['limit']} ký tự"))

    # 2) 30 ký tự đầu (đoạn có trọng số cao nhất trên Shopee)
    if p["first_n"]:
        head = t[:p["first_n"]]
        res.append(("INFO", "first30", f"\"{head}\" ← 30 ký tự đầu, từ khóa chính bắt buộc nằm ở đây"))

    # 3) Từ cấm
    forbidden = args.forbidden or []
    if isinstance(forbidden, str):
        forbidden = [w.strip() for w in forbidden.split(",") if w.strip()]
    if args.forbidden_file:
        try:
            with open(args.forbidden_file, encoding="utf-8") as f:
                forbidden += [ln.strip() for ln in f if ln.strip()]
        except OSError as e:
            res.append(("WARN", "forbidden", f"Không đọc được file từ cấm: {e}"))
    hits = [w for w in forbidden if w and w.lower() in t.lower()]
    if hits:
        res.append(("FAIL", "forbidden", f"Dính từ cấm: {', '.join(hits)} (tên thương hiệu chưa ủy quyền / từ ngữ tuyệt đối hóa có nguy cơ bị gỡ sản phẩm)"))
    elif forbidden:
        res.append(("PASS", "forbidden", f"Không dính từ nào (đã kiểm tra {len(forbidden)} từ)"))

    # 4) Độ phủ từ khóa
    if args.keywords:
        kws = [k.strip() for k in args.keywords.split(",") if k.strip()]
        missing = [k for k in kws if k.lower() not in t.lower()]
        if missing:
            res.append(("WARN", "keywords", f"Chưa phủ từ khóa cốt lõi: {', '.join(missing)}"))
        else:
            res.append(("PASS", "keywords", f"Đã phủ đủ {len(kws)} từ khóa cốt lõi"))

    # 5) Emoji (Shopee cấm)
    if EMOJI_RE.search(t):
        res.append(("FAIL" if platform == "shopee" else "WARN", "emoji",
                    f"Phát hiện emoji / ký hiệu: {EMOJI_RE.findall(t)[:5]}"))

    # 6) Từ viết hoa toàn bộ (Shopee cấm viết hoa tràn lan)
    caps = [w for w in re.findall(r"[A-Za-z]{4,}", t) if w.isupper()]
    if caps:
        res.append(("WARN", "all_caps", f"Từ viết hoa toàn bộ: {', '.join(caps[:6])} (Shopee cấm viết hoa tràn lan, chỉ chấp nhận tên viết tắt của thương hiệu)"))

    # 7) Từ khuyến mãi
    promos = [w for w in PROMO_WORDS if w in t.lower()]
    if promos:
        lv = "FAIL" if p["promo"] == "fail" else "WARN"
        res.append((lv, "promo_words", f"Từ khuyến mãi: {', '.join(promos)} (ML khuyến cáo rõ là không dùng; Shopee: cẩn trọng, đây là thông tin khuyến mãi nên đưa vào ảnh / mô tả)"))

    # 8) Nhồi từ khóa lặp lại
    words = re.findall(r"[A-Za-zÀ-ÿ0-9]+", t.lower())
    dup = [w for w in set(words) if words.count(w) >= 3 and len(w) > 2]
    if dup:
        res.append(("FAIL", "duplicates", f"Lặp ≥3 lần: {', '.join(dup)} (nhồi từ khóa sẽ bị giảm thứ hạng)"))

    # 9) Lẫn ngôn ngữ (tiêu đề trên sàn PT-BR có tiếng Trung)
    if CJK_RE.search(t):
        res.append(("FAIL", "locale", "Tiêu đề chứa ký tự tiếng Trung — văn bản người mua nhìn thấy trên Shopee Brazil phải là PT-BR"))

    ok = not any(lv == "FAIL" for lv, _, _ in res)
    return dict(platform=platform, chars=n, limit=p["limit"], ok=ok, checks=res,
                first_30=t[:30])


def main():
    ap = argparse.ArgumentParser(description="Kiểm tra tuân thủ tiêu đề (số ký tự đo thực tế, không ước lượng)")
    ap.add_argument("title", nargs="?", help="Nội dung tiêu đề; hoặc truyền vào bằng --file")
    ap.add_argument("--file", help="Đọc tiêu đề từ file (mỗi dòng một tiêu đề, kiểm tra lần lượt)")
    ap.add_argument("--platform", required=True, choices=list(PLATFORMS))
    ap.add_argument("--forbidden", help="Từ cấm, phân tách bằng dấu phẩy (tên thương hiệu / từ ngữ tuyệt đối hóa)")
    ap.add_argument("--forbidden-file", help="File từ cấm (mỗi dòng một từ)")
    ap.add_argument("--keywords", help="Từ khóa cốt lõi, phân tách bằng dấu phẩy (kiểm tra độ phủ)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    titles = []
    if args.file:
        try:
            with open(args.file, encoding="utf-8") as f:
                titles = [ln.strip() for ln in f if ln.strip()]
        except OSError as e:
            sys.exit(f"[ERROR] Không đọc được file: {e}")
    elif args.title:
        titles = [args.title]
    else:
        sys.exit("[ERROR] Cần truyền nội dung tiêu đề hoặc --file")

    reports = [analyse(t, args.platform, args) for t in titles]
    all_ok = all(r["ok"] for r in reports)

    if args.json:
        print(json.dumps(reports if len(reports) > 1 else reports[0],
                         ensure_ascii=False, indent=2))
    else:
        for r in reports:
            icon = {"PASS": "✅", "WARN": "⚠️ ", "FAIL": "❌", "INFO": "ℹ️ "}
            print(f"\n\"{r['first_30']}{'…' if r['chars'] > 30 else ''}\""
                  f"  [{r['platform']}  {r['chars']}/{r['limit']} ký tự]"
                  f"  Kết luận: {'✅ Đạt' if r['ok'] else '❌ Không đạt'}")
            for lv, name, detail in r["checks"]:
                print(f"  {icon[lv]} {name:<12} {detail}")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
