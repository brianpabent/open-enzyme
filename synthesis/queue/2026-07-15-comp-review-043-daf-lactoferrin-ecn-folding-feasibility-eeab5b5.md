---
type: comp-review
sweep_date: 2026-07-15
sweep_sha: eeab5b5
comp: comp-043
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-043

Canonical review log: [`logs/comp-reviews/2026-07-15-comp-043-eeab5b5.md`](../../logs/comp-reviews/2026-07-15-comp-043-eeab5b5.md)

ACTION_REQUIRED: yes

REVIEWED_SNAPSHOT: commit:eeab5b53054b93544c428a476dad06a8f8fe2621

# Independent comp review — comp-043

## Reviewed snapshot
Reviewer: OpenAI API independent review. Reviewed daemon snapshot `eeab5b53054b93544c428a476dad06a8f8fe2621`.

Snapshot matched the supplied comp-043 bundle and targeted repository reads where available. Fixed-string `grep_repo` failed because `rg` was unavailable in the tool environment, so affected-surface discovery was limited to supplied explicit pages plus targeted `read_file` calls.

## Bottom-line verdict
**Action required.** The computational artifact is internally coherent for a Phase 0 mechanistic-prior analysis, and the code/output contract is plausible by inspection. However, propagation is not clean: `wiki/computational-experiments.md` still cites `chaperone-orthogonal-stacking.md §8 item 6` for the DsbA/DsbC capacity gap, while the experiment, interpretive page, provenance, and output summary now cite **§8 item 8**. Several downstream wet-lab/hypothesis surfaces still describe EcN/LBP as a DAF fallback without carrying comp-043’s new “EcN DAF is only provisional/capacity-gated” caveat.

The quantitative verdict is **not invalidated**, but it remains a proxy-based feasibility ranking, not evidence of folding rate, titer, functional activity, or in vivo efficacy.

## Implementation and constraint closure
I traced the implemented model from inputs through `analyze.py` into both generated outputs.

**Question/model fit**
- The computation answers a bounded question: relative feasibility of EcN periplasmic disulfide-folding plus colonic protease exposure for C1-INH, DAF SCR1-4, and lactoferrin.
- It does **not** resolve actual EcN expression titer, native-fold attainment, DsbA/DsbC turnover, secretion flux, periplasmic residence time, functional complement activity, lactoferrin iron binding, or in vivo efficacy.
- The load-bearing substitution is explicit but central: **precedent-derived “effective folding demand/capacity” stands in for a measured DsbA/DsbC oxidative-folding/isomerization capacity.** This is transparently labeled, sensitivity-tested, and used to keep DAF provisional.

**Code closure**
- `disulfide_topology.json` supplies sequence length, engineering construct boundaries, folded core windows, RCL exclusion, N-glycan sites, and disulfide pairs.
- `analyze.py` asserts sequence length and verifies every disulfide coordinate is a cysteine in the supplied FASTA. It also asserts expected disulfide counts: C1-INH 2, DAF 8, lactoferrin 16.
- Effective folding demand is computed as:
  - loop-length weights: `<=50 → 1.0`, `50–150 → 1.5`, `>150 → 2.5`;
  - plus `0.5 × topological_crossings`.
- Folding verdicts are derived from demand/capacity ratios against capacity anchors 5/8/12.
- Protease axis uses `experiments/lib/protease_stability.py`: P1/P1′ sequence scan, pLDDT-window accessibility proxy, pH activity factor, and salt activity. The pH/salt fields flagged by the unused-input heuristic are mostly documentation or dynamically consumed through the protease library. `active_pH_range`, `optimal_pH`, duration, temperature, and pH range are not computationally used; they document the environment.
- Glycosylation axis is categorical and hard-coded by payload key; it is not derived from a biochemical model.

**Stored-but-unused / partially-used inputs**
- `signal_peptide`, `mature_chain`, `mature_ectodomain`, `sushi_domains`, `lobe_boundaries`, and `_disulfide_count_verification` are documentation/provenance inputs, not computation inputs.
- `shio_koji_conditions.pH_range`, `temperature_C`, `duration_days`, and `NaCl_pct_range` are not used; only `NaCl_pct` is used in protease scoring.
- Protease `active_pH_range` and `optimal_pH` are not used; only `ph_activity_at_shio_koji` is used.
- This is acceptable if documented as an operational panel, but the output should not imply the code integrates pH range, exposure duration, or transit kinetics.

**Constraint closure**
- **Substrates/products/cofactors:** This is not an enzyme-reaction flux model. DsbA/DsbC redox cycling, DsbB/quinone reoxidation, oxygen/redox replenishment, and periplasmic residence time are not modeled. The artifact notes capacity uncertainty but does not explicitly mass-balance redox equivalents or secretion throughput.
- **Physiological concentration vs constants:** No Km/Kd/kcat/Km-style operating constants exist in the model. The relevant “constant” is the inferred DsbA/DsbC capacity band, which is not measured.
- **Finite mass balance/replenishment/time:** No finite folding-machinery occupancy, payload production rate, secretion rate, DegP degradation competition, or residence-time model is implemented.
- **Localization/transport/access:** The analysis assumes a luminal-secreted EcN format but does not model Sec/YebF/Type I secretion topology, periplasmic hold time, outer-membrane transit, or OmpT/DegP exposure sequence. This is named as a limitation.
- **Coproducts/off-targets/safety:** Local proteolysis and missing glycans are discussed; redox burden, misfolded-protein stress, endotoxin/LBP safety, complement off-targets, and local immune activation are outside model scope.
- **Sensitivity ranges:** Folding capacity is sensitivity-tested over three anchors, and this is the dominant uncertainty. Other dominant uncertainties—redox capacity, secretion residence time, DsbC turnover, native-fold attainment, and real SASA protease accessibility—are not quantitatively swept.

## Summary-fidelity audit
**README / output summary / results JSON**
- README, `outputs/results.json`, and `outputs/summary.md` agree on the headline:
  - C1-INH: **VIABLE** on the disulfide/protease/glyco axes, with comp-037 kinetic/native-fold caveats.
  - DAF SCR1-4: **PROVISIONAL**, folding-capacity-gated.
  - Lactoferrin: **NOT-VIABLE**, folding-limited across the capacity band, with protease RED secondary.
- They consistently state the DsbA/DsbC capacity band is precedent-derived, not measured.
- They consistently warn that pLDDT is not SASA and that comp-034 exposed the proxy’s undercounting issue.
- They consistently avoid clinical claims.

**Interpretive page**
- `wiki/daf-lactoferrin-ecn-folding-feasibility-computational.md` is materially faithful to the artifact and correctly cites `chaperone-orthogonal-stacking.md §8 item 8`.
- It correctly softens C1-INH to “disulfide-axis viable” and keeps DAF provisional.
- It correctly frames glycosylation as not independently killing DAF/lactoferrin function.

**Index / affected pages**
- `wiki/computational-experiments.md` contains a stale reference in the comp-043 key findings:
  - It still says `chaperone-orthogonal-stacking.md §8 item 6`.
  - The reviewed artifact and interpretive page now say **§8 item 8**.
  - This is a required propagation fix.
- `wiki/validation-experiments.md §1.25` and `wiki/hypotheses/H05-daf-scr14-cp0-thesis.md` still use the older framing that LBP/EcN is an alternative DAF route if koji routing fails. That is not necessarily wrong, but comp-043 requires a caveat: EcN DAF SCR1-4 is **capacity-gated/provisional**, not an unqualified fallback.
- `wiki/engineered-lbp-chassis.md` already contains an appropriate comp-043 section.
- `wiki/chaperone-orthogonal-stacking.md` already contains §8 item 8 with the DsbA/DsbC capacity gap.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---|---|
| `wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/outputs/results.json` | generated output | Yes | Internally consistent with code by inspection; carries §8 item 8; verdicts match summary. |
| `wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/outputs/summary.md` | generated output | Yes | Faithful to results JSON and code; correctly labels capacity inference and limitations. |
| `wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/README.md` | changed artifact summary | Yes | Matches output summary; cites §8 item 8. |
| `wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/analyze.py` | changed executable | Yes | Implements the reported three-axis model; no execution performed. |
| `wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/inputs/provenance.md` | changed provenance | Yes | Cites §8 item 8 and names sources; primary UniProt flatfiles are not included. |
| `wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/inputs/disulfide_topology.json` | supporting input | Yes | Provides load-bearing disulfide coordinates, construct regions, glycan sites. Source claims are not independently primary-verified from included files. |
| `wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/inputs/colonic_ecn_protease_panel.json` | supporting input | Yes | Protease specificities and activity factors used; many environmental range fields are documentation-only. |
| `wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/inputs/P02788.fasta` | supporting input | Yes | Lactoferrin sequence used for length/Cys assertions. |
| `wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/inputs/P05155.fasta` | supporting input | Yes | C1-INH sequence used for length/Cys assertions. |
| `wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/inputs/P08174.fasta` | supporting input | Yes | DAF/CD55 sequence used for length/Cys assertions. |
| `wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/inputs/alphafold_P02788_plddt.json` | supporting input | Yes | Used for lactoferrin pLDDT stats/protease proxy; pLDDT≠SASA caveat remains load-bearing. |
| `wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/inputs/alphafold_P05155_plddt.json` | supporting input | Yes | Used for C1-INH pLDDT stats/protease proxy. |
| `wiki/etc/experiments/comp-043-daf-lactoferrin-ecn-folding-feasibility/inputs/alphafold_P08174_plddt.json` | supporting input | Yes | Used for DAF pLDDT stats/protease proxy. |
| `wiki/daf-lactoferrin-ecn-folding-feasibility-computational.md` | interpretive wiki page | Yes | Faithful to artifact; cites §8 item 8. |
| `wiki/computational-experiments.md` | affected index page | Partially targeted around comp-043 | **Change required:** stale §8 item 6 reference remains. |
| `wiki/chaperone-orthogonal-stacking.md` | affected mechanism page | Relevant sections inspected from supplied bundle | Already contains §8 item 8 DsbA/DsbC capacity gap. |
| `wiki/engineered-lbp-chassis.md` | affected chassis page | Supplied relevant section inspected | Already contains comp-043 bounded thesis. |
| `wiki/validation-experiments.md` | affected wet-lab queue | Targeted reads | Change required/at least caveat required in §1.25 cross-reference: EcN/LBP fallback for DAF is provisional/capacity-gated. |
| `wiki/hypotheses/H05-daf-scr14-cp0-thesis.md` | affected hypothesis card | Yes | Change required/at least caveat required: LBP peer route for DAF should inherit comp-043’s provisional capacity gate. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| C1-INH has 2 disulfides, C123-C428 and C130-C205 | `disulfide_topology.json`, `provenance.md`, `results.json` | Asserted count; coordinates verified against supplied FASTA cysteines; used in folding demand | Named as UniProt P05155 grep-verified, but UniProt flatfile not included | Internally checked against FASTA; primary annotation not independently verified here. |
| DAF SCR1-4 has 8 disulfides, all in aa 35–285 | `disulfide_topology.json`, `provenance.md`, `results.json` | Asserted count; coordinates verified against supplied FASTA cysteines; drives demand 10.0 | Named as UniProt P08174 grep-verified, but flatfile not included | Internally checked against FASTA; primary annotation not independently verified here. |
| Lactoferrin has 16 disulfides | `disulfide_topology.json`, `provenance.md`, `results.json` | Asserted count; coordinates verified against supplied FASTA cysteines; drives demand 23.5 | Named as UniProt P02788 grep-verified, but flatfile not included | Internally checked against FASTA; primary annotation not independently verified here. |
| Loop-length weights 1.0/1.5/2.5 and crossing surcharge 0.5 | `analyze.py` constants | Directly computes effective folding demand | No primary measurement; transparent model assumption | Acceptable as proxy only; not a measured DsbC kinetic model. |
| Capacity anchors 5/8/12 effective-demand units | `analyze.py`, `provenance.md`, `results.json`, summary | Directly determine C1-INH/DAF/lactoferrin folding verdicts | Precedent-derived from Fab/DsbC/SHuffle narrative; no direct DsbA/DsbC capacity source included | Load-bearing unresolved parameter; correctly forces DAF PROVISIONAL. |
| No published DsbA/DsbC capacity metric at 8–16 disulfide scale | README, `analyze.py`, provenance, outputs, interpretive page | Justifies capacity-band uncertainty and DAF label | Corpus claim in `chaperone-orthogonal-stacking.md §8 item 8`; no primary literature search reproduced here | Corpus propagation mostly correct; computational index stale as item 6. |
| Optimistic SHuffle anchor is cytoplasmic and compartment-mismatched | `results.json`, `summary.md`, interpretive page | Limitation; does not alter numeric anchor but affects interpretation | Named as reasoning from SHuffle topology; no primary source in artifact | Important caveat; correctly included. |
| pLDDT accessibility proxy | `protease_stability.py`, `analyze.py`, outputs | Directly determines protease max risk and exposed-site counts | Library caveat cites comp-034; not SASA | Acceptable as secondary axis; not sufficient for definitive protease stability. |
| Protease panel pH/salt activity | `colonic_ecn_protease_panel.json`, `protease_stability.py` | P1/P1′ scan, pH factor, NaCl factor used | Citation strings in JSON/provenance; primary sources not included | Mechanistically plausible; environmental ranges/duration not computationally integrated. |
| C1-INH glycosylation not required for luminal inhibitory function | `glyco_axis()` rationale, outputs | Hard-coded `not_required`, penalty 0.0 | Bos/Liu-style literature named in corpus, not primary-verified here | Plausible but not independently verified in this review. |
| DAF N95 glycan not function-killing | `glyco_axis()` rationale, outputs | Hard-coded `aids_not_required`, penalty 0.3 | Mechanistic rationale; no direct aglycosyl SCR1-4 demonstration included | Correctly caveated as “not affirmatively demonstrated.” |
| Lactoferrin glycosylation aids stability but does not encode iron-binding/lactoferricin function | `glyco_axis()` rationale, outputs | Hard-coded `aids_not_required`, penalty 0.3 | Sun 1999/Ward 1995 cited; primary papers not included | Plausible; folding remains dominant modeled gate. |

## Affected wiki pages
- `wiki/daf-lactoferrin-ecn-folding-feasibility-computational.md` — already consistent — matches outputs and cites §8 item 8.
- `wiki/computational-experiments.md` — **change required** — comp-043 key finding still cites `chaperone-orthogonal-stacking.md §8 item 6`; should be §8 item 8.
- `wiki/chaperone-orthogonal-stacking.md` — already consistent — §8 item 8 contains the EcN-side DsbA/DsbC capacity gap and comp-043 framing.
- `wiki/engineered-lbp-chassis.md` — already consistent — includes the bounded comp-043 EcN thesis and lactoferrin-on-koji conclusion.
- `wiki/validation-experiments.md` — change required — §1.25/DAF routing language should inherit comp-043’s caveat that EcN/LBP DAF is provisional/capacity-gated, not an unqualified fallback.
- `wiki/hypotheses/H05-daf-scr14-cp0-thesis.md` — change required — the LBP peer-route language should be updated to cite comp-043 and label EcN DAF as provisional/capacity-gated.
- `wiki/complement-c5a-gout.md` — likely change required if it still uses older “DAF to LBP peer track if reject outcome” phrasing without the comp-043 caveat; targeted read showed older DAF/LBP fallback framing in CP0 status material, but full page search was limited by tool failure.

## New connections or implications
- The comp-043 result should sharpen the **DAF wet-lab readout**: secretion alone is insufficient for any EcN DAF route. A DAF-in-EcN experiment must measure correct disulfide pairing/native fold and decay-accelerating activity, because the modeled risk is DsbC isomerization/topological mispairing, not merely secretion yield.
- The result creates an EcN-side analogue of the koji α-coefficient gap: a direct DsbA/DsbC capacity/isomerization-rate assay at 8–16 disulfides would de-risk not just DAF but any future bacterial periplasm complement-regulator payload.
- The lactoferrin conclusion reinforces chassis specialization: lactoferrin should remain a koji/fungal secretory payload unless a non-periplasmic bacterial display/secretion strategy is separately proven.

## Required actions
1. Update `wiki/computational-experiments.md` comp-043 key finding from `chaperone-orthogonal-stacking.md §8 item 6` to **§8 item 8**. Verification criterion: no comp-043-related DsbA/DsbC capacity-gap reference points to item 6.
2. Update `wiki/validation-experiments.md` §1.25 cross-reference/routing language so any EcN/LBP DAF route is explicitly **PROVISIONAL / DsbA-DsbC-capacity-gated**, not an unqualified fallback. Verification criterion: §1.25 references comp-043 or repeats its bounded caveat.
3. Update `wiki/hypotheses/H05-daf-scr14-cp0-thesis.md` to cite comp-043 in the LBP peer-track discussion and state that EcN DAF SCR1-4 is provisional secondary, while koji remains primary. Verification criterion: H05 no longer implies EcN/LBP is an automatically viable DAF route.
4. Review `wiki/complement-c5a-gout.md` for older DAF-to-LBP fallback language and add the same comp-043 caveat where needed. Verification criterion: CP0 architecture text says the two-chassis architecture stands, but EcN does not dominate koji and DAF-on-EcN is capacity-gated.
5. If primary-source verification is intended to be auditable from the artifact, commit or quote the relevant UniProt `FT DISULFID` and `FT CARBOHYD` lines used for the disulfide/glycan counts, or soften provenance wording from “verified” to “reported verified by author.” Verification criterion: an independent reviewer can reproduce the primary annotation check from committed text without external fetch.

## Review limits
- I did not execute `analyze.py`; reproducibility was assessed by static inspection only.
- Primary sources were not independently fetched. UniProt disulfide/glycan annotations, Ward 1995, Sun 1999, Bos/Liu C1-INH glycosylation claims, and protease-specific literature were available only as citation strings or corpus summaries.
- `grep_repo` failed because `rg` was not available, limiting full-corpus affected-page discovery. I used supplied explicit pages and targeted `read_file` calls instead.
- The supplied `chaperone-orthogonal-stacking.md` page was truncated in the bundle, though the relevant §8 item 8 text was present.
- Full recalculation of pLDDT statistics and protease-site lists was not performed; code/output consistency was checked by tracing implementation logic and spot-checking the load-bearing data paths.
