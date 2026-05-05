# comp-012 — DAF/CD55 SCR1-4 Truncated Construct: Shio-Koji Protease Stability

**Protein:** DAF/CD55 (complement decay-accelerating factor), Homo sapiens (P08174)  
**AlphaFold model:** AF-P08174-F1-model_v6 (source; pLDDT subset to aa 35-285)  
**Construct:** SCR1-4 only (aa 35-285; stalk aa 286-353 removed)  
**Construct length analyzed:** 251 aa (aa 35–285 inclusive)  
**Conditions modeled:** 17.5% NaCl, pH 4.5–5.2, 22°C, 7–14 days  
**Analysis date:** 2026-05-05  
**Script:** `experiments/comp-012-daf-cd55-scr14-truncated/analyze.py`  
**Library:** `experiments/lib/protease_stability.py`  

---

## Overall Verdict

### DAF/CD55 SCR1-4 (aa 35–285): **LOW**

Max risk score: **0.039** (worst protease: `NPr`)  

protease degradation of the DAF/CD55 SCR1-4 construct is unlikely to meaningfully reduce activity under shio-koji fermentation conditions. The stalk truncation is validated as a stability-conferring engineering choice.

---

## Comparison with comp-006 (Full Ectodomain aa 35–353)

| Scope | Verdict | Max risk score | Worst protease |
|---|---|---|---|
| comp-006: Soluble ectodomain (aa 35–353, SCR1-4 + stalk) | **HIGH** | 0.388 | `NPr` |
| comp-012: SCR1-4 only (aa 35–285, stalk removed) | **LOW** | 0.039 | `NPr` |

**Sites eliminated by the stalk truncation (comp-006 stalk-exposed sites removed in comp-012):**

| Protease | Stalk exposed sites removed | Outcome |
|---|---|---|
| ALP (alkaline subtilisin) | 48 | All eliminated |
| NPr (neutral metalloprotease) | 9 | All eliminated |
| acid_protease (aspergillopepsin) | 1 | All eliminated |

The stalk truncation removes every exposed site from every protease in the ectodomain analysis. Only buried and partially exposed SCR-domain sites remain in comp-012.

---

## Structural Overview — SCR1-4 Construct

| Metric | Value |
|---|---|
| Sequence length analyzed | 251 aa (aa 35–285) |
| Mean pLDDT (AlphaFold confidence) | 96.7 / 100 |
| Minimum pLDDT (most flexible residue) | 85.6 / 100 |
| % residues pLDDT > 80 (well-folded) | 100.0% |
| % residues pLDDT > 90 (core-folded) | 98.8% |

**Structural notes:**

- SCR1 (aa 35–96): pLDDT 85–98 — well-folded. Inter-SCR junction (aa 83–96) pLDDT 89–96.
- SCR2 (aa 97–160): pLDDT 90–98 — well-folded. Minor dip at aa 99–102 (~91) at interdomain connection.
- SCR3 (aa 161–222): pLDDT 97–98 — the most confidently modelled region. All sites buried.
- SCR4 (aa 223–285): pLDDT 91–98 — well-folded. Minor reduction at aa 270–272 (~93–94).
- Construct terminates at aa 285 (end of SCR4). No stalk, no GPI propeptide.
- In the engineered A. oryzae construct, the human signal peptide (aa 1–34) is replaced by the koji-native α-amylase signal (Ward et al. 1995); aa 1–34 are not present in the expressed product.

---

## Per-Protease Risk Assessment

### Alkaline protease (subtilisin-type, Alp/NpII) (`ALP`)

| Parameter | Value |
|---|---|
| Recognition sites in SCR1-4 construct | 157 |
| Buried (pLDDT ≥ 80) | 157 |
| Partially exposed (pLDDT 65–80) | 0 |
| Exposed (pLDDT < 65) | 0 |
| Residual activity at 17.5% NaCl | 19% |
| pH activity factor (shio-koji pH) | 100% |
| Effective protease activity (salt × pH) | 18.8% |
| Max risk score (SCR1-4 construct, 0–1) | 0.019 |

**Top 5 highest-risk cleavage sites (SCR1-4 construct):**

| Local pos | Full-seq pos | Region | P1 | P1' | pLDDT (window) | Accessibility | Risk score |
|---|---|---|---|---|---|---|---|
| 3 | 37 | SCR1 | G | L | 94.6 | buried | 0.019 |
| 4 | 38 | SCR1 | L | P | 94.8 | buried | 0.019 |
| 8 | 42 | SCR1 | V | P | 96.6 | buried | 0.019 |
| 11 | 45 | SCR1 | A | Q | 96.6 | buried | 0.019 |
| 14 | 48 | SCR1 | A | L | 94.4 | buried | 0.019 |

### Neutral metalloprotease (thermolysin-like, NpI) (`NPr`)

| Parameter | Value |
|---|---|
| Recognition sites in SCR1-4 construct | 60 |
| Buried (pLDDT ≥ 80) | 60 |
| Partially exposed (pLDDT 65–80) | 0 |
| Exposed (pLDDT < 65) | 0 |
| Residual activity at 17.5% NaCl | 39% |
| pH activity factor (shio-koji pH) | 100% |
| Effective protease activity (salt × pH) | 38.8% |
| Max risk score (SCR1-4 construct, 0–1) | 0.039 |

**Top 5 highest-risk cleavage sites (SCR1-4 construct):**

| Local pos | Full-seq pos | Region | P1 | P1' | pLDDT (window) | Accessibility | Risk score |
|---|---|---|---|---|---|---|---|
| 3 | 37 | SCR1 | G | L | 94.6 | buried | 0.039 |
| 7 | 41 | SCR1 | D | V | 96.3 | buried | 0.039 |
| 10 | 44 | SCR1 | N | A | 96.8 | buried | 0.039 |
| 13 | 47 | SCR1 | P | A | 95.3 | buried | 0.039 |
| 14 | 48 | SCR1 | A | L | 94.4 | buried | 0.039 |

### Acid protease (aspergillopepsin I) (`acid_protease`)

| Parameter | Value |
|---|---|
| Recognition sites in SCR1-4 construct | 25 |
| Buried (pLDDT ≥ 80) | 25 |
| Partially exposed (pLDDT 65–80) | 0 |
| Exposed (pLDDT < 65) | 0 |
| Residual activity at 17.5% NaCl | 65% |
| pH activity factor (shio-koji pH) | 30% |
| Effective protease activity (salt × pH) | 19.5% |
| Max risk score (SCR1-4 construct, 0–1) | 0.02 |

**Top 5 highest-risk cleavage sites (SCR1-4 construct):**

| Local pos | Full-seq pos | Region | P1 | P1' | pLDDT (window) | Accessibility | Risk score |
|---|---|---|---|---|---|---|---|
| 7 | 41 | SCR1 | D | V | 96.3 | buried | 0.02 |
| 14 | 48 | SCR1 | A | L | 94.4 | buried | 0.02 |
| 26 | 60 | SCR1 | V | I | 96.1 | buried | 0.02 |
| 35 | 69 | SCR1 | F | V | 93.3 | buried | 0.02 |
| 45 | 79 | SCR1 | V | I | 97.0 | buried | 0.02 |

---

## Limitations

- **Disulfide bonds not modelled.** Each SCR domain contains 3 conserved disulfide bonds (6 Cys per domain, 12 total in SCR1–4). Disulfide cross-linking reduces backbone flexibility and proteolytic accessibility substantially beyond what pLDDT captures. This analysis likely **overestimates risk in the SCR domains** — partially and even some 'exposed' sites may be disulfide-locked and inaccessible in the native fold.
- **pLDDT ≠ solvent accessibility.** pLDDT 85–98 predicts well-folded regions but cannot distinguish buried residues from surface-exposed loops at domain interfaces. SASA calculation on the AlphaFold structure would refine the partially-exposed site count.
- **P1/P1' rules only.** Extended subsite specificity (P2–P4) not modelled. May over-count recognition sites in the SCR domains where extended context is unfavorable.
- **ALP and NPr pH factors conservatively set to 1.0.** ALP is outside its active range (pH 6–12) at shio-koji pH 4.5–5.0; NPr is at the lower edge. True activity is lower; risk is conservatively overstated for both.
- **CCP-regulatory activity not assessable in silico.** Whether the stalk-truncated SCR1-4 construct retains the ability to inhibit C3b deposition, accelerate CP/AP C3 convertase decay, or reduce C5a generation in a gut-lumen environment is a wet-lab question. Structural integrity is necessary but not sufficient for functional complement regulation.
- **O-glycosylation not modelled.** The SCR domains carry N-linked glycans; stalk O-glycans are absent from this construct (by design). Glycosylation patterns in A. oryzae differ from human; net effect on stability and function is unknown.

---

### Comparison with uricase (comp-001), lactoferrin (comp-005), and CD55 ectodomain (comp-006)

| Feature | Uricase (comp-001) | Lactoferrin (comp-005) | CD55 ectodomain (comp-006) | CD55 SCR1-4 (comp-012) |
|---|---|---|---|---|
| Construct length | 301 aa | 710 aa | 319 aa (aa 35–353) | 251 aa (aa 35–285) |
| Mean pLDDT | 97.1 | 95.0 | 78.3 (full ecto) | 96.7 |
| Min pLDDT | 80.5 | 35.8 | 29.9 (full ecto) | 85.6 |
| % pLDDT > 80 | 100% | 96.1% | 65.9% (full ecto) | 100.0% |
| Dominant disordered region | None | Signal peptide | Ser/Thr stalk (aa 286–353) | None (stalk removed) |
| Verdict | LOW | HIGH/MODERATE | HIGH | **LOW** |

---

*Generated by `analyze.py` on 2026-05-05. Uses experiments/lib/protease_stability.py. Re-run after any AlphaFold model update or MEROPS specificity revision. See inputs/provenance.md for data sources and the relationship to comp-006.*
