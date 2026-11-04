# Area 3 · Portfolio integration and the price of values (research brief for Win)

Prepared 4 Nov 2026 for the Final (21 Nov 2026; slides due 16 Nov, 17:00). Owner: Win. Covers brief area 3 ("Portfolio
Integration") and the evidence for "the price of values" in area 1.

**How to read the tags.**

- SOURCED: published or measured by the cited source; I or a research agent opened it, unless the row says "snippet".
- ESTIMATED: our arithmetic on sourced inputs, with the working shown.
- ILLUSTRATIVE: an assumption or design choice of ours.
- UNVERIFIED: not confirmed this session.

The brief's words "measured, estimated and illustrative" map to SOURCED, ESTIMATED and ILLUSTRATIVE.

**Limits.**

- The session's web-search budget ran out partway. Later facts come from known primary URLs opened directly.
- Search-based gaps are listed in §7.
- Secondary sources are labelled as such.

**Fits with** `Final/research/area1_6_framework.md`. Its §3c rules are a 5bp cost test for shared money and a tracking-error
budget of 3% or less for Carmen. Its Annex S counting rule asks for carbon intensity at least 30% below the parent.
This brief closes its open items for Win (lines 292 and 600–603): the ESG core's index, its fee, and its tracking error.

---

## 1. Bottom line for Win

1. **Our Round One ESG core cannot be bought.**
   - The BOC-Prudential MSCI World ESG Index Fund is on the SFC's list of ESG funds (authorised 2 May 2024).
   - Its fund size is **US$0.00M in every monthly filing from Sep 2024 to Sep 2026**. Its sibling, the BOC-Prudential
     S&P 500 Index Fund, holds US$67.27M.
   - It has no offering document on the SFC or HKEX registers, and it is missing from the series' Dec 2025 brochure.
   - That fund was HK$1.49M of our HK$2.64M "ESG" (56%). It passed the label test; the product doesn't exist for sale.
     Call BOCI-Prudential to confirm before anyone says it on stage.
2. **The price of ESG equity is in the index design, not the fee.**
   - Irish UCITS ESG ETFs on MSCI World cost **0.20%, the same as IWDA**.
   - Long run, the best-in-class index (MSCI World Selection, ESG Leaders until 3 Feb 2025) returned **7.88% a year
     vs 7.85%** for MSCI World, Sep 2007 to Oct 2026. Tracking error was 1.42%.
   - Last five years, the gap against the plain index widens as the screen tightens:
     - Selection −0.44 points a year
     - Low Carbon SRI Selection −0.99
     - Climate Transition Benchmark (CTB) −1.43
     - SRI −2.93
3. **The greenium is noise; the fee is the price.**
   - Same-issuer studies find about 0–8bp; German twin Bunds were about 1–2bp by 2024.
   - On Carmen's HK$207K of green bonds, 2–10bp is **HK$41–207 a year**. Allianz Green Bond's fee gap over a plain
     aggregate ETF is **HK$2,153 a year** (1.04 points), 10 to 50 times more.
   - Since Jan 2017 the fund has trailed its own benchmark by **≈0.98 points a year** (−11.46% vs −2.49%
     cumulative), about its 1.09% all-in fee.
4. **A green label is not a low-carbon portfolio.**
   - iShares' USD green bond ETF (BGRN) shows a weighted average carbon intensity (WACI) of **708.64 tCO2e per US$M
     of sales**, with 82.39% coverage, and an implied temperature rise **above 3.0°C**.
   - Those metrics score the issuers, not the projects. A green bond sleeve has to be measured by financed projects
     (an impact report).
   - We found no fund-level impact report for Allianz Green Bond.
5. **The Hong Kong retail menu is thin, and the label doesn't protect the client.** Hong Kong retail investors have:
   - 179 SFC-listed ESG funds (list file of 23 Oct 2026), of which only 2 are classed "impact";
   - no government retail green bond outstanding since 4273 matured on 12 Oct 2026;
   - one personal green deposit found, paying **0.001%** in HKD;
   - a clean-energy ETF **on the SFC list** (2809) that lost **30.95% in 2023**. ICLN fell **61.5%** from Jan 2021
     to Oct 2023.
6. **Sustainability-linked bonds mostly fail.**
   - **80%** of the SLB volume the Climate Bonds Initiative (CBI) has recorded fails its alignment test (US$309.0bn
     not aligned vs US$77.8bn aligned, to H1 2026).
   - The usual penalty is a 25bp coupon step-up.
7. **Recommendation (candidate A): ESG ≈28% of investable assets (HK$2.91M), counted by measured outcome, not
   by label.**
   - The equity core moves to iShares MSCI World CTB Enhanced ESG (EDMW, 0.20%). Its index must, by the EU CTB rule,
     run carbon intensity at least 30% below the parent and cut it about 7% a year.
   - Adrian holds 30% and Carmen 60%, sized by each person's tracking-error budget.
   - Green bonds stay in Carmen's portfolio only (10%). The Sun Life MPF low-carbon fund stays.
   - Fees on the two portfolios fall from about HK$18.2K to **HK$8.5K a year**.
   - The fee price of values is **HK$5.1K a year (0.05% of HK$10.47M)**.
   - The return price is about 0 on the long-run evidence, or up to **HK$26.6K a year** if the last five years repeat.
   - A 25% variant (candidate B: Carmen 45% CTB, 15% plain) gives **24.8%**.

---

## 2. Facts table

### A. The holdings: what exists, what it costs

| Fact | Number | Source (URL, date) | Tag | Conf. |
|---|---|---|---|---|
| BOC-Prudential MSCI World ESG Index Fund (BUM645) is on the SFC ESG list | Best-in-class / positive screening; authorised 02/05/2024; offering-document field `null` | SFC ESG list data file https://www.sfc.hk/-/media/SFC/js/json/esg.json (server last-modified 23 Oct 2026; read 4 Nov 2026) | SOURCED | High |
| Its fund size | **US$0.00M** at every filing, 30 Sep 2024 to 30 Sep 2026 (23 records) | HKEX Integrated Fund Platform, https://ifp.hkex.com.hk/fund-repository/ifp/api/v1/fund/getFundSizeList?fundId=BUM645&page=1&size=30 (opened 4 Nov 2026) | SOURCED | High |
| Control: sibling BOC-Prudential S&P 500 Index Fund (BHG905) | US$67.27M (30 Sep 2026) | same API, fundId=BHG905 (opened 4 Nov 2026) | SOURCED | High |
| BUM645 has no offering document; every sibling has one | SFC register shows no "Offering Documents" link for BUM645 | SFC product list https://apps.sfc.hk/productlistWeb/searchProduct/UTMF.do?lang=EN (4 Nov 2026) | SOURCED | High |
| Series brochure lists 7 sub-funds, none ESG | Principal Brochure 18 Dec 2025 (+ addenda 28 Apr and 22 Jun 2026) | https://ifp.hkex.com.hk/fund-repository/documents/Offering_Documents/66/669b4b83e809ddb1724dd877cf5ace1b0ed3eaccd1bd6819c288fa9ec13a9133 | SOURCED (agent opened) | High |
| Inference: authorised but not launched or offered | Combination of the four rows above | — | ESTIMATED (inference) | High that it is not on sale; medium that it never launched |
| Index the BOC fund tracks; its OCF and fees | Not published. Round One's 0.775% is the series' 2023 Retail Class fee for other sub-funds; the Dec 2025 brochure shows a trustee fee of 0.0875% | Brochure above | UNVERIFIED | — |
| IWDA (iShares Core MSCI World, USD Acc, IE00B4L5Y983) | TER **0.20%**; US$151.4bn; MSCI World (Net); 1,250 holdings | iShares factsheet, 30 Sep 2026, https://www.ishares.com/uk/individual/en/literature/fact-sheet/swda-ishares-core-msci-world-ucits-etf-fund-fact-sheet-en-gb.pdf | SOURCED | High |
| IBTA ($ Treasury 1–3yr) | TER **0.07%**; effective duration 1.85 yrs; yield to worst 4.85% | iShares factsheet, 30 Sep 2026, https://www.ishares.com/uk/individual/en/literature/fact-sheet/ibta-ishares-treasury-bond-1-3yr-ucits-etf-fund-fact-sheet-en-gb.pdf | SOURCED | High |
| AGGU (Core Global Aggregate, **USD hedged, accumulating**) | TER **0.10%**; effective duration 6.02 yrs; yield to worst 4.47%; 19,978 holdings | iShares factsheet, 30 Sep 2026, https://www.ishares.com/uk/individual/en/literature/fact-sheet/aggu-ishares-core-global-aggregate-bond-ucits-etf-fund-fact-sheet-en-gb.pdf | SOURCED | High |
| Global X US Treasury 3–5 Year ETF (**3450** HKD / 9450 USD) | Ongoing charges **0.30%** (single management fee, capped); fund NAV US$48.9M (3 Nov 2026); index duration 3.65 (30 Apr 2026) | https://www.globalxetfs.com.hk/funds/global-x-us-treasury-3-5-year-etf/ ; KFS (ZH) 29 Sep 2025 https://www.hkexnews.hk/listedco/listconews/sehk/2025/0926/2025092600412_c.pdf | SOURCED | High |
| CSOP HKD Money Market ETF (3053) | Ongoing charges **0.31%** (year to 31 Dec 2023); management fee 0.30% | KFS 26 Apr 2024, https://www1.hkexnews.hk/listedco/listconews/sehk/2024/0426/2024042602633.pdf | SOURCED (possibly stale) | Medium |
| Allianz Green Bond: ongoing charges, all HK classes | **1.14%** (all-in fee 1.09% + Luxembourg tax; FY to 30 Sep 2025); subscription **up to 5%**; minimum HK$50,000 | Allianz GI Fund HK KFS, Sept 2026, https://hk.allianzgi.com/documents/hk-agif-kfs-en (Green Bond pages 248–253) | SOURCED | High |
| Allianz Green Bond: mandate | At least 85% in green bonds. Each bond is checked against the four ICMA Green Bond Principles components; projects must be on Allianz GI's list "based on research from the Climate Bonds Initiative". Exclusions include thermal coal >1% of revenue, oil >10%, gas >50%, power generation >100g CO2e/kWh >50% | same KFS | SOURCED | High |
| Allianz Green Bond: shape | EUR 360.18M; 150 holdings; duration 5.95; SFDR Article 9; base EUR. Countries: Italy 11.8%, Netherlands 11.6%, Spain 11.3%, Germany 10.6%, US 8.6%. HK classes: AT (EUR), **AT (H2-USD)**, AM (H2-USD); **no HKD class** | Factsheet 30 Sep 2026, https://hk.allianzgi.com/-/media/allianzgi/ap/hongkong/documents/factsheet/factsheet/2024/07/29/10/11/hk-allianz-green-bond-factsheet-en-202609.pdf | SOURCED | High |
| Allianz Green Bond vs its benchmark (AT EUR, since Jan 2017) | **−11.46% vs −2.49%** cumulative; 5 yrs −18.34% vs −11.91%; 2022 −21.91% vs −18.72% | same factsheet (I read the text extract) | SOURCED | High |
| … annualised | −1.24% vs −0.26% a year over ≈9.7 years: **−0.98 points a year**. Working: (1−0.1146)^(1/9.72)−1 and (1−0.0249)^(1/9.72)−1 | — | ESTIMATED | High (inception date taken from the chart, "01/17") |
| Allianz green bond impact report (avoided tCO2e, MW) | **None found.** The HK fund page lists only the factsheet. The HK annual report has no impact annex for this fund. The Allianz GI 2025 stewardship report mentions an impact report only for a private-markets strategy | https://www.allianzglobalinvestors.de/MDBWS/doc/AllianzGI_Sust_Investing_Stewardship_Report_2025_EN26.pdf (Apr 2026) | UNVERIFIED (absence) | Medium |
| Sun Life MPF Global Low Carbon Index Fund | FER **1.16948%**; management fee "up to 1.02%"; HK$5,933M; launched 5 Jun 2023; risk class 5; returns 2025 19.92%, 2024 13.92% | MPFA fund platform, data 30 Sep 2026, https://mfp.mpfa.org.hk/eng/cf_detail.jsp?cf_id=2065 ; scheme brochure June 2026, https://www.sunlife.com.hk/content/dam/sunlife/regional/hong-kong/documents/pensions/Rainbow_MPF_Scheme_Brochure_E.pdf | SOURCED | High |
| Its index and carbon rule | FTSE Custom MPF Developed Selected Countries ESG Low Carbon Select Hedged Index. At each September rebalance it targets, against its parent: ESG rating +20%, **operational carbon intensity −50%**, fossil-fuel reserve intensity −50%. Industry weights within ±5%. Conventional oil and gas not excluded | Sun Life AM Global Low Carbon Index Fund KFS, Apr 2026, https://ifp.hkex.com.hk/fund-repository/documents/Offering_Documents/ad/ad901291eb8bd956386efc04a74e82e68137e3b1bc737d1f2f6bc29a15350885 ; FTSE ground rules v1.8, Mar 2026, https://www.lseg.com/content/dam/ftse-russell/en_us/documents/ground-rules/ftse-custom-mpf-developed-selected-countries-esg-low-carbon-select-index-ground-rules.pdf | SOURCED | High |
| Its listing status | The MPF fund is on the **MPFA list of MPF ESG constituent funds** (5 in all). Its underlying unit trust (Sun Life AM Global Low Carbon Index Fund) is on the **SFC** list. Round One's wording "underlying fund on the SFC list" is correct | https://www.mpfa.org.hk/en/mpf-investment/sustainable-investing/list-of-mpf-esg-constituent-funds (3 Nov 2026); SFC list above | SOURCED | High |
| MPF fund vs its index | 2025: 19.92 − 21.67 = **−1.75 points**; 2024: 13.92 − 16.03 = −2.11. The 1.17% FER explains most of it | MPFA (fund) vs KFS (index) | ESTIMATED | Medium |
| MPF market fees | Simple mean FER 1.21% (446 rows); cheapest global equity fund 0.81568% (Hang Seng SuperTrust Plus Global Equity). Sun Life ranks 10th cheapest of 26 global equity rows | MPFA export, 30 Sep 2026, https://mfp.mpfa.org.hk/eng/mpp_download_excel.jsp | ESTIMATED (our average of MPFA data; no official average found) | Medium |
| The SFC-authorised retail route to a global ESG index | Sun Life AM Global Low Carbon Index Fund, Class B (retail): management fee 0.99%; OCF 1.095% HKD (estimate, no units in issue), **2.45% USD**; tracking difference 2025 **−3.91%** (USD B) | KFS Apr 2026 above | SOURCED | High |
| MPF Full Portability (affects the Employee Choice Arrangement route) | Phase One from **21 Dec 2026**, only for employees who started or changed jobs **on or after 1 May 2025**; one transfer a year; 2026 window 21–31 Dec | MPFA Chairman's blog, 25 Oct 2026, https://www.mpfa.org.hk/en/info-centre/press-releases/20261025 (opened) | SOURCED | High |

### B. ESG index performance, tracking error and tilts

| Fact | Number | Source | Tag | Conf. |
|---|---|---|---|---|
| Rename | "The MSCI ESG Leaders Indexes were renamed the MSCI Selection Indexes as of Feb 3, 2025." Launched 1 Oct 2007 | MSCI World Selection Index (USD) factsheet, net, 30 Oct 2026, https://www.msci.com/documents/10199/93cd5e86-afeb-496c-9d52-c5ad2f81a691 | SOURCED | High |
| Annualised net USD returns, Selection / World | 1y 12.20/12.11; 3y 21.94/22.28; 5y **10.05/10.49**; 10y 12.96/12.95; since 28 Sep 2007 **7.88/7.85** | same | SOURCED | High |
| Gap, Selection − World | +0.09 / −0.34 / **−0.44** / +0.01 / **+0.03** points a year | — | ESTIMATED | High |
| Calendar-year gaps 2012–2025 | Range −1.43 (2022) to +2.88 (2021); behind in 9 of 14 years; mean −0.01; standard deviation of yearly gaps 1.27 | factsheet calendar returns; our arithmetic | ESTIMATED | High |
| Risk, Selection / World | **Tracking error 1.42%** (window not printed); 3y standard deviation 12.56/11.63; turnover 8.47/3.18 (12 months) | same | SOURCED | High |
| Concentration | 632 vs 1,248 constituents; largest weight 10.06% (NVIDIA) vs 5.65% (Apple); **top 10 = 35.05% vs 26.58%** | Selection factsheet; MSCI World factsheet 30 Oct 2026, https://www.msci.com/documents/10199/178e6643-6ae6-47b9-82be-e1fc565ededb | SOURCED | High |
| Sector tilts, Selection − World (points) | **Energy −1.76** (2.83 vs 4.59); Comm. Services +1.58; Health Care +1.18; Utilities −0.80; IT −0.62; Financials −0.18 | both factsheets | SOURCED weights; ESTIMATED differences | High |
| Apple, Amazon, Broadcom, Meta | Absent from the Selection top 10, though at the index's ≈1.9× scaling of parent weights they would be in it if held | inference from both top-10 tables | ESTIMATED (inference) | Medium |
| Selection method | MSCI ESG rating BB or better; controversy score 3 or above; 50% of free-float cap per GICS sector. Exclusions: controversial and nuclear weapons, tobacco ≥5%, thermal coal and unconventional oil and gas ≥5%, and others. **Conventional oil and gas is not excluded** | MSCI Selection Indexes Methodology, Dec 2025, https://www.msci.com/index/methodology/latest/ESG | SOURCED (agent opened) | High |
| Five-year returns of 0.20% UCITS ETFs (same site, same display currency, dates not printed) | IWDA **+68.70%**; EDMW (CTB) +58.08%; XZW0 (Low Carbon SRI Selection) +61.29%; SUSW (SRI) +47.57% | justETF profiles, fetched 4 Nov 2026: IE00B4L5Y983, IE00BHZPJ569, IE00BZ02LR44, IE00BYX2JD69 | SOURCED, secondary | Medium-low (currency and date unlabelled) |
| … annualised gap vs IWDA | EDMW **−1.43**; XZW0 −0.99; SUSW −2.93 points a year. Working: (1+cum)^(1/5)−1 for each, minus IWDA's 11.03% | — | ESTIMATED | Medium-low |
| … calendar gaps vs IWDA, 2022–25 | EDMW −2.17, −1.05, −0.92, −1.51 (behind every year); SUSW −3.46, +1.05, −8.37, −5.27; XZW0 −3.09, +2.79, +1.09, −1.27; SAWD (Screened) −1.73, +2.46, +1.34, +0.15 | same | ESTIMATED | Medium-low (SAWD's printed 3y and 5y were identical, so I used only its calendar years) |
| EDMW | iShares MSCI World CTB Enhanced ESG UCITS ETF USD (Acc); index MSCI World ESG Enhanced Focus CTB; TER **0.20%**; EUR 4.58bn; physical, optimised; launched 16 Apr 2019 | justETF IE00BHZPJ569 (4 Nov 2026) | SOURCED, secondary | Medium |
| SUSW | TER 0.20%; MSCI World SRI Select Reduced Fossil Fuel; 356 holdings; NVIDIA 9.04%; top 10 32.45%; Article 8 | iShares factsheet 30 Sep 2026, https://www.ishares.com/uk/individual/en/literature/fact-sheet/susw-ishares-msci-world-sri-ucits-etf-fund-fact-sheet-en-gb.pdf | SOURCED | High |
| EU CTB / PAB minimum rules | CTB: GHG intensity (per enterprise value incl. cash, Scope 3 phased in) **≥30% below** the investable universe, and **≥7% a year** self-decarbonisation. PAB: ≥50% below, 7% a year, plus fossil-fuel revenue exclusions (coal ≥1%, oil ≥10%, gas ≥50%, power >100g CO2e/kWh ≥50%) | Commission Delegated Regulation (EU) 2020/1818, https://eur-lex.europa.eu/eli/reg_del/2020/1818/oj (EUR-Lex returned an empty page this session) | **UNVERIFIED** (from memory; re-open before quoting) | Medium-high |
| Theory on green expected returns | "Despite that outperformance, we estimate lower expected returns for green stocks than for brown, consistent with theory." Green outperformance came from unexpected shifts in climate concern | Pástor, Stambaugh & Taylor, "Dissecting Green Returns", NBER WP 28940 (rev. Jun 2022), https://www.nber.org/system/files/working_papers/w28940/w28940.pdf | SOURCED | High |

### C. Greenium

| Fact | Number | Source | Tag | Conf. |
|---|---|---|---|---|
| Zerbib, matched green vs conventional bonds, 2013–17 | **−2bp** | J. Banking & Finance 98:39–60 (2019), https://econpapers.repec.org/RePEc:eee:jbfina:v:98:y:2019:i:c:p:39-60 | SOURCED (abstract) | High |
| Larcker & Watts, US munis from the same issuer on the same day | "essentially zero" | J. Accounting & Economics 69 (2020), https://edwardwatts.netlify.app/publication/larcker_watts_2020_jae | SOURCED | High |
| Flammer, 152 corporate green bonds vs the same issuer's other bonds | −1.9bp, not significant (p = 0.942). Certified green bond issuers then improve: "higher environmental ratings and lower CO2 emissions" | J. Financial Economics 142 (2021), https://www.columbia.edu/~cf2870/PDFs/Corporate-Green-Bonds_Flammer_JFE2021.pdf | SOURCED | High |
| Caramichael & Rapp (Fed), 2014–21 corporates | Average **8bp**; ≈14bp in 2019, 9 in 2020, 8 in 2021; concentrated in large investment-grade banks | Fed IFDP 1346, Jun 2022, https://www.federalreserve.gov/econres/ifdp/the-green-corporate-bond-issuance-premium.htm | SOURCED | High |
| Pietsch & Salakhova (ECB), 124 same-issuer euro pairs | ≈4bp (significant only at 10%); ≈11.9bp from 2020; driven by retail demand | ECB WP 2728, Sep 2022, https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp2728~7baba8097e.en.pdf | SOURCED | High |
| Larger estimates from looser matching | Ehlers & Packer (BIS) ≈18bp (21 bonds at issue); Löffler et al. 15–20bp (cross-issuer matching) | BIS QR Sep 2017, https://www.bis.org/publ/qtrpdf/r_qt1709h.htm ; Eurasian Econ. Rev. 11 (2021), https://ideas.repec.org/a/spr/eurase/v11y2021i1d10.1007_s40822-020-00165-y.html | SOURCED | Medium (method) |
| German twin Bunds | Mostly −7 to −2bp in Sep 2020–Nov 2021 (avg −4.6bp, Pástor et al.); about −1 to −2bp by early 2024 (read off the chart) | NBER w28940; Finanzagentur Green Bond Investor Presentation Jan 2026 p.46, https://www.deutsche-finanzagentur.de/fileadmin/user_upload/Institutionelle-investoren/green/presentations/Green_Bond_Investor_Presentation_2026.pdf | SOURCED (chart read by eye) | Medium |
| It depends on market conditions | Share of green bonds pricing inside their own curve: **61% (H2 2020) → 20% (H1 2022)**. It widens with ESG demand and shrinks in rate shocks | CBI Green Bond Pricing H2 2022, https://www.climatebonds.net/files/documents/publications/Green-Bond-Pricing-in-the-Primary-Market-H2-2022.pdf | SOURCED | High |
| Latest CBI pricing report | **H1 2023** (16th, posted 14 Sep 2023); no later edition found. CBI counts bonds inside their curve and publishes no average greenium in bp; 32% priced on or inside their curve in H1 2023 | https://www.climatebonds.net/files/documents/publications/Green-Bond-Pricing-Paper-H1-2023.pdf | SOURCED | High |
| HK Government green bonds (Jan 2021) | Books 5–7x; CBI "could not build a yield curve", so no greenium was measured | CBI H1 2021, https://www.climatebonds.net/files/documents/publications/Green-Bond-Pricing-in-the-Primary-Market-H1-2021.pdf | SOURCED | High |
| The greenium on the family's money | Carmen's HK$207,000 × 2 / 5 / 10bp = **HK$41 / 104 / 207 a year** | — | ESTIMATED | High |

### D. Measurement

| Fact | Number | Source | Tag | Conf. |
|---|---|---|---|---|
| Green bond ETF issuer carbon | BGRN: WACI **708.64 tCO2e/US$M sales** (82.39% covered); ITR **>3.0°C**; MSCI ESG rating A; TER 0.20% (MSCI data 18 Sep 2026) | iShares BGRN factsheet 30 Sep 2026, https://www.ishares.com/us/literature/fact-sheet/bgrn-ishares-usd-green-bond-etf-fund-fact-sheet-en-us.pdf | SOURCED | High |
| MSCI index factsheets (Oct 2026) | **No** WACI, ITR, SBTi share or taxonomy data on the World, Selection or Select Impact factsheets | factsheets above | SOURCED (absence) | High |
| iShares US factsheet for MSCI World (URTH, 30 Sep 2026) | No MSCI carbon metrics printed (only Morningstar data) | URTH factsheet PDF (I extracted the text) | SOURCED (absence) | High |
| MSCI ITR | Uses NGFS 1.5°C pathways; "enhanced ITR model was implemented by MSCI on February 19, 2024"; iShares shows ITR only in bands | iShares SWDA product page (BlackRock's description), 3 Nov 2026 | SOURCED, secondary | Medium |
| WACI of MSCI World, EDMW, Selection | Not obtained (iShares loads it by script; MSCI blocks automated access) | — | **UNVERIFIED** | — |
| Taxonomy alignment for HK retail funds | None found reporting **HK Taxonomy** alignment; the SFC circular does not require it. HK Taxonomy is voluntary: Phase 1 (May 2024, 12 activities); Phase 2A final Jan 2026 (25 activities, adds transition and adaptation); Phase 2B prototype Sept 2026 | HKMA Insight 8 Sep 2025, https://www.hkma.gov.hk/eng/news-and-media/insight/2025/09/20250908/ ; CBI blog 22 Jan 2026 | SOURCED (absence UNVERIFIED) | Medium |
| EU Taxonomy alignment in Allianz's SFDR periodic report | Article 9 funds report it in an annex; the value for this fund was not read | — | **UNVERIFIED** | — |

### E. Due diligence and anti-greenwashing rules

| Fact | Number | Source | Tag | Conf. |
|---|---|---|---|---|
| SFC ESG funds circular | **29 June 2021** (not 25 June), ref **21EC27**; in force 1 Jan 2022 | https://apps.sfc.hk/edistributionWeb/gateway/EN/circular/products/product-authorization/doc?refNo=21EC27 | SOURCED | High |
| Naming (¶10–12) | Investments "should reflect the particular ESG focus which the fund name represents"; ESG terms "should not overstate or over-emphasize" | same | SOURCED | High |
| Disclosure (¶14) | Includes "the expected or minimum proportion" of ESG-aligned holdings and a reference benchmark. Climate funds: carbon footprint or WACI, and how a climate benchmark differs from a broad index | same | SOURCED | High |
| Annual assessment (¶18–19) | "at least annually": the actual % of ESG-aligned holdings, the % of the universe screened out, engagement and votes | same | SOURCED | High |
| UCITS deeming (¶22) | Funds meeting SFDR Art 8/9 are "deemed to have generally complied in substance" | same | SOURCED | High |
| SFC staff test for best-in-class (workshop slides) | "at least 20% of companies will be removed from the investment universe; OR the portfolio's ESG rating is at least 20% better". Not eligible: "Remove 5-10% worst performing companies" | SFC industry workshop slides, 14 Mar 2023, https://www.sfc.hk/-/media/files/PCIP/FAQ-PDFS/Presentation-Materials-on-industry-workshops-for-ESG-funds_20230314.pdf | SOURCED | High |
| Sanction (¶26–27) | A fund that fails the circular is removed from the list; possible further action | 21EC27 | SOURCED | High |
| ESG ratings and data providers | Voluntary code of conduct launched 29 Nov 2024; SFC circular 24EC58 (25 Nov 2024): managers should do "reasonable due diligence" on third-party ESG providers | SFC 24PR204; 24EC58 | SOURCED | High |
| HK greenwashing enforcement | No SFC, HKMA or HKEX case found; no HK law specifically on greenwashing (law firm view, Jul 2025) | DLA Piper, 16 Jul 2025, https://www.dlapiper.com/insights/publications/2025/07/greenwashing-claims-from-a-global-perspective/hong-kong | SOURCED, secondary; absence UNVERIFIED | Medium |
| HKMA for banks | Due diligence for green products, 9 Dec 2022; sale and distribution of green products, 29 Nov 2023 (mentions "greenwashing, social washing and impact washing"); FAQ of 29 Dec 2025: "Some RIs have yet to establish proper policies… governing the classification framework" | https://brdr.hkma.gov.hk/eng/doc-ldg/docId/20231129-5-EN ; https://brdr.hkma.gov.hk/eng/doc-ldg/docId/getPdf/20251229-1-EN/20251229-1-EN.pdf | SOURCED | High |
| SFC ESG list composition | 179 funds (170 unlisted, 9 ETFs). Strategies: best-in-class 102, thematic 68, other 6, **impact 2**, fund of funds 1 | SFC list data file (23 Oct 2026) | SOURCED (agent counted) | High |
| Not on the SFC list | EDMW, SUSW, IWDA (Irish UCITS ETFs, not SFC-authorised); ICLN/INRG | same | SOURCED | High |

### F. Other instruments

| Fact | Number | Source | Tag | Conf. |
|---|---|---|---|---|
| Personal green deposit (only one found) | Standard Chartered HK **Sustainable Savings Account**: the first HK$200K "will reference qualified green and sustainable activities". Board rate **HKD 0.001%**, USD 0.125% (page "As at 5 June 2026", fetched 4 Nov 2026) | https://www.sc.com/hk/deposits/savings-accounts/sustainable-savings-account/ ; https://www.sc.com/hk/deposits/board-rates/ | SOURCED | High (product), medium (rate date) |
| BOCHK Green Time Deposit | **Corporate customers only** | https://www.bochk.com/en/corporate/ESG/greendeposit.html | SOURCED | High |
| HSBC HK, Hang Seng, DBS HK, Citi HK | No personal green-deposit page found in their sitemaps | site sitemaps, 4 Nov 2026 | SOURCED (absence) | Medium |
| Deposit Protection Scheme | HK$800,000 per depositor per bank since 1 Oct 2024 | https://www.dps.org.hk/en/ | SOURCED | High |
| Government retail green bonds | 2022 issue: HK$20bn, 3 years, minimum 2.5%, matured May 2025. 2023 issue (**4273**): HK$20bn, minimum 4.75%, **matured 12 Oct 2026** (final coupon 4.75%). **No retail green issue in 2024–26.** Recent retail bonds are Silver Bonds (2026: minimum 4.25%, aged 60+) and infrastructure bonds | https://www.hkgb.gov.hk/en/news/sustainbondpress/press_20260925.html ; press index https://www.hkgb.gov.hk/en/news/sustainablebond_press.html | SOURCED | High |
| Tokenised green bonds | Feb 2023 HK$0.8bn; Feb 2024 ≈HK$6bn; Nov 2025 ≈HK$10bn; **29 Sep 2026 ≈HK$20bn** (HKD 2-year 3.80%). Sold to institutions; retail access UNVERIFIED | HKGB press releases 16 Feb 2023, 11 Nov 2025, 29 Sep 2026; HKMA 7 Feb 2024 | SOURCED | High (terms) |
| Thematic clean energy: ICLN | Expense ratio 0.38%; 103 holdings. Calendar NAV returns 2021 −23.80%, 2022 −5.29%, 2023 −20.33%, 2024 −25.78%, 2025 +46.59%; 5-year annualised **−3.39%** (to 30 Sep 2026) | https://www.ishares.com/us/products/239738/ishares-global-clean-energy-etf (4 Nov 2026) | SOURCED | High |
| ICLN drawdown | **−61.5%**, close US$33.41 (7 Jan 2021) to US$12.86 (30 Oct 2023); −68.4% to 8 Apr 2025; still −51.8% on 3 Nov 2026 | Yahoo Finance daily closes; calendar returns match iShares within 0.1 points | SOURCED, secondary; ESTIMATED drawdown | Medium-high |
| 2809 Global X China Clean Energy (**on the SFC ESG list**) | Ongoing charges 0.68%; 35 holdings; 2023 **−30.95%**, 2022 −19.01% (NAV, RMB) | https://www.globalxetfs.com.hk/funds/china-clean-energy-etf/ (3 Nov 2026) | SOURCED | High |
| HK-listed green bond ETF | **3059** Global X Bloomberg MSCI Asia ex Japan Green Bond: 0.40%; AUM **HK$38.44M**; duration 3.21 | https://www.globalxetfs.com.hk/funds/bloomberg-msci-asia-ex-japan-green-bond-etf/ (3 Nov 2026) | SOURCED | High |
| Other green bond index ETFs | BGRN 0.20% (US-domiciled); GRON 0.20% (**EUR, unhedged**, duration 5.99) | iShares factsheets 30 Sep 2026 | SOURCED | High |
| Impact vehicles for HK retail | 2 SFC-listed funds classed "impact": Amundi Funds EM Green Bond; BlackRock BGF US Government Mortgage Impact. No microfinance or social-bond retail fund found | SFC list data file | SOURCED | High |
| SLB alignment (CBI) | Cumulative to H1 2026: US$77.8bn aligned vs US$309.0bn not, so **≈20% aligned**. H1 2026 aligned SLBs US$4.7bn, the "lowest first-half level since H1 2021" | CBI Sustainable Debt State of the Market H1 2026, 8 Sep 2026, https://www.climatebonds.net/files/documents/publications/Climate-Bonds_Sustainable-Debt-State-of-the-Market-H1-2026_8-Sep-2026.pdf | SOURCED | High |
| SLB pricing ignores ambition | Of nine SLBs with curves, "None of them priced inside"; "investors in EUR bonds are not giving preference to aligned deals" | CBI pricing H1 2023 | SOURCED | High |
| SLB penalty | Typical step-up "by 25 basis points" (Enel example) | Baker et al., Annual Review of Financial Economics (2022), https://pages.stern.nyu.edu/~jwurgler/papers/greenbonds_arfe_v6.pdf | SOURCED | High (example); low as a market-wide average |
| ICMA SLB Principles | Targets "beyond a 'Business as Usual' trajectory" | ICMA, Jun 2024, https://www.icmagroup.org/assets/documents/Sustainable-finance/2024-updates/Sustainability-Linked-Bond-Principles-June-2024.pdf | SOURCED | High |

---

## 3. Candidate allocation (each parent HK$2.07M; MPF ESG halves HK$0.835M)

**Counting rule, new.** A holding counts as sustainable only if it passes three tests:
1. **A binding, published outcome rule.** Equity: an index whose carbon intensity must sit at least 30% below its parent (EU CTB or stricter). Bonds: at least 85% use-of-proceeds bonds checked against ICMA.
2. **Measured and reported each year.** WACI and coverage for equity, or an impact report for bonds.
3. **Within the owner's budgets.** Fee gap and tracking error.

"On the SFC list" becomes an entry check for HK-authorised funds, not the test. This matches Annex S item 4(c) in
`area1_6_framework.md`.

**Candidate A (recommended)**

| Holding | Adrian | Carmen | HK$ | Currency | Duration | Liquidity | OCF | HK$ fee a year | Carbon metric |
|---|---|---|---|---|---|---|---|---|---|
| iShares MSCI World CTB Enhanced ESG (EDMW, IE00BHZPJ569) | 30% | 60% | 621K + 1,242K = **1,863K** | USD, unhedged | — | Daily, LSE; fund EUR 4.6bn | 0.20% | 3,726 | By rule: intensity ≥30% below MSCI World, −7% a year (UNVERIFIED rule text). Measured WACI UNVERIFIED |
| iShares Core MSCI World (IWDA) | 10% | — | 207K | USD | — | Daily, LSE | 0.20% | 414 | Parent; WACI UNVERIFIED |
| US Treasury notes 2037–41 | 20% | — | 414K | USD | Ladder | Held to maturity; tradable | 0 | 0 | Sovereign: not comparable with corporate WACI |
| IBTA | 10% | — | 207K | USD | 1.85 | Daily | 0.07% | 145 | Sovereign |
| Global X US Treasury 3–5 Year ETF (3450) | — | 5% | 103.5K | HKD counter | ≈3.65 (index) | Daily, HKEX; fund US$49M | 0.30% | 311 | Sovereign |
| AGGU (USD hedged) | 25% | 20% | 517.5K + 414K = 931.5K | USD hedged | 6.02 | Daily | 0.10% | 932 | Mixed; not reported |
| Allianz Green Bond AT (H2-USD) | — | 10% | 207K | EUR base, USD hedged | 5.95 | Daily NAV; minimum HK$50K | 1.14% (+ subscription up to 5%: negotiate to 0) | 2,360 | Measure by financed projects; impact report UNVERIFIED. Issuer WACI misleads (BGRN: 708.64, >3.0°C) |
| CSOP HKD Money Market ETF (3053) | 5% | 5% | 207K | HKD | Very short | Daily | 0.31% | 642 | — |
| **Portfolio** | **40/60** | **60/40** | 4,140K | | | | Adrian 0.128%, Carmen 0.285% | **8,528** | Listed equity 90% CTB, so carbon intensity **≥27% below** an all-IWDA equity book by rule (ESTIMATED: 1 − 0.30 × 0.90) |
| Sun Life MPF Global Low Carbon Index Fund (half of each MPF) | ½ MPF | ½ MPF | 835K | HKD (hedged index) | — | Locked until retirement; switchable yearly | FER 1.169% | 9,765 | By rule: operational carbon intensity −50% vs FTSE parent; measured UNVERIFIED |

- **Family ESG:** 1,863 + 207 + 835 = **HK$2.905M = 27.7% of HK$10.47M**. Round One was HK$2.636M, 25.2%.
- **Candidate B (keeps ≈25%):** Carmen holds EDMW 45% and IWDA 15%; the rest as A. ESG = 1,552.5 + 207 + 835 =
  **HK$2.595M = 24.8%**. Fees are identical, because EDMW and IWDA both charge 0.20%.

**Why each parent's CTB weight is what it is** (ILLUSTRATIVE budgets, ESTIMATED arithmetic).
- Use the Selection index's 1.42% tracking error as the proxy for the ESG sleeve.
- **Carmen** (values high; area 1/6 budget ≤3% a year): 60% × 1.42 = 0.85%, well inside. All her equity goes ESG.
- **Adrian** (prudent): with a portfolio tracking-error budget of 0.5% a year (our proposal), the cap is 0.5 / 1.42 ≈
  35%. We use 30%, three quarters of his equity: 30% × 1.42 = 0.43%.
- **The point:** the ESG share is an output of each person's budgets, not a target typed in. That is why it lands at
  27.7% rather than 25%.

**What changed from Round One, and why**

| Change | From → to | Why (number) |
|---|---|---|
| ESG equity core | BOC-Prudential MSCI World ESG Index Fund (35% / 37%) → EDMW (30% / 60%) | BOC fund: US$0.00M size, no offering document, not on sale. EDMW: 0.20% = IWDA's fee, with a binding carbon rule. Removes a possible 5% initial charge (≈HK$74.5K once on HK$1.49M) |
| Adrian's green bonds | Allianz 5% → AGGU (+5%) | Fails the 5bp cost test for shared or prudent money: 1.04-point fee gap vs a 0–8bp greenium. Saves HK$1,076 a year and up to HK$5,175 one-off |
| Carmen's plain equity | IWDA 23% → 0% (candidate B keeps 15%) | No fee cost, and inside her tracking-error budget |
| Counting rule | "On the SFC ESG list" → measured outcome rule | The label let an unbuyable fund carry 56% of our ESG total, and puts a −31%-in-a-year clean-energy ETF (2809) on the same list |
| Measurement | None → each year: equity WACI vs parent with coverage, green bond impact per HK$1M, MPF fund's carbon vs parent | Brief area 3, bullet 3 |
| Unchanged | Sun Life MPF fund; Allianz for Carmen; bond ladder; IBTA, AGGU, 3450, 3053 | MPF FER 1.17% is below the MPF mean (1.21%); carbon rule −50% |

Fees, both portfolios: Round One HK$18,175 a year (with the BOC fund at the unverified 0.775%) → **HK$8,528**. The
saving, ≈HK$9.6K a year, comes mostly from the wrapper, not from ESG.

---

## 4. The price of values (against an all-plain twin: EDMW → IWDA, Allianz → AGGU, Sun Life MPF → cheapest MPF global equity fund)

**Return: fees.**
- EDMW vs IWDA: 0.20% − 0.20% = **HK$0**.
- Allianz vs AGGU: 207,000 × (1.14% − 0.10%) = **HK$2,153**.
- Sun Life MPF vs the cheapest MPF global equity fund: 835,000 × (1.169% − 0.816%) = **HK$2,954**. Against the MPF
  simple mean (1.21%) it **saves HK$339**.
- **Total HK$5,107 a year = 0.049 points of HK$10.47M** (ESTIMATED). Over 20 years at 4%, ≈HK$152K (ILLUSTRATIVE).

**Return: tracking.** Three readings of the same HK$1.863M CTB sleeve (ESTIMATED):
- **Long-run evidence:** best-in-class vs parent +0.03 points a year, 2007–2026 (MSCI, live data). Expected cost ≈
  **HK$0**. This is the "evidence that it need not give up much".
- **Typical year (one standard deviation):** 1.42% × 1,863,000 ≈ **±HK$26.5K** relative to the plain twin, in either
  direction.
- **If the last five years repeat:** EDMW −1.43 points a year × 1,863,000 = **HK$26.6K a year = 0.25 points of
  investable assets**. Adrian's share is 621,000 × 1.43% = HK$8.9K; Carmen's is 1,242,000 × 1.43% = HK$17.8K.
  Candidate B: HK$22.2K.
- **Green bond yield given up (greenium):** 207,000 × 2–10bp = **HK$41–207 a year**.

**Diversification.**
- The best-in-class index holds about half the parent's names (632 vs 1,248). Its top 10 is 35.05% vs 26.58%, and
  NVIDIA is 10.06% vs 5.25%.
- Energy is 1.76 points lower, and Apple, Amazon, Broadcom and Meta appear to be out.
- EDMW's holding count and concentration are UNVERIFIED; check them on its factsheet.
- The green bond sleeve is 150 bonds, mostly euro-area issuers (Italy, Netherlands, Spain, Germany ≈45%). That adds
  euro rate and credit exposure the rest of the book lacks.
- **Price: concentration, not fewer sectors.**

**Liquidity.**
- **None given up.** Every listed holding deals daily; the MPF lock is the same with or without ESG.
- We refuse the illiquid options (impact vehicles; tokenised green bonds, which retail can't access).

**Who pays.**
- Carmen's portfolio carries HK$2,360 of the HK$5,107 fee price, plus the larger tracking exposure.
- Adrian's carries only his MPF switch (≈HK$1.9K of the HK$2,954, pro rata to his HK$525K MPF half) and a small
  tracking exposure.
- Separate sleeves decide who pays; the cheaper wrapper lowers what is paid.

**The deck line (proposal):** "Values cost this family HK$5K a year in fees: 0.05% of what they invest. The real price is
tracking: in a bad five years, about HK$27K a year. We set it, cap it, and review it."

---

## 5. Refusals and trade-offs

**Refusals, each with its number.**
1. **Thematic clean-energy funds.**
   - ICLN fell **61.5%** (Jan 2021 to Oct 2023) and **68.4%** at the Apr 2025 low; its 5-year annualised return is
     −3.39%.
   - 2809, which is *on the SFC ESG list*, lost **30.95% in 2023**.
   - A sector bet with a green label. Carmen's belief in sustainability trends is already expressed through her
     business (her human capital and income), which is concentration enough.
2. **A fund because it is on the list.** The BOC-Prudential ESG fund: US$0.00M in every filing since Sep 2024 (23
   monthly records), no offering document.
   We check that a product exists, its size, its documents and its tracking before its label.
3. **Sustainability-linked bonds as a "sustainable" holding.** About 80% of cumulative SLB volume fails CBI alignment;
   pricing ignores ambition; the typical penalty is a 25bp step-up. We treat them as ordinary credit.
4. **Green deposits for the reserve.** SC's account pays HKD 0.001% on a HK$200K "sustainable balance".
   - The money references the bank's existing green loan book, so there is no visible additionality.
   - Interest given up: HK$200K × the HKD time-deposit rate. At an illustrative 2–3%, that is HK$4–6K a year
     (ILLUSTRATIVE: today's rate not checked).
5. **Cheap green bond ETFs that change the risk.**
   - GRON is EUR and unhedged, so it adds currency risk to a bond sleeve.
   - BGRN is US-domiciled, so US estate-tax exposure; that rule is known but was not re-checked this session.
   - 3059 is HK$38M and Asia ex Japan only: closure risk, and more home-region exposure.
6. **Claiming impact for listed equity.** A lower WACI measures what we hold, not what we changed. Avoided emissions are
   reported only for use-of-proceeds bonds, separately, never netted against the footprint.

**Trade-offs we accept.**
- **T1. Carbon rule vs tracking.** The CTB sleeve has a binding carbon cut. Over the last five years it lagged by
  1.43 points a year (≈HK$26.6K a year on candidate A), against ≈0 for the best-in-class index over 19 years.
  **Review trigger (ILLUSTRATIVE):** if the CTB sleeve trails IWDA by more than its budget over rolling 3 years
  (Adrian 0.5 points at portfolio level; Carmen 3 points), the owner re-decides at the annual meeting.
- **T2. Active green bond fee vs verification.** HK$2,153 a year buys bond-by-bond ICMA and CBI-list checks and an
  Article 9 mandate.
  - It has not bought return: −0.98 points a year against its benchmark since 2017.
  - Conditions: subscription charge waived; the manager supplies an impact report (tCO2e avoided per million
    invested, and its method). Otherwise Carmen's 10% moves to AGGU at the next review, and the family ESG share
    falls to 25.8% under candidate A ((2.905 − 0.207) / 10.47).
- **T3. MPF low-carbon fund vs the cheapest MPF global equity fund.** It costs HK$2,954 a year, buys a −50% carbon
  rule, and is cheaper than the average MPF fund.

---

## 6. Likely judge questions (short answers for Win)

1. **"Have you checked your ESG fund exists?"**
   - Yes. The fund we named in Round One shows US$0.00M in every HKEX filing for two years and has no offering
     document. It is on the SFC list, but you cannot buy it.
   - That is our case for measuring before labelling. We replaced it with a fund we can buy, priced at the plain
     index's fee.
2. **"Why a fund the SFC hasn't authorised?"**
   - Hong Kong's only two global ESG equity index funds on the SFC list are that unlaunched fund and a Sun Life unit
     trust. Its retail class costs 2.45% (USD) and trailed its index by 3.91 points in 2025.
   - Round One already holds Irish UCITS ETFs (IWDA, IBTA, AGGU) for estate-tax and withholding reasons.
   - Under SFC ¶22, SFDR Art 8/9 UCITS are "deemed" compliant in substance for SFC-authorised funds. EDMW itself is
     not authorised here, so suitability is done case by case through a licensed broker (see §7).
3. **"What does ESG cost the client?"** HK$5.1K a year in fees (0.05% of investable assets). Tracking is ≈0 over 19
   years of the best-in-class index, but up to ≈HK$27K a year in a bad five years. We cap tracking per person and
   review it.
4. **"Isn't a lower WACI just moving shares between owners?"**
   - Yes: it measures exposure, not real-world change. We report it as footprint.
   - Real change comes from use of proceeds: certified green bond issuers cut CO2 after issuance (Flammer 2021).
   - Above all, it comes from Carmen's own business (area 2), where the family's emissions actually are.
5. **"The greenium is 2bp. Why pay 104bp?"** We don't pay for the greenium. Carmen pays HK$2.2K a year for verified
   use of proceeds, on two conditions (T2). Adrian doesn't pay it.
6. **"ESG Leaders, Selection: which index is it?"** MSCI renamed ESG Leaders as Selection on 3 Feb 2025. It keeps the
   top half of each sector by ESG rating (BB or better, controversy score 3 or above). It does not exclude
   conventional oil and gas, and has no carbon target. That is why we moved to a CTB index with a binding cut.
7. **"Why not thematic clean energy? It fits Carmen's values."** ICLN −61.5% peak to trough; 2809 −31% in 2023 while
   on the SFC list. It is a sector bet, and her income is already in the sector.
8. **"Sustainability-linked bonds?"** 80% of their volume fails CBI alignment, and markets don't price ambition. We
   hold none on purpose and treat any in a fund as ordinary credit.
9. **"What is implied temperature rise and would you show it?"**
   - It is a model output (MSCI, enhanced Feb 2024, NGFS 1.5°C pathways), shown in bands. We report the band, never
     a target.
   - A green bond ETF can read above 3°C because it scores issuers, not projects.
10. **"What happens to the 28% when the MPF buys annuities (2037, 2039)?"**
    - The MPF halves (HK$0.835M) become HKMC annuities, so the ESG share falls by about 8 points.
    - The IPS measures the share on the investment portfolios from then on. The CTB core continues.
11. **"Taxonomy alignment?"** No HK retail fund reports HK Taxonomy alignment, which is voluntary (Phase 2A final
    Jan 2026). For Allianz we would read the EU Taxonomy share from its SFDR periodic report (not yet read).
12. **"Greenwashing rules in HK?"** The SFC circular 21EC27 (29 Jun 2021) sets naming, disclosure and annual
    assessment rules. HKMA guidance covers banks' sale of green products. We found no HK greenwashing enforcement
    case.
13. **"BlackRock runs your core. Doesn't its stewardship matter?"** The index rule, not the manager's pledge, sets the
    carbon cut. We review votes once a year. (Any claim about BlackRock leaving net-zero alliances is UNVERIFIED;
    don't raise it.)

---

## 7. Open items and what is unverified

**Before 16 Nov (owner Win unless stated)**
1. **Call BOCI-Prudential** (hotline in its 22 Jun 2026 notice: (852) 2280 8615). Is the MSCI World ESG Index Fund
   launched, and is it on sale? If yes: its index, OCF, class, and a channel without the initial charge. Until then,
   say "not on sale (HKEX data, 30 Sep 2026)".
2. **EDMW from iShares primary documents.** I have only justETF (secondary): the factsheet and KIID, the index
   methodology (MSCI World ESG Enhanced Focus CTB), holdings count, top 10, and the LSE ticker and trading currency.
   Also the WACI and ITR shown on the iShares product page (it loads by script: open it in a browser). Same for
   IWDA/SWDA, to get a **measured** WACI pair.
3. **Re-pull the five-year and calendar returns** for EDMW, SUSW, XZW0, SAWD and IWDA from iShares or Xtrackers
   factsheets in USD with a date. The justETF figures carry no currency or date label. All five came from the same
   site, so the comparison holds, but the levels need dating.
4. **EU Delegated Regulation 2020/1818**: confirm the CTB and PAB thresholds (30% / 50%, 7% a year, PAB exclusions)
   from the official text. EUR-Lex returned empty pages here.
5. **Allianz Green Bond**: ask Allianz GI for the fund's impact report and its SFDR periodic report (EU Taxonomy
   share; avoided tCO2e per €1M), and for any channel waiving the 5% subscription.
6. **Suitability and channel for a UCITS ETF bought by HK retail**: complex or non-complex classification under the
   SFC Code of Conduct, and broker access to the LSE. UNVERIFIED; Round One relies on the same for IWDA.
7. **Sun Life fund's measured carbon intensity vs its parent** (annual ESG periodic assessment; not found online).

**Unverified or weak in this brief**
- WACI of MSCI World, the Selection index and EDMW: none obtained. Carbon figures above are **rule-based**, not measured.
- The tracking-error window on the MSCI factsheet (1.42%) is not printed.
- Greenium papers not opened this session: Kölbel & Lambillon, and Berrada et al. on SLBs; a Dec 2025 meta-analysis
  claiming −12.44bp (snippet only, low quality); the ABN AMRO 2025 estimate (snippet).
- Whether retail can buy the tokenised government green bonds.
- The 3053 ongoing charge is from Apr 2024.
- Round One arithmetic: 0.72 × 2.07M = 1.4904M, but the manuscript notes use 1.4876M (each parent ≈HK$2.066M). Pick
  one before quoting HK$ figures.
- SFC ESG fund counts and AUM over time (204 in Jun 2025 → 179 now; US$153.7bn) come only from secondary news (Tiger,
  24 Aug 2026). Don't quote them without the FSTB source.
- EU fund-name rules (ESMA guidelines on funds' names with ESG terms, May 2024: an 80% threshold, and PAB or CTB
  exclusions by term) are from memory; the ESMA page returned no text. Confirm before using them as a naming test.
- The MPF Full Portability Phase One covers only those who joined or changed jobs from 1 May 2025, so it probably
  doesn't help Adrian. The Employee Choice Arrangement route in Round One stands.

**Research files** (local only, not for the repo): scratchpad folders `esgidx_*`, `dl/me`, `agentESG/d`, `pdfs` in
this session's scratchpad.
