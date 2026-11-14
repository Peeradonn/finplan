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


def signed(key):
    """A '−HK$0.57M' or '+HK$0.51M' value from numbers.json, as a signed number in HK$M."""
    s = json.load(open(NUMBERS, encoding="utf-8"))[key]
    v = float(re.sub(r"[^\d.]", "", s))
    return -v if s.strip()[0] in "−-" else v


# slide 3: every decision on one measure (Pete, 13 Nov), as bars from zero in its SVG (units = px). Each decision's
# change in the children's median inheritance in a normal future (numbers.json fin_dot_*_n), against its ordinary choice.
BAR_ZERO, BAR_SCALE, BAR_MIN, BAR_MAX = 660.0, 230.0, 365.0, 800.0
# the gift: the recommended plan's scholarship for life, funded now (14 Nov, Final_Plan.md §5.3), when exported
BAR_KEY = {"gift": "fin_plan_gift_n"}
BARS = ("vans", "data", "values", "gift", "flat")
BROKEN = "flat"     # the one bar drawn broken (its value is printed on it): the rest keep a readable scale


def bars3():
    """[[b3_zero]]; for each decision [[b3_vans_l]] (left x), [[b3_vans_w]] (width), [[b3_vans_e]] (the outer end).
    The flat's bar is longer than the chart and is drawn from BAR_MIN with a break; any other bar must fit."""
    tok = {"b3_zero": f"{BAR_ZERO:.1f}"}
    for d in BARS:
        nums = json.load(open(NUMBERS, encoding="utf-8"))
        v = signed(BAR_KEY[d] if BAR_KEY.get(d) in nums else f"fin_dot_{d}_n")
        end = BAR_ZERO + v * BAR_SCALE
        if d == BROKEN:
            if end >= BAR_MIN:
                raise ValueError(f"slide 3: {d} at {v:+.2f} now fits; draw it unbroken (drop the break mark)")
            end = BAR_MIN
        elif not BAR_MIN <= end <= BAR_MAX:
            raise ValueError(f"slide 3: {d} at {v:+.2f} runs off the chart; change BAR_ZERO or BAR_SCALE")
        tok[f"b3_{d}_l"], tok[f"b3_{d}_w"] = f"{min(BAR_ZERO, end):.1f}", f"{abs(end - BAR_ZERO):.1f}"
        tok[f"b3_{d}_e"] = f"{end:.1f}"
    return tok


# slide 6: where the limit flips the flat's route (Pete, 13 Nov). In the 2030-31 downturn, the odds of each route as older
# flats fall 0-15% behind newer ones (numbers.json fin_flip_rmp_i, fin_flip_down_i at 0, 2.5 ... 15%), the limit of 85
# and the crossing (fin_flip_cross_x). Units = px in slide 6's SVG.
F6_X0, F6_X1, F6_Y0, F6_Y1, F6_LO, F6_HI = 70.0, 600.0, 330.0, 40.0, 80.0, 98.0


def flip6():
    """The downturn against 85 (fin_flip_*, a 2.5% grid) and, from 13 Nov night, a normal future against 95
    (fin_flipn_*, a 1% grid), where the normal limit binds first.
    [[f6_rmp]] [[f6_down]] (downturn) and [[f6n_rmp]] [[f6n_down]] (normal) polyline points; [[f6_rmp_ey]] etc. their
    ends' y; [[f6_cross]] [[f6n_cross]] each crossing's x, [[f6_cross_y]] the downturn crossing's y (on 85);
    [[f6n_shade_w]] the width from the normal crossing to the chart's end; [[f6_x0]] ... [[f6_x15]] and
    [[f6_y80]] [[f6_y85]] [[f6_y90]] [[f6_y95]] for the axes; [[f6_lim]] the y of 85, [[f6_limn]] of 95."""
    nums = json.load(open(NUMBERS, encoding="utf-8"))
    x = lambda d: F6_X0 + d / 15.0 * (F6_X1 - F6_X0)
    y = lambda v: F6_Y0 - (v - F6_LO) / (F6_HI - F6_LO) * (F6_Y0 - F6_Y1)
    tok = {}
    # f6/f6n: the family's plan as it stands (fin_flip*); p6/p6n: the recommended plan (fin_pflip*, 14 Nov), drawn on
    # the same axes. Each set only if its keys exist, so an older numbers.json still builds the v4 deck.
    sets = (("f6", "fin_flip"), ("p6", "fin_pflip"))
    for pre, key in sets:
        if f"{key}_cross_x" not in nums:
            continue
        for p2, k2, n, step in ((pre, key, 7, 2.5), (pre + "n", key + "n", 16, 1.0)):
            for line in ("rmp", "down"):
                vals = [float(nums[f"{k2}_{line}_{i}"].rstrip("%")) for i in range(n)]
                if not all(F6_LO <= v <= F6_HI for v in vals):
                    raise ValueError(f"slide 6: the {p2} {line} line runs off the chart; change F6_LO or F6_HI")
                tok[f"{p2}_{line}"] = " ".join(f"{x(step * i):.1f},{y(v):.1f}" for i, v in enumerate(vals))
                tok[f"{p2}_{line}_ey"] = f"{y(vals[-1]):.1f}"
        c, cn = float(nums[f"{key}_cross_x"]), float(nums[f"{key}n_cross_x"])
        tok[f"{pre}_cross"], tok[f"{pre}n_cross"] = f"{x(c):.1f}", f"{x(cn):.1f}"
        tok[f"{pre}n_shade_w"] = f"{F6_X1 - x(cn):.1f}"
        tok[f"{pre}_cross_y"] = f"{y(85):.1f}"
    for d in (0, 5, 10, 15):
        tok[f"f6_x{d}"] = f"{x(d):.1f}"
    for v in (80, 85, 90, 95):
        tok[f"f6_y{v}"] = f"{y(v):.1f}"
    tok["f6_lim"], tok["f6_limn"], tok["f6_cross_y"] = tok["f6_y85"], tok["f6_y95"], tok["f6_y85"]
    return tok


# backup: the headline taken apart (14 Nov, evening). The label approach's median inheritance, then each part in order,
# then our plan, on an axis from FW_LO to FW_HI HK$M (broken at the left: the bars start at FW_LO, not zero).
FW_X0, FW_X1, FW_LO, FW_HI = 470.0, 1130.0, 12.0, 13.5


def fair():
    """[[fw_x12]] ... [[fw_x135]] the ticks; [[fw_lab_w]] the label approach's bar from FW_X0; [[fw_vans_l]] [[fw_vans_w]],
    [[fw_gift_l]] [[fw_gift_w]], [[fw_fees_l]] [[fw_fees_w]] each part from where the last ended; [[fw_plan_w]] our plan."""
    nums = json.load(open(NUMBERS, encoding="utf-8"))
    if "fin_fair_lab_leg89" not in nums:
        return {}
    x = lambda v: FW_X0 + (v - FW_LO) / (FW_HI - FW_LO) * (FW_X1 - FW_X0)
    lab, plan = signed("fin_fair_lab_leg89"), signed("fin_plan_leg89x")
    if not FW_LO < lab < plan < FW_HI:
        raise ValueError("headline backup: the ends left the axis; change FW_LO or FW_HI")
    tok = {"fw_lab_w": f"{x(lab) - FW_X0:.1f}", "fw_plan_w": f"{x(plan) - FW_X0:.1f}", "fw_plan_e": f"{x(plan):.1f}"}
    at = lab
    for k in ("vans", "gift", "fees"):
        v = signed(f"fin_fair_{k}")
        tok[f"fw_{k}_l"], tok[f"fw_{k}_w"], tok[f"fw_{k}_e"] = f"{x(at):.1f}", f"{x(at + v) - x(at):.1f}", f"{x(at + v):.1f}"
        at += v
    for v, name in ((12.0, "12"), (12.5, "125"), (13.0, "13"), (13.5, "135")):
        tok[f"fw_x{name}"] = f"{x(v):.1f}"
    return tok


# backup: if Adrian's job goes (14 Nov, evening), each run's odds in 100 as a bar from JB_X0, JB_PX px per point.
JB_X0, JB_PX = 360.0, 6.4


def job():
    """[[jb_none_n]] [[jb_none_s]] ... each bar's width (normal, downturn); [[jb_l95]] [[jb_l85]] [[jb_l0]] [[jb_l50]] x."""
    nums = json.load(open(NUMBERS, encoding="utf-8"))
    if "fin_job_none_odds" not in nums:
        return {}
    tok = {f"jb_l{v}": f"{JB_X0 + v * JB_PX:.1f}" for v in (0, 50, 85, 95, 100)}
    for k in ("none", "half", "fix"):
        for s, key in (("n", f"fin_job_{k}_odds"), ("s", f"fin_job_{k}_sodds")):
            tok[f"jb_{k}_{s}"] = f"{float(nums[key].rstrip('%')) * JB_PX:.1f}"
            tok[f"jb_{k}_{s}_e"] = f"{JB_X0 + float(nums[key].rstrip('%')) * JB_PX:.1f}"
    return tok


def fill(text):
    charts = {p: Chart(p) for p in BOX}
    tok = {}
    for p, c in charts.items():
        tok.update(c.tokens(p))
    tok.update(bars(charts["sp"]))
    tok.update(bars3())
    tok.update(flip6())
    tok.update(fair())
    tok.update(job())

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
