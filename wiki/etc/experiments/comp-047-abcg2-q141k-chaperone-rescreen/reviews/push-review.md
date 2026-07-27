COMP_VERDICT: action_required
REVIEWED_SNAPSHOT: 9001ca20952e1d387636f3336388dd563ee6908d7a1a805933eaf8a394beb874
PROPAGATION_ELIGIBILITY: blocked
SYNTHESIS_ELIGIBILITY: blocked
ACTION_REQUIRED: yes
PROPAGATION_ALLOWED_SCOPE: none
SYNTHESIS_ALLOWED_SCOPE: none
FORBIDDEN_INFERENCES: docking-backed compound ranking; wet-lab prioritization from COMP-047 Vina scores; direct chaperone or binding evidence; absence of an ABCG2 rescue site; Q141K clinical, dietary, butyrate, fiber, or genotype-treatment claims; treating UniProt/DrugBank ABCG2 relationships as substrate subtype evidence; treating ChEMBL absence as absence of transporter relationship

# Independent comp review — comp-047

## Reviewed snapshot
Independent daemon reviewer; daemon trigger commit `b3c1568bca27613c8a525732bba8b95bda39ed01`; push manifest SHA-256 bound to `9001ca20952e1d387636f3336388dd563ee6908d7a1a805933eaf8a394beb874`. Text shards report complete inspection of the covered text spans, and targeted reopened files were consistent with shard summaries. However, the review brief reports one or more binary artifacts lacking inspectable text/rendered representation; this is a deterministic block.

## Bottom-line verdict
Action required. The reader-facing scientific conclusion is mostly bounded correctly: COMP-047 is inconclusive, produces no defensible docking-backed ranking, excludes rosuvastatin, and leaves vorinostat only as a marginal non-priority row. But deterministic binary-representation failure blocks propagation and synthesis. Additional action is needed to preserve implementation caveats: static apo-monomer docking cannot answer Q141K trafficking rescue; sensitivity coverage is narrower than stated in code; Axis-2 relationship fields are conservative exclusions, not substrate typing.

## Implementation and constraint closure
The computation tests static AutoDock Vina scores in a residue-141 local box versus a Walker-A comparison box, then applies ChEMBL and UniProt/DrugBank exclusion layers. That does not model folding intermediates, ΔΔG, mutant-selective stabilization, ATP-bound dimer state, membrane/substrate access, intracellular folding-compartment exposure, residence time, or urate flux. Therefore the computation can invalidate this ranking configuration but cannot resolve whether ABCG2 Q141K is pharmacologically rescuable.

Implementation issues:
- `prep_receptor.py` uses a static Q141K side-chain substitution without relaxation/rotamer/folding-energy minimization.
- Sensitivity code tests only Q141K fold-site rank/affinity, not Walker-A scores or fold-versus-transport margins. Its docstring overstates perturbations: implementation lacks the full ±2 Å axis set.
- `analyze.py` can count stale resumed partial entries, does not check Vina subprocess return codes/stderr, and reuses uncommitted ligand PDBQT intermediates if present.
- `build_results.py` rewrites `outputs/results.json` in place, making raw/final provenance fragile unless the frozen raw snapshot is separately hash-pinned.
- `repair.py`, if used after Axis-2 processing, can drop postprocessing exclusion metadata.
- Receptor verification passes only within the declared SER655→`UNK` symmetric PDBQT warning; it validates file integrity, not biological suitability.

Constraint closure remains deliberately negative/limited: no concentration, intracellular exposure, direct ABCG2 inhibition, barrier integrity, viability, coproduct/off-target, or urate-flux constraints are measured. Sensitivity explores convenient docking perturbations, not dominant biological uncertainties.

## Summary-fidelity audit
`outputs/summary.md`, README, the dedicated COMP-047 page, `wiki/computational-experiments.md`, `wiki/abcg2-modulators.md`, `wiki/chassis-pending-interventions.md`, `wiki/gout-genetic-variants.md`, and validation §1.22 are materially aligned: no defensible docking-backed ranking; 0 `yes`, 1 `uncertain`; vorinostat marginal and not a wet-lab priority from docking; rosuvastatin excluded by independent BCRP-substrate evidence plus relationship flags; COMP-032 superseded; next decisive observation is a trafficking + urate-flux + inhibition counterscreen.

Important fidelity limits:
- “N=134 docked” is valid only as 134 completed scores out of 135 attempted molecules; cyclosporine A failed.
- The “FDA-approved drug library” includes withdrawn/investigational/research rows; row-level status matters.
- Base-score tables are descriptive only and must not be converted into shortlists.
- ChEMBL no-record status is not a no-substrate claim.
- UniProt/DrugBank flags are relationship flags, not subtype proof.

## Reader-facing ownership audit
The dedicated COMP-047 page owns its evidence boundary and points correctly to validation §1.22 for empirical resolution. `abcg2-modulators.md` owns the ABCG2 mechanism separation: WT/PPARγ induction, HDAC-inhibitor Q141K trafficking rescue, and untested butyrate-mediated rescue remain separate. `chassis-pending-interventions.md` correctly gates any chassis/intervention development behind trafficking, urate flux, inhibition counterscreen, exposure, viability, and barrier integrity.

No inspected page improperly gives COMP-047 a portfolio ranking role or personalized treatment instruction. Cross-track comparisons remain on portfolio/index surfaces. The remaining ownership defect is not prose placement but artifact representation: binary outputs without inspectable representation violate the reader/reviewer contract.

## Conjecture preservation audit
COMP-047 kills only the exact static-docking ranking and decision rule. It does not kill:
- the Q141K rescue route;
- Basseville-grounded HDAC-inhibitor phenotypic control roles;
- future folding-ensemble/ΔΔG computational hypotheses;
- unranked direct-chaperone candidate inventories.

Vorinostat survives as a Basseville phenotypic positive-control candidate, not as a docking hit. Butyrate-mediated Q141K rescue remains a Research Conjecture requiring direct surface-trafficking and urate-flux evidence. COMP-032 rankings remain invalid; its compounds survive only as unranked inventory.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---|---|
| `wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/outputs/results.json` | generated_output | yes | Supports 135 attempted/134 complete; 0 yes, 1 uncertain; cyclosporine A error; some class-label/Axis-2 nuance. |
| `.../outputs/summary.md` | generated_output | yes | Faithful if read as 134 completed dockings and descriptive base scores only. |
| `.../outputs/controls.md` | generated_output | yes | Controls do not validate pocket or positive-control sensitivity. |
| `.../outputs/sensitivity.json` | generated_output | yes | Shows rank instability; margins for vorinostat/rosuvastatin within perturbation variability. |
| `.../outputs/receptor_verification.json` | generated_output | yes | Integrity passes with symmetric SER655→`UNK` warning; not biological validation. |
| `.../outputs/chembl_axis2.json` | generated_output | yes | Bounded activity check; absence is not absence of transporter relationship. |
| `.../outputs/drugbank_substrate_axis.json` | generated_output | yes | Relationship flags only; not substrate subtype evidence. |
| `.../work/receptor/*`, `boxes.json`, `smiles_resolved.json` | generated/intermediate text | yes | Reproducibility relies on frozen intermediates; resolver/live prep reruns are not equivalent. |
| Unspecified binary artifact(s) in push manifest | generated_output/binary | no inspectable representation | Deterministic block; propagation and synthesis blocked. |
| `wiki/abcg2-q141k-chaperone-rescreen-computational.md` | proposed_update | yes | Correctly bounded; no docking-backed wet-lab priority. |
| `wiki/abcg2-q141k-chaperone-screen-computational.md` | proposed_update | yes | COMP-032 superseded; no ranking use. |
| `wiki/abcg2-modulators.md` | proposed_update | yes | Mechanism separation preserved; no butyrate/Q141K overclaim. |
| `wiki/chassis-pending-interventions.md` | proposed_update | yes | Empirical gates preserved; no compounding/personalized leap. |
| `wiki/computational-experiments.md` | proposed_update | yes | COMP-047 marked done/inconclusive; consistent. |
| `wiki/validation-experiments.md` §1.22 | proposed_update/affected | yes targeted | Correctly owns empirical rescue gate. |
| `wiki/gout-genetic-variants.md` | affected_update | yes | Q141K clinical/dietary claims remain unvalidated. |
| `wiki/etc/chembl-cross-check.md` | affected_update | yes | Correctly constrains ChEMBL/relationship interpretation. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| 135 attempted, 134 complete dockings | README/results/summary | Counts result set; failed cyclosporine A | Direct artifact rows inspected | Valid with wording constraint. |
| 0 `yes`, 1 `uncertain` after exclusions | `results.json`, `summary.md` | Final executable result | Direct artifact inspected | Supported. |
| Vorinostat marginal survivor | `results.json`, `chembl_axis2.json`, summary | Sole uncertain row | Artifact supports no ChEMBL/DrugBank flag, but literature substrate uncertainty remains | Not priority; do not upgrade. |
| Rosuvastatin excluded as BCRP substrate | summary, dedicated wiki, provenance | Axis-2 exclusion | FDA label cited, not primary-verified here beyond citation/link | Conservative exclusion supported; substrate claim source not independently reopened. |
| UniProt/DrugBank ABCG2 flags | `drugbank_substrate_axis.json` | Conservative final exclusion | Artifact records relationships, not subtype | Use only as relationship exclusion. |
| ChEMBL ABCG2 no-record | `chembl_axis2.json` | Exclusion screen | Bounded query artifact inspected | Not evidence of no ABCG2 relationship. |
| AlphaFold Q141 local confidence | AF confidence JSON/provenance | Receptor confidence context | Direct artifact inspected | Does not validate folding/chaperone model. |
| Q141K static side-chain substitution | `prep_receptor.py`, receptor files | Mutant model | Direct code inspected | Major validity boundary. |
| Receptor integrity hashes/counts/box geometry | `verify_receptors.py`, expected JSON, output | File-integrity check | Direct code/output inspected | Passes with SER655→`UNK`; not biological suitability. |
| Sensitivity rank instability | `sensitivity.py`, `sensitivity.json` | Robustness caveat | Direct artifact inspected | Supports invalidating ranking; coverage narrower than docstring. |
| Vina seed/exhaustiveness/cpu | README/analyze code | Docking reproducibility | Code/output inspected; Vina not rerun | Plausible but not independently reproduced. |
| Basseville HDAC Q141K rescue | wiki/provenance citation | Justifies validation controls, not docking | Citation/link present; primary not reopened | Preserve as cited in-vitro precedent only. |

## Affected wiki pages
- `wiki/abcg2-q141k-chaperone-rescreen-computational.md` — already consistent — states inconclusive, static-model limits, no ranking, vorinostat boundary.
- `wiki/abcg2-q141k-chaperone-screen-computational.md` — already consistent — COMP-032 superseded; no ranking use.
- `wiki/abcg2-modulators.md` — already consistent — separates WT induction, HDAC rescue, and untested butyrate/Q141K rescue.
- `wiki/chassis-pending-interventions.md` — already consistent — keeps pharmacological chaperone development gated by direct functional assays.
- `wiki/computational-experiments.md` — already consistent — COMP-047 done but inconclusive.
- `wiki/validation-experiments.md` §1.22 — already consistent — owns the decisive trafficking/urate-flux/inhibition/exposure gate.
- `wiki/gout-genetic-variants.md` — already consistent — no Q141K-stratified fiber/butyrate clinical claim; COMP-047 not a validated chaperone result.
- `wiki/etc/chembl-cross-check.md` — already consistent — ChEMBL is not a substrate-clearance database; relationship flags are conservative exclusions.
- `wiki/etc/experiments/comp-047-abcg2-q141k-chaperone-rescreen/README.md` — change required — ensure 135 attempted/134 complete wording and sensitivity artifact/provenance boundaries remain explicit; account for binary representation block.

## New connections or implications
The most useful connection is methodological: COMP-047 and the ChEMBL cross-check jointly establish a reusable evidence-axis rule for transporter screens—database absence cannot clear substrate status, while broad relationship flags can conservatively exclude but cannot type mechanism. This should inform future ABCG2/OAT/URAT transporter screens.

Research Conjecture boundary: a future folding-ensemble or ΔΔG model could generate better Q141K rescue hypotheses, but only if coupled to intracellular exposure and functional urate-flux validation. COMP-047 supplies a negative control for static apo-monomer docking, not a negative result for the route.

## Required actions
1. Provide inspectable text/rendered representations for every binary artifact in the push manifest, or remove nonessential binary outputs from result-bearing scope; verification criterion: a subsequent daemon review can inspect all manifest entries without deterministic blocks.
2. Tighten COMP-047 README/provenance wording where needed to say “135 attempted / 134 complete dockings,” not 135 completed results.
3. Correct or annotate the sensitivity implementation documentation: recorded perturbations are narrower than “±2 Å along each axis,” and robustness applies to fold-site rank/affinity, not the full executable margin rule.
4. Preserve Axis-2 terminology everywhere: UniProt/DrugBank = ABCG2 relationship flags; ChEMBL absence = no bounded activity record, not no substrate/inhibitor relationship.
5. If COMP-047 is ever rerun or extended, freeze raw `results.json`, ligand preparation hashes, Vina return-code/stderr logs, and live-query snapshots before postprocessing.

## Review limits
Code was not executed. Primary papers and external databases were not independently reopened except where committed text/artifacts were inspected. The actual `push-review.manifest.json` file was not available through the read tool, so binding relies on the supplied daemon SHA and hash-bound shard audits. One or more binary artifacts lacked inspectable text/rendered representation; this is the controlling deterministic block.
