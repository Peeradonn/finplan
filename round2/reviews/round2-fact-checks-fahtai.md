# Round Two fact checks (Fahtai)

From Fahtai (model and numbers) · 23 Oct 2026 · for Pete

These are the three facts the deck plan (§8, "Evidence the deck is waiting for") assigns to me. All figures are current
as of October 2026 and were researched from official sources: vhis.gov.hk, hkmc.com.hk, hkmca.hk, info.gov.hk and hkma.gov.hk.
Model runs use the repo at `0586b8b` (main, 22 Oct).

## Summary

| # | Question | Answer | What to change |
|---|---|---|---|
| a | Can the parents switch from Flexi to Standard at Adrian's 75 without new medical checks? | **Yes, guaranteed by the VHIS rules**, at any renewal, with no age limit | Slide 7 notes: drop "subject to underwriting"; say "guaranteed under the VHIS rules". The 97% holds |
| b | Could "their own way" take a reverse mortgage at 83 instead of selling the flat? | **Yes, she could stay home**: about HK$916K a year as paid in 2060 (≈HK$396K in today's money). **But in our model the money runs out more often** (lasts 51% vs 62% selling), because a fixed payout doesn't keep up with her bills | Keep "sells" on slide 3, add one line to the notes (suggested wording below). Optionally soften the title |
| c | If Adrian dies soon after buying the HKMC annuity, does the family lose the money? | **No.** The family gets back at least 100% of the premium (lump sum) or 105% (monthly payments) | Slide 6 notes: one line (below). Two policies, since it's single life only. Carmen's MPF at 62 still to confirm |

---

## (a) VHIS: Flexi → Standard at 75

**What the deck assumes.** Both parents hold an individual VHIS Flexi Plan, bought before group cover ends. At Adrian's
75 (2047) they move to the same insurer's Standard Plan, which costs about a third as much. This move takes the odds
from 83% to 97% (`switch_89`).

**What the rules say.** The switch is a right under the scheme, not left to the insurer.

- **VHIS FAQ for insurers, Q30 (25 Sep 2025):** "as in the case of all Flexi Plans, the VHIS Providers are required to
  provide the policy holders with the option … to switch to the Standard Plan without re-underwriting upon policy
  renewal." https://www.vhis.gov.hk/doc/en/information_centre/e_insurer_faq.pdf
- **Code of Practice for Insurers, s.2.11 (version as at 1 Jul 2022):** for existing Flexi holders, the insurer "should
  also offer the Standard Plan as the fall-back renewal option". Under s.1.4 it must keep renewing Certified Plans even if it leaves
  the scheme. https://www.vhis.gov.hk/doc/en/information_centre/e_cop.pdf
- **Standard Plan policy template, Part 4 (version as at 1 Jul 2022):**
  - renewal is guaranteed "up to the Age of one hundred (100) years";
  - the insurer cannot add new premium loading or exclusions "by reason of any change in the Insured Person's health conditions";
  - re-underwriting is allowed only when the policyholder asks for more cover, so moving down to Standard can't trigger it.

  https://www.vhis.gov.hk/doc/en/information_centre/e_standard_plan_template.pdf
- **Government launch notice (1 Mar 2018):** "guaranteed renewal up to 100 years of age (without re-underwriting)" is a minimum
  requirement. https://www.info.gov.hk/gia/general/201803/01/P2018030100438.htm

**No age limit** applies to the switch. It attaches to every renewal, and renewal is guaranteed to 100, so 75 is well inside.

**Caveats for the notes:**
1. **Timing.** The switch happens at each policy's renewal date, so the two policies may switch at different times in 2047–48.
2. **Old exclusions likely stay.** No *new* exclusions or loading can be added, but anything set when they first bought
   probably carries over. That's a strong inference from the template; no text says it outright. Say "no new
   exclusions", not "every condition covered".
3. **Flexi extras are lost**, such as higher limits and room upgrades. Getting them back later needs underwriting, and
   Bupa says reversing a move "isn't guaranteed". https://bupa.com.hk/en/about-vhis/vhis-migration
4. **Premiums still rise with age** for the whole pool, but never because of one person's health.
5. **The rules could change.** The Code is a condition of insurers' registration, not law.

**Premium check (optional).** Bowtie's comparison puts the Standard Plan at about HK$8.8K–16.4K a year at age 70 and
HK$12K–23.7K at age 80, in today's money. https://www.bowtie.com.hk/blog/en/learn/vhis-compare-standard-plan/ I found
no same-insurer Flexi-to-Standard ratio at 75, so "about a third" stays our model's estimate from the VHIS age curve.

**Suggested slide 7 note:** *"The switch is guaranteed: under the VHIS rules, every Flexi policyholder can move to the
Standard Plan at renewal without new medical checks, at any age (VHIS Code of Practice s.2.11; FAQ Q30)."*

---

## (b) HKMC reverse mortgage at about 83

**What the deck assumes.**
- **Slide 3, "their own way":** when the money runs out, usually at about 83 (79–87), Carmen sells the flat and downsizes.
- **Slide 6, our plan:** a reverse mortgage from 2037 paying HK$230K a year for life (`rmp_income`).

### The current programme (HKMC, table in effect from 10 Mar 2026)

**Property value counted:**
- 100% of the valuation up to HK$8M, plus **only 50% above HK$8M**, capped at HK$25M.
- A HK$11.5M flat counts as HK$9.75M.
- The "HK$15M" rule is out of date (replaced in July 2021).

**Monthly payout per HK$1M counted, single borrower:**

| Age | Fixed, life | Floating, life |
|---|---|---|
| 60 | 2,020 | 1,840 |
| 65 | 2,500 | 2,270 |
| 70 | 3,070 | 2,790 |
| 75 | 3,960 | 3,600 |
| 80 | 4,780 | 4,420 |
| **83** | **5,640** | **5,270** |
| 85 | 6,400 | 6,030 |
| 90 | 9,130 | 8,750 |

- **Joint borrowers get less**, and the rate uses the youngest borrower's age. For example, two borrowers at 65 get 2,200 fixed.
- **No gender split** in the tables. **No maximum age** (55+, and the table runs to 100).
- **She can stay for life.** The loan is non-recourse: if the sale falls short, HKMC Insurance covers the gap.
- **Costs:**
  - interest 4% fixed for the first 30 years, cut from 4.5% on 10 Mar 2026;
  - insurance 1.25% a year on the balance (one 2021 source says 1.5% for the fixed-rate plan, unresolved);
  - an upfront premium of 1.96% of the counted value, added to the loan in years 3–9.
- **The table moves with interest rates.** The age-60 fixed figure ranged from HK$1,930 to HK$2,590 between 2021 and 2026.

**Sources:**
- Programme page: https://www.hkmc.com.hk/chi/our_business/reverse_mortgage_programme.html
- Payout table (March 2026): https://www.hkmc.com.hk/files/product_file/1/1471/C_Level%20of%20Monthly%20Payout%20and%20Maximum%20Lump-Sum%20Payout%20Amount%20at%20Closing%20%28March%202026%29.pdf
- Information pack: https://www.hkmc.com.hk/files/product_file/1/1509/C_HKMC%20RMP%20Info%20Pack.pdf
- Press release, 9 Mar 2026: https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/03/20260309-3

⚠ I read the payout PDF through a summarising tool. The ages that also appear on HKMC's web page match, but **check the
age-83 row in the PDF itself** before it goes on a slide.

### What it would pay Carmen

At today's flat value of HK$11.5M (counted HK$9.75M), age 83, fixed rate, for life: **HK$54,990 a month, about HK$660K a
year.**

The more accurate figure uses the model's own flat value in the year it happens (1.5% a year growth):

| Year | Carmen | Flat (as paid) | Payout, as paid | Payout, today's money |
|---|---|---|---|---|
| 2056 | 79 | HK$18.0M | HK$719K a year | HK$343K |
| **2060** | **83** | **HK$19.1M** | **HK$916K a year** | **HK$396K** |
| 2064 | 87 | HK$20.2M | HK$1.27M a year | HK$497K |

This assumes HKMC's HK$8M threshold stays fixed, the age payout rates are interpolated, and today's table applies.

### What our model says: a late reverse mortgage doesn't rescue their own way

I tested it in the model (a separate test script; `run_model.py` itself is unchanged). The setup is "their own way" as on slide 3, except that
the first time the money runs out, Carmen takes an HKMC reverse mortgage for life at her age that year, instead of
selling the flat.

| Their own way, 10,000 markets | Money lasts to Carmen's 89 | Flat sold or mortgaged | Median age |
|---|---|---|---|
| Sell the flat when the money runs out (deck) | **62%** | 51% | 83 |
| Reverse mortgage instead of selling | **51%** | 51% | 83 |
| Reverse mortgage, survivor budget 70% | 63% | 40% | 83 |

**Why it's worse.** The payout is a fixed amount for life. At 83 it is about HK$396K a year in today's money, while her
bills are the full budget plus Flexi premiums of up to HK$375K a year. Selling releases a lump sum that lasts longer. So
she can stay in the home, but in about half of these futures the money still runs out before 89.

### Is our HK$230K from 2037 right?

Mostly, if Carmen is on the loan.
- **Value counted in 2037:** the flat is worth about HK$13.5M as paid, so the counted value is about HK$10.75M.
- **Single borrower at 65:** today's table gives about HK$323K a year (fixed), so HK$230K would be conservative.
- **Carmen on the loan:** she must be, to stay in the flat after Adrian's death, since the loan falls due nine months
  after the last borrower dies. Then the rate uses her age, about 60, and the joint table.
  - Single at 60: about HK$261K.
  - Joint at 60: the table row wasn't retrieved, but it is lower, roughly HK$230K.
- **So HK$230K is about right for a joint loan with Carmen at 60. Don't call it conservative on a slide.**

### Suggestions for the deck

1. **Recommended: keep slide 3 as it is and add a note.** The model measured selling, and selling is the better of the two options for their own way, so "sells" is defensible.
   Suggested slide 3 note:
   > *"Why not a reverse mortgage at 83? It would let Carmen stay: about HK$400K a year in today's money for life
   > (HKMC, March 2026 table). But it's fixed and doesn't cover her bills: the money then lasts to 89 in only 51%,
   > worse than selling (62%), and the loan eats into what Ryan and Chloe inherit."*
2. **Optional title change:** "Their own way, Carmen sells **or mortgages** the family home at about 83, and the children's
   inheritance pays the bills". It's accurate, but longer and less vivid. My preference is option 1.
3. **Make it official (if Pete wants it on screen):** add the late reverse mortgage as a model variant in `export_numbers()`
   (e.g. `own_rm_89`), using the March 2026 table, so the 51% is a `{{key}}` and not a typed number.
4. **Slide 6 is unaffected.** It's still "decide now, at 65", and that is the plan's real advantage: an income for 30 years
   instead of a smaller one for the last few, plus a choice made in calm.

---

## (c) HKMC Annuity Plan: if Adrian dies early

**What the deck assumes.** Adrian (2037, at 65) and Carmen (2039, at 62) each buy a single-life HKMC annuity with
their MPF. These are fixed HK$ payments for life (decision 4 on slide 6).

**The death benefit.** Under the "Guaranteed Period", payments are guaranteed until they total **105% of the premium**.
If the insured dies within that period, the beneficiaries choose one of two options:
- **keep receiving the monthly payments** until 105% of the premium has been paid; or
- **take a lump sum**: the higher of the Guaranteed Cash Value or **the premium minus the payments already received**.

If they don't choose within 30 days, they get the lump sum. With no named beneficiary, it goes to the estate. After the
Guaranteed Period there is no death benefit and no surrender value.

Sources:
- Product brochure LAS(04/2024): https://www.hkmca.hk/eng/files/Product_brochure_E.pdf
- FAQ: https://www.hkmca.hk/eng/information_centre/faq.html
- Investor and Financial Education Council: https://www.ifec.org.hk/web/en/retiree/annuity/insurance-surrender.html

**Worked example (Adrian, HK$1M at 65, today's rates).**
- He receives HK$5,800 a month.
- If he dies after 12 payments, the family has had HK$69,600.
- They then get at least **HK$930,400 as a lump sum** (HK$1.0M in total) or **HK$980,400 in monthly payments** (HK$1.05M in total).
- His guarantee runs about 181 payments, to roughly age 80. Carmen's runs about 213 payments, to roughly age 79–80.
- **The only real loss is the investment return, not the premium.**

**Other terms:**

| Term | Value | Source |
|---|---|---|
| Who's covered | **Single life only.** No joint-life option found, so the couple buys two policies (as planned) | Brochure |
| Entry age | Hong Kong permanent residents aged **60+** (65+ until Feb 2020) | LegCo reply, 12 May 2021: https://www.info.gov.hk/gia/general/202105/12/P2021051100589p.htm |
| Premium | **HK$50,000 to HK$5,000,000 per person** (cap since 1 Jun 2022) | https://www.info.gov.hk/gia/general/202205/31/P2022053100383.htm |
| Payout per HK$1M | **Male 65: HK$5,800 a month (6.9% a year); female 62: HK$4,940 (5.9%)** | Brochure |
| Indexation | None: fixed HK$ for life ("remain unchanged") | Brochure |
| Rates since | Unchanged since 2018, but not guaranteed for buyers in 2037/2039 | https://www.info.gov.hk/gia/general/201812/12/P2018121200400.htm |
| Internal rate of return | "About 4%" at average life expectancy | https://www.ifec.org.hk/web/en/retiree/annuity/return.html |
| Medical withdrawal | Once in a lifetime, up to 100% of the unreturned premium (max HK$1M) for Hong Kong medical or dental bills, no charge since 29 Apr 2024 | https://www.hkma.gov.hk/eng/news-and-media/press-releases/2024/04/20240426-3 |
| MPF transfer | **No direct transfer**: withdraw the MPF, then pay the premium | HKMCA pages (only MPF promotional discounts mentioned) |

**Open point: Carmen's MPF at 62.** To withdraw at 62 she'd use the MPF early-retirement ground: age 60 and permanently
stopped working. She does retire in 2039, so it should apply, but this wasn't sourced. Confirm with the MPFA before
saying it on a slide.

**Suggested slide 6 note:** *"If Adrian died soon after buying, the family wouldn't lose the money: HKMC refunds the
premium less payments received as a lump sum, or keeps paying until 105% is returned (HKMC Annuity brochure)."*

---

## Not confirmed

- That old Flexi exclusions carry over into the Standard Plan (strong inference only).
- The age-83 row of HKMC's payout PDF (read through a summarising tool; check the PDF).
- The two-borrower reverse-mortgage rate at age 60.
- The fixed-rate reverse mortgage's insurance rate (1.25% vs 1.5%).
- The HKMC annuity's Guaranteed Cash Value schedule (not public).
- Carmen's early MPF withdrawal at 62.
- All rates are today's. Tables, thresholds and annuity rates can change before 2037–2060.
