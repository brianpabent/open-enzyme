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

- **ABCG2 Q141K** (rs2231142) → butyrate emphasis (PPARγ-driven WT ABCG2 induction + HDAC trafficking rescue for the Q141K variant per [`abcg2-modulators.md`](./abcg2-modulators.md) §6); pharmacological-chaperone class as the orthogonal small-molecule track (chassis-pending; [comp-032](./computational-experiments.md))
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

## Worked example — ABCG2 Q141K heterozygous carrier, butyrate-emphasis stack

A subject genotyped via a clinical-grade panel returns **ABCG2 Q141K heterozygous** (rs2231142 C/A). Per [`abcg2-modulators.md`](./abcg2-modulators.md), butyrate is the dual-mechanism lever for this genotype: PPARγ-driven ABCG2 induction acts on the wild-type allele, and HDAC-inhibitor trafficking rescue acts on the Q141K variant. The standard supplement-stack recommendation elevates butyrate via fermentable-fiber-rich diet + targeted butyrate-producing probiotics or direct butyrate-ester supplementation.

Workflow application:

1. **Genotype:** Q141K heterozygous, confirmed via clinical lab (not 23andMe).
2. **Selection:** Butyrate-emphasis stack — fermentable-fiber dietary baseline (resistant starch, inulin, RS2-type sources) + optional direct sodium butyrate supplementation.
3. **Source:** Resistant starch from a known source (e.g., Bob's Red Mill unmodified potato starch, a documented RS2 source); sodium butyrate from a documented supplement vendor with reported potency.
4. **Tier 2 batch QC:** Indirect readout — stool SCFA panel (butyrate + acetate + propionate) at week 4 of intervention vs. baseline. This is a *biomarker* of effective butyrate delivery, not a direct quantification of the supplement potency — but it's the available Tier 2 surface for the workflow. Direct supplement quantification would require GC-MS → defer to a Tier 3 lab if precision matters for a specific decision.
5. **Track biomarkers:** Serum UA quarterly + the standard four-biomarker panel per §4. Predicted effect from [comp-019](./uricase-abcg2-genotype-stratification-computational.md): WT/WT non-Q141K cohort sees larger ΔSUA than Q141K heterozygotes under the substrate-limited gut-lumen uricase regime; for Q141K-positive subjects, the rescue mechanism (HDAC inhibition) is the dominant lever and per-patient response can be larger if it activates. Track UA trajectory at 3-month intervals.

**What this example does NOT claim:**
- Does NOT claim butyrate alone produces clinically meaningful ΔSUA — gated by [H08 — Gut-Lumen Sink Platform Thesis](./hypotheses/H08-gut-lumen-sink-platform-thesis.md) and the absence of a typical-gout Phase 2b RCT.
- Does NOT claim the SCFA stool panel is mechanistically equivalent to a direct butyrate-supplement potency assay — it's an indirect proxy.
- DOES illustrate the workflow shape: every link in the chain is verified rather than assumed.

## Why this exists

Two failure modes the workflow blocks:

**1. Silent underdosing.** Without batch QC, a subject who "did the protocol" but happened to source a 20%-potency batch will conclude the mechanism doesn't work. With batch QC, they see the dose was 0.2× target and either re-dose against verified potency or flag the source for replacement.

**2. Genotype-blind selection.** Without genotype-informed selection, a Q141K homozygote will get the same recommendation as a Q141K-negative subject, even though their response curves are different. Stratified selection puts the right compound class in front of the right genotype.

The workflow is the **operational instantiation** of the platform's "open-source, democratized, rigorous" thesis. Open-source: every step uses methods documented in the wiki. Democratized: every step is achievable at home or via a community biolab. Rigorous: every step is verified, not assumed.

## How this fits with H09 (Community Fermentation Reliability)

[H09](./hypotheses/H09-community-fermentation-reliability.md) is the platform-level test of whether home / community-biolab fermentation can reliably deliver therapeutic doses. The workflow above *assumes* H09 holds — that home-produced fermentate has enough cordycepin / lactoferrin / uricase activity to matter. If H09 fails, the workflow's step 2 (Source or produce) reshapes: genotype-informed selection (step 1) still works, dose calibration (step 3-4) still works, biomarker tracking (step 5) still works, but home-production routes through commercial supplement vendors with verified potency rather than home fermentation. The workflow shape survives even if the home-production assumption fails.

## Open follow-ups

### Tier 3 anchor library

A growing list of compound-specific Tier 3 anchors (GC-MS / HPLC / spectrophotometric vendor or community-biolab assays) that the Tier 2 home assays calibrate against. Currently scattered across [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md), [`enzyme-quantification-protocol.md`](./enzyme-quantification-protocol.md), and [`quantification-ladder.md`](./quantification-ladder.md). Consolidating into a single anchor table is queued for when enough Tier 3 entries land — premature today; ~6+ entries justifies the index.

### Multi-user pilot validation

The workflow has been instantiated at n=1. The natural next-step gate is an N=5–10 multi-user pilot that validates the workflow under realistic user-variability conditions before the larger H09 community-fermentation trial. Tracked as walkthrough Item 20 (open-question-3 in the 2026-05-15 sweep batch).

## Cross-references

- [`self-experiment-protocol.md`](./self-experiment-protocol.md) — parent self-experiment framework (§3–§4 biomarker tracking, §7 daily log); §12 now points here for the workflow detail
- [`personal-genome-protocol.md`](./personal-genome-protocol.md) — variant-informed compound selection layer (step 1)
- [`gout-genetic-variants.md`](./gout-genetic-variants.md) — unified cascade-stratified variant index
- [`quantification-ladder.md`](./quantification-ladder.md) — Tier 1 / 2 / 3 framework for batch QC (step 3)
- [`enzyme-quantification-protocol.md`](./enzyme-quantification-protocol.md) — enzyme-specific Tier 2 assays
- [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) — mushroom-extract Tier 2 SOPs
- [`abcg2-modulators.md`](./abcg2-modulators.md) — Q141K rescue mechanisms (worked example anchor)
- [`uricase-abcg2-genotype-stratification-computational.md`](./uricase-abcg2-genotype-stratification-computational.md) — comp-019 genotype-stratified ΔSUA modeling
- [`gout-action-guide.md`](./gout-action-guide.md) — user-facing entry point; "This year (advanced)" sections route here
- [H08](./hypotheses/H08-gut-lumen-sink-platform-thesis.md), [H09](./hypotheses/H09-community-fermentation-reliability.md) — platform-level hypotheses the workflow operationalizes

---

*Promoted from `self-experiment-protocol.md` §12 on 2026-05-16 per walkthrough Items 8 + 21 (sweep `8653de9` Connection 2 + Priority Action 2). Both items closed via this promotion.*
