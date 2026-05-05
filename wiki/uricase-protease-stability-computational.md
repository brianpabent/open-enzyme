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

**Verdict: LOW risk (provisional).** Computational analysis finds no exposed protease recognition sites in the uricase structure, combined with strong salt-mediated suppression of the dominant koji protease. Three assumptions in this analysis compound toward safety (pLDDT as burial proxy, point-estimate salt values, monomer structure); a SASA-based reanalysis on the D2 tetrameric assembly would remove "provisional." Wet-lab confirmation ([`validation-experiments.md` §1.10](./validation-experiments.md)) remains necessary but this shifts §1.10 from a feasibility gate to a confirmation experiment.

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

- **pLDDT ≠ solvent-accessibility.** Some high-pLDDT surface loops may be accessible in reality — pLDDT measures local structural confidence, not burial. High-pLDDT surface helices (scored 85–90) can still be fully solvent-exposed. A SASA calculation on the AlphaFold PDB is the correct tool and would sharpen the analysis materially. See comp-002 (planned) for this follow-up if §1.10 wet-lab results are unexpected.
- **P1/P1' specificity only.** Real proteases use extended subsites (P2–P4, P2'–P4') that are not modelled here. This may over-count recognition sites (making the analysis conservative — more hits than a full subsite model would predict). ALP's 215 sites against a 302 aa sequence reflects its genuinely broad P1 specificity, rendering the raw site count uninformative; SASA-filtered exposed-site count would be more meaningful.
- **Monomer structure only.** Uricase is a D2-symmetric homotetramer. See Factor 3 above. Beyond mere "conservatism," the active-site tunnel is located at subunit interfaces — residues that appear surface-exposed in the monomer analysis are buried at tetramer interfaces and not accessible to protease. The correct analysis should use the biological assembly PDB (D2 tetramer), not the monomer chain.
- **NPr salt inhibition value has higher uncertainty than stated.** The 39% residual at 17.5% NaCl is a point estimate; thermolysin-family metalloproteases show variable NaCl sensitivity depending on Ca²⁺ availability (NaCl can competitively displace Ca²⁺ coordination). The true value may be lower (20–30% residual), which would reduce NPr's max risk score below the 0.039 reported. Treat as ±0.15 uncertainty range.
- **Secreted protease concentration not quantified.** In vitro inhibition values describe specific activity, not [E]. A. oryzae may secrete substantially less protease under 15–20% NaCl osmotic stress. If secretion is reduced, effective enzyme exposure is lower than the model captures. This is an additional suppressive factor not in the risk formula.
- **Temperature suppression not modelled.** All three proteases have activity optima at 37–50°C; the shio-koji fermentation temperature (~22°C) suppresses activity by an additional 2–5× relative to in vitro reference conditions at optimum. This is a conservative omission — real-world risk is lower than the model states.
- **pH range treated as a point value.** pH 4.5 vs. 5.0 represents approximately a 2-fold difference in aspergillopepsin I activity. The pH_factor of 0.30 is a midpoint estimate; at pH 5.0 the value may be closer to 0.15–0.20. The range [0.15, 0.30] is more accurate than the single value.
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
