---
type: contradiction
sweep_date: 2026-05-15
sweep_sha: 8653de9
section_index: 1
global_index: 5
pass3_verdict: Augment
overlap_tag: EXTENSION
---

# The `gout-kill-chain-delivery-routes.md` page describes intra-articular uricase + catalase as "genuinely unexplored" and a "highest-leverage 🟡 cell," while `delivery-route-matrix.md` §"Why SC uricase doesn't work" argues that SC uricase fails for layered biochemical reasons, and the intra-articular route inherits some of the same H₂O₂ housekeeping challenges.

1. **The `gout-kill-chain-delivery-routes.md` page describes intra-articular uricase + catalase as "genuinely unexplored" and a "highest-leverage 🟡 cell," while `delivery-route-matrix.md` §"Why SC uricase doesn't work" argues that SC uricase fails for layered biochemical reasons, and the intra-articular route inherits some of the same H₂O₂ housekeeping challenges.** *Locations:* `gout-kill-chain-delivery-routes.md` §"Uricase — Uric Acid Degradation / Crystal Dissolution" (Open territory bullet: "Intra-articular Pickering emulsion cascade bioreactor") and `delivery-route-matrix.md` §"Why SC uricase doesn't work (even with catalase co-formulation, even with tolerogenic NP)" (bullet 2: "H₂O₂ byproduct accumulates in tissue without local catalase"). *Analysis:* The kill-chain page frames intra-articular uricase as a high-leverage open vector, citing the Pickering emulsion bioreactor and self-propelled nanomotor preclinical papers that co-deliver catalase. The delivery-route-matrix page, in its SC uricase analysis, argues that even co-formulated catalase doesn't fully solve the H₂O₂ problem because H₂O₂ diffuses faster than catalase can scavenge it spatially. The intra-articular space is a smaller, more contained volume than a SC depot, and the Pickering emulsion approach co-confines uricase and catalase at an oil-water interface with angstrom-scale proximity — far tighter spatial coupling than co-formulated free enzymes. The delivery-route-matrix page's SC critique may not fully transfer to the intra-articular case, but the underlying biochemistry concern (H₂O₂ diffusion kinetics vs. catalase scavenging kinetics) is unresolved for both routes. The contradiction is not a factual error in either page — it's a genuinely unresolved question about whether spatial confinement (Pickering emulsion, fusion protein, or nanoparticle co-encapsulation) closes the H₂O₂ diffusion gap tightly enough for tissue-local uricase delivery to be safe. *Suggested resolution:* A dedicated "Intra-articular uricase H₂O₂ safety" section in either `delivery-route-matrix.md` or a new `intra-articular-uricase.md` page, explicitly comparing the spatial coupling of the three approaches (Pickering emulsion, uricase-catalase fusion protein, and free co-formulated enzymes) against the H₂O₂ diffusion coefficient and catalase kcat, to determine whether the diffusion gap is closable at achievable enzyme densities.

> **Pass 3 review — Augment.** `[OVERLAP: EXTENSION]` The unresolved-H₂O₂ framing is sound: `delivery-route-matrix.md` argues SC uricase fails partly because H₂O₂ diffuses in tissue without sufficiently co-localized catalase, while `gout-kill-chain-delivery-routes.md` treats intra-articular uricase ± catalase / Pickering emulsion as a high-leverage open vector. Add the chassis-pending routing explicitly: this hits CP6/local tophi dissolution and already belongs in `chassis-pending-interventions.md` rather than being judged by koji fit.

---

## ✓ Actioned 2026-05-16

Two-step action: lit-scan-first verified novelty, then spawn comp.

**Lit scan (foreground subagent, ~10 min):** Confirmed the reaction-diffusion math is **missing from every published architecture paper** (Pickering emulsion, fusion protein, nanozyme, nanomotor, free co-formulated). Liu 2025 *J Nanobiotechnology* Pickering emulsion (PMID 41390400) is closest — FRET >85%, interfacial enzyme densities — but doesn't compute predicted steady-state H₂O₂ escape flux. Toxicity threshold itself weakly anchored (Schalkwijk 1986/87 PMID 3707631 reports injected GOx dose not steady-state [H₂O₂]; sub-10 µM presumptively safe / 100+ µM documented-toxic / gray band between is unmodeled). Lit scan confirmed comp-NNN would be **novel work that closes a real gap, not duplicating existing published analysis.**

**[`wiki/chassis-pending-interventions.md` §6](../../wiki/chassis-pending-interventions.md):** added a "Key biochemistry gap — H₂O₂ diffusion-vs-catalase-scavenging math" paragraph naming the unresolved question, citing the lit-scan headline papers (Liu 2025 PMID 41390400, Lin 2022 PMID 34968071, Liu 2025 PMID 40057522, Jung 2017 PMID 28287162, Schalkwijk PMID 3707631), and noting [comp-035](../../wiki/computational-experiments.md) is in flight. Cross-references updated.

**comp-035 spawned as background Opus subagent** following the `new-comp-experiment` skill discipline. Brief: reaction-diffusion model with Damköhler-number analysis for the three spatial-coupling architectures (Pickering emulsion at nm scale, fusion protein at Å scale, free co-formulated at µm scale), parameterized by published kinetic constants (uricase kcat ~10 s⁻¹, catalase kcat ~4 × 10⁷ s⁻¹, D_H2O2 ~1.4 × 10⁻⁹ m²/s scaled for synovial fluid viscosity), compared against a literature-derived synovial-tissue toxicity threshold band. Output: per-architecture GREEN/YELLOW/RED verdict with sensitivity analysis + wet-lab handoff recommendation. Lit-scan output used as inputs/provenance starting context.

Auto-appended walkthrough **Item 26 — Review comp-035 output** per skill Section 4 background-subagent rule.

Pass 3's "chassis-pending routing" note was already satisfied (§6 has existed since Item 1's Pass-3 reading; cross-references in delivery-route-matrix.md and gout-kill-chain-delivery-routes.md still resolve to §6 correctly).
