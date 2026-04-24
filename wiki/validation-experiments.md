---
title: Validation Experiments
aliases: [experiments, validation, testing phases]
related: [engineered-yeast-uricase-proposal, engineered-koji-protocol, open-source-platform, supplements-stack]
sources: [engineered-yeast-uricase-proposal.md, engineered-koji-protocol.md, open-enzyme-vision.md, nlrp3-exploit-map.md, gout-deep-dive.md]
---

# Validation Experiments

## Overview

A comprehensive map of all proposed experiments for the Open Enzyme project, organized by phase and documented across all research documents. Each experiment includes its purpose, proposing source, estimated timeline/cost, and dependencies.

---

## Phase 1: In Vitro Validation

### 1.1 Uricase Gene Performance Comparison

**What it tests:** Which uricase gene (Aspergillus flavus, Candida utilis, or Vibrio vulnificus) performs best in S. cerevisiae?

**Proposed in:** engineered-yeast-uricase-proposal.md (§3)

**Protocol:**
- Order codon-optimized synthetic genes for all three candidates (*A. flavus*, *C. utilis*, *V. vulnificus*)
- Each in the same expression cassette (pTEF1 promoter, CYC1 terminator)
- Integrate at the same chromosomal locus in S. cerevisiae
- Compare: (a) expression level by Western blot, (b) specific uricase activity in cell lysate, (c) enzyme stability at 37°C over 24h

**Estimated cost:** $2,000–3,000 (gene synthesis ~$0.10/bp × ~900 bp × 3 genes + reagents)

**Estimated timeline:** 4–6 weeks

**Dependencies:** None

**Success criteria:** Identify highest-performing gene with >50 μmol/h/OD activity

---

### 1.2 Secretion vs. Intracellular Expression

**What it tests:** Should uricase be secreted into the medium or retained intracellularly?

**Proposed in:** engineered-yeast-uricase-proposal.md (§3)

**Protocol:**
- Clone A. flavus uaZ into two constructs: (1) with α-factor signal peptide for secretion, (2) without for intracellular accumulation
- Transform both into same yeast strain
- At 48h growth in liquid culture, draw samples and run uricase activity assay:
  - Supernatant (for secreted enzyme)
  - Cell pellet lysate (for intracellular enzyme)
- Compare total enzyme output, specific activity, and fraction secreted

**Estimated cost:** $500–1,000

**Estimated timeline:** 2–3 weeks

**Dependencies:** None (can be done in parallel with 1.1)

**Success criteria:** Identify format with highest bioavailable uricase in food product context

---

### 1.3 Uricase Survival in Beer Fermentation

**What it tests:** Does uricase remain enzymatically active through beer fermentation?

**Proposed in:** engineered-yeast-uricase-proposal.md (§4)

**Protocol:**
- Brew 1-gallon test batch with engineered yeast
- At each stage—active fermentation (day 3), end of primary (day 7), after conditioning (day 14), after bottling (day 21)—draw samples
- Run uricase activity assay (spectrophotometric at 293 nm, measuring uric acid consumption)
- Control: purified uricase added to finished beer at same stages (distinguishes production from survival)

**Estimated cost:** $200–400 (homebrew supplies + uric acid assay reagents)

**Estimated timeline:** 3–4 weeks

**Dependencies:** Requires engineered yeast strain from Phase 1 optimization

**Success criteria:** Retain >30% activity through bottling (lower indicates degradation during fermentation)

---

### 1.4 Uricase Stability After Drying

**What it tests:** Can uricase survive lyophilization or heat drying for a shelf-stable product?

**Proposed in:** engineered-yeast-uricase-proposal.md (§4)

**Protocol:**
- Take concentrated pellet of engineered yeast, split into four aliquots:
  1. Fresh lysate (positive control)
  2. Freeze-dried/lyophilized pellet
  3. Heat-killed at 55°C then dried
  4. Spray-dried at 120°C inlet temperature
- Rehydrate each, lyse, and assay uricase activity
- Report as % activity retained vs. fresh lysate

**Estimated cost:** $300–800 (lyophilizer access via core facility)

**Estimated timeline:** 1–2 weeks

**Dependencies:** Requires engineered yeast strain from Phase 1 optimization

**Success criteria:** >40% activity retained via lyophilization for capsule formulation viability

---

### 1.5 Koji Uricase Expression and Activity

**What it tests:** Can A. flavus uricase gene express functionally in A. oryzae?

**Proposed in:** engineered-koji-protocol.md (§3, §5)

**Protocol:**
- Clone uaZ into engineered A. oryzae with PamyB promoter + SPamyB secretion signal + uaZ CDS + TtrpC terminator
- Grow on steamed rice (traditional koji conditions: 30°C, 48–72h)
- Harvest koji, prepare extract, assay uricase activity
- Compare: (a) expression level by Western blot, (b) specific uricase activity, (c) total enzyme yield per gram rice

**Estimated cost:** $1,500–2,500 (gene synthesis, transformation, reagents)

**Estimated timeline:** 4–6 weeks

**Dependencies:** None

**Success criteria:** >20 μmol/h/OD activity; enzyme properly secreted into rice substrate

---

### 1.6 Koji Enzyme Stability at Digestive pH and Temperature

**What it tests:** Does koji-produced uricase survive gastric and duodenal conditions?

**Proposed in:** engineered-koji-protocol.md (§6)

**Protocol:**
- Prepare koji extract with active uricase
- Expose to simulated gastric juice (pH 2.0, 37°C, pepsin) for 30 min
- Then simulated intestinal juice (pH 8.0, 37°C, pancreatin) for 120 min
- Assay uricase activity at each stage
- Compare to control uricase (Aspergillus nidulans uricase or rasburicase)

**Estimated cost:** $300–600 (digestive enzyme prep, assay reagents)

**Estimated timeline:** 1–2 weeks

**Dependencies:** Requires koji strain from 1.5

**Success criteria:** Retain >20% activity after duodenal transit (similar to ALLN-346 engineering target)

---

### 1.7 NLRP3 Inflammasome Pathway Validation (THP-1 MSU Macrophage Assay)

**What it tests:** Do proposed compounds in the [[supplements-stack]] actually inhibit NLRP3 at stated chokepoints?

**Proposed in:** nlrp3-exploit-map.md, gout-deep-dive.md

**Protocol:**
- Use macrophage cell line (**THP-1 differentiated with PMA** preferred over primary mouse macrophages — the species-gap caveat in [supplements-stack.md](./supplements-stack.md) makes human cells mandatory for translation)
- Prime with LPS (Signal 1: NF-κB priming)
- Expose to MSU crystals (NLRP3 trigger)
- Treat with individual compounds and read out in parallel
- Measure endpoints: IL-1β secretion (ELISA), caspase-1 activity, ASC specks (fluorescence), **IκBα retention (Western — mechanistic readout for proteasome-pathway inhibitors)**
- Compare dose-response and mechanistic target (which chokepoint affected)

**Priority compounds (ordered by information value of the specific mechanistic claim being tested):**

- **EGCG — highest-priority single-compound assay.** The mechanistic claim in [egcg.md](./egcg.md) (proteasome inhibition → IκBα stabilization → unified CP1 + CP1a + CP4 + CP5a coverage) is specific and testable. Readouts: IL-1β ELISA + **Western for IκBα retention** + TNFSF14-induced IL-6 in HGF co-culture (tests CP1a). If the proteasome mechanism is correct, EGCG should show a steeper dose-response than quercetin or ursolic acid at equimolar concentrations, and IκBα retention should track the proteasome IC50 (86 nM cellular) rather than the reported IKK IC50 (≥10 μM). Phytosome-formulated EGCG recommended alongside free EGCG to test the bioavailability-gated translation question. This brings a falsifiable mechanistic claim to a format that can actually falsify it.
- **Oridonin** — direct NLRP3 NACHT Cys279 covalent binder; 5.18 μM human THP-1 IC50 per ChEMBL. Tests whether the curated human IC50 replicates in our hands.
- **BHB** — tests direct NLRP3 K⁺-efflux-block mechanism; straightforward positive-control-class compound.
- **Sulforaphane** — Nrf2 activator; tests whether the Nrf2/NF-κB crosstalk mechanism translates to MSU-triggered cells at achievable sub-μM doses.
- **Quercetin** — now primarily a CP6a (5-LOX) compound; tests whether the weaker NF-κB/NLRP3 claim holds at μM concentrations.
- **Carnosine + Lactoferrin** — unique mechanism classes (dual UA/NLRP3 and CP5 GSDMD-axis respectively); tests whether the rat/murine evidence translates to human THP-1.

**Estimated cost:** $5,000–8,000 (cell culture, cytokines, assay kits, Western reagents, compound panel)

**Estimated timeline:** 8–10 weeks (larger compound panel than original scope)

**Dependencies:** None

**Success criteria:** 
- Confirm >50% IL-1β reduction at stated compound doses; validate chokepoint targets
- **EGCG-specific:** dose-response for IκBα retention tracks the 86 nM proteasome IC50 (falsifies or confirms the proteasome-pathway reframe); dose-response is steeper than quercetin at equimolar (confirms mechanistic difference between direct-proteasome and NF-κB-pathway-modulator compounds)

---

## Phase 2: Animal Model Validation

### 2.1 Gnotobiotic Mouse Colonization with Engineered S. boulardii

**What it tests:** Can engineered probiotic yeast survive and function in the mouse gut? What dosing is needed?

**Proposed in:** engineered-yeast-uricase-proposal.md (§4.d)

**Protocol:**
- Colonize germ-free mice with engineered S. boulardii expressing uricase
- Measure:
  - Fecal yeast counts daily for 14 days (CFU/g)
  - Fecal and cecal uricase activity assay
  - Serum uric acid in Uox-knockout mice (or potassium oxonate-hyperuricemic model)
- Compare: engineered strain vs. wild-type S. boulardii vs. untreated controls

**Estimated cost:** $5,000–15,000 (gnotobiotic mouse facility time, staff, housing, assays)

**Estimated timeline:** 8–12 weeks

**Dependencies:** 
- Requires optimized S. boulardii uricase strain from Phase 1
- Requires access to a gnotobiotic facility — ideally Rheinallt Jones's Emory Gnotobiotic Animal Core, if he joins as a collaborator

**Success criteria:** 
- Maintain >10⁶ CFU/mL fecal yeast counts through day 7
- Achieve measurable cecal uricase activity
- Reduce serum uric acid by ≥20% vs. controls

---

### 2.2 Hyperuricemic Rat Model: Engineered Yeast Efficacy

**What it tests:** Does oral administration of engineered yeast reduce systemic uric acid in a whole-organism model?

**Proposed in:** engineered-yeast-uricase-proposal.md (§5)

**Protocol:**
- Induce hyperuricemia in Sprague-Dawley rats using oxonic acid + allopurinol (standard model)
- Administer engineered yeast strain (lyophilized powder in capsules) daily for 14 days at varying doses
- Measure:
  - Serum uric acid (HPLC or uricase-catalase assay)
  - Urinary uric acid excretion (24h collection)
  - Fecal uric acid (as proxy for gut lumen degradation)
  - Kidney function markers (BUN, creatinine)
- Compare: treated vs. vehicle control vs. allopurinol positive control

**Estimated cost:** $8,000–12,000 (animal costs, housing, blood assays, LC-MS analysis)

**Estimated timeline:** 6–8 weeks

**Dependencies:** Requires Phase 1 optimization of yeast strain

**Success criteria:** 
- Achieve serum uric acid reduction of ≥30% vs. vehicle
- Increase fecal uric acid by ≥50% vs. vehicle
- Non-inferior to allopurinol in serum uric acid reduction

---

### 2.3 Engineered Koji Efficacy in Digestive Enzyme-Deficient Model

**What it tests:** Does engineered koji effectively supplement digestive enzymes in vivo?

**Proposed in:** engineered-koji-protocol.md

**Protocol:**
- Use pancreatic lipase knockout mice (or pancreatectomized mice as EPI model)
- Administer koji fermented on rice (whole food) as supplement (10% dietary w/w) for 14 days
- Measure:
  - Fat absorption (coefficient of fecal fat; <7g/day = normal)
  - Protein digestion (fecal nitrogen)
  - Starch digestion (breath hydrogen test)
  - Intestinal inflammation markers (fecal calprotectin)
- Compare: engineered koji vs. wild-type koji vs. no supplement vs. commercial enzyme supplement (Creon)

**Estimated cost:** $6,000–10,000 (genetically modified mice, housing, specialized assays)

**Estimated timeline:** 8–10 weeks

**Dependencies:** Requires koji strain from Phase 1

**Success criteria:** 
- Normalize fat absorption to >92% (vs. <50% in untreated EPI)
- Non-inferior to commercial enzyme supplement

---

### 2.4 NLRP3 Inflammasome Inhibition in MSU Crystal Arthritis Model

**What it tests:** Do proposed NLRP3 inhibitor compounds reduce gout flare severity in vivo?

**Proposed in:** nlrp3-exploit-map.md, gout-deep-dive.md

**Protocol:**
- Induce acute gout in C57BL/6 mice by intra-articular MSU crystal injection into knee
- Treat with compounds or combinations:
  - Individual compounds (BHB via ketogenic diet, oridonin oral gavage, sulforaphane)
  - Multi-compound stack (BHB + oridonin + sulforaphane)
  - Positive control: colchicine
  - Negative control: vehicle
- Measure:
  - Joint swelling (calipers measurement, MRI)
  - Pain behavior (weight bearing on affected limb, mechanical hyperalgesia)
  - Inflammatory cytokines in joint lavage (IL-1β, TNF-α, IL-6 by multiplex assay)
  - Histology: neutrophil infiltration, synovial inflammation score
- Timeline: measure at 4h, 24h, 48h, 72h post-injection

**Estimated cost:** $10,000–15,000 (transgenic mice, surgical arthritis induction, imaging, cytokine assays)

**Estimated timeline:** 10–12 weeks (including 2-week ketogenic diet adaptation)

**Dependencies:** Requires Phase 1 validation of NLRP3 pathway

**Success criteria:**
- Reduce peak joint swelling by ≥40% vs. vehicle
- Reduce joint IL-1β by ≥50% vs. vehicle
- Reduce neutrophil infiltration by ≥30% vs. vehicle

---

### 2.5 PULSE Probiotic Validation in Hyperuricemic Mice

**What it tests:** Can PULSE system (urate-responsive engineered E. coli) maintain uric acid homeostasis?

**Proposed in:** gout-deep-dive.md (Section 8)

**Protocol:**
- Colonize Uox-knockout mice with PULSE engineered E. coli Nissle 1917
- Administer at varying doses and dosing frequencies (daily vs. every 3 days)
- Measure:
  - Fecal E. coli counts and uric acid-responsive biosensor activity (reporter assay)
  - Serum uric acid over 28 days (weekly measurements)
  - Response to acute uric acid challenge (potassium oxonate injection)
  - Off-target metabolite accumulation (allantoin, oxaluric acid)
- Compare: PULSE vs. wild-type E. coli Nissle vs. untreated controls

**Estimated cost:** $5,000–8,000 (transgenic mice, E. coli handling, weekly blood draws, biomarker assays)

**Estimated timeline:** 8 weeks

**Dependencies:** Requires PULSE strain (Source: Cell Reports Medicine 2025 reference)

**Success criteria:**
- Maintain serum uric acid within 2.0–4.0 mg/dL range (homeostatic)
- Self-regulate in response to acute uric acid load
- Clear allantoin without accumulation

---

## Phase 3: Human Self-Experimentation and Biomarker Tracking

### 3.1 Brian: Engineered Yeast Uricase — Serum Uric Acid & Flare Tracking

**What it tests:** Does daily oral engineered yeast reduce serum uric acid and gout flare frequency in the primary user?

**Proposed in:** engineered-yeast-uricase-proposal.md (§5), open-enzyme-vision.md (§8)

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

**What it tests:** Does the multi-compound NLRP3 stack reduce inflammatory markers and flare severity?

**Proposed in:** nlrp3-exploit-map.md, open-enzyme-vision.md (§9)

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

### 3.3 Lynn: Wild-Type Koji Digestive Enzyme Supplementation

**What it tests:** Does traditional koji effectively supplement digestive enzymes in EPI/SIBO?

**Proposed in:** engineered-koji-protocol.md, open-enzyme-vision.md (§4)

**Protocol:**
- Lynn (EPI/SIBO patient) takes traditional koji fermented on rice daily
- Baseline: 2 weeks pre-intervention (establish GI symptom baseline, stool frequency/consistency)
- Intervention: 8 weeks daily koji consumption (10–20g dried koji powder or equivalent rice koji)
- Biomarkers measured weekly:
  - GI symptom score (abdominal pain, bloating, diarrhea on validated scale)
  - Stool frequency, consistency (Bristol Scale)
  - Fat absorption assessment (72h fecal fat collection or non-invasive fat absorption test)
  - Inflammatory markers: fecal calprotectin, serum CRP
  - Microbiome composition (stool 16S rRNA at baseline, week 4, week 8 if budget allows)
- Crossover: 2-week washout, then repeat with engineered koji (once available from Phase 1)

**Estimated cost:** $200–400 (koji ingredients, fecal tests) + $400–600 (optional microbiome analysis)

**Estimated timeline:** 12 weeks

**Dependencies:**
- Requires wild-type koji protocol
- Once Phase 1 complete, can compare vs. engineered koji

**Success criteria:**
- Reduce abdominal pain/bloating score by ≥50% vs. baseline
- Normalize stool frequency to 1–2× daily
- Reduce fecal calprotectin by ≥30% (if elevated at baseline)

---

### 3.4 Joint Trial: Engineered Koji (Both Users)

**What it tests:** Does engineered koji providing both digestive enzymes and uricase work as a dual-purpose therapeutic food?

**Proposed in:** engineered-koji-protocol.md, open-enzyme-vision.md (§4, dual-enzyme vision)

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

**What it tests:** Does uricase supplementation provide sustained reduction in gout flares?

**Proposed in:** open-enzyme-vision.md (§8)

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

## Cross-Experiment Dependencies and Sequencing

```text
Phase 1 (In Vitro)
├─ 1.1: Gene performance [weeks 1-6] ─────┬─→ 1.2, 1.3, 1.5, 1.6
├─ 1.2: Secretion vs. intracellular ──────┤
├─ 1.3: Beer survival ──────────────┬─────→ 2.2 (yeast efficacy)
├─ 1.4: Drying stability ───────────┤ ────→ 3.1 (yeast formulation)
├─ 1.5: Koji expression ────────────┬─────→ 1.6, 1.7 (koji validation)
├─ 1.6: Koji digestive stability ───┤────→ 2.3 (EPI model)
├─ 1.7: NLRP3 pathway validation ───┤────→ 2.4 (MSU arthritis model)
│
├─→ Phase 2 (Animal Models)
    ├─ 2.1: Gnotobiotic S. boulardii [weeks 12-20] ──┬─→ 3.1
    ├─ 2.2: Hyperuricemic rat model [weeks 10-16] ───┤─→ 3.1
    ├─ 2.3: EPI koji model [weeks 12-18] ───────────┬─→ 3.3
    ├─ 2.4: MSU arthritis model [weeks 14-22] ──────┬─→ 3.2
    └─ 2.5: PULSE E. coli probiotic [weeks 12-18] ──┤
    
    ├─→ Phase 3 (Human Self-Experimentation)
        ├─ 3.1: Yeast uricase (Brian) [weeks 24-44] ──┬─→ 3.5
        ├─ 3.2: NLRP3 stack (Brian) [weeks 24-44] ────┼─→ parallel with 3.1
        ├─ 3.3: Koji enzymes (Lynn) [weeks 20-32] ────┤─→ 3.4
        ├─ 3.4: Engineered koji (both) [weeks 36-50] ─┤
        └─ 3.5: Long-term flare prevention [weeks 45-71]
```

---

## Success Metrics Summary

| Phase | Experiment | Primary Endpoint | Target Threshold |
|-------|-----------|------------------|------------------|
| 1 | Gene performance | Uricase specific activity | >50 μmol/h/OD |
| 1 | Secretion | Bioavailable enzyme fraction | >30% extracellular |
| 1 | Beer survival | Enzyme activity retention | >30% post-fermentation |
| 1 | Drying | Lyophilization stability | >40% activity retained |
| 1 | Koji expression | Secreted uricase activity | >20 μmol/h/OD |
| 1 | Koji digestive pH | Duodenal survival | >20% activity post-transit |
| 1 | NLRP3 pathway | IL-1β reduction | >50% at stated doses |
| 2 | S. boulardii colonization | Fecal yeast counts | >10⁶ CFU/mL by day 3 |
| 2 | Yeast efficacy (rat) | Serum uric acid reduction | ≥30% vs. vehicle |
| 2 | Koji EPI model | Fat absorption | >92% (vs. <50% baseline) |
| 2 | MSU arthritis | Joint swelling reduction | ≥40% vs. vehicle |
| 2 | PULSE homeostasis | Uric acid range maintained | 2.0–4.0 mg/dL |
| 3 | Yeast uricase (Brian) | Flare frequency reduction | ≥50% vs. baseline |
| 3 | NLRP3 stack (Brian) | IL-1β reduction | ≥30% vs. baseline |
| 3 | Koji enzymes (Lynn) | GI symptom improvement | ≥50% vs. baseline |
| 3 | Engineered koji (both) | Tolerability + efficacy | >80% adherence + dual benefit |
| 3 | Long-term prevention | Sustained flare reduction | ≥40% reduction sustained 6mo |

---

## Notes on Open Questions

- **GLUT9 and urate transport bottleneck:** Could engineered koji produce high fructokinase inhibitors to address the fructose-gout link? (Source: gout-deep-dive.md, Section 9)
- **Delivery route optimization:** Is intestinal lumen degradation sufficient, or would systemic absorption of recombinant uricase be superior? (Source: blood-barrier-exploits.md)
- **Microbiome stability:** Will engineered probiotics persist without colonization, or is daily dosing required long-term? (Source: gout-deep-dive.md, Section 8)
- **Gene therapy as alternative:** Should we pursue CRISPR-based uricase gene therapy in parallel? (Source: gout-deep-dive.md, Section 6)

---

*Document maintained as part of the [[open-source-platform]] initiative. All experiments are designed for replication and community contribution.*
