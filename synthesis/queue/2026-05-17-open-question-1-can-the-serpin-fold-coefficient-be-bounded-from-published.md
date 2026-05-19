---
type: open-question
sweep_date: 2026-05-17
sweep_sha: a2990bd
section_index: 1
global_index: 12
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# Can the serpin-fold α coefficient be bounded from published serpin folding kinetics without a dedicated koji calibration experiment?

1. **Can the serpin-fold α coefficient be bounded from published serpin folding kinetics without a dedicated koji calibration experiment?** The chaperone-orthogonal-stacking framework has provisional coefficients for three fold classes (CCP/SCR, Ig-like, transferrin-lobe) but none for the serpin fold that C1-INH belongs to. Serpins have a distinctive metastable fold with a β-sheet A that undergoes a dramatic conformational change upon RCL cleavage — fundamentally different kinetics from the cooperative unfolding of CCP domains or the hierarchical folding of transferrin lobes. C1-INH has only 2 disulfides (grep-verified in comp-037), making it PDI-light, but the metastable serpin fold may engage BiP/calnexin differently than any calibrated class. A literature search for "serpin folding kinetics BiP OR PDI OR endoplasmic reticulum" could bound the α coefficient from published in vitro serpin folding data (α1-antitrypsin, antithrombin III, C1-INH itself) without requiring a new koji experiment. (Context: Connection 4 above; `chaperone-orthogonal-stacking.md` §3.5.2 + §8 item 6)

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` The open question is well posed. `chaperone-orthogonal-stacking.md` already warns that α coefficients come from non-koji folding literature and do not cover C1-INH serpin architecture, while comp-037 establishes C1-INH as a now-relevant CP0 payload with only two disulfides but a metastable RCL-driven serpin mechanism. A literature-derived bound from α1-antitrypsin, antithrombin, or C1-INH folding kinetics would be useful, provided it stays explicitly labeled as non-koji extrapolation.
