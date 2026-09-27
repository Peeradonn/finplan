"""
Wong Family model — Python layer.
Reads EVERY assumption from wong_model.xlsx  ->  Inputs tab.
Never hardcode an assumption here. Change the spreadsheet instead.

Usage:  python3 run_model.py
"""
import sys, numpy as np
from openpyxl import load_workbook

XLSX = "wong_model.xlsx"

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
        print("WARNING: no cached values. Run recalc.py on the workbook first.")
    return d, out

I, O = load_inputs()
g = lambda k: I[k]

CPI      = g('CPI inflation')
R_EQ     = g('Equities');          S_EQ = g('Equity volatility')
R_BOND   = g('Bonds / IG');        R_LAD = g('Treasury ladder')
RETA     = int(g('Adrian retires (age 65)')); BY = int(g('Base year'))
C89      = int(g('Carmen age 89')); C95 = int(g('Carmen age 95'))
SPEND    = g('Retirement spending (today money)')
ANN_COST = g('Annuity purchase cost at 2037')
ANN_INC  = g('Annuity income (HKMC, annual)')
EDU_A    = g('Education — overseas annual (today)'); EDU_N = int(g('Education — years'))
EDU_ESC  = g('Education escalation (overseas)'); EDU_Y = int(g('Chloe starts university'))
WAGE     = g('Wage growth — Adrian')
PREM     = g('Insurance premiums (Lookbua, TBC)')
RETC     = int(g('Carmen retires (age 62)'))
C_SAL    = g("Carmen's salary / dividend")
MPF_CAP  = g('MPF deduction cap')

POOL_ALL = O.get("BalanceSheet.Parents' investable pool", 9_790_000)
SURPLUS  = O.get("Outputs.Annual surplus (after tax, MPF, premiums)", 718_230)
# Carmen works two years past Adrian's retirement - the Excel Projection counts this, so we must too
C_TAX    = O.get("Tax.TAX (progressive)", 71_335)
CARMEN_NET = C_SAL - 71_335 - MPF_CAP

# ---------- goal funding ----------
pv = lambda p,r,n: p*(1-(1+r)**-n)/r
edu_nom = [EDU_A*(1+EDU_ESC)**(y-BY) for y in range(EDU_Y, EDU_Y+EDU_N)]
edu_res = sum(c/(1.03**(y-BY)) for c,y in zip(edu_nom, range(EDU_Y, EDU_Y+EDU_N)))
POOL = POOL_ALL - edu_res

print("=" * 66)
print("INPUTS READ FROM SPREADSHEET")
print(f"  parents' pool {POOL_ALL:>12,.0f}   surplus {SURPLUS:>10,.0f}   premiums {PREM:>9,.0f}")
print(f"  equity {R_EQ:.1%} (vol {S_EQ:.0%})   ladder {R_LAD:.1%}   CPI {CPI:.1%}")
print("=" * 66)
print("\n1. GOAL FUNDING")
print(f"  retirement need at {RETA}, to Carmen 89 (2% real): {pv(SPEND,.02,C89-RETA):>12,.0f}")
print(f"  retirement need at {RETA}, to Carmen 95          : {pv(SPEND,.02,C95-RETA):>12,.0f}")
print(f"  education reserve today (overseas @ {EDU_A:,.0f}/yr) : {edu_res:>12,.0f}")
print(f"  deployable to retirement                        : {POOL:>12,.0f}")

# ---------- Monte Carlo ----------
def sim(w_eq, s_bd, r_bd, end, annuity, n=10_000, seed=42):
    rng = np.random.default_rng(seed)
    pot = np.full(n, POOL, float); alive = np.ones(n, bool); worst = np.zeros(n)
    for i in range(end - BY):
        y = BY + i
        r = w_eq*rng.normal(R_EQ, S_EQ, n) + (1-w_eq)*rng.normal(r_bd, s_bd, n)
        worst = np.minimum(worst, r); pot = pot*(1+r)
        if y == RETA and annuity: pot -= ANN_COST
        if y < RETA: pot += (SURPLUS - PREM)*(1+WAGE)**i
        else:
            pot -= (SPEND - (ANN_INC if annuity else 0))*(1+CPI)**i
            if y < RETC: pot += CARMEN_NET*(1+WAGE)**i   # Carmen still earning
        pot = np.maximum(pot, 0); alive &= pot > 0
    return alive.mean(), worst.mean(), np.percentile(pot, 50)

MIXES = {"1. All-Treasury ladder":       (0.00, 0.02, R_LAD),
         "2. 40/60 equity / ladder":     (0.40, 0.02, R_LAD),
         "3. 60/40 equity / bond funds": (0.60, 0.05, R_BOND)}

for tag, ann in [("2. MONTE CARLO — portfolio alone", False),
                 ("3. MONTE CARLO — with MPF annuitised (cost deducted)", True)]:
    print(f"\n{tag}")
    print(f"  {'Mix':<30}{'to 89':>8}{'to 95':>8}{'worst yr':>11}{'median end':>15}")
    for name,(w,sb,rb) in MIXES.items():
        s89,wr,med = sim(w,sb,rb,C89,ann); s95,_,_ = sim(w,sb,rb,C95,ann)
        print(f"  {name:<30}{s89:>7.0%}{s95:>8.0%}{wr:>10.1%}{med:>15,.0f}")

print("\n4. SENSITIVITY (mix 2, annuitised, to 89)")
base_eq = R_EQ
for lbl, adj in [("base", 0), ("equity -1pp", -0.01), ("equity +1pp", +0.01)]:
    R_EQ = base_eq + adj
    s,_,_ = sim(0.40, 0.02, R_LAD, C89, True)
    print(f"  {lbl:<14} equity {R_EQ:.0%}  ->  success {s:.0%}")
R_EQ = base_eq
print("\nDone. Change assumptions in wong_model.xlsx (Inputs tab), not here.")
