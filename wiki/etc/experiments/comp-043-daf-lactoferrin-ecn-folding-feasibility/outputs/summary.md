# comp-043 — EcN periplasmic disulfide-folding + colonic-protease scaling: C1-INH (2) vs DAF SCR1-4 (8) vs lactoferrin (16)

**Question:** Does EcN periplasmic disulfide-folding (DsbA/DsbC) + colonic-protease survival scale from C1-INH (2 disulfides, comp-037) to DAF SCR1-4 (8) and lactoferrin (16)?
**Chassis:** Engineered E. coli Nissle 1917 (EcN) LBP, luminal-secreted format
**Environment:** Colonic lumen, pH 6-7, 37C, ~0.15 M NaCl; bile-acid + commensal proteases out-of-model
**Method:** NOT a genome-scale metabolic model (a GEM models flux, not folding-machinery competition). Structural + sequence folding-feasibility analysis across three orthogonal axes with a limiting-factor (Liebig) composite.

> **Honesty constraint (load-bearing):** No published DsbA/DsbC capacity metric exists at 8-16 disulfide scale. These are precedent-derived inferences, NOT measurements. This is the single biggest assumption.

---

## Head-to-head verdict

| Payload | Disulfides | Eff. folding demand | Composite verdict | Driver |
|---|---|---|---|---|
| C1-INH (serpin, 2 SS) | 2 | 4.0 | **VIABLE** | disulfide-axis viable across the capacity band; protease LOW; glyco not function-limiting. CAVEAT: Axis 1 scores disulfide formation/isomerization burden, NOT native-fold attainment — serpin metastability (recombinant C1-INH is made in mammalian/milk systems, not E. coli) is an unmodeled attainment risk |
| DAF SCR1-4 (CCP/sushi, 8 SS) | 8 | 10.0 | **PROVISIONAL** | folding-capacity-gated: viability flips across the (unmeasured) DsbA/DsbC capacity band |
| Lactoferrin (transferrin-lobe, 16 SS) | 16 | 23.5 | **NOT-VIABLE** | folding-limited across the entire plausible DsbA/DsbC capacity band |

**Crossover:** EcN periplasmic DsbA/DsbC folding is plausible up to ~2 disulfides (C1-INH, VIABLE); PROVISIONAL / capacity-gated at 8 disulfides (DAF SCR1-4); and NOT plausible at 16 disulfides (lactoferrin, folding-limited across the entire capacity band). The plausible-to-not-plausible crossover sits AT DAF SCR1-4 (8 disulfides) and its exact location is gated by the one unmeasured parameter — the DsbA/DsbC oxidative-folding capacity metric at 8-16 disulfide scale, which does not exist in the published literature.

---

## Axis 1 — Disulfide-folding burden vs. DsbA/DsbC capacity

Reference capacity band (effective-demand units) — **precedent-derived estimates, not measured:**

- conservative 5.0 — Certolizumab pegol Fab' — secreted periplasmic E. coli manufacture, ~5 disulfides
- moderate 8.0 — Fab-class precedent + DsbC-isomerase co-expression credit
- optimistic 12.0 — Engineered oxidizing strain (SHuffle trxB/gor + cytoplasmic DsbC); set BELOW full-IgG 16

| Payload | SS count | max loop | long-range (>150) | crossings | eff. demand (loop+cross) | nonviab @cons/mod/opt | folding verdict |
|---|---|---|---|---|---|---|---|
| C1-INH (serpin, 2 SS) | 2 | 305 | 1 | 0 | 4.0 (4.0+0.0) | 0.3/0.0/0.0 | **FOLDING-PLAUSIBLE** |
| DAF SCR1-4 (CCP/sushi, 8 SS) | 8 | 47 | 0 | 4 | 10.0 (8.0+2.0) | 1.0/0.75/0.333 | **FOLDING-EDGE** |
| Lactoferrin (transferrin-lobe, 16 SS) | 16 | 281 | 3 | 4 | 23.5 (21.5+2.0) | 1.0/1.0/1.0 | **FOLDING-LIMITED** |

Interpretation: folding-nonviability runs 0 (plausible) -> 1 (folding-limited). C1-INH stays plausible across the whole band; DAF SCR1-4 STRADDLES it (viable only at optimistic capacity); lactoferrin is folding-limited even at optimistic capacity (its 3 C-lobe-spanning long-range bonds — 424-705, 446-668, 502-696 — are the transferrin-fold hierarchical-folding signature that a periplasmic oxidase is poorly suited to).

---

## Axis 2 — Strictly-degradative colonic-luminal protease exposure (folded core)

| Payload | Folded core (aa) | Max risk | Worst protease | Exposed sites | Verdict |
|---|---|---|---|---|---|
| C1-INH (serpin, 2 SS) | 123-500 | 0.1 | `OmpT` | 0 | **LOW** |
| DAF SCR1-4 (CCP/sushi, 8 SS) | 35-285 | 0.1 | `OmpT` | 0 | **LOW** |
| Lactoferrin (transferrin-lobe, 16 SS) | 20-710 | 1.0 | `OmpT` | 5 | **RED** |

Note: C1-INH excludes the RCL (aa 452-467) — exposed BY DESIGN for the serpin mechanism; its cleavage is a kinetic-competition question (comp-037), not strictly degradative. Protease exposure is a SECONDARY axis — moot for lactoferrin, whose folding fails first.

---

## Axis 3 — Glycosylation dependence for FUNCTION (EcN cannot glycosylate)

| Payload | N-glyc sites | Class | Penalty | Kills function in EcN? |
|---|---|---|---|---|
| C1-INH (serpin, 2 SS) | 7 | not_required | 0.0 | No |
| DAF SCR1-4 (CCP/sushi, 8 SS) | 1 | aids_not_required | 0.3 | No |
| Lactoferrin (transferrin-lobe, 16 SS) | 3 | aids_not_required | 0.3 | No |

- **C1-INH (serpin, 2 SS):** N-glycans drive plasma half-life (Bos 1998 PMID 9799502); the serpin suicide-inhibitor mechanism (RCL presentation -> acyl-enzyme covalent trap) is polypeptide-encoded. For a gut-luminal format, plasma half-life is irrelevant. Deglycosylated C1-INH is functionally inhibitory (Bos 1998).
- **DAF SCR1-4 (CCP/sushi, 8 SS):** Single N-glycan (N95, SCR1). Decay-accelerating activity is a protein-protein interaction (SCR2-4 bind C3b/C4b and accelerate convertase decay) — not glycan-dependent. The bulk glycan liability (O-glycans) is on the truncated stalk. Loss of N95 glycan is unlikely to abolish function but is not affirmatively demonstrated for an aglycosyl SCR1-4 fragment.
- **Lactoferrin (transferrin-lobe, 16 SS):** 3 N-glycans (N156/N497/N642). Iron sequestration + lactoferricin antimicrobial activity are polypeptide-encoded; glycans contribute to protease resistance and thermal stability. Non-native (fungal) glycans are tolerated with native fold (Sun 1999 PMID 10089347, A. awamori hLf). CRITICAL: glycosylation is NOT the function-killer for lactoferrin in EcN — the disulfide-FOLDING axis is. In EcN the glycans are entirely absent, removing their protease-resistance contribution and COMPOUNDING (not causing) the folding problem.

**Key honest finding on Axis 3:** glycosylation-dependence does NOT independently kill DAF or lactoferrin function in EcN — both retain core polypeptide-encoded function without glycans (DAF decay-acceleration is protein-protein; lactoferrin iron-binding tolerates non-native glycans, Sun 1999). The dominant filter is Axis 1 (disulfide folding), not Axis 3. Over-attributing the lactoferrin problem to glycosylation would be a mechanism error.

---

## Card claim evaluated

**Claim:** 'EcN is superior to koji for PDI-heavy payloads like DAF SCR1-4 (8 disulfides) and lactoferrin (16 disulfides).'

**Verdict: REFUTED as stated (blanket 'PDI-heavy' claim).**

EcN's periplasmic DsbA/DsbC folding plausibly extends to LOW-to-MODERATE disulfide, COMPACT-fold, glycosylation-independent payloads (C1-INH VIABLE 2 disulfides; DAF SCR1-4 PROVISIONAL 8 disulfides, CCP/sushi fold). It does NOT plausibly scale to lactoferrin (16 disulfides, bilobal transferrin fold with C-lobe-spanning long-range bonds). Moreover koji is NOT dominated: koji (eukaryotic ER + PDI/ERO1 + glycosylation) folds DAF SCR1-4 at LOW protease risk (comp-012) and has a >2 g/L lactoferrin precedent (Ward 1995, A. awamori; Sun 1999 native fold). So EcN is a plausible ALTERNATIVE at low/moderate disulfide scale, not a superior chassis for PDI-heavy payloads — and is inferior to koji for lactoferrin specifically.

---

## Compounding optimistic assumptions (verdict is PROVISIONAL where these stack)

- Reference DsbA/DsbC capacity band (5/8/12) is precedent-derived, NOT a measured capacity (no published metric at 8-16 disulfide scale — chaperone-orthogonal-stacking.md §8 item 8).
- Axis 1 scores disulfide FORMATION/ISOMERIZATION burden, NOT native-fold ATTAINMENT. Serpin metastability (C1-INH) and transferrin molten-globule hierarchy (lactoferrin) are additional unmodeled attainment risks — disulfides are necessary, not sufficient, for a functional fold. Recombinant C1-INH is manufactured in mammalian/milk systems, not E. coli, for this reason.
- The OPTIMISTIC anchor (12.0, SHuffle trxB/gor + cytoplasmic DsbC) describes CYTOPLASMIC disulfide formation. A cytoplasmically-folded protein does not route through the Sec→periplasm→outer-membrane luminal-secretion path this LBP format requires — so the optimistic anchor is compartment-mismatched with the secreted format. The realistic ceiling for a SECRETED payload is nearer the conservative/moderate anchors, which pushes DAF SCR1-4 toward the folding-limited end of its band (i.e., DAF's 'viable-only-at-optimistic' read leans on an anchor that may not apply).
- pLDDT is used as a burial proxy for the protease axis (comp-034 showed this under-counts SASA-exposed helical/linker sites ~10x, e.g. the lactoferrin inter-lobe linker).
- Per-bond loop-length weighting (1.0/1.5/2.5) + per-crossing surcharge (0.5) are transparent monotone proxies for DsbC isomerization demand, not measured k_cat values.
- Secretion topology (Sec/YebF/Type I) and its effect on OmpT/DegP exposure is not modeled.
- Colonic commensal-microbiome protease load and bile-acid unfolding are out-of-model.
- The koji lactoferrin precedent (>2 g/L) is Aspergillus AWAMORI (Ward 1995), a sister species of A. oryzae koji — genus-level evidence, not koji proper.

Because 3+ optimistic assumptions compound toward any 'viable'-leaning read, the DAF SCR1-4 verdict is labelled **PROVISIONAL** and the single biggest unresolved question is named explicitly: the DsbA/DsbC oxidative-folding capacity metric at 8-16 disulfide scale.

---

*Generated by `analyze.py`. Uses `experiments/lib/protease_stability.py`. Disulfide counts grep-verified against UniProt P05155 (2), P08174 (8), P02788 (16). See `inputs/provenance.md`.*
