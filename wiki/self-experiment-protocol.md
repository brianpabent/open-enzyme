---
title: "Self-Experiment Protocol"
date: 2026-04-25
tags: ["self-experiment", "n-of-1", "safety", "monitoring", "open-enzyme", "protocol"]
related:
  - etc/open-enzyme-vision.md
  - cross-validation.md
  - validation-experiments.md
sources:
  - "n-of-1 trial methodology (e.g., Kravitz & Duan, Ann Intern Med 2014)"
---

# Self-Experiment Protocol

A generic monitoring framework for n=1 self-experiments — applicable to any intervention an Open Enzyme user chooses to track on themselves: oral compounds, peptides, prescription dose changes, engineered organisms, injectable agents, dietary changes, sleep / training interventions, anything.

The protocol's job is to make sure (a) risks are surfaced before exposure, (b) data is collected prospectively rather than reconstructed afterward, (c) halt conditions are pre-defined, and (d) results are structured well enough to be useful to anyone — including a clinician you eventually share them with.

This page is the framework. Specific experiments (gout, EPI, autoimmune, sleep, performance) substitute their own metrics, timelines, and red-flag criteria into the structure below.

**Evidence level for this page.** The framework is Mechanistic Extrapolation — it applies standard clinical-monitoring principles to the n=1 setting. It does not establish efficacy of any intervention.

---

## 1. Scope

This protocol covers **any single-variable intervention** the experimenter chooses to track:

- Oral supplements / nutraceuticals
- Peptides (oral, intranasal, sublingual, injected, transdermal)
- Prescription medications and dose changes (with prescriber's knowledge)
- Engineered organisms
- Diet / lifestyle changes if framed as an experiment

It is intended for personal self-experimentation. It is **not** a clinical trial protocol and does not establish efficacy against a control. It is a framework for collecting your own data well.

---

## 2. Designing the experiment

Before starting any new intervention, define and write down:

| Element | Question to answer |
|---|---|
| **Hypothesis** | What change is expected? Why? Mechanism of action? |
| **Intervention** | Specific dose / form / timing / route |
| **Metrics** | Which markers / symptoms / outcomes change if the hypothesis is right? |
| **Cadence** | How often to retest, based on the intervention's pharmacokinetics and the marker's biology |
| **Timeline** | Total experiment window — from start to primary endpoint |
| **Halt criteria** | What outcomes mean stop |
| **Single-variable rule** | What other things you commit to *not* change during the window |

Write these down before starting. A retrospective hypothesis is hindsight, not data. Single-variable change is what makes the result interpretable.

---

## 3. Cadence — pick by mechanism

Different interventions need different retest cadences. Picking the wrong window produces noise, not signal — premature retests miss the effect; late retests miss safety problems.

| Mechanism class | Typical retest window |
|---|---|
| Drug at steady-state (most prescriptions, T-modulators, hormones) | 4–6 weeks after dose change (to reach new equilibrium) |
| Vitamin / mineral correction with stored forms (D3, iron, B12) | 8–12 weeks |
| Antibody-mediated effect (autoimmune-targeting interventions) | 3–6 months |
| Microbiota-mediated (probiotics, dietary fibre interventions) | 6–8 weeks (community shifts stabilize) |
| Acute / pharmacodynamic (caffeine, single-dose peptides) | hours to days |
| Tissue-level adaptation (training, structured exercise) | weeks to months depending on outcome |
| Cancer-prevention / risk-modifying (long-latency outcomes) | annual or longer; surrogate markers monthly |

Match the half-life of the intervention and the kinetics of the affected marker. Don't average them — pick whichever is longer.

---

## 4. Metrics — pick by what the intervention affects

Standard elements common to most experiments:

- **Primary efficacy marker** — the thing the hypothesis says should change
- **Safety markers** — organ-function and systemic markers relevant to the intervention's known risk profile
- **Symptom diary** — daily entries with domain-relevant fields, designed to take <60 seconds/day to enter
- **Compliance / adherence log** — did you take the intervention as planned, and when?

Common safety baseline for blood-panel-based experiments:
- **CBC with differential** — catches infection, anemia, WBC shifts (especially relevant for any immunomodulator)
- **CMP** — liver enzymes, kidney function, electrolytes (catches the most common organ-toxicity signals)
- **hs-CRP** — systemic inflammation; useful even when not the primary endpoint

Beyond that, the panel is intervention-specific:
- T-axis intervention → Total T, Free T, Estradiol, **SHBG**, Hematocrit, lipids
- Thyroid intervention → TSH, Free T4, Free T3, antibodies if autoimmune
- Microbiota intervention → stool sequencing (16S minimum) baseline + endpoint
- Glucose/metabolic intervention → fasting glucose, fasting insulin, A1C, lipids
- Specialty markers (complement, leukotrienes, etc.) → as the mechanism dictates

For symptom-only experiments without labs, structured daily tracking + a clear primary outcome is enough.

### Chokepoint-biomarker map

For NLRP3-targeted experiments specifically (the gout / autoimmune-flare track), a four-biomarker specialty panel — serum C5a, urinary LTE4, plasma SPMs (RvD1, MaR1), hs-CRP — maps onto distinct chokepoints in the [NLRP3 exploit map v1.2](./nlrp3-exploit-map.md). The point of this map is operational, not descriptive: the panel converts a binary "inflammation present / absent" readout into "which mechanism is currently active," and the decision rules below convert that into "which compound to add next if the stack underperforms." Evidence level is **Mechanistic Extrapolation** grounded in In Vitro and Animal Model evidence from the cited pages — not Clinical Trial. Specific cutoffs vary by lab; defer numeric thresholds to the ordering physician and the lab's reference range. The contingent NET panel (rule 5 below) is the only entry on this map that costs additional money per flare — keep it contingent.

| Biomarker | Reads out chokepoint | What "elevated" means | What "normal/low" means | Suggested next action if at variance with stack expectation |
|---|---|---|---|---|
| Serum C5a (+ desArg) | **CP0** — complement priming (MSU → C1/CRP → C5 convertase → C5a) | Active complement-driven priming; the upstream non-transcriptional "Signal 1" the stack does not currently cover (see [complement-c5a-gout.md §11](./complement-c5a-gout.md)) | Complement priming is not the rate-limiter for this flare phenotype | Persistently elevated C5a + clinical flares despite stack → discuss [avacopan](./complement-c5a-gout.md) (FDA-approved C5aR1 antagonist) with prescriber. Pre-analytics matter: cold-chain EDTA, spun within 30 min, –80 °C — warm transit generates spurious C5a in vitro. **Optional flare-trajectory addition (added 2026-05-19, source: spm-resolution-pathway.md §7.3 falsifiable prediction):** measure C5a at flare onset (within 24 h) AND at flare resolution (7–14 days post-onset). Compute decline slope = (onset − resolution) / days. Pair with concurrent blood omega-3 index (EPA + DHA % of total RBC fatty acids; OmegaQuant or equivalent). Per the SPM → aggNET → C5a-degradation loop, decline slope should be steeper in DHA-loaded subjects (omega-3 index ≥8%) than DHA-deficient subjects (omega-3 index <4%) — falsifiable prediction that converts SPM/omega-3 supplementation from generic anti-inflammatory framing into a CP0-coverage hypothesis testable on existing flare events. Adds ~$100–200/flare in lab cost (two extra C5a draws); doesn't change the intervention protocol. |
| Urinary LTE4 | **CP6a** — 5-LOX / LTB4 neutrophil amplification (on-target PD readout for 5-LOX engagement) | Active leukotriene amplification arm; neutrophil chemotaxis loop is open (see [zileuton.md](./zileuton.md)) | 5-LOX flux is low — quercetin / AKBA / EPA substrate competition is engaging target, or this patient's gout is not CP6a-dominant | LTE4 fails to drop on quercetin/AKBA/zileuton → "non-absorber, not non-responder" — PK / bioavailability problem, not target-engagement problem; check formulation (Phytosome quercetin, Boswellin AKBA) before escalating dose. Clean LTE4 drop + unchanged flare frequency → CP6a is not rate-limiting; redirect attention to CP0 or CP2 |
| Plasma SPMs (RvD1, MaR1) by LC-MS/MS | **CP5b** — active resolution via ALX/FPR2 (see [spm-resolution-pathway.md §12](./spm-resolution-pathway.md)) | Resolution program is engaged; omega-3 substrate is being converted to bioactive D-resolvins / maresins | Resolution-incompetent — substrate-limited (low omega-3 index) or pathway-limited (15-LOX / aspirin-acetylated COX-2 not generating intermediates) | Low SPMs + post-flare hs-CRP not returning to baseline → CP5b deficit; reframe omega-3 toward DHA emphasis per [supplements-stack.md](./supplements-stack.md) and check omega-3 index (target >8%); consider RvE1/LTE4 ratio (CP6a↔CP5b axis, [spm-resolution-pathway.md §12](./spm-resolution-pathway.md)) rather than absolute SPM number |
| hs-CRP | **Systemic inflammation endpoint** — no specific chokepoint; the integrated downstream readout | Active systemic inflammation; non-specific to mechanism. Also an upstream stratifier for CP0 (CRP is the dominant classical-pathway initiator on MSU surfaces, [complement-c5a-gout.md §11.3](./complement-c5a-gout.md)) | Systemic inflammation suppressed regardless of which chokepoint is doing the work | hs-CRP elevated + all three mechanism-specific markers normal → look outside the NLRP3 axis (occult infection, metabolic, training load); CRP doubling from baseline is already a §6 universal halt criterion |

**Red-flag decision rules.** Each rule is a pattern across the four-biomarker panel that points to a specific next compound to discuss with the prescribing physician. None of these are clinical thresholds — they are interpretive heuristics for an n=1 PD readout.

- **C5a elevated + LTE4 normal + hs-CRP elevated** → CP0 is the rate-limiting bottleneck; the stack's downstream (CP1/CP2/CP6a) coverage is fine but priming is unchecked → consider [avacopan](./complement-c5a-gout.md) discussion with the prescribing physician.
- **LTE4 fails to drop despite quercetin / AKBA / zileuton at adequate dose** → "non-absorber, not non-responder" — PK / bioavailability problem, not target-engagement problem; check formulation and absorption (Phytosome quercetin, fed-state dosing) before concluding the drug doesn't work in this patient.
- **Plasma SPMs low + hs-CRP elevated post-flare (>2 weeks)** → CP5b resolution-incompetent; reframe omega-3 toward DHA emphasis per [supplements-stack.md](./supplements-stack.md) and verify omega-3 index >8% before adding pharma at CP5a (anakinra / canakinumab / rilonacept).
- **C5a normal + LTE4 normal + SPMs normal + hs-CRP elevated** → the inflammation signal is not coming from the NLRP3 axis this panel covers; investigate non-NLRP3 sources (occult infection, training load, metabolic) before adjusting the stack.
- **If a flare occurs AND the standard panel returns ambiguous on the resolution axis** (specifically: plasma SPMs borderline + urinary LTE4 borderline + hs-CRP elevated, with no clear bottleneck pattern from the four rules above) → add a citH3 + cfDNA + MPO-DNA complex panel at the next post-flare draw (~$200–400 specialty lab). Reads out the free-vs-aggregated NET ratio — distinguishes a resolution-competent flare (cytokines being sequestered into aggNETs) from a resolution-stuck flare (free NETs amplifying inflammation), per the aggNET vs. free-NET framing in [nlrp3-exploit-map.md v1.2](./nlrp3-exploit-map.md) (Schauer 2014, PMID 24784231; In Vitro + Animal Model for the framing, Mechanistic Extrapolation for the resolution-competence interpretation) and the upstream SPM driver of aggNET formation in [spm-resolution-pathway.md §5](./spm-resolution-pathway.md). Don't run routinely; the existing SPM panel covers the resolution axis indirectly under most circumstances — citH3/cfDNA is the *consequence* readout where SPMs are the *signal*, and the marginal information rarely justifies the cost. (V4-Pro 2026-04-25 peer-review flagged routine NET panels as "impractical for n=1"; this contingent rule keeps the option available without burning $200–400/flare on routine cases.)

**Cross-references:** [nlrp3-exploit-map.md](./nlrp3-exploit-map.md) (canonical chokepoint definitions, v1.2; aggNET vs. free-NET framing), [complement-c5a-gout.md](./complement-c5a-gout.md) (CP0 biomarker handling and avacopan), [spm-resolution-pathway.md](./spm-resolution-pathway.md) (CP5b SPM panel methodology, RvE1/LTE4 ratio, §5 SPM-driven NET resolution), [zileuton.md](./zileuton.md) (urinary LTE4 as 5-LOX PD readout).

---

## 5. Symptom diary

Daily, low-friction entries. Pick fields relevant to what you're testing. Common scales:

- **Likert (0–10)** for severity/intensity (pain, fatigue, energy, cognitive clarity, sleep quality)
- **Bristol Stool Scale (1–7)** for GI consistency
- **Likert (0–3)** for binary-with-gradient signals (bloating: none / mild / moderate / severe)
- **Free-text "novel signal" field** for anything not covered (always include this)
- **Timestamp + one row per day** — even a "nothing today" entry documents adherence

Storage: spreadsheet, plain text file, journaling app, daily log markdown — whatever you'll actually use consistently. The best diary is the one you'll fill out. Export to a structured format at endpoint for analysis.

---

## 6. Red-flag halt criteria

These are **universal** halt criteria — apply regardless of what intervention is being tested:

1. **New GI bleeding** (blood in stool, melena, hematemesis) — halt + seek care same-day
2. **Acute liver injury** (ALT or AST >2× upper limit of normal on a draw) — halt + re-draw at 2 weeks
3. **Kidney function decline** (eGFR drop >15% from baseline, or creatinine rise) — halt + evaluate
4. **New allergic / hypersensitivity signal** (rash, urticaria, angioedema, anaphylaxis) — halt immediately; seek care if airway involved
5. **Unexplained weight loss >5 lb over 4 weeks** — halt + evaluate
6. **New fever without identified infection** — halt + seek care
7. **CRP doubling from baseline** on a scheduled draw — halt + re-draw at 1 week to confirm
8. **Persistent diarrhea >72 hours** — halt + evaluate for dysbiosis or infection
9. **Any new severe symptom not present at baseline** — halt + evaluate

In addition to universal criteria, **define experiment-specific halt criteria at design time**. Examples:
- NLRP3-modulating interventions → unmasked infections (canakinumab side-effect class)
- T-modulating interventions → hematocrit >50%, mood / aggression, lipid degradation
- Anticoagulant changes → bruising, bleeding gums, blood pressure
- Microbiota interventions → dysbiotic shift on 16S
- Thyroid interventions → palpitations, anxiety, sleep disruption (T3 over-replacement signature)

"Halt" means stop the investigational intervention. It does **not** mean stop medically-prescribed therapy unless the trigger specifically implicates that therapy. When in doubt, contact your prescriber.

---

## 7. Logging and version control

**Principle: personal n=1 data does not live in the public Open Enzyme repository.**

Lab results, daily logs, self-experiment plans, and stack tracking are PHI-bearing. Keep them in a **separate private location** of your choice. Common patterns:

| Pattern | When it fits |
|---|---|
| Private GitHub repository | Multi-machine sync, collaborator access, version history, off-site backup |
| Local folder, not in git | Simplest; single-user; manual backup |
| Encrypted volume + cloud backup | Higher privacy posture |

The public Open Enzyme repo's `.gitignore` should exclude whatever directory your private storage lives in if you nest it inside the working tree. The choice of folder name, internal layout, and tooling is yours.

**Consent on partner / family data**: if your storage includes someone else's data (e.g., a spouse's labs), that data is theirs. Document their agreement before adding anything — a dated note in the relevant location is the lowest-friction way.

**Summary log (public, committed)**: a stripped, de-identified summary can be added to `logs/self-experiment-log.md` in the public repo (append-only). Fields: date, intervention, observation, any protocol deviation. Safe to commit because it contains no raw PHI. Never reference specific lab values; use qualitative framing ("CRP trending up" rather than "CRP = 4.2"). Numeric trending stays in your private storage.

**When a stack compound is added or removed**: note it with a dated rationale in your private location. The public-log version (if any) can be a stripped one-liner.

---

## 8. What this protocol does NOT do

- **Establish efficacy against a control.** n=1 is uncontrolled, unblinded. Efficacy signals are suggestive, not generalizable. They can motivate a future controlled trial; they cannot replace one.
- **Replace medical supervision.** Your primary care provider and any specialists should know what you're doing. Halt criteria are escalation-to-care triggers, not self-directed-recovery instructions.
- **Cover regulatory territory.** This is personal self-experimentation, not a clinical trial. Do not distribute engineered strains, compounded products, or off-label prescriptions to others under this protocol.

---

## 9. Review and update

Review this document and your active experiment designs: (a) before starting a new intervention arm, (b) after any halt, (c) annually, (d) whenever your understanding of the relevant biology changes. Changes go through git, not inline edits.

---

## 10. Example: PERT-Timing Sub-Experiment (EPI Track, April 2026)

An example of this protocol applied to the EPI track. A structured self-experiment on BoulderBio (wild-type *A. oryzae* OTC, 40,000 FIP lipase per capsule) dose and timing was run across ~30 meals (2026-04-19 → present). Key design elements:

- **Hypothesis:** Label-default 1-cap dosing is insufficient for meals >15 g fat; 2-cap or split-dose protocol will improve symptom outcomes.
- **Intervention variants:** A (1 cap at first bite), B (2 caps at first bite), C (1+1 split), D (pre-emptive during cooking).
- **Metrics:** Post-meal stool consistency (Bristol Scale), pain (0–10 Likert), floaters/steatorrhea (binary), fat content per meal (estimated g).
- **Single-variable rule:** Enzyme dose/timing varied; diet, other supplements held constant within each variant window.
- **Confound flagged:** Lying flat <90 min post-meal identified as a strong contributor to overnight episodes — must be controlled separately from enzyme-dose effects.

**Interim findings (n=1, unblinded, uncontrolled; source: digestive-enzyme-optimization.md):**
- Variant B (2 caps at first bite) decoupled liquid-stool from pain on 2026-04-25 breakfast (~15–20 g fat) — a clear shift from a long-stable baseline.
- Variant C (1+1 split) successful for >25 g fat meals.
- No adverse reactions across 30+ meals; no allergic response.

**Evidence level:** Clinical n=1, single subject, unblinded, uncontrolled. Suggestive only. Generates hypotheses for formal testing; does not establish efficacy. Paired stool-fat (steatocrit) measurement before and after a controlled trial would be the next-rigor step.

Full daily log lives in the experimenter's private storage (e.g., `<your-private-repo>/<subject>/experiments/<date>_<topic>.md`). Only de-identified pattern findings are reproduced here, per the PHI policy in §7 above.

---

## 11. Optional ex vivo monitoring add-ons

Lower-cost subject-specific assays that supplement the standard four-biomarker panel for specific intervention contexts. Each is opt-in, runs as a quarterly add-on to the standard blood draw, and stays in the subject's private storage per §7.

### 11.0 Selenium + yanthine — PDB function screen *(added 2026-05-15)*

**When relevant:** Any draw while hyperuricemia is active or gout risk is being managed. One-time triage, not ongoing monitoring.

**Rationale:** The PDB (purine-degrading bacteria) gut pathway enzyme DOPDH is selenium-dependent and runs 27x faster with selenium than without. Selenium deficiency could functionally knock out PDB activity without any change in bacterial abundance — the bacteria are present, they just can't work. Yanthine (2,8-dioxopurine) is the first PDB pathway intermediate; elevated serum yanthine indicates PDB are depleted or dysfunctional (can't process it downstream). Together these two markers answer whether Brian's gut-compartment urate disposal is operating normally or is constrained by a potentially trivial dietary factor. See [purine-degrading-bacteria.md §"Cofactor Requirements"](./purine-degrading-bacteria.md).

**What to order:**
- **Serum selenium** — standard clinical test, available at any reference lab (Quest/LabCorp), ~$40–80. Normal range 70–150 ng/mL; optimal for DOPDH function is likely mid-to-upper-normal. If low-normal (<90 ng/mL), supplementation at 100–200 µg/day (selenomethionine) is safe and cheap.
- **Yanthine (2,8-dioxopurine)** — not on standard panels. Triage step: check whether Metabolon Precision Metabolomics, Genova NutrEval, Great Plains Organic Acids, or a clinical pharmacology lab measures it. If a metabolomics panel (Metabolon, ~$300–600) already on the radar covers it, add at no incremental cost. If not available without a research lab arrangement, defer — serum selenium alone is the practical first step.

**Cost:** Selenium ~$40–80 (clinical). Yanthine: $0 if a planned metabolomics panel includes it; $300–600 for a standalone metabolomics run; defer if unavailable commercially.

**Cross-references:** [purine-degrading-bacteria.md](./purine-degrading-bacteria.md) §"Open Questions" PDB-Q3 and PDB-Q4.

### 11.0a Cranberry juice n=1 — direct hippuric-acid → ABCG2 axis test *(added 2026-05-15)*

**When relevant:** Same draw context as §11.0 — any draw while hyperuricemia is active or gout risk is being managed. Particularly informative when run in the same window as a §11.0 selenium / yanthine draw (the two protocols test parallel mechanisms hitting the same downstream node, ABCG2).

**Rationale:** *Alistipes indistinctus* produces hippuric acid via aromatic amino acid catabolism; hippuric acid enhances PPARγ binding to the ABCG2 promoter and promotes ABCG2 localization to the apical brush border via PDZK1 (Xu et al. 2024 Cell Host & Microbe, PMID 38412863). The standard dietary route is polyphenol-rich foods → gut catabolism → hippuric acid — slow, indirect, microbiome-dependent. **Cranberries bypass the bacterial step**: cranberries contain unusually high natural benzoic acid; benzoic acid is conjugated with glycine in the liver to produce hippuric acid directly. This is the established mechanism behind the cranberry-UTI lore (cranberry consumption → elevated urinary hippuric acid). For an n=1 test of whether the hippuric-acid → ABCG2 mechanism moves serum urate at dietary doses, cranberry juice is the cleanest probe — independent of needing to colonize *A. indistinctus*. See [`abcg2-modulators.md` Alistipes Tier 2 entry](./abcg2-modulators.md).

**Protocol:**
- 4 weeks unsweetened cranberry juice, ~8 oz/day with breakfast (or split across day if GI tolerance is an issue).
- Cost: ~$20 for the protocol.
- No other intervention changes during the 4 weeks (hold supplements stack constant; hold allopurinol dose constant).
- Standard 4-biomarker panel (serum urate + hs-CRP + fasting insulin + ApoB) at week 0 baseline + week 4.
- Optional add: urinary hippuric acid (specialty test, ~$40 at some reference labs) at week 0 + week 4 — confirms the cranberry → hippuric-acid mechanism is engaging in this individual.

**Expected effects:**
- **Serum urate down 0.2–0.5 mg/dL** if the hippuric-acid → ABCG2 axis is meaningful at dietary doses (Mechanistic Extrapolation; the Animal Model + Human Observational data in Xu et al. 2024 doesn't quantify the magnitude at dietary cranberry doses).
- **Urinary hippuric acid up substantially** at week 4 vs. baseline — confirms the mechanism is engaging.
- **No change in hs-CRP / insulin / ApoB** — cranberry-juice carb load is small (unsweetened); no expected metabolic-syndrome effects at this dose.

**Why this is informative regardless of outcome:**
- If serum urate moves AND urinary hippuric is up → mechanism replicates in this physiology, supports the broader chassis-pending PDB / *A. indistinctus* axis.
- If serum urate doesn't move AND urinary hippuric is up → mechanism engages but doesn't translate to ABCG2 / SUA effect at dietary dose; the *A. indistinctus* / hippuric axis may need higher concentrations than dietary route delivers, or may not be rate-limiting in this patient.
- If urinary hippuric doesn't move → cranberry isn't getting absorbed / conjugated as expected; the experiment didn't actually test the mechanism. Interpretation problem, not a mechanism falsification.

**Cross-references:** [`abcg2-modulators.md`](./abcg2-modulators.md) §"Tier 2 — Alistipes / Hippuric acid"; [`chassis-pending-interventions.md` §1](./chassis-pending-interventions.md) (PDB entry, "Cheapest first move" includes this).

### 11.1 Ex vivo MSU PBMC challenge (androgen-elevated subjects, Tier 4 of `validation-experiments.md` §1.23)

**When relevant:** Subject is on clomid, TRT, anabolic-androgenic steroids, or has high baseline endogenous testosterone, AND has gout / hyperuricemia history. The 2026-05-05 androgen × NLRP3 literature scan ([`androgen-urate-axis.md`](./androgen-urate-axis.md) §"Beyond transporters") identified a gap: testosterone × MSU-crystal × NLRP3 in macrophages has zero indexed papers. The general-tissue literature suggests androgens are anti-inflammatory in macrophages (Norata 2006 in vitro), but cardiac macrophages flip the direction (testosterone → ↑NLRP3 → male-skewed myocarditis). Whether gout-relevant macrophages follow the general-tissue pattern or the cardiac-tissue pattern is an open question. This add-on provides a low-cost personal signal in the absence of formal Tier 1–3 wet-lab data.

**What it measures:** Whether subject's PBMCs (peripheral blood mononuclear cells) produce more or less IL-1β in response to MSU crystal challenge ex vivo, tracked across panels as serum testosterone fluctuates (e.g., mid-cycle vs. trough on clomid; pre/post a TRT dose adjustment).

**Protocol:**
- **Sample:** Add 10 mL EDTA tube to the standard quarterly draw. Send to a clinical lab offering ex vivo cytokine release assays (these exist; vendors include Cellular Technology Limited and several specialty hospital labs).
- **Lab protocol (request from vendor):** Isolate PBMCs by Ficoll gradient → seed at 1×10⁶/well → 6-hr challenge with MSU crystals (100 μg/mL) ± LPS pre-priming (100 ng/mL × 3 hr, optional second arm) → measure IL-1β in supernatant by ELISA. Negative control: vehicle only. Positive control: nigericin 5 μM (NLRP3 activator).
- **Cost:** $500–1,000 per panel (vendor-dependent). Add-on to standard quarterly draw — no extra venipuncture.
- **Tracking:** IL-1β (pg/mL) per panel, alongside serum total + free testosterone, hs-CRP, and the standard four-biomarker panel from §4. Plot quarterly trajectory.

**What you can and can't conclude:**
- **Can:** Detect within-subject directional signal — does *your* MSU-induced IL-1β response track *your* serum T fluctuations? Useful for personal protocol decisions (e.g., does a heavier anti-inflammatory layer correlate with lower MSU-IL-1β release in your own cells?).
- **Cannot:** Prove causality (n=1, uncontrolled). Cannot generalize to other androgen-elevated subjects. Cannot substitute for the formal `validation-experiments.md` §1.23 Tier 1–3 cascade — that's where mechanistic claims get established.

**Evidence level:** Clinical n=1, single subject, unblinded, uncontrolled. Suggestive only for personal protocol decisions. Generates hypotheses; does not establish efficacy.

**Cross-references:** [`validation-experiments.md` §1.23](./validation-experiments.md) (the formal Tier 1–3 cascade this is the n=1 parallel of); [`androgen-urate-axis.md`](./androgen-urate-axis.md) §"Beyond transporters" (the literature gap being probed); [`nlrp3-inflammasome.md`](./nlrp3-inflammasome.md) (NLRP3 activation mechanism background).

---

## 12. Genotype-informed supplement quantification workflow

**Promoted to standalone page 2026-05-16.** The five-step workflow composing genotype-informed selection + home/community-biolab batch QC + biomarker tracking now lives at [`genotype-informed-supplement-workflow.md`](./genotype-informed-supplement-workflow.md). That page is the user-facing canonical surface for the closed-loop n=1 pharmacogenomics pipeline.

This protocol page focuses on the per-subject self-experiment mechanics (§1–§11 above) — daily log, biomarker tracking, intervention scheduling. The genotype-informed-workflow page focuses on the cross-component pipeline that those mechanics participate in.

When walking a new intervention end-to-end, follow [`genotype-informed-supplement-workflow.md`](./genotype-informed-supplement-workflow.md) for the workflow shape; come back here for the biomarker-tracking detail.

---

## 13. Acute-flare stack sub-experiment — Protocol C, prospective n=1 *(added 2026-05-21)*

**Scope.** Prospective n=1 evaluation of the Protocol C triple-mechanism acute-flare stack from [`gout-action-guide.md` §"Combined-route flare protocols"](./gout-action-guide.md) — colchicine + topical CBD:THC + DHA-emphasis omega-3. The combination has not been tested in any human RCT and is tagged Speculative. The point of running it as a structured n=1 across multiple flares is to **separate timing and endpoints by mechanism arm** rather than collapsing into one "flare better" composite signal — the three arms operate on different time scales and different chokepoints, and pooling them obscures which arm is doing the work.

**When relevant.** Subject has recurrent gout flares (≥3 per year), is already on colchicine (no statin / macrolide / cyclosporine / severe renal contraindication), maintains a chronic DHA-emphasis omega-3 dose with a measured blood omega-3 index ≥ 8% (the DHA-SPM arm is gated on chronic loading state; acute loading during a flare does not rescue an inadequate baseline), and has medical-cannabis access for the topical 1:1 CBD:THC arm.

**Pre-flare baseline (panel before the next flare event).**
- Serum omega-3 index (DHA + EPA % of total RBC fatty acids) — target ≥ 8%
- Serum hs-CRP (baseline inflammatory tone)
- Serum urate (chronic level — should already be tracked per §4)
- 24h-urine urate if available

**During the flare (Protocol C timing per `gout-action-guide.md` Protocol C):**
- **t = 0:** Oral colchicine 1.2 mg + topical 1:1 CBD:THC on affected joint + ice cycle 10–15 min
- **t = +1 h:** Oral colchicine 0.6 mg + re-apply topical CBD:THC + ice cycle 30–60 min
- **Throughout:** Continue chronic DHA-emphasis omega-3 at the standing dose (no acute load — baseline is the gating variable)
- **At onset (t = 0–6 h) — draw 1:** Serum C5a, hs-CRP, IL-1β if available. *This is the resolution-slope anchor — without an onset C5a value, the wind-down slope is unmeasurable.*

**Mechanism-separated endpoints — pick by which arm you want to evaluate.**

| Arm | Endpoint | Measurement windows | What a positive signal looks like |
|---|---|---|---|
| Colchicine (suppression, systemic) | Joint pain (VAS 0–10), joint circumference (cm), patient global flare-severity (VAS 0–10) | 6 h, 24 h, 48 h, 72 h | AGREE-style ≥50% pain reduction by 24 h |
| Topical CBD:THC (suppression, local) | Local joint pain at the application site (VAS 0–10) | 30 min, 1 h, 2 h, 4 h (rapid topical-onset window — separate from systemic colchicine timing) | Local pain drop within 30–120 min, before systemic colchicine kinetics would predict |
| DHA SPM (resolution-class, systemic) | Serum C5a slope days 3–7 (resolution phase per [`spm-resolution-pathway.md` §7.3](./spm-resolution-pathway.md)); serum 17-HDHA / 14-HDHA on LC-MS/MS lipidomic panel if accessible | Onset draw (t = 0–6 h), resolution draws day 3, day 5, day 7 | Steeper C5a decline slope (faster ng/L per day) in DHA-loaded events vs. omega-3-deficient comparator events (within-subject across flares) |
| Composite resolution | Flare duration to < 2/10 pain (days from onset) | Daily VAS log | Shorter than personal baseline median flare duration |

**Cadence and within-subject control.** A single flare event is one data point per arm. Useful inference requires **n = several flares per arm-state combination** — ideally the subject can compare events where:
- Omega-3 index was ≥ 8% (DHA arm "active") vs. < 4% (DHA arm "inactive") at flare onset
- Topical CBD:THC was applied vs. omitted (controlling for jurisdictional access)
- Colchicine was used at full AGREE dosing vs. partial / late

Logging discipline (per §5 symptom diary) is the load-bearing variable here — without dated per-arm logs across flares, the mechanism-separated endpoints collapse back into the "flare better" composite.

**What you can conclude.**
- **Per-arm directional signal:** Does *your* local pain drop on the topical CBD:THC arm timing window? Does *your* C5a slope steepen in DHA-loaded events? Does *your* composite flare duration shorten on Protocol C vs. prior single-arm protocols?
- **Within-subject mechanism-class evidence:** Is the resolution-class arm doing distinct work from the suppression-class arms in your own data, or is the composite signal entirely explained by the suppression arms?

**What you cannot conclude.**
- Cannot generalize to other subjects (n=1, uncontrolled, unblinded).
- Cannot substitute for a future formal Protocol C RCT — that's where population-level claims get established.
- Cannot disentangle a non-DHA arm of the SPM mechanism from a DHA-specific effect (the n=1 omega-3-index comparison is correlational across the subject's flare history).

**Evidence level:** Clinical n=1, single subject, unblinded, uncontrolled. Suggestive only for personal protocol decisions. Generates hypotheses; does not establish efficacy.

**Cross-references:** [`gout-action-guide.md` §"Combined-route flare protocols" Protocol C](./gout-action-guide.md) (the protocol composition canonical surface); [`spm-resolution-pathway.md` §7.3](./spm-resolution-pathway.md) (the C5a-decline-slope falsifiable prediction this n=1 partially tests); [`colchicine.md` §3.3.1](./colchicine.md) (colchicine arm mechanism + AGREE dosing); [`cannabinoids-terpenes.md` §4a](./cannabinoids-terpenes.md) (topical CBD:THC arm mechanism + Brian's n=1 layered-flare-interrupt anchor); [`complement-c5a-gout.md` §3.1](./complement-c5a-gout.md) (C5a half-life kinetics bounding the slope-measurement window).
