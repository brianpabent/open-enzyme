---
title: "Genotype-Informed Supplement Quantification Workflow"
date: 2026-05-16
tags:
  - self-experiment
  - n-of-1
  - pharmacogenomics
  - genotype-stratified
  - quantification-ladder
  - personal-genome
  - workflow
  - operational
  - community-biolab
related:
  - self-experiment-protocol.md
  - personal-genome-protocol.md
  - quantification-ladder.md
  - enzyme-quantification-protocol.md
  - medicinal-mushroom-extract-sops.md
  - abcg2-modulators.md
  - gout-genetic-variants.md
  - t-axis-adjuvant-urate-mapping-computational.md
  - uricase-abcg2-genotype-stratification-computational.md
  - gout-action-guide.md
  - hypotheses/H08-gut-lumen-sink-platform-thesis.md
  - hypotheses/H09-community-fermentation-reliability.md
sources:
  - "self-experiment-protocol.md §12 (origin — promoted to standalone page 2026-05-16)"
status: published
---

# Genotype-Informed Supplement Quantification Workflow

The user-facing operational backbone for the platform's personalized-medicine thesis: a five-step closed-loop n=1 pharmacogenomics pipeline that turns "I took some supplement" into "I took *N* mg of compound *X*, chosen because my genotype favors it, verified at the dose level, with biomarker readout."

This page composes three previously disconnected wiki threads into a single named workflow:
1. Genotype-informed compound selection ([`personal-genome-protocol.md`](./personal-genome-protocol.md))
2. Home / community-biolab batch quantification ([`quantification-ladder.md`](./quantification-ladder.md) + [`enzyme-quantification-protocol.md`](./enzyme-quantification-protocol.md) + [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md))
3. Biomarker-tracked self-experimentation ([`self-experiment-protocol.md`](./self-experiment-protocol.md))

Standard self-experiment protocols treat supplement dose / form / timing as a **fixed input variable** — "take 500 mg of X, see what happens." That framing has a silent failure mode: a batch producing 20% of expected titer is indistinguishable from a mechanism that doesn't work. Without batch QC, every n=1 result is contaminated by invisible dose noise. The quantification ladder converts dose into a **verified variable**; the personal genome converts compound selection into a **genotype-informed variable**; the self-experiment protocol tracks the biomarker. Compose all three and every link in the chain is verified rather than assumed.

## The closed loop

> **genotype → compound selection → home or community-biolab production → Tier 2 batch QC → calibrated dose → biomarker tracking → adjust**

Every link verifiable. Every link logged.

## The five-step workflow

For each intervention the subject considers:

### 1. Genotype-inform the selection

Per [`personal-genome-protocol.md`](./personal-genome-protocol.md) §"Gout-specific pharmacogenomic query list" + the unified variant index at [`gout-genetic-variants.md`](./gout-genetic-variants.md). Specific variants change compound priority:

- **ABCG2 Q141K** (rs2231142) → prospective stratification variable, not a current butyrate recommendation. Butyrate can induce the wild-type allele through PPARγ; direct rescue of Q141K trafficking is unvalidated. The orthogonal chaperone screen is also inconclusive ([comp-047](./abcg2-q141k-chaperone-rescreen-computational.md)).
- **URAT1 gain-of-function variants** (uncommon; SLC22A12 not RHUC1-causing) → cordycepin > eurycomanone per [comp-015 v2](./t-axis-adjuvant-urate-mapping-computational.md)
- **SLC22A12 W258X (RHUC1 carrier)** → urate excretion is enhanced; the platform's gut-lumen sink thesis is *less* load-bearing for these carriers
- **NLRP3 gain-of-function variants** (CAPS spectrum; rare) → upweight CP6 (oridonin, BHB) over CP1–CP4
- **HLA-B\*58:01** (East Asian / Han Chinese / Korean / Thai ancestry) → exclude allopurinol; route urate-lowering through the gut-lumen sink, alternative uricosurics, or non-XO-inhibitor strategies
- **G6PD deficiency** → exclude systemic recombinant uricase (rasburicase, pegloticase contraindicated); gut-lumen approach is plausibly safer but empirically untested

Source-quality requirement: **clinical-grade genotyping** (rheumatologist-ordered panel or CLIA-grade direct-to-consumer service). Consumer panels (23andMe, AncestryDNA) are not recommended for trial-grade decisions per [`gout-action-guide.md`](./gout-action-guide.md) "This year (advanced)." Consumer panels are useful for *personal exploration* but should not be the data source when a clinical decision or supplement-stack stratification rides on the variant.

### 2. Source or produce the compound

Three production routes, choose by track:

- **Engineered koji / engineered yeast** for enzyme cassettes (uricase, lactoferrin, etc.) — see [`engineered-koji-protocol.md`](./engineered-koji-protocol.md) for the home-fermentation procedure.
- **Cultivated medicinal mushrooms / extracts** for native-compound payloads (cordycepin / pentostatin via whole-fermentate *Cordyceps militaris*, GLPP via *Ganoderma lucidum*, ergothioneine via *Pleurotus citrinopileatus*) — see [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md).
- **Commercial supplement purchase** when home production isn't tractable or the compound isn't fermentation-accessible (e.g., resistant starch from a documented RS2 source, sodium butyrate from a vendor with reported potency, FDA-approved off-label small molecules via compounding pharmacy per [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md)).

Log batch / lot / source in the [`self-experiment-protocol.md`](./self-experiment-protocol.md) §7 daily log. Without per-batch identity, downstream QC has no anchor.

### 3. Tier 2 batch QC via the quantification ladder

Use the matched assay from [`quantification-ladder.md`](./quantification-ladder.md):

- Cordycepin: diazo-coupling colorimetric assay
- Ergothioneine: Ellman's reagent
- Total polysaccharide (GLPP): phenol-sulfuric method
- Uricase activity: 293 nm UV absorbance
- Lactoferrin: protein-quantification + iron-saturation readout (see [`enzyme-quantification-protocol.md`](./enzyme-quantification-protocol.md))

Output: a per-batch potency number (mg compound per gram dried product, or activity units per gram). **Calibrate once at Tier 3** (vendor or community-biolab analytical assay — HPLC, GC-MS, LC-MS) if available; **track each subsequent batch at Tier 2** against the Tier 3 anchor. This is the calibrate-once / track-batches-cheap operating model that makes home QC sustainable.

### 4. Calibrate dose against batch potency

A batch returning 50% of expected potency means the subject takes 2× the gram weight to hit the same calibrated dose — or notes the silent underdosing as a confound in §7 of the self-experiment protocol. Without this step, batch variation produces invisible noise in the biomarker readout.

The discipline isn't "always hit the target dose." The discipline is "always know whether you hit it, and if not, by how much." A subject who knows they delivered 60% of target can attribute partial biomarker movement correctly; a subject who assumes they delivered 100% can't.

### 5. Track biomarkers per [`self-experiment-protocol.md`](./self-experiment-protocol.md) §3–§4

With dose closed as a verified variable, any biomarker movement is attributable to **dose × biology**, not **dose × batch-variation × biology**. The four-biomarker panel + serum UA quarterly is the canonical readout for gout-context interventions. Adjust the intervention based on the result.

## Proposed experiment example — ABCG2 Q141K heterozygous carrier × butyrate

A subject genotyped via a clinical-grade panel returns **ABCG2 Q141K heterozygous**. Butyrate can test PPARγ-driven induction of the remaining wild-type allele; whether it also rescues Q141K trafficking is an unvalidated mechanistic hypothesis. This is an experiment-design example, not a supplement recommendation.

Workflow application:

1. **Genotype:** Q141K heterozygous, confirmed via clinical lab (not 23andMe).
2. **Selection:** A research comparison of a butyrate-generating intervention against a matched control, with direct exposure and ABCG2-function readouts.
3. **Source:** Resistant starch from a known source (e.g., Bob's Red Mill unmodified potato starch, a documented RS2 source); sodium butyrate from a documented supplement vendor with reported potency.
4. **Tier 2 batch QC — exposure-proxy tier, NOT input-verification tier (clarified 2026-05-22 per comp-038 + sweep 2026-05-20 Connection #4 + Priority Action #4):** Indirect readout — stool SCFA panel (butyrate + acetate + propionate) at week 4 of intervention vs. baseline. **This step operates at the exposure-proxy tier, not the input-verification tier** — it answers "did butyrate eventually show up in the colon?" but it does NOT answer "did the supplement bottle contain the labeled dose?" For every other compound class in this workflow (cordycepin via diazo-coupling, EGT via Ellman's reagent, GLPP via phenol-sulfuric, engineered-strain uricase via 293 nm UV), the Tier 2 assay verifies the **input** directly. For butyrate, no such input-verification assay exists at the Tier 2 level (per [comp-038](./tier-2-butyrate-assay-audit-computational.md) YELLOW verdict, 2026-05-20). The "calibrate once at Tier 3, track batches at Tier 2" discipline (per [`quantification-ladder.md`](./quantification-ladder.md)) is partially broken at step 4 for butyrate.

   **Practical user guidance — pick one of three approaches:**

   - **(a) Vendor with published third-party potency verification.** Some sodium-butyrate vendors publish independent COA (certificate of analysis) showing butyrate-ester content vs. label claim. Where available, this substitutes for an in-house Tier 2 input check. Verify the COA is recent and lot-matched.
   - **(b) One-time Tier 3 GC-MS anchor on a single batch.** Send one batch to a GC-MS lab for absolute butyrate quantification (~$80–150). Treat this as the calibration anchor for that vendor + lot combination. As long as the vendor's manufacturing process is stable across lots, the anchor remains representative — but the calibration is vendor-specific and lot-class-specific, not universal.
   - **(c) Accept the exposure-proxy limitation explicitly.** Use the stool SCFA panel as documented, but interpret negative results with appropriate caution: a low stool butyrate could mean the supplement was under-dosed, OR that the microbiome didn't convert it, OR that the mechanism didn't work in this patient. Document the ambiguity in the experiment log so future analysis can re-examine if input-verification becomes available.

   Direct supplement quantification by HPLC-UV or electrochemical SCFA profiling is plausible (per comp-038's next-step path) but research-grade and not workflow-ready today. The workflow design IS sound; the butyrate-specific limitation is a class-level methodology gap (see "Tier 2 assay gap for microbiome-derived metabolites" below + the class-level Open Question added to `open-questions.md` 2026-05-22).
5. **Track biomarkers:** Serum UA quarterly + the standard four-biomarker panel per §4. Do not use comp-019 to predict genotype-specific UOX response; [comp-044](./gut-lumen-uricase-physiologic-regime-computational.md) retired that mapping. Q141K can still motivate a transporter-rescue experiment, but response attribution requires direct exposure and ABCG2-function evidence.

**Compound uncertainty:** a serum-UA or flare change cannot establish Q141K trafficking rescue. Exposure, surface ABCG2, functional urate flux, exertion, and regression to the mean remain confounded at n=1.

**What this example does NOT claim:**
- Does NOT claim butyrate alone produces clinically meaningful ΔSUA—gated by [H08 — Gut-Lumen Sink Mechanism](./hypotheses/H08-gut-lumen-sink-platform-thesis.md) and the absence of a typical-gout Phase 2b RCT.
- Does NOT claim the SCFA stool panel is mechanistically equivalent to a direct butyrate-supplement potency assay — it's an indirect exposure-proxy at step 4, explicitly documented as such above.
- DOES illustrate the workflow shape: every link in the chain is verified rather than assumed — *except* the butyrate input-verification at step 4, which is documented as the class-level methodology gap it is.

## Worked example — OCTN1/SLC22A4 variant carrier, substrate-engineered ergothioneine cultivation *(added 2026-05-22)*

A second example demonstrates the workflow with **home cultivation as the production route** and a more complete assay chain than the proposed Q141K experiment. It makes the medicinal-mushroom track visible, tests a contributor-accessible production route, and provides an EGT workflow dry run. It does not establish clinical efficacy.

A subject genotyped via a clinical-grade panel returns **OCTN1 / SLC22A4 variant** carrier — common variants (e.g., rs1050152, ~40–50% allele frequency in European populations) reduce OCTN1's transport capacity for ergothioneine into target tissues. The variant doesn't break the transporter outright; it shifts the dose-response curve, suggesting that *elevated* dietary EGT intake may be needed to reach equivalent tissue concentrations in variant carriers vs wild-type. Ergothioneine has anti-oxidative, anti-inflammatory, and Nrf2-pathway activity relevant to gout adjacent pathways (per [`medicinal-mushroom-complement-track.md`](./medicinal-mushroom-complement-track.md)).

Workflow application:

1. **Genotype:** OCTN1 / SLC22A4 variant carrier, confirmed via clinical-grade panel (one-shot test; ~$30–60 single-SNP PCR via Quest/LabCorp, or consumer-array raw data if 23andMe / Ancestry kit on file — rs1050152 is on standard arrays).
2. **Selection:** Elevated EGT priority. Dietary EGT comes overwhelmingly from mushrooms (the highest fungal EGT producer is *Pleurotus citrinopileatus* — golden oyster — at ~7.0 mg/g dry weight; *P. ostreatus* and *P. eryngii* also produce substantial EGT). For a variant carrier, the dose target is the upper end of the dietary-mushroom-derived plasma EGT range (~10–25 µM rather than ~5 µM baseline).
3. **Source / produce:** Two paths, either alone or combined.
   - **Path A — Commercial dried *P. citrinopileatus* fruiting body** (vendor with published EGT content per gram dry weight; this is the lower-friction option for the first n=1 cycle).
   - **Path B — Home cultivation on methionine-supplemented substrate per SOP-7.** Per [`medicinal-mushroom-extract-sops.md` SOP-7](./medicinal-mushroom-extract-sops.md), L-methionine 2 mM in mycelial culture produces a 1.7–3.1× EGT yield boost (Lee 2009 PMC3749454). Substrate kit + pharmacy-grade methionine (amino acid supplement; ~$15/kg) → grow *P. citrinopileatus* per the kit's standard protocol → harvest dried fruiting body. This is the distributed-contributor substrate-engineering execution — the variant carrier produces their own EGT-elevated mushroom batch with food-grade reagents at kitchen scale.
4. **Tier 2 batch QC — INPUT-VERIFICATION TIER (contrast with the Q141K example):** Per SOP-6 + SOP-3 (ergothioneine row), the Tier 2 assay is **Ellman's reagent (DTNB) thiol detection with smartphone colorimetry** at 412 nm. DTNB → 412 nm yellow on free thiol; EGT's free thiol is the substrate. Reagent is pharmacy-accessible (~$25 for enough DTNB for ~50 assays). Calibrate against the Tier 3 EGT-quantified reference batch (HILIC-HPLC with stable-isotope ²H₉-EGT internal standard per SOP-3; outsourced to a community-biolab or contract lab at ~$80–150 per batch). The calibrate-once-at-Tier-3 / track-batches-at-Tier-2 discipline works cleanly here — every link in the chain has a verified input measurement. **No exposure-proxy substitution.** This is what the workflow looks like when the methodology infrastructure is complete.
5. **Track biomarkers:** Standard four-biomarker panel per §4. Add EGT-specific biomarkers: serum ergothioneine (LC-MS/MS, send-out; ~$80–120) at baseline + 8–12 weeks; urinary 8-oxo-deoxyguanosine (oxidative-DNA-damage marker; standard send-out, ~$60) at baseline + endpoint as a downstream functional readout (EGT's anti-oxidative activity should reduce 8-oxodG if the dose is reaching mitochondria). The OCTN1-variant prediction is that a higher dietary EGT dose is required to reach the same serum EGT concentration as in wild-type carriers; the n=1 read is the dose-response shape, not absolute level.

**Why this example matters for testing the workflow end to end.** The proposed Q141K experiment has both an exposure-verification gap and an unvalidated direct-rescue mechanism. The OCTN1 / EGT example has a more complete assay chain and is therefore the cleaner workflow dry run. Its biomarker result would still be an n=1 feasibility signal, not clinical validation.

**What this example does NOT claim:**
- Does NOT claim EGT supplementation reduces gout flares at n=1 — EGT's gout-relevance is mechanistic (anti-oxidative / anti-inflammatory / Nrf2) rather than a documented anti-gout intervention.
- Does NOT claim the OCTN1 variant × EGT dose interaction predicts an effect size at the gout-flare level — the dose-response shape is the n=1 readout, not flare-frequency outcome.
- DOES illustrate the workflow shape with **no class-level Tier 2 methodology gap** — contrast with the proposed Q141K experiment above.
- DOES operationalize the cheapest end-to-end workflow dry-run (per sweep 2026-05-20 Riskiest Assumption #1).

## Pattern library — variant → pathway vulnerability → bypass intervention *(added 2026-05-22)*

The OCTN1 × EGT worked example and the Q141K and CFH candidate hypotheses illustrate a reusable pattern, but they do not share the same evidence status. The workflow's value is making those differences and their falsification gates explicit.

**Pattern statement:**

> Identify a variant-linked vulnerability → propose an intervention that might bypass or rescue it → verify exposure and mechanism → test the genotype interaction. A carrier-specific recommendation requires that evidence; mechanistic analogy alone is insufficient.

**Instances and evidence status:**

| Variant | Pathway vulnerability | Bypass intervention | Status |
|---|---|---|---|
| ABCG2 Q141K (rs2231142) | Misfolded transporter; reduced intestinal urate efflux | PPARγ induction of remaining WT ABCG2 is supported; direct butyrate rescue of Q141K is a testable hypothesis | Proposed experiment; not a confirmed bypass |
| OCTN1 / SLC22A4 variant (rs1050152 et al.) | Reduced EGT transport capacity → lower tissue EGT for equivalent dietary intake | Elevated dietary EGT to shift the dose-response upward | Documented worked example above (added 2026-05-22) |
| CFH Y402H (rs1061170) | Weakened Factor H alternative-pathway complement regulation → elevated C5a generation on MSU crystals | Dietary CP0 candidates (rosmarinic acid, luteolin, Houttuynia, Helicteres) operating **upstream of Factor H** rather than through Factor H | Documented [`complement-c5a-gout.md` §9.7](./complement-c5a-gout.md) + [`cfh-mechanism-dissociation-cp0-candidates-computational.md`](./cfh-mechanism-dissociation-cp0-candidates-computational.md). AMD-paradox counter-evidence flagged. UKB ↔ AoU biobank cross-tab is the empirical falsification gate. |

**Unaudited candidate instances (queued as Phase 2 audit):**

- **URAT1 W258X loss-of-function variants** → reduced renal urate reabsorption → carriers may benefit more from **uricosurics** (lesinurad, probenecid) OR from **siRNA-URAT1** ([`sirna-urat1-modality.md`](./sirna-urat1-modality.md)) than wild-type carriers, because the variant has already done part of the URAT1-blocking work. Loss-of-function carriers are protective for gout at baseline — the question is whether the *therapeutic* response curve differs for carriers vs non-carriers when uricosurics are prescribed.
- **NLRP3 CAPS gain-of-function variants** (NLRP3 R260W, D305N, etc. — cryopyrin-associated periodic syndromes) → constitutive NLRP3 activation. Carriers with gout-overlap phenotype may benefit more from **direct NLRP3 inhibitors (CP2-CP4)** than from upstream priming interventions (CP0-CP1), because the priming step is bypassed by the gain-of-function. Different "upstream vs downstream of the broken protein" logic from the Q141K and CFH examples — here the variant makes the downstream node hot, so downstream blockade is the bypass.
- **HLA-B*58:01 carriers** → severe hypersensitivity reaction to allopurinol (the standard first-line ULT) → carriers must route ULT through **non-XO-inhibitor pathways** (uricosurics, gut-lumen sink via engineered koji, or future modalities). Pharmacogenetic contraindication rather than mechanism-bypass, but the operational pattern is structurally identical: variant → vulnerability (here drug-class toxicity) → bypass class.

**How to use the pattern.** When a new genetic variant is added to [`gout-genetic-variants.md`](./gout-genetic-variants.md), ask: (1) what specific pathway step does the variant break or amplify? (2) is there a known intervention class that operates *around* that step (upstream, downstream, or via a different protein in the same pathway)? (3) if yes, write a worked example like the Q141K / OCTN1 / CFH examples above. If no, queue the variant as "named vulnerability, no bypass intervention identified" — the absence is itself useful information about where the platform's discovery engine should look.

**What the pattern does NOT claim.** Carriers benefiting more than wild-type is the **mechanistic prediction**, not an empirical fact for any of the unaudited candidates. The CFH × AMD counter-evidence (Vavvas 2018, Merle 2015) is the empirical case study that the pattern doesn't always hold — AMD interventions that work *through* Factor H paradoxically harm carriers, while the OE prediction is that AMD interventions are not analogous to the dietary-CP0 candidates the OE corpus identifies (which work *upstream of* Factor H). Whether the upstream-bypass logic holds in gout for CFH carriers is empirically open and gated on the UKB ↔ AoU cross-tab. The same falsification structure applies to every new pattern instance: predict carrier-benefit direction, design a falsification test, accept null or inverted results as productive information.

**Cross-references:** [`gout-genetic-variants.md`](./gout-genetic-variants.md) (variant catalog), [`abcg2-modulators.md`](./abcg2-modulators.md) (Q141K instance), [`cfh-mechanism-dissociation-cp0-candidates-computational.md`](./cfh-mechanism-dissociation-cp0-candidates-computational.md) (CFH instance), [`medicinal-mushroom-complement-track.md`](./medicinal-mushroom-complement-track.md) (OCTN1 / EGT instance + medicinal mushroom track), [`modality-chokepoint-matrix.md`](./modality-chokepoint-matrix.md) (intervention class taxonomy useful for identifying bypass routes).

## Why this exists

Two failure modes the workflow blocks:

**1. Silent underdosing.** Without batch QC, a subject who "did the protocol" but happened to source a 20%-potency batch will conclude the mechanism doesn't work. With batch QC, they see the dose was 0.2× target and either re-dose against verified potency or flag the source for replacement.

**2. Genotype-blind experimental design.** Q141K reduces transporter function, but genotype-specific intervention response has not been established for the proposed butyrate route. Stratified experiments can measure that interaction instead of assuming it.

The workflow is the **operational instantiation** of the platform's "open-source, democratized, rigorous" thesis. Open-source: every step uses methods documented in the wiki. Democratized: every step is achievable at home or via a community biolab. Rigorous: every step is verified, not assumed.

## How this fits with H09 (Community Fermentation Reliability)

[H09](./hypotheses/H09-community-fermentation-reliability.md) is the platform-level test of whether home / community-biolab fermentation can reliably deliver therapeutic doses. The workflow above *assumes* H09 holds — that home-produced fermentate has enough cordycepin / lactoferrin / uricase activity to matter. If H09 fails, the workflow's step 2 (Source or produce) reshapes: genotype-informed selection (step 1) still works, dose calibration (step 3-4) still works, biomarker tracking (step 5) still works, but home-production routes through commercial supplement vendors with verified potency rather than home fermentation. The workflow shape survives even if the home-production assumption fails.

## Open follow-ups

### Tier 3 anchor library

A growing list of compound-specific Tier 3 anchors (GC-MS / HPLC / spectrophotometric vendor or community-biolab assays) that the Tier 2 home assays calibrate against. Currently scattered across [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md), [`enzyme-quantification-protocol.md`](./enzyme-quantification-protocol.md), and [`quantification-ladder.md`](./quantification-ladder.md). Consolidating into a single anchor table is queued for when enough Tier 3 entries land — premature today; ~6+ entries justifies the index.

### Multi-user pilot validation

The workflow has been instantiated at n=1. The natural next-step gate is an N=5–10 multi-user pilot that validates the workflow under realistic user-variability conditions before the larger H09 community-fermentation trial. Tracked as walkthrough Item 20 (open-question-3 in the 2026-05-15 sweep batch).

**Pre-pilot single-subject anchor (added 2026-05-22 per sweep 2026-05-20 Riskiest Assumption #1):** the OCTN1 / EGT worked example above is the cheapest path to a *fully-documented* end-to-end execution of the workflow on a single subject with no class-level methodology gaps. Cost ~$500, time 8–12 weeks. Sequenced before the N=5–10 multi-user pilot — the single-subject execution surfaces operational friction (cultivation timing, reagent sourcing, Tier 2 colorimetry reliability, biomarker turnaround) without the recruitment + coordination overhead of multi-user work. Note distinction from Pass 3's framing of the prior Riskiest Assumption: the workflow has been instantiated at n=1 in pieces (Q141K example specified, OCTN1 example specified, individual Tier 2 assays validated separately), but no subject has executed the FULL five-step pipeline end-to-end with documented Tier 2 batch QC + Tier 3 anchor + biomarker readout published in one place. The EGT worked example provides that anchor. The N=5–10 multi-user pilot then exercises the inter-operator variability dimension (per the [Tier 2 inter-operator reproducibility open question](./open-questions.md) under Compound-Specific Questions).

### Tier 2 assay gap for microbiome-derived metabolites

The proposed Q141K experiment above uses a **stool SCFA panel** only as a downstream exposure proxy. It does not measure input potency, epithelial concentration, surface trafficking, or urate flux. Those are separate gates; a stool result cannot by itself establish mechanism or response.

**This is a known methodology gap, not a workflow failure.** It applies to any future intervention relying on microbiome-derived metabolites (SCFAs, bile acids, indoles, lactate, etc.). Three candidate Tier 2 paths worth investigating:

1. **Colorimetric** — does a butyrate-specific colorimetric reagent exist at hobbyist-lab affordability? (Most SCFA assays require derivatization + GC-MS.)
2. **Enzymatic** — could an enzyme-coupled assay (e.g., acetyl-CoA synthetase-coupled NADH readout) be miniaturized for Tier 2?
3. **Breath hydrogen proxy** — a hydrogen breath test correlates loosely with colonic fermentation activity; could it be calibrated as a *change-in-butyrate-production* proxy rather than an absolute butyrate concentration?

comp-038 (2026-05-20) ran the first desk audit and returned **YELLOW**: no ready-to-adopt simple/home colorimetric or breath-based butyrate assay surfaced. HPLC-UV is plausible for engineered-strain / culture-supernatant work, and electrochemical fecal SCFA profiling is a promising stool-specific future direction, but both require full-text/protocol review and paired GC-MS validation before adoption. **A validated Tier 2 butyrate proxy would still strengthen the workflow not just for Q141K but for any future microbiome-metabolite intervention**; comp-038 narrows the next step to a focused Tier 2-vs-GC-MS validation, not a broad assay hunt. See [`tier-2-butyrate-assay-audit-computational.md`](./tier-2-butyrate-assay-audit-computational.md).

Tracked from 2026-05-19 sweep-walkthrough Cluster B1; first computational prior completed as comp-038 on 2026-05-20.

## Cross-references

- [`self-experiment-protocol.md`](./self-experiment-protocol.md) — parent self-experiment framework (§3–§4 biomarker tracking, §7 daily log); §12 now points here for the workflow detail
- [`personal-genome-protocol.md`](./personal-genome-protocol.md) — variant-informed compound selection layer (step 1)
- [`gout-genetic-variants.md`](./gout-genetic-variants.md) — unified cascade-stratified variant index
- [`quantification-ladder.md`](./quantification-ladder.md) — Tier 1 / 2 / 3 framework for batch QC (step 3)
- [`enzyme-quantification-protocol.md`](./enzyme-quantification-protocol.md) — enzyme-specific Tier 2 assays
- [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) — mushroom-extract Tier 2 SOPs
- [`abcg2-modulators.md`](./abcg2-modulators.md) — Q141K rescue mechanisms (worked example anchor)
- [`uricase-abcg2-genotype-stratification-computational.md`](./uricase-abcg2-genotype-stratification-computational.md) — superseded comp-019 interpretation; quantitative predictions retired
- [`gout-action-guide.md`](./gout-action-guide.md) — user-facing entry point; "This year (advanced)" sections route here
- [H08](./hypotheses/H08-gut-lumen-sink-platform-thesis.md), [H09](./hypotheses/H09-community-fermentation-reliability.md) — platform-level hypotheses the workflow operationalizes

---

*Promoted from `self-experiment-protocol.md` §12 on 2026-05-16 per walkthrough Items 8 + 21 (sweep `8653de9` Connection 2 + Priority Action 2). Both items closed via this promotion.*
