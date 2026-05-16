---
title: "Complestatin-Family BGC LBP-Chassis Feasibility — Computational Analysis (comp-024)"
date: 2026-05-16
tags:
  - complestatin
  - nrps
  - bgc
  - engineered-lbp
  - cp0
  - upstream-complement
  - heterologous-expression
  - computational
related:
  - computational-experiments.md
  - upstream-complement-modulator-sweep-computational.md
  - engineered-lbp-chassis.md
  - hypotheses/H05-daf-scr14-cp0-thesis.md
  - complement-c5a-gout.md
  - chassis-pending-interventions.md
sources:
  - "Chiu HT et al. PNAS 2001;98(15):8548-53 PMID 11447274 — original BGC sequencing (48.7 kb, 16 ORFs, 7 NRPS modules)"
  - "Park JW et al. ChemBioChem 2016;17(15):1442-7 PMID 27383040 — 54.5 kb cluster reconstituted in S. lividans TK24; M55/S56 P450-knockout derivatives inactive"
  - "MIBiG BGC0000326 — isocomplestatin from S. lavendulae"
  - "comp-018 — surfaced complestatin BGC as named CP0 engineering thread"
status: complete
---

# Complestatin-Family BGC LBP-Chassis Feasibility (comp-024)

**Question.** Is the complestatin NRPS BGC tractable in an LBP chassis (*E. coli* Nissle 1917, *Bacteroides thetaiotaomicron*) as the next CP0 engineering payload after H05 DAF SCR1-4?

**Verdict. RED for the LBP-track framing.** Best host (EcN) is YELLOW 0.544; *Bacteroides* RED 0.225. No host clears GREEN (≥0.60). Complestatin BGC is **not** the right next CP0 LBP payload. The **C1-INH (LBP-luminal) parallel thread scores GREEN-provisional 0.774** and is recommended as the next computational gate instead. Complestatin BGC stays in scope as an aerobic-fermentation production candidate (Streptomyces-class manufacturing), not an LBP-track payload.

## BGC summary (grep-verified)

48.7 kb (Chiu 2001) / 54.5 kb reconstituted (Park 2016); 16 ORFs; 7 NRPS modules (1 loading + 6 extension + TE) on ComA-D; tailoring = ComI/ComJ (P450 phenolic coupling), ComH (nonheme halogenase), Hmo (FMN oxidase), inferred OxyD β-hydroxylase; in-cluster Hpg pathway (HmaS/Hmo/HpgT/PD); heterologous-expression precedent = *S. lividans* TK24 only (phylum-internal); none in *E. coli*, none in *Bacteroides*. Full architecture + provenance in `experiments/comp-024-.../inputs/`.

## Method

Nine feasibility factors per host scored 0.0 → 1.0; geometric mean (right composition when every factor must succeed). Factors: cluster size, GC content (Strep ~72% vs EcN ~50.7% vs B. theta ~42.8%), non-canonical AA precursor supply, PPTase, P450 redox, O2 dependence vs. host lifestyle, toolkit maturity, expression precedent, host toxicity / self-resistance. Comparator: C1-INH on EcN as LBP-luminal payload.

## Result

| Host | Mean | Verdict | Limiting factor |
|---|---|---|---|
| *E. coli* Nissle 1917 | **0.544** | YELLOW | O2-dependent tailoring (0.30) |
| *B. thetaiotaomicron* | **0.225** | RED | P450 redox + O2 (both 0.05) |
| C1-INH on EcN (comparator) | **0.774** | GREEN (provisional) | luminal protease stability (0.35) |

## Two independent blocking mechanisms

(1) **O2-dependent tailoring chemistry.** ComI/ComJ P450 + ComH halogenase + Hmo oxidase all need molecular O2. Without P450-mediated phenolic coupling the linear peptide lacks the rigid crosslinked architecture giving complestatin C1q/C4b affinity (Park 2016 M55/S56 deletion derivatives are inactive). EcN runs anaerobic metabolism in colon lumen; *Bacteroides* is strict anaerobe. (2) **No precedent outside Actinomycetota.** Negative evidence, not proof of infeasibility, but caps engineering-confidence factor for a multi-year campaign at edge of state-of-art.

## Comparator: C1-INH (LBP-luminal) is more tractable

C1-INH wins because its dominant question (luminal-protease stability + glycosylation) is a *single-axis* problem testable with a comp-006-style protease-stability analysis on SERPING1. Complestatin's dominant question (O2-dependent tailoring in anaerobic-resident host) has no known engineering workaround. C1-INH's 0.774 is **provisional** — depends on two factors at 0.35–0.40 not yet validated. The 11-vs-9-factor apples-to-oranges caveat: restricted 7-factor C1-INH mean ~0.70, still meaningfully above complestatin's 0.544.

## Multilingual source check

No additional canonical primary literature surfaced beyond English-indexed Chiu 2001 / Park 2016 axis. Park 2016 group includes Korean authors; published in English. TCM materia medica has no entry for complestatin-class actinomycete antibiotics. No translation cross-check needed.

## Verification-agent pass

Self-reviewed as fresh-eyes reader (subagent spawning blocked per task constraints). Catches: (a) original headline framing was internally inconsistent (YELLOW headline + "do not invest" recommendation) — corrected to RED-for-LBP-track since the original question is binary; (b) C1-INH 0.774 reframed as GREEN-provisional; (c) 11-vs-9-factor caveat now documented. All reflected in `outputs/summary.md` and experiment README.

## Limitations

Factor scores are expert estimates (±0.1 robust). Module substrate specificities partly inferred from chloroeremomycin homology. β-OHTyr biosynthesis gene inferred. No Bacteroides NRPS megacluster precedent (absence of precedent ≠ infeasibility). CAI values genus-typical ±0.1. Aerobic-fermentation route out of scope (Park 2016 already showed *S. lividans* works for production).

## Impact on experimental priorities

- **Complestatin BGC as next LBP-chassis CP0 payload → dropped.** Not the right payload for this chassis class.
- **C1-INH (LBP-luminal) → promoted to next computational gate** (sister to H05; comp-006-pattern protease-stability analysis on SERPING1).
- **Complestatin BGC as aerobic-fermentation candidate → parked open** per [`chassis-pending-interventions.md`](./chassis-pending-interventions.md) pattern. Re-open as separate comp-NNN if an actinomycete-aerobic chassis track surfaces.
- **Updated CP0 stack:** primary = engineered DAF SCR1-4 (koji-secreted, §1.25); next gate = engineered C1-INH (LBP-luminal); non-engineering axis = dietary rosmarinic acid / luteolin; parked = complestatin BGC.
