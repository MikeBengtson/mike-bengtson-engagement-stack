#!/usr/bin/env python3
"""Generate Engagement Stack README and social branding assets."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W = 1280
H_BANNER = 320
H_SOCIAL = 640

ROOT = Path(__file__).resolve().parent
BANNER_DIR = ROOT / "banner"
SOCIAL_DIR = ROOT / "social"

HELV = "/System/Library/Fonts/Helvetica.ttc"
MENLO = "/System/Library/Fonts/Menlo.ttc"


def font(path, size, index=0):
    return ImageFont.truetype(path, size, index=index)


def gradient(size):
    w, h = size
    img = Image.new("RGBA", size, (0, 0, 0, 255))
    px = img.load()
    top = (8, 13, 32)
    mid = (43, 35, 100)
    bot = (203, 55, 112)
    for y in range(h):
        t = y / max(h - 1, 1)
        if t < 0.55:
            tt = t / 0.55
            c = tuple(int(top[i] + (mid[i] - top[i]) * tt) for i in range(3))
        else:
            tt = (t - 0.55) / 0.45
            c = tuple(int(mid[i] + (bot[i] - mid[i]) * tt) for i in range(3))
        for x in range(w):
            px[x, y] = (*c, 255)
    return img


def round_card(draw, xy, fill, outline, radius=12, width=1):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def draw_stack_cards(draw, x, y, scale=1.0, social=False):
    mono_bold = font(MENLO, int(18 * scale), index=1)
    mono = font(MENLO, int(16 * scale), index=0)
    card_w = int(500 * scale)
    card_h = int(58 * scale)
    gap = int(12 * scale)
    rows = [
        ("CV", "canonical truth", (34, 211, 238)),
        ("PORTFOLIO", "claims -> evidence", (16, 185, 129)),
        ("ENGAGEMENTS", "preferences -> offers", (245, 158, 11)),
        ("SHADERS", "role-specific resumes", (244, 63, 94)),
    ]
    if not social:
        rows = rows[:3]
    for i, (label, value, color) in enumerate(rows):
        yy = y + i * (card_h + gap)
        round_card(
            draw,
            [(x, yy), (x + card_w, yy + card_h)],
            fill=(84, 70, 138, 245),
            outline=(230, 220, 255, 120),
            radius=int(10 * scale),
        )
        draw.rectangle([(x, yy), (x + int(6 * scale), yy + card_h)], fill=(*color, 255))
        draw.text((x + int(18 * scale), yy + int(10 * scale)), label, font=mono_bold, fill=(255, 255, 255, 232))
        draw.text((x + int(170 * scale), yy + int(11 * scale)), "->", font=mono, fill=(255, 255, 255, 190))
        draw.text((x + int(220 * scale), yy + int(11 * scale)), value, font=mono, fill=(255, 255, 255, 222))


def draw_badges(draw, x, y):
    mono = font(MENLO, 16, index=0)
    badges = [
        ("human-first", (34, 211, 238)),
        ("agent-readable", (16, 185, 129)),
        ("resume shaders", (244, 63, 94)),
    ]
    for label, color in badges:
        w = 28 + len(label) * 10
        round_card(draw, [(x, y), (x + w, y + 34)], fill=(*color, 44), outline=(*color, 190), radius=17)
        draw.text((x + 14, y + 8), label, font=mono, fill=(255, 255, 255, 230))
        x += w + 12


def social():
    img = gradient((W, H_SOCIAL))
    draw = ImageDraw.Draw(img)
    title = font(HELV, 94, index=1)
    subtitle = font(HELV, 36, index=0)
    mono = font(MENLO, 20, index=0)
    draw.text((72, 96), "Engagement Stack", font=title, fill=(255, 255, 255, 255))
    draw.text((78, 230), "a Career OS for humans and agents", font=subtitle, fill=(255, 255, 255, 230))
    draw_badges(draw, 78, 300)
    draw_stack_cards(draw, 760, 250, scale=0.88, social=True)
    draw.text((72, 560), "GitHub-native dossier -> evidence -> offers -> scoped resumes", font=mono, fill=(255, 255, 255, 220))
    return img


def banner():
    img = gradient((W, H_BANNER))
    draw = ImageDraw.Draw(img)
    title = font(HELV, 68, index=1)
    subtitle = font(HELV, 25, index=0)
    mono = font(MENLO, 16, index=0)
    draw.text((54, 58), "Engagement Stack", font=title, fill=(255, 255, 255, 255))
    draw.text((58, 150), "human-first career OS, agent-readable by design", font=subtitle, fill=(255, 255, 255, 226))
    draw_badges(draw, 58, 204)
    draw.text((58, 260), "CV + portfolio + evidence + offers + resume shaders", font=mono, fill=(255, 255, 255, 210))
    draw_stack_cards(draw, 760, 56, scale=0.86, social=False)
    return img


def save(img, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, "PNG", optimize=True)
    print(f"wrote {path}")


def main():
    save(banner(), BANNER_DIR / "engagement-stack-banner.png")
    save(social(), SOCIAL_DIR / "engagement-stack-social.png")


if __name__ == "__main__":
    main()
