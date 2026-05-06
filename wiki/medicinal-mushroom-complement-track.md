---
title: "Medicinal Mushroom Complement Track — Phase 7 Platform Expansion"
date: 2026-05-06
tags:
  - medicinal-mushrooms
  - chassis-strategy
  - native-compound-producers
  - peer-track
  - platform-strategy
  - cultivation
  - scope-page
  - first-principles
related:
  - open-enzyme-vision.md
  - open-source-platform.md
  - modality-chokepoint-matrix.md
  - engineered-lbp-chassis.md
  - sirna-urat1-modality.md
  - medicinal-mushroom-compound-mapping-computational.md
  - computational-experiments.md
  - engineered-koji-protocol.md
  - koji-home-fermentation.md
sources:
  - "Brian framing 2026-05-06: 'we were using koji as the tool that we want to jam these things onto, and that itself is a fungus. We just looked at all these other fungi, and I'm wondering: is there another fungus that could be easily grown at home that would be either a better solution than koji or a complementary solution with koji?'"
  - "comp-014 Phase 6 triage (2026-05-06) — GLPP / cordycepin / ergothioneine routed to cultivation track; GLPP+cordycepin synergy pair flagged"
  - "Phase 1 chassis-comparison analysis: ascomycete (koji) genetics is 5-10x more mature than basidiomycete (medicinal mushrooms) for protein-secretion engineering"
status: scoped (Phase 1)
---

# Medicinal Mushroom Complement Track — Phase 7 Platform Expansion

## Why this page exists

Open Enzyme's koji thesis is "engineered *A. oryzae* secretes therapeutic enzymes via home-fermentable food." The koji chassis is uniquely positioned for that role — decades of ascomycete secretion-biology toolkit (KEX2 protease handling, glucoamylase fusion machinery, CRISPR works, signal-peptide engineering precedent). It is the right engineering chassis.

But comp-014 (medicinal mushroom × chokepoint mapping) surfaced a different category of leverage: **medicinal mushrooms are native producers of compounds that don't lend themselves to koji engineering** — polysaccharide-peptide hybrids (GLPP), nucleoside analogs (cordycepin), thiol antioxidants (ergothioneine), terpenoid-class secondary metabolites. These don't fit the "express recombinant protein in koji" paradigm; they fit a "cultivate the producer organism, extract the compound" paradigm.

Brian's 2026-05-06 inversion was the right one: not "find a better engineering chassis than koji" (basidiomycete genetics is 5-10× harder than ascomycete; engineering Pleurotus / Lentinula / Hericium / Ganoderma for protein secretion is a multi-year toolkit-building project before first construct expresses) but **"are there other home-cultivable fungi whose native compound profile complements what koji produces?"** Yes.

This page formalizes the **medicinal mushroom complement track** as a peer track to the koji engineering track under the broader Open Enzyme platform thesis. Same pattern as [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md) (engineered LBPs as obligate-anaerobe chassis sibling to koji) and [`sirna-urat1-modality.md`](./sirna-urat1-modality.md) (kidney-tropic siRNA as discovery-engine output sibling to fermentable enzymes). All three peer tracks expand Open Enzyme from "engineered enzymes in koji" to "solve gout, every avenue, fully open."

## Platform thesis expansion

| Track | Chassis | Engineering effort | Therapeutic class | Consumption UX |
|---|---|---|---|---|
| **Engineered koji (existing)** | *A. oryzae* | Heavy — recombinant cassette + secretion engineering | Therapeutic enzymes (uricase, lactoferrin, DAF SCR1-4, koji-secreted complement regulators) | Shio-koji / amazake / miso (daily food condiments) |
| **Engineered LBPs (peer)** | *F. prausnitzii* / *Akkermansia* | Heavy — anaerobe engineering, LBP regulatory path | Live therapeutic with sustained colonic activity (butyrate, IL-22, anti-complement) | Refrigerated capsule / reconstituted suspension (commercial pharma) |
| **siRNA / kidney-tropic discovery (peer)** | n/a (synthetic) | Heavy — sequence design, conjugate chemistry, delivery | Sequence-specific knockdown (URAT1) | Subcutaneous injection (commercial pharma) |
| ***Medicinal mushroom complement (THIS page)*** | *G. lucidum*, *C. militaris*, *Pleurotus*, *Lentinula*, *Hericium*, *G. applanatum*, *Inonotus* | **Light — strain selection + cultivation optimization + extract characterization. NO genetic engineering.** | Native-compound supplements (GLPP, cordycepin, ergothioneine, eritadenine, erinacines, betulinic acid derivatives) | Dried fruiting body / tincture / broth / powder (home cultivation OR consumer supplement) |

The fourth track is **the lightest engineering effort and the most accessible UX** — but it covers a chemistry space koji cannot reach.

## What goes on this track vs. the koji track

**Routed to the medicinal-mushroom-complement track (per comp-014 Phase 6):**

- **GLPP polysaccharide-peptide** (*Ganoderma lucidum*) — ADA + GLUT9 + OAT1 chokepoints, 40.6% UA reduction in HUA mice. Not a koji-engineering target; biosynthesis is mycelium-specific. Native cultivation is the route. **MW caveat (Phase 7-1a strain scan, 2026-05-06):** The 520 kDa figure I originally cited needs Phase 5b primary-source verification — Lin lab's own follow-up papers characterize GL-PP at 37 kDa and GL-PP2 at 31 kDa, an order-of-magnitude gap. The 520 kDa may be the crude pre-fractionation fraction or sourced from a different paper. Re-anchor before downstream synthesis depends on it.
- **Cordycepin** (*Cordyceps militaris*) — URAT1 chokepoint, animal model SUA 337→203 µmol/L. C. militaris liquid fermentation is mature; top strain GYS60 (plasma-mutagenesis derivative) hits 7,883 mg/L static liquid (PMID 33463932). **Major Phase 7-1b finding:** Cordycepin CAN be produced in food-grade *A. oryzae* via cns1+cns2 heterologous expression at 564 mg/L/d on glucose (Jeennor 2023, PMID 38071331). This **rebalances the chassis decision** — cordycepin is a koji-engineering candidate, not just a Cordyceps-cultivation candidate. Both routes coexist; the koji route is novel and aligned with OE's chassis thesis.

- **The natural Cordyceps ADA-inhibitor pairing** — C. militaris natively co-produces **pentostatin** from the same BGC cluster as cordycepin (Xia 2017, PMID 29056419). Pentostatin is a clinical-grade ADA inhibitor; this means whole-fermentate Cordyceps preparations have a built-in safeguard against cordycepin deamination that purified cordycepin lacks. **This reframes the Phase 6 GLPP+cordycepin synergy hypothesis** — the native ADA inhibitor is already packaged with cordycepin in fermented C. militaris. The GLPP+cordycepin synergy may be redundant with whole-fermentate Cordyceps, but a **purified cordycepin + GLPP** combination would still benefit from GLPP's ADA modulation. Wet-lab gate now has a 4-arm question: whole-fermentate Cordyceps vs purified cordycepin vs purified cordycepin + GLPP vs purified cordycepin + pentostatin.

- **Ergothioneine** — **Phase 7-1c correction:** *Pleurotus ostreatus* is NOT the highest EGT producer; ***P. citrinopileatus* (golden oyster) is 2-3× higher** (7.0 vs 2.4 mg/g DW). Apex strain: *P. citrinopileatus* 303 with two-stage H₂O₂+vit C oxidative stimulus → 641.76 mg/L submerged fermentation (Li 2025). Dietary intake plausibly therapeutic-dose: 50-100g fresh oyster ≈ 12-24 mg EGT, within published RCT-investigational range. OCTN1/SLC22A4 saturates at ~25 mg/day → **concentrated extracts have diminishing returns**, "daily oyster mushroom in dinner stir-fry" is mechanistically sound. *A. oryzae* / koji also produces ergothioneine (secondary).
- **Eritadenine** (*Lentinula edodes*) — cardiovascular activity, cholesterol-lowering. Native cultivation route.
- **Erinacines / hericenones** (*Hericium erinaceus*) — NGF-inducing (CNS-relevant). Native cultivation route.
- **Inotodiol / betulinic acid derivatives** (*Inonotus obliquus*) — triterpenoid chemistry overlapping reishi. Native cultivation route.
- **PSK / PSP polysaccharide-protein complexes** (*Trametes versicolor*) — β-glucan immunomodulator, FDA-approved adjuvant in Japan. Native cultivation route.

**Stays with the koji-engineering track:**

- **Recombinant uricase** (existing OE thesis — `engineered-yeast-uricase-proposal.md`, `engineered-koji-protocol.md`)
- **Lactoferrin** (existing OE thesis)
- **DAF SCR1-4 truncated complement regulator** (comp-006 / comp-012)
- **DAE (methyl 2,4-dihydroxybenzoate)** — small molecule, chemical synthesis preferred over fungal extraction (per comp-014 Phase 6 production-route assessment)
- **Any future therapeutic protein** — koji is the chassis when secreted protein is the deliverable

**Combined / synergy candidates (per comp-014 Phase 6, refined by Phase 7-1b strain scan):**

- **Whole-fermentate Cordyceps (cordycepin + native pentostatin)** — Phase 7-1b discovered that *C. militaris* natively co-produces pentostatin from the same BGC as cordycepin. Whole-fermentate preparations have the ADA-inhibitor safeguard built in. **This is the cleanest single-organism medicinal-mushroom-complement product** — fermented C. militaris on brown rice (4-8 week home cycle) delivers cordycepin + pentostatin in their natural ratio, no synergy assembly required.
- **GLPP + (purified) cordycepin** — only relevant if purified cordycepin is the delivery format. With whole-fermentate Cordyceps, the ADA-inhibitor pairing is already intrinsic. Wet-lab gate (4-arm comparison) now answers: which delivery format wins on dose efficiency + reproducibility.
- **Engineered koji cordycepin (cns1+cns2) + GLPP supplement** — the *engineered-koji-track* equivalent of the synergy pair. Koji's heterologous cordycepin lacks the natural pentostatin co-production unless the whole BGC is engineered in. May need pentostatin co-engineering OR GLPP supplementation as the ADA-inhibitor source. Open engineering question.
- **Engineered koji uricase + GLPP supplement** — koji handles bulk urate degradation in gut lumen; GLPP modulates ADA upstream + GLUT9/OAT1 transporters for renal-side support. Cleanest cross-track synergy (engineering + cultivation).

## Scope (Phase 1)

### Candidate species

Subset of the comp-014 Phase 5 anchor list, prioritized by:
1. Strength of comp-014 chokepoint-mapping evidence (in vivo > in vitro > predicted)
2. Home-cultivability (kit-scale UX > requires bioreactor > requires specialized substrate)
3. GRAS / pharmacopoeia status (no regulatory novelty needed)
4. Native compound profile diversity (multi-compound producers preferred — broader Open Enzyme value)

| Species | Common name | Top compounds | Cultivation UX | Regulatory |
|---|---|---|---|---|
| *Ganoderma lucidum* | reishi / lingzhi | GLPP, ganoderic acids (400+), ergosterol | Solid-state on hardwood; commercial mycelium kits widely available; 6-12 months for fruiting body | GRAS supplement |
| *Cordyceps militaris* | cultivated cordyceps | cordycepin, polysaccharides, ergosterol peroxide | Liquid fermentation OR solid-state on brown rice; 4-8 weeks home cycle; commercial kits available | GRAS supplement |
| ***P. citrinopileatus*** | golden oyster | **ergothioneine (highest fungal producer — 7.0 mg/g DW)**, β-glucans | Same straw / sawdust substrate as P. ostreatus; commercially less common than oyster but kits available | GRAS food |
| *Pleurotus ostreatus* | oyster mushroom | ergothioneine (2.4 mg/g DW — was originally claimed as highest, corrected by Phase 7-1c scan), lovastatin (190-342 mg/kg DW), pleuran | **Easiest home cultivation** — straw / coffee grounds / sawdust substrate; 4-6 weeks; widely sold consumer kits | GRAS food |
| *P. djamor* | pink oyster | β-glucans (43% DW — highest in genus) | Same as P. ostreatus | GRAS food |
| *P. eryngii* | king oyster | ergothioneine (5.84 mg/g DW Hi-Ergo strain) | Same as P. ostreatus | GRAS food |
| *Lentinula edodes* | shiitake | lentinan, eritadenine, ergosterol→D2 | Log / sawdust block; 6-18 months; widely sold consumer kits | GRAS food |
| *Hericium erinaceus* | lion's mane | erinacines, hericenones | Sawdust block / log; 4-8 weeks; widely sold consumer kits | GRAS food |
| *Trametes versicolor* | turkey tail / yun zhi | PSK, PSP | Hardwood log / dowels; 6-18 months for fruiting body | Supplement (PSK is approved drug in Japan) |
| *Inonotus obliquus* | chaga | betulinic acid derivatives, inotodiol, melanin | Wild-harvest from birch (slow growth); cultivation difficult; commercial mycelium-grown extracts widely available | Supplement |
| *Ganoderma applanatum* | artist's conk | DAE (small molecule), polysaccharides | Solid-state on hardwood; less commercially developed than G. lucidum | Supplement |
| *Aspergillus oryzae* (koji) | koji | ergothioneine (secondary), kojic acid, secreted enzymes | Already documented in `koji-home-fermentation.md` | GRAS food |

The medicinal-mushroom-complement track is **species-additive to comp-014's anchor list, not separate** — the same well-studied species, evaluated through a different lens (cultivation feasibility + native-compound consumption rather than engineering-chassis suitability).

### Cultivation method comparison (Phase 7 follow-up)

Three home-feasibility levels:

1. **Consumer-kit** (oyster, lion's mane, shiitake, reishi, turkey tail) — pre-inoculated grow blocks ($15-50), 4-12 weeks fruiting cycle, no specialized equipment beyond mister bottle + plastic tent.
2. **Mycelium kit** (cordyceps, more advanced reishi) — agar plate or grain spawn → fermentation jar / brown rice substrate; 4-8 weeks; requires sterilization (pressure cooker).
3. **Bioreactor** (defined-media liquid fermentation for standardized GLPP / cordycepin yield) — not home-feasible at consumer scale; commercial extract supply is the route.

Open Enzyme's value-add at the cultivation-method layer is **standardization + characterization protocols**, not novel cultivation. Consumer-grade reishi grow kits are ubiquitous; what's missing is the protocol that says "this batch contains X mg/g GLPP, Y% triterpene content, Z µg/g ergosterol — verified by standardized extraction + analysis." That's the Open Enzyme contribution to this track.

### Therapeutic UX

Consumption modalities for the cultivation track:

- **Dual decoction** (water + ethanol sequential extraction → blended) — captures both polysaccharide and terpenoid fractions. Traditional Chinese medicine standard for reishi. Concentrated to liquid extract or spray-dried to powder.
- **Tincture** (ethanol-only extraction) — captures terpenoid + small molecule fractions; not polysaccharides. Better for ganoderic acids, erinacines, betulinic acid derivatives.
- **Hot water tea** (decoction only) — captures polysaccharides, water-soluble small molecules. Lentinan from shiitake, GLPP from reishi.
- **Dried powder** (whole fruiting body or mycelium → dried → ground) — broad-spectrum but low concentration. Familiar consumption format (capsule or food-incorporation).
- **Co-administration with koji-condiment** (the integration point with the koji track) — daily shio-koji + periodic mushroom decoction, or mushroom powder added to koji condiments.

The UX is meaningfully different from the koji track and that's a feature, not a bug — different therapeutic categories may be best served by different formats. Daily koji shio-koji on rice for uricase; weekly reishi tea for GLPP-mediated ADA modulation; oyster mushroom in dinner stir-fry for ergothioneine.

## Why this isn't just "buy mushroom supplements"

Consumer-grade mushroom supplements have known quality issues:

1. **Species mis-identification** — DNA-barcoded studies of Ganoderma supplements regularly find <50% contain the species labeled.
2. **Compound content uncharacterized** — "reishi extract 1000mg" tells you nothing about GLPP, ganoderic acid, ergosterol content. Triterpene content alone varies 100× between products.
3. **Adulteration with inactive carriers** — mycelium-on-grain products are mostly grain (β-glucan from grain ≠ β-glucan from mushroom).
4. **Extract method opaque** — water-only extracts miss terpenoids; ethanol-only extracts miss polysaccharides; consumers can't tell which they bought.

**Open Enzyme's contribution to this track:** publish reproducible cultivation + extraction + characterization protocols. Strain selection criteria. HPLC/MS validation methods. Make a comp-014-style triage repeatable for any open-source contributor. The chemistry IS in the public domain — what's missing is the rigor.

## Six Phase 7 follow-ups queued

Same pattern as `engineered-lbp-chassis.md` and `sirna-urat1-modality.md`:

1. **Strain selection lit scan** — for each top species (G. lucidum, C. militaris, Pleurotus, Lentinula, Hericium, Trametes, Inonotus), identify which commercial / academic strains have characterized compound yields. CNKI + J-STAGE + Korean sources critical here (the multilingual ingestion the comp-014 anchor list was originally drafted for, now applied to cultivation rather than chokepoint mapping). Output: per-species strain table with cultivation precedent + compound yield evidence.

2. **comp-NNN cultivation method × yield study** — for ≥3 priority species (start with reishi GLPP + cordyceps cordycepin + oyster ergothioneine), comparative study of liquid fermentation vs solid-state vs fruiting body cultivation, measuring target-compound yield. Open Enzyme runs this as a literature meta-analysis first; wet-lab follow-up only if literature is insufficient or self-experimentation is direct path. The cordycepin yield literature in particular has wide ranges (0.5-5 mg/g dry weight in C. militaris fruiting body) that warrant consolidation.

3. **Extract characterization protocol standardization** — write the open-source SOPs for: (a) reishi dual-decoction extraction yielding GLPP-enriched fraction, (b) cordyceps water extraction yielding cordycepin + polysaccharide fraction, (c) HPLC quantification methods + reference standards. The goal is reproducibility — an Open Enzyme contributor anywhere should be able to follow the SOP and produce a comparable extract.

4. **GLPP + cordycepin synergy wet-lab gate** — comp-014 Phase 6 flagged this as the cleanest synergy pair in the breadth pass. Study design: PO HUA mouse model, 4 arms (control / GLPP alone / cordycepin alone / combination), measure SUA + cordycepin PK + ADA activity. Critical question: does ADA inhibition co-treatment extend cordycepin half-life enough to lower the daily dose meaningfully? This is a focused, falsifiable experiment.

5. **Hypothesis card H06 — medicinal-mushroom-complement track viability**. Specifies: what's the kill criterion? When would we abandon this track? Default: if (a) compound yield variability across cultivation batches exceeds 50% even with standardized protocols AND (b) standardized extracts cannot replicate the published in vivo effect sizes within 2× — that's pipeline failure regardless of mechanism truth. Falsifiable.

6. **Comparative chassis/platform matrix for gout** — extend `modality-chokepoint-matrix.md` with a new row "Native-compound mushroom complement" populated with the Phase 7 candidates × chokepoint mapping. Forces explicit comparison: koji-uricase vs reishi-GLPP at the gut-lumen / urate-axis cells. Doesn't pre-determine which wins; makes the comparison tractable for case-by-case decisions.

## Regulatory clarity (compared to the koji track)

The medicinal-mushroom-complement track has **simpler regulatory positioning** than engineered-organism tracks:

- All species are GRAS food (Pleurotus, Lentinula, Hericium) or established supplement-grade (Ganoderma, Cordyceps, Trametes, Inonotus)
- No genetic modification → no GMO regulatory burden
- Traditional-use precedent is decades to centuries (TCM, Kampo, Korean medicine, Western mycology)
- Existing supplement industry framework (DSHEA in US, equivalent elsewhere) — not a novel regulatory category

This is a real platform advantage, not just a cultivation-feasibility advantage. The koji-engineered tracks (uricase, lactoferrin, DAF SCR1-4) need GRAS-pathway-certification or equivalent for any therapeutic claim. The medicinal-mushroom track is already there.

**Caveat:** dosing claims and efficacy claims are still regulated. "Reishi extract supports urate metabolism" is supplement-language-acceptable; "reishi extract reduces serum uric acid by 40.6%" is structure-function-claim regulated under DSHEA + equivalent. Open Enzyme contributes the **reproducibility and characterization** layer; therapeutic claims remain user-side / clinician-side responsibility.

## Cross-references

- [`open-enzyme-vision.md`](./open-enzyme-vision.md) — top-level mission this expands
- [`open-source-platform.md`](./open-source-platform.md) — platform-strategy positioning; Phase 7 reinforces "explore every avenue" claim
- [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) — canonical chokepoint inventory; Phase 7 follow-up #6 adds new row
- [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md), [`sirna-urat1-modality.md`](./sirna-urat1-modality.md) — sister peer-track scope pages
- [`medicinal-mushroom-compound-mapping-computational.md`](./medicinal-mushroom-compound-mapping-computational.md) — comp-014 (the parent computational analysis that generated the Phase 7 candidate list)
- [`engineered-koji-protocol.md`](./engineered-koji-protocol.md), [`koji-home-fermentation.md`](./koji-home-fermentation.md) — koji track this complements

## Maintenance

- **When a new candidate species lands** (via comp-NNN extension, new wiki research, or a new compound-pharmacology paper): add to candidate species table; mark its top compounds + cultivation UX + regulatory status; consider for Phase 7 cultivation comp-NNN.
- **When a Phase 7 follow-up resolves**: promote from "queued" to canonical wiki content (e.g., the strain-selection lit scan output becomes a dedicated page per top species).
- **When the koji track adds a new compound**: re-evaluate whether the medicinal-mushroom track has a complementary compound at the same chokepoint (synergy pair candidate).
- **The track is a peer to koji, not a replacement.** Phase 7 deliverables expand the platform without competing with the koji-engineering thesis.

---

**Status:** Phase 1 (scope) committed 2026-05-06. Phases 2-6 are the queued follow-ups above. Brian's call on which phase to fire first.

---

## CTO-actionable items (no scientific expertise required, doable from desk this week)

These three items don't require chemistry expertise or wet-lab access — they're CTO-seat work that closes load-bearing dependencies for the rest of the Phase 7 track. Tracked here as canonical TODOs (and cross-referenced from [`open-questions.md`](./open-questions.md) for umbrella TODO aggregation).

**TODO-1 — Order a *P. citrinopileatus* (golden oyster) grow kit (~$30).**
Run the [Phase 7-2 home-cultivation protocol](../experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-7-cultivation-yield-meta-analysis.md) — pasteurized-straw bag, 12-20 day cycle, freeze-dry to powder. Document the yield + cycle + any deviations from the protocol. **Why:** self-experiment data validating the Open Enzyme reproducibility-layer thesis from your own kitchen; cleanest n=1 contribution to the medicinal-mushroom-complement track; zero scientific-expertise barrier; surfaces SOP-3 (EGT HILIC-HPLC) data dependencies if you have or get HPLC access; informs H06 hypothesis card §"Dimension 1 — Cultivation reproducibility" with first-operator data point. **Status:** ☐ Open. **Estimated effort:** $30 + 3 weeks elapsed (10 minutes ordering, 5 minutes/day during cycle, 2 hours documentation).

**TODO-2 — Email the Lin Zhanxi (林占熺) lab at Fujian Agriculture and Forestry University / Juncao Center.**
10-minute task asking for the Juncao GLPP cultivation SOP referenced in [PMID 36385640](https://pubmed.ncbi.nlm.nih.gov/36385640) (the GLPP 40.6% UA reduction paper). Search terms for finding the right contact: `菌草 灵芝 栽培` (CNKI) or institutional email at Fujian Agriculture & Forestry U. **Why:** closes the load-bearing CNKI gating dependency for [SOP-1 GLPP fractionation](./medicinal-mushroom-extract-sops.md#sop-1--ganoderma-lingzhi-glpp-polysaccharide-peptide-fractionation-load-bearing) — without the upstream Juncao substrate protocol, GLPP work cannot be reproduced from English-language literature alone (Phase 7-1a strain scan finding). Worst case they don't reply; best case it's a research collaboration opening with the canonical authority on Juncao-cultivated *G. lucidum*. **Status:** ☐ Open. **Estimated effort:** 10 minutes.

**TODO-3 — Open a GitHub Issue on Open-Enzyme repo for Phase 5b CNKI/J-STAGE deep-dive.**
Title suggestion: "Phase 5b CNKI/J-STAGE/KISS deep-dive contributions wanted — comp-014 medicinal-mushroom-complement track". Body: link to [Phase 7-1a Ganoderma scan](../experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-7a-ganoderma-strain-scan.md) §"Phase 5b CNKI follow-ups queued", Phase 7-1b §"Phase 5b CNKI/KISS follow-ups queued", Phase 7-1c §"Phase 5b multilingual follow-ups queued". Each scan's "queued follow-ups" section has specific paper IDs and search strategies — that's the contributor brief. **Why:** community-source the institutional-CNKI-access problem; exact OSS-thesis play; multiplies reach without requiring institutional subscription on Brian's side. **Status:** ☐ Open. **Estimated effort:** 15 minutes drafting + 5 minutes posting.

**TODO-4 (medium-term) — Frame comp-014 findings as recruiting material for the three open collaborator roles.**
Per [`team.md`](./team.md) the project is recruiting for three collaborator roles (Gut Microbiome / In Vivo Validation; Pharma Translation / Regulatory; Innate Immune Safety). The Phase 7 corpus — multi-vendor-validated chokepoint mapping, peer-reviewed verdicts, falsification cards, structured wet-lab gates — is significantly stronger ground for a recruiting conversation than "we have a wiki and an idea." **Why:** the SOP and wet-lab gate work needs a chemistry-capable collaborator; comp-014 demonstrates the project has substance. **Status:** ☐ Open. **Estimated effort:** 30-60 minutes drafting outreach + variable response time. **Suggested timing:** after TODO-1/2/3 land — having the self-experiment data point + the Lin lab outreach status + the GitHub Issue gives concrete context for the recruiting ask.

**Maintenance:** when an item closes, mark it ✓ with a date and brief outcome. New CTO-actionable items surface as the medicinal-mushroom-complement track evolves; add them here under the same numbered structure.
