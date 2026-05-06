---
title: "Medicinal Mushroom Extract Characterization SOPs (Phase 7-3 Stub)"
date: 2026-05-06
tags:
  - medicinal-mushroom-complement
  - phase-7
  - sop
  - extract-characterization
  - stub
  - reproducibility
related:
  - medicinal-mushroom-complement-track.md
  - medicinal-mushroom-compound-mapping-computational.md
  - hypotheses/H06-medicinal-mushroom-complement-track.md
  - validation-experiments.md
sources:
  - "comp-014 Phase 7-2 cultivation × yield meta-analysis (`experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-7-cultivation-yield-meta-analysis.md`) — handoff items for SOP work"
  - "comp-014 Phase 7-1a/b/c strain selection lit scans"
  - "Phase 7 scope page `medicinal-mushroom-complement-track.md` §6 follow-up #3"
status: stub
---

# Medicinal Mushroom Extract Characterization SOPs — Stub

> **Stub status.** Committed 2026-05-06 to register the planned SOP work in canonical wiki. Each section below is a placeholder enumerating the protocol that will land here when a chemistry collaborator joins or when self-experimentation reaches the relevant stage. Cross-references point to the comp-014 outputs that informed the SOP scope.
>
> Per H06 hypothesis card §"Dimension 2 — Characterization protocol robustness", these SOPs need to achieve **±15% inter-operator reproducibility** to validate the medicinal-mushroom-complement track viability. Each SOP must specify operator-independent tolerances, not just "what reagents to use."

## Why this stub exists

The Phase 7 medicinal-mushroom-complement track positions Open Enzyme as a **reproducibility + characterization layer** on top of the existing supplement industry. Per Phase 7-1a finding: 93-100% of US "G. lucidum" supplements are species-mis-IDed. Per Phase 7-2 conclusion: cultivation + extraction protocol standardization is what Open Enzyme actually contributes — the chemistry is in the public domain.

A chemistry collaborator joining the project (one of the three actively-recruiting collaborator roles per CLAUDE.md / [`team.md`](./team.md)) should be able to find the SOP work registered here, not buried in a scope-page follow-up list.

## Planned SOPs

### SOP-1 — *Ganoderma lingzhi* GLPP Polysaccharide-Peptide Fractionation (load-bearing)

**Status:** Stub — gated on Phase 5b CNKI dive (Lin Zhanxi 林占熺 Juncao SOP + Lin Zhibin 林志彬 GLPP fractionation primary literature).

**Source material:** mycelium from ITS-verified *G. lingzhi* (Mycelia.bvba M9724 is the only commercially-verified ITS-authenticated strain per Phase 7-1a; Cao 2012 *Ganoderma*-specific primers G-ITS-F1/G-ITS-R2 at academic core facility, ~$20-40/sample, mandatory upstream gate).

**Planned method (extrapolated from English-language pharmacology papers — needs CNKI-sourced upstream protocol verification):**
1. Hot water extraction of dried mycelium (or freeze-dried fruiting body), 90°C, 2 hr, water:biomass = 10:1
2. Centrifugation + concentration of supernatant under vacuum
3. Ethanol precipitation (4 vol EtOH, 4°C overnight) → polysaccharide-peptide fraction
4. DEAE-Sepharose anion-exchange chromatography → fraction by charge profile
5. Sephacryl S-500 size-exclusion chromatography → MW-based separation
6. SEC-MALS verification of MW (target: determine which Lin-lab fraction the HUA mechanism load-bears on — 520 kDa is the bulk crude prep per sister paper PMC11351902; 31–42 kDa are post-DEAE sub-fractions per PMID 37852403 + 29541200; Lin 2022 HUA paper itself does not specify which fraction. Resolved 2026-05-06 grep-verify gate — see [`medicinal-mushroom-complement-track.md`](./medicinal-mushroom-complement-track.md) for full citation chain)
7. Amino acid analysis (peptide composition)
8. Glycan linkage NMR fingerprint

**Phase 5b prerequisite:** without the Lin Zhanxi Juncao cultivation SOP from CNKI, the upstream substrate is not Western-reproducible. SOP-1 cannot be drafted at usable detail before that dive lands. Phase 7-1a strain scan documents the specific search terms: `菌草 灵芝 栽培` (CNKI), `林占熺 灵芝` (CNKI author search).

**Reproducibility target (per H06 Dimension 2):** ±15% inter-operator on MW + peptide:polysaccharide ratio + glycan composition.

### SOP-2 — *Cordyceps militaris* Cordycepin + Pentostatin HPLC Quantification

**Source material:** *C. militaris* fruiting body or mycelium from cultivated source (top-yield strain GYS60 per Phase 7-1b, or commercial cultivation kit for home-cultivation track).

**Planned method (Wang 2014 with Xia 2017 cluster diagnostic ratio):**
1. Aqueous extraction of dried biomass, 80°C, 1 hr
2. C18 SPE cleanup
3. RP-HPLC, C18 column, water-methanol gradient
4. UV detection at 260 nm
5. Co-quantify: cordycepin (3'-deoxyadenosine), adenosine (precursor + ADA-deamination context), **pentostatin** (the natural ADA-inhibitor co-product per Xia 2017 PMID 29056419)
6. Pentostatin:cordycepin ratio is a diagnostic for whether the cordycepin BGC is fully expressed — this is the load-bearing readout for whole-fermentate-vs-purified cordycepin clinical positioning (per Phase 7-4 wet-lab gate)
7. Reference standard: cordycepin ≥98% HPLC purity (Sigma C9881 or equivalent); pentostatin reference standard is regulated (FDA-approved drug, restricted access — sourcing requires research-use license)

**Reproducibility target:** ±15% inter-operator on cordycepin mg/g; ±20% on pentostatin:cordycepin ratio (lower-abundance target).

### SOP-3 — *Pleurotus citrinopileatus* Ergothioneine HILIC-HPLC Quantification

**Source material:** dried fruiting body of *P. citrinopileatus* (golden oyster — highest fungal EGT producer at 7.0 mg/g DW per Phase 7-1c). Pasteurized-straw bag cultivation per Phase 7-2, freeze-dry to powder.

**Planned method (Cohen 2014 with HILIC modification for polar zwitterion):**
1. UA-DES (urea-based deep eutectic solvent) or aqueous methanol extraction
2. HILIC chromatography (suitable for polar zwitterionic EGT — reverse-phase fails for this analyte)
3. UV detection at 254 nm (or LC-MS for sensitivity)
4. Stable-isotope-labeled internal standard (²H₉-ergothioneine) for absolute quantification
5. Calibration: 0.1-10 mg/g range covers dietary-relevant content

**Reproducibility target:** ±15% inter-operator; consistent with the 7.0 mg/g DW Singapore RCT formulation reference (PMID 40552321 per Phase 7-1c).

### SOP-4 — Functional Verification Readouts

For each compound, a downstream functional readout that confirms bioactivity beyond chemical identification:

- **GLPP — ADA inhibition assay:** purified GLPP fraction + recombinant human ADA + adenosine substrate → measure 3'-deoxyinosine production decrease via HPLC. Target: dose-dependent inhibition with IC50 measurable.
- **Cordycepin — URAT1 expression assay:** HEK293 cells stably expressing human SLC22A12 (URAT1) + qPCR for URAT1 mRNA after 24h cordycepin treatment. Target: dose-dependent URAT1 mRNA reduction (matches in vivo finding from PMID 29422889).
- **Ergothioneine — Nrf2-ARE reporter assay:** HepG2 cells with stable ARE-luciferase reporter + EGT treatment → luciferase induction. Target: dose-dependent activation matching dietary-mushroom-derived EGT plasma range (~5-25 µM).

**Reproducibility target:** consistent dose-response shape across operators; absolute potency may vary 2× operator-to-operator on cell-based assays (typical for biological readouts).

### SOP-6 — Tiered methodology framework (added 2026-05-06)

The SOPs above (SOP-1 GLPP, SOP-2 cordycepin, SOP-3 EGT) are written at **Tier 3 (bench, publication-grade)** rigor. The koji enzyme quantification work has matured a four-tier framework — kitchen → smartphone → bench → outsourced — that **transfers cleanly to mushroom extract characterization**, giving any open-source contributor a rigor-graded path from "I made a tea, did anything happen?" up to "this is a quantified extract suitable for synergy-experiment use." Reuse pattern: calibrate once at Tier 3, then track downstream batches at Tier 1 / Tier 2 against the calibrated reference standard. This is the same "calibrate-once-track-batches-cheap" discipline that makes the koji track home-feasible.

**Source framework:** [`enzyme-quantification-protocol.md`](./enzyme-quantification-protocol.md). Tier definitions adapted from that document's structure.

| Compound | Tier 1 (kitchen, ~$0) | Tier 2 (smartphone colorimetry, ~$50) | Tier 3 (bench HPLC, ~$2K) | Tier 4 (outsourced regulatory) |
|---|---|---|---|---|
| **Cordycepin** | Visual + dosing-by-known-extract-ratio (calibrated against Tier 3 batch); not analytical, just consistency | **Speculative — needs literature verification.** Diazo-coupling chemistry typically targets phenolic/amine groups; cordycepin is a 3'-deoxyadenosine analog without those motifs. Pass 2's diazo proposal is plausible but unverified — do NOT commit until primary-literature confirmation of a validated colorimetric cordycepin assay at this sensitivity range. Alternative: borrow UV-vis at 260 nm (purine absorption) with known extract-ratio backing. | **SOP-2** above (HPLC, calibrated cordycepin standard from Sigma C3394) | Outsourced GMP-grade HPLC if regulatory submission ever needed |
| **Ergothioneine** | Visual + dosing-by-known-extract-ratio | **Ellman's reagent (DTNB) thiol detection**, smartphone colorimetry. Well-established chemistry (DTNB → 412 nm yellow on free thiol); EGT's free thiol is the substrate. Pharmacy-accessible reagent. Calibrate against a Tier 3 EGT-quantified batch to convert absorbance → mg/g. | **SOP-3** above (HILIC-HPLC with stable-isotope internal standard) | Outsourced GMP-grade HILIC-HPLC if regulatory ever needed |
| **GLPP** | Visual + extract weight + standardized decoction yield (mass-balance check, not compound-specific) | **Phenol-sulfuric acid total polysaccharide assay** (well-established colorimetric method, ~490 nm). **Caveat: measures total polysaccharide, not GLPP specifically.** Co-extracted *Ganoderma* polysaccharides + any residual decoction polysaccharides will be counted. Useful as a batch-to-batch consistency check ("this batch is in the same polysaccharide ballpark as the calibrated reference"), NOT as a GLPP-specific quantification. SOP-1's SEC-MALS at Tier 3 is non-negotiable for the protein:polysaccharide ratio per H06 Dimension 2 reproducibility discipline. | **SOP-1** above (SEC-MALS for MW + protein:polysaccharide ratio, with phenol-sulfuric and Bradford / Lowry as orthogonal anchors) | Outsourced GMP-grade SEC-MALS if regulatory ever needed |

**Operational pattern (the calibrate-once-track-batches workflow):**

1. **Initial Tier 3 calibration** — quantify a reference batch by SOP-1/2/3 above. Anchor numbers: mg/g extract for each target compound; document extract source, batch ID, lot, harvest details.
2. **Batch tracking at Tier 2** — for each new batch of extract from the same protocol, run the Tier 2 colorimetric assay against the reference batch as the standard curve anchor. If batch reads within ±20% of reference, accept. If outside, escalate to Tier 3 re-quantification.
3. **Field-grade Tier 1** — for end-user / kitchen-grade reproducibility, dosing follows the Tier 3-calibrated extract-ratio (e.g., "1 g of this batch ≈ 8 mg cordycepin per the SOP-2 quantification done on this lot"). Tier 1 is consumption-side, not characterization-side.
4. **Tier 4 outsourced** — only invoked if regulatory submission requires it. Adds GLP/GMP overhead but uses the same analytical chemistry as Tier 3.

**Why this matters operationally:** without the tiered framework, every batch would need full Tier 3 HPLC (cost-prohibitive at scale and impossible for distributed open-source contributors without HPLC access). With it, Tier 3 is invoked once per protocol revision; Tier 2 handles batch consistency cheaply; Tier 1 keeps end-user dosing tied to verified content. Same discipline that lets the koji track work as a home-fermentation project rather than a CRO-only project.

**Cross-reference to [§"Reality check — current consumer-grade fruiting-body extracts deliver sub-therapeutic cordycepin doses"](./medicinal-mushroom-complement-track.md):** the tiered framework is *also* the discipline that catches dose-vs-product-content mismatches like the Real Mushrooms Cordyceps-M case (3-4 mg cordycepin per 1 g serving at 0.4% content). A Tier 2 colorimetric check on a commercial extract would surface this mismatch before it became a "URAT1 layer" recommendation. Anyone evaluating a commercial mushroom extract for therapeutic-dose targeting should run the Tier 2 check (or insist on the manufacturer's published HPLC content) before downstream reasoning depends on the active-compound dose.

### SOP-5 — Strain Banking + ITS Authentication

**Cross-reference:** Phase 7-1a outlined the ITS-PCR authentication protocol (Cao 2012 *Ganoderma*-specific primers); applies to all medicinal mushroom strains used for Open Enzyme protocols.

**Planned method:**
1. ITS region amplification (ITS1-5.8S-ITS2)
2. Sanger sequencing
3. BLAST against NCBI nt database with species-level confidence threshold (≥98% identity for genus, ≥99.5% for species)
4. Deposit verified strain in -80°C glycerol stock with documented provenance
5. Re-verify ITS every 6 months or after 5 serial passages (whichever first)

**Reproducibility target:** binary — pass/fail on species ID; provenance fully documented per strain.

## Cross-references

- [`medicinal-mushroom-complement-track.md`](./medicinal-mushroom-complement-track.md) — the scope page these SOPs operationalize
- [`hypotheses/H06-medicinal-mushroom-complement-track.md`](./hypotheses/H06-medicinal-mushroom-complement-track.md) — H06 Dimension 2 (characterization protocol robustness) is the falsification mirror for these SOPs
- [`medicinal-mushroom-compound-mapping-computational.md`](./medicinal-mushroom-compound-mapping-computational.md) — comp-014, parent computational analysis
- [`validation-experiments.md`](./validation-experiments.md) §2.6 — GLPP+cordycepin synergy wet-lab gate (uses these SOPs as input materials)
- [`experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-7-cultivation-yield-meta-analysis.md`](../experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-7-cultivation-yield-meta-analysis.md) — Phase 7-2 source for cultivation upstream parameters
- [`experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-7a-ganoderma-strain-scan.md`](../experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-7a-ganoderma-strain-scan.md), [`phase-7b-cordyceps-strain-scan.md`](../experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-7b-cordyceps-strain-scan.md), [`phase-7c-pleurotus-strain-scan.md`](../experiments/comp-014-medicinal-mushroom-compound-mapping/outputs/phase-7c-pleurotus-strain-scan.md) — strain selection inputs

## Maintenance

- **When a chemistry collaborator joins:** SOP-1 GLPP work is the load-bearing first task; SOP-3 EGT is lowest-friction (well-characterized analyte); SOP-2 cordycepin requires pentostatin reference standard sourcing (regulated FDA-approved drug — handle as separate research-license task).
- **When Phase 5b CNKI dive lands:** SOP-1 GLPP fractionation gets its upstream Juncao cultivation protocol; promotes from stub to draft.
- **When self-experimentation reaches an SOP-relevant stage:** SOP-3 EGT and SOP-5 ITS authentication are the lowest-barrier-to-entry — Brian's *P. citrinopileatus* grow-kit self-experiment surfaces dietary-EGT data without needing chromatography access.
- **Track promotions:** stub → draft (when collaborator drafts protocol) → published (when ≥2 independent operators verify ±15% reproducibility per H06 Dimension 2).

---

**Status:** Stub committed 2026-05-06. Phase 7-3 follow-up #3 of `medicinal-mushroom-complement-track.md`.
