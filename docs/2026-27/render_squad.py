#!/usr/bin/env python3
"""Render the FPL 2026/27 GW1 squad as a pitch graphic (PNG)."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1500, 1990
SS = 2  # supersample factor for crisp output
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

def f(name, size):
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size * SS)

BOLD = lambda s: f("DejaVuSans-Bold.ttf", s)
REG = lambda s: f("DejaVuSans.ttf", s)

CLUB = {  # club -> (band colour, text colour on band)
    "BHA": ("#0057B8", "#FFFFFF"), "MCI": ("#6CABDD", "#0B2240"),
    "TOT": ("#132257", "#FFFFFF"), "MUN": ("#DA291C", "#FFFFFF"),
    "LEE": ("#FFCD00", "#1A1A1A"), "LIV": ("#C8102E", "#FFFFFF"),
    "BRE": ("#E30613", "#FFFFFF"), "CHE": ("#034694", "#FFFFFF"),
    "IPS": ("#3A64A3", "#FFFFFF"),
}

# (name, club, price, note, badge)
XI = [
    [("Verbruggen", "BHA", "4.5", "130 pts", None)],
    [("Guéhi", "MCI", "6.0", "179 pts", None),
     ("Van Hecke", "TOT", "5.0", "148 pts", None),
     ("Shaw", "MUN", "4.5", "113 pts", None)],
    [("B. Fernandes", "MUN", "12.0", "235 pts", "V"),
     ("Mbeumo", "MUN", "8.0", "148 pts", None),
     ("Szoboszlai", "LIV", "7.0", "160 pts", None),
     ("Anderson", "MCI", "6.5", "180 pts", None)],
    [("Haaland", "MCI", "15.5", "239 pts", "C"),
     ("João Pedro", "CHE", "7.5", "177 pts", None),
     ("Calvert-Lewin", "LEE", "6.0", "142 pts", None)],
]
BENCH = [("Yarmoliuk", "BRE", "5.0", "Sub 1", None),
         ("Rodon", "LEE", "4.5", "Sub 2", None),
         ("Diop", "IPS", "4.0", "Sub 3", None),
         ("Palmer", "IPS", "4.0", "GK", None)]

img = Image.new("RGB", (W * SS, H * SS), "#0B1220")
d = ImageDraw.Draw(img, "RGBA")

def s(v):
    return v * SS

def text(xy, txt, font, fill, anchor="mm"):
    d.text((s(xy[0]), s(xy[1])), txt, font=font, fill=fill, anchor=anchor)

# ---------------- header ----------------
d.rectangle([0, 0, s(W), s(150)], fill="#12203A")
text((44, 52), "FANTASY PREMIER LEAGUE 2026/27", BOLD(30), "#7FB2E5", "lm")
text((44, 104), "Gameweek 1  ·  Formasi 3-4-3", BOLD(44), "#FFFFFF", "lm")
text((W - 44, 52), "£100.0m / £100.0m", BOLD(38), "#3DDC84", "rm")
text((W - 44, 106), "Deadline: Jum'at 21 Agu 2026, 17:30 UTC", REG(26), "#9BB0CC", "rm")

# ---------------- pitch ----------------
PX0, PY0, PX1, PY1 = 36, 172, W - 36, 1600
d.rounded_rectangle([s(PX0), s(PY0), s(PX1), s(PY1)], radius=s(18), fill="#16803C")
stripe_h = (PY1 - PY0) / 12
for i in range(12):
    if i % 2 == 0:
        y0 = PY0 + i * stripe_h
        d.rectangle([s(PX0), s(y0), s(PX1), s(min(y0 + stripe_h, PY1))], fill="#199447")

LINE = (255, 255, 255, 115)
LW = s(4)
cx = (PX0 + PX1) / 2
d.rounded_rectangle([s(PX0 + 16), s(PY0 + 16), s(PX1 - 16), s(PY1 - 16)],
                    radius=s(10), outline=LINE, width=LW)
midy = (PY0 + PY1) / 2
d.line([s(PX0 + 16), s(midy), s(PX1 - 16), s(midy)], fill=LINE, width=LW)
d.ellipse([s(cx - 130), s(midy - 130), s(cx + 130), s(midy + 130)], outline=LINE, width=LW)
d.ellipse([s(cx - 7), s(midy - 7), s(cx + 7), s(midy + 7)], fill=LINE)

def vrect(half_w, y_a, y_b):
    lo, hi = sorted((y_a, y_b))
    d.rectangle([s(cx - half_w), s(lo), s(cx + half_w), s(hi)], outline=LINE, width=LW)

for top in (True, False):
    base = PY0 + 16 if top else PY1 - 16
    sgn = 1 if top else -1
    vrect(400, base, base + sgn * 230)
    vrect(185, base, base + sgn * 95)
    vrect(105, base, base - sgn * 34)
    a_lo, a_hi = sorted((base + sgn * 150, base + sgn * 310))
    d.arc([s(cx - 90), s(a_lo), s(cx + 90), s(a_hi)],
          start=0 if top else 180, end=180 if top else 360, fill=LINE, width=LW)

# ---------------- player cards ----------------
CW, CH, RAD = 232, 158, 16

def card(cxp, cyp, name, club, price, note, badge):
    x0, y0 = cxp - CW / 2, cyp - CH / 2
    x1, y1 = cxp + CW / 2, cyp + CH / 2
    d.rounded_rectangle([s(x0 + 4), s(y0 + 6), s(x1 + 4), s(y1 + 8)],
                        radius=s(RAD), fill=(0, 0, 0, 70))
    d.rounded_rectangle([s(x0), s(y0), s(x1), s(y1)], radius=s(RAD), fill="#FFFFFF")

    band, btxt = CLUB[club]
    bh = 46
    d.rounded_rectangle([s(x0), s(y0), s(x1), s(y0 + bh)], radius=s(RAD), fill=band)
    d.rectangle([s(x0), s(y0 + bh - RAD), s(x1), s(y0 + bh)], fill=band)
    text((cxp, y0 + bh / 2 + 1), club, BOLD(25), btxt)

    size = 28
    while BOLD(size).getlength(name) > s(CW - 26) and size > 17:
        size -= 1
    text((cxp, y0 + 88), name, BOLD(size), "#111827")
    text((cxp, y0 + 129), f"£{price}m  ·  {note}", REG(21), "#6B7280")

    if badge:
        bx, by, r = x1 - 8, y0 + 6, 23
        col = "#F5C518" if badge == "C" else "#D1D5DB"
        d.ellipse([s(bx - r), s(by - r), s(bx + r), s(by + r)], fill=col, outline="#FFFFFF", width=s(3))
        text((bx, by + 1), badge, BOLD(26), "#111827")

ROW_Y = [318, 660, 1010, 1360]
for row_i, row in enumerate(XI):
    n = len(row)
    span = PX1 - PX0 - 120
    step = span / n
    for i, p in enumerate(row):
        xp = PX0 + 60 + step * (i + 0.5)
        card(xp, ROW_Y[row_i], *p)

# ---------------- bench ----------------
BY0 = 1636
d.rounded_rectangle([s(PX0), s(BY0), s(PX1), s(H - 96)], radius=s(18), fill="#152238")
text((PX0 + 32, BY0 + 42), "BANGKU CADANGAN", BOLD(26), "#7FB2E5", "lm")
text((PX1 - 32, BY0 + 42), "urutan sub dari kiri", REG(22), "#7C8DA6", "rm")
step = (PX1 - PX0 - 60) / 4
for i, p in enumerate(BENCH):
    card(PX0 + 30 + step * (i + 0.5), BY0 + 152, *p)

# ---------------- footer ----------------
text((W / 2, H - 52),
     "Kapten: Haaland  ·  Wakil: B. Fernandes        MCI 3  ·  MUN 3  ·  IPS 2  ·  LEE 2        Sisa budget: £0.0m",
     REG(24), "#8FA3BD")

img.resize((W, H), Image.LANCZOS).save(
    "/home/user/mancity-fantasyleague/docs/2026-27/gw1-squad.png")
print("saved")
