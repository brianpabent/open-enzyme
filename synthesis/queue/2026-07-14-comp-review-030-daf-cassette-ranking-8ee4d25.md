---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: 8ee4d25
comp: comp-030
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-030

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-030-8ee4d25.md`](../../logs/comp-reviews/2026-07-14-comp-030-8ee4d25.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-030

## Bottom-line verdict

Action required — the cassette ranking is useful as a heuristic design screen, but the artifact overstates what its proxies resolve, contains reproducibility defects, and has several code/summary mismatches. The quantitative shortlist files are internally plausible as generated tables, but the “α-coefficient CORROBORATED” and “fusion/architecture tested by ESM2” conclusions are stronger than the implementation supports.

## Implementation and constraint closure

I traced the three-step pipeline:

1. `code/analyze.py` enumerates 43,200 candidates, computes CAI, ViennaRNA MFE, fixed chaperone-load scores, promoter/SP prior, and writes the all-candidate table plus ESM2 FASTA/keymap.
2. `code/run_esm2.py` scores 720 `(SP, scaffold_base, propeptide, nglyc)` keys using ESM2 unmasked log-likelihood rescaled to “pseudo-pLDDT.”
3. `code/rerank_final.py` joins scores, assigns ESM2 top-quintile flags, computes N-of-5 concordance, and writes final outputs.

Load-bearing closure issues:

- **Executable scripts appear to end with bare `EOF` tokens.** In all three bundled scripts, `EOF` appears as a final top-level expression after output writing. In Python this will raise `NameError` after the outputs are written, so the stated commands do not cleanly complete. This is a reproducibility defect even if committed outputs were produced before the crash.
- **Local codon-usage input is not used.** `analyze.py` loads `COMP022_INPUTS / "a_oryzae_codon_usage.json"` rather than `inputs/a_oryzae_codon_usage.json`, despite README listing the local file as a key input. The local JSON’s `_meta` and `rare_codon_definition` are effectively documentation-only in this artifact.
- **Rare-codon metadata is not used in scoring.** `rare_cluster_by_codon_sp` is computed with a hard-coded RSCU threshold but never written to the main outputs or used in model scoring. The JSON logic also says rare requires RSCU and frequency conditions, while code uses only RSCU `<0.4`.
- **ESM2 “protein-distinct” space is not truly protein-distinct.** The keymap has 720 keys, but many have identical amino-acid sequences because:
  - `nglyc_native` and `nglyc_ablated` do not alter sequence;
  - most `scaffold_base` choices do not alter sequence except C-terminal tag;
  - `glaA` fusion carriers are not included in the sequence at all.
  The true unique sequence count is far below 720. This affects both the interpretation of the pLDDT distribution and the weighting of the ESM top-quintile flag.
- **ESM2 does not test the stated fusion-carrier context.** `build_protein_sequence()` ignores the `glaA` carrier and returns `SP + propeptide + mature DAF + ctag`. Therefore the direct-vs-glaA “fusion” comparison in `plddt_distribution.csv` is not a test of whether the carrier perturbs folding. It mostly compares duplicated sequences under different labels.
- **The ESM2 method is not actual pLDDT and not true masked pseudo-likelihood.** The script uses unmasked next-token-style log-probabilities from one forward pass and rescales them to `[50, 90]`. This is not ESMFold pLDDT and not a direct folding-confidence or PDI-residence metric. It can be described as a sequence-model compatibility proxy, not as empirical corroboration of α.
- **The chaperone-load model is a fixed prior, not measured folding capacity.** DAF load is `8 × 0.45 = 3.6`; alpha range is documented but not swept through the ranking. There is no implemented sensitivity analysis over α, promoter priors, signal-peptide priors, carrier load, secretion efficiency, or tag effects.
- **Baseline-survival count is broadened.** `is_1_25_baseline()` counts both `SPamyB` and `SPamyB_pro` as “baseline,” even though §1.25 baseline wording is `amyB signal peptide + direct secretion`. The reported 60 baseline candidates may therefore be broader than the literal baseline.
- **Propeptide summary mismatch.** `shortlist_n5eq5.csv` contains strict-tier `short_kex2_pro` candidates, yet the archived interpretation says the 40 strict-tier candidates all share “no propeptide.” The top ranks favor no propeptide, but the strict tier does not exclusively contain no-propeptide designs.
- **Scoring answers a design-proxy question, not direct wet-lab feasibility.** The computation ranks cassettes by CAI, 5′ MFE, fixed chaperone-load priors, promoter/SP priors, and ESM2 sequence compatibility. It does not model actual secretion titer, ER redox kinetics, signal-peptide cleavage, KEX2 processing, complement activity, MSU-surface access, gut/mucus exposure, or safety/off-target complement suppression.

Constraint closure:

- **Reaction/substrate/product closure:** DAF/CD55 SCR1-4 is a complement regulator, not a catalytic enzyme. The computation does not model C3b/C4b binding, C3/C5 convertase decay, C5a reduction, or any dose-response binding constant.
- **Concentration/Kd/IC50 closure:** No DAF concentration, binding Kd, complement assay IC50, or functional operating range enters this ranking.
- **Mass balance/residence time:** No finite expression yield, secretion flux, protein residence/stability, gut exposure time, or complement-consumption mass balance is modeled.
- **Localization/transport/access:** The model assumes secretion via SP sequence but does not predict signal-peptide cleavage fidelity, extracellular accumulation, mucus/epithelial access, MSU-surface access, or complement-compartment geometry.
- **Coproducts/safety:** No assessment of human-complement off-target suppression, local complement immunology, glycan immunogenicity, tag effects on function, or handling/regulatory safety is implemented.
- **Sensitivity coverage:** Dominant uncertainties — promoter/SP priors, α coefficient, actual PDI kinetics, signal peptide processing, secretion titer, DAF activity, and physical access — are not swept. The reported ranges mainly document priors rather than stress-test the ranking.

## Summary-fidelity audit

Material matches:

- Design-space size `43,200`, N-of-5 ≥4 size `632`, N-of-5 =5 size `40`, and final concordance distribution match `final_summary.json`.
- The top-ranked rows in `top25.md`, `shortlist_n5eq5.csv`, and `final_summary.json` agree: PamyB + SPamyB + `cai_max`/`high_gc` + direct His6/no-tag/3xAla + no propeptide are top.
- `validation-experiments.md` §1.25 has propagated the key design refinement: max-CAI and direct secretion.

Mismatches / overstatements:

- **“α-coefficient CORROBORATED” is too strong.** The ESM2 proxy is not a measured PDI residence time, not ESMFold pLDDT, and not a kinetic folding assay. The artifact supports only “consistent with the low-α prior under a weak in silico sequence-model proxy.”
- **“Direct vs glaA fusion pLDDT comparison” is not implemented.** Since the `glaA` carrier is omitted from ESM2 sequences, claims that the pLDDT distribution tests fusion context or carrier interference should be removed or rewritten.
- **“720 protein-distinct candidates” is false as written.** There are 720 scored keys but many duplicate protein sequences.
- **“All strict-tier candidates have no propeptide” is false.** `shortlist_n5eq5.csv` includes `short_kex2_pro` rows. The valid statement is that the highest composite rows have no propeptide and no propeptide is recommended.
- **“glaA-KEX2 fusion is wrong for CCP/SCR” is stronger than the modeled evidence.** The ranking penalizes `glaA` by a fixed chaperone-load prior; it does not test actual fusion expression or folding. “Not favored by this scoring model” is supported.
- **`provenance.md` overclaims primary-source verification.** Several entries are verified by reading other wiki pages or inherited comp-022 provenance, not by direct primary-source inspection within this artifact. That should be labeled as secondary/internal verification.
- **README reproducibility path is stale/misaligned.** It says `cd experiments/comp-030-daf-cassette-ranking`, while tracked path is `wiki/etc/experiments/comp-030-daf-cassette-ranking`. It also depends on an external comp-022 environment and sibling input files.
- **No `outputs/summary.md` exists.** The artifact uses `results/final_summary.json` and `results/top25.md`; if the corpus expects an `outputs/summary.md` contract, this comp does not satisfy it.

## Load-bearing verification table

| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| DAF SCR1-4 = UniProt P08174 aa 35–285, 251 aa | `inputs/P08174_scr14.fasta`; `analyze.py` assertions | Sequence loaded and asserted length 251 | Provenance says UniProt / comp-012 extraction; primary source not directly present | Plausible but primary-source verification not independently present |
| 16 Cys / 8 disulfides | `analyze.py` assertions; `provenance.md`; `summary_pre_esm2.json` | Cys count asserted; disulfide count sets chaperone load | Provenance relies partly on existing wiki grep | Supported for count; primary-source verification unresolved in artifact |
| α = 0.3–0.6, central 0.45 | `analyze.py`; `alpha_coefficient_check.json`; chaperone page | `DAF_INTRINSIC_LOAD = 8 × 0.45` | Source wiki explicitly says partially unverified structural estimate | Valid as prior only; not verified kinetic constant |
| Effective DAF PDI load = 3.6 | `analyze.py`; outputs | Determines chaperone-load model and top20 flag | Arithmetic from prior | Internally correct; biological validity unresolved |
| `glaA` carrier load +9.8 to +10.8 | `SCAFFOLD_LOADS` in `analyze.py` | Penalizes fusion scaffolds | Inherited from chaperone framework / comp-022; not directly verified here | Usable as prior; not measured |
| DAF has no N-glyc sequons in SCR1-4 | `analyze.py` comments; equal `NGLYC_PENALTY` | `nglyc_native` and `nglyc_ablated` score identically | Sequence inspection supports no obvious N-X-S/T | Supported; but creating duplicate sequence keys affects ESM weighting |
| CAI model and codon usage | `calc_cai()`; `COMP022_INPUTS/a_oryzae_codon_usage.json` | CAI top20 flag | Local JSON not used; comp-022 input not in bundle | Implementation-source mismatch; action needed |
| Rare codon definition | local `inputs/a_oryzae_codon_usage.json`; `count_rare_clusters()` | Rare clusters computed but unused | Local JSON logic not used | Non-load-bearing but misleading as input |
| ViennaRNA 5′ MFE | `analyze.py`; outputs `mfe` | MFE top20 flag | Kudla citation only; ViennaRNA version not programmatically logged | Implemented; biological transfer to koji translation is proxy |
| Promoter/SP prior | `analyze.py`; comp-022 `parts_list.json` and hard-coded SP efficiencies | Prior top20 flag | Inherited bounded estimates; `parts_list.json` absent from bundle | Material but not fully auditable from bundle |
| ESM2 pseudo-pLDDT mean 88.8 | `run_esm2.py`; `alpha_coefficient_check.json`; `plddt_distribution.csv` | ESM top20 flag and alpha-check narrative | Output present; code not executed by reviewer | Output/code coherent, but interpretation overstated |
| 720 “protein-distinct” candidates | README; `run_esm2.py`; keymap | ESM distribution denominator | Code creates 720 keys, not unique protein sequences | Claim wording invalid |
| Strict tier = 40 | `final_summary.json`; `shortlist_n5eq5.csv` | Summary number | Directly output | Supported |
| N-of-5 ≥4 = 632 | `final_summary.json`; `shortlist_n5ge4.csv` | Summary number | Directly output | Supported |
| §1.25 baseline survives with 60 candidates | `rerank_final.py`; `top25.md`; `final_summary.json` | Summary number | Computed with broadened `SPamyB` or `SPamyB_pro` baseline definition | Needs definition correction |
| Top recommendation: max-CAI/high-GC, not 5′-softened | `shortlist_n5eq5.csv`; MFE/CAI outputs | Ranking outcome | Internally supported for top rows | Supported within proxy model |
| His6 top-composite tag | `final_summary.json`; `top25.md` | Recommendation | ESM/tag proxy plus composite score | Supported as model result; function/purification effects not tested |
| No propeptide recommended | `top25.md`; `shortlist_n5eq5.csv` | Recommendation | Top rows no propeptide, but strict tier includes short propeptide | Recommendation okay; “all strict tier no propeptide” false |
| Reproducible command path | README | Reproduction contract | Uses stale path, external env, and scripts contain `EOF` | Not clean; action required |

## Affected wiki pages

- `wiki/daf-cd55-scr14-cassette-ranking-computational.md` — change required — archived interpretation overstates α corroboration, says 720 protein-distinct candidates, and misstates strict-tier no-propeptide architecture.
- `wiki/computational-experiments.md` — change required — comp-030 entry says “α-coefficient CORROBORATED,” “glucoamylase-KEX2 fusion is wrong,” and “in silico fingerprint of cooperatively-folding” more strongly than the implementation supports.
- `wiki/validation-experiments.md` — change required — §1.25 can keep max-CAI/direct/no-propeptide design refinements, but should soften α “corroborated” language and note that ESM2 did not test `glaA` fusion context or actual folding kinetics.
- `wiki/chaperone-orthogonal-stacking.md` — change required — §3.5.2 cites comp-030 as in silico corroboration of α; should be downgraded to weak consistency with a sequence-model proxy, not validation of PDI residence time.
- `wiki/hypotheses/H05-daf-scr14-cp0-thesis.md` — already mostly consistent / minor change required — it still treats α as a bounded assumption; if comp-030 is cited later, it should not be used to upgrade H05’s evidence tier.
- `wiki/combined-cp0-systems-model-computational.md` — already consistent — references comp-030 only as cassette-design refinement, not as clinical or kinetic evidence.
- `wiki/engineered-koji-protocol.md` — change required if comp-030 is used for design instructions — the protocol’s older generic “codon optimization” and uricase/DAF design language should distinguish target-specific max-CAI for DAF from 5′-softening for uricase, without importing overstrong pLDDT claims.
- `wiki/koji-endgame-strain.md` — change required if it inherits DAF cassette recommendations — should frame DAF direct/no-fusion as a scoring-model preference, not as experimentally proven secretion topology.
- Search limitation: repository `grep_repo` failed because `rg` was unavailable, so affected-page discovery relied on explicit bundle pages plus targeted file reads. Additional surfaces may exist.

## New connections or implications

- The artifact strengthens a **target-specific codon-design rule**: uricase and DAF should not share a default codon strategy. For DAF SCR1-4, max-CAI/high-GC happens to score well on both CAI and 5′ MFE; the uricase 5′-softening lesson should not be blindly transferred.
- The model exposes a **cassette-ranking vs. topology-selection boundary** also seen in later uricase comps: comp-030 can rank designs inside the assumed *A. oryzae* secreted-cassette space, but it cannot establish physiological access, functional complement inhibition, or in vivo relevance.
- The duplicate “protein-distinct” ESM2 setup implies that future ClockBase-style experiments should explicitly collapse identical AA sequences before ESM scoring and before assigning top-quintile flags, or intentionally weight by design-key frequency and label it as such.
- Because `glaA` carrier sequences are omitted from ESM2, comp-030 cannot be used as evidence that `glaA` fusion contexts preserve CCP/SCR fold quality. Any future fusion-vs-direct DAF claim needs a real fusion sequence or wet-lab comparison.

## Required actions

1. **Fix executable scripts** in `wiki/etc/experiments/comp-030-daf-cassette-ranking/code/` by removing bare trailing `EOF` tokens; verification criterion: all three scripts terminate cleanly under the declared environment.
2. **Correct input closure** in `analyze.py` or README: either load `inputs/a_oryzae_codon_usage.json` locally or state that comp-022’s codon table and `parts_list.json` are the actual dependencies; verification criterion: README dependency table matches code paths.
3. **Collapse or relabel ESM2 sequence space.** Either deduplicate identical AA sequences before ESM scoring/top-quintile assignment, or explicitly call them 720 scored design keys rather than 720 protein-distinct candidates; verification criterion: summary reports both key count and unique-sequence count.
4. **Remove or qualify fusion-context ESM claims.** If claiming `glaA` context effects, rerun ESM/ESMFold on actual fusion-carrier sequences; otherwise state that ESM2 ignored `glaA` carrier context.
5. **Downgrade α language across summaries.** Replace “CORROBORATED” with “weakly consistent with low-α prior under an indirect sequence-model proxy; not a PDI-residence measurement”; verification criterion: interpretive page, computational index, validation §1.25, and chaperone page use consistent evidence-tier wording.
6. **Correct strict-tier architecture wording.** State that the highest composite candidates have no propeptide, while strict N-of-5 includes some `short_kex2_pro` candidates; verification criterion: wiki/archive text matches `shortlist_n5eq5.csv`.
7. **Clarify §1.25 baseline definition.** Decide whether `SPamyB_pro` counts as baseline; if not, recompute/report baseline survival for literal `SPamyB` only; verification criterion: baseline count definition and number match `rerank_final.py`.
8. **Fix reproducibility README.** Use the committed repo path (`wiki/etc/experiments/...` or the correct project-relative path), declare required packages/versions, and mention the comp-022 sibling dependency if retained; verification criterion: a fresh reader can identify all required files and commands without hidden local paths.
9. **Revise `provenance.md` labels.** Separate direct primary-source verification from inherited wiki/citation-string verification; verification criterion: no statement claims primary verification where only internal grep or secondary summary was used.

## Review limits

I did not execute code. Repository search via `grep_repo` failed because `rg` was unavailable, so affected-surface discovery is incomplete. I inspected the provided bundle plus targeted reads of `chaperone-orthogonal-stacking.md`, `validation-experiments.md` §1.25, `engineered-koji-protocol.md`, `complement-c5a-gout.md`, and `hypotheses/H05-daf-scr14-cp0-thesis.md` where tool budget allowed. Primary sources such as UniProt, Schmidt 2010, Kudla 2009, and promoter/source papers were not directly accessed; provenance claims relying on them remain unresolved unless the artifact itself included the primary extract.
