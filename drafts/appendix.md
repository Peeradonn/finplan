> **Source material only (30 Sep 2026).** The proposal text now lives in `document/manuscript.md`, with model
> numbers filled from `figures/numbers.json`. Decisions since this draft: critical illness HK$1.5M each; ESG base
> HK$10.47M; Carmen's portfolio 60% equity. Edit the manuscript, not this file.

# Appendix — draft (Fahtai)

> **Notes for Fahtai (delete before layout).** One page. A1 condenses Pete's lock table (`Pete/working-brief.md` §4)
> and the methodology summary; A2 is the Monte Carlo note you owe; A4 follows the reference report. Check every row
> against the `Inputs` tab before layout — the model is the source of truth. Equity return is your 6%.

---

## APPENDIX

### A1. Key assumptions

| Assumption | Base | Stress | Source |
|---|---|---|---|
| CPI | 2.5% | 3.5% | HK 2006–25 average 2.52%; Fed 2026 PCE projection 3.7% |
| Medical trend | 10% (2027) grading to 6% by 2036 | 8.5% flat | SOA Getzen three-stage method; WTW, Mercer Marsh Benefits 2026 |
| Medical ageing | VHIS Flexi median premium by age | — | Health Bureau VHIS standard-premium data |
| Wage growth | 3% | 0% for 3 years | WTW 2026 salary survey |
| Equities | 6.0% (17% volatility) | 4.0% | Long-run equity premium; conservative choice |
| Treasury ladder / IG bonds | 4.0% | 2.5% | US 5-year Treasury 5.0%, HK 10-year 3.86% |
| Cash | 3.0% (2027–28) grading to 2.5% | 0.5% from 2029 | HIBOR curve; Fed longer-run 3.2% |
| Property | +1.5% a year | −15% once | RVD index history |
| Education (overseas) | HK$600K today, +5% a year | + FX stress | Case; methodology §3 |
| FX | ECB spot, 22 Sep 2026 | GBP +10% · CAD +14% · SGD +19% | 95th percentile of 2–5 year moves, 2006–26 |
| MPF annuity | HK$268K a year, fixed for life | — | HKMC Annuity Plan payout rates |
| Reverse mortgage | HK$230K a year for life, from 2037 | — | HKMC programme; valuation cap |
| New protection premiums | HK$159K a year average, to retirement | — | Published rate cards (§8) |
| Life expectancy | Adrian 84, Carmen 89 | both to 95 | Case |
| Survivor spending | 70% of HK$780K after Adrian's 84 | 100% | Planning convention |

### A2. Model and method

One spreadsheet holds every assumption and projects 2026–2072 year by year: income, 2026/27 salaries tax
(separate assessment reproduced to the dollar: HK$181,770), MPF, spending, education, medical premiums and the
portfolio. A Monte Carlo simulation draws 10,000 sequences of annual equity and bond returns from normal
distributions and records whether the parents' portfolio stays above zero to Carmen's 89 and 95. The protection
register ranks risks by severity × occurrence × detection (failure-mode analysis).

**Limits.** Returns are normal and uncorrelated, which understates crash risk; inflation is fixed within each
scenario; the main results hold spending fixed; the guardrails are modelled separately (§3); the
home and business enter only as the decisions in Figure 6. Results compare decisions; they are not forecasts.

### A3. Main sources

Case study and workshop deck (SRFP&S, 19 Sep 2026) · Inland Revenue Ordinance and Budget 2026/27 · HKMC Annuity
and Reverse Mortgage terms · Health Bureau VHIS data · Hospital Authority fee schedule (1 Jan 2026) · Domestic
Health Accounts 2023/24 · WTW, Mercer Marsh Benefits and Aon medical trend surveys 2026 · SOA Getzen model ·
Federal Reserve SEP (Sep 2026) · HKAB HIBOR · ECB reference rates · Statistics Canada, UBC, IRCC, NTU fee
schedules · Bowtie published rate cards · Berg, Kölbel & Rigobon (2022) · Meese & Rogoff (1983).

### A4. Use of AI tools

AI tools were used to check calculations, draft and edit text, and review the model code. All analysis,
assumptions, recommendations and conclusions are the team's own.
