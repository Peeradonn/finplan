"""
Charts for the proposal, drawn from the model so every figure matches run_model.py.
Usage:  python3 make_charts.py      -> ../figures/*.png (300 dpi) and ../figures/figure-data.md

Style (dataviz method, print adaptation): one accent, validated 30 Sep 2026 — crimson #b3202f vs blue #2f6fa3
(categorical: Flexi vs Standard, raises vs lowers); dark/light crimson #8c1824/#d9737d (ordinal: to 89 vs 95;
portfolio vs home equity); crimson tints for the fan chart. Thin marks, hairline grid, sans text,
Times New Roman to match the document; no chart titles (the document's "Figure N:" caption carries the title), a data table for every chart.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import run_model as M

OUT = os.path.join(os.path.dirname(M.HERE), "figures")
os.makedirs(OUT, exist_ok=True)

ACC, ACC_D, ACC_L, ALT = "#b3202f", "#8c1824", "#d9737d", "#2f6fa3"
BLUE, AQUA = ACC, ACC_L                          # role aliases used below
SEQ = {"100": "#f6dde0", "200": "#ebb4ba", "450": ACC}
INK, INK2, MUTED, GRID, AXIS = "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
W = 6.3                                    # inches: A4 text width with 1-inch margins

plt.rcParams.update({
    "font.family": "serif", "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
    "font.size": 10.5, "text.color": INK, "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
    "axes.edgecolor": AXIS, "axes.linewidth": 0.8, "axes.grid": False, "grid.color": GRID, "grid.linewidth": 0.6,
    "figure.facecolor": "white", "axes.facecolor": "white", "savefig.dpi": 300, "legend.frameon": False,
})
DATA = []                                  # (figure, markdown table) for figure-data.md

def tidy(ax, grid_axis="x"):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(True, axis=grid_axis); ax.set_axisbelow(True)
    ax.tick_params(length=0)

def save(fig, name):
    fig.savefig(os.path.join(OUT, name), bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)

def pct(x):
    return f"{x:.0%}"

C89, C95, MIX2 = M.C89, M.C95, M.MIX2
FULL = M.full_plan()

# 1 ---------- decision ladder ----------
steps = M.ladder_steps() + [(f"+ Standard plan from {M.SWITCH_Y}", {**FULL, "med": M.SWITCH})]
short = ["Investments alone,\nmedical premiums on top",
         "+ spending falls to 70%\nafter Adrian's 84", "+ Carmen's business\nsold in 2039",
         "+ reverse mortgage\nfrom 2037", "+ MPF annuity\n(fixed HK$, single life)", "+ Standard plan\nfrom Adrian's 75"]
r89 = [M.sim(*MIX2, C89, **kw)[0] for _, kw in steps]
r95 = [M.sim(*MIX2, C95, **kw)[0] for _, kw in steps]
fig, ax = plt.subplots(figsize=(W, 3.1))
y = np.arange(len(steps))[::-1]; h = 0.34
ax.barh(y + h/2 + 0.02, r89, h, color=ACC_D, label="Money lasts to Carmen's 89")
ax.barh(y - h/2 - 0.02, r95, h, color=ACC_L, label="to Carmen's 95")
for yi, a, b in zip(y, r89, r95):
    ax.text(a + 0.01, yi + h/2 + 0.02, pct(a), va="center", fontsize=9, color=INK)
    ax.text(b + 0.01, yi - h/2 - 0.02, pct(b), va="center", fontsize=9, color=INK2)
ax.axhline(0.5, color=AXIS, lw=0.8)
ax.set_yticks(y, short, fontsize=9); ax.set_xlim(0, 1.08); ax.set_xticks(np.arange(0, 1.01, 0.25))
ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
ax.set_xlabel("Share of 10,000 simulated markets in which the money lasts")
tidy(ax); ax.legend(loc="lower center", bbox_to_anchor=(0.4, 1.0), ncol=2, fontsize=9)
save(fig, "decision-ladder.png")
DATA.append(("decision-ladder.png: decision ladder (mix 2, 40/60)",
             "| Step | to 89 | to 95 |\n|---|---|---|\n" +
             "\n".join(f"| {lbl} | {pct(a)} | {pct(b)} |" for (lbl, _), a, b in zip(steps, r89, r95))))

# 2 ---------- fan chart ----------
_, _, _, paths = M.sim(*MIX2, C95, **FULL, paths=True)
years = np.arange(M.BY + 1, C95 + 1)
real = paths / ((1 + M.CPI) ** np.arange(1, C95 - M.BY + 1))[:, None] / 1e6
q = {p: np.percentile(real, p, axis=1) for p in (10, 25, 50, 75, 90)}
fig, ax = plt.subplots(figsize=(W, 3.2))
ax.fill_between(years, q[10], q[90], color=SEQ["100"], lw=0, label="10th–90th percentile")
ax.fill_between(years, q[25], q[75], color=SEQ["200"], lw=0, label="25th–75th percentile")
ax.plot(years, q[50], color=BLUE, lw=2, solid_capstyle="round", label="Median")
for yr, lbl in ((M.RETA, "Adrian retires: annuity bought,\nmortgage cleared (2037)"), (C89, "Carmen 89")):
    ax.axvline(yr, color=AXIS, lw=0.8)
    ax.text(yr + 0.4, max(q[90])*0.98, lbl, fontsize=9, color=INK2, va="top")
ax.set_xlim(years[0], years[-1]); ax.set_ylim(0, None)
ax.set_ylabel("Portfolio, HK$ million (today's money)")
tidy(ax, "y"); ax.legend(loc="lower center", fontsize=9, bbox_to_anchor=(0.5, 1.02), ncol=3)
save(fig, "fan-chart.png")
pick = [2030, M.RETA, 2045, M.ALE, C89, C95]
DATA.append(("fan-chart.png: portfolio percentiles, full plan, HK$M today's money",
             "| Year | P10 | P25 | Median | P75 | P90 |\n|---|---|---|---|---|---|\n" +
             "\n".join(f"| {yr} | " + " | ".join(f"{q[p][yr - years[0]]:.1f}" for p in (10, 25, 50, 75, 90)) + " |"
                       for yr in pick)))

# 3 ---------- medical premiums ----------
yrs = np.arange(M.RETA, C95 + 1)
defl = lambda yr: (1 + M.CPI) ** (yr - M.BY)
fx = np.array([M.FLEXI.get(v, 0)/defl(v) for v in yrs]) / 1e3
st = np.array([M.STD.get(v, 0)/defl(v) for v in yrs]) / 1e3
fig, ax = plt.subplots(figsize=(W, 2.4))
ax.plot(yrs, fx, color=BLUE, lw=2, solid_capstyle="round", label="Flexi plan (median)")
ax.plot(yrs, st, color=ALT, lw=2, solid_capstyle="round", label="Standard plan (median)")
for arr, c in ((fx, INK), (st, INK2)):
    ax.plot(yrs[-1], arr[-1], "o", ms=5, color=BLUE if c == INK else ALT, mec="white", mew=1.5)
    ax.text(yrs[-1] + 0.6, arr[-1], f"HK${arr[-1]:.0f}K", va="center", fontsize=9, color=c)
ax.axvline(M.ALE, color=AXIS, lw=0.8)
ax.text(M.ALE + 0.6, max(fx)*0.92, "Adrian's life expectancy (84):\nhis premium stops", ha="left", va="top",
        fontsize=9, color=INK2)
ax.set_xticks([2037, 2045, 2055, 2066, 2072], ["2037\nC 60", "2045\nC 68", "2055\nC 78", "2066\nCarmen 89", "2072\nC 95"])
ax.set_ylabel("Both parents, HK$K a year\n(today's money)"); ax.set_ylim(0, None); ax.set_xlim(yrs[0], yrs[-1] + 4)
tidy(ax, "y"); ax.legend(loc="upper left", fontsize=9)
save(fig, "medical-premiums.png")
DATA.append(("medical-premiums.png: medical line net of HK$65K already in the HK$780K, HK$K today's money",
             "| Year | Carmen's age | Flexi | Standard |\n|---|---|---|---|\n" +
             "\n".join(f"| {v} | {v-1977} | {fx[v-yrs[0]]:.0f} | {st[v-yrs[0]]:.0f} |" for v in (2037, 2039, 2045, 2050, 2056, 2057, 2066, 2072))))

# 4 ---------- education by destination ----------
# HK$K a year at 2028/29 prices, from methodology §3d (not model inputs): (low, high, FX stress on the high end)
EDU = [("Hong Kong (case band)", 150, 250, 0.0), ("Singapore, with Tuition Grant", 224, 271, 0.19),
       ("Singapore, no grant", 332, 400, 0.19), ("United Kingdom", 335, 555, 0.10), ("Canada", 400, 554, 0.14)]
budget = M.EDU_A * (1 + M.EDU_ESC) ** (M.EDU_Y - M.BY) / 1e3
fig, ax = plt.subplots(figsize=(W, 2.8))
ax.axvspan(350, 600, color="#f0efec", lw=0)
ax.text(475, len(EDU) - 0.35, "Case band for overseas study,\nHK$350–600K", ha="center", fontsize=9, color=INK2)
for i, (lbl, lo, hi, s) in enumerate(EDU[::-1]):
    ax.barh(i, hi - lo, 0.34, left=lo, color=BLUE)
    if s:
        ax.barh(i, hi*s, 0.34, left=hi, color=SEQ["200"])
    ax.text(lo - 8, i, f"{lo}", va="center", ha="right", fontsize=9, color=INK2)
    end = hi*(1 + s)
    if budget - 45 < end < budget:           # too close to the budget line: label inside the bar end
        ax.text(end - 6, i, f"{end:.0f}", va="center", ha="right", fontsize=9, color=INK)
    else:
        ax.text(end + 8, i, f"{end:.0f}", va="center", fontsize=9, color=INK)
ax.axvline(budget, color=INK2, lw=1)
ax.text(budget + 6, -0.75, f"Model budget: {budget:.0f}K", fontsize=9, color=INK2, va="center")
ax.set_yticks(range(len(EDU)), [e[0] for e in EDU[::-1]], fontsize=9)
ax.set_xlim(0, 800); ax.set_ylim(-1.1, len(EDU) + 0.1); ax.set_xlabel("HK$K a year, 2028/29 prices")
tidy(ax)
from matplotlib.patches import Patch
ax.legend([Patch(color=BLUE), Patch(color=SEQ["200"])], ["Typical cost range", "Added by FX stress (95th percentile)"],
          loc="lower center", bbox_to_anchor=(0.5, 1.09), ncol=2, fontsize=9)
save(fig, "education-costs.png")
DATA.append(("education-costs.png: HK$K a year, 2028/29 prices (methodology §3d)",
             "| Destination | Low | High | FX stress | High after stress |\n|---|---|---|---|---|\n" +
             "\n".join(f"| {l} | {lo} | {hi} | {s:.0%} | {hi*(1+s):.0f} |" for l, lo, hi, s in EDU) +
             f"\n\nModel budget: HK$600K today, escalated 5% a year = HK${budget:.0f}K in {M.EDU_Y}/{M.EDU_Y % 100 + 1}."))

# 5 ---------- sensitivity tornado ----------
def run(kw=None, prem=None, rmp_y=None):
    old = (M.PREM, M.RMP_Y)
    if prem is not None: M.PREM = prem
    if rmp_y is not None: M.RMP_Y = rmp_y
    try:
        return M.sim(*MIX2, C89, **(kw or FULL))[0]
    finally:
        M.PREM, M.RMP_Y = old
base = run()
cases = [("Standard plan from Adrian's 75", run({**FULL, "med": M.SWITCH})),
         ("Equities 7% (not 6%)", run({**FULL, "r_eq": M.R_EQ + 0.01})),
         ("Equities 5%", run({**FULL, "r_eq": M.R_EQ - 0.01})),
         ("No MPF annuity", run({**FULL, "annuity": False})),
         ("Reverse mortgage from 2045 (not 2037)", run(rmp_y=2045)),
         ("Couple's spending continues after 2056", run({**FULL, "surv": 1.0})),
         ("Business not sold", run({**FULL, "biz": 0})),
         (f"CPI {M.ST_CPI:.1%} (not {M.CPI:.1%})", run({**FULL, "cpi": M.ST_CPI})),
         (f"Medical trend {M.M_ST:.1%} flat", run({**FULL, "med": M.STRESS}))]
cases.sort(key=lambda c: abs(c[1] - base))
fig, ax = plt.subplots(figsize=(W, 3.6))
for i, (lbl, v) in enumerate(cases):
    d = v - base
    ax.barh(i, d, 0.5, color=ALT if d >= 0 else ACC)
    ax.text(d + (0.008 if d >= 0 else -0.008), i, pct(v), va="center", ha="left" if d >= 0 else "right",
            fontsize=9, color=INK)
ax.axvline(0, color=INK2, lw=1)
ax.set_yticks(range(len(cases)), [c[0] for c in cases], fontsize=9)
ax.set_xlim(min(0, min(v - base for _, v in cases)) - 0.08, max(0, max(v - base for _, v in cases)) + 0.08)
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, _: f"{x*100:+.0f}pp" if x else f"{base:.0%}"))
ax.set_xlabel(f"Change in the chance the money lasts to Carmen's 89 (full plan = {base:.0%})")
tidy(ax)
from matplotlib.patches import Patch
ax.legend([Patch(color=ALT), Patch(color=ACC)], ["Raises the chance", "Lowers the chance"],
          loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2, fontsize=9)
save(fig, "sensitivity-tornado.png")
DATA.append((f"sensitivity-tornado.png: one change at a time to the full plan (base {base:.0%} to 89)",
             "| Change | Success to 89 | vs base |\n|---|---|---|\n" +
             "\n".join(f"| {l} | {pct(v)} | {100*(v-base):+.0f}pp |" for l, v in cases[::-1])))

# 6 ---------- stress scenarios ----------
SC = [("Full plan,\nbase assumptions", FULL, M.R_LAD),
      ("A. Low-return\ndecade", {**FULL, "r_eq": M.ST_EQ}, M.ST_BD),
      ("B. Inflation\nshock", {**FULL, "cpi": M.ST_CPI, "med": M.STRESS}, M.R_LAD),
      ("C. Medical costs\n8.5% a year", {**FULL, "med": M.STRESS}, M.R_LAD)]
s89 = [M.sim(MIX2[0], MIX2[1], rb, C89, **kw)[0] for _, kw, rb in SC]
s95 = [M.sim(MIX2[0], MIX2[1], rb, C95, **kw)[0] for _, kw, rb in SC]
fig, ax = plt.subplots(figsize=(W, 2.8))
x = np.arange(len(SC)); w = 0.3
ax.bar(x - w/2 - 0.02, s89, w, color=ACC_D, label="to Carmen's 89")
ax.bar(x + w/2 + 0.02, s95, w, color=ACC_L, label="to Carmen's 95")
for xi, a, b in zip(x, s89, s95):
    ax.text(xi - w/2 - 0.02, a + 0.02, pct(a), ha="center", fontsize=9, color=INK)
    ax.text(xi + w/2 + 0.02, b + 0.02, pct(b), ha="center", fontsize=9, color=INK2)
ax.set_xticks(x, [s[0] for s in SC], fontsize=9); ax.set_ylim(0, 1.05)
ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
tidy(ax, "y"); ax.legend(loc="upper right", fontsize=9, ncol=2)
save(fig, "stress-scenarios.png")
DATA.append(("stress-scenarios.png: full plan under the stress scenarios (methodology §5)",
             "| Scenario | to 89 | to 95 |\n|---|---|---|\n" +
             "\n".join(f"| {s[0].replace(chr(10), ' ')} | {pct(a)} | {pct(b)} |" for s, a, b in zip(SC, s89, s95)) +
             f"\n\nA: equities {M.ST_EQ:.1%}, ladder {M.ST_BD:.1%} · B: CPI {M.ST_CPI:.1%} with medical {M.M_ST:.2%} flat · C: medical {M.M_ST:.2%} flat (read the 95 column)."))

# 7 ---------- property options ----------
opts = M.property_options(C89)
labels = ["Keep the home", "Reverse mortgage\nfrom 2037", "Downsize\nin 2037"]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(W, 2.6), gridspec_kw={"wspace": 0.55})
yy = np.arange(3)[::-1]
a1.barh(yy, [o[1] for o in opts], 0.45, color=ACC_D)
for yi, o in zip(yy, opts):
    a1.text(o[1] + 0.02, yi, pct(o[1]), va="center", fontsize=9)
a1.set_yticks(yy, labels, fontsize=9); a1.set_xlim(0, 1.15)
a1.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
a1.set_xlabel("Money lasts to Carmen's 89"); tidy(a1)
pf = np.array([o[2] for o in opts])/1e6; he = np.array([o[3] for o in opts])/1e6
a2.barh(yy, pf, 0.45, color=ACC_D, label="Portfolio (median)")
a2.barh(yy, he, 0.45, left=pf + 0.08, color=AQUA, label="Home equity")
for yi, p, e in zip(yy, pf, he):
    a2.text(p + e + 0.3, yi, f"{p+e:.1f}M", va="center", fontsize=9)
a2.set_yticks(yy, [""]*3); a2.set_xlim(0, max(pf + he) * 1.25)
a2.set_xlabel("Left to heirs at Carmen's 89, HK$M today"); tidy(a2)
a2.legend(loc="lower center", bbox_to_anchor=(0.45, 1.0), ncol=2, fontsize=9)
save(fig, "property-options.png")
DATA.append(("property-options.png: annuity, survivor spending and business sale on; mix 2; HK$M today's money at Carmen's 89",
             "| Option | Success to 89 | Portfolio | Home equity | Legacy |\n|---|---|---|---|---|\n" +
             "\n".join(f"| {o[0]} | {pct(o[1])} | {o[2]/1e6:.1f} | {o[3]/1e6:.1f} | {(o[2]+o[3])/1e6:.1f} |" for o in opts)))

# ---------- half-width versions: drawn at print size (95mm) so text is not shrunk ----------
HW = 95 / 25.4                               # inches
with plt.rc_context({"font.size": 10.5}):
    # 1h decision ladder
    lab = ["Investments alone", "+ lower spending\nafter first death", "+ business sale",
           "+ home released", "+ MPF annuity", "+ Standard plan\nfrom 75"]
    fig, ax = plt.subplots(figsize=(HW, 3.2))
    y = np.arange(len(lab))[::-1]; h = 0.36
    ax.barh(y + h/2 + 0.02, r89, h, color=ACC_D, label="to Carmen's 89")
    ax.barh(y - h/2 - 0.02, r95, h, color=ACC_L, label="to 95")
    for yi, a, b in zip(y, r89, r95):
        ax.text(a + 0.015, yi + h/2 + 0.02, pct(a), va="center", fontsize=10, color=INK)
        ax.text(b + 0.015, yi - h/2 - 0.02, pct(b), va="center", fontsize=10, color=INK2)
    ax.axhline(0.5, color=AXIS, lw=0.8)
    ax.set_yticks(y, lab); ax.set_xlim(0, 1.12); ax.set_xticks([0, .5, 1])
    ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    tidy(ax); ax.legend(loc="lower center", bbox_to_anchor=(0.35, 1.0), ncol=2, handlelength=1.2)
    save(fig, "decision-ladder-half.png")

    # 3h medical premiums
    fig, ax = plt.subplots(figsize=(HW, 2.5))
    ax.plot(yrs, fx, color=ACC, lw=1.8, solid_capstyle="round", label="Flexi")
    ax.plot(yrs, st, color=ALT, lw=1.8, solid_capstyle="round", label="Standard")
    for arr, col in ((fx, ACC), (st, ALT)):
        ax.plot(yrs[-1], arr[-1], "o", ms=4, color=col, mec="white", mew=1.2)
        ax.text(yrs[-1] + 0.8, arr[-1], f"{arr[-1]:.0f}K", va="center", fontsize=10, color=INK)
    ax.axvline(M.ALE, color=AXIS, lw=0.8)
    ax.text(M.ALE + 0.6, max(fx)*0.97, "Adrian 84:\nhis premium stops", va="top", fontsize=8.5, color=INK2)
    ax.set_xticks([2037, 2050, 2066], ["2037", "2050", "2066\nCarmen 89"])
    ax.set_ylabel("HK$K a year, today's money"); ax.set_ylim(0, None); ax.set_xlim(yrs[0], yrs[-1] + 6)
    tidy(ax, "y"); ax.legend(loc="upper left", handlelength=1.2)
    save(fig, "medical-premiums-half.png")

    # 2h fan chart, same size as the medical chart so the two can sit side by side
    fig, ax = plt.subplots(figsize=(HW, 2.5))
    ax.fill_between(years, q[10], q[90], color=SEQ["100"], lw=0, label="Middle 80%")
    ax.fill_between(years, q[25], q[75], color=SEQ["200"], lw=0, label="Middle 50%")
    ax.plot(years, q[50], color=ACC, lw=1.8, solid_capstyle="round", label="Median")
    ax.axvline(M.RETA, color=AXIS, lw=0.8)
    ax.text(M.RETA - 0.6, 0.6, "Annuity\nbought,\nmortgage\ncleared", ha="right", va="bottom", fontsize=9.5, color=INK2)
    ax.set_xticks([2030, 2037, 2050, 2066], ["2030", "2037", "2050", "2066\nCarmen 89"])
    ax.set_xlim(years[0], C89 + 1); ax.set_ylim(0, None)
    ax.set_ylabel("HK$M, today's money")
    tidy(ax, "y"); ax.legend(loc="upper right", handlelength=1.2, fontsize=9)
    save(fig, "fan-chart-half.png")

# ---------- more half-width charts (95mm), for the ANNOT and PAIR layouts ----------
RAMP = ["#e3a1a8", "#c24a56", "#8c1824"]          # cash · bonds · equity: ordered by risk, validated 30 Sep
with plt.rc_context({"font.size": 10.5}):
    # Figure 3: where each year's income goes (parents, low bonus, 2026/27 tax)
    tx = M.WB["Tax"]
    steps_w = [("Income", tx["B23"].value), ("Salaries\ntax", tx["B24"].value), ("MPF", tx["B25"].value),
               ("Spending", tx["B26"].value), ("Surplus", tx["B27"].value)]
    fig, ax = plt.subplots(figsize=(HW, 2.9))
    level = 0
    for i, (lab_, v) in enumerate(steps_w):
        if i == 0 or i == len(steps_w) - 1:
            bottom, height, col = 0, v, (ACC_D if i == 0 else ACC)
        else:
            bottom, height, col = level + v, -v, ACC_L
        ax.bar(i, height/1e3, 0.6, bottom=bottom/1e3, color=col)
        ax.text(i, (bottom + height)/1e3 + 25, f"{abs(v)/1e3:,.0f}K", ha="center", fontsize=10, color=INK)
        level = v if i == 0 else (level + v if i < len(steps_w) - 1 else level)
    ax.set_xticks(range(len(steps_w)), [s_[0] for s_ in steps_w]); ax.set_ylabel("HK$K a year")
    ax.set_ylim(0, steps_w[0][1]/1e3 * 1.12); tidy(ax, "y")
    save(fig, "cashflow-half.png")
    DATA.append(("cashflow-half.png: parents' annual cash flow, low bonus (Tax tab)",
                 "| Step | HK$ |\n|---|---|\n" + "\n".join(f"| {l.replace(chr(10), ' ')} | {v:,.0f} |" for l, v in steps_w)))

    # Figure 12: education cost by destination, 2028/29 prices
    fig, ax = plt.subplots(figsize=(HW, 2.9))
    ax.axvspan(350, 600, color="#f0efec", lw=0)
    for i, (lbl, lo, hi, st_) in enumerate(EDU[::-1]):
        ax.barh(i, hi - lo, 0.42, left=lo, color=ACC)
        if st_:
            ax.barh(i, hi*st_, 0.42, left=hi, color=SEQ["200"])
        end_ = hi*(1 + st_)
        xl = budget + 8 if budget - 45 < end_ + 10 < budget + 45 else end_ + 10   # keep labels off the budget line
        ax.text(xl, i, f"{end_:.0f}", va="center", fontsize=10, color=INK)
    ax.axvline(budget, color=INK2, lw=1)
    ax.text(budget + 6, -0.55, f"Budget {budget:.0f}K", ha="left", va="center", fontsize=9.5, color=INK2)
    short_edu = ["Hong Kong", "Singapore\n(grant)", "Singapore", "UK", "Canada"]
    ax.set_yticks(range(len(EDU)), short_edu[::-1]); ax.set_xlim(0, 790); ax.set_ylim(-0.85, len(EDU) - 0.4)
    ax.set_xlabel("HK$K a year, 2028/29 prices"); tidy(ax)
    from matplotlib.patches import Patch
    ax.legend([Patch(color=ACC), Patch(color=SEQ["200"])], ["Cost range", "+ FX stress"],
              loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=2, handlelength=1.2)
    save(fig, "education-costs-half.png")

    # Figure 13: today's holdings vs the target (parents' freely allocable money: liquid + non-MPF investments)
    bs = {"cash": 620_000 + 1_480_000 + 400_000,
          "bonds": 900_000 + 450_000,
          "equity": 1_000_000 + 1_350_000 + 700_000 + 800_000}                  # case statement
    total = sum(bs.values())
    emergency, edu_fund = 1_000_000, M.edu_res
    each = (total - emergency - edu_fund) / 2                                    # long-term, split 50:50
    ADRIAN = {"cash": .05, "bonds": .55, "equity": .40}                          # Win's table
    CARMEN = {"cash": .07, "bonds": .33, "equity": .60}                          # decision 3 (2% digital held as cash)
    tgt = {k: ADRIAN[k]*each + CARMEN[k]*each for k in bs}
    tgt["cash"] += emergency + edu_fund/2; tgt["bonds"] += edu_fund/2          # education: deposits, then short bonds
    fig, ax = plt.subplots(figsize=(HW, 1.9))
    for row, (lbl, d_) in enumerate((("Target", tgt), ("Today", bs))):
        left = 0
        for k, col in zip(("cash", "bonds", "equity"), RAMP):
            ax.barh(row, d_[k]/1e6, 0.55, left=left, color=col, edgecolor="white", linewidth=1.5)
            ax.text(left + d_[k]/2e6, row, f"{d_[k]/1e6:.1f}M", ha="center", va="center", fontsize=10,
                    color="white" if k != "cash" else INK)
            left += d_[k]/1e6
    ax.set_yticks([0, 1], ["Target", "Today"]); ax.set_xlim(0, total/1e6); ax.set_xlabel("HK$M")
    tidy(ax)
    ax.legend([Patch(color=c) for c in RAMP], ["Cash and deposits", "Bonds", "Equity"],
              loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=3, handlelength=1.2)
    save(fig, "allocation-half.png")
    DATA.append(("allocation-half.png: parents' freely allocable money, HK$",
                 "| | Cash | Bonds | Equity |\n|---|---|---|---|\n" +
                 f"| Today | {bs['cash']:,.0f} | {bs['bonds']:,.0f} | {bs['equity']:,.0f} |\n"
                 f"| Target | {tgt['cash']:,.0f} | {tgt['bonds']:,.0f} | {tgt['equity']:,.0f} |\n\n"
                 f"Target = emergency {emergency:,.0f} + education {edu_fund:,.0f} (half deposits, half short bonds) + "
                 f"Adrian {each:,.0f} at 40/55/5 + Carmen {each:,.0f} at 60/33/7 (equity/bonds/cash)."))

    # Figure 20: property options, legacy with success labelled
    fig, ax = plt.subplots(figsize=(HW, 2.2))
    yy = np.arange(3)[::-1]; lab_p = ["Keep the home", "Reverse mortgage", "Downsize"]
    pf = np.array([o[2] for o in opts])/1e6; he = np.array([o[3] for o in opts])/1e6
    ax.barh(yy, pf, 0.5, color=ACC_D, label="Portfolio")
    ax.barh(yy, he, 0.5, left=pf, color=ACC_L, edgecolor="white", linewidth=1.5, label="Home equity")
    for yi, p_, e_, o in zip(yy, pf, he, opts):
        ax.text(p_ + e_ + 0.3, yi, f"{p_ + e_:.1f}M · lasts {pct(o[1])}", va="center", fontsize=10, color=INK)
    ax.set_yticks(yy, lab_p); ax.set_xlim(0, max(pf + he)*1.6); ax.set_xlabel("Left to heirs at Carmen's 89, HK$M today")
    tidy(ax); ax.legend(loc="lower center", bbox_to_anchor=(0.4, 1.02), ncol=2, handlelength=1.2)
    save(fig, "property-options-half.png")

    # Figures 26-27: stress scenarios and sensitivity, same size so they pair.
    # The half chart compares fixed spending with the recommended plan (tier review at 75 + guardrails), to 89.
    def rec_kw(kw):
        return {**kw, "med": M.SWITCH_ST if kw.get("med") is M.STRESS else M.SWITCH, "guard": True}
    r89 = [M.sim(MIX2[0], MIX2[1], rb, C89, **rec_kw(kw))[0] for _, kw, rb in SC]
    fig, ax = plt.subplots(figsize=(HW, 2.6))
    x = np.arange(len(SC)); w_ = 0.36
    ax.bar(x - w_/2 - 0.02, s89, w_, color=ACC, label="Fixed spending")
    ax.bar(x + w_/2 + 0.02, r89, w_, color=ALT, label="Our rules")
    for xi, a_, b_ in zip(x, s89, r89):
        ax.text(xi - w_/2 - 0.02, a_ + 0.02, pct(a_), ha="center", fontsize=9.5, color=INK)
        ax.text(xi + w_/2 + 0.02, b_ + 0.02, pct(b_), ha="center", fontsize=9.5, color=INK)
    ax.set_xticks(x, ["Base", "Low-return\ndecade", "Inflation\nshock", "Medical\n8.5% a year"])
    ax.set_ylim(0, 1.3); ax.set_yticks([0, .25, .5, .75, 1])
    ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    tidy(ax, "y"); ax.legend(loc="upper center", ncol=2, handlelength=1.2, bbox_to_anchor=(0.5, 1.02))
    save(fig, "stress-half.png")
    DATA.append(("stress-half.png: chance the money lasts to Carmen's 89, fixed spending vs the recommended plan "
                 "(Standard plan from Adrian's 75 + guardrails)",
                 "| Scenario | Fixed spending | Recommended plan |\n|---|---|---|\n" +
                 "\n".join(f"| {s[0].replace(chr(10), ' ')} | {pct(a_)} | {pct(b_)} |" for s, a_, b_ in zip(SC, s89, r89))))

    SHORT = {"CPI": "Inflation 3.5%", "Medical trend": "Medical 8.5% a year", "Business not sold": "Business not sold",
             "Standard plan": "Standard plan from 75", "Couple's spending": "No spending drop at 84",
             "Equities 5%": "Equities 5%", "Reverse mortgage": "Reverse mortgage 2045", "Equities 7%": "Equities 7%",
             "No MPF annuity": "No MPF annuity"}
    def short_lbl(l):
        return next((v for k, v in SHORT.items() if l.startswith(k)), l)
    fig, ax = plt.subplots(figsize=(HW, 2.6))
    for i, (lbl, v) in enumerate(cases):
        d_ = v - base
        ax.barh(i, d_, 0.55, color=ALT if d_ >= 0 else ACC)
        ax.text(d_ + (0.008 if d_ >= 0 else -0.008), i, pct(v), va="center", ha="left" if d_ >= 0 else "right",
                fontsize=9.5, color=INK)
    ax.axvline(0, color=INK2, lw=1)
    ax.set_yticks(range(len(cases)), [short_lbl(c[0]) for c in cases], fontsize=9.5)
    ax.set_xlim(min(v - base for _, v in cases) - 0.12, max(v - base for _, v in cases) + 0.1)
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x_, _: f"{x_*100:+.0f}" if x_ else f"{base:.0%}"))
    ax.set_xlabel("Points, from the full plan"); tidy(ax)
    save(fig, "sensitivity-half.png")

# ---------- data twin ----------
with open(os.path.join(OUT, "figure-data.md"), "w", encoding="utf-8") as f:
    f.write("# Figure data\n\nGenerated by `model/make_charts.py` from `model/wong_model.xlsx`. "
            "Do not edit by hand; rerun the script.\nEvery chart's numbers, for captions, text and checking.\n")
    for title, table in DATA:
        f.write(f"\n## {title}\n\n{table}\n")
import json
NUM = M.export_numbers()
with open(os.path.join(OUT, "numbers.json"), "w", encoding="utf-8") as f:
    json.dump(NUM, f, indent=1, ensure_ascii=False)
print(f"Wrote {len(DATA)} charts, figure-data.md and numbers.json ({len(NUM)} values) to {OUT}")
