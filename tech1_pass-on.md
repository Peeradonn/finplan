# Pass-on numbers — v2

Owner: Fahtai (model). Updated 27 Sep 2026. Supersedes v1 of 24 Sep.
Model: `wong_model.xlsx` (inputs, balance sheet, tax engine) · `model.py`, `mc3.py` (projection, Monte Carlo).

**Nothing goes into the proposal that is not on this page or out of the model.**

---

## 0. Headline for tonight

> **The deterministic plan works, but only just — and the Monte Carlo is what makes the case for the income floor.**
> Parents' portfolio alone: **61–65%** chance of sustaining HK$780K to Carmen 89.
> With the MPF annuitised (cost deducted): **80–88%**.
> The family needs a real return of only **1.5%**, but the margin of safety is thin, not comfortable.
> That is the single most useful number we have: it turns Pete's income floor from a nice idea into a necessity.

---

## 1. Corrections to v1 — please re-read if you used it

v1 was built on 2025/26 tax parameters. **Pete's figures were right and mine were wrong.** Now fixed.

| | v1 (wrong) | v2 (correct) |
|---|---|---|
| Basic allowance | 132,000 | **145,000** |
| Married | 264,000 | **290,000** |
| Child | 130,000 | **140,000** |
| Dependent parent 60+ | 50,000 | **55,000** |
| Home loan interest | not modelled | **63,000, split 50/50** |
| Couple's tax | 200,300 | **181,770** |
| Annual surplus | 699,700 | **718,230** |

---

## 2. Confirmed — open item #3 is closed

The tax engine in `wong_model.xlsx` reproduces Pete's workings to the dollar.

| | Joint | Separate |
|---|---|---|
| Adrian | — | **110,435** |
| Carmen | — | **71,335** |
| **Couple** | **199,770** | **181,770** |
| Ryan | 8,000 | 8,000 |

Separate taxation wins by **exactly 18,000**, for the reason Pete gives: the married allowance (290,000)
is exactly two basic allowances, so joint gains nothing on allowances but loses one set of progressive
bands — 17% × 200,000 − 16,000 = 18,000.

> **Caveat worth one line in §2:** separate assessment is the *default* in Hong Kong. This 18,000 is a
> mistake avoided, not value created, unless the Wongs are currently electing joint. Ask them. Presenting
> it as advice value would be overclaiming, and a judge who knows the system would notice.

**Surplus:** 1,920,000 − 181,770 tax − 36,000 MPF − 984,000 expenses = **718,230**. Matches Pete.

**Balance sheet:** the model reproduces 24,405,000 net worth exactly. Check cell is zero.

---

## 3. Retirement — Pete's numbers confirmed

| | Model | Pete |
|---|---|---|
| Need at 2037, to Carmen 89 (29 yrs, 2% real) | **17,038,620** | ≈17.0M |
| Need at 2037, to Carmen 95 (35 yrs) | 19,498,923 | — |
| Projected pool at 2037 (2% real) | **17,719,962** | ≈17.4M |
| Funded ratio | **104%** | — |
| **Required real return** | **1.51%** (≈4.05% nominal) | "≈2%, they need little risk" |

Pete's characterisation is right: the *required return* is low. But 104% funded is a thin margin, and
the Monte Carlo below shows what that thinness costs once you allow for volatility and sequence risk.

Education reserve used: **2,567,698** (overseas at the case's 600K high end, escalated 5%, discounted 3%).
Local high-end would be 1,069,874 — the overseas-high choice is deliberately conservative.

---

## 4. Monte Carlo — Win's three mixes (10,000 paths, equity 6%/17% vol)

**Portfolio alone — no annuity, no property, no business**

| Mix | to 89 | to 95 | Avg worst year | Median end (89) |
|---|---|---|---|---|
| 1. All-Treasury ladder | 39% | 1% | −0.6% | 0 |
| 2. 40/60 equity / ladder | **65%** | 45% | −10.1% | 8,029,299 |
| 3. 60/40 equity / bond funds | 61% | 49% | −17.3% | 9,308,608 |

**With MPF annuitised — 4.12M cost deducted, 268K/yr income added**

| Mix | to 89 | to 95 |
|---|---|---|
| 1. All-Treasury ladder | **100%** | 76% |
| 2. 40/60 equity / ladder | **88%** | 76% |
| 3. 60/40 equity / bond funds | 80% | 70% |

Three findings worth writing up:

1. **Safety alone fails.** The all-Treasury ladder has a 39% chance of lasting to 89 and 1% to 95.
   Capital preservation without growth is not the safe choice — that is a strong line for Adrian's section.
2. **The annuity is the single biggest lever**, worth more than any allocation change: +23pp on mix 2.
   It converts sequence risk into a guaranteed floor. This quantifies Pete's innovation ①.
3. **More equity does not help here.** Mix 3 is worse than mix 2 on every measure once the annuity is in.
   **Recommend mix 2 (40/60 with the ladder) for Adrian.**

---

## 5. Answers to Win's three asks

**Equity return: lock 6.0%.** With the annuity in place, 6% gives 88% success and 7% gives 94% — the plan
works either way, so the conservative number costs us nothing and buys credibility. It also means every
recommendation is stress-tested at the lower figure. Note this **differs from Pete's lock table (7.0%)** —
needs 30 seconds of agreement tonight.

**Bond row:** Treasury ladder held to maturity at **4.0% nominal, ~2% volatility** (no price risk if held).
Bond *funds* carry ~5% volatility — that difference is why mix 2 beats mix 3, so keep the two distinct.

**Recommended mix for Adrian: #2, 40/60 equity / Treasury ladder.**

Rules M1–M9 testing is next; I have the harness and will report Tuesday as asked.

---

## 6. Value of advice — status quo vs plan, at 2037

| | HK$ |
|---|---|
| Status quo | 19,701,480 |
| With the plan | 24,858,714 |
| **Value added** | **5,157,234 (+26%)** |

Four drivers, largest first:
1. Deploying idle cash — the emergency reserve falls from 30.5 months to 12, freeing ~1.5M
2. **Repaying the 85,000 card — 1,438,336 of avoided interest over 11 years at 30%**
3. Investments rebalanced to the target mix (5.5% vs 4.2% unmanaged)
4. TVC/QDAP at 60,000 each — 20,400/yr of tax saved, reinvested

> **Two assumptions this number depends on, both need the team to sign off tonight:**
> (a) the status-quo investment return of **4.2%** — this is Win's open "current-fund-fee" question, and it
> drives most of the 5.16M; (b) the card genuinely revolves at ~30%. The case says "credit card and
> revolving balance", but if the Wongs clear it monthly, driver 2 disappears. **Ask the question rather than
> assume it** — an unchallenged 1.4M claim is exactly what a judge will probe.

---

## 7. Open items

| # | Item | Owner | Due |
|---|---|---|---|
| 1 | Agree equity return 6% vs Pete's 7% | Team | tonight |
| 2 | Agree the status-quo return assumption (4.2%) for value of advice | Team / Win | tonight |
| 3 | Confirm the card revolves, and whether the Wongs elect joint assessment | Lead → client assumptions | tonight |
| 4 | Test rules M1–M9 against "hold the target" | Fahtai | 29 Sep |
| 5 | Load the medical path, VHIS ageing curve, cash path and FX stress | Fahtai | 29 Sep |
| 6 | Insurance premiums — they reduce the 718,230 surplus, so every number here shifts | Lookbua | 29 Sep |
| 7 | Six charts | Fahtai | 30 Sep |

---

## 8. Change log

| Version | Date | Change |
|---|---|---|
| v2 | 2026-09-27 | Tax rebuilt on 2026/27 parameters; open item #3 closed; baseline, Monte Carlo, value of advice added; Excel model published. |
| v1 | 2026-09-24 | First issue. Superseded — tax parameters were wrong. |
