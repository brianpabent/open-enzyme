PRE_RUN_GATE: GO
REVIEWED_SNAPSHOT: 5a731dea92173350d274538e51c29bbc611d2a2659731d9119badd43fcf635ad

# Adversarial pre-run review — COMP-017 maintenance

**Reviewer:** `/root/comp044_pre_rebind`

The manifest digest and every bound file matched the six-file design snapshot
and two prior-output baselines.

The maintenance rerun may proceed. The only executable change replaces one
hard-coded Sub-claim 4 rationale string. README changes clarify the current
authoring boundary and H07's retracted status. Inputs, provenance, aggregation
logic, thresholds, decision mapping, output construction, and all other result
fields are unchanged. The changed rationale cannot affect
`assemble_overall_verdict`, so the core sex-dimorphism verdict cannot change.

The authorized correction is narrow:

- H07 remains retracted.
- COMP-017 selects no intervention or stack.
- Cordycepin, each exact *Eurycoma* material, and butyrate require independent
  material-identity, exposure, and functional evidence.

The historical outputs contain the stale recommendation. A rerun should change
only that rationale in `results.json` and its rendered copy in `summary.md`;
all other fields and the core verdict should remain identical.

No required action remains before execution.
