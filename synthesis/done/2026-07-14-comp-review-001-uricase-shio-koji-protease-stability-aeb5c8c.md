---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: aeb5c8c
comp: comp-001
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-001

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-001-aeb5c8c.md`](../../logs/comp-reviews/2026-07-14-comp-001-aeb5c8c.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-001

## Bottom-line verdict
Quantitative verdict invalid; the computation substitutes AlphaFold pLDDT confidence for solvent accessibility/burial and then applies an arbitrary single-site risk score. It is reproducible as a sequence-confidence screen, but it does **not** resolve whether *A. flavus* uricase retains meaningful activity after 7–14 days in shio-koji.

## Implementation and constraint closure
The artifact loads Q00511 sequence, per-residue pLDDT, and three *A. oryzae* protease rule sets; scans adjacent residues for P1/P1′ matches; classifies a ±3 residue pLDDT window as “buried / partially exposed / exposed”; interpolates salt inhibition at 17.5% NaCl; multiplies by a fixed pH factor and an accessibility weight; and reports the maximum per-site score.

Load-bearing closure problems:

- **Question/model mismatch:** The stated question is retained uricase activity over 7–14 days. The code does not model cleavage kinetics, protease concentration, enzyme/protein mass, residence time, cumulative site hazard, activity loss per cut, tetramer integrity, pH unfolding, thermal instability, or actual solvent access.
- **Hidden substitution:** “High pLDDT” is treated as “buried.” This is physically wrong. pLDDT is local model confidence, not solvent accessibility. A high-confidence surface helix or terminus can be fully exposed. The current shared library itself now warns that this proxy under-counted real lactoferrin cleavage risk by ~10× in a later SASA check.
- **N/C-terminal issue:** Top-ranked ALP sites include positions 1–5 and are classified “buried” because pLDDT windows are high. Termini are often solvent-accessible even when confidently modeled. This alone invalidates “no exposed termini.”
- **Stored-but-unused / silent simplifications:**
  - `duration_days` is stored and printed but never used.
  - `temperature_C` is stored and printed but never used.
  - `pH_range` is stored and printed but not used to calculate pH activity.
  - `active_pH_range` and `optimal_pH` are not used; only pre-entered `ph_activity_at_shio_koji` is used.
  - `NaCl_pct_range` is not used; the model only evaluates the midpoint 17.5%.
  - `type`, `family`, `merops_id`, and notes are provenance/documentation only.
  - Salt interpolation uses only 10% and 20% points, not the stored 15% point, though the numerical effect here is small.
- **Arbitrary risk score:** `risk_score = accessibility_weight × salt_activity × pH_factor`; “buried” is fixed to 0.1. No source is given for the weights or the LOW/MODERATE/HIGH thresholds.
- **No cumulative hazard:** 356 recognition sites are reduced to the maximum single-site score. The model never asks whether many low-probability cuts over 7–14 days accumulate into meaningful degradation.
- **Reaction/constraint gaps:** Protease hydrolysis requires enzyme concentration, substrate accessibility, water, pH, ionic strength, and time; NPr also depends on metalloprotease cofactors/metal stability. These are not modeled. Uricase reaction constraints—urate, O₂, H₂O₂ coproduct, tetramer activity—are outside this protease scan and not closed here.
- **Compartment/localization gap:** Whether uricase is secreted into shio-koji pore fluid, retained intracellularly/peroxisomally, tetrameric, partially unfolded at pH 4.5–5.2, or shielded by matrix/cell wall is not represented.
- **Sensitivity gap:** The dominant uncertainties are SASA/accessibility, protease concentration/activity over time, pH/thermal unfolding, tetramer state, and fermentation dynamics. The model effectively varies none of them.

The computation can support only a narrow statement: **Q00511 has uniformly high AlphaFold confidence and many simple P1/P1′ motifs; no low-pLDDT/disordered regions were detected.** It cannot support “all sites are buried,” “no exposed loops or termini,” or “protease degradation is unlikely to meaningfully reduce activity.”

## Summary-fidelity audit
- `README.md` overstates the result: “low risk,” “all recognition sites are in confidently-folded regions,” and “structural evidence argues against significant proteolytic degradation” are stronger than the implementation supports. “Confidently folded” is true by pLDDT; “buried/protected” is not established.
- `outputs/summary.md` is not faithful to the physical limits of the code. It says “no disordered loops or exposed termini” and “all potential cleavage sites … in confidently-folded regions” as if that establishes protease inaccessibility. The former is not derived; the latter is not equivalent to accessibility.
- `wiki-archive.md` / interpretive page language is too strong: “no exposed protease recognition sites,” “every recognition site is buried,” “zero exposed cleavage sites,” and “monomer analysis is conservative” are not established. Tetramer burial may protect some sites, but monomer-only analysis without SASA cannot prove conservatism.
- `wiki/computational-experiments.md` repeats the unsupported quantitative verdict: “LOW risk,” “all 356 recognition sites … confidently-folded,” “no exposed loops or disordered termini,” and max risk 0.039 as if meaningful.
- `wiki/validation-experiments.md` §1.10 partially preserves the right wet-lab gate, but the comp-001 prior reframes the uricase arm as a “confirmation experiment.” That is too strong for protease survival, and especially too strong for “meaningful activity retained” because comp-002 separately flags thermal/pH/tetramer stability as MODERATE/YELLOW.
- Relevant platform pages now updated after later comps correctly stage UOX topology and peroxide questions (§1.33/§1.36), but older shio-koji delivery-format language should not rely on comp-001 as proof of uricase stability.
- Reproducibility claim is mostly plausible but incomplete: `analyze.py` imports a repo-internal shared library `wiki/etc/experiments/lib/protease_stability.py`, which is not in the comp directory inventory and is not mentioned as a dependency in the README. The stated “stdlib only” claim is true for Python packages but omits the repo-local dependency.

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| Q00511 sequence length 302 aa | `inputs/Q00511.fasta`; `outputs/cleavage_sites.json` | Sequence scanned for P1/P1′ sites | FASTA included; source named as UniProt, not independently fetched here | Internally usable; note some wiki pages say 301 aa and need reconciliation |
| AlphaFold pLDDT mean 97.1, min 80.5 | `inputs/alphafold_Q00511_plddt.json`; summary outputs | Computes sequence stats and accessibility class | JSON included; original PDB/B-factor extraction not included | Reproducible from artifact, but source extraction unverified |
| pLDDT ≥80 = “buried” | `protease_stability.py` thresholds | Load-bearing accessibility classification | No valid provenance; pLDDT is not SASA | Invalid physical substitution |
| pLDDT <65 = exposed | `protease_stability.py` | Used to count exposed sites | AlphaFold confidence categories loosely related to disorder, not surface exposure | Useful for disorder screen only, not solvent exposure |
| Accessibility weights buried 0.1, partial 0.4, exposed 1.0 | `protease_stability.py` | Directly sets risk scores | No source given | Arbitrary; quantitative risk invalid |
| LOW threshold <0.15 | `analyze.py` summary logic | Sets final verdict | No source given | Arbitrary; cannot support verdict |
| ALP P1 specificity list | `inputs/protease_specificities.json` | Generates 215 sites | MEROPS/literature named but not included or line-verified | Unverified hand-encoding |
| NPr P1′ specificity list | `inputs/protease_specificities.json` | Generates 97 sites | MEROPS/literature named but not included | Unverified hand-encoding |
| Acid protease P1/P1′ specificity | `inputs/protease_specificities.json` | Generates 44 sites | MEROPS/Koaze named but not included | Unverified hand-encoding |
| ALP residual activity ~18.8% at 17.5% NaCl | JSON salt table; library interpolation | Multiplicative risk factor | Citation strings only; original curves unavailable | Numerically traceable, primary-source unverified |
| NPr residual activity ~38.8% at 17.5% NaCl | JSON salt table; library interpolation | Multiplicative risk factor | Citation string only | Traceable, uncertain, unverified |
| Acid protease residual activity 65% and pH factor 30% | JSON | Multiplicative risk factor | Citation string / estimate only | Traceable, high uncertainty |
| ALP/NPr pH factors set to 1.0 | JSON | Used directly | Deliberately conservative note, but active ranges not computed | Conservative for those enzymes, but does not rescue model |
| Shio-koji pH 4.5–5.2, 17.5% NaCl, 22°C, 7–14 d | `protease_specificities.json`; outputs | Only NaCl midpoint affects computation; others printed | Source not directly verified | Mostly unused scenario metadata |
| “All 356 sites are buried” | `outputs/summary.md`; `wiki-archive.md` | Derived from pLDDT proxy | Not derived from SASA or structure | Unsupported |
| “No exposed loops or termini” | README/summary/archive/index | Interpretive conclusion | Not implemented; termini not structurally assessed | Unsupported |
| “Uricase homotetramer makes monomer analysis conservative” | summary/archive | Not implemented | Biological fact likely, but not verified in artifact | Unresolved; may be true for interface sites, not a blanket protection claim |
| “§1.10 becomes confirmation, not feasibility gate” | README, summary, archive, validation page | Summary recommendation | Depends on unsupported quantitative verdict and ignores thermal/pH axis | Too strong |

## Affected wiki pages
- `wiki/uricase-protease-stability-computational.md` — change required — the archived analysis it points to contains unsupported “buried/no exposed site/LOW risk” language.
- `wiki/computational-experiments.md` — change required — comp-001 entry should be recast from LOW quantitative verdict to “high-pLDDT disorder screen; protease accessibility unresolved pending SASA/wet lab.”
- `wiki/validation-experiments.md` — change required — §1.10 should not describe the uricase arm as merely confirmation on the basis of comp-001. It remains an empirical stability gate, with protease, thermal/pH, tetramer, and activity readouts.
- `wiki/uricase-shio-koji-thermal-stability-computational.md` — change required — its “proteases are not the load-bearing failure mode” conclusion should be softened because comp-001 did not actually establish solvent accessibility.
- `wiki/engineered-koji-protocol.md` — change required — delivery-format statements implying shio-koji preserves uricase activity should be qualified; comp-001 does not prove protease survival, and comp-002 flags thermal/pH risk.
- `wiki/koji-endgame-strain.md` — already mostly consistent after comp-044/045 staging — it correctly moves UOX topology/system gating upstream; any residual “shio-koji works for uricase” framing should not cite comp-001 as decisive.
- `wiki/uricase.md` — change required — reconcile Q00511 length wording (301 vs artifact’s 302 aa) and avoid implying oral/koji uricase stability is established by comp-001.
- `wiki/aspergillus-oryzae.md` — change required where it repeats shio-koji/delivery-format confidence — should distinguish wild-type enzyme preservation from heterologous uricase activity retention.
- `wiki/lactoferrin-protease-stability-computational.md` — change required / cross-model caveat — uses the same pLDDT accessibility proxy class; later SASA warning should be propagated to archived quantitative claims.
- `wiki/daf-cd55-protease-stability-computational.md` — change required / cross-model caveat — same pLDDT proxy affects exposed/buried claims.
- `wiki/daf-cd55-scr14-truncated-computational.md` — change required / cross-model caveat — same pLDDT proxy affects “LOW / all buried” style conclusions.

## New connections or implications
- Later comp-002 materially changes interpretation: even if protease risk were low, “meaningful activity retained” is dominated by thermal/pH/tetramer stability. comp-001 should be explicitly narrowed to the protease-axis screen.
- The shared `protease_stability.py` caveat means this is not isolated to comp-001. Any comp using the pLDDT-as-accessibility model should be reclassified as a disorder-confidence screen unless a SASA/secondary-structure reanalysis exists.
- Uricase topology matters for protease exposure: intracellular/peroxisomal, cell-associated, displayed, or secreted UOX will experience different protease access and catalase co-localization. comp-001 assumes a free folded monomer/tetramer substrate but does not state or model topology.
- The top-ranked sites being at the N-terminus provides a concrete wet-lab diagnostic: Western blot or mass spec should watch for N-terminal trimming even if the folded core remains intact.

## Required actions
1. Re-run or replace the accessibility model with explicit SASA on an appropriate structure: AlphaFold PDB and preferably biological tetramer/crystal structure. Verification criterion: report cleavage sites by relative SASA, secondary structure, N/C-terminal status, and tetramer-interface burial; remove pLDDT-as-burial scoring.
2. Rewrite comp-001 outputs/README/interpretive text/index entry. Verification criterion: no page says “all sites buried,” “no exposed termini,” or “LOW risk” unless supported by SASA/kinetic evidence; allowed wording is “no low-pLDDT/disordered sites detected.”
3. Add a kinetic/time-bound model or explicitly narrow the question. Verification criterion: either include protease concentration/activity, cumulative 7–14 day exposure, cleavage-rate assumptions, and retained-activity mapping, or state that retained activity cannot be predicted from this artifact.
4. Update `validation-experiments.md` §1.10. Verification criterion: uricase shio-koji stability remains an empirical gate with native-PAGE/tetramer, activity, Western degradation pattern, pH/temperature tracking, and microbial/protease controls.
5. Fix reproducibility/provenance. Verification criterion: README names the repo-local shared library dependency; provenance includes checksums or archived source extracts for UniProt/AlphaFold/MEROPS/literature-derived values, or explicitly labels them unverified hand-encodings.
6. Reconcile Q00511 length across wiki pages. Verification criterion: pages consistently distinguish UniProt Q00511 artifact length from any rasburicase/mature-form numbering if they differ.

## Review limits
I did not execute the code. Primary sources named in provenance—UniProt live record, AlphaFold PDB, MEROPS entries, and salt/pH literature curves—were not fetched or independently verified. Repository fixed-string search failed because the underlying `rg` binary was unavailable, so affected-page discovery used the provided bundle plus manual inspection of likely linked pages. Some long wiki pages were inspected only in bounded chunks. The review therefore verifies internal traceability and model fit, not primary-source truth.

---

## ✓ Closed as duplicate 2026-07-14

comp-001 was reviewed twice in the 2026-07-14 backfill run (this item = trigger sha `aeb5c8c`; the fuller item = sha `f7ef901`). Both audits reached the same verdict (pLDDT-proxy substituted for SASA; quantitative "no exposed sites" over-strong). **Actioned via `f7ef901`** (relabel + comp-002 axis note); no separate work needed here.
