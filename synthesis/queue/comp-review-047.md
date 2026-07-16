---
type: comp-review
sweep_date: 2026-07-15
sweep_sha: eeab5b5
comp: comp-047
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-047


ACTION_REQUIRED: yes

REVIEWED_SNAPSHOT: commit:eeab5b53054b93544c428a476dad06a8f8fe2621

# Independent comp review — comp-047

## Reviewed snapshot
Independent API reviewer; daemon snapshot `commit:eeab5b53054b93544c428a476dad06a8f8fe2621`. I reviewed the supplied artifact bundle plus additional affected wiki pages via repository tools where possible. The snapshot is materially inspectable, but several load-bearing generated receptor files/PDBQT files were omitted from the bundle and not fully inspected; the grep tool also failed because `rg` is unavailable in the review environment.

## Bottom-line verdict
**Action required.** The high-level scientific conclusion “rigid docking does not establish a Q141K chaperone candidate” is directionally plausible, but the artifact-summary-wiki contract is not clean. The most serious issues are:

- `results.json` / `summary.md` still list **rosuvastatin as a wet-lab “uncertain” candidate**, while `chembl_axis2.json`, `drugbank_substrate_axis.json`, and the interpretive wiki page say it is substrate-disqualified.
- `drugbank_substrate_axis.json` is not integrated into `build_results.py` or `results.json`, even though it is now load-bearing for the final “known ABCG2” disqualifier.
- `wiki/computational-experiments.md` is stale relative to the artifact and interpretive page: it says sensitivity did not run and Axis 2 is thin, even though the committed artifact includes `sensitivity.json` and DrugBank Axis 2b.
- The reproduction command is not plausible as written: scripts use repo-root-relative `HERE` paths but README tells users to `cd` into the experiment directory; `$VBIN` is undefined; Vina/Open Babel paths are hardcoded to a private temp directory; `logs/` and `work/docking/` are not committed and may not be created.
- The computation still answers a weak proxy question: static rigid docking to an AlphaFold monomer is not a folding-ΔΔG / trafficking-rescue model.

## Implementation and constraint closure
I traced the main pipeline as follows:

- `prep_receptor.py`:
  - Cleans AlphaFold ABCG2 monomer.
  - Builds Q141K as a static side-chain substitution.
  - Defines `fold_site` around residue 141/contact shell and `transport_site` around Walker A residues 80–87.
- `resolve_smiles.py`:
  - Resolves 134 library molecules plus novobiocin.
  - Assigns `role_tag` using CFTR names/classes and a hardcoded inhibitor/substrate name list.
- `analyze.py`:
  - Prepares ligands with Open Babel/RDKit/Meeko.
  - Docks each ligand to `fold_site@Q141K`, `fold_site@WT`, and `transport_site@WT`.
  - Classifies using fold affinity, fold-vs-transport margin, and curated `known_inhibitor_flag`.
- `build_results.py`:
  - Merges only `outputs/chembl_axis2.json` into `results.json`.
  - Does **not** read `outputs/drugbank_substrate_axis.json`.
  - Does **not** honor `substrate_disqualified` from `chembl_axis2.json`.
- `sensitivity.py`:
  - Re-docks selected top fold-site binders plus controls under fold-site perturbations only.

Key implementation findings:

1. **Rosuvastatin disqualification is not implemented.**  
   `chembl_axis2.json` explicitly includes `"substrate_disqualified": true` for rosuvastatin and says it should be overridden to non-candidate. `drugbank_substrate_axis.json` also flags rosuvastatin as ABCG2-interacting. But `build_results.py` only treats `has_activity is True` as disqualifying. Because rosuvastatin has `has_activity: false`, `results.json` leaves:
   - `final_known_abcg2: false`
   - `wetlab_candidate: "uncertain"`
   This propagates to `outputs/summary.md`, which reports rosuvastatin in the ranked shortlist.

2. **DrugBank Axis 2b exists but is orphaned.**  
   `outputs/drugbank_substrate_axis.json` is a load-bearing generated output: the interpretive page relies on it to close the ChEMBL substrate blind spot and reduce the shortlist from two uncertain hits to one. However, no executable code integrates it into `results.json`, `controls.md`, or `summary.md`.

3. **Input substrate/inhibitor annotations are incompletely consumed.**  
   The input library contains `class_prior: "abc_substrate"` for molecules such as rosuvastatin, atorvastatin, simvastatin, pravastatin, gefitinib, sorafenib, etc. The scoring rightly avoids the old class prior, but the disqualification logic also fails to use the substrate annotation consistently. `resolve_smiles.py` only role-tags a small hardcoded substrate set as `abcg2_inhibitor`; rosuvastatin is therefore treated as `other`.

4. **The sensitivity analysis does not test the full classifier.**  
   `sensitivity.py` perturbs only `fold_site@Q141K`. It does not re-dock the transport site under the same perturbations, so it cannot determine whether `fold_vs_transport_margin` or final tier classification is stable. It is still useful as a fold-site robustness diagnostic, but it does not fully support “candidate tier robustness.”

5. **Reproducibility path is broken by path assumptions.**
   - Scripts set `HERE = Path("wiki/etc/experiments/...")`, which works only from repo root.
   - README instructs `cd wiki/etc/experiments/comp-047-...` and then run `$VENV analyze.py`; from that directory the hardcoded `HERE` path becomes nested and will not resolve.
   - `VINA`, `VBIN`, and `OBABEL` are hardcoded to a private `/private/tmp/claude-501/...` path.
   - README uses `$VBIN/obabel` but defines only `VENV`, not `VBIN`.
   - `analyze.py` writes `logs/run.log`, but `logs/` is absent from the tracked inventory.
   - `work/docking/` is ignored and absent; `analyze.py` does not create it before writing Vina outputs.

6. **Stored-but-unused / intentionally unused inputs.**
   - The descriptor fields in `fda_approved_drug_library.json` (`logp`, `rings`, `charge_phys`, etc.) are intentionally not used for scoring, consistent with the goal of avoiding comp-032’s descriptor/class-prior problem.
   - The AlphaFold confidence JSON is used for provenance/interpretation, not executable decisions.
   - However, substrate-relevant fields/classes are inconsistently used: this matters because the final verdict depends on excluding ABCG2 substrates.

Constraint closure:

- Reaction/substrate/product closure is not biochemical in the enzyme sense; the experiment is a docking triage. It does not model urate transport, ATP hydrolysis, ABCG2 dimerization, ER folding, trafficking, or urate flux.
- Compartment/localization access is acknowledged as unmodeled. No intracellular free concentration, ER access, Cmax, tissue exposure, membrane/dimer context, or residence time is modeled.
- The “transport site” is Walker A in an apo monomer, not the physiological dimeric ATP site and not the transmembrane drug/urate cavity. The artifact acknowledges this, but the classifier still uses this margin as a central tier gate.
- Safety/off-target closure is limited to “known ABCG2 inhibitor/substrate” filtering. Broader pharmacology and exposure safety are not modeled.

## Summary-fidelity audit
Major mismatches found:

1. **`outputs/summary.md` vs interpretive page conflict.**
   - `outputs/summary.md`: “0 yes, 2 uncertain,” shortlist = rosuvastatin + vorinostat.
   - `wiki/abcg2-q141k-chaperone-rescreen-computational.md`: rosuvastatin is disqualified by DrugBank substrate Axis 2b, leaving vorinostat as the sole marginal hit.
   - `results.json`: still leaves rosuvastatin as `wetlab_candidate: "uncertain"`.
   This is the central artifact-summary inconsistency.

2. **`wiki/computational-experiments.md` stale relative to current artifact.**
   Its comp-047 entry says:
   - “2 marginal uncertain (rosuvastatin, vorinostat)”;
   - “sensitivity analysis did not run (no sensitivity.json)”;
   - “Axis 2 populated for only 3/135 molecules.”
   But the committed artifact includes `outputs/sensitivity.json`, `outputs/drugbank_substrate_axis.json`, and expanded `chembl_axis2.json`. This page must be reconciled.

3. **README output inventory omits `drugbank_substrate_axis.json`.**
   README lists `results.json`, `sensitivity.json`, `controls.md`, `summary.md`, `chembl_axis2.json`, but the tracked/generated outputs include `drugbank_substrate_axis.json`, which is load-bearing for the interpretive conclusion.

4. **README says “sensitivity analysis mandatory,” and output exists, but executable summary does not incorporate sensitivity.**
   `build_results.py` does not read `sensitivity.json`, so no robustness information affects `results.json` or `summary.md`.

5. **Interpretive page stronger than executable outputs.**
   The interpretive page’s “residual gaps closed” narrative depends on manual/sidecar outputs and logic not implemented in the merge script. The conclusion may be reasonable, but it is not executable from the declared pipeline.

6. **Validation surface incomplete.**
   The interpretive page says the real next step is a Q141K trafficking-rescue assay paired with urate flux and ABCG2-inhibition counterscreen. The supplied `validation-experiments.md` contains related ABCG2/Q141K arms (e.g., §1.14 and §1.22), but I did not see a clean, comp-047-updated dedicated validation entry for “candidate pharmacological chaperone trafficking + urate flux + inhibitor counterscreen.” If the corpus intends this as a required next gate, it should be registered explicitly or the interpretive language softened.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---|---|
| `wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/results.json` | generated output | Yes, text bundle | Internally inconsistent with Axis 2b: rosuvastatin remains `wetlab_candidate: "uncertain"` despite substrate-disqualification note and DrugBank flag. |
| `wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/summary.md` | generated summary | Yes | Reports 2 uncertain candidates including rosuvastatin; conflicts with interpretive page and DrugBank Axis 2b. |
| `wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/controls.md` | generated summary | Yes | Control table is mostly faithful to `results.json`; does not reflect broader DrugBank substrate axis. |
| `wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/sensitivity.json` | generated output | Yes | Fold-site perturbation data exist; supports fold-site instability but does not test transport-margin/tier robustness. |
| `wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/chembl_axis2.json` | generated/manual Axis 2 output | Yes | Explicitly notes ChEMBL substrate blind spot and rosuvastatin substrate-disqualification, but `build_results.py` ignores `substrate_disqualified`. |
| `wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/drugbank_substrate_axis.json` | generated/manual Axis 2b output | Yes | Load-bearing output; flags 31 ABCG2-interacting drugs and disqualifies rosuvastatin. Not integrated into executable merge. |
| `wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/work/ligands/smiles_resolved.json` | generated intermediate | Yes | All 135 SMILES resolved; role tagging incomplete for ABCG2 substrates such as rosuvastatin. |
| `wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/work/receptor/boxes.json` | generated intermediate | Yes | Box coordinates match code/provenance; note overstates “molecule scoring well at both is rare,” whereas results show many transport affinities stronger than fold affinities. |
| `wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/work/receptor/abcg2_wt_clean.pdb` | generated intermediate | No | Omitted from bundle as non-text; not fully inspected. |
| `wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/work/receptor/abcg2_q141k_clean.pdb` | generated intermediate | No | Omitted from bundle as non-text; not fully inspected. Q141K geometry remains a load-bearing unchecked intermediate. |
| `wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/work/receptor/abcg2_wt.pdbqt` | generated intermediate | No | Omitted from bundle as non-text; not fully inspected. |
| `wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/work/receptor/abcg2_q141k.pdbqt` | generated intermediate | No | Omitted from bundle as non-text; not fully inspected. |
| `wiki/abcg2-q141k-chaperone-rescreen-computational.md` | committed interpretive wiki update | Yes | Scientifically cautious, but depends on DrugBank Axis 2b logic not implemented in `build_results.py`; conflicts with `summary.md` and `results.json` on candidate count. |
| `wiki/computational-experiments.md` | committed index update | Yes, relevant comp section | Stale: says sensitivity did not run and Axis 2 thin; must be updated. |
| `wiki/abcg2-q141k-chaperone-screen-computational.md` | committed superseded comp-032 page | Yes | Mostly consistent with comp-047 null/inconclusive framing. |
| `wiki/validation-experiments.md` | committed validation page | Partially, supplied excerpt | Related Q141K arms exist, but a dedicated comp-047 follow-up assay is not clearly registered in the inspected material. |
| `wiki/abcg2-modulators.md` | affected wiki page | Yes, relevant sections | Largely reconciled: comp-032 demoted, comp-047 inconclusive, no compounding conversation. |
| `wiki/chassis-pending-interventions.md` | affected wiki page | Yes, relevant §7 | Largely reconciled: comp-047 inconclusive, no compounding conversation. |
| `wiki/gout-genetic-variants.md` | affected wiki page | Yes, Q141K row | Largely reconciled: comp-047 inconclusive; no validated chaperone ranking. |
| `wiki/genotype-informed-supplement-workflow.md` | affected wiki page | Yes, relevant sections | Largely reconciled: chaperone class marked hypothesis-only after comp-047. |
| `wiki/compounding-pharmacy-track.md` | affected wiki page | Yes, relevant parts | Does not appear to promote Q141K chaperone compounding; consistent with no action on this route. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Q141K is a folding/trafficking defect and relevant gout-risk variant | README, provenance, wiki pages | Biological rationale only | Cites UniProt/Saranko/Basseville; primary sources not directly verified in this review | Plausible but not independently primary-verified here. |
| AlphaFold ABCG2 monomer Q9UNQ0 v6 | `inputs/provenance.md`, PDB input | Receptor for docking | Source URL/citation given; PDB not fully inspected due bundle/tool limits | Adequate provenance string, but structure file not fully audited. |
| Q141K static side-chain substitution | `prep_receptor.py`, README | Builds Q141K receptor | No rotamer/relaxation source; idealized geometry | Weak but honestly disclosed; not a folding model. |
| Fold-site grid center `[1.089, 12.029, 10.327]`, 22 Å cube | `prep_receptor.py`, `boxes.json`, `results.json` meta | Vina docking box | Derived from AlphaFold residues 137–145/141 sidechain | Implemented; pocket biological validity unproven. |
| Transport-site grid center `[-21.76, -11.112, 12.754]`, 22 Å cube | `prep_receptor.py`, `boxes.json`, `results.json` meta | Vina docking box | Derived from Walker A 80–87 | Implemented; not full ABCG2 transport/drug cavity or dimeric ATP site. |
| Classifier thresholds: yes if fold ≤ −7 and margin ≥ 1.5; uncertain if fold ≤ −6 and margin ≥ 0.5 | `analyze.py::classify()` | Assigns `chaperone_tier` | Heuristic; no empirical calibration | Implemented but not validated; margins within Vina noise for uncertain hits. |
| Known inhibitor/substrate disqualification | `analyze.py`, `build_results.py`, `chembl_axis2.json`, `drugbank_substrate_axis.json` | Should set final candidate status | ChEMBL partial; DrugBank/UniProt source string only; primary substrate sources not verified | **Not implemented consistently.** Rosuvastatin remains candidate in results/summary. |
| Rosuvastatin substrate disqualification | `chembl_axis2.json`, `drugbank_substrate_axis.json`, interpretive page | Should remove candidate | Stated from FDA label/DrugBank; not independently verified here | Artifact logic says disqualify; executable output fails to do so. |
| Vorinostat sole marginal survivor after Axis 2b | Interpretive page | Final narrative conclusion | Depends on manual DrugBank axis + classifier | Not reflected in `summary.md` or `results.json`; action required. |
| CFTR correctors fail positive-control tier | `results.json`, `controls.md`, interpretive page | Validity argument | Direct from docking output | Supported by artifact, but CFTR correctors are analog controls, not true ABCG2-positive controls. |
| Known ABCG2 inhibitor controls rejected | `results.json`, `controls.md` | Validity argument | Some curated, some ChEMBL | Supported, but partly tautological via `role_tag` disqualifier rather than docking. |
| Sensitivity analysis run | `sensitivity.py`, `sensitivity.json`, interpretive page | Robustness narrative | Generated output present | Present; `computational-experiments.md` stale. Does not test final tier margins. |
| Repro command deterministic | README | Reproducibility contract | Depends on private env paths and run directory | Not plausible as written. |

## Affected wiki pages
- `wiki/abcg2-q141k-chaperone-rescreen-computational.md` — **change required** — reconcile candidate count with executable outputs, or update outputs/code so rosuvastatin is actually disqualified and only vorinostat remains marginal.
- `wiki/computational-experiments.md` — **change required** — comp-047 entry is stale: it says sensitivity did not run and Axis 2 is thin, contradicting committed `sensitivity.json`, `chembl_axis2.json`, and `drugbank_substrate_axis.json`.
- `wiki/validation-experiments.md` — **change required / at least clarify** — if the next gate is a Q141K pharmacological-chaperone trafficking + urate-flux + ABCG2-inhibition counterscreen, it should be explicitly registered or linked to an existing section; the supplied excerpt does not cleanly close this.
- `wiki/abcg2-q141k-chaperone-screen-computational.md` — already consistent — comp-032 is clearly retracted/superseded and points to comp-047.
- `wiki/abcg2-modulators.md` — already mostly consistent — comp-047 inconclusive, comp-032 list hypothesis-only, no compounding action.
- `wiki/chassis-pending-interventions.md` — already mostly consistent — pharmacological-chaperone route remains open hypothesis, no candidate or compounding action.
- `wiki/gout-genetic-variants.md` — already mostly consistent — Q141K row notes comp-047 inconclusive and comp-032 list hypothesis-only.
- `wiki/genotype-informed-supplement-workflow.md` — already mostly consistent — chaperone class marked hypothesis-only after comp-047.
- `wiki/compounding-pharmacy-track.md` — already consistent — does not promote Q141K chaperone compounding.

## New connections or implications
- The artifact surfaces a reusable transporter-screen design rule: **ChEMBL inhibition assays are insufficient for transporter substrate disqualification.** A complete ABCG2 exclusion axis must include a curated transporter substrate/interactor source such as DrugBank/UniProt, TransPortal, or PharmGKB. The interpretive page captures this, but the executable pipeline does not.
- The CFTR-corrector failure should be framed as **failure of this static docking assay to recover analog chaperone-like behavior**, not proof that CFTR correctors are invalid positive controls in all contexts or proof that ABCG2 Q141K has no small-molecule chaperone surface.
- The fold-site sensitivity results are more damning for pocket validity than for individual compounds: top-rank reshuffling under grid perturbation suggests the residue-141 surface is not a stable, discriminating druggable pocket in this static AlphaFold monomer.
- The “known inhibitor controls pass” is partly a curation sanity check, not an independent docking validation, because `known_inhibitor_flag` directly forces `tier = "no"`.

## Required actions
1. **Integrate Axis 2b into executable results generation.**  
   Update `build_results.py` to read `outputs/drugbank_substrate_axis.json` and/or honor `substrate_disqualified` in `chembl_axis2.json`. Verification criterion: rerun merge produces `results.json` with rosuvastatin `final_known_abcg2: true` or equivalent and `wetlab_candidate: "no"`.

2. **Regenerate `outputs/results.json`, `outputs/controls.md`, and `outputs/summary.md`.**  
   Verification criterion: `summary.md` candidate shortlist matches the interpretive page: rosuvastatin removed; vorinostat is the sole marginal/uncertain survivor, or the interpretive page is changed to match executable output.

3. **Update `wiki/computational-experiments.md`.**  
   Verification criterion: comp-047 entry no longer says sensitivity did not run or Axis 2 is only thin/3-molecule; it should reflect `sensitivity.json`, DrugBank Axis 2b, rosuvastatin disqualification, and the remaining null/inconclusive conclusion.

4. **Update README reproducibility instructions and scripts.**  
   Verification criterion: the command works from the stated directory or scripts use `Path(__file__).parent`; remove hardcoded private temp paths or document required environment variables; define `$VBIN`; create `logs/` and `work/docking/` as needed; list `drugbank_substrate_axis.json` in outputs.

5. **Clarify validation follow-up registration.**  
   Verification criterion: `validation-experiments.md` either has a dedicated Q141K trafficking-rescue + urate-flux + ABCG2-inhibition counterscreen entry, or the comp-047 interpretive page links to a specific existing section and states how candidate compounds would enter it.

6. **Either fully inspect/verify generated receptor intermediates or mark them explicitly as unverified.**  
   Verification criterion: Q141K clean PDB/PDBQT and WT PDB/PDBQT are either reviewed/validated with hashes and basic residue/atom checks, or the review/provenance states that the receptor intermediates are assumed from script output and not independently inspected.

## Review limits
- I did not execute code or rerun docking.
- Repository grep failed because `rg` is unavailable, so affected-page discovery relied on supplied explicit pages plus targeted `read_file` calls.
- Tool result budget was exhausted before I could inspect additional pages such as full `gut-lumen-sink.md` or `purine-degrading-bacteria.md`; I focused on ABCG2/Q141K/chaperone surfaces.
- Non-text receptor intermediates (`*.pdb`, `*.pdbqt`) were omitted from the bundle and not fully inspected.
- Primary literature and external databases (ChEMBL, DrugBank, PubChem, FDA label, UniProt) were not independently queried; provenance is assessed from artifact strings and committed files only.
- The review does not provide medical advice and treats all wet-lab/clinical implications as Phase 0 research hypotheses.
