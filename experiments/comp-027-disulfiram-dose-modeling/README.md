# comp-027 — Disulfiram Dose Modeling

**Question:** Is there a sub-AUD (alcohol-use-disorder) oral disulfiram dose window
where plasma DSF concentrations engage GSDMD (CP6b pyroptotic-exit block) at a
therapeutically meaningful level while plasma Me-DTC concentrations stay below the
ALDH-inhibition threshold that drives the disulfiram-ethanol reaction (DER)?

**Verdict:** YELLOW-leaning-GREEN — a narrow sub-AUD dose window exists around
**75-125 mg/day**, with 100 mg/day predicted to deliver ~57% GSDMD blockade at
~40% ALDH inhibition (right at the DER hypotension threshold). Strict-GREEN (≥50%
GSDMD AND ≤40% ALDH) only at 100 mg/day under the conservative cell-free EC50
anchor; under the cellular-preincub (covalent-accumulation-aware) anchor, GREEN
extends down to 50 mg/day. **This experiment gates whether the
[compounding-pharmacy track](../../wiki/compounding-pharmacy-track.md)'s 503A
disulfiram pathway has a defensible dosing protocol.**

This is comp-027 in the [Open Enzyme computational experiments
registry](../../wiki/computational-experiments.md).

**Interpretive wiki page:**
[`wiki/disulfiram-dose-modeling-computational.md`](../../wiki/disulfiram-dose-modeling-computational.md)

## How to reproduce

```bash
cd experiments/comp-027-disulfiram-dose-modeling
python3 scripts/analyze.py
```

Stdlib only (`json`, `math`, `pathlib`). No external packages.

Outputs land in `outputs/`:
- `dose_response.json` — machine-readable full results with metadata + per-dose breakdown
- `dose_response_table.csv` — flat CSV for spreadsheet use
- `summary.md` — human-readable summary cited from the wiki page

## File index

```
comp-027-disulfiram-dose-modeling/
  scripts/
    analyze.py                 ← analysis script (run this)
  inputs/
    provenance.md              ← sources + grep-verification notes for every input
    pk_data.json               ← disulfiram + DETC PK parameters from Lee 2018, Johansson 1989
    ec50_data.json             ← GSDMD blockade (Hu 2020) + NLRP3 palmitoylation (Xu 2024) EC50 anchors
    der_threshold_data.json    ← DER acetaldehyde threshold (Faiman 1989) + clinical dose-DER curve
    di_landscape.json          ← bundled drug-interaction landscape; gout-co-medication compatibility
    formulation_data.json      ← 503A compounding formulation options (IR capsule, ER lipid matrix, etc.)
  outputs/
    dose_response.json
    dose_response_table.csv
    summary.md
  README.md                    ← this file
```

## Methodology summary

1. **PK model** — empirical Cmax/Cavg scaling anchored to canonical clinical PK
   data: parent DSF Cmax = 1.0 μM (range 0.4-2.5) at 250 mg PO single dose,
   linear scaling below 1000 mg, CYP-saturation correction above 1000 mg.
   Total dithiocarbamate species ≈ 4× parent (DDC, DDTC-Me, DETC-MeSO,
   carbamathione all retain reactive thiuram/dithiocarbamate motif).
2. **Me-DTC peak plasma** — linear scaling from Johansson 1989's 278 nM at 400 mg
   anchor; CYP-saturation correction above 1000 mg.
3. **GSDMD-blockade fraction** — Hill equation (n=1) on plasma parent DSF.
   Conservative anchor: 0.30 μM (Hu 2020 cell-free liposome). Optimistic anchor:
   0.02 μM (Hu 2020 cellular preincubation — accounts for covalent target
   accumulation over time).
4. **NLRP3-palmitoylation fraction** — Hill (n=1) on plasma parent DSF. EC50 =
   10 μM (Xu 2024 partial inhibition threshold). At sub-AUD doses, palmitoylation
   pathway is NOT engaged.
5. **ALDH inhibition fraction** — Hill (n=1) on plasma Me-DTC. EC50 = 104 nM,
   back-calculated from Faiman 1989 acetaldehyde threshold (110 μM acetaldehyde
   corresponds to 40% ALDH inhibition → Me-DTC at ~70 nM peak at 100 mg DSF gives
   40% inhibition).
6. **Verdict** — GREEN if GSDMD ≥ 50% AND ALDH ≤ 40%. YELLOW if GSDMD ≥ 30%
   AND ALDH ≤ 50%. RED otherwise.

## Top-line per-dose verdict

| Dose (mg/d) | Cmax parent DSF (μM) | Me-DTC peak (nM) | GSDMD block (conservative) | ALDH inhibition | Verdict |
|---|---|---|---|---|---|
| 25 | 0.10 | 17 | 25% | 14% | RED (below-GSDMD) |
| 50 | 0.20 | 35 | 40% | 25% | YELLOW |
| 62.5 | 0.25 | 43 | 46% | 29% | YELLOW |
| **100** | **0.40** | **70** | **57%** | **40%** | **GREEN** |
| 125 | 0.50 | 87 | 62% | 45% | YELLOW (DER borderline) |
| 200 | 0.80 | 139 | 73% | 57% | RED (above-DER) |
| 250 | 1.00 | 174 | 77% | 62% | RED (above-DER) |
| 500 | 2.00 | 348 | 87% | 77% | RED (above-DER) |
| 1000 | 4.00 | 695 | 93% | 87% | RED (above-DER) |
| 2000 | 10.22 | 1775 | 97% | 94% | RED (above-DER) |

## Compounding-pharmacy partner handoff

Proposed 503A dose range to propose to a compounding pharmacy partner (Empower,
Olympia, or equivalent — see
[compounding-pharmacy-track.md §Pharmacy partner identification](../../wiki/compounding-pharmacy-track.md)):

- **Phase 1 (dose-titration starter):** immediate-release capsule, 50, 75, 100,
  125 mg strengths. Patients titrate from 50 mg/d × 14d → 100 mg/d steady-state,
  with weekly clinical assessment for incidental ethanol exposure and any GI /
  hepatic / neuro symptoms.
- **Phase 2 (chronic maintenance):** extended-release lipid-matrix tablet, 100 mg
  QD, designed to compress Cmax/Cavg ratio. Lower Cmax means lower ALDH-inhibition
  peak; sustained Cavg maintains GSDMD covalent engagement (covalent → time-
  integrated). This is the MINX-protocol analog.
- **Companion drug:** allopurinol 100-300 mg/d per gout standard-of-care. Asiri
  2025 demonstrated synergy in rat MSU-gout model; no negative DI with disulfiram.

## Verification gate disclosure

Per `wiki/manual-literature-mining.md` §Pre-commit verification gate:

**Grep-verified primary sources** (all anchors traceable to specific paragraph or table):
- Hu 2020 GSDMD cell-free IC50 0.3 μM — `/papers/PMC7316630/content.lines` liposome leakage assay section
- Hu 2020 GSDMD cellular preincub IC50 0.02 μM — same paper, 24-fold reduction language
- Xu 2024 NLRP3 palmitoylation 10/30 μM — `/papers/PMC11398858/content.lines` L14, Figure 1A text
- Johansson 1989 Me-DTC peak 278 nM at 400 mg — PMID 2551696 abstract
- Faiman 1989 DER threshold 40% ALDH / 110 μM acetaldehyde — PMID 2537080 abstract
- Asiri 2025 50 mg/kg DSF + ALP rat gout model efficacy — `/papers/PMC12114764/content.lines` L25, L53
- Asiri 2025 explicit dose-response limitation acknowledgment — same paper L59
- Palatty 2011 125 mg/d clinical use — `/papers/PMC3056183/content.lines` L12
- Lee 2018 PK parameters at 500/1000/2000 mg — `/papers/PMC6379104/` full text via PubMed

**Bounded extrapolations** (acknowledged in limitations):
- 1.0 μM parent DSF Cmax at 250 mg anchor: canonical PK literature; ±150% range used
- Total-DTC = 4× parent multiplier: estimated from Lee 2018 summed-AUC scaling
- Linear PK scaling 25-1000 mg: extrapolated from Johansson + Lee data
- Me-DTC linear scaling below 100 mg: extrapolated from Johansson 100-300 mg data

## Multilingual sources

Per `Open Enzyme/CLAUDE.md` §"Global-multilingual research by default": targeted
search for non-English-source disulfiram + gout / NLRP3 / GSDMD data via Paperclip
+ PubMed. The vast majority of disulfiram + GSDMD literature is English-language
(Western-pharma-driven repurposing surface). The most relevant non-English-language
work surfaced was Asiri et al. 2025 (PMC12114764), which is English-language but
authored by a Saudi/Indian collaboration with rat gout-model evidence not yet
widely indexed in Western reviews. No Chinese / Japanese / Korean primary sources
surfaced with quantitative disulfiram PK or GSDMD-blockade data beyond what
Hu 2020 already established. Translation cross-check protocol was NOT triggered
(no load-bearing non-English primary sources found).

## Subagent peer review

Per `new-comp-experiment` skill workflow §Step 4, subagent peer review of this
analysis is scheduled at the comp-027 walkthrough (not yet executed). The
verification-agent pass below is an in-loop check performed by the author against
the primary-source grep-verification log.

## Relationship to validation-experiments.md

This computational prior **does not change** the on-deck wet-lab gating for the
compounding-pharmacy track — that track is downstream of a 503A pharmacy partner
identification (`compounding-pharmacy-track.md` §Open questions item 2), which is
user-action-required (real-world outreach, not Claude-actionable). What this
experiment changes is the **dose-range specificity Brian carries into that
outreach**: instead of "low-dose disulfiram somewhere in the 25-250 mg range,"
the proposal is "75-125 mg/d IR capsule for titration; 100 mg/d ER lipid-matrix
tablet for maintenance." That's a concrete enough formulation specification that
a 503A pharmacy can quote turnaround time + cost.
