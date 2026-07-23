---
title: Quantification Ladder (kitchen → portable → bench → outsourced)
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
| **2. Portable / low-cost quantitative assay** | Tier 1 plus a phone photometer, portable electrochemical reader, or comparable accessible instrument and its required reagents. | Relative or semi-absolute concentration from an analyte- and matrix-specific calibration. | Batch tracking or distributed measurement after validation against a Tier 3 method. Smartphone colorimetry is the current common implementation, not the tier definition. |
| **3. Bench** | Calibrated spectrophotometer, HPLC or comparable, balance, pipettes, qualified analytical standards. Equipment ~$2K capital, ~$200–500 per run. | Publication-grade U/mL or mg/g with cited standards and a validated method. | Initial calibration per protocol revision; clinical / synergy-experiment-grade data; the ground truth that anchors every Tier 1 and Tier 2 reading. |
| **4. Outsourced** | Contract lab (GMP / GLP tier). ~$300–1,500 per sample. | Audit-trail-grade certified analysis. | One-time benchmarking before committing to in-house Tier 3; independent verification of a surprising Tier 3 result; regulatory submission. |

## The operational pattern: calibrate once, track batches cheap

1. **Initial Tier 3 calibration.** Quantify a reference batch by the protocol's validated bench method. Anchor numbers (e.g., mg cordycepin / g extract; U lipase / g koji). Document extract source, batch ID, lot, and harvest conditions.
2. **Batch tracking at Tier 1 or Tier 2.** For each new batch from the same protocol, run a cheap assay against the reference batch as the standard curve anchor. If the batch reads within ±20% of reference, accept. If outside, escalate to Tier 3 re-quantification or investigate the deviation.
3. **Experimental sample mass follows the calibrated ratio.** Record the lot-specific relationship between material mass and measured compound or activity. This is an experimental input, not a human dose recommendation.
4. **Tier 4 only on demand.** Use it when an audit trail, regulatory-grade result, or independent verification is required.

Tier 1 and Tier 2 are optional conveniences, not required links. If no lower-tier method has been validated for the exact analyte, matrix, and decision, measure at Tier 3 directly. Do not substitute a different analyte or matrix merely to preserve a cheap-tracking step.

## Why this matters operationally

Tier 3 establishes the reference value; Tier 2 tracks routine batch variation; Tier 1 provides categorical process control. The ladder reduces routine assay cost without pretending that visual or phone-based measurements are equivalent to instrumented analysis.

The ladder also catches a specific class of failure: dose-vs-product-content mismatches. If a commercial extract is marketed at one content level but a Tier 2 colorimetric check shows another, the discrepancy surfaces before downstream therapeutic-dose reasoning depends on the marketed number. See [`medicinal-mushroom-complement-track.md`](./medicinal-mushroom-complement-track.md) §"Reality check" for the Real Mushrooms Cordyceps-M case (3–4 mg cordycepin per 1 g serving at 0.4% content, surfaced by tier-discipline thinking).

**Optional low-cost automation.** Operator variation in serial dilution, mixing, transfer order, and image timing can dominate assay variance. [Picolab v2](https://github.com/OmkarKovvali/picolab_v2) provides engineering prior art for tube-scale automation using a printer gantry, syringe actuation, G-code planning, camera snapshots, and operator-approved actions. Validate any adaptation first with benign dye and standard-curve work; this is method infrastructure, not evidence that a biological assay is validated.

## Instantiations

- **Koji digestive enzyme quantification.** [`enzyme-quantification-protocol.md`](./enzyme-quantification-protocol.md). Lipase (olive-oil titration → p-NPP smartphone → spectrophotometer p-NPP or pH-stat → outsourced HUT or USP units). Amylase (starch-iodine clearance → DNS reducing-sugar smartphone → bench DNS or Bernfeld → outsourced). Protease (gelatin liquefaction or skim-milk plate → ninhydrin or azocasein smartphone → bench azocasein or pH-stat → outsourced).
- **Medicinal mushroom extract characterization.** [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) §SOP-6. Cordycepin (visual dosing-by-ratio → speculative diazo Tier 2 pending verification, UV 260 nm fallback → HPLC SOP-2 → outsourced GMP-HPLC). EGT (visual → DTNB Ellman's thiol smartphone → HILIC-HPLC SOP-3 → outsourced). GLPP (visual + mass-balance → phenol-sulfuric total-polysaccharide smartphone → SEC-MALS SOP-1 → outsourced).
- **Microbiome-derived butyrate / SCFA quantification.** [`tier-2-butyrate-assay-audit-computational.md`](./tier-2-butyrate-assay-audit-computational.md) (comp-038) found no ready-to-adopt Tier 1 or Tier 2 butyrate method for current OE use. HPLC-UV is a **Tier 3 bench method**, not Tier 2; De Baere et al. validated it for bacterial culture supernatants, and [validation §1.31](./validation-experiments.md#131-butyrate-culture-supernatant-hplc-uv-method-transfer-against-gc-ms) tests transfer into an exact OE culture matrix. GC-MS is a Tier 3 comparator when run in-house and Tier 4 when outsourced. Gu et al.'s electrochemical/ANN method is a separate stool-specific Tier 2 candidate whose complete hardware–chemistry–model transfer is staged in [validation §1.45](./validation-experiments.md#145-fecal-butyrate-electrochemicalann-reproducibility-and-transfer-gate).

  **Class-level measurement gap.** Butyrate does not stand in for all microbiome-derived metabolites. Propionate, acetate, secondary bile acids, microbial indoles, and TMAO each require analyte- and matrix-specific validation. Measuring a production input, precursor, culture supernatant, or stool concentration does not establish target-compartment exposure. PMID 23542733 supports the culture-supernatant HPLC-UV method; PMID 42041444 supports a GC-MS-compared electrochemical/ANN method in stool. Neither result transfers automatically to another metabolite or matrix.
- **Future tracks.** TCM compound triage (per [`tcm-modern-rigor-intersection.md`](./tcm-modern-rigor-intersection.md)) and siRNA / URAT1 modality (per [`sirna-urat1-modality.md`](./sirna-urat1-modality.md)) inherit the framework as new compound classes are added.

## Discipline notes

- **Keep one tier definition.** Tier-specific assay details live in the method pages; do not redefine the ladder within each assay.
- **Tier 3 is the calibration anchor for the others.** Every Tier 1 and Tier 2 reading needs to translate back to an absolute number, and the only way to get there is through a Tier 3 standard curve. Skipping Tier 3 ("we'll just do Tier 1 forever") collapses inter-sample ratios into vibes.
- **Do not force a lower tier.** If the only defensible method is Tier 3, use Tier 3. Relative affordability does not turn HPLC, GC-MS, or another bench analytical method into Tier 2.
- **Tier 4 is not a default escalation.** Outsourced assay is for one-time benchmarking or regulatory submission, not routine analysis. The 10× cost gap from Tier 3 to Tier 4 is not value-additive unless you specifically need the audit trail or the GMP chain of custody.
- **The framework is operational quality, not novelty.** Adopting it does not require any new science. It requires the discipline to run the calibration step once, log the reference numbers somewhere persistent, and trust the cheap-tier readings against that anchor.

## See also

- **[`genotype-informed-supplement-workflow.md`](./genotype-informed-supplement-workflow.md)**: genotype-stratified intervention research workflow using batch QC and exposure measurement.
- [`enzyme-quantification-protocol.md`](./enzyme-quantification-protocol.md): digestive-enzyme assays for lipase, amylase, and protease.
- [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) §SOP-6: second instantiation; cordycepin, EGT, GLPP.
- [`open-source-platform.md`](./etc/open-source-platform.md): platform-level quality methodologies; this ladder is one of them.
