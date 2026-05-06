# comp-014 Phase 5 — Deep-Read Findings + Verdicts (2026-05-06)

Five parallel subagent deep-reads of the top Phase 4 candidates (Model A = Claude). Two-model cross-check completed via DeepSeek-Chat-V3 (Model B) over OpenRouter — same `.env` key the wiki sweep daemon uses. Brian flagged the key was available; Model B cross-check landed substantive findings. See `phase-5-deepseek-cross-check.md` for full Model B output; key disagreement annotations integrated below per CLAUDE.md §Translation protocol.

## Headline: Phase 4 over-claimed; Phase 5 corrected

Phase 5 substantially refined Phase 4. Three of the five top-tier candidates got downgraded after full-text inspection. This is the multi-pass discipline working as designed — the Phase 4 ranked-list claims would have propagated into the canonical wiki and downstream synthesis without Phase 5's verification step. The CLAUDE.md pre-commit grep-verify gate ("every load-bearing quantitative claim must be grep-verified against its primary source") applies here: Phase 5 IS the grep-verify pass for the breadth-pass-derived findings.

## Per-candidate verdicts

### #1 — *Ganoderma applanatum* 2,4-DAE (PMID 35750011) → KEEP, with corrections

| Aspect | Phase 4 claim | Phase 5 finding |
|---|---|---|
| Journal | Fitoterapia 2022 | **Biomed Pharmacother** (correct upstream) |
| Compound | "2,4-DAE" ambiguous | Methyl 2,4-dihydroxybenzoate, single defined small molecule, PubChem 78329, SMILES `COC(=O)c1ccc(O)cc1O` |
| In vivo data | SUA 407→134 µmol/L | **Verified — but at 80 mg/kg top dose only.** Lower doses 195 (20 mg/kg), 145 (40 mg/kg) µmol/L |
| Source attribution | "from G. applanatum" | **Computational only** — paper uses commercial reagent, not isolated from fungus |
| URAT1 effect | Direct chokepoint hit | **Expression-level downregulation, not direct binding** — mechanistically distinct from benzbromarone |
| Over-correction risk | Not flagged | 134 µmol/L is below normal control SUA (~111 µmol/L) — antioxidant-loss liability for human translation |

**Verdict: KEEP as a top candidate**, with the dose-qualification, the source-attribution caveat, and the URAT1-mechanism-clarification recorded. Single defined small molecule is the cleanest Phase 6 carry-forward of the breadth pass.

**Model B cross-check (DeepSeek):** AGREE-WITH-CAVEATS. Adds:
- DAE's *natural abundance* in *G. applanatum* needs confirmation (commercial reagent in paper ≠ proof of meaningful biosynthesis in the fungus)
- Pure-compound vs fungal-extract activity may differ — matrix effects unaddressed
- "降尿酸作用" (hypouricemic effect) translation accurate but duration of effect not specified — TCM context typically prioritizes sustained effects

**Phase 6 prerequisites:** Retrieve full PDF (paywalled, ~$30) to verify XOD IC50, inhibition type, kinetic constants. CNKI dive recommended — Yong/Liang group is Chinese-affiliated, anchored in TCM diuresis literature.

### #2 — *Ganoderma lucidum* GLPP (PMID 36385640) → KEEP, drives ADA chokepoint addition

| Aspect | Phase 4 claim | Phase 5 finding |
|---|---|---|
| 40.6% UA reduction | Claimed | **Verified at abstract level** (PubChem-indexed, RSC paywalled) |
| ADA chokepoint | "New chokepoint candidate" | **ADA causally upstream of XO** — biochemically canonical (adenosine → inosine → hypoxanthine → xanthine → UA) |
| Redox/disulfide mechanism | Implied (proposed chokepoint) | **Not in this paper**, but sister paper (PMC11351902, same Yang group) shows GLPP activates Keap1/Nrf2/HO-1 (disulfide-redox switch via Keap1 cysteines) |

**Verdict: KEEP**. **ADD ADA TO CANONICAL OPEN ENZYME CHOKEPOINT INVENTORY** — biochemically defensible, evidence-supported, complementary to existing XO and uricase chokepoints. **Caveat:** pentostatin-class ADA inhibitors are chemotoxicity-grade — the chokepoint is druggable but the toxicity profile constrains chronic HUA adoption. Fungal natural-product ADA inhibitors with cleaner profiles are an open exploration vector.

**Model B cross-check (DeepSeek):** AGREE-WITH-CAVEATS. Adds:
- "Polysaccharide peptide" terminology ambiguity — could mean glycopeptide OR proteoglycan; distinction is critical for pharmacological characterization and Model A glossed over it
- Model A's "ADA inhibition is the main reason" overstates the case without comparative efficacy data between ADA and transporter (GLUT9/OAT1) effects in the same paper
- ADA's role in T-cell activation / immune function complicates chronic inhibition — adds a different toxicity dimension to the pentostatin caveat
- Polysaccharide nature may limit bioavailability/consistency in clinical settings (real-world consideration Model A under-emphasized)

### #3 — AMC-BFE (PMID 41905012, 2026 Cordyceps × Astragalus SSF) → DOWNGRADE Tier 1 → Tier 2

| Aspect | Phase 4 claim | Phase 5 finding |
|---|---|---|
| 4 chokepoint hits | URAT1 + GLUT9 + ABCG2 + PPARα | **Qualitatively yes, quantitatively unverified (paywalled).** Direction unclear for ABCG2 |
| ABCG2 site | Implied intestinal (Open Enzyme target) | **Hepatic** — bile-route ABCG2, not the canonical intestinal-secretion chokepoint. Mapping to Open Enzyme target is weaker than first read |
| PPARα | "Activation" | **Gene-expression-downstream evidence**, not direct ligand binding |
| Active compound | Implied identified | **Not identified.** Whole-extract evidence; authors explicitly hedge "contribution of individual metabolites requires further investigation" |

**Verdict: DOWNGRADE to Tier 2.** Still platform-relevant (Cordyceps × Astragalus solid-state fermentation maps directly onto engineered-koji-style production) but the multi-chokepoint claim is over-strong without compound identification. **Phase 6 prerequisites:** retrieve full PDF before any number propagates to wiki (per CLAUDE.md pre-commit grep-verify gate). Email corresponding author Ling J at Shandong University (lingjian-ya@sdu.edu.cn).

**Model B cross-check (DeepSeek):** AGREE-WITH-CAVEATS. Adds:
- TCM literature's emphasis on **herb-fungus synergistic effects** missing from Model A's framing — *Astragalus* metabolites likely modulate *Cordyceps* metabolism in this co-fermentation (the SSF chemistry isn't just additive)
- Isoflavone aglycones deglycosylation pharmacological implications (bioavailability, activity) under-qualified — important for TCM pharmacology
- *Cordyceps militaris* strain variability not discussed — known issue in fungal fermentation studies; affects reproducibility

### #4 — Cordyceps sinensis Cochrane (PMID 26457607) → DOWNGRADE Tier 1 → Tier 3

| Aspect | Phase 4 claim | Phase 5 finding |
|---|---|---|
| Indication | "Cordyceps × hyperuricemia, 5 RCTs" | **NOT a CKD/hyperuricemia review** — kidney-transplant-recipient adjuvant immunosuppression review (Hong et al. 2015) |
| SUA evidence | "Clinical-grade, 5 RCTs" | **Reported in ONE RCT only** (Ding 2011, n=109 subset). MD −84.19 µmol/L (95% CI −117.86 to −50.52). No pooling, no I². Confounded by CsA dose-sparing co-intervention |
| Cochrane verdict | Implied positive | **"Limited low quality evidence" per Cochrane's own assessment** |
| Preparation | "Cordyceps" generic | **4 of 5 RCTs = Bailing capsule (*Hirsutella sinensis* CS-4 fermented mycelium).** Not wild *O. sinensis*, not *C. militaris*, not Jinshuibao |
| Hyperuricemia status | Implied primary endpoint | **Secondary endpoint** in CKD-management trials |

**Verdict: DOWNGRADE Tier 1 → Tier 3** for urate-axis purposes. The breadth pass over-read this paper. Phase 6 carry-forward, IF any, is **Bailing-capsule-specific** — not Cordyceps-generic. **Phase 5b CNKI dive on Ding 2011** is the single Phase 5b action that would either upgrade or finally bury this lead.

**Model B cross-check (DeepSeek):** AGREE-WITH-CAVEATS. Adds:
- Q80 strain (the cultivated *C. sinensis* preparation in Yu 1991) lacks pharmacological-profile context — different strain may give different activity
- Chinese-language RCT reporting standards variability not flagged strongly enough — Cochrane's own "unclear risk of bias" notes apply specifically to several included Chinese trials
- Pooling across different Cordyceps preparations (without disaggregating by preparation type) could mask significant differences — methodology concern beyond what Model A surfaced

### #5 — Sanghuangporus davallialactone (PMID 36801789) → DOWNGRADE: not a clean Phase 6 candidate

| Aspect | Phase 4 claim | Phase 5 finding |
|---|---|---|
| XO IC50 90 µM | Mid-tier biochemistry hit | **Verified (90.07 ± 2.12 µM)** |
| Purity 97.7% | Characterized purity claim | **Verified (97.726%)** |
| Selectivity | Implied XO-selective | **Red flag — more potent against aldose reductase (IC50 ~20.5 µM rat, ~35.4 µM human).** Cleaner-framed as aldose reductase inhibitor with SECONDARY XO activity |
| Source organism for engineered chassis | "Korean medicinal mushroom" | ***Sanghuangporus* is a slow-growing wood-decay basidiomycete, not koji-grade.** Heterologous expression of styrylpyrone pathway in *A. oryzae* would itself be a project |
| In vivo evidence | Phase 4 didn't claim | **NONE.** Strictly biochemistry + cell culture |

**Verdict: DROP from urgent Phase 6 list.** Better-framed as aldose reductase / hyperglycemia-adjacent compound class (phelligridimer A from same family has aldose reductase IC50 0.63 µM — stronger class lead). Open Enzyme's gout/urate axis is not the primary leverage for this chemistry. **Author affiliation correction:** all 9 authors at Changchun Normal University (Jilin, China) — Chinese paper, not Korean. The Korean-traditional-medicine framing in my Phase 4 brief was wrong.

**Model B cross-check (DeepSeek) — most divergent of the 5:** AGREE-WITH-CAVEATS but pushes back on Model A's framing:
- **"In TCM pharmacology, multi-target activity is often intentional, not necessarily a 'red flag'"** — Western drug-discovery selectivity discipline (one target, off-target = bad) doesn't map onto TCM evaluation logic. Davallialactone's aldose reductase + XO dual activity may be a design feature in TCM context, not a defect
- 桑黄 (*Sanghuang*) is interchangeable with *P. linteus* and *P. baumii* in TCM literature — source attribution may have ambiguity Model A treated as resolved
- Mycelium-based production is the modern trend in Chinese commercial Sanghuang — not just fruiting-body extraction
- This is the cleanest example of a translation-protocol disagreement worth recording: Western Phase-6 "selectivity red flag" judgment may not survive an East-Asian-pharmacology re-read of the same data. Doesn't change the DROP-from-urgent-list verdict (Sanghuangporus is still a slow-growing wood-decay basidiomycete, not koji-grade), but it widens the framing for any future re-evaluation.

## Phase 5 Verdict on Proposed Redox/Disulfide Chokepoint

Per the three-tier rubric in `chokepoint-targets.json`:

- **ADMIT:** ≥20 fungal compounds across ≥3 mechanistic classes
- **PRELIMINARY:** 10-19 compounds across ≥2 classes
- **REJECT:** <10 compounds OR dominated by one class

**Phase 5 verdict: REJECT.** The breadth pass surfaced essentially zero direct evidence base for a standalone redox/disulfide chokepoint. PubMed Phase 2c had only one entry under `ergothioneine_thioredoxin_TXNIP` and that entry was empty. Phase 5 GLPP deep-read confirmed redox chemistry exists in fungal compounds (Keap1/Nrf2/HO-1 via GLPP) but the redox axis is NOT the load-bearing claim for any HUA outcome — it's a sister-paper finding, decoupled from the urate-axis chokepoints comp-014 is mapping.

**Action:** Fold redox/disulfide-modulating fungal compounds into the existing NLRP3 sub-chokepoint map as a "redox/Keap1-Nrf2 priming axis" rather than elevating to a standalone chokepoint. The TXNIP target stays in the chokepoint-targets.json under the NLRP3 axis, not as a standalone chokepoint.

**Re-evaluation trigger:** if a future comp-NNN extending to marine fungi (per §6.9 limitation) surfaces ETP-class compounds with disulfide-bridge-mediated activity at ≥3 mechanistic classes, re-open the decision. The terrestrial-fungi-only scope of comp-014 is the binding constraint.

## Phase 5 Recommendation: ADD ADA as canonical chokepoint

Adenosine deaminase (ADA, UniProt P00813, gene ADA) is biochemically upstream of xanthine oxidase in purine catabolism. GLPP evidence (40.6% UA reduction in vivo) supports the chokepoint. ADD to:

- `wiki/modality-chokepoint-matrix.md` — new column under the urate-axis grouping
- `wiki/gout-pathophysiology.md` — purine-catabolism upstream layer
- `wiki/abcg2-modulators.md` — adjacent transporter biology page
- `experiments/comp-014/inputs/chokepoint-targets.json` — promote from "implicit downstream of XO" to first-class chokepoint

Caveat to include in the canonical wiki entry: existing ADA inhibitors (pentostatin) are chemotoxicity-grade. ADA chokepoint is druggable but the toxicity profile constrains chronic HUA adoption. Fungal natural-product ADA inhibitors with cleaner profiles are an open exploration vector — and GLPP being a polysaccharide-peptide rather than a nucleoside analog is a structurally distinct class that may avoid the pentostatin-class toxicity.

## Phase 5 Recommendation: ADD PINK1/mitophagy as PRELIMINARY chokepoint

PINK1/mitophagy (PMID 40334761, *Cordyceps cicadae*) is a single-paper finding — not enough evidence for canonical addition, but enough for PRELIMINARY tier with explicit "needs Phase 5b expansion" tag. The mechanism connects to NLRP3 priming via mitochondrial dysfunction-induced ROS, so it folds naturally into the existing NLRP3 sub-chokepoint map.

**Action:** Add as PRELIMINARY entry in `chokepoint-targets.json`, not yet propagated to the canonical wiki. Phase 5b decision: needs ≥3 additional papers from independent groups before promoting to canonical.

## Refined Top Tier (Phase 5-corrected)

| Rank | Compound | Producer | Chokepoints | Evidence | Phase 6 readiness |
|---:|---|---|---|---|---|
| 1 | **Methyl 2,4-dihydroxybenzoate (DAE)** | *Ganoderma applanatum* (chemistry only — commercial reagent in paper) | XO + URAT1 (expression-level for URAT1) | in vivo mouse, 80 mg/kg = SUA 407→134 µmol/L; 40 mg/kg = 145; 20 mg/kg = 195 | Defined small molecule. Cleanest Phase 6 carry-forward. Need full PDF for IC50/kinetics. |
| 2 | **GLPP polysaccharide-peptide** | *Ganoderma lucidum* (mycelium, Juncao source) | ADA + GLUT9 + OAT1 (also Keap1/Nrf2 in sister paper) | in vivo mouse, 40.6% UA reduction at top dose | Polysaccharide-peptide is harder for engineered-koji production than small molecule; characterize the active fraction first. |
| 3 (was 1) | LOVASTATIN | *A. terreus* / *Pleurotus ostreatus* | HDAC6 + PPARγ | in vitro biochem | Already a commercial drug; gout-axis relevance is secondary. |
| 4 (was 4) | AMC-BFE | *Cordyceps militaris* × *Astragalus* SSF | URAT1 + GLUT9 + (hepatic) ABCG2 + PPARα downstream | whole-extract in vivo mouse, paywalled | Need full PDF before propagating numbers. |
| 5 (was 6) | FZ-formula Poria | *Wolfiporia cocos* (in multi-herb formula) | ABCG2/GLUT9/OAT1 + NLRP3/ASC | in vivo, multi-herb confounded | Multi-herb attribution makes single-component verdict impossible. |
| — (was 3) | Cordyceps sinensis Cochrane | downgrade Tier 1 → Tier 3 | urate axis general | 1 underlying RCT, low quality, transplant-confounded | Bailing-capsule-specific; need Ding 2011 CNKI dive |
| — (was 7) | Sanghuangporus davallialactone | downgrade — not Phase 6 candidate | XO secondary (aldose reductase primary) | in vitro only | Better as aldose reductase lead, not gout-axis |

## Phase 5b Recommendations (deferred follow-up turns)

1. ~~**Provision OpenRouter API key**~~ **DONE** — Brian flagged the key is in `.env` (same one the wiki sweep daemon uses). Model B cross-check ran in this turn; full output at `phase-5-deepseek-cross-check.md`. Pattern reusable for future comp-NNN multilingual passes.
2. **CNKI dive on Ding 2011** (the single SUA-reporting RCT in the Cochrane review). Decides whether Cordyceps Bailing capsule retains any urate-axis lead.
3. **Full PDF retrieval** for PMID 35750011 (DAE, ~$30) and PMID 41905012 (AMC-BFE, ~$30). $60 total — negligible vs. Phase 6 wet-lab cost.
4. **Sister-paper read** for GLPP Keap1/Nrf2 evidence (PMC11351902) to determine if there's any *direct* urate-axis × redox coupling, or if redox is genuinely orthogonal.
5. **Run KNApSAcK + NPASS + TCMSP pulls** when Asian-DB scraping infrastructure is set up. The breadth pass is incomplete on the East-Asian-curated side.
6. **Consider comp-NNN extension to marine fungi** for ETP-class compounds (gliotoxin, sirodesmin, chetomin family) that would expand the redox/disulfide chokepoint surface. The current REJECT verdict is binding only on terrestrial-fungi-only scope.

## Methodology lesson

Phase 5 is the grep-verify gate for breadth-pass findings. Three of the five top Phase 4 hits got downgraded on full-text inspection. This is the multi-pass discipline working — the alternative would be propagating Phase 4's over-claims into canonical wiki entries. The CLAUDE.md pre-commit grep-verify gate ("every load-bearing quantitative claim must be grep-verified against its primary source") is exactly what Phase 5 implements for comp-014's outputs. Future comp-NNN breadth experiments should bake this Phase 5 verification step into the methodology, not treat it as an optional follow-up.
