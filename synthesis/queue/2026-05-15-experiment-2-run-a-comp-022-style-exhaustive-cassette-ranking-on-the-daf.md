---
type: experiment
sweep_date: 2026-05-15
sweep_sha: 9fd8d05
section_index: 2
global_index: 6
pass3_verdict: Confirmed
overlap_tag: EXTENSION
---

# Run a comp-022-style exhaustive cassette ranking on the DAF SCR1-4 design space (promoters, signal peptides, codon variants, secretion scaffolds) using the same multi-model concordance gate, with real ViennaRNA MFE and ESMFold pLDDT from the start.

2. **Run a comp-022-style exhaustive cassette ranking on the DAF SCR1-4 design space (promoters, signal peptides, codon variants, secretion scaffolds) using the same multi-model concordance gate, with real ViennaRNA MFE and ESMFold pLDDT from the start.** *Cost: $0 (in silico). Time: 2–4 weeks. Decides: whether the current §1.25 single-cassette design (PamyB, amyB SP, direct secretion) is optimal, and provides a direct empirical comparison to the chaperone framework’s prediction that CCP/SCR folds require minimal PDI engagement.* `[CHAIN-DEPTH: 2]` `[PHASE-A-MATCH: no]`
   - *Rationale:* comp-022 validated the ClockBase methodology on a target where the answer was already known (comp-010’s manual design). DAF SCR1-4 is a target where the right answer is not obvious — it has 8 disulfides, 4 CCP modules, and different folding kinetics than uricase. An exhaustive ranking would either confirm the current design or surface a better one, and the ranking’s chaperone-load axis would provide an independent check on the α = 0.3–0.6 coefficient. This is the logical next application of the pattern and costs only subagent time.
   - *Dependencies:* None. Can run immediately as a comp-NNN follow-up.

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` The proposal follows directly from `uricase-cassette-ranking-computational.md` §6.3, which names DAF SCR1-4 as a future cassette where comp-022-style ranking would be more valuable because the correct architecture is not obvious and fold-quality matters. The requested “real ViennaRNA MFE and ESMFold/pLDDT from the start” is justified by comp-022 v2: ViennaRNA replaced the weak GC-clamp proxy, and the v1 top cluster survived the tighter N-of-5 gate. This is not fully new, but it turns an existing “recommended follow-up” into a concrete comp-NNN design.
