---
type: comp-review
sweep_date: 2026-07-14
sweep_sha: 8ee4d25
comp: comp-037
reviewer_model: openai/gpt-5.5
pass3_verdict: Independent comp audit
overlap_tag: N/A
---

# Independent artifact review requires action: comp-037

Canonical review log: [`logs/comp-reviews/2026-07-14-comp-037-8ee4d25.md`](../../logs/comp-reviews/2026-07-14-comp-037-8ee4d25.md)

ACTION_REQUIRED: yes

# Independent comp review — comp-037

## Bottom-line verdict
Action required — the artifact is reproducible by inspection and internally coherent at the “sequence-rule + pLDDT proxy” level, but the corpus overstates that proxy as protease survival. The quantitative LOW/MODERATE framing needs stronger caveats or SASA/kinetic follow-up, the README has a stale RCL site count, the stated reproduction path is path-inconsistent, and the C1-INH wet-lab gate is not fully propagated into the validation queue.

## Implementation and constraint closure
The code loads the C1-INH sequence, AlphaFold pLDDT, and a five-protease EcN/colonic panel; scans P1/P1′ motifs; scores each site as `accessibility_weight × salt_activity × pH_factor`; partitions sites into full/mature/core/non-RCL/RCL scopes; and writes JSON plus `summary.md`.

Key closure findings:

- **Model fit is limited.** The computation answers: “Which P1/P1′ motif sites fall in low-pLDDT windows under fixed activity multipliers?” It does **not** directly answer “will C1-INH survive the colonic lumen?” because it does not model protease concentration, enzyme kinetics, substrate concentration, residence time, degradation half-life, secretion route, true solvent accessibility, or target-vs-off-target RCL competition.
- **pLDDT is used as burial/accessibility.** The shared library now explicitly warns that this proxy can misclassify confidently predicted surface helices/loops as “buried” and states the caveat affects comp-037. Therefore “zero exposed non-RCL sites” is a proxy-output statement, not physical protease-access closure. A SASA/refined structural rerun is needed before the corpus can treat the non-RCL LOW score as a robust body-stability result.
- **Duration/time is stored but unused.** `duration_days: [1,7]` appears in input and output summaries as “conditions modeled,” but no calculation uses time or cumulative exposure. This is load-bearing for any survival claim.
- **pH range/temperature/active ranges are mostly documentary.** The algorithm uses only fixed `ph_activity_at_shio_koji` multipliers; it does not derive those from `pH_range`, `active_pH_range`, `optimal_pH`, or temperature.
- **Salt fields are only partly operative.** Salt interpolation uses 10% and 20% values and clamps below 10%; at 0.9% NaCl all proteases return 1.0. This is acceptable for the chosen physiological-salt assumption, but the 15% values are not used.
- **Compartment mismatch remains unresolved.** DegP is periplasmic quality-control protease; target complement proteases act after secretion at luminal/mucus/surface sites. The RCL “kinetic competition” framing is biologically plausible as an engineering assay, but the real system may be sequential/route-dependent rather than a single well-mixed competition between C1s and DegP.
- **RCL risk is correctly separated conceptually, but not quantified kinetically.** The code reports RCL exposure and non-RCL body risk separately; that is good. But it cannot determine productive C1r/C1s/MASP-2 trapping vs. unproductive DegP/elastase cleavage.
- **Glycosylation feasibility is categorical, not computed from evidence.** The GREEN call rests on cited literature that deglycosylated C1-INH can retain inhibitor function and on the luminal-topology argument that plasma half-life is moot. The artifact provides citation strings but not primary-source text. N272 is included as a “variant” site despite the canonical sequence lacking an N-X-S/T sequon; this should be worded as a variant annotation, not a canonical remaining N-glycan.
- **Reaction/constraint closure is incomplete.** Complement targets, off-target protease concentrations, colonic residence, secretion topology, transport/access to CP0 priming sites, local complement suppression, LBP containment, endotoxin/safety handling, and microbiome protease load are all acknowledged partially or not modeled. These gaps are acceptable for Phase 0 only if the conclusions remain explicitly prior-level.

## Summary-fidelity audit
- **README mismatch:** The README headline table says “DegP and elastase have 9 + 13 exposed sites in the RCL,” while the generated outputs and interpretive wiki page report elastase RCL exposed sites as **11**. The README must be corrected to 9 + 11 unless a rerun changes outputs.
- **README reproduction path mismatch:** The README command says `cd experiments/comp-037-c1-inh-protease-stability-ecn`, but the committed path is `wiki/etc/experiments/comp-037-c1-inh-protease-stability-ecn/`. The script/library references also omit the `wiki/etc/` path. This weakens the reproducibility contract.
- **Output/JSON agreement:** `outputs/summary.md` and `outputs/cleavage_sites.json` are mutually consistent for the key numerical outputs: non-RCL serpin-core LOW, worst non-RCL OmpT 0.1, RCL DegP 0.8, elastase RCL 11, DegP RCL 9.
- **Interpretive page agreement:** `wiki/c1-inh-protease-stability-ecn-computational.md` faithfully preserves the intended decomposition: non-RCL LOW, RCL RED but by-design, glyco GREEN, combined MODERATE. However, wording such as “serpin body folds and persists” and “no exposed protease sites” should be softened to “under the pLDDT proxy” unless SASA/kinetic validation is added.
- **Computational index agreement:** `wiki/computational-experiments.md` is broadly consistent, including MODERATE kinetic-gated verdict and glyco GREEN. It adds Liu 2004 as a load-bearing glycosylation/function anchor; that source is not directly available in the comp-037 artifact and should be marked as citation-only unless the artifact is expanded.
- **Validation propagation incomplete:** The interpretive page says a sister wet-lab gate for C1-INH should be added. In the inspected validation dashboard there is no C1-INH RCL kinetic-competition experiment entry. `complement-c5a-gout.md` also names the RCL assay as a wet-lab gate. This should be registered in `validation-experiments.md` or an explicit LBP-track validation file.
- **Cross-page consistency with comp-043:** comp-043 correctly narrows C1-INH to “disulfide-axis viable” and preserves comp-037’s kinetic caveat. This is a useful later correction and should inform comp-037 wording.

## Load-bearing verification table
| Claim or parameter | Artifact location | Implementation use | Provenance status | Verdict |
|---|---|---|---|---|
| C1-INH sequence length 500 aa | `inputs/P05155.fasta`; `analyze.py` assert | Asserted before analysis | UniProt citation string; FASTA present | Internally verified by artifact, primary-source fetch not independently rechecked |
| Signal peptide aa 1–22; mature aa 23–500 | `analyze.py` constants; provenance | Used for scope partitions | UniProt cited; no flatfile included | Plausible, citation-only |
| Serpin-core boundary aa 123–500 | `analyze.py` `SERPIN_CORE_START`; README | Defines recommended construct and core scopes | Justified by disulfide C123 and pLDDT transition | Load-bearing design choice; defensible but wet-lab unresolved |
| Mucin-like domain aa 23–119 truncation | `analyze.py`; README; summary | Removes major low-pLDDT region | UniProt/AlphaFold cited; pLDDT file present | Plausible; construct-function consequence unresolved |
| RCL aa 452–467, R466–T467 reactive bond | `analyze.py` constants/assert; outputs | Separates by-design RCL risk from body risk | UniProt cited; sequence assertion present | Internally verified against FASTA; primary source not independently rechecked |
| Disulfides C123–C428 and C130–C205 | `analyze.py` constants/assert; outputs | Glyco/folding discussion; construct boundary | UniProt cited; sequence assertion checks Cys residues | Internally checked for residue identity, not disulfide existence |
| N-glycan sites `[25,69,81,238,253,272,352]` | `analyze.py`; provenance; outputs | Glyco verdict narrative | UniProt cited; N272 described as variant/noncanonical | Needs wording correction: N272 is not a canonical sequon in provided sequence |
| O-glycan sites `[47,48,64,71,83,88,92,96]` | `analyze.py`; provenance; outputs | Supports mucin truncation | UniProt cited | Citation-only but internally consistent |
| pLDDT values and mean 79.6 | `inputs/alphafold_P05155_plddt.json`; outputs | Drives all accessibility/risk scoring | AFDB URL cited; JSON present | Reproducible from committed input, but pLDDT is not SASA |
| Accessibility thresholds 80/65 and weights 0.1/0.4/1.0 | `wiki/etc/experiments/lib/protease_stability.py` | Dominant risk-score mechanism | Library convention; not a physical calibration | Load-bearing proxy; requires caveat/rerun for survival claims |
| Protease P1/P1′ specificity panel | `protease_specificities.json`; library scan | Defines recognition sites | MEROPS/literature citations only | Plausible screening panel; extended specificity omitted |
| pH activity factors trypsin/chymo 0.6, elastase 0.5, OmpT 1.0, DegP 0.8 | `protease_specificities.json`; library | Multiplicative risk factor | Citation strings; not derived from pH range in code | Load-bearing estimates, not directly verified |
| NaCl 0.9% physiological | `protease_specificities.json`; outputs | Salt interpolation clamps to no inhibition | Documented in provenance | Correctly no salt inhibition; range fields not used |
| Duration 1–7 days | `protease_specificities.json`; outputs summary | Not used in scoring | Transit/colonization citations only | Stored-but-unused; survival wording must not imply time integration |
| Non-RCL serpin-core worst score 0.1 LOW | `outputs/cleavage_sites.json`; `summary.md` | Headline “strictly-degradative LOW” | Derived from pLDDT proxy | Internally reproducible, physically under-closed |
| RCL DegP 9 exposed, elastase 11 exposed | `outputs/cleavage_sites.json`; `summary.md` | Kinetic-competition gate | Derived from pLDDT proxy and P1 rules | Outputs consistent; README has stale “13” |
| Glyco feasibility GREEN | `analyze.py`; outputs; wiki | Independent verdict axis | Bos/Stavenhagen/Liu citations; primary texts absent | Mechanistically plausible but citation-only; fold/activity needs wet-lab |
| Reproduction command | README | User rerun path | Command path omits `wiki/etc/` | Correction required |

## Affected wiki pages
- `wiki/etc/experiments/comp-037-c1-inh-protease-stability-ecn/README.md` — change required — stale elastase RCL count “13” vs generated “11”; reproduction path omits `wiki/etc/`; should clarify duration/pH/temperature are not used in scoring.
- `wiki/etc/experiments/comp-037-c1-inh-protease-stability-ecn/outputs/summary.md` — change required — generated summary is internally consistent, but physical wording should be softened to pLDDT-proxy language; “conditions modeled” should distinguish reported vs computationally used fields.
- `wiki/c1-inh-protease-stability-ecn-computational.md` — change required — broadly faithful, but overstates “serpin body folds and persists” and “no exposed sites” beyond the pLDDT proxy; should mention the later library caveat and SASA/kinetic follow-up.
- `wiki/computational-experiments.md` — change required — comp-037 entry is mostly consistent, but should mark the LOW 0.1 as pLDDT-proxy/non-SASA and avoid treating Liu 2004 as artifact-verified unless the source packet is added.
- `wiki/validation-experiments.md` — change required — inspected dashboard lacks a C1-INH RCL kinetic-competition assay entry despite comp-037/complement page naming it as the next gate.
- `wiki/complement-c5a-gout.md` — already mostly consistent / minor change required — §9.8 correctly carries MODERATE and wet-lab gate, but should inherit any pLDDT/SASA softening; §9.9 dormant C1-INH + rosmarinic-acid composition remains appropriately dormant.
- `wiki/engineered-lbp-chassis.md` — already consistent — includes C1-INH as MODERATE kinetic-gated and comp-043 scaling caveat.
- `wiki/daf-lactoferrin-ecn-folding-feasibility-computational.md` — already consistent — usefully narrows C1-INH to disulfide-axis viable with comp-037 kinetic caveat.
- `wiki/complestatin-bgc-lbp-feasibility-computational.md` — already consistent historically — correctly says comp-024 only provided GREEN-provisional prior that comp-037 later tested.
- `wiki/hypotheses/H05-daf-scr14-cp0-thesis.md` — change required / extension required — it notes C1-INH as a sister hypothesis if stability passes; comp-037 has now passed only as MODERATE kinetic-gated, so a separate C1-INH hypothesis card or explicit “queued” status should be created rather than leaving it implicit.
- `wiki/chaperone-orthogonal-stacking.md` — already consistent — later comp-043/serpin caveats are appropriately more conservative than comp-037’s original framing.

## New connections or implications
- The later library caveat from comp-034 is directly relevant: comp-037’s non-RCL LOW verdict should be treated as “low low-pLDDT motif risk,” not “low surface protease risk,” until SASA/refined structure scoring is done.
- DegP-vs-C1s “kinetic competition” is not just kinetic; it is also **topology/sequence-of-exposure** dependent. DegP exposure occurs during periplasmic transit or misfolding, while C1s/MASP-2 engagement occurs after secretion. The wet-lab assay should include route-relevant pre-exposure designs, not only simultaneous co-incubation.
- comp-043 provides a needed interpretive correction: C1-INH is plausible on the EcN disulfide axis, but serpin native-fold attainment remains unmodeled. That should be cross-propagated back to comp-037 summaries.
- The comp-037 construct boundary at C123 is functionally attractive for protease/glyco reasons, but it also deletes the native N-terminal domain. The retained inhibitor activity of aa123–500 should be tested directly against C1r/C1s/MASP-2 rather than inferred from deglycosylation literature.

## Required actions
1. Correct `README.md`: replace elastase RCL “13” with the output-supported “11,” unless a rerun changes the outputs.
2. Correct reproduction/path text in README and generated summary references to use the committed repo-relative path `wiki/etc/experiments/comp-037-c1-inh-protease-stability-ecn/` and library path `wiki/etc/experiments/lib/protease_stability.py`.
3. Add a clear “proxy limitation” note to README, `outputs/summary.md`, interpretive page, and computational index: pLDDT is not solvent accessibility; non-RCL LOW is a pLDDT-based screening result, not demonstrated protease survival.
4. Register the C1-INH wet-lab gate in `validation-experiments.md` or an LBP-specific validation page: recombinant aa123–500 construct, target C1r/C1s/MASP-2 inhibition, off-target DegP/elastase pre-exposure and co-incubation, intact/proteolyzed C1-INH readouts, and secretion-route-relevant controls.
5. Add or link primary-source packets for load-bearing glycosylation/function claims, especially deglycosylated C1-INH retaining inhibitory function; otherwise mark them as citation-only.
6. Clarify N272 wording everywhere: it is a variant/noncanonical annotation, not a canonical N-glycan sequon in the provided P05155 sequence.
7. Consider a v2 computational rerun using SASA/structure-aware accessibility and, if possible, simple exposure-time/protease-concentration sensitivity rather than only fixed pH/salt multipliers.
8. Update affected corpus pages after the above, especially `c1-inh-protease-stability-ecn-computational.md`, `computational-experiments.md`, and `complement-c5a-gout.md`.

## Review limits
I did not execute `analyze.py`; reproducibility was assessed by code and committed-output inspection only. Primary sources cited in provenance were not fetched or independently verified; only committed FASTA/pLDDT/protease JSON and wiki text were inspected. Repository fixed-string search failed because the underlying `rg` binary was unavailable, so affected-page discovery relied on explicit bundle pages plus targeted reads of omitted pages. The full `validation-experiments.md` and all omitted corpus surfaces were not exhaustively searched.
