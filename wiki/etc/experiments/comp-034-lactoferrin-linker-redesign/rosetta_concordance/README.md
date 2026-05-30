---
title: "comp-034 Rosetta concordance leg — physics ΔΔG + structure-gated cleavage"
date: 2026-05-30
experiment_id: comp-034 (extension)
parent: lactoferrin-linker-redesign-computational.md
status: complete
evidence_level: Mechanistic Extrapolation (in silico only)
---

# comp-034 — Physics ΔΔG + structure-gated cleavage on the inter-lobe linker

Two orthogonal methods added to the comp-034 concordance gate, unblocked by the
PyRosetta install of 2026-05-29 (UW academic-license update). They answer a
question the original five sequence/proxy metrics could not see: **what does each
linker redesign do to the actual fold, and is the WT linker even cleavable given
its structure?**

The five original metrics (ESM2 pseudo-pLDDT, sequence cleavage score, CAI,
loop-pLDDT, WT-similarity) are all sequence- or proxy-based. Neither a physics
ΔΔG on the 3-D structure nor a real solvent-accessibility/secondary-structure
gate on the cleavage score existed in the gate. Both are added here.

## TL;DR

**`NEEEQQQEEEQ` (the MPNN-native arm) wins on both axes and is the wet-lab pick.
The proline-rigidification arms are self-defeating.** One variable explains the
whole result: **inter-lobe helix retention.** The WT linker (UniProt 353–363,
`SEEEVAARRAR`) is a structured α-helix (9 of 11 residues helical). Keep the helix
and you keep fold stability *and* protease resistance (proteases require an
extended substrate; a helix resists). Break it with proline and you lose both.

| Candidate | linker | Cartesian ΔΔG (REU) | structure-gated cleavage vs WT | helix | verdict |
|---|---|---|---|---|---|
| WT | `SEEEVAARRAR` | 0.00 (ref) | — | 0.818 | reference |
| **MPNN `NEEEQQQEEEQ`** | 8 subs | **+0.23 (neutral)** | **−66%** | 0.818 | **wins both** |
| MPNN `NEEEQEEQDQQ` | 8 subs | +2.39 (neutral) | −66% | 0.818 | wins both |
| `S353E+V357P` | 2 subs | +21.26 (destabilizing) | −17% | 0.727 | loses both |
| `V357P` | 1 sub | +20.11 (destabilizing) | −9% | 0.727 | loses both |
| multi-proline `EEEEPAAPPAP` | 6 subs | +57.48 (severe) | −3% | 0.364 | loses both, worst |

## Method 1 — Cartesian ΔΔG (fold stability)

Relaxed-neighborhood ΔΔG: thread the linker mutations onto the AlphaFold
structure (`AF-P02788-F1-model_v6.pdb`, full 710-residue monomer), FastRelax the
linker neighborhood (residues within 8 Å of 353–363; 23 movable residues) in
**Cartesian space** (`ref2015_cart` + `cart_bonded`, LBFGS), coordinate-
constrained to the start coords. 10 independent-seed trajectories per candidate;
**minimum-energy** trajectory is the estimator (correct for a stochastic relax
search); ΔΔG = min(mutant) − min(WT). Script: `rosetta_ddg.py`. This follows the
Park et al. 2016 Cartesian-ddG method already cited in
[`protein-engineering-strategy.md` §5.2](../../../protein-engineering-strategy.md).

**Result:** both MPNN charge/polar arms are statistically indistinguishable from
WT (ΔΔG +0.23 / +2.39 REU, helix retained at 0.818). Every proline arm is
destabilizing: +20 REU (single V357P), +21 REU (S353E+V357P), +57 REU
(multi-proline, helix collapsed to 0.364).

**Estimator note (load-bearing).** Per-trajectory spread is large (sd ≈ 30 REU):
by the *mean*, `NEEEQQQEEEQ` even scores "more stable than WT" (−8.31), which is
sampling noise. By the *minimum* it is a clean +0.23. The WT min-energy basin
(−736.8 REU) was independently re-found on trajectories 1, 4, and 8 of 10, so
min-of-10 is converged — more trajectories would not move it. (Cross-method
caveat: a first-pass **torsion-space, mean-based** run was noisy enough to
mis-rank `NEEEQEEQDQQ` above `V357P`; it motivated the upgrade to Cartesian-min
and is retained only as `rosetta_ddg_results_torsion3.json` for genealogy. It is
**not** an independent confirmation.)

## Method 2 — Structure-gated cleavage (protease axis)

The existing comp-005/034 cleavage model
([`lib/protease_stability.py`](../../lib/protease_stability.py)) uses **pLDDT as
its accessibility proxy**: `classify_accessibility(mean_plddt)` → buried (≥80,
0.1×) / partial / exposed. The inter-lobe linker has pLDDT 93–98, so all 11
residues are scored **"buried" → 0.1× protection.** But pLDDT is a *confidence*
score, not burial — a confidently-predicted solvent-exposed helix scores 95.
Real SASA (Tien 2013 relative) on the structure: **8 of 11 linker residues are
solvent-exposed, 3 partial, 0 buried.** The proxy mis-classifies an exposed
helix as buried, suppressing the linker's sequence-driven cleavage risk ~10×.

The real protection is **conformation, not burial**: proteases need an extended
substrate across the active-site cleft (Tyndall et al. 2005), so a helix resists
even when solvent-exposed. The re-gated score replaces the pLDDT proxy with
real SASA × a secondary-structure conformation factor (helix 0.2×, strand 0.7×,
loop/turn 1.0×). Computed first on the WT backbone (`structure_gated_cleavage.py`)
and then on **each mutant's own relaxed structure** (`refold_via_relax.py` —
thread → Cartesian-relax → dump pose → real per-residue SASA + DSSP), which
removes the WT-backbone approximation.

**Result (real mutant structures):** the MPNN arms cut structure-gated cleavage
~66% vs WT (they strip preferred residues *and* keep the helix). The proline arms
deliver only −9% (V357P), −17% (S353E+V357P), and −3% (multi-proline): breaking
the protective helix re-exposes the backbone and largely cancels the
sequence-preference gain. **The proline-rigidification strategy is self-defeating
on this target.**

## Two corrections vs the first-pass approximation (intellectual honesty)

The WT-backbone approximation (`structure_gated_cleavage.py`) overstated two
things; real mutant structures (`refold_via_relax.py`) corrected both:

1. **Multi-proline is *not* worse than WT.** The approximation put it at 1.624
   (above WT's 1.155) because it assumed too much helix loss (0.273). On the real
   relaxed structure it retains more helix (0.364) and lands at 1.104 — **roughly
   WT-equivalent, not worse.** Honest reading: 6 substitutions buy ~3% net
   protease benefit. Damning for an "aggressive" design, but "no better than WT."
2. **`NEEEQQQEEEQ`'s cleavage edge is ~3×, not ~9×.** The approximation (0.134)
   borrowed the WT backbone's smaller side chains; the real Glu/Gln-loaded
   structure is more exposed (0.388). Still decisively best — by an honest margin.

## Wet-lab implication (revises the §1.10 arm recommendation)

The original comp-034 framing treated the proline single/double mutants as the
"conservative / safe regulatory story" and `NEEEQQQEEEQ` as the "aggressive" arm.
**The physics inverts that risk ordering.** `NEEEQQQEEEQ` is the most stable
(ΔΔG ≈ 0) and most protease-resistant (−66%) candidate, with the helix intact —
it should be the **primary** wet-lab arm, not the aggressive one. The proline
arms are destabilizing and deliver little protease benefit; they are the higher-
risk choices and should be demoted or dropped. Recommended plate: **WT control +
`NEEEQQQEEEQ` (primary) + `NEEEQEEQDQQ` (sibling/backup)**, with a proline arm
retained only if an orthogonal-mechanism control is wanted.

## Caveats

- **Evidence level: Mechanistic Extrapolation (in silico).** Wet-lab proteolysis
  + thermal-stability (Tm) assays are the validators.
- Conformation-gate weights (helix 0.2×) are heuristic; the **direction** is
  robust (helix-breaking raises accessibility; MPNN arms dominate under any
  reasonable weighting), the absolute structure-gated numbers are not precise.
- ΔΔG is single-AlphaFold-backbone; no backbone-conformational ensemble, no
  explicit solvent, no entropy term. Multi-mutant additivity is not assumed
  (full relax of each mutant), but ref2015 force-field error (~1–2 kcal/mol
  class) dominates the residual, not sampling.
- A genuinely orthogonal ML predictor (ESMFold/AF2) was **blocked on this host**
  (openfold + deepspeed not installed; hard Apple-Silicon/CPU build). Method 2's
  "real structures" come from Rosetta relax, not an independent fold. An
  independent re-fold belongs on the GPU/cloud path (bio-ai-tools A4 backlog).

## Reproduce

```bash
cd etc/experiments/comp-034-lactoferrin-linker-redesign/rosetta_concordance
python3 rosetta_ddg.py --ntraj 10 --out rosetta_ddg_results_cartesian10.json   # ~2.1 h CPU
python3 structure_gated_cleavage.py                                            # seconds
python3 refold_via_relax.py                                                    # ~38 min CPU
```

Requires PyRosetta (`pyrosetta 2026.3`, installed 2026-05-29 under the Rosetta &
PyRosetta Non-Commercial License). See `provenance.md` for tool versions, inputs,
and the pre-commit verification record.

## Artifacts

- `rosetta_ddg_results_cartesian10.json` — gold-standard ΔΔG (min/mean/sd/all-traj)
- `rosetta_ddg_results_torsion3.json` — noisy first-pass (genealogy only)
- `structure_gated_cleavage_results.json` — WT-backbone structure-gated cleavage
- `refold_via_relax_results.json` — structure-gated cleavage on real mutant structures
- `relaxed_mutant_poses/*.pdb` — 6 dumped relaxed mutant structures
