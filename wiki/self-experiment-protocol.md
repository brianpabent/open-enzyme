---
title: "N-of-1 Research Design and Safety Monitoring"
date: 2026-04-25
tags: ["n-of-1", "study-design", "safety", "monitoring", "falsification"]
related:
  - cross-validation.md
  - validation-experiments.md
  - genotype-informed-supplement-workflow.md
sources:
  - "n-of-1 trial methodology (e.g., Kravitz & Duan, Ann Intern Med 2014)"
---

# N-of-1 Research Design and Safety Monitoring

This page defines a generic framework for prospectively measuring a single-subject intervention. It is a method for generating feasibility signals and identifying confounders; it does not establish efficacy, prescribe treatment, or justify exposing a person to an unvalidated compound, engineered organism, off-label drug, or combination.

The framework's evidence level is **Mechanistic Extrapolation** from standard clinical-monitoring and n-of-1 methods. Clinical decisions, prescription changes, acute-flare care, and abnormal results require qualified medical oversight.

## 1. Appropriate scope

An n-of-1 design is useful when:

- the intervention and exposure are already sufficiently characterized for the proposed context;
- the primary outcome can change within a practical observation window;
- baseline care can remain stable;
- safety monitoring and halt criteria are defined before exposure; and
- a single-subject result is explicitly treated as non-generalizable.

It is not an authorization path for experimental biologics, engineered strains, unapproved delivery systems, or medication changes. Those require their own preclinical, regulatory, and clinical gates.

## 2. Prespecify the experiment

Define these fields before collecting outcome data:

| Element | Required question |
|---|---|
| **Hypothesis** | What mechanism predicts the outcome, and what result would falsify it? |
| **Intervention** | What source, form, route, exposure, and timing are being studied? |
| **Comparator** | Baseline, withdrawal, crossover, matched control, or another appropriate condition? |
| **Primary outcome** | Which single measure decides the result? |
| **Secondary outcomes** | Which measures explain mechanism, adherence, or safety without changing the primary decision? |
| **Cadence** | When should exposure, target engagement, outcome, and safety be measured? |
| **Confounders** | Which diet, medication, sleep, training, infection, or behavior changes must remain stable or be logged? |
| **Halt criteria** | What result stops exposure and triggers clinical review? |
| **Decision rule** | What result means pass, revise, null, or stop? |

A retrospective hypothesis is not prospective evidence. If multiple variables change together, interpret the result as a confounded observation rather than attributing it to one arm.

## 3. Match cadence to mechanism

| Mechanism class | Typical observation window |
|---|---|
| Drug at steady state | 4–6 weeks after a change |
| Stored vitamin or mineral correction | 8–12 weeks |
| Antibody-mediated effect | 3–6 months |
| Microbiota-mediated intervention | 6–8 weeks |
| Acute pharmacodynamic effect | Hours to days |
| Tissue-level adaptation | Weeks to months |
| Long-latency risk modification | Annual or longer; surrogate markers may be more frequent |

Use the longer of the intervention's equilibration time and the outcome's response time. Add earlier safety measurements when the risk profile requires them.

## 4. Measurement hierarchy

Every experiment should distinguish four layers:

1. **Input identity and potency** — what was actually delivered?
2. **Exposure** — did the relevant compartment receive it?
3. **Target engagement** — did the proposed mechanism change?
4. **Outcome** — did the prespecified clinical or biological measure change?

A negative outcome with unverified input or exposure does not falsify the mechanism. A biomarker change without a matched outcome does not establish benefit.

Common safety measurements include CBC with differential, CMP, and hs-CRP where relevant. Additional tests should follow the intervention's known risk surface rather than a universal stack panel.

## 5. Gout and NLRP3 measurement map

These markers can help localize a signal, but none independently selects a compound or treatment.

| Marker | Research axis | Interpretation limits |
|---|---|---|
| Serum C5a (+ desArg) | CP0 complement priming | Strict pre-analytics: cold-chain EDTA, processing within 30 minutes, and frozen storage are required because warm transit can generate C5a in vitro. Onset and resolution measurements can estimate a decline slope, but the slope remains a mechanistic hypothesis. |
| Urinary LTE4 | CP6a leukotriene flux | A pharmacodynamic readout for 5-LOX engagement; it does not by itself establish flare benefit or identify why exposure failed. |
| Plasma SPMs (RvD1, MaR1) | CP5b active resolution | Research-grade LC-MS/MS; low values can reflect substrate, conversion, timing, or analytical limitations. |
| hs-CRP | Integrated systemic inflammation | Non-specific; cannot identify a chokepoint without mechanism-specific measurements. |
| Serum urate | Urate balance | Does not distinguish production, renal handling, intestinal export, or luminal degradation without additional measurements. |

Optional genotype stratification such as CFH Y402H or ABCG2 Q141K must be prespecified. A genotype association does not establish a carrier-specific intervention response.

## 6. Home and laboratory formats

| Marker | Lower-friction format | Reference format | Method note |
|---|---|---|---|
| Serum urate | Capillary UA meter | Venous serum UA | Pair the meter with a venous draw to estimate device-specific offset; emphasize within-device change. |
| Omega-3 index | Mail-in dried-blood spot | Venous RBC fatty-acid profile | Event-linked sampling is feasible; use the same format across comparisons. |
| Genotype | Existing array data or single-SNP assay | Clinical PCR | One-time measurement; trial-grade stratification requires an appropriate-quality assay. |
| C5a | None | Specialty venous assay | Pre-analytical handling is load-bearing. |
| Urinary LTE4 | Specialty urine collection | Specialty laboratory | Not a routine home test. |
| Plasma SPMs | None | Research LC-MS/MS | Limited availability and timing sensitivity. |
| hs-CRP | Some home immunoassays | Venous hs-CRP | Venous measurement is preferred for low-range interpretation. |

Use lower-friction formats for trajectory sampling only when analytically fit. Use reference methods for calibration anchors and decisions that require clinical-grade accuracy.

## 7. Daily outcome and confounder log

Keep entries brief enough to complete every day:

- timestamp and adherence;
- primary outcome on a fixed scale;
- relevant symptoms using the same scale throughout;
- medication, diet, alcohol, sleep, training, infection, and travel deviations;
- adverse events; and
- a free-text field for unexpected signals.

Examples include 0–10 severity scales, the Bristol Stool Scale, joint circumference, or a binary event count. Choose the measure before the experiment and do not redefine success after seeing the data.

## 8. Safety and halt criteria

The following existing project thresholds are conservative research triggers, not a substitute for clinical judgment:

1. New GI bleeding — halt and seek same-day care.
2. ALT or AST above 2× the upper limit of normal — halt and obtain clinical review.
3. eGFR decline above 15% from baseline or a creatinine rise — halt and evaluate.
4. New rash, urticaria, angioedema, or anaphylaxis — halt immediately; airway symptoms require urgent care.
5. Unexplained weight loss above 5 lb over four weeks — halt and evaluate.
6. New unexplained fever — halt and seek care.
7. hs-CRP doubling from baseline — halt and confirm with clinical review.
8. Persistent diarrhea over 72 hours — halt and evaluate for infection or dysbiosis.
9. Any new severe symptom absent at baseline — halt and evaluate.

Define additional intervention-specific criteria before exposure. “Halt” applies to the investigational intervention; prescribed therapy should not be stopped without the responsible clinician unless emergency guidance requires it.

## 9. Privacy and consent

Raw laboratory results, daily logs, intervention plans, and identifiable health information do not belong in the public repository. Store them in a private repository, encrypted volume, or other controlled location with appropriate backup.

Data about another person requires their documented agreement. Public summaries must be de-identified and should report study design, deviations, qualitative outcome direction, and limitations without exposing raw personal health data.

## 10. Interpretation

Classify the result using the prespecified chain:

- **Input failure** — identity or potency was not as specified.
- **Exposure failure** — the intended compartment did not receive the intervention.
- **Target-engagement failure** — exposure occurred but the proposed mechanism did not move.
- **Outcome null** — target engagement occurred without the primary outcome.
- **Safety stop** — adverse findings prevent interpretation or further exposure.
- **Feasibility signal** — exposure, target engagement, and outcome moved in the predicted direction, subject to n=1 limitations.

An n=1 feasibility signal can motivate a controlled study. It cannot establish population efficacy, comparative effectiveness, a personalized treatment rule, or a dose recommendation.

## 11. Worked design patterns

### Timing or formulation comparison

Use a characterized intervention, keep total exposure constant, randomize or alternate timing/formulation conditions where practical, and measure a short-latency outcome. A prior fungal-enzyme timing observation across approximately 30 meals illustrates how meal composition and lying flat after meals can emerge as confounders. The observation was single-subject, unblinded, and uncontrolled; it informs formal study design but does not establish a dosing framework.

### Biomarker-linked mechanism study

For a candidate transporter or inflammasome mechanism, pair the clinical outcome with input verification, exposure, and a direct functional readout. For example, stool SCFAs alone are an exposure proxy and cannot establish epithelial ABCG2 trafficking or urate flux.

### Ex vivo challenge

An ex vivo MSU challenge can measure within-subject IL-1β response under prespecified biological strata. It remains a subject-specific feasibility signal and cannot replace the tiered cell, organoid, or animal experiments in [validation-experiments.md](./validation-experiments.md).

## 12. Related methods

- [Genotype-informed intervention research workflow](./genotype-informed-supplement-workflow.md)
- [Validation experiments](./validation-experiments.md)
- [Quantification ladder](./quantification-ladder.md)
- [Cross-validation](./cross-validation.md)
