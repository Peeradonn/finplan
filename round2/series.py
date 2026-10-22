"""Chart series for the deck, read from the model's own output (figures/figure-data.md), so a drawn line moves with
the model like every {{placeholder}} does. make.py replaces each [[token]] in the built deck with the value here.

The medical-premium line (slides 4 and 7): HK$K a year in today's money, above the HK$65K the HK$780K budget already
holds. "Flexi" is the plan bought now, kept for life; the recommended path is Flexi until the review at Adrian's 75
(2047) and the Standard plan after. Chart box: x 2037 -> 2066 (Carmen 60 -> 89) on 0..1000, y 0 -> 400 on 300..0.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "figures", "figure-data.md")
X0, X1, VMAX, W, H = 2037, 2066, 400.0, 1000.0, 300.0
SWITCH = 2047


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


def premiums():
    rows = [r for r in table("medical-premiums.png") if X0 <= int(r[0]) <= X1]
    return [(int(r[0]), float(r[2]), float(r[3])) for r in rows]  # year, Flexi, Standard


def at(pts, year):
    """Straight-line value between the table's years (what a drawn line shows anyway)."""
    for (y0, v0), (y1, v1) in zip(pts, pts[1:]):
        if y0 <= year <= y1:
            return v0 + (v1 - v0) * (year - y0) / (y1 - y0)
    raise ValueError(year)


def xy(year, v):
    return round((year - X0) / (X1 - X0) * W, 1), round(H - v / VMAX * H, 1)


def pts(seq):
    return " ".join(f"{x},{y}" for x, y in (xy(yr, v) for yr, v in seq))


def tokens():
    p = premiums()
    flexi = [(y, f) for y, f, s in p]
    std = [(y, s) for y, f, s in p]
    before = [(y, f) for y, f in flexi if y < SWITCH] + [(SWITCH, at(flexi, SWITCH))]
    after = [(SWITCH, at(std, SWITCH))] + [(y, s) for y, s in std if y > SWITCH]
    rec = before + after
    flexi_after = [(SWITCH, at(flexi, SWITCH))] + [(y, f) for y, f in flexi if y > SWITCH]
    peak_y, peak_v = max(flexi, key=lambda t: t[1])
    std_peak = dict(std)[peak_y]
    px, py = xy(peak_y, peak_v)
    sx, sy = xy(peak_y, std_peak)
    T = {
        "prem_flexi_pts": pts(flexi),
        "prem_flexi_area": pts([(X0, 0)] + flexi + [(X1, 0)]),
        "prem_rec_pts": pts(rec),
        "prem_saving_poly": pts(flexi_after + list(reversed(after))),
        "prem_peak_year": str(peak_y),
        "prem_peak_v": f"HK${peak_v:.0f}K",
        "prem_peak_l": f"{px / W * 100:.2f}%",
        "prem_peak_t": f"{py / H * 100:.2f}%",
        "prem_std_v": f"HK${std_peak:.0f}K",
        "prem_std_t": f"{sy / H * 100:.2f}%",
        "prem_switch_l": f"{xy(SWITCH, 0)[0] / W * 100:.2f}%",
        "prem_rec_end_t": f"{xy(X1, rec[-1][1])[1] / H * 100:.2f}%",   # where the recommended line ends (its label)
    }
    return T


def fill(text):
    T = tokens()
    def sub(m):
        k = m.group(1)
        if k not in T:
            raise KeyError("unknown series token [[%s]]" % k)
        return T[k]
    return re.sub(r"\[\[([a-z0-9_]+)\]\]", sub, text)


if __name__ == "__main__":
    for k, v in tokens().items():
        print(k, "=", v)
