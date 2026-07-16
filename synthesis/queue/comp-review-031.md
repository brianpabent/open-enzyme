---
type: comp-review
comp: comp-031
reviewed_snapshot: commit:eeab5b53054b93544c428a476dad06a8f8fe2621
action_required: true
---

# Current COMP actions: comp-031

**Why blocked:** Action required. The invalidation direction is correct, and the main corpus pages are mostly reconciled, but the artifact contract is not clean:

## Required actions

1. Reconcile `wiki/chassis-pending-interventions.md` M1: replace “separate-strain-vs-dual-cassette engineering conclusion still stands” / “route PDB and uricase to SEPARATE strains” with language matching the interpretive page: separate strains remain an experimental option; comp-031 does not validate a two-strain recommendation; topology/staging are gated by comp-044/045/046 and validation §§1.33/1.34/1.37. Verification criterion: no remaining M1 sentence presents comp-031 substrate-competition reasoning as an active engineering recommendation.
2. Fix the generated-output reproducibility contract for `outputs/summary.md`. Either update `analyze.py` to emit the invalidation banner and clearly mark the rest as historical/frozen, or move invalidation text out of generated outputs and document that the output is historical and not to be regenerated. Verification criterion: running the stated command either reproduces the committed `summary.md` or the README explicitly says the committed invalidated summary is a manually frozen provenance file not reproducible byte-for-byte.
3. Clarify the comp artifact README/summary status. The current banner is good but should be paired with a short note before the stale YELLOW text that all following original findings are historical invalidated output, not current interpretation. Verification criterion: a reader cannot reasonably cite the old ΔSUA or engineering handoff without passing an invalidation warning.
4. If comp-031 is ever reused, rerun from a new model rather than patching the old one. Required model gates: explicit substrate/Km/residence-time UOX calculation, isotope-resolved CBT2.0 carbon fate, matched background butyrate comparators, compartment/staging terms, oxygen/H₂O₂/safety coproducts, and no serum ΔSUA mapping without a validated compartmental flux model.

The full review is available through Git history. A new exact-artifact review must pass before propagation or synthesis eligibility is restored.
