#!/usr/bin/env python3
"""Kiểm tra tuân thủ ảnh chính sản phẩm ở cấp pixel (Shopee / Mercado Livre / Amazon).

  python check_main_image.py anh.png --platform mercadolivre
  python check_main_image.py anh.png --platform shopee --fix anh_da_sua.png
  python check_main_image.py anh.png --platform amazon --json

Chỉ phụ thuộc Pillow. Ngưỡng kiểm tra lấy từ thẻ quy tắc của từng sàn trong references/, không phải tự nghĩ ra.

Các mục kiểm tra
  size_min        : số pixel cạnh ngắn (thấp hơn mức tối thiểu của sàn = fail luôn)
  square          : tỷ lệ rộng/cao 1:1 (±1%, ảnh không vuông sẽ bị sàn tự động cắt)
  coverage        : cạnh dài nhất của khung bao chủ thể ÷ cạnh ảnh (ba sàn yêu cầu khác nhau, ML khắt khe nhất ~95%)
  white_bg        : tỷ lệ pixel gần trắng trong dải viền 2% (Amazon bắt buộc / Shopee ưu tiên / ML không áp dụng)
  bg_uniformity   : tỷ lệ màu chủ đạo ở dải viền ("nền sạch" của ML, informational)
  file_size       : giới hạn dung lượng mỗi ảnh của sàn (Shopee 2MB khắt khe nhất)

--fix tự động sửa: kéo pixel gần trắng về trắng tinh, bù thành hình vuông, sắp xếp lại canvas theo tỷ lệ chiếm khung mục tiêu.
  (Việc "làm sạch" nền bối cảnh thật của ML cần tách nền, script không làm, sẽ nhắc rõ.)
"""
import argparse
import json
import os
import sys

try:
    from PIL import Image, ImageChops
except ImportError:
    sys.exit("Cần Pillow: pip install pillow")

# Ngưỡng theo sàn (nguồn: thẻ quy tắc references/platform-*.md)
PLATFORMS = {
    "shopee": dict(
        min_px=500, rec_px=1024, cover_min=0.60, cover_lo=0.70, cover_hi=0.92,
        white_fail=0.90, white_warn=0.98, uniform_info=0.90, max_mb=2, fix_target=0.80,
    ),
    "mercadolivre": dict(
        min_px=500, rec_px=1200, cover_min=0.80, cover_lo=0.85, cover_hi=0.97,
        white_fail=None, white_warn=None, uniform_info=0.90, max_mb=10, fix_target=0.88,
    ),
    "amazon": dict(
        min_px=1000, rec_px=2000, cover_min=0.85, cover_lo=0.85, cover_hi=0.97,
        white_fail=0.98, white_warn=0.99, uniform_info=0.90, max_mb=10, fix_target=0.87,
    ),
}


def _min_channel(img):
    """Lấy kênh RGB nhỏ nhất của mỗi pixel: dist = 255 - giá trị đó, 0 = trắng tinh. Viết thuần Pillow."""
    r, g, b = img.convert("RGB").split()
    return ImageChops.darker(ImageChops.darker(r, g), b)


def _near_white_ratio(mc_img, tol):
    """Tỷ lệ pixel gần trắng (min channel >= 255-tol). histogram được cài đặt ở tầng C nên nhanh."""
    h = mc_img.histogram()
    total = sum(h)
    if not total:
        return 0.0
    return sum(h[256 - tol:]) / total


def analyse(img, plt_name, tol=3, product_thr=12, band_pct=0.02):
    p = PLATFORMS[plt_name]
    w, h = img.size
    mc = _min_channel(img)
    hist = mc.histogram()
    total = w * h

    # Khung bao chủ thể: pixel có min channel < 255-thr = rõ ràng không phải trắng
    lut = [255 if v < 255 - product_thr else 0 for v in range(256)]
    bbox = mc.point(lut).getbbox()
    if bbox is None:
        return dict(width=w, height=h, coverage=0.0, bbox=None,
                    white_background=1.0, exact_ffffff=1.0, bg_uniformity=1.0)

    x0, y0, x1, y1 = bbox
    bw, bh = x1 - x0 + 1, y1 - y0 + 1
    coverage = max(bw / w, bh / h)

    # Dải viền 2% (bốn dải), tính riêng tỷ lệ gần trắng và tỷ lệ màu chủ đạo
    band = max(2, round(min(w, h) * band_pct))
    strips = [img.crop((0, 0, w, band)), img.crop((0, h - band, w, h)),
              img.crop((0, 0, band, h)), img.crop((w - band, 0, w, h))]
    mc_strips = [_min_channel(s) for s in strips]
    white_bg = sum(_near_white_ratio(m, tol) for m in mc_strips) / len(mc_strips)

    uni = []
    for s in strips:
        q = s.convert("RGB").quantize(colors=8)
        cols = q.getcolors(maxcolors=256) or []
        tot = sum(c for c, _ in cols)
        uni.append((max(c for c, _ in cols) / tot) if tot else 0.0)
    bg_uniformity = sum(uni) / len(uni)

    # Tỷ lệ trắng tinh trên số pixel nền (informational)
    product_px = sum(hist[:256 - product_thr])
    bg_px = total - product_px
    exact = (hist[255] / bg_px) if bg_px else 0.0

    return dict(width=w, height=h, coverage=round(coverage, 4), bbox=list(bbox),
                white_background=round(white_bg, 4), exact_ffffff=round(exact, 4),
                bg_uniformity=round(bg_uniformity, 4))


def check(img, path, plt_name, args):
    p = PLATFORMS[plt_name]
    m = analyse(img, plt_name, tol=args.tolerance)
    res = []          # (mức, mục kiểm tra, mô tả)

    def add(level, name, detail):
        res.append((level, name, detail))

    # Kích thước
    mn = min(m["width"], m["height"])
    if mn < p["min_px"]:
        add("FAIL", "size_min", f"{mn}px < mức tối thiểu của sàn {p['min_px']}px")
    elif mn < p["rec_px"]:
        add("WARN", "size_min", f"{mn}px đạt mức tối thiểu nhưng thấp hơn khuyến nghị {p['rec_px']}px (tính năng zoom bị hạn chế)")
    else:
        add("PASS", "size_min", f"{mn}px ≥ khuyến nghị {p['rec_px']}px")

    # Hình vuông
    ratio = abs(m["width"] - m["height"]) / max(m["width"], m["height"])
    if ratio > 0.01:
        add("FAIL", "square", f"{m['width']}×{m['height']} không vuông (sẽ bị sàn tự động cắt)")
    else:
        add("PASS", "square", "1:1")

    # Tỷ lệ chiếm khung của chủ thể
    c = m["coverage"]
    if c < p["cover_min"]:
        add("FAIL", "coverage", f"{c:.0%} < mức tối thiểu của sàn {p['cover_min']:.0%}")
    elif c < p["cover_lo"] or c > p["cover_hi"]:
        add("WARN", "coverage", f"{c:.0%} nằm ngoài vùng tối ưu {p['cover_lo']:.0%}–{p['cover_hi']:.0%}")
    else:
        add("PASS", "coverage", f"{c:.0%}")

    # Nền trắng tinh (Amazon bắt buộc / Shopee ưu tiên / ML không áp dụng)
    if p["white_fail"] is not None:
        wb = m["white_background"]
        if wb < p["white_fail"]:
            add("FAIL", "white_bg", f"Gần trắng ở dải viền {wb:.1%} < {p['white_fail']:.0%}")
        elif wb < p["white_warn"]:
            add("WARN", "white_bg", f"Gần trắng ở dải viền {wb:.1%} (gần đạt nhưng chưa tới {p['white_warn']:.0%}, hay gặp với nền xám/nền be)")
        else:
            add("PASS", "white_bg", f"{wb:.1%}")
    else:
        add("INFO", "white_bg", "ML không bắt buộc trắng tinh (trắng/màu trơn/bối cảnh thật theo ngành hàng), bỏ qua")

    # Độ đồng đều của nền ("nền sạch" của ML)
    u = m["bg_uniformity"]
    if u < 0.60:
        add("WARN", "bg_uniformity", f"Màu chủ đạo ở dải viền chỉ {u:.0%} —— nền có thể lộn xộn (ML: avoid messy backgrounds)")
    elif u < p["uniform_info"]:
        add("WARN", "bg_uniformity", f"Màu chủ đạo ở dải viền {u:.0%}, nền hơi rối")
    else:
        add("PASS", "bg_uniformity", f"{u:.0%} —— nền sạch")

    # Dung lượng file
    mb = os.path.getsize(path) / 1048576 if os.path.exists(path) else 0
    if mb > p["max_mb"]:
        add("FAIL", "file_size", f"{mb:.2f} MB > giới hạn {p['max_mb']} MB")
    else:
        add("PASS", "file_size", f"{mb:.2f} MB ≤ {p['max_mb']} MB")

    # Các mục không tự động kiểm tra được → người xác nhận
    if plt_name == "mercadolivre":
        add("MANUAL", "ml_cover_text", "Ảnh đầu cấm chữ khuyến mãi/từ thuộc tính của sàn/watermark/khung viền —— người xác nhận")
    if plt_name == "shopee":
        add("MANUAL", "shopee_text_ratio", "Chữ trong ảnh ≤ 20% khung hình và không lớn hơn chủ thể —— người xác nhận")

    ok = not any(lv == "FAIL" for lv, _, _ in res)
    return dict(platform=plt_name, ok=ok, metrics=m, checks=res)


def fix(img, plt_name, out_path, args):
    p = PLATFORMS[plt_name]
    target = p["fix_target"]
    w, h = img.size
    mc = _min_channel(img)

    # 1) Kéo gần trắng về trắng tinh (chỉ với sàn dùng nền trắng)
    if p["white_fail"] is not None:
        snap_tol = max(8, args.tolerance + 5)
        mask = mc.point([255 if v >= 255 - snap_tol else 0 for v in range(256)])
        white = Image.new("RGB", img.size, (255, 255, 255))
        img = Image.composite(white, img.convert("RGB"), mask)

    # 2) Sắp xếp lại canvas theo khung bao chủ thể để đạt tỷ lệ chiếm khung mục tiêu
    mc2 = _min_channel(img)
    lut = [255 if v < 255 - args.tolerance else 0 for v in range(256)]
    bbox = mc2.point(lut).getbbox()
    if bbox:
        product = img.crop(bbox)
        pw, ph = product.size
        side = int(max(pw, ph) / target)
        canvas_bg = (255, 255, 255) if p["white_fail"] is not None else _dominant_bg(img, bbox)
        canvas = Image.new("RGB", (side, side), canvas_bg)
        canvas.paste(product, ((side - pw) // 2, (side - ph) // 2))
        img = canvas

    # 3) Phóng to lên kích thước khuyến nghị
    rec = p["rec_px"]
    if img.size[0] < rec:
        img = img.resize((rec, rec), Image.LANCZOS)

    img.save(out_path, quality=92)
    return img


def _dominant_bg(img, bbox):
    """Lấy màu chủ đạo bên ngoài khung bao làm màu nền canvas cho ML (giữ cảm giác nền gốc)."""
    w, h = img.size
    x0, y0, x1, y1 = bbox
    strips = [img.crop((0, 0, w, max(1, y0))), img.crop((0, y1, w, h)),
              img.crop((0, 0, max(1, x0), h)), img.crop((x1, 0, w, h))]
    strips = [s for s in strips if s.size[0] > 0 and s.size[1] > 0]
    if not strips:
        return (255, 255, 255)
    best, best_n = (255, 255, 255), -1
    for s in strips:
        q = s.convert("RGB").quantize(colors=4)
        pal = q.getpalette() or []
        for cnt, idx in (q.getcolors(maxcolors=8) or []):
            if cnt > best_n:
                best_n = cnt
                best = tuple(pal[idx * 3: idx * 3 + 3])
    return best


def main():
    ap = argparse.ArgumentParser(description="Kiểm tra tuân thủ ảnh chính sản phẩm ở cấp pixel")
    ap.add_argument("image")
    ap.add_argument("--platform", required=True, choices=list(PLATFORMS),
                    help="shopee / mercadolivre / amazon")
    ap.add_argument("--tolerance", type=int, default=3, help="Dung sai xác định gần trắng (mặc định 3)")
    ap.add_argument("--fix", metavar="OUT", help="Tự động sửa và lưu vào đường dẫn chỉ định")
    ap.add_argument("--json", action="store_true", help="Xuất JSON")
    args = ap.parse_args()

    if not os.path.exists(args.image):
        sys.exit(f"[ERROR] File không tồn tại: {args.image}")
    img = Image.open(args.image)

    report = check(img, args.image, args.platform, args)

    if args.fix:
        fixed = fix(img, args.platform, args.fix, args)
        re_report = check(fixed, args.fix, args.platform, args)
        report["fixed_to"] = args.fix
        report["after_fix_ok"] = re_report["ok"]
        report["after_fix_checks"] = re_report["checks"]

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        icon = {"PASS": "✅", "WARN": "⚠️ ", "FAIL": "❌", "INFO": "ℹ️ ", "MANUAL": "👤"}
        print(f"\nSàn: {args.platform}   Kích thước: {report['metrics']['width']}×"
              f"{report['metrics']['height']}   Kết luận: {'✅ Đạt' if report['ok'] else '❌ Không đạt'}\n")
        for lv, name, detail in report["checks"]:
            print(f"  {icon[lv]} {name:<16} {detail}")
        if args.fix:
            print(f"\nĐã sửa → {args.fix}   Kết luận sau khi sửa: "
                  f"{'✅ Đạt' if report.get('after_fix_ok') else '❌ Vẫn còn mục FAIL'}")
    sys.exit(0 if report["ok"] else 1)


if __name__ == "__main__":
    main()
