---
type: comp-review
sweep_date: 2026-07-15
sweep_sha: eeab5b5
comp: comp-001
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-001


ACTION_REQUIRED: yes

REVIEWED_SNAPSHOT: commit:eeab5b53054b93544c428a476dad06a8f8fe2621

# Independent comp review — comp-001

## Reviewed snapshot
Independent API reviewer; daemon snapshot `eeab5b53054b93544c428a476dad06a8f8fe2621`. I inspected the comp-001 artifact files supplied in the bundle and used repository tools for the shared library dependency and affected wiki surfaces. The inspected code path includes `wiki/etc/experiments/lib/protease_stability.py`, which is not in the comp-directory inventory but is load-bearing for reproduction.

No `reviews/` directory exists for comp-001 in the inspected experiment folder.

## Bottom-line verdict
**Action required.** The new caveat in `outputs/summary.md` is directionally correct, but the artifact-summary-wiki contract remains materially inconsistent. The implementation is a P1/P1′ sequence scan plus pLDDT-confidence proxy, not a protease-survival, solvent-accessibility, exposure-time, or fermentation-kinetics model. Several corpus surfaces still state or imply a stronger “LOW risk / confirmation experiment” conclusion than the artifact supports.

## Implementation and constraint closure
I traced the comp-001 execution path:

- `analyze.py` loads:
  - `inputs/Q00511.fasta`
  - `inputs/alphafold_Q00511_plddt.json`
  - `inputs/protease_specificities.json`
- It imports all core logic from `../lib/protease_stability.py`.
- It writes:
  - `outputs/cleavage_sites.json`
  - `outputs/summary.md`

The core model:

- Scans adjacent residue pairs for P1/P1′ matches.
- Computes mean pLDDT in a ±3 residue window.
- Classifies:
  - pLDDT ≥80 as `buried`
  - 65–80 as `partially_exposed`
  - <65 as `exposed`
- Computes risk as:

`accessibility_weight × salt_residual_activity × ph_activity_factor`

Major closure issues:

1. **pLDDT is used as solvent-accessibility/burial.**  
   The shared library explicitly states this is a known-invalid proxy for accessibility. High pLDDT means model confidence, not burial. A confidently modeled surface helix/loop may be solvent-exposed and protease-accessible. This invalidates “buried sites” as a literal conclusion.

2. **No SASA, structure exposure, peptide conformation, or time-integrated degradation model.**  
   The output fields `buried_sites`, `exposed_sites`, and `max_risk_score` look quantitative, but the implementation does not calculate actual surface accessibility, residence time, cleavage kinetics, protease concentration, enzyme:substrate ratio, or survival fraction.

3. **Duration and temperature are stored but not modeled.**  
   `temperature_C` and `duration_days` appear in conditions and summaries but do not influence risk. The question asks survival over 7–14 days at room temperature; the computation does not model cumulative exposure.

4. **pH range is not mechanistically modeled.**  
   The code uses a per-protease scalar `ph_activity_at_shio_koji`. `pH_range`, `optimal_pH`, and `active_pH_range` are carried as documentation/output, not used to derive activity.

5. **Salt interpolation ignores the 15% data point.**  
   `interpolate_salt_inhibition()` linearly interpolates only between 10% and 20% NaCl, ignoring stored 15% values. At 17.5% this is conservative for ALP relative to piecewise 15–20 interpolation, but it is still an implementation/documentation mismatch.

6. **Several JSON fields are documentation-only, not unused bugs.**  
   The heuristic “unused leaf paths” includes dynamic fields that are used (`P1_preferred`, `P1_prime_preferred`, `ph_activity_at_shio_koji`, 10% and 20% salt values), plus fields that are only documented/output (`family`, `type`, `merops_id`, `active_pH_range`, `optimal_pH`, `NaCl_pct_range`, duration, temperature).

7. **Reaction/constraint closure is incomplete.**  
   Protease hydrolysis requires physical access to peptide bonds, enzyme concentration, exposure time, water, and permissive local conformation. The model only tests local sequence motifs and pLDDT confidence. It does not address replenishment, finite protease burden, local peaks, diffusion through the shio-koji matrix, or cumulative degradation.

8. **Tetramer conservatism is asserted but not implemented.**  
   Summaries/archive state or imply that monomer analysis is conservative because tetramer interfaces bury additional surface. No tetramer biological assembly or interface SASA calculation is run, so this remains a plausible hypothesis, not a computed result.

## Summary-fidelity audit
The trigger diff improves `outputs/summary.md` and `analyze.py` by adding an explicit pLDDT-vs-SASA caveat and by softening the recommended action. However, other artifact and wiki surfaces remain stale or too strong:

- `outputs/summary.md` now contains a good caveat, but still reports:
  - `Overall risk: Low`
  - `LOW — protease degradation ... is unlikely`
  - `Buried (pLDDT ≥ 80)`
  - `Exposed (pLDDT < 65)`
  - “All potential cleavage sites ... located in confidently-folded regions”
  
  These are acceptable only if clearly framed as **pLDDT-proxy categories**, not literal burial/exposure or survival.

- `outputs/summary.md` footer says generated by `analyze.py` on `2026-05-05` even though the text now includes a 2026-07-14 review caveat. This is confusing provenance.

- `outputs/cleavage_sites.json` still encodes `accessibility: buried` for all sites. Machine-readable consumers can easily misread this as true structural burial.

- `README.md` remains over-strong:
  - “Computational analysis predicts low risk.”
  - “All protease recognition sites are in confidently-folded regions... structural evidence argues against significant proteolytic degradation.”
  - “reframing §1.10 as confirmation rather than feasibility gate.”
  
  This no longer matches the corrected caveat.

- `wiki-archive.md` is materially stale and over-strong:
  - “no exposed protease recognition sites”
  - “Every recognition site is buried”
  - “Wet-lab confirmation... shifts §1.10 from feasibility gate to confirmation experiment”
  - “real-world structure is more protease-resistant”
  - temperature/protease-concentration omissions framed mostly as conservative
  - comp-002 described as planned / low priority, whereas the current summary says comp-002 found MODERATE/YELLOW on another axis.

- `wiki/uricase-protease-stability-computational.md` is only a stub and lacks the explicit pLDDT-proxy caveat now present on comp-005, comp-012, and comp-037 pages.

- `wiki/computational-experiments.md` still states comp-001 as `LOW` with no caveat and says it “reframes from feasibility gate to confirmation experiment.”

- `wiki/validation-experiments.md` §1.10 still states the uricase arm is shifted “from a feasibility gate to a confirmation experiment.” This should be softened to “pLDDT-proxy prior; wet lab remains the actual stability test.”

- `wiki/uricase-shio-koji-thermal-stability-computational.md` says the combined picture is that proteases are not the load-bearing failure mode and thermal cooperative unfolding is. That may be a reasonable hypothesis after comp-002, but it should not rest on comp-001 as if comp-001 computed true protease exposure/survival.

## Generated-output and proposed-update inventory
| Path | Manifest kind | Inspected completely? | Finding |
|---|---|---:|---|
| `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/outputs/cleavage_sites.json` | generated_output | Yes | Numerically matches the implemented pLDDT-proxy model; machine-readable `accessibility: buried` is misleading because no SASA/burial calculation was run. |
| `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/outputs/summary.md` | generated_output / changed summary | Yes | Caveat improved, but residual “LOW risk,” “buried/exposed,” and generated-date wording remain stronger/less clear than the implementation supports. |
| `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/wiki-archive.md` | archived interpretive summary | Yes | Stale and materially over-strong relative to the corrected caveat; requires reconciliation or a prominent frozen/stale warning. |
| `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/README.md` | experiment summary | Yes | Stale: still frames §1.10 as confirmation and states low risk without the pLDDT/SASA caveat. |
| `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/analyze.py` | executable / changed | Yes | Writes updated caveat, but retains old generated date and inherits pLDDT-as-accessibility logic from shared library. |
| `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/inputs/Q00511.fasta` | input | Yes | Sequence length 302 aa; not independently verified against UniProt in this review. |
| `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/inputs/alphafold_Q00511_plddt.json` | input | Yes | 302 pLDDT entries; values support the reported pLDDT statistics by inspection. AlphaFold source not independently fetched. |
| `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/inputs/protease_specificities.json` | input | Yes | Supplies specificity and condition parameters; multiple stored fields are documentation-only. Primary literature values not independently verified. |
| `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/inputs/provenance.md` | provenance | Yes | Citation/provenance strings present; no primary-source verification performed in this review. |
| `wiki/uricase-protease-stability-computational.md` | affected wiki page | Yes | Stub lacks the caveat now present on related pLDDT-proxy pages. |
| `wiki/computational-experiments.md` | affected wiki index | Partially, relevant comp-001 section inspected | Needs caveat/softening for comp-001 entry. |
| `wiki/validation-experiments.md` | affected validation page | Partially, §1.10 relevant section inspected from bundle | Needs caveat/softening; wet lab should not be called mere confirmation based on comp-001. |
| `wiki/koji-endgame-strain.md` | affected mechanism/platform page | Partially, relevant uricase/format sections inspected | Some broader platform claims depend on uricase format viability; no direct comp-001 mismatch found in inspected excerpt beyond needing consistency with §1.33/§1.10 gates. |
| `wiki/engineered-koji-protocol.md` | affected protocol/platform page | Partially, relevant uricase/shio-koji sections inspected | Contains broader shio-koji “excellent preservation” framing; should remain conditional on §1.10 and comp-002/thermal concerns. |
| `wiki/aspergillus-oryzae.md` | affected mechanism/platform page | Partially, relevant protease/uricase sections inspected | No direct comp-001 citation issue found in inspected excerpt, but related platform claims should avoid treating comp-001 as survival evidence. |

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Q00511 sequence length 302 aa | `Q00511.fasta`, `cleavage_sites.json` | Sequence scanned for P1/P1′ motifs | Provenance cites UniProt; not independently fetched | Internally consistent; source unverified here. |
| Mean pLDDT 97.1, min 80.5, 100% ≥80 | `alphafold_Q00511_plddt.json`, outputs | Used to classify every cleavage window as `buried` | Provenance cites AlphaFold v6; not independently fetched | Internally consistent as pLDDT confidence, not burial. |
| pLDDT ≥80 means buried/protease-inaccessible | `protease_stability.py`, outputs | Central risk-classification mechanism | No valid physical provenance; shared library itself warns this is invalid proxy | Not supported as literal burial/accessibility. |
| ALP recognition sites = 215 | `protease_specificities.json`, outputs | P1 residue scan | MEROPS/literature cited; not independently verified | Code-consistent, but specificity simplified to P1/P1′ only. |
| NPr recognition sites = 97 | same | P1′ scan | MEROPS/literature cited; not independently verified | Code-consistent, simplified. |
| Acid protease recognition sites = 44 | same | P1+P1′ scan | MEROPS/literature cited; not independently verified | Code-consistent, simplified. |
| ALP residual activity at 17.5% NaCl = 0.188 | `protease_specificities.json`, `protease_stability.py`, outputs | Interpolated between 10% and 20% salt points | Literature cited; not independently verified | Reproducible, but ignores stored 15% datum; conservative at 17.5%. |
| NPr residual activity at 17.5% NaCl = 0.388 | same | Interpolated between 10% and 20% | Literature cited; not independently verified | Reproducible; ignores 15% datum with small effect. |
| Acid protease residual activity at 17.5% NaCl = 0.65 | same | Interpolated between 10% and 20% | Literature cited; not independently verified | Reproducible. |
| ALP/NPr pH factor = 1.0 | `protease_specificities.json`, outputs | Multiplies risk score | Chosen conservative scalar, not derived from pH curve | Conservative assumption, but not modeled from pH range. |
| Acid protease pH factor = 0.30 | same | Multiplies risk score | Koaze et al. cited; not independently verified | Assumption; no pH-range sensitivity in code. |
| 7–14 days exposure | conditions JSON, summaries | Output only | Shio-koji condition asserted | Not modeled; cannot support survival conclusion. |
| 22°C temperature | conditions JSON, summaries | Output only | Shio-koji condition asserted | Not modeled in comp-001. |
| “LOW protease degradation risk” | outputs, README, index | Derived from max single-site proxy score <0.15 | Threshold appears internal/heuristic | Overstated unless labeled “pLDDT-proxy low-site-confidence prior.” |
| “§1.10 is confirmation” | README, wiki-archive, computational index, validation §1.10 | Not implemented; interpretive propagation | Not evidence-derived | Unsupported; wet lab remains actual stability test. |
| “Tetramer makes monomer analysis conservative” | summary/wiki-archive | Not implemented | Biological plausibility only | Should be labeled uncomputed hypothesis. |
| “No exposed recognition sites” | outputs/wiki-archive/index phrasing | Actually means no low-pLDDT windows | No SASA/protease-access verification | Misleading as written. |

## Affected wiki pages
- `wiki/uricase-protease-stability-computational.md` — **change required** — add explicit pLDDT-proxy / not-SASA / not-survival-model caveat, consistent with comp-005/012/037 pages.
- `wiki/computational-experiments.md` — **change required** — comp-001 entry should not simply say `LOW` or “confirmation experiment”; mark as LOW/YELLOW pLDDT-proxy prior, wet-lab still actual test.
- `wiki/validation-experiments.md` — **change required** — §1.10 should not call uricase arm a confirmation experiment based on comp-001; it remains the empirical stability test, especially after comp-002 thermal/tetramer concerns.
- `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/wiki-archive.md` — **change required** — archived longform is materially over-strong and stale; either reconcile text or prepend a prominent frozen/stale caveat.
- `wiki/etc/experiments/comp-001-uricase-shio-koji-protease-stability/README.md` — **change required** — short answer/verdict must be softened and aligned with the summary caveat.
- `wiki/uricase-shio-koji-thermal-stability-computational.md` — **change required / consistency check** — “proteases are not the load-bearing failure mode” should be phrased as a pLDDT-proxy prior from comp-001, not as established protease-survival evidence.
- `wiki/koji-endgame-strain.md` — **already partly consistent** — the top-level gate order now correctly emphasizes §1.33/§1.9 staging; any residual shio-koji delivery claims should remain conditional on §1.10 and comp-002.
- `wiki/engineered-koji-protocol.md` — **change may be required** — broad “shio-koji preserves enzyme activity” language should not be extended to uricase without the §1.10 empirical gate and comp-002 thermal caveat.
- `wiki/aspergillus-oryzae.md` — **already mostly consistent in inspected sections** — no direct comp-001 citation mismatch found, but downstream uricase format claims should avoid treating comp-001 as survival evidence.

## New connections or implications
- The shared-library warning shows comp-001 belongs to the same pLDDT-proxy class as comp-005, comp-006, comp-012, and comp-037. The corpus should standardize labels for this whole family: “sequence-rule + pLDDT-confidence screen,” not “protease stability model.”
- The comp-001 result is best interpreted as: **Q00511 lacks low-confidence/disordered regions in the AlphaFold monomer, so obvious disorder-driven cleavage is not flagged.** That is useful, but it does not answer whether shio-koji proteases can access high-confidence surface segments over 7–14 days.
- Comp-002’s MODERATE/YELLOW thermal/tetramer result should dominate the current shio-koji uricase stability framing more than comp-001’s LOW proxy score. The combined message should be axis-dependent: protease-site proxy looks favorable; thermal/pH/tetramer stability remains a real gate.

## Required actions
1. Update `README.md` to align with the corrected summary: pLDDT-proxy prior only; no SASA/time/protease-concentration model; §1.10 remains the actual empirical test, not mere confirmation.
2. Update `wiki/uricase-protease-stability-computational.md` with an explicit caveat block matching the pLDDT-proxy warnings already present on related pages.
3. Update `wiki/computational-experiments.md` comp-001 entry to soften `LOW` and remove/qualify “reframes from feasibility gate to confirmation experiment.”
4. Update `wiki/validation-experiments.md` §1.10 to state that comp-001 lowers concern only on the low-pLDDT/sequence-site axis and does not close shio-koji stability.
5. Add a prominent stale/frozen caveat to `wiki-archive.md` or regenerate/rewrite it so it no longer claims literal burial, no exposed sites, or confirmation status.
6. Clarify machine-readable output semantics in future reruns, e.g. rename `accessibility` to `plddt_proxy_accessibility` or include an explicit `method_caveat` field in `cleavage_sites.json`.
7. Fix summary provenance wording: if regenerated or revised in 2026-07, do not leave only “Generated by analyze.py on 2026-05-05” without noting the later review/caveat edit.
8. If decision-grade protease stability is needed, run a true structural/accessibility follow-up: biological tetramer assembly, SASA/relative solvent accessibility, secondary-structure/conformation gate, pH/salt/temperature sensitivity, and exposure-time/protease-concentration model or wet-lab degradation assay.

## Review limits
- I did not execute the code; this was a read-only daemon inspection.
- I did not independently fetch UniProt, AlphaFold, MEROPS, or the cited primary literature. Provenance strings were inspected but not externally verified.
- Repository `grep_repo` failed because the runtime lacked `rg`; affected pages were assessed from the supplied explicit pages and targeted `read_file` calls.
- Only relevant portions of large wiki pages were inspected where full files exceeded practical review scope.
- No manifest SHA was supplied because this was daemon mode; review is bound to commit `eeab5b53054b93544c428a476dad06a8f8fe2621`.
