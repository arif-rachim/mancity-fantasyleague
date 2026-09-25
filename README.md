# mancity-fantasyleague

This repository holds the planning notes for a Fantasy Premier League (FPL) team, "The Grendel", for the 2026/27 season. It is not an app. It is a Markdown planning document, plus two small Python scripts for graphics. The document keeps the reasoning behind each squad decision in one place, so choices about transfers and chips can be checked against the original plan later in the season. The main document is the Gameweek 1 plan. It covers this season's scoring rules, including Defensive Contribution (DefCon) points, and ranks fixture difficulty for GW1 to GW6. It then sets out the final 15-player squad within the £100.0m budget, with captain and vice-captain picks, a transfer plan for GW1 to GW8, a chip plan for the first half of the season, a watchlist and a list of known risks. Prices, ownership and statistics come from the official FPL API, pulled on 19 August 2026. The scripts use Pillow and CairoSVG to render a pitch graphic of the squad and the team's crest variants. The repo covers Gameweek 1 so far, and the plan itself is written in Indonesian.

> Status: in use for the 2026/27 season. Only the Gameweek 1 plan exists so far.

## Contents

| Path | Description |
| --- | --- |
| [`docs/2026-27/gw1-plan.md`](docs/2026-27/gw1-plan.md) | Gameweek 1 plan (Indonesian): season rules, GW1–6 fixture analysis, selection principles, final squad, captaincy, GW1–8 transfer plan, first-half chip plan, watchlist, risks and a pre-deadline checklist |
| [`docs/2026-27/gw1-squad.png`](docs/2026-27/gw1-squad.png) | Pitch graphic of the GW1 3-4-3 lineup and bench |
| [`docs/2026-27/render_squad.py`](docs/2026-27/render_squad.py) | Pillow script that draws `gw1-squad.png` |
| [`docs/brand/`](docs/brand) | "The Grendel" crest variants A, B and C (SVG and PNG), an overview image of the options, and the script that generates them (`render_crest.py`) |

## 2026/27 season info

- GW1 deadline: **Friday, 21 August 2026, 17:30 UTC** (18:30 BST)
- Budget: **£100.0m** for 15 players (2 GKP / 5 DEF / 5 MID / 3 FWD)
- Maximum of **3 players per club**
- The first set of chips (Wildcard, Free Hit, Triple Captain, Bench Boost) expires at the GW19 deadline, 2 January, 13:30 GMT
- Free transfers can be banked up to 5

The data source for prices, ownership and statistics is the official FPL API
(`https://fantasy.premierleague.com/api/bootstrap-static/` and `/api/fixtures/`),
pulled on 19 August 2026. Points, minutes and DefCon figures in the plan are 2025/26 season totals.

## Regenerating the graphics

Prerequisites: Python 3 with Pillow (squad graphic) or CairoSVG (crests), and the DejaVu fonts at `/usr/share/fonts/truetype/dejavu`.

```bash
pip install pillow cairosvg
python3 docs/2026-27/render_squad.py     # writes gw1-squad.png
python3 docs/brand/render_crest.py       # writes all crest variants
python3 docs/brand/render_crest.py grendel-crest-a   # one variant only
```

The squad data is written directly in `render_squad.py`, in the `XI` and `BENCH` lists. Both scripts write to the absolute path `/home/user/mancity-fantasyleague/...`. Change the output path in the script if the repo is cloned somewhere else.

## Tech stack

Markdown · Python 3 · Pillow · CairoSVG
