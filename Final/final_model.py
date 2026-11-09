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
"""
import os, sys
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
          inflows=None, ret_add=None, level=None, n=N, seed=SEED):
    """run_model.sim() without guardrails, plus: ret_add {year: (equity addend, bond addend)},
    level {year: factor} (a permanent price-level step on retirement spending from that year), rmp_y.
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
SHARE = 0.5                      # Carmen's share of the business (team decision open)
EQ_MULT = 5.6                    # equity value / net profit (area2_business.md §3a; no HK SME source)
TAX_KEEP = 0.835                 # after 16.5% profits tax at the margin
HAIRCUT = m.BIZ / 5_000_000      # the plan counts HK$3.0M of the HK$5.0M: 60%
SAVE_LIST, SAVE_25 = 372_000, 240_300   # vans + LED + air-con a year: diesel at HK$37.93/L list; at HK$25/L
STAKE_PER_PCT = 209_000          # Carmen's stake per 1% of sales lost (area2_business.md §3e)
FEE_SAVED = 18_175 - 8_528       # both portfolios' fees, Round One -> candidate A (area3_portfolio.md §3)
FEE_VALUES = 5_107               # price of values in fees against an all-plain twin (area3 §4)
TRACK_BAD = 26_600               # the climate sleeve's lag a year if the last five years repeat (area3 §4)
RELIEF = 0.17                    # salaries tax relief on cash gifts while earning (area1_6 §7)


DIV_FROM = 2033                  # the 5-year van loan (HK$1.5M, ≈HK$349K a year) takes the saving to 2032


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
        for lbl, save in [("Saving at the diesel list price (HK$372K a year)", SAVE_LIST),
                          ("Saving at HK$25/L diesel (HK$240K a year)", SAVE_25)]:
            up = sale_uplift(save)
            w(row(f"{lbl}: sale +HK${up/1e6:.2f}M", run(base, biz=m.BIZ + up), b))
        divs = {y: SAVE_LIST * TAX_KEEP * SHARE for y in range(2028, 2039)}
        w(row("List price, plus Carmen's half paid out as dividends 2028-38 (ignores the loan: an upper bound)",
              run(base, biz=m.BIZ + sale_uplift(SAVE_LIST), inflows=divs), b))
        for lbl, save in [("list price", SAVE_LIST), ("HK$25/L", SAVE_25)]:
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
        w(row(f"Tracking: a bad five years, 2027-31, at the worst five-year lag (HK${TRACK_BAD:,} a year)",
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
        new = dict(biz=m.BIZ + sale_uplift(SAVE_LIST), r_eq=r_eq_for(FEE_SAVED), inflows=scholarship_funded())
        new_25 = dict(new, biz=m.BIZ + sale_uplift(SAVE_25))
        w(row("New plan: vans (list diesel) + portfolio fees + funded scholarship", run(base, **new), b))
        w(row("New plan, diesel at HK$25/L", run(base, **new_25), b))
        new_div = dict(new, inflows={**dividends(SAVE_LIST),
                                     **{y: v + dividends(SAVE_LIST).get(y, 0) for y, v in scholarship_funded().items()}})
        w(row(f"New plan + dividends once the van loan is repaid ({DIV_FROM}-38)", run(base, **new_div), b))
        written = run(base, inflows=scholarship_as_written())
        w(row("Label approach (Round One as written: list funds, unfunded lifelong pledge)", written, b))
        w(f"\nAgainst the label approach, the framework's plan changes the odds by "
          f"{(run(base, **new)['odds']-written['odds'])*100:+.1f} points and the median inheritance by "
          f"HK${run(base, **new)['leg_med']-written['leg_med']:+.2f}M.\n")

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
