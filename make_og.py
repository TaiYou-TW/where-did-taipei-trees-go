# -*- coding: utf-8 -*-
"""產生分享用的 og.png（1200×630）。需要 Pillow。"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = "#f3f6f2"
INK = "#16211b"
INK2 = "#3f5248"
MUTED = "#697d72"
GREEN = "#1c7a4b"
TRUNK = "#14543a"
AMBER = "#a9700e"

BOLD = "C:/Windows/Fonts/msjhbd.ttc"
REG = "C:/Windows/Fonts/msjh.ttc"

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# 右側的樹（與 icon.svg 同一個構圖，放大到 og 版面）
cx, cy, s = 905, 300, 9.2


def circle(x, y, r, fill):
    d.ellipse([cx + (x - 32) * s - r * s, cy + (y - 25) * s - r * s,
               cx + (x - 32) * s + r * s, cy + (y - 25) * s + r * s], fill=fill)


d.rounded_rectangle([cx + (29.6 - 32) * s, cy + (35 - 25) * s,
                     cx + (34.4 - 32) * s, cy + (53 - 25) * s],
                    radius=2.4 * s, fill=TRUNK)
for x, y, r in [(32, 25, 13.4), (21.2, 29.6, 8.8), (42.8, 29.6, 8.8),
                (25.4, 18.2, 7.8), (38.6, 18.2, 7.8)]:
    circle(x, y, r, GREEN)
for x, y, r in [(25.2, 26.6, 2.7), (37.6, 21.2, 2.3), (31.2, 33, 2.0)]:
    circle(x, y, r, BG)
circle(47.5, 44, 3.1, AMBER)

# 左側文字
title = ImageFont.truetype(BOLD, 104)
sub = ImageFont.truetype(REG, 38)
small = ImageFont.truetype(REG, 26)
tag = ImageFont.truetype(BOLD, 26)

x0, y = 86, 150
d.text((x0, y), "樹都去哪了？", font=title, fill=INK)
y += 148
d.text((x0, y), "臺北市 24,340 棵樹的去向", font=sub, fill=INK2)
y += 62
d.text((x0, y), "除役原因、移植紀錄、樹蔭損失，全市地圖與分區查詢", font=small, fill=MUTED)

# 底部標籤
d.line([x0, 520, x0 + 320, 520], fill="#c6d1c5", width=2)
d.text((x0, 544), "2016–2026 ‧ 資料來源：臺北市公園路燈工程管理處", font=small, fill=MUTED)

img.save("og.png", optimize=True)
print("og.png", img.size)
