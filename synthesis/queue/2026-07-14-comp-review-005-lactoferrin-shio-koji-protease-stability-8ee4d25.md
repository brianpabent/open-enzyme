---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: 8ee4d25
comp: comp-005
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-005

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-005-8ee4d25.md`](../../logs/comp-reviews/2026-07-14-comp-005-8ee4d25.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-005

## Bottom-line verdict
Action required — the artifact is deterministic and mostly internally consistent, but the quantitative verdict is a heuristic protease-vulnerability score, not a degradation/survival model. Several summary claims are stronger than the implementation supports, and later corpus knowledge (especially comp-034 / real SASA + structure-gated cleavage) exposes a load-bearing flaw in the pLDDT-as-accessibility proxy for lactoferrin’s true inter-lobe linker.

The headline **HIGH full / MODERATE mature** should be treated as a provisional sequence/structure prior only, not as a resolved answer to “will lactoferrin survive 7–14 days of shio-koji?”

## Implementation and constraint closure
What I traced:

- `analyze.py` loads:
  - `inputs/P02788.fasta`
  - `inputs/alphafold_P02788_plddt.json`
  - `inputs/protease_specificities.json`
  - shared library `wiki/etc/experiments/lib/protease_stability.py`
- Core scoring is:
  - recognition-site match by P1/P1′ lists;
  - mean pLDDT in a ±3 residue window;
  - pLDDT-derived accessibility class;
  - `risk_score = accessibility_weight × salt_residual_activity × ph_activity_factor`.
- Outputs are deterministic by inspection; no stochastic component.

Major implementation/closure findings:

1. **Model answers “predicted cleavage-site vulnerability,” not “survival over shio-koji residence time.”**  
   There is no protease concentration, lactoferrin concentration, enzyme kinetics, Km/kcat, protease abundance over 7–14 days, substrate depletion, peptide product accumulation, or time integration. The `duration_days` field is stored and printed but not mechanistically used.

2. **pLDDT is used as a burial/accessibility proxy, and the shared library now explicitly flags this as flawed.**  
   `protease_stability.py` states that high pLDDT can be a confidently predicted exposed helix and that comp-034 showed the lactoferrin inter-lobe linker was under-counted by this proxy. This is directly relevant to comp-005’s mature-protein verdict.

3. **The actual planned expression construct likely uses mature hLf, not the native mammalian signal peptide.**  
   comp-005 analyzes full UniProt P02788 including the mammalian signal peptide and frames the HIGH verdict as signal-peptide-contingent. That is acceptable as a conservative bracket, but the Open Enzyme Ward-style construct elsewhere uses glucoamylase/KEX2 processing and mature hLf logic; the native signal peptide may never be present. The artifact should not let the full-sequence HIGH score dominate operational design language unless the construct truly includes native hLf signal peptide.

4. **README contains a direct contradiction.**  
   It says “All full-sequence exposed sites are in the signal peptide,” but the same README table reports ALP exposed sites full = 21 and mature = 3. Therefore not all exposed full-sequence sites are signal-peptide sites. The supported statement is narrower: all **top-5** sites across all three proteases are in the signal peptide.

5. **Mature ALP site locations are not output.**  
   The artifact reports “ALP mature exposed sites = 3” and mature max risk 0.188, but `outputs/cleavage_sites.json` only stores top-5 full-sequence sites, all in the signal peptide. The actual mature sites are not committed in machine-readable output, so the mature verdict cannot be audited from the output alone without rerunning or reimplementing the scan.

6. **Salt interpolation ignores stored 15% NaCl measurements.**  
   `protease_specificities.json` stores 10%, 15%, and 20% residual activities. `interpolate_salt_inhibition()` uses only 10% and 20% endpoints. At 17.5% NaCl:
   - ALP endpoint interpolation gives 0.188.
   - Piecewise interpolation using the stored 15% value would give ~0.150.
   This is load-bearing because ALP mature max risk is exactly the mature-protein driver. The verdict threshold is `<0.15 LOW`, `<0.30 MODERATE`; even small changes around 0.15 matter.

7. **pH activity is manually supplied, not computed from active pH ranges.**  
   `optimal_pH`, `active_pH_range`, and pH notes are stored but unused. `ph_activity_at_shio_koji` is the load-bearing value. ALP and NPr are conservatively set to 1.0 despite shio-koji pH being outside or near the edge of their ranges. This may be intentionally conservative, but it means the numerical score is not a physiologic reaction-rate estimate.

8. **pH range mismatch exists across surfaces.**  
   Inputs and output summary use pH `4.5–5.2`; the archived wiki text says `4.5–5.0` in several places. This is minor for the current heuristic because pH is collapsed to a single per-protease factor, but it is a fidelity issue.

9. **Reaction/cofactor closure is incomplete.**
   - Protease substrate: lactoferrin sequence is scanned.
   - Protease cofactors: NPr is described as zinc-requiring, but zinc availability is not modeled.
   - Protease abundance/activity over fermentation: not modeled.
   - Water activity, salt time-course, pH time-course, matrix effects, and host protease expression dynamics: not modeled.
   - Lactoferrin glycosylation, iron state, and actual SASA: not modeled.
   - Signal peptide processing and KEX2/glucoamylase product identity: discussed but not implemented.

10. **Sensitivity ranges do not cover dominant uncertainties.**  
    The dominant uncertainties are pLDDT-vs-SASA accessibility, ALP/NPr pH activity, salt interpolation choice, actual protease abundance, signal peptide/product form, glycosylation, iron state, and time exposure. The artifact does not run a sensitivity sweep over these.

## Summary-fidelity audit
Agreement:

- `outputs/summary.md`, `README.md`, `wiki-archive.md`, and `wiki/computational-experiments.md` agree on the main headline numbers:
  - Full sequence: HIGH, max 0.388, NPr.
  - Mature aa 20–710: MODERATE, max 0.188, ALP.
  - All full-sequence top-5 sites are signal-peptide sites.
- `validation-experiments.md §1.10` correctly keeps the lactoferrin arm as a feasibility gate rather than upgrading it to a confirmation experiment.

Mismatches / overstatements:

- `README.md`: “All full-sequence exposed sites are in the signal peptide” is false because ALP has 3 mature exposed sites.
- `wiki-archive.md` and summaries imply the inter-lobe linker is the key mature-protein soft spot based on comp-005, but comp-005’s own committed output does not list mature-site positions. Later corpus material (comp-034) identifies the biologically relevant linker as full-sequence aa 353–363 / mature 334–344, high-pLDDT helical, not the pLDDT-low aa 432–445 region described in comp-005.
- The diagnostic recommendation for ~40 kDa N-lobe/C-lobe products is biologically plausible and later supported by comp-034’s focus, but it is not directly derived from the committed comp-005 output.
- The phrase “shio-koji format is likely to degrade lactoferrin” in the full-sequence verdict is too strong for a score driven by a native signal peptide that may not exist in the actual engineered product.
- `outputs/summary.md` presents 7–14 days in “conditions modeled,” but duration is not modeled.
- `computational-experiments.md` should retain the index entry but add an explicit stale/limitation note: comp-005’s pLDDT-accessibility model under-counts structured exposed helices, and comp-034 supersedes the linker-specific interpretation.

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Human lactoferrin sequence length 710 aa | `inputs/P02788.fasta`; `inputs/provenance.md`; outputs | Loaded by `load_sequence()` and scanned | FASTA present; primary UniProt fetch not independently verified here | Accept by artifact |
| Signal peptide aa 1–19 | `analyze.py` `SIGNAL_PEPTIDE_END = 19`; provenance; summaries | Used to label top-5 sites and compute mature-only scores | Citation string to UniProt annotation; feature annotation not present in FASTA | Plausible but not primary-verified |
| AlphaFold pLDDT per residue | `inputs/alphafold_P02788_plddt.json` | Used for accessibility classification and sequence stats | JSON present; AlphaFold URL cited but not independently fetched | Accept as artifact input; primary unverified |
| pLDDT ≥80 = buried, 65–80 = partial, <65 = exposed | `lib/protease_stability.py` | Central scoring determinant | Heuristic; no primary source in artifact; library caveat flags known failure | Action required — not sufficient for mature-linker claims |
| Accessibility weights 0.1 / 0.4 / 1.0 | `lib/protease_stability.py` | Multiplicative risk score | Heuristic, no calibration source | Accept only as arbitrary model parameter |
| Protease P1/P1′ specificity lists | `inputs/protease_specificities.json` | Recognition-site inclusion/exclusion | MEROPS and papers cited; primary tables not included | Plausible but unresolved |
| ALP/NPr/acid pH factors 1.0 / 1.0 / 0.30 | JSON `ph_activity_at_shio_koji` | Multiplicative risk score | Citation notes only; active pH ranges stored but unused | Action required — pH factor is manual and load-bearing |
| Salt residual activity at 17.5% NaCl | JSON salt table; `interpolate_salt_inhibition()` | Multiplicative risk score | 10/15/20 values stored; citations string only | Action required — 15% data ignored |
| Full-sequence max risk 0.388, NPr | `outputs/cleavage_sites.json`; summary | Derived from top signal-peptide NPr sites | Reproducible by code path | Internally consistent, but product-form contingent |
| Mature max risk 0.188, ALP | `outputs/cleavage_sites.json`; summary | Derived from filtered sites >19 | Mature site positions not output | Partly auditable only by rerun/reimplementation |
| “All top-5 sites are signal peptide” | Output top-5 lists | Directly visible in output | Artifact-supported | Supported |
| “All exposed full-sequence sites are signal peptide” | README | Contradicts ALP full/mature counts | Not supported | Correct |
| Inter-lobe linker pLDDT 68–81 at aa 432–445 | `outputs/summary.md`; `wiki-archive.md` | Interpretive only | Conflicts with lactoferrin page / comp-034 linker aa 353–363 high-pLDDT helix | Action required |
| Glycosylation sites N137/N478/N623 may shield | `wiki-archive.md`; summary limitations | Not implemented | Corpus-supported elsewhere; not verified in comp artifact | Limitation only, not modeled |
| Duration 7–14 days | JSON conditions; summary | Printed only | Shio-koji condition assumption | Stored but mechanistically unused |

## Affected wiki pages
- `wiki/lactoferrin-protease-stability-computational.md` — change required — add a review/staleness note that comp-005’s pLDDT-accessibility proxy is known to under-count structured exposed helices and that linker-specific interpretation is superseded/refined by comp-034.
- `wiki/computational-experiments.md` — change required — comp-005 entry should retain headline numbers but add that the mature 0.188 score is a heuristic pLDDT-proxy result, mature sites are not emitted, and comp-034 supersedes the inter-lobe-linker mechanism.
- `wiki/validation-experiments.md` — change required — §1.10 should clarify that comp-005 supports only a coarse feasibility prior; the linker-variant plate should cite comp-034 as the operative linker-risk source, not comp-005 alone. Also clarify that full-sequence HIGH may be irrelevant for mature/KEX2-processed hLf constructs.
- `wiki/lactoferrin-linker-redesign-computational.md` — already mostly consistent — it explicitly documents comp-034’s correction that pLDDT-as-accessibility failed for the lactoferrin linker.
- `wiki/lactoferrin.md` — already mostly consistent — it contains the more current comp-034/PyRosetta correction and treats wet-lab validation as required.
- `wiki/koji-endgame-strain.md` — change required — where it references lactoferrin protease risk or shio-koji delivery, distinguish mature engineered hLf product form from native full-length P02788 signal-peptide analysis.
- `wiki/engineered-koji-protocol.md` — change required — avoid broad “shio-koji preserves enzyme activity” language for heterologous lactoferrin without the §1.10 wet-lab result; comp-005 is not sufficient to guarantee Lf survival.
- `wiki/daf-lactoferrin-ecn-folding-feasibility-computational.md` — already consistent — uses comp-005 as a koji-context sibling, but its main lactoferrin conclusion is folding/chassis assignment, not comp-005’s mature risk number.

## New connections or implications
- The mature-protein MODERATE verdict appears to be driven by a small number of pLDDT-low mature N-terminal sites, while the later biologically important inter-lobe linker risk is a high-pLDDT structured helix that comp-005’s model would tend to classify as buried. This means comp-005 and comp-034 are not redundant; comp-034 identifies a different failure mode that comp-005’s model was structurally biased against detecting.
- The full-sequence HIGH verdict is most useful as a construct-design warning: do not include the native mammalian signal peptide unless the production architecture requires it. For Ward-style glucoamylase/KEX2 mature hLf, the mature-only and comp-034 results are the relevant priors.
- The stored 15% NaCl activity values create a hidden model-choice issue. Because the ALP mature score sits near a LOW/MODERATE threshold, interpolation method and ALP pH factor can change the qualitative mature verdict more than the summary conveys.
- comp-005’s output schema is insufficient for downstream redesign: it should emit all mature sites, not just full-sequence top-5 sites, so comp-034-style design can be tied directly back to the original scan.

## Required actions
1. Correct `README.md` wording: replace “All full-sequence exposed sites are in the signal peptide” with “All full-sequence top-5 sites are in the signal peptide”; verify ALP full/mature exposed-site counts remain consistent.
2. Update `outputs/cleavage_sites.json` schema or rerun artifact to include all cleavage sites or at least all mature-protein sites above a reporting threshold, with positions, regions, pLDDT windows, and risk scores. Verification criterion: ALP’s 3 mature exposed sites are visible without rerunning code.
3. Reconcile comp-005 with comp-034: add a summary note that pLDDT-accessibility under-counts high-confidence exposed helices and that comp-034 supersedes linker-specific conclusions.
4. Decide and document salt interpolation policy. If 15% NaCl values are retained in JSON, either use piecewise interpolation or explicitly justify endpoint-only interpolation. Verification criterion: ALP 17.5% residual activity is reproducible from the stated rule.
5. Separate “construct-product form” scenarios: native full-length P02788 with signal peptide, mature hLf aa 20–710, and Ward-style glucoamylase/KEX2 mature hLf. Verification criterion: validation §1.10 and affected wiki pages state which scenario each verdict applies to.
6. Add a pH-factor sensitivity or at minimum a table showing ALP/NPr scores under plausible lower pH activity factors. Verification criterion: mature verdict is reported as a range or explicitly conservative upper bound.
7. Correct pH-range mismatch (`4.5–5.0` vs `4.5–5.2`) across archive/summary/index, or explain why the wider range is used.
8. Fix reproduction path wording: README should use the actual repository path `wiki/etc/experiments/comp-005-lactoferrin-shio-koji-protease-stability` or a repo-root-relative command that works as written.

## Review limits
- I did not execute `analyze.py`; this review is by static inspection only.
- Primary sources such as UniProt feature tables, AlphaFold API, MEROPS, Koaze 1964, Ikeda 1975, and Tominaga/Tsujisaka papers were not independently fetched; provenance is mostly citation-string level.
- Repository `grep_repo` failed because `rg` was unavailable in the tool environment, so corpus search was limited to provided explicit pages plus targeted reads of major omitted pages.
- `wiki/validation-experiments.md` was provided truncated after §1.16; later sections were not needed for comp-005 but were not fully inspected.
- I did not inspect every cross-reference page in full; affected-surface conclusions are based on the artifact bundle plus targeted reads of `lactoferrin.md`, `koji-endgame-strain.md`, `engineered-koji-protocol.md`, and the comp-034/043 pages provided in the bundle.
