---
type: comp-review
comp: comp-042
reviewed_snapshot: commit:eeab5b53054b93544c428a476dad06a8f8fe2621
action_required: true
---

# Current COMP actions: comp-042

**Why blocked:** **Action required.** The central transport arithmetic is internally consistent and the JSON strictness fix is reasonable, but the artifact still needs reconciliation on three material surfaces: README omission of the new pharmacodynamic-timing caveat, incomplete/central-only A2 selectivity sensitivity over route concentration/Km despite those ranges being declared, and independent verification of the full §1.32 validation-protocol propagation because the supplied validation page was truncated before that section.

## Required actions

1. **Update the comp-042 README.** Add the PD-timing caveat: KPV is upstream of inflammasome firing while GSDMD pores form downstream, so pore influx is not therapeutic-timing sufficiency. Verification criterion: README headline/verdict/limitations name both PepT1 confounding and PD timing as independent reasons KPV is the wrong proof-of-concept payload.
2. **Add or explicitly disclaim A2 sensitivity.** Either extend `analyze.py` outputs to sweep selectivity over declared `Km_used_uM` lower/central/upper and route concentration lower/central/upper, or state in README/summary/verdicts that A2 ratios are central-scenario diagnostics only. Verification criterion: no “no route clears both filters” wording is left ambiguous between central-only and full uncertainty-space claims.
3. **Document JSON `null` semantics.** Add a machine-readable note in relevant JSON outputs or README that `selectivity_ratio: null` in absent-PepT1 rows encodes mathematical infinity after strict-JSON conversion, not missing data. Verification criterion: strict JSON remains valid and downstream readers can distinguish infinite selectivity from unknown selectivity.
4. **Verify `validation-experiments.md` §1.32.** Confirm the full section reflects the comp-042 reframe: primary transporter-orphan membrane-impermeant tracer, KPV only as PepT1-confounded comparator, PepT1 inhibition/knockdown arm, and no claim that KPV efficacy via pores is established. Verification criterion: independent reviewer can inspect the full §1.32 text and mark it consistent.

The full review is available through Git history. A new exact-artifact review must pass before propagation or synthesis eligibility is restored.
