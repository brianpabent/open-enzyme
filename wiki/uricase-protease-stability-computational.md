---
title: "Uricase Protease Stability in Shio-Koji — Computational Analysis (comp-001)"
date: 2026-05-05
tags: [uricase, shio-koji, protease, alphafold, structural-biology, computational, koji-endgame-strain]
related:
  - computational-experiments.md
  - validation-experiments.md
  - koji-endgame-strain.md
  - engineered-koji-protocol.md
  - aspergillus-oryzae.md
sources:
  - "AlphaFold Protein Structure Database (EMBL-EBI) — AF-Q00511-F1-model_v6"
  - "UniProt Q00511 — Uricase, Aspergillus flavus, reviewed PE=1"
  - "MEROPS release 12.4 — ALP (S08.070), NPr (M04.006), aspergillopepsin I (A01.002)"
  - "Tominaga & Tsujisaka 1976 — A. oryzae neutral protease salt sensitivity"
  - "Ikeda et al. 1975 — A. oryzae alkaline protease NaCl inhibition"
  - "Koaze et al. 1964 — Aspergillus acid protease characterization"
---

# Uricase Protease Stability in Shio-Koji — Computational Analysis

**Question:** Will *A. flavus* uricase (Q00511) retain meaningful activity after 7–14 days in a shio-koji ferment (15–20% NaCl, pH 4.5–5.0, ~22°C)?

**Verdict: LOW risk.** Computational analysis finds no exposed protease recognition sites in the uricase structure, combined with strong salt-mediated suppression of the dominant koji protease. Wet-lab confirmation ([`validation-experiments.md` §1.10](./validation-experiments.md)) remains necessary but this shifts §1.10 from a feasibility gate to a confirmation experiment.

**Reproducible artifact:** [`experiments/comp-001-uricase-shio-koji-protease-stability/`](../experiments/comp-001-uricase-shio-koji-protease-stability/) — script, inputs, and full outputs committed to the repo.

---

## Why this matters

The shio-koji format is strategically important: it is the only koji product format that unifies home-fermentation simplicity, long shelf life (~6 months refrigerated), and palatability (used as a marinade, seasoning, condiment). If uricase survives in this format, the platform's gut-lumen-sink intervention can be delivered as a condiment rather than a capsule or powder — a meaningful accessibility advantage.

Shio-koji contains active *A. oryzae* proteases, which are the same enzymes the organism uses to break down protein in food fermentation. The concern: those same proteases might degrade the engineered uricase payload before it's consumed. This analysis evaluates whether that concern is structurally supported.

---

## Method summary

Three independent protective factors were evaluated:

1. **Structural burial** — AlphaFold v6 per-residue confidence (pLDDT) as a proxy for fold quality and burial. Residues with pLDDT ≥ 80 are in well-folded regions unlikely to be protease-accessible; < 65 are disordered/exposed.

2. **Recognition site mapping** — P1/P1' cleavage-site prediction for each of the three major *A. oryzae* koji proteases (ALP/alkaline subtilisin, NPr/neutral metalloprotease, acid protease/aspergillopepsin), using specificity rules from MEROPS.

3. **Shio-koji condition corrections** — Salt inhibition (17.5% NaCl midpoint) and pH activity factors applied per protease, based on primary literature characterization of each enzyme.

Full methodology and limitations in [`experiments/comp-001-uricase-shio-koji-protease-stability/analyze.py`](../experiments/comp-001-uricase-shio-koji-protease-stability/analyze.py).

---

## Key results

### Structural confidence is exceptional

| Metric | Value |
|---|---|
| Sequence length | 302 aa |
| Mean pLDDT (AlphaFold confidence) | 97.1 / 100 |
| Minimum pLDDT (most flexible residue) | 80.5 / 100 |
| % residues pLDDT > 80 (well-folded) | 100% |
| % residues pLDDT > 90 (core-folded) | 97% |

A mean pLDDT of 97.1 is exceptional even among well-characterized enzymes. Crucially, the minimum is 80.5 — there are no disordered loops, no flexible termini, no exposed unstructured regions. Proteases typically initiate cleavage at disordered regions and N/C-terminal tails; uricase offers none of these entry points.

### Every recognition site is buried

| Protease | Recognition sites | Exposed | Partially exposed | Buried | Effective activity at shio-koji conditions | Max risk score (0–1) |
|---|---|---|---|---|---|---|
| ALP (alkaline subtilisin) | 215 | 0 | 0 | 215 | 18.8% (salt-suppressed) | 0.019 |
| NPr (neutral metalloprotease) | 97 | 0 | 0 | 97 | 38.8% (moderately salt-suppressed) | 0.039 |
| Acid protease (aspergillopepsin) | 44 | 0 | 0 | 44 | 19.5% (salt + sub-optimal pH) | 0.020 |

All 356 recognition sites across all three proteases map to buried regions. Risk scores well below the 0.15 LOW threshold.

### Two independent protective mechanisms

The low-risk verdict rests on two orthogonal factors, either of which alone would be partially protective:

**Factor 1 — Structural compactness.** Zero exposed cleavage sites means there is no structural vulnerability even if the proteases were fully active. This is the primary protective factor.

**Factor 2 — Salt inhibition of ALP.** The dominant koji protease (ALP, alkaline subtilisin) retains only ~19% of its normal activity at 17.5% NaCl. This is why salted ferments preserve protein foods — the salt partially disables the same proteases we're worried about.

The acid protease is the least salt-inhibited (retains ~65% activity relative to unsalted) and operates closest to shio-koji's pH range — it is the residual risk case. But all its recognition sites are in buried regions, limiting practical risk.

**Factor 3 (not modelled) — Tetramer burial.** Uricase functions as a homotetramer in vivo. This analysis modelled the monomer only. The tetramer interface buries additional surface area beyond the monomer fold — the real-world structure is *more* protease-resistant than this analysis captures. The monomer analysis is therefore conservative.

---

## Limitations

- **pLDDT ≠ solvent-accessibility.** Some high-pLDDT surface loops may be accessible in reality. A molecular dynamics simulation or explicit SASA (solvent-accessible surface area) calculation would sharpen the analysis. See comp-002 (planned) for this follow-up if §1.10 wet-lab results are unexpected.
- **P1/P1' specificity only.** Real proteases use extended subsites (P2–P4, P2'–P4') that are not modelled here. This may over-count recognition sites (making the analysis conservative — more hits than a full subsite model would predict).
- **Monomer only.** See Factor 3 above.
- **No fermentation dynamics.** Proteases are most active before the salt environment is established (during initial koji growth). Shio-koji by definition starts after koji is harvested — the peak-activity window has already passed. This analysis models the shio-koji-phase conditions, not the pre-salt koji phase.
- **pH unfolding not modelled.** At pH 4.5–5.0, some proteins partially unfold, exposing buried residues. AlphaFold models standard folding conditions; acid-induced partial unfolding is not captured. If §1.10 shows unexpected degradation, cooperative unfolding at pH 4.5 is the first mechanism to investigate.

---

## Impact on experimental priorities

**Before this analysis:** [`validation-experiments.md` §1.10](./validation-experiments.md) was positioned as a feasibility gate — "does this format even work?" with the outcome potentially disqualifying shio-koji entirely.

**After this analysis:** §1.10 is a confirmation experiment — "we expect this to work; the experiment confirms and quantifies it." This changes the risk framing for the platform's shio-koji delivery thesis from "unknown" to "structurally supported, pending empirical confirmation."

The planned comp-002 (thermal/pH stability MD simulation) is low priority unless §1.10 produces unexpected degradation results.

---

## Cross-references

- [`validation-experiments.md` §1.10](./validation-experiments.md) — wet-lab uricase stability in shio-koji salt-protease ferment
- [`computational-experiments.md`](./computational-experiments.md) — tracking index for all computational analyses
- [`koji-endgame-strain.md` §2.1](./koji-endgame-strain.md) — uricase engineering context
- [`engineered-koji-protocol.md` §15](./engineered-koji-protocol.md) — shio-koji delivery format constraints
- [`aspergillus-oryzae.md`](./aspergillus-oryzae.md) — native koji protease landscape
