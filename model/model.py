"""Wong Family deterministic model - assumptions per Pete's lock table (working-brief.md §4)."""
import numpy as np, json

# ---------------- ASSUMPTIONS (Pete's lock table) ----------------
CPI          = 0.025
WAGE_A       = 0.03
WAGE_C       = 0.03
EDU_OVERSEAS = 0.05
R_EQ         = 0.06      # Fahtai recommendation, see note (Pete's table says 0.07)
R_BOND       = 0.04
R_CASH_EARLY = 0.03      # 2027-28
R_CASH_LATE  = 0.025     # from 2031
R_IDLE       = 0.002
R_MPF        = 0.05
R_REIT       = 0.055

Y0 = 2026
A_AGE, C_AGE, CH_AGE = 54, 49, 16
A_RET, C_RET = 2037, 2039          # Adrian 65, Carmen 62
C89, C95     = 2066, 2072

# balance sheet
CASH, TDEP, MMF = 620_000, 1_480_000, 400_000
HK_EQ, GL_EQ, IG_BOND, ESG_EQ, GREEN_BD, STK_REIT = 1_000_000,1_350_000,900_000,700_000,450_000,800_000
MPF_A, MPF_C, MPF_R = 1_050_000, 620_000, 180_000
DIGITAL, INS_CV = 500_000, 420_000
CARD = 85_000

EXPENSE  = 984_000
SURPLUS0 = 718_230          # parents only, low bonus, after tax + MPF
RET_SPEND= 780_000          # today's money

# ---------------- 1. RETIREMENT NEED (confirm Pete's 17.0M) ----------------
def pv_annuity(pmt, r, n): return pmt*(1-(1+r)**-n)/r
N_RET = C89 - A_RET          # 29 years
need_2037 = pv_annuity(RET_SPEND, 0.02, N_RET)
need_2037_95 = pv_annuity(RET_SPEND, 0.02, C95-A_RET)
print("=== 1. RETIREMENT NEED (today's money, 2% real) ===")
print(f"  to Carmen 89 ({N_RET} yrs): {need_2037:>12,.0f}   [Pete: ~17.0M]")
print(f"  to Carmen 95 ({C95-A_RET} yrs): {need_2037_95:>12,.0f}")

# ---------------- 2. EDUCATION RESERVE ----------------
print("\n=== 2. EDUCATION (Chloe starts 2028, 4 years) ===")
for label, base in [("local high 250k",250_000),("overseas low 350k",350_000),("overseas high 600k",600_000)]:
    nom = [base*(1+EDU_OVERSEAS)**(y-Y0) for y in range(2028,2032)]
    pv  = sum(c/(1.03**(y-Y0)) for c,y in zip(nom,range(2028,2032)))
    print(f"  {label:<20} nominal total {sum(nom):>10,.0f}   reserve needed today {pv:>10,.0f}")
edu_reserve = sum(600_000*(1+EDU_OVERSEAS)**(y-Y0)/(1.03**(y-Y0)) for y in range(2028,2032))

# ---------------- 3. PARENTS' POOL AT 2037 ----------------
parents_pool = (CASH+TDEP+MMF+HK_EQ+GL_EQ+IG_BOND+ESG_EQ+GREEN_BD+STK_REIT+MPF_A+MPF_C+INS_CV)
print(f"\n=== 3. PARENTS' INVESTABLE POOL TODAY ===")
print(f"  total liquid + investment            10,470,000")
print(f"  less Ryan's MPF (180k) and digital (500k)")
print(f"  parents' pool                        {parents_pool:>10,.0f}")
print(f"  less overseas education reserve      {edu_reserve:>10,.0f}")
print(f"  deployable to retirement             {parents_pool-edu_reserve:>10,.0f}")

yrs = A_RET - Y0
for rr,lab in [(0.02,"2% real"),(0.025,"2.5% real"),(0.015,"1.5% real")]:
    fv_assets  = (parents_pool-edu_reserve)*(1+rr)**yrs
    fv_surplus = SURPLUS0*(((1+rr)**yrs-1)/rr)
    tot=fv_assets+fv_surplus
    flag = "  <-- Pete's 17.4M check" if rr==0.02 else ""
    print(f"  at {lab}: assets {fv_assets:>11,.0f} + surplus {fv_surplus:>11,.0f} = {tot:>12,.0f}  vs need {need_2037:>11,.0f}  ratio {tot/need_2037:.0%}{flag}")

# ---------------- 4. REQUIRED REAL RETURN (Win's ask) ----------------
print("\n=== 4. REQUIRED REAL RETURN (Win's 'what must be true' check) ===")
lo,hi=-0.02,0.10
for _ in range(200):
    mid=(lo+hi)/2
    tot=(parents_pool-edu_reserve)*(1+mid)**yrs + SURPLUS0*(((1+mid)**yrs-1)/mid if mid else yrs)
    if tot<need_2037: lo=mid
    else: hi=mid
print(f"  required real return to exactly fund the 2037 need: {hi:.2%}")
print(f"  = nominal {(1+hi)*(1+CPI)-1:.2%} at CPI 2.5%")
