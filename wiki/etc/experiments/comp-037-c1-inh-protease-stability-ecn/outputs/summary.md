# comp-037 — C1-INH (SERPING1) Protease Stability + Glycosylation Feasibility in EcN LBP

**Protein:** Plasma protease C1 inhibitor (SERPING1 / C1-INH), Homo sapiens (P05155)  
**AlphaFold model:** AF-P05155-F1-model_v6  
**Signal peptide:** 1-22 (cleaved during secretion in native context; replaced by EcN-native secretion signal in engineered LBP construct)  
**Mature chain:** 23-500  
**Mucin-like O-glycan domain (candidate truncation):** 23-119 (heavily O-glycosylated tandem-repeat region in vivo; unglycosylated in EcN expression; candidate truncation)  
**Serpin-core construct (mucin-truncated):** 123-500 (mucin-truncated construct, retains RCL R466-T467)  
**RCL (reactive-center loop):** 452-467 (reactive-center loop; P1-P1' R466-T467)  
**N-glycosylation sites (UniProt CARBOHYD, full-seq numbering):** [25, 69, 81, 238, 253, 272, 352]  
**O-glycosylation sites (UniProt CARBOHYD, full-seq numbering):** [47, 48, 64, 71, 83, 88, 92, 96]  
**Disulfide bonds (UniProt DISULFID):** [(123, 428), (130, 205)] — 2 bonds total (verified)  
**Conditions modeled:** colonic lumen, pH 6.0-7.0, 37°C, 1-7 days  
**Chassis:** Engineered E. coli Nissle 1917 (EcN) LBP, luminal-secreted format  
**Analysis date:** 2026-05-17  
**Script:** `experiments/comp-037-c1-inh-protease-stability-ecn/analyze.py`  
**Library:** `experiments/lib/protease_stability.py`  

---

## Structural Overview

| Metric | Value |
|---|---|
| Sequence length | 500 aa (incl. signal peptide aa 1-22) |
| Mean pLDDT (AlphaFold confidence) | 79.6 / 100 |
| Minimum pLDDT | 28.8 / 100 |
| % residues pLDDT > 80 (well-folded) | 71.8% |
| % residues pLDDT > 90 (core-folded) | 65.8% |

**C1-INH structural notes:**

- Signal peptide (aa 1-22): disordered, low pLDDT. Replaced by EcN-native signal in the engineered construct.
- Mucin-like N-terminal domain (aa 23-119): disordered (UniProt MobiDB-lite REGION annotations at aa 20-43 and aa 65-118, with REPEAT 85-119 being 7 × [QE]-P-T-[TQ] tandem repeats). Heavily O-glycosylated in vivo; **completely unglycosylated when expressed in EcN.** This is the dominant disordered liability in a bacterial-expression context — directly analogous to the CD55 Ser/Thr stalk in comp-006.
- Serpin core (aa ~120-450): canonical serpin fold (β-sheet + α-helices), well-folded (pLDDT > 80 across most of this region). Contains both disulfides (C123-C428, C130-C205) and the four canonical N-glycan sites of the serpin body (N238, N253, N272-variant, N352).
- Reactive-center loop (RCL, aa ~452-467): exposed flexible loop ending at the P1-P1' R466-T467 scissile bond. **Inherently protease-accessible by design** — this is how the suicide-substrate inhibitor mechanism works. The RCL must be cleavable for the inhibitor to function.

---

## Per-Protease Risk Assessment

### Pancreatic trypsin (bovine/human, residual colonic activity) (`trypsin`)

| Parameter | Value |
|---|---|
| Recognition sites (full sequence) | 43 |
| Buried (pLDDT ≥ 80) | 36 |
| Partially exposed (pLDDT 65-80) | 1 |
| Exposed (pLDDT < 65) | 6 |
| Residual activity at modeled NaCl | 100% |
| pH activity factor at colonic pH | 60% |
| Effective protease activity | 60.0% |
| Max risk (full sequence) | 0.6 |
| Max risk (mature, aa 23-500) | 0.6 |
| Max risk (mucin domain, aa 23-119) | 0.6 |
| Max risk (serpin core, aa 123-500) | 0.24 |
| Max risk (RCL, aa 452-467) | 0.24 |
| Max risk (serpin core non-RCL, aa 123-451 + 468-500) | 0.06 |
| Mucin-domain exposed sites | 4 |
| Serpin-core exposed sites (incl RCL) | 0 |
| Serpin-core exposed sites (excl RCL — strictly-degradative) | 0 |
| RCL exposed sites (inherent inhibitor-mechanism risk) | 0 |

**Top 5 highest-risk cleavage sites (full sequence):**

| Position | Region | P1 | P1' | pLDDT (window) | Accessibility | Risk score |
|---|---|---|---|---|---|---|
| 4 | signal_peptide | R | L | 41.1 | exposed | 0.6 |
| 19 | signal_peptide | R | A | 39.4 | exposed | 0.6 |
| 40 | mucin_like_O_glycan_domain | R | G | 35.6 | exposed | 0.6 |
| 44 | mucin_like_O_glycan_domain | K | V | 33.2 | exposed | 0.6 |
| 52 | mucin_like_O_glycan_domain | K | M | 33.6 | exposed | 0.6 |

### Pancreatic chymotrypsin (bovine/human, residual colonic activity) (`chymotrypsin`)

| Parameter | Value |
|---|---|
| Recognition sites (full sequence) | 112 |
| Buried (pLDDT ≥ 80) | 94 |
| Partially exposed (pLDDT 65-80) | 1 |
| Exposed (pLDDT < 65) | 17 |
| Residual activity at modeled NaCl | 100% |
| pH activity factor at colonic pH | 60% |
| Effective protease activity | 60.0% |
| Max risk (full sequence) | 0.6 |
| Max risk (mature, aa 23-500) | 0.6 |
| Max risk (mucin domain, aa 23-119) | 0.6 |
| Max risk (serpin core, aa 123-500) | 0.06 |
| Max risk (RCL, aa 452-467) | 0 |
| Max risk (serpin core non-RCL, aa 123-451 + 468-500) | 0.06 |
| Mucin-domain exposed sites | 7 |
| Serpin-core exposed sites (incl RCL) | 0 |
| Serpin-core exposed sites (excl RCL — strictly-degradative) | 0 |
| RCL exposed sites (inherent inhibitor-mechanism risk) | 0 |

**Top 5 highest-risk cleavage sites (full sequence):**

| Position | Region | P1 | P1' | pLDDT (window) | Accessibility | Risk score |
|---|---|---|---|---|---|---|
| 1 | signal_peptide | M | A | 41.7 | exposed | 0.6 |
| 5 | signal_peptide | L | T | 41.2 | exposed | 0.6 |
| 7 | signal_peptide | L | L | 39.8 | exposed | 0.6 |
| 8 | signal_peptide | L | T | 39.8 | exposed | 0.6 |
| 10 | signal_peptide | L | L | 39.4 | exposed | 0.6 |

### Pancreatic elastase (human PRSS2 / elastase-2A, residual colonic activity) (`elastase`)

| Parameter | Value |
|---|---|
| Recognition sites (full sequence) | 267 |
| Buried (pLDDT ≥ 80) | 178 |
| Partially exposed (pLDDT 65-80) | 3 |
| Exposed (pLDDT < 65) | 86 |
| Residual activity at modeled NaCl | 100% |
| pH activity factor at colonic pH | 50% |
| Effective protease activity | 50.0% |
| Max risk (full sequence) | 0.5 |
| Max risk (mature, aa 23-500) | 0.5 |
| Max risk (mucin domain, aa 23-119) | 0.5 |
| Max risk (serpin core, aa 123-500) | 0.5 |
| Max risk (RCL, aa 452-467) | 0.5 |
| Max risk (serpin core non-RCL, aa 123-451 + 468-500) | 0.05 |
| Mucin-domain exposed sites | 55 |
| Serpin-core exposed sites (incl RCL) | 11 |
| Serpin-core exposed sites (excl RCL — strictly-degradative) | 0 |
| RCL exposed sites (inherent inhibitor-mechanism risk) | 11 |

**Top 5 highest-risk cleavage sites (full sequence):**

| Position | Region | P1 | P1' | pLDDT (window) | Accessibility | Risk score |
|---|---|---|---|---|---|---|
| 2 | signal_peptide | A | S | 41.0 | exposed | 0.5 |
| 3 | signal_peptide | S | R | 41.5 | exposed | 0.5 |
| 5 | signal_peptide | L | T | 41.2 | exposed | 0.5 |
| 6 | signal_peptide | T | L | 41.5 | exposed | 0.5 |
| 7 | signal_peptide | L | L | 39.8 | exposed | 0.5 |

### E. coli outer membrane protease OmpT (omptin family) (`OmpT`)

| Parameter | Value |
|---|---|
| Recognition sites (full sequence) | 3 |
| Buried (pLDDT ≥ 80) | 3 |
| Partially exposed (pLDDT 65-80) | 0 |
| Exposed (pLDDT < 65) | 0 |
| Residual activity at modeled NaCl | 100% |
| pH activity factor at colonic pH | 100% |
| Effective protease activity | 100.0% |
| Max risk (full sequence) | 0.1 |
| Max risk (mature, aa 23-500) | 0.1 |
| Max risk (mucin domain, aa 23-119) | 0 |
| Max risk (serpin core, aa 123-500) | 0.1 |
| Max risk (RCL, aa 452-467) | 0 |
| Max risk (serpin core non-RCL, aa 123-451 + 468-500) | 0.1 |
| Mucin-domain exposed sites | 0 |
| Serpin-core exposed sites (incl RCL) | 0 |
| Serpin-core exposed sites (excl RCL — strictly-degradative) | 0 |
| RCL exposed sites (inherent inhibitor-mechanism risk) | 0 |

**Top 5 highest-risk cleavage sites (full sequence):**

| Position | Region | P1 | P1' | pLDDT (window) | Accessibility | Risk score |
|---|---|---|---|---|---|---|
| 161 | serpin_core | K | K | 92.8 | buried | 0.1 |
| 306 | serpin_core | K | K | 96.5 | buried | 0.1 |
| 328 | serpin_core | K | K | 96.2 | buried | 0.1 |

### E. coli periplasmic protease DegP / HtrA (`DegP`)

| Parameter | Value |
|---|---|
| Recognition sites (full sequence) | 178 |
| Buried (pLDDT ≥ 80) | 138 |
| Partially exposed (pLDDT 65-80) | 1 |
| Exposed (pLDDT < 65) | 39 |
| Residual activity at modeled NaCl | 100% |
| pH activity factor at colonic pH | 80% |
| Effective protease activity | 80.0% |
| Max risk (full sequence) | 0.8 |
| Max risk (mature, aa 23-500) | 0.8 |
| Max risk (mucin domain, aa 23-119) | 0.8 |
| Max risk (serpin core, aa 123-500) | 0.8 |
| Max risk (RCL, aa 452-467) | 0.8 |
| Max risk (serpin core non-RCL, aa 123-451 + 468-500) | 0.08 |
| Mucin-domain exposed sites | 18 |
| Serpin-core exposed sites (incl RCL) | 9 |
| Serpin-core exposed sites (excl RCL — strictly-degradative) | 0 |
| RCL exposed sites (inherent inhibitor-mechanism risk) | 9 |

**Top 5 highest-risk cleavage sites (full sequence):**

| Position | Region | P1 | P1' | pLDDT (window) | Accessibility | Risk score |
|---|---|---|---|---|---|---|
| 2 | signal_peptide | A | S | 41.0 | exposed | 0.8 |
| 5 | signal_peptide | L | T | 41.2 | exposed | 0.8 |
| 7 | signal_peptide | L | L | 39.8 | exposed | 0.8 |
| 8 | signal_peptide | L | T | 39.8 | exposed | 0.8 |
| 10 | signal_peptide | L | L | 39.4 | exposed | 0.8 |

---

## Per-Scope Verdicts (Protease Risk)

| Scope | Verdict | Max risk | Worst protease |
|---|---|---|---|
| Full sequence (aa 1-500) | **RED** | 0.8 | `DegP` |
| Mature protein (aa 23-500, signal peptide removed) | **RED** | 0.8 | `DegP` |
| Serpin core (aa 123-500, mucin truncated, **includes RCL**) | **RED** | 0.8 | `DegP` |
| Serpin core **non-RCL** (strictly-degradative scope) | **LOW** | 0.1 | `OmpT` |

**Full-sequence verdict: RED** — severe protease risk; this scope is not viable without major engineering.

**Mature-protein verdict: RED** — severe protease risk; this scope is not viable without major engineering.

**Serpin-core (engineered construct, includes RCL) verdict: RED** — severe protease risk; this scope is not viable without major engineering.

**Serpin-core non-RCL (strictly-degradative) verdict: LOW** — protease degradation under the modeled colonic-luminal EcN conditions is unlikely to meaningfully reduce activity.

**Why two serpin-core verdicts.** The reactive-center loop (RCL, aa 452-467) is **exposed by design** — the serpin suicide-substrate mechanism requires the RCL to be cleavable by target proteases (C1r, C1s, MASP-2 in this case). Cleavage of the RCL by C1r/C1s is the inhibitor mechanism itself. RCL cleavage by *off-target* proteases (DegP, elastase, chymotrypsin) is different — it consumes the inhibitor without productive trapping of a complement protease. The 'serpin-core including RCL' verdict reflects the full risk (both productive and unproductive RCL cleavage); the 'serpin-core non-RCL' verdict reflects the strictly-degradative risk to the inhibitor body. **The non-RCL verdict is the better measure of whether the protein folds and persists; the RCL exposure-vs-engagement question is a kinetic-competition wet-lab question (k_C1s_engagement vs k_DegP_cleavage on the RCL).**

The serpin-core construct (aa 123-500) replaces aa 1-22 (human signal peptide) with an EcN-native secretion signal and truncates the mucin-like O-glycan domain (aa 23-119), which is unglycosylated in EcN and would otherwise be the dominant protease liability — directly analogous to the CD55 stalk truncation in comp-006 → comp-012.

---

## Glycosylation Feasibility (Independent Axis)

### Mature-protein construct (aa 23-500, mucin domain retained)

**Verdict: YELLOW**

Full mature construct (aa 23-500) retains the mucin-like O-glycan domain (aa 47-96) with 8 O-glycan sites — all unglycosylated in EcN expression. The disordered, unglycosylated mucin region is a major protease liability (see protease-scoring above). 7 N-glycan sites in mature chain, none glycosylated. Plasma half-life concern is moot for luminal topology, but the unshielded mucin domain is the dominant degradation risk.

### Serpin-core construct (aa 123-500, mucin domain truncated)

**Verdict: GREEN**

Serpin-core construct (aa 123-500) truncates the mucin-like O-glycan domain entirely. 4 N-glycan sites remain in the construct (N238, N253, N272-variant, N352 — all in the serpin core, none glycosylated by EcN). 0 O-glycan sites remain (all 8 O-sites are in the truncated mucin domain). For luminal-secreted topology, plasma half-life is not a concern; serpin suicide-mechanism activity does not strictly require glycosylation. The major risk is loss of N-glycan-mediated folding-quality-control during EcN secretion — addressable with disulfide-bond-aware folding partners (DsbA/DsbC in the EcN periplasm) and signal-peptide / chassis tuning.

**Key supporting facts:**

- C1-INH carries ~26 kDa of glycan on a ~52 kDa polypeptide chain (Bos 1998 PMID 9799502; Stavenhagen 2018 PMID 29381136 mass-spec characterization).
- In the **plasma / IV** context, N-glycans are critical for the ~30 h circulating half-life. Bos 1998 showed deglycosylated C1-INH is functionally inhibitory but is cleared rapidly.
- For a **luminal-secreted** format (this scope), plasma half-life is irrelevant — the inhibitor acts in the gut lumen on locally generated C1r / C1s / MASP-2 at MSU-crystal interfaces and submucosal CP0 sites. The serpin suicide-mechanism (RCL presentation → acyl-enzyme covalent trap) does not strictly require glycosylation; the catalytic mechanism is encoded in the polypeptide.
- EcN does not have an endogenous N-glycosylation system. The *C. jejuni* pgl pathway can be heterologously transplanted (Wacker 2002), but produces a bacterial-glycan structure distinct from mammalian biantennary complex N-glycans. The added engineering complexity is substantial and not warranted unless wet-lab data shows non-glycosylated C1-INH has unacceptable folding or stability behavior in EcN.
- The mucin-like O-glycan domain (aa 47-96) carries 8 O-linked GalNAc sites in vivo. In an EcN expression context all are absent. This region is then a disordered hydrophobic-rich stretch directly accessible to luminal proteases (especially elastase / DegP for the hydrophobic-prone subsites, and OmpT for any basic-residue pairs).

---

## Combined Verdict — Recommendation for the LBP Engineering Track

**Protease verdict (serpin-core construct, includes RCL):** RED  
**Protease verdict (serpin-core non-RCL, strictly-degradative):** LOW  
**Glycosylation feasibility (serpin-core construct):** GREEN  

The two protease verdicts and the glycosylation verdict are computed independently and are all load-bearing for the engineering decision. The serpin-core construct (aa 123-500) is the recommended engineering scope for EcN-LBP luminal C1-INH expression. The headline finding: strictly-degradative protease risk on the serpin body is LOW; the additional RCL-cleavage risk by off-target proteases is the kinetic-competition wet-lab question that decides ultimate effectiveness.

**What this analysis does NOT establish:**

- Whether the truncated serpin-core construct retains full inhibitor activity (i.e., still engages C1r / C1s / MASP-2 productively). The reactive-center loop and serpin body fold are retained in the construct, but the contribution of the N-terminal mucin domain to inhibitor function (vs. purely a plasma-half-life function) is not fully resolved in the primary literature. Wet-lab assay against C1r / C1s / MASP-2 substrates is the gate.
- Whether EcN can fold the serpin-core construct with both disulfides correctly formed. EcN periplasmic DsbA / DsbC can in principle catalyze the two C123-C428 and C130-C205 bonds, but serpin-fold quality in a bacterial chassis is a known wet-lab risk (Bottomley 2000-era literature on bacterial serpin expression).
- Whether luminal C1-INH can productively reach the CP0 priming sites (submucosal macrophages, MSU-crystal-interface convertases) at functionally relevant concentrations. This is the same H05-class wet-lab gate question facing the DAF SCR1-4 koji track.

---

## Limitations

- **Disulfides not modeled.** The C123-C428 and C130-C205 bonds substantially reduce backbone flexibility in the serpin core. This analysis likely **overestimates risk in the serpin core**. Note that C1-INH has only 2 disulfides — far less stabilization than CD55 SCR1-4 (8 bonds) — so the over-estimate is modest.
- **O-glycosylation of the mucin domain not modeled in the native baseline.** In a glycosylated native context, the mucin domain is sterically shielded by O-GalNAc / sialylated chains. The scoring here treats the mucin domain as an unglycosylated polypeptide — which is the correct model for the EcN expression context, but means the score is NOT directly comparable to the in vivo (heavily glycosylated) protease-stability profile of native serum C1-INH.
- **pLDDT ≠ solvent accessibility.** Surface-exposed loops on a well-folded serpin core may have high pLDDT but still be protease-accessible. SASA-based refinement would tighten the score.
- **P1/P1' rules only.** Extended subsite specificity (P2-P4) not modeled. Trypsin and OmpT in particular have non-trivial P2 preferences (e.g., trypsin K/R-P bonds resist cleavage) which would refine site counts downward.
- **Commensal-bacterial protease load not modeled.** The five-protease panel covers the dominant identifiable risks (pancreatic + EcN-native) but the colonic microbiome contributes a diffuse additional protease landscape that is not enzyme-level characterized for this scope.
- **Bile-acid effects not modeled.** Bile acids in the upper colon can partially unfold proteins and may enhance protease access to otherwise-buried sites — treated here as out-of-model.
- **EcN secretion topology not directly modeled.** Whether the construct is exported via Type I (HlyA-like), Type II (secretome), Sec/YebF (extracellular), or signal-peptide-driven periplasmic + outer-membrane-permeabilized release is an engineering choice that will affect exposure to OmpT and DegP. This analysis pools both risks but does not condition on a specific export pathway.

---

## Comparison with comp-006 / comp-012 (DAF/CD55 on koji)

| Feature | DAF/CD55 (comp-006, koji) | DAF/CD55 SCR1-4 (comp-012, koji) | C1-INH (comp-037, EcN) |
|---|---|---|---|
| Chassis | A. oryzae koji | A. oryzae koji | E. coli Nissle 1917 LBP |
| Environment | Shio-koji (17.5% NaCl, pH 4.5-5) | Shio-koji | Colonic lumen (~0.15 M NaCl, pH 6-7) |
| Mechanism | Convertase decay (surface) | Convertase decay (surface) | C1r / C1s / MASP-2 inhibition (entry) |
| Protease panel | ALP, NPr, acid_protease | ALP, NPr, acid_protease | trypsin, chymotrypsin, elastase, OmpT, DegP |
| Construct (engineered) | aa 35-353 (ectodomain) | aa 35-285 (SCR1-4 only) | aa 123-500 (serpin core, mucin truncated) |
| Verdict (engineered construct) | HIGH (stalk-driven) | LOW | **RED** |
| Glycosylation issue | O-glyc stalk (koji can O-glyc but differently) | O-glyc stalk removed | N-glyc (EcN cannot N-glyc); O-glyc (mucin removed) |
| Disulfide load | 8 bonds in SCR1-4 (canonical CCP) | 8 bonds in SCR1-4 | 2 bonds in serpin body |

**Architectural read:** comp-037 + comp-012 together support the two-chassis CP0 architecture surfaced 2026-05-16 in [`complement-c5a-gout.md` §9.8](../../../complement-c5a-gout.md): C1-INH on EcN at classical/lectin entry, DAF SCR1-4 on koji at surface convertase decay. Two independent mechanisms at two cascade points via two independent chassis.

---

*Generated by `analyze.py` on 2026-05-17. Uses experiments/lib/protease_stability.py. Re-run after any AlphaFold model update or MEROPS specificity revision. See inputs/provenance.md for data sources and citations.*
