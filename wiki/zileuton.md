---
title: "Zileuton (Zyflo / Zyflo CR)"
date: 2026-05-05
tags: ["zileuton", "zyflo", "5-lox", "ltb4", "asthma", "gout", "cp6a", "repurposing", "pharmaceutical"]
related:
  - nlrp3-exploit-map.md
  - gout-clinical-pipeline.md
  - etc/chembl-cross-check.md
  - supplements-stack.md
  - disulfiram.md
  - cross-validation.md
  - self-experiment-protocol.md
sources:
  - "Israel et al. *Ann Intern Med* 1993;119(11):1059–1066 (PMID 8239223) — zileuton pivotal asthma efficacy"
  - "Carter et al. *Drug Saf* 1995;13(1):19–35 — zileuton hepatotoxicity review"
  - "Bell et al. *Allergy Asthma Proc* 2008;29(1):55–65 — Zyflo CR 1,200 mg BID bioequivalence / safety"
  - "Ford-Hutchinson *Crit Rev Immunol* 1990;10(1):1–12 — LTB4 as neutrophil chemoattractant, 100× C5a in some assays"
  - "Rae & Smith *Prostaglandins Leukot Med* 1981;6(1):71–78 — LTB4 in synovial fluid of gout patients (citation present in zileuton review literature; PMID could not be confirmed via direct PubMed search 2026-05-15 — treat as uncorroborated until full-text obtained)"
  - "*J Med Chem* 1991 — quercetin 5-LOX IC50 = 300 nM (ChEMBL v34, cross-check 2026-05-05)"
  - "ClinicalTrials.gov search 2026-05-05 — zero zileuton gout trials registered"
  - "Watkins et al., Drug Safety 2007;30(9):805-815 (PMID 17722971) — zileuton hepatotoxicity surveillance, n=2,458; 4.4% ALT ≥3x ULN, zero ALF"
  - "Luo et al. *Rheumatology* 2019 (PMID 30247644) — metabolic profiling of 5-LOX activation in human acute gout; explicitly states '5-lipoxygenase inhibition may be of therapeutic value clinically'"
  - "Amaral et al., Arthritis & Rheumatism 2012 — LTB4/BLT1/NLRP3/IL-1β in murine MSU-crystal gout"
  - "Awni et al. 1995 (PMID 8620667) — zileuton + naproxen PK: no clinically significant interaction"
  - "DailyMed zileuton ER FDA label — prednisone interaction formally studied, negative; zileuton-colchicine no documented interaction"
---

# Zileuton (Zyflo / Zyflo CR)

Zileuton is an oral 5-lipoxygenase (5-LOX) inhibitor approved for asthma. Its gout-relevant hypothesis is direct blockade of the 5-LOX → LTB4 → neutrophil-chemotaxis amplification loop at CP6a. Zileuton has never been tested in gout, so this is a repurposing experiment rather than an efficacy claim.

See [supplements-stack.md](./supplements-stack.md) for other compounds proposed to reach CP6a.

---

## What it is

- **Chemistry:** N-hydroxy-N-(1-benzo[b]thien-2-ylethyl)urea. Orally bioavailable small molecule, MW 236.29.
- **Mechanism class:** Direct, reversible, iron-chelating 5-LOX inhibitor. Binds the non-heme iron at the active site of the 5-LOX enzyme and prevents arachidonic acid → 5-HPETE → LTA4 conversion. Unlike montelukast (a leukotriene-receptor antagonist acting downstream at CysLT1), zileuton blocks upstream leukotriene synthesis — both the LTB4 branch (neutrophil chemotaxis) and the cysteinyl-leukotriene branch (LTC4/D4/E4, bronchoconstriction).
- **Approval:** FDA-approved 1996 for prophylaxis and chronic treatment of asthma in patients ≥12 years. Zyflo (immediate-release, 600 mg QID) and Zyflo CR (controlled-release, 1,200 mg BID) are bioequivalent for AUC.
- **Access:** Prescription required; written most often by pulmonologists for asthma. No current rheumatology indication.

---

## Mechanistic hypothesis in gout (CP6a)

This section frames the case as a testable hypothesis, not an efficacy claim. No gout clinical trial of zileuton exists (ClinicalTrials.gov search 2026-05-05 returns zero results).

1. **MSU crystal deposition activates macrophages and recruits neutrophils**, which synthesize eicosanoids from arachidonic acid via 5-LOX. Synovial fluid from gout patients contains elevated LTB4 during flares (Rae & Smith *Prostaglandins Leukot Med* 1981;6(1):71-78 — In Vitro / ex vivo human; PMID not confirmed via direct PubMed search, treat as uncorroborated until full-text obtained). The same finding is independently confirmed by Luo et al. 2019 (PMID 30247644) — metabolic profiling of n=26 + n=20 acute gout patients showed plasma LTB4 elevation driven primarily by 5-LOX activation in uric-acid-stimulated neutrophils, dose- and time-dependent (Human observational).
2. **The primary 5-LOX product relevant to gout is leukotriene B4 (LTB4)** — a potent neutrophil chemoattractant. In some early chemotaxis assays LTB4 was reported as ~100× more active than C5a for neutrophil migration (Ford-Hutchinson *Crit Rev Immunol* 1990 — In Vitro). The quantitative ratio is assay-dependent, but LTB4's status as a dominant neutrophil chemoattractant in tissue-level inflammation is well established.
3. **LTB4 pulls additional neutrophils into the joint,** amplifying the flare. The neutrophil infiltration phase — not the initial macrophage activation — is what produces the clinical pain, swelling, and erosive tissue damage that define a gout attack.
4. **Zileuton blocks 5-LOX directly**, reducing LTB4 (and cysteinyl-leukotriene) production, and should therefore attenuate the neutrophil-amplification loop. This is on-mechanism in asthma; the translation to gout is mechanistically reasonable but has not been clinically tested.
5. **This is CP6a** — a first-class chokepoint in the v1.2 map. See [nlrp3-exploit-map.md § CP6a](./nlrp3-exploit-map.md). Blocking CP6a is orthogonal to CP0 (complement C5a priming), CP1 (NF-κB priming), CP2 (NLRP3 assembly), CP5a (IL-1β receptor blockade), and CP6b (GSDMD pore formation).
6. **Mechanistic parallel to quercetin.** Quercetin's most potent curated ChEMBL bioactivity is 5-LOX IC50 = 300 nM (*J Med Chem* 1991; ChEMBL v34). Zileuton reaches the same enzyme through an approved small-molecule route with established asthma pharmacology.

**Evidence level summary:**
- 5-LOX → LTB4 → neutrophil chemotaxis in gout: In Vitro + ex vivo human (Rae & Smith 1981; Ford-Hutchinson 1990).
- Metabolic profiling of human acute gout patients confirms elevated plasma LTB4 is primarily driven by 5-LOX activation in uric-acid-stimulated neutrophils, dose- and time-dependent; same paper states "5-lipoxygenase inhibition may be of therapeutic value clinically." (Human observational — Luo et al. *Rheumatology* 2019, PMID 30247644)
- LTB4 via BLT1 receptor was *necessary* for NLRP3 inflammasome activation and caspase-1-dependent IL-1β production in murine MSU-crystal gout. LTB4 drives MSU-induced ROS → NLRP3 → neutrophil influx cascade. (Animal Model — Amaral et al., Arthritis & Rheumatism 2012)
- Zileuton achieves dose-dependent inhibition of urinary LTE4 in mild-to-moderate asthma at 1.6–2.4 g/d (39.2 pg/mg creatinine reduction at 2.4 g/d, p=0.007 vs placebo) with significant FEV1 improvement (Israel et al. *Ann Intern Med* 1993, PMID 8239223 — the pivotal asthma efficacy trial; n=139, 4-week double-blind RCT). (Clinical Trial — asthma registration PD data)
- Zileuton reduces gout flare frequency or severity: **No evidence of any level.** Hypothesis only.

---

## Falsification tests

- **Target engagement:** urinary LTB4 / LTE4 should fall with exposure, as in asthma dose-ranging studies. Without that change, a gout efficacy result cannot test the CP6a hypothesis cleanly.
- **Disease effect:** with urate lowering held stable, compare flare frequency, duration, pain, and neutrophil influx between zileuton and control.
- **Mechanistic specificity:** serum urate should not change if the effect is confined to 5-LOX amplification rather than urate production or transport.

**Null outcome to rule out:** urinary LTE4 drops cleanly on drug (target is engaged) but flare frequency is unchanged. That would imply CP6a is not rate-limiting in this specific patient — complement-C5a priming (CP0) or NLRP3 assembly (CP2) may be the dominant bottleneck instead. A clean null result at CP6a is informative: it points the stack toward CP0/CP2 rather than amplification blockade.

---

## Exposure and safety constraints

All of the below are currently used or plausibly used in gout management. Nothing here is an endorsement of any specific regimen.

- **Zileuton:** Hepatotoxicity is the main concern. Watkins et al. 2007 (PMID 17722971; n=2,458 prospective open-label safety surveillance) reported ALT ≥3× ULN in 4.4% versus 1.0% in controls and ALT ≥8× ULN in 1.3%. Most elevations occurred within the first three months. The [FDA label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2018/022052s014lbl.pdf) requires hepatic-enzyme assessment before treatment, monthly for the first three months, every 2–3 months for the rest of the first year, and periodically thereafter; it contraindicates use in active liver disease or persistent enzymes ≥3× ULN. CYP1A2 interactions include theophylline and warfarin. Naproxen and prednisone interaction studies were negative; no zileuton–colchicine interaction is documented.
- **Colchicine:** Diarrhea is dose-limiting; GI upset common. Rare myopathy. Well-established for acute flares and prophylaxis. Cheap. Narrow therapeutic index; cumulative toxicity at high doses. CYP3A4 / P-glycoprotein interactions (statins, macrolides) — several reported deaths from co-administration with clarithromycin in renal insufficiency.
- **Allopurinol:** Hypersensitivity is rare but severe (SJS/TEN, notably in HLA-B*58:01 carriers — test before starting in Asian ancestry patients). Rash. Hepatotoxicity exists but is less common than zileuton's. Renal dose adjustment needed. Gold standard for UA lowering; does **not** address inflammation.
- **Canakinumab (Ilaris):** Injection-site reactions. Infection risk — bacterial pneumonia ~5% of exposed patients in some cohorts. ~$300K/year US list price. Directly neutralizes IL-1β (CP5a). Used off-label for gout until FDA-approved August 2023. Reserved for refractory or contraindicated-to-colchicine cases.
- **NSAIDs (indomethacin, naproxen):** GI ulcers and bleeding. Renal toxicity. Cardiovascular risk (all non-aspirin NSAIDs carry some signal; indomethacin worse than naproxen). First-line for acute flares in patients without contraindications; not appropriate for chronic prevention.
- **Disulfiram (CP6b):** Ethanol intolerance — the disulfiram-ethanol reaction is a major practical issue for any patient who drinks. Hepatotoxicity exists but is less common than zileuton's. ~$30/month. Mechanism (GSDMD pore block) is **orthogonal to zileuton's** (5-LOX block), and the two could in principle be combined for dual CP6 coverage. See [disulfiram.md](./disulfiram.md).

Comparisons with standard gout therapies do not establish a preferred regimen. Zileuton's distinguishing feature is direct CP6a target engagement; its distinguishing constraint is the liver-safety burden.

---

## Source, formulation, and access

- **Generic, prescription required.** No OTC path. US only — some countries never approved zileuton.
- **Approved formulations:** immediate-release and controlled-release oral products have established asthma pharmacokinetics.
- **Compounded formulation:** A lower-dose extended-release formulation is an untested delivery hypothesis. Bulk API availability, release kinetics, target engagement, and liver safety all require verification.

---

## Open questions

1. **Has zileuton ever been tested in gout clinically?** ClinicalTrials.gov and PubMed searches found no gout-specific efficacy study. The available hits are incidental rather than clinical tests.
2. **Does timing change the effect?** The amplification loop may be more tractable before peak neutrophil recruitment than after it. Acute and prophylactic study designs should therefore be tested separately rather than assuming one indication.
3. **Are there published case reports of asthma patients with incidental gout who responded to zileuton?** This is a natural population to survey — any pulmonology clinic with a zileuton-prescribing practice has a few dozen patients who also have gout. Retrospective chart review of flare frequency before/after zileuton start is cheap and could generate signal. **No such study has been published as of 2026-05-05** (re-confirmed via PubMed full-text + bioRxiv audit; the existence-search question is closed in the negative — the gap is real, not a "buried negative result" problem).
4. **Does 5-LOX block synergize with NLRP3 block, or show a ceiling effect?** CP2 (NLRP3 assembly) and CP6a (LTB4 amplification) are mechanistically different. The prediction is additive, but a plateau is plausible if one branch is already rate-limiting. A quercetin + BHB combination in a MSU-mouse model would be the cheapest first test of the synergy question.
5. **Is urinary LTE4 a reliable gout pharmacodynamic marker?** It is used in asthma but has not been validated in gout; baseline and response curves may differ.

---

## Related

- [NLRP3 Exploit Map](./nlrp3-exploit-map.md) — CP6a is defined here, v1.2.
- [Gout Clinical Pipeline](./gout-clinical-pipeline.md) — zileuton is flagged as a latent CP6a repurposing candidate.
- [ChEMBL Cross-Check](./etc/chembl-cross-check.md) — quercetin 5-LOX comparative activity.
- [Supplements Stack](./supplements-stack.md) — quercetin, AKBA, EPA are the OTC CP6a entries.
- [Disulfiram](./disulfiram.md) — companion pharma drug at CP6b (GSDMD).
- [Cross-Validation](./cross-validation.md) — methodology for integrating in vitro and clinical evidence.
- [Self-Experiment Protocol](./self-experiment-protocol.md) — safety framework and endpoint design for n-of-1 evaluations.

---

*Research hypothesis, not medical advice. Zileuton has not been tested in gout.*
