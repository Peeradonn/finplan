"""Chart series for the Final deck, read from the model's own output (figures/figure-data.md, written by
model/make_charts.py from Final/final_model.py), so a drawn line moves with the model as every {{key}} does.
make.py replaces each [[token]] in the slides before it fills the {{keys}}. Adapted from round2/series.py (11 Nov).

Slide 5, the parents' net worth (table "fin-storm-path"): the plan in a normal future against the 2030-31 scenario.
Chart box, in the slide's SVG units: x 2026 -> 2066 on PX0 -> PX1; y 0 -> VMAX (HK$M) on PY0 -> PY1.
Tokens:
  [[sp_normal]] [[sp_storm]]        polyline points of the two lines
  [[sp_gap]]                        polygon points of the area between them
  [[sp_x:2030]]                     x of a year;  [[sp_x:2030+12]] the same, 12 units to the right
  [[sp_yn:2032]] [[sp_ys:2032-18]]  y of the normal / storm line in that year (an offset in units, optional)
  [[sp_y:10]]                       y of a value in HK$M (gridlines)
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
X0, X1, PX0, PX1 = 2026, 2066, 64.0, 840.0
VMAX, PY0, PY1 = 32.0, 392.0, 44.0


def table(name):
    """Rows of the markdown table under the '## name' heading, as lists of cells."""
    text = open(DATA, encoding="utf-8").read()
    i = text.index("## " + name)
    rows = []
    for line in text[i:].split("\n")[1:]:
        if line.startswith("## "):
            break
        if line.startswith("|") and not re.match(r"\|\s*-", line):
            rows.append([c.strip() for c in line.strip("|").split("|")])
    return rows[1:]  # drop the header row


def x(year):
    return PX0 + (year - X0) / (X1 - X0) * (PX1 - PX0)


def y(v):
    return PY0 - v / VMAX * (PY0 - PY1)


def pts(seq):
    return " ".join(f"{x(t):.1f},{y(v):.1f}" for t, v in seq)


def money(key):
    """A '−HK$2.48M' value from numbers.json, as a size in HK$M."""
    s = json.load(open(NUMBERS, encoding="utf-8"))[key]
    return abs(float(re.sub(r"[^\d.]", "", s)))


def storm():
    rows = table("fin-storm-path")
    normal = {int(r[0]): float(r[1]) for r in rows}
    stormy = {int(r[0]): float(r[2]) for r in rows}
    years = sorted(normal)
    tok = {
        "sp_normal": pts((t, normal[t]) for t in years),
        "sp_storm": pts((t, stormy[t]) for t in years),
        "sp_gap": pts([(t, normal[t]) for t in years] + [(t, stormy[t]) for t in reversed(years)]),
    }
    # the gap at Carmen's 89, split by channel (each run on its own, so the parts are scaled to the gap they explain)
    end = years[-1]
    parts = [("port", money("fin_shockport_leg")), ("flat", money("fin_stormflat_leg")), ("biz", money("fin_stormbiz_leg"))]
    scale = (normal[end] - stormy[end]) / sum(v for _, v in parts)
    top, lab = normal[end], -1e9
    for name, v in parts:
        y0, y1 = y(top), y(top - v * scale)
        tok[f"sp_bar_{name}_y"], tok[f"sp_bar_{name}_h"] = f"{y0:.1f}", f"{y1 - y0:.1f}"
        tok[f"sp_bar_{name}_m"] = f"{(y0 + y1) / 2:.1f}"
        lab = max((y0 + y1) / 2, lab + 21)
        tok[f"sp_lab_{name}"] = f"{lab:.1f}"
        top -= v * scale
    return tok, normal, stormy


def fill(text):
    tok, normal, stormy = storm()

    def sub(m):
        name, arg, off = m.group(1), m.group(2), float(m.group(3) or 0)
        if arg is None:
            if name not in tok:
                raise KeyError("unknown series token [[%s]]" % name)
            return f"{float(tok[name]) + off:.1f}" if m.group(3) else tok[name]
        if name == "sp_x":
            v = x(int(arg))
        elif name == "sp_yn":
            v = y(normal[int(arg)])
        elif name == "sp_ys":
            v = y(stormy[int(arg)])
        elif name == "sp_y":
            v = y(float(arg))
        else:
            raise KeyError("unknown series token [[%s:%s]]" % (name, arg))
        return f"{v + off:.1f}"

    out = re.sub(r"\[\[([a-z0-9_]+)(?::(\d+(?:\.\d+)?))?([+-]\d+(?:\.\d+)?)?\]\]", sub, text)
    if "[[" in out:
        raise ValueError("unfilled series token near: " + out[out.index("[["):][:60])
    return out
