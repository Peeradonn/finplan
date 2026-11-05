# Area 2, part 2: supply-chain finance, "compostable" PLA, and who pays the green premium

Research brief for Fahtai. Written 5 Nov 2026 for the Final on 21 Nov 2026. It extends
`Final/research/area2_business.md` (read that first; this brief doesn't repeat its baseline, abatement curve or loan
arithmetic) and corrects two of its numbers (§4c).

**Tags.** SOURCED: a public figure. ESTIMATED: our arithmetic from sourced inputs, working shown. ILLUSTRATIVE: our
assumption about the Wongs' business (same illustrative HK$35M distributor as `area2_business.md`). UNVERIFIED: could
not confirm. The arithmetic is in one script (`scf_calcs.py`, on this session's scratchpad; every line is reproduced
below, so the script isn't needed to check it).

**Limits.** Web-search budget was limited. CLP's and S&P Global's sites refused automated fetches (HTTP 403), and
e-Legislation's page didn't render, so the ordinance text itself wasn't read: the legal points rest on the EPD's
guidance pages, the LegCo Brief, the 2021 consultation document and LegCo replies, which I did read. Where a figure
comes only from a search-engine extract of a page I couldn't open, it says "search extract".

**Thesis tested:** "A distributor's transition runs through its suppliers and customers, so supply-chain finance and
customers' willingness to pay are the instruments that fit, not a green loan on a small balance."
**Result: half right.** The transition does run through suppliers and customers. But *bank* supply-chain finance
doesn't reach Carmen in any form that matters: she is far too small to anchor a programme, we found no programme run
by a food-and-beverage or packaging buyer in Hong Kong, and even inside one the ESG discount is worth hundreds of
dollars a year. The instruments that work are her own purchasing terms, her own price list, and one ESG rating used
several ways. And the willingness-to-pay hurdle is lower than we assumed: recycled PET resin traded **at the same
price as virgin** in Southeast Asia in October 2026.

---

## 1. Bottom line for Fahtai

1. **Carmen cannot anchor a supply-chain finance programme: no.**
   - Her purchases are about **US$3.4M a year** (HK$26.25M, ILLUSTRATIVE). One bank's published guide is
     **US$100M of annual trade spend** and an investment-grade or near-investment-grade buyer. She is at 1/30 of it.
   - No Hong Kong bank page we read states a minimum. Every programme we found is anchored by a large company:
     Towngas, CLP Power, Sanfield.

2. **Could she join a customer's programme as a supplier? Yes in principle; but none exists in her market that we
   could find.**
   - Hong Kong programmes found: Towngas with HSBC (2024, appliance-installation suppliers), CLP Power with HSBC
     (Jan 2026, "local suppliers"), Sanfield with DBS (2024, construction subcontractors).
   - We found **none run by a restaurant group, retailer or packaging buyer** in Hong Kong. Private programmes may
     exist unannounced (UNVERIFIED).

3. **The ESG part of the discount is unpublished, and small at her size.**
   - **No programme we checked publishes a basis-point figure.** We checked HSBC, Citi, DBS, Standard Chartered,
     CLP, Towngas, Sanfield, Santander–Sonae and Deutsche Bank–BASF. They say "preferential rates" or "tiered".
   - At an assumed 10–25bp, a HK$4M-a-year customer's programme is worth **HK$600–1,500 a year** to Carmen
     (ESTIMATED from ILLUSTRATIVE inputs).
   - The ordinary early-payment benefit is about **HK$14K a year**, and that benefit isn't green at all. It exists only
     if she funds her receivables with debt.

4. **The verification cost is about the size of the reward.**
   - An EcoVadis rating, the KPI most programmes use, costs a small company roughly **HK$3.9K–23K a year**
     (secondary sources; EcoVadis says only that the fee is "tailored").
   - The Hong Kong Green Organisation Certificate (HKGOC) is free, and HSBC's Sustainability Improvement Loan accepts
     it until 31 Dec 2026.
   - A rating pays only if customers require it anyway. **Buy one rating and use it four ways:** customer tenders,
     entry to any buyer's programme, a loan-rate step, and the buyer's due diligence in 2035–39.

5. **PLA "compostable" tableware is plastic in Hong Kong: yes.**
   - The EPD lists polylactic acid (PLA) as a regulated "biodegradable plastic", and PLA linings as regulated plastic
     linings.
   - **Phase 1 (since 22 Apr 2024):** PLA cutlery, straws, stirrers and plates are banned. PLA cups and containers are
     banned for dine-in only.
   - **Phase 2 (takeaway cups and containers) has no date:** it was "tentatively" 2025. The EPD's own packaging guide
     (revised Sep 2025) says it is "still premature to pursue biodegradable and compostable plastics as packaging
     alternatives".

6. **No public composting route takes PLA: no.**
   - The EPD's code for food-waste collectors counts packaging and utensils as "inert" and rejects loads over **20%**
     inert by weight.
   - One vendor (Vegware) claims a private collection loop into O·PARK. That claim is undated and UNVERIFIED.

7. **The recycled-PET green premium has nearly vanished at resin level.**
   - Platts assessed food-grade recycled PET pellets **at parity with virgin PET (US$1,240/t, FOB Southeast Asia)**
     in October 2026. In May 2026 recycled PET flake traded at a discount to virgin (search extracts).
   - Our 10% cost assumption (HK$328K a year, HK$3,030 a tonne CO2e) implies a resin premium of **US$641/t**. That is
     more than double the highest premium we found anywhere: US$295/t, US market, November 2023.
   - Re-costed, recycled content is **HK$0–151K a year, HK$0–1,395 per tonne**. At the 2023 peak that is about
     **1.4 HK cents per 12 g cup** (ESTIMATED; the cup weight is ILLUSTRATIVE).

8. **Who pays:**
   - **At today's prices nobody pays much for the resin.** The real costs are data, certification and food-contact
     checks (UNVERIFIED).
   - **At a 2023-style premium, the customer should pay**, as an itemised line priced in HK$ per tonne of CO2e.
     Absorbed by the business, it would cost Carmen about **HK$69K a year after tax**: 6–7 times the family's whole
     portfolio "price of values" (≈HK$9.4–11.9K).
   - **The family's values budget should not fund it.**

---

## 2. Facts table

### 2a. Sustainable supply-chain finance (SCF): banks, programmes, mechanics

| Fact | Number / text | Source (URL, date) | Tag | Confidence |
|---|---|---|---|---|
| **How SCF works (HSBC)** | <ul><li>"a facility set up by a buyer to help their suppliers access liquidity".</li><li>The supplier's invoice is approved by the buyer. The bank pays early and debits the buyer on the due date, priced on the **buyer's** credit.</li><li>The sustainable version "rewards and incentivises suppliers for adopting environmentally and socially responsible practices".</li><li>It "does not cost the buyer anything".</li><li>No tiers or basis points are given.</li></ul> | HSBC, *Explained: sustainable supply chain financing*, https://www.business.hsbc.com/en-gb/insights/explained-sustainable-supply-chain-financing, 14 Jul 2025 | SOURCED | High |
| **CLP Power + HSBC Sustainable Supply Chain Finance Programme** | <ul><li>Signed 28 Jan 2026.</li><li>"local suppliers" that meet "predefined ESG performance indicators based on third-party sustainability scoring" get "more flexible payment arrangements at preferential rates". The main focus is carbon measurement and reduction.</li><li>No basis points, no supplier count, no size floor.</li><li>CLP's own release could not be fetched (403).</li></ul> | HSBC HK press release, https://www.about.hsbc.com.hk/news-and-media/clp-power-and-hsbc-launch-sustainable-supply-chain-finance-programme, 29 Jan 2026 | SOURCED | High |
| **Towngas Green Supply Chain Finance Programme (HSBC)** | <ul><li>"the first sustainability-linked supplier payment solution by a utility company in Greater China".</li><li>Initially for appliance sales and installation suppliers.</li><li>KPIs on "emissions management, disclosure, and occupational health and safety"; early payment at lower rates; ESG training for suppliers.</li><li>No rates; no verifier named.</li></ul> | ESG Post, https://esgpost.com/towngas-and-hsbc-launch-green-supply-chain-finance-programme/, 26 Jul 2024 (secondary). SCMP, https://www.scmp.com/business/companies/article/3271900/ (not opened; the search extract says the target suppliers are "20 per cent to 30 per cent" of the relevant purchases) | SOURCED (secondary) | Medium |
| **DBS Hong Kong + Sanfield "Sustainability-linked Supplier Payment Services"** | <ul><li>First of its kind in Hong Kong construction.</li><li>Targets cover "ESG disclosure, safety performance, waste reduction, adoption of innovative technology and carbon-emissions reduction".</li><li>Suppliers and subcontractors get early payment.</li><li>No pricing, verifier, size or supplier count is stated.</li></ul> | DBS newsroom, https://www.dbs.com/newsroom/DBS_Hong_Kong_and_Sanfield_pave_the_way_for_green_construction_with_a_pioneering_sustainability_linked_supplier_payment_services_program_EN, 16 May 2024 | SOURCED | High |
| **DBS Sustainable Supply Chain Financing (product)** | <ul><li>Buyer and suppliers agree "joint sustainability linked KPIs"; suppliers get "differential pricing upon meeting these targets".</li><li>The buyer can "improve its own cash position by extending payment terms".</li><li>Buyers: "all DBS Corporate Customers"; no supplier criteria are given.</li></ul> | DBS (Singapore page), https://www.dbs.com.sg/corporate/sustainability/green-and-sustainable-trade-financing, accessed 5 Nov 2026 (undated) | SOURCED | High |
| **Citi Sustainability-linked SCF, Asia Pacific** | <ul><li>Launched with Henkel; first suppliers in Australia.</li><li>"preferential rates on a tiered basis with rates improving as a supplier's sustainability score improves", "at a rate lower than their usual cost of funds".</li><li>The rating agency is not named in the release; secondary sources say EcoVadis.</li><li>No basis points.</li></ul> | Citigroup press release, https://www.citigroup.com/global/news/press-release/2021/citi-launches-sustainability-linked-supply-chain-financing-in-asia-pacific, 1 Nov 2021 | SOURCED | High (date: current status UNVERIFIED) |
| **Standard Chartered** | <ul><li>Sustainable trade finance proposition (Mar 2021): supports "suppliers who meet acceptable thresholds against ESG ratings or metrics such as gender equality, responsible sourcing criteria and water use".</li><li>Sustainable Borrowing Base Trade Loan variants (Oct 2024), listed as available in Hong Kong.</li><li>No Hong Kong supplier programme or pricing found.</li></ul> | BusinessWire, https://www.businesswire.com/news/home/20210324005206/en/ (search extract); fintech.global, https://fintech.global/2024/10/22/standard-chartered-unveils-sustainable-finance-variants-to-boost-trade-loan-flexibility/ (secondary) | SOURCED (secondary) | Medium |
| **BOCHK** | <ul><li>First Sustainable Supplier Forum, 17 Apr 2026 (150+ of BOCHK's *own* suppliers); a "Green Supply Chain Strategic Partnership Alliance" in IT, professional services and engineering.</li><li>**No BOCHK SCF product for clients found.**</li></ul> | LinkedIn post (secondary), https://hk.linkedin.com/in/ivy-lee-a488918a | SOURCED (secondary) | Low |
| **Hang Seng** | <ul><li>No sustainable SCF programme found.</li><li>Nearest precedent: green receivables financing for Leo Paper Group, certified by SGS against the Green Loan Principles, with an HKECIC premium discount on green export credit insurance.</li></ul> | The Asset, https://www.theasset.com/article-esg/48917/hang-seng-delivers-leo-paper-green-financing, 3 Apr 2023; SGS, https://www.sgs.com/en-hk/news/2023/05/hong-kong-credit-insurance-corporation-launches-innovative-green-export-credit-insurance, May 2023 | SOURCED | Medium |
| **HSBC Sustainability Improvement Loan (SIL), Hong Kong** | <ul><li>For "mid-market and smaller businesses in Hong Kong"; covers "revolving credit facilities, term loans and selected trade finance products".</li><li>The margin is "linked to changes in borrowers' sustainability assessments and ratings from EcoVadis"; annual assessment for the life of the facility.</li><li>No basis points.</li><li>The campaign page adds the HKGOC option and enrolment until **31 Dec 2026** (see `area2_business.md`).</li></ul> | HSBC HK press release, https://www.about.hsbc.com.hk/news-and-media/hsbc-launches-sustainability-improvement-loan, 26 Sep 2024 | SOURCED | High |
| **A peer that used it: Finest Industrial** | <ul><li>"a family-owned plastic packaging manufacturer based in Hong Kong".</li><li>Its SIL is "a trade finance facility supporting its export contracts"; EcoVadis gold medal.</li><li>The rate "may" fall if the score improves and rise if it falls.</li><li>No basis points.</li></ul> | HSBC case study, https://www.business.hsbc.com/en-gb/insights/sustainability/how-a-packaging-manufacturer-used-its-sustainability-score-to-drive-business-growth, 12 Nov 2025 | SOURCED | High |
| HSBC sustainability-linked trade facility, Epic Group | <ul><li>A borrower's revolving trade facility, not a buyer programme.</li><li>KPIs: greenhouse-gas intensity, freshwater intensity, Higg Facility Environmental Module.</li><li>No pricing.</li></ul> | GTR, https://www.gtreview.com/news/sustainability/hsbc-rolls-out-first-sustainability-linked-trade-finance-deal-in-hong-kong/, 12 Jan 2022 | SOURCED (trade press) | High |
| Other programmes using EcoVadis scores | <ul><li>Santander–Sonae (Portugal and Spain): "preferential discount rates based on their ESG rating" (EcoVadis).</li><li>Deutsche Bank–BASF (China suppliers): preferential rates if the EcoVadis score improves; the lender "declined to say how many suppliers are participating".</li><li>**None publishes a figure.**</li></ul> | Santander, https://www.santander.com/en/press-room/press-releases/2022/05/santander-launches-first-sustainability-linked-supply-chain-finance-in-portugal, 11 May 2022; GTR, https://www.gtreview.com/news/asia/basf-puts-china-suppliers-on-deutsche-bank-sustainability-linked-payables-solution/ (search extract) | SOURCED | High on "no figure published" |
| **Basis points of the ESG discount** | Not published by any programme above | — | UNVERIFIED | — |
| **Minimum buyer size (indicative, US bank)** | "Investment-grade or near investment-grade credit profile; $100 million in annual trade spend" | Regions Bank SCF page, https://www.regions.com/commercial-banking/commercial-lending/business-capital/supply-chain-finance (search extract, undated) | SOURCED (US, secondary) | Medium as a guide; no Hong Kong bank publishes one |
| Minimum supplier size (historical) | Suppliers were onboarded only above "$1M minimum spend" because of KYC cost; the article says this is now easier | Kyriba, https://info.kyriba.com/wbn/untapped-working-capital-at-emerging-enterprises (search extract) | SOURCED (vendor, secondary) | Low |
| **EcoVadis fee** | <ul><li>Official: fees "tailored" by size, plan and location.</li><li>Secondary sources: US$500–11,000 a year for US companies; small-company examples €409 (Feb 2024) and US$2,979 (extra-small, Select plan).</li></ul> | https://support.ecovadis.com/hc/en-us/articles/360011788959; dcycle, https://dcycle.io/blog/ecovadis-pricing-plans-medals (secondary) | SOURCED (secondary) | Low–medium |
| **HKMA support** | <ul><li>Circular "Risk-based approach in supporting green transformation of corporate customers" (30 Sep 2025): shares tools banks "may adopt", "particularly SMEs"; imposes no new requirements.</li><li>Deputy Chief Executive Darryl Chan (forum 11 Sep 2026): a free greenhouse-gas calculator that works from energy and water bills, and a Grant Scheme refined to cover "advisory services in developing sustainable finance frameworks and transition plans".</li><li>**No HKMA supply-chain finance scheme.**</li></ul> | HKMA letter (Chinese PDF), https://brdr.hkma.gov.hk/chi/doc-ldg/docId/getPdf/20250930-4-TC/20250930-4-TC.pdf; summary, https://www.timothyloh.com/insights/latest-news/risk-based-approach-in-supporting-green-transformation-of-corporate-customers-20250930; BIS, https://www.bis.org/speeches/20261006-shaping-inclusive-transitions-asia-enhancing-smes-resilience-and-adaptation-climate-change (posted 6 Oct 2026) | SOURCED | High (circular content from a summary: Medium) |
| HKMA Grant Scheme | Loans need to be at least HK$100M | `area2_business.md` (HKMA guideline, 24 Apr 2026) | SOURCED | High |
| **HKECIC green export credit insurance** | <ul><li>A premium discount for exporters holding "relevant green certification" (first case: Leo Paper, 2023).</li><li>**Discount % not found.** Hotline 2732 9933.</li></ul> | The Standard, https://www.thestandard.com.hk/finance/article/51307/Export-credit-insurer-breaks-new-ground; SGS (above) | SOURCED | Medium; % UNVERIFIED |
| **DBS Hong Kong SME Sustainable Finance Programme** | <ul><li>Launched 14 Jan 2026. Proceeds "cannot be used for general working capital", but "trade facilities" are eligible loan types if the money funds an eligible green activity.</li><li>Eligible uses include "Repurposing materials or facilities for reusable, recyclable, and refurbished products".</li><li>"preferential rates" (no figure).</li><li>Reward: HK$1,000 per HK$500,000 drawn, capped at HK$5,000, for the first 40; dates shown are 31 Dec 2026, 28 Feb 2027 and the first 6 months of repayment.</li></ul> | https://www.dbs.com.hk/sme/sustainable-finance-programme, accessed 5 Nov 2026; https://www.dbs.com/newsroom/DBS_Hong_Kong_empowers_SMEs_sustainability_journey_with_new_SME_Sustainable_Finance_Programme_EN | SOURCED | High; whether buying recycled-content stock qualifies is UNVERIFIED |
| Hong Kong buyer in food, retail or packaging with an SCF programme | None found (searched restaurant groups, Dairy Farm, Maxim's, Café de Coral) | — | UNVERIFIED (absence of evidence) | Medium |

### 2b. Plastics law, PLA, composting and green claims

| Fact | Number / text | Source (URL, date) | Tag | Confidence |
|---|---|---|---|---|
| **What counts as plastic (EPD)** | <ul><li>Plastic: "a material consisting of a polymer, to which an additive or any other substance may have been added".</li><li>Regulated examples include "Biodegradable plastic", e.g. **PLA**, PHB and PBS, and "Plastic lining", e.g. **PE lining, PLA lining**.</li></ul> | EPD, https://www.cuttheplastics.hk/index.php/en/about-the-regulation-en.html (undated), accessed 5 Nov 2026 | SOURCED | High (EPD guidance; the ordinance text itself was not read) |
| **Why biodegradable plastics are covered** | "we suggest that the Regulation Scheme should cover disposable tableware made of all kinds of plastics, including oxo-degradable plastics and biodegradable plastics" (para 3.2, p.13) | EPD consultation document, https://www.epd.gov.hk/epd/sites/default/files/epd/english/environmentinhk/waste/pub_consult/files/tableware-con-doc-en.pdf, 2021 | SOURCED | High |
| Sustainable Development Council report, annexed to the LegCo Brief | "There is a lack of evidence that various 'new plastics'… including but not limited to biodegradable, compostable and bio-based plastics, would fully degrade in the actual and anaerobic landfill environment. Hence, any control measure on single-use plastics shall cover such 'new plastics' as well." (para 3.5) | LegCo Brief, https://www.legco.gov.hk/yr2023/english/brief/eeb20230208_20230208-e.pdf, Annex G, Feb 2023 | SOURCED | High |
| **Phase 1, from 22 Apr 2024** | <ul><li>Banned for sale, takeaway and dine-in: polystyrene tableware, straws, stirrers, cutlery and plates.</li><li>Plastic cups, lids, bowls and food containers "Can continue to be sold" and used for takeaway, but not for dine-in.</li></ul> | EPD page (above) | SOURCED | High |
| Exclusion | "Pre-packaged food or drink products (e.g. … plastic cutlery provided inside cup noodles…)" are excluded; tableware added after manufacture is not (para 7(a), as proposed) | LegCo Brief, Feb 2023 | SOURCED | High as proposed; final enacted wording UNVERIFIED |
| **Phase 2** | <ul><li>Feb 2023: "we tentatively intend to implement the second phase in 2025" (para 8).</li><li>8 May 2024: "There is no implementation timetable at present."</li><li>7 May 2025: "While there is no implementation timetable at the moment".</li><li>22 Apr 2026: "no word on when the next phase will be rolled out".</li><li>The EPD's Non-Plastic Container Trial Programme started mid-Aug 2025; containers for sauces, soups and drinks "require a higher standard of safety and sealing performance".</li></ul> | LegCo Brief; LCQ22, https://www.info.gov.hk/gia/general/202405/08/P2024050800233.htm; LCQ14, https://www.info.gov.hk/gia/general/202505/07/P2025050700299.htm; HKFP via https://news.spill.org/en/article/earth-day-2-years-on-from-single-use-plastic-ban-42-penalties-issued-but-no-sign-of-phase--382 | SOURCED | High: **no date** |
| Biodegradable tableware for takeaway now | "no specific requirements to reduce the use of biodegradable disposable plastic tableware at this stage" (reply to a question on PLA cups and containers still given to takeaway customers) | LCQ22, 8 May 2024 | SOURCED | High |
| **EPD packaging guide on compostables** | <ul><li>"It is still premature to pursue biodegradable and compostable plastics as packaging alternatives at this stage, as they may eventually harm the wildlife and ecosystems if treated improperly without suitable recycling and treatment infrastructures" (p.12).</li><li>Overseas examples cited have "no implication on the suitability in the context of Hong Kong".</li><li>It encourages "increasing the use of recycled content… where applicable to Hong Kong's context" (p.25).</li></ul> | EPD, *Practical Guides on Packaging Reduction and Management – Food Manufacturing Sector*, revision Sep 2025, https://www.wastereduction.gov.hk/sites/default/files/resources_centre/Practical_Guides_on_Packaging_Reduction_And_Management-Food_Manufacturing_Sector_ENG.pdf (I read the text). An Importer-sector edition exists (could not open) | SOURCED | High |
| Enforcement | <ul><li>To 22 Apr 2025: about 48,000 premises inspected, 144 written warnings, 21 fixed penalties of HK$2,000.</li><li>To end-Mar 2026: 282 complaints, 475 warnings, **42 fixed penalties**.</li><li>Penalties: maximum fine at level 6 (HK$100,000) and a fixed penalty of HK$2,000 (as proposed, para 13).</li></ul> | LCQ14, 7 May 2025; HKFP, 22 Apr 2026; LegCo Brief | SOURCED | High |
| Testing | "Testing or material analysis could determine whether or not a product contains plastic content" | LCQ14, 7 May 2025 | SOURCED | High |
| **Food-waste route** | <ul><li>"Examples of inert materials include packaging materials, plastic wraps and bags, plastic straws and utensils…"</li><li>"Food waste containing over 20% by weight of inert materials is not accepted."</li></ul> | EPD *Code of Practice on Separating, Collecting and Transporting Food Waste*, https://www.epd.gov.hk/epd/sites/default/files/epd/english/environmentinhk/waste/prob_solutions/files/CoPforCollector_eng_20171130.pdf (search extract; PDF dated 30 Nov 2017) | SOURCED | Medium (old, not opened) |
| **Conflict: a vendor's composting loop** | Vegware says O·PARK "now accepts Vegware disposables along with food waste" via its own collection points | Liv Magazine, https://liv-magazine.com/?p=18717 (undated, vendor-sourced) | UNVERIFIED | Low; contradicts EPD's guidance |
| Consumer Council | <ul><li>2021: "Consumers may be misled into believing that 'biodegradable' plastics are not harmful to the environment" (search extract).</li><li>11 Jul 2025: concerned about "the increasing prevalence of greenwashing" and recommends stronger "oversight of environmental and biodiversity claims".</li><li>**No Hong Kong green-claims law, guidance or prosecution found.**</li></ul> | https://www.consumer.org.hk/en/advocacy/consultation-papers/202109016 ; https://www.consumer.org.hk/en/advocacy/consultation-papers/20250711 | SOURCED | Medium |
| Trade Descriptions Ordinance (Cap. 362) | A false trade description of goods is an offence; up to HK$500,000 and 5 years on indictment; no green-claims case found | `area2_business.md` (Customs page) | SOURCED | High on penalty; its use for green claims is our inference |

### 2c. Prices, the green premium and willingness to pay

| Fact | Number / text | Source (URL, date) | Tag | Confidence |
|---|---|---|---|---|
| **Recycled vs virgin PET, Southeast Asia, Oct 2026** | Virgin bottle-grade PET US$1,240/t FOB Southeast Asia; food-grade recycled PET pellets "at the same price"; the spread "reaching zero for the first time since May" | S&P Global Commodity Insights (Platts), https://www.spglobal.com/energy/en/news-research/latest-news/chemicals/100726-recycled-virgin-pet-spread-hits-zero-amid-rising-virgin-feedstock-costs (≈7 Oct 2026; search extract, site returns 403) | SOURCED (search extract) | Medium |
| Recycled vs virgin, May 2026 | Recycled polymers at a discount to virgin "for the first time globally"; recycled PET clear flake **−US$373/t** against virgin, FOB Southeast Asia | S&P Global, https://www.spglobal.com/energy/en/news-research/latest-news/chemicals/051426-recycled-polymers-trade-at-discount-to-virgin-for-first-time-globally (≈14 May 2026; search extract) | SOURCED (search extract) | Medium |
| Historical premium (stress case) | US food-grade pellet premium over virgin **US$295/t** (early Nov 2023), from US$110/t (early May 2023) | Chemical Week citing Platts, https://chemweek.mydigitalpublication.com/november-6-13/page-29 (search extract) | SOURCED (US, search extract) | Medium; not Asia |
| Europe | Food-grade pellets over virgin: premium fell to €340/t from over €460/t (Mar 2026) | Argus, https://www.argusmedia.com/de/news-and-insights/latest-market-news/2798903-nwe-vpet-outstrips-rpet-for-first-time-in-2-years (search extract) | SOURCED (search extract) | Medium |
| **Asian buyers without mandates** | <ul><li>Pellets US$1,158/t (16 Jul 2026).</li><li>"In countries without mandatory recycled content regulations, buyers will naturally choose the cheaper option."</li><li>"Sustainability targets alone are currently insufficient to drive significant demand" (Indonesian recycler).</li></ul> | OPIS, https://www.opis.com/resources/energy-market-news-from-opis/asias-rpet-demand-subdued-despite-lower-prices-sources/, 17 Jul 2026 | SOURCED | High |
| Brand-owner pull | <ul><li>Q1 2026: "brand owners and packaging producers increased procurement to meet recycled content targets"; India's compliance named.</li><li>Pellets US$1,122–1,148/t, Jan–Mar 2026.</li><li>A Thai producer (Oct 2026): "If the price gap between recycled and virgin PET is low enough, big brands will certainly ramp up R-PET usage" (S&P search extract).</li></ul> | OPIS, https://www.opis.com/resources/energy-market-news-from-opis/asia-rpet-prices-up-in-q1-on-holiday-disruptions-mandates-mideast-conflict/, 16 Apr 2026 | SOURCED | High |
| EU Packaging and Packaging Waste Regulation (PPWR) recycled-content targets | <ul><li>From 2030: 30% for contact-sensitive PET, 10% for other contact-sensitive plastics, 30% for single-use drinks bottles, 35% for other plastic packaging.</li><li>2030 start: or 3 years after the implementing act, if later.</li><li>Non-EU recycled content counts only if collected to equivalent standards.</li></ul> | Secondary summaries (e.g. https://projetcelsius.com/en/blog/ppwr-recycled-plastic-content-targets/); EUR-Lex Art. 7 not read | SOURCED (secondary) | Medium; applies only to packaging placed on the EU market |
| **Cost of non-plastic tableware, Hong Kong, Feb 2024** | <ul><li>Wooden cutlery 10 HK cents, "4 cents more than plastic".</li><li>Paper straw 1 cent cheaper.</li><li>Polystyrene container about 34 cents; switching to other plastic +14 cents a box.</li><li>Source: Sing Tao quotes from 50 manufacturers.</li></ul> | The Standard, https://www.thestandard.com.hk/news/article/60680/Earth-friendly-yet-pocket-friendly, 26 Feb 2024 | SOURCED (press) | Medium |
| Same, from the trade and the Executive Council | <ul><li>Executive Councillor Lam Ching-choi: "non-plastic substitutes are just 10 to 20 cents more expensive".</li><li>A restaurant owner: recyclable materials "around HK$3 to HK$4" against polystyrene at about HK$1. Passing it on would cut sales.</li></ul> | The Standard, https://www.thestandard.com.hk/news/article/213375/Upcoming-plastic-tableware-ban-will-hike-restaurant-operating-costs-catering-representatives, 13 Feb 2024 | SOURCED (press) | Medium (anecdotes) |
| "30% pricier" | A catering federation figure for alternatives | Search extract; source article not identified | UNVERIFIED | Low |
| Government on prices | "several alternative options available in the market with steady reduction in prices" | LCQ14, 7 May 2025 | SOURCED | High (qualitative) |
| **Consumer willingness to pay** | <ul><li>"66% are willing to pay more for sustainable packaging when ordering takeaways": **no amount asked**. Deliveroo; n = 1,000; fieldwork 6–12 Sep 2022.</li><li>More than 60% think recycling non-plastic tableware "would not help reduce waste"; about 70% don't bring their own utensils. Greenpeace / Hong Kong Public Opinion Research Institute, May 2024.</li></ul> | Marketing-Interactive, https://www.marketing-interactive.com/two-thirds-customers-in-hk-prefer-takeaways-sustainable, 2 Nov 2022; The Standard, https://www.thestandard.com.hk/news/article/218109/Over-60pc-believe-switching-to-non-plastic-tableware-will-not-help-reduce-waste-survey, 5 Jul 2024 | SOURCED | Medium (stated preference, platform-sponsored) |
| Merchant cost pass-through after April 2024 | No survey found that measures it | — | UNVERIFIED | — |
| Hong Kong B2B premium paid for recycled content | No evidence found | — | UNVERIFIED | — |

---

## 3. A supply-chain structure for Carmen's business (with arithmetic)

### 3a. Option (a): Carmen anchors a programme for her mainland suppliers. **Refuse.**

- **Size:** purchases are HK$26.25M ÷ 7.8 = **US$3.37M a year**, which is **3.4%** of one bank's US$100M guide.
- **Credit:** a buyer programme is priced on the buyer's credit. Carmen's company is unrated, has HK$10M of equity
  (ILLUSTRATIVE), and its owner guarantees its only loan.
- **Onboarding:** her suppliers are Pearl River Delta factories, so every one is a cross-border know-your-customer
  case for a Hong Kong bank.
- No Hong Kong bank page offers anything at this scale.
- **Verdict:** the label "supply-chain finance" doesn't fit her buying side. The idea behind it does: pay early in
  exchange for performance (§3c).

### 3b. Option (b): Carmen joins a large customer's programme. **Accept only if offered, and only if payment terms don't lengthen.**

Assumptions (ILLUSTRATIVE):
- One listed restaurant or retail customer buys **HK$4M a year** (11.4% of sales) on 60-day terms.
- The bank pays her on day 5.
- Her own working-capital cost is prime 5.00% (SOURCED) + 1.00% = 6.00%.
- The programme rate is 1-month HIBOR 2.64% (SOURCED, 4 Nov 2026) + 1.00% (buyer's spread) = 3.64%.

| Line | Arithmetic | HK$ a year | Tag |
|---|---|---|---|
| Amount financed on average | 4,000,000 × 55 ÷ 365 | 602,740 | ESTIMATED |
| Her own funding cost | × 6.00% | 36,164 | ILLUSTRATIVE |
| The programme's cost | × 3.64% | 21,940 | ILLUSTRATIVE |
| **Ordinary benefit of supply-chain finance** (not green) | 36,164 − 21,940 | **14,225** | ESTIMATED |
| **ESG discount ("greenium")** at 5 / 10 / 25bp | 602,740 × bp | **301 / 603 / 1,507** | ESTIMATED; basis points UNVERIFIED |
| Cost of the KPI: an EcoVadis rating | US$500–2,979 × 7.8 | **3,900–23,236** | ESTIMATED from secondary sources |
| Same, using the HKGOC instead | Free. HSBC's loan accepts it; whether buyer programmes accept it is UNVERIFIED (CLP says "third-party sustainability scoring") | ≈0 | SOURCED / UNVERIFIED |

**Reading it:**
- **The green part can't pay for its own verification.** At 25bp the rating pays for itself only if
  HK$1.56–9.3M sits in programmes (3,900–23,236 ÷ 0.25%).
- **The ordinary part helps only if she borrows.** If she funds receivables from cash earning about 2.5%, the
  programme costs her **HK$6,871 a year more** than waiting to be paid (21,940 − 15,068).
- **The trap:** DBS's own product page says the buyer can "improve its own cash position by extending payment terms".
  If a customer offers its programme alongside a move from 60 to 120 days, Carmen pays to get her own money back.
  The rule: compare against today's terms, not against the new ones.
- **Correction to `area2_business.md`.** Its "HK$28.8K a year" assumed all HK$5.75M of receivables in programmes at
  50bp. No source gives 50bp, and only customers with programmes count. The upper bound at 25bp is
  **HK$14.4K a year**, and the realistic figure is HK$0–1,500 (ESTIMATED).

### 3c. What works instead: three moves that cost little and use her own contracts

| # | Move | Instrument | Arithmetic | HK$ a year | Tag |
|---|---|---|---|---|---|
| 1 | **One ESG rating, used four ways** | EcoVadis (or the free HKGOC first) | Cost 3,900–23,236. It is the entry ticket to buyers' tenders and any buyer programme, the KPI for an HSBC Sustainability Improvement Loan rate step (enrol by **31 Dec 2026**), and a credential for the 2035–39 buyer | −3.9K to −23K | ESTIMATED |
| 2 | **Conditional early payment to her PET supplier** ("dynamic discounting", funded from her own cash) | Pay 30 days early if the supplier gives (i) a product carbon footprint, (ii) a recycled-content certificate, and (iii) a 0.5% discount | <ul><li>PET purchases 131 t × HK$25/kg = 3,275,000.</li><li>Cash tied up: × 30 ÷ 365 = 269,178.</li><li>Cost of that cash: 6,729 at 2.5%, 14,805 at 5.5%.</li><li>Discount: 0.5% = 16,375, equal to a 6.1% annual rate for the supplier.</li></ul> | **+1.6K to +9.6K** net, and it buys the supplier data that `area2_business.md` calls "the first project" | ILLUSTRATIVE (the supplier's acceptance is UNVERIFIED) |
| 3 | **A green trade line for recycled or reusable stock** | DBS SME Sustainable Finance Programme (trade facilities allowed; "reusable, recyclable, and refurbished products" eligible) or an HSBC SIL trade line | <ul><li>Reward: HK$1,000 per HK$0.5M drawn, capped at HK$5,000.</li><li>Rate step on a HK$3M line at 10–25bp: 3,000–7,500.</li><li>Breaks even with an EcoVadis rating only above HK$1.56–9.3M at 25bp.</li></ul> | +3K to +12.5K, once | ESTIMATED; whether a stock purchase qualifies is UNVERIFIED (ask DBS) |

**Comparing the instruments the brief names** (for one slide or the price card):

| Instrument | Tenor | Covenants and verification | Verification cost | Grant Scheme subsidy | Worth to Carmen |
|---|---|---|---|---|---|
| Green loan (vans) | 5 years | Use of proceeds; self-certified or the bank's framework | HK$0–12K | None (needs ≥HK$100M) | Greenium ≈HK$0 net (`area2_business.md`) |
| Sustainability-linked loan / HSBC SIL | Facility life | KPI tested annually; EcoVadis or HKGOC | HK$0–23K a year | None | HK$450–7,500 a year |
| Customer's sustainable supply-chain finance | Invoice by invoice (60 days here) | No covenant for the supplier; KPI from third-party scoring | HK$0–23K a year | None | HK$300–1,500 green; HK$14K ordinary, only if she borrows |
| Own conditional early payment | Invoice by invoice | Her own contract terms | ≈0 (the supplier supplies the data) | n/a | +HK$1.6–9.6K, plus the supplier data |
| Transition finance | — | Needs an entity-level transition plan | Review fee | Needs ≥HK$100M | Doesn't fit (`area2_business.md`) |

**Bankability (brief area 2, bullet 3):**
- Moves 2 and 3 add no long-term debt. Move 2 uses about HK$0.27M of cash, under a fifth of a year's retained profit
  (HK$1.43M; `area2_business.md`).
- Debt service cover is unchanged from `area2_business.md` (3.3× after the vans).
- The real bankability test for the recycled range is **offtake**: a customer's written commitment to buy it at a
  stated price (§4).

### 3d. The strongest case against this view
- **A practitioner may say "supplier finance is about to arrive for SMEs."** Platforms such as Taulia and EcoVadis
  now offer one score across several working-capital products. The HKMA is pushing banks toward SMEs (circular,
  Sep 2025). CLP's programme names "local suppliers" with no size floor.
- **How much this worries us: moderately.** None of it changes the arithmetic: the green tier is worth hundreds of
  dollars at HK$4M of sales. The value is in *being on the list*, and that is a customer-retention argument (about
  HK$209K of Carmen's stake per 1% of sales; `area2_business.md`), not a pricing one.

---

## 4. The green premium and who pays it

### 4a. What recycled content really costs now (re-costed)

PET range: 131 t. At 50% recycled content that is 65.5 t, cutting **108.1 t CO2e** a year (`area2_business.md`'s DESNZ
factors).

| Scenario | Resin premium | HK$ a year (65.5 t × premium × 7.8) | HK$ per t CO2e | Per 12 g cup at 50% recycled | Tag |
|---|---|---|---|---|---|
| Southeast Asia parity, Oct 2026 | US$0/t | **0** | **0** | 0 | ESTIMATED from a search extract |
| US, May 2023 | US$110/t | 56,199 | 520 | 0.5 HK cents | ESTIMATED |
| **Stress: US, Nov 2023 peak** | **US$295/t** | **150,716** | **1,395** | **1.4 HK cents** | ESTIMATED |
| *Our earlier assumption* | *10% of product price = US$641/t of recycled resin* | *327,500* | *3,030* | *3.1 HK cents* | ILLUSTRATIVE, **too high** |

Checks:
- Resin is about **39%** of her HK$25/kg PET purchase price (US$1,240 × 7.8 ÷ 1,000 ÷ 25).
- A 10% product premium therefore means a 52% premium on the recycled resin (US$641 ÷ US$1,240). That is not seen in
  any market we found.
- **Not in the table** (UNVERIFIED): the converter's margin for food-contact recycled sheet; chain-of-custody
  certification (e.g. the Global Recycled Standard); food-contact compliance of recycled PET made in the Pearl River
  Delta. **These, not the resin, are probably now the real green premium.**

**The Phase 2 catch.**
- Recycled PET cups and containers are still plastic. When Phase 2 arrives they will be banned for takeaway, the same
  as virgin ones.
- So point recycled content at **packaging outside the tableware rules**: pre-packaged food (excluded, LegCo Brief
  para 7(a)), retail trays and clamshells. Point fibre at tableware.
- Keep tableware stock short (the PLA lesson in `area2_business.md`: about HK$0.77M exposed).

### 4b. Who pays: three candidates

| Payer | At today's ≈US$0 premium | At the stress premium (HK$151K a year) | Evidence | Verdict |
|---|---|---|---|---|
| **Carmen's business** | <ul><li>Data and certification only: rating HK$3.9–23K; footprint work about HK$50K (`area2_business.md`, ILLUSTRATIVE).</li><li>Certification UNVERIFIED.</li></ul> | <ul><li>EBITDA −7.0% (151 ÷ 2,150).</li><li>Company value −HK$769K at 5.1×; Carmen's stake **−HK$384K**.</li><li>Her after-tax income **−HK$69K a year** (151K × 0.9175 × 50%).</li></ul> | OPIS: Asian buyers without mandates "choose the cheaper option" | **Pay the data, not the premium** |
| **Her customers** | ≈0 extra per item: offer recycled content at the same price | <ul><li>Pass-through **+3.45%** on the PET range (151K ÷ HK$4.37M sales).</li><li>**1.4 HK cents per cup**, against the 4–20 cents a piece merchants already absorbed in 2024 for non-plastic substitutes.</li><li>Priced as **HK$1,395 per t CO2e**, about twice the EU carbon price (€75–82 ≈ HK$638–697; FX assumed at 8.5).</li></ul> | Restaurants complained about 4–20 cents a piece, yet more than 70% had switched within a month (search extract, The Standard). Listed customers need lower Scope 3 Category 1 figures (HKEX; `area2_business.md`) | **They should pay any premium above parity**, as an itemised line with the tonnes it buys |
| **The family's values budget** | n/a | <ul><li>HK$69K a year after tax is **5.8–7.4 times** the whole portfolio's price of values (≈HK$9.4–11.9K; `area1_6_framework.md`).</li><li>Adrian would be paying, through the shared household, for his customers' emissions.</li></ul> | — | **No.** It mixes the household's money with the business's sales decision. Keep the values budget for the portfolio and for funded giving |

### 4c. The greenium against the green premium, in one line
- **The greenium** (the supply-chain finance ESG discount) is **HK$600–1,500 a year**.
- **The green premium** is **HK$0–151K a year**. At the 2023 premium, the greenium covers **0.4–1.0%** of it.
- At today's parity there is little premium to cover. What remains is the data cost, which a finance discount doesn't
  pay for either.
- **The planner's sentence:** "The bank's green price doesn't move this decision. The customer's price does, and so
  does the law on plastic."

Two corrections to `area2_business.md` (for Fahtai to apply there):
1. The recycled-PET row of the abatement curve, **+HK$3,030 a tonne**, should become a range: **HK$0–1,395 a tonne
   at resin level**, plus unpriced certification. That moves recycled content from the right of the curve toward
   zero.
2. The "HK$28.8K a year" supply-chain finance line should read **HK$0–1,500 realistic, HK$14.4K upper bound** (§3b).

---

## 5. Likely judge questions, with short answers

1. **"Why not set up a green supply-chain finance programme for your mainland suppliers?"**
   Her purchases are US$3.4M a year, against one bank's guide of US$100M of trade spend and an investment-grade
   buyer. She does the same thing with her own cash: pay 30 days early in return for a footprint, a recycled-content
   certificate and a 0.5% discount. It nets about HK$2–10K a year and gets her the data.

2. **"What discount does a sustainability-linked programme give?"**
   None of nine programmes we checked publishes one: HSBC, Citi, DBS, Standard Chartered, CLP, Towngas, Sanfield,
   Santander, Deutsche–BASF. At an assumed 10–25bp it is worth HK$600–1,500 a year on a HK$4M customer. The value is
   being on the buyer's approved list.

3. **"Isn't supplier finance a way for big buyers to squeeze small suppliers?"**
   It can be. DBS's own page says the buyer can extend payment terms. Our rule: join only if terms don't lengthen. And
   it helps only if Carmen borrows to fund her receivables. From cash it costs her about HK$7K a year more.

4. **"Will customers pay for recycled content?"**
   Asian buyers without mandates choose the cheaper option (OPIS, Jul 2026). But in October 2026 recycled PET resin
   cost the same as virgin in Southeast Asia, so the question is now mostly about certification and data. Even at
   2023's peak premium it is 1.4 HK cents a cup. In 2024, merchants absorbed 4–20 cents a piece for non-plastic
   substitutes.

5. **"Your client sells 'compostable' PLA. Isn't that the green product?"**
   Not in Hong Kong. The EPD counts PLA as plastic. Its own packaging guide (Sep 2025) calls compostables
   "premature". And food-waste collectors reject loads over 20% packaging and utensils. One vendor claims a private
   loop into O·PARK; we couldn't verify it. So no "compostable" claims to customers.

6. **"What happens to your recycled-PET cups when Phase 2 comes?"**
   They're plastic, so they will be banned for takeaway with the rest. That is why recycled content goes into
   pre-packaged and retail packaging, which sits outside the tableware rules, and fibre goes into tableware. Phase 2
   has had no date since the 2025 target lapsed.

7. **"Separate the greenium from the green premium for us."**
   Greenium: the finance discount, HK$600–1,500 a year. Green premium: the extra cost of the lower-carbon product,
   HK$0–151K a year depending on the resin market. The first covers at most 1% of the second. So the decision turns
   on the customer's price and the law, not on the bank.

8. **"66% of Hong Kong people say they'll pay more for green packaging."**
   That 2022 survey was sponsored by a delivery platform and asked no amount. It is a stated preference, which is the
   social-desirability bias the brief's area 6 warns about. We price from revealed behaviour instead: what buyers do
   when recycled content costs more.

9. **"Who verifies the KPI?"**
   - In the programmes: EcoVadis (HSBC's loan, Santander, BASF) or "third-party sustainability scoring" (CLP).
   - For Carmen: start with the free HKGOC; buy EcoVadis only when a customer asks for it.
   - For recycled-content claims: a chain-of-custody certificate. Its cost is UNVERIFIED.

10. **"Does any Hong Kong government scheme help?"**
    - We found no green supply-chain finance scheme.
    - The Grant Scheme needs HK$100M of debt.
    - The HKMA's Sep 2025 circular nudges banks toward SMEs, with no new rule, and there is a free carbon calculator.
    - HKECIC discounts green export credit insurance, but only if she exports, and the percentage isn't published.

11. **"Will your restaurant customers really ask for data?"**
    - Mandatory Scope 3 applies to LargeCap issuers only, from financial years starting in 2026.
    - We couldn't verify which of Hong Kong's listed restaurant groups are LargeCap; some may only "comply or explain".
    - Multinational brands' own targets are the other pull, also UNVERIFIED for her customers.
    - That is why the rating comes first and the expensive footprint work waits for a request.

---

## 6. Open items and what is unverified

**Questions to put to a bank or organisation (Fahtai, before 16 Nov if any is to reach a slide)**
- **HSBC:** the Sustainability Improvement Loan's rate step in basis points, and whether a trade line qualifies with an
  HKGOC certificate rather than EcoVadis.
- **CLP:** the programme's supplier size floor and its scoring provider.
- **DBS:** whether a trade facility used to buy recycled-content or reusable stock counts as "pollution prevention",
  and the "preferential rate".
- **HKECIC:** the green premium discount percentage and which certificates qualify.

**UNVERIFIED**
- Any published basis-point figure for an ESG supply-chain finance tier, anywhere.
- Whether any Hong Kong restaurant, retail or packaging buyer runs a supplier finance programme (none announced).
- A Hong Kong bank's minimum programme or supplier size. The US$100M guide is a US bank's; the US$1M supplier floor
  comes from a vendor.
- EcoVadis's fee for a Hong Kong company of 14 staff (only secondary US and EU figures found).
- The S&P Global and Argus price figures, read from search extracts (the sites refuse fetches); and an Asian
  (not US) recycled-PET premium series for 2025.
- The converter's premium for food-contact recycled-PET sheet; Global Recycled Standard (or similar) certification
  cost; mainland and Hong Kong food-contact rules for recycled PET.
- Item weights (the 12 g cup is ILLUSTRATIVE).
- Whether suppliers in the Pearl River Delta would accept 0.5% for 30 days early (an annual rate of 6.1%).
- The enacted wording of Cap. 603's definitions and exclusions (e-Legislation didn't render). EPD guidance and the
  LegCo Brief were read instead.
- Whether O·PARK accepts any certified-compostable packaging through a vendor loop (Vegware's undated claim against
  the EPD's code).
- Merchants' cost pass-through after April 2024 (no survey found); the source of the "30% pricier" figure.
- The PPWR's exact Article 7 text (secondary summaries only). It touches Carmen only through EU-bound customers.
- Which Hong Kong restaurant groups are Hang Seng Composite LargeCap constituents.

**For the team**
- If any number here reaches a slide, it is ESTIMATED from ILLUSTRATIVE inputs, not a model output. Decide whether
  the business arithmetic should go into `export_numbers()` (owner: Pete). The family's money stays at HK$3.0M from
  the sale, as before.
- Apply the two corrections in §4c to `area2_business.md` (owner: Fahtai).
