---
id: H05
title: "An *A. oryzae*-engineered soluble DAF/CD55 SCR1-4 truncated construct (aa 35-285) is a viable fermentable CP0 modulator that closes the platform's documented complement-priming gap"
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
  - "comp-006 (full DAF ectodomain protease stability) — `daf-cd55-protease-stability-computational.md`"
  - "comp-012 (SCR1-4 truncated DAF protease stability — verdict LOW, 2026-05-05) — `daf-cd55-scr14-truncated-computational.md`"
  - "DAF/CD55 UniProt P08174"
  - "Sweep daemon Pass 2 (commit 487fad3, 2026-05-05) Connection #2 — surfaced the truncation hypothesis as wet-lab proposal"
  - "complement-c5a-gout.md — CP0 mechanism + therapeutic landscape"
---

# H05 — DAF SCR1-4 CP0-Closure Thesis (Stub)

> **Stub status.** Committed 2026-05-05 to register the hypothesis in the falsification-card directory and force the "what would kill this thesis" framing onto the just-closed (computationally) CP0 gap. Full population (assumption stack, killshot menu, pre-committed thresholds, kill switches, failure-mode coverage map) queued as a Phase 2 item — see [`complement-c5a-gout.md` § CP0 status update](../complement-c5a-gout.md) and [`daf-cd55-scr14-truncated-computational.md`](../daf-cd55-scr14-truncated-computational.md).
>
> Pre-registration discipline (per H01) does not apply until this stub is upgraded to a full card.

---

## Claim (provisional, stub-level)

A soluble DAF/CD55 SCR1-4 truncated construct (UniProt P08174, residues 35–285) heterologously expressed in *A. oryzae* via the standard Ward 1995 / Huynh 2020 secretory cassette architecture, delivered in shio-koji or dried-koji format, is a viable fermentable CP0 (complement priming) modulator that closes the Open Enzyme platform's documented complement-coverage gap.

The thesis composes three sub-claims, each independently falsifiable:

1. **Cassette feasibility.** The SCR1-4 construct can be cloned with a koji-native α-amylase signal peptide, expressed in *A. oryzae* (RIB40 or NSlD-ΔP10 protease-deletion host) at therapeutic-relevant titers (≥50 mg/L pore-fluid equivalent, mirroring the H01 lactoferrin floor scaled for the smaller protein), and secreted as a correctly-folded soluble fragment with all 12 intrachain disulfide bonds (3 per SCR domain × 4 SCRs) intact.

2. **Functional CCP-regulatory activity.** The expressed soluble truncated fragment retains decay-accelerating function — specifically C3b and C4b binding, and C3 convertase decay-acceleration sufficient to suppress C5a generation in a complement-activation assay (e.g., zymosan-stimulated human serum + ELISA for C5a).

3. **Mucosal-surface delivery.** Luminal-side soluble DAF SCR1-4 (delivered orally as part of an engineered koji product) actually engages the gout-relevant complement-priming step in the gut → submucosal macrophage signaling axis, OR alternatively acts at the bacterial/mucus complement-priming interface in a manner that meaningfully reduces downstream CP0 priming load. The macrophages doing the CP0 priming are submucosal; whether luminal DAF can reach them or only modulate proximal complement activation is empirically open.

The truncation is grounded in [comp-012](../daf-cd55-scr14-truncated-computational.md): the full DAF ectodomain (aa 35–353) failed comp-006 protease stability (HIGH risk, max 0.388 — driven by the disordered Ser/Thr stalk aa 286–353); the truncated SCR1-4 construct (aa 35–285) tested LOW (0.039, identical to uricase) with 100% of exposed sites eliminated. Computational feasibility is in silico-validated; the three sub-claims above are the wet-lab gating questions.

---

## Assumption Stack (placeholder — to be populated when this stub is upgraded)

Anticipated load-bearing assumptions:

1. **Disulfide folding fidelity.** *A. oryzae* ER PDI capacity is sufficient to fold 12 intrachain disulfides on a single ~28 kDa secreted protein. Comp-010 noted the OE pair (uricase 0 disulfides + lactoferrin 17 disulfides = 17 total) is within demonstrated NSlD-ΔP10 capacity per Huynh 2020. Adding DAF SCR1-4's 12 disulfides as a third co-expressed cassette would push to 29 total — a real but not catastrophic increase.
2. **CCP-regulatory function survives truncation.** Native DAF/CD55's decay-accelerating function uses all four SCR domains plus the membrane GPI anchor for proper geometry; truncating to soluble SCR1-4 changes the geometry. Some published soluble DAF constructs retain function; whether the specific aa 35–285 boundary preserves activity is not pre-validated.
3. **Mucosal access geometry.** Submucosal macrophages doing CP0 priming are on the basolateral side of the epithelium; luminal-side soluble DAF would need to either cross the epithelium (unlikely for a 28 kDa protein) or modulate complement upstream (in the lumen, on bacterial surfaces, in the mucus layer) in a way that meaningfully reduces priming load reaching the macrophages.
4. **Alternative-pathway dominance in gout-relevant complement priming.** DAF inhibits both classical and alternative pathway C3 convertases; if the gout-relevant priming is driven primarily by a pathway DAF doesn't cover (e.g., MBL-pathway dominance or direct C5 cleavage), the inhibition is incomplete.
5. **Ferment-stability of the active form.** comp-012 verifies protease stability of the polypeptide backbone in shio-koji; whether the disulfide-folded active form survives ALL of fermentation + storage + gut transit + reaching the colonic activity site is empirically open.

---

## Killshot Menu (placeholder — to be populated when this stub is upgraded)

Anticipated highest-priority killshots:

- **Wet-lab expression in *A. oryzae* RIB40 first** (~$2K, ~6 weeks): is the construct secreted at all? SDS-PAGE under non-reducing conditions for disulfide assessment.
- **CCP-regulatory activity assay on the secreted fragment** (~$1K reagents + assay): does the truncated soluble form retain function?
- **Literature deep-dive on published soluble DAF constructs** ($0, ~1 week — could be a Paperclip-grep follow-up per `manual-literature-mining.md`): has anyone made and tested an aa 35–285 soluble DAF? What was the activity profile?
- **Comparison with sCR1 / Factor H truncated soluble constructs** ($0): if other complement regulators have published soluble-truncated activity precedents, that informs the DAF design space.

---

## Pre-Committed Thresholds (placeholder — to be populated when this stub is upgraded)

Anticipated structure:
- **Alive:** secreted ≥50 mg/L pore-fluid equivalent + ≥40% native disulfide-folded form on non-reducing SDS-PAGE + ≥30% C5a-generation inhibition vs. control in a zymosan-activation assay
- **Killed:** secreted <10 mg/L OR fully reduced (no disulfides) OR no detectable CCP-regulatory activity
- **Pending:** intermediate values; iterate on construct boundaries (try aa 35–250 alternative truncation), host strain (NSlD-ΔP10 vs. RIB40), or secretion signal

---

## Status

**Stub.** Computational claim verified by comp-012 (LOW protease risk, 2026-05-05). Wet-lab not yet executed. Falsification card to be upgraded to full when wet-lab access is confirmed and a sub-experiment is committed.

**Survival count:** 0.

**Survival score:** 0.0 (undefined until full card and first survived killshot).

---

## Cross-References

- [`daf-cd55-protease-stability-computational.md`](../daf-cd55-protease-stability-computational.md) — comp-006, the analysis that surfaced the stalk problem
- [`daf-cd55-scr14-truncated-computational.md`](../daf-cd55-scr14-truncated-computational.md) — comp-012, the in silico validation of the truncated construct
- [`complement-c5a-gout.md`](../complement-c5a-gout.md) — CP0 mechanism + therapeutic landscape (note the 2026-05-05 status update reframing the platform gap)
- [`engineered-lbp-chassis.md`](../engineered-lbp-chassis.md) — alternative chassis for soluble complement regulators (LBP track)
- [`modality-chokepoint-matrix.md`](../modality-chokepoint-matrix.md) — the matrix's "Engineered soluble complement regulators" row (now reflecting comp-012 verdict)
- [`koji-endgame-strain.md`](../koji-endgame-strain.md) — could add CP0 as a candidate row alongside the four current chokepoints if H05 progresses through wet-lab
- [`linter-design.md`](../linter-design.md) — schema for the Falsification Card format
- [H01](./H01-ward-dual-cassette.md), [H02](./H02-engineered-lbp-thesis.md), [H03](./H03-sirna-urat1-thesis.md), [H04](./H04-tcm-rigor-intersection.md) — sibling falsification cards
