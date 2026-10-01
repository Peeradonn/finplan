"""
Wong Family — plan model (v2). Reproduces the submission's retirement numbers.

Reads the base assumptions (returns, CPI, surplus, dates, spending, pool) from
wong_model.xlsx -> Inputs / Outputs, exactly as run_model.py does. The plan-level
assumptions that the spreadsheet does not yet hold are in PLAN below, each with its
source; they are the rows of Appendix A1 in the proposal.

Usage:  python3 plan_model.py            # decision ladder, stress table, guardrails
        python3 plan_model.py --charts   # also writes ../figures/*.png
"""
import sys, numpy as np
from openpyxl import load_workbook

XLSX = "wong_model.xlsx"
N, SEED = 10_000, 42

# ---------------------------------------------------------------- inputs
wb = load_workbook(XLSX, data_only=True)
I = {str(r[0].value).strip(): r[1].value for r in wb["Inputs"].iter_rows(min_row=4, max_col=2)
     if r[0].value and r[1].value is not None}
O = {str(r[0].value).strip(): r[1].value for r in wb["Outputs"].iter_rows(max_col=2)
     if r[0].value and r[1].value is not None}
BS = {str(r[0].value).strip(): r[1].value for r in wb["BalanceSheet"].iter_rows(max_col=2)
      if r[0].value and r[1].value is not None}
PJ = {r[0]: r for r in wb["Projection"].iter_rows(min_row=4, values_only=True) if isinstance(r[0], int)}

CPI, R_EQ, S_EQ, R_BD = I["CPI inflation"], I["Equities"], I["Equity volatility"], I["Treasury ladder"]
BY, RETA, RETC = int(I["Base year"]), int(I["Adrian retires (age 65)"]), int(I["Carmen retires (age 62)"])
C89, C95 = int(I["Carmen age 89"]), int(I["Carmen age 95"])
SPEND = I["Retirement spending (today money)"]
EDU_A, EDU_N, EDU_ESC, EDU_Y = (I["Education — overseas annual (today)"], int(I["Education — years"]),
                                I["Education escalation (overseas)"], int(I["Chloe starts university"]))
POOL0 = O["Parents' investable pool"]
EDU_RES = sum(EDU_A * (1 + EDU_ESC) ** (y - BY) / 1.03 ** (y - BY) for y in range(EDU_Y, EDU_Y + EDU_N))

PLAN = dict(                       # Appendix A1 rows not yet on the Inputs tab
    w_eq=0.40, s_bd=0.02,          # model mix 40/60 whole pool; ladder held to maturity
    cover_y1=100_000, cover_g=0.026,   # new cover HK$100K yr 1, avg ≈114K to 2036 (Lookbua §8)
    med_in_budget=65_000,          # medical premiums already inside the HK$780K (today's money)
    adrian_death=2056, adrian_95=2067,  # Adrian 84 (case LE); 95 for the longevity test
    ann_A=161_000, ann_C=107_000,  # HKMC single life, fixed nominal; bought 2037 / 2039
    mpf_A=2_310_000, mpf_C=1_810_000,   # MPF used to buy them (Pete's projection)
    mortgage_2037=460_000,         # balance cleared from the portfolio in 2037
    rm=230_000, rm_start=2037,     # HKMC reverse mortgage, fixed nominal, life of last survivor
    biz=3_000_000, biz_years=(2035, 2039),  # sale proceeds, today's money, equal tranches
    survivor=0.70,                 # spending after Adrian's death
    std_from=2047,                 # tier review: Standard plan from Adrian's 75
    gr_from=2039, gr_band=0.20, gr_step=0.10, gr_floor=0.70,  # Guyton–Klinger
)

# --------------------------------------------------------------- medical
MTR = {2027: .10, 2028: .0956, 2029: .0911, 2030: .0867, 2031: .0822,
       2032: .0778, 2033: .0733, 2034: .0689, 2035: .0644}          # methodology §1b, 6% from 2036
AGES = [55, 60, 62, 65, 70, 75, 80]
FLEXI = {"M": [17140, 23050, 26578, 32542, 42122, 53887, 63644],
         "F": [18186, 23210, 25895, 31599, 40990, 53228, 62772]}   # VHIS Flexi medians
STD = [6119, 7887, 8765, 10452, 13008, 16184, 18920]               # VHIS Standard median (M; used for both)

def premium(age, sex, std=False):
    t = STD if std else FLEXI[sex]
    return np.interp(age, AGES, t) if age <= 80 else t[-1] * 1.034 ** (age - 80)

MED_LR = 0.06                                                      # long-run trend from 2036

def med_factor(y, trend=None):
    f = 1.0
    for k in range(2027, y + 1):
        f *= 1 + (trend if trend is not None else MTR.get(k, MED_LR))
    return f

def medical_excess(y, a_alive, std=False, trend=None):
    """Nominal premiums above what the HK$780K already holds. Group cover ends at 65/62."""
    tot = 0.0
    if a_alive and y > RETA:  tot += premium(y - 1972, "M", std)
    if y > RETC:              tot += premium(y - 1977, "F", std)
    if y <= RETA: return 0.0
    return max(tot * med_factor(y, trend) - PLAN["med_in_budget"] * (1 + CPI) ** (y - BY), 0.0)

# ------------------------------------------------------------ simulation
def simulate(end, annuity=False, survivor=False, business=False, home=None, std75=False,
             guardrails=False, cpi=None, r_eq=None, eq_lowdecade=False, med_trend=None,
             adrian_death=None, rm_start=None, n=N, seed=SEED, paths=False):
    p = PLAN; cpi = CPI if cpi is None else cpi; r_eq = R_EQ if r_eq is None else r_eq
    ad = p["adrian_death"] if adrian_death is None else adrian_death
    rms = p["rm_start"] if rm_start is None else rm_start
    rng = np.random.default_rng(seed)
    pot = np.full(n, float(POOL0)); ok = np.ones(n, bool)
    lvl = np.ones(n); wr0 = None; prev_r = np.zeros(n)
    spend_rec = np.full((n, end - BY), np.nan); pot_rec = np.zeros((n, end - BY + 1)); pot_rec[:, 0] = pot
    for i, y in enumerate(range(BY, end)):
        eq_mu = r_eq - (0.04 if eq_lowdecade and RETA <= y < RETA + 10 else 0)
        r = p["w_eq"] * rng.normal(eq_mu, S_EQ, n) + (1 - p["w_eq"]) * rng.normal(R_BD, p["s_bd"], n)
        pot = pot * (1 + r)
        infl = (1 + cpi) ** (y - BY)
        if y < RETA:                                   # accumulation: model's own surplus, less new cover
            row = PJ[y]
            pot += row[14] - p["cover_y1"]   # row 14 = spreadsheet net cash flow, education paid as it falls due
            pot += 0 * row[11] * (1 + p["cover_g"]) ** i
            pot_rec[:, i + 1] = pot; prev_r = r; continue
        a_alive = y < ad
        target = SPEND * infl * (p["survivor"] if survivor and not a_alive else 1.0)
        if guardrails and y >= p["gr_from"]:
            if wr0 is None:
                wr0 = target / np.maximum(pot, 1)
            else:
                wr = target * lvl / np.maximum(pot, 1)
                cut = (wr > wr0 * (1 + p["gr_band"]))
                lvl = np.where(cut, np.maximum(lvl * (1 - p["gr_step"]), p["gr_floor"]), lvl)
                rise = (wr < wr0 * (1 - p["gr_band"]))
                lvl = np.where(rise & ~cut, np.minimum(lvl * (1 + p["gr_step"]), 1.0), lvl)
                lvl = np.where((prev_r < 0) & ~cut, lvl / (1 + cpi), lvl)   # skip inflation rise
                lvl = np.clip(lvl, p["gr_floor"], 1.0)
        spend = target * lvl
        out = spend + medical_excess(y, a_alive, std=std75 and y >= p["std_from"], trend=med_trend)
        if y < RETC:                                   # Carmen still earning
            row = PJ[y]; out -= row[4] - row[8] - 18_000
        if y == RETA: out += p["mortgage_2037"]
        if annuity:
            if y == RETA: out += p["mpf_A"]
            if y == RETC: out += p["mpf_C"]
            if a_alive: out -= p["ann_A"]
            if y >= RETC: out -= p["ann_C"]
        if business and p["biz_years"][0] <= y <= p["biz_years"][1]:
            out -= p["biz"] / (p["biz_years"][1] - p["biz_years"][0] + 1) * infl
        if home == "rm" and y >= rms: out -= p["rm"]
        if home == "downsize" and y == rms:
            out -= (11_500_000 * 1.015 ** (y - BY) - 7_000_000 * infl) * 0.97   # 3% costs
        pot = pot - out
        ok &= pot > 0; pot = np.maximum(pot, 0)
        spend_rec[:, i] = np.where(pot > 0, spend, np.nan); pot_rec[:, i + 1] = pot; prev_r = r
    res = dict(success=ok.mean(), pot=pot, spend=spend_rec, potpath=pot_rec)
    return res if paths else res["success"]

LADDER = [("Investments alone", {}),
          ("+ MPF annuity", dict(annuity=True)),
          ("+ lower spending after first death", dict(annuity=True, survivor=True)),
          ("+ business sale", dict(annuity=True, survivor=True, business=True)),
          ("+ home released", dict(annuity=True, survivor=True, business=True, home="rm")),
          ("+ Standard plan from 75", dict(annuity=True, survivor=True, business=True, home="rm", std75=True))]
FULL = LADDER[4][1]

if __name__ == "__main__":
    print(f"pool {POOL0:,.0f} (education {EDU_RES:,.0f} PV, paid from it 2028-31); "
          f"equity {R_EQ:.1%}/{S_EQ:.0%}, ladder {R_BD:.1%}, CPI {CPI:.1%}")
    print("\nDECISION LADDER (slide: 33/16 31/14 41/22 59/36 83/61 97/89)")
    for name, kw in LADDER:
        print(f"  {name:<38}{simulate(C89, **kw):>6.0%}{simulate(C95, **kw):>6.0%}")
    print("\nOTHER SLIDE NUMBERS")
    chk = [("medical inside budget, alone (64%)", None),
           ("full plan, no business sale (66%)", dict(FULL, business=False)),
           ("full plan, keep home (59%)", dict(FULL, home=None)),
           ("full plan, downsize (83%)", dict(FULL, home="downsize")),
           ("full plan, RM from 2045 (73%)", dict(FULL, rm_start=2045)),
           ("full plan, equity 7% (89%)", dict(FULL, r_eq=0.07)),
           ("full plan, medical 4.5% LR (91%)", "med45"),
           ("full plan + std75 + guardrails (100%)", dict(FULL, std75=True, guardrails=True))]
    for lbl, kw in chk:
        if kw is None:
            PLAN["med_in_budget"], keep = 1e12, PLAN["med_in_budget"]
            s = simulate(C89); PLAN["med_in_budget"] = keep
        elif kw == "med45":
            keep = dict(MTR)
            for k in range(2027, 2036): MTR[k] = 0.10 - (0.10 - 0.045) * (k - 2027) / 9
            MED_LR = 0.045; s = simulate(C89, **FULL)
            MTR.clear(); MTR.update(keep); MED_LR = 0.06
        else:
            s = simulate(C89, **kw)
        print(f"  {lbl:<42}{s:>6.0%}")

    print("\nSTRESS — fixed spending / plan (tier review + guardrails)   [slide Fig. 27]")
    G = dict(FULL, std75=True, guardrails=True)
    for lbl, kw, end, sl in [("F1 inflation 3.5%", dict(cpi=0.035), C89, "49/96"),
                             ("F2 medical 8.5% flat", dict(med_trend=0.085), C89, "58/99"),
                             ("F4 business not sold", dict(business=False), C89, "66/100"),
                             ("F5 last to Carmen 95", {}, C95, "61/99"),
                             ("F6 base", {}, C89, "83/100")]:
        print(f"  {lbl:<24}{simulate(end, **dict(FULL, **kw)):>6.0%}{simulate(end, **dict(G, **kw)):>6.0%}   slide {sl}")
