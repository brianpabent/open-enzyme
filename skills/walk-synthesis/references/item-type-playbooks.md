# Item-type playbooks

Each synthesis-queue item type has its own playbook for what action typically lands. Consult this when deciding the proposed action in Step A.

## Connections
Usually: extend an existing wiki page with a new mechanistic synthesis section, update cross-references, possibly add a bullet to a related concept page. Rarely needs a new page.

## Contradictions
Usually: either (a) document the contradiction with a stratified-guidance section in the relevant page, or (b) propose a wet-lab experiment that resolves it (then add to validation-experiments.md). Often actioned earlier in the sweep — check before re-actioning.

## Proposed Experiments
Three sub-cases:
- **Already in `validation-experiments.md`:** closure note, no new work. Most proposed experiments duplicate existing entries — check first.
- **Needs new entry:** add a new §1.X section in `validation-experiments.md`. Use the Tiered Protocol pattern (Tier 1 → gated Tier 2 → gated Tier 3) when escalating cost matters (see `templates.md` §"Tiered wet-lab protocol entry").
- **Needs computational prior first:** spawn the `new-comp-experiment` skill instead. (If it's a *literature* question, not a computation — it's a lit scan, not a comp; see `new-comp-experiment` SKILL.md §"COMP vs lit-scan".)

## Open Questions
Three sub-cases:
- **Closed by prior work:** closure note pointing at the experiment that closed it (e.g., §1.21 closed CP0 natural-product question).
- **Genuine open question, evidence thin:** queue a literature scan (Opus subagent) — see `subagent-decisions.md`.
- **Genuine open question, exploration vector:** create a dedicated scope page following the peer-track skeleton in `templates.md` — see also `engineered-lbp-chassis.md` and `sirna-urat1-modality.md` as reference shapes.

## Priority Actions
Almost always either:
- **Already done structurally** (e.g., Ward 1995 §1.9 was already #1 priority gate before the sweep re-asserted it): closure note, name the execution-bottleneck if any.
- **Needs propagation work** (e.g., supplement stratification): verify what's already there, do the propagation if needed, closure note.
- **Needs a new dedicated wiki page** (e.g., siRNA / URAT1): use the peer-track skeleton in `templates.md`.
