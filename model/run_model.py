"""
Wong Family model — Python layer.
Reads EVERY assumption from wong_model.xlsx  ->  Inputs tab (and the Medical age curve).
Never hardcode an assumption here. Change the spreadsheet instead.

Usage:  python3 run_model.py          (prints sections 1-9)
        import run_model              (functions only, for make_charts.py)
"""
import os, sys, numpy as np
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
XLSX = os.path.join(HERE, "wong_model.xlsx")

def load_inputs(path=XLSX):
    """Label -> value, straight off the Inputs tab."""
    wb = load_workbook(path, data_only=True)
    if "Inputs" not in wb.sheetnames:
        sys.exit(f"{path} has no Inputs tab.")
    d = {}
    for row in wb["Inputs"].iter_rows(min_row=4, max_col=2):
        label, val = row[0].value, row[1].value
        if label and val is not None:
            d[str(label).strip()] = val
    out = {}
    for name in ("Outputs", "Tax", "BalanceSheet"):
        if name in wb.sheetnames:
            for row in wb[name].iter_rows(min_col=1, max_col=2):
                a, b = row[0].value, row[1].value
                if a and b is not None:
                    out[f"{name}.{str(a).strip()}"] = b
    if out.get("Outputs.Net worth") is None:
        sys.exit("No cached values: open wong_model.xlsx in Excel (or LibreOffice), save, then rerun.")
    return wb, d, out

WB, I, O = load_inputs()
g = lambda k: I[k]

CPI      = g('CPI inflation')
R_EQ     = g('Equities');          S_EQ = g('Equity volatility')
R_BOND   = g('Bonds / IG');        R_LAD = g('Treasury ladder')
RETA     = int(g('Adrian retires (age 65)')); BY = int(g('Base year'))
C89      = int(g('Carmen age 89')); C95 = int(g('Carmen age 95'))
SPEND    = g('Retirement spending (today money)')
ANN_COST = g('Annuity purchase cost at 2037')
ANN_INC  = g('Annuity income (HKMC, annual)')     # fixed HK$ for life: never indexed
EDU_A    = g('Education — overseas annual (today)'); EDU_N = int(g('Education — years'))
EDU_ESC  = g('Education escalation (overseas)'); EDU_Y = int(g('Chloe starts university'))
WAGE     = g('Wage growth — Adrian')
PREM     = g('Insurance premiums (Lookbua, TBC)')  # paid while working, as in the Projection tab
RETC     = int(g('Carmen retires (age 62)'))
C_SAL    = g("Carmen's salary / dividend")
MPF_CAP  = g('MPF deduction cap')
ALE      = int(g('Adrian life expectancy (year, age 84)'))

# medical (methodology §1)
TIER     = int(g('Medical plan (1 = Flexi, 2 = Standard, 0 = off)'))
M_NT     = g('Medical trend — near term (2027)'); M_LR = g('Medical trend — long run')
M_LRY    = int(g('Medical trend — long run reached (year)'))
M_ST     = g('Medical trend — stress (flat)'); M_STS = int(g('Use medical stress in base (1/0)'))
M_OFF    = g('Premiums already inside the 780,000 (today money)')
# backstops: values always available to the ladder; switches decide the base case
SURV     = g('Survivor spending after Adrian (share)'); SURV_S = int(g('Use survivor spending in base (1/0)'))
BIZ      = g("Carmen's business: net sale proceeds"); BIZ_Y = int(g("Carmen's business: sale year"))
BIZ_S    = int(g('Use business sale in base (1/0)'))
RMP      = g('Reverse mortgage: annual income (level)'); RMP_Y = int(g('Reverse mortgage: first year'))
RMP_S    = int(g('Use reverse mortgage in base (1/0)'))
# stress scenarios (methodology §5)
ST_EQ, ST_BD, ST_CPI = g('Stress: equities'), g('Stress: bonds / ladder'), g('Stress: CPI')
# property options (§9)
HOME, P_G = g('Home value today'), g('Property growth')
RMP_R, RMP_INS, RMP_UP = g('RMP: loan rate (fixed)'), g('RMP: insurance on balance (a year)'), g('RMP: upfront insurance (share of value)')
RMP_CAP, RMP_ABOVE = g('RMP: value counted in full up to'), g('RMP: share of value counted above that')
DS_P, DS_STAMP, DS_AG = g('Downsize: new home price (today money)'), g('Downsize: stamp duty on purchase'), g('Downsize: agents and legal (both sides)')
DS_MOVE, DS_Y = g('Downsize: moving and refit'), int(g('Downsize: year'))

POOL_ALL = O.get("BalanceSheet.Parents' investable pool", 9_790_000)
SURPLUS  = O["Tax.SURPLUS"]            # after tax and MPF, BEFORE new premiums (the sim deducts PREM itself)
# Carmen works two years past Adrian's retirement - the Excel Projection counts this, so we must too
C_TAX    = WB["Tax"]["C13"].value
CARMEN_NET = C_SAL - C_TAX - MPF_CAP

# ---------- medical line, rebuilt from the workbook's age curve ----------
def _curve():
    cur = {}
    for row in WB["Medical"].iter_rows(min_col=1, max_col=4, values_only=True):
        if isinstance(row[0], int) and 55 <= row[0] <= 100 and isinstance(row[1], (int, float)):
            cur.setdefault(row[0], row[1:4])      # first block with every age is the age curve
    return cur
CURVE = _curve()

def med_path(tier=1, stress=False):
    """Year -> net medical line (nominal), same formulas as the Medical tab."""
    if tier == 0:
        return {}
    out, idx = {}, 1.0
    for y in range(BY, C95 + 1):
        if y > BY:
            t = M_ST if stress else (M_LR if y >= M_LRY else M_NT - (M_NT - M_LR) * (y - (BY + 1)) / (M_LRY - (BY + 1)))
            idx *= 1 + t
        aA, aC = y - 1972, y - 1977
        a = (CURVE[aA][0] if tier == 1 else CURVE[aA][2]) if RETA <= y <= ALE else 0
        c = (CURVE[aC][1] if tier == 1 else CURVE[aC][2]) if y >= RETC else 0
        off = M_OFF * (1 + CPI) ** (y - BY) if y >= RETA else 0
        out[y] = max((a + c) * idx - off, 0)
    return out

MED_BASE = med_path(TIER, bool(M_STS))
FLEXI, STD, STRESS = med_path(1), med_path(2), med_path(1, stress=True)

def _check_against_workbook():
    proj = {r[0]: r[13] for r in WB["Projection"].iter_rows(min_row=4, values_only=True) if isinstance(r[0], int)}
    drift = max(abs(MED_BASE.get(y, 0) - (proj.get(y) or 0)) for y in proj)
    if drift > 1:
        sys.exit(f"Medical line differs from the Projection tab by {drift:,.0f}. Recalculate the workbook.")
_check_against_workbook()

# ---------- goal funding ----------
pv = lambda p,r,n: p*(1-(1+r)**-n)/r
edu_nom = [EDU_A*(1+EDU_ESC)**(y-BY) for y in range(EDU_Y, EDU_Y+EDU_N)]
edu_res = sum(c/(1.03**(y-BY)) for c,y in zip(edu_nom, range(EDU_Y, EDU_Y+EDU_N)))
POOL = POOL_ALL - edu_res

BASE = dict(med=MED_BASE, surv=SURV if SURV_S else 1.0, biz=BIZ if BIZ_S else 0, rmp=RMP if RMP_S else 0)

# ---------- Monte Carlo ----------
def sim(w_eq, s_bd, r_bd, end, annuity, med=None, surv=1.0, biz=0, rmp=0, r_eq=None, cpi=None,
        inflows=None, n=10_000, seed=42, paths=False):
    """Success share, mean worst year, median end pot (and, with paths=True, every path's pot by year)."""
    r_eq = R_EQ if r_eq is None else r_eq
    cpi = CPI if cpi is None else cpi
    med, inflows = med or {}, inflows or {}
    rng = np.random.default_rng(seed)
    pot = np.full(n, POOL, float); alive = np.ones(n, bool); worst = np.zeros(n)
    track = np.zeros((end - BY, n)) if paths else None
    for i in range(end - BY):
        y = BY + i
        r = w_eq*rng.normal(r_eq, S_EQ, n) + (1-w_eq)*rng.normal(r_bd, s_bd, n)
        worst = np.minimum(worst, r); pot = pot*(1+r)
        if y == RETA and annuity: pot -= ANN_COST
        if y < RETA: pot += SURPLUS*(1+WAGE)**i - PREM
        else:
            spend = SPEND*(1+cpi)**i*(surv if y > ALE else 1)
            pot -= spend - (ANN_INC if annuity else 0)      # annuity: fixed HK$, not indexed
            if y < RETC: pot += CARMEN_NET*(1+WAGE)**i   # Carmen still earning
            if rmp and y >= RMP_Y: pot += rmp
        if biz and y == BIZ_Y: pot += biz
        pot += inflows.get(y, 0)
        pot -= med.get(y, 0)
        pot = np.maximum(pot, 0); alive &= pot > 0
        if paths: track[i] = pot
    out = (alive.mean(), worst.mean(), np.percentile(pot, 50))
    return out + (track,) if paths else out

MIXES = {"1. All-Treasury ladder":       (0.00, 0.02, R_LAD),
         "2. 40/60 equity / ladder":     (0.40, 0.02, R_LAD),
         "3. 60/40 equity / bond funds": (0.60, 0.05, R_BOND)}
MIX2 = MIXES["2. 40/60 equity / ladder"]

def ladder_steps():
    """The decision ladder: each step adds one decision to the one before."""
    return [
        ("Portfolio alone; Flexi premiums on top of the 780,000", dict(annuity=False, med=FLEXI)),
        ("+ MPF annuitised (HKMC, fixed HK$ for life)",           dict(annuity=True,  med=FLEXI)),
        (f"+ spending falls to {SURV:.0%} after Adrian's {ALE - 1972}",
                                                                 dict(annuity=True,  med=FLEXI, surv=SURV)),
        (f"+ Carmen's business sold ({BIZ/1e6:.1f}M in {BIZ_Y})",  dict(annuity=True,  med=FLEXI, surv=SURV, biz=BIZ)),
        (f"+ reverse mortgage ({RMP/1e3:.0f}K a year from {RMP_Y})",
                                                                 dict(annuity=True,  med=FLEXI, surv=SURV, biz=BIZ, rmp=RMP)),
    ]

def full_plan():
    return dict(ladder_steps()[-1][1])

# ---------- property options (§9) ----------
def home_value(y):
    return HOME*(1+P_G)**(y-BY)

def rmp_balance(start, end, income):
    """Reverse-mortgage loan at `end`: upfront insurance plus level payouts, rolled up at rate + insurance."""
    v = home_value(start)
    counted = min(v, RMP_CAP) + RMP_ABOVE*max(v - RMP_CAP, 0)
    bal = RMP_UP*counted
    for y in range(start, end + 1):
        bal = bal*(1 + RMP_R + RMP_INS) + income
    return bal

def downsize_release(y):
    sale, buy = home_value(y), DS_P*(1+P_G)**(y-BY)
    return sale - buy - buy*DS_STAMP - sale*DS_AG - DS_MOVE*(1+CPI)**(y-BY)

def property_options(end):
    """Success and legacy (median portfolio + home equity, today's money) for keep / reverse mortgage / downsize."""
    common = dict(annuity=True, med=FLEXI, surv=SURV, biz=BIZ)
    defl = (1+CPI)**(end-BY)
    rows = []
    s,_,m = sim(*MIX2, end, **common)
    rows.append(("Keep the home, no release", s, m, home_value(end)))
    s,_,m = sim(*MIX2, end, rmp=RMP, **common)
    rows.append((f"Reverse mortgage, {RMP/1e3:.0f}K a year from {RMP_Y}", s, m,
                 max(home_value(end) - rmp_balance(RMP_Y, end, RMP), 0)))
    s,_,m = sim(*MIX2, end, inflows={DS_Y: downsize_release(DS_Y)}, **common)
    rows.append((f"Downsize in {DS_Y} (release {downsize_release(DS_Y)/1e6:.1f}M)", s, m,
                 DS_P*(1+P_G)**(end-BY)))
    return [(lbl, s, m/defl, h/defl) for lbl, s, m, h in rows]

# ---------- rebalancing rules (Win's M1 / M3 / M9) ----------
def sim_rules(policy, end, w_t=0.40, n=10_000, seed=42):
    """Two sleeves (equity, ladder) under the full plan's cash flows. Policies:
    'target' rebalance to target every year · 'drift' never rebalance ·
    'bands' rebalance when equity is 5pp off target (M3/M9), new money to the underweight sleeve first ·
    'm1' rebalance only after equities fall 20% or more in a year (M1)."""
    kw = full_plan(); med = kw["med"]
    rng = np.random.default_rng(seed)
    eq = np.full(n, POOL*w_t); bd = np.full(n, POOL*(1-w_t)); alive = np.ones(n, bool); worst = np.zeros(n)
    for i in range(end - BY):
        y = BY + i
        re, rb = rng.normal(R_EQ, S_EQ, n), rng.normal(R_LAD, 0.02, n)
        tot0 = eq + bd
        eq, bd = eq*(1+re), bd*(1+rb)
        worst = np.minimum(worst, np.where(tot0 > 0, (eq + bd)/np.maximum(tot0, 1) - 1, 0))
        flow = 0.0
        if y == RETA: flow -= ANN_COST
        if y < RETA: flow += SURPLUS*(1+WAGE)**i - PREM
        else:
            flow -= SPEND*(1+CPI)**i*(SURV if y > ALE else 1) - ANN_INC
            if y < RETC: flow += CARMEN_NET*(1+WAGE)**i
            if y >= RMP_Y: flow += RMP
        if y == BIZ_Y: flow += BIZ
        flow -= med.get(y, 0)
        tot = np.maximum(eq + bd + flow, 0)
        w = np.where(eq + bd > 0, eq/np.maximum(eq + bd, 1), w_t)
        if policy == "target":
            w_new = np.full(n, w_t)
        elif policy == "drift":
            w_new = w
        elif policy == "bands":
            # new money goes to the underweight sleeve first (withdrawals come from the overweight one);
            # then rebalance fully only if equity is still more than 5pp off target
            gap = w_t*tot - eq
            eq_f = eq + (np.minimum(flow, np.maximum(gap, 0)) if flow >= 0 else -np.minimum(-flow, np.maximum(-gap, 0)))
            w_after = np.where(tot > 0, np.clip(eq_f, 0, tot)/np.maximum(tot, 1), w_t)
            w_new = np.where(np.abs(w_after - w_t) > 0.05, w_t, w_after)
        elif policy == "m1":
            w_new = np.where(re <= -0.20, w_t, w)
        eq, bd = tot*w_new, tot*(1-w_new)
        alive &= tot > 0
    return alive.mean(), worst.mean(), np.percentile(eq + bd, 50)

# ---------- printout ----------
def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 72)
    print("INPUTS READ FROM SPREADSHEET")
    print(f"  parents' pool {POOL_ALL:>12,.0f}   surplus {SURPLUS:>10,.0f} before premiums   premiums {PREM:>9,.0f}")
    print(f"  equity {R_EQ:.1%} (vol {S_EQ:.0%})   ladder {R_LAD:.1%}   CPI {CPI:.1%}")
    print(f"  base case: medical {['off','Flexi','Standard'][TIER]}{' (stress)' if M_STS else ''}"
          f" · survivor {'on' if SURV_S else 'off'} · business sale {'on' if BIZ_S else 'off'}"
          f" · reverse mortgage {'on' if RMP_S else 'off'}")
    print("=" * 72)
    print("\n1. GOAL FUNDING")
    print(f"  retirement need at {RETA}, to Carmen 89 (2% real): {pv(SPEND,.02,C89-RETA):>12,.0f}")
    print(f"  retirement need at {RETA}, to Carmen 95          : {pv(SPEND,.02,C95-RETA):>12,.0f}")
    print(f"  education reserve today (overseas @ {EDU_A:,.0f}/yr) : {edu_res:>12,.0f}")
    print(f"  deployable to retirement                        : {POOL:>12,.0f}")

    for tag, ann in [("2. MONTE CARLO — base case, portfolio alone", False),
                     ("3. MONTE CARLO — base case, MPF annuitised (cost deducted)", True)]:
        print(f"\n{tag}")
        print(f"  {'Mix':<30}{'to 89':>8}{'to 95':>8}{'worst yr':>11}{'median end':>15}")
        for name,(w,sb,rb) in MIXES.items():
            s89,wr,med = sim(w,sb,rb,C89,ann,**BASE); s95,_,_ = sim(w,sb,rb,C95,ann,**BASE)
            print(f"  {name:<30}{s89:>7.0%}{s95:>8.0%}{wr:>10.1%}{med:>15,.0f}")

    print("\n4. SENSITIVITY (base case, mix 2, annuitised, to 89)")
    for lbl, adj in [("base", 0), ("equity -1pp", -0.01), ("equity +1pp", +0.01)]:
        s,_,_ = sim(*MIX2, C89, True, r_eq=R_EQ+adj, **BASE)
        print(f"  {lbl:<14} equity {R_EQ+adj:.0%}  ->  success {s:.0%}")

    print("\n5. DECISION LADDER (mix 2; each row adds one decision to the row above)")
    print(f"  {'':<62}{'to 89':>7}{'to 95':>7}")
    for lbl, kw in ladder_steps():
        s89,_,_ = sim(*MIX2, C89, **kw); s95,_,_ = sim(*MIX2, C95, **kw)
        print(f"  {lbl:<62}{s89:>7.0%}{s95:>7.0%}")
    full = full_plan()
    print("  Alternatives on the last row:")
    for lbl, kw in [("   Standard plan instead of Flexi", {**full, "med": STD}),
                    (f"   medical stress, {M_ST:.2%} flat",  {**full, "med": STRESS}),
                    ("   equities -1pp",                    {**full, "r_eq": R_EQ - 0.01}),
                    ("   without the annuity",              {**full, "annuity": False})]:
        s89,_,_ = sim(*MIX2, C89, **kw); s95,_,_ = sim(*MIX2, C95, **kw)
        print(f"  {lbl:<62}{s89:>7.0%}{s95:>7.0%}")
    s89,_,_ = sim(*MIX2, C89, True); s95,_,_ = sim(*MIX2, C95, True)
    print(f"  {'Memo: no medical line at all (the pre-29 Sep base)':<62}{s89:>7.0%}{s95:>7.0%}")

    print("\n6. MEDICAL LINE (base case, nominal HK$, net of the part inside the 780,000)")
    for y in (RETA, RETC, 2045, 2050, ALE, C89):
        print(f"  {y}  Adrian {y-1972:>3}  Carmen {y-1977:>3}   {MED_BASE.get(y,0):>12,.0f}")

    print("\n7. STRESS SCENARIOS on the full plan (methodology §5; mix 2)")
    print(f"  {'':<62}{'to 89':>7}{'to 95':>7}")
    for lbl, kw in [("Full plan, base assumptions", full),
                    (f"A. Low-rate decade: equities {ST_EQ:.1%}, ladder {ST_BD:.1%}", {**full, "r_eq": ST_EQ}),
                    (f"B. Inflation shock: CPI {ST_CPI:.1%} + medical {M_ST:.2%}", {**full, "cpi": ST_CPI, "med": STRESS}),
                    (f"C. Long life + medical: medical {M_ST:.2%} (read the 95 column)", {**full, "med": STRESS})]:
        rb = ST_BD if lbl.startswith("A.") else R_LAD
        s89,_,_ = sim(MIX2[0], MIX2[1], rb, C89, **kw); s95,_,_ = sim(MIX2[0], MIX2[1], rb, C95, **kw)
        print(f"  {lbl:<62}{s89:>7.0%}{s95:>7.0%}")

    print(f"\n8. PROPERTY OPTIONS (annuity, survivor spending and business sale on; mix 2; today's money)")
    for end in (C89, C95):
        print(f"  to {end} (Carmen {end-1977})")
        print(f"  {'':<52}{'success':>9}{'portfolio':>12}{'home equity':>13}{'legacy':>11}")
        for lbl, s, m, h in property_options(end):
            print(f"  {lbl:<52}{s:>9.0%}{m/1e6:>11.1f}M{h/1e6:>12.1f}M{(m+h)/1e6:>10.1f}M")

    print("\n9. REBALANCING RULES vs HOLD-THE-TARGET (full plan, 40/60, to 89)")
    print(f"  {'':<52}{'success':>9}{'worst yr':>10}{'median end':>14}")
    for lbl, pol in [("Hold the target (rebalance every year)", "target"), ("Never rebalance (drift)", "drift"),
                     ("M3/M9: 5pp bands, new money to the underweight side", "bands"),
                     ("M1 only: rebalance after a 20% equity fall", "m1")]:
        s, wr, m = sim_rules(pol, C89)
        print(f"  {lbl:<52}{s:>9.0%}{wr:>10.1%}{m:>14,.0f}")

    print("\nDone. Change assumptions in wong_model.xlsx (Inputs tab), not here.")

if __name__ == "__main__":
    main()
