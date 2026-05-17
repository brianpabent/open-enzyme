---
title: "C1-INH (SERPING1) Protease Stability + Glycosylation Feasibility in EcN LBP: Computational Analysis (comp-037)"
date: 2026-05-17
tags: [complement, C1-INH, SERPING1, serpin, protease, EcN, E-coli-Nissle, LBP, computational, alphafold, structural-biology, CP0, glycosylation, two-chassis]
related:
  - complement-c5a-gout.md
  - engineered-lbp-chassis.md
  - daf-cd55-protease-stability-computational.md
  - daf-cd55-scr14-truncated-computational.md
  - complestatin-bgc-lbp-feasibility-computational.md
  - computational-experiments.md
  - validation-experiments.md
  - hypotheses/H05-daf-scr14-cp0-thesis.md
sources:
  - "UniProt P05155 (human SERPING1 / C1-INH, canonical isoform, SV=2)"
  - "AlphaFold AF-P05155-F1-model_v6 (EMBL-EBI)"
  - "MEROPS database release 12.4"
  - "Bos 1998 PMID 9799502 (C1-INH glycosylation analysis)"
  - "Stavenhagen 2018 PMID 29381136 (C1-INH glycoproteomic characterization)"
  - "Dekker 2001 PMID 11226160 (OmpT di-basic specificity)"
  - "Krojer 2008 PMID 18261546 (DegP / HtrA mechanism)"
  - "Schechter & Berger 1967 (pancreatic protease subsite specificity)"
  - "Carroll 2013 PMID 23859510 (residual colonic pancreatic protease activity)"
status: archived-to-experiments
---

# C1-INH (SERPING1) Protease Stability + Glycosylation Feasibility in EcN LBP: Computational Analysis (comp-037)

> **Frozen analysis archived to [`./etc/experiments/comp-037-c1-inh-protease-stability-ecn/`](./etc/experiments/comp-037-c1-inh-protease-stability-ecn/)** (full pipeline: `analyze.py` + `inputs/` + `outputs/` + `README.md`).
> This wiki page is the interpretive summary; the long content + reproducible code lives next to the experiment.

**Status:** Complete — 2026-05-17 **Experiment folder:** [`etc/experiments/comp-037-c1-inh-protease-stability-ecn/`](./etc/experiments/comp-037-c1-inh-protease-stability-ecn/) **Evidence level:** Mechanistic Extrapolation — AlphaFold pLDDT-based structural inference; no wet-lab confirmation.

**Sister analyses:** [comp-006 (DAF/CD55 ectodomain, koji, HIGH)](./daf-cd55-protease-stability-computational.md) · [comp-012 (DAF/CD55 SCR1-4 truncated, koji, LOW)](./daf-cd55-scr14-truncated-computational.md) · [comp-024 (complestatin BGC on LBP, RED; C1-INH-on-EcN comparator GREEN-provisional 0.774)](./complestatin-bgc-lbp-feasibility-computational.md)

---

## Question

Would human C1-INH (SERPING1, UniProt P05155) survive the colonic-luminal protease environment if expressed as a secreted LBP-luminal payload in engineered *E. coli* Nissle 1917 (EcN)? And does the heavy native glycosylation (~26 kDa glycan on ~52 kDa polypeptide) — which EcN cannot reproduce — preclude functional inhibitor activity?

This is the computational gate that decides whether C1-INH joins DAF SCR1-4 as the second CP0 engineering candidate, completing the two-chassis architecture surfaced 2026-05-16 in [`complement-c5a-gout.md` §9.8](./complement-c5a-gout.md): C1-INH at classical/lectin entry (LBP chassis) + DAF SCR1-4 at surface convertase decay (koji chassis). See [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md) for the chassis peer track and [comp-024](./complestatin-bgc-lbp-feasibility-computational.md) for the upstream feasibility prior that flagged C1-INH as the right next computational gate.

---

## Headline verdict

**MODERATE — kinetic-competition gated.**

Three independent verdicts decompose to:

| Scope / axis | Verdict | Driver |
|---|---|---|
| Serpin core, strictly-degradative (non-RCL, aa 123-451 + 468-500) | **LOW** (0.1) | Once mucin domain (aa 23-119) truncated, serpin body is protease-resistant; only buried OmpT di-basic sites remain |
| Serpin core including RCL (aa 123-500) | **RED** (0.8) | DegP and elastase have 9 + 11 exposed sites in the RCL (aa 452-467) — but **RCL exposure is by design** (serpin suicide-substrate mechanism) |
| Glycosylation feasibility, serpin core | **GREEN** | EcN cannot N-glycosylate; for luminal-secreted topology plasma half-life concern is moot; serpin catalytic mechanism is encoded in polypeptide, not glycan |

**The combined verdict is MODERATE, not RED**, because:

1. Strictly-degradative protease risk on the folded serpin body is **LOW** after mucin truncation.
2. Glycosylation feasibility is **GREEN** for luminal topology.
3. The remaining risk lives in the RCL kinetic competition — does C1s / C1r / MASP-2 engage the reactive bond R466-T467 productively before DegP / elastase cleaves it unproductively? That is a wet-lab kinetic assay question, not an in silico question.

A naive read of the "RED 0.8 serpin core" verdict would mis-attribute the risk axis. The serpin body folds and persists; the question is whether the inhibitor mechanism wins the kinetic race at the RCL.

---

## What the analysis establishes (and what it doesn't)

**Establishes:**

- The mucin-like N-terminal domain (aa 23-119) is the dominant protease liability in an unglycosylated EcN expression context. Truncating it eliminates 55 elastase exposed sites, 18 DegP sites, 7 chymotrypsin sites, and 4 trypsin sites. This is directly analogous to the CD55 stalk truncation in comp-006 → comp-012.
- The serpin body (aa 123-450, anchored by the two disulfides C123-C428 and C130-C205) is well-folded (AlphaFold pLDDT 80-95) and has no exposed protease sites outside the RCL after mucin truncation.
- The RCL (aa 452-467) is intrinsically exposed — and must be, for the serpin suicide-substrate mechanism. The "RED 0.8" score reflects this by-design exposure, not degradative vulnerability of the body.
- N-glycans are not strictly required for inhibitor mechanism in the luminal-secreted format. The catalytic activity (acyl-enzyme covalent trap) is encoded in the polypeptide; the plasma-half-life function of N-glycans is moot for a gut-luminal therapeutic.

**Does NOT establish:**

- Whether the truncated serpin-core construct retains *full* inhibitor activity against C1r, C1s, and MASP-2. Native C1-INH includes the N-terminal mucin-like domain; whether that domain contributes to substrate recognition beyond plasma half-life is not fully resolved in primary literature. **Wet-lab kinetic assay against C1r/C1s/MASP-2 substrates is the gate.**
- Whether EcN can fold the serpin-core construct with both disulfides correctly formed. EcN periplasmic DsbA/DsbC can in principle catalyze both C123-C428 and C130-C205 bonds, but serpin-fold quality in a bacterial chassis is a known wet-lab risk class (broader serpin-bacterial-expression literature is mixed).
- The k_C1s_engagement vs k_DegP_RCL_cleavage kinetic ratio at the RCL. This is the load-bearing wet-lab measurement.
- Whether luminal C1-INH reaches the CP0 priming sites (submucosal macrophages, MSU-crystal-interface convertases) at functionally relevant concentrations. This is the same H05-class clinical-translation question facing the DAF SCR1-4 koji track.

---

## Engineering implications

If the wet-lab gates clear, the recommended C1-INH-on-EcN construct is:

- **Boundary:** aa 123-500 (serpin core, mucin truncated, retains RCL R466-T467).
- **N-terminal anchor:** truncation starts at C123 (first canonical disulfide cysteine) to preserve the disulfide-anchored fold.
- **Signal peptide:** human aa 1-22 replaced with EcN-native secretion signal (OmpA, PelB, or YebF for extracellular release — choice TBD by expression-system optimization).
- **Disulfide partner support:** EcN periplasmic DsbA/DsbC; potentially DsbC-overexpression strain if folding-quality issues emerge.
- **No N-glycosylation system needed** — for luminal-format activity, the catalytic mechanism does not strictly require N-glycans. *C. jejuni* pgl-pathway heterologous transplant (Wacker 2002) is an unnecessary engineering burden for this topology.

---

## Architectural read: the two-chassis CP0 architecture

[`complement-c5a-gout.md` §9.8](./complement-c5a-gout.md) (2026-05-16) proposed pairing C1-INH on EcN with DAF SCR1-4 on koji as a **two-engineered-payload, two-independent-chassis, two-cascade-node** CP0 coverage architecture. This comp-037 computational gate substantiates the C1-INH-on-EcN side:

| Property | DAF SCR1-4 on koji (comp-012, H05) | C1-INH on EcN (comp-037) |
|---|---|---|
| Cascade node | Surface convertase decay (already-assembled C4b2a, C3bBb) | Classical / lectin entry (C1r, C1s, MASP-2) — **upstream of convertase formation** |
| Mechanism logic | Disassembles convertases that form | Prevents convertases from forming |
| Chassis | A. oryzae (koji, food-grade, transit) | E. coli Nissle 1917 (LBP, regulated drug, resident) |
| Distribution | Home-fermentable condiment | Pharmacy-distributed pharmaceutical |
| Computational verdict | LOW (post-stalk-truncation) | MODERATE (kinetic-competition gated) |
| Wet-lab gate | [§1.25 validation-experiments.md](./validation-experiments.md) (queued) | RCL kinetic competition assay (to be specified) |

**Together: two independent mechanisms at two distinct cascade points, delivered via two completely independent chassis, with two completely independent regulatory paths.** Neither competes for the other's production infrastructure; neither mechanism is mechanistically redundant.

**What this does NOT claim:**

- C1-INH on EcN-LBP has NOT been wet-lab validated for luminal stability or complement-regulatory activity in the gut environment. The MODERATE verdict here is a feasibility prior, not an empirical result.
- The C1-INH + DAF composition has NOT been wet-lab tested as a combined intervention. The mechanism-level coverage claim is a **testable hypothesis**, not an asserted synergy.
- No clinical effect-size prediction. Both arms must validate individually before any composition question can be tested.

---

## Files

- **Analysis script:** [`./etc/experiments/comp-037-c1-inh-protease-stability-ecn/analyze.py`](./etc/experiments/comp-037-c1-inh-protease-stability-ecn/analyze.py)
- **Inputs (provenance + sequence + AlphaFold pLDDT + protease panel):** [`./etc/experiments/comp-037-c1-inh-protease-stability-ecn/inputs/`](./etc/experiments/comp-037-c1-inh-protease-stability-ecn/inputs/)
- **Outputs (cleavage map JSON + human-readable summary):** [`./etc/experiments/comp-037-c1-inh-protease-stability-ecn/outputs/`](./etc/experiments/comp-037-c1-inh-protease-stability-ecn/outputs/)
- **README:** [`./etc/experiments/comp-037-c1-inh-protease-stability-ecn/README.md`](./etc/experiments/comp-037-c1-inh-protease-stability-ecn/README.md)

---

## Pre-commit verification (CLAUDE.md Rule 4)

Every load-bearing number in this analysis was grep-verified against primary source before commit:

- **Sequence length 500 aa, signal peptide aa 1-22, mature aa 23-500:** UniProt P05155 SV=2 (fetch 2026-05-17, direct grep against text-format flatfile).
- **Reactive bond R466-T467:** UniProt FT SITE 465..466 ("Reactive bond for chymotrypsin") + SITE 466..467 ("Cleavage; by C1S" + "Reactive bond"); asserted programmatically in `analyze.py main()` (`seq[465]=='R' and seq[466]=='T'`).
- **Disulfide bonds C123-C428 and C130-C205 — exactly 2 total:** UniProt FT DISULFID (exactly two entries; counted with `grep -c`). Asserted programmatically in `analyze.py main()` for both Cys positions. **Note:** casual literature sometimes quotes higher counts; the canonical SV=2 UniProt entry has 2.
- **N-glycan sites 25, 69, 81, 238, 253, 272-variant, 352; O-glycan sites 47, 48, 64, 71, 83, 88, 92, 96:** UniProt FT CARBOHYD direct grep; N-sequon (N-X-S/T) verified by direct sequence inspection for each N-site (see `inputs/provenance.md`).
- **~26 kDa glycan on ~52 kDa polypeptide:** Bos 1998 PMID 9799502 + Stavenhagen 2018 PMID 29381136 (cited PMID-anchored in provenance.md).
- **DegP P1 specificity V/I/L/F/Y/A:** Krojer 2008 PMID 18261546.
- **OmpT di-basic P1-P1' specificity:** Dekker 2001 PMID 11226160; Hwang 2007 PMID 17263510.
- **Colonic pH 6-7:** Fallingborg 1999 PMID 10204470.
- **Trypsin / chymotrypsin / elastase MEROPS IDs (S01.151, S01.001, S01.153) and P1 specificities:** MEROPS release 12.4 + Schechter & Berger 1967 + Hedstrom 2002 PMID 12475195 + Largman 1976 PMID 988044.

The DAF SCR1-4 disulfide-count incident (2026-05-06, documented in `CLAUDE.md` Rule 4) is the canonical case this verification gate exists to prevent. C1-INH disulfide count was the first place that gate was applied here — 2 bonds, grep-verified, not the inflated counts sometimes appearing in secondary literature.

---

## Limitations

- **Disulfides not modeled by the scoring algorithm.** The C123-C428 and C130-C205 bonds reduce backbone flexibility in the serpin core; this analysis likely overestimates risk in the body. C1-INH has only 2 disulfides — far less than CD55 SCR1-4 (8) — so the overestimate is modest.
- **O-glycosylation of the mucin domain not modeled in the native baseline.** The scoring treats the mucin domain as the unglycosylated polypeptide that EcN would produce; this is the right model for the EcN-expression context but means the score is NOT comparable to in vivo (heavily glycosylated) protease stability.
- **pLDDT ≠ solvent accessibility.** Surface-exposed loops on a well-folded serpin core may have high pLDDT but still be protease-accessible. SASA refinement would tighten the per-residue score.
- **P1/P1' rules only.** Extended subsite specificity (P2-P4) not modeled. Trypsin K/R-P bonds resist cleavage; DegP and OmpT have non-trivial P2 preferences. Site counts likely over-estimated for some proteases.
- **Commensal-bacterial protease load not modeled.** The five-protease panel covers the dominant identifiable risks (pancreatic + EcN-native); the diffuse colonic-microbiome protease landscape is not enzyme-level characterized for this scope.
- **Bile-acid effects not modeled.** Bile acids in the upper colon may partially unfold proteins and enhance protease access.
- **EcN secretion topology not directly modeled.** Type I (HlyA-like), Type II (secretome), Sec/YebF (extracellular), or signal-peptide-driven release affects exposure to OmpT and DegP. This analysis pools both risks without conditioning on a specific export pathway.
- **RCL kinetic-competition treatment is in-scope only as a flagged wet-lab question, not in silico modeled.** k_C1s_engagement vs. k_DegP_RCL_cleavage on the recombinant construct is the load-bearing wet-lab measurement that decides whether C1-INH is a viable luminal CP0 candidate.

---

## Cross-references

- [`complement-c5a-gout.md` §9.8](./complement-c5a-gout.md) — two-chassis CP0 coverage architecture (C1-INH on EcN + DAF SCR1-4 on koji); this comp-037 substantiates the C1-INH side
- [`engineered-lbp-chassis.md`](./engineered-lbp-chassis.md) — LBP chassis peer track; EcN protease environment, secretion topology, regulatory path
- [`daf-cd55-scr14-truncated-computational.md`](./daf-cd55-scr14-truncated-computational.md) — comp-012, the sister koji-track analysis
- [`daf-cd55-protease-stability-computational.md`](./daf-cd55-protease-stability-computational.md) — comp-006, full DAF ectodomain (HIGH, stalk-driven; rescued by truncation in comp-012)
- [`complestatin-bgc-lbp-feasibility-computational.md`](./complestatin-bgc-lbp-feasibility-computational.md) — comp-024, the upstream feasibility scan that flagged C1-INH as the right next computational gate (GREEN-provisional 0.774); comp-037 substantiates that prior
- [`hypotheses/H05-daf-scr14-cp0-thesis.md`](./hypotheses/H05-daf-scr14-cp0-thesis.md) — falsification card for the koji-side DAF thesis; a parallel H-card for the EcN-side C1-INH thesis should be created (queued)
- [`validation-experiments.md` §1.25](./validation-experiments.md) — wet-lab gate for DAF SCR1-4; sister wet-lab gate for C1-INH (RCL kinetic-competition assay) should be added (queued)
- [`computational-experiments.md`](./computational-experiments.md) — tracking index entry for comp-037
