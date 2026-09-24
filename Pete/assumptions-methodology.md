# Assumption Methodology: Medical Inflation, Cash Return, FX

**For:** Fahtai (model inputs), Win (cash and FX in the allocation), Lookbua (stress cases), and the proposal's
assumptions appendix.
**Data date:** 22–23 September 2026. Raw data and sources are in [macro-snapshot-2026-09-23.md](macro-snapshot-2026-09-23.md).

**Principle.** None of these three numbers is picked by vote. Each is built the way an institutional wealth manager
builds capital-market assumptions:
1. Start from what the market or current data says **now**.
2. Anchor the **long run** in an economic relationship that has held historically.
3. **Grade** between the two over a stated period.
4. Set the stress case from the **historical distribution**, not a round number.

Every figure below can be traced to a dataset or a formula.

---

## 1. Medical inflation: a three-stage trend, with ageing modelled separately

### 1a. Why a single flat number is wrong
Health actuaries don't project medical costs with one rate. The Society of Actuaries' long-run model (the
*Getzen model*, updated annually for US pension and retiree-medical valuations) uses three stages:
- a near-term trend taken from current insurer data;
- a long-run trend equal to nominal income growth plus a small "excess";
- a linear grade-down between the two.

The logic: medical spending cannot outgrow the economy by 4–5 points a year forever, because the health share of
GDP would eventually crowd out everything else. We apply the same structure to Hong Kong data.

### 1b. The three stages

| Stage | Value | How it is derived |
|---|---|---|
| **Near term (2027)** | **10.0%** | Average of the 2026 HK projections from the two largest insurer/broker surveys: WTW 9.9%, Mercer Marsh Benefits 10.5%. Aon puts HK below the 11.3% APAC average. |
| **Long run (2036 onward)** | **6.0%** | = nominal GDP-per-capita growth **4.0%** + excess cost growth **2.0pp**, derived below |
| **Grade-down** | linear, 2027 → 2036 | −0.44pp a year. Ten years is the standard grading period in actuarial practice |

**Long-run components:**
- *Nominal GDP per capita growth, 4.0%.*
  - HK history (World Bank): 3.0% a year over 1995–2025, 3.9% over 2005–2025.
  - Forward view: real GDP growth 2.7% less population growth 0.7% gives about 2.0% real per capita; add 2.5% CPI for about 4.5%.
  - 4.0% sits between the historical and forward figures.
- *Excess cost growth, 2.0pp.*
  - HK total health spending rose from **3.6% of GDP (1989/90) to 5.7% (2013/14)**, which is about 1.9pp a year faster than GDP (Domestic Health Accounts).
  - Current health spending reached **8.3% of GDP in 2023/24**. Over the full 34 years that is about 2.5pp a year.
  - The Getzen model assumes excess growth fades towards ~1pp as the health share rises. HK's share is still low by developed-market standards, so we use 2.0pp, at the lower end of HK's own history.

**Resulting path (use these rows in the model):**

| 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | 2036+ |
|---|---|---|---|---|---|---|---|---|---|
| 10.00% | 9.56% | 9.11% | 8.67% | 8.22% | 7.78% | 7.33% | 6.89% | 6.44% | 6.00% |

30-year average (2027–2056): **6.67%**. The handout's flat 7% was close on average but wrong in shape. It understates the
next five years and overstates the long run.

**Stress case: 8.54% every year, no grade-down.** This is the mean of WTW's HK trend over 2020–2026
(6.2, 9.8, 6.9, 8.8, 8.4, 9.8, 9.9). It asks what happens if the last seven years persist for another thirty.

### 1c. Ageing is a separate factor. This is the step most plans miss
A medical-trend survey measures cost growth **for a person of the same age**. An individual's premium also rises
because they get older. The two effects multiply, and a model that uses only the trend understates retirement
medical costs badly.

The age curve comes from the government's own data: the **VHIS standard-premium dataset** (Health Bureau, data.gov.hk,
tables effective 2025–26). It covers 424 Flexi plans and 33 Standard plans, standalone, non-smoker.

| Age | Flexi median, male | Flexi median, female | Standard median, male | Ratio to age 65 (Flexi) |
|---|---|---|---|---|
| 55 | 17,140 | 18,186 | 6,119 | 0.55 |
| 60 | 23,050 | 23,210 | 7,887 | 0.74 |
| 62 | 26,578 | 25,895 | 8,765 | 0.83 |
| 65 | 32,542 | 31,599 | 10,452 | 1.00 |
| 70 | 42,122 | 40,990 | 13,008 | 1.29 |
| 75 | 53,887 | 53,228 | 16,184 | 1.63 |
| 80 | 63,644 | 62,772 | 18,920 | 2.01 |

Premiums in HK$ a year at today's prices.
- **Age-only escalation from 65 to 80 is about 4.7% a year for Flexi plans and 3.9% for Standard.**
- The tables stop at age 80–81. Beyond 80, extrapolate the 75→80 slope, which is **3.4% a year**.
- **Use the Flexi median.** It is the realistic tier for a household with HK$24M of net worth; the Standard plan is the floor.

**Model formula:** premium(person, year) = VHIS_Flexi_median(age in that year) × ∏(1 + medical trend) from 2027 to that year.

**What it produces (nominal HK$ per person a year, base case):**

| | 2037 | 2042 | 2047 | 2052 |
|---|---|---|---|---|
| Adrian (age 65 / 70 / 75 / 80) | 74K | 129K | 221K | 349K |
| Carmen (age 60 / 65 / 70 / 75) | 53K | 97K | 168K | 292K |

This replaces the handout's "HK$40–60K per person, grown at 7%". That line overstated costs in the early years of
retirement and understated them late in life, which is the dangerous direction for longevity planning.

**Scope:** this covers insurance premiums only. Deductibles, co-payments and uncovered treatment are the
"extraordinary medical costs" the case excludes from the HK$780K. Cover them with the critical-illness cover and a
medical reserve inside the retirement liquidity bucket, not with this line.

**Practical implication for the proposal:** Carmen should buy an individual VHIS/Flexi policy **while still employed
and healthy**, before the employer group cover ends at 62. Pre-existing-condition exclusions and underwriting are the
real risk there, not the premium.

---

## 2. Cash and deposit return: forward curve, then a neutral-rate anchor

### 2a. Why not just use today's deposit rate
A 30-year plan needs the average cash return across rate cycles, not this month's promotional rate. Using 3.05% for
30 years would overstate returns. Using 2.5% flat would ignore that money deposited today locks in about 3%.

### 2b. The build

| Stage | Value | How it is derived |
|---|---|---|
| **2027–2028** | **3.0%** | Lockable today: best 12-month HKD time deposit is 3.05%. The HIBOR curve is upward-sloping (1M 2.89%, 12M 3.91%); the implied 6-month rate in six months is **4.27%**. The Fed's Sep 2026 projections put policy rates in the low 4s through 2027. |
| **Long run (2031 onward)** | **2.5%** | Average of two independent anchors (below) |
| **Grade** | 2029: 2.83% · 2030: 2.67% · 2031+: 2.50% | Linear. By about 2030 the Fed's projections converge on their longer-run rate |

**Long-run anchors.** Both take off an executable spread of −0.5pp: the gap between interbank rates and what a depositor
or money-market-fund holder actually earns after bank margin and fund fees. The spread observed today is −0.2 to −0.9pp.
1. *Forward-looking:* the Fed's longer-run neutral rate is **3.2%** (Sep 2026 median). The HKD peg imports US monetary
   policy, so HKD neutral ≈ USD neutral: 3.2% − 0.5 = **2.7%**.
2. *Historical:* HK money-market rates averaged **+0.2% real** over 1994–2025 (IMF IFS, World Bank CPI).
   2.5% CPI + 0.2% − 0.5 = **2.2%**.

Mean of the two = **2.45%, which rounds to 2.5%**. The handout's 2.5% was right, and it now has a derivation.

**Stress case: 0.5% from 2029 onward.** This is a return to the 2009–2021 regime, when HK money-market rates averaged
**0.36%** and the real return on cash was **−2.3% a year**. That happened within the last 15 years, so it is a real
scenario, not a tail event.

**Separate line for idle balances: 0.2%.** The HK savings-account rate averaged 0.20% in 2025 (World Bank). The Wongs'
HK$620K in savings and current accounts earns this unless it is moved. Moving the excess into time deposits or an
MMF is an easy quantified recommendation: for HK$500K, (3.0% − 0.2%) × 500K ≈ **HK$14,000 a year**.

---

## 3. FX: spot as the base, historical distribution for stress

### 3a. Base case = spot rate, no drift
- Exchange rates are close to a random walk. Since Meese & Rogoff (1983), no forecasting model has reliably beaten
  "tomorrow = today" at 1–5 year horizons.
- Forward rates are not forecasts either. They only reflect interest-rate differences, and they are a well-documented
  biased predictor (the forward premium puzzle).
- So the base case is **spot at the lock date**, from ECB reference rates (22 Sep 2026, HKD per unit):

| USD | GBP | CAD | SGD |
|---|---|---|---|
| 7.843 | 10.481 | 5.585 | 6.153 |

(The snapshot's earlier CAD of 5.68 came from a 4 Sep quote and is superseded.)

### 3b. Stress case = the 95th-percentile adverse move over the payment horizon
Chloe's fees fall in 2028/29–2031/32, **2 to 5 years ahead**. The risk is the foreign currency *strengthening* against
HKD. From 20 years of daily ECB rates (2006–2026), we measured every 2-, 3-, 4- and 5-year change and took the 95th
percentile:

| | 2y | 3y | 4y | 5y | **Stress (average of 2–5y)** | Worst 2–5y move ever |
|---|---|---|---|---|---|---|
| GBP | +11.0% | +9.2% | +10.4% | +8.7% | **+10%** | +28% |
| CAD | +15.0% | +11.5% | +15.3% | +15.6% | **+14%** | +33% |
| SGD | +16.8% | +14.7% | +20.6% | +24.7% | **+19%** | +32% |
| USD | — | — | — | — | **±1%** (peg band 7.75–7.85) | +1.4% |

- The handout's blanket ±10% is right for GBP but **understates CAD by a third and SGD by half**.
- SGD is the riskiest of the three for an HKD payer. It has drifted up about 1% a year against HKD for 20 years,
  consistent with the MAS policy of gradual appreciation. We treat that drift as a risk, captured in the stress case,
  not as a base-case forecast.

Annualised volatility (10 years) supports the same ranking: GBP 8.6%, CAD 6.6%, SGD 4.4%. Volatility alone understates
SGD because it misses the drift. That is why the stress case uses the distribution of moves, not volatility.

### 3c. Implementation rule: this is where the FX analysis becomes a recommendation
Holding the education money in the foreign currency *before* the destination is known has a cost: you give up the HKD
interest rate for the foreign one.

| If the money is held early in | Yield given up vs HKD (12M HIBOR 3.91%) |
|---|---|
| GBP (Bank Rate 3.75%) | **0.2pp a year**, almost nothing |
| CAD (BoC 2.25%) | 1.7pp a year |
| SGD (SORA ~1.1%) | 2.8pp a year |

**Recommendation:**
1. Hold the education fund in HKD deposits and short bonds until offers are confirmed (about early 2028).
2. Size a currency buffer equal to the stress percentage above multiplied by the destination's year-1 and year-2 costs.
3. Once the destination is known, convert or hedge the first two years.
4. If the UK looks most likely, pre-converting part of the fund to GBP costs almost nothing, so it can start earlier.

### 3d. Check on the case's overseas cost band

| Destination | Typical total a year (local currency) | ≈ HK$ a year at spot |
|---|---|---|
| UK | £29K–48K | 304K–503K |
| Canada | CAD 30K–60K | 168K–335K |
| Singapore | SGD 25K–55K | 154K–338K |

The case's HK$350–600K band describes the UK. For Canada and Singapore, **keep the case band as the planning
budget** (it is the client's estimate) and present the surplus as contingency headroom that covers the FX stress.

---

## 4. For context: general CPI (the anchor the other three rest on)
**2.5% base, 3.5% stress.**
- Base: HK CPI averaged **2.52% over 2006–2025** (World Bank). The government forecasts 2.6% for 2026. Under the peg,
  HK imports US inflation (Fed target 2%) plus a structural premium from housing and services.
- Stress: the Fed's own 2026 PCE projection is 3.7%, the reason for the September hike. 3.5% is therefore a live
  scenario, not a tail event.

---

## Summary for the assumption table

| Assumption | Base | Stress | One-line justification for the proposal |
|---|---|---|---|
| Medical trend | 10% in 2027, grading to 6% by 2036 | 8.54% flat | Actuarial (SOA Getzen) three-stage method on WTW/MMB 2026 data and HK Domestic Health Accounts |
| Medical ageing | VHIS Flexi median age curve (~4.7% a year, 65→80) | same | Health Bureau VHIS standard-premium dataset |
| Cash / deposits | 3.0% in 2027–28, grading to 2.5% by 2031 | 0.5% from 2029 | HIBOR forward curve; Fed longer-run 3.2%; HK real money-market rate 1994–2025 |
| Idle savings balances | 0.2% | 0.2% | HK savings rate 2025 (World Bank) |
| FX base | Spot, 22 Sep 2026 (ECB) | — | Random-walk evidence (Meese–Rogoff) |
| FX stress (foreign currency up) | — | GBP +10% · CAD +14% · SGD +19% | 95th percentile of 2–5y moves, 2006–2026 |
| General CPI | 2.5% | 3.5% | HK 2006–25 average; Fed 2026 PCE projection |

## Data sources
- WTW Global Medical Trends (HK series 2020–2026): https://www.wtwco.com/en-hk/insights/2025/12/asia-pacific-medical-inflation-continues-to-soar-in-2026
- Mercer Marsh Benefits Health Trends 2026: https://www.marsh.com/hk/en/services/employee-health-benefits/insights/health-trends-report.html
- Aon 2026 Global Medical Trend Rates, APAC: https://www.aon.com/apac/insights/blog/default/2026-medical-trend-rates-insights-asia-pacific
- SOA Getzen Model: https://www.soa.org/resources/research-reports/2025/2026-getzen-model-update/
- HK Domestic Health Accounts 2023/24: https://www.info.gov.hk/gia/general/202510/16/P2025101500854.htm · 1989/90–2013/14: https://www.healthbureau.gov.hk/statistics/download/dha/en/dha_summary_report_1314.pdf
- VHIS standard premiums (Health Bureau): https://data.gov.hk/en-data/dataset/hk-hhb-hhbvhis-vhis-standard-premium
- World Bank API, HK indicators (CPI, deposit rate, GDP per capita, population): https://api.worldbank.org/v2/country/HKG/indicator/
- IMF IFS HK money-market rate, via DBnomics: https://db.nomics.world/IMF/IFS/M.HK.FIMM_PA
- HKAB HIBOR fixings: https://www.hkab.org.hk/en/rates/hibor
- Fed Summary of Economic Projections, 16 Sep 2026: https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260916.htm
- ECB reference rates via Frankfurter API: https://api.frankfurter.dev/
- Bank of England, Sep 2026: https://www.bankofengland.co.uk/monetary-policy-summary-and-minutes/2026/september-2026
- Bank of Canada, 2 Sep 2026: https://www.bankofcanada.ca/2026/09/fad-press-release-2026-09-02/
- Meese, R. & Rogoff, K. (1983), "Empirical exchange rate models of the seventies", *Journal of International Economics* 14.
