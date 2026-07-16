You are performing bounded cross-page propagation for Open Enzyme.

Mission: **use red-teaming techniques to identify exploitable weaknesses in gout, and use creative engineering to exploit them.** Koji is one falsifiable track, never the project or a scope filter.

Read `CLAUDE.md`, then the exact trigger paths appended to this prompt. This is propagation, not full synthesis.

## Do

1. Extract changed claims, evidence levels, assumptions, decisions, and track status.
2. Search for direct dependents across `wiki/`, `wiki/hypotheses/`, `index.md`, and `mkdocs.yml`.
3. Keep the complete evidence in one canonical home. On other pages, add only the local decision delta and a link.
4. Rewrite contradicted claims in place. Do not leave a stale claim beside its correction.
5. Update hypothesis status, track state, dashboard, or site navigation only when the trigger changes them.
6. Verify load-bearing numbers against the named primary source before propagating them.
7. Use standard Markdown links, explicit evidence levels, and inline provenance.

## Do not

- invent a project claim in order to challenge it;
- rank tracks by narrative appeal or current chassis fit;
- copy long exposition between pages;
- add revision histories, successful-run logs, or completed queue artifacts;
- perform cross-corpus novelty search or create synthesis findings;
- edit `reference/`, HTML, workflow/code/instruction files, or `synthesis/queue/`.

Before propagating a COMP-backed trigger, read its record in `logs/sweep-state.json` and its current `reviews/push-review.json` receipt. `eligible_with_warning` is not clean: obey the receipt's `lane_adjudication.propagation_allowed_scope` and `forbidden_inferences`. When that scope says corrective-only, repair or retract stale claims but do not spread any derived claim. A `blocked` COMP is excluded by the coordinator. The coordinator handles cursor state and commits. Make no commit yourself.

Exit cleanly when every direct dependent was considered, including a legitimate no-op.
