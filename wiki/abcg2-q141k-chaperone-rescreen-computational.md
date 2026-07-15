---
title: "ABCG2 Q141K Pharmacological-Chaperone Re-screen (real docking) — Computational Analysis (comp-047)"
date: 2026-07-14
tags:
  - abcg2
  - q141k
  - pharmacological-chaperone
  - cftr-corrector
  - autodock-vina
  - docking
  - drug-repurposing
  - computational-experiment
  - null-result
related:
  - abcg2-q141k-chaperone-screen-computational.md
  - abcg2-modulators.md
  - chassis-pending-interventions.md
  - gout-genetic-variants.md
  - validation-experiments.md
  - computational-experiments.md
sources:
  - "UniProt Q9UNQ0 (ABCG2_HUMAN) — NBD aa 37-286; Walker A P-loop; Q141K rs2231142 (high serum UA, gout, decreased protein abundance)"
  - "AlphaFold AF-Q9UNQ0-F1-model_v6 (EMBL-EBI): WT ABCG2 monomer; comp-032's receptor, reused"
  - "AutoDock Vina 1.2.5 (Eberhardt et al. 2021, J Chem Inf Model) — docking engine"
  - "ChEMBL target CHEMBL5393 (ABCG2/BCRP), 1307 human bioactivity records — Axis 2 empirical grounding (partial; see limitations)"
  - "comp-032 independent audit 2026-07-13 (logs/comp-reviews/2026-07-13-comp-032-fae0e36.md) — the review this experiment answers"
---

# ABCG2 Q141K Pharmacological-Chaperone Re-screen — real docking (comp-047)

**Question.** Does the FDA-approved drug surface contain a small molecule that binds a *fold-stabilizing* site on Q141K ABCG2's nucleotide-binding domain (NBD) — not the transport/ATP pocket — and is not already a known ABCG2 inhibitor/substrate, worth a wet-lab Q141K trafficking-rescue assay? This is the same question [comp-032](./abcg2-q141k-chaperone-screen-computational.md) asked with a descriptor heuristic; comp-047 re-asks it with **real AutoDock Vina docking**.

## Verdict: INCONCLUSIVE (honest null)

> **The screen does not identify a credible pharmacological-chaperone candidate, and — more importantly — it cannot, as designed, discriminate one.** Of 134 docked molecules: **0 high-confidence candidates, 2 marginal "uncertain"** (rosuvastatin, vorinostat), 132 "no." The decisive result is in the controls: **the four CFTR-corrector positive controls failed to earn rank** (0 of 4 reached candidate tier), while all known ABCG2 inhibitors were correctly rejected (0 false positives). Because the positive controls — the closest thing to ground-truth pharmacological chaperones in the set — do not separate from the field, the screen has no demonstrated power to find real chaperones. **The chaperone-rescue candidate ranking for ABCG2 Q141K is not computationally established** (In Silico; comp-047).

**This empirically confirms the comp-032 audit.** The [2026-07-13 independent review](../logs/comp-reviews/2026-07-13-comp-032-fae0e36.md) argued comp-032's "positive-control pass" was **tautological** — CFTR correctors scored high only because they were *assigned* the maximum drug-class prior (1.00), not because the heuristic detected chaperone-like binding. comp-047 removes every prior and forces the same positive controls to earn their rank from docking alone. **They don't.** That is the review's suspicion, confirmed by construction: when the class prior is gone, the chaperone signal comp-032 reported disappears.

## Control performance — the validity check comp-032 lacked

Positive controls carry **no prior** here; they must earn rank from Vina scores. "fold-rank" is the rank of the fold-site@Q141K affinity among all 134 molecules (1 = strongest).

**Positive controls — CFTR correctors (must earn candidate tier):**

| Molecule | fold@Q141K (kcal/mol) | transport@WT | margin | fold-rank | tier |
|---|---|---|---|---|---|
| lumacaftor | −7.35 | −8.77 | −1.42 | **2/134** | no |
| tezacaftor | −5.91 | −7.35 | −1.44 | 16/134 | no |
| elexacaftor | −5.80 | −7.75 | −1.95 | 18/134 | no |
| ivacaftor | −4.54 | −6.80 | −2.26 | 91/134 | no |

**0 of 4 earned candidate tier.** The tell: lumacaftor is the **#2 strongest fold-site binder of 134** — yet it binds the ATP/Walker-A pocket even harder (−8.77 vs −7.35), so the "prefers-fold-over-transport" filter (margin ≥ +1.5 for a candidate) kills it. Its margin is −1.42.

**Negative controls — known ABCG2 inhibitors/substrates (must NOT rank as chaperones):** all 13 (Ko143, fumitremorgin C, tariquidar, elacridar, novobiocin, azoles, methotrexate, mitoxantrone, topotecan, etoposide, sulfasalazine, + cyclosporine A which errored on a docking timeout) ranked **as "no." 0 false positives.** The screen correctly rejects inhibitors — but note this rests partly on the curated `role_tag` disqualifier, not purely on docking (see gap 2 below).

## Why it fails — two mechanistic reasons

The null is not a bug; it is what rigid-receptor docking can and cannot see:

1. **The fold-vs-transport margin is confounded.** The ATP/Walker-A pocket is a strong *generic* binder — across the library its affinities run stronger than the fold-site's (median transport −6.09 vs fold-site −4.86 kcal/mol). Only **9 of 134 molecules** have any positive margin (fold-preferring) at all, and the largest is just +0.76. The "prefers the fold site" criterion therefore selects against almost everything, including real chaperones, because almost everything prefers the deep ATP pocket. The two grid boxes are genuinely disjoint (centers 32.6 Å apart), so this is not a box-overlap artifact — the fold-site surface near residue 141 simply is not a discriminating druggable cavity in the static structure.
2. **Docking cannot model the chaperone mechanism.** A pharmacological chaperone works by stabilizing a *folding intermediate* / raising the protein's melting temperature — a thermodynamic, dynamic property. Docking a ligand into a single static folded (or statically-mutated) conformation tests shape/chemistry complementarity to that one snapshot; it does not compute whether the ligand lowers the folding free-energy barrier or rescues trafficking. This is comp-047's own stated weakest link (README limitation 1), and it is why even a perfectly executed docking screen would not be expected to rank chaperones reliably.

## Two residual gaps — comp-047 is a partial, not complete, upgrade

comp-047 fixes comp-032's **primary, fatal flaw** (the tautological positive-control validation) but inherits two of comp-032's other weaknesses. Neither changes the INCONCLUSIVE verdict — which rests entirely on Axis 1 positive controls failing to separate — but both must be stated:

1. **Sensitivity analysis did not run.** `sensitivity.py` (grid-center shifts, box-size 18/26 Å, alternate seeds, protonation) is written and called "mandatory" in the README, but `outputs/sensitivity.json` was not produced. For a *null* this matters less — there are no positive candidates to stress-test — but it means we cannot formally exclude that a differently-placed fold-site box would let the positive controls earn rank. The disjoint-box geometry and the large margin by which ivacaftor fails (rank 91/134) argue the null is robust, but a formal perturbation study was not completed. This is the same gap (comp-032 review critique #3) that comp-032 was faulted for.
2. **Axis 2 (empirical ChEMBL) is thin.** Only **3 of 135 molecules** were actually queried against ChEMBL CHEMBL5393 (ivacaftor, novobiocin, elacridar); the rest of the known-inhibitor disqualification rests on the curated `role_tag`, i.e., the same hand-curation comp-032 was criticized for. Because no molecule earned candidate status regardless, this does not affect the verdict — but Axis 2 is not the independent empirical inhibitor filter the README describes.

## What comp-047 establishes — and what it does not

**Establishes:** (a) comp-032's chaperone signal was an artifact of its class prior (positive controls fail without it); (b) rigid-receptor fold-vs-transport docking does not discriminate pharmacological chaperones for ABCG2 Q141K; (c) no FDA-approved molecule in this 134-compound library is a docking-supported chaperone candidate.

**Does not establish:** that no chaperone exists (absence of a docking signal ≠ absence of a chaperone, given the mechanism mismatch); folding rescue; Q141K-vs-WT selectivity; urate-flux effect; or any wet-lab priority.

## What this means for the corpus

- **The pharmacological-chaperone rescue route for Q141K stays a hedged hypothesis, not a validated repurposing surface.** Neither comp-032 (descriptor heuristic) nor comp-047 (real docking) produces a defensible candidate ranking. Any downstream page presenting a comp-032 "top-10 chaperone candidates" list must downgrade it to "prior-ranked hypotheses; real docking (comp-047) came back inconclusive."
- **No compounding-pharmacy conversation is warranted on this route** until a fundamentally different method produces candidates. comp-032's queuing of a diflunisal/lumacaftor partner call is retracted.
- **The route is not dead — the method is.** A genuine computational answer needs folding-stability modeling (MD-based ΔΔG of folding, FoldX/Rosetta ΔΔG on the Q141K mutant, or an explicit thermal-shift surrogate), not docking. The cheapest real answer is wet-lab: a HEK293/Caco-2 Q141K trafficking-rescue screen (surface 5D3 epitope by flow cytometry) paired with basolateral→apical **urate flux** and an ABCG2-inhibition counterscreen, registered as a validation experiment ([`validation-experiments.md`](./validation-experiments.md)).

## Cross-references

Supersedes: [comp-032 descriptor screen](./abcg2-q141k-chaperone-screen-computational.md). Experiment folder: [`etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/`](./etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/) (verdict in [`outputs/summary.md`](./etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/summary.md), control check in [`outputs/controls.md`](./etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/controls.md)). Platform context: [`abcg2-modulators.md`](./abcg2-modulators.md), [`chassis-pending-interventions.md`](./chassis-pending-interventions.md), [`gout-genetic-variants.md`](./gout-genetic-variants.md). Registry: [`computational-experiments.md`](./computational-experiments.md).
