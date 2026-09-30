> **Source material only (30 Sep 2026).** The proposal text now lives in `document/manuscript.md`, with model
> numbers filled from `figures/numbers.json`. Decisions since this draft: annuities single life (Adrian 2037, Carmen 2039); mortgage cleared in 2037; critical illness HK$1.5M each; ESG base
> HK$10.47M; Carmen's portfolio 60% equity. Edit the manuscript, not this file.

# §10 Implementation Roadmap · §11 Risk and Compliance — draft

> **Notes for Lookbua (delete before layout).** 1.25 pages for both. §11 merges your risk register with Win's
> regulatory matrix (`Updated_Investment_Win.md` §4): codes F (financial), P (protection), B (behavioural),
> R (regulatory), E (ethical/compliance). Impacts come from `run_model.py` §7 and `figures/sensitivity-tornado.png`;
> Figure 16 (the matrix) still needs drawing. Owners in the roadmap are the family's, not ours.

---

## 10. IMPLEMENTATION ROADMAP

**Twelve actions in twelve months, then reviews that are triggered by events, not by the calendar.**

| When | Action | Owner | Cost / effect |
|---|---|---|---|
| **Month 1** | Mirror wills, guardian for Chloe, EPAs, advance directives; check title and policy beneficiaries | Adrian, Carmen + solicitor | < HK$25K once |
| Month 1 | Joint account with 12 months' spending; move idle savings to deposits and a money-market fund | Adrian, Carmen | +HK$14K a year |
| Months 1–3 | Disability, term life, CI and individual VHIS for both parents; Ryan's starter cover | Family + adviser | ≈HK$135K a year |
| Months 1–3 | Shareholders' and buy-sell agreement; key-person cover | Carmen + co-founder | paid by the company |
| Months 1–6 | Restructure into the three portfolios in 3–4 tranches; sign the family IPS | Family + adviser | fees ≈HK$59K a year lower |
| Month 6 | First annual family meeting; Ryan's savings and digital-asset policy agreed | All four | — |
| **Early 2028** | Chloe accepts an offer: convert years 1–2 of fees that month | Adrian, Carmen | FX risk on years 1–2 removed |
| 2028–2031 | Years 3–4 converted 12 months ahead; shortfalls paid from surplus | Adrian, Carmen | ≤HK$90K a year at stress |
| **2034–2036** | Adrian de-risks to 35% equity; business managers in place; decide the CI renewal | Adrian, Carmen | — |
| **2037** | Adrian retires: annuitise the MPF; choose reverse mortgage or downsizing | Adrian, Carmen | 62% → 85% security |
| 2039 | Carmen retires; staged business sale completes | Carmen | +19 points |
| **Age 75, or a major diagnosis** | Review the medical tier (Flexi or Standard) | Carmen, Adrian | +13 points (85% → 98%) |

**Triggers for a full review:** a death, a disability, a business sale, a 20% equity fall, or interest rates
moving more than 1.5 points.

## 11. RISK AND COMPLIANCE

**The largest risks to this plan are inflation and medical costs, and the family controls the best defence
against both: what they spend.** Figure 16 places each risk by likelihood and impact; the impact is the change in
the chance the money lasts to Carmen's 89, from 85% under the full plan (Figures 17 and 18).

| Code | Risk | Impact (model) | Mitigation |
|---|---|---|---|
| **F1** | Inflation 3.5% instead of 2.5% | 85% → **52%** | Spending guardrails (cut discretionary spending after bad years); shorten bonds when CPI > 3.5% (rule M7); CPI-linked Silver Bonds from 60 |
| **F2** | Medical costs rise 8.5% a year, not 10% → 6% | 85% → **60%** | Review the medical tier at 75: switching to Standard adds 13 points; CI lump sum for self-financed treatment |
| **F3** | A low-return decade (equities 4%, bonds 2.5%) | 85% → **35%** | Guardrails; the 2037–41 Treasury ladder funds the first five retirement years regardless of markets |
| **F4** | The business cannot be sold | 85% → **70%** | Buy-sell agreement now; managers in place by 55–58; the sale treated as a buffer, not a certainty |
| **F5** | Both parents live to 95 | 85% → **64%** | Annuity pays for life; reverse mortgage pays for life; downsizing kept in reserve |
| **P1** | Disability of either parent before retirement | Highest-ranked risk in the register | Disability income cover (§8) |
| **B1** | Four members, four risk appetites | Arguments at the worst moment | One portfolio per person; rules agreed in advance in the family IPS |
| **B2** | Selling in a crash, or letting the mix drift | Never rebalancing: 85% → **82%** | 5-point rebalancing bands (as good as yearly rebalancing in our test) |
| **R1** | Virtual-asset rules or a platform licence change | Ryan's portfolio | Regulated platforms and HKEX spot ETFs only; switch within 30 days (rule D5) |
| **R2** | Greenwashing; ESG fund downgraded | Carmen's values, not returns | Two-rating rule; holdings check; replace within 3 months |
| **E1** | Joint clients with different interests | Suitability | Recommendations kept symmetric; each spouse may take separate legal advice; risk profile set at the lowest of tolerance, capacity and need |
| **E2** | Model risk | Overconfidence | Normal returns understate market crashes; the model does not let spending adjust, which *understates* success under guardrails. Results used to compare decisions, not as forecasts |

**Compliance.** Every product named is SFC-authorised or HKMC-issued; insurance figures are published rates, to
be replaced by quotes; assumptions are stated in the Appendix. We earn no commission on any recommendation.
