# Areas 1 and 6: the framework, profiles, mandate, dashboard and governance (research brief for Pete)

**Written:** 4 Nov 2026 by an AI research assistant, with three parallel research agents. Every fact was checked
against a primary page or PDF that was actually fetched, unless it is marked UNVERIFIED or "secondary".
**Limits:** the web-search budget ran out partway through (about 200 searches across all agents). The pages that could
not be reached are listed in §9.
**Tags:**
- **SOURCED:** a named source.
- **ESTIMATED:** our arithmetic, shown.
- **ILLUSTRATIVE:** our assumption.
- **MODEL (exploratory):** the Round One model (`model/run_model.py`), run on 4 Nov with scratch scripts. These numbers
  are **not** in `numbers.json`. They go on no slide until they are added to `export_numbers()` and logged (CLAUDE.md
  "Numbers"; Final_Plan §2).

Source keys [S#] are listed at the end.

---

## 1. Bottom line for Pete

1. **Round One's ESG section is "screening", not "ESG integration", in the industry's own terms.** The CFA Institute,
   GSIA and PRI define ESG integration (Nov 2023 [S11]) as "Ongoing consideration of ESG factors within an investment
   analysis and decision-making process with the aim to improve risk-adjusted returns". What our funds do (exclusions,
   best-in-class) is *screening*. Integration, done properly, is a planning discipline across the whole balance sheet:
   the business, the flat, the MPF and the insurance.
   - **Implication:** the 25% earns *alignment*, not *impact*. Buying listed funds on the secondary market rarely
     passes the additionality test (Brest & Born 2013 [S12]; Kölbel et al. 2020 [S13]).
   - **Where additionality can be claimed:** in Carmen's business and in a funded scholarship.
   - This supports the thesis, and the definitions alone let us say so with authority.

2. **The price of values is measurable, and in Round One it is fees, not expected returns.**
   - **Expected return:** the evidence says it need not cost much. Atz et al. 2023 [S60] find ESG returns roughly
     "on par" on average. Pástor, Stambaugh & Taylor 2022 [S55] say expected green returns are *lower*, and the
     recent outperformance came from climate-concern shocks.
   - **Fees:** Round One's ESG funds cost about **HK$11.9K a year more than plain-index twins** (ESTIMATED; the fees
     are still Win's `[CHECK]`). That is ≈16 to 25bp of the whole pot.
   - **Effect on the plan:** ≈**3.8 to 6.2 points** off the odds the money lasts to Carmen's 89, from 82.6% to
     ≈76 to 79% (MODEL, exploratory).
   - **Comparison:** the green bond fund's fee gap (≈104bp) is about 50 times the greenium (≈2bp; Zerbib 2019 [S14]).
   - **Line for the deck:** "the label's price is the fee, not the greenium".

3. **Hong Kong has no duty to ask about sustainability preferences.** The HKMA's FAQ to its Nov 2023 circular says
   [S23]: "Is it mandatory for RIs to make enquiry about a customer's sustainability preference? It is not a mandatory
   requirement." The SFC Code of Conduct contains no occurrence of "sustainab" (Jan 2026 edition, text search).
   - We borrow the EU's structure (Reg. 2021/1253 [S17]; ESMA 2022 ¶26–29, ¶84 [S18]) as voluntary best practice, and
     say so.
   - The EU evidence shows that box-ticking fails. In a German mystery-shopping study, 46% of recommendations matched
     the client's sustainability preference, against 87% for risk, and 78% of stated preferences were documented
     wrongly (Cauthorn et al. 2024 [S22]). ESMA's 2026 Common Supervisory Action found similar gaps [S19].
   - **Our innovation:** profile by *revealed* preference. Use trade-off cards priced in the family's own currency
     (HK$ a year, and points of odds to 89), and write the answers into the mandate as binding terms.

4. **Resolve Adrian against Carmen with separation plus a cost test, not an average.**
   - **The EU precedent:** ESMA's guidelines for a client that is "a group of two or more natural persons" say to
     "adopt the most prudent approach", and that "an average profile … would unlikely be compliant" (¶65–70 [S18]).
   - **The rule:**
     - shared money (reserve, education, retirement floor) follows Adrian's profile;
     - a sustainability option enters shared money only if it costs ≤5bp a year more than its plain twin;
     - Carmen's values live in her own sleeve, at her own cost, within a tracking-error budget.
   - **Result:** family ESG ≈**21.8%**, still above the case's 20% goal. The family's fee gap falls from ≈HK$11.9K to
     ≈HK$9.4K a year, nearly all of it in Carmen's sleeve (ESTIMATED, §3).

5. **Round One's scholarship was aspirational and uncosted.**
   - **What it costs as promised:** about HK$30K a year, from cash flow, for life. That takes **≈6.9 points** off the
     odds to 89 (82.6% → 75.7%) and ≈HK$1.6M off the median legacy (MODEL, exploratory).
   - **The funded alternative:** a **20-year named fund at an existing s.88 charity**, ≈HK$0.48M given in 2027–28 while
     both salaries are taxed at 17%. Net cost ≈HK$0.40M; ≈2.6 points (→ 80.0%).
   - **Perpetual endowment** (≈HK$1.0–1.5M): only from business-sale proceeds above the HK$3.0M the plan counts.
     Zero cost to the base plan if the sale fetches HK$4.0M (MODEL, exploratory).
   - **The tax clock matters.** Relief exists only while they earn, only for gifts of money, and up to 35% of income
     (IRD guide, June 2023 [S39]).

6. **The dashboard: 12 metrics, the brief's four outcome types, reviewed once a year.**
   - Annual review, with event triggers in between. Frequent evaluation makes loss-averse people take less risk
     (Benartzi & Thaler 1995; Gneezy & Potters 1997).
   - Every number is tagged. Impact sits in a separate ledger; avoided emissions are never netted (WBCSD 2023 [S45]).
   - **Attribution is pre-registered:** a plain-index "twin" is agreed in writing at the start. Each year the gap
     between the actual portfolio and the twin splits into market, tilt, cost and decisions.
   - **Ryan, a data analyst, keeps the dashboard's data; the adviser verifies it.** This is our opinion: it gives the
     next generation a real role (family goals 3 and 8).

7. **What sounds clever but fails with a practitioner judge:**
   - claiming "impact" from listed ESG funds;
   - netting avoided emissions against a footprint;
   - quoting an implied temperature rise as a point estimate (GFANZ 2022 [S46] reports it as a range);
   - a "MiFID-compliant" profile in Hong Kong (not applicable);
   - assuming Carmen is "the green one" because she is a woman (the evidence on gender is mixed [S21]);
   - extrapolating ESG's 2020–21 outperformance;
   - a perpetual endowment that sinks Adrian's retirement;
   - precise Scope 3 numbers for fund holdings (Busch et al. 2022 [S48]: the most inconsistent data).

---

## 2. Definitions: the five kinds of finance and where each sits in the Wongs' plan

| Term | One-line definition (source wording where quoted) | Source | Where it sits for the Wongs |
|---|---|---|---|
| **Green finance: green bond** (use of proceeds) | "any type of bond instrument where the proceeds or an equivalent amount will be exclusively applied to finance or re-finance … eligible Green Projects". Four core components: use of proceeds; project evaluation and selection; management of proceeds; reporting. Recommends a framework and external review | ICMA Green Bond Principles, June 2025 [S1] | **Portfolio:** the green bond fund, each bond checked against the GBP. **Flat:** a green mortgage is the household version (Lookbua). The label covers the proceeds, not the issuer |
| **Green loan** | "any type of loan instruments and/or contingent facilities … where the proceeds … shall be exclusively applied to finance, re-finance or guarantee … eligible Green Projects". "a facility cannot be labelled as green if it includes a green and non-green tranche" | LMA/APLMA/LSTA Green Loan Principles, 26 Mar 2025 [S2] | **Business:** a specific asset (e.g. electric vans, rooftop solar on the warehouse; ILLUSTRATIVE, Fahtai) |
| **Sustainability-linked bond / loan** (KPI-linked pricing) | Characteristics "can vary depending on whether the issuer achieves predefined Sustainability/ESG objectives". Proceeds "for general purposes" (SLB). KPIs "relevant, core and material"; SPTs "ambitious … beyond a 'Business as Usual' trajectory". Margin ratchet "is the most common example" and "may include a neutral bracket" (SLL). Five components: KPIs, SPTs, characteristics, reporting, verification ("a necessary element") | ICMA SLBP, June 2024 [S3]; SLLP, 26 Mar 2025 [S4] | **Business:** refinancing the HK$0.9M term loan. Test whether the ratchet beats the verification cost. On HK$0.9M, each 10bp of ratchet is HK$900 a year (ESTIMATED; ratchet sizes UNVERIFIED), so verification likely costs more than it saves. Candidate refusal (Fahtai) |
| **Transition finance** (decarbonising existing assets) | ICMA's four key elements: "1. The issuer's climate transition strategy and governance; 2. Business model environmental materiality; 3. Climate transition strategy and targets to be 'science-based'; and 4. Implementation transparency." ICMA added a standalone **Climate Transition Bond** label (6 Nov 2025). HK Taxonomy Phase 2A (22 Jan 2026) adds transition elements and an adaptation objective. Prototype wording for a transition activity: one "progressing towards 'green' based on a decarbonisation pathway within a defined timeframe" | ICMA CTF Handbook, Nov 2025 [S5]; CTB Guidelines [S6]; LMA Guide to Transition Loans, 16 Oct 2025 [S7]; HKMA Taxonomy 2A [S8] | **Business:** the credibility test for Carmen's transition plan, and the core of the buyer's due-diligence pack for 2035–39. **Banks:** under HKMA GS-2 (22 Sep 2026 [S10]), banks "should" have transition-planning documentation by 1 Jul 2030, and the HKMA "does not expect AIs to mitigate their risks simply by exiting relationships with high-emitting clients". So her lender will ask for her data |
| **Impact investing** | "Investing with the intention to generate positive, measurable social and/or environmental impact alongside a financial return" (CFA/GSIA/PRI). GSIA adds that it requires "demonstrating the investor contribution". GIIN's own four characteristics: UNVERIFIED (site unreachable) | CFA/GSIA/PRI, Nov 2023 [S11] | **Not in the listed portfolio** (no additionality). The only plausible impact is in Carmen's business. The scholarship is philanthropy, not investment. No private impact fund for Adrian: illiquid and complex. Candidate refusal |
| **Additionality** (investor contribution) | "Investment impact is a particular investor's financial contribution to the social value created by an enterprise": it must increase outcomes "beyond what would otherwise have occurred". Engagement has the clearest evidence; capital allocation partial; indirect effects little | Brest & Born, SSIR 2013 [S12]; Kölbel, Heeb, Paetzold & Busch 2020 [S13] | The test that separates "aligned" (the 25%) from "impact" (the business transition, the funded scholarship) |
| **ESG integration** | "Ongoing consideration of ESG factors within an investment analysis and decision-making process with the aim to improve risk-adjusted returns"; it "does not imply … restrictions on the investment universe". PRI (2018): "systematic and explicit inclusion of material ESG criteria into investment analysis and investment decisions" | CFA/GSIA/PRI 2023 [S11] | **The whole plan:** climate risk in the flat's 2037 exit, the business's customers' Scope 3 demands, the insurance renewals, the scenario. This is the reframe |
| **Screening** (exclusions, best-in-class) | "Applying rules based on defined criteria that determine whether an investment is permissible" | [S11] | What the Round One ESG funds do: exclude thermal coal, controversial weapons and tobacco, and hold best-in-class |
| **Stewardship** | "The use of investor rights and influence to protect and enhance overall long-term value …" | [S11] | Fund voting and engagement records, checked once a year. Carmen as an owner engaging her own suppliers |
| **Thematic investing** | "Selecting assets to access specified trends" | [S11] | Excluded in Round One (no thematic fund). Keep excluded |
| **Greenium** | The lower yield on a green bond than on a comparable conventional bond. ≈−2bp on average (Zerbib 2019); "essentially zero" for US munis (Larcker & Watts 2020) | Zerbib, J. Banking & Finance 98:39–60 [S14]; Larcker & Watts, JAE 69(2–3) [S15] | **A cost to the investor** of ≈0–2bp. Negligible beside a ≈104bp fund-fee gap (ESTIMATED) |
| **Green premium** | Bill Gates's term: the extra cost of the zero-carbon option over the fossil one (a real-economy cost, not a yield). Exact wording UNVERIFIED (gatesnotes.com returned 403) | Gates / Breakthrough Energy | **Business:** e.g. electric van against diesel. Fahtai's abatement curve prices it per tonne |
| **Sustainability preferences** (EU) | "a client's … choice as to whether and, if so, to what extent" (a) a Taxonomy share, (b) an SFDR sustainable-investment share or (c) consideration of principal adverse impacts "shall be integrated into his or her investment" | Reg. (EU) 2021/1253, applies from 2 Aug 2022 [S17] | **Our model for the profile**, used voluntarily. It is not a Hong Kong rule |

**Confusions a judge may probe** (sources as above):

| Claim | The correct position |
|---|---|
| "A green bond means a green company" | The label covers use of proceeds only; the issuer can be a high emitter [S1] |
| "An SLB funds green projects" | Proceeds are for "general purposes"; the incentive is the coupon or margin linked to a KPI [S3][S4] |
| "ESG integration is ethical investing" | Its stated aim is "risk-adjusted returns", with no universe restriction implied [S11] |
| "Owning an ESG fund is impact" | Impact needs intention, measurement and investor contribution [S11][S12] |
| "Transition finance is greenwashing brown firms" | It can fund high emitters if the four elements hold [S5]; the HKMA says don't simply exit them [S10] |
| "The SFC list is an SFC endorsement" | The list is "not … an official recommendation or endorsement" (SFC List of ESG funds page [S26]) |
| "External review certifies impact" | A GBP external review checks alignment with the four components, not outcomes [S1] |
| "Greenium = green premium" | Different things: the first is a bond-price effect, the second a technology cost gap |
| "An ESG rating = a carbon footprint" | Ratings blend E, S and G and disagree (average correlation ≈0.54, Berg, Kölbel & Rigobon 2022 [S47]); a footprint is tonnes per unit (our inference) |

### 2b. Hong Kong policy context (one paragraph each)

**HKMA Sustainable Finance Action Agenda (21 Oct 2024) [S31].**
- Four pillars and eight goals: banking for net zero; investing in a sustainable future; financing net zero; making
  sustainability more inclusive.
- Headline goal: "All banks to strive to achieve net zero in their own operations by 2030 and in their financed
  emissions by 2050".
- The Exchange Fund Investment Portfolio is to reach net zero by 2050.
- Banks are to make transition plans available to the HKMA "tentatively from 2030" on a "comply or explain" basis,
  including a "managed phase-out of financing for carbon-intensive assets".
- **For the Wongs:** Carmen's lender will measure the emissions it finances, and her business is one of them.

**Climate Action Plan 2050 (Oct 2021) [S32].**
- Headline: "strive to achieve carbon neutrality before 2050"; cut carbon emissions by 50% "before 2035 as compared to
  the 2005 level".
- Four strategies: net-zero electricity generation; energy saving and green buildings; green transport; waste
  reduction.
- Electricity: cease using coal for daily electricity generation by 2035.
- Buildings, against 2015 electricity use: commercial −15 to 20% and residential −10 to 15% by 2035, then −30 to 40%
  and −20 to 30%.
- Transport: stop new registration of fuel-propelled and hybrid private cars "in 2035 or earlier".
- Buildings use about 90% of electricity.
- **For the Wongs:** the van fleet, the warehouse, and the flat's running costs and resale.

**HKMA SPM GS-1 "Climate Risk Management" (V.1, 30 Dec 2021) [S33]** and **GS-2 "Transition Planning" (V.1,
22 Sep 2026) [S10].**
- GS-1 sets expectations for banks on governance, strategy, risk management (including climate scenario analysis and
  stress testing) and disclosure "aligned with TCFD".
- It notes climate drivers "may reduce collateral value, borrowers' repayment ability" and asks banks to monitor
  collateral exposed to physical risk.
- GS-2 adds transition plans: documentation by 1 Jul 2030.
- GS-2 also says the HKMA "will not assess an AI's performance … based on its financed emissions alone".
- **Our inference:** flood-exposed or energy-poor collateral could face tighter terms. GS-1 itself does not mandate
  green mortgages.

**HKFRS S1/S2 and the HKEX rules [S34][S35][S36].**
- The HKICPA issued HKFRS S1 and S2 on 12 Dec 2024, effective 1 Aug 2025, "fully aligned" with IFRS S1/S2.
- The Government's Roadmap (Dec 2024): large publicly accountable entities to fully adopt the ISSB Standards "no later
  than 2028".
- HKEX's amended climate requirements (Appendix C2), for financial years from 1 Jan 2025:
  - Scope 1 and 2 mandatory for all issuers;
  - the rest "comply or explain" on the Main Board;
  - Hang Seng Composite LargeCap issuers mandatory from 1 Jan 2026.
- How Scope 3 is treated: UNVERIFIED (not on the page read).
- **For the Wongs:** listed customers of Carmen's packaging will ask her for data (their Scope 3).

**HKEX Core Climate (launched 28 Oct 2022) [S37].** An "international carbon marketplace" to "source, hold, trade,
settle and retire voluntary carbon credits". HKD/RMB settlement: UNVERIFIED. **For the Wongs:** relevant only to
offset claims, which our anti-greenwashing rule should forbid in place of reductions (opinion).

**SFC ESG fund rules and the HKMA's sales rules [S26][S27][S23].**
- The SFC's ESG-funds circular (29 Jun 2021, effective 1 Jan 2022) covers funds that "incorporate ESG factors as their
  key investment focus". ESG names "should not overstate", and funds must be assessed "at least annually".
- The SFC's climate amendments to the Fund Manager Code (20 Aug 2021) cover governance, investment management, risk
  management and disclosure.
- The HKMA's circular "Sale and Distribution of Green and Sustainable Investment Products" (29 Nov 2023, B1/15C
  G16/1C) sets standards for banks selling such products. Asking for a sustainability preference is "not a mandatory
  requirement" (FAQ Q7). A client with no answer is "sustainability-neutral" (Q9).

**Green and Sustainable Finance Grant Scheme [S38].**
- Launched 10 May 2021; extended in the 2024-25 Budget "by three years to 2027" and widened to transition bonds and
  loans. The current guideline is effective 24 Apr 2026.
- Track II covers external review costs up to HK$800K per issue (75% if Taxonomy-aligned, else 50%), but **a loan
  tranche must exceed HK$100M**.
- **For the Wongs:** irrelevant to a HK$0.9M loan, which is itself a point worth making. Fahtai confirms from the
  guideline.

---

## 3. Profiles and the mandate

### 3a. Profiles

**Where the entries come from.**
- **"Case":** the case says so.
- **ILLUSTRATIVE:** our reading of the case.
- **To ask:** settled in the profiling session (§5).

**How each profile is taken.**
- Following ESMA ¶81 [S18]: first the financial profile, then the sustainability profile, never the reverse.
- ESMA ¶26 and ¶22 add that preferences are asked in a "neutral and unbiased" way.

| Dimension | **Adrian (54)** | **Carmen (49)** | **Ryan (24)** | **Chloe (16)** |
|---|---|---|---|---|
| Risk profile | Low to Medium (case) | Medium to High (case) | High (case) | — (minor) |
| Values intensity | Low to moderate (ILLUSTRATIVE: the case gives him no ESG view, only "capital preservation, retirement adequacy and healthcare protection") | High (case: "her personal values and her belief in the long-term economic opportunities") | Unknown (case silent): ask, don't assume | Unknown; design interest (case) |
| Motive, on 2DII's return / values / impact goals [S21] | Return (ILLUSTRATIVE) | Values + return, *and she expects ESG to pay*: record that expectation (Giglio et al. 2025 [S58]: holdings follow beliefs about ESG returns) | To ask | Values (philanthropy only) |
| Return requirement | The household plan needs ≈2% real on the retirement pot (manuscript §3) | Same household requirement; her sleeve may run more equity | Growth; saves 30% (Round One) | Education money must be safe (2028–32) |
| Liquidity | High: retirement 2037; Treasury ladder 2037–41; 12-month reserve | Low today: ≈HK$5.0M sits in an illiquid business until the 2035–39 sale | Three months' spending in cash (his tokenised MMF counts) | All education money in deposits and short bonds |
| Horizon | 2037 retirement; joint money to 2066 | To 2066 (her 89) | 40+ years | 2028–32 for her fund |
| Tracking-error tolerance vs policy benchmark | ≤1% a year (ILLUSTRATIVE) | ≤3% a year in her sleeve (ILLUSTRATIVE) | High | None |
| Illiquidity tolerance | None: daily dealing only | Low *in the portfolio*: the business is already her concentrated, illiquid sustainability bet | Moderate | None |
| Complexity tolerance | Low: index funds, Treasuries, annuities | Moderate | High; overconfidence risk (Barber & Odean 2000, 2001) | — |
| Decision rights (charter) | Shared money jointly with Carmen; his own sleeve alone | Shared money jointly; her sleeve alone; the business with her co-founder | His own money only; advisory voice on family matters; keeps the dashboard data | Advisory voice on the scholarship's criteria |

### 3b. What each will and won't accept

- **Adrian will accept:** exclusions and ESG index funds that cost about the same as the plain fund (≤5bp more) and
  carry the same risk; green deposits at the same rate as ordinary deposits (a costless label, never counted as
  impact).
- **Adrian won't accept:** a lower expected return, thematic funds, lock-ups, private impact funds, crypto, or an
  ESG choice that lowers the odds to 89.
- **Carmen will accept:**
  - ESG index tilts and ICMA-checked green bonds in her sleeve, paying the fee gap herself;
  - transition investment in her own business, judged on business returns;
  - a funded scholarship.
- **Carmen won't accept:** "greenwashing" (case concern), offsets in place of reductions, and fossil-expansion
  exposure.
- **Carmen, to test:** whether she pays the fee gap once she sees it in HK$ and points.
- **Ryan will accept:** his own growth plan; tokenised green products when retail-accessible (Round One watch-list).
- **Ryan won't accept:** for others to decide his own money (opinion; consistent with Round One).
- **Chloe:** no investment decisions; a voice in the scholarship's criteria, never a beneficiary (IRD: beneficiaries
  can't be defined by "family relationship" [S39] ¶11).

### 3c. How disagreement is resolved (four rules, recorded in the charter and the investment policy)

1. **Separate the money.** Shared money (reserve, Chloe's fund, Adrian's ladder, the annuities, the insurance) follows
   the more prudent profile.
   - The precedent is ESMA ¶65–70 [S18]: for a group client, "adopt the most prudent approach"; "an average profile …
     would unlikely be compliant". The Swiss Bankers Association guidelines (Art 11(2) [S30]) let a firm collect
     different ESG preferences per portfolio.
   - Mental-account sleeves need not be inefficient in aggregate (Das, Markowitz, Scheid & Statman 2010).
2. **A cost test for shared money.** A sustainability option replaces its plain twin only if its all-in cost (fee plus
   expected tracking drag) is within **5bp a year** and the risk is unchanged.
   - Basis: on the Round One model, each 5bp of whole-portfolio cost ≈ 1.2 points of odds to 89 (MODEL, exploratory:
     5bp → 81.4%, 10bp → 80.2%, from 82.6%).
   - The threshold is ILLUSTRATIVE, for the family to set using the trade-off card.
3. **A values budget for each sleeve.**
   - Carmen's sleeve may spend more on values, within a tracking error of ≤3% a year against its policy benchmark
     (rolling 3 years).
   - Any choice that would take the household below a floor (ILLUSTRATIVE: 80% to Carmen's 89 on the model) needs
     both parents' signatures.
   - No published source prescribes such a budget; it is our design, and we say so.
4. **A default and a record.**
   - If the parents disagree on shared money, the plain twin stays until the next annual meeting (a status-quo
     default, so a dispute never blocks the plan).
   - Every mismatch or change of preference is recorded with reasons. This follows MiFID's Art 54(10) and ESMA ¶84:
     "The decision of the client should be recorded in the mandate."

**What the rules do to Round One's portfolio** (ESTIMATED).
- Fee inputs are Round One's, still `[CHECK: Win]`:
  - BOC-Prudential MSCI World ESG Index Fund ≈0.78%;
  - Allianz Green Bond 1.14%;
  - IWDA ≈0.20%;
  - AGGU ≈0.10% (AGGU is UNVERIFIED).
- **Adrian's sleeve fails the cost test.** His ESG core (35% × HK$2.07M = HK$0.72M) and his green bond fund (5%,
  HK$0.10M) move to the plain twins. That saves ≈HK$5.3K a year in his sleeve.
- **Carmen's sleeve goes all-ESG.** Her 23% plain world fund (HK$0.48M) moves into the ESG core, so her equity is
  ESG-led: 60% × HK$2.07M = HK$1.24M.
- **Family ESG:** HK$1.24M (Carmen's equity) + HK$0.21M (Carmen's green bonds) + HK$0.84M (MPF low-carbon halves) =
  HK$2.28M = **21.8% of HK$10.47M**, still above the case's 20% floor.
  - The MPF fee gap is unknown (Win). Adrian's MPF half needs the same cost test.
- **Family fee gap:** HK$11.9K → ≈HK$9.4K a year, borne by Carmen's sleeve (HK$1.24M × 0.58% + HK$0.21M × 1.04%).
- **The point for the deck:** separate sleeves decide *who pays*; only a cheaper vehicle lowers *what is paid*.
- **Win to test, the label's own price:**
  - Round One counted only SFC-listed ESG funds. If no cheaper SFC-listed global ESG index fund exists, insisting on
    the list costs ≈HK$8.6K a year (1.49M × 0.58%).
  - An Irish UCITS ESG ETF (SFDR Art 8) might hold much the same companies for far less (fee UNVERIFIED).
  - Compare the two on holdings overlap and carbon intensity before deciding.

**The price of values, on four lines** (brief area 1, bullet 4):

| Line | What the family gives up | Evidence | Tag |
|---|---|---|---|
| Expected return | Assumed zero, as in Round One. Theory says green expected returns are lower (Pástor et al. 2022; Bolton & Kacperczyk 2021's carbon premium). The empirical average is roughly on par (Atz et al. 2023) | [S55][S56][S60] | SOURCED (range of views) |
| Fees | ≈HK$11.9K a year at Round One's funds (≈16–25bp of the pot) → ≈3.8–6.2 points to 89 | Fund documents (Win to confirm); model | ESTIMATED + MODEL (exploratory) |
| Tracking error / diversification | Not yet measured: needs the index factsheets (MSCI ESG index vs MSCI World) | MSCI factsheets: not obtained (msci.com runs on JavaScript) | UNVERIFIED (Win) |
| Liquidity | None: all daily-dealing funds | Fund documents | SOURCED (Round One) |

The evidence that the family "need not give up much" is about expected *return*. The cost they can control is the fee,
so the planner's job is to lower that price, not to argue about it.

---

## 4. Draft sustainability annex to the investment policy statement (half a page)

**Annex S to the Wong Family Investment Policy (draft; ILLUSTRATIVE thresholds marked *)**

The structure follows CFA Institute "Elements of an IPS for Individual Investors" (May 2010) [S29], whose §3e says "The
use of ESG or other criteria should be explicitly allowed or disallowed in the IPS". The content follows ESMA 2022
¶26–29, ¶84, ¶88 [S18], CFA Global ESG Disclosure Standards [S28], and HKMA Annex I [S23].

1. **Scope.** Adrian's and Carmen's portfolios and MPF accounts; the shared reserve and education fund. Ryan's plan is
   his own. Effects of business and property decisions are reported on the dashboard, not governed here.
2. **Objectives, in three layers.**
   - (a) **Risk:** consider financially material climate and ESG risk in every holding and decision, with one climate
     scenario a year.
   - (b) **Values:** in Carmen's sleeve, exclusions plus best-in-class.
   - (c) **Impact:** claimed only where investor contribution can be shown. Listed funds are reported as "aligned",
     never as "impact".
3. **Share.** Family ESG ≥20% of investable assets (case goal), target 22–25%.
   - Counted by holding, under the counting rule in item 4.
4. **Counting rule.** A product counts only if three things hold:
   - (a) it publishes its method: index rules, or an ESG disclosure statement covering CFA GESDS 2.A.3, 2.A.8–10 and
     2.A.16–18;
   - (b) it is on the SFC List of ESG funds, or is an equivalent with an SFDR Art 8/9 disclosure (the family's choice:
     to decide);
   - (c) it shows a measured outcome against its parent: weighted average carbon intensity at least 30%* below the
     parent, with data coverage at least 80%*.
5. **Exclusions.** Recorded as characteristic, threshold and exceptions (CFA GESDS 2.A.9–10): thermal coal,
   controversial weapons, tobacco, at the index methodology's thresholds (thresholds UNVERIFIED).
6. **Cost and tracking budgets.**
   - Shared money: all-in cost ≤ plain twin + 5bp*.
   - Carmen's sleeve: tracking error ≤3%* a year (rolling 3 years); fee gap borne by her sleeve.
   - Any choice taking the household below 80%* to 89 needs both parents.
7. **No match.** If no product meets a preference within budget, the plain twin is used and the decision is recorded
   with reasons (ESMA ¶84; MiFID Art 54(10)).
8. **Stewardship.** Funds with a published engagement and voting policy are preferred; voting records are reviewed once
   a year.
9. **Benchmark and attribution.** A plain-index twin, fixed at signing: the same weights, with each ESG fund replaced
   by its parent index fund. It is reported each year (§6b).
10. **Measurement and data.** Each metric is tagged SOURCED, ESTIMATED or ILLUSTRATIVE, with its data-quality score
    (PCAF 1–5 where applicable). Avoided emissions are reported separately and never netted.
11. **Restatement.** If a provider restates a figure, show old and new, say why, and do not restate targets
    retroactively.
12. **Review.** The annual family meeting, plus the triggers in §6. Preferences are re-asked only on a material change
    (ESMA CSA 2026 [S19]).
13. **Signed by** Adrian, Carmen and the adviser. Ryan and Chloe are noted as consulted.
14. **Who may give the advice.** Product advice through SFC-licensed or HKMA-registered intermediaries, and insurance
    through IA licensees (opinion: the planner coordinates).

---

## 5. Behavioural biases: how the plan is presented and reviewed

| Bias | Evidence (verified citation; one-line finding) | How we present and review against it |
|---|---|---|
| **Present bias** | Laibson 1997, QJE 112(2): hyperbolic discounters value illiquid commitment. O'Donoghue & Rabin 1999, AER 89(1): procrastination when costs come now. Thaler & Benartzi 2004, JPE 112(S1): committing *future* raises lifted savings rates from 3.5% to 13.6%. Weber 2006, Climatic Change 77: climate risk is delayed and abstract, so it doesn't trigger worry | **Pre-commit now, pay later:** dated milestones (energy audit 2027, data pack by 2034). The scholarship funded *before* retirement while tax relief exists. Climate risk shown as concrete consequences for *their* assets (the flat's insurance, the buyer's questions), not as global probabilities |
| **Ambiguity aversion** | Ellsberg 1961, QJE 75(4): people prefer known odds. Fox & Tversky 1995, QJE 110(3): the effect appears mainly when a vague option sits *next to* a clear one ("comparative ignorance"). Barnett, Brock & Hansen 2020, RFS 33(3): climate model uncertainty is priced | **Same uncertainty display for every option:** odds to 89 and a range, never a crisp number for the plain plan beside a fuzzy one for the ESG choice. Climate as two or three named scenarios |
| **Social desirability** (stated vs revealed ESG preference) | Fisher 1993, J. Consumer Research 20(2): indirect questions reduce the bias. Riedl & Smeets 2017, JF 72(6): social preferences and *signalling* drive SRI holdings; SRI investors expect lower returns and pay higher fees. Hartzmark & Sussman 2019, JF 74(6): Morningstar globes moved >US$24bn into high-rated funds with no evidence of higher returns. Heeb, Kölbel, Paetzold & Zeisberger 2023, RFS 36(5): people pay for sustainability but not more for *more* impact ("warm glow"). Anderson & Robinson 2022, Review of Finance 26(6): green-minded households don't hold greener portfolios. Bauer, Ruof & Smeets 2021, RFS 34(8): two-thirds of pension members backed SDG engagement even when they expected it to hurt returns | **Revealed-preference profiling.** Trade-off cards priced in HK$ a year and points to 89 ("this costs HK$9K a year, ≈2 points; it lowers carbon intensity by __%"). One indirect question ("what would families like yours choose?"). A scope test: does doubling the impact change what you would pay? Each person's expected ESG return recorded (Giglio et al. 2025 [S58]). Each parent answers separately, then together |
| **Loss aversion** | Kahneman & Tversky 1979, Econometrica 47(2). Benartzi & Thaler 1995, QJE 110(1): loss aversion plus annual evaluation explains the equity premium ("myopic loss aversion"). Gneezy & Potters 1997, QJE 112(2): more frequent feedback, less risk taken. ESG-specific: Humphrey, Kogan, Sagi & Starks 2021, NBER WP 29288 (working paper): negative ESG news weighs more than positive | **One substantive review a year**; the ESG sleeve judged against its twin over rolling 3–5 years, never month by month. A pre-agreed **controversy rule** (a flagged holding is reviewed within three months, not sold on the headline). The flat and the business shown as "what you keep", not "what you lose" |
| **Mental accounting** (and single-action bias, moral licensing) | Thaler 1985, Marketing Science 4(3); Thaler 1999, JBDM 12(3): labelled accounts break fungibility. Shefrin & Statman 2000, JFQA 35(2): layered portfolios. Das et al. 2010, JFQA 45(2): goal sub-portfolios can still be efficient in aggregate. Weber 1997 (book chapter; described in Weber 2006): people take *one* action and stop. Merritt, Effron & Monin 2010, SPPC 4(5): moral licensing. No investor-specific licensing evidence found | **One household balance sheet on page one;** the 25% shown as a slice of it, beside the business (HK$5.0M) and the flat (HK$11.5M), so "we did our ESG" can't stand in for the bigger decisions. Sleeves kept for *who pays*, never for *what risk* |
| **Label halo** (extra) | Ceccarelli, Ramelli & Wagner 2024, Review of Finance 28(1): Morningstar's Low Carbon Designation raised flows | **The label sits next to the metric it implies:** carbon intensity against the parent, holdings overlap, fee gap |
| **Overconfidence** (Ryan) | Barber & Odean 2000, JF 55(2): heaviest traders earned 11.4% against the market's 17.9%. Barber & Odean 2001, QJE 116(1): men trade 45% more | Position cap and written trading rule (Round One glide path); Ryan sees his own after-cost turnover drag each year |

The URL for each paper is in [S57]. Citations were checked on journal, RePEc, SSRN or author pages. Giglio et al. are cited from the **published** JFE version: its numbers differ from the NBER working
paper.

---

## 6. The one-page dashboard

**Design.**
- One page, in the brief's four outcome types.
- Reviewed **once a year** at the family meeting, with **event triggers** in between.
- Every figure carries its tag and data source. Impact is a separate ledger, not netted against anything.

| # | Metric | Type | Source (and tag) | Frequency | Trigger → action |
|---|---|---|---|---|---|
| F1 | Odds the money lasts to Carmen's 89 (today {{ladder_5_89}}) | Financial | Our model (MODEL) | Annual; and after any trigger | Falls >5 points or below 75%* → re-plan meeting |
| F2 | Price of values: all-in cost gap and realised tracking difference, each sleeve against its plain twin (HK$ a year; rolling 3 years) | Financial | Fund key facts statements and factsheets (SOURCED); our arithmetic (ESTIMATED) | Annual | Shared money gap >5bp*, or Carmen's tracking error >3%* → replace or re-decide |
| F3 | Business: debt-service cover on the HK$0.9M loan, margin, and the buyer-ready data pack (% complete) | Financial | Management accounts (SOURCED, the company's) | Half-yearly | Cover below the lender's covenant, or the pack <100% by 2034 → act (Fahtai) |
| F4 | Flat: value against the downsizing target, and the home-insurance renewal (premium, flood or typhoon exclusions) | Financial | RVD price index; insurer renewal notice (SOURCED) | Annual | Premium up >25%* or a new exclusion → review the 2037 exit year (Lookbua) |
| S1 | Weighted average carbon intensity (tCO2e per US$M revenue, Scope 1+2) of the listed holdings against the twin, with data coverage % | Sustainability | Fund or index reports. TCFD formula: Σ(weight × issuer emissions ÷ issuer revenue) [S42] (SOURCED) | Annual | Not ≥30%* below the twin, or coverage <80%* → the fund fails Annex S item 4 |
| S2 | Financed emissions of listed holdings (tCO2e, PCAF attribution: holding ÷ EVIC × company emissions) with PCAF data-quality score | Sustainability | PCAF Standard Part A, 3rd ed. 2025 [S43]; TCFD Table 2 [S42] (ESTIMATED) | Annual | Reported, no target (a family-sized portfolio can't steer it) |
| S3 | Business emissions: Scope 1+2 measured; Scope 3 as a range; intensity per HK$M revenue | Sustainability | Fuel and electricity bills, supplier data; GHG Protocol (MEASURED for 1–2; ESTIMATED for 3) | Annual | A listed customer asks for data, or the lender asks under its transition plan → baseline update (Fahtai) |
| S4 | Flat: electricity kWh a year and household Scope 2 | Sustainability | CLP bills × CLP's published emission factor (factor UNVERIFIED; Lookbua) | Annual | Rises >10%* → retrofit check |
| I1 | Business transition outcome: tCO2e cut against baseline by the financed projects (the one place with additionality) | Impact | Project data; verified if any KPI-linked loan exists (MEASURED / verified) | Annual | Behind the plan's path → review the project, not the claim |
| I2 | Green bond fund: share of bonds with external review and post-issuance reports; estimated avoided emissions, **shown apart and never netted** | Impact | Fund impact report; WBCSD guidance [S45] (ESTIMATED, issuer-reported) | Annual | External-review share falls below 90%* → fund review |
| I3 | Scholarship: funded ratio (capital held ÷ capital needed for the promised term) and scholars supported | Impact | The charity's annual statement (SOURCED) | Annual | Funded ratio <100% → pay out less, or top up from the sale upside; never from retirement money |
| M1 | Milestones: Annex S signed (Q1 2027*); profiling session (Dec 2026*); energy audit (2027*); loan decision (2027*); gift agreement (2027*); data pack (2034); flat decision with physical-risk check (2037) | Implementation | Adviser's tracker (MEASURED) | Each meeting | Any milestone missed by >6 months → named owner explains at the meeting |

*ILLUSTRATIVE thresholds and dates, for the family to set.

**Review triggers (between annual meetings).**
- **Markets:** global equities −20%, or 5-point drift (Round One rules).
- **Plan:** F1 falls more than 5 points.
- **Products:** a fund leaves the SFC ESG list or changes its index or method; a rating downgrade under the two-rating
  test; a fee rise; a controversy (review within 3 months, under the controversy rule).
- **Business:** a customer or lender asks for emissions data; loan refinancing; sale talks begin.
- **Property:** insurance renewal terms; a flood-map change.
- **Regulation:** Taxonomy Phase 2B; changes to the SFC's ESG rules or the HKMA's sales rules.
- **Life events:** a death, disability, Chloe's university offer (early 2028), Ryan's trust stages (25, 30, 35),
  retirement (2037, 2039).
- **Values:** a family member asks to change preferences. Record the change. ESMA ¶82–83: an adaptation applies "only
  … to the investment advice in question".

### 6b. Attribution against narrative

**"What the plan changed" against "what the market did": a pre-registered twin.** This is our design; no standard
prescribes it for a household.

1. **At signing,** fix the counterfactual in writing: the same strategic weights, with each ESG fund replaced by its
   parent index fund. Mapping: MSCI World for the ESG core; a global aggregate index for the green bond fund; a plain
   global equity MPF fund for the low-carbon MPF fund.
2. **Each year,** split the gap between the actual portfolio and its twin into four parts:
   - (a) **the market:** the twin's own return;
   - (b) **the ESG tilt at index level:** the ESG index minus its parent. Split it by Brinson–Fachler (Brinson &
     Fachler 1985, JPM 11(3); Brinson, Hood & Beebower 1986, FAJ 42(4)) into *sector allocation*, i.e. the screen's
     sector bets (allocation_i = (w_p,i − w_b,i)(R_b,i − R_b)), and *within-sector selection*
     (selection_i = w_b,i(R_p,i − R_b,i)). Both indices publish sector weights and returns. Add a factor check where
     possible (quality, size, tech).
   - (c) **implementation:** fees and tracking difference between each fund and its index;
   - (d) **decisions:** rebalancing, timing and cash drag (actual against policy weights), and a residual.
3. **Why this matters.** ESG returns are mostly sector and factor exposure, not the label. Bruno, Esakia & Goltz 2022,
   Journal of Investing 31(3): no significant ESG alpha after sector and quality adjustment. Giese et al. 2019, JPM
   45(5): the three channels (cash flow, risk, valuation). Pástor, Stambaugh & Taylor 2022, JFE 146(2): green
   outperformance from unexpected rises in climate concern.
   - "2020–21 outperformance came from the energy underweight" is **UNVERIFIED**: no source found. Keep it off slides.
4. **A lighter version, if the panel or the family wants less:** the twin comparison plus one sector-allocation bar,
   once a year. Fund holdings are disclosed with a lag, so a family-sized portfolio can't do more with confidence
   (agent's counter-argument; agreed).

**What cannot yet be measured** (say so on the dashboard):
- **Scope 3 of holdings:** the most inconsistent data across providers. Third-party estimates are less consistent
  than company-reported figures (Busch, Johnson & Pioch 2022, J. Industrial Ecology 26(1) [S48]). Show it as a range
  with its PCAF score (score 5 = "the necessary starting point" [S44]).
- **ESG ratings:** pairwise correlation 0.38–0.71 across six raters; divergence comes from measurement 56%, scope 38%
  and weights 6% (Berg, Kölbel & Rigobon 2022 [S47]). Always name the rater.
- **Avoided emissions:** "shall always be reported separately from: GHG inventory footprints" and "shall not be used to
  claim … carbon neutrality, net-zero" (WBCSD, Mar 2023 [S45]). Superseded by v2.0 on 24 Jul 2025: confirm the rule
  survives (UNVERIFIED).
- **Additionality of listed holdings:** the counterfactual is unknowable. Divestment barely moves the cost of capital:
  it is "too small to meaningfully affect real investment decisions" (Berk & van Binsbergen 2025, JFE 164).
- **Implied temperature rise:** methods diverge; practitioners "shy away … due to the perceived opaqueness of the
  underlying assumptions" (GFANZ, Nov 2022 [S46]). Use a range or nothing.

---

## 7. Funded philanthropy

**What "funded rather than aspirational" means in practice** (our five tests):
1. **The money is set aside or legally committed:** a gift agreement, a fund at a charity, a will clause.
2. **Its size is set by arithmetic** to the promise: an amount, a term, an assumed return.
3. **Its cost is tested in the plan,** in points of odds to 89.
4. **It has governance:** who picks scholars, what is reported, what happens on a shortfall.
5. **It has a step-down rule:** if underfunded, pay less, never draw on retirement money.

Round One passes none of the five. "About HK$30K a year through a registered charity" has no capital, no term and no
cost in the plan.

**The Hong Kong rules that shape it** (IRD, *Tax Guide for Charitable Institutions and Trusts of a Public Character*,
June 2023 [S39]; SOURCED):
- **Tax deduction.** Under ss.16D and 26C of the Inland Revenue Ordinance (IRO), an "approved charitable donation" is a
  donation **of money** to a s.88 tax-exempt charity, or to the Government, for charitable purposes (¶54).
  - The donor's (and spouse's) aggregate must be at least HK$100.
  - "the allowable deduction in any year cannot exceed 35% of the person's assessable income or profits".
  - One deduction per donation, claimed once (¶55).
  - A payment that buys "an advantage of a material character" is not a donation (¶56–57).
- **What this means for the Wongs** (our inference):
  - Giving units or shares is not deductible; sell first and give cash (Hong Kong has no capital gains tax, so selling
    costs nothing).
  - Relief exists only while they have assessable income: **after 2039, gifts get no relief**.
- **"Registered charity" is loose wording.** "The Department is not responsible for the registration of charities"
  (¶2); the s.88 list "does not constitute a formal register". The Law Reform Commission recommended registration on
  6 Dec 2013 [S41]; whether it was implemented is UNVERIFIED. **Fix the wording to "a tax-exempt charity under s.88".**
- **Public benefit.** A scholarship fund "for employees of a particular company" is not charitable (¶9(d)).
  Beneficiaries "must not be defined by a personal connection like family relationship or common employer" (¶11).
  - So the scholarship can't favour Carmen's staff's children or Chloe.
  - "Scholarships based on academic merit" are an accepted example of advancing education (Appendix).
- **Structures** (¶16): a trust, a society, a company limited by guarantee (most s.88 charities), or a statutory body.
  - It must have a written governing instrument with standard clauses (¶17): no remuneration of governors, conflicts
    declared, assets passed to a charity on dissolution, annual accounts.
  - The IRD aims to answer an exemption application within 4 months (¶63) and may call for accounts at any time (¶65).
- **Stamp duty:** gifts of HK stock or property to charity are exempt (¶52; Stamp Duty Ordinance s.44).

**Vehicles compared** (costs UNVERIFIED unless stated; get quotes):

| Route | Set-up and running | Tax | Control | Funded? |
|---|---|---|---|---|
| Annual gifts from cash flow to a s.88 charity that runs scholarships (Round One) | None | 17% relief while earning, nothing after | Low | **No:** stops in the first tight year |
| A **named term or endowed fund within an existing s.88 charity**, under a gift agreement | The charity's terms: minimum gift and admin fee UNVERIFIED | Deduction in the year given, within the 35% cap, so spread over 2 years | Medium (the family advises on criteria; the charity awards) | **Yes** |
| The family's own charitable trust or company limited by guarantee, with s.88 status | Legal drafting, annual accounts (audit for a company), governance, a 4-month IRD review | Same for donors; the charity itself is exempt | High | Yes, but costly at HK$0.5–1.5M |
| A donor-advised fund | No statutory donor-advised-fund category found in Hong Kong. Some providers may run donor-advised accounts under their own s.88 status: UNVERIFIED | — | Medium | — |
| A bequest in the wills | Already in the plan's will drafting | No relief; estate duty abolished 2006 (manuscript §9) | — | Only at death |

**Capital needed** (ESTIMATED, in today's money, HK$30K a year rising with CPI).
- **Return assumption:** the Round One model's 50/50 mix, 6% equities and 4% bonds, gives 5.0% nominal. Less 2.5% CPI
  that is 2.44% real; less ≈0.5% charity investment cost (ILLUSTRATIVE) it is ≈1.95% real. We show 2.0%, 2.5% and 3.0%.
- **Formulas:** perpetuity = 30K ÷ r. Term of n years = 30K × [1 − (1+r)^−n] ÷ r (payments at year-end).

| Real return r | Perpetuity | 20 years | 10 years |
|---|---|---|---|
| 2.0% | HK$1,500,000 | HK$490,543 (factor 16.351) | HK$269,478 |
| 2.5% | **HK$1,200,000** | **HK$467,675** (15.589) | HK$262,562 |
| 3.0% | HK$1,000,000 | HK$446,324 (14.877) | HK$255,906 |

- **A perpetuity paid at a fixed real amount is not safe in bad markets.** Endowments use a spending rule, so the award
  would vary. Write that rule into the gift agreement.
- **Tax value** (ESTIMATED; model Tax sheet, 2026/27):
  - Adrian's net chargeable income is HK$755.5K and Carmen's HK$525.5K. Both are taxed at the progressive rates, both
    in the 17% top band.
  - **HK$480K given over 2027–28:** relief ≈HK$81.6K; net cost ≈HK$398K. Each year's HK$240K is under Adrian's cap
    (35% × ≈HK$1.2M ≈ HK$420K).
  - **HK$1.2M perpetual:** relief ≈HK$204K if spread over 3 years within the caps; net ≈HK$996K. Carmen's cap is
    ≈HK$252K a year.

**The options tested on the Round One model** (MODEL, exploratory, 4 Nov; full plan 82.6% to Carmen's 89, median pot at
89 HK$6.68M in today's money):
- Gifts are nominal outflows in the year given.
- Relief is 17% of the gift, credited the next year, for gifts made while a salary is still taxed (before 2039).
- The script is `scratchpad/scripts/giving_runs.py`, on this session's temporary scratchpad. Its logic is described
  here so Pete can rebuild it in `export_numbers()`.

| Option | Odds to 89 | Median pot at 89 | Change |
|---|---|---|---|
| Round One as written: HK$30K a year, CPI-linked, 2027–2065, from cash flow | 75.7% | HK$5.09M | **−6.9 pts** |
| The same for 20 years only (2027–46) | 79.0% | HK$5.78M | −3.6 |
| **A funded 20-year fund: 2 × HK$240K in 2027–28, with relief** | **80.0%** | HK$5.91M | **−2.6** |
| Built while earning: HK$120K a year, 2027–36, with relief | 76.2% | HK$5.01M | −6.4 |
| Perpetual now: 3 × HK$400K in 2027–29, with relief | 75.2% | HK$4.75M | −7.4 |
| Perpetual from the sale: HK$1.2M from a HK$3.0M sale in 2039 (no relief) | 76.6% | HK$5.30M | −6.0 |
| **Perpetual from the upside: the sale fetches HK$4.0M, HK$1.0M of it endows** | **82.6%** | HK$6.68M | **0.0** (the HK$4.0M sale with no gift: 86.4%) |

These agree with Final_Plan §2's runs (HK$300K → 80.5%; HK$600K → 78.3%): ≈0.7 points per HK$100K of net gift.

**Recommendation to test** (opinion):
- **Now:** a 20-year named "sustainable design" scholarship fund held by an existing s.88 charity: ≈HK$0.48M given in
  2027–28, net ≈HK$0.40M after relief, ≈2.6 points (MODEL, exploratory).
- **Later:** a written rule converts it to a perpetual endowment only from sale proceeds above the HK$3.0M the plan
  counts (e.g. half the excess, up to HK$1.0M). The will carries a backstop clause.
- **The refusal:** we refuse to promise HK$30K a year for life from cash flow. Unfunded it costs ≈7 points, and it
  would stop in the first bad year.
- **Who decides:** whether ≈2.6 points is worth it is the family's call. It shows the price of their values in their
  own currency. Adrian may say no, and the trade-off card exists for exactly that.

---

## 8. Likely judge questions, with short answers

1. **"Green loan or sustainability-linked loan for Carmen?"**
   - A green loan funds a defined asset (vans, solar) and needs use-of-proceeds tracking. An SLL is general-purpose,
     priced on KPIs, and needs annual verification.
   - At HK$0.9M, each 10bp of ratchet is worth about HK$900 a year, likely less than verification (ESTIMATED; ratchet
     sizes UNVERIFIED). A green loan for a specific asset fits better. Fahtai has the numbers.
2. **"Isn't your 25% just a label?"**
   - Yes, in October it was. It buys alignment and lower carbon intensity, not impact: it fails the additionality test
     (Brest & Born; Kölbel et al.).
   - We now count it by outcome (carbon intensity against the parent, coverage) and price it in HK$. The money that
     changes outcomes is in the business and the flat.
3. **"Does Hong Kong require you to ask about sustainability preferences?"** No: HKMA FAQ Q7 (Nov 2023): "not a
   mandatory requirement". The SFC Code has only general suitability (¶5.2). We use the EU's structure voluntarily and
   make the answers binding.
4. **"How do you settle Adrian and Carmen?"** Separate the money, a cost test for shared money, a values budget for
   Carmen's sleeve, a status-quo default. This matches ESMA's "most prudent approach" for group clients. Family ESG
   stays ≈21.8%.
5. **"What does Adrian give up for Carmen's values?"**
   - Under the mandate, almost nothing: his sleeve passes only cost-neutral choices.
   - At Round One's funds, the family was giving up ≈HK$12K a year, ≈4–6 points (MODEL, exploratory). The new rule
     moves that cost to Carmen's sleeve and asks for a cheaper vehicle.
6. **"Is there a greenium for the family?"** It is ≈0–2bp (Zerbib 2019; Larcker & Watts 2020), a slightly lower yield.
   The fund fee is ≈50 times larger. Don't confuse it with the green premium, a technology cost gap.
7. **"How do you know the ESG fund is better than the index?"** By the pre-registered twin: tilt, cost and market
   separated each year, Brinson–Fachler by sector. If carbon intensity isn't ≥30% below the parent with ≥80%
   coverage, the fund fails Annex S.
8. **"Can you measure the green bond fund's impact?"** Only as issuer-reported, estimated avoided emissions, shown
   separately and never netted (WBCSD). We don't call it additional.
9. **"Why not a perpetual scholarship?"** Paid now it costs ≈7 points of Adrian and Carmen's security. We fund 20 years
   now (≈2.6 points) and endow from the sale upside (zero cost to the base plan).
10. **"Is the donation deductible?"** Money only, to a s.88 charity, within 35% of assessable income, and only while
    they earn. Giving shares gets no deduction.
11. **"Why annual reviews, not quarterly?"** Frequent evaluation makes loss-averse people take less risk (Benartzi &
    Thaler 1995; Gneezy & Potters 1997). Triggers handle real events between meetings.
12. **"Isn't Carmen's stated preference just social desirability?"** Possibly: stated and revealed preferences differ
    (Anderson & Robinson 2022; Heeb et al. 2023). Hence priced trade-off cards and an indirect question, and each
    parent answers separately.
13. **"Who decides on Ryan's crypto and tokenised products?"** Ryan, with his own money under his Round One glide
    path. The charter gives him no claim on shared money. He keeps the dashboard data, which engages him without
    giving him control.
14. **"What can't you measure?"** Scope 3 of holdings, avoided emissions, additionality of listed holdings, implied
    temperature rise. Each is shown as a range or marked "not measured".
15. **"Where's the Taxonomy in this?"**
    - Phase 2A (22 Jan 2026) adds transition elements and adaptation. It is a classification tool for banks and
      issuers, not a family rule.
    - It matters to the Wongs through Carmen's lender (labelling, GS-2 transition plans), and, under the Grant
      Scheme, 75% subsidy for Taxonomy-aligned issues above HK$100M. Not for her.

**Sounds clever, fails** (opinion; each listed in §1, point 7).

---

## 9. Open items and what is unverified

**For Win, before the price-of-values slide:**
- The BOC-Prudential ESG sub-fund's own fee (≈0.78% is the series brochure); Allianz Green Bond 1.14%; AGGU's and
  IWDA's ongoing charges; the MPF Low Carbon fund's fee against a plain MPF equity fund.
- The ESG core's index and its tracking error against MSCI World: factsheets not obtained.
- Whether a cheaper SFC-listed global ESG index fund exists; holdings overlap and carbon intensity against a UCITS
  Article 8 ESG ETF.

**For Pete (model):**
- Add to `export_numbers()`: the fee-drag runs (5–25bp) and the giving options (§7), then diff `numbers.json`.
- Model the Grant / relief logic properly. The scratch runs credit 17% relief the following year and ignore the 35% cap
  beyond the annual split.

**Not reached** (sites returned 403, empty pages, or needed JavaScript; or the search budget ran out):
- thegiin.org: GIIN's own wording and four characteristics.
- gatesnotes.com: the "Green Premium" wording.
- msci.com: all ESG index factsheets.
- The PRI site: responsible-investment policy guidance.
- Morgan Stanley Sustainable Signals.
- The FCA's SDR consumer research.
- The European Commission's 2023 SFDR consultation.
- The full Taxonomy Phase 2A text (>10 MB): sector sunset dates and the activity list.
- IFRS S2 ¶29 cross-industry metrics: not re-read today. Its effective date (1 Jan 2024) and the Dec 2025 amendments to
  the GHG disclosures are confirmed on ifrs.org; their effect on Category 15 is UNVERIFIED.

**UNVERIFIED claims, don't use without a check:**
- HKEX Scope 3 treatment (Appendix C2);
- Core Climate HKD/RMB settlement;
- Hong Kong donor-advised-fund providers;
- charity minimum gifts and admin fees;
- whether the 2013 charity registration recommendation was implemented;
- margin-ratchet sizes;
- CLP's emission factor;
- exclusion thresholds of the ESG index;
- WBCSD v2.0's separate-reporting rule;
- the "energy underweight" explanation of 2020–21;
- Chhabra 2005's content (citation verified);
- Bacon 2008;
- the 2DII "Lost in the maze" figures;
- the date the ESMA guidelines apply from in translation;
- the Berk & van Binsbergen basis-point figure;
- the unit of Giglio et al.'s −2.1% (annualised or cumulative).

**Untested assumptions in this brief** (test, don't build on):
1. The family accepts a status-quo default on disputes.
2. A 5bp cost test is the right level (set it with the trade-off card).
3. An existing s.88 charity will hold a named 20-year fund of ≈HK$0.48M.
4. The model's 17% relief timing is close enough.
5. Ryan wants the dashboard role.

**What would change these conclusions:**
- If Win finds the ESG core's real all-in fee is near the plain fund's, the price of values falls to ≈0. The cost test
  then lets the ESG core back into Adrian's sleeve, and "the label's price is the fee" weakens.
- If a charity requires a much larger minimum, the 20-year fund becomes the family's own trust or a smaller term.

---

## Sources

Dates are publication or edition dates; all accessed 4 Nov 2026. "Primary" unless marked.

- [S1] ICMA, Green Bond Principles, June 2025. https://www.icmagroup.org/assets/documents/Sustainable-finance/2025-updates/Green-Bond-Principles-GBP-June-2025.pdf
- [S2] LMA/APLMA/LSTA, Green Loan Principles, 26 Mar 2025. https://lma.eu.com/application/files/1917/4298/0817/Green_Loan_Principles_-_26_March_2025.pdf
- [S3] ICMA, Sustainability-Linked Bond Principles, June 2024. https://www.icmagroup.org/assets/documents/Sustainable-finance/2024-updates/Sustainability-Linked-Bond-Principles-June-2024.pdf
- [S4] LMA/APLMA/LSTA, Sustainability-Linked Loan Principles, 26 Mar 2025. https://www.lsta.org/content/sustainability-linked-loan-principles-sllp/
- [S5] ICMA, Climate Transition Finance Handbook, Nov 2025. https://www.icmagroup.org/assets/documents/Sustainable-finance/2025-updates/Climate-Transition-Finance-Handbook-November-2025.pdf
- [S6] ICMA, Climate Transition Bond Guidelines announcement, 6 Nov 2025. https://www.icmagroup.org/News/news-in-brief/the-executive-committee-of-the-principles-announces-guidance-for-climate-transition-bonds/
- [S7] LMA/APLMA/LSTA, Guide to Transition Loans, 16 Oct 2025 (landing page; PDF behind member login). https://www.lsta.org/content/transition-loans-guide/
- [S8] HKMA, Hong Kong Taxonomy Phase 2A, circular 22 Jan 2026. https://brdr.hkma.gov.hk/eng/doc-ldg/docId/20260122-7-EN ; press release https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/01/20260122-3/
- [S9] HKMA, Phase 2B prototype consultation, 7 Sep 2026. https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/09/20260907-3/
- [S10] HKMA, SPM GS-2 "Transition Planning", V.1, 22 Sep 2026. https://brdr.hkma.gov.hk/eng/doc-ldg/spm/current/GS-2
- [S11] CFA Institute, GSIA and PRI, *Definitions for Responsible Investment Approaches*, Nov 2023. https://www.gsi-alliance.org/wp-content/uploads/2023/10/ESG-Terminology-Report_Online.pdf
- [S12] Brest, P. & Born, K., "When Can Impact Investing Create Real Impact?", *Stanford Social Innovation Review* 11(4), Fall 2013. https://ssir.org/up_for_debate/article/impact_investing
- [S13] Kölbel, J., Heeb, F., Paetzold, F. & Busch, T., "Can Sustainable Investing Save the World?", *Organization & Environment* 33(4): 554–574, 2020. https://safe-frankfurt.de/publications/working-papers/details/publicationname/can-sustainable-investing-save-the-world-reviewing-the-mechanisms-of-investor-impact.html
- [S14] Zerbib, O.D., *Journal of Banking & Finance* 98: 39–60, 2019 (abstract via RePEc).
- [S15] Larcker, D. & Watts, E., "Where's the greenium?", *Journal of Accounting and Economics* 69(2–3): 101312, 2020.
- [S16] Flammer, C., "Corporate green bonds", *Journal of Financial Economics* 142(2): 499–516, 2021.
- [S17] Commission Delegated Regulation (EU) 2021/1253, 21 Apr 2021, applies from 2 Aug 2022 (CELEX 32021R1253; read via the lawplayer.com mirror, because EUR-Lex returned an empty page). https://lawplayer.com/eu/act/32021R1253
- [S18] ESMA, Guidelines on certain aspects of the MiFID II suitability requirements, ESMA35-43-3172, 23 Sep 2022. https://www.esma.europa.eu/sites/default/files/library/esma35-43-3172_final_report_on_mifid_ii_guidelines_on_suitability.pdf
- [S19] ESMA, Public Statement on the CSA on MiFID II sustainability aspects, ESMA35-915049491-6291, 6 May 2026. https://www.esma.europa.eu/sites/default/files/2026-05/ESMA35-915049491-6291_Statement_on_the_CSA_on_MiFID_II_sustainability_aspects.pdf
- [S20] 2DII, "Please Don't Let Them Be Misunderstood!", May 2022. https://www.euki.de/wp-content/uploads/2022/08/20_095_Misunderstood.pdf
- [S21] 2DII (Mangot & Bayer), "What do your clients actually want?", May 2022. https://www.euki.de/wp-content/uploads/2022/08/20_095_Whatclientswant.pdf
- [S22] Cauthorn, Eckert, Kellers, Klein & Zwergel, "Do advisors respond to investors' preferences?", working paper, June 2024. https://sustainablefinancealliance.org/wp-content/uploads/2024/02/Do-advisors-respond-to-investors-preferences_-_Grasfi-2024.pdf
- [S23] HKMA, "Sale and Distribution of Green and Sustainable Investment Products", circular 29 Nov 2023. https://brdr.hkma.gov.hk/eng/doc-ldg/docId/getPdf/20231129-5-EN/20231129-5-EN.pdf
  - Annex I: https://brdr.hkma.gov.hk/eng/doc-ldg/docId/getPdf/20231129-6-EN/20231129-6-EN.pdf
  - Annex II FAQs: https://brdr.hkma.gov.hk/chi/doc-ldg/docId/getPdf/20231129-7-EN/20231129-7-EN.pdf
- [S24] HKMA, Further FAQs, 29 Dec 2025. https://brdr.hkma.gov.hk/eng/doc-ldg/docId/getPdf/20251229-1-EN/20251229-1-EN.pdf
- [S25] SFC, Code of Conduct for Persons Licensed by or Registered with the SFC, edition dated Jan 2026, ¶5.1–5.2 (read by a research agent; URL not recorded).
- [S26] SFC, Circular to management companies … ESG funds, 29 Jun 2021, effective 1 Jan 2022. https://apps.sfc.hk/edistributionWeb/api/circular/openFile?lang=EN&refNo=21EC27 ; List of ESG funds https://www.sfc.hk/en/Regulatory-functions/Products/List-of-ESG-funds
- [S27] SFC, Circular on climate-related risks (Fund Manager Code), 20 Aug 2021. https://apps.sfc.hk/edistributionWeb/api/circular/openFile?lang=EN&refNo=21EC31
- [S28] CFA Institute, Global ESG Disclosure Standards for Investment Products (© 2021; footnote "As of 1 November 2021"). https://rpc.cfainstitute.org/esg-standards
- [S29] CFA Institute, *Elements of an Investment Policy Statement for Individual Investors*, May 2010. https://rpc.cfainstitute.org/sites/default/files/-/media/documents/article/position-paper/investment-policy-statement-individual-investors.pdf
- [S30] Swiss Bankers Association, Guidelines on the integration of ESG-preferences and ESG-risks (adopted 16 Jun 2022; updated 26 Nov 2025). https://www.swissbanking.ch/_Resources/Persistent/1/0/3/c/103cd03894ec90ebde7ce137be0d92b9accc5392/SBA_Guidelines_investment_advice_and_portfolio_management_EN_2025.pdf
- [S31] HKMA, Sustainable Finance Action Agenda, 21 Oct 2024. https://www.hkma.gov.hk/eng/news-and-media/press-releases/2024/10/20241021-4/
- [S32] HKSAR Government, Hong Kong's Climate Action Plan 2050, Oct 2021. https://cnsd.gov.hk/wp-content/uploads/pdf/CAP2050_leaflet_en.pdf ; https://cnsd.gov.hk/en/climate-ready/climate-targets-of-hk/
- [S33] HKMA, SPM GS-1 "Climate Risk Management", V.1, 30 Dec 2021. https://brdr.hkma.gov.hk/eng/doc-ldg/spm/current/GS-1
- [S34] HKICPA, HKFRS S1 and S2 issued, 12 Dec 2024. https://www.hkicpa.org.hk/en/News/News-Release/20241212_HKFRS_S1_S2
- [S35] FSTB, Roadmap on Sustainability Disclosure in Hong Kong, Dec 2024. https://www.fstb.gov.hk/fsb/en/publication/report/docs/FSTB_Roadmap2024_eBooklet_EN.pdf
- [S36] HKEX, ESG Academy: Rules and Regulations (Appendix C2 climate requirements). https://www.hkex.com.hk/Listing/Sustainability/ESG-Academy/Rules-and-Regulations?sc_lang=en
- [S37] HKEX, Core Climate launch, 28 Oct 2022. https://www.hkex.com.hk/News/News-Release/2022/221028news?sc_lang=en
- [S38] HKMA, Green and Sustainable Finance Grant Scheme (guideline effective 24 Apr 2026). https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/bond-market-development/tax-concessions-and-incentive-schemes/
- [S39] IRD, *Tax Guide for Charitable Institutions and Trusts of a Public Character*, June 2023 (PDF text extracted and read in full for ¶2, 9–11, 16–17, 51–57, 61–65). https://www.ird.gov.hk/eng/pdf/tax_guide_for_charities.pdf
- [S40] IRD, s.88 tax-exempt charities: search and list. https://www.ird.gov.hk/eng/tax/ach_index.htm
- [S41] Law Reform Commission of Hong Kong, Report on Charities, 6 Dec 2013. https://www.hkreform.gov.hk/en/publications/rcharities.htm
- [S42] TCFD, *Implementing the Recommendations*, Oct 2021: Tables 2–3 (PCAF attribution formulas; WACI "expressed in tons CO2e/$M revenue"); asset managers "should disclose … WACI for each product". https://assets.bbhub.io/company/sites/60/2021/07/2021-TCFD-Implementing_Guidance.pdf
- [S43] PCAF, Global GHG Accounting and Reporting Standard, Part A Financed Emissions, 3rd edition (2025). https://carbonaccountingfinancials.com/standard
- [S44] CDP and PCAF, data quality report, June 2023. https://carbonaccountingfinancials.com/files/Importance-of-data-quality-CDP-PCAF.pdf
- [S45] WBCSD, Guidance on Avoided Emissions, 22 Mar 2023. https://archive.wbcsd.org/contentwbc/download/15909/229494/1 ; v2.0, 24 Jul 2025: https://www.wbcsd.org/resources/guidance-on-avoided-emissions-helping-business-drive-innovations-and-scale-solutions-towards-net-zero/
- [S46] GFANZ, *Measuring Portfolio Alignment: Driving Enhancement, Convergence, and Adoption*, Nov 2022. https://assets.bbhub.io/company/sites/63/2022/09/Measuring-Portfolio-Alignment-Enhancement-Convergence-and-Adoption-November-2022.pdf
- [S47] Berg, F., Kölbel, J. & Rigobon, R., "Aggregate Confusion", *Review of Finance* 26(6): 1315–1344, 2022. https://papers.ssrn.com/abstract=3438533
- [S48] Busch, T., Johnson, M. & Pioch, T., *Journal of Industrial Ecology* 26(1): 350–363, 2022. https://econpapers.repec.org/RePEc:bla:inecol:v:26:y:2022:i:1:p:350-363
- [S55] Pástor, Ľ., Stambaugh, R. & Taylor, L., "Dissecting green returns", *JFE* 146(2): 403–424, 2022. https://econpapers.repec.org/RePEc:eee:jfinec:v:146:y:2022:i:2:p:403-424
- [S56] Bolton, P. & Kacperczyk, M., "Do investors care about carbon risk?", *JFE* 142(2): 517–549, 2021.
- [S57] Behavioural and attribution papers (§5, §6b), each verified on a journal, RePEc, SSRN or author page by a research agent on 4 Nov 2026:
  - Laibson 1997: https://dash.harvard.edu/bitstream/1/4481499/2/Laibson_GoldenEggs.pdf
  - O'Donoghue & Rabin 1999: https://econpapers.repec.org/RePEc:aea:aecrev:v:89:y:1999:i:1:p:103-124
  - Thaler & Benartzi 2004: https://ideas.repec.org/a/ucp/jpolec/v112y2004is1ps164-s187.html (the 3.5% → 13.6% figure is from https://www.anderson.ucla.edu/faculty-and-research/faculty-directory/benartzi)
  - Weber 2006, also the source for Weber 1997's single-action bias: https://elke-u-weber.com/media/2006_climaticchange_weber.pdf
  - Ellsberg 1961: https://ideas.repec.org/a/oup/qjecon/v75y1961i4p643-669..html
  - Fox & Tversky 1995: https://ideas.repec.org/a/oup/qjecon/v110y1995i3p585-603..html
  - Barnett, Brock & Hansen 2020: https://econpapers.repec.org/RePEc:oup:rfinst:v:33:y:2020:i:3:p:1024-1066.
  - Fisher 1993: https://academic.oup.com/jcr/article-abstract/20/2/303/1793106
  - Riedl & Smeets 2017: https://econpapers.repec.org/RePEc:bla:jfinan:v:72:y:2017:i:6:p:2505-2550
  - Hartzmark & Sussman 2019: https://ecgi.global/sites/default/files/working_papers/documents/finalhartzmarksussman2.pdf
  - Bauer, Ruof & Smeets 2021: https://cris.maastrichtuniversity.nl/en/publications/get-real-individuals-prefer-more-sustainable-investments/
  - Heeb, Kölbel, Paetzold & Zeisberger 2023: https://papers.ssrn.com/abstract=3765659
  - Anderson & Robinson 2022: https://econpapers.repec.org/RePEc:oup:revfin:v:26:y:2022:i:6:p:1551-1584.
  - Kahneman & Tversky 1979: https://www.econometricsociety.org/publications/econometrica/1979/03/01/prospect-theory-analysis-decision-under-risk
  - Benartzi & Thaler 1995: https://econpapers.repec.org/RePEc:oup:qjecon:v:110:y:1995:i:1:p:73-92.
  - Gneezy & Potters 1997: https://ideas.repec.org/a/oup/qjecon/v112y1997i2p631-645..html
  - Humphrey, Kogan, Sagi & Starks 2021 (NBER WP 29288, a working paper): https://www.nber.org/papers/w29288
  - Thaler 1985: https://econpapers.repec.org/RePEc:inm:ormksc:v:4:y:1985:i:3:p:199-214
  - Thaler 1999: https://people.bath.ac.uk/mnsrf/Teaching%202011/Thaler-99.pdf
  - Shefrin & Statman 2000: https://ideas.repec.org/a/cup/jfinqa/v35y2000i02p127-151_00.html
  - Das, Markowitz, Scheid & Statman 2010: https://ideas.repec.org/a/cup/jfinqa/v45y2010i02p311-334_00.html
  - Merritt, Effron & Monin 2010: https://www.kellogg.northwestern.edu/faculty/research/detail/2010/moral-self-licensing-when-being-good-frees-us-to
  - Ceccarelli, Ramelli & Wagner 2024: https://academic.oup.com/rof/article-abstract/28/1/45/7103324
  - Barber & Odean 2000: https://econpapers.repec.org/RePEc:bla:jfinan:v:55:y:2000:i:2:p:773-806
  - Barber & Odean 2001: https://ideas.repec.org/a/oup/qjecon/v116y2001i1p261-292..html
  - Brinson, Hood & Beebower 1986 (DOI 10.2469/faj.v42.n4.39)
  - Brinson & Fachler 1985 (DOI 10.3905/jpm.1985.409005; details from secondary sources only)
  - Giese et al. 2019: https://www.longfinance.net/documents/1722/Research_Insight_Foundations_of_ESG_Investing_Part_1.pdf
  - Bruno, Esakia & Goltz 2022: https://cdn.ihsmarkit.com/www/pdf/0521/Honey-I-Shrunk-the-ESG-Alpha.pdf
- Journal citations without a URL here (S14–S16, S56, S59, S60, Chhabra 2005) were checked against Crossref, OpenAlex or RePEc by a research agent; the URLs were not recorded.
- [S58] Giglio, S., Maggiori, M., Stroebel, J., Tan, Z., Utkus, S. & Xu, X., "Four facts about ESG beliefs and investor portfolios", *JFE* 164: 103984, 2025. https://pages.stern.nyu.edu/~jstroebe/PDF/GMSTUX_VanguardESG_JFE.pdf
- [S59] Berk, J. & van Binsbergen, J., "The impact of impact investing", *JFE* 164: 103972, 2025.
- [S60] Atz, U., Van Holt, T., Liu, Z. & Bruno, C., *Journal of Sustainable Finance & Investment* 13(1): 802–825, 2023. Also: Friede, Busch & Bassen, JSF&I 5(4), 2015 (firm-level performance, not investor returns); Pedersen, Fitzgibbons & Pomorski, "The ESG-efficient frontier", JFE 142(2), 2021; Cornell, *European Financial Management* 27(1), 2021.
