# Assumption Methodology: Medical Inflation, Cash Return, FX

**For:** Fahtai (model inputs), Win (cash and FX in the allocation), Lookbua (stress cases), and the proposal's
assumptions appendix.
**Data date:** 22–23 September 2026; education costs and foreign-currency deposit rates added 29 September 2026.
Raw data and sources are in [macro-snapshot-2026-09-23.md](macro-snapshot-2026-09-23.md). Changes since the first
version are listed at the end.

**Principle.** None of these three numbers is picked by vote. Each is built the way an institutional wealth manager
builds capital-market assumptions:
1. Start from what the market or current data says **now**.
2. Anchor the **long run** in an economic relationship that has held historically.
3. **Grade** between the two over a stated period.
4. Set the stress case from **historical experience**: a percentile where the data allow it (FX), otherwise a regime
   that actually happened (medical, cash). Never a round number.

Every figure below can be traced to a dataset or a formula.

**Where the effort goes.** For the Wongs, the assumptions that change decisions are medical costs in late retirement,
longevity, investment returns and the value of Carmen's business. The cash-rate path and FX barely move the retirement
result. In the proposal, give medical costs the space and keep cash and FX to a few lines.

**Precision.** The model keeps full precision. The proposal shows rounded figures (for example "10% grading to 6%",
"stress 8.5%") so the reader doesn't take a two-decimal number as a forecast.

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
| **Near term (2027)** | **10.0%** | 2026 HK projections from the two largest insurer/broker surveys: WTW 9.9%, Mercer Marsh Benefits 10.5%. Their average is 10.2%, rounded down to 10.0%. Aon puts HK below the 11.3% APAC average. |
| **Long run (2036 onward)** | **6.0%** | = nominal GDP-per-capita growth **4.0%** + excess cost growth **2.0pp**, derived below |
| **Grade-down** | linear, 2027 → 2036 | −0.44pp a year, reaching 6% after nine steps. A grade of about ten years is common in actuarial practice |

**Long-run components:**
- *Nominal GDP per capita growth, 4.0%.*
  - HK history (World Bank): 3.0% a year over 1995–2025, 3.9% over 2005–2025.
  - Forward view: real GDP growth 2.7% less population growth 0.7% gives about 2.0% real per capita; add 2.5% CPI for about 4.5%.
  - 4.0% sits between the historical and forward figures.
- *Excess cost growth, 2.0pp.*
  - HK *total* health expenditure rose from **3.6% of GDP (1989/90) to 5.7% (2013/14)**, about 1.9pp a year faster than GDP (Domestic Health Accounts).
  - *Current* health expenditure reached **8.3% of GDP in 2023/24**. Current expenditure excludes capital spending, so it runs below the total. Measured against the 1989/90 total, it implies about 2.5pp a year over 34 years, which if anything understates the true rise.
  - The Getzen model assumes excess growth fades towards ~1pp as the health share rises. HK's share is still low by developed-market standards, so we use 2.0pp, at the lower end of HK's own history.
  - **A deliberate margin.** Part of HK's historical excess comes from population ageing (more older people in the population), and §1c adds ageing again for each person. So 2.0pp counts some ageing twice. We keep it on purpose: for a cost assumption, a margin protects the client. A figure without the overlap would be lower; we have not estimated it precisely.

**Resulting path (use these rows in the model):**

| 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | 2036+ |
|---|---|---|---|---|---|---|---|---|---|
| 10.00% | 9.56% | 9.11% | 8.67% | 8.22% | 7.78% | 7.33% | 6.89% | 6.44% | 6.00% |

30-year average (2027–2056): **6.67%** (6.66% compounded). A flat 7% would be close on average but wrong in shape: it
understates the next five years and overstates the long run.

**Stress case: 8.5% every year (8.54% in the model), no grade-down.** This is the mean of WTW's HK trend over 2020–2026
(6.2, 9.8, 6.9, 8.8, 8.4, 9.8, 9.9). It asks what happens if the last seven years persist for another thirty.
- *Check (Win):* confirm the seven WTW figures are all the same type, either all projected or all actual.
- *Timing:* because the base starts at 10%, the stress is **milder than the base until about 2034** (cumulative
  1.77× vs 1.79× by 2033). It overtakes the base from about 2034 and is 1.7× the base by 2056. Premiums before
  retirement sit inside today's HK$82K a month, and the separate premium line starts around 2037, so the stress
  applies where it matters.

### 1c. Ageing is a separate factor. This is the step most plans miss
A medical-trend survey measures cost growth **for a person of the same age**. An individual's premium also rises
because they get older. The two effects multiply, and a model that uses only the trend understates retirement
medical costs badly.

The age curve comes from the government's own data: the **VHIS standard-premium dataset** (Health Bureau, data.gov.hk,
tables effective 2025–26). It covers 424 Flexi plans and 33 Standard plans, standalone, non-smoker.

| Age | Flexi median, male | Flexi median, female | Standard median, male | Ratio to age 65 (Flexi, male) |
|---|---|---|---|---|
| 55 | 17,140 | 18,186 | 6,119 | 0.53 |
| 60 | 23,050 | 23,210 | 7,887 | 0.71 |
| 62 | 26,578 | 25,895 | 8,765 | 0.82 |
| 65 | 32,542 | 31,599 | 10,452 | 1.00 |
| 70 | 42,122 | 40,990 | 13,008 | 1.29 |
| 75 | 53,887 | 53,228 | 16,184 | 1.66 |
| 80 | 63,644 | 62,772 | 18,920 | 1.96 |

Premiums in HK$ a year at the dataset's prices.
- **Age-only escalation from 65 to 80 is 4.6% a year for Flexi (male; 4.7% female) and 4.0% for Standard.**
- The tables stop at age 80–81. Beyond 80, extrapolate the 75→80 slope, which is **3.4% a year**.
- **Use the Flexi median.** It is the realistic tier for a household with HK$24M of net worth; the Standard plan is the floor.
- **Check before use (Fahtai):** the tables are labelled 2025–26, but the trend below starts in 2027, so 2026 is
  skipped. Search results point to a VHIS summary dated 17 Jul 2026 on vhis.gov.hk (not yet confirmed). If a 2026–27
  table exists, use it; if not, add one year of trend (about +10%). The figures in this section do not yet include
  that adjustment.

**Model formula:** premium(person, year) = VHIS_Flexi_median(age in that year) × ∏(1 + medical trend) from 2027 to that year.

**What it produces (nominal HK$ per person a year, base case):**

| | 2037 | 2042 | 2047 | 2052 | Final year of life expectancy |
|---|---|---|---|---|---|
| Adrian (age 65 / 70 / 75 / 80 / **84**) | 74K | 129K | 221K | 349K | **503K** in 2056 (≈ 240K in today's money) |
| Carmen (age 60 / 65 / 70 / 75 / **89**) | 53K | 97K | 168K | 292K | **1,049K** in 2066 (≈ 390K in today's money) |

"Today's money" deflates at the 2.5% CPI base. A flat HK$40–60K per person grown at 7% would overstate costs early in
retirement (84–126K in 2037, against 53–74K here) and understate them late (304–457K by 2056, against 503K for Adrian
here). Understating late costs is the dangerous direction for longevity planning.

**How this line relates to the HK$780K.** The case puts premiums inside today's HK$82K a month, and the HK$780K excludes
only "extraordinary" medical costs, so routine premiums could be read as already inside it. We model them as a
**separate line** instead. Today both parents are on employer group cover, so the family's HK$780K estimate almost
certainly doesn't price the move to individual cover at retirement, and that is the cost that grows fastest. This is
the conservative reading; the proposal should say so in one sentence.
- *Data gap:* confirm what premiums the parents pay today. It may be existing individual or top-up cover, which would
  change the advice in §1d.

**Scope:** this covers insurance premiums only. Deductibles, co-payments and uncovered treatment are the
"extraordinary medical costs" the case excludes from the HK$780K. Cover them with the critical-illness cover and a
medical reserve inside the retirement liquidity bucket, not with this line.

### 1d. What the family can do about it. This is the advice, not just the assumption
On the base case, by Carmen's 89th birthday her premium alone is about HK$1.05M a year, **about HK$390K in today's
money, half her HK$780K budget**. The proposal should show this number and then the levers:

1. **Both parents buy individual cover now, not at retirement.**
   - Adrian (54) is older and closer to the age where underwriting brings exclusions or refusal. Waiting until 64
     (Adrian) or 61 (Carmen) is the real risk, more than the premium.
   - VHIS certified plans guarantee renewal to age 100, so cover bought now can't be withdrawn later because of claims.
   - To keep the cost of overlapping with group cover low, consider a Flexi plan with a deductible roughly equal to
     what the group plan pays. Ask for plans that let the deductible be reduced at retirement without new underwriting.
   - Premiums are tax-deductible up to HK$8,000 per insured person.
2. **Step down later if needed.** At every age in the table, the Standard plan costs about 30% of the Flexi median.
   At Carmen's 89 that is roughly HK$0.3M a year instead of HK$1.05M, nominal. Moving down a tier is generally
   simpler than moving up, which needs underwriting (confirm the terms of the chosen plan).
3. **The public system is the floor.** Since 1 Jan 2026, public hospital fees have been capped at HK$10,000 a year
   per patient, with general wards at HK$200–300 a day. Self-financed items, such as many new cancer drugs, sit
   outside the cap; that is what critical-illness cover and the medical reserve are for.
4. **Review rule for the family IPS:** at age 75, and after any major diagnosis, decide whether the Flexi tier still
   earns its cost, given health and the portfolio at that point.

---

## 2. Cash and deposit return: forward curve, then a neutral-rate anchor

### 2a. Why not just use today's deposit rate
A 30-year plan needs the average cash return across rate cycles, not this month's promotional rate. Using 3.05% for
30 years would overstate returns. Using 2.5% flat would ignore that money deposited today locks in about 3%.

### 2b. The build

| Stage | Value | How it is derived |
|---|---|---|
| **2027–2028** | **3.0%** | Lockable today for 12 months: best 12-month HKD time deposit is 3.05%. The HIBOR curve is upward-sloping (1M 2.89%, 12M 3.91%); the implied 6-month rate in six months is **4.27%** (this needs the 6M HIBOR fixing, which is not yet in the snapshot). The Fed's Sep 2026 projections put policy rates in the low 4s through 2027, so 3.0% for 2028 is conservative. |
| **Long run (2031 onward)** | **2.5%** | Average of two independent anchors (below) |
| **Grade** | 2029: 2.83% · 2030: 2.67% · 2031+: 2.50% | Linear. By about 2030 the Fed's projections converge on their longer-run rate |

**Long-run anchors.** Both take off an executable spread of −0.5pp: the gap between interbank rates and what a depositor
or money-market-fund holder actually earns after bank margin and fund fees. The spread observed today is −0.2 to −0.9pp.
1. *Forward-looking:* the Fed's longer-run neutral rate is **3.2%** (Sep 2026 median). The HKD peg imports US monetary
   policy, so HKD neutral ≈ USD neutral: 3.2% − 0.5 = **2.7%**.
2. *Historical:* HK money-market rates averaged **+0.2% real** over 1994–2025 (IMF IFS, World Bank CPI).
   2.5% CPI + 0.2% − 0.5 = **2.2%**.

Mean of the two = **2.45%, which rounds to 2.5%**.

**Stress case: 0.5% from 2029 onward**, about −2% real at the 2.5% CPI base. This is a return to the 2009–2021 regime,
when HK money-market rates averaged **0.36%** and the real return on cash was **−2.3% a year**. That happened within
the last 15 years, so it is a real scenario, not a tail event.
- **Run it with CPI at base, not with the 3.5% CPI stress.** Under the peg, low HKD rates come with low US rates, which
  rarely coexist with high inflation. Combined, the two would give −3% real, worse than anything since 2009. See §5.

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

- A blanket ±10% is right for GBP but **understates CAD by a third and SGD by half**.
- SGD is the riskiest of the three for an HKD payer. It has drifted up about 1% a year against HKD for 20 years,
  consistent with the MAS policy of gradual appreciation. We treat that drift as a risk, captured in the stress case,
  not as a base-case forecast.
- **Caveat: small sample.** Twenty years of overlapping windows contain only about four independent 5-year periods,
  and each currency's tail is dominated by one episode (for SGD, 2006–11). The irregular GBP pattern (the 3-year figure
  is below the 2- and 4-year ones) is a symptom. Read the stress figures as accurate to within a few points.

Annualised volatility (10 years) supports the same ranking: GBP 8.6%, CAD 6.6%, SGD 4.4%. Volatility alone understates
SGD because it misses the drift. That is why the stress case uses the distribution of moves, not volatility.

### 3c. Implementation rule: this is where the FX analysis becomes a recommendation
Holding the education money in the foreign currency *before* the destination is known has a cost: you give up the HKD
deposit rate for a lower foreign one. The fair comparison is 12-month deposits an HK resident can actually open.
UK and Canadian savings accounts paying more (UK 1-year bonds up to ~5%, Canadian 1-year GICs up to ~3.65%) generally
require local residency, so they are not available to the family until Chloe is enrolled.

| Held early in | Policy rate | 12-month deposit available to an HK resident (indicative) | Yield given up vs best HKD 12-month deposit (3.05%) |
|---|---|---|---|
| GBP | 3.75% | ~2.5% (HSBC HK, Jun 2026, top balance tier) | **≈ 0.5pp a year** |
| CAD | 2.25% | ~1.0% (HSBC HK, Jun 2026) | ≈ 2pp a year |
| SGD | SORA ~1.1% | ~1.8% best in Singapore itself; HK-bank quotes lower or unavailable | ≥ 1.3pp a year, likely ~2pp |

The HK-bank rates are board rates from June for large balances; smaller balances earn less. Get quotes from the
family's own bank before acting. The ranking is robust: GBP is cheap to hold early, CAD and SGD are not.

**Recommendation:**
1. Hold the education fund in HKD deposits and short bonds until offers are confirmed (about early 2028).
2. Size a currency buffer equal to the stress percentage above multiplied by the destination's year-1 and year-2 costs.
   At the top of each band in 2028/29 prices: **UK ≈ HK$115K, Canada ≈ HK$160K, Singapore (no grant) ≈ HK$155K.**
3. Once the destination is known, convert or hedge the first two years.
4. **Years 3–4: convert each year about 12 months before it is due.** The remaining risk at stress is about
   HK$60–90K a year, paid from the family's surplus (≈ HK$718K a year, with both parents still working in
   2030–32). Converting all four years at acceptance is not recommended: it adds carry cost and leaves money in the
   wrong currency if Chloe transfers or leaves.
5. If the UK is clearly the favourite before offers arrive, pre-converting part of the fund to GBP costs about 0.5pp a
   year, so it can start earlier. Not worth it for CAD or SGD.

### 3d. Check on the case's overseas cost band

| Destination | Typical total a year (local currency) | ≈ HK$ a year at spot, today's prices | ≈ HK$ in 2028/29 (5% a year) |
|---|---|---|---|
| UK | £29K–48K | 304K–503K | 335K–555K |
| Canada | CAD 65K–90K | 363K–503K | 400K–554K |
| Singapore, with MOE Tuition Grant | SGD 33K–40K | 203K–246K | 224K–271K |
| Singapore, without the grant | SGD 49K–59K | 301K–363K | 332K–400K |

How the local-currency ranges are built:
- **UK:** tuition £15K–30K plus living £14K–18K (Save the Student).
- **Canada:** tuition CAD 42K–67K, from the national average for international undergraduates (CAD 41,746 in
  2025/26, Statistics Canada) to UBC Sauder's Bachelor of Commerce (CAD 66,679 for year 1, 2026/27). Add living costs
  of CAD 23,448, the IRCC study-permit minimum from 1 Sep 2026.
- **Singapore:** NTU business tuition is about SGD 21–22K a year with the Tuition Grant (2026 intake) and about
  SGD 36–41K without it (secondary source). Living costs of SGD 12–18K are an estimate and not yet verified.

**Whether the case band has headroom depends on how it is read.** The case calls it "estimated future costs" but gives
no year.
- **Read as 2028/29 prices:** the HK$350–600K band **matches the UK and Canada, with no headroom**. The FX buffer in
  §3c is real money on top. Four years at the top ≈ HK$2.4M.
- **Read as today's prices and escalated at 5% (what the model does):** the top of the band is ≈ HK$661K in 2028/29.
  That covers the UK and Canada *including* their FX stress (555K × 1.10–1.14 ≈ 610–633K), so the buffer sits inside
  the budget and only needs earmarking. Four years ≈ HK$2.85M.

**Use the second reading.** It is the conservative one, it matches the model, and the family's HK$718K yearly surplus
carries the extra cost easily. State it in one line in the proposal. Singapore sits well below the band on either
reading. With the Tuition Grant it costs about half, but the grant requires three years' work in Singapore after
graduating, which is a career decision for Chloe, not only a cost one. **Keep the case band as the planning budget**
(it is the client's estimate).

---

## 4. For context: general CPI (the anchor the other three rest on)
**2.5% base, 3.5% stress.**
- Base: HK CPI averaged **2.52% over 2006–2025** (World Bank). The government forecasts 2.6% for 2026. Under the peg,
  HK imports US inflation (Fed target 2%) plus a structural premium from housing and services.
- Stress: the Fed's own 2026 PCE projection is 3.7%, the reason for the September hike. 3.5% is therefore a live
  scenario, not a tail event.

---

## 5. Run the stress cases as coherent scenarios, not one at a time

Stacking every stress at once produces a world that can't exist under the peg (for example near-zero HKD rates with
3.5% inflation). Stressing one input at a time understates how bad a real bad decade is. Run a few internally
consistent scenarios instead. The other assumption figures come from the lock table in
[working-brief.md](working-brief.md) §4.

| Scenario | What happens | Inputs |
|---|---|---|
| **A. Low-rate decade** (2009–21 again) | Rates collapse, inflation stays moderate, markets disappoint | Cash 0.5% from 2029 · CPI 2.5% · IG bonds 2.5% · equities 4.0% · medical base |
| **B. Inflation shock** | US inflation persists; the peg pushes HKD rates up | CPI 3.5% · medical 8.5% flat · cash at base or higher · mortgage 5.0% (Prime) · property −15% |
| **C. Long life, high medical costs** | Both parents live longer, and medical costs keep rising | Both to 95 · medical 8.5% flat · everything else at base |

FX stress applies only to the education module, in every scenario. Report each scenario's retirement success rate and
the age at which the portfolio would run out, next to the base case.

---

## Summary for the assumption table

| Assumption | Base | Stress | One-line justification for the proposal |
|---|---|---|---|
| Medical trend | 10% in 2027, grading to 6% by 2036 | 8.5% flat | Actuarial (SOA Getzen) three-stage method on WTW/MMB 2026 data and HK Domestic Health Accounts |
| Medical ageing | VHIS Flexi median age curve (~4.6–4.7% a year, 65→80) | same | Health Bureau VHIS standard-premium dataset |
| Medical premiums | Separate line from the HK$780K (conservative reading) | — | The family's estimate predates the move from group to individual cover |
| Cash / deposits | 3.0% in 2027–28, grading to 2.5% by 2031 | 0.5% from 2029, with CPI at base | HIBOR forward curve; Fed longer-run 3.2%; HK real money-market rate 1994–2025 |
| Idle savings balances | 0.2% | 0.2% | HK savings rate 2025 (World Bank) |
| FX base | Spot, 22 Sep 2026 (ECB) | — | Random-walk evidence (Meese–Rogoff) |
| FX stress (foreign currency up) | — | GBP +10% · CAD +14% · SGD +19% | 95th percentile of 2–5y moves, 2006–2026 |
| Overseas education | Case band HK$350–600K in today's prices, escalated 5% a year | FX stress; fits inside the escalated band for UK and Canada | Local-currency costs at 2028/29 prices (§3d) |
| General CPI | 2.5% | 3.5% | HK 2006–25 average; Fed 2026 PCE projection |

## Data sources
- WTW Global Medical Trends (HK series 2020–2026): https://www.wtwco.com/en-hk/insights/2025/12/asia-pacific-medical-inflation-continues-to-soar-in-2026
- Mercer Marsh Benefits Health Trends 2026: https://www.marsh.com/hk/en/services/employee-health-benefits/insights/health-trends-report.html
- Aon 2026 Global Medical Trend Rates, APAC: https://www.aon.com/apac/insights/blog/default/2026-medical-trend-rates-insights-asia-pacific
- SOA Getzen Model: https://www.soa.org/resources/research-reports/2025/2026-getzen-model-update/
- HK Domestic Health Accounts 2023/24: https://www.info.gov.hk/gia/general/202510/16/P2025101500854.htm · 1989/90–2013/14: https://www.healthbureau.gov.hk/statistics/download/dha/en/dha_summary_report_1314.pdf
- VHIS standard premiums (Health Bureau): https://data.gov.hk/en-data/dataset/hk-hhb-hhbvhis-vhis-standard-premium · VHIS plan lists: https://www.vhis.gov.hk/en/consumer_corner/standard-plan.html
- Hospital Authority fees reform, from 1 Jan 2026: https://www.info.gov.hk/gia/general/202503/25/P2025032500462.htm · https://www.ha.org.hk/ho/corpcomm/fncr/index-en.html
- World Bank API, HK indicators (CPI, deposit rate, GDP per capita, population): https://api.worldbank.org/v2/country/HKG/indicator/
- IMF IFS HK money-market rate, via DBnomics: https://db.nomics.world/IMF/IFS/M.HK.FIMM_PA
- HKAB HIBOR fixings: https://www.hkab.org.hk/en/rates/hibor
- Fed Summary of Economic Projections, 16 Sep 2026: https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260916.htm
- ECB reference rates via Frankfurter API: https://api.frankfurter.dev/
- Bank of England, Sep 2026: https://www.bankofengland.co.uk/monetary-policy-summary-and-minutes/2026/september-2026
- Bank of Canada, 2 Sep 2026: https://www.bankofcanada.ca/2026/09/fad-press-release-2026-09-02/
- HSBC HK foreign-currency time deposits: https://www.hsbc.com.hk/accounts/products/time-deposits/foreign-currency/ · https://www.hsbc.com.hk/investments/market-information/hk/deposit-rate/
- Singapore fixed deposits, Sep 2026: https://growbeansprout.com/insights/savings/singapore-best-fixed-deposit-rate
- UK 1-year bonds, Sep 2026: https://moneyfactscompare.co.uk/savings-accounts/1-year-fixed-rate-bonds/ · Canada GICs: https://www.ratehub.ca/gics/best-gic-rates
- UK student costs: https://www.savethestudent.org/international-students/international-student-fees.html
- Statistics Canada, tuition 2025/26: https://www150.statcan.gc.ca/n1/daily-quotidien/250910/dq250910d-eng.htm
- UBC Sauder BCom fees: https://www.sauder.ubc.ca/programs/bachelors-degrees/bachelor-commerce/admissions-finance/fees-financing
- IRCC study-permit proof of funds from 1 Sep 2026: https://assist.applyboard.com/hc/en-us/articles/48505036826509-Canada-Study-Permit-Proof-of-Funds-2026-New-23-448-Amount-From-September-1
- NTU tuition, 2026 intake: https://www.ntu.edu.sg/admissions/undergraduate/financial-matters/tuition-fees/accepted-programme-offer-in-2026 · without grant (secondary): https://leapscholar.com/blog/ntu-singapore-fees/
- Meese, R. & Rogoff, K. (1983), "Empirical exchange rate models of the seventies", *Journal of International Economics* 14.

## Changes on 29 September 2026
- **Corrections:** near-term medical average (10.2%, rounded to 10%); ratio column in §1c recomputed; Standard-plan
  escalation 4.0% (was 3.9%); Flexi escalation 4.6–4.7%.
- **§3c:** the foreign-currency cost table compared a 12-month HKD rate with overnight policy rates. It is replaced
  with deposits an HK resident can open. The GBP cost is ≈ 0.5pp (was 0.2pp); the recommendation is unchanged.
- **§3d:** the Canada band was too low (CAD 30–60K → 65–90K) and Singapore is now split by Tuition Grant. The UK and
  Canada now sit at the top of the case band. Headroom for FX stress exists only if the band is read as today's prices
  and escalated, as the model does; §3d now says to use that reading and state it.
- **§3c:** added the handling of years 3–4 and buffer sizes.
- **Disclosures added:** the ageing margin in the 2.0pp excess; premiums as a separate line from the HK$780K; the stress
  case is milder than the base until about 2034; the mixed health-spending series; the small FX sample; the VHIS base
  year check; cash stress paired with base CPI.
- **Advice added:** §1d (late-retirement premium, both parents buy cover now, step-down, public-system floor, review
  rule) and §5 (combined scenarios). Comparisons with the earlier handout are reworded so the text can go into the
  proposal as it stands.
