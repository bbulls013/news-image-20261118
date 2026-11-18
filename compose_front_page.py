#!/usr/bin/env python3
"""Compose the 18 November 2026 front-page image (1024x1024 PNG).

Reads assets/hero.png (AI-illustrated summit hall, no people, no text),
lays out a newspaper front page with PIL, writes entry.png.
Deterministic: same inputs -> same bytes (PNG written with fixed settings).
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
M = 30  # margin
PAPER = (246, 241, 231)
INK = (18, 18, 18)
RED = (178, 34, 34)
NAVY = (27, 58, 110)
GREY = (90, 86, 78)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    lines = []
    for para in text.split("\n"):
        lines.extend(textwrap.wrap(para, width=1000) if False else _wrap(draw, para, fnt, width))
    return lines


def _wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # border
    d.rectangle([8, 8, W - 9, H - 9], outline=INK, width=3)
    d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=1)

    y = 28
    # masthead
    f_mast = font(SERIF_B, 58)
    d.text((W // 2, y), "THE WORLD IN ONE PAGE", font=f_mast, fill=INK, anchor="ma")
    y += 66
    f_date = font(SANS_B, 17)
    d.text((W // 2, y), "WEDNESDAY 18 NOVEMBER 2026", font=f_date, fill=RED, anchor="ma")
    y += 26
    d.line([(M, y), (W - M, y)], fill=INK, width=2)
    y += 12
    # headline
    f_head = font(SERIF_B, 52)
    d.text((W // 2, y), "THREE LEADERS, ONE TABLE", font=f_head, fill=INK, anchor="ma")
    y += 58
    d.text((W // 2, y), "AS TWO WARS ESCALATE", font=f_head, fill=INK, anchor="ma")
    y += 66
    d.line([(M, y), (W - M, y)], fill=INK, width=2)
    y += 10

    # hero image
    hero = Image.open("assets/hero.png").convert("RGB")
    hw, hh = W - 2 * M, 348
    hero = hero.resize((hw, hh), Image.LANCZOS)
    img.paste(hero, (M, y))
    d.rectangle([M, y, M + hw - 1, y + hh - 1], outline=INK, width=2)
    y += hh + 8
    f_cap = font(SANS, 17)
    cap = "Xi Jinping and Vladimir Putin met in Shenzhen ahead of Thursday's trilateral summit with Donald Trump."
    for line in _wrap(d, cap, f_cap, W - 2 * M):
        d.text((M, y), line, font=f_cap, fill=GREY)
        y += 22
    y += 6
    d.line([(M, y), (W - M, y)], fill=INK, width=2)
    y += 12

    # three columns
    cols = [
        ("THE GULF", RED, "US strikes Qeshm Island;\nIran hits Kuwait\nand Bahrain",
         "American jets hit a missile site on Qeshm Island. Iran answered with drones at US bases in Kuwait and Bahrain."),
        ("UKRAINE", NAVY, "Kerch Bridge partly\ncollapses after\nUkrainian attack",
         "Drone and missile strikes brought down part of the bridge linking Russia to annexed Crimea."),
        ("AMERICA", (34, 90, 60), "Democrats take the\nSenate as Peltola\nwins Alaska, 56-44",
         "Mary Peltola's win in Alaska gives Democrats a projected 56-seat majority in the US Senate."),
    ]
    col_w = (W - 2 * M - 2 * 16) // 3
    x0 = M
    f_tag = font(SANS_B, 16)
    f_colh = font(SERIF_B, 25)
    f_body = font(SANS, 16)
    col_bottom = y
    for tag, color, head, body in cols:
        x = x0
        d.rectangle([x, y, x + col_w, y + 26], fill=color)
        d.text((x + col_w // 2, y + 13), tag, font=f_tag, fill=(255, 255, 255), anchor="mm")
        cy = y + 36
        for line in _wrap(d, head, f_colh, col_w):
            d.text((x, cy), line, font=f_colh, fill=INK)
            cy += 30
        cy += 4
        for line in _wrap(d, body, f_body, col_w):
            d.text((x, cy), line, font=f_body, fill=(40, 40, 40))
            cy += 21
        col_bottom = max(col_bottom, cy)
        x0 += col_w + 16
    y = col_bottom + 10
    d.line([(M, y), (W - M, y)], fill=INK, width=2)
    y += 10
    f_also = font(SANS_B, 16)
    d.text((M, y), "ALSO TODAY", font=f_also, fill=RED)
    y += 24
    f_small = font(SANS, 16)
    also = ("Ebola surges in DR Congo  ·  US loses its measles-free status  ·  Russian military plane "
            "crashes in Siberia, 19 dead  ·  Cyclone Xavier hits the Cook Islands  ·  Nvidia posts record revenue")
    for line in _wrap(d, also, f_small, W - 2 * M):
        d.text((M, y), line, font=f_small, fill=(40, 40, 40))
        y += 21
    y += 8
    d.line([(M, y), (W - M, y)], fill=INK, width=1)
    y += 8
    f_foot = font(SERIF, 15)
    d.text((W // 2, y), "18 November 2026 — one image, the whole day.", font=f_foot, fill=GREY, anchor="ma")

    img.save("entry.png", format="PNG", optimize=True)


if __name__ == "__main__":
    main()
