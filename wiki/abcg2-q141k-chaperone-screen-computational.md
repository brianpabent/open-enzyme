---
title: "ABCG2 Q141K Pharmacological-Chaperone Virtual Screen — Computational Analysis (comp-032)"
date: 2026-05-16
tags:
  - abcg2
  - q141k
  - pharmacological-chaperone
  - cftr-corrector
  - virtual-screen
  - drug-repurposing
  - compounding-pharmacy
  - computational-experiment
related:
  - abcg2-modulators.md
  - chassis-pending-interventions.md
  - compounding-pharmacy-track.md
  - gout-genetic-variants.md
  - purine-degrading-bacteria.md
  - computational-experiments.md
sources:
  - "UniProt Q9UNQ0 (ABCG2_HUMAN) — feature table 2026-05-16: NBD aa 37-286, Q141K rs2231142 VARIANT note (high serum UA, gout association, decreased protein abundance)"
  - "AlphaFold AF-Q9UNQ0-F1-model_v6 (EMBL-EBI, 2026-05-16): WT ABCG2 monomer; Q141 pLDDT 97.06"
  - "Basseville et al. 2012 Cancer Research PMID 22472121 (HDAC-inhibitor rescue of Q141K-ABCG2 trafficking; mechanistic precedent for the chaperone class)"
  - "Van Goor et al. 2011 / 2014 (CFTR corrector class — ivacaftor/tezacaftor/elexacaftor; ABC-superfamily corrector precedent)"
---

# ABCG2 Q141K Pharmacological-Chaperone Virtual Screen (comp-032)

> **⚠️ SUPERSEDED — do not cite the GREEN verdict or the candidate list below as support (comp-review 2026-07-13 + comp-047 2026-07-14).** The 2026-07-13 independent audit found comp-032's "positive-control pass" is **tautological**: CFTR correctors ranked high only because they were *assigned* the maximum drug-class prior (1.00), not because the heuristic detected chaperone binding (decoy max 0.684 = 0.15^(1/5), a formula artifact). It does no docking, no Q141K side-chain modeling, no chaperone-vs-inhibitor discrimination, no sensitivity analysis; ABCG2 *inhibitors* (the opposite of what we want) score high. **[comp-047](./abcg2-q141k-chaperone-rescreen-computational.md) re-ran the screen with real AutoDock Vina docking and no class prior, and the CFTR-corrector positive controls failed to earn rank — INCONCLUSIVE.** The chaperone-rescue candidate ranking for Q141K is **not computationally established**. Everything below is retained as the frozen historical record; treat the GREEN verdict, the top-10 list, and the compounding-pharmacy queuing as **retracted**. See [comp-047](./abcg2-q141k-chaperone-rescreen-computational.md) for the current state.

**Question.** Does the FDA-approved drug surface contain a small molecule that binds Q141K ABCG2's nucleotide-binding domain (NBD) and could rescue trafficking from the ER aggresome to the apical brush border? Or does the surface lack chaperone-active hits, requiring novel chemistry?

**Verdict: ~~GREEN~~ RETRACTED → superseded by [comp-047](./abcg2-q141k-chaperone-rescreen-computational.md) (INCONCLUSIVE).** *(Historical claim, retained for the record:)* Shortlist of 10 candidates passes the four-gate filter (heuristic composite >= 0.75, chaperone-compatible drug class, 503A-eligible-or-chaperone-class, oral bioavailable). All four CFTR-corrector positive controls (lumacaftor, tezacaftor, ivacaftor, elexacaftor) rank in the top 11% of the 134-molecule library, all above the highest-scoring decoy.

**Why this matters.** [`chassis-pending-interventions.md` §7](./chassis-pending-interventions.md) named pharmacological chaperones as an orthogonal small-molecule rescue route for Q141K (the #1 gout-risk GWAS variant), with the CFTR-corrector class as the precedent. comp-032 is the cheap-first move that bounds the question: is this a repurposing surface, or does the chokepoint need novel chemistry? Empty shortlist would have dropped the repurposing thesis. The actual result — a class-diverse shortlist of 10, with three mechanistically-distinct chemistry classes scoring >= 0.85 — supports the repurposing thesis at heuristic resolution and queues real-docking re-screen + HEK293-Q141K trafficking assay as the next steps.

**Method (in one paragraph).** Stdlib-only descriptor-based heuristic — NOT real AutoDock Vina docking. Five score components, geometric-mean-aggregated: Lipinski oral-druggability fit, pocket-charge complementarity against the Q141K +1 NBD pocket, MW/ring-count volume fit, drug-class chaperone prior (CFTR class = 1.00, misfolded-chaperone = 0.80, decoy = 0.15), HBA/HBD/rotbond pose-stability proxy. Pocket descriptor built from the AlphaFold WT model: 21 residues within 10 Å of Q141 CA, mean pLDDT 95.6, WT charge +3 / Q141K charge +4. The Q141 chaperone site sits 28 Å from Walker A and 16 Å from ATP loop 2 — distinct from the ATP-binding pocket, which is the right profile for a chaperone (binds without competing with ATP). Library: 134 hand-curated molecules covering CFTR correctors, chemical chaperones, iminosugar chaperones, Hsp modulators, ABC inhibitors/substrates, plus ~75 decoy molecules across unrelated classes for positive-control statistics.

**Top 3-5 candidates (class-diverse).**

| Rank | Name | Drug class | Composite | 503A tier | Mechanism rationale |
|---|---|---|---|---|---|
| 1 | lumacaftor | CFTR corrector | 1.000 | Tier 2 | Same ABC superfamily as the target; F508del-CFTR corrector with NBD/TMD-interface binding — strongest mechanistic prior |
| 2 | tafamidis | TTR tetramer stabilizer | 0.956 | Tier 2 | Aromatic-acid stabilizer of misfolded protein at a hydrophobic interface; analogous binding-site geometry |
| 3 | ursodiol | Bile acid chaperone (UDCA) | 0.956 | Tier 1 | Broad ER-stress chaperone via ATF6/Hsp70; documented F508del-CFTR rescue precedent |
| 4 | diflunisal | TTR stabilizer (NSAID, off-label ATTR) | 0.950 | Tier 1 | Anionic at pH 7.4 → strong electrostatic match for Q141K +1 pocket |
| 5 | TUDCA | Bile acid chaperone | 0.934 | Tier 2 | F508del-CFTR rescue precedent + ALS clinical trial data; CNS-penetrant |

**~~Positive-control validation passed.~~ RETRACTED — tautological.** *(Historical claim:)* All four CFTR correctors rank above the highest-scoring decoy (decoy max 0.684 < lowest control 0.829 elexacaftor). **This is not independent validation:** the decoy max 0.684 = 0.15^(1/5) is a direct consequence of the hard-coded decoy class prior (0.15), so "controls beat decoys" is built into the scoring, not learned from pocket fit. When [comp-047](./abcg2-q141k-chaperone-rescreen-computational.md) removed the prior and made the same controls earn rank from real docking, **all four failed** — the chaperone signal was the prior all along.

**Cross-validation correction (2026-07-13).** The heuristic elevates sodium butyrate and vorinostat, but Basseville 2012 directly anchors the pharmacological rescue class—not sodium butyrate. Ranking butyrate is hypothesis generation, not independent biological corroboration; it requires direct trafficking and urate-flux testing.

**Limitations.** (1) Heuristic ≠ real docking; no 3D pose, no co-crystal-trained scoring — every shortlisted molecule needs AutoDock Vina or DiffDock re-screen before wet-lab. (2) Library 134 << full DrugBank ~3,800 approved; the screen does not exhaustively cover the FDA-approved surface. (3) Q141K mutant structure is INFERRED from WT AlphaFold + +1 charge perturbation, not independently predicted — does not capture Q141K-induced conformational reorganization. (4) No membrane / homodimer context (ABCG2 functions as a homodimer in the lipid bilayer). (5) Q141K-vs-WT selectivity NOT tested by this heuristic — a real chaperone needs to bind selectively to the misfolded variant; equal binding to WT is bad. (6) The CFTR-corrector mechanism is at the TMD/NBD interface, not pure-NBD; this NBD-centric pocket may miss the true ABC-corrector binding mode. Full limitations list in [`etc/experiments/comp-032-abcg2-q141k-chaperone-screen/outputs/summary.md`](./etc/experiments/comp-032-abcg2-q141k-chaperone-screen/outputs/summary.md).

**Impact on experimental priorities.** This is a GREEN that warrants escalation, not a clinical-candidate verdict. Next steps: (a) real-docking re-screen of the top 10 against the ABCG2 NBD pocket on Colab GPU (~$0-100); (b) HEK293-Q141K transfectant trafficking-rescue assay on top 3 — lumacaftor, tafamidis, ursodiol — via flow cytometry against the extracellular 5D3 epitope (~$8-15K); (c) preliminary compounding-pharmacy partner conversation for the top 3, with diflunisal (Tier 1, off-patent NSAID) the lowest-friction first call. ~~The repurposing-surface thesis for this target is empirically supported; pivot to AI-aided novel binder design (RFdiffusion) is NOT triggered.~~ **RETRACTED:** the repurposing surface is **not** empirically supported — [comp-047](./abcg2-q141k-chaperone-rescreen-computational.md)'s real-docking rescreen was INCONCLUSIVE (positive controls failed to earn rank). Rigid-receptor docking cannot discriminate chaperones here (mechanism mismatch); the real next step is folding-ΔΔG modeling (MD / Rosetta) or a wet-lab Q141K trafficking + urate-flux assay, not another docking pass.

**Cross-references.** Experiment folder: [`etc/experiments/comp-032-abcg2-q141k-chaperone-screen/`](./etc/experiments/comp-032-abcg2-q141k-chaperone-screen/). Platform context: [`abcg2-modulators.md` §"Pharmacological-chaperone route"](./abcg2-modulators.md) and [`chassis-pending-interventions.md` §7](./chassis-pending-interventions.md). Delivery route: [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md). Orthogonal HDAC/butyrate rescue track: [`purine-degrading-bacteria.md`](./purine-degrading-bacteria.md).
