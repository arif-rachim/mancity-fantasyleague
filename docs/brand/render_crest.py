#!/usr/bin/env python3
"""Generate 'The Grendel' FPL club crest variants as PNG."""
import cairosvg, pathlib, sys

OUT = pathlib.Path("/home/user/mancity-fantasyleague/docs/brand")
OUT.mkdir(parents=True, exist_ok=True)

INK    = "#0B111F"   # midnight
INK2   = "#131C31"
BLOOD  = "#B01221"
BLOOD2 = "#7E0B17"
GOLD   = "#E7B32A"
BONE   = "#F3E7D0"
SKY    = "#6CABDD"

# ---------------------------------------------------------------- beast head
def beast(cx, cy, s, skin, eye, shade):
    """Angular horned beast head, drawn around (cx,cy), scale s (1 = 200px wide)."""
    return f'''
  <g transform="translate({cx},{cy}) scale({s})">
    <!-- horns -->
    <path d="M -74 -30 C -112 -60 -128 -112 -118 -158 C -96 -120 -74 -96 -46 -76 Z"
          fill="{skin}"/>
    <path d="M  74 -30 C  112 -60  128 -112  118 -158 C  96 -120  74 -96  46 -76 Z"
          fill="{skin}"/>
    <path d="M -74 -30 C -104 -58 -117 -102 -112 -142 C -95 -112 -76 -92 -52 -74 Z"
          fill="{shade}" opacity=".35"/>
    <path d="M  74 -30 C  104 -58  117 -102  112 -142 C  95 -112  76 -92  52 -74 Z"
          fill="{shade}" opacity=".35"/>

    <!-- skull -->
    <path d="M 0 -104 L 78 -66 L 92 10 L 60 74 L 0 122 L -60 74 L -92 10 L -78 -66 Z"
          fill="{skin}"/>
    <!-- cheek shading -->
    <path d="M 0 -104 L 78 -66 L 92 10 L 60 74 L 0 122 Z" fill="{shade}" opacity=".18"/>

    <!-- brow ridge -->
    <path d="M -84 -46 L 0 -20 L 84 -46 L 84 -22 L 0 6 L -84 -22 Z" fill="{shade}" opacity=".45"/>

    <!-- eyes -->
    <path d="M -70 -8 L -18 12 L -26 42 L -66 26 Z" fill="{eye}"/>
    <path d="M  70 -8 L  18 12 L  26 42 L  66 26 Z" fill="{eye}"/>
    <path d="M -62 2 L -30 14 L -34 30 L -60 20 Z" fill="#FFFFFF" opacity=".55"/>
    <path d="M  62 2 L  30 14 L  34 30 L  60 20 Z" fill="#FFFFFF" opacity=".55"/>

    <!-- snout + jaw -->
    <path d="M -44 54 L 44 54 L 30 92 L 0 122 L -30 92 Z" fill="{shade}" opacity=".55"/>
    <!-- fangs -->
    <path d="M -40 54 L -26 54 L -30 84 Z" fill="{skin}"/>
    <path d="M  40 54 L  26 54 L  30 84 Z" fill="{skin}"/>
    <path d="M -14 56 L -2 56 L -8 76 Z" fill="{skin}"/>
    <path d="M  14 56 L  2 56 L  8 76 Z" fill="{skin}"/>
  </g>'''


def condensed(x, y, txt, size, fill, weight="bold", squeeze=.84, ls=2, anchor="middle"):
    return (f'<g transform="translate({x},{y}) scale({squeeze},1)">'
            f'<text x="0" y="0" text-anchor="{anchor}" font-family="DejaVu Sans" '
            f'font-weight="{weight}" font-size="{size}" letter-spacing="{ls}" '
            f'fill="{fill}">{txt}</text></g>')


# ---------------------------------------------------------------- variant A
SHIELD = ("M 70 96 L 256 44 L 442 96 L 442 250 "
          "C 442 364 358 440 256 478 C 154 440 70 364 70 250 Z")

def variant_a():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    <linearGradient id="sg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{INK2}"/><stop offset="1" stop-color="{INK}"/>
    </linearGradient>
    <clipPath id="sc"><path d="{SHIELD}"/></clipPath>
  </defs>

  <path d="{SHIELD}" fill="{GOLD}"/>
  <path d="{SHIELD}" fill="url(#sg)" transform="translate(256,262) scale(.945) translate(-256,-262)"/>

  <g clip-path="url(#sc)">
    <path d="M 70 300 L 442 300 L 442 500 L 70 500 Z" fill="{BLOOD2}" opacity=".55"/>
    <path d="M 70 96 L 442 96 L 442 118 L 70 118 Z" fill="{BLOOD}" opacity=".7"/>
  </g>

  {beast(256, 236, 1.0, BONE, BLOOD, INK)}

  <!-- banner -->
  <path d="M 44 336 L 468 336 L 448 396 L 64 396 Z" fill="{BLOOD}"/>
  <path d="M 44 336 L 468 336 L 464 348 L 48 348 Z" fill="#D6202F"/>
  <path d="M 44 336 L 20 316 L 26 372 L 64 396 Z" fill="{BLOOD2}"/>
  <path d="M 468 336 L 492 316 L 486 372 L 448 396 Z" fill="{BLOOD2}"/>
  {condensed(256, 380, "THE GRENDEL", 52, BONE, ls=3)}

  {condensed(256, 434, "2026/27", 22, GOLD, ls=4)}
  {condensed(256, 96, "EST. 2026", 20, GOLD, ls=5)}
</svg>'''


# ---------------------------------------------------------------- variant B
def variant_b():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#16233D"/><stop offset="1" stop-color="{INK}"/>
    </linearGradient>
  </defs>
  <circle cx="256" cy="256" r="244" fill="{SKY}"/>
  <circle cx="256" cy="256" r="230" fill="url(#bg)"/>
  <circle cx="256" cy="256" r="212" fill="none" stroke="{SKY}" stroke-width="5"/>

  {beast(256, 226, .92, SKY, "#FF3B4E", "#06101F")}

  <path d="M 152 358 L 360 358 L 360 364 L 152 364 Z" fill="{SKY}" opacity=".55"/>
  {condensed(256, 408, "THE GRENDEL", 42, "#FFFFFF", ls=3)}
  {condensed(256, 442, "FPL · EST. 2026", 17, SKY, ls=4)}
</svg>'''


# ---------------------------------------------------------------- variant C
def variant_c():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    <linearGradient id="cg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{BLOOD}"/><stop offset="1" stop-color="{BLOOD2}"/>
    </linearGradient>
  </defs>
  <clipPath id="cc"><rect x="26" y="26" width="460" height="460" rx="74"/></clipPath>
  <rect x="0" y="0" width="512" height="512" rx="96" fill="{INK}"/>
  <rect x="22" y="22" width="468" height="468" rx="78" fill="none" stroke="url(#cg)" stroke-width="7"/>

  {condensed(256, 300, "TG", 232, BONE, squeeze=.92, ls=-6)}

  <!-- claw slashes, confined to the monogram band -->
  <g clip-path="url(#cc)" opacity=".92">
    <path d="M 44 132 L 470 222 L 468 240 L 42 150 Z" fill="{BLOOD}"/>
    <path d="M 44 202 L 470 292 L 468 308 L 42 218 Z" fill="{BLOOD}"/>
    <path d="M 44 272 L 470 362 L 468 376 L 42 288 Z" fill="{BLOOD}"/>
  </g>

  {condensed(256, 412, "THE GRENDEL", 44, BONE, ls=3)}
  {condensed(256, 452, "FANTASY PREMIER LEAGUE", 15, "#8496B5", ls=4)}
</svg>'''


VARIANTS = {"grendel-crest-a": variant_a, "grendel-crest-b": variant_b, "grendel-crest-c": variant_c}
only = sys.argv[1:] or list(VARIANTS)
for name in only:
    svg = VARIANTS[name]()
    (OUT / f"{name}.svg").write_text(svg)
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(OUT / f"{name}.png"),
                     output_width=1024, output_height=1024)
    print("wrote", name)
