---
id: H08
title: "Can a gut-lumen uricase sink produce clinically meaningful serum-urate reduction under physiological substrate, oxygen, and transit constraints?"
committed: 2026-05-15
updated: 2026-07-13
status: Reopened
survival_count: 0
tags: [hypothesis, core-thesis, gut-lumen-sink, uricase, abcg2, clinical-translation, riskiest-assumption]
related:
  - ../gut-lumen-sink.md
  - ../uricase.md
  - ../gut-lumen-uricase-physiologic-regime-computational.md
  - ../uricase-topology-oxygen-peroxide-design-computational.md
  - ../validation-experiments.md
  - ../open-questions.md
  - ./README.md
sources:
  - "Miyazaki et al. 2025 — PMID 40033341; direct human jejunal urate measurement"
  - "Gao et al. 2025 — PMID 41038159; PULSE animal-model precedent"
  - "Zhao et al. 2022 — PMID 35491895; EcN UOX oxygen-recycling precedent"
  - "comp-044 — physiological-regime audit, 2026-07-13"
  - "comp-045 — topology × oxygen × peroxide design, 2026-07-13"
---

# H08 — Gut-Lumen Sink Platform Thesis

> **2026-07-13 correction:** the original H08 magnitude claim—−0.5 to −1.0 mg/dL at 25 mg/day, based on comp-019—is retracted as a quantitative prior. comp-019 stored luminal urate and UOX Km inputs but did not use them; it also granted 24 hours of saturated activity. [comp-044](../gut-lumen-uricase-physiologic-regime-computational.md) shows that the flat-dose regime is not robust. The biological hypothesis remains open.

## Claim

An intestinal UOX system can lower systemic urate if it removes a meaningful fraction of ABCG2-delivered luminal urate under the substrate concentration, oxygen, transit, localization, and reabsorption conditions that actually exist at the reaction site.

This is deliberately not a numeric ΔSUA claim. A defensible magnitude requires local dynamic measurements and human translation that the current corpus does not have.

## Current evidence

1. **Clinical human physiology:** ABCG2 contributes to intestinal urate transport, and direct human jejunal measurements show sub-micromolar baseline luminal urate in the sampled setting (Miyazaki 2025). This supports the route but creates a substrate-occupancy constraint.
2. **Animal models:** PULSE lowered urate in hyperuricemic mice/rats using a 1:1:1 mixture of intracellular, secreted, and displayed smUOX topologies with KatG+VHb support (Gao 2025). Zhao 2022 independently demonstrated an EcN PucLM+YgfU+KatG+VHb architecture under restricted oxygen. **Evidence level: Animal Model + In Vitro.**
3. **Computational audit:** comp-044 finds that the original regime classification changes when substrate occupancy and a finite active window are applied. It does not predict efficacy.
4. **Topology uncertainty:** comp-045 finds that no topology can yet be eliminated; the decisive comparison must measure urate, product, oxygen, peroxide, viability, and localization together.

## Retracted quantitative prior

The following historical comp-019 outputs are no longer active evidence:

- predicted genotype-specific ΔSUA values;
- the −0.5 to −1.0 mg/dL effect band;
- capacity ratios 32–1,300× as evidence of physiological saturation;
- “flat above 5 mg/day”;
- “yield optimization no longer matters”;
- a single 25 mg/day dose as the preferred validation design.

They remain visible in the frozen comp-019 artifact for revision history, but downstream decisions must cite comp-044 instead.

## Updated assumption stack

1. The reaction site receives enough urate for the chosen UOX Km and dose.
2. The reaction site supplies enough oxygen for sustained oxidative turnover.
3. UOX and peroxide control occupy compatible compartments, or indirect peroxide handling is empirically sufficient.
4. Active UOX persists for enough of the local transit window.
5. Removing luminal urate increases net elimination rather than being offset by reabsorption, renal compensation, or reduced transporter supply.
6. The effect survives translation from rodent hyperuricemia models to typical human gout.
7. Luminal urate removal does not create a barrier/oxidative liability larger than the urate-lowering benefit.

## Ranked killshots

| Rank | Killshot | Assumptions tested | Status |
|---:|---|---|---|
| 1 | Physiological topology × oxygen × peroxide factorial at 0.59/50/250 µM urate | 1–4, 7 | [Designed in §1.33](../validation-experiments.md#133-physiological-uox-topology--oxygen--peroxide-factorial) |
| 2 | Dynamic compartmental model using measured local urate replenishment, O2, decay, residence, and reabsorption | 1–5 | Awaiting §1.33 measurements |
| 3 | Human enteroid UOX redox/barrier assay ±NSAID context | 7 | [Designed in §1.36](../validation-experiments.md#136-luminal-urate-antioxidant-loss--uox-h2o2-safety-assay) |
| 4 | Human or human-relevant in-vivo local urate/product measurement with active UOX | 1–5 | Not started |
| 5 | Controlled human efficacy study with local-mechanism biomarkers and genotype recorded | 5–6 | Downstream only |

## Pre-committed interpretation

- **Mechanism strengthened:** reproducible UOX product formation at the human-baseline substrate prior under physiological oxygen, with controlled peroxide and viable epithelium, followed by increased net transepithelial elimination in a dynamic model or human-relevant system.
- **Mechanism narrowed:** activity appears only at the 250 µM benchmark or only under oxic conditions; the platform becomes meal/inflammation- or niche-dependent rather than a continuous baseline sink.
- **Current topology killed:** no measurable product at physiological substrate/oxygen despite confirmed expression and localization, or unacceptable peroxide/barrier injury relative to inactive-UOX controls.
- **Platform thesis killed:** a controlled human study with verified local UOX activity and adequate exposure shows no meaningful change in whole-body urate handling.

No mg/dL boundary is pre-committed until the dynamic local model is rebuilt from measured inputs.

## Status

**Reopened.** The original numeric prior did not survive audit. No biological killshot has yet been executed.

**Survival count:** 0.

## Open follow-ups

| ID | Item | Status |
|---|---|---|
| H08-1 | comp-044 physiological-regime audit | Complete 2026-07-13 |
| H08-2 | comp-045 factorial design | Complete 2026-07-13 |
| H08-3 | Run validation §1.33 | Proposed |
| H08-4 | Run validation §1.36 | Proposed |
| H08-5 | Rebuild dynamic compartmental model from measured §1.33 inputs | Blocked on data, not started |
| H08-6 | Reassess clinical-study design only after H08-3/H08-5 | Deferred |

## Cross-references

- [Gut-lumen sink](../gut-lumen-sink.md)
- [comp-044 interpretive page](../gut-lumen-uricase-physiologic-regime-computational.md)
- [comp-045 interpretive page](../uricase-topology-oxygen-peroxide-design-computational.md)
- [Validation experiments](../validation-experiments.md)
- [Superseded comp-019 page](../uricase-abcg2-genotype-stratification-computational.md)
