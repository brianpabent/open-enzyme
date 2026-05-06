# Phase 6 — Triage of Phase 5-Surviving Leads

**Date:** 2026-05-06
**Method:** comp-013-style production-route + dose-feasibility + chokepoint-occupancy assessment, adapted for non-small-molecule compound classes.

## Summary

- **PURSUE (koji-track / chemical-synthesis):** DAE, cordycepin
- **PURSUE in Phase 7 (medicinal-mushroom cultivation track):** GLPP
- **DEFER (Phase 5b prerequisites):** AMC-BFE, FZ-Poria
- **DROP:** lovastatin

## DAE — methyl 2,4-dihydroxybenzoate (DAE)

**Class:** small molecule (phenolic ester)
**MW:** 168.15 g/mol
**Source:** Ganoderma applanatum (computational attribution; commercial reagent in PMID 35750011)
**Chokepoints:** XO, URAT1 (expression-level)

**Verdict: PURSUE**

*Rationale:* Defined small molecule with verified mouse dose-response. Human equivalent dose (~455 mg/day at top mouse dose) is supplement-grade and feasible. Chemical synthesis is the right production route — heterologous expression in koji is not warranted for a simple methyl ester. Wet-lab gate is straightforward.

**Dosing math:** Mouse top dose → human equivalent ≈ 6.5 mg/kg → ~455 mg/day for a 70 kg person.

**Production routes:**

- chemical synthesis ⭐ — trivial (Fischer esterification of 2,4-dihydroxybenzoic acid + methanol); cost: <$1/g at 100g scale
- commercial purchase — available (Sigma, Combi-Blocks); cost: ~$50/g pharma grade
- extraction from G. applanatum — low — natural abundance not validated; Model B flagged this gap; cost: high
- heterologous expression in koji — not warranted — small phenolic, synthesis is much easier than engineering BGC; cost: n/a

**Wet-lab gate:**

- Synthesize or purchase 100g methyl 2,4-dihydroxybenzoate (≥99% purity, HPLC)
- PO+HX mouse HUA model, dose-response 20/40/80 mg/kg PO daily x 14d, n=8/group
- Primary endpoint: SUA reduction at d14
- Mechanism: liver XO activity + renal URAT1 mRNA/protein at endpoint
- Safety: ALT/AST, BUN/Cr, body weight, liver/kidney histology
- **Critical**: confirm SUA does not over-correct below normal mouse SUA (~88 µmol/L) — Phase 5 flagged 134 is sub-normal-control

**Phase 5b verifications outstanding:**

- Full PDF of PMID 35750011 (~$30) — verify XOD IC50, kinetic constants, inhibition type
- CNKI dive on Yong/Liang group's TCM diuresis literature (per Model A recommendation)
- Confirm DAE natural abundance in G. applanatum (Model B flag)

---

## cordycepin — cordycepin (3'-deoxyadenosine)

**Class:** small molecule (nucleoside analog)
**MW:** 251.24 g/mol
**Source:** Cordyceps militaris (cultivated) — abundant; sparse in wild O. sinensis
**Chokepoints:** URAT1

**Verdict: PURSUE**

*Rationale:* Production route is commercial fermentation (mature) or home C. militaris cultivation (substrate-limited but feasible). Mechanism (URAT1 modulation) is in-vivo-validated. The BA caveat is the binding constraint — combination with ADA inhibitor (e.g., GLPP from G. lucidum?) could dramatically extend half-life. Adjacent to GLPP — the comp-014 GLPP+cordycepin combination is a real Phase 6 question.

**Dosing math:** Mouse top dose → human equivalent ≈ 2.0 mg/kg → ~142 mg/day for a 70 kg person.

**BA caveat:** Cordycepin has notoriously poor oral BA — rapidly deaminated to 3'-deoxyinosine by serum/intestinal ADA. Effective BA may be <5% without prodrug or co-administration with ADA inhibitor.

**Production routes:**

- C. militaris liquid fermentation (commercial) ⭐ — well-established; commercial cordycepin available at $200-500/g pharma-grade; cost: ~$200-500/g
  - Shih et al. published optimized fermentation conditions; this is the production-mature route
- C. militaris solid-state fermentation (home) — moderate — slower than liquid culture; brown rice substrate works; cost: low (substrate + spores)
  - Home-grown Cordyceps fruiting body cordycepin content varies 0.5-5 mg/g dry weight
- chemical synthesis — possible but more complex than DAE (nucleoside chemistry); not cost-competitive with fermentation; cost: high
- heterologous expression in koji — not warranted — C. militaris fermentation is mature; cost: n/a

**Wet-lab gate:**

- Source: commercial cordycepin (≥98% HPLC purity) for first wet-lab pass; Phase 7 home-cultivation comparison
- PO HUA mouse model, dose-response 6.25/12.5/25 mg/kg PO daily x 14d
- Primary endpoint: SUA reduction
- Mechanism arm: cordycepin alone vs cordycepin + ADA-inhibitor (pentostatin or GLPP)
- Pharmacokinetics: cordycepin + 3'-deoxyinosine plasma levels at multiple timepoints
- Critical question: does ADA inhibition co-treatment extend cordycepin half-life enough to lower the daily dose?

**Phase 5b verifications outstanding:**

- PK studies with/without ADA inhibitor co-administration
- Verify cordycepin content in commercially available C. militaris fruiting bodies (literature varies 0.5-5 mg/g dry weight)

**Synergy candidates:**
- GLPP (G. lucidum) — ADA inhibition could extend cordycepin half-life. Both are accessible via medicinal mushroom cultivation. This is the Phase 7 medicinal-mushroom-complement integration point.

---

## GLPP — GLPP (Ganoderma lucidum polysaccharide-peptide)

**Class:** polysaccharide-peptide hybrid (~520 kDa; glycopeptide vs proteoglycan distinction unresolved per Model B)
**MW:** 520000 Da
**Source:** Ganoderma lucidum mycelium (Juncao substrate, per Yang lab)
**Chokepoints:** ADA, GLUT9, OAT1, (Keap1/Nrf2 in sister paper PMC11351902)

**Verdict: PURSUE in Phase 7 (cultivation track, not koji-engineering)**

*Rationale:* Polysaccharide-peptide is fundamentally not a koji-engineering target — it's a fermentation product of G. lucidum mycelium. This is exactly the Phase 7 medicinal-mushroom-complement strategy use case. Native cultivation route is mature; the binding question is **strain selection + extraction protocol standardization** rather than genetic engineering. Polysaccharides have ~0% systemic bioavailability — they work via gut signaling (immune modulation, microbiome), not direct ADA binding. The 'ADA inhibition' mechanism is likely indirect via gut-associated lymphoid tissue.

**Dosing math:** Mouse top dose → human equivalent ≈ 32.5 mg/kg → ~2276 mg/day for a 70 kg person.

**Production routes:**

- G. lucidum mycelium liquid fermentation ⭐ — well-established commercial process; multiple manufacturers; cost: ~$1-5/g extract grade
  - Phase 7 territory — native cultivation track, not koji-engineering track
- G. lucidum solid-state fermentation (home) — moderate — Reishi mushroom kits available consumer-grade; fruiting body extraction yields lower polysaccharide than mycelium; cost: low ($10-30 grow kit)
- G. lucidum fruiting body extraction (commercial supplement) — ubiquitous; quality varies wildly; 'GLPP' specifically requires defined extraction protocol; cost: consumer supplements $0.50-2/g but uncharacterized
- heterologous expression in koji — infeasible — polysaccharide-peptide is biosynthesis product, not single gene; mycelium-specific glycosylation machinery; cost: n/a

**Wet-lab gate (Phase 7 cultivation track):**

- Strain selection: compare 3-5 commercial G. lucidum strains for GLPP yield + composition
- Cultivation method comparison: liquid fermentation (defined media) vs Juncao substrate vs other solid-state
- Extraction protocol: hot water > ethanol precipitation > Sephacryl S-500 chromatography (per Yang lab method)
- Characterization: MW (SEC-MALS), peptide composition (amino acid analysis), glycan linkage (NMR)
- Mechanism question: is ADA inhibition direct or indirect? Test purified GLPP fraction vs intestinal lysate ADA in vitro
- Mouse HUA model verification: 200/400 mg/kg PO daily, replicate 40.6% UA reduction claim

**Phase 5b verifications outstanding:**

- Full PDF of PMID 36385640 (Food & Function paywalled)
- Sister paper PMC11351902 review for Keap1/Nrf2 mechanism evidence
- Resolve glycopeptide vs proteoglycan distinction (Model B flag) — affects pharmacology framing

**Synergy candidates:**
- cordycepin — GLPP's ADA inhibition could extend cordycepin's notoriously short half-life. Both are home-cultivable medicinal mushrooms. Phase 7 medicinal-mushroom-complement integration.

---

## AMC-BFE — AMC-BFE (Cordyceps militaris × Astragalus membranaceus solid-state fermentation extract)

**Class:** whole extract — active components NOT identified
**Source:** Cordyceps militaris co-fermented with Astragalus
**Chokepoints:** URAT1, GLUT9, (hepatic) ABCG2, PPARα downstream

**Verdict: DEFER — full PDF retrieval required before triage**

*Rationale:* Phase 5 deep-read flagged that authors explicitly hedge 'contribution of individual metabolites requires further investigation.' Whole-extract evidence cannot be triaged with comp-013 IC50-occupancy methodology — there's no defined active compound to model. Phase 6 cannot complete this triage without (a) full PDF + (b) compound-fractionation work.

**Production routes:**

- solid-state co-fermentation (academic protocol) — documented in analog studies (Zhao 2025 PMC12805540); reproducibility uncertain without full PDF; cost: moderate — substrate + dual-strain inoculum

**Wet-lab gate:**

BLOCKED on Phase 5b: retrieve full PDF, attempt compound fractionation, then re-triage. Estimated $30 + 4-6 weeks fractionation → re-enter Phase 6.

---

## lovastatin — lovastatin (mevinolin)

**Class:** small molecule (HMG-CoA reductase inhibitor, statin class)
**MW:** 404.54 g/mol
**Source:** Aspergillus terreus (industrial), Pleurotus ostreatus (native producer)
**Chokepoints:** HDAC6 (in vitro 16.3 µM), PPARγ (functional 1 µM, Kd ~110 µM)

**Verdict: DROP**

*Rationale:* In vitro HDAC6 + PPARγ IC50s are ~100-1000× higher than clinical lovastatin Cmax. The chokepoint hits are pharmacologically irrelevant at clinical doses. Lovastatin's gout-axis relevance, IF any, is via hepatic HMG-CoA reductase inhibition reducing isoprenoid synthesis (NLRP3-priming-adjacent), NOT via the ChEMBL HDAC6/PPARγ off-targets. Statins are already a commercial drug class — Open Enzyme has nothing to add by re-engineering them.

**Clinical exposure at standard dose:** Lovastatin 20-80 mg/day → systemic Cmax ~50-200 nM
**In vitro chokepoint IC50:** HDAC6 16.3 µM; PPARγ Kd ~110 µM
**Occupancy at clinical exposure:** <0.5% at HDAC6; <0.1% at PPARγ

**Wet-lab gate:**

Not applicable — DROPPED for chokepoint occupancy reasons. The Pleurotus-as-native-lovastatin-producer thesis remains valid but for HMG-CoA-reductase pathway, not the comp-014 chokepoint set.

---

## FZ-Poria — Wolfiporia cocos (Poria cocos) in FZ multi-herb formula

**Class:** multi-herb formula component (Poria + Pinellia + Cinnamomum + Achyranthes + Atractylodes)
**Source:** Wolfiporia cocos sclerotium (TCM 茯苓)
**Chokepoints:** ABCG2, GLUT9, OAT1, NLRP3/ASC

**Verdict: DEFER — needs single-component Poria study before advancing**

*Rationale:* FZ formula contains 5+ herbs. The chokepoint-modulation is real for the formula but unattributable to Poria specifically. A standalone Poria study would be needed to triage. CNKI likely has single-component Poria pharmacology papers (Wolfiporia is heavily studied in TCM); a Phase 5b CNKI dive could resolve this.

---

## Synergy pairs

### GLPP + cordycepin

GLPP's ADA inhibition could extend cordycepin's notoriously short half-life (cordycepin is rapidly deaminated to 3'-deoxyinosine by serum/intestinal ADA). Both are accessible via medicinal mushroom cultivation (G. lucidum + C. militaris). This is the cleanest Phase 7 medicinal-mushroom-complement integration point — two home-cultivable organisms producing complementary compounds.

**Wet-lab question:** Does combined GLPP + cordycepin co-administration achieve URAT1 modulation at lower individual doses than either alone, with acceptable PK/PD?

---

## Phase 7 handoff

**Compounds routed to cultivation track:** GLPP (G. lucidum), cordycepin (C. militaris), ergothioneine (Pleurotus ostreatus, koji A. oryzae) — comp-014 anchor species

**Compounds staying with koji engineering track:** DAE (chemical synthesis preferred; not engineering candidate), DAF SCR1-4 / uricase / lactoferrin (existing koji engineering thesis, not comp-014 derived)

**Platform thesis expansion:** Engineering chassis (koji) + native-compound complement (medicinal mushrooms) = expanded Open Enzyme platform. Phase 7 scope page formalizes the parallel track.
