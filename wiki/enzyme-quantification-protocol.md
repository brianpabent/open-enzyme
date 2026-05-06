---
title: "Enzyme Quantification Protocol — Tiered Methods for Amylase / Protease / Lipase Activity in Koji-Derived Products"
date: 2026-05-06
tags: [protocol, methods, enzyme-assay, koji, EPI, validation, home-scale, bench-scale, calibration]
related:
  - koji-home-fermentation.md
  - engineered-koji-protocol.md
  - digestive-enzymes.md
  - digestive-enzyme-optimization.md
  - validation-experiments.md
  - self-experiment-protocol.md
sources:
  - USP General Chapter <1601> (microbial enzyme activity assays — unit definitions)
  - Bernfeld P. *Methods Enzymol.* 1, 149–158 (1955) — DNS reducing-sugar amylase assay (canonical)
  - Charney J., Tomarelli R.M. *J. Biol. Chem.* 171, 501–505 (1947) — azocasein protease assay (canonical)
  - Winkler U.K., Stuckmann M. *J. Bacteriol.* 138, 663–670 (1979) — p-nitrophenyl palmitate lipase assay (canonical)
  - Pancreaze / Creon prescribing information (USP unit content per capsule)
  - digestive-enzyme-optimization.md §"Lipase activity" and §"BoulderBio FIP↔USP conversion" — published *A. oryzae* U/g values + commercial benchmarks
  - validation-experiments.md §1.18 — 2-arm GI-survival assay design (Koji-S vs. Koji-I)
---

# Enzyme Quantification Protocol — Tiered Methods for Amylase / Protease / Lipase Activity in Koji-Derived Products

A protocol-and-methods companion to the koji wiki. Specifies **how to measure** the three native koji enzymes (amylase, protease, lipase) at four tiers of effort, what each tier can and cannot tell you, and how to anchor cheap home-scale assays against bench-grade ground truth so ongoing batch QC stays interpretable.

**This page does not relock literature U/g values for wild-type *A. oryzae* enzymes** — those live in [digestive-enzyme-optimization.md](./digestive-enzyme-optimization.md). It does not relock the GI-survival 2-arm experimental design — that lives in [validation-experiments.md §1.18](./validation-experiments.md). It is the **methods layer** that operationalizes the open question called out in [koji-home-fermentation.md §"Open questions"](./koji-home-fermentation.md): *quantitative comparison of shio-koji enzyme activity (units/g) vs. commercial PERT (Creon, Zenpep) units per pill — lab-measurable but not yet done.*

---

## 1. Decision frame — what to measure and why

For the EPI / PERT-comparison clinical question, the three koji enzymes are not equally load-bearing.

| Enzyme | Clinical relevance for EPI | Mechanism in food integration | Priority for this protocol |
|---|---|---|---|
| **Lipase** | **Primary bottleneck.** Pancreatic insufficiency is dominantly a lipase deficit; Creon dosing is calibrated on USP lipase units. | Hydrolyzes triglycerides → free fatty acids + monoglycerides in the gut. Koji-derived lipase activity per gram is an order of magnitude lower than commercial PERT (Mechanistic Extrapolation from published *A. oryzae* lipase yields vs. Creon label content; see [digestive-enzyme-optimization.md §"Lipase activity"](./digestive-enzyme-optimization.md)). | **High** — measure first. |
| **Protease** | Secondary. Protein digestion has more redundancy (gastric pepsin + brush-border peptidases) than fat digestion. | Different mechanism than gut substitution: pre-marinating protein in shio-koji partially hydrolyzes muscle protein **before ingestion**, reducing the protease + peptidase load on the gut rather than supplementing it. | **High** for the marinade-pre-digestion question; **low** for direct PERT comparison. |
| **Amylase** | Low. Salivary + pancreatic amylase + brush-border glucosidases provide redundancy; symptomatic starch malabsorption is uncommon in EPI. | Starch → maltose / glucose during shio-koji ferment + amazake; primary contributor to product sweetness. | **Low** for clinical comparison; **medium** for batch QC and fermentation-health monitoring. |

What **not** to bother measuring at this stage: α-glucosidase, glucoamylase, individual peptidase classes (acid vs. neutral protease can be informative but aren't gating), and lactase. These add complexity without changing the EPI / PERT-comparison verdict.

**Reference standard for "how much is enough."** Creon is labeled in USP lipase / amylase / protease units per capsule (see Creon prescribing information). A standard fat-meal Creon dose is 25,000 USP lipase units (cited in [digestive-enzyme-optimization.md §"Creon dosing equivalence"](./digestive-enzyme-optimization.md)). The OTC analogue benchmark is BoulderBio at 40,000 FIP per capsule (~9,000–10,000 USP equivalent — *In Vitro*; conversion source in [digestive-enzyme-optimization.md §"BoulderBio FIP↔USP conversion"](./digestive-enzyme-optimization.md)). Any koji-derived measurement should be expressed as a fraction of one of these reference doses to be clinically interpretable.

---

## 2. Tier 1 — Kitchen-grade semi-quantitative

**Equipment ceiling:** kitchen scale (0.01 g), pH-buffered water, food-safe thermometer, timer, smartphone camera. Total reagent cost typically <$25 (vendor-dependent; pharmacy-grade indicators + grocery substrates).

**Output type:** **inter-sample ratios at fixed temperature and pH**, not absolute units. Useful for: batch-to-batch comparison, control vs. treatment within a single run, calibrating against a Tier 3 ground truth (see §6). **Not useful for:** quoting USP units; comparing across labs; clinical claims.

**Discipline that makes Tier 1 worth running:**
- Always include a **water blank** (zero) and a **dissolved Creon capsule** (positive reference) in the same run.
- Triplicate samples per condition; report median + range.
- Hold temperature within ±2°C and pH within ±0.3 across the run — kitchen pH-7 phosphate buffer made from KH₂PO₄ + K₂HPO₄ is fine.
- Read endpoints by phone photo at fixed lighting and fixed timing, not by eye.

### 2.1 Lipase — olive oil + pH indicator

**Principle.** Lipase hydrolyzes olive-oil triglycerides → free fatty acids → pH drops → bromothymol blue (or phenol red) shifts color (blue→yellow for BTB, red→yellow for phenol red). Time-to-shift at fixed substrate load is inversely proportional to lipase activity.

**Setup (per sample):**
- 5 mL emulsified olive oil (homogenized 30 s in 5 mL pH-7 phosphate buffer + 1 drop dish detergent as emulsifier; matches Winkler & Stuckmann 1979 emulsion principle without the p-NPP).
- 3 drops bromothymol blue (0.04% in ethanol, pharmacy grade) or phenol red (0.02%).
- 1 mL test sample (clarified shio-koji liquid; see §5 for extract prep).
- Hold at 37°C in a water bath or yogurt-mode Instant Pot.

**Readout.** Photograph at t=0, 15, 30, 60, 90, 120 min. Score color shift on a 0–4 scale against the Creon-positive control's progression. Time-to-half-shift is the comparable metric.

**Sensitivity floor.** This assay reliably detects lipase activity within roughly an order of magnitude of one dissolved Creon capsule's per-mL activity (Mechanistic Extrapolation from indicator pKa range and typical pancreatic lipase specific activity). Below ~5% of Creon per mL the shift is too slow to call against drift.

### 2.2 Amylase — starch-iodine clearance

**Principle.** α-amylase cleaves starch to maltodextrin / maltose / glucose. Iodine forms a deep blue-black complex with intact amylose and a brown-to-clear color with the cleavage products. Time-to-clear (no blue) at fixed starch load is proportional to amylase activity. Direct kitchen analog of the spot-test stage of the Bernfeld 1955 DNS assay.

**Setup (per sample):**
- 50 mL 1% (w/v) starch solution in pH-6 acetate buffer (pH 6 because *A. oryzae* α-amylase optimum is acidic-neutral; matches typical assay conditions).
- 1 mL test sample.
- Hold at 37°C.

**Readout.** Every 2 min, withdraw 100 µL into a well plate or shot glass containing 2–3 drops Lugol's iodine (pharmacy USP). Score blue intensity by phone photo against a printed calibration card (deep purple-black → red-brown → clear). Time-to-clear is the metric.

**Notes.** Hishiroku white-koji (*A. luchuensis*) extract clears more slowly than yellow-koji (*A. oryzae*) extract at equivalent dose (Mechanistic Extrapolation from published amylase yields by species; see [digestive-enzyme-optimization.md §"Amylase activity by strain"](./digestive-enzyme-optimization.md)). This is expected, not a contamination signal.

### 2.3 Protease — gelatin liquefaction (or skim-milk-agar plate)

**Principle.** Protease cleaves gelatin (or casein) and liquefies a set gel (or clears an opaque skim-milk-agar lawn). Time-to-liquefy or halo diameter at fixed time = relative activity.

**Setup A — Gelatin tube (simplest):**
- 5 mL liquefied 4% (w/v) gelatin in pH-7 phosphate buffer per test tube; let set at 4°C for 1 h.
- Add 0.5 mL test sample on top; hold at 37°C.
- Time the inversion-test point (tube can be inverted without flow). Compare against Creon-positive and water-blank tubes.

**Setup B — Skim-milk-agar plate (more discriminating):**
- Pour 15 mL skim-milk agar (1% skim-milk powder + 1.5% agar in pH-7 buffer, autoclaved or pressure-cooked) into a sterile petri dish. Set at 4°C.
- Punch 6 mm wells with a sterile straw or cork borer.
- Add 50 µL test sample per well; hold at 37°C for 24 h.
- Photograph; measure the clear halo diameter around each well.

**Readout.** Halo diameter (mm) at 24 h, or time-to-liquefy in the tube assay. Both are linear-ish in log(activity) over a useful 1–2-log dynamic range.

---

## 3. Tier 2 — Smartphone colorimetry

**Equipment ceiling:** Tier 1 plus a smartphone-photometer rig (a 3D-printed cuvette holder or a phone case with a fixed light source and a slot for a 1 cm cuvette; multiple open-source designs, e.g., Adams 2017 *PLoS ONE*) plus a small reagent kit (DNS reagent, ninhydrin, p-NPP — total ~$50–80 in single-experiment quantities). Output: **A405 / A440 / A540 readings translated to relative concentration**; with proper standard curves, semi-absolute units.

**Output type:** approximate U/mL with a 2–4× error bar relative to a calibrated bench instrument; suitable for tracking changes over batch / time / condition with confidence; not suitable for publication-grade absolute claims.

### 3.1 Lipase — p-NPP with phone OD

**Principle.** Winkler & Stuckmann 1979: p-nitrophenyl palmitate (p-NPP) is hydrolyzed to p-nitrophenol (yellow, A405 max) + palmitate. Rate of A405 increase = lipase activity in U/mL (1 U = 1 µmol p-nitrophenol released per minute at 37°C, pH 8).

**Reagent.** p-NPP (Sigma N2752 or equivalent), made up fresh at 1 mM in 2-propanol; dilute 1:10 into pH-8 Tris buffer immediately before assay. Reagent ~$30 / 1 g (enough for ~500 assays).

**Procedure.** 0.9 mL substrate working solution + 0.1 mL test sample in a 1 cm cuvette at 37°C; phone-photograph through the cuvette holder at t = 0, 1, 2, 5, 10 min. Convert RGB to A405 via the phone-photometer calibration curve. Slope (ΔA405/min) → µmol/min via ε(p-nitrophenol, pH 8) = 18,500 M⁻¹cm⁻¹ (well-established).

**Calibration.** A 5-point standard curve with commercial pancreatic lipase (Sigma L3126) at 0, 0.1, 0.5, 1, 5 U/mL bridges the phone OD to U/mL.

### 3.2 Amylase — DNS reducing-sugar (Bernfeld 1955)

**Principle.** α-amylase releases reducing-sugar termini from starch; 3,5-dinitrosalicylic acid reagent reacts with reducing sugars to form an orange-red product (A540). 1 U = 1 mg maltose-equivalent released per minute at 37°C, pH 6.

**Reagent.** DNS reagent: 1% DNS + 30% sodium potassium tartrate + 0.4 N NaOH (Bernfeld 1955 recipe). Premixed kits also available (~$40 / 100 assays).

**Procedure.** Mix 0.5 mL 1% starch (pH 6 acetate) + 0.5 mL test sample at 37°C; quench at 5 min with 1 mL DNS reagent; boil 5 min; dilute 1:5 with water; phone-photograph A540. Standard curve: maltose 0.1–2 mg/mL.

### 3.3 Protease — ninhydrin or azocasein with phone OD

Two acceptable Tier 2 protease readouts:

- **Ninhydrin / free amino-N.** Hydrolyze 1 mL 1% casein (pH 7) with 0.1 mL test sample at 37°C for 30 min; precipitate residual protein with 2 mL 5% TCA; centrifuge or filter; react supernatant with ninhydrin reagent (heat 100°C × 15 min); read A570. Free amino-N released → relative protease activity. Ninhydrin reagent ~$30 / 100 assays.
- **Azocasein (Charney & Tomarelli 1947).** 0.5 mL 0.5% azocasein (pH 7) + 0.5 mL test sample; 37°C × 30 min; quench with 1 mL 10% TCA; centrifuge; read supernatant A440. Azocasein ~$50 / 1 g (enough for ~100 assays). Higher dynamic range than ninhydrin; closer to bench-grade.

Both methods have a 2–4× spread vs. spectrophotometer readout depending on phone-photometer build quality; serviceable for relative-activity tracking.

---

## 4. Tier 3 — Bench enzymology

**Equipment ceiling:** community-college biology lab or undergraduate teaching lab. UV-Vis spectrophotometer (any cuvette-based instrument; even a Spec-20 works for visible-range assays), micropipettes, water bath, centrifuge. **No specialized enzymology equipment required.**

**Output type:** **publication-grade absolute units** (USP, FIP, IU as configured). Comparable to Creon label values directly.

**Reagent cost:** ~$200 total for one-time per-enzyme stocks (p-NPP, azocasein, DNS, soluble starch, control enzymes from Sigma/Fisher).

The Tier 3 assays are the same chemistry as Tier 2, with the phone-photometer replaced by a calibrated spectrophotometer. The discipline shifts:

- **Triplicate biological replicates × triplicate technical replicates** (n=9 per condition).
- **Standard curves run same-day** with each batch.
- **Positive controls every plate**: pancreatic lipase (Sigma L3126), trypsin (Sigma T1426), α-amylase from *A. oryzae* (Sigma 10065).
- **USP unit calibration**: USP General Chapter <1601> defines lipase / amylase / protease units against specific substrate / temperature / pH / endpoint conventions. Match those conditions to report USP-equivalent units. Otherwise, report in IU and footnote the assay conditions.

**Suggested first run** (one-day bench session):
1. Extract preparation from a single shio-koji batch — one extract, three aliquots (§5).
2. Triplicate p-NPP lipase assay vs. dissolved Creon (matched per-mg basis).
3. Triplicate azocasein protease assay vs. dissolved Creon.
4. Triplicate DNS amylase assay vs. dissolved Creon.
5. Output: a single ratio table — *koji-extract activity per gram of fresh koji vs. Creon activity per capsule, expressed as percent-of-one-Creon-cap-equivalent per gram koji, separately for lipase / protease / amylase.*

**This first run is the load-bearing experiment** — it converts every subsequent Tier 1 / Tier 2 home assay into a number that means something clinically. Without it, home assays are only inter-sample ratios; with it, home assays become "this batch is 12% of one Creon cap per gram, which is consistent with our Tier 3 calibration of 14% ± 3%."

### 3.X GI-survival 2-arm design

A logical extension of the Tier 3 first-run is the [validation-experiments.md §1.18](./validation-experiments.md) 2-arm GI-survival assay (Koji-S free extract vs. Koji-I whole biomass, both passed through SGF → SIF → assay at each stage). That experiment is fully specified there — the present page provides the assay methodology it depends on. The §1.18 cost estimate of $300–500 includes the assay reagents covered above.

---

## 5. Sample preparation — extracting enzymes from finished koji / shio-koji

**For Tier 1 / 2 / 3, the sample matrix matters.** Protocol below is the default for fresh koji rice, shio-koji, and amazake samples; adapt buffer pH for the specific enzyme being measured.

1. **Mass.** Weigh 5–10 g fresh sample; record mass.
2. **Homogenize** in 4× volume of pH-extraction buffer (pH 7 phosphate for general; pH 5 acetate if measuring acid protease specifically; pH 8 Tris if measuring lipase under USP conditions). Use a stick blender or mortar for ≥1 min.
3. **Cold extract** at 4°C for 30 min with occasional inversion.
4. **Clarify** by centrifugation (10,000 × g, 10 min, 4°C) or filtration through a folded coffee filter pre-rinsed with extraction buffer.
5. **Aliquot** the clear supernatant into 0.5–1 mL portions; assay fresh same day or freeze at −20°C in single-use aliquots (avoid freeze-thaw — koji enzymes lose 20–40% activity per cycle in our Mechanistic Extrapolation from generic soluble-protein literature; verify per batch in §6 calibration).

**Whole-biomass assay** (the §1.18 Koji-I arm): lyophilize whole koji, grind to <100 µm powder, resuspend in extraction buffer at the same w/v as the extract for matched comparison. The assay is otherwise identical; the readout difference between whole-biomass and free-extract arms is the cell-wall-encapsulation-protection effect.

**Shio-koji liquid** as-is (not extracted from solids) is acceptable for direct lipase / amylase / protease assay if the question is "what enzyme activity does the marinade actually deliver to a steak surface" rather than "what's in the koji rice itself." Salt content (typically ~25% w/w in the liquid phase) does suppress some enzymes' activity at standard assay conditions — dilute 1:10 minimum into assay buffer to mitigate, and run salt-matched controls.

---

## 6. Calibration — anchoring home tests against bench ground truth

The calibration discipline is the bridge that makes Tier 1 home assays clinically meaningful.

**One-time calibration run (~half-day bench session):**
1. Prepare one well-mixed sample extract (100 mL or more, single source, single time point).
2. Run **Tier 3** assays for lipase / protease / amylase → publication-grade U/mL.
3. Run **Tier 1 OR Tier 2** assays on aliquots of the same extract → relative-activity scores.
4. Fit a linear regression: bench U/mL = α × (home score) + β. The slope α is the **calibration coefficient** for this batch / equipment / operator.

**Ongoing batch QC (all Tier 1 from then on):**
- Every batch is assayed at home using the same Tier 1 protocol, scored on the same scale.
- Multiply by the calibration coefficient → estimated U/mL → estimated U/g fresh koji.
- Report "this batch is X% of one Creon-cap-lipase-equivalent per gram koji" using the Tier 3 PERT comparison.

**Recalibrate annually** or when any of the following changes: koji starter (yellow ↔ white ↔ black), substrate (rice ↔ rice bran ↔ barley), incubation conditions (>5°C shift in mean temperature or >12 h shift in fermentation duration), home-assay equipment (new phone, new buffer batch).

**Interpretive bands** (post-calibration, for the lipase axis specifically — the EPI bottleneck):

| Lipase activity per gram fresh koji | Clinical interpretation | Action |
|---|---|---|
| <1% of one Creon cap | Trace activity. | Shio-koji as a flavor-and-pre-digestion vehicle; not a meaningful PERT contributor. |
| 1–5% | Plausible adjunct effect for moderate-fat meals. | Track in [self-experiment-protocol.md](./self-experiment-protocol.md) — does GI tolerance shift on shio-koji-marinade days? |
| 5–15% | Clinically interesting. | Consider whether it justifies dose reduction of a co-administered PERT cap on shio-koji-marinade meals (clinician discussion). |
| >15% | Surprising; verify against an outsource (Tier 4) before acting. | High-yield batch + high-lipase strain combination; document conditions, attempt to replicate. |

These bands are **Mechanistic Extrapolation** from PERT dose-response physiology; they are not validated clinical thresholds. Treat as orienting heuristics, not decision rules.

---

## 7. Tier 4 — Outsourced contract assay

**When to use:**
- One-time benchmarking of a strain × substrate combination before committing to Tier 3 in-house.
- Independent verification of a surprising Tier 3 result before publishing or acting clinically.
- Regulatory-grade activity reporting if any product-development path opens.

**Vendor landscape** (food / feed enzyme analytical labs as of 2026, sample-quote basis):

| Vendor type | Typical service | Per-enzyme cost (single sample) | Turnaround |
|---|---|---|---|
| Major food/feed contract lab (e.g., Eurofins, Romer, Covance) | USP / FIP / DSC-equivalent units, full QC documentation | ~$50–150 | 1–3 weeks |
| Specialty enzyme house (Megazyme, Novozymes contract services) | Substrate-specific activity assays (α-amylase, glucoamylase, lipase), often using the vendor's own substrate kits | ~$80–200 | 2–4 weeks |
| University core fee-for-service | Custom assay design, often cheaper per sample if you're patient | ~$30–100 | 4–8 weeks |

Cost ranges are vendor-published 2025–2026 sample quotes; verify per-vendor before committing. (Current as of date on this page; refresh quarterly via the literature-mining queue if needed.)

**What to send.** A homogenized 50 g fresh-koji sample on dry ice, vacuum-sealed, with a one-page chain-of-custody note specifying: sample mass, fermentation start/end timestamps, substrate and starter used, intended assay (lipase / protease / amylase + which units the vendor should report). Most labs accept dry-ice ground shipping; overnight not required for short routes.

---

## 8. Unit conventions and cross-mapping

| Unit | Definition (paraphrased) | Canonical for |
|---|---|---|
| **USP lipase unit** | Amount of enzyme that liberates 1 µmol fatty acid per minute from olive-oil emulsion under USP General Chapter <1601> conditions (37°C, pH ~9, specific substrate prep) | Pancreatic enzyme replacement (Creon, Zenpep, Pancreaze) |
| **FIP unit** | Per Fédération Internationale Pharmaceutique standard; substrate, temperature, and pH differ from USP — *not* directly interchangeable. **Approximate empirical conversion: 1 USP lipase unit ≈ 4 FIP lipase units** at standard assay conditions (source: digestive-enzyme-optimization.md §"BoulderBio FIP↔USP conversion") | Microbial-derived OTC digestive enzymes (BoulderBio, Now Foods, Pure Encapsulations) |
| **IU (International Unit)** | Generic enzymology — 1 µmol substrate transformed per minute at specified conditions | Bench enzymology, research literature |
| **U** (Sigma / supplier-specific) | Vendor-defined; always check vendor datasheet for assay conditions before comparing | Commercial assay kits |

Always report the unit + the assay conditions. Cross-vendor comparison without specifying conditions is ~order-of-magnitude meaningful only.

---

## 9. Common pitfalls

1. **No salt-matched control for shio-koji liquid.** 25% NaCl suppresses some enzymes' apparent activity 30–60% at standard assay conditions; without a salt-matched blank, you under-report.
2. **Reading kitchen-tier endpoints by eye.** Operator drift across a single batch is larger than the inter-batch signal; use phone photos at fixed lighting.
3. **Assuming USP and FIP units interconvert linearly across all enzymes.** They don't — the conversion factor is enzyme- and condition-specific. Stay within one unit system per comparison; convert once at the end with a cited conversion factor.
4. **Single-replicate assays.** Lipase assays in particular are noisy (emulsion variability, temperature drift); n=3 minimum, n=9 if it's the first time on a new substrate.
5. **Freeze-thawing extracts.** Koji enzymes lose meaningful activity per freeze-thaw cycle; aliquot before first freeze; assay one aliquot fresh as a baseline.
6. **Ignoring pH-optimum mismatch.** White koji (*A. luchuensis*) acid protease optimum is pH ~3; reporting its activity at pH 7 (the convention for pancreatic protease) under-reports by 2–3-fold. Run at the strain's optimum if measuring intrinsic capacity; run at pH 7 if measuring expected gut-equivalent activity.
7. **Not running a same-day positive control.** Without a reference, a "low" reading is indistinguishable from an instrument or reagent issue. Always include a Sigma standard or a dissolved Creon capsule on every assay day.

---

## 10. Hooks into project work

- **Wild-type batch QC** ([koji-home-fermentation.md](./koji-home-fermentation.md)): Tier 1 amylase + protease batch QC after every Stage 1 harvest answers "did this batch ferment to a normal enzyme load?" before committing the batch to a 7–14 day Stage 2A shio-koji ferment. Lipase Tier 1 informs whether the resulting shio-koji is worth Tier 3 calibration this round.
- **Strain comparison** ([digestive-enzyme-optimization.md §"Yellow vs white vs black"](./digestive-enzyme-optimization.md)): Tier 3 first-run on yellow koji vs. white koji vs. black koji from matched substrate batches converts the published U/g literature into household-equipment-anchored numbers, which then drive the strain choice for ongoing fermentation.
- **GI-survival 2-arm assay** ([validation-experiments.md §1.18](./validation-experiments.md)): the Tier 3 assays specified here are the readouts §1.18 depends on. The §1.18 estimated cost ($300–500) covers the assay reagents under §3 above plus SGF/SIF reagents and Creon control.
- **Engineered platform benchmarking** ([engineered-koji-protocol.md](./engineered-koji-protocol.md)): the Tier 3 wild-type baseline established here is the floor any engineered cassette must outperform. A useful platform metric: *engineered-strain U/g per cassette / wild-type U/g per matched-strain control* — values >2× justify the engineering complexity; <1.5× suggest substrate or condition optimization (already covered in [digestive-enzyme-optimization.md](./digestive-enzyme-optimization.md)) is the cheaper path.
- **n=1 self-experiment integration** ([self-experiment-protocol.md](./self-experiment-protocol.md)): every shio-koji-marinade-day in the PERT-timing experiment can carry a Tier 1 lipase score for the marinade used that day; correlate against GI-tolerance metrics over the experiment window.

---

## 11. Open questions this protocol enables answering

Each of these is currently called out as "lab-measurable but not yet done" in one of the related wiki pages. The methodology above operationalizes them.

1. **What is the per-gram lipase activity of shio-koji from the household's standard fermentation, expressed as percent of one Creon-cap-lipase-equivalent?** Tier 3 first-run. Settles whether shio-koji is a meaningful adjunct (>1%) or trace (<1%).
2. **Does shio-koji-marinade pre-digestion measurably reduce the protease + peptidase load on the gut?** Tier 3 protease assay on marinated vs. unmarinated protein extracts (not the marinade itself — the meat after marinating). Settles whether the "different mechanism" framing in §1 is empirically supported.
3. **What is the GI-survival fraction of native koji enzymes through SGF → SIF, free-extract vs. whole-biomass?** Specified in [validation-experiments.md §1.18](./validation-experiments.md); methodology operationalized here.
4. **Does *A. luchuensis* (white koji) have a meaningfully higher acid-protease yield than *A. oryzae* (yellow koji), and does this matter for shio-koji marinade efficacy at gastric pH?** Tier 3 protease assay at pH 3 vs. pH 7 across matched batches.
5. **What is the freeze-thaw stability of koji-derived lipase / protease / amylase?** Tier 3 across 0, 1, 2, 5, 10 freeze-thaw cycles. Settles freezer-storage strategy for batched shio-koji production.
6. **What is the salt-tolerance curve of native koji enzymes at shio-koji-relevant NaCl concentrations (0–25% w/v)?** Tier 3 across a salt gradient. Informs whether reduced-salt shio-koji variants would deliver meaningfully more enzyme activity to food, or whether the salt concentration is already past the suppression knee.

---

## 12. What this protocol does **not** cover

- **Inhibitor and effector studies** (e.g., the effect of fat in the meal matrix on lipase apparent Km). Out of scope; standard enzyme-kinetics protocols apply if pursued.
- **Identification of which lipase / protease isoforms are active.** Requires SDS-PAGE + zymography or LC-MS proteomics; out of scope for a clinical-comparison protocol.
- **In vivo bioavailability.** This protocol measures activity in vitro; the gut does not behave like a buffered cuvette. The §1.18 SGF → SIF bridge in [validation-experiments.md](./validation-experiments.md) is the closest in-scope proxy.
- **Engineered-strain construct verification.** That work belongs in [engineered-koji-protocol.md](./engineered-koji-protocol.md) and the per-cassette stability pages ([uricase-protease-stability-computational.md](./uricase-protease-stability-computational.md), etc.).
- **Allergenicity, mycotoxin, or contamination assays.** Critical for any downstream consumption claim but out of scope for activity quantification. Standard food-safety panels apply.

---

## 13. Status

Protocol is **drafted, not yet field-tested in this repo's household run.** The first-run Tier 3 calibration is queued; estimated cost ~$200–400 in reagents at a community-college bench, single-day session. Linked to the [Ward 1995 lab-access global landscape](./ward-1995-lab-access-global.md) work — when the §1.9 dual-cassette feasibility-test partner is identified, the Tier 3 first-run is a low-risk warm-up assay that builds the relationship without committing the partner to the engineered work.

(Evidence level for this page: **Mechanistic Extrapolation** for the assay-tier mappings, calibration logic, and interpretive bands. **In Vitro / Methods** for the named canonical assay protocols (Bernfeld 1955, Charney & Tomarelli 1947, Winkler & Stuckmann 1979) and USP unit definitions (General Chapter <1601>). No Clinical Trial or Animal Model claims are made on this page.)
