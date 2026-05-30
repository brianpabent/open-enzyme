---
title: Validation Experiments — Archive
date: 2026-05-29
tags: [experiments, validation, archive, corpus-excluded, self-experiments, closed-experiments]
related: [validation-experiments]
sources: [validation-experiments.md]
---

# Validation Experiments — Archive

> **Corpus-excluded archive.** This page was split out of [`validation-experiments.md`](../validation-experiments.md) on 2026-05-29 to remove closed / deprioritized / designed-but-not-active experiment blocks from the wiki-sweep synthesis corpus (the synthesis glob covers `wiki/*.md` + `wiki/hypotheses/*.md` but **excludes** `wiki/etc/**`). Content here is preserved **verbatim** — evidence tags, numbering, provenance, and cross-references are unchanged from the pre-split main page. Active / in-flight experiments remain on the main [`validation-experiments.md`](../validation-experiments.md).
>
> **What lives here:**
> - **§2.7** — Koji × *Cordyceps* co-formulation ADA-challenge stability test. **Deprioritized 2026-05-16** ("do not execute"); retained for traceability.
> - **§3.1, §3.2, §3.4–§3.11** — Phase 3 human self-experiment / biomarker protocols that are **Proposed (designed but not started)**. The one active Phase 3 experiment — **§3.3 (Lynn: wild-type koji digestive enzyme supplementation, In Progress)** — stays on the main page.
>
> Re-promote any block back to the main page if its status changes from designed/deprioritized to active.

---

## Phase 2 (archived) — Deprioritized

### 2.7 Koji × *Cordyceps* Co-Formulation Stability Test — ADA-Challenge Assay (added 2026-05-15; **Deprioritized 2026-05-16**)

> **Deprioritized 2026-05-16 — koji-cordycepin engineering removed from active cassette stack.** Walkthrough Item 7 strategic call. This experiment was a gate for the engineered-koji cordycepin route + cross-chassis pentostatin protection; with the koji-cordycepin engineering effort deprioritized (full reasoning at [`koji-endgame-strain.md` §3.5](../koji-endgame-strain.md)), the experiment is moot — the cultivation route already delivers cordycepin + pentostatin together at the natural co-evolved ratio, and no engineered-koji cordycepin product is being developed for the gate to evaluate. Section retained for traceability; **do not execute.** Re-open only if the koji-cordycepin engineering thesis is re-prioritized (new evidence on therapeutic-dose achievability or a chokepoint that koji-engineered cordycepin uniquely addresses).

**Status**: ~~Proposed~~ **Deprioritized** | **Cost**: $1,500–3,000 | **Weeks**: 3–4 | **Phase**: 2 (low-cost, low-friction)

**Affected wiki**: [medicinal-mushroom-complement-track](../medicinal-mushroom-complement-track.md) §"Combined / synergy candidates"; [cordycepin-cassette-burden-computational.md](../cordycepin-cassette-burden-computational.md) §"Impact on experimental priorities"; [computational-experiments.md](../computational-experiments.md) comp-025 (ADA × cns1 kinetic modeling); [koji-endgame-strain.md](../koji-endgame-strain.md) cordycepin arm.

**What it tests:** Does whole-fermentate *C. militaris* extract (providing native pentostatin) protect engineered-koji-produced cordycepin from ADA-mediated deamination when the two are co-formulated? If yes, the cross-chassis pairing (engineered koji handles bulk cordycepin production at scale; cultivated *C. militaris* extract provides ADA-protecting pentostatin from native co-evolved chemistry) becomes a minimal-complexity delivery strategy that avoids the additional cassette OR ADA-knockout work that comp-024 / comp-025 would otherwise gate. If no, the co-formulation strategy fails and the platform routes through full-BGC engineering OR ADA knockout OR purified pentostatin co-supplementation.

**Proposed in:** 2026-05-14 sweep Connection 4 (synthesis/done/2026-05-14-connection-4-cordycepins-ada-vulnerability-creates-a-two-organism.md).

**Background on the gap:** comp-023 confirmed engineered cns1+cns2 cordycepin production in koji is metabolically feasible (GREEN at Jeennor 2023 564 mg/L/d). But cordycepin is rapidly deaminated by adenosine deaminase (ADA) to its inactive 3'-deoxyinosine form. Native *C. militaris* solves this by co-producing pentostatin (a clinical-grade ADA inhibitor) from the same BGC as cordycepin (Xia 2017, PMID 29056419). The minimal-complexity workaround for engineered koji: don't engineer pentostatin; pair the koji fermentate with a small co-formulated dose of cultivated *C. militaris* extract. This experiment tests whether the pairing actually delivers ADA protection or whether the formulation context (mixing solid-state koji + dried *Cordyceps* extract) compromises pentostatin's activity.

**Protocol:**

- **Test article preparation:**
  - Arm A (negative control): engineered-koji cordycepin fermentate alone, no ADA inhibitor
  - Arm B (positive control — native): whole-fermentate *C. militaris* alone (intrinsic cordycepin + pentostatin from native BGC)
  - Arm C (cross-chassis pairing — the test): engineered-koji cordycepin fermentate + dried *C. militaris* extract at pentostatin dose calibrated to match Arm B's pentostatin content
  - Arm D (purified-pentostatin reference): engineered-koji cordycepin fermentate + commercial pentostatin (Nipent or research-grade)
- **ADA challenge assay:**
  - Spike each arm with bovine intestinal ADA (or human recombinant ADA) at a defined enzyme concentration
  - Sample at t = 0, 15 min, 30 min, 60 min, 120 min, 240 min
  - Quantify cordycepin vs. 3'-deoxyinosine (the ADA product) by LC-MS at each timepoint
- **Readout:** cordycepin half-life under ADA challenge for each arm; comparison vs. Arm A baseline (no ADA inhibition)
- **Stability check:** Arm C cordycepin + pentostatin content at 0, 7, 14 days post-co-formulation (room temperature + 4°C storage) to verify the co-formulation doesn't degrade pentostatin
- **Success criterion (test → next phase):** Arm C cordycepin half-life ≥ 50% of Arm B's half-life. (Arm B is the native co-evolved benchmark; co-formulation reaching half of native protection is meaningful evidence the strategy works.)

**Estimated cost:** $1,500–3,000
- *C. militaris* cultivation (~2 weeks home or community-biolab) + dried extract preparation: ~$200–400
- Engineered-koji cordycepin fermentate (or comp-023-feasibility-proxy via Jeennor 2023 reference batch): ~$500 if outsourced; gated on engineered-koji-cordycepin strain availability
- LC-MS quantification ($25–50/sample × 4 arms × 6 timepoints × 3 replicates = 72 samples × $35 ≈ $2,500)
- Bovine ADA reagent: ~$100

**Estimated timeline:** 3–4 weeks (2 weeks *Cordyceps* cultivation + 1 week assay run + 1 week LC-MS turnaround)

**Success criteria (overall):**
- **Arm C cordycepin half-life ≥ 50% of Arm B (native co-evolved):** the cross-chassis pairing works as a minimal-complexity ADA-protection route. Update [`medicinal-mushroom-complement-track.md`](../medicinal-mushroom-complement-track.md) to promote the pairing from "synergy candidate" to "validated route"; update [`koji-endgame-strain.md`](../koji-endgame-strain.md) cordycepin-arm framing to note this avoids pentostatin co-engineering complexity.
- **Arm C half-life < 50% of Arm B:** the co-formulation strategy fails. Route through pentostatin co-engineering (additional cassette in koji) OR ADA knockout (host engineering) OR purified pentostatin co-supplementation. Comp-024 / comp-025 outcomes determine which.

**Limitations:**

1. In vitro ADA challenge does not capture gut-lumen-realistic conditions (mixed flora, gut-wall ADA distribution, pH variation). Use the in vitro result as a go/no-go for whether the cross-chassis pairing is mechanistically possible, not as a guarantee of in vivo performance.
2. Pentostatin dose-matching across Arm B (native) and Arm C (co-formulated) requires accurate quantification of pentostatin in the dried *C. militaris* extract. Use an HPLC-UV anchor measurement per [`medicinal-mushroom-extract-sops.md`](../medicinal-mushroom-extract-sops.md) or send to a Tier 3 vendor for absolute quantification before the assay.
3. Engineered-koji cordycepin fermentate availability is gated on the cns1+cns2 cassette being expressed in koji. Until that happens, this experiment uses Jeennor 2023's *C. militaris* fermentate as a stand-in cordycepin source (with the native pentostatin removed via chromatographic purification before re-spiking).

**Cross-references:** [`medicinal-mushroom-complement-track.md`](../medicinal-mushroom-complement-track.md) §"Combined / synergy candidates" (originating section); [`cordycepin-cassette-burden-computational.md`](../cordycepin-cassette-burden-computational.md) §"Impact on experimental priorities" (cordycepin engineering-feasibility prior); [comp-025 ADA × cns1 substrate competition](../computational-experiments.md) (computational gate that informs whether this experiment is needed); §2.6 (4-arm whole-fermentate vs. purified comparison — sister experiment); [Xia 2017 PMID 29056419](https://pubmed.ncbi.nlm.nih.gov/29056419/) (native pentostatin co-production primary source).

---

## Phase 3 (archived) — Human Self-Experimentation and Biomarker Tracking (Proposed / not-yet-active)

> Note: **§3.3 (Lynn: wild-type koji, In Progress)** is intentionally NOT here — it remains on the main [`validation-experiments.md`](../validation-experiments.md) as an active experiment.

### 3.1 Brian: Engineered Yeast Uricase — Serum Uric Acid & Flare Tracking

**Status**: Proposed | **Cost**: $200–400 | **Weeks**: 20 | **Phase**: 3

**Affected wiki**: [engineered-yeast-uricase-proposal](../engineered-yeast-uricase-proposal.md), [self-experiment-protocol](../self-experiment-protocol.md), [open-enzyme-vision](./open-enzyme-vision.md)

**What it tests:** Does daily oral engineered yeast reduce serum uric acid and gout flare frequency in the primary user?

**Proposed in:** engineered-yeast-uricase-proposal.md (§5), etc/open-enzyme-vision.md (§8)

**Protocol:**
- Brian (primary user with gout) takes engineered yeast supplement daily
- Baseline: 4 weeks pre-intervention (establish flare frequency, serum urate baseline)
- Intervention: 12 weeks daily supplementation with engineered yeast (dose TBD from animal studies)
- Biomarkers measured weekly:
  - Serum uric acid (HPLC or uricase-catalase assay)
  - Inflammatory markers (CRP, IL-6 if available)
  - Gout flare frequency and severity (patient-reported, validated scale)
  - Tissue urate (tophi size if present, via ultrasound)
- Control: 4-week washout period after intervention

**Estimated cost:** $200–400 (blood assays, home kit supplies)

**Estimated timeline:** 20 weeks (4 baseline + 12 intervention + 4 washout)

**Dependencies:** 
- Requires Phase 1 & 2 validation
- Requires medical oversight (likely rheumatologist or primary care)

**Success criteria:**
- Reduce serum uric acid by ≥15% vs. baseline
- Reduce flare frequency by ≥50% vs. baseline period
- No adverse events

---
### 3.2 Brian: NLRP3 Inflammasome Suppression Stack — Biomarker Panel

**Status**: Proposed | **Cost**: $700–1,400 | **Weeks**: 20 | **Phase**: 3

**Affected wiki**: [nlrp3-exploit-map](../nlrp3-exploit-map.md), [supplements-stack](../supplements-stack.md), [self-experiment-protocol](../self-experiment-protocol.md), [open-enzyme-vision](./open-enzyme-vision.md)

**What it tests:** Does the multi-compound NLRP3 stack reduce inflammatory markers and flare severity?

**Proposed in:** nlrp3-exploit-map.md, etc/open-enzyme-vision.md (§9)

**Protocol:**
- Brian takes NLRP3 suppression stack (BHB/exogenous ketones + KPV nasal spray + BPC-157 nasal spray + sulforaphane + oridonin + omega-3 + NAC, dosed per [[supplements-stack]])
- Baseline: 4 weeks pre-intervention
- Intervention: 12 weeks daily stack
- Biomarkers measured weekly:
  - Serum IL-1β (high-sensitivity ELISA)
  - Serum CRP, calprotectin, and fibrinogen
  - Blood ketone bodies (BHB) if using exogenous ketones
  - Joint pain (VAS scale, validated)
  - Gout flare frequency
- Control: 4-week washout post-intervention

**Estimated cost:** $300–600 (supplement costs) + $400–800 (blood assays)

**Estimated timeline:** 20 weeks

**Dependencies:**
- Requires Phase 1 NLRP3 pathway validation
- Can run in parallel with 3.1 (same subject, complementary endpoints)
- Requires medical oversight

**Success criteria:**
- Reduce IL-1β by ≥30% vs. baseline
- Reduce CRP by ≥25% vs. baseline
- Reduce flare frequency by ≥40% vs. baseline

---
### 3.4 Joint Trial: Engineered Koji (Both Users)

**Status**: Proposed | **Cost**: $300–500 | **Weeks**: 14 | **Phase**: 3

**Affected wiki**: [engineered-koji-protocol](../engineered-koji-protocol.md), [open-enzyme-vision](./open-enzyme-vision.md), [self-experiment-protocol](../self-experiment-protocol.md)

**What it tests:** Does engineered koji providing both digestive enzymes and uricase work as a dual-purpose therapeutic food?

**Proposed in:** engineered-koji-protocol.md, etc/open-enzyme-vision.md (§4, dual-enzyme vision)

**Protocol:**
- Both Brian and Lynn take engineered koji daily for 12 weeks
- Brian measures:
  - Serum uric acid, gout flare frequency (as in 3.1)
  - GI tolerance (stool frequency, abdominal symptoms)
- Lynn measures:
  - GI symptom score, stool characteristics (as in 3.3)
  - Serum uric acid (as secondary endpoint; she may have mild hyperuricemia)
  - Inflammatory markers
- Both:
  - Palatability/adherence assessment
  - Adverse event monitoring
  - Serum inflammatory panel (CRP, IL-6)

**Estimated cost:** $300–500 (koji production, bioassays)

**Estimated timeline:** 14 weeks (2 week prep + 12 week trial)

**Dependencies:** 
- Requires Phase 1 completion of engineered koji with both enzyme activities validated
- Requires both 3.1 and 3.3 baseline data for comparison

**Success criteria:**
- Brian: ≥15% reduction serum uric acid, ≥50% reduction flare frequency
- Lynn: ≥50% improvement GI symptoms, normalized stool, ≥30% reduction fecal calprotectin
- Both: tolerate koji at therapeutic doses with >80% adherence
- No safety signals in 12-week course

---

### 3.5 Biomarker Tracking: Long-term Flare Prevention (Brian, 6-month extension)

**Status**: Proposed | **Cost**: $400–600 | **Weeks**: 26 | **Phase**: 3

**Affected wiki**: [open-enzyme-vision](./open-enzyme-vision.md), [self-experiment-protocol](../self-experiment-protocol.md), [gout-deep-dive](../gout-deep-dive.md)

**What it tests:** Does uricase supplementation provide sustained reduction in gout flares?

**Proposed in:** etc/open-enzyme-vision.md (§8)

**Protocol:**
- After Phase 3.1 completes successfully, continue engineered yeast supplementation for additional 6 months
- Measure monthly:
  - Serum uric acid
  - Gout flare frequency and severity
  - Tophi size (if present, ultrasound at months 1, 3, 6)
  - Joint function/mobility scores
  - Adherence and side effect monitoring

**Estimated cost:** $400–600 (monthly blood assays, ultrasound imaging)

**Estimated timeline:** 6 months

**Dependencies:** Requires successful completion and validation of Phase 3.1

**Success criteria:**
- Sustain serum uric acid reduction over 6-month period
- Maintain ≥40% reduction in flare frequency from baseline
- No tophi growth; ideally small reduction in tophi size
- Continued >80% adherence

---

### 3.6 Brian: Urinary LTB4 Assay — Validating Quercetin's 5-LOX (CP6a) Mechanism In Vivo

**Status**: Proposed | **Cost**: $150–300 | **Weeks**: 12 | **Phase**: 3

**Affected wiki**: [self-experiment-protocol](../self-experiment-protocol.md), [nlrp3-exploit-map](../nlrp3-exploit-map.md), [nlrp3-inhibitor-screen](../nlrp3-inhibitor-screen.md), [synthesis/](../../synthesis/README.md)

**What it tests:** Does the current supplement stack suppress 5-LOX/LTB4 activity in vivo in Brian specifically? This directly validates quercetin's CP6a mechanism (5-LOX IC50 = 300 nM from ChEMBL, now the stack's most potent curated 5-LOX activity) as the operative mechanism — rather than its weaker NF-κB/NLRP3 effects that currently dominate the stack rationale.

**Proposed in:** `synthesis/` (architecture: synthesis/README.md) 2026-04-24 Pass 2 Proposed Experiment #1 and New Connection #3. Brian's 2026-04-24 annotation: "do it. also, i have recent extensive labs that i can add to the project."

**Protocol:**
- Add urinary LTB4 assay to existing self-experiment timepoints in [self-experiment-protocol.md](../self-experiment-protocol.md): **baseline, week 4, week 12** (three measurements total).
- Collect first-morning urine (~20 mL), freeze at -80°C until shipment (standard for eicosanoid stability).
- Ship to a commercial lab offering LTB4 ELISA or LC-MS/MS (e.g., Cayman Chemical assay kit format via CLIA lab, or direct Mayo Clinic / ARUP specialty testing).
- No additional study visit required — piggybacks on the existing self-experiment draw schedule.
- Compare with hs-CRP and urate trajectories at the same timepoints to separate "stack is working" (hs-CRP drop) from "stack is working via CP6a" (urinary LTB4 drop).

**Estimated cost:** $50-100 per assay × 3 timepoints = **$150-300 total**

**Estimated timeline:** No additional study time — piggybacks on the existing 12-week self-experiment. Results available ~2 weeks after each draw.

**Dependencies:** Existing self-experiment infrastructure (`wiki/self-experiment-protocol.md`). No new study visits or logistics beyond adding a urine collection to existing draws.

**Success criteria:**
- Measurable baseline urinary LTB4 (confirms the assay is sensitive at Brian's baseline state)
- ≥30% reduction at week 4 or week 12 relative to baseline → suggests CP6a engagement in vivo
- No change in LTB4 despite hs-CRP improvement → suggests stack effect is via other chokepoints (NF-κB, NLRP3 assembly), not 5-LOX

**Cross-references:** `wiki/self-experiment-protocol.md` (baseline/week 4/week 12 timepoints), `wiki/nlrp3-exploit-map.md` (CP6a), `wiki/nlrp3-inhibitor-screen.md` (quercetin 5-LOX IC50 = 300 nM)

---

### 3.7 Brian: Serum C5a Baseline + Week 12 — Validating CP0 Complement Priming Status

**Status**: Proposed | **Cost**: $300–400 | **Weeks**: 12 | **Phase**: 3

**Affected wiki**: [complement-c5a-gout](../complement-c5a-gout.md), [nlrp3-exploit-map](../nlrp3-exploit-map.md), [self-experiment-protocol](../self-experiment-protocol.md)

**What it tests:** Documents complement priming status (C5a, the dominant NLRP3 priming signal per Cumpelik 2016 PMID 26245757 + Khameneh 2017 PMID 28167912) before and after the 12-week supplement stack. The stack currently covers CP1-CP5a but not CP0 — this experiment tests whether it modulates complement at all, and establishes a baseline for future CP0-targeted interventions (e.g., avacopan, flavonoid C5aR1 antagonists per `wiki/complement-c5a-gout.md`).

**Proposed in:** `synthesis/` (architecture: synthesis/README.md) 2026-04-24 Pass 2 Proposed Experiment #2 and New Connection #3.

**Protocol:**
- Add serum C5a to the baseline and week 12 blood panels in `wiki/self-experiment-protocol.md`.
- Alternative marker: **sC5b-9** (soluble terminal complement complex) — often more stable in serum than free C5a and available on standard commercial panels.
- LabCorp (Complement C5a by enzyme immunoassay, test code 142046) or Quest (sC5b-9 panel) both offer this as a routine specialty test with physician order.
- No new study visit — piggybacks on the already-planned week 0 and week 12 draws.
- Cross-reference with CBC, urate, hs-CRP at the same timepoints.

**Estimated cost:** $150-200 per C5a or sC5b-9 test × 2 timepoints = **$300-400 total**

**Estimated timeline:** No additional study time. Results available ~1 week after draw.

**Dependencies:** Existing self-experiment infrastructure; rheumatologist or primary-care order for the specialty test.

**Success criteria:**
- Measurable baseline C5a (confirms assay sensitivity; establishes whether Brian is a "high-complement-priming" or "low-complement-priming" gout patient — relevant for stack design)
- **Predicted: minimal change at week 12**, since the stack doesn't cover CP0. This is a negative-control-type experiment: if C5a drops significantly, that tells us something unexpected is happening and CP0 is engaged. If C5a doesn't change, that validates the wiki's claim that CP0 is an uncovered chokepoint needing dedicated interventions.
- Either result informs next-phase stack design.

**Cross-references:** `wiki/self-experiment-protocol.md` (week 0 and week 12 panels), `wiki/complement-c5a-gout.md` (CP0 chokepoint), `wiki/nlrp3-exploit-map.md` (CP0 entry)

---

### 3.8 Brian: DHA vs. EPA Split Omega-3 Crossover — Resolving the Gout-Specific SPM Precursor Question

**Status**: Proposed | **Cost**: $550–700 | **Weeks**: 9 | **Phase**: 3

**Affected wiki**: [spm-resolution-pathway](../spm-resolution-pathway.md), [supplements-stack](../supplements-stack.md), [tnfsf14-gout-target](../tnfsf14-gout-target.md), [self-experiment-protocol](../self-experiment-protocol.md)

**What it tests:** Is DHA or EPA the optimal omega-3 precursor for gout flare prevention in Brian's specific case? The 2026-04-24 synthesis pass identified a contradiction between the cardiovascular literature (EPA-dominant) and the gout-specific SPM evidence (DHA-derived RvD1 and MaR1 both show direct MSU animal-model efficacy; DHA also inversely associates with circulating TNFSF14/LIGHT per Mendelian randomization). The `supplements-stack.md` currently recommends 2:1 or 3:1 EPA:DHA for gout, which may be a cardiovascular-biased extrapolation.

**Proposed in:** `synthesis/` (architecture: synthesis/README.md) 2026-04-24 Pass 2 Proposed Experiment #4 and New Connection #2 ("DHA should be preferentially dosed over EPA for gout").

**Protocol:**
- **Phase A (4 weeks): High-EPA protocol.** 3 g EPA + 0.5 g DHA daily (≈6:1 ratio — commercial high-EPA omega-3 formulations like Nordic Naturals ProEPA or Minami Platinum-Plus EPA).
- **Washout (1 week):** No omega-3 supplementation. Continue rest of base stack.
- **Phase B (4 weeks): High-DHA protocol.** 3 g DHA + 0.5 g EPA daily (≈6:1 ratio DHA-dominant — e.g., Nordic Naturals ProDHA or Life Extension Mega EPA/DHA adjusted by dropping EPA capsules).
- Biomarkers measured at baseline, end of Phase A, end of washout, end of Phase B:
  - **Urinary LTB4** (from 3.6 above; tests whether DHA or EPA better suppresses 5-LOX/LTB4 output)
  - **hs-CRP** (generic inflammation marker)
  - **Serum SPM panel (RvD1, RvE1, MaR1 metabolites if a CLIA lab offers this — otherwise spot-measure via Cayman Chemical research kit through a lab contact)**
  - **Gout flare count and severity (daily log)**
- Washout rationale: 7-day omega-3 washout is short relative to RBC phospholipid half-life (~8 weeks) but sufficient to allow downstream SPM levels to decay. Accept the limitation — n=1 study, not a clinical trial.

**Estimated cost:** $200 (supplement differentials across 9 weeks) + $300 (SPM panel) + $50-100 × 2-3 additional LTB4 assays = **$550-700 total** on top of 3.6

**Estimated timeline:** 9 weeks (4 + 1 + 4), concurrent with the existing self-experiment or as a post-experiment extension.

**Dependencies:**
- Experiment 3.6 (urinary LTB4 assay infrastructure)
- Availability of a lab offering SPM metabolite measurement (Mayo Clinic has an eicosanoid panel; research-grade SPM kits from Cayman require a CLIA lab partnership)
- Brian's flare calendar (existing self-tracking)

**Success criteria:**
- **Clear directional effect:** one phase (either EPA or DHA) produces lower urinary LTB4, higher serum RvD1 or RvE1, and fewer flares than the other.
- **Ambiguous result** (both phases similar): the ratio doesn't matter clinically for Brian; revert to a balanced 1:1 or the cheaper formulation.
- **Directional toward DHA:** revises `supplements-stack.md` and confirms the 2026-04-24 synthesis recommendation.
- **Directional toward EPA:** the current stack recommendation was right; synthesis flagged a literature signal that doesn't translate for Brian.

**Cross-references:** `wiki/spm-resolution-pathway.md` (RvD1/MaR1 DHA-derived), `wiki/supplements-stack.md` (omega-3 entry, currently EPA-leaning), `wiki/self-experiment-protocol.md` (integration with the existing protocol), `wiki/tnfsf14-gout-target.md` (DHA-TNFSF14 Mendelian randomization link), `wiki/nlrp3-exploit-map.md` (CP5b SPM entry)

---

### 3.9 Brian: Zileuton Off-Label Trial — Pharma-Grade CP6a Inhibition in Flare-Prevention Protocol

**Status**: Proposed | **Cost**: ~$500 | **Weeks**: 16 | **Phase**: 3

**Affected wiki**: [zileuton](../zileuton.md), [gout-clinical-pipeline](../gout-clinical-pipeline.md), [nlrp3-exploit-map](../nlrp3-exploit-map.md), [self-experiment-protocol](../self-experiment-protocol.md)

**What it tests:** Does the FDA-approved 5-LOX inhibitor **zileuton** (Zyflo / Zyflo CR, asthma indication) abort or prevent gout flares in Brian's specific case? This is the pharma-grade equivalent of quercetin's CP6a mechanism — cleaner readout, stronger effect size expected. Cross-references the `wiki/zileuton.md` dossier (in progress per synthesis queue).

**Proposed in:** `synthesis/` (architecture: synthesis/README.md) 2026-04-24 Pass 2 Proposed Experiment #5 and New Connection #5 ("Zileuton is the closest pharma-grade CP6a analog to quercetin, and has never been tested in gout"). Brian's 2026-04-24 annotation: "yes add it to the clinical pipeline and also let's do a wiki page about it."

**Protocol:**
- **Phase 1: Physician conversation.** Request off-label prescription from rheumatologist or primary-care physician with the CP6a mechanistic rationale. Key talking points:
  - Zileuton (Zyflo CR) is FDA-approved for asthma, dosed 1200 mg BID, generic available, ~$50/month.
  - 5-LOX is mechanistically upstream of neutrophil chemotaxis in gout (LTB4 is a potent neutrophil chemoattractant; colchicine blocks microtubule-dependent chemotaxis downstream).
  - No published gout efficacy trials; this is a genuine off-label novelty.
  - Safety profile: liver enzyme elevation is the primary monitoring concern (~2% patients); monthly LFTs for the first 3 months standard.
  - Duration: 12 weeks, consistent with the existing self-experiment window.
- **Phase 2: Baseline documentation.** Pre-zileuton flare frequency from Brian's self-experiment-protocol flare log; 4-week pre-zileuton observation window if feasible.
- **Phase 3: Zileuton 1200 mg BID × 12 weeks.** Continue base supplement stack (including quercetin — zileuton does not contraindicate quercetin and any additive effect is informative).
- Biomarkers:
  - **Urinary LTB4** at baseline and week 12 (from 3.6 — direct pharmacodynamic confirmation)
  - **Gout flare count and severity** (primary endpoint; daily log)
  - **LFTs** (AST, ALT) at baseline, week 2, week 4, week 8, week 12 (safety)
  - **hs-CRP** at baseline and week 12

**Estimated cost:** $150-200/month × 3 months = **$450-600** (prescription) + existing LFT coverage via insurance + $0 additional lab cost (piggybacks on 3.6 and insurance-covered LFTs). **Net additional: ~$500.**

**Estimated timeline:** 12 weeks active treatment + 4-week follow-up for post-treatment flare rate. Single additional physician conversation to set up.

**Dependencies:**
- Rheumatologist or primary-care physician willing to prescribe off-label. The mechanistic rationale + clean safety profile + low cost should clear this bar.
- Completion of `wiki/zileuton.md` dossier (in progress; synthesis queue item) for Brian to share with the prescribing physician.
- Experiment 3.6 (urinary LTB4 as pharmacodynamic confirmation)

**Success criteria:**
- **Urinary LTB4 ≥50% reduction at week 12** (confirms pharmacodynamic engagement — zileuton's on-target effect)
- **Flare frequency reduced ≥50% vs. pre-zileuton observation baseline** (clinical efficacy signal)
- **LFTs remain within normal range throughout** (safety)
- **Negative result (no flare reduction despite LTB4 drop)** is also informative: suggests LTB4/neutrophil-chemotaxis is not rate-limiting for Brian's flare biology, and colchicine's mechanism (microtubule → chemotaxis) is doing more work than expected.

**Cross-references:** `wiki/zileuton.md` (to be created), `wiki/gout-clinical-pipeline.md` (mechanistic gap entry), `wiki/nlrp3-exploit-map.md` (CP6a), `wiki/self-experiment-protocol.md` (integration with existing protocol)

---

### 3.10 Brian: Fructose Challenge Test as Acute n=1 Uricase Efficacy Readout

**Status**: Proposed | **Cost**: ~$50 | **Weeks**: 0.1 per run (single 2-hour session); ~4 wk gap between baseline and post-intervention | **Phase**: 3

**Affected wiki**: [fructose-connection](../fructose-connection.md), [self-experiment-protocol](../self-experiment-protocol.md), [synthesis/](../../synthesis/README.md), [open-enzyme-vision](./open-enzyme-vision.md)

**What it tests:** Whether engineered uricase is active in the gut in real-time, using a fructose bolus as a predictable acute UA challenge. Per [fructose-connection.md](../fructose-connection.md), oral fructose loads generate a serum UA spike within 60–120 min via the unregulated KHK pathway. A blunted post-fructose UA spike after starting koji therapy directly validates uricase action in the gut — without waiting weeks for baseline UA to drift on chronic monitoring.

**Proposed in:** `synthesis/` (architecture: synthesis/README.md) 2026-04-27 Proposed Experiment #1 (sweep on commit `b7df491`). Pass 3 review: highest insight-per-dollar experiment in the queue, elevated to Priority Action status. Within-subject before/after design controls for most confounders (genetics, kidney function, baseline diet) — the only systematic variable changing between runs is the koji intervention.

**Protocol:**
- **Subject:** Brian (n=1).
- **Pre-load conditions:** 8-hour fasted; baseline UA established (UASure home meter or equivalent, **duplicate readings at each timepoint** per Pass 3 review to manage UASure CV ~10–15%).
- **Challenge:** 50 g fructose load (oral) — standardized matrix (water-dissolved); record exact dose and dissolution medium.
- **Sampling:** Fingerstick UA at t = 0, 30, 60, 90, 120 minutes. Duplicate at each timepoint. Record peak UA delta from baseline.
- **Run #1 (baseline):** Before any engineered-koji intervention. Establishes Brian's individual fructose-induced UA spike profile under current stack.
- **Run #2 (post-intervention):** After ≥4 weeks of stable koji therapy (engineered when available; wild-type baseline as interim per the multi-vendor metabolite campaign). Same protocol exactly.
- **Optional Run #3 (washout):** Off-koji washout after the post-intervention run to confirm reversibility (rules out baseline drift or concurrent variable shifts).

**Estimated cost:** ~$50 — UASure meter ~$25, strips ~$15 for the panel (10 readings × 2 runs = 20 strips minimum), fructose ~$5, miscellaneous.

**Estimated timeline:** 2 hours per session; ~4 weeks elapsed between baseline and post-intervention runs (matches stable plateau on a new koji regimen).

**Dependencies:** No specialized lab access. Self-administered. Slots cleanly into the operational backlog tracked separately on the personal-health side.

**Success criteria:**
- **Validates engineered uricase activity:** post-intervention UA spike at t = 60–90 min is ≥30% reduced vs. baseline run, with the koji intervention as the only changed variable. Effect size scales with how much of the fructose-derived urate is degraded by gut-lumen uricase before systemic absorption.
- **Null result:** spike unchanged. Possible interpretations: insufficient uricase expression / activity, fructose absorbs faster than uricase can degrade the resulting urate, or the koji format isn't delivering active enzyme to the lumen. Triages next experimental questions (e.g., §1.10 stability, §1.6 enzyme survival).
- **Adverse:** spike worsens — suggests run-to-run variance dominated by other factors. Add additional baseline runs to characterize variance before re-interpreting.

**Caveats and confounds:**
- UASure CV ~10–15% — duplicate readings + ≥30% effect-size threshold helps separate signal from noise.
- Brian's clomid taper is in flight (UA mobilization risk during T transition). Schedule the runs to either bracket or sit firmly inside one phase of that taper to avoid confounding.
- Hydration status confounds UA: standardize water intake (e.g., 500 mL on waking, no other fluids during the 2-hour window).
- Recent flares within 4 weeks change baseline UA dynamics — defer until 4+ weeks post-flare.

**Cross-references:** [synthesis/](../../synthesis/README.md) 2026-04-27 Proposed Experiment #1; [fructose-connection.md](../fructose-connection.md); [self-experiment-protocol.md](../self-experiment-protocol.md).

---

### 3.11 Brian: Exertion Challenge Test (Mechanical vs. Metabolic Trigger Discrimination, n=1)

**Status**: Proposed | **Cost**: ~$50–80 per run (UASure strips + urinary urate/Cr) | **Weeks**: 0.25 per run (~6h observation + 72h flare-log); n=several runs over months | **Phase**: 3

**Affected wiki**: [mechanical-flare-triggers](../mechanical-flare-triggers.md), [self-experiment-protocol](../self-experiment-protocol.md), [fructose-connection](../fructose-connection.md), [synthesis/](../../synthesis/README.md)

**What it tests:** Whether exertion/fatigue triggers Brian's flares via **metabolic-overload** (mechanism #5 in [`mechanical-flare-triggers.md`](../mechanical-flare-triggers.md) — sustained exertion → impaired urate clearance → transient supersaturation) or via the **mechanical mechanisms** (#1–4: shedding / mechanotransduction / DAMP / effusion). This is the cheapest n=1 protocol that empirically discriminates between the two classes of explanation for the single most common non-dietary flare trigger in the Li XD 2012 Qingdao n=1,713 cohort (劳累 / fatigue-overwork at **19.3%** of self-reported flare triggers — #3 after high-purine diet and alcohol, and more common than cold + emotion + trauma combined).

**Distinct from §3.10 (NOT a replacement):** §3.10 fructose challenge tests acute uricase efficacy via the PRPS / XO → urate pathway (sugar bolus → UA spike → does the spike blunt after koji therapy starts). §3.11 exertion challenge tests whether physical exertion triggers flares via the metabolic-overload or mechanical route. Different questions; complementary; run both. Pass 2 originally proposed replacing §3.10 with §3.11 based on a hallucinated premise (assumed Brian was on allopurinol — he isn't); both probes test independent mechanisms and have independent value.

**Proposed in:** [`synthesis/`](../../synthesis/README.md) 2026-05-20 Connection 1 + Experiment 1 + Open Question 2 + Priority Action 2 (sweep on commit `6437cb4`). Walkthrough 2026-05-21 narrowed Pass 2's two-phase ± colchicine-cover design to single-phase based on Brian's medication access (Brian has never been on colchicine — Pass 2 hallucinated this premise from `validation-experiments.md` §3.7's incorrect "colchicine-era baseline" language, since corrected). Colchicine cover deferred as future variant (see "Deferred extensions" below).

**Protocol — single-phase mechanism discrimination:**

- **Subject:** Brian (n=1).
- **Pre-exertion conditions:** 2-hour rested baseline. **Hydration standardized** (500 mL water on waking, no other fluids during the 6-hour observation window — matches §3.10 discipline; Pass 3 augment notes hydration confounds both serum UA AND urinary urate/Cr, so standardization is load-bearing).
- **Exertion bout:** **30 minutes weighted walking** (default — low equipment overhead, replicable, joint-loading without high cardio confound). Default load: 20–25 lb in a backpack; steady moderate pace; same route across runs. Alternative bouts (stationary cycling at defined wattage; structured joint-loading protocol) acceptable but the SAME bout must be used across runs for within-subject reproducibility.
- **Sampling — serum UA** (UASure home meter, duplicate readings per timepoint per §3.10 discipline):
  - t = 0 (immediately pre-exertion)
  - t = +30 min post (immediately at exertion end)
  - t = +60 min
  - t = +90 min
  - t = +120 min
- **Sampling — urinary urate/creatinine ratios** (Pass 3 augment — directly addresses the renal-clearance question, not just serum UA which is a "blunt proxy"):
  - Spot urinary urate/Cr at t = 0, immediately post, +60 min, +120 min
  - Dipstick (Quantofix Urate + Creatinine, ~$1/test) OR Quest/LabCorp send-out if dipstick accuracy insufficient
- **Symptom tracking:** Joint pain scores (VAS 0–10) for any previously-flared joints at 6 / 12 / 24 / 48 / 72 hours. Continue flare-log monitoring per [`self-experiment-protocol.md`](../self-experiment-protocol.md) §5.
- **Run cadence:** n=several runs over months, runs spaced by ≥4 weeks. Within-subject statistical signal requires multiple runs to characterize variance.

**Pre-registered predictions (commit to interpretation BEFORE running):**

| Observed pattern | Interpretation |
|---|---|
| Serum UA rises (Δ ≥ 0.5 mg/dL) AND urinary urate/Cr drops (impaired clearance) AND a flare follows within 72h | **Mechanism #5 supported** (metabolic-overload — TCM 劳累 model in modern kinetic terms) |
| Serum UA unchanged AND urinary urate/Cr unchanged AND a flare follows within 72h | **Mechanisms #1–4 supported** (mechanical — shedding / mechanotransduction / DAMP / effusion, NOT via systemic urate kinetics) |
| Serum UA rises but no flare | Threshold not crossed this run; additional runs needed to characterize the UA→flare relationship at this bout intensity |
| No UA change, no flare across ≥3 consecutive runs | Exertion at this bout intensity is NOT a personal trigger for Brian (different from 19.3% of Qingdao cohort) — mechanism question becomes academic in Brian's case |
| Mixed (UA dynamics + flare pattern point different directions) | Document and continue running to build within-subject distribution |

**Safety / stopping rule (Pass 3 augment):**

- If Phase 1 provokes a clear flare (pain ≥ 4/10 at any flared joint within 72h), **hold further exertion-challenge runs for ≥6 months** to avoid cumulative flare burden. The experiment's value is in within-subject pattern, not in repeated provocation.
- If 3 consecutive runs show no flare, conclude exertion at this bout intensity is not Brian's personal trigger; mechanism question moot.

**Estimated cost:** ~$50–80 per run = UASure strips (10 readings × $1.50) + urinary urate/Cr dipsticks (~$30) OR Quest send-out (~$40).

**Estimated timeline:** ~6-hour observation window per run; ~72h flare-log monitoring window; runs spaced ≥4 weeks.

**Dependencies:** UASure meter + strips (existing infrastructure from §3.10). Urine collection cup + Quantofix dipsticks OR Quest/LabCorp send-out arrangement.

**Success criteria:**

- **Validates mechanism #5 (metabolic-overload):** post-exertion serum UA rises ≥ 0.5 mg/dL AND urinary urate/Cr drops AND a flare follows within 72h. Across ≥2 runs to confirm.
- **Validates mechanisms #1–4 (mechanical):** serum UA unchanged AND urinary urate/Cr unchanged AND a flare follows within 72h. Across ≥2 runs to confirm.
- **Negative provocation across ≥3 runs:** exertion at this bout intensity is not Brian's personal trigger; mechanism question moot.

**Caveats and confounds:**

- UASure CV ~10–15% — duplicate readings + ≥ 0.5 mg/dL effect-size threshold helps separate signal from noise (parallel to §3.10 discipline).
- Hydration confounds both serum UA AND urinary urate/Cr — strict water standardization is load-bearing.
- Recent flares within 4 weeks change baseline UA dynamics — defer runs until 4+ weeks post-flare.
- Brian's clomid taper is in flight; testosterone changes affect both UA and inflammation tone. Schedule runs to bracket OR sit firmly inside one phase of that taper.
- **Per Pass 3 augment:** serum UA alone is a "blunt proxy" for the renal-clearance question; urinary urate/Cr is the direct test that [`mechanical-flare-triggers.md` §"Open question 7"](../mechanical-flare-triggers.md) names. Both together strengthen the mechanism call.

**Deferred future variants (gated on access):**

- **Phase 2 — colchicine cover.** If Brian gains colchicine access (rheumatologist referral), repeat the same bout with AGREE-style colchicine pre-dosing. Tests whether NLRP3-axis blockade prevents the exertion-triggered flare. Per Pass 3 caveat: colchicine is a "broad neutrophil/microtubule perturbation" not a "clean NLRP3-specific isolation" — interpretive caveat preserved.
- **Topical CBD:THC cover.** Brian-accessible NLRP3-blockade variant (CB2 GPCR per [`cannabinoids-terpenes.md` §4a](../cannabinoids-terpenes.md)): apply pre-exertion to historically-flaring joint. Could be a separate sub-experiment under the Protocol C n=1 framework at [`self-experiment-protocol.md` §13](../self-experiment-protocol.md) rather than a sub-arm of §3.11 (scope discipline: one experiment, one decision).

**Cross-references:** [`mechanical-flare-triggers.md` §"Experimental designs that would close the gaps" item 7](../mechanical-flare-triggers.md) (the modern-physiology testable equivalent — this §3.11 is its n=1 self-experiment form); [`fructose-connection.md`](../fructose-connection.md); [`self-experiment-protocol.md`](../self-experiment-protocol.md) §5 (flare-log integration); [`validation-experiments.md` §3.10](../validation-experiments.md) (fructose challenge — complementary, NOT replaced).

---
