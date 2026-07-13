---
type: comp-review
sweep_date: 2026-07-13
sweep_sha: fae0e36
comp: comp-006
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-006

Canonical review log: [`logs/comp-reviews/2026-07-13-comp-006-fae0e36.md`](../../logs/comp-reviews/2026-07-13-comp-006-fae0e36.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-006

## Bottom-line verdict
Action required — the qualitative finding is mostly supported as a **stalk-contingent protease-liability prior**, but the artifact contract is not clean. The committed code/output summary and README still contain the known-wrong **“3 disulfides per SCR / 12 total”** claim, while the archived wiki text and later corpus correctly say **2 per SCR / 8 total**. The numeric **HIGH** verdict is also a heuristic stress-test, not a kinetic survival model; it depends on conservative NPr pH activity set to 1.0 and on pLDDT-as-accessibility rather than SASA.

## Implementation and constraint closure
I traced the computation through `analyze.py`, `inputs/protease_specificities.json`, `inputs/P08174.fasta`, `inputs/alphafold_P08174_plddt.json`, `outputs/cleavage_sites.json`, and `outputs/summary.md`, plus the shared library `wiki/etc/experiments/lib/protease_stability.py`.

What the implementation actually does:

- Loads the 381 aa UniProt P08174 sequence and per-residue AlphaFold pLDDT.
- Scans every adjacent residue pair for P1/P1′ matches against three proteases: ALP, NPr, acid protease.
- Scores each matched site as:

  `risk_score = pLDDT-derived accessibility weight × interpolated salt residual activity × ph_activity_at_shio_koji`

- Uses pLDDT window mean as the exposure proxy:
  - `>=80` → “buried” weight 0.1
  - `65–80` → “partially_exposed” weight 0.4
  - `<65` → “exposed” weight 1.0
- Filters sites into three scopes:
  - full sequence aa 1–381
  - mature protein aa 35–381
  - soluble ectodomain aa 35–353
- Computes verdict solely from the **maximum single-site risk score** across proteases, not from cumulative site count, degradation kinetics, protein half-life, enzyme concentration, or activity remaining.

Key implementation findings:

- **Stored-but-unused / documentation-only inputs:** `active_pH_range`, `optimal_pH`, `NaCl_pct_range`, `temperature_C`, and `duration_days` are not mechanistically used in the scoring. They are stored and printed. The pH factor is taken directly from `ph_activity_at_shio_koji`; time and temperature do not affect risk.
- **15% NaCl residual activity is stored but unused.** The interpolation uses only 10% and 20% values. At 17.5% NaCl this slightly changes ALP and NPr if piecewise interpolation through the 15% point were used, but does not change the headline NPr-driven HIGH under the current pH factor.
- **The HIGH verdict depends on conservative NPr pH activity = 1.0.** The JSON note itself says true NPr activity at pH 4.5–5.0 is likely 0.3–0.5. If NPr pH factor were 0.5, the NPr max score would be about 0.194; if 0.3, about 0.116. Then the ectodomain headline could shift from HIGH to MODERATE/LOW depending on acid protease and thresholds. The summary notes conservatism but does not make the dependency explicit enough.
- **The pLDDT accessibility proxy is load-bearing.** The shared library now contains a caveat, added after comp-034, that pLDDT is not solvent accessibility and can undercount confidently modeled exposed helices/loops. For comp-006, this does not invalidate the stalk-liability signal because the stalk is low-pLDDT/disordered, but it weakens the strong wording “SCR1–4 contribute zero exposed sites.” More precise wording is “zero low-pLDDT exposed-by-proxy sites; no SASA calculation was performed.”
- **No finite degradation model is implemented.** Duration 7–14 days is printed but not used. The score is not a predicted percent survival, cleavage probability, or retained activity.
- **No protease abundance, enzyme kinetics, transport/localization, replenishment, or host-strain protease-deletion state is modeled.** The model assumes extracellular soluble CD55 is physically accessible to the listed native koji proteases under the specified salt/pH condition.
- **Reaction closure is partial.** Substrate is the CD55 polypeptide; products would be cleavage fragments. Water is implicit. NPr zinc requirement is mentioned in the input notes but not modeled; protease concentrations and active-site kinetics are absent.
- **Glycosylation and disulfides are not modeled.** O-glycosylation of the Ser/Thr stalk could shield or alter the risk; *A. oryzae* O-glycans may differ from native mammalian glycans. SCR disulfides reduce flexibility but are absent from scoring.
- **Generated summary has stale biology encoded in code.** `write_summary()` still writes “3 disulfides per SCR” and “12 total in SCR1-4.” This is not a one-off markdown typo; a rerun will regenerate the wrong statement unless `analyze.py` is fixed.

Overall, the computation answers: “Does a pLDDT/P1-P1′ heuristic identify low-confidence CD55 regions that match broad koji protease motifs under conservative salt/pH activity assumptions?” It does **not** directly answer: “Will the soluble ectodomain retain meaningful complement-regulatory activity after 7–14 days in shio-koji?”

## Summary-fidelity audit
Artifact-summary agreement is mixed.

Clean / supported:

- README, output JSON, output summary, and wiki archive agree on the main computed numbers:
  - full / mature / ectodomain verdicts: HIGH / HIGH / HIGH
  - worst protease: NPr
  - worst score: 0.388
  - ectodomain exposed-site counts: ALP 48, NPr 9, acid protease 1
  - stalk aa 286–353 as driver
- `wiki/computational-experiments.md` correctly describes comp-006 as stalk-contingent and notes comp-012 later became the follow-up.
- `wiki/daf-cd55-protease-stability-computational.md` is now only a stub pointing to the archived experiment, so it does not itself repeat most stale numerical claims.
- `wiki/hypotheses/H05-daf-scr14-cp0-thesis.md`, `wiki/complement-c5a-gout.md`, `wiki/chaperone-orthogonal-stacking.md`, and `wiki/daf-lactoferrin-ecn-folding-feasibility-computational.md` mostly use the corrected **8-disulfide** DAF SCR1–4 count.

Mismatches / stale claims requiring action:

- `outputs/summary.md` says each SCR domain contains **3 disulfides / 6 Cys** and comparison table says **12 total in SCR1–4**. This is wrong.
- `analyze.py` will regenerate that wrong disulfide text on every rerun.
- `README.md` structural interpretation also says SCR1–4 have **3 disulfides / domain**, contradicting the corrected archive and later corpus.
- `wiki-archive.md` has been corrected in the trigger diff, but the committed generated output and README have not been reconciled.
- README’s reproduction command says `cd experiments/comp-006-...`; the tracked path is `wiki/etc/experiments/comp-006-...`. As written, the command is likely wrong from repository root.
- README still says “comp-007” is the logical follow-up. The corpus says the actual follow-up became **comp-012**. If the README is meant to be historical, it should say so; otherwise it is stale.
- `wiki/modality-chokepoint-matrix.md` has an older “Open exploration questions” paragraph still saying comp-006’s next step is comp-007 and “expected LOW,” despite comp-012 being complete.
- Several corpus surfaces repeat “zero exposed sites” for SCR1–4 without making clear this is **zero exposed by the pLDDT proxy**, not a physical SASA result.
- Some pages still phrase DAF SCR1–4 folding as comfortably within “demonstrated capacity” rather than “predicted tractable but empirically unproven.” The trigger diff correctly softened this wording in `wiki-archive.md`; similar wording should be audited in linked pages.

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| CD55 sequence length 381 aa | `inputs/P08174.fasta`, `inputs/provenance.md` | Directly loaded by `load_sequence()` | UniProt REST URL and fetch date provided; primary source not independently fetched in this review | Plausible, not primary-verified here |
| Signal peptide aa 1–34 | `analyze.py` constants; `inputs/provenance.md`; outputs | Used to compute mature scope | Named as UniProt P08174 SV=4 annotation; UniProt flatfile not included | Plausible, not primary-verified here |
| Soluble ectodomain aa 35–353 | `analyze.py`; provenance; outputs | Used to compute operational ectodomain verdict | Named as UniProt P08174 SV=4; direct source not included | Plausible, but boundary should remain verification-gated |
| Stalk aa 286–353 | `analyze.py`; provenance; README; summary | Used for stalk-specific counts | Boundary based on pLDDT drop and annotation, not an external primary feature in artifact | Reasonable heuristic; not primary-verified |
| pLDDT values, mean 78.3, min 29.9 | `inputs/alphafold_P08174_plddt.json`; outputs | Directly used for site-window accessibility | AlphaFold confidence JSON URL named; original not included | Internally traceable; not independently verified |
| pLDDT thresholds 80/65 and weights 0.1/0.4/1.0 | `wiki/etc/experiments/lib/protease_stability.py` | Core scoring mechanism | No calibration source; library-defined heuristic | Load-bearing heuristic; not a physical accessibility measurement |
| ALP/NPr/acid P1/P1′ specificity | `inputs/protease_specificities.json` | Directly used in `find_cleavage_sites()` | MEROPS/citations named but not included; source copied from comp-005 | Traceable to artifact, not source-verified |
| Salt residual activity at 17.5% NaCl | `protease_specificities.json`; library interpolation | Directly multiplies risk | Source strings named; 15% stored point unused | Partially closed; interpolation choice should be documented |
| pH factors ALP 1.0, NPr 1.0, acid 0.30 | `protease_specificities.json` | Directly multiplies risk and drives HIGH | JSON notes admit ALP/NPr are conservative defaults; primary curves not present | Load-bearing; sensitivity needed because NPr factor controls HIGH |
| Conditions pH 4.5–5.2, 22°C, 7–14 days | `protease_specificities.json`; outputs | Printed only; not used except NaCl | Shio-koji condition note only | Not implementation-closed for time/temperature |
| Ectodomain NPr max risk 0.388 | `outputs/cleavage_sites.json`; `outputs/summary.md` | Derived from exposed weight 1.0 × NPr salt 0.388 × pH 1.0 | Internally reproducible by code inspection | Correct under model assumptions; not a survival probability |
| Ectodomain exposed sites: ALP 48, NPr 9, acid 1 | outputs; README | Derived from site scan and pLDDT proxy | Internally traceable | Correct as proxy counts; should not be overread as SASA |
| “SCR1–4 contribute zero exposed sites” | README, wiki archive, computational index | Derived from pLDDT proxy counts | No SASA or structural solvent-accessibility calculation | Needs wording correction: zero low-pLDDT exposed-by-proxy sites |
| DAF SCR1–4 disulfides = 8, 2 per SCR | Corrected `wiki-archive.md`; H05; later corpus | Not used in scoring; interpretive only | UniProt feature positions named in archive; source not bundled | Corrected corpus claim plausible; artifact output/README still wrong |
| DAF SCR1–4 disulfides = 12, 3 per SCR | `outputs/summary.md`; `analyze.py`; README | Interpretive output, not scoring | Known hallucinated/incorrect claim | Must be fixed and regenerated |
| Verdict thresholds LOW <0.15, MODERATE <0.30, HIGH ≥0.30 | `analyze.py` | Directly maps score to verdict | No external calibration | Arbitrary qualitative bins; should be labeled heuristic |

## Affected wiki pages
- `wiki/etc/experiments/comp-006-daf-cd55-shio-koji-protease-stability/README.md` — change required — wrong 3-disulfides-per-SCR claim; stale comp-007 follow-up; likely wrong repo-root reproduction path.
- `wiki/etc/experiments/comp-006-daf-cd55-shio-koji-protease-stability/analyze.py` — change required — `write_summary()` regenerates the wrong 3/SCR and 12-total disulfide text.
- `wiki/etc/experiments/comp-006-daf-cd55-shio-koji-protease-stability/outputs/summary.md` — change required — generated output contains the stale disulfide count and should be regenerated after code correction.
- `wiki/etc/experiments/comp-006-daf-cd55-shio-koji-protease-stability/wiki-archive.md` — already partly consistent — trigger diff correctly softens the disulfide-capacity wording and archive already has 8 disulfides; consider adding pLDDT-proxy/SASA caveat if archive is still considered interpretive.
- `wiki/daf-cd55-protease-stability-computational.md` — already mostly consistent — stub points to archive; no detailed stale numerical claims found.
- `wiki/computational-experiments.md` — change required — comp-006 entry is broadly correct but should qualify “zero exposed sites” as pLDDT-proxy exposure, not physical SASA.
- `wiki/modality-chokepoint-matrix.md` — change required — one row is up to date, but the “Open exploration questions” / per-modality prose still says comp-007 is the next step and expected LOW; comp-012 is already complete. Also qualify comp-006/012 exposure claims as proxy-based.
- `wiki/complement-c5a-gout.md` — change likely required — mostly reconciled to 8 disulfides and §1.25, but wording such as “effective PDI load 2.4–4.8 vs demonstrated capacity of 16” should be softened to match the corrected “predicts tractability but does not demonstrate capacity” framing.
- `wiki/chaperone-orthogonal-stacking.md` — change required — mostly correct on 8 DAF disulfides and 16 lactoferrin disulfides, but §5.5.1 still shows lactoferrin as 17 in one table while later text uses 16; also relevant to DAF capacity wording.
- `wiki/hypotheses/H05-daf-scr14-cp0-thesis.md` — already consistent on disulfide count and wet-lab gates; optional update to add the pLDDT/SASA limitation if not already covered in the full-card upgrade.
- `wiki/validation-experiments.md` — likely already consistent at the dashboard/§1.25 level, but should be audited for “demonstrated capacity” wording and for pLDDT-proxy caveat in the DAF SCR1–4 gate.
- `wiki/daf-cd55-scr14-truncated-computational.md` — already consistent as a stub, but downstream archived comp-012 should be checked for the same pLDDT-as-accessibility limitation because it shares the library.
- `wiki/daf-lactoferrin-ecn-folding-feasibility-computational.md` — already consistent — correctly treats DAF SCR1–4 as 8 disulfides and notes capacity-gated folding for EcN; no comp-006 correction required.

## New connections or implications
- The comp-034 library caveat now directly affects how comp-006 and comp-012 should be worded. The stalk conclusion remains robust because low pLDDT/disorder is a genuine protease-liability signal, but the SCR-domain claim should be softened from “zero exposed sites” to “zero low-pLDDT exposed-by-proxy sites; SASA not run.”
- The full-ectodomain HIGH verdict is less stable than the prose implies. If NPr’s true pH factor is 0.3–0.5, as the input note itself suggests, the max score could drop below the HIGH threshold. That does not eliminate the stalk as an engineering liability, but it changes the verdict from “predicted significant degradation” to “conservative stress-test flags a disordered stalk.”
- The known disulfide-count hallucination is not fully contained: the archive was fixed, but the executable summary generator and committed output still reproduce it. Any future automated synthesis that reads `outputs/summary.md` rather than `wiki-archive.md` could re-contaminate the corpus.
- comp-006’s model is useful as a **construct-ranking heuristic** but not as a degradation/survival model. Wet-lab prioritization should not treat 0.388 as a percent cleavage, rate constant, or retained-activity estimate.

## Required actions
1. **Fix comp-006 generator and outputs.** Owner: comp-006 artifact maintainer. Update `analyze.py::write_summary()` to say **2 disulfides per SCR, 8 total in SCR1–4**, not 3/12; rerun `python3 analyze.py`; verify `outputs/summary.md` and `outputs/cleavage_sites.json` remain otherwise unchanged except summary text.
2. **Fix README.** Owner: comp-006 artifact maintainer. Correct the SCR disulfide count, update the reproduction path to the actual repo-relative path, and either replace “comp-007” with “comp-012” or explicitly mark the statement as historical.
3. **Add pH-factor sensitivity or relabel verdict.** Owner: comp-006 maintainer. Either add a small ALP/NPr pH sensitivity table using NPr 0.3–0.5 and ALP near-zero, or explicitly label HIGH as a **conservative stress-test verdict dependent on NPr pH factor = 1.0**. Verification criterion: output summary identifies whether realistic pH factors could move ectodomain HIGH to MODERATE/LOW.
4. **Propagate pLDDT-proxy wording.** Owner: wiki maintainer. Update `computational-experiments.md`, `modality-chokepoint-matrix.md`, and relevant DAF/H05 pages to say “zero low-pLDDT exposed-by-proxy sites” rather than physically “zero exposed sites,” unless/until SASA confirms it.
5. **Clean stale corpus surfaces.** Owner: wiki maintainer. Update `modality-chokepoint-matrix.md` sections still saying comp-007 is pending/expected; replace with comp-012 completed LOW and its limitations.
6. **Primary-source verification packet.** Owner: comp-006 maintainer. Include or cite exact UniProt feature lines for CD55 boundaries/disulfides and exact protease/salt/pH source excerpts, or state that provenance is citation-only. Verification criterion: every load-bearing number in the table above has a directly inspectable source or is explicitly labeled unverified.
7. **If SCR-domain protease stability is used for wet-lab prioritization, run a SASA/refined structural pass.** Owner: DAF SCR1–4 wet-lab planning surface / §1.25 owner. Verification criterion: solvent-accessible cleavage sites in SCR1–4 are quantified from structure, not inferred solely from pLDDT.

## Review limits
- I did not execute `analyze.py`; reproducibility was assessed by code and committed-output inspection only.
- I did not fetch UniProt, AlphaFold, MEROPS, or the named historical protease papers; provenance status is therefore “named/citation-only” unless the source text was included in the artifact.
- Repository `grep_repo` failed because the backend `rg` executable was unavailable, so corpus search was performed by reading the bundle and selected omitted pages with `read_file`, not by full-text grep.
- `wiki/validation-experiments.md` is large; I relied on the provided bundle excerpts plus bounded reads rather than a full-file audit.
- The review does not assess clinical efficacy or safety of CD55/DAF as an intervention; this is Phase 0 computational scrutiny only.
