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

> **Pass 3 review — Confirmed.** `[OVERLAP: EXTENSION]` The proposal follows directly from `uricase-cassette-ranking-computational.md` §6.3, which names DAF SCR1-4 as a future cassette where comp-022-style ranking would be more valuable because the correct architecture is not obvious and fold-quality matters. The requested "real ViennaRNA MFE and ESMFold/pLDDT from the start" is justified by comp-022 v2: ViennaRNA replaced the weak GC-clamp proxy, and the v1 top cluster survived the tighter N-of-5 gate. This is not fully new, but it turns an existing "recommended follow-up" into a concrete comp-NNN design.

---

## ✓ Actioned 2026-05-15 — queued + subagent launched

Pass 3 confirmed; the recommended-follow-up has been turned into a concrete comp-NNN AND launched as a background subagent.

**Files shipped:**

- **`wiki/computational-experiments.md` Planned Analyses — `comp-030` row** added. Full brief: exhaustive enumeration of DAF SCR1-4 cassette design space (promoters × signal peptides × codon variants × secretion scaffolds, ~43,200 candidates), 5 orthogonal scoring models (CAI / ViennaRNA MFE / chaperone-load α prior / promoter×SP prior / ESMFold pLDDT), N-of-5 ≥ 4 concordance gate. Two upgrades from comp-022 v1 baked in: real ViennaRNA MFE from the start, real ESMFold (or ESM2 pseudo-pLDDT fallback) from the start — explicitly avoiding the v1 GC-clamp proxy failure (ρ = 0.241, 430/501 reranked). Independent α-coefficient check on the chaperone framework's α = 0.3–0.6 CCP/SCR prediction baked into the methodology — by examining the ESMFold pLDDT distribution across the candidate space, the predicted "low PDI load" hypothesis is empirically testable in silico.

**Subagent launched (background):**

- **Sonnet via Agent tool**, agentId `a7a9997f267cbf4c5`, briefed comprehensively (~600-word brief). Self-contained with all load-bearing context: design-space dimensions, scoring axes, BioDesignBench multi-method discipline anchor, pre-commit grep-verify gate, no `[skip-wiki-sweep]`, explicit `git add <file>` discipline (parallel session on `feature/delivery-route-matrix` may have uncommitted files in `wiki/`), instruction to commit eagerly but NOT push (batch-push held until end of walk), and clear "report back in ~600 words" cap for the eventual completion notification.
- Output artifacts the agent will produce: `wiki/etc/experiments/comp-030-daf-cassette-ranking/` (README, provenance, code, results, figures) + `wiki/daf-cd55-scr14-cassette-ranking-computational.md` wiki write-up + cross-link updates on `daf-cd55-scr14-truncated-computational.md` (comp-012) and `validation-experiments.md` §1.25.
- Subagent may produce a full 43,200-candidate ranking OR a smaller pilot with scaling notes, depending on tool availability (ViennaRNA install, ESMFold weights, etc.). Either is acceptable; the structured methodology + α-coefficient check verdict is the load-bearing deliverable.

**Per the walk-synthesis SKILL.md "auto-append review item" rule:** TaskCreate Task #8 entered as the future review step. When the subagent's completion notification arrives, the walkthrough does NOT process the result immediately — it presents the findings as a walkthrough briefing item, waits for Brian's go-ahead, then handles the closure annotation + cross-link updates per standard discipline. Item 29's queue→done has already happened (the queueing + launch was the canonical work for this walkthrough item); the comp-030 *output* is downstream.

Pass 3 verdict honored. Closing.
