# comp-015: T-axis Adjuvant Urate-Target Mapping — Summary (v2)

**Version:** v2 (XO added as 5th target)
**Date:** 2026-05-07
**Framework:** comp-013 (compound × chokepoint mapping with verdict tagging) + comp-007 achievable/IC50 thresholds + comp-004 gut-conc model. Evaluates H-AN-02 (cordycepin as uniquely gout-favorable T-axis adjuvant). v2 adds XO as 5th target with mechanism-orthogonal verdict logic.
**Compounds × targets evaluated:** 4 × 5 = 20 pairs
**Interpretive wiki page:** [`wiki/t-axis-adjuvant-urate-mapping-computational.md`](../../wiki/t-axis-adjuvant-urate-mapping-computational.md)

## v1 → v2 change

Added xanthine oxidase (XO, CHEMBL1929) as 5th target. v1 4-target panel was systematically incomplete because XO was excluded. v2 adds: (a) cordycepin × XO IC50 = 55.7 µM in vitro (PMID 38141695) — direction-aligned but ratio ~0.001 at supplement Cmax (BELOW THRESHOLD for systemic activity); (b) eurycomanone × XO NO-DATA but verification of trigger papers (PMID 31920654, 34785103) shows mechanism is multi-target transporter modulation + purine-synthesis suppression — substantively REVERSING v1's GOUT-UNFAVORABLE eurycomanone verdict; (c) icariin × XO negative-screen (Mo 2007 PMID 17666819, icariin tested but not in significant-XO-inhibitor flavonoid group); (d) echinacoside × XO no-data.

## Hypothesis under test

> H-AN-02 (androgen-natural-modulation.md §10): Cordyceps cordycepin elevates T modestly + modulates URAT1 in animal models; predicted net UA effect favorable or neutral despite T elevation.

### Status: **PARTIALLY FALSIFIED — cordycepin still favorable but NOT UNIQUELY SO; Eurycomanone also gout-favorable via different mechanism. The 'uniquely positioned' framing of H-AN-02 v1 does not survive v2 evidence ingestion.**

## Verdict matrix (per-compound × target, v2 with XO column)

| Compound | URAT1 | ABCG2 | OAT1 | SHBG | XO | Per-compound verdict |
|---|---|---|---|---|---|---|
| Cordycepin | ✓ Anim (PMID 29422889) | no-data | no-data | no-data | ✓ InVit (PMID 38141695) | **GOUT-FAVORABLE** |
| Eurycomanone | ✓ InVit (PMID 31920654) | ✓ Anim (PMID 31920654) | ✓ Mech (PMID 34785103) | ✓ Clin (PMID 36013514) | no-data | **GOUT-FAVORABLE** |
| Icariin | no-data | no-data | no-data | no-data | ? ? (PMID 17666819) | **MECHANISM-UNCLEAR** |
| Echinacoside | no-data | no-data | no-data | no-data | no-data | **MECHANISM-UNCLEAR** |

## Coverage statistics

- ChEMBL/published bioactivity records with IC50: **1 of 20** (5%) — *ChEMBL API was BLOCKED in this run; v2 manually surfaced 1 published primary-literature IC50 (cordycepin × XO PMID 38141695, not yet ChEMBL-curated). The fundamental sparsity pattern (5/9 in comp-013) holds.*
- Pairs with primary-literature evidence: **7 of 20** (35%)
- Pairs with NO data at all: **13 of 20**

## Per-compound rationale

### Cordycepin → **GOUT-FAVORABLE**

- Favorable transporter hits: 1
- Unfavorable transporter hits: 0
- Indirect/extrapolated hits: 0
- No-data pairs: 2
- T-axis SHBG mechanism strength: absent-or-not-mechanism
- XO arm classification: **xo-favorable-in-vitro**
- XO arm rationale: XO INHIBITOR direction (PMID 38141695, In Vitro); achievable/IC50 ratio = 0.001 (below 10× systemic-activity threshold OR direct-comparison absent). In vitro positive but not meaningfully active at systemic concentrations.

**Driving mechanism(s):**
- URAT1 INHIBITOR (DOWNREGULATES URAT1 PROTEIN/MRNA EXPRESSION) (tier 3, PMID 29422889)
- XO INHIBITOR (in vitro only, ratio below 10× threshold) — XO INHIBITOR direction (PMID 38141695, In Vitro); achievable/IC50 ratio = 0.001 (below 10× systemic-activity threshold OR direct-comparison absent). In vitro positive but not meaningfully active at systemic concentrations.

**Rationale:**
  - URAT1 FAVORABLE direction (INHIBITOR (DOWNREGULATES URAT1 PROTEIN/MRNA EXPRESSION)) backed by Animal Model (PMID 29422889) — magnitude: Dose-response: 15/30/60 mg/kg PO daily → SUA 216/210/203 µmol/L vs hyperuricemic-control 337 µmol/L (normal-control 202 µmol/L) — Kunming mice, potassium-oxonate (100 mg/kg IP) + hypoxanthine (600 mg/kg PO) co-induced HUA model
  - XO supplementary in vitro positive — XO INHIBITOR direction (PMID 38141695, In Vitro); achievable/IC50 ratio = 0.001 (below 10× systemic-activity threshold OR direct-comparison absent). In vitro positive but not meaningfully active at systemic concentrations.

**Per-target detail:**

| Target | Site | IC50 (nM) | Achievable conc (µM) | Ratio | Class | Direction | Evidence level | PMID |
|---|---|---|---|---|---|---|---|---|
| URAT1 | plasma | — | 0.0570 | — | lit-evidence-only-no-IC50 | INHIBITOR (DOWNREGULATES URAT1 PROTEIN/MRNA EXPRESSION) | Animal Model | 29422889 |
| ABCG2 | gut_lumen+plasma | — | 780.0000 | — | no-data | UNKNOWN | No-Data | — |
| OAT1 | plasma | — | 0.0570 | — | no-data | UNKNOWN | No-Data | — |
| SHBG | plasma | — | 0.0570 | — | no-data | N/A | No-Data | — |
| Xanthine Oxidase | plasma | 55700 | 0.0570 | 0.001 | below-threshold | INHIBITOR | In Vitro | 38141695 |

### Eurycomanone → **GOUT-FAVORABLE**

- Favorable transporter hits: 2
- Unfavorable transporter hits: 0
- Indirect/extrapolated hits: 0
- No-data pairs: 0
- T-axis SHBG mechanism strength: robust-clinical
- XO arm classification: **xo-no-data**
- XO arm rationale: No published direct XO evidence; mechanism not established.

**Driving mechanism(s):**
- URAT1 INHIBITOR (URATE-UPTAKE INHIBITION IN HURAT1-EXPRESSING CELLS; IN VIVO URAT1 PROTEIN DOWNREGULATION) (tier 2, PMID 31920654)
- ABCG2 INDUCER (ABCG2 PROTEIN UPREGULATION IN KIDNEY → ENHANCES URATE SECRETION → FAVORABLE) (tier 3, PMID 31920654)

**Rationale:**
  - URAT1 FAVORABLE direction (INHIBITOR (URATE-UPTAKE INHIBITION IN HURAT1-EXPRESSING CELLS; IN VIVO URAT1 PROTEIN DOWNREGULATION)) backed by In Vitro (PMID 31920654) — magnitude: PMID 31920654 (Front Pharmacol 2019): *Eurycoma longifolia* stem extract (EL) at 100/200/400 mg/kg PO significantly reduced serum/plasma uric acid in PO-rat and adenine-PO-mouse hyperuricemia models; mechanism includes URAT1 + GLUT9 protein downregulation in kidney; quassinoids isolated from EL (eurycomanone, eurycomanol, eurycomalactone) showed inhibitory effects on urate uptake in hURAT1-expressing cells in vitro (specific IC50 numbers behind paywall but DIRECTION is INHIBITOR). Eurycomanol confirmed in vivo at 5-20 mg/kg PO (PMID 34785103, J Ethnopharmacol 2022) — same direction.
  - ABCG2 FAVORABLE direction (INDUCER (ABCG2 PROTEIN UPREGULATION IN KIDNEY → ENHANCES URATE SECRETION → FAVORABLE)) backed by Animal Model (PMID 31920654) — magnitude: PMID 31920654: ABCG2 protein expression was UPREGULATED in kidney of EL-treated hyperuricemia rats/mice (Western blot evidence, dose-dependent at 100/200/400 mg/kg PO EL). Confirmed in PMID 34785103 for purified eurycomanol. Specific fold-change numbers behind paywall.

**Per-target detail:**

| Target | Site | IC50 (nM) | Achievable conc (µM) | Ratio | Class | Direction | Evidence level | PMID |
|---|---|---|---|---|---|---|---|---|
| URAT1 | plasma | — | 0.0073 | — | lit-evidence-only-no-IC50 | INHIBITOR (URATE-UPTAKE INHIBITION IN HURAT1-EXPRESSING CELLS; IN VIVO URAT1 PROTEIN DOWNREGULATION) | In Vitro | 31920654 |
| ABCG2 | gut_lumen+plasma | — | 17.5000 | — | lit-evidence-only-no-IC50 | INDUCER (ABCG2 PROTEIN UPREGULATION IN KIDNEY → ENHANCES URATE SECRETION → FAVORABLE) | Animal Model | 31920654 |
| OAT1 | plasma | — | 0.0073 | — | lit-evidence-only-no-IC50 | UNKNOWN — POSSIBLY INDUCER PER MULTI-TRANSPORTER PATTERN | Mechanistic Extrapolation | 34785103 |
| SHBG | plasma | — | 0.0073 | — | lit-evidence-only-no-IC50 | DISPLACER (CLAIMED) | Clinical Trial | 36013514 |
| Xanthine Oxidase | plasma | — | 0.0073 | — | no-data | UNKNOWN / NOT-XO | No-Data | — |

### Icariin → **MECHANISM-UNCLEAR**

- Favorable transporter hits: 0
- Unfavorable transporter hits: 0
- Indirect/extrapolated hits: 0
- No-data pairs: 3
- T-axis SHBG mechanism strength: absent-or-not-mechanism
- XO arm classification: **xo-negative-screen**
- XO arm rationale: Negative-screen evidence (PMID 17666819): No-Data. Direction: WEAK / NON-SIGNIFICANT. Magnitude: PMID 17666819 (Mo 2007 Biol Pharm Bull — *Hypouricemic action of selected flavonoids in mice*): 15 flavonoids screened in PO-induced hyperuricemia mice at 50 + 100 mg/kg PO; **icariin was tested but did NOT make the significant-XO-inhibition group**. The five flavonoids that DID show significant hypouricemic XO inhibition were quercetin, morin, myricetin, kaempferol, puerarin. Structure-activity rule: planar flavones/flavonols with 7-OH (chrysin, luteolin, kaempferol, quercetin, myricetin, isorhamnetin) inhibit XO at 0.4-5 µM IC50. **Icariin is a flavonol-glycoside (rhamnose-glucose disaccharide on C-7 OH + prenyl group), structurally NON-COMPATIBLE with the strong-XO-inhibitor planar-flavonoid class — glycosylation dramatically reduces XO activity (PMC11312107 review).** Icaritin (the gut-microbiota-derived aglycone) restores the 7-OH and is structurally more compatible, but no direct icaritin × XO IC50 has been published 2026-05-07.

**Driving mechanism(s):**
- (no favorable mechanism identified)

**Rationale:**
  - No urate-axis evidence (transporter no-data + XO no-data or negative-screen). T-axis effect modest or unconfirmed. Insufficient evidence to triage as favorable, unfavorable, or neutral.
  - XO arm: negative-screen finding — Negative-screen evidence (PMID 17666819): No-Data. Direction: WEAK / NON-SIGNIFICANT. Magnitude: PMID 17666819 (Mo 2007 Biol Pharm Bull — *Hypouricemic action of selected flavonoids in mice*): 15 flavonoids screened in PO-induced hyperuricemia mice at 50 + 100 mg/kg PO; **icariin was tested but did NOT make the significant-XO-inhibition group**. The five flavonoids that DID show significant hypouricemic XO inhibition were quercetin, morin, myricetin, kaempferol, puerarin. Structure-activity rule: planar flavones/flavonols with 7-OH (chrysin, luteolin, kaempferol, quercetin, myricetin, isorhamnetin) inhibit XO at 0.4-5 µM IC50. **Icariin is a flavonol-glycoside (rhamnose-glucose disaccharide on C-7 OH + prenyl group), structurally NON-COMPATIBLE with the strong-XO-inhibitor planar-flavonoid class — glycosylation dramatically reduces XO activity (PMC11312107 review).** Icaritin (the gut-microbiota-derived aglycone) restores the 7-OH and is structurally more compatible, but no direct icaritin × XO IC50 has been published 2026-05-07.

**Per-target detail:**

| Target | Site | IC50 (nM) | Achievable conc (µM) | Ratio | Class | Direction | Evidence level | PMID |
|---|---|---|---|---|---|---|---|---|
| URAT1 | plasma | — | 0.0076 | — | no-data | UNKNOWN | No-Data | — |
| ABCG2 | gut_lumen+plasma | — | 175.3000 | — | no-data | UNKNOWN | No-Data | — |
| OAT1 | plasma | — | 0.0076 | — | no-data | UNKNOWN | No-Data | — |
| SHBG | plasma | — | 0.0076 | — | no-data | N/A | No-Data | — |
| Xanthine Oxidase | plasma | — | 0.0076 | — | lit-evidence-only-no-IC50 | WEAK / NON-SIGNIFICANT | No-Data | 17666819 |

### Echinacoside → **MECHANISM-UNCLEAR**

- Favorable transporter hits: 0
- Unfavorable transporter hits: 0
- Indirect/extrapolated hits: 0
- No-data pairs: 3
- T-axis SHBG mechanism strength: absent-or-not-mechanism
- XO arm classification: **xo-no-data**
- XO arm rationale: No published direct XO evidence; mechanism not established.

**Driving mechanism(s):**
- (no favorable mechanism identified)

**Rationale:**
  - No urate-axis evidence (transporter no-data + XO no-data or negative-screen). T-axis effect modest or unconfirmed. Insufficient evidence to triage as favorable, unfavorable, or neutral.

**Per-target detail:**

| Target | Site | IC50 (nM) | Achievable conc (µM) | Ratio | Class | Direction | Evidence level | PMID |
|---|---|---|---|---|---|---|---|---|
| URAT1 | plasma | — | 0.0113 | — | no-data | UNKNOWN | No-Data | — |
| ABCG2 | gut_lumen+plasma | — | 378.1000 | — | no-data | UNKNOWN | No-Data | — |
| OAT1 | plasma | — | 0.0113 | — | no-data | UNKNOWN | No-Data | — |
| SHBG | plasma | — | 0.0113 | — | no-data | N/A | No-Data | — |
| Xanthine Oxidase | plasma | — | 0.0113 | — | no-data | UNKNOWN | No-Data | — |

## H-AN-02 evaluation (v2)

**Hypothesis:** H-AN-02 (androgen-natural-modulation.md §10): Cordyceps cordycepin elevates T modestly + modulates URAT1 in animal models; predicted net UA effect favorable or neutral despite T elevation.

**Status: PARTIALLY FALSIFIED — cordycepin still favorable but NOT UNIQUELY SO; Eurycomanone also gout-favorable via different mechanism. The 'uniquely positioned' framing of H-AN-02 v1 does not survive v2 evidence ingestion.**

**Reasoning (v2):**

- **Cordycepin** has TWO direct mechanisms now: (a) URAT1 protein/mRNA downregulation (PMID 29422889, Animal Model, dose-response in PO-induced HUA mice) — load-bearing for v1 verdict; (b) direct in vitro XO IC50 = 55.7 µM (PMID 38141695, with allopurinol comparator IC50 8.94 µM in same assay) — NEW in v2. **However, the cordycepin systemic Cmax (~0.057 µM) is ~1000× below the XO IC50, so the systemic-XO arm is BELOW THRESHOLD.** Cordycepin's gout-favorable verdict is dominated by URAT1, with XO as supplementary in vitro evidence not meaningfully active at supplement doses.
- **Eurycomanone — MAJOR v2 REVERSAL.** v1 marked eurycomanone GOUT-UNFAVORABLE (mechanistic extrapolation). v2 verification of trigger-source primary literature (PMID 31920654 Front Pharmacol 2019, PMID 34785103 J Ethnopharmacol 2022) shows: (a) URAT1 + GLUT9 protein DOWNREGULATION in kidney (favorable), (b) ABCG2 + NPT1 protein UPREGULATION (favorable), (c) direct urate-uptake inhibition in hURAT1-expressing cells in vitro (favorable), (d) purine SYNTHESIS suppression via decreased PRPS expression (favorable, off-panel). Combined with the 2021 placebo-controlled human RCT (n=105, Physta 100/200 mg/d × 12 wk → SUA ↓7-11%) cited in `androgen-natural-modulation.md`, eurycomanone joins cordycepin in the GOUT-FAVORABLE category. **The XO trigger that motivated v2 was itself a citation-laundering artifact** — eurycomanone is NOT a direct XO inhibitor; primary sources document multi-target transporter modulation + purine-synthesis suppression. But adding XO to the panel was still correct (the v1 panel was systematically incomplete).
- **Icariin** has a NEGATIVE-SCREEN result on XO (PMID 17666819 Mo 2007: icariin tested in 15-flavonoid hypouricemia screen, NOT in significant-XO-inhibitor group — quercetin/morin/myricetin/kaempferol/puerarin were). Icariin is structurally NOT in the planar-7-OH-flavone XO-inhibitor class (icariin is a flavonol-glycoside; glycosylation reduces XO activity). Icariin's gout-context evidence (PMID 33135192) remains ANTI-INFLAMMATORY (NLRP3 axis), NOT urate-lowering. Verdict: MECHANISM-UNCLEAR at urate axis (XO ruled out; transporter axis no-data). NLRP3 axis remains a possibly favorable but separate-chokepoint role.
- **Echinacoside** has no direct evidence at any of URAT1/ABCG2/OAT1 transporters AND no XO evidence. Compound class (large polar phenylethanoid glycoside, MW 786.73) is structurally distinct from any known small-molecule urate-axis modulator. Verdict: MECHANISM-UNCLEAR.
- **The H-AN-02 framing 'cordycepin uniquely positioned' is PARTIALLY FALSIFIED in v2.** Cordycepin and eurycomanone are BOTH gout-favorable (different mechanisms — cordycepin = URAT1-dominant + weak in vitro XO; eurycomanone = multi-target transporter + purine-synthesis). The 'uniquely positioned' wording does not survive v2. Brian's wet-lab gate (cordyceps vs tongkat ali, UA primary endpoint) becomes a HEAD-TO-HEAD between two gout-favorable mechanisms rather than a feasibility-vs-confirmation contrast.

## v1 → v2 methodology adaptation note

v1 4-target panel (URAT1/ABCG2/OAT1/SHBG) was systematically incomplete because XO was excluded. The v1 eurycomanone GOUT-UNFAVORABLE verdict relied on absent direct evidence — a parallel Sci-Hub-second-pass verification subagent on `wiki/androgen-natural-modulation.md` then surfaced (a) the XO claims that motivated v2 panel-expansion AND (b) the previously-missed PMID 31920654 + 34785103 transporter+purine-synthesis primary literature. v2's primary contribution is therefore TWO-FOLD: panel completeness (XO column added) + previously-missed eurycomanone evidence integrated. The XO addition is the version label, but the larger substantive change is the eurycomanone verdict reversal.

## Caveats and limitations

1. **ChEMBL REST API was blocked in this analysis run.** Most bioactivity records routed through `[API-BLOCKED]` annotations. Cordycepin × XO IC50 (55.7 µM, PMID 38141695) is the only pair with a direct numerical IC50; the rest rely on direction-of-effect tagging from primary literature.
2. **Cordycepin × URAT1 evidence is expression-level, not direct binding.** PMID 29422889 measured URAT1 protein/mRNA downregulation; no direct in vitro URAT1 IC50 was reported. The mechanism may be transcriptional or post-translational, not orthosteric.
3. **Cordycepin oral PK is poor for purified compound** (PMC6823370). The Cmax estimate (0.057 µM) is order-of-magnitude bound; whole-fermentate Cordyceps with native pentostatin co-delivery may raise BA 5-10× — still well below the XO IC50 of 55.7 µM, so the systemic-XO arm remains below threshold even with the optimistic BA correction.
4. **Eurycomanone evidence: in vitro hURAT1 IC50 numbers behind paywall.** PMID 31920654 abstract reports DIRECTION (inhibitor) for individual quassinoids in hURAT1-expressing cells but specific IC50 values are not in the abstract. Magnitude-confident verdict requires Sci-Hub-level access or institutional subscription.
5. **The eurycomanone × XO 'NO-DATA' verdict surfaces a CITATION LAUNDERING PATTERN.** The v2 trigger claim (eurycomanone as XO inhibitor, attributed to PMID 31920654 / 34785103) does NOT survive primary-source verification — those papers establish transporter+purine-synthesis modulation, not XO. This is itself a v2 finding worth surfacing to `wiki/androgen-natural-modulation.md` for citation-laundering audit.
6. **The 5-target panel is still narrow.** PDE5 (icariin), CYP17/StAR (steroidogenic mechanism for cordycepin/icariin), NLRP3 (icariin's anti-flare effect), and PRPS (purine synthesis enzyme — eurycomanol mechanism) are NOT in this panel. PRPS specifically is a v2-surfaced new-target candidate worth proposing for any future panel expansion.
7. **No Chinese-language primary literature accessed in this run.** CLAUDE.md global-multilingual discipline applies; CNKI / WanFang access not available. Likely-existing Chinese-language papers on echinacoside × urate, icariin × XO, or eurycomanone × additional mechanisms not surfaced.
8. **Per-compound BA values are rat-derived.** Allometric scaling to human is approximate. For cordycepin × XO specifically, the achievable/IC50 ratio is so far below threshold (0.001) that even 10× BA scaling does not change the verdict.
9. **The 'MECHANISM-UNCLEAR' verdict for icariin and echinacoside is the H-discipline-aware verdict.** It is NOT 'no effect.' Icariin's NLRP3-axis activity is real but off-panel; echinacoside's *Cistanche* TCM-context use suggests possible CNKI-only evidence not surfaced here.
10. **The v2 methodology adaptation is documented in the interpretive wiki page** (`wiki/t-axis-adjuvant-urate-mapping-computational.md` §'Methodology adaptation — v1 → v2: adding XO as 5th target') alongside this summary.