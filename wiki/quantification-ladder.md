---
title: Quantification Ladder (kitchen → smartphone → bench → outsourced)
date: 2026-05-14
tags: [methodology, quality, open-source, distributed-rigor, sop, infrastructure]
related:
  - enzyme-quantification-protocol.md
  - medicinal-mushroom-extract-sops.md
  - open-source-platform.md
---

# Quantification Ladder

A four-tier framework for measuring compound or enzyme content in Open Enzyme outputs (engineered koji, medicinal mushroom extracts, future TCM and siRNA tracks). The ladder lets a distributed open-source contributor work at the lowest rigor tier their use case tolerates, while staying anchored to a higher-rigor calibration done once per protocol revision.

This page is the **canonical definition** of the framework. Track-specific instantiations (assay chemistry, target compounds, calibration anchors) live in their own protocol pages and reference this one.

## The four tiers

| Tier | Equipment ceiling | Output type | Use case |
|---|---|---|---|
| **1. Kitchen** | Hand tools, eyes, kitchen scale, basic reagents (vinegar, milk, starch, gelatin). Marginal cost ~$0. | Visual or categorical readings; inter-sample ratios at fixed conditions. Not absolute units. | Batch-to-batch consistency check; "did this batch ferment to a normal load?"; end-user dosing tied to a Tier 3-calibrated extract ratio. |
| **2. Smartphone colorimetry** | Tier 1 plus a phone photometer rig (3D-printed cuvette holder or a DIY box with a fixed light source) plus a small reagent kit (DNS, ninhydrin, p-NPP, DTNB, phenol-sulfuric, etc.; ~$50–80 in single-experiment quantities). | A405 / A440 / A540 readings translated to relative concentration; with proper standard curves, semi-absolute units. | Batch tracking against a calibrated reference; mid-rigor surveillance for distributed contributors without lab access. |
| **3. Bench** | Calibrated spectrophotometer, HPLC or comparable, balance, pipettes, qualified analytical standards. Equipment ~$2K capital, ~$200–500 per run. | Publication-grade U/mL or mg/g with cited standards and a validated method. | Initial calibration per protocol revision; clinical / synergy-experiment-grade data; the ground truth that anchors every Tier 1 and Tier 2 reading. |
| **4. Outsourced** | Contract lab (GMP / GLP tier). ~$300–1,500 per sample. | Audit-trail-grade certified analysis. | One-time benchmarking before committing to in-house Tier 3; independent verification of a surprising Tier 3 result; regulatory submission. |

## The operational pattern: calibrate once, track batches cheap

1. **Initial Tier 3 calibration.** Quantify a reference batch by the protocol's canonical bench method. Anchor numbers (e.g., mg cordycepin / g extract; U lipase / g koji). Document extract source, batch ID, lot, harvest conditions.
2. **Batch tracking at Tier 1 or Tier 2.** For each new batch from the same protocol, run a cheap assay against the reference batch as the standard curve anchor. If the batch reads within ±20% of reference, accept. If outside, escalate to Tier 3 re-quantification or investigate the deviation.
3. **End-user dosing follows the Tier 3-calibrated ratio.** "1 g of this batch ≈ 8 mg cordycepin per the SOP done on this lot." Tier 1 at the consumption side, not the characterization side.
4. **Tier 4 only on demand.** Invoked when regulatory submission requires it, or when in-house Tier 3 produces a result surprising enough to want independent verification before publishing or acting clinically.

## Why this matters operationally

Without the tiered framework, every batch would need a full Tier 3 instrumented assay. That is cost-prohibitive at scale and impossible for distributed open-source contributors without lab access. With it, Tier 3 is invoked once per protocol revision; Tier 2 handles batch consistency cheaply; Tier 1 keeps end-user dosing tied to verified content. This is the same discipline that lets the koji track work as a home-fermentation project rather than a CRO-only project, and that lets the medicinal mushroom track ship characterized compounds without an HPLC in every contributor's basement.

The ladder also catches a specific class of failure: dose-vs-product-content mismatches. If a commercial extract is marketed at one content level but a Tier 2 colorimetric check shows another, the discrepancy surfaces before downstream therapeutic-dose reasoning depends on the marketed number. See [`medicinal-mushroom-complement-track.md`](./medicinal-mushroom-complement-track.md) §"Reality check" for the Real Mushrooms Cordyceps-M case (3–4 mg cordycepin per 1 g serving at 0.4% content, surfaced by tier-discipline thinking).

## Instantiations

- **Koji digestive enzyme quantification.** [`enzyme-quantification-protocol.md`](./enzyme-quantification-protocol.md). Lipase (olive-oil titration → p-NPP smartphone → spectrophotometer p-NPP or pH-stat → outsourced HUT or USP units). Amylase (starch-iodine clearance → DNS reducing-sugar smartphone → bench DNS or Bernfeld → outsourced). Protease (gelatin liquefaction or skim-milk plate → ninhydrin or azocasein smartphone → bench azocasein or pH-stat → outsourced).
- **Medicinal mushroom extract characterization.** [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) §SOP-6. Cordycepin (visual dosing-by-ratio → speculative diazo Tier 2 pending verification, UV 260 nm fallback → HPLC SOP-2 → outsourced GMP-HPLC). EGT (visual → DTNB Ellman's thiol smartphone → HILIC-HPLC SOP-3 → outsourced). GLPP (visual + mass-balance → phenol-sulfuric total-polysaccharide smartphone → SEC-MALS SOP-1 → outsourced).
- **Future tracks.** TCM compound triage (per [`tcm-modern-rigor-intersection.md`](./tcm-modern-rigor-intersection.md)) and siRNA / URAT1 modality (per [`sirna-urat1-modality.md`](./sirna-urat1-modality.md)) inherit the framework as new compound classes are added.

## Discipline notes

- **Single source of truth for tier definitions.** This page. Tier-specific assay details live in the instantiation pages; the abstract framework definition stays here. Reason: two parallel definitions diverge over time. The 2026-05-14 walkthrough caught the early drift between `enzyme-quantification-protocol.md` and `medicinal-mushroom-extract-sops.md` SOP-6 and consolidated them here.
- **Tier 3 is the calibration anchor for the others.** Every Tier 1 and Tier 2 reading needs to translate back to an absolute number, and the only way to get there is through a Tier 3 standard curve. Skipping Tier 3 ("we'll just do Tier 1 forever") collapses inter-sample ratios into vibes.
- **Tier 4 is not a default escalation.** Outsourced assay is for one-time benchmarking or regulatory submission, not routine analysis. The 10× cost gap from Tier 3 to Tier 4 is not value-additive unless you specifically need the audit trail or the GMP chain of custody.
- **The framework is operational quality, not novelty.** Adopting it does not require any new science. It requires the discipline to run the calibration step once, log the reference numbers somewhere persistent, and trust the cheap-tier readings against that anchor.

## See also

- **[`genotype-informed-supplement-workflow.md`](./genotype-informed-supplement-workflow.md)**: closed-loop n=1 pharmacogenomics workflow that composes this ladder (steps 3–4: Tier 2 batch QC + calibrated dose) with genotype-informed compound selection and biomarker tracking. The user-facing entry point that walks the whole pipeline end-to-end.
- [`enzyme-quantification-protocol.md`](./enzyme-quantification-protocol.md): canonical first instantiation; koji digestive enzymes (lipase, amylase, protease).
- [`medicinal-mushroom-extract-sops.md`](./medicinal-mushroom-extract-sops.md) §SOP-6: second instantiation; cordycepin, EGT, GLPP.
- [`open-source-platform.md`](./open-source-platform.md): platform-level quality methodologies; this ladder is one of them.
