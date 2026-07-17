---
title: Quantification Ladder (kitchen → smartphone → bench → outsourced)
date: 2026-05-14
tags: [methodology, quality, open-source, distributed-rigor, sop, infrastructure]
related:
  - enzyme-quantification-protocol.md
  - medicinal-mushroom-extract-sops.md
  - etc/open-source-platform.md
  - etc/practitioner-toolkit.md
---

# Quantification Ladder

A four-tier framework for measuring compound or enzyme content. Use the lowest tier that satisfies the decision, anchored to a higher-rigor calibration for each protocol and material class.

Track-specific pages define assay chemistry, standards, sample preparation, and calibration anchors.

## The four tiers

| Tier | Equipment ceiling | Output type | Use case |
|---|---|---|---|
| **1. Kitchen** | Hand tools, eyes, kitchen scale, basic reagents (vinegar, milk, starch, gelatin). Marginal cost ~$0. | Visual or categorical readings; inter-sample ratios at fixed conditions. Not absolute units. | Batch-to-batch consistency check; "did this batch ferment to a normal load?"; end-user dosing tied to a Tier 3-calibrated extract ratio. |
| **2. Smartphone colorimetry** | Tier 1 plus a phone photometer rig (3D-printed cuvette holder or a DIY box with a fixed light source) plus a small reagent kit (DNS, ninhydrin, p-NPP, DTNB, phenol-sulfuric, etc.; ~$50–80 in single-experiment quantities). | A405 / A440 / A540 readings translated to relative concentration; with proper standard curves, semi-absolute units. | Batch tracking against a calibrated reference; mid-rigor surveillance for distributed contributors without lab access. |
| **3. Bench** | Calibrated spectrophotometer, HPLC or comparable, balance, pipettes, qualified analytical standards. Equipment ~$2K capital, ~$200–500 per run. | Publication-grade U/mL or mg/g with cited standards and a validated method. | Initial calibration per protocol revision; clinical / synergy-experiment-grade data; the ground truth that anchors every Tier 1 and Tier 2 reading. |
| **4. Outsourced** | Contract lab (GMP / GLP tier). ~$300–1,500 per sample. | Audit-trail-grade certified analysis. | One-time benchmarking before committing to in-house Tier 3; independent verification of a surprising Tier 3 result; regulatory submission. |

## The operational pattern: calibrate once, track batches cheap

1. **Initial Tier 3 calibration.** Quantify a reference batch by the protocol's validated bench method. Anchor numbers (e.g., mg cordycepin / g extract; U lipase / g koji). Document extract source, batch ID, lot, and harvest conditions.
2. **Batch tracking at Tier 1 or Tier 2.** For each new batch from the same protocol, run a cheap assay against the reference batch as the standard curve anchor. If the batch reads within ±20% of reference, accept. If outside, escalate to Tier 3 re-quantification or investigate the deviation.
3. **Experimental sample mass follows the calibrated ratio.** Record the lot-specific relationship between material mass and measured compound or activity. This is an experimental input, not a human dose recommendation.
4. **Tier 4 only on demand.** Use it when an audit trail, regulatory-grade result, or independent verification is required.

## Why this matters operationally

Tier 3 establishes the reference value; Tier 2 tracks routine batch variation; Tier 1 provides categorical process control. The ladder reduces routine assay cost without pretending that visual or phone-based measurements are equivalent to instrumented analysis.

The ladder also catches a specific class of failure: dose-vs-product-content mismatches. If a commercial extract is marketed at one content level but a Tier 2 colorimetric check shows another, the discrepancy surfaces before downstream therapeutic-dose reasoning depends on the marketed number. See [`medicinal-mushroom-complement-track.md`](./medicinal-mushroom-complement-track.md) §"Reality check" for the Real Mushrooms Cordyceps-M case (3–4 mg cordycepin per 1 g serving at 0.4% content, surfaced by tier-discipline thinking).

**Optional low-cost automation.** Operator variation in serial dilution, mixing, transfer order, and image timing can dominate assay variance. [Picolab v2](https://github.com/OmkarKovvali/picolab_v2) provides engineering prior art for tube-scale automation using a printer gantry, syringe actuation, G-code planning, camera snapshots, and operator-approved actions. Validate any adaptation first with benign dye and standard-curve work; this is method infrastructure, not evidence that a biological assay is validated.

## Instantiations

- **Koji digestive enzyme quantification.** [`enzyme-quantification-protocol.md`](./enzyme-quantification-protocol.md). Lipase (olive-oil titration → p-NPP smartphone → spectrophotometer p-NPP or pH-stat → outsourced HUT or USP units). Amylase (starch-iodine clearance → DNS reducing-sugar smartphone → bench DNS or Bernfeld → outsourced). Protease (gelatin liquefaction or skim-milk plate → ninhydrin or azocasein smartphone → bench azocasein or pH-stat → outsourced).
- **Medicinal mushroom extract characterization.** [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) §SOP-6. Cordycepin (visual dosing-by-ratio → speculative diazo Tier 2 pending verification, UV 260 nm fallback → HPLC SOP-2 → outsourced GMP-HPLC). EGT (visual → DTNB Ellman's thiol smartphone → HILIC-HPLC SOP-3 → outsourced). GLPP (visual + mass-balance → phenol-sulfuric total-polysaccharide smartphone → SEC-MALS SOP-1 → outsourced).
- **Microbiome-derived butyrate / SCFA quantification.** [`tier-2-butyrate-assay-audit-computational.md`](./tier-2-butyrate-assay-audit-computational.md) (comp-038) found no ready-to-adopt home/colorimetric butyrate Tier 2 assay. Current path: GC-MS remains the Tier 3 anchor; HPLC-UV is a plausible Tier 2-lab candidate for culture supernatants after spike-recovery + GC-MS validation; electrochemical fecal SCFA profiling is a promising stool-specific future direction, not production-ready.

  **Class-level measurement gap.** The lack of Tier 2 assays extends to other *in situ* microbiome metabolites: propionate and acetate generally retain GC-MS as the Tier 3 anchor; secondary bile acids, microbial indoles, and TMAO generally require LC-MS/MS. Measuring a precursor does not establish that the downstream metabolite reached the target tissue at the intended concentration. For butyrate, PMID 23542733 supports HPLC-UV in culture supernatant and PMID 42041444 reports a GC-MS-validated electrochemical/ANN approach for stool (n=30); paired spike-recovery against GC-MS remains the wet-lab gate ([validation experiment §1.31](./validation-experiments.md)). See the [class-level Tier 2 assay question](./open-questions.md).
- **Future tracks.** TCM compound triage (per [`tcm-modern-rigor-intersection.md`](./tcm-modern-rigor-intersection.md)) and siRNA / URAT1 modality (per [`sirna-urat1-modality.md`](./sirna-urat1-modality.md)) inherit the framework as new compound classes are added.

## Discipline notes

- **Keep one tier definition.** Tier-specific assay details live in the method pages; do not redefine the ladder within each assay.
- **Tier 3 is the calibration anchor for the others.** Every Tier 1 and Tier 2 reading needs to translate back to an absolute number, and the only way to get there is through a Tier 3 standard curve. Skipping Tier 3 ("we'll just do Tier 1 forever") collapses inter-sample ratios into vibes.
- **Tier 4 is not a default escalation.** Outsourced assay is for one-time benchmarking or regulatory submission, not routine analysis. The 10× cost gap from Tier 3 to Tier 4 is not value-additive unless you specifically need the audit trail or the GMP chain of custody.
- **The framework is operational quality, not novelty.** Adopting it does not require any new science. It requires the discipline to run the calibration step once, log the reference numbers somewhere persistent, and trust the cheap-tier readings against that anchor.

## See also

- **[`genotype-informed-supplement-workflow.md`](./genotype-informed-supplement-workflow.md)**: genotype-stratified intervention research workflow using batch QC and exposure measurement.
- [`enzyme-quantification-protocol.md`](./enzyme-quantification-protocol.md): digestive-enzyme assays for lipase, amylase, and protease.
- [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) §SOP-6: second instantiation; cordycepin, EGT, GLPP.
- [`open-source-platform.md`](./etc/open-source-platform.md): platform-level quality methodologies; this ladder is one of them.
