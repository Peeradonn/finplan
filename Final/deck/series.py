"""Chart series for the Final deck, read from the model's own output (figures/figure-data.md, written by
model/make_charts.py from Final/final_model.py), so a drawn line moves with the model as every {{key}} does.
make.py replaces each [[token]] in the slides before it fills the {{keys}}. Adapted from round2/series.py (11 Nov).

Two charts, each a net worth by year, a normal future against the 2030-31 storm, each with its own box (SVG units):
  sp  backup 12, the plan (table "fin-storm-path")
  lp  slide 1, the family that followed the labels (table "fin-label-path")
Tokens, with sp or lp in front:
  [[sp_normal]] [[sp_storm]]        polyline points of the two lines
  [[sp_gap]]                        polygon points of the area between them
  [[sp_x:2030]]                     x of a year;  [[sp_x:2030+12]] the same, 12 units to the right
  [[sp_yn:2032]] [[sp_ys:2032-18]]  y of the normal / storm line in that year (an offset in units, optional)
  [[sp_y:10]]                       y of a value in HK$M (gridlines)
Backup 12 only:
  [[sp_bar_port_y]] [[sp_bar_port_h]] (and _flat_, _biz_)   the gap at Carmen's 89, split by channel
  [[sp_bar_port_m]] [[sp_lab_port]]  the middle of that part; its label's y, spread so labels never overlap
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(ROOT, "figures", "figure-data.md")
NUMBERS = os.path.join(ROOT, "figures", "numbers.json")
X0, X1 = 2026, 2066
# per chart: table, x of 2026 and 2066, y of HK$0 and of VMAX, VMAX
BOX = {"sp": ("fin-storm-path", 64.0, 840.0, 392.0, 44.0, 32.0),
       "lp": ("fin-label-path", 56.0, 680.0, 452.0, 72.0, 32.0)}


def table(name):
    """Rows of the markdown table under the '## name' heading, as lists of cells."""
    text = open(DATA, encoding="utf-8").read()
    i = text.index("## " + name + ":")
    rows = []
    for line in text[i:].split("\n")[1:]:
        if line.startswith("## "):
            break
        if line.startswith("|") and not re.match(r"\|\s*-", line):
            rows.append([c.strip() for c in line.strip("|").split("|")])
    return rows[1:]  # drop the header row


def money(key):
    """A '−HK$2.48M' value from numbers.json, as a size in HK$M."""
    s = json.load(open(NUMBERS, encoding="utf-8"))[key]
    return abs(float(re.sub(r"[^\d.]", "", s)))


class Chart:
    def __init__(self, prefix):
        name, self.px0, self.px1, self.py0, self.py1, self.vmax = BOX[prefix]
        rows = table(name)
        self.normal = {int(r[0]): float(r[1]) for r in rows}
        self.storm = {int(r[0]): float(r[2]) for r in rows}
        self.years = sorted(self.normal)

    def x(self, year):
        return self.px0 + (year - X0) / (X1 - X0) * (self.px1 - self.px0)

    def y(self, v):
        return self.py0 - v / self.vmax * (self.py0 - self.py1)

    def pts(self, seq):
        return " ".join(f"{self.x(t):.1f},{self.y(v):.1f}" for t, v in seq)

    def tokens(self, p):
        n, s, ys = self.normal, self.storm, self.years
        return {f"{p}_normal": self.pts((t, n[t]) for t in ys),
                f"{p}_storm": self.pts((t, s[t]) for t in ys),
                f"{p}_gap": self.pts([(t, n[t]) for t in ys] + [(t, s[t]) for t in reversed(ys)])}


def bars(c):
    """Backup 12: the gap at Carmen's 89, split by channel (each run on its own, so scaled to the gap they explain)."""
    tok = {}
    end = c.years[-1]
    parts = [("port", money("fin_shockport_leg")), ("flat", money("fin_stormflat_leg")), ("biz", money("fin_stormbiz_leg"))]
    scale = (c.normal[end] - c.storm[end]) / sum(v for _, v in parts)
    top, lab = c.normal[end], -1e9
    for name, v in parts:
        y0, y1 = c.y(top), c.y(top - v * scale)
        tok[f"sp_bar_{name}_y"], tok[f"sp_bar_{name}_h"] = f"{y0:.1f}", f"{y1 - y0:.1f}"
        tok[f"sp_bar_{name}_m"] = f"{(y0 + y1) / 2:.1f}"
        lab = max((y0 + y1) / 2, lab + 21)
        tok[f"sp_lab_{name}"] = f"{lab:.1f}"
        top -= v * scale
    return tok


def fill(text):
    charts = {p: Chart(p) for p in BOX}
    tok = {}
    for p, c in charts.items():
        tok.update(c.tokens(p))
    tok.update(bars(charts["sp"]))

    def sub(m):
        name, arg, off = m.group(1), m.group(2), float(m.group(3) or 0)
        if arg is None:
            if name not in tok:
                raise KeyError("unknown series token [[%s]]" % name)
            return f"{float(tok[name]) + off:.1f}" if m.group(3) else tok[name]
        p, _, kind = name.partition("_")
        c = charts.get(p)
        if c is None or kind not in ("x", "yn", "ys", "y"):
            raise KeyError("unknown series token [[%s:%s]]" % (name, arg))
        if kind == "x":
            v = c.x(int(arg))
        elif kind == "yn":
            v = c.y(c.normal[int(arg)])
        elif kind == "ys":
            v = c.y(c.storm[int(arg)])
        else:
            v = c.y(float(arg))
        return f"{v + off:.1f}"

    out = re.sub(r"\[\[([a-z0-9_]+)(?::(\d+(?:\.\d+)?))?([+-]\d+(?:\.\d+)?)?\]\]", sub, text)
    if "[[" in out:
        raise ValueError("unfilled series token near: " + out[out.index("[["):][:60])
    return out
