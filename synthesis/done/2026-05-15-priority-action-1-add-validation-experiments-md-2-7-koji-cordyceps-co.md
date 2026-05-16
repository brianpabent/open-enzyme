---
type: priority-action
sweep_date: 2026-05-15
sweep_sha: 8653de9
section_index: 1
global_index: 13
pass3_verdict: Push back
overlap_tag: RESTATEMENT
---

# Add `validation-experiments.md` §2.7 (Koji × *Cordyceps* co-formulation stability test) and §1.26 sixth-arm extension (engineered-koji cordycepin + GLPP) to the experiment queue.

1. **Add `validation-experiments.md` §2.7 (Koji × *Cordyceps* co-formulation stability test) and §1.26 sixth-arm extension (engineered-koji cordycepin + GLPP) to the experiment queue.** These two experiments together answer whether the koji-track cordycepin arm can achieve ADA protection without pentostatin co-engineering — the single most consequential design decision for the cordycepin sub-track. Both are low-cost ($1,500–3,000 and $500–1,000 adder, respectively) and together resolve the chassis-complexity question.

> **Pass 3 review — Push back.** `[OVERLAP: RESTATEMENT]` `[GAP: tool-gap]` The action is stale as written: `validation-experiments.md` already contains §2.7 “Koji × *Cordyceps* Co-Formulation Stability Test” and §1.26 already has the sixth-arm engineered-koji cordycepin + GLPP extension. The prioritization remains correct, but the proposed action should be changed from “add these sections” to “execute / keep prioritized,” otherwise the queue will duplicate existing experiment entries.

---

## ✓ Closed via strategic deprioritization 2026-05-16

**Walkthrough Item 18 — sections existed; both now marked Deprioritized.** Pass 3 was right that §2.7 and §1.26 sixth-arm were already in validation-experiments.md (added during the 2026-05-14/15 sweep cycle, before the walkthrough started). With koji-cordycepin engineering deprioritized via Item 7's strategic call, both sections are now marked Deprioritized in-place with explicit "do not execute" annotations pointing at [`koji-endgame-strain.md` §3.5](../../wiki/koji-endgame-strain.md) for the reasoning.

This Priority Action is therefore closed with the opposite outcome from what the synthesizer recommended: rather than "execute / keep prioritized," the action was "mark the existing sections as Deprioritized so a future operator (or daemon) doesn't try to run them." Cluster-closure: closes with Items 7, 13, 16, 17 via the same strategic call.

The Pass 3 staleness flag (`[GAP: tool-gap]` — both sections already existed) is now documented as a recurring bias in [`scripts/SWEEP-ARCHITECTURE.md` §"Recommend creating what already exists"](../../scripts/SWEEP-ARCHITECTURE.md) (Item 18 case study, paired with Item 6's static-rubric flavor of the same root pattern).
