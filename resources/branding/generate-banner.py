#!/usr/bin/env python3
"""Generate the README banner for Mike Bengtson's Engagement Stack instance.

Reuses the framework brand helpers (gradient, badges, stack cards) from
generate.py, but makes *Mike Bengtson* the headline and *Engagement Stack*
the subtitle, with a representative keyword set drawn from the framework README.
"""

from PIL import ImageDraw

from generate import (
    gradient, draw_badges, draw_stack_cards, font, save,
    HELV, MENLO, W, H_BANNER, BANNER_DIR,
)

GOLD = (245, 201, 120, 255)  # warm gold accent from the brand family


def mike_banner():
    img = gradient((W, H_BANNER))
    draw = ImageDraw.Draw(img)

    name = font(HELV, 66, index=1)   # main element
    sub = font(HELV, 26, index=1)    # "Engagement Stack" subtitle (gold)
    tag = font(HELV, 18, index=0)
    mono = font(MENLO, 15, index=0)

    draw.text((54, 42), "Mike Bengtson", font=name, fill=(255, 255, 255, 255))
    draw.text((56, 120), "Engagement Stack", font=sub, fill=GOLD)
    draw.text((58, 158), "human-first, agent-readable Career OS", font=tag, fill=(255, 255, 255, 224))
    draw_badges(draw, 58, 200)
    draw.text((58, 256), "CV · Portfolio · Evidence · Engagements · Resume Shaders",
              font=mono, fill=(255, 255, 255, 212))
    draw_stack_cards(draw, 760, 56, scale=0.86, social=False)
    return img


if __name__ == "__main__":
    save(mike_banner(), BANNER_DIR / "mike-bengtson-banner.png")
