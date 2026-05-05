---
id: H04
title: "Modern scientific rigor (chokepoint-mapping + ChEMBL cross-check + bioavailability honesty + falsification card discipline) applied to TCM materia medica produces actionable, gout-relevant findings beyond what reductionist single-compound analysis or holistic 'alternative medicine' framings produce in isolation"
committed: 2026-05-05
status: Stub
survival_count: 0
tags:
  - hypothesis
  - tcm
  - methodology-lens
  - chokepoint-mapping
  - chembl-cross-check
  - empirical-prior
  - discovery-engine
  - global-multilingual
related:
  - ../tcm-modern-rigor-intersection.md
  - ../modality-chokepoint-matrix.md
  - ../chembl-cross-check.md
  - ../engineered-lbp-chassis.md
  - ../sirna-urat1-modality.md
  - ../open-enzyme-vision.md
  - ../open-questions.md
  - ./H01-ward-dual-cassette.md
  - ./H02-engineered-lbp-thesis.md
  - ./H03-sirna-urat1-thesis.md
  - ./README.md
sources:
  - "Si Miao San / Si Miao Wan family — modern Chinese RCT meta-analyses (ChiCTR registry)"
  - "ChEMBL bioactivity curation as cross-check substrate"
  - "Berberine / resveratrol / EGCG ChEMBL surprise cases (most-potent target ≠ most-cited mechanism)"
  - "Comp-004 (supplement-abcg2-antagonism-computational.md) demonstrating gut-luminal IC50 occupancy framework on TCM-lineage compounds (curcumin, quercetin, EGCG)"
---

# H04 — TCM × Modern Rigor Methodology Lens (Stub)

> **Stub status.** This card is committed at stub-level on 2026-05-05 to register the meta-hypothesis in the falsification-card directory and force the "what would kill this thesis" framing onto the [TCM × modern rigor scope page](../tcm-modern-rigor-intersection.md). Full population (assumption stack, killshot menu, pre-committed thresholds, kill switches, failure-mode coverage map) is queued as Phase 2 P2-5 — see [tcm-modern-rigor-intersection.md § Open Follow-Ups](../tcm-modern-rigor-intersection.md#open-follow-ups).
>
> The pre-registration note on H01 ([H01-ward-dual-cassette.md](./H01-ward-dual-cassette.md) §Pre-registration) does not apply until this stub is upgraded to a full card. When the upgrade happens, the upgraded version is what gets pre-registered; the stub is informational scaffolding only.

---

## Claim (provisional, stub-level)

The methodology lens defined in [`tcm-modern-rigor-intersection.md`](../tcm-modern-rigor-intersection.md) — six-rule discipline of (1) mechanism-mapped to chokepoints, (2) ChEMBL cross-checked, (3) bioavailability-honest with explicit gut-luminal embrace, (4) formula-decomposed for designed-coverage analysis, (5) standardized-extract-specified, (6) falsification-card-disciplined — produces **actionable, gout-relevant findings** beyond what either reductionist single-compound analysis (which loses the multi-component design) or holistic "alternative medicine" framings (which lose the rigor) produce in isolation.

The "actionable" bar is operationalized as one or more of:

1. **Mechanistically-grounded compound recommendations** that survive ChEMBL cross-check at biologically achievable concentrations and map cleanly to a named chokepoint (NLRP3, ABCG2, URAT1, etc.).
2. **Multi-component formula decompositions** that surface designed-coverage patterns (different components hitting different chokepoints) that justify the formula structure beyond folk tradition.
3. **Falsification-card-grade hypotheses** for specific TCM-derived interventions (Smilax glabra as koji-payload candidate; Si Miao San as allopurinol adjunct; etc.) with pre-committed kill thresholds.
4. **Cross-domain insights** — e.g., a TCM compound's classical "damp-heat" indication mapping onto a specific modern chokepoint (XO + ABCG2 modulation) suggests other "damp-heat" herbs in the same classical category may share the mechanism — testable hypothesis.

The thesis is **gated on multilingual research access** — Chinese-language clinical trial literature, ChiCTR registry data, Japanese Kampo literature, Korean traditional medicine sources. The 2026-05-05 conversation that triggered this page made explicit that Open Enzyme should ingest global multilingual sources by default rather than treating language as a "barrier" — the AI substrate (Claude, DeepSeek, Qwen) is multilingual at zero marginal cost. See [`CLAUDE.md`](../../CLAUDE.md) for the global-multilingual-search default rule.

---

## Assumption Stack (placeholder — to be populated in Phase 2 P2-5)

The full assumption stack will be populated after the Phase 2 lit scans (P2-1 classical formulas, P2-3 Smilax glabra deep-dive, P2-4 Si Miao San decomposition, P2-6 bioavailability characterization) and comp-011 (P2-2 ChEMBL cross-check) land. Anticipated load-bearing assumptions:

1. The chokepoint map ([`nlrp3-exploit-map.md`](../nlrp3-exploit-map.md), [`gout-pathophysiology.md`](../gout-pathophysiology.md)) is granular enough to capture TCM compound mechanisms (vs. forcing them into mismatched modern categories)
2. ChEMBL's curated bioactivity dataset has sufficient coverage of TCM-relevant compounds (many natural products are sparsely curated in ChEMBL relative to medicinal-chemistry-derived compounds — this is documented in `chembl-cross-check.md`)
3. Modern Chinese clinical trial literature (ChiCTR registry) is sufficient quality to update wiki evidence tiers (Chinese RCTs have heterogeneous quality; this is empirically verifiable)
4. The "embrace gut-luminal mechanisms" reframe (rule #3) actually predicts therapeutic effect for low-bioavailability TCM compounds (vs. the alternative explanation that they don't work at all). Comp-004's IC50 occupancy framework on curcumin / quercetin / EGCG is a partial validation; broader compound classes need similar treatment.
5. The "designed coverage" interpretation of multi-component formulas (rule #4) is biologically defensible vs. being modern bias projection onto historical practice. Formula decomposition needs to falsify this too.
6. Open Enzyme's bandwidth is sufficient to apply the methodology rigorously across enough compounds to surface non-obvious findings (vs. a cataloging exercise that adds compound pages without producing new platform-relevant insight)

---

## Killshot Menu (placeholder — to be populated in Phase 2 P2-5)

Full killshot menu follows the H01 / H02 / H03 template. Anticipated highest-priority killshots:

- **Lit scan + ChEMBL cross-check first** (Phase 2 P2-1 + P2-2). Cheapest move. If the systematic ChEMBL cross-check of the 8 candidate gout compounds reveals that most have NO curated bioactivity at biologically achievable concentrations against any chokepoint, the methodology lens produces nothing actionable — kill.
- **Si Miao San decomposition outcome** (P2-4). If decomposition reveals all four herbs hit the same chokepoint (redundant rather than designed-coverage), the "formula decomposition surfaces designed coverage" claim weakens substantially.
- **Smilax glabra clinical evidence quality assessment** (P2-3). If Chinese-language modern clinical literature on Smilax glabra is uniformly low-quality (small n, no controls, no hard endpoints), the "modern Chinese clinical trial literature is sufficient quality" assumption fails.
- **Cross-validation against existing wiki TCM-lineage compounds** (oridonin, berberine, EGCG, theaflavins, curcumin, resveratrol). For each, retroactively apply the six-rule discipline. If the discipline produces no new insight beyond what the existing pages already capture, the methodology lens doesn't add value over the existing per-compound treatment.

---

## Pre-Committed Thresholds (placeholder — to be populated in Phase 2 P2-5)

To be defined when the killshot menu is populated. Anticipated structure follows H01: declared Alive / Killed / Pending thresholds for each load-bearing claim.

---

## Failure Modes Probed (placeholder — to be populated in Phase 2 P2-5)

To be populated. Anticipated relevant failure modes from [linter-design.md](../linter-design.md) §5: published-literature-gap, training-distribution bias (Western-research bias in the corpus), evidence-tier inflation (overstating "Animal Model" claims as "Supported" because TCM has long traditional use), the alternative-medicine-washing failure mode (modern-language dressing without underlying rigor — rule #6's discipline is the guard).

---

## Status

**Stub.** No killshot executed. No assumption stack pre-registered. Full hypothesis card is queued as Phase 2 P2-5 — see [tcm-modern-rigor-intersection.md § Open Follow-Ups](../tcm-modern-rigor-intersection.md#open-follow-ups).

**Survival count:** 0.

**Survival score:** 0.0 (undefined until full card and first survived killshot).

---

## Cross-References

- [tcm-modern-rigor-intersection.md](../tcm-modern-rigor-intersection.md) — the platform thesis this hypothesis formalizes
- [modality-chokepoint-matrix.md](../modality-chokepoint-matrix.md) — the chokepoint framework the lens applies across
- [chembl-cross-check.md](../chembl-cross-check.md) — the cross-check discipline (rule #2)
- [supplement-abcg2-antagonism-computational.md](../supplement-abcg2-antagonism-computational.md) (comp-004) — partial validation of the gut-luminal IC50 occupancy framework on TCM-lineage compounds
- [engineered-lbp-chassis.md](../engineered-lbp-chassis.md), [sirna-urat1-modality.md](../sirna-urat1-modality.md) — sister peer-track scope pages under chase-every-avenue
- [linter-design.md](../linter-design.md) — schema for the Falsification Card format
- [H01](./H01-ward-dual-cassette.md), [H02](./H02-engineered-lbp-thesis.md), [H03](./H03-sirna-urat1-thesis.md) — sibling falsification cards
