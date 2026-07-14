---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: f7ef901
comp: comp-001
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-001

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-001-f7ef901.md`](../../logs/comp-reviews/2026-07-14-comp-001-f7ef901.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-001

## Bottom-line verdict

Action required — the artifact is reproducible by inspection as a deterministic pLDDT/P1/P1′ heuristic, but the quantitative “all sites buried / LOW protease risk / §1.10 is confirmation” contract is not clean. The implementation substitutes AlphaFold pLDDT confidence for solvent accessibility, ignores exposure time and protease concentration, and the corpus now contains comp-002 showing uricase shio-koji stability is MODERATE/YELLOW on the thermal/tetramer axis. The protease-axis conclusion may still be directionally plausible, but the stated “no exposed recognition sites” and wet-lab reprioritization are over-strong.

## Implementation and constraint closure

I traced the executable path through `analyze.py` and the repo-local shared library `wiki/etc/experiments/lib/protease_stability.py`. The comp directory inventory does not include this shared library, but `analyze.py` imports it with:

```python
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))
from protease_stability import ...
```

So the stated reproduction path depends on an external repo-local dependency, not just files in the comp folder.

Key implementation findings:

- **Core hidden substitution:** `classify_accessibility()` labels sites as `buried` solely from mean pLDDT:
  - pLDDT ≥ 80 → `buried`
  - 65–80 → `partially_exposed`
  - <65 → `exposed`
- This is physically wrong as a burial test. pLDDT is model confidence, not solvent accessibility. A high-confidence surface helix or terminus can be fully exposed.
- The shared library itself now contains a warning added after comp-001: this proxy undercounted real cleavage risk by ~10× for the lactoferrin linker in comp-034, and “affects comp-001/005/006/012/037.”
- The top ALP sites in comp-001 include positions 1–5, i.e. the N-terminus. Calling the N-terminal M-S / S-A / A-V region “buried” because its pLDDT window is high is not physically justified.
- The model does not compute SASA, secondary structure accessibility, biological tetramer exposure, protease-substrate geometry, or real proteolysis kinetics.

Stored-but-unused / partly-used inputs:

- `active_pH_range`, `optimal_pH`, `_ph_note`, protease `type`, `family`, `merops_id`, free-text `notes`, and source strings are stored but not algorithmically used.
- `shio_koji_conditions.temperature_C` and `duration_days` are written to outputs but not used in any degradation calculation.
- `pH_range` is written to outputs but not used dynamically; the model uses each protease’s fixed `ph_activity_at_shio_koji`.
- `NaCl_pct_range` is stored but unused; no salt sensitivity range is run.
- `salt_inhibition.NaCl_15pct_residual_activity` is stored but ignored. `interpolate_salt_inhibition()` linearly interpolates only between 10% and 20%. For ALP at 17.5% NaCl, this gives 18.8%; a piecewise interpolation using the stored 15% point would give ~15%. This does not change the qualitative verdict, but it is a real implementation/input mismatch.
- The sequence length is not explicitly cross-checked against pLDDT length in code. By inspection both are 302 residues here, so no output error is apparent.
- `site_plddt()` has a minor end-window off-by-one behavior near the C-terminus because the upper `range()` bound excludes `seq_len`; not load-bearing here because all C-terminal pLDDTs remain high.

Constraint closure:

- **Reaction/substrates:** The artifact models protease recognition on uricase peptide bonds. It does not model the uricase catalytic reaction, post-ferment activity, or degradation products.
- **Proteases/cofactors:** It includes ALP, NPr, and acid protease. It does not model other koji peptidases/exoproteases. NPr zinc/calcium dependence is mentioned in notes but not modeled.
- **Physiological operating constants:** No protease Km/kcat, enzyme concentration, uricase concentration, protease secretion level, or substrate residence-time kinetic model is included.
- **Mass balance/exposure time:** The output states 7–14 days but degradation is not integrated over time. A site with low per-site heuristic risk and 14 days of exposure is treated the same as a short exposure.
- **Localization/access:** The code assumes sequence-level exposure to proteases but does not distinguish secreted extracellular uricase, intracellular/peroxisomal retained uricase, matrix-adsorbed protein, or tetrameric assembly. These are dominant physical access variables.
- **Tetramer:** The summary claims the monomer analysis is conservative because tetramerization buries more surface area. This is plausible for interface residues but not proven for all predicted sites and not implemented. Exterior tetramer surfaces can still be solvent/protease accessible.
- **Safety/off-targets:** H₂O₂, oxygen, activity retention, and product formation are outside this comp. That is acceptable for a protease-axis analysis, but the “meaningful activity retained” wording goes beyond what is computed.
- **Sensitivity coverage:** There is no real sensitivity analysis. The dominant uncertainties—SASA vs pLDDT, protease concentrations, time, pH range, topology/localization, tetramer exposure—are not swept.

## Summary-fidelity audit

Artifact-internal mismatches and overstatements:

- `outputs/summary.md`, `README.md`, and `wiki-archive.md` repeatedly say all sites are “buried” or that there are “no exposed recognition sites.” That is exactly what the code labels, but it is not a justified physical conclusion because “buried” is derived from pLDDT alone.
- “No exposed unstructured regions” is partly supported as “no low-pLDDT regions,” but not as “no exposed regions.”
- “No exposed termini” is not supported. The N-terminus is included among top predicted cleavage sites and is physically a terminus.
- “LOW risk” as a heuristic output is reproducible, but the numeric max-risk score is an arbitrary formula:
  - `risk = accessibility_weight × salt_activity × pH_factor`
  - No kinetic derivation, time integration, or degradation threshold derivation is present.
- The `summary.md` script path says `experiments/comp-001-.../analyze.py`; the actual repo path is `wiki/etc/experiments/comp-001-.../analyze.py`.
- README says requirements are stdlib only. That is true for Python packages, but incomplete as a dependency declaration because the run depends on the shared repo-local `experiments/lib/protease_stability.py`.

Corpus-level mismatches:

- `wiki/computational-experiments.md` still says comp-001 reframes §1.10 “from feasibility gate to confirmation experiment.” That is stale/over-strong after comp-002, which found MODERATE/YELLOW thermal/tetramer risk and says §1.10 is still a YELLOW gate for uricase stability.
- `wiki/validation-experiments.md` §1.10, in the inspected section, repeats comp-001 as making the uricase arm a confirmation experiment and does not incorporate the comp-002 readout additions described in the comp-002 page.
- `wiki/uricase-shio-koji-thermal-stability-computational.md` is already more current: it explicitly says comp-001 covers only the protease axis and that the combined picture is MODERATE-overall, with thermal cooperative unfolding as the residual risk.
- The comp-001 archived interpretive page says comp-002 is “planned” and low priority unless §1.10 is unexpected. This is now stale because comp-002 exists and materially changes the shio-koji uricase stability framing.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Q00511 sequence is 302 aa *A. flavus* uricase | `inputs/Q00511.fasta`; `inputs/provenance.md` | Loaded by `load_sequence()` and scanned for sites | FASTA present; UniProt URL cited but not independently verified here | Usable by inspection; primary-source verification unresolved |
| pLDDT mean 97.1, min 80.5, 100% ≥80 | `inputs/alphafold_Q00511_plddt.json`; `outputs/cleavage_sites.json` | `compute_sequence_stats()` and site-window means | JSON present; AlphaFold URL cited but PDB not included | Arithmetic plausible; source not independently verified |
| pLDDT ≥80 means “buried” | `protease_stability.py` thresholds | Directly determines all exposure counts and risk scores | No primary source supports pLDDT as burial; library caveat says this is wrong for real SASA | Load-bearing invalid proxy; requires SASA/tetramer reanalysis |
| All 356 recognition sites are buried | `outputs/summary.md`; `outputs/cleavage_sites.json` | Consequence of pLDDT thresholding | Depends entirely on invalid proxy | Not physically established |
| ALP P1/P1′ rules produce 215 sites | `inputs/protease_specificities.json`; `outputs/cleavage_sites.json` | Sequence scan using P1 list and any P1′ | MEROPS/literature cited but not included | Reproducible from encoded rules; provenance unresolved |
| NPr rules produce 97 sites | Same | Sequence scan using any P1 and hydrophobic P1′ | Citation string only | Reproducible from encoded rules; provenance unresolved |
| Acid protease rules produce 44 sites | Same | Sequence scan requiring hydrophobic/acidic P1 and hydrophobic P1′ | Citation string only | Reproducible from encoded rules; provenance unresolved |
| ALP residual activity 18.8–19% at 17.5% NaCl | `inputs/protease_specificities.json`; `protease_stability.py` | Interpolated from 10% and 20% points only | Literature cited but not included | Implementation ignores stored 15% point; should be reconciled |
| NPr residual activity 38.8–39% at 17.5% NaCl | Same | Interpolated from 10% and 20% points only | Citation string only | Minor mismatch with stored 15% point; not qualitative |
| Acid protease residual activity 65% at 17.5% NaCl | Same | Interpolated from 10% and 20% | Citation string only | Internally consistent; source unresolved |
| ALP pH factor = 1.0 is conservative | `protease_specificities.json`; `outputs/summary.md` | Multiplicative factor in effective activity | Active range and rationale stored; primary source not included | Conservative by assertion; not dynamically modeled |
| NPr pH factor = 1.0 is conservative | Same | Multiplicative factor | Citation string only | Plausible but unverified |
| Acid protease pH factor = 0.30 | Same | Multiplicative factor | Koaze et al. cited but not included | Load-bearing estimate; unresolved |
| Conditions: 17.5% NaCl, pH 4.5–5.2, 22°C, 7–14 days | `protease_specificities.json`; outputs | NaCl used; pH range/temp/duration mostly output-only | “Standard shio-koji” note only | Incomplete model use; duration/temp not used |
| Highest risk score 0.039 | `outputs/cleavage_sites.json`; `summary.md` | `0.1 × 0.388 × 1.0`, rounded | Formula is artifact-defined, not externally validated | Reproducible but not a degradation probability |
| LOW threshold <0.15 | `analyze.py` | Determines overall verdict | No derivation or calibration in artifact | Arbitrary; should not drive strong biological wording |
| “Uricase is tetramer; monomer analysis conservative” | `outputs/summary.md`; `wiki-archive.md` | Not implemented | UniProt/crystal structure cited elsewhere; no tetramer SASA here | Plausible but unproven; must not be used as computed evidence |
| “§1.10 is confirmation, not feasibility gate” | README, output summary, wiki archive, computational index | Summary-level inference only | Contradicted/softened by later comp-002 | Stale; change required |

## Affected wiki pages

- `wiki/uricase-protease-stability-computational.md` — change required — the stub links to the frozen comp-001 archive but should flag that the long-form “all sites buried / confirmation experiment” wording is superseded by the pLDDT≠SASA caveat and by comp-002’s MODERATE thermal/tetramer result.
- `wiki/computational-experiments.md` — change required — comp-001 still says §1.10 is reframed from feasibility gate to confirmation; comp-002 is still listed as planned/low in the provided index despite an existing comp-002 interpretive page reporting MODERATE/YELLOW.
- `wiki/validation-experiments.md` — change required — §1.10 should incorporate comp-002’s native-PAGE/tetramer, specific-activity, pH-over-time, and temperature-control readouts, and should stop presenting the uricase arm as merely a confirmation experiment.
- `wiki/uricase-shio-koji-thermal-stability-computational.md` — already consistent — explicitly states comp-001 only covers protease risk and that combined shio-koji uricase stability is MODERATE-overall with thermal cooperative unfolding as the residual risk.
- `wiki/lactoferrin-protease-stability-computational.md` — change required / review required — same pLDDT-as-accessibility library affects comp-005; later comp-034 already showed a high-pLDDT lactoferrin helix can be exposed and protease-vulnerable.
- `wiki/daf-cd55-protease-stability-computational.md` — change required / review required — same shared pLDDT proxy affects comp-006 conclusions; the page should carry the SASA caveat or a replacement analysis.
- `wiki/daf-cd55-scr14-truncated-computational.md` — change required / review required — same shared pLDDT proxy affects comp-012’s LOW comparison to uricase.
- `wiki/c1-inh-protease-stability-ecn-computational.md` — change required / review required — not inspected in detail, but the shared library caveat explicitly names comp-037 as affected.
- `wiki/koji-endgame-strain.md` — already broadly consistent in inspected sections — it now places §1.33 as upstream Gate 0 and does not appear to rely on comp-001 alone to green-light UOX topology.
- `wiki/engineered-koji-protocol.md` — mostly consistent in inspected sections, but should avoid using shio-koji uricase survival as settled until §1.10 plus comp-002 readouts are reconciled.

## New connections or implications

- The comp-034 SASA/PyRosetta finding is directly relevant to comp-001: it demonstrates the exact failure mode in the shared protease-stability model—high pLDDT can coexist with solvent exposure and protease vulnerability.
- The top comp-001 cleavage sites being at the N-terminus is a useful diagnostic: a real SASA/tetramer reanalysis should explicitly check terminal accessibility rather than treating high terminal pLDDT as burial.
- Comp-001 and comp-002 should be represented as orthogonal axes, not as sequential confidence upgrades. Protease risk may be low while total shio-koji activity retention remains YELLOW due to thermal/tetramer instability.
- The shared library means this is not isolated to uricase. Any corpus claim saying “zero exposed sites” from comp-001/005/006/012/037 should be treated as “zero low-pLDDT sites” until SASA is computed.

## Required actions

1. **Replace or qualify comp-001 accessibility analysis.** Owner surface: `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/` and `wiki/uricase-protease-stability-computational.md`. Verification criterion: a rerun using explicit solvent accessibility on the AlphaFold/PDB biological tetramer, with termini and secondary-structure conformation reported separately from pLDDT.
2. **Reconcile salt interpolation.** Owner surface: `protease_stability.py` or comp-001 inputs/summary. Verification criterion: either use piecewise interpolation through the stored 15% NaCl values or remove unused midpoint values and document the two-point interpolation.
3. **Propagate the pLDDT≠SASA caveat.** Owner surface: comp-001, comp-005, comp-006, comp-012, and comp-037 interpretive pages/index entries. Verification criterion: no page claims “buried” or “no exposed sites” from pLDDT alone without a SASA caveat or replacement analysis.
4. **Update §1.10 framing.** Owner surface: `wiki/validation-experiments.md`. Verification criterion: §1.10 describes uricase shio-koji stability as protease-axis LOW but overall YELLOW pending thermal/tetramer wet-lab confirmation, and includes comp-002’s native-PAGE, specific-activity, pH-over-time, and temperature arms.
5. **Update computational index.** Owner surface: `wiki/computational-experiments.md`. Verification criterion: comp-001 no longer says §1.10 is simply a confirmation experiment; comp-002 is represented as completed MODERATE/YELLOW rather than planned low priority.
6. **Fix reproducibility contract.** Owner surface: comp-001 README/output summary. Verification criterion: declared dependencies include the repo-local shared `wiki/etc/experiments/lib/protease_stability.py` with version/hash or the algorithm is vendored/frozen into the comp folder; script path is corrected to `wiki/etc/experiments/...`.

## Review limits

- I did not execute the code; reproducibility was assessed by source inspection and committed outputs.
- Primary sources for MEROPS specificity, salt inhibition, pH activity, UniProt, and AlphaFold were not independently retrieved; only artifact files and citation strings were inspected.
- `grep_repo` failed in this environment because `rg` was unavailable, so affected-page discovery relied on explicit bundle pages plus manual inspection of likely linked pages and the shared library caveat.
- I inspected the shared library, comp-001 files, the computational index, validation §1.10 excerpt, comp-002 interpretive archive, and several platform context pages, but not every page in the corpus.
- No medical or clinical efficacy inference is made here; this remains Phase 0 computational artifact review.

---

## ✓ Actioned 2026-07-14

**Disposition: fix-in-place relabel** (protease-axis LOW holds *directionally* as a proxy prior; the quantitative "no exposed sites / feasibility closed" framing overstated). Same pLDDT-proxy class as comp-006.

- **pLDDT-proxy relabel:** `analyze.py` interpretation now states LOW is a **pLDDT/sequence-confidence prior**, not SASA — "no exposed unstructured regions" → "no low-pLDDT (disordered) regions by the pLDDT proxy; pLDDT is model confidence, not solvent accessibility; no SASA/exposure-time/protease-concentration model run." Outputs regenerated.
- **Softened over-strong framing:** "§1.10 is a confirmation experiment, not make-or-break" → "§1.10 is the actual test, not mere confirmation; protease-axis prior only, not decision-grade."
- **comp-002 axis dependence** now noted: uricase shio-koji stability is **MODERATE/YELLOW on the thermal/tetramer axis** — not uniformly LOW; the outdated "a follow-up comp-002 could model…" updated to comp-002's actual result.

**Residual (noted):** downstream `computational-experiments.md` comp-001 entry could echo the pLDDT-proxy + axis-dependence caveat (non-verdict).
