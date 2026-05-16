# comp-001 — Uricase Shio-Koji Protease Stability: Summary

**Protein:** Uricase (urate oxidase), Aspergillus flavus (Q00511)  
**Conditions modeled:** 17.5% NaCl, pH 4.5–5.2, 22°C, 7–14 days  
**Analysis date:** 2026-05-05  
**Script:** `experiments/comp-001-uricase-shio-koji-protease-stability/analyze.py`  

---

## Structural Overview

| Metric | Value |
|---|---|
| Sequence length | 302 aa |
| Mean pLDDT (AlphaFold confidence) | 97.1 / 100 |
| Minimum pLDDT (most flexible residue) | 80.5 / 100 |
| % residues pLDDT > 80 (well-folded) | 100.0% |
| % residues pLDDT > 90 (core-folded) | 97.0% |

**Interpretation:** A mean pLDDT of 97.1 with a minimum of 80.5 is exceptional — essentially the entire protein is predicted to be in a well-folded conformation with no disordered loops or flexible termini. This is the primary structural argument for protease resistance: there are no exposed unstructured regions for proteases to initiate cleavage.

---

## Per-Protease Risk Assessment

### Alkaline protease (subtilisin-type, Alp/NpII) (`ALP`)

| Parameter | Value |
|---|---|
| Recognition sites in sequence | 215 |
| Buried (pLDDT ≥ 80) | 215 |
| Partially exposed (pLDDT 65–80) | 0 |
| Exposed (pLDDT < 65) | 0 |
| Residual activity at 17.5% NaCl | 19% |
| pH activity factor (shio-koji pH) | 100% |
| Effective protease activity (salt × pH) | 18.8% |
| Max risk score (0–1) | 0.019 |

**Top 5 highest-risk cleavage sites:**

| Position | P1 | P1' | pLDDT (window) | Accessibility | Risk score |
|---|---|---|---|---|---|
| 1 | M | S | 90.8 | buried | 0.019 |
| 2 | S | A | 92.0 | buried | 0.019 |
| 3 | A | V | 92.8 | buried | 0.019 |
| 4 | V | K | 93.5 | buried | 0.019 |
| 5 | K | A | 96.0 | buried | 0.019 |

### Neutral metalloprotease (thermolysin-like, NpI) (`NPr`)

| Parameter | Value |
|---|---|
| Recognition sites in sequence | 97 |
| Buried (pLDDT ≥ 80) | 97 |
| Partially exposed (pLDDT 65–80) | 0 |
| Exposed (pLDDT < 65) | 0 |
| Residual activity at 17.5% NaCl | 39% |
| pH activity factor (shio-koji pH) | 100% |
| Effective protease activity (salt × pH) | 38.8% |
| Max risk score (0–1) | 0.039 |

**Top 5 highest-risk cleavage sites:**

| Position | P1 | P1' | pLDDT (window) | Accessibility | Risk score |
|---|---|---|---|---|---|
| 2 | S | A | 92.0 | buried | 0.039 |
| 3 | A | V | 92.8 | buried | 0.039 |
| 5 | K | A | 96.0 | buried | 0.039 |
| 6 | A | A | 97.0 | buried | 0.039 |
| 13 | N | V | 98.8 | buried | 0.039 |

### Acid protease (aspergillopepsin I) (`acid_protease`)

| Parameter | Value |
|---|---|
| Recognition sites in sequence | 44 |
| Buried (pLDDT ≥ 80) | 44 |
| Partially exposed (pLDDT 65–80) | 0 |
| Exposed (pLDDT < 65) | 0 |
| Residual activity at 17.5% NaCl | 65% |
| pH activity factor (shio-koji pH) | 30% |
| Effective protease activity (salt × pH) | 19.5% |
| Max risk score (0–1) | 0.02 |

**Top 5 highest-risk cleavage sites:**

| Position | P1 | P1' | pLDDT (window) | Accessibility | Risk score |
|---|---|---|---|---|---|
| 3 | A | V | 92.8 | buried | 0.02 |
| 6 | A | A | 97.0 | buried | 0.02 |
| 16 | V | Y | 98.5 | buried | 0.02 |
| 30 | V | Y | 97.9 | buried | 0.02 |
| 37 | V | L | 98.9 | buried | 0.02 |

---

## Overall Risk Verdict

**Overall risk: Low**

**LOW** — protease degradation in shio-koji is unlikely to meaningfully reduce uricase activity

The highest single-site risk score is 0.039 (from `NPr` — Neutral metalloprotease (thermolysin-like, NpI)). 

### Key factors driving the verdict

1. **Exceptional structural stability (pLDDT 97.1 mean, 80.5 minimum).** All potential cleavage sites in the sequence are located in confidently-folded regions. There are no disordered loops or exposed termini — the primary entry points for protease attack.
2. **Strong ALP salt inhibition.** ALP (the dominant koji protease) retains only ~10–20% activity at 15–20% NaCl. Shio-koji's defining salt level substantially neutralises the most active protease.
3. **Uricase is a homotetramer.** This analysis models the monomer. In the native quaternary structure, subunit interfaces bury additional surface area, further protecting internal residues from protease access. The monomer analysis is conservative.
4. **Acid protease is active at shio-koji pH (~4.5–5.0) but at reduced efficacy (~30% of pH-optimal).** It is also the most salt-tolerant of the three — the residual risk from the acid protease is the most meaningful of the three, but still modest given that all its recognition sites are in folded regions.

### Limitations

- pLDDT ≠ solvent accessibility. Some high-pLDDT residues on protein surface loops may still be accessible. A molecular dynamics simulation or explicit solvent-accessibility calculation would sharpen this.
- P1/P1' rules only. Real protease extended binding subsites (P2–P4) are not modelled; this may over-count recognition sites.
- Monomer structure only. Quaternary burial (tetramer interfaces) would reduce accessible surface further — this analysis is conservative.
- ALP and NPr pH factors set to 1.0 (conservative). ALP is outside its active pH range at shio-koji pH 4.5–5.0; NPr is at its lower edge. True risk from these two proteases is lower than computed.
- No fermentation dynamics. During active koji growth (before shio-koji is made), proteases operate at higher activity. The shio-koji format specifically starts after koji is harvested and mixed with salt — the peak-activity phase is before the salt environment.

### Recommended action

The structural analysis supports the hypothesis that uricase will be substantially resistant to shio-koji proteolysis. **`validation-experiments.md` §1.10 should still be run** — the experiment remains the ground truth — but this analysis shifts the prior from 'unknown' to 'probably fine', which changes the priority framing: §1.10 is a confirmation experiment, not a make-or-break feasibility gate.

If §1.10 shows unexpected degradation, the primary suspects are: (a) the acid protease operating at pH 4.5–5.0 on any surface-accessible sites; (b) cooperative unfolding of the monomer in the salt/acid environment (the structure is stable in silico under standard conditions; shio-koji conditions may differ). A follow-up comp-002 could model thermal/pH stability explicitly.

---

*Generated by `analyze.py` on 2026-05-05. Re-run after any AlphaFold model update or MEROPS specificity revision. See `inputs/provenance.md` for data sources.*
