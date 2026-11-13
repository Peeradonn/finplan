"""Final Round price tags: EXPLORATORY runs on the Round One model (model/run_model.py), which this script
imports and never changes. Nothing here is a slide number until Pete moves it into export_numbers() and
logs it (CLAUDE.md "Numbers"; Final_Plan.md §3).

Run:  .venv/Scripts/python.exe Final/final_model.py      (from the repo root; writes Final/model_runs.md)

What it adds to the Round One model:
- sim_x(): the plan's simulation (no guardrails, as in ladder_5_89 and switch_89) with year-by-year return
  shocks, a spending price-level shock and a reverse-mortgage start year. With no shocks it must reproduce
  run_model.sim() exactly; the script checks this first and stops if not.
- The inheritance at Carmen's 89 including the flat (median and 10th percentile, today's money), as
  run_model.property_options() defines legacy: the portfolio left plus home equity.
- A price tag per decision (Final/Decision_List.md), on two bases: Round One's plan without the medical
  review (82.6%, the base the research briefs used) and with it (switch_89, the plan as presented).
- M8: each decision under the 2030-31 scenario on all channels at once (stressed()), against its value in a
  normal future, and the carbon data's cost inside the new plan.
"""
import functools, os, sys
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "model"))
import run_model as m  # noqa: E402  (loads model/wong_model.xlsx)

N, SEED = 10_000, 42
W_EQ, S_BD, R_BD = m.MIX2
END = m.C89
DEFL = (1 + m.CPI) ** (END - m.BY)


# ---------- the simulation, with hooks ----------
def sim_x(end=END, annuity=True, med=None, surv=1.0, biz=0, rmp=0, rmp_y=None, r_eq=None, cpi=None,
          inflows=None, ret_add=None, level=None, n=N, seed=SEED, track=None):
    """run_model.sim() without guardrails, plus: ret_add {year: (equity addend, bond addend)},
    level {year: factor} (a permanent price-level step on retirement spending from that year), rmp_y.
    track: a dict that receives the median pot at the start of each later year (nominal HK$), for slide 5's path.
    Returns (success share, pot at `end` per path)."""
    r_eq = m.R_EQ if r_eq is None else r_eq
    cpi = m.CPI if cpi is None else cpi
    rmp_y = m.RMP_Y if rmp_y is None else rmp_y
    med, inflows, ret_add, level = med or {}, inflows or {}, ret_add or {}, level or {}
    rng = np.random.default_rng(seed)
    pot = np.full(n, m.POOL, float)
    alive = np.ones(n, bool)
    lvl = 1.0
    for i in range(end - m.BY):
        y = m.BY + i
        r = W_EQ * rng.normal(r_eq, m.S_EQ, n) + (1 - W_EQ) * rng.normal(R_BD, S_BD, n)
        ea, ba = ret_add.get(y, (0.0, 0.0))
        r = r + W_EQ * ea + (1 - W_EQ) * ba
        pot = pot * (1 + r)
        if annuity and y == m.RETA:
            pot -= m.ANN_A_COST
        if annuity and y == m.RETC:
            pot -= m.ANN_C_COST
        if y == m.RETA:
            pot -= m.MORT
        pot += m.mpf_in(y)
        lvl *= level.get(y, 1.0)
        if y < m.RETA:
            pot += m.SURPLUS * (1 + m.WAGE) ** i - m.PREM
        else:
            target = m.SPEND * (1 + cpi) ** i * (surv if y > m.ALE else 1) * lvl
            income = (m.ann_income(y, annuity) + (rmp if rmp and y >= rmp_y else 0)
                      + (m.CARMEN_NET * (1 + m.WAGE) ** i if y < m.RETC else 0))
            pot += income - target
        if biz and y == m.BIZ_Y:
            pot += biz
        pot += inflows.get(y, 0)
        pot -= med.get(y, 0)
        pot = np.maximum(pot, 0)
        alive &= pot > 0
        if track is not None:
            track[y + 1] = float(np.median(pot))
    return alive.mean(), pot


# ---------- the flat ----------
def counted(v):
    """HKMC's value for the reverse mortgage: in full up to the cap, a share above it."""
    return min(v, m.RMP_CAP) + m.RMP_ABOVE * max(v - m.RMP_CAP, 0)


def flat_value(y, mult=lambda y: 1.0):
    return m.home_value(y) * mult(y)


def rmp_income(mult=lambda y: 1.0, start=None):
    """Level reverse-mortgage income, scaled from the model's HK$230K by HKMC's counted value."""
    start = start or m.RMP_Y
    return m.RMP * counted(flat_value(start, mult)) / counted(m.home_value(m.RMP_Y))


def rmp_balance_x(start, end, income, mult=lambda y: 1.0):
    """run_model.rmp_balance() with the flat's value multiplied by mult(start) for the upfront insurance."""
    bal = m.RMP_UP * counted(flat_value(start, mult))
    for _ in range(start, end + 1):
        bal = bal * (1 + m.RMP_R + m.RMP_INS) + income
    return bal


def downsize_release_x(y, mult=lambda y: 1.0):
    """run_model.downsize_release() with only the old flat's value multiplied (newer flats hold)."""
    sale, buy = flat_value(y, mult), m.DS_P * (1 + m.P_G) ** (y - m.BY)
    return sale - buy - buy * m.DS_STAMP - sale * m.DS_AG - m.DS_MOVE * (1 + m.CPI) ** (y - m.BY)


# ---------- one run, both measures ----------
def run(base, route="rmp", mult=lambda y: 1.0, **kw):
    """route 'rmp' (the plan) or 'down' (downsize in DS_Y). Returns odds, median and 10th-percentile
    inheritance at Carmen's 89 (portfolio + home equity, today's money, HK$M)."""
    args = dict(base)
    args.update(kw)
    if route == "rmp":
        inc = rmp_income(mult) if mult(m.RMP_Y) != 1.0 else args.get("rmp", m.RMP)
        args["rmp"] = inc
        s, pot = sim_x(**args)
        equity = max(flat_value(END, mult) - rmp_balance_x(m.RMP_Y, END, inc, mult), 0)
    else:
        args["rmp"] = 0
        flows = dict(args.get("inflows") or {})
        flows[m.DS_Y] = flows.get(m.DS_Y, 0) + downsize_release_x(m.DS_Y, mult)
        args["inflows"] = flows
        s, pot = sim_x(**args)
        equity = m.DS_P * (1 + m.P_G) ** (END - m.BY)
    return dict(odds=s, leg_med=(np.median(pot) + equity) / DEFL / 1e6,
                leg_p10=(np.percentile(pot, 10) + equity) / DEFL / 1e6)


def check_against_round_one():
    """sim_x must reproduce run_model.sim() exactly, and the inheritance must match numbers.json."""
    full = m.full_plan()
    for label, kw in [("ladder_5", full), ("switch", {**full, "med": m.SWITCH}),
                      ("inflows", {**full, "inflows": {2027: -300_000}}), ("r_eq", {**full, "r_eq": m.R_EQ - 0.005})]:
        s_ref, _, med_ref = m.sim(W_EQ, S_BD, R_BD, END, **kw)
        s, pot = sim_x(**kw)
        if abs(s - s_ref) > 1e-12 or abs(np.median(pot) - med_ref) > 1e-6:
            sys.exit(f"sim_x does not reproduce run_model.sim() for {label}: {s} vs {s_ref}")
    rows = {lbl.split(",")[0].split(" ")[0]: (s, mp, h) for lbl, s, mp, h in m.property_options(END)}
    leg_rmp = rows["Reverse"][1] + rows["Reverse"][2]
    mine = run(full)["leg_med"] * 1e6
    if abs(mine - leg_rmp) > 1:
        sys.exit(f"inheritance does not match property_options(): {mine:,.0f} vs {leg_rmp:,.0f}")
    return leg_rmp


# ---------- inputs for the price tags (ILLUSTRATIVE unless marked; sources in Final/Decision_List.md) ----------
SHARE = 0.5                      # Carmen's share of the business (decided, Pete, 9 Nov)
EQ_MULT = 5.6                    # equity value / net profit (area2_business.md §3a; no HK SME source)
TAX_KEEP = 0.835                 # after 16.5% profits tax at the margin
HAIRCUT = m.BIZ / 5_000_000      # the plan counts HK$3.0M of the HK$5.0M: 60%
def saving(diesel):
    """Vans + LED + air-con, HK$ a year: 4 vans × (2,500 L × diesel − HK$8,788 of power), LED HK$16,872,
    air-con HK$11,389 (area2_business.md §3)."""
    return 4 * (2_500 * diesel - 8_788) + 16_872 + 11_389


# Diesel: HK$31/L is the government's average after forecourt discounts, Aug 2026 (HK$30.91-31.51; LCQ11 Annex I,
# 7 Oct 2026); contract fleets pay less, unpublished. HK$37.93 is the pump list (4 Nov); HK$25 the low case.
SAVE, SAVE_LIST, SAVE_25 = saving(31.0), saving(37.93), saving(25.0)
STAKE_PER_PCT = 209_000          # Carmen's stake per 1% of sales lost (area2_business.md §3e)
FEE_SAVED = 18_175 - 8_528       # both portfolios' fees, Round One -> candidate A (area3_portfolio.md §3)
FEE_VALUES = 5_107               # price of values in fees against an all-plain twin (area3 §4)
TRACK_BAD = 26_600               # the climate sleeve's lag a year if the last five years repeat (area3 §4)
RELIEF = 0.17                    # salaries tax relief on cash gifts while earning (checked on each parent, 9 Nov)
# HKMC reverse mortgage, two borrowers, life, fixed rate, HK$ a month per HK$1M (HKMC table, March 2026): the
# youngest borrower's entry age counts, so Carmen's: 60 in 2037, 68 in 2045.
RMP_AGE_60, RMP_AGE_68 = 1_810, 2_470


DIV_FROM = 2033                  # the 5-year van loan (HK$1.5M, ≈HK$349K a year) takes the saving to 2032
# B3 carbon data: ≈HK$54-73K a year, paid by the business from 2027 (Final/Decision_List.md B3; ILLUSTRATIVE).
CARBON_LO, CARBON_HI = 54_000, 73_000


def rmp_from(base, year, income):
    """The plan with the reverse mortgage starting in `year` at a level `income`: odds and inheritance."""
    s, pot = sim_x(**{**base, "rmp": income, "rmp_y": year})
    equity = max(flat_value(END) - rmp_balance_x(year, END, income), 0)
    return dict(odds=s, leg_med=(np.median(pot) + equity) / DEFL / 1e6,
                leg_p10=(np.percentile(pot, 10) + equity) / DEFL / 1e6)


def sale_uplift(saving):
    return saving * TAX_KEEP * EQ_MULT * SHARE * HAIRCUT


def dividends(saving, start=DIV_FROM, end=m.BIZ_Y):
    """Carmen's half of the after-tax saving, paid out once the van loan is repaid, until the sale."""
    return {y: saving * TAX_KEEP * SHARE for y in range(start, end)}


def r_eq_for(pot_addend_hkd):
    """A HK$ amount a year on the pool, as a change in the expected equity return (equity is W_EQ of the mix)."""
    return m.R_EQ + (pot_addend_hkd / m.POOL) / W_EQ


def scholarship_as_written():
    """Round One: about HK$30K a year, rising with CPI, from cash flow, 2027 to 2065; relief while earning."""
    f = {}
    for y in range(2027, END):
        gift = 30_000 * (1 + m.CPI) ** (y - m.BY)
        f[y] = f.get(y, 0) - gift
        if y < m.RETC:
            f[y + 1] = f.get(y + 1, 0) + RELIEF * gift
    return f


def scholarship_funded():
    """A 20-year named fund: HK$240K in 2027 and 2028, relief credited the following year."""
    return {2027: -240_000, 2028: -240_000 + RELIEF * 240_000, 2029: RELIEF * 240_000}


# ---------- M9 (review, 12 Nov): fair comparisons for the headline and the values budget ----------
# The label approach's ESG equity core: the BOC-Prudential fund, 35% of Adrian's and 37% of Carmen's HK$2.07M
# (area3_portfolio.md §3), at Round One's 0.775%, which was never verified for this fund (area3 line 92).
BOC_SLEEVE = (0.35 + 0.37) * 2_070_000
BOC_FEE = 0.00775
REAL_R = 0.025                   # the scholarship's real return (area1_6_framework.md §7: the 2.5% row, 20 years ≈ HK$468K)
GIFT = 30_000                    # a year, today's money, CPI-linked


def label_core_at(fee):
    """The label approach's portfolio with its ESG core at `fee` instead of the unverified 0.775%: HK$ a year the
    base's return gains (negative if dearer). The base already carries the 0.775%."""
    return BOC_SLEEVE * (BOC_FEE - fee)


def pledge_for(years):
    """HK$30K a year, CPI-linked, from cash flow, from 2027 for `years` years; relief while earning, as written."""
    f = {}
    for y in range(2027, min(2027 + years, END)):
        gift = GIFT * (1 + m.CPI) ** (y - m.BY)
        f[y] = f.get(y, 0) - gift
        if y < m.RETC:
            f[y + 1] = f.get(y + 1, 0) + RELIEF * gift
    return f


def fund_size(years):
    """Capital that pays HK$30K a year in today's money for `years` years at REAL_R (area1_6 §7's formula)."""
    return GIFT * (1 - (1 + REAL_R) ** -years) / REAL_R


def funded_for(total):
    """A named fund given in two halves, 2027 and 2028, relief credited the following year (as scholarship_funded())."""
    h = total / 2
    return {2027: -h, 2028: -h + RELIEF * h, 2029: RELIEF * h}


def scenario():
    """'Late and sudden' (area4_property_scenario.md §5.1): shocks in 2030-31."""
    ret = {2030: (-0.10, -0.05), 2031: (-0.05, -0.01)}
    for y in range(2032, 2037):
        ret[y] = (0.0, 0.005)
    level = {2030: 1.02, 2031: 1.01}

    def mult(y):
        drag = (1 - 0.0015) ** max(y - m.BY, 0)
        shock = 1.0 if y < 2030 else (0.90 if y == 2030 else 0.85)
        return drag * shock
    flows = {2030: -100_000, 2031: -100_000}
    return dict(ret_add=ret, level=level, inflows=flows, biz=m.BIZ * 0.9), mult


def plus(*flows):
    """Sum {year: HK$} dicts, e.g. the scenario's draw cut and a decision's own flows."""
    out = {}
    for f in flows:
        for y, v in (f or {}).items():
            out[y] = out.get(y, 0) + v
    return out


def stressed(base, sc, mult, biz_add=0.0, flows=None, **kw):
    """M7's 'All together' (reverse-mortgage route) with a decision on top. biz_add (a change in the sale price)
    takes the scenario's cut like the rest of the sale; flows are added to the scenario's own. With no decision
    it is exactly run(base, 'rmp', mult, **sc)."""
    biz = sc["biz"] + biz_add * sc["biz"] / m.BIZ if biz_add else sc["biz"]
    return run(base, "rmp", mult, ret_add=sc["ret_add"], level=sc["level"],
               inflows=plus(sc["inflows"], flows), biz=biz, **kw)


# ---------- slide 5: the parents' net worth, year by year (Pete, 11 Nov) ----------
MORT0 = m.O["BalanceSheet.Mortgage"]                        # the case's balance sheet, 2026
MORT_R = m.I["Mortgage rate (for HLI deduction)"] / 12


def mortgage_owed(t):
    """The mortgage at the start of year t: the case's HK$1.8M in 2026, repaid monthly down to the model's balance in
    2037 (MORT), which the plan clears from the portfolio that year. The payment is the one that joins the two."""
    if t > m.RETA:
        return 0.0
    g, k, j = 1 + MORT_R, 12 * (m.RETA - m.BY), 12 * (t - m.BY)
    pay = (MORT0 * g ** k - m.MORT) * MORT_R / (g ** k - 1)
    return MORT0 * g ** j - pay * (g ** j - 1) / MORT_R


def net_worth_path(base, mult=lambda y: 1.0, biz_from=None, **kw):
    """The parents' net worth at the start of each year, 2026 to Carmen's 89 (HK$M, today's money; the median
    portfolio across the futures): the portfolio (after the children's education money), plus the flat less the
    mortgage and the reverse-mortgage loan, plus the business at its modelled sale price until it is sold (ILLUSTRATIVE
    before the sale: the model has no business value until then). The scenario's cut to the sale counts from
    biz_from. A point is the start of a year, so the flat carries the shocks of the years before it (mult(t − 1)):
    the 2030 shock shows at the start of 2031, inside 2030-31 on the chart, like the portfolio's. The last point
    uses mult(END), so it is run()'s median inheritance exactly (storm_path() checks it)."""
    args = dict(base)
    args.update(kw)
    inc = rmp_income(mult) if mult(m.RMP_Y) != 1.0 else args.get("rmp", m.RMP)
    args["rmp"] = inc
    track = {m.BY: float(m.POOL)}
    sim_x(track=track, **args)
    sale_before, sale_after = base.get("biz") or 0, args.get("biz") or 0
    out = {}
    for t in range(m.BY, END + 1):
        loan = rmp_balance_x(m.RMP_Y, t, inc, mult) if t > m.RMP_Y else 0.0
        flat = flat_value(t, mult) if t == END else m.home_value(t) * mult(t - 1)
        home = max(flat - loan, 0) - mortgage_owed(t)
        biz = (sale_after if biz_from and t >= biz_from else sale_before) if t <= m.BIZ_Y else 0.0
        out[t] = (track[t] + home + biz) / (1 + m.CPI) ** (t - m.BY) / 1e6
    return out


@functools.lru_cache(maxsize=None)
def storm_path():
    """Slide 5: the plan (the Final's base) in a normal future against M7's 'All together' (the 2030-31 scenario on
    every channel). Returns two {year: HK$M} dicts; stops if either path doesn't end at run()'s inheritance."""
    base = {**m.full_plan(), "med": m.SWITCH}
    sc, mult = scenario()
    a = net_worth_path(base)
    s = net_worth_path(base, mult, biz_from=min(sc["ret_add"]) + 1, **sc)   # the sale is worth less once 2030 is over
    for p, r in ((a, run(base)), (s, run(base, "rmp", mult, **sc))):
        if abs(p[END] - r["leg_med"]) > 1e-9:
            sys.exit(f"net_worth_path() does not end at run()'s inheritance: {p[END]} vs {r['leg_med']}")
    return a, s


@functools.lru_cache(maxsize=None)
def label_storm_path():
    """Slide 1 (the open, Pete 11 Nov): the family that followed the labels (the label approach: the plan plus the
    unfunded lifelong pledge, as in M8) in a normal future against the same 2030-31 scenario. Stops unless each path
    ends at run()'s and stressed()'s inheritance."""
    base = {**m.full_plan(), "med": m.SWITCH}
    sc, mult = scenario()
    pl = scholarship_as_written()
    a = net_worth_path(base, inflows=pl)
    s = net_worth_path(base, mult, biz_from=min(sc["ret_add"]) + 1, ret_add=sc["ret_add"], level=sc["level"],
                       inflows=plus(sc["inflows"], pl), biz=sc["biz"])
    for p, r in ((a, run(base, inflows=pl)), (s, stressed(base, sc, mult, flows=pl))):
        if abs(p[END] - r["leg_med"]) > 1e-9:
            sys.exit(f"label_storm_path() does not end at the label approach's inheritance: {p[END]} vs {r['leg_med']}")
    return a, s


def export_final_series():
    """The Final deck's chart series, as (heading, markdown table) for figures/figure-data.md (through
    run_model.final_series() and make_charts.py); Final/deck/series.py draws them."""
    out = []
    for name, what, (a, s) in (
            ("fin-storm-path", "backup 12 (cut slide 5). The parents' net worth at the start of each year (median "
             "portfolio, the flat less its loans, the business at its sale price until 2039), HK$M today's money: the "
             "plan in a normal future against the 2030-31 scenario on every channel (M7, All together)", storm_path()),
            ("fin-label-path", "slide 1. The same measure for the family that followed the labels (the label approach, "
             "as in M8): a normal future against the same 2030-31 scenario", label_storm_path())):
        rows = "\n".join(f"| {t} | {a[t]:.3f} | {s[t]:.3f} | {s[t] - a[t]:+.3f} |" for t in sorted(a))
        out.append((f"{name}: Final deck {what}", "| Year | Normal | Storm | Gap |\n|---|---|---|---|\n" + rows))
    return out


# ---------- the slides' numbers (into figures/numbers.json through run_model.export_numbers()) ----------
def export_final():
    """The Final deck's model numbers, formatted as printed, on the Final's base (`switch_89`, Pete 9 Nov). Added slide by
    slide (Final_Plan.md §4.5); every key starts with "fin_". Each is the change in the children's median inheritance at
    Carmen's 89 (today's HK$, including the flat), or in the odds (points), against the base."""
    base = {**m.full_plan(), "med": m.SWITCH}
    b = run(base)
    dM = lambda r: ("−" if r["leg_med"] < b["leg_med"] else "+") + f"HK${abs(r['leg_med'] - b['leg_med']):.2f}M"
    dP = lambda r: f"{(r['odds'] - b['odds']) * 100:+.1f}".replace("-", "−")
    out = {}
    # slide 4 (R and I): what each climate route does to the family's money, each on its own (M3, M6, M7)
    r = run(base, biz=m.BIZ - STAKE_PER_PCT * 10 * HAIRCUT)          # a customer worth 10% of sales leaves
    out["fin_cust10_leg"], out["fin_cust10_pts"] = dM(r), dP(r)
    r = run(base, "rmp", lambda y: 0.9 if y >= m.RMP_Y else 1.0)     # older flats fall behind: 10% lower from 2037
    out["fin_flat10_leg"], out["fin_flat10_pts"] = dM(r), dP(r)
    sc, mult = scenario()
    r = run(base, ret_add=sc["ret_add"], level=sc["level"])          # a late, sudden carbon policy: the portfolio
    out["fin_shockport_leg"], out["fin_shockport_pts"] = dM(r), dP(r)
    port = r
    # slide 5 (R, the whole household): the same scenario on the flat, the business, and all at once (M7)
    flat = run(base, "rmp", mult)
    out["fin_stormflat_leg"], out["fin_stormflat_pts"] = dM(flat), dP(flat)
    biz = run(base, biz=sc["biz"], inflows=sc["inflows"])
    out["fin_stormbiz_leg"], out["fin_stormbiz_pts"] = dM(biz), dP(biz)
    allr = run(base, "rmp", mult, **sc)
    out["fin_storm_leg"], out["fin_storm_pts"] = dM(allr), dP(allr)
    apart = sum(x["odds"] - b["odds"] for x in (port, flat, biz)) * 100
    out["fin_storm_apart_pts"] = f"{apart:+.1f}".replace("-", "−")
    out["fin_base_odds"], out["fin_storm_odds"] = f"{b['odds']:.1%}", f"{allr['odds']:.1%}"
    out["fin_base_leg89"], out["fin_storm_leg89"] = f"HK${b['leg_med']:.1f}M", f"HK${allr['leg_med']:.1f}M"
    a, s = storm_path()
    out["fin_storm_gap32"] = f"−HK${a[2032] - s[2032]:.1f}M"         # the gap once the two years are over
    # slide 1 (the open): the family that followed the labels, in the same storm
    pl = scholarship_as_written()
    ln = run(base, inflows=pl)
    lp = [x["leg_med"] - ln["leg_med"] for x in (
        run(base, inflows=pl, ret_add=sc["ret_add"], level=sc["level"]),        # the portfolio
        run(base, "rmp", mult, inflows=pl),                                     # the flat
        run(base, biz=sc["biz"], inflows=plus(sc["inflows"], pl)))]             # the business
    out["fin_lab_homebiz"] = f"{(lp[1] + lp[2]) / sum(lp):.0%}"     # share of the loss on the home and the business
    a, s = label_storm_path()
    out["fin_lab_gap32"] = f"HK${a[2032] - s[2032]:.1f}M"             # poorer within two years
    out["fin_lab_gap89"] = f"HK${a[END] - s[END]:.1f}M"               # what the children inherit, at the end
    # slide 3 (the answer, Pete 13 Nov: one measure for every decision): each decision against its best ordinary
    # alternative, in the children's median inheritance; _n a normal future (against the base), _s under the 2030-31
    # scenario (against the plan under it, as in M8). The flat is the reverse mortgage against downsizing.
    sg = lambda v: ("−" if v < 0 else "+") + f"HK${abs(v):.2f}M"
    st0 = stressed(base, sc, mult)
    up, dcut = sale_uplift(SAVE), sale_uplift(-CARBON_LO)
    for k, nkw, skw in (("vans", dict(biz=m.BIZ + up), dict(biz_add=up)),
                        ("div", dict(inflows=dividends(SAVE)), dict(flows=dividends(SAVE))),
                        ("values", dict(r_eq=r_eq_for(-FEE_VALUES)), dict(r_eq=r_eq_for(-FEE_VALUES))),
                        ("gift", dict(inflows=scholarship_funded()), dict(flows=scholarship_funded())),
                        ("data", dict(biz=m.BIZ + dcut), dict(biz_add=dcut))):
        out[f"fin_dot_{k}_n"] = sg(run(base, **nkw)["leg_med"] - b["leg_med"])
        out[f"fin_dot_{k}_s"] = sg(stressed(base, sc, mult, **skw)["leg_med"] - st0["leg_med"])
    down, down_s = run(base, "down"), run(base, "down", mult, **sc)
    out["fin_dot_flat_n"] = sg(b["leg_med"] - down["leg_med"])
    out["fin_dot_flat_s"] = sg(allr["leg_med"] - down_s["leg_med"])
    out["fin_dot_down_sodds"] = f"{down_s['odds']:.1%}"              # downsizing under the scenario: below the 85 floor
    out["fin_dot_down_s100"] = f"{round(down_s['odds'] * 100)}"      # the same in whole futures in 100 (slide 3's words)
    # slide 4 (P, Pete 13 Nov: the room above the limit; Final_Plan.md §5.4, M9c): the limit sizes the values budget
    # before anything is priced. From the plan with plain choices (plain funds, no giving, no vans), the room above the
    # 95-in-100 limit is the most values may cost; the ESG funds and the 20-year scholarship fund are what the parents
    # choose to use. Whole futures in 100 on the slide, so its arithmetic reads (98 - 95 = 3).
    plain = dict(r_eq=r_eq_for(FEE_SAVED + FEE_VALUES))
    p_n, p_s = run(base, **plain), stressed(base, sc, mult, **plain)
    u_n = run(base, r_eq=r_eq_for(FEE_SAVED), inflows=scholarship_funded())
    u_s = stressed(base, sc, mult, r_eq=r_eq_for(FEE_SAVED), flows=scholarship_funded())
    plain_in100 = round(p_n["odds"] * 100)
    out["fin_room_plain"] = f"{plain_in100}"                               # futures in 100, plain choices
    out["fin_room_pts"] = f"{plain_in100 - 95}"                            # room above the limit of 95
    out["fin_room_use"] = f"{(p_n['odds'] - u_n['odds']) * 100:.0f}"       # what the values choices use
    out["fin_room_use_hk"] = f"HK${p_n['leg_med'] - u_n['leg_med']:.1f}M"  # the same, in the children's median
    out["fin_room_plain_s"] = f"{p_s['odds']:.1%}"                         # notes: plain choices under the scenario
    out["fin_room_use_s"] = f"{(p_s['odds'] - u_s['odds']) * 100:.1f}"     # notes: what the choices use under it
    # storyline v5 (13 Nov, night). Slide 3: what the room buys, in giving funded now with the ESG tilt, and Carmen's
    # fuller wish against it (M11). Slide 4: Adrian's bonus lost in the downturn, against the plan in the scenario (M10a).
    tilt = dict(r_eq=r_eq_for(FEE_SAVED))
    gift = most_gift(base, tilt, sc, mult)
    out["fin_room_gift"], out["fin_room_gift_x"] = f"HK${gift / 1e6:.1f}M", f"{gift / 1e6:.2f}"
    both39 = gift_now(2 * fund_size(END - 2027))
    out["fin_room_both39_hk"] = f"HK${2 * fund_size(END - 2027) / 1e6:.2f}M"
    out["fin_room_both39_odds"] = f"{run(base, **dict(tilt, inflows=both39))['odds']:.1%}"
    two = plus(pledge_for(END - 2027), pledge_for(END - 2027))
    out["fin_room_pledge2_odds"] = f"{run(base, **dict(tilt, inflows=two))['odds']:.1%}"
    out["fin_room_pledge2_sodds"] = f"{stressed(base, sc, mult, flows=two, **tilt)['odds']:.1%}"
    bon = stressed(base, dict(sc, inflows=plus(sc["inflows"], bonus_lost())), mult)
    out["fin_bonus_leg"] = ("−" if bon["leg_med"] < allr["leg_med"] else "+") + f"HK${abs(bon['leg_med'] - allr['leg_med']):.2f}M"
    out["fin_bonus_pts"] = f"{(bon['odds'] - allr['odds']) * 100:+.1f}".replace("-", "−")
    out["fin_bonus_sodds"] = f"{bon['odds']:.1%}"                         # the plan in the downturn, bonus lost
    # slide 9 (Climate Facts, Pete 14 Nov: the card shows our recommended plan, as the close does): the new plan (vans at
    # HK$31/L through the sale, candidate A's fees, the 20-year scholarship fund), normally and in the 2030-31 downturn.
    nw = run(base, biz=m.BIZ + sale_uplift(SAVE), r_eq=r_eq_for(FEE_SAVED), inflows=scholarship_funded())
    ns = stressed(base, sc, mult, biz_add=sale_uplift(SAVE), flows=scholarship_funded(), r_eq=r_eq_for(FEE_SAVED))
    out["fin_new_odds"], out["fin_new_storm_odds"] = f"{nw['odds']:.1%}", f"{ns['odds']:.1%}"
    out["fin_new_odds100"], out["fin_new_storm_odds100"] = f"{round(nw['odds'] * 100)}", f"{round(ns['odds'] * 100)}"
    out["fin_new_leg89"] = f"HK${nw['leg_med']:.1f}M"
    # slide 6 (S, the flat; 13 Nov): where the limit flips the route. The scenario has the old flat fall 15% behind
    # newer flats from 2031 (10% in 2030), on top of its 0.15% a year drag; here that fall runs from 0 to 15%, the
    # rest of the scenario unchanged. The reverse mortgage barely moves (HKMC counts half the value above HK$8M);
    # downsizing sells the old flat and buys a newer one, so the gap hits it in full.
    out["fin_down_odds100"], out["fin_base_odds100"] = f"{round(down['odds'] * 100)}", f"{round(b['odds'] * 100)}"
    out["fin_storm_odds100"] = f"{round(allr['odds'] * 100)}"            # the reverse mortgage in the downturn
    out["fin_down_more_n"] = f"HK${down['leg_med'] - b['leg_med']:.2f}M"   # downsizing's extra, normally
    grid, rm_o, dn_o = (0.0, 0.025, 0.05, 0.075, 0.10, 0.125, 0.15), [], []
    for i, d in enumerate(grid):
        def mult_d(y, d=d):
            return (1 - 0.0015) ** max(y - m.BY, 0) * (1.0 if y < 2030 else (1 - d * 2 / 3 if y == 2030 else 1 - d))
        rm, dn = run(base, "rmp", mult_d, **sc), run(base, "down", mult_d, **sc)
        rm_o.append(rm["odds"])
        dn_o.append(dn["odds"])
        out[f"fin_flip_rmp_{i}"], out[f"fin_flip_down_{i}"] = f"{rm['odds']:.1%}", f"{dn['odds']:.1%}"
    if abs(dn_o[-1] - down_s["odds"]) > 1e-12 or abs(rm_o[-1] - allr["odds"]) > 1e-12:
        sys.exit("slide 6: the 15% end of the flip grid must reproduce the scenario's runs")
    cross = next((grid[i - 1] + (grid[i] - grid[i - 1]) * (dn_o[i - 1] - 0.85) / (dn_o[i - 1] - dn_o[i])
                  for i in range(1, len(grid)) if dn_o[i - 1] >= 0.85 > dn_o[i]), None)
    if cross is None or min(rm_o) < 0.85:
        sys.exit("slide 6: downsizing no longer crosses the 85 limit inside the grid (or the reverse mortgage does)")
    out["fin_flip_cross"], out["fin_flip_cross_x"] = f"{cross:.0%}", f"{cross * 100:.2f}"
    # slide 6, a normal future (13 Nov, night): the same fall behind newer flats without the downturn, against the
    # normal limit of 95, on M6's shape (the old flat d lower from 2037, the year of the sale). The normal limit binds
    # first: downsizing crosses 95 at a smaller gap than it crosses 85 in the downturn. A 1% grid, so the crossing
    # doesn't move with the grid's spacing; the 0% end must reproduce the base and M6's downsizing.
    gridn, rmn_o, dnn_o = [i / 100 for i in range(16)], [], []
    for i, d in enumerate(gridn):
        mult_n = (lambda d: (lambda y: 1 - d if y >= m.RMP_Y else 1.0))(d)
        rm, dn = run(base, "rmp", mult_n), run(base, "down", mult_n)
        rmn_o.append(rm["odds"])
        dnn_o.append(dn["odds"])
        out[f"fin_flipn_rmp_{i}"], out[f"fin_flipn_down_{i}"] = f"{rm['odds']:.1%}", f"{dn['odds']:.1%}"
    if abs(dnn_o[0] - down["odds"]) > 1e-12 or abs(rmn_o[0] - b["odds"]) > 1e-12:
        sys.exit("slide 6: the 0% end of the normal-future grid must reproduce the base and M6's downsizing")
    crossn = next((gridn[i - 1] + (gridn[i] - gridn[i - 1]) * (dnn_o[i - 1] - 0.95) / (dnn_o[i - 1] - dnn_o[i])
                   for i in range(1, len(gridn)) if dnn_o[i - 1] >= 0.95 > dnn_o[i]), None)
    if crossn is None or min(rmn_o) < 0.95:
        sys.exit("slide 6: downsizing no longer crosses the 95 limit inside the normal grid (or the reverse mortgage does)")
    if crossn >= cross:
        sys.exit("slide 6: the normal limit no longer binds first; the slide's words assume it does")
    out["fin_flipn_cross"], out["fin_flipn_cross_x"] = f"{crossn:.0%}", f"{crossn * 100:.2f}"
    out["fin_flipn_rmp100"], out["fin_flipn_down100"] = f"{round(rmn_o[-1] * 100)}", f"{round(dnn_o[-1] * 100)}"
    return out


def m9(w, row, head, base):
    """M9 (review, 12 Nov): is the headline earned against a fair comparator, and how big is the values budget if
    the floors set it? On the Final's base only."""
    b = run(base)
    sc, mult = scenario()
    st0 = stressed(base, sc, mult)
    n_life = END - 2027
    life, f20 = fund_size(n_life), fund_size(20)
    pct = lambda r, c: f"{(r['odds'] - c['odds']) * 100:+.1f}"
    hk = lambda r, c: f"{r['leg_med'] - c['leg_med']:+.2f}"

    w("\n## M9. Fair comparisons (review, 12 Nov; the Final's base, `switch_89`)\n")
    w("The headline (+3.4 points, +HK$2.44M against the label approach) mixes three things: the vans, a fee saving "
      f"measured against a fund whose 0.775% fee was never verified (HK${BOC_SLEEVE/1e6:.2f}M in it), and a lifelong "
      f"pledge ({n_life} years) replaced by a 20-year fund. These rows separate them. EXPLORATORY.\n")

    w("### M9a. The scholarship: the same awards, paid two ways\n")
    w(f"Fund sizes at {REAL_R:.1%} real (area1_6 §7's formula; ESTIMATED): 20 years HK${f20/1e3:.0f}K "
      f"(the plan uses HK$480K); {n_life} years HK${life/1e3:.0f}K, given in two halves in 2027-28 with 17% relief "
      f"(each half under Adrian's ≈HK$420K cap, ESTIMATED).\n")
    w(head)
    rows = [("Lifelong pledge, from cash flow (the label approach)", scholarship_as_written()),
            ("The same awards funded now: a 39-year fund", funded_for(life)),
            ("20 years of awards, from cash flow", pledge_for(20)),
            ("20 years of awards, funded now (the plan's fund, HK$480K)", scholarship_funded())]
    res = {lbl: run(base, inflows=f) for lbl, f in rows}
    for lbl, _ in rows:
        w(row(lbl, res[lbl], b))
    l39, f39, p20, f20r = (res[k] for k, _ in rows)
    w(f"\n- Of the funded fund's gain over the lifelong pledge ({pct(f20r, l39)} points, HK${hk(f20r, l39)}M): "
      f"giving 20 years instead of {n_life} is {pct(p20, l39)} points, HK${hk(p20, l39)}M; funding the same 20 years "
      f"now is {pct(f20r, p20)} points, HK${hk(f20r, p20)}M.")
    w(f"- Like for like ({n_life} years of awards): funding now instead of pledging is {pct(f39, l39)} points, "
      f"HK${hk(f39, l39)}M. That is what the framework's funding rule is worth; the rest is a smaller gift.\n")

    w("### M9b. The headline against a fair comparator\n")
    w("The label approach's ESG core at three fees (0.20% = a labelled index fund as cheap as ours; 0.775% = Round One's "
      "unverified figure, as now; 1.50% = a sensitivity point, not a checked fee), and the scholarship compared as now "
      "or like for like. Our plan: vans (HK$31/L) + candidate A's fees + the scholarship. Normal future and the 2030-31 "
      "scenario. Change is our plan minus the label approach.\n")
    w("| Label approach's ESG core fee | Scholarship compared | Label approach, odds (normal / stress) | Our plan, odds (normal / stress) | Gain: points (normal / stress) | Gain: median HK$M (normal / stress) |\n"
      "|---|---|---|---|---|---|")
    fair = {}
    for fee in (0.0020, BOC_FEE, 0.0150):
        lab_kw = dict(r_eq=r_eq_for(label_core_at(fee)))
        for mode, ours_gift in (("as now (20-year fund vs lifelong pledge)", scholarship_funded()),
                                (f"like for like ({n_life}-year fund vs lifelong pledge)", funded_for(life))):
            lab_n = run(base, inflows=scholarship_as_written(), **lab_kw)
            lab_s = stressed(base, sc, mult, flows=scholarship_as_written(), **lab_kw)
            ours = dict(r_eq=r_eq_for(FEE_SAVED))
            our_n = run(base, biz=m.BIZ + sale_uplift(SAVE), inflows=ours_gift, **ours)
            our_s = stressed(base, sc, mult, biz_add=sale_uplift(SAVE), flows=ours_gift, **ours)
            fair[(fee, mode[:2])] = (lab_n, lab_s, our_n, our_s)
            w(f"| {fee:.3%} | {mode} | {lab_n['odds']:.1%} / {lab_s['odds']:.1%} | {our_n['odds']:.1%} / "
              f"{our_s['odds']:.1%} | {pct(our_n, lab_n)} / {pct(our_s, lab_s)} | {hk(our_n, lab_n)} / {hk(our_s, lab_s)} |")
    lab_n, lab_s, our_n, our_s = fair[(0.0020, "li")]
    w(f"\n- **The fairest row** (a labelled fund as cheap as ours, the same awards both ways): the label approach is at "
      f"{lab_n['odds']:.1%} normally and {lab_s['odds']:.1%} under the scenario; our plan {our_n['odds']:.1%} and "
      f"{our_s['odds']:.1%}. Whether the label approach is below the 85% floor under stress: "
      f"{'yes' if lab_s['odds'] < 0.85 else 'no'}; below the 95% floor normally: {'yes' if lab_n['odds'] < 0.95 else 'no'}.")
    w(f"- Each 0.10% of fee on the label approach's HK${BOC_SLEEVE/1e6:.2f}M ESG core is HK${BOC_SLEEVE*0.001:,.0f} a "
      f"year. Win's purchasable fund sets where the headline lands between the 0.20% and 1.50% rows.\n")

    w("### M9c. The values budget, if the floors set it\n")
    w("Start from the plan with plain funds (candidate A with EDMW → IWDA, Allianz → AGGU, the MPF fund → the cheapest "
      f"MPF global equity fund: HK${FEE_SAVED + FEE_VALUES:,} a year less than the base's funds), no giving and no "
      "vans. The room above the floors (95% normal, 85% under the scenario) is the most the family could spend on values "
      "without breaking a limit. Then add the values choices.\n")
    w(head)
    plain = dict(r_eq=r_eq_for(FEE_SAVED + FEE_VALUES))
    tilt = dict(r_eq=r_eq_for(FEE_SAVED))
    track5 = {y: (-(TRACK_BAD / m.POOL) / W_EQ, 0.0) for y in range(2027, 2032)}
    choices = [
        ("Plain funds, no giving, no vans (the starting point)", plain, None),
        ("+ the ESG tilt (price of values in fees)", tilt, None),
        ("+ the ESG tilt + the 20-year fund (HK$480K)", dict(tilt, inflows=scholarship_funded()), None),
        ("+ the ESG tilt + the 20-year fund + a bad five years of tracking (2027-31)",
         dict(tilt, inflows=scholarship_funded(), ret_add=track5), "normal only"),
        (f"+ the ESG tilt + the same awards for {n_life} years, funded (HK${life/1e3:.0f}K)",
         dict(tilt, inflows=funded_for(life)), None),
        ("+ the ESG tilt + the lifelong pledge from cash flow", dict(tilt, inflows=scholarship_as_written()), None),
    ]
    p_n = run(base, **plain)
    w(row(choices[0][0] + ", normal future", p_n, p_n))
    for lbl, kw, note in choices[1:]:
        w(row(lbl + ", normal future", run(base, **kw), p_n))
    p_s = stressed(base, sc, mult, **plain)
    w(row(choices[0][0] + ", under the scenario", p_s, p_s))
    for lbl, kw, note in choices[1:]:
        if note:
            continue
        kw2 = dict(kw)
        fl = kw2.pop("inflows", None)
        w(row(lbl + ", under the scenario", stressed(base, sc, mult, flows=fl, **kw2), p_s))
    w(f"\n- Room above the floors on the starting point: {(p_n['odds'] - 0.95) * 100:.1f} points normally "
      f"({p_n['odds']:.1%} against 95%), {(p_s['odds'] - 0.85) * 100:.1f} points under the scenario "
      f"({p_s['odds']:.1%} against 85%). The binding limit is the smaller one.")
    w("- The floors are ours (ILLUSTRATIVE, Pete 10 Nov). A verdict that depends on one is shown with the floor at "
      "which it flips.\n")


# ---------- M10-M11 (Claude, 13 Nov, night): Adrian's pay, and what the values budget pays for ----------
A_GROSS = m.WB["Tax"]["B7"].value     # Adrian's HK$1.2M in the model: HK$1.05M salary + the case's low bonus (Tax tab)
A_TAX = m.WB["Tax"]["B13"].value      # his progressive salaries tax, 2026/27 (Tax tab)
A_NET = A_GROSS - A_TAX - m.MPF_CAP   # take-home after tax and his MPF
BONUS = 150_000                       # the case's range is HK$150-300K; the model's income counts the low end
MARGINAL = 0.17                       # his top band (net chargeable HK$755,500, Tax tab)
SEVERANCE = 390_000                   # Employment Ordinance cap on severance pay (not taxable); his years of service unknown


def grown(y):
    return (1 + m.WAGE) ** (y - m.BY)


def bonus_lost(years=(2030, 2031)):
    """Adrian's bonus after tax, lost in the downturn's years, as the scenario already cuts Carmen's draw."""
    return {y: -BONUS * (1 - MARGINAL) * grown(y) for y in years}


def job_lost(from_y=2031, rehire_from=None, rehire_share=0.0):
    """Adrian's take-home and both MPF sides lost from `from_y` until he would have retired; the severance cap paid
    in `from_y`; optionally re-hired at a share of his pay. Spending is unchanged unless a cut is added."""
    f = {}
    for y in range(from_y, m.RETA):
        kept = rehire_share if rehire_from and y >= rehire_from else 0.0
        f[y] = -(1 - kept) * (A_NET * grown(y) + 2 * m.MPF_CAP)
    f[from_y] = f.get(from_y, 0) + SEVERANCE
    return f


def spend_less(per_year, start=2031, end=m.RETA):
    """A spending cut, today's money, CPI-linked, from `start` until Adrian would have retired."""
    return {y: per_year * (1 + m.CPI) ** (y - m.BY) for y in range(start, end)}


def carmen_works_to(age):
    """Carmen works past 62: her take-home and both MPF sides for the extra years; the sale year unchanged."""
    return {y: m.CARMEN_NET * grown(y) + 2 * m.MPF_CAP for y in range(m.RETC, m.RETC + age - 62)}


def gift_now(total, start=2027):
    """Give `total` now, in yearly pieces within both parents' 35% caps (2026 incomes, grown), relief the next year."""
    cap = 0.35 * (A_GROSS + m.C_SAL)
    f, y, left = {}, start, total
    while left > 1:
        piece = min(left, cap * grown(y))
        f[y] = f.get(y, 0) - piece
        f[y + 1] = f.get(y + 1, 0) + RELIEF * piece
        left -= piece
        y += 1
    return f


def most_gift(base, kw, sc, mult, iters=24):
    """The most giving funded now (gift_now) before either limit breaks (95 normally, 85 in the scenario): bisection."""
    lo, hi = 0.0, 6e6
    for _ in range(iters):
        mid = (lo + hi) / 2
        f = gift_now(mid)
        ok = run(base, **dict(kw, inflows=f))["odds"] >= 0.95 and stressed(base, sc, mult, flows=f, **kw)["odds"] >= 0.85
        lo, hi = (mid, hi) if ok else (lo, mid)
    return lo


def down_cross(base, sc, limit=0.85):
    """Where downsizing crosses `limit` in the downturn as the old flat's fall behind newer flats runs from 0 to 15%
    (export_final()'s slide 6 shape, on a 1% grid, interpolated)."""
    grid, odds = [i / 100 for i in range(16)], []
    for d in grid:
        def mult_d(y, d=d):
            return (1 - 0.0015) ** max(y - m.BY, 0) * (1.0 if y < 2030 else (1 - d * 2 / 3 if y == 2030 else 1 - d))
        odds.append(run(base, "down", mult_d, **sc)["odds"])
    return next((grid[i - 1] + (grid[i] - grid[i - 1]) * (odds[i - 1] - limit) / (odds[i - 1] - odds[i])
                 for i in range(1, len(grid)) if odds[i - 1] >= limit > odds[i]), None)


def m10(w, row, head, base):
    """M10: Adrian's pay, which the risk register left out. The bonus in the downturn, and his job as a sensitivity."""
    sc, mult = scenario()
    sc_b = dict(sc, inflows=plus(sc["inflows"], bonus_lost()))
    b, st0 = run(base), stressed(base, sc, mult)
    new_s = dict(biz_add=sale_uplift(SAVE), flows=scholarship_funded(), r_eq=r_eq_for(FEE_SAVED))

    w("\n## M10. Adrian's pay: the route the register left out (Claude, 13 Nov, night; the Final's base, `switch_89`)\n")
    w(f"The model counts Adrian's pay inside one household surplus until he retires in {m.RETA}: HK${A_GROSS/1e6:.2f}M a "
      f"year (HK$1.05M salary + the case's low bonus, HK${BONUS/1e3:.0f}K; the case's range is HK$150-300K), top band "
      f"{MARGINAL:.0%}, take-home HK${A_NET:,.0f} after tax and his MPF. **Every odds figure in these runs assumes he "
      f"keeps his job to 65.** The scenario cuts Carmen's draw in 2030-31 but not his bonus. EXPLORATORY.\n")
    w("### M10a. His bonus in the downturn (the scenario made consistent)\n")
    w("Each pair: a plan in today's scenario, then the same with Adrian's bonus after tax lost in 2030-31. Change is "
      "against the first row of its pair.\n")
    w(head)
    pairs = [("The plan as it stands", {}, "rmp"),
             ("New plan: vans + portfolio fees + funded scholarship", new_s, "rmp"),
             ("Label approach (list funds, unfunded lifelong pledge)", dict(flows=scholarship_as_written()), "rmp")]
    for lbl, kw, _ in pairs:
        a, c = stressed(base, sc, mult, **kw), stressed(base, sc_b, mult, **kw)
        w(row(f"{lbl}, today's scenario", a, a))
        w(row(f"{lbl}, with the bonus lost", c, a))
    dn_a, dn_c = run(base, "down", mult, **sc), run(base, "down", mult, **sc_b)
    w(row("Downsizing instead (only the old flat falls), today's scenario", dn_a, dn_a))
    w(row("Downsizing instead, with the bonus lost", dn_c, dn_a))
    x_a, x_c = down_cross(base, sc), down_cross(base, sc_b)
    w(f"\n- Downsizing crosses the 85 limit in the downturn at a {x_a:.1%} gap behind newer flats in today's scenario "
      f"and at {x_c:.1%} with the bonus lost (slide 6's shape, 1% grid). The normal-future crossing (≈5%, "
      f"`fin_flipn_cross`) doesn't move: the bonus is lost only in the downturn, so the normal limit still binds first.")
    w("- No verdict against a limit changes: the plan as it stands and the new plan stay above 85; the label approach "
      "was already below it at the unverified fee (§5.2).\n")

    w("### M10b. If his job goes (a sensitivity, not a forecast)\n")
    w(f"Lost at the end of 2030, at 58: his bonus that year, then his take-home and both MPF sides until {m.RETA}, with "
      f"the severance cap (HK${SEVERANCE/1e3:.0f}K) paid in 2031. Spending unchanged unless a row says otherwise. "
      f"Any planner draws this route, so it isn't a climate finding; it is priced because it is the largest risk to "
      f"the limits. The plan as it stands; change against the base (normal) or today's scenario (under it).\n")
    w(head)
    job = plus(bonus_lost((2030,)), job_lost())
    half = plus(bonus_lost((2030,)), job_lost(rehire_from=2032, rehire_share=0.5))
    cases = [("No work again before 65", job),
             ("Re-hired from 2032 at half pay", half),
             ("Re-hired from 2032 at three-quarter pay",
              plus(bonus_lost((2030,)), job_lost(rehire_from=2032, rehire_share=0.75))),
             ("Lost at the end of 2033 instead (at 61), no work again", job_lost(from_y=2034)),
             ("Half pay from 2032, and HK$200K a year less spending to 2036", plus(half, spend_less(200_000))),
             ("Half pay from 2032, HK$200K a year less, and Carmen works to 65",
              plus(half, spend_less(200_000), carmen_works_to(65)))]
    res = []
    for lbl, f in cases:
        n_r, s_r = run(base, inflows=f), stressed(base, sc, mult, flows=f)
        w(row(f"{lbl}, normal future", n_r, b))
        w(row(f"{lbl}, under the scenario", s_r, st0))
        res.append((lbl, n_r, s_r))
    w(f"\n- Without a response, losing the job breaks both limits in either future; the climate scenario makes it "
      f"worse, it doesn't cause it. The last row ({res[-1][1]['odds']:.1%} normally, {res[-1][2]['odds']:.1%} under the "
      f"scenario) is a contingency that restores both: half his pay again, HK$200K a year less spending, Carmen "
      f"working three more years (her draw continues; the sale year unchanged, an assumption).")
    w("- The case: \"Neither Adrian nor Carmen has standalone long-term disability income protection.\" Disability is "
      "the insurable form of this risk; redundancy is not. Severance years of service: unknown (ILLUSTRATIVE cap).\n")


def m11(w, row, head, base):
    """M11: what the values budget pays for, and where it binds. M9c's starting point; gifts funded now."""
    sc, mult = scenario()
    plain = dict(r_eq=r_eq_for(FEE_SAVED + FEE_VALUES))
    tilt = dict(r_eq=r_eq_for(FEE_SAVED))
    p_n, p_s = run(base, **plain), stressed(base, sc, mult, **plain)
    life, f20 = fund_size(END - 2027), fund_size(20)

    def both(kw, f):
        return run(base, **dict(kw, inflows=f)), stressed(base, sc, mult, flows=f, **kw)

    def most(kw):
        return most_gift(base, kw, sc, mult)

    w("\n## M11. What the values budget pays for, and where it binds (Claude, 13 Nov, night; the Final's base)\n")
    w("M9c's starting point (plain funds, no giving, no vans): the room above the limits is what values may cost. Gifts "
      "are funded now, in yearly pieces within both parents' 35% caps, with 17% relief. The case's wish: \"a possible "
      "philanthropic plan related to education or environmental causes\"; Carmen's fuller wish is both, the "
      "environmental gift sized like the scholarship (ILLUSTRATIVE). EXPLORATORY.\n")
    mx0, mx1 = most(plain), most(tilt)
    w(f"- **The room, in giving:** about HK${mx0/1e6:.2f}M funded now with plain funds, HK${mx1/1e6:.2f}M with the ESG "
      f"tilt (the most before a limit breaks; the normal limit of 95 binds first). A fund paying HK$30K a year in "
      f"today's money costs HK${f20/1e3:.0f}K for 20 years, HK${life/1e3:.0f}K for {END - 2027}.\n")
    w(head)
    w(row("Plain funds, no giving, no vans, normal future", p_n, p_n))
    w(row("Plain funds, no giving, no vans, under the scenario", p_s, p_s))
    wish = [(f"ESG tilt + the scholarship for {END - 2027} years, funded", gift_now(life)),
            ("ESG tilt + education and environment, 20 years each, funded", gift_now(2 * f20)),
            (f"ESG tilt + education and environment, {END - 2027} years each, funded", gift_now(2 * life)),
            ("ESG tilt + both as lifelong pledges from cash flow", plus(pledge_for(END - 2027), pledge_for(END - 2027)))]
    out = []
    for lbl, f in wish:
        n_r, s_r = both(tilt, f)
        w(row(f"{lbl}, normal future", n_r, p_n))
        w(row(f"{lbl}, under the scenario", s_r, p_s))
        out.append((n_r, s_r))
    z_n = run(base, **dict(plain, biz=0))
    z_s = run(base, "rmp", mult, ret_add=sc["ret_add"], level=sc["level"], inflows=sc["inflows"], biz=0, **plain)
    w(f"\n- Carmen's fuller wish, both causes for life, funded now (HK${2 * life / 1e6:.2f}M), uses all of the room: "
      f"{out[2][0]['odds']:.1%} normally, at the limit of 95 within the model's sampling error. 20 years each fits with "
      f"room to spare ({out[1][0]['odds']:.1%}); the same awards pledged from cash flow break both limits "
      f"({out[3][0]['odds']:.1%} normally, {out[3][1]['odds']:.1%} under the scenario). The budget decides the size and "
      f"the form.")
    w(f"- A proxy for a family with less room (not a second client): the same plan if the business sold for nothing "
      f"is at {z_n['odds']:.1%} normally and {z_s['odds']:.1%} under the scenario with plain funds, below both limits, "
      f"so it has no room: only choices that cost nothing pass.\n")


# ---------- the runs ----------
def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    leg_check = check_against_round_one()
    full = m.full_plan()
    bases = [("The family's plan without the medical review at 75 (`ladder_5_89`, the briefs' base)", full),
             ("The family's plan with the medical review at 75 (`switch_89`, the base: Pete, 9 Nov)", {**full, "med": m.SWITCH})]
    out = []
    w = out.append
    w("# Final Round model runs (EXPLORATORY)\n")
    w("Written by `Final/final_model.py` from the Round One model (`model/run_model.py`, unchanged). "
      "**Not slide numbers** until Pete moves them into `export_numbers()` and logs them. 10,000 futures, the same "
      "seed as Round One, so each row differs from its base only by the change named. Inheritance: the portfolio left "
      "at Carmen's 89 plus home equity, today's money, HK$M; median and the worst 10% (10th percentile).\n")
    w(f"Check: `sim_x()` reproduces `run_model.sim()` exactly on four cases, and the base inheritance matches "
      f"`property_options()` (HK${leg_check/1e6:.2f}M = `legacy_rmp`).\n")
    w(f"Inputs (ILLUSTRATIVE unless the brief says otherwise): Carmen's share {SHARE:.0%}; equity value "
      f"{EQ_MULT}× net profit; profits kept after tax {TAX_KEEP:.1%}; the plan counts {HAIRCUT:.0%} of the business "
      f"value; the pool is HK${m.POOL/1e6:.2f}M, equity {W_EQ:.0%} of the mix.\n")

    def row(label, r, b):
        return (f"| {label} | {r['odds']:.1%} | {(r['odds']-b['odds'])*100:+.1f} | {r['leg_med']:.2f} | "
                f"{r['leg_med']-b['leg_med']:+.2f} | {r['leg_p10']:.2f} | {r['leg_p10']-b['leg_p10']:+.2f} |")

    head = ("| Run | Odds to 89 | Change (pts) | Inheritance, median | Change | Inheritance, worst 10% | Change |\n"
            "|---|---|---|---|---|---|---|")

    for bname, base in bases:
        b = run(base)
        w(f"\n## Base: {bname}\n")
        w(f"Odds {b['odds']:.1%}; inheritance median HK${b['leg_med']:.2f}M, worst 10% HK${b['leg_p10']:.2f}M.\n")

        w("### M2. B1 the vans, LED and air-con, through the sale price\n")
        w(head)
        diesel = [("HK$31/L, the government's after-discount average (base)", SAVE),
                  ("HK$37.93/L, the pump list price", SAVE_LIST), ("HK$25/L, the low case", SAVE_25)]
        for lbl, save in diesel:
            up = sale_uplift(save)
            w(row(f"Diesel at {lbl}: saving HK${save/1e3:.0f}K a year, sale +HK${up/1e6:.2f}M",
                  run(base, biz=m.BIZ + up), b))
        divs = {y: SAVE * TAX_KEEP * SHARE for y in range(2028, 2039)}
        w(row("HK$31/L, plus Carmen's half paid out as dividends 2028-38 (ignores the loan: an upper bound)",
              run(base, biz=m.BIZ + sale_uplift(SAVE), inflows=divs), b))
        for lbl, save in diesel:
            w(row(f"Diesel at {lbl}, plus Carmen's half paid out once the van loan is repaid ({DIV_FROM}-38)",
                  run(base, biz=m.BIZ + sale_uplift(save), inflows=dividends(save)), b))

        w("\n### M3. B3 emissions data: what a lost customer would cost (a sensitivity, not a forecast)\n")
        w(head)
        for pct in (5, 10):
            loss = STAKE_PER_PCT * pct * HAIRCUT
            w(row(f"A customer worth {pct}% of sales leaves: sale −HK${loss/1e6:.2f}M", run(base, biz=m.BIZ - loss), b))
        w(row("Per HK$1M off the sale price", run(base, biz=m.BIZ - 1_000_000), b))

        w("\n### M4. P1-P5 the portfolio\n")
        w(head)
        w(row(f"Fees: label-approach funds → candidate A (HK${FEE_SAVED:,} a year saved)", run(base, r_eq=r_eq_for(FEE_SAVED)), b))
        w(row(f"Price of values in fees vs an all-plain twin (HK${FEE_VALUES:,} a year)",
              run(base, r_eq=r_eq_for(-FEE_VALUES)), b))
        w(row(f"Tracking: a bad five years, 2027-31, at the last five years' lag (HK${TRACK_BAD:,} a year)",
              run(base, ret_add={y: (-(TRACK_BAD / m.POOL) / W_EQ, 0.0) for y in range(2027, 2032)}), b))
        w(row(f"Tracking, if that lag repeated every year to 89 (a stress)",
              run(base, r_eq=r_eq_for(-TRACK_BAD)), b))

        w("\n### M5. G1 the scholarship\n")
        w(head)
        w(row("Label approach (Round One as written): ≈HK$30K a year for life, from cash flow", run(base, inflows=scholarship_as_written()), b))
        w(row("Funded: a 20-year fund, 2 × HK$240K in 2027-28, with relief", run(base, inflows=scholarship_funded()), b))

        w("\n### M6. H1 the flat: the route, if the old flat loses value (newer flats hold)\n")
        w(head)
        for d in (0.0, 0.10, 0.20):
            mult = (lambda d: (lambda y: 1 - d if y >= m.RMP_Y else 1.0))(d)
            w(row(f"Reverse mortgage, old flat {d:.0%} lower from 2037", run(base, "rmp", mult), b))
            w(row(f"Downsize in {m.DS_Y}, old flat {d:.0%} lower", run(base, "down", mult), b))
        w(row("Reverse mortgage from 2045 instead, 2037's payout kept (Round One's `rmp2045_89` run: understated)",
              rmp_from(base, 2045, m.RMP), b))
        w(row("Reverse mortgage from 2045 instead, at the 2045 flat value and Carmen's age 68 (HKMC 2026 table)",
              rmp_from(base, 2045, m.RMP * counted(m.home_value(2045)) / counted(m.home_value(m.RMP_Y))
                       * RMP_AGE_68 / RMP_AGE_60), b))

        w("\n### M7. The scenario: late and sudden (2030-31)\n")
        w(head)
        sc, mult = scenario()
        w(row("Portfolio only (returns and inflation)", run(base, ret_add=sc["ret_add"], level=sc["level"]), b))
        w(row("Flat only (smaller reverse mortgage, lower equity)", run(base, "rmp", mult), b))
        w(row("Business only (sale −10%, Carmen's draw −HK$100K in 2030-31)",
              run(base, biz=sc["biz"], inflows=sc["inflows"]), b))
        w(row("**All together**", run(base, "rmp", mult, **sc), b))
        w(row("All together, downsizing instead (only the old flat falls)", run(base, "down", mult, **sc), b))

        w("\n### The recommendation: the framework's plan against the label approach\n")
        w(head)
        new = dict(biz=m.BIZ + sale_uplift(SAVE), r_eq=r_eq_for(FEE_SAVED), inflows=scholarship_funded())
        w(row("New plan: vans (diesel HK$31/L) + portfolio fees + funded scholarship", run(base, **new), b))
        w(row("New plan, diesel at the HK$37.93/L list price", run(base, **dict(new, biz=m.BIZ + sale_uplift(SAVE_LIST))), b))
        w(row("New plan, diesel at HK$25/L", run(base, **dict(new, biz=m.BIZ + sale_uplift(SAVE_25))), b))
        new_div = dict(new, inflows={**dividends(SAVE),
                                     **{y: v + dividends(SAVE).get(y, 0) for y, v in scholarship_funded().items()}})
        w(row(f"New plan + dividends once the van loan is repaid ({DIV_FROM}-38)", run(base, **new_div), b))
        written = run(base, inflows=scholarship_as_written())
        w(row("Label approach (Round One as written: list funds, unfunded lifelong pledge)", written, b))
        w(f"\nAgainst the label approach, the framework's plan changes the odds by "
          f"{(run(base, **new)['odds']-written['odds'])*100:+.1f} points and the median inheritance by "
          f"HK${run(base, **new)['leg_med']-written['leg_med']:+.2f}M.\n")

        # ---------- M8: each decision under the 2030-31 scenario, against its value in a normal future ----------
        w("### M8. The whole household under stress (2030-31, all channels)\n")
        w("Every row runs M7's **All together** scenario (portfolio returns and inflation, the flat, the business at "
          "once; reverse-mortgage route). **Change is against row 1**, the plan as it stands under the scenario. A "
          "decision that moves the sale price takes the scenario's 10% cut with the rest of the sale; a decision's "
          "own flows are added to the scenario's (Carmen's draw −HK$100K in 2030-31).\n")
        w(head)
        st0 = stressed(base, sc, mult)
        m7 = run(base, "rmp", mult, **sc)
        if any(abs(st0[k] - m7[k]) > 1e-12 for k in st0):
            sys.exit(f"M8 row 1 does not reproduce M7's All together: {st0} vs {m7}")
        w(row("The plan as it stands, under the scenario (reproduces M7's All together exactly)", st0, st0))
        label_st = stressed(base, sc, mult, flows=scholarship_as_written())
        w(row("Label approach (list funds, unfunded lifelong pledge), under the scenario", label_st, st0))
        new_st_kw = dict(biz_add=sale_uplift(SAVE), flows=scholarship_funded(), r_eq=r_eq_for(FEE_SAVED))
        new_st = stressed(base, sc, mult, **new_st_kw)
        w(row("New plan: vans (diesel HK$31/L) + portfolio fees + funded scholarship, under the scenario", new_st, st0))
        new_div_st = stressed(base, sc, mult, **dict(new_st_kw, flows=plus(scholarship_funded(), dividends(SAVE))))
        w(row(f"New plan + dividends once the van loan is repaid ({DIV_FROM}-38), under the scenario", new_div_st, st0))
        up = sale_uplift(SAVE)
        decisions = [
            ("Vans", f"Vans, LED and air-con alone (HK$31/L): sale +HK${up/1e6:.2f}M before the 10% cut",
             dict(biz_add=up), dict(biz=m.BIZ + up)),
            ("Dividends", f"Dividends {DIV_FROM}-38 alone (Carmen's half of the HK$31/L saving; no sale uplift)",
             dict(flows=dividends(SAVE)), dict(inflows=dividends(SAVE))),
            ("Fees", f"Fees alone: label-approach funds → candidate A (HK${FEE_SAVED:,} a year saved)",
             dict(r_eq=r_eq_for(FEE_SAVED)), dict(r_eq=r_eq_for(FEE_SAVED))),
            ("Price of values", f"Price of values in fees vs an all-plain twin (HK${FEE_VALUES:,} a year)",
             dict(r_eq=r_eq_for(-FEE_VALUES)), dict(r_eq=r_eq_for(-FEE_VALUES))),
            ("Funded scholarship", "Funded scholarship alone: 2 × HK$240K in 2027-28, with relief",
             dict(flows=scholarship_funded()), dict(inflows=scholarship_funded())),
            ("Lifelong pledge", "The label approach's lifelong pledge alone: ≈HK$30K a year from cash flow",
             dict(flows=scholarship_as_written()), dict(inflows=scholarship_as_written())),
        ]
        pairs = []
        for short, lbl, skw, nkw in decisions:
            s_r = stressed(base, sc, mult, **skw)
            w(row(lbl, s_r, st0))
            pairs.append((short, s_r, run(base, **nkw)))
        pairs += [("New plan (the package)", new_st, run(base, **new)),
                  ("New plan + dividends (the package)", new_div_st, run(base, **new_div))]
        w("\n**Stress minus normal:** each decision's change under the scenario (against row 1) minus its change in a "
          "normal future (against the base, as in M2-M5 and the recommendation). Odds in points, inheritance in HK$M. "
          "Positive: the decision is worth more when climate hits; negative: it adds value mainly in calm times.\n")
        for short, s_r, n_r in pairs:
            d = {k: (s_r[k] - st0[k], n_r[k] - b[k]) for k in ("odds", "leg_med", "leg_p10")}
            w(f"- {short}: odds {d['odds'][0]*100:+.1f} under stress, {d['odds'][1]*100:+.1f} normal "
              f"(**{(d['odds'][0]-d['odds'][1])*100:+.1f}**); median {d['leg_med'][0]:+.2f} under stress, "
              f"{d['leg_med'][1]:+.2f} normal (**{d['leg_med'][0]-d['leg_med'][1]:+.2f}**); worst 10% "
              f"{d['leg_p10'][0]:+.2f} under stress, {d['leg_p10'][1]:+.2f} normal "
              f"(**{d['leg_p10'][0]-d['leg_p10'][1]:+.2f}**).")
        new_n, new_div_n = run(base, **new), run(base, **new_div)

        def vs(a, c):
            return (f"{(a['odds']-c['odds'])*100:+.1f} points, median HK${a['leg_med']-c['leg_med']:+.2f}M, "
                    f"worst 10% HK${a['leg_p10']-c['leg_p10']:+.2f}M")
        w(f"\n**Headline under stress:** against the label approach, both under the scenario, the new plan changes "
          f"the odds by {vs(new_st, label_st)} (normal future: {vs(new_n, written)}). With the dividends: "
          f"{vs(new_div_st, label_st)} under stress (normal: {vs(new_div_n, written)}).\n")

        w(f"**The carbon data's cost in the new plan** (≈HK${CARBON_LO/1e3:.0f}-{CARBON_HI/1e3:.0f}K a year, paid "
          f"by the business from 2027; `Decision_List.md` B3). It goes through the sale price as the vans' saving "
          f"does: × {TAX_KEEP:.1%} kept after tax × {EQ_MULT} × Carmen's {SHARE:.0%} × the {HAIRCUT:.0%} counted, "
          f"so the buyer is assumed to keep paying it; like the saving, the cost before the sale is not taken from "
          f"Carmen's draw. Change against the base in a normal future, against row 1 above under the scenario.\n")
        w(head)
        carbon = []
        for cost in (CARBON_LO, CARBON_HI):
            cut = sale_uplift(-cost)
            n_r = run(base, **dict(new, biz=m.BIZ + up + cut))
            w(row(f"Normal future: new plan + carbon data at HK${cost/1e3:.0f}K a year (sale −HK${-cut/1e6:.2f}M)",
                  n_r, b))
            carbon.append((cost, cut, n_r))
        lines = []
        for cost, cut, n_r in carbon:
            s_r = stressed(base, sc, mult, **dict(new_st_kw, biz_add=up + cut))
            w(row(f"Under the scenario: new plan + carbon data at HK${cost/1e3:.0f}K a year "
                  f"(sale −HK${-cut/1e6:.2f}M before the 10% cut)", s_r, st0))
            lines.append(f"- At HK${cost/1e3:.0f}K a year, the carbon data costs the new plan {vs(n_r, new_n)} in a "
                         f"normal future and {vs(s_r, new_st)} under the scenario. The new plan with it, against the "
                         f"label approach: {vs(n_r, written)} normal; {vs(s_r, label_st)} under stress.")
        w("")
        for line in lines:
            w(line)

        nw = {k.split(".", 1)[1]: v for k, v in m.O.items() if k.startswith("BalanceSheet.")}
        fixed = nw["Residential property"] + nw["Carmen's business"]
        fixed_net = fixed - nw["Mortgage"] - nw["Business term loan"]
        w(f"\nNotes on M8:\n"
          f"- The scenario does not raise diesel prices, so the vans' saving is not larger under stress; and the ESG "
          f"sleeve takes the same shock as other equity (M7), so the fee change and the price of values get no "
          f"stress-specific credit. Any difference between stress and normal for them comes only from the model's "
          f"arithmetic (a fixed sum or return on a pot that is smaller or empty in more futures).\n"
          f"- Under the scenario the worst-10% future has already run out of money (its inheritance is the flat's "
          f"equity only): a cost cannot lower it further, and a gain moves it only if it keeps that future solvent. "
          f"So the positive worst-10% gaps of the costs above are a floor, not risk removed; read the odds.\n"
          f"- The label approach is the plan as it stands plus the lifelong pledge (the plan's fees are already the "
          f"list funds'), so its row and the pledge's are the same by construction.\n"
          f"- The carbon data's benefit (customers kept, M3) is not in these rows: they price its cost only.\n"
          f"- Dividends start in {DIV_FROM}, after the shock; the scenario's draw cut in 2030-31 is unchanged.\n"
          f"- Not run: the median share of net worth in the flat and the business in 2033 and 2039. The model has no "
          f"business value before the {m.BIZ_Y} sale and no mortgage balance before {m.RETA}, and `sim_x()` keeps only "
          f"the end pot, so it would need new ILLUSTRATIVE paths; in {m.BIZ_Y} the business is sold in the year, so its "
          f"share is nil by construction. In {m.BY} (the case's balance sheet; no decision acts before 2027, so the "
          f"same for both plans) the flat and the business are HK${fixed/1e6:.2f}M of HK${nw['TOTAL ASSETS']/1e6:.2f}M "
          f"of assets ({fixed/nw['TOTAL ASSETS']:.0%}); net of the mortgage and the business loan, "
          f"HK${fixed_net/1e6:.2f}M of HK${nw['NET WORTH']/1e6:.2f}M net worth ({fixed_net/nw['NET WORTH']:.0%}).\n")

    m9(w, row, head, bases[1][1])
    m10(w, row, head, bases[1][1])
    m11(w, row, head, bases[1][1])

    w("\n## What is not in these runs\n")
    w("- Tonnes (the world side) are not model outputs: ≈134 t a year from the business (vans 19.3, LED 4.1, "
      "air-con 2.8, recycled PET 108.1; ESTIMATED on an ILLUSTRATIVE business), from `Final/Decision_List.md`.\n"
      "- The vans' effect assumes a buyer pays for the higher profit at the same multiple; no green premium on the "
      "multiple.\n- The scenario's shocks are the property brief's (§5.1); the ESG sleeve takes the same equity shock.\n"
      "- Guardrails are off, as in `ladder_5_89` and `switch_89`.\n")
    text = "\n".join(out) + "\n"
    path = os.path.join(ROOT, "Final", "model_runs.md")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
