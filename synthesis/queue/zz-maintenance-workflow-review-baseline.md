---
type: maintenance
scope: workflow-review-provenance-test
priority: last
---

# Update the reviewed-COMP provenance test after exact-review progress

## Why action remains open

`tests/test_knowledge_workflows.py::WorkflowTriggerTests::test_completed_review_baseline_preserves_real_provenance`
still expects 16 `review_completed_open_actions` records. COMP-019 and COMP-044
legitimately moved to exact-review `clean_with_limitations`, so the current
reviewed-state distribution is:

- 14 `review_completed_open_actions`
- 24 `review_completed_actioned`
- 2 `clean_with_limitations`

The test also assumes every completed receipt has a migration or
fresh-authoring `binding_mode`. Exact push-review receipts instead establish
provenance through valid authoring gates plus exact lane adjudication.

Seventeen retired/invalidated COMPs in the current unpushed batch have also had
their obsolete push receipts removed pending push-time review regeneration.
Missing exact receipts must not be silently skipped merely to make the local
test green.

## Required action

After the logical batch is pushed and push review has regenerated current
receipts:

1. update the expected distribution to 14 open, 24 actioned, and 2
   `clean_with_limitations`;
2. use `receipt.get("binding_mode")` and preserve the migration and
   fresh-authoring provenance branches;
3. add an exact-push branch requiring:
   - `authoring_gates.valid`;
   - `lane_adjudication.method == "exact push review"`; and
   - `new_artifact_review_performed is true`;
4. do not weaken the test by ignoring missing receipts; and
5. rerun the complete workflow suite against the regenerated state.

Verification criterion:
`python3 -m unittest tests.test_knowledge_workflows tests.test_sweep_pipeline tests.test_evidence_radar`
passes without provenance skips. Delete this queue file in the same commit.
