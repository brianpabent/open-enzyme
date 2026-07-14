---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: 537562f
comp: comp-002
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-002

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-002-537562f.md`](../../logs/comp-reviews/2026-07-14-comp-002-537562f.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-002

## Bottom-line verdict

Action required. The computation is plausibly reproducible and its core 64.0% reference-retention arithmetic is traceable to the committed code and outputs, but the artifact-summary contract is not clean: the generated narrative and interpretive page report the pH 4.5 interface integrity as ~88% while the code computes **66.1%**; `wiki/computational-experiments.md` still lists comp-002 as planned; `validation-experiments.md` has not incorporated the comp-002 handoff; and several biological substitutions are stronger than the implementation supports.

The quantitative point estimate should be treated as a **model-derived storage-retention prior**, not a resolved answer to “will uricase maintain activity under shio-koji conditions” in the broader physiological sense.

## Implementation and constraint closure

I traced the load-bearing path:

- `inputs/biophysical_priors.json` → thermal parameters, salt factor, reference conditions, sensitivity grid.
- `inputs/tetramer_interface_residues.json` → interface residue ranges and 3 acidic pKa estimates.
- `inputs/alphafold_Q00511_plddt.json` → pLDDT statistics.
- `analyze.py` → thermal, pH-interface, pLDDT, salt, composite retention, uncertainty band, sweep, summary.
- `outputs/stability_predictions.json` and `outputs/summary.md` → committed results.

Key implementation findings:

- **Reference output is internally consistent with code by inspection.** Reference retention is `0.6442 thermal × 0.9396 interface_term × 1.058 salt = 0.6404`, rendered as 64.0%.
- **Major generated-summary mismatch:** `ph_interface_integrity(4.5)` computes per-pair fractions `[0.557, 0.760, 0.666]`, mean **0.6611 / 66.1%**, but `outputs/summary.md`, `wiki-archive.md`, and the interpretive page state pH 4.5 is ~88% intact/deprotonated. This is a hard code-vs-summary error.
- **pH activity curve is stored but unused.** `pH_stability.ph_residual_activity_curve` includes severe low-pH activity penalties, but the code does not use it. The output is therefore post-storage structural/activity-retention at an assumed assay pH, not in-ferment catalytic activity at pH 4.5–6.0.
- **Reaction closure is out of scope in the code.** Uricase substrates/products are urate + O₂ + H₂O → allantoin/5-HIU pathway + CO₂ + H₂O₂, but the model does not include substrate concentration, Km, oxygen, product formation, H₂O₂, catalase, or finite urate mass balance. That is acceptable only if the question is narrowed to storage stability, not therapeutic activity.
- **pLDDT is overused as an interface-integrity proxy.** Monomer AlphaFold pLDDT supports local fold confidence at residues that are asserted to be interface residues; it does not directly validate tetramer assembly, interface energetics, salt effects, or pH-dependent dissociation.
- **Interface footprint and salt-bridge pairs are hand/inference encoded.** The artifact is transparent that no PDB coordinate extraction was performed. This is a model assumption, not verified structural contact closure.
- **`a_floor = 0.30` has no provenance and conflicts with the artifact’s own biology.** The archive says dimer/tetramer interface is required for catalytic competence, but the composite grants 30% “monomer-level” retained activity if the interface is fully compromised. At the reference pH this has modest numerical effect, but it is load-bearing for low-pH conditions.
- **Uncertainty band is a worst/best simultaneous bracket, not statistical ±sigma.** The summary calls it an uncertainty band and sometimes “±sigma”; code perturbs fixed Tm to 25/29 °C and ΔH to 300/500 kJ/mol. It is a deterministic scenario bracket, not a probabilistic confidence interval.
- **Hard-coded uncertainty overrides are not future-proof.** If `wt_Tm_celsius` is edited, the uncertainty helper still uses fixed 25/29 °C rather than `Tm ± 2`.
- **Sensitivity “other parameters held at reference” is approximate.** Driver sensitivity uses grid-aligned pH 5.0 rather than the reference pH 5.25, because 5.25 is not in the grid.
- **Sequence is loaded but unused.** No consistency check confirms pLDDT length, residue ranges, numbering, or protein identity against the FASTA. This weakens the README claim that the script is generic across uricase variants.
- **Numbering caveat:** provenance says the AlphaFold/FASTA use 302-residue precursor numbering; `tetramer_interface_residues.json` contains an internally confusing `_numbering` note. A one-residue offset would not change the high pLDDT conclusion much, but it could affect residue-specific salt-bridge claims.

Constraint closure:

- **Substrates/cosubstrates/products:** not modeled except indirectly as “activity retention.” Oxygen and H₂O₂ are absent.
- **Physiological concentration vs Km:** absent. This comp cannot answer physiological urate-turnover sufficiency.
- **Finite mass balance/residence time:** storage duration is modeled; substrate mass balance and GI residence are not.
- **Localization/transport/access:** tetramer stability in the ferment matrix is modeled heuristically; secretion/intracellular localization and physical access are not.
- **Coproducts/local peaks/redox/safety:** H₂O₂ and catalase are not included.
- **Sensitivity coverage:** temperature and duration are useful; pH and salt are covered; dominant uncertainties in Tm, ΔH, f_u exponent, pKa, interface geometry, carbohydrate/osmolyte protection, oxygen/peroxide, and actual matrix pH drift are only partly covered.

## Summary-fidelity audit

The artifact has multiple summary-fidelity problems:

- **`outputs/summary.md` pH 4.5 value is wrong.** It states modeled Asp/Glu partners are ~88% deprotonated at pH 4.5; code and JSON output show **66.1%**.
- **`wiki-archive.md` repeats the wrong pH 4.5 integrity.**
- **`wiki/uricase-shio-koji-thermal-stability-computational.md` repeats the wrong pH 4.5 integrity and should clarify that the 64% is post-storage model retention, not in-ferment catalytic activity.**
- **`wiki/computational-experiments.md` is stale.** comp-002 remains in “Planned Analyses” as “Low (pending §1.10 result)” instead of in completed analyses with the YELLOW verdict.
- **`validation-experiments.md` §1.10 is stale relative to comp-002.** The section still frames the uricase arm around the comp-001 protease prior; the comp-002 additions claimed by the artifact—native-PAGE tetramer band, specific activity per total protein, and ferment pH over time—were not present in the inspected §1.10 text.
- **Disulfide-engineered “Tm boost” wording is too strong where it appears.** The artifact mostly caveats this correctly as T_optimum/thermal half-life, but the interpretive page source line says “disulfide-engineered Tm-boost.” The implementation does not verify a mutant Tm shift.
- **Wet-lab reprioritization is only partially propagated.** README/output say §1.10 becomes a YELLOW gate and §1.16 is strategically reinforced, but the validation page and computational index do not reflect this.
- **The pH activity curve appears in inputs and provenance but not in the result.** Any summary phrase “activity under shio-koji conditions” should be narrowed unless the pH-activity penalty is included or explicitly excluded.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| WT *A. flavus* uricase Tm = 27 °C | `inputs/biophysical_priors.json`; `inputs/provenance.md`; README | Used in `thermal_retention_fraction()` | Citation + abstract quote in provenance; primary paper not present | Load-bearing; externally unverified in this review |
| WT half-life at 40 °C = 38 min | `biophysical_priors.json` | Used to compute `k_40 = ln(2)/38` | Citation + quote; independent citation string for 38.5 min | Load-bearing; plausible but not primary-source verified here |
| `wt_thermal_inactivation_rate_constant_per_min_at_40C = 0.018` | `biophysical_priors.json` | Not used directly; recomputed from half-life | Citation string only | Stored but unused; not a defect if documented |
| ΔH_vH = 400 kJ/mol | `biophysical_priors.json` | Used in van’t Hoff unfolded fraction | Generic globular-protein prior, not Q00511-specific | Major uncertainty; appropriately caveated but not verified |
| Residual Arrhenius Ea = 50 kJ/mol | Hard-coded in `analyze.py` | Used in thermal k_eff | Not in inputs; no named source in table | Actionable provenance gap |
| f_u² sub-Tm kinetic-refolding protection | `analyze.py`; README; summary | Dominates 22 °C survival | Heuristic; no Q00511 measurement | Load-bearing modeling choice; requires wet-lab validation |
| Reference conditions 17.5% NaCl, pH 5.25, 22 °C, 14 d | `biophysical_priors.json`; `main()` | Used for headline prediction | Wiki protocol-derived; not independently verified here | Reasonable reference, but pH/time drift not modeled |
| pH residual activity curve | `biophysical_priors.json` | Not used | Estimated/interpolated; provenance caveats | Important unused input; summaries must not imply it was applied |
| 3 interface salt bridges and pKa 4.0–4.4 | `tetramer_interface_residues.json` | Used in pH integrity | Inferred, no coordinate extraction | Load-bearing but unresolved; needs PDB/PROPKA or wet-lab validation |
| pH 4.5 interface integrity | Code/JSON output vs summaries | Code computes 66.1% | Derived from pKa estimates | Summary says ~88%; correction required |
| Interface pLDDT mean 97.3, score 1.0 | `alphafold_Q00511_plddt.json`; `analyze.py` | Used as saturated interface score | AlphaFold pLDDT copied from comp-001; not reverified | Supports local fold confidence, not tetramer energetics |
| Interface residue footprint | `tetramer_interface_residues.json` | Determines pLDDT subset | Hand-encoded from PDB/literature; no PDB parsing | Acceptable as prior, not verified ground truth |
| Salt factor 1.058 at 17.5% NaCl | `biophysical_priors.json`; `salt_stability_factor()` | Multiplicative retention boost | Generic Hofmeister/Timasheff prior | Weakly grounded; not Q00511-specific |
| Composite floor `a = 0.30` | `analyze.py` | Adds activity even when interface compromised | No named source | Biologically questionable; needs justification or sensitivity |
| “No native disulfides” | `inputs/provenance.md`; wiki archive | Used interpretively, not in code | UniProt claim; not directly verified here | Important and likely correct, but should be propagated to pages claiming endogenous disulfides |
| Disulfide variants raise T_optimum ~10 °C and half-life ~3.6× | README, summary, wiki archive | Interpretive only | Citation string; no primary-source verification here | Do not call this a verified Tm boost without DSF data |
| 64.0% reference retention, 0.2–100% band | `outputs/stability_predictions.json`; `outputs/summary.md` | Final output | Reproducible from code by inspection | Internally traceable; model validity limited |
| `python3 analyze.py`, stdlib only | README; code imports | Reproduction path | Dependencies visible in code | Plausible deterministic path; not executed in review |

## Affected wiki pages

- `wiki/etc/experiments/comp-002-uricase-shio-koji-thermal-stability/outputs/summary.md` — change required — generated narrative says pH 4.5 integrity is ~88%; code output is 66.1%. Also clarify “uncertainty band” is a deterministic bracket, not statistical confidence.
- `wiki/etc/experiments/comp-002-uricase-shio-koji-thermal-stability/wiki-archive.md` — change required — repeats the pH 4.5 integrity error and should narrow “activity under shio-koji” to modeled post-storage retention unless pH activity is added.
- `wiki/etc/experiments/comp-002-uricase-shio-koji-thermal-stability/README.md` — change required — mostly faithful numerically, but should flag pH activity curve is not implemented, pLDDT is not tetramer-interface validation, and the script is not truly generic without input consistency checks.
- `wiki/uricase-shio-koji-thermal-stability-computational.md` — change required — repeats pH 4.5 ~88%; source line overstates mutant “Tm-boost”; should state the computation is a storage-retention prior.
- `wiki/computational-experiments.md` — change required — comp-002 is still listed as planned/low-priority pending §1.10 instead of completed YELLOW.
- `wiki/validation-experiments.md` — change required — §1.10 did not reflect comp-002’s YELLOW thermal/tetramer gate or the claimed native-PAGE, specific-activity, and pH-over-time additions.
- `wiki/engineered-koji-protocol.md` — change required — broad statements that shio-koji preserves enzyme activity should be qualified for engineered uricase: comp-002 predicts moderate thermal/tetramer risk over 7–14 days, especially with warm-room exposure.
- `wiki/koji-home-fermentation.md` — change required — format-constraint section should add folded-protein thermal/tetramer caveat for uricase, not only peptide proteolysis caveats.
- `wiki/uricase-variant-selection.md` — change required — inspected text says *A. flavus* uricase likely contains endogenous disulfide bonds; comp-002 provenance says UniProt Q00511 has zero native DISULFID features. Also avoid treating engineered T_optimum increases as measured Tm shifts.

## New connections or implications

- comp-002 strengthens the case that **storage format** is a separate gate from expression and protease resistance. A construct can pass comp-001 protease stability and still fail a warm shio-koji storage window.
- The artifact’s unmodeled protective-osmolyte point is important: the Imani lactose Tm shift suggests the real shio-koji carbohydrate matrix could materially alter Tm. §1.10 should test purified Q00511 in actual matrix or matrix-mimic, not buffer alone.
- comp-002 interacts with later topology/peroxide work: if UOX is extracellular/secreted, thermal storage and H₂O₂ safety are both matrix/topology problems; intracellular/peroxisomal formats may alter both retention and peroxide handling.
- The zero-native-disulfide finding should clean up variant-selection language and strengthens the rationale for engineered disulfide variants, but only as a hypothesis until mutant Tm is directly measured.

## Required actions

1. Correct all pH 4.5 interface-integrity statements from ~88% to the code-derived **66.1%**, or rerun after changing the pKa model. Verification criterion: `outputs/summary.md`, `wiki-archive.md`, and the interpretive page agree with `stability_predictions.json`.
2. Move comp-002 from “Planned Analyses” to completed analyses in `wiki/computational-experiments.md` with the YELLOW verdict and correct links. Verification criterion: no stale planned comp-002 row remains.
3. Update `validation-experiments.md` §1.10 to include comp-002’s required readouts: native-PAGE or SEC/AUC tetramer readout, specific activity normalized to protein, and ferment pH-over-time; reframe uricase as thermal/tetramer YELLOW rather than protease-only confirmation. Verification criterion: §1.10 explicitly cites comp-002 and defines pass/fail thresholds for those readouts.
4. Clarify the modeled endpoint across README, output summary, and interpretive page: “post-ferment residual activity at assay pH / storage-retention prior,” not direct catalytic activity at shio-koji pH unless the pH activity curve is incorporated.
5. Add provenance or sensitivity for the unproven `a_floor = 0.30` monomer/dissociated activity term, or remove it. Verification criterion: composite equation either cites a source/assay or includes a zero-floor sensitivity.
6. Either implement or explicitly retire the stored pH-activity curve in `biophysical_priors.json`. Verification criterion: the summary states whether pH catalytic activity was excluded, and why.
7. Add input consistency checks to `analyze.py`: sequence length vs pLDDT length, residue-range bounds, numbering convention, and non-empty interface residues. Verification criterion: rerun fails loudly on mismatched protein/input files.
8. Qualify AlphaFold pLDDT language: it supports local fold confidence, not tetramer interface energetics. Verification criterion: summary and interpretive page avoid “tetramer interface integrity” overclaim unless backed by multimer/PDB-coordinate analysis.
9. Propagate the zero-native-disulfide correction to `uricase-variant-selection.md` and any other uricase pages with endogenous-disulfide language. Verification criterion: no page claims WT Q00511 has native disulfide bonds.
10. Do not describe Rezaeian mutants as a measured “Tm boost” unless a mutant Tm source is added. Verification criterion: wording says T_optimum/half-life boost, with Tm effect unresolved.
11. Primary-source verification pass: verify Tm, half-life, Rezaeian mutant effects, UniProt disulfide absence, and PDB/interface residues against accessible primary databases/papers. Verification criterion: provenance distinguishes directly verified values from citation-string carryover.
12. If the model remains decision-relevant, rerun after any code/text corrections and commit regenerated outputs. Verification criterion: `python3 analyze.py` reproduces committed `stability_predictions.json` and `summary.md`.

## Review limits

The code was not executed. Primary papers, UniProt, AlphaFold, and PDB records were not independently fetched; provenance claims were assessed only from committed artifact text. Repository search via `grep_repo` failed because the backend `rg` executable was unavailable, and subsequent tool-result budget was exhausted after inspecting large wiki pages. I inspected the bundled artifact, `validation-experiments.md` first chunk including §1.10, `uricase.md`, `uricase-variant-selection.md`, `engineered-koji-protocol.md`, and part of `koji-home-fermentation.md`; other affected pages may exist but could not be searched exhaustively.

---
## ✓ Actioned 2026-07-14
**Disposition: caveat/downgrade** (relabel/hygiene tier). Added a ⚠️ caveat banner to the interpretive page (or artifact README for comp-015) capturing the audit's headline finding — the qualitative direction holds, but the quantitative/verdict framing overstated what the model resolves. Deeper artifact fixes (reproducibility defects, provenance-tier labeling, code/summary mismatches, any recompute) remain in the Required-actions above as residuals for a focused follow-up.
