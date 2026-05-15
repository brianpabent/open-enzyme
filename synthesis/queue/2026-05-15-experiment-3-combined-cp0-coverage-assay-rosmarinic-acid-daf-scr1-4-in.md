---
type: experiment
sweep_date: 2026-05-15
sweep_sha: 8653de9
section_index: 3
global_index: 9
pass3_verdict: Partial
overlap_tag: EXTENSION
---

# Combined CP0 coverage assay: rosmarinic acid + DAF SCR1-4 in zymosan-activation C5a-generation model.

3. **Combined CP0 coverage assay: rosmarinic acid + DAF SCR1-4 in zymosan-activation C5a-generation model.** *Cost: $1,500–2,500. Time: 3–4 weeks. Decides:* Whether the combined two-layer CP0 strategy (Connection 3) produces additive C5a suppression relative to either intervention alone. Protocol: zymosan-activated human serum ± rosmarinic acid (10–100 μM) ± purified DAF SCR1-4 (1–10 μg/mL), measure C5a by ELISA. Additivity would justify the combined strategy and trigger comp-029 systems modeling. Specified in `complement-c5a-gout.md` §9.7 and `validation-experiments.md` §1.25 extension.

> **Pass 3 review — Partial.** `[OVERLAP: EXTENSION]` `[GAP: tool-gap]` The assay is scientifically reasonable, but the Pass 2 sequencing is wrong: `complement-c5a-gout.md` §9.7 says the rosmarinic-acid + DAF co-treatment experiment is **gated on comp-029 GREEN**, whereas the proposed experiment text says additivity would “trigger comp-029 systems modeling.” It also overstates that the arm is already specified in `validation-experiments.md` §1.25; the explicit co-treatment language lives in `complement-c5a-gout.md` §9.7, not in the §1.25 protocol text I could verify. Keep the experiment, but put comp-029 first.
