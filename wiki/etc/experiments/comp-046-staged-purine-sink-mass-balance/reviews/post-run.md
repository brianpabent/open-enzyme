ACTION_REQUIRED: no
REVIEWED_SNAPSHOT: ae81b0ae5766f7947cc17d22a98a3a7b2face2d0c3d61c64ec861272cf4e15bd

# Independent comp review — comp-046

## Reviewed snapshot

Reviewer `/root/comp046_post_review5`; replacement authoring-time post-run manifest SHA-256 `ae81b0ae5766f7947cc17d22a98a3a7b2face2d0c3d61c64ec861272cf4e15bd`. The canonical manifest check passed, and all 17 entries matched their recorded byte counts and SHA-256 hashes. Five design files and both generated outputs are unchanged from the prior clean review. The reviewer inspected the final deltas in `index.md`, `wiki/computational-experiments.md`, and `wiki/validation-experiments.md`; they improve Q141K/COMP claim hygiene without changing comp-046's contract. The unrelated comp-008 actions and queue remain open.

## Bottom-line verdict

**Clean with limitations.** The artifact correctly implements two separate, conditional algebraic questions: a conserved dietary fate ledger and a non-conserved endogenous capture-architecture comparison. Generated outputs match the code and fixed inputs. All prior narrative defects are closed, the index no longer uses a terminal COMP count and includes comp-047, and `synthesis/queue/comp-review-046.md` is absent.

The model remains a design-space boundary analysis rather than physiological kinetics, efficacy, or serum-urate prediction; that limitation is explicit throughout.

## Implementation and constraint closure

The dietary path closes five mutually exclusive fates against a fixed 100-unit input and asserts exact conservation. Signs, absorption cap, matched-control denominator, and reduction polarity are correct. The nine adverse cells—`0.111` of 81—are exactly the no-salvage, high-relative-base-absorption combinations across three intercept levels.

The architecture path implements the documented equations:

- Well mixed: `max(uox,pdb) + (1-overlap) × min(uox,pdb) × (1-max(uox,pdb))`
- Staged: `uox + (1-uox) × transfer × pdb`

UOX precedes PDB in the staged hypothesis, and transfer gates only the post-UOX residual. Both results are constrained to `[0,1]`. The two four-factor products are genuinely separate 81-cell grids.

`endogenous_luminal_urate_units` is stored but unused, appropriately disclosed because the endogenous structure reports fractions rather than conserved mass. `architecture_equations`, purpose text, and query strategy are documentation rather than executable parameters; the executable formulas agree with them.

The model does not implement kinetics, Km, oxygen, residence time, diffusion, biomass density, microbial turnover, re-release, cross-feeding, product toxicity, cofactors, renal compensation, colonization, inflammation, or serum dynamics. Those omissions are explicitly bounded and routed to isotope-resolved and sequential-reactor experiments.

## Summary-fidelity audit

`results.json` and `summary.md` match `analyze.py`, including:

- two independent 81-cell grids;
- the five central dietary fate values summing to 100;
- median dietary reduction `0.181`, 5th–95th percentile `-0.042–0.724`, and adverse-cell fraction `0.111`;
- central architecture captures `0.48609375` and `0.58384375`;
- architecture counts 57 staging-greater, 24 well-mixed-greater, zero equal;
- median signed architecture difference `0.010`;
- repeated warnings that grid occupancy is not probability and the structures cannot be summed into ΔSUA.

All earlier stale language is removed:

- README and provenance now define only the dietary side as a conserved ledger.
- The endogenous output object is renamed as an architecture comparison and carries `accounting_type: capture_fraction_not_conserved`.
- Computational tracking, multihop program, interpretive page, comp-031 tombstone, PDB page, purine-load page, validation page, and dashboard preserve the same boundary.
- `index.md` contains no terminal COMP-count scope label and explicitly includes comp-047.
- The resolved comp-046 queue file is deleted.
- Active-corpus searches found no residual “two conserved ledgers,” “conserves both pools,” automatic additivity, topology winner, or general staging-superiority claim.

## Generated-output and proposed-update inventory

| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-046-staged-purine-sink-mass-balance/README.md` | design | Yes | Faithful question, method, exclusions, reproduction command, and output contract. |
| `wiki/etc/experiments/comp-046-staged-purine-sink-mass-balance/analyze.py` | design | Yes | Deterministic standard-library implementation; formulas and output generation reconcile. |
| `wiki/etc/experiments/comp-046-staged-purine-sink-mass-balance/inputs/model_parameters.json` | design | Yes | Two independent four-factor grids; scenario—not empirical—levels clearly identified. |
| `wiki/etc/experiments/comp-046-staged-purine-sink-mass-balance/inputs/provenance.md` | design | Yes | Correct evidence boundary; only dietary accounting is described as conserved. |
| `wiki/etc/experiments/comp-046-staged-purine-sink-mass-balance/inputs/query-strategy.json` | design | Yes | Documentation-only query framing; consistent with scope. |
| `wiki/etc/experiments/comp-046-staged-purine-sink-mass-balance/outputs/results.json` | generated_output | Yes | Machine output matches code schema and corrected accounting distinction. |
| `wiki/etc/experiments/comp-046-staged-purine-sink-mass-balance/outputs/summary.md` | generated_output | Yes | Faithful quantitative summary with correct experimental and inference limits. |
| `index.md` | proposed_update | Yes | Corrected comp-046 summary; no terminal COMP count; comp-047 included. |
| `wiki/computational-experiments.md` | proposed_update | Yes | Comp-046 and invalidated comp-031 entries are mutually consistent. |
| `wiki/dual-chassis-ecn-pdb-uricase-computational.md` | proposed_update | Yes | Comp-031 claims fully retracted; comp-046 used only as a conditional boundary. |
| `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/README.md` | proposed_update | Yes | Clean invalidation tombstone; no result or architecture recommendation survives. |
| `wiki/etc/experiments/comp-031-dual-chassis-ecn-pdb-uricase-additive-sua/outputs/summary.md` | proposed_update | Yes | Clearly identified as an invalidation record rather than reproducible generated output. |
| `wiki/gout-multihop-research-program.md` | proposed_update | Yes | Says dietary fate is conserved and endogenous architectures are separately compared. |
| `wiki/purine-degrading-bacteria.md` | proposed_update | Yes | Conditional complementarity, unresolved carbon fate, and no automatic additivity are explicit. |
| `wiki/purine-load-koji-vs-yeast.md` | proposed_update | Yes | Correctly separates biomass purines, urate, and species-resolved fate. |
| `wiki/staged-purine-sink-mass-balance-computational.md` | proposed_update | Yes | Quantitative and interpretive claims match outputs; prior ledger wording is closed. |
| `wiki/validation-experiments.md` | proposed_update | Yes | §1.34 preserves separate isotope accounting and requires residual/product/viability closure. |

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Canonical post-run snapshot | `reviews/post-run.manifest.json` | Binds all 17 reviewed entries | Local manifest check | Pass |
| Two independent 81-cell grids | Inputs and `main()` | Separate `3^4` dietary and architecture products | Fully code-derived | Pass |
| Conserved 100-unit dietary ledger | `dietary_ledger()` | Partitions five exclusive fates; assertion enforces closure | Explicit normalization, not physiology | Pass |
| Central dietary values | Results and summary | Derived from middle factor levels | Direct arithmetic | Pass; sums to 100 |
| Median reduction `0.181`; adverse fraction `0.111` | Results and summary | Derived from dietary grid | Deterministic code/output | Pass by static trace and adverse-cell enumeration |
| GR-5 benefit is conditional on retention or lower base absorption | Code and narrative | Determines reduction sign | Biological anchors named; scenario magnitudes not source-derived | Pass within model scope |
| UOX/PDB capture equations | Inputs and `architecture_capture()` | Defines architecture comparison | Explicit hypothetical equations | Pass |
| Central captures `0.48609375` / `0.58384375` | Results | Middle-level arithmetic | Direct derivation | Pass |
| Architecture counts 57/24/0 and median difference `0.010` | Results and summary | Derived from 81 architecture cases | Deterministic code/output | Pass by implementation/output reconciliation |
| `endogenous_luminal_urate_units = 100` | Inputs | Intentionally unused | Explicitly disclosed | Pass; no conserved-endogenous inference remains |
| Grid occupancy is not probability | All summary surfaces | Interpretation restriction | Explicit policy | Pass |
| No ΔSUA, topology winner, or joint three-stage efficacy | README, outputs, wiki surfaces | No such model exists | Repeated limitation | Pass |
| Reproduction path | README, code, fixed inputs | `python3 analyze.py`, standard library only | Deterministic local contract | Plausible; not executed in this review |

## Affected wiki pages

- `index.md` — already consistent; stale scope label closed and comp-047 present.
- `wiki/computational-experiments.md` — already consistent; one dietary ledger plus one endogenous comparison.
- `wiki/staged-purine-sink-mass-balance-computational.md` — already consistent; quantitative output and limitations match.
- `wiki/gout-multihop-research-program.md` — already consistent; no “conserves both pools” language.
- `wiki/purine-degrading-bacteria.md` — already consistent; complementarity conditional and carbon fate unresolved.
- `wiki/purine-load-koji-vs-yeast.md` — already consistent; species-resolved fate required.
- `wiki/dual-chassis-ecn-pdb-uricase-computational.md` — already consistent; comp-031 invalidated.
- `wiki/validation-experiments.md` — already consistent; §1.34 is the correct empirical gate.
- `wiki/open-questions.md` — already consistent; UOX/PDB topology remains open.
- `synthesis/queue/comp-review-046.md` — resolved and deleted.

## New connections or implications

None newly requiring propagation. The meaningful implication—keeping dietary isotope recovery separate from endogenous UOX/PDB residual-flux accounting—is already encoded in validation §1.34 and the active corpus.

## Required actions

None.

## Review limits

All 17 manifest entries were inspected and matched the binding snapshot. This was static, read-only review; `analyze.py` was not executed. Central arithmetic and the adverse dietary-cell count were independently checked, while complete aggregate quantiles and architecture counts were reconciled from code and committed outputs rather than independently regenerated. Primary papers named in provenance were not reopened; no numerical scenario level is represented as a primary-source estimate. The existing push-review receipt records an older snapshot and remains a separate Gate 3 concern; it is outside this authoring manifest and does not alter this clean post-run authoring verdict.
