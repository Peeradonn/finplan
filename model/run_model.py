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
# HKMC annuities: fixed HK$, single life. Adrian buys at 65 (2037), Carmen when she stops work at 62 (2039).
ANN_A_COST, ANN_A_INC = g('Annuity: Adrian premium (MPF at 65, 2037)'), g('Annuity: Adrian income a year')
ANN_C_COST, ANN_C_INC = g('Annuity: Carmen premium (MPF at 62, 2039)'), g('Annuity: Carmen income a year')
ANN_INC = ANN_A_INC + ANN_C_INC                   # both alive, from 2039
MORT     = g("Mortgage: balance repaid at Adrian's retirement (2037)")   # outside the 780K; cleared in 2037
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
def mpf_in(y):
    """MPF contributions into the pool: employee + employer (HK$18K each side, capped) per working parent.
    The surplus is after the employee's contribution, and the MPF balances are inside the pool, so both sides
    must be added back while each parent works."""
    working = (y < RETA) + (y < RETC)
    return 2 * MPF_CAP * working
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
SWITCH_Y = int(g('Medical plan review: switch to Standard (year)'))
SWITCH = {y: (FLEXI.get(y, 0) if y < SWITCH_Y else STD.get(y, 0)) for y in set(FLEXI) | set(STD)}
STD_ST = med_path(2, stress=True)
SWITCH_ST = {y: (STRESS.get(y, 0) if y < SWITCH_Y else STD_ST.get(y, 0)) for y in set(STRESS) | set(STD_ST)}

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

def ann_income(y, annuity=True):
    """Annuity income in year y: Adrian's from his retirement until his death (single life), Carmen's from hers."""
    if not annuity:
        return 0
    return (ANN_A_INC if RETA <= y <= ALE else 0) + (ANN_C_INC if y >= RETC else 0)

# ---------- Monte Carlo ----------
FLOOR_SHARE = g('Retirement income floor %')      # essentials: never cut by the guardrails
GK_MED = False                                    # set True to let medical premiums trigger cuts
GK_MIN = g('Guardrails: lowest discretionary share')   # discretionary spending never cut below this

def sim(w_eq, s_bd, r_bd, end, annuity, med=None, surv=1.0, biz=0, rmp=0, r_eq=None, cpi=None,
        inflows=None, n=10_000, seed=42, paths=False, guard=False, detail=False):
    """Success share, mean worst year, median end pot.
    paths=True also returns every path's pot by year. detail=True returns a dict instead (run-out years,
    spending cuts). guard=True applies Guyton-Klinger guardrails to the discretionary share of spending:
    no inflation rise after a negative year; cut 10% if the withdrawal rate is 20% above its starting level;
    raise 10% (never above the target) if it is 20% below. Essentials (FLOOR_SHARE) are never cut."""
    r_eq = R_EQ if r_eq is None else r_eq
    cpi = CPI if cpi is None else cpi
    med, inflows = med or {}, inflows or {}
    rng = np.random.default_rng(seed)
    pot = np.full(n, POOL, float); alive = np.ones(n, bool); worst = np.zeros(n)
    track = np.zeros((end - BY, n)) if paths else None
    d = np.ones(n); wr0 = None; last_r = np.zeros(n)
    runout = np.zeros(n, int); d_min = np.ones(n); lvl_sum = np.zeros(n); lvl_n = 0
    lvl_hist, lvl_years = [], []
    for i in range(end - BY):
        y = BY + i
        r = w_eq*rng.normal(r_eq, S_EQ, n) + (1-w_eq)*rng.normal(r_bd, s_bd, n)
        worst = np.minimum(worst, r); pot = pot*(1+r)
        if annuity and y == RETA: pot -= ANN_A_COST
        if annuity and y == RETC: pot -= ANN_C_COST
        if y == RETA: pot -= MORT                           # mortgage still owed, cleared at retirement
        pot += mpf_in(y)                                   # MPF contributions, both sides, while working
        if y < RETA:
            pot += SURPLUS*(1+WAGE)**i - PREM
        else:
            target = SPEND*(1+cpi)**i*(surv if y > ALE else 1)
            income = ann_income(y, annuity) + (rmp if rmp and y >= RMP_Y else 0)                      + (CARMEN_NET*(1+WAGE)**i if y < RETC else 0)
            if guard and y >= RETC:                          # rules start with full retirement (Carmen at 62)
                d = np.where(last_r < 0, d/(1+cpi), d)     # no inflation rise after a negative year
                # trigger on lifestyle spending only: the planned rise in medical premiums is budgeted, not a
                # market signal, so it must not cause cuts (premiums are still paid in full below)
                net = target*(FLOOR_SHARE + (1-FLOOR_SHARE)*d) - income + (med.get(y, 0) if GK_MED else 0)
                wr = np.where(pot > 0, net/np.maximum(pot, 1), np.inf)
                if wr0 is None: wr0 = wr.copy()            # starting withdrawal rate, per path, in 2039
                cut_ok = y <= C89 - 15                      # Guyton-Klinger: no cuts in the last 15 years
                d = np.where(cut_ok & (wr > 1.2*wr0), d*0.9, np.where(wr < 0.8*wr0, np.minimum(d*1.1, 1.0), d))
                d = np.maximum(d, GK_MIN); d_min = np.minimum(d_min, d)
                lvl_sum += FLOOR_SHARE + (1-FLOOR_SHARE)*d; lvl_n += 1
                spend = target*(FLOOR_SHARE + (1-FLOOR_SHARE)*d)
            elif guard:
                spend = target*(FLOOR_SHARE + (1-FLOOR_SHARE)*d)
            else:
                spend = target
            pot += income - spend
            # share of target actually spent: when the pot is empty, only guaranteed income and what was left
            short = np.maximum(-pot, 0)
            lvl_hist.append(np.maximum(spend - short, 0) / target); lvl_years.append(y)
        if biz and y == BIZ_Y: pot += biz
        pot += inflows.get(y, 0)
        pot -= med.get(y, 0)
        pot = np.maximum(pot, 0)
        newly = alive & (pot <= 0); runout[newly] = y
        alive &= pot > 0; last_r = r
        if paths: track[i] = pot
    if detail:
        return dict(success=alive.mean(), runout=runout, alive=alive, d_min=d_min, end_pot=pot,
                    level=(lvl_sum/lvl_n if lvl_n else np.ones(n)),
                    low=FLOOR_SHARE + (1-FLOOR_SHARE)*d_min,
                    levels=np.array(lvl_hist), level_years=np.array(lvl_years))
    out = (alive.mean(), worst.mean(), np.percentile(pot, 50))
    return out + (track,) if paths else out

MIXES = {"1. All-Treasury ladder":       (0.00, 0.02, R_LAD),
         "2. 40/60 equity / ladder":     (0.40, 0.02, R_LAD),
         "3. 60/40 equity / bond funds": (0.60, 0.05, R_BOND)}
MIX2 = MIXES["2. 40/60 equity / ladder"]

def ladder_steps():
    """The decision ladder: each step adds one decision to the ones before. The annuity comes last: it is
    insurance for the worst markets and a long life, and added first (onto a failing plan) its premium shows as a
    loss that it is not. Its value is reported separately (ann_* numbers)."""
    return [
        ("Portfolio alone; Flexi premiums on top of the 780,000", dict(annuity=False, med=FLEXI)),
        (f"+ spending falls to {SURV:.0%} after Adrian's {ALE - 1972}",
                                                                 dict(annuity=False, med=FLEXI, surv=SURV)),
        (f"+ Carmen's business sold ({BIZ/1e6:.1f}M in {BIZ_Y})",  dict(annuity=False, med=FLEXI, surv=SURV, biz=BIZ)),
        (f"+ reverse mortgage ({RMP/1e3:.0f}K a year from {RMP_Y})",
                                                                 dict(annuity=False, med=FLEXI, surv=SURV, biz=BIZ, rmp=RMP)),
        ("+ MPF annuitised (HKMC, fixed HK$, single life)",
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
        if y == RETA: flow -= ANN_A_COST
        if y == RETC: flow -= ANN_C_COST
        if y == RETA: flow -= MORT
        flow += mpf_in(y)
        if y < RETA: flow += SURPLUS*(1+WAGE)**i - PREM
        else:
            flow -= SPEND*(1+CPI)**i*(SURV if y > ALE else 1) - ann_income(y, True)
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


# ---------- numbers quoted in the proposal (written to figures/numbers.json by make_charts.py) ----------
def export_numbers():
    """Every model number the text quotes, formatted as printed. Documents use {{key}} placeholders."""
    global RMP_Y, ALE
    P = lambda x: f"{x*100:.0f}%"                       # 0.873 -> "87%"
    K = lambda x: f"HK${x/1e3:,.0f}K"                    # 751000 -> "HK$751K"
    Mn = lambda x: f"HK${x/1e6:.1f}M"
    pts = lambda a, b: f"{(b-a)*100:+.0f}"               # step size in points
    N = {}
    full = full_plan()
    s89 = lambda kw, **o: sim(*MIX2, C89, **{**kw, **o})[0]
    s95 = lambda kw, **o: sim(*MIX2, C95, **{**kw, **o})[0]
    # decision ladder
    lad = [(s89(kw), s95(kw)) for _, kw in ladder_steps()]
    for i, (a, b) in enumerate(lad, 1):
        N[f"ladder_{i}_89"], N[f"ladder_{i}_95"] = P(a), P(b)
    N["step_survivor"], N["step_business"] = pts(lad[0][0], lad[1][0]), pts(lad[1][0], lad[2][0])
    N["step_home"], N["step_annuity"] = pts(lad[2][0], lad[3][0]), pts(lad[3][0], lad[4][0])
    sw89, sw95 = s89(full, med=SWITCH), s95(full, med=SWITCH)
    N["switch_89"], N["switch_95"], N["switch_pts"] = P(sw89), P(sw95), pts(lad[4][0], sw89)
    # one change at a time to the full plan
    N["eq7_89"], N["eq5_89"] = P(s89(full, r_eq=R_EQ+.01)), P(s89(full, r_eq=R_EQ-.01))
    N["no_annuity_89"], N["no_annuity_95"] = P(s89(full, annuity=False)), P(s95(full, annuity=False))
    N["biz_not_sold_89"] = P(s89(full, biz=0))
    N["cpi_stress_89"] = P(s89(full, cpi=ST_CPI))
    N["med_stress_89"], N["med_stress_95"] = P(s89(full, med=STRESS)), P(s95(full, med=STRESS))
    N["survivor_none_89"] = P(s89(full, surv=1.0))
    keep = RMP_Y; RMP_Y = 2045; N["rmp2045_89"] = P(s89(full)); RMP_Y = keep
    # stress scenarios
    N["stressA_89"] = P(sim(MIX2[0], MIX2[1], ST_BD, C89, **{**full, "r_eq": ST_EQ})[0])
    N["stressB_89"] = P(s89(full, cpi=ST_CPI, med=STRESS))
    # property options
    po = property_options(C89)
    for key, (lbl, s_, m_, h_) in zip(("keep", "rmp", "down"), po):
        N[f"prop_{key}_89"], N[f"legacy_{key}"] = P(s_), Mn(m_ + h_)
    N["legacy_down_vs_rmp"] = Mn((po[2][2] + po[2][3]) - (po[1][2] + po[1][3]))
    # rebalancing rules
    N["rebal_target_89"], N["rebal_bands_89"], N["rebal_drift_89"] = (P(sim_rules(p_, C89)[0]) for p_ in ("target", "bands", "drift"))
    # what happens when the plan falls short
    def life(kw):
        a = sim(*MIX2, C89, detail=True, **{**full, **kw}); b = sim(*MIX2, C95, detail=True, **{**full, **kw})
        L = b["levels"]
        return a, b, np.median(a["levels"].mean(0))*SPEND, np.percentile(L.min(0), 5)*SPEND
    for key, kw in (("fixflex", dict(guard=False, med=FLEXI)), ("fixswitch", dict(guard=False, med=SWITCH)),
                    ("guardswitch", dict(guard=True, med=SWITCH))):
        a, b, typ, w5 = life(kw)
        N[f"{key}_89"], N[f"{key}_95"], N[f"{key}_typical"], N[f"{key}_worst5"] = P(a["success"]), P(b["success"]), K(typ), K(w5)
        if key == "fixflex":
            fail = ~a["alive"]
            N["runout_age"] = f"{np.median(a['runout'][fail]) - 1977:.0f}" if fail.any() else "n/a"
            N["runout_age_p10"] = f"{np.percentile(a['runout'][fail], 10) - 1977:.0f}" if fail.any() else "n/a"
    # the same stresses on the recommended plan: tier review at 75 plus guardrails (§11 register)
    rec = {**full, "med": SWITCH, "guard": True}
    for key, o in (("cpi", dict(cpi=ST_CPI)), ("med", dict(med=SWITCH_ST)), ("lowret", dict(r_eq=ST_EQ)),
                   ("biz", dict(biz=0)), ("surv", dict(surv=1.0)), ("stressB", dict(cpi=ST_CPI, med=SWITCH_ST))):
        bd = ST_BD if key == "lowret" else MIX2[2]
        a = sim(MIX2[0], MIX2[1], bd, C89, detail=True, **{**rec, **o})
        N[f"rec_{key}_89"], N[f"rec_{key}_typical"] = P(a["success"]), K(np.median(a["levels"].mean(0))*SPEND)
    N["guard_cost"] = K(SPEND - float(N["guardswitch_typical"].strip("HK$K").replace(",", ""))*1e3)
    N["guaranteed_income_today"] = K((ann_income(2062, True) + RMP)/(1 + CPI)**(2062 - BY))
    N["guaranteed_income_nominal"] = K(ann_income(2062, True) + RMP)
    N["annuity_adrian"], N["annuity_carmen"] = K(ANN_A_INC), K(ANN_C_INC)
    # the annuity is insurance for the worst markets: on the recommended plan, the lowest year of spending in the
    # worst 1% of paths (to Carmen's 95), with and without it, and what it costs the typical family
    rec = {**full, "med": SWITCH, "guard": True}
    w, wo = sim(*MIX2, C95, detail=True, **rec), sim(*MIX2, C95, detail=True, **{**rec, "annuity": False})
    N["ann_w1_with"] = K(np.percentile(w["levels"].min(0), 1)*SPEND)
    N["ann_w1_without"] = K(np.percentile(wo["levels"].min(0), 1)*SPEND)
    N["ann_typ_cost"] = K((np.median(wo["levels"].mean(0)) - np.median(w["levels"].mean(0)))*SPEND)
    l89w, l89wo = sim(*MIX2, C89, detail=True, **rec), sim(*MIX2, C89, detail=True, **{**rec, "annuity": False})
    N["ann_legacy_cost"] = Mn((np.median(l89wo["end_pot"]) - np.median(l89w["end_pot"]))/(1 + CPI)**(C89 - BY))
    # the income floor over time (nominal): essentials are 40% of spending (70% of it after Adrian's death)
    for y in (RETC, ALE + 1, C89):
        ess = SPEND*FLOOR_SHARE*(SURV if y > ALE else 1)*(1 + CPI)**(y - BY)
        inc = ann_income(y, True)
        N[f"floor_{y}_ess"], N[f"floor_{y}_ann"] = K(ess), K(inc)
        N[f"floor_{y}_pct"] = P((inc + RMP)/ess)
    # accumulation: what is invested each year, and the range of the portfolio when Adrian retires
    N["surplus_invest"] = K(SURPLUS - PREM)
    track = sim(*MIX2, C89, paths=True, **full)[3]
    i = RETA - 1 - BY                                   # end of 2036 = the day Adrian retires
    real = track[i] / (1 + CPI)**(i + 1)
    N["port2037_p10"], N["port2037_p90"] = Mn(np.percentile(real, 10)), Mn(np.percentile(real, 90))
    # the annuity is longevity insurance: its value shows when Adrian outlives his life expectancy
    keep = ALE; ALE = 2067
    try:
        N["annuity_longlife_pts"] = pts(s95(full, annuity=False), s95(full))
    finally:
        ALE = keep
    # positions from the workbook
    N["portfolio_2037_today"] = Mn(O["Outputs.Portfolio at 2037 in TODAY money"])
    N["need_2037"] = Mn(pv(SPEND, .02, C89 - RETA))
    N["premiums_avg"] = K(PREM)
    N["surplus"] = K(SURPLUS)
    return N

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
    for lbl, kw in [(f"   Standard plan from {SWITCH_Y} (tier review)", {**full, "med": SWITCH}),
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

    print("\n10. WHEN THE PLAN FALLS SHORT (full plan, mix 2)")
    print(f"  {'':<52}{'to 89':>7}{'to 95':>7}{'avg spend':>11}{'hit floor':>11}")
    floor_level = FLOOR_SHARE + (1 - FLOOR_SHARE) * GK_MIN
    for lbl, kw in [("Fixed spending, Flexi for life", dict(guard=False, med=FLEXI)),
                    (f"Fixed spending, Standard from {SWITCH_Y}", dict(guard=False, med=SWITCH)),
                    ("Guardrails, Flexi for life", dict(guard=True, med=FLEXI)),
                    (f"Guardrails, Standard from {SWITCH_Y}", dict(guard=True, med=SWITCH))]:
        a = sim(*MIX2, C89, detail=True, **{**full, **kw}); b = sim(*MIX2, C95, detail=True, **{**full, **kw})
        if kw["guard"]:
            extra = f"{np.median(a['level']):>11.0%}{(a['low'] <= floor_level + 1e-3).mean():>11.0%}"
        else:
            extra = f"{'100%':>11}{'-':>11}"
        print(f"  {lbl:<52}{a['success']:>7.0%}{b['success']:>7.0%}{extra}")
    print("  How the family lives (today's money; target = HK$780K):")
    print(f"  {'':<40}{'avg typical':>12}{'avg worst10':>12}{'low typical':>12}{'low worst10':>12}{'yrs<90% typ':>12}{'low w5%,95':>12}")
    for lbl, kw in [("Fixed spending, Flexi for life", dict(guard=False, med=FLEXI)),
                    (f"Fixed spending, Standard from {SWITCH_Y}", dict(guard=False, med=SWITCH)),
                    ("Guardrails, Flexi for life", dict(guard=True, med=FLEXI)),
                    (f"Guardrails, Standard from {SWITCH_Y}", dict(guard=True, med=SWITCH))]:
        L = sim(*MIX2, C89, detail=True, **{**full, **kw})["levels"]
        avg, low = L.mean(0)*SPEND/1e3, L.min(0)*SPEND/1e3
        L95 = sim(*MIX2, C95, detail=True, **{**full, **kw})["levels"]
        print(f"  {lbl:<40}{np.median(avg):>11.0f}K{np.percentile(avg,10):>11.0f}K{np.median(low):>11.0f}K"
              f"{np.percentile(low,10):>11.0f}K{np.median((L<0.9).mean(0)):>12.0%}{np.percentile(L95.min(0)*SPEND/1e3,5):>11.0f}K")
    D = sim(*MIX2, C89, detail=True, **full); fail = ~D["alive"]
    if fail.any():
        ages = D["runout"][fail] - 1977
        print(f"  Fixed spending, Flexi: failing paths run out at Carmen's {np.median(ages):.0f} (median), "
              f"{np.percentile(ages, 10):.0f} (10th percentile)")
    y = 2062; inc = ann_income(y, True) + RMP
    print(f"  Guaranteed income after a run-out (annuity + reverse mortgage): HK${inc/1e3:.0f}K nominal, "
          f"HK${inc/(1+CPI)**(y-BY)/1e3:.0f}K in today's money at Carmen's 85")

    print("\nDone. Change assumptions in wong_model.xlsx (Inputs tab), not here.")

if __name__ == "__main__":
    main()
