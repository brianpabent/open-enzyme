---
title: "Zileuton (Zyflo / Zyflo CR)"
date: 2026-05-05
tags: ["zileuton", "zyflo", "5-lox", "ltb4", "asthma", "gout", "cp6a", "repurposing", "pharmaceutical"]
related:
  - nlrp3-exploit-map.md
  - gout-clinical-pipeline.md
  - chembl-cross-check.md
  - supplements-stack.md
  - disulfiram.md
  - cross-validation.md
  - self-experiment-protocol.md
sources:
  - "Israel et al. *Ann Intern Med* 1993;119(11):1059–1066 (PMID 8239225) — zileuton pivotal asthma efficacy"
  - "Liu et al. *Chest* 1996;110(6):1446–1454 (PMID 8969089) — zileuton Phase 3 chronic asthma"
  - "Carter et al. *Drug Saf* 1995;13(1):19–35 — zileuton hepatotoxicity review"
  - "Bell et al. *Allergy Asthma Proc* 2008;29(1):55–65 — Zyflo CR 1,200 mg BID bioequivalence / safety"
  - "Ford-Hutchinson *Crit Rev Immunol* 1990;10(1):1–12 — LTB4 as neutrophil chemoattractant, 100× C5a in some assays"
  - "Rae & Smith *Prostaglandins Leukot Med* 1981;6(1):71–78 (PMID 6259703) — LTB4 in synovial fluid of gout patients"
  - "*J Med Chem* 1991 — quercetin 5-LOX IC50 = 300 nM (ChEMBL v34, cross-check 2026-05-05)"
  - "ClinicalTrials.gov search 2026-05-05 — zero zileuton gout trials registered"
---

# Zileuton (Zyflo / Zyflo CR)

Zileuton is an oral 5-lipoxygenase (5-LOX) inhibitor. FDA-approved for asthma in 1996 and still the only approved direct 5-LOX drug in the US. It is **never been tested in gout** and sits squarely on top of the CP6a chokepoint in the v1.2 [NLRP3 exploit map](./nlrp3-exploit-map.md) — the 5-LOX → LTB4 → neutrophil-chemotaxis amplification loop that drives the tissue-destructive phase of a gout flare. This dossier treats zileuton as a **testable hypothesis**, not an efficacy claim.

**Repurposing surface origin:** Zileuton is one of three concrete examples surfaced by the Open Enzyme discovery engine's chokepoint-to-FDA-drug mapping methodology — FDA-approved drugs that hit a gout chokepoint but were never clinically tested for gout. The other two are disulfiram (CP6b GSDMD, FDA-approved for alcohol use disorder) and avacopan (CP0 C5aR1, FDA-approved for ANCA vasculitis). See [open-enzyme-vision.md §2.2](./open-enzyme-vision.md) for the full repurposing surface framing. (source: open-enzyme-vision.md)

See [supplements-stack.md](./supplements-stack.md) for the over-the-counter CP6a entries (quercetin, AKBA, EPA) that already sit on this mechanism. Zileuton is the pharma-grade version of the same pathway reach.

---

## What it is

- **Chemistry:** N-hydroxy-N-(1-benzo[b]thien-2-ylethyl)urea. Orally bioavailable small molecule, MW 236.29.
- **Mechanism class:** Direct, reversible, iron-chelating 5-LOX inhibitor. Binds the non-heme iron at the active site of the 5-LOX enzyme and prevents arachidonic acid → 5-HPETE → LTA4 conversion. Unlike montelukast (a leukotriene-receptor antagonist acting downstream at CysLT1), zileuton blocks upstream leukotriene synthesis — both the LTB4 branch (neutrophil chemotaxis) and the cysteinyl-leukotriene branch (LTC4/D4/E4, bronchoconstriction).
- **Approval:** FDA-approved 1996 for prophylaxis and chronic treatment of asthma in patients ≥12 years. Zyflo (immediate-release, 600 mg QID) and Zyflo CR (controlled-release, 1,200 mg BID) are bioequivalent for AUC.
- **Sponsor history:** Abbott → Critical Therapeutics → Cornerstone Therapeutics → Chiesi. Now available generic.
- **Cost:** ~$50/month generic as of 2026-05-05 (varies; the brand Zyflo CR remains expensive).
- **Access:** Prescription required; written most often by pulmonologists for asthma. No current rheumatology indication.

---

## Mechanism in gout (CP6a) — our theory

This section frames the case as a testable hypothesis, not an efficacy claim. No gout clinical trial of zileuton exists (ClinicalTrials.gov search 2026-05-05 returns zero results).

1. **MSU crystal deposition activates macrophages and recruits neutrophils**, which synthesize eicosanoids from arachidonic acid via 5-LOX. Synovial fluid from gout patients contains elevated LTB4 during flares (Rae & Smith 1981, PMID 6259703 — In Vitro / ex vivo human).
2. **The primary 5-LOX product relevant to gout is leukotriene B4 (LTB4)** — a potent neutrophil chemoattractant. In some early chemotaxis assays LTB4 was reported as ~100× more active than C5a for neutrophil migration (Ford-Hutchinson *Crit Rev Immunol* 1990 — In Vitro). The quantitative ratio is assay-dependent, but LTB4's status as a dominant neutrophil chemoattractant in tissue-level inflammation is well established.
3. **LTB4 pulls additional neutrophils into the joint,** amplifying the flare. The neutrophil infiltration phase — not the initial macrophage activation — is what produces the clinical pain, swelling, and erosive tissue damage that define a gout attack.
4. **Zileuton blocks 5-LOX directly**, reducing LTB4 (and cysteinyl-leukotriene) production, and should therefore attenuate the neutrophil-amplification loop. This is on-mechanism in asthma; the translation to gout is mechanistically reasonable but has not been clinically tested.
5. **This is CP6a** — a first-class chokepoint in the v1.2 map. See [nlrp3-exploit-map.md § CP6a](./nlrp3-exploit-map.md). Blocking CP6a is orthogonal to CP0 (complement C5a priming), CP1 (NF-κB priming), CP2 (NLRP3 assembly), CP5a (IL-1β receptor blockade), and CP6b (GSDMD pore formation).
6. **Mechanistic parallel to quercetin.** Quercetin's most potent curated ChEMBL bioactivity is 5-LOX IC50 = 300 nM (*J Med Chem* 1991; ChEMBL v34). Zileuton is the pharma-grade version of the same mechanism the stack already tries to reach via quercetin — higher potency, verified oral bioavailability, and dose precedent in humans at 1,200 mg BID for years of continuous dosing.

**Evidence level summary:**
- 5-LOX → LTB4 → neutrophil chemotaxis in gout: In Vitro + ex vivo human (Rae & Smith 1981; Ford-Hutchinson 1990).
- Zileuton blocks 5-LOX at therapeutic oral doses: Clinical Trial (asthma registration, PMID 8239225, PMID 8969089).
- Zileuton reduces gout flare frequency or severity: **No evidence of any level.** Hypothesis only.

---

## What would we want to see (expected outcomes)

Framed as hypothesis-testing, n-of-1 style, on top of a stable allopurinol baseline. Pre-register endpoints before starting.

- **Reduced flare frequency** on allopurinol + zileuton versus allopurinol alone. Primary endpoint: flares/year. This is the cleanest test of whether the neutrophil-amplification loop is rate-limiting in a given patient's gout.
- **Shorter flare duration** when flares do occur. Neutrophil influx is a major determinant of how long a flare persists; cutting the chemotactic signal should compress the tail.
- **Lower peak pain scores** during flares — less neutrophil recruitment should mean less tissue damage and less inflammatory mass.
- **Urinary LTB4 / LTE4 should drop substantially** on zileuton. This is the on-target pharmacodynamic readout, well-established in asthma dose-ranging studies, and it functions as a check that the drug is reaching tissue and engaging 5-LOX. If LTE4 does not drop, the patient is either a non-absorber or non-compliant — investigate before interpreting efficacy.
- **No change in serum uric acid.** Zileuton does not touch CP0 (complement), CP2 (NLRP3 assembly), or upstream purine metabolism. It is **not** a urate-lowering therapy. Keeping allopurinol in the regimen is essential if UA is above target.
- **Secondary: hs-CRP** may decline if sustained 5-LOX block meaningfully reduces chronic low-grade inflammation between flares. Not a primary endpoint — the 5-LOX → hs-CRP link is indirect.

**Null outcome to rule out:** urinary LTE4 drops cleanly on drug (target is engaged) but flare frequency is unchanged. That would imply CP6a is not rate-limiting in this specific patient — complement-C5a priming (CP0) or NLRP3 assembly (CP2) may be the dominant bottleneck instead. A clean null result at CP6a is informative: it points the stack toward CP0/CP2 rather than amplification blockade.

---

## Side effects — honest compare vs. alternatives

All of the below are currently used or plausibly used in gout management. Nothing here is an endorsement of any specific regimen.

- **Zileuton:** Hepatotoxicity is the main concern — boxed warning. ALT/AST elevation in roughly 1–3% of trial subjects, mostly reversible on discontinuation (Carter *Drug Saf* 1995). Nausea and headache are common but usually mild. **Requires baseline + monthly LFTs for the first 3 months, then quarterly.** Pregnancy category C. Contraindicated in active liver disease. Many CYP1A2 drug interactions — notably theophylline and warfarin (dose-adjust).
- **Colchicine:** Diarrhea is dose-limiting; GI upset common. Rare myopathy. Well-established for acute flares and prophylaxis. Cheap. Narrow therapeutic index; cumulative toxicity at high doses. CYP3A4 / P-glycoprotein interactions (statins, macrolides) — several reported deaths from co-administration with clarithromycin in renal insufficiency.
- **Allopurinol:** Hypersensitivity is rare but severe (SJS/TEN, notably in HLA-B*58:01 carriers — test before starting in Asian ancestry patients). Rash. Hepatotoxicity exists but is less common than zileuton's. Renal dose adjustment needed. Gold standard for UA lowering; does **not** address inflammation.
- **Canakinumab (Ilaris):** Injection-site reactions. Infection risk — bacterial pneumonia ~5% of exposed patients in some cohorts. ~$300K/year US list price. Directly neutralizes IL-1β (CP5a). Used off-label for gout until FDA-approved August 2023. Reserved for refractory or contraindicated-to-colchicine cases.
- **NSAIDs (indomethacin, naproxen):** GI ulcers and bleeding. Renal toxicity. Cardiovascular risk (all non-aspirin NSAIDs carry some signal; indomethacin worse than naproxen). First-line for acute flares in patients without contraindications; not appropriate for chronic prevention.
- **Disulfiram (CP6b):** Ethanol intolerance — the disulfiram-ethanol reaction is a major practical issue for any patient who drinks. Hepatotoxicity exists but is less common than zileuton's. ~$30/month. Mechanism (GSDMD pore block) is **orthogonal to zileuton's** (5-LOX block), and the two could in principle be combined for dual CP6 coverage. See [disulfiram.md](./disulfiram.md).

**Takeaway on comparative safety:** zileuton is not the safest option in this list, but it is the only option that hits CP6a directly at pharma-grade potency. Its hepatotoxicity signal is real and needs active monitoring — it's also the reason it has remained niche even in asthma practice since montelukast took over the leukotriene-modifier market. The monitoring is known and cheap (monthly LFT × 3 months); the risk is manageable but not zero.

---

## Where it fits in the stack

Zileuton is a **pharma-grade adjunct** to the CP6a chokepoint, not a replacement for any other chokepoint. The working mental model:

- **Upstream priming (CP0, CP1):** allopurinol (XO block, upstream UA), plus optional adjuncts — EGCG, quercetin, sulforaphane for NF-κB / Nrf2. See [supplements-stack.md](./supplements-stack.md).
- **Assembly (CP2):** BHB, oridonin, dapansutrile (if accessible).
- **Signal 1 scavenging (CP3, CP4):** colchicine (approved, CP3 ASC-speck / microtubule).
- **Downstream (CP5a receptor, CP5b resolution):** anakinra / canakinumab / rilonacept (receptor), EPA → RvE1 / MaR1 for active resolution, lactoferrin as fermentable adjunct.
- **Amplification + Exit (CP6):** **Zileuton (CP6a)** + **disulfiram (CP6b)** together give dual-branch coverage of the neutrophil-amplification-and-pyroptotic-exit chokepoint. Quercetin and AKBA are the supplement-tier options at CP6a.

**Ideal combination** if the goal is maximum chokepoint coverage with the minimum number of moving parts:

> allopurinol (UA lowering) + engineered koji (gut-lumen urate degradation + multi-chokepoint NLRP3 modulation) + zileuton (CP6a LTB4 block) ± disulfiram (CP6b GSDMD block, if ethanol-free lifestyle is acceptable)

The koji intervention is still in Phase 0 — research and design. Zileuton is available today by prescription.

---

## Availability + access

- **Generic, prescription required.** No OTC path. US only — some countries never approved zileuton.
- **Who writes the script:** pulmonology writes it routinely for asthma. Rheumatology and primary care are unlikely to think of it for gout — the CP6a mechanism rationale has to be explicitly pitched. A forward-thinking internist is more likely to engage than a gout-specialist rheumatologist; gout rheumatology is heavily anchored on urate-lowering + colchicine + IL-1 biologics, and 5-LOX is not part of the standard framework.
- **Monitoring logistics:** baseline ALT/AST, then monthly × 3 months, then quarterly. Cheap lab — same panel most patients get anyway. Requires discipline, not expertise.
- **Cost:** ~$50/month generic as of 2026-05-05. Brand Zyflo CR is substantially more expensive; insurance coverage variable (it's an asthma drug, not a gout drug — off-label billing may be required).

---

## Open questions

1. **Has zileuton ever been tested in gout clinically?** ClinicalTrials.gov search 2026-05-05: **zero gout trials.** PubMed search (2026-05-05): no gout-specific efficacy publications. The two PubMed hits for "zileuton + gout/uric acid" are incidental (PMID 34723750 — ESRD metabolomics paper mentioning zileuton-O-glucuronide as a biomarker; PMID 29727733 — Sri Lankan medicinal plant 5-LOX assay using zileuton as a positive control). Refreshed via the 2026-05-05 Paperclip-equivalent audit. This is a complete pipeline gap, not a "buried negative result" problem.
2. **Does it abort acute flares or only reduce frequency?** 5-LOX block is continuous — the drug has a short half-life (~2.5 hours for immediate-release, longer for CR) but its effect on leukotriene synthesis is ongoing while circulating. Unlike colchicine, zileuton probably cannot "rescue" an in-progress flare the way microtubule disruption can; the amplification loop has already delivered most of its neutrophils by the time pain peaks. Best use case is chronic prophylaxis, not acute rescue.
3. **Are there published case reports of asthma patients with incidental gout who responded to zileuton?** This is a natural population to survey — any pulmonology clinic with a zileuton-prescribing practice has a few dozen patients who also have gout. Retrospective chart review of flare frequency before/after zileuton start is cheap and could generate signal. **No such study has been published as of 2026-05-05** (re-confirmed via PubMed full-text + bioRxiv audit; the existence-search question is closed in the negative — the gap is real, not a "buried negative result" problem).
4. **Does 5-LOX block synergize with NLRP3 block, or show a ceiling effect?** CP2 (NLRP3 assembly) and CP6a (LTB4 amplification) are mechanistically different. The prediction is additive, but a plateau is plausible if one branch is already rate-limiting. A quercetin + BHB combination in a MSU-mouse model would be the cheapest first test of the synergy question.
5. **Is urinary LTE4 a reliable biomarker to titrate zileuton dose in gout?** In asthma, urinary LTE4 is the standard PD readout for leukotriene-modifier drugs. Its use in gout patients has not been validated — baseline LTE4 and response curves may differ. Worth including as a secondary endpoint in any n-of-1 protocol.

---

## Related

- [NLRP3 Exploit Map](./nlrp3-exploit-map.md) — CP6a is defined here, v1.2.
- [Gout Clinical Pipeline](./gout-clinical-pipeline.md) — zileuton is flagged as a latent CP6a repurposing candidate.
- [ChEMBL Cross-Check](./chembl-cross-check.md) — quercetin 5-LOX = 300 nM, the finding that first surfaced CP6a as a first-class branch.
- [Supplements Stack](./supplements-stack.md) — quercetin, AKBA, EPA are the OTC CP6a entries.
- [Disulfiram](./disulfiram.md) — companion pharma drug at CP6b (GSDMD).
- [Cross-Validation](./cross-validation.md) — methodology for integrating in vitro and clinical evidence.
- [Self-Experiment Protocol](./self-experiment-protocol.md) — safety framework and endpoint design for n-of-1 evaluations.

---

*Last updated: May 2026. This is a research hypothesis dossier, not medical advice. Zileuton has not been tested in gout; the CP6a mechanism case is real but unvalidated clinically.*
