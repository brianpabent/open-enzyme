---
type: comp-review
comp: comp-047
source_commit: b3c1568bca27613c8a525732bba8b95bda39ed01
propagation_eligibility: blocked
synthesis_eligibility: blocked
---

# Current independent artifact review: comp-047

Current receipt: [`wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/reviews/push-review.md`](../../wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/reviews/push-review.md)

**Why action remains open:** Action required. The reader-facing scientific conclusion is mostly bounded correctly: COMP-047 is inconclusive, produces no defensible docking-backed ranking, excludes rosuvastatin, and leaves vorinostat only as a marginal non-priority row. But deterministic binary-representation failure blocks propagation and synthesis. Additional action is needed to preserve implementation caveats: static apo-monomer docking cannot answer Q141K trafficking rescue; sensitivity coverage is narrower than stated in code; Axis-2 relationship fields are conservative exclusions, not substrate typing.

## Required actions

1. Provide inspectable text/rendered representations for every binary artifact in the push manifest, or remove nonessential binary outputs from result-bearing scope; verification criterion: a subsequent daemon review can inspect all manifest entries without deterministic blocks.
2. Tighten COMP-047 README/provenance wording where needed to say “135 attempted / 134 complete dockings,” not 135 completed results.
3. Correct or annotate the sensitivity implementation documentation: recorded perturbations are narrower than “±2 Å along each axis,” and robustness applies to fold-site rank/affinity, not the full executable margin rule.
4. Preserve Axis-2 terminology everywhere: UniProt/DrugBank = ABCG2 relationship flags; ChEMBL absence = no bounded activity record, not no substrate/inhibitor relationship.
5. If COMP-047 is ever rerun or extended, freeze raw `results.json`, ligand preparation hashes, Vina return-code/stderr logs, and live-query snapshots before postprocessing.
