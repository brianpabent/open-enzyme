---
id: H01
title: "Ward 1995 glucoamylase-KEX2 dual-cassette architecture layers uricase + lactoferrin in *A. oryzae* solid-state rice koji without silencing either or disrupting native metabolite production"
committed: 2026-04-24
status: Pending
survival_count: 0
tags:
  - hypothesis
  - koji
  - aspergillus-oryzae
  - ward-1995
  - dual-cassette
  - uricase
  - lactoferrin
  - kojic-acid
  - ergothioneine
  - feasibility-gate
  - endgame-strain
related:
  - ../koji-endgame-strain.md
  - ../engineered-koji-protocol.md
  - ../lactoferrin.md
  - ../uricase-variant-selection.md
  - ../validation-experiments.md
  - ../aspergillus-oryzae.md
  - ../linter-design.md
  - ./README.md
sources:
  - "Ward PP, Piddington CS, Cunningham GA, Zhou X, Wyatt RD, Conneely OM. Biotechnology (N Y) 1995;13(5):498-503 (PMID: 9634791)"
  - "Ward PP, Lo JY, Duke M, May GS, Headon DR, Conneely OM. Biotechnology (N Y) 1992;10(7):784-9 (PMID: 1368268)"
  - "Sun XL, Baker HM, Shewry SC, Jameson GB, Baker EN. Acta Crystallogr D Biol Crystallogr 1999;55(Pt 2):403-7 (PMID: 10089347)"
  - "Li Q, Zhang C, Li J, et al. Synth Syst Biotechnol 2024;10(2):365-372 (PMID: 39830075)"
  - "Wang S, Xue Y, Zhang P, et al. J Agric Food Chem 2023;71(41):15194-15203 (PMID: 37807677)"
  - "US Patent 5,571,697 (Conneely et al., 1996) — expired"
---

# H01 — Ward Dual-Cassette Feasibility

> **Pre-registration note.** The claim, assumption stack, and killshot menu below are frozen as of the first commit of this file (2026-04-24, git SHA TBD at commit time). Subsequent edits log in git with rationale in the commit message. See [README.md](./README.md) and [../linter-design.md](../linter-design.md) §6 for the convention.

---

## Claim

Ward's *A. awamori* glucoamylase-KEX2 dual-cassette architecture, validated for single-cassette human lactoferrin (hLf) expression at >2 g/L submerged (Ward 1995, PMID 9634791), can be layered with a second expression cassette for *A. flavus* uricase (*uaZ*) in *A. oryzae* solid-state rice koji fermentation without silencing either heterologous protein or disrupting native metabolite production (kojic acid, ergothioneine).

This is the single gating feasibility test for the [koji endgame strain](../koji-endgame-strain.md) thesis. If it passes, Year 2–3 koji development converges on one engineered strain delivering four molecules covering five NLRP3-pathway chokepoints. If it fails, the platform falls back to the two-strain co-ferment path ([koji-endgame-strain.md §4.1](../koji-endgame-strain.md)) which preserves the coverage matrix at the cost of single-strain elegance.

---

## Assumption Stack

1. **Ward 1995 results translate from *A. awamori* to *A. oryzae*.** — *load-bearing.* The two species share >99.5% coding-region identity for secretion-machinery genes (glucoamylase, KEX-2-family endoprotease, ER folding chaperones). *A. oryzae* has independently been validated as an hLf expression host at 25 mg/L in Ward 1992 (PMID 1368268) — the floor, not the ceiling — so the species-translation assumption is supported at the lower titer and extrapolated at the Ward 1995 higher titer. Evidence level: **In Vitro (Ward 1992 direct; Ward 1995 by extrapolation)**.

2. **Solid-state rice koji fermentation supports the protein-folding + secretion loads of both cassettes simultaneously.** — *load-bearing, no direct published precedent.* Ward 1995 was submerged culture with defined iron supplementation and controlled O₂/pH/feed. Solid-state rice koji has different mass transfer, different water activity, different available iron, different O₂ gradients. No published paper demonstrates dual-heterologous-protein expression in *A. oryzae* solid-state koji at g/L-scale titers. Evidence level: **Mechanistic Extrapolation**.

3. **Native *A. oryzae* proteases do not degrade the expressed uricase or lactoferrin at substrate-relevant rates.** — *load-bearing.* *A. oryzae* secretes a suite of proteases (alkaline serine [alp], neutral metallo [npr], acid-stable aspartic) as part of its starch-degrading lifestyle. Lactoferrin is moderately protease-resistant (pepsin digestion generates active lactoferricin rather than full degradation); uricase protease susceptibility in this matrix is empirically open. Protease-knockout host strains (Δalp, Δnpr) are available as a fallback but complicate the selection / integration design. Evidence level: **Mechanistic Extrapolation**.

4. **Iron-binding capacity of recombinant lactoferrin is preserved in solid-state rice conditions.** — *supporting.* Published Lf work in *Aspergillus* is submerged culture with defined Fe³⁺ supplementation (Ward 1995; Sun 1999 PMID 10089347 confirmed native fold and iron-binding at 2.2 Å resolution). Rice grain has low free iron (~1–3 ppm bioavailable); rice bran is higher but variable. Fe supplementation of the solid-state substrate (FeCl₃ or iron citrate at 10–100 ppm) is likely the workaround if native iron is insufficient, but the assumption that solid-state-produced Lf retains apo/holo-switchable iron-binding is untested. Evidence level: **In Vitro (submerged only)**.

5. **Selection markers for the two cassettes can co-exist without metabolic competition or cassette loss during propagation.** — *stylistic / routine.* pyrG (uracil biosynthesis), niaD (nitrate reductase), amdS (acetamidase), and ptrA (pyrithiamine resistance) are the standard food-grade-compatible marker set for *A. oryzae*. Pairwise combinations are routine in the filamentous-fungus literature. Cassette copy-number stability over industrial-scale propagation (~10⁹-fold expansion from master seed to production run) is a standard production-engineering question, not a scientific one. Evidence level: **In Vitro (established industrial practice)**.

6. **KEX-2 processing capacity in *A. oryzae* is sufficient for fusion-based cassettes at g/L-scale combined titer.** — *load-bearing if both cassettes use fusion architecture.* If only the lactoferrin cassette is a glucoamylase-KEX2 fusion and the uricase cassette uses direct secretion with its own signal peptide, KEX-2 capacity is non-competing. If both cassettes depend on endogenous processing peptidase, KEX-2 becomes a shared resource and the dual-cassette strain could saturate it. Published *A. oryzae* KEX-2 capacity studies are thin. Evidence level: **Mechanistic Extrapolation**.

7. **Fungal-style glycosylation of solid-state koji lactoferrin remains within the Ward 1995 submerged envelope.** — *supporting.* *Aspergillus* hLf has simpler mannose-rich N-glycans vs. native milk hLf complex sialylated/fucosylated glycans (Almond 2012 PMID 23012214). The glycosylation difference makes recombinant Lf ~40× less immunogenic and ~200× less allergenic in BALB/c mice — potentially a *feature* for chronic oral dosing. Whether solid-state fermentation further shifts glycosylation (water-activity-dependent mannosyltransferase activity is documented in other *Aspergillus* species) is empirically open. Evidence level: **Animal Model (submerged material only)**.

---

## Killshot Menu

Ranked by `score = (kill_pr × info_weight) / (cost × time_penalty)` per `linter-design.md` §4. Sorted descending. Higher score = run first.

| # | Killshot | Cost | Weeks | kill_pr | info_weight | Failure modes | Score (rel.) |
|---|---|---|---|---|---|---|---|
| 1 | **Literature/patent landscape deep-dive** on *A. oryzae* dual-heterologous-cassette expression + solid-state koji multi-protein precedent. Scope: PubMed + Google Scholar + Espacenet patent search; adjacent precedents (Wang 2023 *A. niger*, Li 2024 *A. oryzae* multi-copy same-protein). Cheapest possible upstream move — answers whether the assumption "no published precedent" is actually correct, or whether we've missed a directly-relevant paper. If a published dual-cassette *A. oryzae* precedent exists, it either validates the hypothesis cheaply or reveals a failure mode we missed. | $0 | 1 | 0.3 | 0.9 (root — tests assumption 2 and partially 1) | published-literature-gap, species-gap-translation | **HIGHEST — run first** |
| 2 | **Dual-cassette transformation + fermentation + quantified readouts.** Both cassettes integrated sequentially (Cassette A lactoferrin PamyB-glucoamylase-KEX2site-hLf-TamyB with pyrG selection; Cassette B uricase PTEF1-amyB_SP-uaZ-TgpdA with niaD selection). Solid-state rice koji 48–60 h at 30°C, 35% moisture, with submerged-culture parallel control. Readouts: uricase activity (UA-disappearance assay), Lf titer (ELISA + Western), iron-binding (UV-Vis 465 nm), native metabolite panel (kojic acid HPLC, ergothioneine LC-MS), qPCR for cassette copy numbers, SDS-PAGE for truncated/unprocessed species. This is the full §3.4 protocol from [koji-endgame-strain.md](../koji-endgame-strain.md). | $5,000 | 12 | 0.5 | 1.0 (root — directly tests the claim) | expression/localization-mismatch, kinetics/concentration, assay-specificity | High |
| 3 | **Single-cassette uricase-only control in *A. oryzae* RIB40 solid-state rice koji.** Tests whether uricase expresses in solid-state format at all, independent of the dual-cassette question. If single-cassette uricase in solid-state koji is already <50 mg/g, the dual-cassette target is off before Ward layering even starts. This is the Year 1 starting strain per [engineered-koji-protocol.md](../engineered-koji-protocol.md) and doubles as a killshot for the endgame hypothesis. | $2,000 | 8 | 0.1 | 0.4 (leaf — tests subset of assumption 2) | expression/localization-mismatch, substrate-availability | Medium |
| 4 | **Native metabolite panel pre/post engineering.** Parallel WT-vs-engineered kojic-acid and ergothioneine titer comparison. If either drops >50% when the two heterologous cassettes are added, the native-metabolite-preservation component of the claim is killed even if the heterologous proteins express fine. This readout overlaps with killshot 2 but is separable — it can be run on a simpler single-cassette intermediate first. | $1,000 | 2 | 0.15 | 0.5 (midstream — tests claim's "without disrupting native metabolite production" clause) | substrate-availability, expression/localization-mismatch | Medium |
| 5 | **Iron-binding functional assay on expressed lactoferrin.** UV-Vis at 465 nm for apo-vs-holo ratio; optional CD spectroscopy for fold confirmation; pH-dependent iron release kinetics. Tests assumption 4 directly. If recombinant solid-state-produced Lf has lost iron-binding, the CP1b (Fenton ROS) mechanism from [koji-endgame-strain.md §2.2](../koji-endgame-strain.md) is compromised, though CP4 and CP6b mitophagy mechanisms may survive. Not a full kill of H01 (the cassette still expresses) but a significant narrowing of the Lf functional claim. | $500 | 2 | 0.2 | 0.3 (leaf — tests assumption 4 only) | expression/localization-mismatch, assay-specificity | Medium-low |

*(Scores are qualitative for v0. Numeric scoring with decay and independence weighting is future work per `linter-design.md` §6.)*

**Sequencing logic.** Run #1 first unconditionally — it's free and tests the literature-gap assumption that several other killshots presume. If #1 surfaces a published precedent (positive: validates; negative: reveals a mode we missed), reshuffle the menu. #3 and #4 can run in parallel with or before #2 as lower-risk intermediate steps — they de-risk #2's larger spend. #5 is a targeted narrowing move that matters most if #2 returns ambiguous Lf-function data.

---

## Failure-Mode Ontology Reference

Tagged modes drawn from [linter-design.md §5](../linter-design.md):

- **published-literature-gap / training-distribution.** The claim rests on a Ward 1995 precedent that's single-protein, submerged, in a different *Aspergillus* species. Killshot 1 probes this directly.
- **species-gap translation.** *A. awamori* → *A. oryzae* (assumption 1). Killshot 1 partially; killshot 2 fully.
- **expression / localization mismatch.** The cassettes integrate but the proteins aren't secreted, folded, or processed. Killshots 2, 3, 5.
- **kinetics / concentration mismatch.** The proteins express but at titers too low for the intended dose (2–3 g/day Lf at 10–15 g/day koji). Killshots 2, 3.
- **assay specificity.** ELISA cross-reactivity with native *Aspergillus* proteins; UA-disappearance interference from native urate-relevant enzymes. Killshots 2, 5.
- **substrate availability / compartment mismatch.** Iron for Lf folding; starch for amyB induction; N source for uricase constitutive expression. Killshots 4, 5.

Two killshots share a failure-mode vector only if the overlap is load-bearing. Killshots 2 and 3 overlap on `expression/localization-mismatch` but #3 is single-cassette while #2 is dual — they probe different sub-modes of the same family. Independence is imperfect but non-zero; roughly 0.4–0.6 Jaccard on failure-mode vectors.

---

## Pre-Committed Thresholds

Declared before any killshot executes. These are the lines in the sand.

### Alive

Dual-cassette *A. oryzae* strain in solid-state rice koji (48–60 h, 30°C, 35% moisture) produces:

- **Uricase:** ≥50 μmol/h/OD (equivalent to ≥100 mg/L pore-fluid / ≥10 mg/g dry koji at industrial ratios — matches ALLN-346 clinical dosing floor)
- **Lactoferrin:** ≥500 mg/L pore-fluid equivalent (or ≥50 mg/g dry koji — the Phase B floor per [koji-endgame-strain.md §3.4](../koji-endgame-strain.md))
- **Native kojic acid:** within 30% of WT titer (WT baseline 3–5 g/L per [aspergillus-oryzae.md](../aspergillus-oryzae.md); floor 2.1 g/L)
- **Native ergothioneine:** within 30% of WT titer (WT baseline ~20 mg/g dry mycelium; floor 14 mg/g)
- **Lactoferrin iron-binding:** ≥40% of submerged-culture reference per UV-Vis 465 nm

### Killed

Any one of the following:

- Either heterologous protein undetectable (uricase <10 mg/L, or Lf <100 mg/L pore-fluid equivalent) after two rounds of cassette/host optimization
- Native kojic acid or ergothioneine drops >50% from WT baseline and does not recover under iron / N supplementation
- Lactoferrin iron-binding <20% of submerged reference (indicates fold collapse, not just titer weakness)

### Pending / Ambiguous

Intermediate outcomes that cross neither threshold:

- Uricase 10–100 mg/L, Lf 100–500 mg/L (expression works but titers are Phase C rather than Phase B)
- Native metabolite drop 30–50% (recoverable with media optimization, not yet disqualifying)
- Iron-binding 20–40% (fold is partially compromised but not lost)

Document explicitly; propose single-variable follow-up experiments per [linter-design.md §7](../linter-design.md) rather than calling Alive or Killed prematurely.

---

## Kill Switches

Sanity / safety stops independent of the scientific thresholds.

1. **Aflatoxin elevation.** *A. oryzae* is GRAS and non-aflatoxigenic (the *aflR* regulator is cryptic / truncated), but engineered strains can drift. If aflatoxin (B1, B2, G1, G2) is detected above regulatory limit (20 ppb total in food matrices) at any point, halt the experiment and re-evaluate. Food-grade status is non-negotiable.
2. **Spore morphology drift.** If sporulation fails or produces aberrant morphology (a sign of stress, marker instability, or major metabolic disruption), halt and return to single-cassette or WT baseline for diagnosis.
3. **Host strain drift.** If qPCR indicates cassette loss >10% over three serial passages, the strain is unstable; halt and redesign integration strategy.
4. **Budget overrun.** Hard cap at $7,500 total spend across killshots 1–5 before re-evaluating the whole program. The cheap-first sequencing is designed to surface go/no-go signal within the first $3,000.

---

## Failure Modes Probed (Coverage Map)

Which failure modes does the killshot menu actually cover?

| Failure mode | Probed by | Coverage |
|---|---|---|
| published-literature-gap | K1 | Full |
| species-gap-translation | K1 (partial), K2 (full) | Full |
| expression / localization | K2, K3, K5 | Full |
| kinetics / concentration | K2, K3 | Full |
| assay specificity | K2, K5 | Partial (ELISA cross-reactivity not separately orthogonalized) |
| substrate availability | K4, K5 | Partial (iron tested via K5; N / starch not separately) |
| chokepoint collapse | — | Not applicable (H01 is an engineering-feasibility claim, not a therapeutic-mechanism claim) |
| dose-translation scaling | — | Not applicable until the therapeutic-use hypothesis H0N (future) is committed |

Coverage gaps are acceptable — H01 is a feasibility-gate hypothesis, not a mechanism claim. The therapeutic-efficacy hypothesis ("dual-cassette koji at dose X produces biomarker change Y in a gout n=1 protocol") is a separate future H0N with its own card.

---

## Status

**Pending.** No killshot executed as of the committed date (2026-04-24).

**Survival count:** 0.

**Survival score:** 0.0 (undefined until first survived killshot).

---

## Log

| Date | Killshot | Outcome | Notes |
|---|---|---|---|
| — | — | — | (empty — no executions yet) |

---

## Retraction History

None.

---

## Cross-References

- [koji-endgame-strain.md](../koji-endgame-strain.md) — the platform-thesis page this hypothesis gates. §3 (Ward 1995 architecture layering), §3.4 (protocol sketch), §4 (fallback paths if H01 is killed).
- [engineered-koji-protocol.md](../engineered-koji-protocol.md) §16 — the single-cassette lactoferrin co-expression module this hypothesis ladders on top of. Also §02–14 (Year 1 uricase-only starting strain, which is killshot 3 reframed as a standalone deliverable).
- [lactoferrin.md](../lactoferrin.md) — full dossier for the Lf side of the dual cassette; §7 discusses the Open Enzyme feasibility bet.
- [uricase-variant-selection.md](../uricase-variant-selection.md) — source-gene analysis (*A. flavus uaZ* primary, *C. utilis* secondary).
- [validation-experiments.md](../validation-experiments.md) §1.9 — the experiment-queue entry for this feasibility test; this hypothesis is the formalization of that entry.
- [aspergillus-oryzae.md](../aspergillus-oryzae.md) — host biology, native kojic acid + ergothioneine baselines.
- [linter-design.md](../linter-design.md) — schema and rationale for the Falsification Card format used here.

---

*This is the seed hypothesis for the `wiki/hypotheses/` directory. The Falsification Card format will be refined as subsequent hypotheses are committed; deviations from this template should be justified in the new hypothesis's commit message and, if structural, propagated back to `linter-design.md` §4.*
