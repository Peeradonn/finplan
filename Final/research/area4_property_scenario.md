# Area 4 and the scenario: the flat, the warehouse, physical risk, the scenario and the risk register

**For:** Lookbua (presents slides 11–12 and answers questions on them). **Written:** 4 Nov 2026, from primary
sources checked that day, five research passes and exploratory model runs. **Status:** research brief, not deck
copy. A number goes on a slide only after the checks in §8.

**Correction (5 Nov, `hook_fact_checks.md`, primary sources):** green mortgage rebates on HK$1.8M are HK$0–3K, not HK$0–4K; Standard Chartered and HSBC exclude refinancing; HKMC also accepts a flat-level BEAM Plus Interiors certificate. Quote those, not the figures below.

**Tags used.** SOURCED: a named source says it. ESTIMATED: our arithmetic on sourced inputs, working shown.
ILLUSTRATIVE: our assumption, because the case doesn't give it. EXPLORATORY: a run of the Round One model
(`model/run_model.py`) from a scratch script, not yet in `export_numbers()`. On a slide, EXPLORATORY numbers become
`{{keys}}` (Final_Plan §3).

**Facts we define (ILLUSTRATIVE, say so on screen).**

- *The flat:* a high-floor unit in a private multi-storey building in Tai Kok Tsui, completed **1996**, so 30 years
  old now, 41 in 2037 and 50 in 2046. About 900 sq ft saleable, not BEAM Plus certified. The owners' corporation (OC)
  owns the roof and the common parts. The age is the one we were asked to test. **§3.4 gives the rule for any age.**
- *The warehouse:* a placeholder until Fahtai's business facts arrive (Fri 6 Nov). About 3,000 sq ft on an upper floor
  of a Kwai Chung industrial building, CLP supply. A 3-year lease, the tenant paying its own CLP bill. The roof belongs
  to the landlord or the OC.

---

## 1. Bottom line for Lookbua

1. **We would not take a green mortgage, and the reason is a number.**
   - Every Hong Kong bank product we found needs the whole building rated BEAM Plus New Buildings or Existing
     Buildings Gold or Platinum. HSBC's covers designated first-hand flats only.
   - Banks pay a one-off rebate, not a lower rate. The Consumer Council found green mortgage rates "basically no
     different" (17 Apr 2023).
   - On HK$1.8M the rebate is HK$0 to about HK$4K. BEA pays nothing below HK$2M. A 0.10% rate cut, if one existed,
     would save about HK$11K over the 11 years until we clear the loan in 2037 (ESTIMATED).
2. **A retrofit of the flat is housekeeping, not wealth.**
   - Grade 1 inverter air-conditioners, LED lighting and window film together save about **HK$1,900 a year**, about
     0.25% of the HK$780K budget (ESTIMATED).
   - Replacing working air-conditioners pays back in 9–15 years. Buy the best Grade 1 model when one fails.
   - Solar is impossible on one flat in a multi-storey building, because the roof is a common part.
3. **Tai Kok Tsui is on no official flood or storm-surge list,** and heat is a present risk, not a future one.
   - CEDD's study of 26 coastal areas at risk to 2050 doesn't include Tai Kok Tsui. Nor do DSD's flooding blackspots,
     HKO's flooded-area lists for Mangkhut and Hato, or the government's Ragasa warning list.
   - Very hot days: a baseline of 14 a year (1995–2014). There were 52 in 2024 and 53 in 2025 (HKO).
   - What reaches the family's money is building-level damage, paid through OC levies, and insurance. A sourced
     price hit for Tai Kok Tsui doesn't exist.
4. **The climate lens changes *how* they leave the flat.** A discount on old buildings costs downsizing about five
   times what it costs the reverse mortgage.
   - If the old flat is worth 10% less in 2037 and newer flats are not:
     - downsizing releases about 30% less, and the plan loses about 6 points (83.1% → 76.9%);
     - the reverse mortgage pays about 6% less, and the plan loses about 1.4 points (82.6% → 81.2%).
   - The reason is HKMC's valuation rule: it counts only 50% of the value above HK$8M (EXPLORATORY; ESTIMATED).
   - The reverse mortgage is the climate hedge. Downsizing still leaves the larger legacy (`{{legacy_down}}` vs
     `{{legacy_rmp}}`).
5. **The climate lens sets *when*: release the flat by the year the building turns 50.** For our illustrative 1996
   building that is 2045 at the latest.
   - Above 50, HKMC's reverse mortgage is "case-by-case" (SOURCED).
   - A buyer's HKMC-insured loan must satisfy age of the building + remaining term ≤ 75 years (SOURCED).
   - **Correction for Round One:** "delay to 2045 → `{{rmp2045_89}}`" kept the 2037 payout of HK$230K. HKMC pays about
     36% more per HK$1M at entry age 68.
   - With that payout, delaying costs about 2 points (80.7%), not 9 (EXPLORATORY). The case against waiting is the
     age cliff and the old-building drag, not the odds.
6. **One scenario, "late and sudden", run through the model.** A disorderly transition in 2030–31 takes the full plan
   from 82.6% to **66.7%** (−16 points, EXPLORATORY). The losses split as follows:
   - Portfolio: −10 points, of which equity −4.4, inflation −3.6 and bonds −1.3 when each runs alone.
   - Business: −2.7 points.
   - Flat: −2.2 points, through a smaller reverse mortgage.
   - The portfolio loss is ordinary market and inflation risk. The 25% ESG label doesn't change it.
   - The plan's guaranteed income is fixed in HK$ (annuities, a level reverse mortgage), so a transition inflation
     shock hurts it.
7. **The warehouse is a split-incentive textbook case.**
   - LED is the tenant's own win: about HK$8.7K a year, paid back in about 1.3 years (ESTIMATED, illustrative unit).
     Do it whatever the lease says.
   - Rooftop solar earns the feed-in tariff of HK$3–4/kWh for the roof owner, and only until 2033.
   - A green lease is the tool: a reinstatement waiver, shared data, cost recovery capped at the measured savings, and
     a renewal option to 2039.
   - Its real value is a secure lease for the 2035–39 sale, not the kWh.

---

## 2. Facts table

Accessed 4 Nov 2026 unless dated otherwise. "P" means a primary source; "S" means secondary.

### Green mortgages and HKMC

| Fact | Number | Source (URL, date) | Tag | Conf. |
|---|---|---|---|---|
| Banks listed by HKGBC as offering green mortgage plans; HKGBC "has no direct or indirect involvement" | BOCHK, BoCom HK, BEA, Citi, DBS, Hang Seng, HSBC, HKMC, Public Bank, Standard Chartered | P: https://www.hkgbc.org.hk/eng/beam-plus/incentive-funding/green-mortgage.jsp | SOURCED | High |
| BEA Green Mortgage Plan: BEAM Plus NB or EB Platinum/Gold (provisional or final); new mortgage or refinancing | Rebate HK$1K (≥HK$2M), HK$2K (≥HK$3M), HK$3K (≥HK$5M); minimum loan HK$1M; to 31 Dec 2026 | P: https://www.hkbea.com/html/en/Green_Mortgage.html | SOURCED | High |
| Standard Chartered Green Mortgage: NB/EB Gold/Platinum | HK$888 (HK$1M–4.99M) or HK$1,888 (≥HK$5M); deposit-linked cap 60% for 3 years; applications closed 30 Jun 2026 | P: https://www.sc.com/hk/mortgages/home-property-loans/green-mortgage-environment-esg/ (factsheet 10/2025) | SOURCED | Medium |
| HSBC Green Mortgage: first-hand flats on its "designated" list, Platinum/Gold | 2022 launch: HK$3,988 (HK$1M–<4M), HK$6,888 (≥HK$4M); amount not stated now | P: https://www.hsbc.com.hk/mortgages/products/home-loans/green/ ; launch 5 May 2022 https://www.about.hsbc.com.hk/-/media/hong-kong/en/news-and-media/220505-hsbc-introduces-green-mortgage-for-building-a-greener-future-en.pdf | SOURCED | Medium |
| DBS Green Mortgage (2022) | Extra rebate of 0.1% (Treasures) or 0.05% (retail) | P: https://www.dbs.com/newsroom/DBSHK_GreenMortgage_EN (7 Jul 2022) | SOURCED (dated) | Medium |
| Consumer Council survey: 10 of 20 banks offered green mortgages; rates "basically no different"; top rebates HK$6,888–12,000; 194 Platinum/Gold residential projects | 0.11–0.2% of a HK$6M loan | P: https://www.consumer.org.hk/en/press-release/p-558-green-mortgage (17 Apr 2023) | SOURCED | High |
| HKMC Green Promotion, 17 Mar–31 Dec 2026. Eligible: NB Platinum/Gold, EB Comprehensive Platinum/Gold (final), **or BEAM Plus Interiors (Residential) Green+/Green** | RMP: HK$3K or 0.1% of value, capped at HK$8K; MIP: HK$3K/5K; Fixed Rate Mortgage Scheme: HK$1K/3K | P: https://www.info.gov.hk/gia/general/202603/09/P2026030900310.htm (9 Mar 2026) | SOURCED | High |
| Same release: RMP fixed rate cut from 4.5% to **4%** for 30 years; payouts up by as much as 5%; funded by HK$2bn of 30-year social bonds (Nov 2025) | Single borrower, life, per HK$1M: age 60 HK$2,020; age 70 HK$3,070 | P: as above | SOURCED | High |
| HKMC sustainable financing framework: no HKMC green bond or green MBS found (social bonds only) | — | P: https://www.hkmc.com.hk/eng/investor_relations/sustainable_finance.html (updated Aug 2025) | SOURCED (absence) | Medium |
| HKMA Sustainable Finance Action Agenda doesn't mention mortgages or buildings | — | P: https://www.hkma.gov.hk/eng/news-and-media/press-releases/2024/10/20241021-4/ (21 Oct 2024) | SOURCED | High |
| Take-up of green mortgages in Hong Kong | none published | — | UNVERIFIED | — |

### BEAM Plus and BEEO

| Fact | Number | Source (URL, date) | Tag | Conf. |
|---|---|---|---|---|
| BEAM Plus Interiors – Residential certifies a flat's fit-out, existing homes included; ratings Green+ (45 items) and Green (30); valid 5 years | Fees from 1 Apr 2026: registration HK$110 + assessment HK$500 (≤100 m²) or HK$1,000 | P: https://www.hkgbc.org.hk/eng/beam-plus/beam-plus-interiors/index_2_0_r.jsp ; fee scale https://hkgbc.org.hk/eng/beam-plus/beam-plus-references/fee/fee.jsp | SOURCED | High |
| Interiors, non-residential (e.g. warehouse fit-out) | Registration HK$1,210 + HK$13K (≤100 m²), HK$17K (101–300 m²) or HK$22K (301–600 m²) per floor | P: fee scale, as above | SOURCED | High |
| EB v2.0 runs to 6 Jul 2026; v3.0 launched Jul 2025; EB Comprehensive is a whole-building (OC) application | Registration HK$11,880; assessment from HK$110K (≤2,499 m²) | P: HKGBC EB pages, fee scale v4.0 | SOURCED | Medium (PDF columns jumbled) |
| Price premium, BEAM Plus certified flats: Hui, Tse & Yu (2017), *Int. J. Strategic Property Management* 21(4):384–400 | **+4.4%** (up to +6.2%); "unclassified" −5.9%; 646 sales in 16 developments, Sham Shui Po–Cheung Sha Wan, Feb 2012–Dec 2014 | P (journal): doi:10.3846/1648715X.2017.1409290 | SOURCED | Medium: one district, new buildings, data 12 years old |
| Earlier studies (cited by Hui et al.; not read) | HK-BEAM +3.4–6.4% (Jayantha & Man 2013); Singapore Green Mark Platinum +11%, Gold +5% (Deng & Wu 2014) | S | SOURCED (secondary) | Medium |
| Buildings Energy Efficiency (Amendment) Ordinance 2025: gazetted 20 Jun 2025; Stage 2 in force **20 Sep 2026** | Energy audits every **5 years** (was 10), for 11 building types (was 2); residential and industrial buildings covered only in common areas; no audit duty for flats or ordinary warehouses | P: https://www.emsd.gov.hk/beeo/en/mibec_beeo.html ; https://www.info.gov.hk/gia/general/202506/18/P2025061700263.htm (18 Jun 2025) | SOURCED | High |
| Climate Action Plan 2050: cut electricity use against 2015 | Commercial −15–20% by 2035, −30–40% by 2050; residential −10–15% and −20–30%; buildings ≈90% of electricity | P: https://www.cnsd.gov.hk/wp-content/uploads/pdf/CAP2050_booklet_en.pdf (Oct 2021) | SOURCED | High |

### Energy prices and retrofit inputs

| Fact | Number | Source (URL, date) | Tag | Conf. |
|---|---|---|---|---|
| CLP 2026 average net tariff | **140.6 ¢/kWh** (−2.6%); basic 101.2 ¢; fuel cost adjustment 39.4 ¢ (Jan 2026) | P: CLP press release, 18 Nov 2025, https://www.clpgroup.com/content/dam/clp-group/channels/media/document/2025/20251118_en.pdf.coredownload.pdf ; government release https://www.info.gov.hk/gia/general/202511/18/P2025111800787.htm | SOURCED | High |
| CLP fuel cost adjustment, November 2026 | 47.4 ¢ (so ≈148.6 ¢ all-in, before rebates) | S: Dim Sum Daily, 26 Oct 2026 | SOURCED (secondary) | Medium |
| CLP 2026 residential block rates; non-residential tariff | — | CLP tariff table (site blocks automated fetches) | UNVERIFIED | — |
| Feed-in tariff, new applications since 27 Apr 2022 | HK$4/kWh (≤10 kW), HK$3 (10–200 kW), HK$2.5 (200 kW–1 MW); runs to the end of the Scheme of Control, **31 Dec 2033**; extension "slim" | P: https://www.info.gov.hk/gia/general/202204/26/P2022042600448.htm ; LCQ2 https://www.info.gov.hk/gia/general/202411/20/P2024112000328.htm (20 Nov 2024) | SOURCED | High |
| Solar yield and cost in Hong Kong (PolyU for EMSD) | ≈1,107 kWh per kWp a year; HK$29.2/Wp (2019 estimate) | P: https://re.emsd.gov.hk/files/Actual_Performances_of_PV_Panels_in_the_Local_Environment.pdf (Jan 2020) | SOURCED / ESTIMATED | Medium (cost dated) |
| Private housing electricity by end use, 2023 | Air-conditioning 39.5%; hot water 10.0%; refrigeration 8.9%; lighting 6.3% | P: EMSD Hong Kong Energy End-use Data 2025, https://www.emsd.gov.hk/filemanager/en/content_762/HKEEUD2025.pdf | SOURCED (shares are our division) | High |
| New air-conditioners registered in 2023 vs 2013 | ≈45% less electricity | P: as above | SOURCED | High |
| Consumer Council test, 1.5 HP inverter split units, all Grade 1 | Price HK$4,890–7,880 (cooling only); running cost HK$679–1,022 a year; best uses up to 33% less than worst | P: https://www.consumer.org.hk/en/press-release/p-595-1-5hp-split-type-air-conditioners (14 May 2026) | SOURCED | High |
| Typical 3-person household | 275 kWh a month | P: government release, 18 Nov 2025 | SOURCED | High |
| Profits tax: environmental protection installations | 100% deductible in year 1 (since YA 2018/19) | P: https://www.ird.gov.hk/eng/tax/bus_pft.htm | SOURCED; whether LED qualifies is UNVERIFIED | High / — |
| CLP 2026 SME equipment subsidy | HK$40M pool; HK$7M for free retro-commissioning; cap per customer UNVERIFIED | P: CLP release, 18 Nov 2025 | SOURCED | Medium |

### Physical climate risk

| Fact | Number | Source (URL, date) | Tag | Conf. |
|---|---|---|---|---|
| Very hot days (≥33 °C), baseline 1995–2014 | 14 a year; projected 54 (2021–40), 65 (2041–60), 95 (2081–2100) under SSP2-4.5; 152 by 2081–2100 under SSP5-8.5 | P: https://www.hko.gov.hk/en/climate_change/proj_hk_annual_vhot_days_info.htm | SOURCED | High |
| Hot nights (≥28 °C) | Baseline 21; 63 (2021–40), 87 (2041–60) under SSP2-4.5 | P: https://www.hko.gov.hk/en/climate_change/proj_hk_annual_hot_nights_info.htm | SOURCED | High |
| 2024: warmest year on record | 24.8 °C; 52 very hot days; 50 hot nights | P: https://www.hko.gov.hk/en/wxinfo/pastwx/2024/ywx2024.htm | SOURCED | High |
| 2025 | 24.3 °C (6th warmest); 53 very hot days, 54 hot nights (both 3rd highest); 5 Black Rainstorms (record); 14 cyclone signals (most since 1946); two No. 10 signals (Wipha 20 Jul, Ragasa 24 Sep); Ragasa raised Quarry Bay to 3.4 mCD | P: https://www.hko.gov.hk/en/wxinfo/pastwx/2025/ywx2025.htm (8 Jan 2026) | SOURCED | High |
| Mean sea level in 2100 vs 1995–2014 | Likely range 0.37–0.82 m (SSP2-4.5), 0.57–1.08 m (SSP5-8.5); observed +32 mm per decade, 1954–2025 | P: https://www.hko.gov.hk/en/climate_change/proj_hk_msl.htm ; https://www.hko.gov.hk/en/climate_change/obs_hk_sea_level.htm | SOURCED | High |
| Annual maximum daily rainfall | Baseline 203 mm; +10.7% by 2041–60 (SSP2-4.5); +28.8% by 2081–2100 (SSP5-8.5); wide ranges | P: https://www.hko.gov.hk/en/climate_change/proj_hk_rainfall_rx1day_info_details.htm | SOURCED | High |
| 7–8 Sep 2023 black rainstorm | 158.1 mm in one hour at HKO HQ, highest since 1884; warning in force 16 h 35 min | P: HKO 2023 review, https://www.hko.gov.hk/en/wxinfo/pastwx/2023/ywx2023.htm | SOURCED | High |
| Mangkhut, 16 Sep 2018 | Quarry Bay 3.88 mCD (surge 2.35 m), second only to Wanda 1962; flooding in coastal and outlying areas; in Tai Kok Tsui only "a tower crane was blown down" | P: https://www.hko.gov.hk/en/publica/tc/tc2018/section3_5rpt.html | SOURCED | High |
| CEDD coastal hazards study: 26 low-lying or windy coastal residential areas at higher risk to 2050 | Tai Kok Tsui, Mong Kok and West Kowloon not listed (Lei Yue Mun is the only urban Kowloon area); seawalls "generally" withstand 100-year events with climate change to 2050 | P: https://www.info.gov.hk/gia/general/202204/07/P2022040700422.htm (7 Apr 2022) | SOURCED | High |
| DSD flooding blackspots | 5 left in 2020, the only Yau Tsim Mong one being Chatham Road South (Tsim Sha Tsui), none in Tai Kok Tsui; 4 left by May 2023 (S) | P: https://www.info.gov.hk/gia/general/202003/29/P2020032700643.htm ; S: The Standard, 29 May 2023 | SOURCED | High / medium |
| Tai Kok Tsui is largely reclaimed land (phases 1867–1945; the Olympian City area in the 1990s) | ground level in mPD UNVERIFIED | S: Wikipedia | SOURCED (secondary) | Medium |
| Insured typhoon losses, market-adjusted (HKFI survey, in HKO annexes) | Hato 2017 HK$1.11bn; **Mangkhut 2018 HK$3.69bn**; Saola 2023 HK$410m; Yagi 2024 HK$36.3m | P: https://www.hko.gov.hk/en/publica/tc/tc2018/annex1.html (and the 2017, 2023 and 2024 annexes) | SOURCED | High |
| Insurance Authority: Sep 2023 black rainstorm and Saola | HK$1.54bn and HK$361m (104 insurers, to 30 Sep 2023) | P: https://www.ia.org.hk/en/infocenter/press_releases/20231204.html (4 Dec 2023), read via snippets | SOURCED | Medium-high |
| Withdrawal of flood cover from Hong Kong home policies | none found | search not exhaustive | UNVERIFIED (absence) | Low |
| Contents insurance premium, example | HK$623–1,108 a year (OneDegree; covers flood and typhoon water damage) | S: https://www.onedegree.hk/en-us/home-insurance | SOURCED (product page) | Medium |
| Owners' corporations must hold third-party risks insurance on common parts | ≥HK$10M per event, since 1 Jan 2011; **liability only, not damage to the building** (our reading) | P: https://www.buildingmgt.gov.hk/en/Policy_and_Legislation/2_4.html | SOURCED / inference | High |

### HKMA and bank treatment

| Fact | Number | Source (URL, date) | Tag | Conf. |
|---|---|---|---|---|
| HKMA pilot climate risk stress test, 27 banks | **32%** of Hong Kong property-related lending "pledged with collateral located in vulnerable areas"; devaluation "could be more than 50% for some properties in vulnerable areas"; residential mortgage 1-year ECL **×25** (HK$0.7bn → HK$17.3bn); insurance recovery excluded; physical scenario RCP8.5, 2051–60; D-SIB capital ratio −3pp over 5 years under disorderly transition | P: https://www.hkma.gov.hk/media/eng/doc/key-functions/banking-stability/Pilot_banking_sector_climate_risk_stress_test.pdf ; https://www.info.gov.hk/gia/general/202112/30/P2021123000495.htm (30 Dec 2021) | SOURCED (checked in the report) | High |
| HKMA second stress test (2023–24) | Capital ratio −1.4 to −3.1pp (trough 16.6%); short-term scenario assumes "a substantial correction in the residential property prices", **no % published**; some banks mapped collateral against DSD data and building age and height, and deducted the present value of repair costs (Box 3) | P: https://brdr.hkma.gov.hk/eng/doc-ldg/docId/getPdf/20250306-2-EN/20250306-2-EN.pdf ; speech 28 Feb 2025 https://www.hkma.gov.hk/eng/news-and-media/speeches/2025/02/20250228-1 | SOURCED | High |
| HKMA Research Memorandum 05/2023 (Wong, Ka & Ng) | Under HKO's "High" scenario average prices "could be 4% to 21% lower by around 2050", warming acting "alongside ageing properties"; "the older the property, the larger the expected adverse impact"; doubling severe typhoons → −1.4%; rainfall "very small". Not a forecast | P: https://www.hkma.gov.hk/media/eng/publication-and-research/research/research-memorandums/2023/RM05-2023.pdf (22 Dec 2023) | SOURCED (checked in the paper) | High as a source; low as a forecast |
| Average age of transacted homes (same paper, Table 1) | 14.1 years (2001–05) → 26.1 years (2021) | P: as above | SOURCED | High |
| SPM GS-1 Climate Risk Management | issued 30 Dec 2021 | P: https://brdr.hkma.gov.hk/eng/doc-ldg/spm/current/GS-1 | SOURCED | High |
| Mortgage terms (LTV, rate) reacting to climate risk in Hong Kong | none found | — | UNVERIFIED (absence) | — |
| HKMA limits since 16 Oct 2024 | LTV 70% "regardless of the value"; DSR 50% | P: https://www.hkma.gov.hk/eng/news-and-media/press-releases/2024/10/20241016-4/ | SOURCED | High |
| HKMC Mortgage Insurance Programme | "Maximum sum of 'remaining term to maturity' and 'age of Property' … **75 years**"; maximum term 30 years | P: HKMC eligibility table (PSAs from 16 Oct 2024), https://www.hkmc.com.hk/files/product/3/4-%20IEC%20-%2080%25%20LTV%20MIP_Eng_Property%20Value%20up%20to%20HK%2417-15%20mn_clean_on%20or%20after%2016102024%20(3).pdf | SOURCED (checked) | High |
| Banks without MIP: buildings over 55 get at most a 20-year tenor; government says HKMA sets no age rule | — | S: HK01, 11 Sep 2025 (LegCo exchange) | SOURCED (secondary) | Medium |

### HKMC reverse mortgage, building age, URA

| Fact | Number | Source (URL, date) | Tag | Conf. |
|---|---|---|---|---|
| RMP property age | "not exceed 50 years of age (otherwise it will be considered on a case-by-case basis)"; over 50 may need a building inspection report | P: https://www.hkmc.com.hk/eng/our_business/reverse_mortgage_programme.html ; LCQ22 https://www.info.gov.hk/gia/general/202505/14/P2025051300589.htm (14 May 2025) | SOURCED | High |
| RMP specified property value | 100% up to HK$8M + 50% of the excess, capped at HK$25M; a "refinancing property" (still mortgaged) counts at most 80% of appraised value | P: RMP page | SOURCED | High |
| RMP costs | Fixed 4% for 30 years, then Prime −2%; floating Prime −2%; upfront premium 1.96% (7 × 0.28%); 1.25% a year on the balance | P: RMP page | SOURCED (matches the model's inputs) | High |
| RMP monthly payout per HK$1M, two borrowers, life term (youngest borrower's age) | Fixed: age 60 **HK$1,810**, age 70 HK$2,770. Floating: age 60 HK$1,650, age 68 HK$2,250, age 70 HK$2,520 | P: RMP page Table 3 ; floating table PDF (03/2026) https://www.hkmc.com.hk/files/product_file/1/1470/E_Level%20of%20Monthly%20Payout%20and%20Maximum%20Lump-Sum%20Payout%20Amount%20at%20Closing%20%28March%202026%29.pdf | SOURCED (checked) | High |
| RMP applications in 2024 | 1,017 | P: LCQ22, 14 May 2025 | SOURCED | High |
| Mandatory Building Inspection (MBIS) and Window Inspection (MWIS) | MBIS: buildings aged 30+, once every 10 years (common parts, external walls, projections), by notice; MWIS: 10+, every 5 years; both exclude domestic buildings of ≤3 storeys | P: https://www.bd.gov.hk/en/safety-inspection/mbis/index.html ; LCQ18 https://www.info.gov.hk/gia/general/201206/13/P201206130430_print.htm | SOURCED | High |
| MBIS selection age cut 50 → 40 (2020) → 30 (2023), rule revoked 2024; ≈600 notices a year, by risk | — | P: Audit Commission Report 84 Ch. 4 (31 Mar 2025) https://www.aud.gov.hk/pdf_e/e84ch04.pdf ; S: HK01 | SOURCED | High / medium |
| Proposed MBIS/MWIS penalties | New HK$6K fixed penalty; MBIS maximum fine HK$50K → HK$200K; HK$300K if injury results; bill "by the end of 2026" | P: https://www.info.gov.hk/gia/general/202412/13/P2024121300735.htm (13 Dec 2024) | SOURCED | High |
| Operation Building Bright 2.0 | 80% of cost, capped at HK$40K per unit (60+ owner-occupiers: 100%, HK$50K); buildings 30+; round 3 closed 30 Sep 2023 | P: https://brplatform.org.hk/en/page/detail/10331 | SOURCED | High |
| Per-flat cost of major repairs | — | URA Cost Reference Centre (not extractable) | UNVERIFIED | — |
| Ageing stock | Private buildings 50+: 4,500 → 9,600 in the ten years to 2023; ≈326,000 private flats aged 70+ by 2046 | P: DEVB LCQ21, 22 Nov 2023, https://www.devb.gov.hk/en/sdev/press/index_id_12678.html | SOURCED | High |
| Yau Ma Tei / Mong Kok District Study | Of 3,350 buildings, 65% are 50+; by 2047, 80% will be 70+; Tai Kok Tsui to become a "park side green community" | P: TPB Paper 10795, 7 Jan 2022, https://www.tpb.gov.hk/uploads/page/meetings/TPB/Yau_Mong_Study/Yau_Mong_Study_MainPaper.pdf | SOURCED | High |
| Compulsory sale thresholds (in force 6 Dec 2024) | <50 years: 90%; 50–59: 70% in designated areas, 80% elsewhere; 60–69: 65%/70%; 70+: 65% | P: EAA circular, 17 Dec 2024, https://eaa.org.hk/Portals/0/Sections/CC/2024_Dec/20241217_Letter_to_Licensees_Eng.pdf | SOURCED | High |
| URA owner-occupier compensation | market value + Home Purchase Allowance based on "a seven-year-old flat" of similar size in the same locality | P: https://www.ura.org.hk/f/page/1898/18309/ | SOURCED | High |
| Price discount per year of building age in Hong Kong | — | none found | UNVERIFIED | — |

### Scenarios

| Fact | Number | Source (URL, date) | Tag | Conf. |
|---|---|---|---|---|
| NGFS Phase V (5 Nov 2024): 7 scenarios. Orderly: Net Zero 2050, Below 2 °C, Low Demand. Disorderly: Delayed Transition. Too little, too late: Fragmented World. Hot house: NDCs, Current Policies. Phase VI not out on 4 Nov 2026 | — | P: https://www.ngfs.net/ngfs-scenarios-portal/ ; outreach deck https://www.ngfs.net/system/files/2025-01/20241108_ngfs_scenarios_phasev_outreach_public_v2.pdf | SOURCED | High |
| Net Zero 2050 carbon price | "around $300/tCO2 … by 2035" | P: high-level overview p.2, https://www.ngfs.net/system/files/import/ngfs/media/2024/11/05/ngfs_scenarios_high-level_overview.pdf | SOURCED | High |
| Delayed Transition carbon price (chart reading, US$2010/t) | ≈0–10 to 2030; ≈100 in 2035; ≈160 in 2040; ≈320 in 2050 | P: outreach deck slides 34–35 | ESTIMATED (chart, ±10%) | Medium |
| NGFS Phase V physical-damage GDP figures (−7% to −15% of world GDP by 2050) use Kotz, Levermann & Wenz (2024), **retracted by Nature on 3 Dec 2025** | **don't quote them** | P: retraction notice, https://pmc.ncbi.nlm.nih.gov/articles/PMC12711553/ | SOURCED (checked) | High |
| NGFS short-term scenarios (May 2025, to 2030): Highway to Paris, Sudden Wake-Up Call, Disasters and Policy Stagnation, Diverging Realities | Sudden Wake-Up Call: world GDP −1.3%, Asia −1.7% by 2030; inflation spike in Asia ≈+5pp (2027, chart); no equity figures in the summary | P: https://www.ngfs.net/system/files/2025-05/NGFS%20Short-term%20scenarios_Presentation_1.pdf | SOURCED / chart | High / medium |
| Bank of England climate stress test (2021 exercise, results May 2022) | No Additional Action: UK equities "just under 20% lower", S&P 500 "25% lower" by the end of 30 years; Late Action: carbon price US$30 to 2030, then over US$1,000 by 2050; short recession | P: https://www.bankofengland.co.uk/stress-testing/2022/results-of-the-2021-climate-biennial-exploratory-scenario | SOURCED | High |
| ECB 2022 climate stress test | 3-year disorderly scenario "not as adverse as a typical EU-wide EBA stress test" | P: https://www.bankingsupervision.europa.eu/ecb/pub/pdf/ssm.climate_stress_test_report.20220708~2e3cc0999f.en.pdf | SOURCED | High |
| CISL "Unhedgeable risk" (2015): cumulative 5-year returns, conservative (40% equity) portfolio | Baseline +12%; Two Degrees +9%; No Mitigation −26% (a market-panic case, 5% probability); about half hedgeable by sector and region | P (research institute): https://www.cisl.cam.ac.uk/system/files/documents/unhedgeable-risk.pdf | SOURCED (dated) | Medium-high |
| HK disposable plastic tableware, Phase 1 from 22 Apr 2024; Phase 2 has no date; biodegradable plastics (PLA etc.) count as plastic | — | P: https://cuttheplastics.hk/index.php/en/faq-en.html | SOURCED | High |
| EU CBAM covers cement, iron and steel, aluminium, fertilisers, electricity and hydrogen; not paper or plastic packaging | — | P: https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en | SOURCED | High |

---

## 3. The flat: keep, retrofit or exit, and when

**Verdict.** Keep the flat to 2037, spend on it only what pays back by itself, and decide the exit in 2037 with one
added test: how far the old flat's price has fallen against a newer one. The climate lens doesn't move the exit
earlier on today's evidence. It does two things: it makes the reverse mortgage the hedge if an old-building discount
opens, and it turns "any time before 2045" into a deadline set by the building's age.

### 3.1 Finance: the green mortgage is a refusal

| Item | Working | Result | Tag |
|---|---|---|---|
| Current loan | HK$1.8M, 3.5%, 168 months → payment = 1.8M × 0.002917 / (1 − 1.002917^−168) | HK$13,568 a month (case: ≈HK$13.6K) | ESTIMATED |
| Owed in 2037 | Present value of the last 36 payments | ≈HK$0.46M (matches the model's input) | ESTIMATED |
| A 0.10% rate cut, if any bank gave one | 132 months at 3.40% vs 3.50% | ≈HK$11K over 11 years (≈HK$1K a year) | ESTIMATED |
| Best rebates on HK$1.8M | BEA HK$0 (below HK$2M); SC HK$888 (closed); HSBC's 2022 band HK$3,988 (first-hand only) | HK$0–4K, once (0–0.2%) | SOURCED / ESTIMATED |
| Eligibility | Needs the **building** rated NB or EB Gold/Platinum; the OC would have to apply and pay EB fees from ≈HK$122K | Not available to one owner | SOURCED |
| HKMC Green Promotion | An Interiors – Residential certificate (≈HK$610 in fees + a fit-out meeting 30 items) unlocks HK$1K–8K, but only until 31 Dec 2026 | Not available in 2037 unless renewed | SOURCED |

**What we would not do:** refinance into a "green" product. The family would pay legal and transfer costs and accept
clawback terms for a rebate of at most about 0.2% of the loan, on a loan we clear in 2037 anyway. Round One's rule
stands: compare the mortgage each year with new offers and switch only if the saving clears the fees. The green label
doesn't change that test.

### 3.2 Retrofit: what pays and what doesn't

The household inputs are ILLUSTRATIVE: 6,000 kWh a year (EMSD's 1,634 kWh per person × 4 ≈ 6,536) at a marginal
HK$1.50/kWh (101.2 ¢ basic + 47.4 ¢ November fuel charge, ESTIMATED).

| Measure | kWh a year | HK$ a year | Cost | Payback | Advice |
|---|---|---|---|---|---|
| 3 working air-conditioners replaced with Grade 1 inverters (45% saving, EMSD) | 6,000 × 39.5% × 45% ≈ 1,067 | ≈1,600 | 3 × HK$4,890–7,880 = HK$14.7K–23.6K before installation | 9–15 years | Don't replace working units. When one fails, buy the best Grade 1 model (up to 33% better than the worst, Consumer Council) |
| LED for the remaining fluorescent lamps | ≈85 (6,000 × 6.3% × half × 45%) | ≈130 | small | short | Do it; trivial |
| Window film or coating | 5–10% of cooling ≈ 65–130 (ILLUSTRATIVE) | ≈100–195 | UNVERIFIED (CLP's Cool Home Pilot subsidises it) | unknown | Only with the subsidy |
| Rooftop solar | — | — | — | — | Impossible for one owner: the roof is a common part (OC decision) |
| **Total** | ≈1,280 | **≈HK$1,900** (≈0.25% of HK$780K) | | | Housekeeping, not a wealth lever |

**Heat adds a cost, but a small one.** Very hot days have gone from 14 to 52–54 a year now (HKO). Even 20% more
air-conditioning use (ILLUSTRATIVE) adds about 470 kWh, or roughly HK$700 a year. The real cost of heat is to health:
the parents will be in their 70s and 80s in the hot nights of the 2040s and 2050s (63 a year by 2021–40 and 87 by
2041–60, SSP2-4.5). That belongs in the medical cover (Round One §8), not in the property line.

**Would a green renovation raise the 2037 sale price?** No Hong Kong evidence says so for an existing flat.
- The only Hong Kong price study (Hui, Tse & Yu 2017: +4.4%) covers **new developments certified as buildings**, sold
  in 2012–14.
- It says nothing about a certified fit-out in a 41-year-old building.
- So we don't claim a premium, as we didn't claim one for ESG returns in Round One.

### 3.3 Physical risk: what reaches the family's money

| Channel | Evidence | Effect on the Wongs | Tag |
|---|---|---|---|
| Storm surge or flooding of the flat | Not on CEDD's 26 areas, DSD's blackspots, HKO's Mangkhut or Hato flooding lists, or the Ragasa warning list | Remote for a high-floor unit, to 2050 | SOURCED (absence) |
| Damage to the building | Mangkhut damaged glass curtain walls in Mong Kok and Hung Hom (HKO); basements and low-level plant are what floods in a black rainstorm (inference) | Repair costs shared by undivided shares, through OC levies; size UNVERIFIED | SOURCED / inference |
| Insurance | Insured typhoon losses: Mangkhut HK$3.69bn; Sep 2023 rain HK$1.54bn; S&P expects tighter property pricing (S) | Contents cover ≈HK$600–1,100 a year: premiums more likely to rise than cover to vanish. **Check the OC holds property cover**: the compulsory policy is liability only | SOURCED / inference |
| Heat | 52–54 very hot days now vs 14 | Cooling ≈+HK$700 a year; health (medical cover) | SOURCED / ILLUSTRATIVE |
| Value at exit | RM05: −4% to −21% by about 2050, district-wide, acting through building age; banks now deduct repair costs in stress tests | The channel that matters: §3.4 | SOURCED (not a forecast) |

### 3.4 Exit: when, and how

**The building's age sets the deadline.** For the illustrative 1996 building:

| Year | Age | Buyer's maximum term (MIP: age + term ≤ 75, cap 30) | Reverse mortgage | Compulsory sale threshold |
|---|---|---|---|---|
| 2026 | 30 | 30 years | eligible | 90% |
| 2037 | 41 | 30 years (75 − 41 = 34) | eligible | 90% |
| 2045 | 49 | **26 years**; repayment per HK$1M at 3.5% ≈ HK$4,890 vs HK$4,490 (+9%) | eligible | 90% |
| 2046 | 50 | 25 years | **case by case**; inspection report may be needed | 70–80% (redevelopment option opens) |
| ≈2051 | 55 | ≈20 years at banks (S) | case by case | 70–80% |

SOURCED rules; ESTIMATED arithmetic. MBIS notices can come at any time from age 30, by risk. The building will
probably face at least one major-repair levy before 2037. Its size is UNVERIFIED. OBB 2.0 caps its 80% subsidy at
HK$40K a unit, so it was sized for bills of up to about HK$50K a unit (inference). Actual costs are UNVERIFIED.

**The rule for any building age: release the home by the year the building turns 50 (completion year + 49).**
- A 1996 building gives 2045.
- A 1986 building would give 2035, before Adrian retires: the release would have to come forward.
- Lookbua should state the rule, not just the year, because the case doesn't give the age.

**How: the reverse mortgage hedges an old-building discount; downsizing is exposed to it.**
- The reverse mortgage income is set once, at application, on HKMC's specified value (8M + 50% above), then paid for
  life and non-recourse.
- The downsizing release is the gap between two prices, so a discount on the old flat alone hits it with leverage.
- Arithmetic, 2037, model path:
  - Home: 11.5M × 1.015^11 = HK$13.55M.
  - Counted value: 8 + 0.5 × 5.55 = HK$10.77M.
  - Income: 10.77 × HK$1,810 × 12 = **HK$234K a year**, at today's table (fixed rate, two borrowers, life, youngest
    borrower Carmen at 60). This confirms the model's HK$230K (ESTIMATED).

| The old flat in 2037 is worth… (newer flats hold) | Reverse mortgage income | Plan lasts to 89 | Downsizing release | Plan lasts to 89 |
|---|---|---|---|---|
| model path | HK$230K | 82.6% (`{{ladder_5_89}}`) | HK$4.46M | 83.1% (`{{prop_down_89}}`) |
| 10% less | HK$216K (−6%) | 81.2% | HK$3.13M (−30%) | 76.9% |
| 16% less (the scenario's level) | HK$206K | 80.4% | HK$2.28M | 72.2% |
| 20% less | HK$201K | 79.9% | HK$1.80M | 69.8% |
| *If both flats fall 16% alike* | — | — | HK$3.68M | 79.7% |

EXPLORATORY: 10,000 paths, same seed, full plan. Scripts:
`C:\Users\User\AppData\Local\Temp\claude\36105602059f4657\4af17e3c-5905-4e9b-a099-11f876be827b\scratchpad\scenario_runs.py`
and `...\timing_runs.py`.

**When, if they downsize.** The run below sizes a relative drag on the old flat on RM05's range (0.15–0.9% a year,
ILLUSTRATIVE as a *relative* drag). Each cell gives the chance the money lasts to 89, then the release.

| Downsizing year | No drag | 0.15%/yr | 0.9%/yr |
|---|---|---|---|
| 2032 (Chloe graduates) | 84.3% (HK$4.15M) | 83.9% | 81.5% (HK$3.50M) |
| 2037 (plan) | 83.1% (HK$4.46M) | 82.1% | 77.3% (HK$3.20M) |
| 2041 | 82.1% | 80.9% | 73.6% |
| 2045 | 80.5% (HK$5.00M) | 79.0% | 70.6% (HK$2.64M) |

*How to read it.*
- With no drag, moving earlier gains only about 1 point. The model also counts no value for the extra space, so treat
  that gain as an upper bound.
- With the high drag, every four years of waiting costs 3–4 points.
- So if downsizing is the route, 2037 is the latest sensible year, and 2032 (an empty nest) is worth a look.

**The 2045 reverse mortgage: a correction for Round One.**
- Page 11 of the proposal says delaying the reverse mortgage to 2045 lowers the plan from `{{ladder_5_89}}` to
  `{{rmp2045_89}}` (73%).
- That run kept the 2037 payout of HK$230K. HKMC pays more per HK$1M at an older entry age:
  - Floating, two borrowers, life: HK$2,250 at age 68 vs HK$1,650 at 60.
  - Estimated fixed rate at 68: ≈HK$2,471.
  - Counted value in 2045: HK$11.63M.
  - Income ≈ **HK$345K a year** (ESTIMATED).
- With that income the plan lasts to 89 in **80.7%** of futures, not 73.5% (EXPLORATORY).
- The 2045 payout will depend on 2045's rates, so today's table is only a basis.
- *Consequence:* waiting for the reverse mortgage costs little in the odds. What argues against it is the building
  turning 50 in 2046, any discount on old buildings, and losing the downsizing option.
- **Pete to confirm, and to log it if it's an error** (CLAUDE.md: the proposal is changed only to fix an error).

**After 2037 the two routes treat climate risk differently.**
- Once the reverse mortgage is signed, a later price fall doesn't touch the parents' income. The loan is non-recourse,
  so HKMC's insurer carries the risk and only the legacy absorbs it (inference from the RMP terms).
- Downsizing exits the old building and its age cliff. The heirs inherit a newer flat.

**Recommendation for the flat.**
1. Keep it to 2037 and clear the HK$0.46M then.
2. No green refinancing. No retrofit beyond replacing air-conditioners when they fail, and LEDs.
3. Lookbua: a land search plus building records for the completion year (it sets the deadline), and the OC's
   insurance schedule (property cover or not).
4. Add one review trigger: each year, compare the price per sq ft of the old flat with a roughly 10-year-old flat in
   the target district. If the gap widens by 10% or more against today, decide the route that year. Prefer the
   reverse mortgage if they want to stay, or downsize at once.
5. Release by 2045 at the latest (completion year + 49).
6. When they buy the smaller flat, prefer a newer building for its age and exit, not for its label. We would not pay
   the 4.4% premium the one Hong Kong study measured. That is ≈HK$0.3M on HK$7M (ESTIMATED), against an energy saving
   near HK$2K a year.

---

## 4. The warehouse and the green lease

**The split incentive, in this warehouse (the ILLUSTRATIVE unit defined at the top):**

| Measure | Who pays | Who gains | Split? |
|---|---|---|---|
| LED inside the unit | Carmen | Carmen (her own CLP meter) | No, unless the lease forces her to reinstate fittings or ends before payback |
| Rooftop solar | Landlord or OC (owns the roof) | The **CLP account holder** gets the feed-in tariff (HK$3–4/kWh, to 2033) | Yes: the tenant can't install without consent and gets no FiT |
| Common-area lighting, lifts, drainage, flood barriers at the loading bay | Landlord or OC | Tenants (lower service charge, less flood loss) | Yes: classic |
| Data for customers' Scope 2/3 questions | — | Carmen and the 2035–39 buyer | Needs landlord cooperation for any shared supply |

**Arithmetic (ESTIMATED on ILLUSTRATIVE inputs).**
- *LED:* 40 twin T8 battens at ≈80 W become 2 × 18 W LED tubes, saving 1.76 kW.
  - At 3,410 hours a year (11 h × 310 days) that is ≈6,000 kWh × ≈HK$1.45 = **≈HK$8.7K a year**.
  - Cost ≈HK$11.4K (tube price UNVERIFIED), so payback ≈1.3 years.
  - Possibly 100% deductible in year 1 (IRD rule SOURCED; whether LED qualifies is UNVERIFIED).
- *Solar, 20 kWp on the roof:* 20 × 1,107 = 22,140 kWh × HK$3 = HK$66K a year until 31 Dec 2033.
  - Cost 20 × HK$29.2K = HK$584K (2019 price).
  - If connected in Jan 2027, it earns HK$465K of FiT by 2033. Payback ≈10.7 years, assuming the output is worth the
    tariff afterwards (UNVERIFIED).
- *Solar, 10 kWp at HK$4:* HK$44K a year against HK$292K, so payback ≈6.6 years, right at the 2033 cliff.

**What we would not do: Carmen paying for solar on a roof she doesn't own.**
- The payback (6.6–10.7 years) is longer than her lease, and longer than her time as owner (the sale is 2035–39).
- The FiT ends in 2033, so each year of delay loses about a seventh of the FiT income.
- We'd reconsider if the landlord pays for it, or if installed cost falls below about HK$20/Wp (UNVERIFIED; ≈6-year
  payback).

**Green lease: the clauses to ask for at the next renewal** (modelled on the Better Buildings Partnership's "Ten Green
Lease Essentials", updated Jan 2024, clauses refreshed Mar 2026:
https://www.betterbuildingspartnership.co.uk/green-lease-toolkit-0; Hong Kong-specific HKGBC or BEC guidance
UNVERIFIED):
1. **Reinstatement waiver** for efficient fittings (LED, controls) and any solar equipment, so tenant investments
   aren't lost at the end of the lease.
2. **Data sharing:** monthly kWh both ways (the tenant's meter, the landlord's common services) to answer customers'
   emissions questions.
3. **Landlord's works and roof access:** the right to install rooftop solar, with the tenant's cooperation. If the
   landlord installs it, a share of the FiT returned as a rent credit (ILLUSTRATIVE, e.g. 20%) buys the tenant's
   support for disruption and data.
4. **Cost recovery capped at savings:** any green works the landlord charges through the service charge are capped
   at the tenant's measured saving. BBP supports this "to the extent of resulting savings", but offers "no drafting",
   so ours is bespoke.
5. **A renewal option to at least 2039:** a buyer of the business in 2035–39 values a secure warehouse lease more than
   any kWh. This is the clause that touches enterprise value (link to Fahtai's slide 8).
6. **Flood resilience** (if on the ground floor): the landlord to maintain drainage and flood barriers at the loading
   bay; the tenant to rack stock off the floor and hold business interruption cover.

**BEEO and certification for the warehouse.**
- BEEO puts no audit duty on an ordinary industrial building or a tenant's unit. Its codes reach industrial buildings
  only in their common areas (from 20 Sep 2026).
- A BEAM Plus Interiors (non-residential) certificate would cost HK$1,210 + HK$17K–22K per floor in fees, plus the
  fit-out work.
- We would not certify the unit unless a named customer requires it. The emissions data from clause 2 answers
  buyers' due diligence at lower cost.

**EV charging** (brief area 4). For the family's car (case: HK$220K):
- The government's EV-Charging at Home Subsidy Scheme is for car parks of existing private residential buildings, and
  an OC decision (Climate Action Plan 2050; current status UNVERIFIED).
- No Hong Kong evidence links it to flat prices.
- For the vans: Fahtai's area. The New Energy Transport Fund's current terms are UNVERIFIED.

---

## 5. The scenario: "Late and sudden" (disorderly transition, 2030–31)

**Story.** Policy waits until 2030, then tightens sharply, as in NGFS Delayed Transition: a carbon price near zero to
2030, then ≈US$100/t by 2035 (chart). The shock unfolds like NGFS "Sudden Wake-Up Call" and the HKMA's short-term
scenario: a Hong Kong recession and "a substantial correction" in home prices. Physical risk keeps rising, per HKO
SSP2-4.5. One scenario, as the brief asks. A hot-house variant and a tail follow as sensitivities.

### 5.1 Inputs, ready for the model

Base = the model's inputs: equity 6%, vol 17%; ladder 4%; CPI 2.5%; property +1.5% a year.

| Variable | Base | Scenario | Years | Source and why this size | Tag |
|---|---|---|---|---|---|
| Equity return | 6% | −10pp, then −5pp (≈−14% level, no catch-up) | 2030, 2031 | Sized between: CISL Two Degrees (−3pp over 5 years for 40% equity) and ECB 2022 ("not as adverse as a typical EBA stress test") as the floor; BoE No Additional Action (−20–25% over 30 years) and CISL No Mitigation as the ceiling. About one standard deviation of equity, two years running | ILLUSTRATIVE, bracketed by SOURCED |
| Ladder / bond return | 4% | −5pp, −1pp, then +0.5pp carry | 2030; 2031; 2032–36 | Yields up ≈1pp on ≈5-year duration; direction from NGFS Sudden Wake-Up Call (US policy rate ≈+2pp; HKD peg). Upper bound for a hold-to-maturity ladder | ILLUSTRATIVE |
| CPI | 2.5% | +2pp, +1pp (price level +3% for good) | 2030, 2031 | Between NGFS Delayed Transition (+0.7pp peak) and the Sudden Wake-Up Call spike in Asia (≈+5pp for one year, chart) | ILLUSTRATIVE, bracketed |
| Flat value | +1.5%/yr | −10%, −5% (level −15%), then base growth; plus a chronic drag of −0.15pp/yr from 2026 → **×0.836 by 2037** | 2030–31; all years | Shock: HKMA second stress test "substantial correction" (no % published). Drag: RM05's low end (−4% by ≈2050) | ILLUSTRATIVE (shock); SOURCED (drag range) |
| Reverse mortgage income | HK$230K | HK$206K (HKMC counted value on the lower 2037 price) | from 2037 | RMP valuation rule, SOURCED; arithmetic ESTIMATED | ESTIMATED |
| Business sale proceeds | HK$3.0M counted | −10% (HK$2.7M) | 2039 | Recession; carbon cost on imported paper (China Delayed Transition ≈US$110/t by 2035, HKMA chart). Upside: plastics Phase 2 (no date). Fahtai to refine | ILLUSTRATIVE |
| Carmen's draw | as modelled | −HK$100K a year | 2030, 2031 | Recession (HKMA short-term scenario: HK GDP ≈−2.0%, −1.5%, −0.7%, chart) | ILLUSTRATIVE |
| Storm repair levy (optional) | 0 | −HK$50K | 2033 | Building damage through the OC; size UNVERIFIED | ILLUSTRATIVE |
| ESG sleeve | same as equity | **same shock** | — | No credit for a smaller hit without the fund's measured carbon exposure (Win's area); CISL's "half hedgeable" needs real sector tilts | — |

**Don't use:** NGFS Phase V GDP damages, because the damage function was retracted (Nature, 3 Dec 2025). Don't quote
the HKMA pilot's "more than 50%" as a Tai Kok Tsui number: it is for "some properties in vulnerable areas" under
RCP8.5 in 2051–60.

### 5.2 Result (EXPLORATORY; 10,000 paths, same seed; full plan with the reverse mortgage)

| Run | Lasts to Carmen's 89 | Median pot at 89 (today) |
|---|---|---|
| Full plan, base (`{{ladder_5_89}}`) | 82.6% | HK$6.68M |
| Portfolio shocks only | 72.2% | HK$4.27M |
| … equity alone / bonds alone / CPI alone | 78.2% / 81.3% / 79.0% | |
| Flat only (smaller reverse mortgage) | 80.4% | HK$6.19M |
| Business only | 79.9% | HK$5.99M |
| **Central: all together** | **66.7% (−15.9 points)** | **HK$3.07M** |
| Central + HK$50K levy in 2033 | 66.1% | HK$2.99M |
| Same shocks in 2039–40 (after the reverse mortgage is locked) | 68.8% | HK$3.44M |
| Downsizing instead, central, both flats fall alike | 67.0% | HK$3.41M |
| Downsizing instead, central, only the old flat falls | **58.0%** | HK$1.56M |
| Hot-house variant: equity −0.9pp a year from 2027 (BoE No Additional Action, S&P 500 −25% over 30 years ≈ −0.95%/yr); flat −0.9pp a year (RM05 top end) | 71.9% | HK$3.94M |
| Tail: equity −30% once in 2030 (a CISL No Mitigation-type repricing), plus central flat and business | 57.5% | HK$1.31M |

**Legacy at 89** (median pot + home equity, today's money):
- Reverse mortgage: HK$8.15M (base, = `{{legacy_rmp}}`) → HK$3.87M (central).
- Downsizing: HK$12.24M (= `{{legacy_down}}`) → HK$7.37M if both flats fall, HK$6.28M if only the old one does.

**What it says (honestly).**
- **The largest loss comes through the portfolio.** It is ordinary market and inflation risk, and the 25% ESG label
  doesn't change it. That cuts against the simple thesis, so frame it as *exposure vs decision*: the portfolio carries
  more climate exposure, but the flat holds the decision that changes the outcome. Choosing the route is worth up to
  9 points (66.7% vs 58.0%) if an old-building discount opens.
- **Inflation matters more than expected (−3.6 points alone),** because the plan's guaranteed income is fixed in HK$.
  The guardrails and the medical review at 75 (`{{switch_89}}`) are the defence. Pete could run the scenario with
  them on.
- **The climate shock is smaller than a bad bear market.** About one standard deviation of equity, two years
  running. The tail case is about nine points worse (57.5% vs 66.7%). That matches the supervisors: the ECB calls a disorderly transition
  "different from a severe economic crisis", and NGFS foresees no climate-caused global recession.
- **Timing of the release:** if the shock lands after 2037, the reverse mortgage income is already locked, and the
  flat's loss falls on the legacy only.

**For Pete (model):**
- Add a year-specific shock function to `sim()`: equity and bond return addends by year, a price-level factor on
  spending, and a flat-value multiplier that feeds `downsize_release()` and the reverse mortgage income. The scratch
  script patches exactly these three lines.
- Proposed keys:
  - `clim_central_89`, `clim_central_pts`
  - `clim_portfolio_89`, `clim_flat_89`, `clim_biz_89`
  - `clim_down_old_89`
  - `clim_hot_89`, `clim_tail_89`
  - `rmp_flat10_pct`, `down_flat10_pct`
  - `rmp2045_table_89`
- Diff `numbers.json` and log in `reviews/applied.md`.

---

## 6. Risk register (the Wongs; area 4 and the scenario)

L = likelihood to 2045, I = impact on the plan (low / medium / high). Points are EXPLORATORY model results.

| # | Type | Risk | L | I | What the plan does | Residual |
|---|---|---|---|---|---|---|
| T1 | Transition | Late, sudden policy in 2030–31: markets, inflation, recession | Medium | High (−16 pts central; −25 pts tail) | Diversified index funds; Treasury ladder; guardrails; the business counted at HK$3.0M, not HK$5.0M | Medium: the inflation channel hits fixed-HK$ income |
| T2 | Transition | Carmen's products: bioplastics count as "plastic"; Phase 2 has no date; no carbon price in Hong Kong | Medium | Medium (business only −2.7 pts) | Staged sale; product-mix review (Fahtai) | Medium, two-sided (Phase 2 could raise demand) |
| T3 | Transition | Energy prices: CLP fuel charge 39.4 → 47.4 ¢ within 2026 | High | Low (≈HK$1K a year for the household) | Efficient air-conditioning at replacement; LED in the warehouse | Low |
| P1 | Physical | Heat: 52–54 very hot days now; 65 by 2041–60 | High (already here) | Low on money, medium on health | Medical cover and the tier review (Round One §8); efficient cooling | Medium (health) |
| P2 | Physical | Typhoon or flood damage to the building's common parts | Medium | Low–medium (OC levies; size UNVERIFIED) | Check the OC's property cover; contents policy with flood and typhoon cover (≈HK$600–1,100) | Low–medium |
| P3 | Physical | Warehouse flooding, stock loss, interruption | Low–medium (ILLUSTRATIVE upper floor) | Medium for the business | Upper-floor unit; racking; business interruption cover; lease clause 6 | Low |
| P4 | Physical | Storm surge at Tai Kok Tsui beyond 2050 | Low to 2050 | Medium after 2050 | Exit by 2045; reverse mortgage non-recourse | Low |
| L1 | Liability | MBIS or MWIS notice ignored; falling-window injury (fines to HK$200K, or HK$300K if injury, proposed) | Low | Low | Comply with notices; owner's liability cover; OC's HK$10M third-party policy | Low |
| L2 | Liability | Carmen's "compostable / sustainable" claims challenged (no industrial composting for most of it) | Medium | Medium | Evidence each claim (Fahtai) | Medium |
| R1 | Reputational | Our own plan's green claims: a green mortgage, retrofit or certification sold as "impact" | Medium | Medium (trust) | We refuse the green mortgage and the label premium; claims tagged | Low |
| Q1 | Liquidity | The flat is 42% of total assets (HK$11.5M of HK$27.19M) and illiquid; buyers' financing shrinks after 50 | Medium | High | Release by completion year + 49; the reverse mortgage as fallback | Low–medium |
| Q2 | Liquidity | A major repair levy as a cash call (size UNVERIFIED; OBB 2.0 cap HK$40K) | Medium | Low | Cash reserve | Low |
| V1 | Valuation | Old-building and heat discount on the flat by 2037 (RM05 range) | Medium | Medium–high for downsizing (−6 pts per −10%); low for the reverse mortgage (−1.4 pts) | Yearly price-gap trigger; route chosen on the measured gap | Medium |
| V2 | Valuation | The business's price in 2035–39 depends on lease security and emissions data | Medium | Medium (≈4 pts per HK$1M, Final_Plan §2) | Green lease renewal option; data sharing | Medium |
| D1 | Data | Not known: building age, Tai Kok Tsui ground level, the OC's insurance, repair costs; NGFS damages retracted; HKMA's price shock unpublished | High | Medium (false precision) | Tags on screen; ranges; we don't use NGFS damages; a restatement policy | Medium |
| D2 | Data | 2037 and 2045 reverse mortgage payouts depend on future rates | High | Medium | Today's table as the basis; sensitivity shown | Medium |
| C1 | Conduct | Suitability for two people who disagree (Adrian stays, Carmen moves?); capacity at 65+ | Medium | High | Enduring powers of attorney first (Round One §9); joint decision at the 2037 review | Low |
| C2 | Conduct | Advising on mortgages and insurance without a licence; product bias | Low | High | Refer to licensed banks and HKMC; no commission; fees disclosed | Low |
| I1 | Transition (the scenario) | Adrian's bonus (case: HK$150–300K; the model counts HK$150K) lost in the 2030–31 downturn, as the scenario already cuts Carmen's draw | Medium | Low (−1.3 pts on the new plan under the scenario, 91.0% → 89.8%; downsizing's downturn crossing ≈11% → ≈9%; `model_runs.md` M10a) | Nothing new: inside both limits. Proposed: add it to the scenario (`Final_Plan.md` §5.10) | Low |
| I2 | Transition, physical | Adrian's employer: a logistics technology company across Hong Kong, the GBA and Southeast Asia (case). Carriers face carbon costs and the region's ports face typhoons and floods; logistics software may gain from customers' emissions reporting | Not known | Not known; the sign is unclear | A missing price: buy the information (ask Adrian about the company's customers, markets and his contract) before pricing it | Not known |

Measured or estimated in this brief: T1, T2, V1, Q1 (the age rule), D2. The rest are managed, not measured.

**Adrian's job itself (Claude, 13 Nov, night): outside the climate register, inside the plan.** Any planner draws
"income lost before retirement" (the case's protection list names "disability / income interruption risk"), so by test
2 it isn't a climate route. It is priced (`model_runs.md` M10b) because it is the largest risk to the limits: every odds
figure assumes Adrian works to 65. Lost at the end of 2030 with no work again, the plan as it stands falls to 45.4%
normally and 22.5% under the scenario; at half pay from 2032, 78.5% and 55.6%. A contingency restores both limits:
half pay from 2032, HK$200K a year less spending to 2036 and Carmen working to 65 (95.9%; 86.7%). Neither parent has
long-term disability income cover (case); disability is the insurable form of this risk.

---

## 7. Likely judge questions, with short answers

1. **"Why not a green mortgage? It's the obvious green finance tool for a home."** The building doesn't qualify: banks
   need NB or EB Gold/Platinum for the whole building. Even if it did, rebates on HK$1.8M are HK$0–4K, and no bank
   offers a lower rate (Consumer Council 2023: "basically no different"). A 0.10% cut would be worth ≈HK$11K before we
   clear the loan in 2037. The green test is the same as any refinancing: the saving must clear the fees.
2. **"Is Tai Kok Tsui a flood risk?"** It isn't on CEDD's 26 coastal areas at risk to 2050, on DSD's blackspots, on
   HKO's flooding lists for Mangkhut or Hato, or on the government's Ragasa warning list. It's reclaimed land, and we haven't checked its spot
   height (open item). The risk that reaches the family is damage to the building, paid as OC levies, and the OC's
   insurance.
3. **"Your scenario's biggest loss is the portfolio, so isn't the portfolio what matters?"** The portfolio carries the
   largest *exposure* (−10 points), but it's market and inflation risk that no ESG label changes. The *decision* that
   changes the outcome is on the flat: the route is worth up to 9 points if an old-building discount opens.
4. **"Where do your shocks come from?"** Each is sized between published bounds (§5.1): NGFS Delayed Transition and
   Sudden Wake-Up Call, the HKMA's two stress tests and RM05, the BoE 2021 exercise, the ECB 2022 test and CISL 2015.
   The sizes are ours and labelled ILLUSTRATIVE, because no regulator publishes a Hong Kong property price shock.
5. **"Why not use NGFS's GDP damage estimates?"** Their damage function (Kotz et al. 2024) was retracted by Nature on
   3 Dec 2025.
6. **"Should they sell now, before climate hits the price?"** Today's evidence doesn't say so. With no drag, moving
   earlier gains about 1 point, and the model counts no value for the space. The evidence that does exist (RM05) is
   district-wide, works through building age and isn't a forecast. So we set a trigger (the price gap against newer
   flats) and a deadline (completion year + 49).
7. **"Reverse mortgage or downsize: which under climate risk?"** The reverse mortgage hedges it: income falls ≈6% per
   10% fall in value (HKMC counts only half the value above HK$8M), and after signing it's fixed and non-recourse.
   Downsizing leaves more to the children (`{{legacy_down}}` vs `{{legacy_rmp}}`), but its release falls ≈30% per 10%
   discount on the old flat alone. Their choice: security or legacy.
8. **"You said in Round One that delaying to 2045 costs 10 points."** That run kept the 2037 payout. At HKMC's payout
   for entry age 68 the cost is about 2 points. The reason not to wait is the building turning 50 in 2046 (the
   reverse mortgage becomes case by case) and buyers' shorter loan terms.
9. **"What does a buyer's bank do with a 41-year-old flat?"** Under HKMC's mortgage insurance, age plus remaining term
   must be at most 75 years: in 2037 a buyer still gets 30 years; in 2045, 26 years (≈9% higher repayments).
10. **"Retrofit: would you insulate, add solar, certify?"** Solar is impossible on one flat. A full set of measures saves
    ≈HK$1,900 a year. Certification of a fit-out costs ≈HK$610 but has no price evidence for old buildings. We replace
    air-conditioners when they fail, with the best Grade 1 unit.
11. **"Explain the split incentive in Carmen's warehouse."** LED is hers and pays in ≈1.3 years. Solar and common
    parts are the landlord's, and the FiT goes to the account holder until 2033. Our green lease asks for a
    reinstatement waiver, shared data, cost recovery capped at savings, and a renewal option to 2039. The last one
    protects the business sale.
12. **"Are insurers pulling out of Hong Kong home cover?"** We found no evidence of it. Losses are large (Mangkhut
    HK$3.69bn insured; Sep 2023 rain HK$1.54bn) and pricing is tightening. We ask the OC whether it holds property
    cover, because the compulsory policy is liability only.
13. **"What would you not do?"** Refinance into a green mortgage (≤HK$4K). Pay the ≈4% label premium on the new flat
    (≈HK$0.3M for ≈HK$2K a year of energy saving). Have Carmen fund solar on a landlord's roof (payback 6.6–10.7
    years against a 2033 FiT cliff and a 2035–39 sale).
14. **"How do you know the building's age?"** We don't: the case doesn't give it. We assume 1996 and state the rule,
    completion year + 49, which changes the deadline if the real age differs.

---

## 8. Open items and what is unverified

**To check before any of it goes on a slide** (owner suggested):
- The building: completion year, saleable area, the OC's insurance schedule, any MBIS notice. These are case
  inventions, so define and label them (Lookbua, with Pete).
- Tai Kok Tsui spot height in mPD (Lands Department GeoInfo Map) (Lookbua).
- CLP 2026 residential block rates and non-residential tariff (CLP's site blocked automated fetches; open in a
  browser) (Lookbua).
- Whether FiT generation's renewable attributes go to CLP (the RE certificates). If so, rooftop solar under the FiT
  doesn't cut a tenant's reported Scope 2, a greenwashing trap for Carmen (Fahtai). UNVERIFIED.
- Whether a tenant can be the FiT account holder with the landlord's consent. UNVERIFIED.
- Hong Kong green-lease guidance (HKGBC, Business Environment Council, Link REIT, Hongkong Land). Only the UK BBP
  toolkit and Swire's Green Performance Pledge (250+ tenants, Jun 2026) are verified.
- Fixed-rate RMP payout at entry age 68: estimated from the floating table. Check HKMC's online calculator.
- **Round One `rmp2045_89`:** likely understated (the payout kept at the 2037 level). Pete to confirm and log.
- Round One's "a reverse mortgage needs a home free of other loans": HKMC accepts a "refinancing property" (counted at
  ≤80% of value). On our 2037 numbers 80% doesn't bind (0.8 × 13.55 = 10.84 > 10.77), so the HK$0.46M could also be
  cleared with an RMP lump sum. Medium confidence; low stakes.
- MBIS repair cost per flat; management-fee rise with age; the price discount per year of building age: no Hong Kong
  figure found. Don't put a number on a slide.
- Window-film savings and cost; LED tube and installation prices; current solar cost per Wp (2019 figure used).
- Ragasa 2025 insured losses (no official figure); IA climate guidance (site blocked fetches).
- HKMA second stress test's property price path (not published); BoE Late Action equity path (images only); IEA WEO
  2025 prices (site blocked).
- NGFS Phase VI: check again before 21 Nov.
- Hui, Tse & Yu (2017) is the only Hong Kong BEAM Plus price study we read; the office green-premium research (JLL,
  CBRE, Knight Frank) is unread.
- HKMC's RMP independent counselling requirement (recalled, not checked).
- The Wang Fuk Court fire (Tai Po, Nov 2025) reforms to major renovation works (China Daily, 15 Jan 2026,
  SECONDARY). Likely to raise repair costs and supervision (inference); bill status UNVERIFIED.

**Process note.** The shared web-search budget ran out during the research, so items marked UNVERIFIED above may be
checkable with a follow-up search session. All EXPLORATORY numbers come from scratch scripts that import the model
without changing it; nothing in `model/` or `figures/` was edited.
