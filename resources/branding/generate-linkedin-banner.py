#!/usr/bin/env python3
"""Mike Bengtson — 1584x396 LinkedIn profile banner (navy + gold).

Spec: submissions/linkedin/media.md — dark navy #1f3d5c with one warm-gold
#c9a227 accent, text right-aligned in the right two-thirds, lower-left kept
clear for LinkedIn's avatar + name overlay. Reuses font/save from generate.py.
Swap KICKER / TAGLINE below to use a different media.md tagline.
"""

from pathlib import Path
from PIL import Image, ImageDraw

from generate import font, save, HELV, MENLO

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "social" / "mike-bengtson-linkedin-banner.png"

W, H = 1584, 396
NAVY_TL = (36, 74, 110)   # lighter navy, top-left
NAVY_BR = (14, 30, 49)    # deeper navy, bottom-right
GOLD = (201, 162, 39)     # #c9a227 warm gold
WHITE = (255, 255, 255)

# --- swap to any media.md tagline; keep lines <= ~37 chars so they stay in the safe zone ---
KICKER = "VP / DIRECTOR  ·  AI ENGINEERING"
TAGLINE = [
    "Agentic AI & Developer Productivity —",
    "scaling platforms to millions and the",
    "toolchains that build them.",
]


def navy_gradient(w, h):
    tl, br = NAVY_TL, NAVY_BR
    data = []
    for y in range(h):
        ty = y / (h - 1)
        for x in range(w):
            t = (x / (w - 1) + ty) / 2.0
            data.append((
                int(tl[0] + (br[0] - tl[0]) * t),
                int(tl[1] + (br[1] - tl[1]) * t),
                int(tl[2] + (br[2] - tl[2]) * t),
            ))
    img = Image.new("RGB", (w, h))
    img.putdata(data)
    return img


def main():
    img = navy_gradient(W, H)
    draw = ImageDraw.Draw(img)
    x_r = W - 76  # right margin; all text right-aligned to here

    kf = font(MENLO, 21, index=1)
    tf = font(HELV, 39, index=1)

    y = 86
    draw.text((x_r, y), KICKER, font=kf, fill=GOLD, anchor="ra")       # gold kicker
    draw.line([(x_r - 140, y + 38), (x_r, y + 38)], fill=GOLD, width=3)  # one thin gold rule
    ty = y + 62
    for line in TAGLINE:                                               # white tagline, right-aligned
        draw.text((x_r, ty), line, font=tf, fill=WHITE, anchor="ra")
        ty += 50

    save(img, OUT)


if __name__ == "__main__":
    main()
