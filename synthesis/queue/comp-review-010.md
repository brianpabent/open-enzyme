---
type: comp-review
comp: comp-010
reviewed_snapshot: commit:eeab5b53054b93544c428a476dad06a8f8fe2621
action_required: true
---

# Current COMP actions: comp-010

**Why blocked:** Action required. The sequence-level LOW-risk conclusion is broadly plausible within its stated narrow scope, but the artifact-summary-wiki contract is not clean. Required fixes include a code logic bug in the Huynh comparison branch, inconsistent lactoferrin residue numbering for a proposed KEX2-site mutation, inconsistent glycosylation burden accounting, a stale `17` lactoferrin-disulfide entry in `chaperone-orthogonal-stacking.md`, and a stale generated-summary script path.

## Required actions

1. Fix `analyze_huynh_comparison()` so the “uricase has 3 cysteine residues, 0 annotated disulfides” easier-than-Huynh note is appended when `known_disulfide_bonds == 0`, not when cysteine count is zero; regenerate `outputs/cassette_analysis.json` and `outputs/summary.md`.
4. Fix the generated summary’s stale script path from `experiments/comp-010-cassette-compatibility/analyze.py` to `wiki/etc/experiments/comp-010-cassette-compatibility/analyze.py`, then regenerate.
5. Update `wiki/chaperone-orthogonal-stacking.md` §5.5.1 to remove the stale lactoferrin “17 disulfides” table entry and ensure all comp-010/Notari-derived counts are 16.
6. Mark load-bearing literature values as citation-only unless primary source text was actually verified, or add primary-source verification artifacts for LF disulfide count, Huynh titer/disulfide baseline, Ward titer, KEX2 P1′ rules, and codon-table provenance.

The full review is available through Git history. A new exact-artifact review must pass before propagation or synthesis eligibility is restored.
