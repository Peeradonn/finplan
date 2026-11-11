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
    return out


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
