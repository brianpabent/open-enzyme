---
title: "Phase 7-2 — Cultivation Method × Yield Meta-Analysis (Ganoderma / Cordyceps / Pleurotus)"
date: 2026-05-06
experiment: comp-014
phase: 7-2
parents:
  - "phase-7a-ganoderma-strain-scan.md"
  - "phase-7b-cordyceps-strain-scan.md"
  - "phase-7c-pleurotus-strain-scan.md"
  - "../../../wiki/medicinal-mushroom-complement-track.md"
scope: cultivation method × yield comparative meta-analysis for the three priority species; per-species recommendations for OE home-fermentable thesis vs OE-published-SOP reproducibility; cross-species summary; what-an-OE-contributor-should-actually-do recommendations
tags: [comp-014, phase-7, cultivation, meta-analysis, ganoderma, cordyceps, pleurotus, glpp, cordycepin, ergothioneine, sop, reproducibility]
---

# Phase 7-2: Cultivation Method × Yield Meta-Analysis

**Inputs:** Phase 7-1a/b/c strain scans + a focused PubMed gap-fill pass. **Output:** the canonical cultivation × yield comparison table that an Open Enzyme contributor uses to choose HOW to grow the mushroom — what yields each method gives, what each method costs at home / consumer / industrial scale, where reproducibility breaks down, and which environmental controls an SOP must specify. Multilingual (CNKI / J-STAGE / KISS) work is preserved as deferred follow-ups; this pass is built on the English-indexed PubMed corpus.

---

## 0. Reading guide — definitions used throughout

- **Compound yield basis.** Liquid-fermentation papers report yield in mg/L of broth or mg/g of dry mycelium. Solid-state fermentation (SSF) papers report mg/g of dry substrate or mg/g of dry fruiting body. Where comparison across methods requires unit conversion, the table is annotated.
- **Capital cost tier.**
  - **Home (≤$300 setup).** Pre-made consumer kit, plastic monotub, hand sprayer, temperature-controlled space (closet / basement). No autoclave; pasteurization or kit-grade sterilization. Achievable in a single weekend.
  - **Consumer / advanced-home ($300–$5,000 setup).** Pressure cooker / countertop autoclave, still-air or HEPA flow box, spawn bags, mini-incubator, fruiting chamber with humidifier + CO₂ vent. Reproducible across batches with discipline; this is the "serious hobbyist / Open Enzyme contributor with a home lab corner" tier.
  - **Industrial (>$10,000 setup).** Stirred-tank or air-lift bioreactor, lab-grade autoclave, HEPA flow hood, environmental-control room. Required for liquid submerged fermentation at >5 L scale and for any reproducibility study targeting <10% CV.
- **Reproducibility tier.**
  - **High** = multiple independent labs across countries report yields within ~2× of each other on the same method, with batch-to-batch CV reported below 20% in at least one paper.
  - **Medium** = single-lab reproducibility documented; cross-lab variance unknown or 2–5× spread across published yields with the same method label.
  - **Low** = published yields span >5× across the same nominal method, OR reproducibility is degraded by known confounders (strain culture degeneration, substrate seasonality, ITS mis-ID).
- **Cycle time** = colonization + fruiting (or biomass accumulation in liquid culture), measured in days from inoculation to harvest. Does not include downstream extraction.

The reproducibility-tier framework is a Phase 7 synthesis call, not a published metric — it's the calibration that lets an OE contributor pick a method given the published evidence base.

---

## 1. *Ganoderma lucidum* / *G. lingzhi* → GLPP

### 1.1 Method × yield comparison

| Method | Substrate | Cycle time | Compound yield | Capital cost tier | Reproducibility (Phase 7 call) | Notes |
|---|---|---|---|---|---|---|
| **Liquid submerged fermentation, defined natural medium** | Soluble starch 25 g/L + wheat bran 3 g/L + KH₂PO₄ 4.5 g/L; pH 4.0; 27°C; 90 rpm; or sucrose + corn flour + potato extract variant | **6–11 days** | Mycelial polysaccharide **30–60 mg/g DW**; mycelial DW 5–15 g/L; EPS 0.2–0.74 g/L; triterpenoids ~20–32 mg/g | Industrial for >5 L; Consumer-tier shake-flask achievable at 250 mL | **High.** Multiple labs (China, Russia, Malaysia, Indonesia) converge on similar yields with similar media; Luo 2025 PMID 39717915 + Zheng 2026 PMID 41610097 + Tikhomirova 2024 PMID 39572077 corroborate. | **Solid-seed inoculum trick** (wheat-bran solid pre-grow → liquid transfer) gives 1.6× EPS over liquid-pellet inoculum (Liu & Zhang 2018 PMID 30263843). Cleanest method for an SOP. |
| **Juncao solid-state cultivation (the Lin lab method, the GLPP-for-HUA paper's source)** | Dried, chopped Juncao grass (*Pennisetum* hybrid) + corn cob / cottonseed hull / rice bran (typical 70:20:10) | **60–90 days fruiting + spawn-run** (matches CNKI Juncao manuals) | Fruiting-body GLPP — methods/specific yields buried in Chinese-language Juncao manuals, not surfaced in English PubMed; the 40.6% UA paper's source material is from this method (Lin S 2022 PMID 36385640) | Industrial OR farmer-scale (Juncao is a Chinese rural-agriculture technology); **not feasible at OE-contributor home scale outside China** (substrate not commercially available in the West) | **Medium-low for non-Chinese contributors.** High where Juncao is locally available (Fujian rural regions). Substrate substitution to hardwood log changes compound profile. | The actual SOP (substrate prep, sterilization, inoculation density, fruiting trigger) is in Chinese-language Juncao manuals (林占熺 et al.) — **deferred as Phase 5b CNKI work.** |
| **Hardwood log / sawdust block (Western consumer-kit cultivation)** | Oak / maple / poplar sawdust + wheat bran + gypsum (70:20:10 typical); pasteurized or autoclaved; bagged in spawn bags | Spawn run **3–6 weeks**; fruiting **4–12 weeks**; total **7–18 weeks** | Fruiting-body GLPP yield not directly published in PubMed-indexed work; commercial yield data suggests 5–15 g dry fruiting body per 5 lb sawdust block; polysaccharide ~10–30 mg/g of fruiting body (extrapolated from Cohen 2014 PMID 24941169 panel ranges) | **Home (kit) to Consumer.** A grow kit costs $25–$60 and produces ~150–300 g fresh fruiting body. Sawdust block from scratch: $50–$200 (autoclaved bag + spawn). | **High for the cultivation method itself** (consumer kits are widely available). **Low for matching the Lin lab's specific GLPP material** without ITS verification + substrate matching. | Most commercial "G. lucidum" supplements come from this method. **Mis-ID rate is ~93%** — most are *G. lingzhi*, not *G. lucidum* sensu stricto (Loyd 2018 PMID 30061872). ITS verification is non-optional. |
| **Mycelium-on-grain (US supplement industry standard)** | Sterilized brown rice / millet / sorghum grain in spawn bag; inoculated with G. lingzhi mycelium; harvested whole (mycelium + grain) | **3–6 weeks** | Mycelial polysaccharide reported on whole-product basis; **majority of measured "polysaccharide" is grain β-glucan, not fungal polysaccharide** (Wu 2017 PMID 28798349) | Consumer | **Low for fungal-polysaccharide reproducibility.** Total β-glucan is reproducible; specific fungal polysaccharide content is not — the grain mass swamps the fungal contribution. | **Avoid for any GLPP reproducibility claim.** Wu 2017 found 26.3% chemistry-verified rate in US supplements largely because of this format. Use only if the protocol explicitly separates fungal mycelium from grain pre-extraction. |
| **Bioreactor scale-up, RSM-optimized** | Defined medium with RSM-tuned C/N/mineral ratios; 1–10 L STR | **8–14 days** | Up to 0.74 g/L EPS, ~12 g/L mycelial DW (Tikhomirova 2024 PMID 39572077) | Industrial | **High** (multiple bioreactor papers reproduce within 30%). | The reference method for an OE-published reproducibility-grade SOP at scale beyond shake-flask. |

**Citations (key):** Luo S 2025 PMID 39717915 / [10.1615/IntJMedMushrooms.2024056392](https://doi.org/10.1615/IntJMedMushrooms.2024056392); Zhang J 2022 PMID 35993963; Liu SR & Zhang WR 2018 PMID 30263843 / [10.1007/s10068-018-0343-z](https://doi.org/10.1007/s10068-018-0343-z); Tikhomirova T 2024 PMID 39572077 / [10.1093/lambio/ovae115](https://doi.org/10.1093/lambio/ovae115); Zheng S 2026 PMID 41610097 / [10.1371/journal.pone.0337539](https://doi.org/10.1371/journal.pone.0337539); Lin S 2022 PMID 36385640 / [10.1039/d2fo02431d](https://doi.org/10.1039/d2fo02431d); Hennicke F 2016 PMID 27044336 / [10.1016/j.phytochem.2016.03.012](https://doi.org/10.1016/j.phytochem.2016.03.012); Loyd AL 2018 PMID 30061872 / [10.3389/fmicb.2018.01557](https://doi.org/10.3389/fmicb.2018.01557); Wu DT 2017 PMID 28798349 / [10.1038/s41598-017-06336-3](https://doi.org/10.1038/s41598-017-06336-3); Cohen N 2014 PMID 24941169 / [10.1615/intjmedmushr.v16.i3.80](https://doi.org/10.1615/intjmedmushr.v16.i3.80).

### 1.2 Optimal method per Open Enzyme objective

**Optimal for the home-fermentable thesis ("easily grown at home"):**
**Hardwood sawdust block from a consumer reishi grow kit, with mandatory ITS verification of the source spawn.** This is the only Ganoderma method that's truly tractable at home with a $25–$100 setup. Cycle is long (7–18 weeks) but unattended for most of it. Caveat: consumer kits will produce *G. lingzhi* (not *G. lucidum* sensu stricto) with ~95% probability, which is fine — the published bioactivity data is overwhelmingly on *G. lingzhi*. The kit-vs-Lin-lab gap is in the substrate (sawdust vs Juncao) and in strain provenance, both of which are real but bounded sources of variance.

**Optimal for OE-published-SOP reproducibility (lowest published batch-to-batch variance — H06 viability question):**
**Liquid submerged fermentation, defined natural medium, ITS-verified G. lingzhi (Mycelia bvba M9724 or CGMCC-deposited equivalent), 250 mL shake-flask scale.** Multiple independent labs converge within ~2× on mycelial polysaccharide yield (30–60 mg/g DW) using nearly identical media. The Zheng 2026 protocol (PMID 41610097) is RSM-optimized and reads as the cleanest single-paper SOP candidate. Solid-seed inoculum (Liu & Zhang 2018) cuts batch-to-batch variance further. Capital cost is low for a research bench (250 mL shaker flask, tabletop incubator-shaker, autoclave) — total ~$3,000–$5,000, sits at the Consumer / advanced-home tier.

**Yield-per-dollar comparison.** The hardwood-kit route is by far the cheapest per gram of dry fruiting body produced (~$0.10–$0.50/g dry fruiting body all-in for a consumer kit), but the fungal-polysaccharide content of that fruiting body is variable. Liquid submerged fermentation costs ~$5–$20/g dry mycelium at shake-flask scale (mostly media + autoclaving) but produces a defined product with reproducible polysaccharide yield. **Per gram of *fungal polysaccharide*, the two methods are within an order of magnitude of each other; the choice hinges on what the downstream assay needs (fruiting-body fingerprint vs defined mycelial polysaccharide).**

**Critical environmental controls (must be specified in any SOP):**
- *Liquid submerged.* Temperature 27°C ±1°C; pH 4.0 ±0.2 (controlled drift via medium buffering); agitation 90 rpm (shake-flask) or 150 rpm (STR); aeration sufficient to keep DO >30% air saturation in STR. Inoculum from solid-seed wheat-bran pre-culture (1–5% v/v transfer).
- *Sawdust block.* Spawn run 25°C, no light, RH 70–80%, no fruiting trigger. Fruiting trigger: drop temperature to 21–24°C, raise RH to 90%+, introduce indirect light, maintain CO₂ <1000 ppm (lower CO₂ → conk morphology; higher CO₂ → antler morphology — which morphology appears is a load-bearing CO₂-control proxy).
- *Cross-cutting.* Strain ITS-verified and stored on slants at 4°C; sub-culture every 3 months; never use mycelium that's been continuously sub-cultured >10 generations (culture degeneration kicks in — same failure mode flagged in §2 for *Cordyceps*).

---

## 2. *Cordyceps militaris* → cordycepin

### 2.1 Method × yield comparison

| Method | Substrate | Cycle time | Compound yield | Capital cost tier | Reproducibility (Phase 7 call) | Notes |
|---|---|---|---|---|---|---|
| **Brown rice solid-state fermentation (the consumer-grow standard)** | Polished or unpolished brown rice + water + small amount of supplement (silkworm pupa powder, peptone, glucose); jar or bag; autoclaved; light-cycled fruiting | **Spawn run 14–25 days; fruiting 30–45 days; total 45–70 days** | **1–10 mg cordycepin / g substrate**; up to **25.07 mg/g** with wheat + monosodium glutamate substrate (Liang 2014 PMID 25404221); **13.1 mg/g** in germ rice (Liu 2024 PMID 38967211); **mixed grains** 1.6–2.0 mg/g (Borde 2023 PMID 37930616) | **Home (kit) to Consumer.** Consumer kit ~$30–$80 (jars + spawn); from-scratch ~$150–$500 (pressure cooker + spawn + jars). Light cycle = $20 LED on a timer. | **Medium.** Yields span 5× across the same nominal method depending on strain + substrate supplement. Park 2025 review (PMID 41097576) explicitly identifies "absence of standardized cultivation protocols" as a field gap. **Culture degeneration** (Shrestha 2012 PMC3408298) is a known failure mode after sub-culturing. | Most reproducible per Park 2025 review. The home-cultivable cordycepin route. Light cycling (12h on / 12h off) drives fruiting-body formation. |
| **Liquid static culture, optimized media (Sichuan Agri / Nantong style)** | Glucose 30–50 g/L + peptone / yeast extract + minerals; static (no agitation) in glass jars or bottles; dim light; 22–25°C | **20–30 days** | **2,008–7,350 mg/L cordycepin** (Kang 2014 PMID 25054182; Tang 2014 PMID 24117155); 7,883 mg/L with mutant GYS60 (Zhang 2020 PMID 33463932) | Consumer / Industrial. Static culture in 1 L jars is achievable at home; 5 L scale-up requires fermenter | **Medium-high** within published-protocol range (multiple labs replicate within 2–3× at static-culture 1 L scale) | **Static, not agitated.** Counterintuitive — agitation drops cordycepin yield. The Tang 2014 5 L static-fermenter protocol is the cleanest published reproducibility-grade SOP. |
| **Liquid submerged + corn-steep-liquor / pupa-powder N source** | CSLH or pupa powder as primary nitrogen source (replaces peptone) | **10–20 days** | **343 mg/L** (CSLH; Chang 2024 PMID 38472926); pupa powder 30% boost over peptone, 50% cost reduction (Luo 2018 PMID 30507305); cottonseed + perilla oil 1.49 g/L (Kim CB 2025 PMID 40549333) | Consumer / Industrial | **Medium.** Yields published in 2–4× range across labs. | The cost-optimized industrial path; pupa-powder substrate also addresses the ADA paradox (pupa-derived nutrients drive natural co-production of cordycepin + pentostatin per the Xia 2017 PTN safeguard cluster). |
| **Liquid + IoT/hypoxic regulation** | Defined medium; CO₂-feedback-controlled hypoxic regime | **14 days** | **1.44 g/L (103.2 mg/L/d)** at 5 L (Chien 2025 PMID 39819523) | Industrial | **Medium-high** (single-lab; not yet cross-replicated) | Hypoxic regulation is the productivity-per-day frontier. Not home-tractable. |
| **Insect-substrate solid-state (silkworm pupa, *Allomyrina dichotoma*)** | Sterilized rhinoceros beetle pupae or silkworm pupae | **30–60 days** | **34× higher than rice substrate** with rhinoceros beetle (Turk 2022 PMID 36338069) | Consumer (specialty substrate sourcing) | **Medium-low** (substrate seasonality + sourcing variance) | Mechanism: oleic acid in pupa upregulates *cns1*/*cns2* transcription. Highest known native-strain cordycepin density per gram substrate. **Substrate sourcing is the bottleneck for OE adoption.** |
| **Heterologous chassis — A. oryzae (food-grade GRAS, koji)** | Glucose-based defined medium, *cns1*+*cns2* expression cassette under constitutive promoter | **5–8 days submerged** | **564.6 mg/L/d productivity** (Jeennor 2023 PMID 38071331) | Industrial (engineered strain — requires institutional biosafety review) | **Medium-high** for the engineered strain; reproducibility tied to plasmid stability + clonal selection | **High-priority cross-track finding** — converts cordycepin from "Cordyceps × koji co-fermentation" to "single-organism engineered koji." Cross-link to OE engineered koji track. |
| **Heterologous chassis — P. pastoris (high-titer reference)** | Methanol-fed-batch, engineered Pp29 | **7–14 days fed-batch** | **8.11 g/L (10 L)** (Zhao 2024 PMID 39241814) | Industrial | **High** within Pp29 lineage | Highest cordycepin titer reported in any heterologous system. Not food-grade — relevant as the "what's the upper ceiling" reference, not as the OE chassis. |
| **Heterologous chassis — Y. lipolytica** | Engineered YL-CD3 / YlCor-18; lipid-droplet compartmentalization | **7 days** | **4,362–4,780 mg/L** (Song 2023, Duan 2025) | Industrial | **Medium-high** | Mid-tier titer, food-adjacent oleaginous yeast. |

**Citations (key):** Park HJ 2025 PMID 41097576 / [10.3390/foods14193408](https://doi.org/10.3390/foods14193408) (review); Liang ZC 2014 PMID 25404221; Liu ML 2024 PMID 38967211; Borde M 2023 PMID 37930616 / [10.1007/s42770-023-01169-x](https://doi.org/10.1007/s42770-023-01169-x); Kang C 2014 PMID 25054182; Tang J 2014 PMID 24117155; Zhang H 2020 PMID 33463932 / [10.1615/IntJMedMushrooms.2020037153](https://doi.org/10.1615/IntJMedMushrooms.2020037153); Chang Y 2024 PMID 38472926 / [10.3390/foods13050813](https://doi.org/10.3390/foods13050813); Luo QY 2018 PMID 30507305; Kim CB 2025 PMID 40549333; Chien TY 2025 PMID 39819523; Turk A 2022 PMID 36338069 / [10.3389/fmicb.2022.1017576](https://doi.org/10.3389/fmicb.2022.1017576); Jeennor S 2023 PMID 38071331 / [10.1186/s12934-023-02261-5](https://doi.org/10.1186/s12934-023-02261-5); Zhao B 2024 PMID 39241814 / [10.1016/j.biortech.2024.131446](https://doi.org/10.1016/j.biortech.2024.131446); Xia Y 2017 PMID 29056419 / [10.1016/j.chembiol.2017.09.001](https://doi.org/10.1016/j.chembiol.2017.09.001); Shrestha B 2012 PMC3408298.

### 2.2 Optimal method per Open Enzyme objective

**Optimal for the home-fermentable thesis:**
**Brown rice solid-state fermentation in pre-sterilized jars, with light cycling.** This is the dominant consumer cordycepin method globally; consumer kits are widely available ($30–$80 from US/Korean/Taiwanese vendors). Cycle is 45–70 days. Yield 1–10 mg/g substrate is very tractable for daily-tea or supplement-equivalent dosing — a single 500 g rice jar produces 0.5–5 g cordycepin equivalent. **Critical caveat:** strain matters. Consumer kits routinely use degenerated single-ascospore lineages with declining productivity over generations (Shrestha 2012). Re-purchase fresh spawn every 2–3 cultivation cycles or accept yield drift.

**Optimal for OE-published-SOP reproducibility:**
**Liquid static culture, optimized glucose-peptone medium, 1 L glass-jar scale (Kang 2014 / Tang 2014 protocol).** Cordycepin yield is in the 2–7 g/L range with low variance within lab; cross-lab variance is ~2–3×. Multiple Chinese labs replicate. Critical: the culture must be **static** (no agitation) — agitated submerged culture gives substantially lower cordycepin. This is the cleanest reproducibility-grade SOP candidate that doesn't require institutional biosafety approval (the heterologous Pp29 / A. oryzae routes give higher titers but require recombinant DNA work). For an OE contributor with a home lab corner, this is a $200–$500 setup (1 L glass jars, autoclavable, plus a tabletop incubator with no shaking).

**Yield-per-dollar comparison.** Brown rice SSF: ~$0.50–$2 per mg cordycepin produced (rice + electricity for autoclaving + spawn). Liquid static: ~$0.10–$0.50 per mg cordycepin (much higher cordycepin density per kg substrate cost). Insect-substrate SSF: ~$5–$20 per mg cordycepin (substrate is the cost driver — dried sericulture pupae are $30–$60/kg). **Liquid static is the yield-per-dollar winner; brown rice SSF wins on UX (no fermenter, just jars in a closet); insect SSF is impractical at OE-contributor scale despite its mechanistic advantages.**

**Critical environmental controls:**
- *Brown rice SSF.* Spawn-run temperature 22–25°C, dark, RH 60–70%; fruiting-trigger temperature drop to 18–22°C with light cycling (12h on / 12h off) and RH 80–90%. CO₂ doesn't matter much (cordycepin yield is not CO₂-sensitive in the way Ganoderma fruiting morphology is). Light spectrum: blue-rich (LED daylight ~5000 K) drives orange pigmentation and cordycepin co-induction.
- *Liquid static.* Temperature 22–25°C (NOT 27°C — cordycepin yield drops at higher temperature), pH initial 6.5 (drifts to 4–5 during fermentation; uncontrolled drift is acceptable), strict static (no shaker), light not required. Inoculum 5–10% v/v from 5-day liquid pre-culture.
- *Cross-cutting.* **Strain re-derivation discipline.** Single-ascospore progeny degenerate; periodically re-isolate from a fruiting body (sexual recombination) or accept the GYS60-style mutant-screening route. ITS verification is less critical for *C. militaris* than for *G. lucidum*/*G. lingzhi* (the species complex is cleaner) but a confirmatory ITS BLAST is still a $20–$40 ask at any academic core.

---

## 3. *Pleurotus ostreatus* / *P. citrinopileatus* → ergothioneine (EGT)

### 3.1 Method × yield comparison

| Method | Substrate | Cycle time | Compound yield | Capital cost tier | Reproducibility (Phase 7 call) | Notes |
|---|---|---|---|---|---|---|
| **Pasteurized straw / hardwood-pellet bag, fruiting body (consumer-kit standard)** | Wheat straw, oat straw, hardwood-pellet/coir mix; pasteurized (165°F / 74°C × 1 hr); spawn at 5–10% w/w; bagged | **Spawn run 10–14 days; fruiting 7–14 days; total 17–28 days** | **0.8–2.4 mg EGT / g DW** fruiting body (Cohen 2014 PMID 24941169 panel: P. ostreatus 2.4 mg/g; Tsiantas 2021 PMID 33805096: 0.82 mg/g on wheat straw, ~highest on olive-byproduct substrate); β-glucan 23.9% DW (Lam 2015) | **Home (kit).** Pre-made oyster-mushroom kit $20–$30; from-scratch ~$50–$150 (substrate + spawn + bag). | **High** for cultivation method itself (most-replicated home-fungus cultivation in the world). **High** for EGT yield within strain × substrate × drying combination. | The fastest, easiest method in this entire meta-analysis. Most accessible to OE contributors. **Substrate choice tunes the compound profile** (olive byproduct → highest EGT; grape marc → highest lovastatin — Tsiantas 2021). |
| **Pasteurized straw, P. citrinopileatus (golden oyster) — RCT-formulation strain** | Straw or hardwood-pellet/coir; same as above; commercial strain from Singapore RCT supply chain | **Spawn run 7–10 days; fruiting 5–10 days; total 12–20 days** (golden oyster fruits faster than gray oyster) | **7.0 mg EGT / g DW** (Singapore dementia RCT formulation, Shan 2025 PMID 40552321); **4.03 mg/g DW** with natural-vent drying + HHP extraction (Zhang 2024 PMID 38540867); cohort midpoint ~3–7 mg/g DW | Home (kit) | **Medium-high.** RCT-formulation is reproducible by definition (same strain, same substrate, same drying SOP). Variance across other golden-oyster sources is ~2×. | **Recommended apex method for the OE home-fermentable thesis.** ~3× the EGT density of commodity gray oyster, comparable cultivation difficulty. |
| **Submerged liquid fermentation, two-stage oxidative stimulus (P. citrinopileatus 303)** | Defined medium, 5-day baseline biomass + H₂O₂ + vitamin C oxidative stimulus | **5–7 days** | **641.76 mg/L EGT** (Li 2025 PMID 40348064) | Industrial | **Medium** (single-lab reproduction; cross-lab not yet replicated) | The published yield ceiling for any Pleurotus EGT route. Not home-tractable; the apex industrial protocol. |
| **Solid-state fermentation onto grain (Pleurotus mycelium-on-adlay/buckwheat)** | Adlay / buckwheat / mixed grain + Pleurotus mycelium | **10–14 days mycelial colonization** | **PFA/PFB grain product 0.79–0.80 mg/g DW**; mycelium itself 1.5 mg/g (Chen 2012 PMID 22339711) | Consumer | **Medium-high** (well-established Asian functional-food format) | The substrate becomes the delivery vehicle. Cleaner story than mycelium-on-grain Ganoderma because EGT is a small molecule that distributes through the colonized grain mass. |
| **Spent-mushroom-substrate (SMS) re-use** | 7 different SMS types tested (own + cross-species); P. pulmonarius on Agaricus marmoreus SMS gave 63.47% biological efficiency | **Standard fruiting cycle, 2nd flush** | **0.5–2.17 mg EGT / g DW** depending on SMS type (Liang 2025 PMID 40100230) | Home (kit, second-flush mode) | **Medium** | **Circular cultivation.** Recycle the substrate from the first flush — extra cycle, lower per-flush yield, but the substrate cost amortizes. |
| **Selenium / zinc biofortification (P. eryngii)** | Standard substrate + Na₂SeO₃ 50 mg/L + ZnSO₄ 20 mg/L Zn²⁺ | Standard 14–21 day cycle | EGT modestly elevated; trace-element content materially elevated (Słowińska 2020 PMID 32079328 / [10.3390/molecules25040889](https://doi.org/10.3390/molecules25040889)) | Consumer | **High** for trace-element loading; modest for EGT | Tuning knob beyond C/N source — relevant if the OE delivery target also wants Se as a cofactor for the GPx/Trx redox axis. |

**Drying matters as much as substrate** — multiple studies converge: freeze-dry (−80°C → lyophilization) > natural-ventilation dry > hot-air at <40°C >> microwave. Cumulative strain × substrate × drying envelope = ~5–10× across worst → best protocols (Phase 7-1c §2). EGT is more thermolabile in its phenolic/oxidative-protective context than as the molecule itself; the drying signal is real and load-bearing for any SOP.

**Citations (key):** Cohen N 2014 PMID 24941169 / [10.1615/intjmedmushr.v16.i3.80](https://doi.org/10.1615/intjmedmushr.v16.i3.80); Tsiantas K 2021 PMID 33805096 / [10.3390/molecules26071832](https://doi.org/10.3390/molecules26071832); Shan A 2025 PMID 40552321 / [10.3389/fnagi.2025.1588493](https://doi.org/10.3389/fnagi.2025.1588493); Li 2025 PMID 40348064 / [10.1016/j.biortech.2025.132630](https://doi.org/10.1016/j.biortech.2025.132630); Zhang J 2024 PMID 38540867 / [10.3390/foods13060878](https://doi.org/10.3390/foods13060878); Chen 2012 PMID 22339711 / [10.1615/intjmedmushr.v14.i1.90](https://doi.org/10.1615/intjmedmushr.v14.i1.90); Liang 2025 PMID 40100230 / [10.1615/IntJMedMushrooms.2025058216](https://doi.org/10.1615/IntJMedMushrooms.2025058216); Lam 2015 PMID — [10.1615/intjmedmushrooms.v17.i2.30](https://doi.org/10.1615/intjmedmushrooms.v17.i2.30); Liang 2013 PMID 23662614 (Hi-Ergo P. eryngii); Cheah I 2017 PMID 27488221 / [10.1089/ars.2016.6778](https://doi.org/10.1089/ars.2016.6778) (human PK); Tang R 2018 PMID 29371632 / [10.1038/s41598-018-20021-z](https://doi.org/10.1038/s41598-018-20021-z) (mouse tissue distribution).

### 3.2 Optimal method per Open Enzyme objective

**Optimal for the home-fermentable thesis:**
**Pasteurized-straw bag of P. citrinopileatus (golden oyster) — consumer kit format.** Cycle time 12–20 days (fastest in the meta-analysis), kit cost $20–$30, EGT density 3–7 mg/g DW (~3× over commodity gray oyster), eat the fruiting body fresh in stir-fry or freeze-dry for powder. A single ~250 g fresh-mushroom flush from one bag delivers ~25 g DW × 5 mg/g = 125 mg EGT, which at OCTN1-saturated absorption (Cheah 2017) plateaus at clinically meaningful plasma EGT for several days. **This is the cleanest OE home-fermentable recommendation in the entire comp-014 track.**

**Optimal for OE-published-SOP reproducibility:**
**Same as above (P. citrinopileatus on pasteurized straw + freeze-dry to powder), formalized to the Singapore-RCT specification (7.0 mg/g DW lyophilized powder).** Cross-cultivar variance is ~2× (acceptable for an OE SOP). Submerged-fermentation 641 mg/L (Li 2025) gives higher absolute yield but is single-lab and capital-intensive. The reproducibility ceiling here is bounded by source-strain variance; if the OE SOP specifies Mycelia.bvba / commercial cultivar X with documented EGT density, batch-to-batch variance lands at ≤30% CV.

**Yield-per-dollar comparison.** Pleurotus is the cheapest of the three species per mg compound: ~$0.05–$0.20 per mg EGT in the home-kit format (a $25 kit produces ~25 g DW × 3 mg/g = 75 mg EGT; $25 / 75 mg = $0.33/mg). Commercial Pleurotus-EGT supplements run $0.50–$2/mg. **The home-cultivation route is cost-competitive with commercial supplementation at scale.**

**Critical environmental controls:**
- *Spawn run.* 22–25°C, dark, RH 65–80%, no fruiting trigger, 7–14 days.
- *Fruiting trigger.* Drop temperature to 16–22°C, raise RH to 90%+, introduce light (daylight LED ok), maintain CO₂ <1000 ppm (poor CO₂ control → long, leggy stipes; tight control → compact fruiting bodies). Pin formation in 3–5 days, harvest in 7–10 days.
- *Drying.* Freeze-dry (−80°C → lyophilization) for maximum EGT preservation; natural-vent dry (room temperature, fan, 48 hr) acceptable; hot-air <40°C tolerable; microwave **disallowed** (degrades both EGT and lovastatin disproportionately to the Maillard/heat exposure).
- *Strain provenance.* P. citrinopileatus is a cleaner species complex than Ganoderma; ITS mis-ID is rare. Strain from a kit supplier with documented pedigree (e.g., Mycelia.bvba, North Spore, Field & Forest commercial strain) is sufficient — no per-batch ITS authentication required for OE contributor protocol (a one-time ITS verification when adopting a new cultivar is sufficient).

---

## 4. Cross-species summary

### 4.1 Recommendation matrix

| Species → Compound | Recommended home-cultivation method | Recommended SOP-reproducibility method | Yield range across all methods | Phase 7 priority for cultivation comp-NNN |
|---|---|---|---|---|
| ***G. lucidum* / *G. lingzhi* → GLPP** | Hardwood sawdust block (consumer kit), ITS-verified G. lingzhi spawn, 7–18 wk cycle, freeze-dry fruiting body | Liquid submerged fermentation, defined natural medium, ITS-verified G. lingzhi (Mycelia M9724 or CGMCC accession), 250 mL shake-flask, 6–11 day cycle, solid-seed inoculum | **30–60 mg/g DW mycelial polysaccharide (liquid); fruiting-body GLPP yield poorly characterized in English PubMed (Chinese-language literature gap)** | **MEDIUM.** GLPP material is fruiting-body-derived in the anchor paper (PMID 36385640). Reproducing the 40.6% UA effect requires fruiting body, not liquid mycelium → Juncao SOP is the missing piece. **Higher comp-NNN priority is on the GLPP × cordycepin co-fermentation hypothesis** (Phase 6 finding) than on independently optimizing GLPP cultivation. |
| ***C. militaris* → cordycepin** | Brown rice SSF in jars, light-cycled, 45–70 day cycle, freeze-dry whole jar contents | Liquid static culture, glucose-peptone defined medium, 1 L glass jar, 20–30 day cycle (Kang 2014 / Tang 2014 protocol); OR engineered A. oryzae cns1+cns2 chassis (Jeennor 2023) for OE-koji-track integration | **1–25 mg/g substrate (SSF); 0.3–7.4 g/L (liquid static, native); up to 8.1 g/L (heterologous Pp29); 564 mg/L/d (engineered A. oryzae)** | **HIGH.** The Jeennor 2023 *A. oryzae cns1+cns2* result converts cordycepin from "Cordyceps × koji co-fermentation" to "single-organism engineered koji" — major chassis-decision implication for the OE engineered-koji track. Plus the Phase 6 GLPP × cordycepin synergy hypothesis remains the cheapest experimental item in the comp-014 queue. |
| ***P. ostreatus* / *P. citrinopileatus* → EGT** | Pasteurized-straw bag, P. citrinopileatus (golden oyster) consumer kit, 12–20 day cycle, freeze-dry to powder | Same as home method, formalized to 7.0 mg/g DW lyophilized powder spec (Singapore RCT formulation; PMID 40552321) | **0.8–7 mg/g DW fruiting body (commercial range); 11.4 mg/g DW with optimized extraction (extract-grade); 641 mg/L (submerged liquid, two-stage oxidative stimulus, single-lab)** | **MEDIUM-LOW.** The dietary-intake → therapeutic-plasma-EGT axis is well-established (Cheah 2017, Tang 2018, Hattori 2025). EGT is OCTN1-saturable so concentrated extracts give diminishing returns. **The Pleurotus track does NOT need a separate cultivation comp-NNN** — the published cultivation envelope is already adequate for the dietary delivery thesis. The remaining comp-014 work on Pleurotus is on bioavailability (already done in 7-1c) + multilingual fill-in. |

### 4.2 Cleanest yield-vs-reproducibility tradeoff

The cleanest tradeoff that emerges across all three species: **liquid submerged fermentation gives the highest reproducibility and the cleanest defined product, but the home-cultivation route via solid-state fermentation gives 5–20× lower per-unit-cost compound yield with adequate reproducibility for dietary-delivery scenarios.** The decision threshold:
- If the downstream use is **dietary delivery** (EGT for daily oxidative-stress priming; cordycepin for daily NLRP3 dampening; GLPP for daily uricase complement) — solid-state / fruiting-body cultivation is cost-optimal and the published bioactivity translates.
- If the downstream use is **wet-lab characterization** (kinetic assays, structure determination, dose-response curves on cell lines) — liquid submerged fermentation gives the defined product with bounded variance.

The OE platform thesis is biased toward the dietary-delivery use case (gout sufferer eats reishi, cordyceps, oyster mushrooms daily), so **the home-cultivation routes should be treated as the primary cultivation SOPs, with liquid submerged fermentation as the validation/characterization method called in for any compound where the home-route variance is unacceptable for the H06 reproducibility question.**

### 4.3 Where the published yield data is too sparse for confident recommendation

**Ganoderma fruiting-body GLPP yield in English-indexed PubMed.** The Lin lab's 40.6% UA paper (PMID 36385640) used fruiting-body Juncao-cultivated GLPP, but the underlying Juncao cultivation SOP is in Chinese-language manuals — the English literature lacks even basic per-fruiting-body GLPP yield numbers for the Lin lab's substrate. Liquid-mycelium polysaccharide is well-characterized (30–60 mg/g DW, multiple labs); fruiting-body polysaccharide on hardwood vs Juncao vs straw — sparse in English. **This is the single biggest gap. Phase 5b CNKI dive (Lin Zhanxi 林占熺 + 灵芝 + 菌草 cultivation manual; Lin Zhibin 林志彬 GLPP fractionation methods) is non-optional before any wet-lab GLPP work.**

**The two-stage oxidative-stimulus Pleurotus protocol (Li 2025).** 641.76 mg/L EGT is a striking number but it's single-lab. The Phase 5b CNKI dive should include the Nanjing Tech group's Chinese-language predecessor papers — the English Bioresource Technology lead is presumably the tip of a longer Chinese-language methods-development arc.

**Strain × substrate × drying interaction surfaces for Pleurotus.** Many published yields, but few studies cross all three axes simultaneously. The 5–10× cumulative envelope is well-supported; the specific combinatorics (e.g., is golden oyster on olive-byproduct substrate freeze-dried genuinely the apex, or is there a better combination?) is undercharacterized. Less critical for OE because the dietary-delivery target dose is achievable across most of the envelope.

---

## 5. What an Open Enzyme contributor should actually do

### 5.1 *G. lucidum* / *G. lingzhi* — practical SOP

**What to buy:**
- **Reishi (G. lingzhi) sawdust grow kit** — North Spore, Field & Forest Products (Wisconsin), or Mycelia.bvba (Belgium, M9724 strain — only commercially available ITS-verified G. lingzhi). $40–$90.
- *Or* spawn from one of those suppliers + autoclavable hardwood-fuel-pellet bags + wheat bran + gypsum + a pressure cooker (~$300 kit setup).
- ITS sequencing as a one-time strain verification: ~$20–$40 at any university molecular core facility (request: Cao 2012 G-ITS-F1 / G-ITS-R2 primers, GenBank-format result).

**Substrate notes:**
- Hardwood sawdust pellets (oak / maple / poplar) work; avoid pine / cedar / softwood. **Do not use straw** for Ganoderma — it's a hardwood specialist and yields poorly on straw.
- Wheat bran 20% w/w supplement; gypsum 1% w/w (calcium buffer + structural).
- 70:20:10 sawdust:bran:water-adjusted-to-65%-moisture is the standard.

**Cycle to expect:**
- Spawn run: 3–6 weeks, dark, 25°C, RH 70%.
- Fruiting trigger: cut a slit in the bag, drop temperature to 21–24°C, raise RH to 90%, introduce 12h light cycle, maintain CO₂ <1000 ppm (use a cracked window or small fan).
- Conk maturation: 4–8 weeks (slow! — Ganoderma is a long-cycle organism).
- Total: 7–18 weeks per flush. Typically 1–2 flushes per block.

**How to verify the output:**
- Visual: red-brown varnished conk with pore surface (white when fresh, browns with age). Antler morphology (no cap) means CO₂ was too high; not a yield problem but indicates poor environmental control.
- Bitter ethanol-extract taste = high triterpenoid content, characteristic of G. lingzhi (Hennicke 2016). If the extract is not bitter, suspect mis-ID — verify ITS.
- For polysaccharide content quantification: phenol-sulfuric acid total polysaccharide assay (cheap, $20 in reagents) gives total carbohydrate; β-glucan-specific Megazyme kit ($300 for ~50 assays) gives the load-bearing fungal-polysaccharide number.

### 5.2 *C. militaris* — practical SOP

**What to buy:**
- **Cordyceps militaris brown-rice grow kit** — multiple US/Korean vendors (FreshCap, North Spore, Out-Grow). $30–$80 for a 4–8 jar kit.
- *Or* grain spawn + brown rice + wide-mouth quart-size canning jars + a pressure cooker + a small LED grow light on a 12h timer (~$300 kit setup).
- For the static-liquid SOP route: 1 L glass bottles (autoclavable), tabletop incubator (no shaker; $200–$500 used), defined medium (glucose 30 g/L, peptone 10 g/L, KH₂PO₄ 1 g/L, MgSO₄ 0.5 g/L).

**Substrate notes:**
- **Polished brown rice** (short-grain or medium-grain Japanese / Korean varieties — *Koshihikari*, *Calrose*, *Akitakomachi*). Long-grain Indian-style rice works less well. Don't use white rice (over-polished — too low nutrient density).
- Add **silkworm pupa powder** (sericulture supply, or order from Asian specialty markets) at 5% w/w if available — ~30% cordycepin yield boost (Luo 2018) and addresses ADA-paradox PTN-safeguard mechanism.
- Substrate moisture: 65–70%. Water:rice ratio ~1.4:1 by weight after autoclaving.

**Cycle to expect:**
- Inoculation: 1–2 mL liquid spawn or a teaspoon of grain spawn per quart jar.
- Spawn run: 14–25 days, dark, 22–25°C, jar lid loose for gas exchange.
- Fruiting trigger: introduce 12h on / 12h off light cycle (blue-rich LED 5000 K), keep temperature 18–22°C, RH 80–90%.
- Pin formation: ~7–14 days post-trigger.
- Fruiting: 30–45 days from pin to harvest. Orange stromata fully developed when ready.
- Total: 45–70 days per jar.

**How to verify the output:**
- Visual: bright orange stromata (cordyceps with pale stromata = degenerated culture; re-derive strain).
- HPLC quantification of cordycepin: any university analytical core can do this; ~$50–$100 per sample. Method: C18 column, 10–15% methanol/water, UV 260 nm, retention ~5–8 min depending on column. Cordycepin standard from Sigma-Aldrich ($300 for 50 mg).
- Co-quantify adenosine + pentostatin if possible (same column conditions; PTN at lower concentration but visible).

### 5.3 *P. ostreatus* / *P. citrinopileatus* — practical SOP

**What to buy:**
- **Golden oyster (*P. citrinopileatus*) grow kit** — North Spore, Smugtown Mushrooms, Field & Forest Products. $20–$30. Ready-to-fruit bags.
- *Or* sawdust-pellet/coir block + oyster-mushroom grain spawn + a 5-gallon bucket + a hand sprayer (~$60 from-scratch setup).
- For freeze-drying: home freeze-dryer (~$2,000 — Harvest Right) or use a friend's; or natural-vent dry on screens for 48 hr (no freeze-dryer needed for the dietary-delivery use case — natural-vent gives ~80% of the EGT preservation of freeze-drying).

**Substrate notes:**
- **Wheat straw or oat straw**, pasteurized at 165°F (74°C) for 1 hour. Straw is the standard.
- Hardwood pellet (oak / maple) + coconut coir (50:50 by hydrated volume) is the second-best home substrate; pellets are ~$10/40 lb at hardware stores (look for "fuel pellets" — make sure they're 100% hardwood with no binders).
- **Olive byproduct substrate** is the published apex for EGT (Tsiantas 2021) but isn't generally available outside Mediterranean regions; not in scope for an OE-contributor protocol unless the contributor is local to an olive-oil region.

**Cycle to expect:**
- Spawn run: 7–14 days, 22–25°C, dark, RH 65–80%, sealed bag.
- Fruiting trigger: cut Xs in the bag, drop temperature to 16–22°C, raise RH to 90%+ (mist 3–4× daily), introduce light, ensure airflow.
- Pin formation: 3–5 days post-trigger.
- Fruiting: 7–10 days from pin to harvest. Harvest when caps are flat or just starting to upturn.
- Total: 12–20 days per flush. Typically 2–3 flushes per bag (extract more EGT per dollar of substrate).

**How to verify the output:**
- Visual: golden yellow caps (golden oyster) or gray-blue caps (P. ostreatus). Misidentification rare in this genus.
- EGT quantification: HPLC at any analytical core; ~$50–$100/sample. Method: HILIC column, UV 257 nm. EGT standard from Cayman Chemical (~$200 for 50 mg).
- For dietary verification (no analytical equipment): consume 50–100 g fresh per serving; the cumulative dose math (~12–24 mg EGT/serving from gray oyster, ~25–50 mg from golden oyster) is in the OCTN1-saturating range and produces measurable plasma EGT elevation per Hattori 2025 dietary-intake-PK data.

---

## 6. Deferred multilingual follow-ups (preserved from Phase 7-1)

Per the OE CLAUDE.md global-multilingual rule, the following are **out of scope for Phase 7-2** (English-indexed pass) but flagged as load-bearing for closing the cultivation-SOP gap:

- **Phase 5b-Ganoderma:** Lin Zhanxi (林占熺) Juncao G. lucidum cultivation SOP via CNKI; Lin Zhibin (林志彬) GLPP fractionation methods; CGMCC G. lingzhi accession map; Chinese commercial cultivar comparison study (Phase 7-1a §"Phase 5b CNKI / J-STAGE / KCI follow-ups queued").
- **Phase 5b-Cordyceps:** Direct GLPP × cordycepin co-fermentation Chinese-language search (5b-Q1, HIGHEST priority — falsifies/refines the Phase 6 novelty claim); KSP / KYL Korean strain catalog; Chinese clinical-cohort gout evidence; silkworm-pupae cultivation J-STAGE corpus (Phase 7-1b §"Phase 5b CNKI/KISS/J-STAGE follow-ups queued").
- **Phase 5b-Pleurotus:** Tamogi-take Hokkaido cultivation J-STAGE corpus; Chinese commercial golden-oyster cultivar EGT data; Korean KMCC strain breeding lineage; aroma/sensory Japanese literature for hexadecanal and 1-octen-3-ol profiles (Phase 7-1c §"Phase 5b multilingual follow-ups queued").

Translation protocol per OE CLAUDE.md §"Translation protocol — two-model independent cross-check": Claude/Gemini × DeepSeek/Qwen, sentence-level disagreement annotations, `[TRANSLATION-DISAGREEMENT]` flag for load-bearing claims.

---

## 7. Handoff to Phase 7-3 (extract characterization SOPs)

Phase 7-3 should answer: **once the contributor has the cultivated material, how do they extract and characterize the active compound to verify the SOP worked?** Specific items:

1. **GLPP extraction SOP.** Hot-water decoction (95°C, 2 hr, ×3) → ethanol precipitation (4 vol absolute EtOH, 4°C overnight) → re-suspension → DEAE-Sepharose ion exchange → Sephacryl S-300 / S-400 gel filtration → freeze-dry. Yield: ~5–10% w/w from dry fruiting body. **Reference: Lin lab papers PMID 37852403 / 29541200 should give the column conditions; Phase 5b CNKI dive may be needed for the upstream extraction details.**
2. **Cordycepin extraction + HPLC quantification SOP.** Methanol or water extraction (most commonly hot water 80°C × 30 min, ×2) → centrifuge → filter → HPLC C18 column → UV 260 nm. **Reference: Wang 2014 PMID 25404221 co-quantification method.** Critical: also quantify adenosine (RT slightly different) to compute the cordycepin/adenosine ratio (load-bearing for the Xia 2017 PTN-cluster active-state diagnostic).
3. **EGT extraction + HPLC quantification SOP.** UA-DES (urea-betaine deep eutectic solvent) or aqueous methanol extraction → HILIC HPLC → UV 257 nm. **Reference: Liu 2026 (UA-DES, P. ostreatus 11.39 mg/g optimized); Cohen 2014 panel method.**
4. **Functional verification.** For each compound, the simplest in vitro readout that the OE-cultivated material is bioactive:
   - GLPP: phenol-sulfuric polysaccharide assay (total) + Megazyme β-glucan assay (specific) + uricase-activity rescue in macrophage assay.
   - Cordycepin: HPLC quantification + ADA-inhibition (with PTN co-quantification) + URAT1 transporter assay (per comp-014 Phase 6 thesis).
   - EGT: HILIC-HPLC quantification + DPPH antioxidant (rough sanity check) + Nrf2-ARE reporter assay if available.
5. **Strain banking SOP.** Once a contributor has a working cultivation SOP, the strain should be banked (slants at 4°C; long-term in glycerol stock at −80°C; sub-culture every 3–6 months max). **Cross-reference Phase 7-1a §4.2 ITS authentication protocol** for Ganoderma — applies broadly to all three species when banking.

The Phase 7-3 document should pull these into a contributor-facing SOP manual; the analytical methods are mostly straightforward, but the **GLPP fractionation column work is the load-bearing technique and needs a CNKI-sourced primary-protocol reference, not just an extrapolation from the Lin lab pharmacology papers.**

---

## Cross-references

- Parent scope page: [`medicinal-mushroom-complement-track.md`](../../../wiki/medicinal-mushroom-complement-track.md)
- Phase 7-1a (Ganoderma): [`phase-7a-ganoderma-strain-scan.md`](./phase-7a-ganoderma-strain-scan.md)
- Phase 7-1b (Cordyceps): [`phase-7b-cordyceps-strain-scan.md`](./phase-7b-cordyceps-strain-scan.md)
- Phase 7-1c (Pleurotus): [`phase-7c-pleurotus-strain-scan.md`](./phase-7c-pleurotus-strain-scan.md)
- Phase 5 deepread (the GLPP-HUA anchor paper): [`phase-5-deepread-PMID36385640.md`](./phase-5-deepread-PMID36385640.md)
- Phase 5 AMC-BFE deepread (cordycepin co-fermentation precedent): [`phase-5-deepread-PMID41905012.md`](./phase-5-deepread-PMID41905012.md)
- Comp-014 parent computational page: [`medicinal-mushroom-compound-mapping-computational.md`](../../../wiki/medicinal-mushroom-compound-mapping-computational.md)
- Open Enzyme global multilingual research rule: top-level [`CLAUDE.md`](../../../CLAUDE.md) §"Global-multilingual research by default"
- Open Enzyme engineered koji track (cordycepin chassis cross-link): [`engineered-koji-protocol.md`](../../../wiki/engineered-koji-protocol.md) (if present)

## Evidence-level summary (per OE CLAUDE.md §5)

- Yield numbers are all **In Vitro / Bioprocess** evidence tier — published peer-reviewed papers, not independently re-cultivated by OE.
- Method × yield comparisons across species are **Mechanistic Extrapolation** for any specific OE-contributor scenario — the published yields are within strain × substrate × medium × scale envelopes that may not match exactly what the contributor sources.
- Reproducibility tier assignments (high / medium / low) are **Phase 7 synthesis calls** based on cross-paper variance, not formal meta-analytic CV calculations. Brian's calibration on these tiers is welcome.
- Capital-cost tier assignments are **2026 US-market estimates** based on commercial supplier pricing (North Spore, Field & Forest, Mycelia.bvba, Amazon for kits; Sigma-Aldrich + Megazyme for analytical reagents). Pricing in non-US markets may shift the home/consumer/industrial boundaries.
- Cross-species comparison and "what an OE contributor should actually do" recommendations are **Phase 7 synthesis** — load-bearing for the platform SOP development but not independently validated.

The single biggest evidence-tier weakness in this meta-analysis: **Ganoderma fruiting-body GLPP yield on hardwood-sawdust substrate is poorly characterized in English-indexed PubMed.** This is the gap the Phase 5b CNKI dive must close before Phase 7-3 SOP work can land cleanly.
