# comp-005 — Lactoferrin Shio-Koji Protease Stability: Summary

**Protein:** Lactoferrin (lactotransferrin), Homo sapiens (P02788)  
**AlphaFold model:** AF-P02788-F1-model_v6  
**Signal peptide:** 1-19 (cleaved during mammalian secretion; retention in A. oryzae expression context uncertain)  
**Conditions modeled:** 17.5% NaCl, pH 4.5–5.2, 22°C, 7–14 days  
**Analysis date:** 2026-05-05  
**Script:** `experiments/comp-005-lactoferrin-shio-koji-protease-stability/analyze.py`  
**Library:** `experiments/lib/protease_stability.py`  

---

## Structural Overview

| Metric | Value |
|---|---|
| Sequence length | 710 aa (incl. signal peptide aa 1–19) |
| Mean pLDDT (AlphaFold confidence) | 95.0 / 100 |
| Minimum pLDDT (most flexible residue) | 35.8 / 100 |
| % residues pLDDT > 80 (well-folded) | 96.1% |
| % residues pLDDT > 90 (core-folded) | 94.1% |

**Contrast with uricase (comp-001):** Uricase had mean pLDDT 97.1 and minimum 80.5 — 100% of residues well-folded. Lactoferrin's mean of 95.0 and minimum of 35.8 reflect two structurally distinct soft spots: (1) the signal peptide (aa 1–19, pLDDT 35–54, fully disordered) and (2) the inter-lobe linker (approx aa 432–445, pLDDT 68–81, partially exposed). These are the structural entry points uricase lacked entirely.

---

## Per-Protease Risk Assessment

### Alkaline protease (subtilisin-type, Alp/NpII) (`ALP`)

| Parameter | Value |
|---|---|
| Recognition sites in sequence | 492 |
| Buried (pLDDT ≥ 80) | 467 |
| Partially exposed (pLDDT 65–80) | 4 |
| Exposed (pLDDT < 65) | 21 |
| Residual activity at 17.5% NaCl | 19% |
| pH activity factor (shio-koji pH) | 100% |
| Effective protease activity (salt × pH) | 18.8% |
| Max risk score (0–1) | 0.188 |

| Mature-protein max risk score (excl. signal peptide) | 0.188 |
| Mature-protein exposed sites (excl. signal peptide) | 3 |

**Top 5 highest-risk cleavage sites (full sequence incl. signal peptide):**

| Position | Region | P1 | P1' | pLDDT (window) | Accessibility | Risk score |
|---|---|---|---|---|---|---|
| 1 | signal_peptide | M | K | 48.8 | exposed | 0.188 |
| 2 | signal_peptide | K | L | 48.6 | exposed | 0.188 |
| 3 | signal_peptide | L | V | 48.2 | exposed | 0.188 |
| 4 | signal_peptide | V | F | 48.1 | exposed | 0.188 |
| 5 | signal_peptide | F | L | 47.4 | exposed | 0.188 |

### Neutral metalloprotease (thermolysin-like, NpI) (`NPr`)

| Parameter | Value |
|---|---|
| Recognition sites in sequence | 234 |
| Buried (pLDDT ≥ 80) | 219 |
| Partially exposed (pLDDT 65–80) | 1 |
| Exposed (pLDDT < 65) | 14 |
| Residual activity at 17.5% NaCl | 39% |
| pH activity factor (shio-koji pH) | 100% |
| Effective protease activity (salt × pH) | 38.8% |
| Max risk score (0–1) | 0.388 |

| Mature-protein max risk score (excl. signal peptide) | 0.155 |
| Mature-protein exposed sites (excl. signal peptide) | 0 |

**Top 5 highest-risk cleavage sites (full sequence incl. signal peptide):**

| Position | Region | P1 | P1' | pLDDT (window) | Accessibility | Risk score |
|---|---|---|---|---|---|---|
| 2 | signal_peptide | K | L | 48.6 | exposed | 0.388 |
| 3 | signal_peptide | L | V | 48.2 | exposed | 0.388 |
| 4 | signal_peptide | V | F | 48.1 | exposed | 0.388 |
| 5 | signal_peptide | F | L | 47.4 | exposed | 0.388 |
| 6 | signal_peptide | L | V | 46.9 | exposed | 0.388 |

### Acid protease (aspergillopepsin I) (`acid_protease`)

| Parameter | Value |
|---|---|
| Recognition sites in sequence | 128 |
| Buried (pLDDT ≥ 80) | 118 |
| Partially exposed (pLDDT 65–80) | 0 |
| Exposed (pLDDT < 65) | 10 |
| Residual activity at 17.5% NaCl | 65% |
| pH activity factor (shio-koji pH) | 30% |
| Effective protease activity (salt × pH) | 19.5% |
| Max risk score (0–1) | 0.195 |

| Mature-protein max risk score (excl. signal peptide) | 0.02 |
| Mature-protein exposed sites (excl. signal peptide) | 0 |

**Top 5 highest-risk cleavage sites (full sequence incl. signal peptide):**

| Position | Region | P1 | P1' | pLDDT (window) | Accessibility | Risk score |
|---|---|---|---|---|---|---|
| 3 | signal_peptide | L | V | 48.2 | exposed | 0.195 |
| 4 | signal_peptide | V | F | 48.1 | exposed | 0.195 |
| 5 | signal_peptide | F | L | 47.4 | exposed | 0.195 |
| 6 | signal_peptide | L | V | 46.9 | exposed | 0.195 |
| 7 | signal_peptide | V | L | 45.4 | exposed | 0.195 |

---

## Overall Risk Verdict

| Scope | Verdict | Max risk score | Worst protease |
|---|---|---|---|
| Full sequence (incl. signal peptide) | **HIGH** | 0.388 | `NPr` |
| Mature protein only (aa 20–710) | **MODERATE** | 0.188 | `ALP` |

**Full-sequence verdict: HIGH** — significant protease risk; shio-koji format is likely to degrade lactoferrin

**Mature-protein verdict: MODERATE** — partial degradation of the mature protein is possible even after signal peptide cleavage

All full-sequence top-5 sites are in the signal peptide (aa 1–19, pLDDT 35–54). If A. oryzae signal peptidase processes the heterologous lactoferrin signal peptide, the operative risk is MODERATE (0.188 max). If signal peptide is retained (uncertain), full-sequence verdict (HIGH) applies.

### Key structural factors

**Signal peptide (aa 1–19):** pLDDT 35–54 throughout — fully disordered. If the signal peptide is retained in the A. oryzae expression product (i.e., not cleaved by the host secretory machinery), these residues are fully exposed and represent high-accessibility cleavage targets. In the native mammalian context the signal peptide is co-translationally cleaved; A. oryzae has its own signal peptidase activity but processing of heterologous signal sequences is not guaranteed.

**Inter-lobe linker (approx aa 432–445):** pLDDT 68–81 — partially exposed. This region connects the N-lobe and C-lobe of lactoferrin and is structurally less constrained than either lobe core. Partial exposure here means recognition sites in this window have non-trivial accessibility scores, unlike the buried sites that dominate the uricase analysis.

**Lobe cores (majority of residues):** pLDDT 88–99 — well-folded. The two lobes themselves are tightly folded, comparable to uricase. Protease risk within the lobe cores is low.

### Limitations

- pLDDT ≠ solvent accessibility. Signal peptide pLDDT scores accurately predict disorder; linker region pLDDT 68–81 indicates partial exposure but SASA calculation would quantify it.
- Signal peptide processing in A. oryzae is uncertain. If cleaved, the exposed aa 1–19 region is removed and risk drops. If retained, it is the dominant vulnerability.
- Glycosylation not modelled. Native lactoferrin carries N-linked glycans that may shield surface-accessible sites; heterologously expressed lactoferrin in A. oryzae may have different glycosylation patterns than the native human protein.
- P1/P1' rules only. Extended subsite specificity (P2–P4) not modelled.
- ALP and NPr pH factors conservatively set to 1.0 (see comp-001 limitations). True risk from ALP/NPr is lower than computed.
- Iron-binding state not modelled. Apo-lactoferrin (iron-free) adopts a more open conformation than holo-lactoferrin, potentially exposing additional surface residues. Iron availability in shio-koji is uncertain; this analysis models the AlphaFold holo-like structure.

### Comparison with comp-001 (uricase)

| Feature | Uricase (comp-001) | Lactoferrin (comp-005) |
|---|---|---|
| Mean pLDDT | 97.1 | 95.0 |
| Min pLDDT | 80.5 | 35.8 |
| % residues pLDDT > 80 | 100% | 96.1% |
| Exposed sites (any protease) | 0 | see per-protease table |
| Signal peptide risk | None (not present in mature form) | Present if unprocessed |
| Inter-lobe linker | N/A (homotetramer, no bilobal structure) | Partially exposed |
| Full-sequence verdict | LOW (provisional) | HIGH |
| Mature-protein verdict (excl. signal peptide) | LOW (provisional) | MODERATE |

### Impact on §1.10 experimental framing

Unlike uricase, this analysis does **not** shift §1.10's lactoferrin arm from a feasibility gate to a confirmation experiment. Exposed sites in the signal peptide and partially exposed sites in the inter-lobe linker represent genuine structural vulnerability. The wet-lab §1.10 result for lactoferrin is the primary determination — this computational analysis identifies *where* to look (signal peptide cleavage, linker degradation) if degradation is observed.

---

*Generated by `analyze.py` on 2026-05-05. Uses experiments/lib/protease_stability.py. Re-run after any AlphaFold model update or MEROPS specificity revision. See inputs/provenance.md for data sources.*
