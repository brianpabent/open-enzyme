---
title: "Does EcN Periplasmic Disulfide-Folding Scale to DAF SCR1-4 (8) and Lactoferrin (16)? — Computational Analysis (comp-043)"
date: 2026-07-13
tags: [complement, C1-INH, DAF, CD55, lactoferrin, disulfide, DsbA, DsbC, EcN, E-coli-Nissle, LBP, chaperone, protease, glycosylation, computational, alphafold, two-chassis, folding-feasibility]
related:
  - c1-inh-protease-stability-ecn-computational.md
  - daf-cd55-scr14-truncated-computational.md
  - daf-cd55-protease-stability-computational.md
  - lactoferrin-protease-stability-computational.md
  - chaperone-orthogonal-stacking.md
  - engineered-lbp-chassis.md
  - complement-c5a-gout.md
  - computational-experiments.md
  - validation-experiments.md
sources:
  - "UniProt P05155 (C1-INH / SERPING1, 2 disulfides — grep-verified)"
  - "UniProt P08174 (DAF / CD55, 8 disulfides in SCR1-4 — grep-verified)"
  - "UniProt P02788 (human lactoferrin / LTF, 16 disulfides — grep-verified)"
  - "AlphaFold AF-P05155-F1 / AF-P08174-F1 / AF-P02788-F1 (model_v6, EMBL-EBI)"
  - "chaperone-orthogonal-stacking.md §8 item 8 (no published DsbA/DsbC capacity metric at 8-16 disulfide scale)"
  - "Ward 1995 (>2 g/L lactoferrin in A. awamori); Sun 1999 PMID 10089347 (A. awamori hLf native fold)"
  - "MEROPS 12.4; Dekker 2001 PMID 11226160 (OmpT); Krojer 2008 PMID 18261546 (DegP)"
status: complete
---

# Does EcN Periplasmic Disulfide-Folding Scale to DAF SCR1-4 (8) and Lactoferrin (16)? — Computational Analysis (comp-043)

> **Reproducible analysis at [`./etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/`](./etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/)** (`analyze.py` stdlib-only + `inputs/` w/ provenance + `outputs/results.json` + `outputs/summary.md` + `README.md`).
> This wiki page is the interpretive summary; the code + frozen artifacts live next to the experiment.

**Status:** Complete — 2026-07-13 **Evidence level:** Mechanistic Extrapolation — AlphaFold pLDDT-based structural inference + literature-grounded folding-capacity reasoning; no wet-lab confirmation.

**Sister analyses:** [comp-037 (C1-INH on EcN, MODERATE)](./c1-inh-protease-stability-ecn-computational.md) · [comp-012 (DAF SCR1-4 on koji, LOW)](./daf-cd55-scr14-truncated-computational.md) · [comp-006 (DAF full ectodomain on koji, HIGH)](./daf-cd55-protease-stability-computational.md) · [comp-005 (lactoferrin on koji, HIGH/MODERATE)](./lactoferrin-protease-stability-computational.md)

---

## Question

comp-037 showed EcN's periplasmic DsbA/DsbC disulfide-folding machinery can plausibly fold **C1-INH (2 disulfides)** as a gut-luminal-secreted LBP payload. A synthesis card then overreached:

> *"so EcN is superior to koji for PDI-heavy payloads like DAF SCR1-4 (8 disulfides) and lactoferrin (16 disulfides)."*

**That leap is untested.** This experiment asks: does EcN's periplasmic disulfide-folding + colonic-luminal protease survival actually *scale* with disulfide count — from C1-INH (2) to DAF SCR1-4 (8) to lactoferrin (16) — and where, by disulfide count, does EcN stop being a plausible chassis?

**This is explicitly NOT a genome-scale metabolic model (GEM).** A GEM models metabolic flux, not folding-machinery competition — the wrong tool, and precisely the card's category error. This is a [comp-006](./daf-cd55-protease-stability-computational.md) / [comp-037](./c1-inh-protease-stability-ecn-computational.md)-style structural + sequence folding-feasibility analysis: disulfide connectivity/count, AlphaFold pLDDT-based protease-exposure scoring, and a literature-grounded assessment of DsbA/DsbC oxidative-folding capacity vs. disulfide scale — composited across three orthogonal axes.

---

## Headline verdict

**A relative ranking with the crossover sitting exactly at DAF SCR1-4 — not a false-precision "GREEN."**

| Payload | Disulfides | Fold | Composite verdict |
|---|---|---|---|
| **C1-INH** (serpin) | **2** | metastable serpin | **VIABLE** (disulfide axis) — folding not the gate; comp-037's kinetic-competition caveat still governs overall |
| **DAF SCR1-4** (CCP/sushi) | **8** | 4 compact β-sandwich modules | **PROVISIONAL** — folding-capacity-gated |
| **Lactoferrin** (transferrin-lobe) | **16** | bilobal, long-range C-lobe bonds | **NOT-VIABLE** — folding-limited across the entire plausible capacity band |

**The plausible-to-not-plausible crossover sits at DAF SCR1-4 (8 disulfides).** EcN's periplasmic DsbA/DsbC folding is plausible for C1-INH (2), capacity-gated/provisional for DAF SCR1-4 (8), and not plausible for lactoferrin (16). The *exact* location of the crossover is set by the one parameter nobody has measured — the DsbA/DsbC oxidative-folding capacity at 8-16 disulfide scale.

---

## The single biggest unresolved question (load-bearing honesty)

Per [`chaperone-orthogonal-stacking.md` §8 item 8](./chaperone-orthogonal-stacking.md), **no published DsbA/DsbC capacity metric exists at the 8-16 disulfide scale.** So the folding-capacity axis is an *inference from E. coli periplasmic-expression precedent, not a measurement.* The reference-capacity band is the single biggest optimistic assumption in this analysis, and it is why DAF SCR1-4 is **PROVISIONAL**, not GREEN. The band is anchored to precedent and sensitivity-tested:

| Anchor | Capacity (effective-demand units) | Precedent |
|---|---|---|
| Conservative | 5.0 | Certolizumab pegol (Cimzia) Fab' — industrially secreted in near-WT *E. coli* periplasm, ~5 disulfides |
| Moderate | 8.0 | Fab-class precedent + DsbC-isomerase co-expression credit |
| Optimistic | 12.0 | Engineered oxidizing strain (SHuffle *trxB/gor* + cytoplasmic DsbC); set *below* full-IgG's 16 |

The optimistic anchor carries its own caveat: SHuffle forms disulfides in the **cytoplasm**, and a cytoplasmically-folded protein does not route through the Sec → periplasm → outer-membrane luminal-secretion path an LBP payload needs. So for a *secreted* format the realistic ceiling is nearer the conservative/moderate anchors — which pushes DAF SCR1-4 toward the folding-limited end of its band.

---

## The three orthogonal axes

The composite is a **limiting-factor (Liebig's-law) gate**: folding must succeed first; if the disulfide-folding axis fails, protease and glycosylation are moot. This mirrors [comp-008](./f-prausnitzii-heterologous-expression-computational.md)'s "chemistry can't run" gate (uricase needs O₂; an obligate anaerobe can't supply it).

### Axis 1 — Disulfide-folding burden vs. DsbA/DsbC capacity

Raw disulfide count is not the right burden metric. **Connectivity is.** DsbA introduces disulfides vectorially as the chain emerges into the periplasm; short-range bonds form correctly with DsbA alone. Two features raise the DsbC-isomerase-limited burden: **long sequence separation** (the chain must be translocated and held until the distal Cys appears) and **interleaved/knotted topology** (mispairing-prone). The metric is an architecture-weighted "effective folding demand":

| Payload | SS count | max loop | long-range bonds (>150) | topological crossings | eff. demand (loop + crossing) | folding-nonviability @ cons/mod/opt |
|---|---|---|---|---|---|---|
| C1-INH | 2 | 305 | 1 | 0 | **4.0** (4.0 + 0.0) | 0.3 / 0.0 / 0.0 → **PLAUSIBLE** |
| DAF SCR1-4 | 8 | 47 | 0 | 4 | **10.0** (8.0 + 2.0) | 1.0 / 0.5 / 0.33 → **EDGE (straddles)** |
| Lactoferrin | 16 | 281 | 3 | 4 | **23.5** (21.5 + 2.0) | 1.0 / 1.0 / 1.0 → **LIMITED** |

Reading it:

- **C1-INH (demand 4.0)** stays plausible across the whole capacity band. Its two bonds include one long-range (C123-C428, L=305), but *only two bonds total* — low absolute isomerization load.
- **DAF SCR1-4 (demand 10.0)** straddles the band — plausible only at the optimistic (compartment-mismatched) anchor, limited at the conservative anchor. Its burden is *topological*, not long-range: the canonical sushi Cys1-Cys3 / Cys2-Cys4 pattern is 4 interleaved pairs (crossings), which DsbC exists to resolve. **Caveat:** koji's framework rates this fold α = 0.3-0.6 ("CCP folds fast"), but that is *eukaryotic PDI* (Schmidt 2010) and does not transfer as reassurance for a bacterial oxidase.
- **Lactoferrin (demand 23.5)** is folding-limited even at the optimistic anchor. Its three C-lobe-spanning long-range bonds (424-705, 446-668, 502-696) are the transferrin-fold hierarchical-folding signature (molten-globule intermediate; only 4 of 32 cysteines seed the cascade — Notari 2023, via [`chaperone-orthogonal-stacking.md` §3.5.1](./chaperone-orthogonal-stacking.md)) — exactly what a periplasmic oxidase is poorly suited to fold.

### Axis 2 — Strictly-degradative colonic-luminal protease exposure

AlphaFold pLDDT-based cleavage scan (shared `lib/protease_stability.py`, five-protease colonic-EcN panel) on each payload's folded-core region:

| Payload | Folded core (aa) | Max risk | Worst protease | Verdict |
|---|---|---|---|---|
| C1-INH (serpin core, RCL excluded) | 123-500 | 0.10 | OmpT | **LOW** |
| DAF SCR1-4 | 35-285 | 0.10 | OmpT | **LOW** |
| Lactoferrin (mature) | 20-710 | 1.00 | OmpT | **RED** |

C1-INH and DAF SCR1-4 are compact, disulfide-locked, and protease-resistant once folded (both reproduce their koji-track LOW verdicts under the colonic panel). Lactoferrin scores RED — driven by its exposed N-terminal poly-Arg (the lactoferricin **GRRRR** cluster, an OmpT di-basic magnet) plus surface loops. **But protease exposure is a secondary axis and moot for lactoferrin — its folding fails first.**

### Axis 3 — Glycosylation dependence for FUNCTION

EcN cannot glycosylate. The question is not *"is it glycosylated"* (all three are) but *"does loss of glycans abolish therapeutic function in a gut-luminal format?"*

| Payload | N-glyc sites | Class | Kills function in EcN? |
|---|---|---|---|
| C1-INH | 7 | not required | No — serpin suicide mechanism is polypeptide-encoded; N-glycans are for plasma half-life (irrelevant luminally) |
| DAF SCR1-4 | 1 (N95) | aids, not required | No — decay-acceleration is a protein-protein interaction (SCR2-4 bind C3b/C4b) |
| Lactoferrin | 3 | aids, not required | No — iron-binding + lactoferricin are polypeptide-encoded; non-native fungal glycans tolerated (Sun 1999) |

**Key honest finding:** glycosylation-dependence does **not** independently kill DAF or lactoferrin function in EcN. Over-attributing the lactoferrin problem to glycosylation would be a mechanism error — the dominant filter is Axis 1 (disulfide folding). In EcN the absent glycans *compound* the lactoferrin folding/protease problem (they normally add protease resistance); they do not *cause* it.

---

## Does this support or refute the card's claim?

**REFUTED as stated.** The blanket "EcN superior to koji for PDI-heavy payloads like DAF SCR1-4 (8) and lactoferrin (16)" does not survive a head-to-head:

1. **EcN does not scale to lactoferrin (16 disulfides).** Folding-limited across the entire capacity band — bilobal transferrin fold with C-lobe-spanning long-range bonds.
2. **EcN's DAF SCR1-4 (8 disulfides) is provisional, not superior.** Capacity-gated on an unmeasured parameter, and leaning conservative once the compartment-mismatched optimistic anchor is discounted.
3. **Koji is not dominated.** Koji (eukaryotic ER + PDI/ERO1 + glycosylation) folds DAF SCR1-4 at LOW protease risk ([comp-012](./daf-cd55-scr14-truncated-computational.md); effective PDI load 2.4-4.8, well under the Huynh-16 reference — [`chaperone-orthogonal-stacking.md` §3.5.3](./chaperone-orthogonal-stacking.md)) and has a **>2 g/L lactoferrin precedent** (Ward 1995, *A. awamori* — a sister species of *A. oryzae* koji; native fold confirmed, Sun 1999). Koji is the *better-characterized* chassis for both PDI-heavy payloads.

### The bounded thesis (how it should read)

> EcN's periplasmic DsbA/DsbC folding plausibly extends to **low-to-moderate disulfide, compact-fold, glycosylation-independent** payloads — **C1-INH (2 disulfides, VIABLE on the disulfide axis)** and **DAF SCR1-4 (8 disulfides, PROVISIONAL, CCP/sushi fold)**. It does **not** plausibly scale to **lactoferrin (16 disulfides, bilobal transferrin fold)**. EcN is therefore a plausible *alternative* chassis for low/moderate-disulfide complement regulators (the two-chassis CP0 architecture stands), **not** a chassis that dominates koji for PDI-heavy payloads — and it is inferior to koji for lactoferrin specifically.

This is consistent with the existing two-chassis framing: [comp-037](./c1-inh-protease-stability-ecn-computational.md) put **C1-INH on EcN** at classical/lectin entry, and [comp-012](./daf-cd55-scr14-truncated-computational.md) put **DAF SCR1-4 on koji** at surface convertase decay. comp-043's contribution is to show the *chassis assignment matters and does not invert*: DAF SCR1-4 could go on EcN (provisionally), but lactoferrin cannot — it belongs on koji.

---

## Limitations

- **Axis 1 scores disulfide formation/isomerization burden, NOT native-fold attainment.** Disulfides are necessary, not sufficient. Serpin metastability (C1-INH) and the transferrin molten-globule folding hierarchy (lactoferrin) are additional *unmodeled* attainment risks. Recombinant C1-INH is manufactured in mammalian/milk systems, not *E. coli*, precisely because bacterial serpin-fold attainment is unreliable — so the C1-INH "VIABLE" verdict is strictly a *disulfide-axis* statement, not a claim that EcN will attain the native serpin fold.
- **The reference DsbA/DsbC capacity band is an inference, not a measurement** (no published metric at 8-16 disulfide scale). This is the biggest assumption and the reason DAF SCR1-4 is provisional.
- **The optimistic (SHuffle) anchor is compartment-mismatched** with the luminal-secreted format (cytoplasmic disulfide formation ≠ secretory pathway). The realistic ceiling for a secreted payload is nearer the conservative/moderate anchors, biasing the honest read conservative for DAF.
- **pLDDT ≠ solvent accessibility.** Per [comp-034](./lactoferrin-linker-redesign-computational.md), the burial proxy under-counts SASA-exposed helical/linker sites ~10× (the lactoferrin inter-lobe linker specifically). Axis 2 max risks are point estimates on a proxy.
- **Loop-length weighting (1.0/1.5/2.5) + per-crossing surcharge (0.5) are transparent monotone proxies** for DsbC isomerization demand, not measured k_cat values.
- **Interleaved-connectivity term is coarse.** It counts topological crossings equally regardless of loop size; a per-domain isomerization model would refine DAF's demand.
- **Secretion topology (Sec/YebF/Type I), colonic commensal-microbiome protease load, and bile-acid unfolding are out-of-model.**
- **Predicts folding FEASIBILITY, not titer or in vivo efficacy.** A VIABLE/PROVISIONAL verdict is a wet-lab prior, not a demonstrated result.

---

## Impact on experimental priorities

- **Does not create a new wet-lab gate; it reallocates chassis assignment and sets a measurement priority.** The card's implied action ("move DAF + lactoferrin to EcN because it's superior") is withdrawn. DAF SCR1-4 stays primarily on koji ([§1.25 validation-experiments](./validation-experiments.md), [comp-012](./daf-cd55-scr14-truncated-computational.md)); EcN is a provisional secondary route for DAF only. **Lactoferrin should not be routed to EcN** — koji is the demonstrated chassis.
- **Names the highest-leverage missing measurement:** a DsbA/DsbC oxidative-folding capacity assay at 8-16 disulfide scale (or a direct EcN-periplasm disulfide-isomerization-rate measurement). Until it exists, any EcN-DAF-SCR1-4 folding claim is provisional. This is the EcN-side analogue of the koji-side α-coefficient calibration gap ([`chaperone-orthogonal-stacking.md` §3.5.4](./chaperone-orthogonal-stacking.md)).
- **If DAF SCR1-4 is ever expressed in EcN,** run it in a DsbC-co-expression strain and read fold quality (non-reducing vs reducing SDS-PAGE + decay-accelerating activity), not just secretion — the interleaved sushi topology is the risk, and secretion alone would not confirm correct pairing.

---

## Cross-references

- [`c1-inh-protease-stability-ecn-computational.md`](./c1-inh-protease-stability-ecn-computational.md) — comp-037, the 2-disulfide EcN precedent this analysis extends (and the card that overreached from it)
- [`daf-cd55-scr14-truncated-computational.md`](./daf-cd55-scr14-truncated-computational.md) — comp-012, DAF SCR1-4 on koji (LOW); the koji comparator that shows EcN does not dominate
- [`daf-cd55-protease-stability-computational.md`](./daf-cd55-protease-stability-computational.md) — comp-006, DAF full ectodomain on koji (HIGH, stalk-driven)
- [`lactoferrin-protease-stability-computational.md`](./lactoferrin-protease-stability-computational.md) — comp-005, lactoferrin on koji
- [`chaperone-orthogonal-stacking.md`](./chaperone-orthogonal-stacking.md) — §8 item 8 (no DsbA/DsbC capacity metric); §3.5 per-architecture PDI-residence-time framework (koji-side analogue of Axis 1)
- [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md) — EcN LBP peer track; the facultative-anaerobe periplasmic-O₂ property that makes DsbA/DsbC work at all
- [`complement-c5a-gout.md`](./complement-c5a-gout.md) — two-chassis CP0 coverage architecture
- [`computational-experiments.md`](./computational-experiments.md) — tracking index entry for comp-043
