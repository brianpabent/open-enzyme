---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: 8ee4d25
comp: comp-012
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-012

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-012-8ee4d25.md`](../../logs/comp-reviews/2026-07-14-comp-012-8ee4d25.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-012

## Bottom-line verdict
Action required — the artifact is internally traceable for the aa 35–285 slice and the arithmetic that yields max score 0.039, but the quantitative LOW verdict rests on a known-invalid proxy: high AlphaFold pLDDT is treated as “buried”/protease-inaccessible. The current shared library itself now warns that this proxy can under-count real solvent-exposed, high-confidence sites. In addition, `outputs/summary.md` and `analyze.py` still contain the corrected-away hallucinated disulfide count of 12 instead of 8, so rerunning the artifact regenerates a known false statement.

## Implementation and constraint closure
I traced the central path:

- `analyze.py` loads full P08174 sequence and pLDDT, slices `full_seq[34:285]`, and rebuilds pLDDT keys 1–251 for the SCR1–4 construct. The aa 35–285 / 251-aa implementation is correct by inspection.
- Protease site finding is delegated to `wiki/etc/experiments/lib/protease_stability.py`.
- The max score 0.039 is mechanically derived as:
  - NPr salt residual at 17.5% NaCl: linear interpolation between 10% = 0.65 and 20% = 0.30 gives 0.3875 → 0.388.
  - NPr pH activity factor: stored `ph_activity_at_shio_koji = 1.0`.
  - “Buried” accessibility weight: 0.1.
  - Risk = 0.1 × 0.388 × 1.0 = 0.0388 → 0.039.

Implementation closure findings:

- **Critical hidden substitution:** the computation does not calculate solvent accessibility, protease access, cleavage kinetics, residence-time degradation, or activity retained. It substitutes **AlphaFold pLDDT confidence** for **protease accessibility**. The shared library now explicitly warns that “high pLDDT => assumed buried” is not valid and can under-count exposed helical/linker sites by ~10× in a later comp-034 audit. This caveat explicitly says it affects comp-001/005/006/012/037.
- **All 242 “buried” sites are buried only under the pLDDT proxy.** High-confidence SCR surface loops can be solvent-exposed and still score pLDDT >80. The statement “zero exposed sites” is true only in the pipeline’s proxy vocabulary, not as a physical solvent-accessibility result.
- **Stored-but-unused / output-only inputs:**
  - `active_pH_range` and `optimal_pH` are documentation only; the calculation uses only `ph_activity_at_shio_koji`.
  - `NaCl_15pct_residual_activity` is not used; interpolation uses only 10% and 20%.
  - `NaCl_pct_range`, `temperature_C`, and `duration_days` are copied into outputs but do not affect scoring.
  - No protease concentration, substrate concentration, enzyme titer, folding yield, or exposure-time term exists.
- **pH handling:** ALP and NPr are conservatively set to pH factor 1.0 despite being outside/edge-of-range for shio-koji. This may be conservative, but it is a silent model choice encoded as a single scalar, not a pH activity curve.
- **Finite mass balance / kinetics absent:** the model does not predict fraction degraded after 7–14 days, does not model protease replenishment, product accumulation, local protease peaks, or dose/activity loss.
- **Localization/access absent:** the construct is assumed available to shio-koji proteases as a folded soluble protein; secretion, folding, glycosylation, surface accessibility, aggregation, binding to matrix, and gut-lumen access are not modeled.
- **Complement-regulatory function absent:** the computation says nothing about C3b/C4b binding, convertase decay acceleration, C5a reduction, or mucosal CP0 engagement.
- **Disulfide inconsistency:** the long wiki archive and H05 correctly state 8 SCR1–4 disulfides, but `analyze.py`’s `write_summary()` and `outputs/summary.md` still state “3 conserved disulfide bonds per SCR domain … 12 total.” This is a concrete artifact error and will recur on rerun.

## Summary-fidelity audit
The artifact-summary contract is not materially clean.

Consistent elements:

- README, JSON output, index, and interpretive stub agree on the main numeric output: LOW, max score 0.039, NPr worst, 251 aa construct, 157 ALP + 60 NPr + 25 acid-protease recognition-site counts.
- The aa 35–285 truncation and mapping from local to full-sequence coordinates are implemented.
- The short interpretive page is a stub pointing to the archive, and the archive contains a correction note for the disulfide hallucination.

Mismatches / overstatements:

- **`outputs/summary.md` is stale/false on disulfides**: says 12 total; corrected corpus says 8. `analyze.py` still writes the false text.
- **README and wiki wording are stronger than the implementation supports.** Phrases such as “computationally validated,” “protease-stable,” “protease stability objection is resolved,” “first computationally validated complement regulator candidate,” and “closes the computational feasibility gate” overstate a pLDDT-only cleavage-recognition scan.
- **`computational-experiments.md` says “All 242 recognition sites buried” and “CP0 platform-gap closure thesis in silico-validated.”** This should be softened to “all sites classified as buried by the pLDDT proxy; SASA/protease-access not computed.”
- **`modality-chokepoint-matrix.md` has both updated and stale topology language.** It correctly lists comp-012 as LOW in one place, but later still says the next step is “comp-007 on the SCR1-4-only truncation … expected LOW verdict,” which is stale after comp-012.
- **`combined-cp0-systems-model-computational.md` relies on comp-012 as having “explicitly verified DAF SCR1-4 LOW protease risk” in an interaction-blocker argument.** That should be qualified as a pLDDT-proxy prior, not a solvent-accessibility or kinetic-degradation verification.
- **`complement-c5a-gout.md` and H05 use “in silico-validated fermentable engineering candidate” framing.** The wet-lab unknowns are correctly listed, but the protease-stability premise should be downgraded to a preliminary structural-confidence prior pending SASA or protease-challenge data.

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Construct is P08174 aa 35–285, length 251 aa | `analyze.py` constants `SCR14_START=35`, `SCR14_END=285`; `outputs/cleavage_sites.json` | Implemented by `full_seq[34:285]` and pLDDT remapping | Source stated as copied UniProt P08174 SV=4; primary not independently verified here | Internally correct by code; source verification unresolved |
| Full-sequence pLDDT subset aa 35–285 | `inputs/alphafold_P08174_plddt.json`; `analyze.py` pLDDT dict comprehension | Directly used for stats and site window scores | Source stated as AlphaFold v6 copied from comp-006; not primary-verified here | Implemented correctly; provenance unresolved |
| Mean pLDDT 96.7, min 85.6, 100% >80 | `outputs/cleavage_sites.json`; `outputs/summary.md` | From `compute_sequence_stats(scr14_plddt)` | Computed from committed JSON | Internally supported |
| 157 ALP, 60 NPr, 25 acid-protease recognition sites | `outputs/cleavage_sites.json`; `protease_specificities.json` | P1/P1′ scan in shared library | MEROPS/literature citation strings only; specificity not primary-verified here | Internally reproducible; biological specificity unresolved |
| All 242 recognition sites are “buried” | README; outputs; archive | Classification via `classify_accessibility(mean_plddt)` | No SASA or structure file used | Proxy-only; physical burial not established |
| Max score 0.039, NPr worst | `outputs/cleavage_sites.json`; README | `0.1 × 0.388 × 1.0`, rounded | Salt/pH factors from JSON citation strings; primary not verified | Arithmetic supported; quantitative biological meaning limited |
| NPr salt residual 0.388 at 17.5% NaCl | `protease_specificities.json`; shared lib interpolation | Linear interpolation between 10% and 20%; 15% value unused | Citation string only | Implemented; provenance unresolved |
| ALP/NPr pH factor 1.0 | `protease_specificities.json`; outputs | Direct scalar multiplier | Conservative rationale in JSON; no curve used | Implemented; dominant uncertainty not explored |
| Temperature 22°C, duration 7–14 days | `protease_specificities.json`; outputs/summary | Output only; not in risk calculation | Conditions stated, not modeled | Misleading if called “modeled” |
| 8 disulfides in SCR1–4 | `wiki-archive.md`; H05 | Not used in code | Archive says UniProt-verified, but primary not rechecked here | Corpus-corrected; not implemented |
| 12 disulfides in SCR1–4 | `analyze.py` `write_summary()`; `outputs/summary.md` | Written to summary on every rerun | Known hallucination per archive correction | False; must be fixed and rerun |
| comp-006 full ectodomain comparison 0.388, 9/48/1 stalk-exposed sites | `analyze.py` hard-coded `comp006_reference`; README | Copied into outputs and summary; not recalculated | Depends on comp-006 artifact; not reverified here | Hard-coded external dependency |
| “Protease-stable / validated / objection resolved” | README, archive, index, affected pages | Interpretive conclusion from proxy score | No SASA, kinetics, wet-lab degradation, or function | Overstated; requires softening |

## Affected wiki pages
- `wiki/etc/experiments/comp-012-daf-cd55-scr14-truncated/outputs/summary.md` — change required — contains false 12-disulfide statement and overstates pLDDT-classified sites as physically buried.
- `wiki/etc/experiments/comp-012-daf-cd55-scr14-truncated/analyze.py` — change required — regenerates the false 12-disulfide limitation text.
- `wiki/etc/experiments/comp-012-daf-cd55-scr14-truncated/README.md` — change required — numeric trace is internally consistent, but “computationally validated,” “zero exposed sites,” and “closes feasibility gate” need explicit pLDDT-proxy/SASA caveat.
- `wiki/etc/experiments/comp-012-daf-cd55-scr14-truncated/wiki-archive.md` — partially consistent / change required — correctly documents the 8-disulfide correction and pLDDT≠SASA limitation, but still uses stronger “protease-stable,” “objection resolved,” and “computational feasibility gate cleared” language than the implementation supports.
- `wiki/daf-cd55-scr14-truncated-computational.md` — change required — stub points to archive; should flag that comp-012 is a pLDDT-proxy prior pending SASA or wet-lab protease challenge, not a completed physical accessibility analysis.
- `wiki/computational-experiments.md` — change required — comp-012 entry should soften “All 242 recognition sites buried” and “CP0 platform-gap closure thesis in silico-validated”; buried means pLDDT-classified only.
- `wiki/validation-experiments.md` — already directionally consistent / minor change required — §1.25 wet-lab gate appropriately tests expression, folding, and function, but any “computational prior” text should not imply solvent-accessibility validation.
- `wiki/hypotheses/H05-daf-scr14-cp0-thesis.md` — change required — disulfide count is corrected, but “computational feasibility is in silico-validated” should be narrowed to “pLDDT/P1-P1′ protease-risk prior; SASA and wet-lab stability unresolved.”
- `wiki/complement-c5a-gout.md` — change required — CP0 status update should soften “in silico-validated fermentable engineering candidate” and “LOW protease risk” to reflect the pLDDT-proxy limitation.
- `wiki/modality-chokepoint-matrix.md` — change required — row should soften comp-012 validation language; later stale statement “next step: comp-007 on SCR1-4-only truncation, expected LOW” should be updated because comp-012 already exists.
- `wiki/combined-cp0-systems-model-computational.md` — change required — comp-029’s interaction-blocker argument should not say comp-012 “explicitly verified” DAF stability without the SASA/kinetic caveat.
- `wiki/chaperone-orthogonal-stacking.md` — change required / adjacent consistency issue — uses comp-012 as a support for DAF SCR1–4 feasibility; should distinguish folding/PDI-load reasoning from protease-access evidence. It also contains an unrelated stale lactoferrin “17 disulfides” row near §5.5.1 while later text corrects to 16.
- `wiki/daf-lactoferrin-ecn-folding-feasibility-computational.md` — already mostly consistent — explicitly notes pLDDT≠SASA and treats DAF-on-EcN as provisional; no comp-012 propagation issue beyond ensuring “koji LOW” is read as proxy-based.
- `wiki/c1-inh-protease-stability-ecn-computational.md` — already mostly consistent — cites comp-012 as sister analysis; no direct action except avoiding cross-page repetition as independent evidence.

## New connections or implications
- The later shared-library caveat from comp-034 is directly load-bearing for comp-012: a high-pLDDT SCR domain can still expose protease-accessible surface loops. This converts comp-012 from “protease stability resolved” into “candidate passes a coarse structural-confidence screen; requires SASA and/or wet-lab protease challenge.”
- The disulfide correction was propagated to the interpretive archive and H05 but not back into executable summary generation. This is a provenance anti-pattern: corrected wiki prose can diverge from rerunnable artifact output unless `analyze.py` is fixed.
- comp-012 remains useful as a **construct-boundary result**: removing aa 286–353 eliminates the low-pLDDT stalk and all pLDDT-proxy exposed stalk sites from comp-006. That narrower conclusion is stronger than the global “SCR1–4 protease-stable” conclusion.
- §1.25 is more important than the current summary suggests: it is not merely confirming expression/function after a solved protease gate; it is the first experiment that can actually test folded-form stability and activity under realistic production/ferment conditions.

## Required actions
1. Fix `analyze.py` `write_summary()` to replace the false “3 conserved disulfide bonds per SCR / 12 total” text with the corrected 8-disulfide UniProt-anchored statement, then rerun `python3 analyze.py` and recommit `outputs/summary.md`. Verification criterion: no “12 total” or “3 conserved disulfide” claim remains in comp-012 generated outputs.
2. Add an explicit model-scope caveat to README, generated summary, archive, and index: “buried” means pLDDT-classified by proxy, not SASA-computed or experimentally inaccessible. Verification criterion: comp-012 summary no longer states “zero exposed sites” without “by pLDDT proxy.”
3. Reframe the comp-012 verdict as “LOW under the pLDDT/P1-P1′ proxy model” rather than “protease-stable / validated / objection resolved.” Verification criterion: affected pages use proxy-qualified language and do not promote the result to physical protease-stability evidence.
4. Run or design a structure-based accessibility follow-up using an AlphaFold structure and SASA / surface-loop / secondary-structure protease-access scoring. Verification criterion: a new artifact reports whether the high-pLDDT SCR recognition sites are solvent-exposed and whether the 0.039 maximum survives a SASA-based model.
5. Update downstream pages that rely on comp-012 as a hard stability premise, especially `computational-experiments.md`, `complement-c5a-gout.md`, `modality-chokepoint-matrix.md`, H05, and comp-029. Verification criterion: no downstream page treats comp-012 as independent wet-lab, kinetic, or solvent-accessibility validation.
6. Correct the stale `modality-chokepoint-matrix.md` text that still says the SCR1–4 follow-up is “comp-007 … expected LOW.” Verification criterion: it names comp-012 as completed and qualified.
7. Clarify reproducibility path in README: use the actual repository-relative directory `wiki/etc/experiments/comp-012-daf-cd55-scr14-truncated/` or state the intended checkout path unambiguously. Verification criterion: a reader can follow the command without path translation.
8. Mark primary-source provenance unresolved unless direct UniProt / AlphaFold / MEROPS / salt-inhibition source verification is added to the artifact. Verification criterion: provenance distinguishes “citation string/copied from comp-006” from “directly verified in this comp.”

## Review limits
I did not execute `analyze.py`. I inspected the supplied files and the shared `protease_stability.py` library by repository read. Primary sources such as UniProt P08174, AlphaFold DB, MEROPS, Tominaga/Ikeda/Koaze papers, and comp-006 outputs were not independently verified. Repository grep tooling failed because `rg` was unavailable, so affected-page discovery used supplied references plus targeted file reads of omitted pages where possible; additional pages may contain repeated comp-012 claims.

---
## ✓ Actioned 2026-07-14
**Disposition: caveat/downgrade** (relabel/hygiene tier). Added a ⚠️ caveat banner to the interpretive page (or artifact README for comp-015) capturing the audit's headline finding — the qualitative direction holds, but the quantitative/verdict framing overstated what the model resolves. Deeper artifact fixes (reproducibility defects, provenance-tier labeling, code/summary mismatches, any recompute) remain in the Required-actions above as residuals for a focused follow-up.
