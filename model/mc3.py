import numpy as np
rng=np.random.default_rng(42); N=10_000
CPI=.025; Y0=2026; RET=2037; C89=2066; C95=2072
POOL=9_790_000-2_567_698; SUR0=718_230; WAGE=.03; SPEND=780_000; CARMEN=300_000
ANNUITY_COST=4_120_000      # Pete: MPF 2.31M (A, 65) + 1.81M (C) annuitised
ANNUITY_INC =268_000        # HKMC payout

def sim(w_eq,r_eq,s_eq,r_bd,s_bd,end,buy_annuity=False):
    yrs=end-Y0; pot=np.full(N,POOL,float); alive=np.ones(N,bool); worst=np.zeros(N)
    for i in range(yrs):
        y=Y0+i
        r=w_eq*rng.normal(r_eq,s_eq,N)+(1-w_eq)*rng.normal(r_bd,s_bd,N)
        worst=np.minimum(worst,r); pot=pot*(1+r)
        if y==RET and buy_annuity: pot-=ANNUITY_COST
        if y<RET: pot+=SUR0*(1+WAGE)**i
        else:
            pot-=(SPEND-(ANNUITY_INC if buy_annuity else 0))*(1+CPI)**i
            if y<2039: pot+=CARMEN*(1+WAGE)**i
        pot=np.maximum(pot,0); alive&=pot>0
    return alive.mean(),worst.mean(),np.percentile(pot,50)

MIX={"1. All-Treasury ladder":(0.00,.02),"2. 40/60 equity / ladder":(0.40,.02),"3. 60/40 equity / bond funds":(0.60,.05)}
for tag,buy in [("PORTFOLIO ALONE",False),("WITH MPF ANNUITISED (cost deducted)",True)]:
    print(f"\n{tag}")
    print(f"{'Mix':<30}{'to 89':>7}{'to 95':>7}{'worst yr':>10}{'median end (89)':>18}")
    for n,(w,sb) in MIX.items():
        s89,wr,med=sim(w,.06,.17,.04,sb,C89,buy); s95,_,_=sim(w,.06,.17,.04,sb,C95,buy)
        print(f"{n:<30}{s89:>6.0%}{s95:>7.0%}{wr:>9.1%}{med:>18,.0f}")

print("\nEQUITY 6% vs 7%  (mix 2, annuitised, to 89 / to 95)")
for r in (.06,.07):
    a,_,_=sim(.40,r,.17,.04,.02,C89,True); b,_,_=sim(.40,r,.17,.04,.02,C95,True)
    print(f"  equity {r:.0%}: {a:.0%} / {b:.0%}")
