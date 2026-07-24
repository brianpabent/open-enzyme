---
id: H05
title: "An *A. oryzae*-engineered soluble DAF/CD55 SCR1-4 construct is a candidate fermentable CP0 modulator"
committed: 2026-05-05
status: Stub
survival_count: 0
tags:
  - hypothesis
  - daf-cd55
  - scr14-truncated
  - cp0
  - complement-priming
  - fermentable-coverage
  - engineered-koji
  - peer-track
related:
  - ../daf-cd55-protease-stability-computational.md
  - ../daf-cd55-scr14-truncated-computational.md
  - ../complement-c5a-gout.md
  - ../engineered-lbp-chassis.md
  - ../modality-chokepoint-matrix.md
  - ../koji-endgame-strain.md
  - ./H01-ward-dual-cassette.md
  - ./H02-engineered-lbp-thesis.md
  - ./H04-tcm-rigor-intersection.md
  - ./README.md
sources:
  - "comp-006 (full DAF ectodomain protease proxy; risk unresolved) — `daf-cd55-protease-stability-computational.md`"
  - "comp-012 (SCR1-4 truncated DAF protease proxy; risk unresolved) — `daf-cd55-scr14-truncated-computational.md`"
  - "DAF/CD55 UniProt P08174"
  - "complement-c5a-gout.md — CP0 mechanism + therapeutic landscape"
---

# H05 — DAF SCR1-4 CP0-Closure Thesis (Stub)

> **Evidence status:** stub. Assumptions, pre-committed thresholds, kill switches, and failure-mode coverage remain incomplete; see [`complement-c5a-gout.md`](../complement-c5a-gout.md) and [`daf-cd55-scr14-truncated-computational.md`](../daf-cd55-scr14-truncated-computational.md).
>
> Pre-registration discipline (per H01) does not apply until this stub is upgraded to a full card.

> **Relationship to adjacent tracks:** H05 examines engineered DAF at C3-convertase decay acceleration. Retired COMP-018 supplies no compound ranking or C1-INH transfer authority. Rosmarinic acid, C1-INH, and EcN DAF remain separate, unranked hypotheses with their own material or configuration gates. [COMP-043](../daf-lactoferrin-ecn-folding-feasibility-computational.md) supplies no EcN folding-capacity or chassis-priority evidence.

---

## Claim (provisional, stub-level)

A soluble DAF/CD55 SCR1-4 construct (UniProt P08174, residues 35–285) heterologously expressed in *A. oryzae* and delivered in a compatible koji format may provide fermentable CP0 complement modulation. Expression, retained activity, luminal access, protease stability, and gout relevance are unvalidated.

The thesis composes three sub-claims, each independently falsifiable:

1. **Cassette feasibility.** The SCR1-4 construct can be cloned with a koji-native α-amylase signal peptide, expressed reproducibly in *A. oryzae* (RIB40 or NSlD-ΔP10), and recovered as an active soluble fragment. The eight annotated intrachain disulfide pairs (two per SCR domain, UniProt P08174) require peptide-level connectivity mapping; titer alone cannot establish native fold.

2. **Functional CCP-regulatory activity.** The expressed soluble truncated fragment retains decay-accelerating function — specifically C3b and C4b binding, and C3 convertase decay-acceleration sufficient to suppress C5a generation in a complement-activation assay (e.g., zymosan-stimulated human serum + ELISA for C5a).

3. **Mucosal-surface delivery.** Luminal-side soluble DAF SCR1-4 (delivered orally as part of an engineered koji product) actually engages the gout-relevant complement-priming step in the gut → submucosal macrophage signaling axis, OR alternatively acts at the bacterial/mucus complement-priming interface in a manner that meaningfully reduces downstream CP0 priming load. The macrophages doing the CP0 priming are submucosal; whether luminal DAF can reach them or only modulate proximal complement activation is empirically open.

The truncation is motivated by [comp-012](../daf-cd55-scr14-truncated-computational.md): the full ectodomain includes a low-confidence Ser/Thr-rich stalk (aa 286–353), while the SCR1-4 construct removes it. The inherited model's HIGH/LOW contrast is invalid because it used pLDDT confidence as solvent accessibility; it neither demonstrated exposed cleavage sites nor validated survival. Stalk truncation remains a useful, falsifiable design hypothesis, and the sub-claims above plus retained activity through processing are wet-lab gating questions.

---

## Assumption Stack (placeholder — to be populated when this stub is upgraded)

Anticipated load-bearing assumptions:

1. **Disulfide folding fidelity.** Whether *A. oryzae* can form the eight annotated intrachain disulfides on the DAF SCR1-4 construct is unmeasured. The annotations define peptide-level connectivity measurements; they do not predict PDI demand, secretion capacity, or compatibility with another payload.

   The falsifiable interaction test measures expression, native fold, secretion, retained activity, stress, and growth for every payload across matched single-, pairwise-, and triple-cassette configurations. A loss in one configuration triggers mechanism-specific diagnosis and redesign; no disulfide count, titer band, or single-payload result selects separate strains or another chassis. See [chaperone-orthogonal-stacking.md](../chaperone-orthogonal-stacking.md#matched-experiment).
2. **CCP-regulatory function survives truncation.** Native DAF/CD55's decay-accelerating function uses all four SCR domains plus the membrane GPI anchor for proper geometry; truncating to soluble SCR1-4 changes the geometry. Some published soluble DAF constructs retain function; whether the specific aa 35–285 boundary preserves activity is not pre-validated.
3. **Mucosal access geometry.** Submucosal macrophages doing CP0 priming are on the basolateral side of the epithelium; luminal-side soluble DAF would need to either cross the epithelium (unlikely for a 28 kDa protein) or modulate complement upstream (in the lumen, on bacterial surfaces, in the mucus layer) in a way that meaningfully reduces priming load reaching the macrophages.
4. **Alternative-pathway dominance in gout-relevant complement priming.** DAF inhibits both classical and alternative pathway C3 convertases; if the gout-relevant priming is driven primarily by a pathway DAF doesn't cover (e.g., MBL-pathway dominance or direct C5 cleavage), the inhibition is incomplete.
5. **Ferment-stability of the active form.** COMP-012 does not verify protease stability. Whether the correctly folded construct retains activity through fermentation, storage, gut transit, and arrival at the intended activity site is empirically open.

---

## Killshot Menu (placeholder — to be populated when this stub is upgraded)

Anticipated highest-priority killshots:

- **Wet-lab expression in *A. oryzae* RIB40 first** (~$2K, ~6 weeks): is intact construct recovered reproducibly? Reducing/nonreducing SDS-PAGE screens identity and aggregation but does not establish native disulfide connectivity.
- **CCP-regulatory activity assay on the secreted fragment** (~$1K reagents + assay): does the truncated soluble form retain function?
- **Literature deep-dive on published soluble DAF constructs** ($0, ~1 week — could be a Paperclip-grep follow-up per `etc/manual-literature-mining.md`): has anyone made and tested an aa 35–285 soluble DAF? What was the activity profile?
- **Comparison with sCR1 / Factor H truncated soluble constructs** ($0): if other complement regulators have published soluble-truncated activity precedents, that informs the DAF design space.

---

## Provisional experiment-design constants

The legacy 50 mg/L titer, 30% C5a-inhibition, and intermediate response bands are provisional routing constants, not literature-derived therapeutic thresholds. Freeze the exact concentration series, assay precision, replicate design, and confirmatory decision rule after a pilot and before the result-bearing comparison.

- **Advance the exact configuration:** reproducible intact-protein recovery; peptide-level LC-MS/MS identifies the eight annotated disulfide pairs without a dominant alternative-connectivity species at the validated detection limit; free-thiol results are consistent with the mapped oxidized form; and the blinded complement assay shows reproducible activity relative to inactive-material and buffer controls.
- **Redirect the configuration:** absent or irreproducible expression, unresolved/mixed connectivity after prespecified optimization, or no activity above the validated assay detection limit.
- **Intermediate:** change one construct, signal, host, or process variable at a time and repeat the full identity, connectivity, free-thiol, and activity workflow.

---

## Status

**Stub.** Stalk truncation is a computationally motivated construct hypothesis; empirical protease risk and function are unresolved. Wet-lab not yet executed. Upgrade the falsification card when a sub-experiment is committed.

**Survival count:** 0.

**Survival score:** 0.0 (undefined until full card and first survived killshot).

---

## Cross-References

- [`daf-cd55-protease-stability-computational.md`](../daf-cd55-protease-stability-computational.md) — comp-006 generated the matched full-ectodomain-versus-truncation hypothesis; it did not establish protease exposure or survival
- [`daf-cd55-scr14-truncated-computational.md`](../daf-cd55-scr14-truncated-computational.md) — comp-012, the invalid pLDDT-accessibility proxy that still motivates direct testing of the truncated construct
- [`complement-c5a-gout.md`](../complement-c5a-gout.md) — CP0 mechanism and therapeutic landscape
- [`engineered-lbp-chassis.md`](../engineered-lbp-chassis.md) — alternative chassis for soluble complement regulators (LBP track)
- [`daf-lactoferrin-ecn-folding-feasibility-computational.md`](../daf-lactoferrin-ecn-folding-feasibility-computational.md) — invalidated COMP-043 arithmetic; any EcN DAF arm requires independent exact-configuration expression, native-fold, and retained-function evidence
- [`modality-chokepoint-matrix.md`](../modality-chokepoint-matrix.md) — portfolio context for engineered soluble complement regulators
- [`koji-endgame-strain.md`](../koji-endgame-strain.md) — could add CP0 as a candidate row alongside the four current chokepoints if H05 progresses through wet-lab
- [`linter-design.md`](../linter-design.md) — schema for the Falsification Card format
- [`validation-experiments.md` §1.25](../validation-experiments.md) — exact single-cassette DAF SCR1-4 test; readouts address expression, disulfide folding, processing stability, and CCP-regulatory activity without preselecting a later architecture.
- [H01](./H01-ward-dual-cassette.md), [H02](./H02-engineered-lbp-thesis.md), [H03](./H03-sirna-urat1-thesis.md), [H04](./H04-tcm-rigor-intersection.md) — sibling falsification cards
