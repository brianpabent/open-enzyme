# comp-006 — DAF/CD55 Shio-Koji Protease Stability: Summary

**Protein:** DAF/CD55 (complement decay-accelerating factor), Homo sapiens (P08174)  
**AlphaFold model:** AF-P08174-F1-model_v6  
**Signal peptide:** 1-34 (cleaved during secretion; replaced by koji-native signal in engineered construct)  
**GPI-anchor propeptide:** 354-381 (cleaved during GPI attachment in vivo; truncated in soluble ectodomain engineering construct)  
**Soluble ectodomain:** 35-353 (SCR1-4 + Ser/Thr stalk; the operationally relevant construct for koji expression)  
**Conditions modeled:** 17.5% NaCl, pH 4.5–5.2, 22°C, 7–14 days  
**Analysis date:** 2026-05-05  
**Script:** `experiments/comp-006-daf-cd55-shio-koji-protease-stability/analyze.py`  
**Library:** `experiments/lib/protease_stability.py`  

---

## Structural Overview

| Metric | Value |
|---|---|
| Sequence length | 381 aa (incl. signal peptide aa 1–34 and GPI propeptide aa 354–381) |
| Mean pLDDT (AlphaFold confidence) | 78.3 / 100 |
| Minimum pLDDT (most flexible residue) | 29.9 / 100 |
| % residues pLDDT > 80 (well-folded) | 65.9% |
| % residues pLDDT > 90 (core-folded) | 65.1% |

**CD55 structural notes:**

- Signal peptide (aa 1–34): pLDDT 43–72 — disordered throughout. Residue 34 (pLDDT 71.6) is partially exposed at the border; aa 1–33 are fully disordered.
- SCR1–SCR4 (aa 35–285): pLDDT 85–98 — well-folded. The four sushi/SCR domains are compact and structurally similar to the comp-001 uricase core.
- Ser/Thr-rich stalk (aa 286–353): pLDDT progressively drops from ~91 at aa 285 to <50 below aa 288 — fully disordered. This is the dominant structural liability for the ectodomain verdict.
- GPI-anchor propeptide (aa 354–381): pLDDT 30–52 — fully disordered. Absent from the soluble ectodomain engineering construct.

---

## Per-Protease Risk Assessment

### Alkaline protease (subtilisin-type, Alp/NpII) (`ALP`)

| Parameter | Value |
|---|---|
| Recognition sites in sequence | 260 |
| Buried (pLDDT ≥ 80) | 158 |
| Partially exposed (pLDDT 65–80) | 4 |
| Exposed (pLDDT < 65) | 98 |
| Residual activity at 17.5% NaCl | 19% |
| pH activity factor (shio-koji pH) | 100% |
| Effective protease activity (salt × pH) | 18.8% |
| Max risk score (full sequence, 0–1) | 0.188 |
| Mature protein max risk score (excl. signal peptide) | 0.188 |
| Soluble ectodomain max risk score (aa 35–353) | 0.188 |
| Ectodomain exposed sites | 48 |
| Stalk max risk score (aa 286–353) | 0.188 |
| Stalk exposed sites | 48 |

**Top 5 highest-risk cleavage sites (full sequence):**

| Position | Region | P1 | P1' | pLDDT (window) | Accessibility | Risk score |
|---|---|---|---|---|---|---|
| 1 | signal_peptide | M | T | 43.9 | exposed | 0.188 |
| 2 | signal_peptide | T | V | 45.2 | exposed | 0.188 |
| 3 | signal_peptide | V | A | 45.9 | exposed | 0.188 |
| 4 | signal_peptide | A | R | 46.2 | exposed | 0.188 |
| 5 | signal_peptide | R | P | 47.4 | exposed | 0.188 |

### Neutral metalloprotease (thermolysin-like, NpI) (`NPr`)

| Parameter | Value |
|---|---|
| Recognition sites in sequence | 100 |
| Buried (pLDDT ≥ 80) | 60 |
| Partially exposed (pLDDT 65–80) | 1 |
| Exposed (pLDDT < 65) | 39 |
| Residual activity at 17.5% NaCl | 39% |
| pH activity factor (shio-koji pH) | 100% |
| Effective protease activity (salt × pH) | 38.8% |
| Max risk score (full sequence, 0–1) | 0.388 |
| Mature protein max risk score (excl. signal peptide) | 0.388 |
| Soluble ectodomain max risk score (aa 35–353) | 0.388 |
| Ectodomain exposed sites | 9 |
| Stalk max risk score (aa 286–353) | 0.388 |
| Stalk exposed sites | 9 |

**Top 5 highest-risk cleavage sites (full sequence):**

| Position | Region | P1 | P1' | pLDDT (window) | Accessibility | Risk score |
|---|---|---|---|---|---|---|
| 2 | signal_peptide | T | V | 45.2 | exposed | 0.388 |
| 3 | signal_peptide | V | A | 45.9 | exposed | 0.388 |
| 7 | signal_peptide | S | V | 49.0 | exposed | 0.388 |
| 9 | signal_peptide | P | A | 48.7 | exposed | 0.388 |
| 10 | signal_peptide | A | A | 47.9 | exposed | 0.388 |

### Acid protease (aspergillopepsin I) (`acid_protease`)

| Parameter | Value |
|---|---|
| Recognition sites in sequence | 42 |
| Buried (pLDDT ≥ 80) | 25 |
| Partially exposed (pLDDT 65–80) | 0 |
| Exposed (pLDDT < 65) | 17 |
| Residual activity at 17.5% NaCl | 65% |
| pH activity factor (shio-koji pH) | 30% |
| Effective protease activity (salt × pH) | 19.5% |
| Max risk score (full sequence, 0–1) | 0.195 |
| Mature protein max risk score (excl. signal peptide) | 0.195 |
| Soluble ectodomain max risk score (aa 35–353) | 0.195 |
| Ectodomain exposed sites | 1 |
| Stalk max risk score (aa 286–353) | 0.195 |
| Stalk exposed sites | 1 |

**Top 5 highest-risk cleavage sites (full sequence):**

| Position | Region | P1 | P1' | pLDDT (window) | Accessibility | Risk score |
|---|---|---|---|---|---|---|
| 3 | signal_peptide | V | A | 45.9 | exposed | 0.195 |
| 10 | signal_peptide | A | A | 47.9 | exposed | 0.195 |
| 11 | signal_peptide | A | L | 47.2 | exposed | 0.195 |
| 14 | signal_peptide | L | L | 46.4 | exposed | 0.195 |
| 17 | signal_peptide | E | L | 48.9 | exposed | 0.195 |

---

## Overall Risk Verdict

| Scope | Verdict | Max risk score | Worst protease |
|---|---|---|---|
| Full sequence (aa 1–381, incl. signal peptide + propeptide) | **HIGH** | 0.388 | `NPr` |
| Mature protein (aa 35–381, excl. signal peptide) | **HIGH** | 0.388 | `NPr` |
| Soluble ectodomain (aa 35–353, excl. signal peptide + propeptide) | **HIGH** | 0.388 | `NPr` |

**Full-sequence verdict: HIGH** — significant protease risk; disordered regions are high-accessibility targets

**Mature-protein verdict: HIGH** — significant risk to mature CD55 independent of signal peptide processing

**Soluble ectodomain verdict: HIGH** — significant risk to the soluble ectodomain; the stalk region drives the verdict and warrants engineering attention

The soluble ectodomain verdict is the operationally relevant figure for the koji engineering question. The engineered construct replaces aa 1–34 (human signal peptide) with a koji-native secretion signal and terminates at aa 353, omitting the GPI-anchor propeptide (aa 354–381). Whether the stalk (aa 286–353) is retained or truncated further is an engineering choice — the stalk is required for membrane-proximal complement regulation in the native context but its requirement for ectodomain folding or activity in a soluble secreted form is unknown.

### Key structural factors

**Signal peptide (aa 1–34):** pLDDT 43–72 throughout — fully disordered. Highest-risk sites in the full-sequence analysis map here. In the engineered construct, the human signal peptide is replaced with the koji-native α-amylase signal (Ward 1995), so this region is not present in the expressed product.

**SCR1–SCR4 (aa 35–285):** pLDDT 85–98 — well-folded, comparable to uricase (comp-001). The four sushi domains are compact, disulfide-stabilized (3 disulfides per SCR), and represent structurally resistant regions. Recognition sites here are largely buried. Note: disulfide bonds are not modelled in this analysis — see Limitations.

**Ser/Thr-rich stalk (aa 286–353):** pLDDT drops sharply from ~91 at aa 285 to <65 by aa 288, and remains fully disordered (pLDDT 30–52) through aa 353. This is the dominant structural liability within the soluble ectodomain. In vivo, this region carries extensive O-linked glycans that likely shield the backbone; A. oryzae O-glycosylation patterns differ substantially from mammalian and may not provide the same shielding.

**GPI-anchor propeptide (aa 354–381):** pLDDT 30–52 — fully disordered. Present in the full-sequence and mature-protein verdicts, absent in the soluble ectodomain verdict. In the native context, this region is post-translationally cleaved during GPI attachment.

### Limitations

- **Disulfide bonds not modelled.** Each SCR domain contains 3 conserved disulfide bonds (6 Cys per domain). Disulfide cross-linking substantially reduces backbone flexibility and proteolytic accessibility beyond what pLDDT alone captures. This analysis likely **overestimates risk in the SCR domains** relative to the disulfide-bonded native fold.
- **O-glycosylation of the stalk not modelled.** The Ser/Thr-rich stalk (aa 286–353) carries dense O-linked glycans in the native context. Glycans sterically shield the polypeptide backbone; A. oryzae O-glycosylation may differ from mammalian. If the stalk is expressed without glycans or with non-shielding glycans, backbone accessibility increases. Stalk risk is likely **underestimated by this analysis for non-glycosylated constructs** and possibly overestimated for fully glycosylated constructs.
- **Stalk engineering option.** The stalk (aa 286–353) is a linker between SCR4 and the GPI anchor — it has no known enzymatic or binding function. A soluble ectodomain construct could truncate at aa 285 (end of SCR4), removing the stalk entirely. This would eliminate the dominant disordered region and likely shift the verdict toward LOW. comp-006 does not model the truncated variant; a comp-007 analysis of the SCR1-4-only construct (aa 35–285) would be the logical follow-up.
- **pLDDT ≠ solvent accessibility.** Stalk pLDDT accurately predicts disorder; SCR pLDDT 85–98 predicts well-folded but SASA calculation would quantify surface exposure of buried-vs-solvent-accessible loops more precisely.
- **P1/P1' rules only.** Extended subsite specificity (P2–P4) not modelled; may over-count recognition sites in the SCR domains.
- **ALP and NPr pH factors conservatively set to 1.0.** ALP is outside its active range (6–12) at shio-koji pH 4.5–5.0; NPr is at the lower edge. True activity of both is lower than modelled; risk is conservatively overstated for both.

### Comparison with comp-001 (uricase) and comp-005 (lactoferrin)

| Feature | Uricase (comp-001) | Lactoferrin (comp-005) | CD55 ectodomain (comp-006) |
|---|---|---|---|
| Analyzed length | 301 aa | 710 aa | 381 aa |
| Mean pLDDT | 97.1 | 95.0 | 78.3 |
| Min pLDDT | 80.5 | 35.8 | 29.9 |
| % residues pLDDT > 80 | 100% | 96.1% | 65.9% |
| Signal peptide | None | Present (aa 1–19) | Present (aa 1–34) |
| GPI propeptide / other disordered region | None | Inter-lobe linker (partial) | GPI propeptide + stalk (both fully disordered) |
| Disulfide bonds | Uricase has no Cys | 2 per lobe (functional) | 3 per SCR domain (12 total in SCR1-4) |
| Full-sequence verdict | LOW | HIGH | see output |
| Mature-protein verdict | LOW | MODERATE | see output |
| Soluble ectodomain verdict | N/A | N/A | **HIGH** (max 0.388) |

---

*Generated by `analyze.py` on 2026-05-05. Uses experiments/lib/protease_stability.py. Re-run after any AlphaFold model update or MEROPS specificity revision. See inputs/provenance.md for data sources.*
