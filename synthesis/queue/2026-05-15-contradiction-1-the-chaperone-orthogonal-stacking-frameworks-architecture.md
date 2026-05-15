---
type: contradiction
sweep_date: 2026-05-15
sweep_sha: 9fd8d05
section_index: 1
global_index: 4
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# The chaperone-orthogonal-stacking framework’s architecture coefficients are derived from in vitro folding kinetics (Notari 2023, Schmidt 2010) and applied to in vivo *A. oryzae* ER-assisted folding — but the framework itself acknowledges that in vivo co-translational folding may be substantially faster, potentially collapsing the α range.

1. **The chaperone-orthogonal-stacking framework’s architecture coefficients are derived from in vitro folding kinetics (Notari 2023, Schmidt 2010) and applied to in vivo *A. oryzae* ER-assisted folding — but the framework itself acknowledges that in vivo co-translational folding may be substantially faster, potentially collapsing the α range.** *Speculative*. `[CHAIN-DEPTH: 1]` `[PHASE-A-MATCH: no]`
   - *Documents Connected:* `chaperone-orthogonal-stacking.md` ( §3.5, §8 item 6), `lactoferrin.md`, `daf-cd55-scr14-truncated-computational.md`
   - *Analysis:* The framework’s §3.5 derives α = 1.5–2.5 for the transferrin-lobe fold from Notari 2023’s in vitro oxidative refolding kinetics (28-cysteine hierarchical cascade from a fully denatured state). §8 item 6 explicitly notes that “in vivo ER-assisted co-translational folding with PDI acting on the nascent chain may be substantially faster, implying the transferrin-lobe α could be closer to 1.0 than 2.5 in the functional secretory context.” If true, lactoferrin’s effective PDI load drops from 24–40 to ~16, and the triple-cassette prediction shifts from the current 0.35–0.65 range upward into the augmentation-feasible gate. The calibration experiment (§1.9 + §1.25) is designed to resolve this, but until it runs, the framework’s predictions are simultaneously the best available tool and explicitly bounded by an unresolved assumption. This is a productive tension, not a flaw — but it should be surfaced as a named uncertainty in any platform document that cites the triple-cassette prediction as load-bearing.

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` This accurately captures the framework’s own caveat: `chaperone-orthogonal-stacking.md` §3.5.2 derives CCP/SCR α = 0.3–0.6 and transferrin-lobe α = 1.5–2.5 from non-koji structural or in vitro folding evidence, and §8 explicitly warns that in vivo ER-assisted co-translational folding may make the transferrin-lobe α closer to 1.0 than 2.5. The implication that lactoferrin’s effective PDI load could collapse from 24–40 toward ~16 and shift the triple-cassette prediction upward is a valid synthesis of §3.5.3 and §5.5’s 0.35–0.65 / central 0.45–0.55 prediction range. The calibration set in §3.5.4 is indeed the designed resolver.
