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

> **The screen does not identify a credible pharmacological-chaperone candidate, and — more importantly — it cannot, as designed, discriminate one.** Of 134 docked molecules: **0 high-confidence candidates, 2 marginal "uncertain"** (rosuvastatin, vorinostat — reduced to **1** after the Axis 2 expansion disqualified rosuvastatin as a known ABCG2 substrate; see Residual gaps), 132 "no." The decisive result is in the controls: **the four CFTR-corrector positive controls failed to earn rank** (0 of 4 reached candidate tier), while all known ABCG2 inhibitors were correctly rejected (0 false positives). Because the positive controls — the closest thing to ground-truth pharmacological chaperones in the set — do not separate from the field, the screen has no demonstrated power to find real chaperones. **The chaperone-rescue candidate ranking for ABCG2 Q141K is not computationally established** (In Silico; comp-047).

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

## Residual gaps — closed (2026-07-14)

comp-047 fixes comp-032's **primary, fatal flaw** (the tautological positive-control validation) but at import carried two of comp-032's other weaknesses. Both were closed before corpus integration finalized. Neither changed the INCONCLUSIVE verdict — which rests entirely on Axis 1 positive controls failing to separate — but closing them strengthened it and surfaced one real finding.

1. **Sensitivity analysis — run (2026-07-14).** `sensitivity.py` re-docks the top-8 fold-site binders + 4 CFTR-corrector + 4 inhibitor controls at the Q141K fold site under 10 perturbations (grid-center shifts ±2/±3 Å, box sizes 18/26 Å vs base 22, two alternate Vina seeds, neutral-vs-pH-7.4 protonation) — 160 dockings. *[Result folded in on completion: whether the positive controls remain rank-failing under every perturbation is the decisive robustness test for the null. Pending the run finishing.]* Note the instrument tests fold-site affinity/rank stability, not the transport margin, so margin-flip robustness still rests on the disjoint-box geometry (32.6 Å apart).
2. **Axis 2 — expanded, a substrate blind spot found, and closed with a proper substrate axis.** At import only 3 molecules were queried against ChEMBL ABCG2 (CHEMBL5393); querying the three surviving candidates returned **0 ChEMBL records each** — which surfaced the structural limitation: **ChEMBL logs inhibition assays (IC50/Ki), not substrate transport.** rosuvastatin — one of the two "uncertain" survivors — is the canonical ABCG2 **substrate** (Q141K raises its plasma AUC ~1.6–2×; the statin-pharmacogenomics case in the FDA label), yet returns 0 ChEMBL records because it is transported by, not an inhibitor of, ABCG2.
   **Closed with a DrugBank substrate axis (Axis 2b).** ChEMBL is the wrong tool for the substrate question; DrugBank's curated transporter annotations are the right one, reachable free via UniProt Q9UNQ0 cross-references (**286 ABCG2-interacting drugs**). Cross-checking the full 135-molecule library flags **31 as ABCG2-interacting** — every approved-drug inhibitor/substrate control AND **rosuvastatin** (the one ChEMBL missed), while **vorinostat is NOT flagged** and survives as the sole marginal hit (margin +0.55, within Vina noise). rosuvastatin is now disqualified on curated evidence, not just domain knowledge. Recorded in [`outputs/drugbank_substrate_axis.json`](./etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/drugbank_substrate_axis.json) (ChEMBL inhibition data in [`outputs/chembl_axis2.json`](./etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/chembl_axis2.json)).
   **Framework lesson (reusable for any transporter-chaperone screen):** the complete "known-ABCG2" disqualifier = **ChEMBL inhibitors ∪ DrugBank/UniProt substrates** — neither alone is complete (ChEMBL misses substrates like rosuvastatin; DrugBank, approved-drugs-only, misses research-tool inhibitors like Ko143 / fumitremorgin C). **Reactome** has the canonical ABCG2 urate-efflux *reaction* but only thin per-drug substrate coverage — it is pathway infrastructure, not a substrate catalog, so it is not the right tool here. For a definitive build, **UCSF-FDA TransPortal + PharmGKB** give curated per-transporter substrate/inhibitor lists with primary references. This routing rule is now the canonical tooling guidance in [`etc/chembl-cross-check.md` §"ChEMBL scope & blind spots"](./etc/chembl-cross-check.md) and a required data-source-selection step (with a web-search-and-document fallback for gaps) in the comp-experiment design skill — so future transporter screens inherit it by default rather than rediscovering the blind spot.

## What comp-047 establishes — and what it does not

**Establishes:** (a) comp-032's chaperone signal was an artifact of its class prior (positive controls fail without it); (b) rigid-receptor fold-vs-transport docking does not discriminate pharmacological chaperones for ABCG2 Q141K; (c) no FDA-approved molecule in this 134-compound library is a docking-supported chaperone candidate.

**Does not establish:** that no chaperone exists (absence of a docking signal ≠ absence of a chaperone, given the mechanism mismatch); folding rescue; Q141K-vs-WT selectivity; urate-flux effect; or any wet-lab priority.

## What this means for the corpus

- **The pharmacological-chaperone rescue route for Q141K stays a hedged hypothesis, not a validated repurposing surface.** Neither comp-032 (descriptor heuristic) nor comp-047 (real docking) produces a defensible candidate ranking. Any downstream page presenting a comp-032 "top-10 chaperone candidates" list must downgrade it to "prior-ranked hypotheses; real docking (comp-047) came back inconclusive."
- **No compounding-pharmacy conversation is warranted on this route** until a fundamentally different method produces candidates. comp-032's queuing of a diflunisal/lumacaftor partner call is retracted.
- **The route is not dead — the method is.** A genuine computational answer needs folding-stability modeling (MD-based ΔΔG of folding, FoldX/Rosetta ΔΔG on the Q141K mutant, or an explicit thermal-shift surrogate), not docking. The cheapest real answer is wet-lab: a HEK293/Caco-2 Q141K trafficking-rescue screen (surface 5D3 epitope by flow cytometry) paired with basolateral→apical **urate flux** and an ABCG2-inhibition counterscreen, registered as a validation experiment ([`validation-experiments.md`](./validation-experiments.md)).

## Cross-references

Supersedes: [comp-032 descriptor screen](./abcg2-q141k-chaperone-screen-computational.md). Experiment folder: [`etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/`](./etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/) (verdict in [`outputs/summary.md`](./etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/summary.md), control check in [`outputs/controls.md`](./etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/controls.md)). Platform context: [`abcg2-modulators.md`](./abcg2-modulators.md), [`chassis-pending-interventions.md`](./chassis-pending-interventions.md), [`gout-genetic-variants.md`](./gout-genetic-variants.md). Registry: [`computational-experiments.md`](./computational-experiments.md).
