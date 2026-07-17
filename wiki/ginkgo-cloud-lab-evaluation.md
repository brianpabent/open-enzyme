---
title: "Ginkgo Cloud Lab — Wet-Lab Partner Evaluation"
date: 2026-05-13
tags: [wet-lab, partners, cloud-lab, cell-free-expression, strain-engineering, Ginkgo-Bioworks]
related:
  - engineered-koji-protocol.md
  - engineered-yeast-uricase-proposal.md
  - uricase-variant-selection.md
  - daf-cd55-scr14-truncated-computational.md
  - validation-experiments.md
  - etc/ai-bio-tools-playbook.md
sources:
  - "EstiMate (Ginkgo Bioworks Cloud Lab compatibility and pricing assistant), vendor chat 2026-05-12"
status: evaluated-deferred
---

# Ginkgo Cloud Lab — Wet-Lab Partner Evaluation

Ginkgo's EstiMate assistant described two relevant offers: cell-free protein-expression validation at **$39/protein** for sequences up to 1,800 bp with an estimated 5–10-day turnaround, and a 96-construct *S. cerevisiae* engineering campaign at approximately **$2,340 total ($24.38/sample)**. These are informal vendor estimates, not formal quotations.

## Decision

**Defer both offers.** The cell-free service answers a narrow translation/solubility question and should be used only if that becomes the next experimental gate. The 96-construct campaign price is not credible enough for budgeting without a formal scope and quotation.

## Claimed capabilities

| Step | Instrument class described | Claimed support |
|---|---|---|
| DNA assembly | Liquid handler / thermal cycler | Echo 525 / Thermo ATC |
| Transformation | Plate shaker / incubator | Bioshake 3000-T / Cytomat |
| Strain selection | Fluorescence / absorbance plate reader | Pherastar / Tecan Spark |
| Uricase activity | Kinetic absorbance plate reader | BMG Pherastar |
| Protein analysis | Capillary electrophoresis | AATI Fragment Analyzer |
| Metabolites | LC-MS or GC-MS | Thermo QE Plus / Sciex Echo MS |

EstiMate described *S. cerevisiae* as supported for automated transformation and screening. It also described *A. oryzae* as supportable in deep-well formats, with morphology complicating liquid handling and optical-density measurements. The Cloud Lab offer is plate-screening oriented; Ambr 250 or other bioreactor work is a separate service.

## What cell-free expression can establish

A low-cost cell-free run would most plausibly use an *E. coli*-derived lysate, although the vendor did not identify the system. It can test whether an ORF translates and whether detectable soluble polypeptide is produced in that lysate. Unless explicitly included, it does not establish enzymatic activity.

It does not establish:

- folding in a fungal host;
- glycosylation or GPI anchoring;
- secretion or signal-peptide processing;
- behavior in fermentation;
- physiological substrate, oxygen, pH, transit, topology, or peroxide handling.

The lysate type, raw-data product, activity-assay scope, and sequence/data ownership therefore need confirmation before purchase.

## Construct fit

| Construct | Fit | Interpretation |
|---|---|---|
| **Uricase variants** | Strong for a translation/solubility pre-gate | Fungal uricase is non-glycosylated and routinely expressed in bacterial systems. A urate A293 activity assay would add much more information than expression alone. A positive result still would not validate fungal secretion or gut-luminal performance. |
| **Digestive enzymes** | Potentially useful | Expression may be tractable, but each enzyme needs an activity-specific assay and lysate-background control. |
| **DAF/CD55 SCR1-4** | Weak | CD55 SCR1-4 has eight annotated disulfide bonds across four SCR domains (UniProt P08174) and native glycosylation. A default reducing bacterial lysate cannot reproduce the relevant secretory folding environment, glycans, or GPI anchor. |

For CD55, a negative result could reflect the assay environment rather than the construct; a positive expression result would not establish functional folding. A eukaryotic secretory-expression system is the appropriate gate.

## Pricing interpretation

The assistant itemized the 96-construct campaign as approximately $1,150 consumables, $840 instrument time, and $350 QC/data delivery. That price may be promotional, incomplete, or generated from a template that excludes DNA construction, labor, genotyping, or assay development. It should not enter an experiment budget until Ginkgo provides a written statement of work.

The $39 cell-free offer is more plausible as a productized SKU, but its utility depends on what confirmation is included. Expression-only data have low incremental value when the dominant risks are secretion, physiological regime, or functional activity.

## Relationship to fungal-host validation

Cell-free expression and fungal-host validation answer different questions:

| Gate | Suitable route |
|---|---|
| Does the ORF produce soluble polypeptide in the specified lysate? | Cell-free expression |
| Is the protein active in a defined biochemical assay? | Cell-free plus activity assay or purified-protein assay |
| Is it folded, secreted, and active from the intended fungal host? | Host-specific expression and fermentation |
| Does it function under intended luminal conditions? | Physiological-regime validation |

A cell-free run should precede fungal work only when ORF translation or soluble folding is itself uncertain enough to change the construct decision.

## Information required for reconsideration

- Lysate identity: S30, PURE, or eukaryotic; redox and chaperone conditions.
- Whether expression confirmation means soluble fraction, total protein, or functional protein.
- Whether uricase activity is included and whether raw kinetic traces are delivered.
- DNA synthesis, construct assembly, genotyping, and assay-development inclusions.
- Data and sequence ownership terms.
- Formal strain-engineering price for a small, precisely scoped variant panel.
- Academic or open-source pricing terms.

## Evidence level

- **Vendor statement:** prices, turnaround, instruments, and host support; unverified without a formal quotation.
- **Mechanistic Extrapolation:** construct-fit and assay-interpretation analysis based on the biology of bacterial cell-free systems and the named proteins.

No clinical, animal, or project-specific in-vitro result is reported here.

## Related

- [AI/bio tools playbook](./etc/ai-bio-tools-playbook.md)
- [Validation experiments](./validation-experiments.md)
- [Uricase variant selection](./uricase-variant-selection.md)
- [DAF/CD55 SCR1-4 computational assessment](./daf-cd55-scr14-truncated-computational.md)
