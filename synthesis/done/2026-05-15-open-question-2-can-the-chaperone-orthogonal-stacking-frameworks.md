---
type: open-question
sweep_date: 2026-05-15
sweep_sha: 9fd8d05
section_index: 2
global_index: 8
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# Can the chaperone-orthogonal-stacking framework’s architecture coefficients be calibrated from non-koji in vitro data, or do they require direct measurement of PDI residence time in *A. oryzae*?

2. **Can the chaperone-orthogonal-stacking framework’s architecture coefficients be calibrated from non-koji in vitro data, or do they require direct measurement of PDI residence time in *A. oryzae*?** The calibration set (§1.9 + §1.25) will provide an empirical test, but even a successful calibration only validates the coefficients for two fold classes in one host under one format. Generalizing to novel folds (C1-INH serpin, complestatin NRPS modules) remains extrapolation. A direct PDI-residence-time assay in *A. oryzae* microsomes would be the gold standard but is a multi-year tool-build. (context: `chaperone-orthogonal-stacking.md` §3.5, §8 item 6, §3.5.4)

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` The concern is grounded in `chaperone-orthogonal-stacking.md` §3.5.2, §3.5.4, and §8: the α coefficients are bounded extrapolations from Notari 2023, Schmidt 2010, and antibody-fold literature, not direct *A. oryzae* PDI residence-time measurements. The finding usefully distinguishes calibration of two fold classes under one host/format from generalization to future folds. I would sharpen one phrase: "complestatin NRPS modules" are not an obvious ER-folding calibration target in the same way C1-INH is, so keep the direct-PDI-residence assay framing focused on secreted disulfide-rich payloads.

---

## ✓ Actioned 2026-05-15

Pass 3 confirmed; Pass 2's substantive concern (two-fold-class calibration doesn't generalize to arbitrary novel folds) is real. Pass 3's correction (cytosolic-payload novel folds like complestatin NRPS modules bypass the question entirely — α framework only covers ER-pathway PDI competition) baked into both edits.

**Files shipped:**

- **`wiki/chaperone-orthogonal-stacking.md` §8 item 6** — new "Generalization caveat (added 2026-05-15)" paragraph appended to the existing extrapolation caveat. Names that §3.5.4 calibration set validates two fold classes only; each future secreted disulfide-rich payload (C1-INH, antibody-derived, etc.) needs its own calibration. Two resolution paths surfaced: calibration-set breadth expansion (~$3–5K + 8 weeks per new fold class, linear scaling) vs. direct PDI-residence-time assay in *A. oryzae* microsomes (multi-year tool-build, no published *A. oryzae*-specific data). Cytosolic payloads explicitly sidestep the concern via the §5.6 / koji-endgame-strain.md §3 design rule.

- **`wiki/open-questions.md` §"Compound-Specific Questions"** — new "Chaperone framework α-coefficient generalization" subsection inserted above the existing "Quantification methodology — Tier 2 inter-operator reproducibility" entry. Includes explicit "Fires when" trigger (OE wants to commit a new secreted disulfide-rich payload + α prediction is load-bearing). Pass 3's cytosolic-bypass caveat baked in. Cross-links to the framework caveat home + calibration arms + H05.

Pass 3 verdict honored. Closing.
