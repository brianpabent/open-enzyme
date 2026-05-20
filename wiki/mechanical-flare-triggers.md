---
title: Mechanical Flare Triggers — Open Questions
date: 2026-05-20
tags: [gout, flare-triggers, biomechanics, open-questions, methodology, nlrp3]
related:
  - gout-deep-dive.md
  - nlrp3-inflammasome.md
  - nlrp3-exploit-map.md
status: open-question
---

# Mechanical Flare Triggers — Open Questions

**Status: open question. This page does not advance a confident claim. It enumerates a research gap.**

The gout literature extensively characterizes (a) hyperuricemia → MSU crystal formation and (b) MSU crystals → NLRP3 inflammasome → IL-1β → acute flare. The middle step — *what triggers an already-deposited subclinical crystal bed to become inflammatory on a given day* — is poorly characterized for the mechanical-use axis specifically. The strongest primary in vitro source on mechanical effects on MSU crystallization is from 1975 (Wilcox & Khalaf). The clinical evidence is mixed, with structural methodology limitations that may bias the field's reading. The mechanism is biologically coherent. None of it is settled.

This page maps what is known, what is unknown, why the unknown is hard to study, and what experiments would close the gap.

## The candidate mechanism (sketched, not established)

Subclinical MSU deposits accumulate in cartilage, synovium, and tendon sheaths in hyperuricemic individuals years before any clinical flare. Dual-energy CT and ultrasound (double-contour sign) show this in many asymptomatic patients. The standing question is not when crystals form, but what makes today the flare day.

A mechanically-mediated trigger axis would look like this:

1. **Crystal shedding under load.** Shear, impact, or repeated load on a joint physically dislodges MSU crystals from synovial surfaces, cartilage, or small tophi into the synovial space. *Mechanistic extrapolation. See open question 1 — no direct in vitro experiment combines MSU-laden cartilage with cyclic load and a free-crystal supernatant readout.*

2. **Mechanotransduction priming.** Compression activates Piezo1 in chondrocytes / synoviocytes → NF-κB → pro-IL-1β + NLRP3 transcription (signal 1 of the two-signal NLRP3 model). *In Vitro + Animal Model in osteoarthritis contexts. Not directly tested in gout / MSU contexts. Counterevidenced by Bougault 2012, which showed NLRP3-knockout cartilage explants still exhibit load-induced matrix breakdown — so the Piezo1 → NLRP3 story is not universal.*

3. **DAMP release from microtrauma.** Mechanical injury releases ATP, HMGB1, and free uric acid from damaged cells, providing additional priming signals to local macrophages. *Mechanistic extrapolation from general DAMP biology; not specifically tested in a gout context.*

4. **Overnight effusion concentration.** Mechanical priming occurs during the day; Simkin's model of overnight synovial-effusion resolution (water leaves the joint faster than urate during sleep) concentrates the primed synovium → transient supersaturation → crystallization or amplified inflammasome activation manifesting on waking. *Hypothetical synthesis of Simkin's overnight-effusion model + mechanical priming. Not directly tested.*

5. **Metabolic overload via exertion / fatigue (劳累).** Sustained exertion or fatigue depletes systemic urate-handling capacity, proposed mechanism: organ-function fatigue → impaired urate excretion → transient hyperuricemia → crystal nucleation or local supersaturation. *Mechanistic framing surfaced from TCM 痹证 (Bi-syndrome) chapter (中医内科学); **empirically the strongest of the activity-related candidates**, with Li XD et al. 2012 (n=1,713, Shandong Medical Journal, verified primary) showing **劳累 (fatigue/overwork) at 19.3% — the most common identifiable trigger after diet and alcohol**, vs pure trauma (外伤) at only 0.35%. The empirical asymmetry between 劳累 (19%) and 外伤 (0.35%) in the same primary cohort argues that whatever is happening with activity-preceded flares is more likely fatigue/metabolic-mediated than mechanical-impact-mediated. **Distinct from the mechanical-shedding hypothesis but compatible with it** — both mechanisms could contribute. The modern-physiology testable equivalent: does sustained exertion measurably impair renal urate clearance in gout patients during/after activity, on a timescale that matches the flare-onset window?*

The five components are individually plausible. Their relative contribution is now partially constrained by the Li XD 2012 primary data: the empirical weight in self-reported activity-preceded flares points toward #5 (metabolic-overload) over #1 (mechanical shedding) — but neither is directly mechanistically tested at the kinetic level.

## What the population evidence does — and does not — show

| Finding | Source | Reading |
|---|---|---|
| 4.9% of patients attribute most-recent flare to "injury or excess activity"; 6.9% to "more than usual physical activity"; 62.6% report no identifiable trigger | Abhishek 2017 (n=550; PMC5638318) **Clinical / cross-sectional** | Low self-reported attribution — but see structural blind spot below |
| Nocturnal flare onset OR 2.36 (midnight–8 AM vs 8 AM–4 PM) | Choi 2015 (n=724, 1433 flares; PMC4360969) **Clinical / case-crossover** | Most flares manifest overnight, when no one is actively loading any joint |
| Post-spine-surgery flare rate 43.8%, predictors are Hb drop / smoking / ULT discontinuation; flares hit knee (66%) and ankle (51%), 0% at the operated spine | Chen K-J 2022 (n=128; PMC9267449) **Clinical / retrospective** | Post-op flares are systemic-perturbation-driven, not mechanical-at-the-operated-joint |
| Chronic physical activity reduces flare frequency; TLR2 downregulation on neutrophils | Jablonski 2020 (PMC7529261) **Animal Model + Clinical observational** | Regular activity is anti-inflammatory in gout, not provocative |
| Cyclic compression of cartilage explants drives matrix breakdown independent of NLRP3 / IL-1RI | Bougault 2012 (PMID 22933232) **Animal Model + In Vitro** | The Piezo1/NLRP3 mechanotransduction story is not universal — load-induced cartilage damage has NLRP3-independent paths |
| Mechanical shock accelerates MSU nucleation in vitro | Wilcox & Khalaf 1975 (PMID 242279) **In Vitro** | Foundational primary source — still the best the field has on this specific question, fifty years later |
| Arthroscopic debridement of gouty knees → 10% acute flare within 48h | Ma W-J 2024 (PMID 39104066; Chinese) **Clinical / retrospective n=235** | Direct intraoperative mechanical disruption of a deposited crystal bed does precipitate flares — the closest available clinical analog to a clean mechanical-trigger event |
| Trigger frequencies in n=1,713 Qingdao acute-flare cohort: 高嘌呤饮食 (high-purine diet) 839 (49.0%); 饮酒 (alcohol) 768 (44.8%); 无明显诱因 (no identifiable trigger) 410 (23.9%); **劳累 (fatigue/overwork) 330 (19.3%)**; 受寒 (cold exposure) 142 (8.3%); 高脂饮食 (high-fat diet) 101 (5.9%); 情绪波动 (emotional fluctuation) 56 (3.3%); **外伤及感染 (trauma + infection, grouped) 6 (0.35%)**. Gender ranking (among identifiable triggers): males — high-purine diet / alcohol / **劳累**; females — high-purine diet / **劳累** / cold exposure | Li XD, Miao ZM, Liu YH, Cheng XY, Liu L, Li CG. 2012. 山东医药 (*Shandong Medical Journal*). **Clinical / case-series, n=1,713.** **Primary abstract verified via cqvip 2026-05-20.** Translation cross-check on key category: 劳累 = {Model A: "fatigue/overwork — broad, includes physical exertion + mental exhaustion + sleep deprivation" \| Model B: "physical tiredness from sustained activity"} — agreement that 劳累 is broader than English "strenuous exercise"; primary paper does NOT break out exercise specifically | **Two corrections to the prior secondary-citation summary**: (1) the category is 劳累 (fatigue/overwork), NOT 剧烈运动 (strenuous exercise) — semantically important because 劳累 maps to candidate mechanism #5 (metabolic-overload), not to mechanical-shedding. (2) Gender ranking was wrong in secondaries: 劳累 is **#3 in males but #2 in females**, not #3 in both. **Substantive finding**: pure trauma (外伤) was only 0.35% — even rarer than Abhishek 2017's 4.9% Western self-attribution. The Chinese primary data REINFORCES that pure mechanical impact is rarely the self-reported proximal trigger, but the broader fatigue/overwork category (19.3%) is substantially higher than any Western category. Supports candidate mechanism #5 (metabolic overload) over candidates #1-4 (mechanical) |

Taken at face value, the population data argues *against* mechanical use being a dominant flare trigger. The next section names a structural limitation in the methodology behind several of these findings that the face-value reading does not weigh.

## A limitation in the trigger-attribution methodology — documented across two designs

Two trigger-study designs were instrument-checked for this page. Both have known structural limitations on detecting habitual-activity inputs, via different mechanisms.

**Design 1 — Deviation-framed self-report (Abhishek 2017; instrument confirmed via Methods section).** Two-arm questionnaire:

1. *An open-ended question* — "identify all factors that triggered their acute gout attacks" — allowing spontaneous reporting.
2. *Pre-specified checklist items framed as deviations from baseline* — "undertaking *more than usual* physical activity," "*greater than usual* intake of red-meats," "drinking *less than usual* non-alcoholic liquids" — over the 1–2 days preceding the most-recent flare.

Each arm has a different relationship to habitual-activity triggers:

- The **deviation-framed checklist items** explicitly ask about acute change. A patient with a stable daily activity pattern would honestly answer "no" to "more than usual physical activity" even if their daily activity is a contributing input. This arm is, by construction, biased toward detecting acute perturbations rather than chronic exposures.
- The **open-ended question** does not structurally exclude habitual inputs — a patient could volunteer "my daily run" spontaneously. The limitation here is cognitive: people often don't identify invariant inputs as causes in their own causal models. How strong this effect is in the gout context is not measurable from the published reports.

**Design 2 — Case-crossover (Yang 2019; design confirmed via Methods, non-vaccination question wording not reproduced in published Methods).** Within-subject comparison of exposure during a 2-day hazard window preceding flare versus 2-day control windows collected every 3 months while flare-free. Case-crossover designs have a well-established structural limitation: **invariant exposures cancel by within-subject comparison.** A patient who engages in the same activity daily would report it equally in both hazard and control windows; the design assigns it zero contribution to the odds ratio by construction. Acute changes are what case-crossover is built to detect; habitual exposures are what it is built to filter out.

Consequence across both designs: the published trigger-attribution numbers are weighted toward acute perturbations and structurally underweight chronic-activity contributions. The magnitude of the underweighting is not directly knowable from the data. (Flynn 2015's 71%-trigger-reported figure refers to food triggers only — the instrument did not ask about activity / exercise / injury, so it does not inform this question either direction.)

In cohort studies of chronic activity (Jablonski 2020 and similar), high-activity cohorts are confounded with metabolic-health correlates (lower urate, less alcohol, better hydration), and any flares they experience may be attributed to non-activity inputs because activity is invariant. The protective effect of chronic activity may be partly real (TLR2 downregulation is a plausible mechanism) and partly artifact of confounding. Stratified re-analysis would clarify this — see open question 4.

**Reading "low self-attribution" as equivalent to "not a trigger" conflates absence of attribution with absence of contribution.** That conflation is a known limitation of both deviation-framed self-report and case-crossover designs, for different structural reasons. It warrants explicit acknowledgement when interpreting the trigger-attribution literature. It does not, by itself, establish that mechanical use *is* a major trigger — only that the existing data is weaker evidence on that question than the face-value numbers suggest.

## What the nocturnal-predominance finding might actually mean

Choi 2015's OR 2.36 for overnight flare onset has been read as counterevidence to mechanical triggers — flares happen at night when no one is loading anything, therefore mechanical use cannot be the proximal trigger.

An alternative reading: **daytime mechanical use is the priming / shedding signal; the symptom threshold is crossed overnight as inflammation builds plus Simkin's overnight-effusion-resolution concentrates the already-primed synovium.** Use is the spark; overnight is the smoke.

The two hypotheses (mechanical-trigger vs nocturnal-onset) have been treated as competing in the literature. They may be the same phenomenon viewed from different windows.

**No published study has done the time-lag analysis** — i.e., what was the patient doing in the 6 / 12 / 24 / 48 hours preceding the flare onset, stratified by activity intensity and affected joint? This is testable and has not been tested. See open question 2.

## Open questions

**1. Crystal shedding from MSU-laden cartilage under cyclic load.** Has any group performed the direct experiment: MSU-laden cartilage explant + cyclic compression + supernatant assay for free crystals (polarized light microscopy or particle counter) and IL-1β / IL-1Ra ratio? Current literature scan: no. This is the cleanest in vitro experiment that would close the central mechanistic question, and the protocols exist (Bougault 2012 cyclic-compression apparatus, standard MSU-loading techniques). The missing step is combining the two.

**2. Time-lag distribution from mechanical exposure to flare onset.** Among patients who experience a flare within 24–48h of an identifiable high-intensity joint-loading event, what is the median lag, how does it cluster by joint, load type, and pre-existing crystal burden (DECT-quantified)? No prospective study with this design has been published. This is what would settle whether the nocturnal-predominance and mechanical-trigger findings are the same phenomenon or independent.

**3. First-MTPJ predilection partitioning.** The competing explanations for first-MTPJ podagra predominance — lower peripheral temperature → reduced solubility; peak gait loading; OA co-localization; Simkin overnight effusion — are treated as parallel candidates in the review literature without disentangling them experimentally. *Note: the widely-cited "first MTPJ is the most-loaded peripheral joint at toe-off" claim does not have a primary biomechanics citation surfaced in this scan; the number is itself* **[UNVERIFIED]**. *The "29–32°C peripheral joint temperature" figure is also widely cited via secondary review without a primary measurement source surfaced —* **[UNVERIFIED]**.

**4. Habitual-activity confound in cohort studies.** Does the "chronic activity is anti-inflammatory in gout" finding survive controlling for the metabolic-health confounders that correlate with activity levels (serum urate, BMI, alcohol intake, hydration markers)? A stratified re-analysis of existing cohort data would clarify whether activity per se is protective or whether the apparent protection is the metabolic-correlate halo.

**5. Pulsed prophylaxis for anticipated mechanical events.** Is there clinical benefit to colchicine (or other NLRP3-axis prophylaxis) administered before an anticipated high-load event — a tournament, a long hike, a planned orthopedic procedure — versus continuous prophylaxis? No RCT has been done. Chen K-J 2022's predictive model for spine-surgery flares is the closest existing work, but it recommends prophylaxis on the basis of systemic risk markers (smoking, Hb), not anticipated mechanical exposure.

**6. Phenotype heterogeneity.** Are there gout subpopulations who are high-mechanical-responders (the 4–7% who self-attribute) versus low-mechanical-responders, and do they differ in baseline crystal burden, cartilage condition, or genetic markers (e.g., ALPK1 variants implicated in mechanically-induced NLRP3 activation in OA)? No published stratification.

**7. Metabolic-overload mechanism testability.** The TCM-derived candidate mechanism #5 — exertion → organ-function fatigue → impaired urate excretion → transient local supersaturation — has not been tested in modern kinetic terms. Does sustained exertion measurably impair renal urate clearance in gout patients during the post-activity window in which flares occur? Serial spot urinary urate / creatinine ratios across an exertion-then-rest period in DECT-confirmed gout patients would directly address this. The mechanism would be testable without requiring TCM ontology buy-in — just as a renal-clearance kinetic question.

## Experimental designs that would close the gaps

| Question | Design | Complexity | Iteration risk |
|---|---|---|---|
| Q1 — Crystal shedding under load | MSU-loaded human articular cartilage explants (cadaveric or arthroplasty waste), cyclic compression in a bioreactor (matching Bougault 2012 protocols), supernatant assayed for free MSU crystals, IL-1β, IL-1Ra, ATP, HMGB1 at multiple time points | Medium | Low — explant + cyclic compression protocols are established; the MSU-loading step is the novelty |
| Q2 — Time-lag distribution | Recruit gout patients with documented MSU deposits (DECT-confirmed); daily activity logging with joint-specific load proxies (step count + intensity + sport tags); patient-reported flare onset with hour granularity; target n ≈ 50 patients × 12 months | Medium | Medium — requires patient adherence to logging; mitigated by smartphone-based passive activity capture |
| Q5 — Pulsed prophylaxis RCT | Patients with ≥2 flares/year and an identifiable recurring high-load activity; randomize to single-dose colchicine 2h pre-activity vs placebo; primary endpoint: flare incidence within 48h of indexed activities | High | Medium — requires a patient population with predictable activity exposure; recruitment is the main risk |

Q3, Q4, and Q6 are secondary analyses of existing data plus targeted re-imaging studies; they don't require new trial infrastructure.

## What this page does NOT claim

- That mechanical use is the dominant flare trigger.
- That mechanical use is not a major flare trigger.
- That a particular mechanism (shedding vs mechanotransduction vs DAMP-priming vs effusion-concentration) is correct.
- That the existing trigger-attribution literature is wrong — only that it has a known methodology blind spot that should be acknowledged when interpreting the data.

## What this page DOES claim

- The mechanistic substrate for mechanical triggering is biologically coherent and partially supported by in vitro and animal-model work in related contexts (OA).
- The strongest primary in vitro source on mechanical effects on MSU crystallization is from 1975. The field has not revisited it with modern methods.
- Deviation-framed self-report items (e.g., "more than usual physical activity") cannot, by construction, detect habitual-activity contributions; open-ended self-report items can, but rely on patient insight into their own causal model. The Abhishek 2017 instrument uses both. Whether the resulting attribution numbers materially underweight habitual-activity inputs is not directly measurable from the published data.
- The nocturnal-flare-predominance finding and the mechanical-trigger hypothesis are not necessarily competing explanations.
- Several testable open questions exist and have not been addressed in the published literature.

This is a research-gap page. The opportunity is open.

## Implications for the Open Enzyme platform

If mechanical use turns out to be a major flare trigger axis — particularly for high-activity patients — the therapeutic posture shifts:

- **Uricase ULT alone may not eliminate flares short-term**, even at well-controlled serum urate, until the existing crystal bed dissolves (months to years). The mechanical-trigger axis would add weight to combination therapy with NLRP3 prophylaxis during the crystal-dissolution window, which the platform already designs for (see [nlrp3-exploit-map.md](./nlrp3-exploit-map.md)).
- **Pulsed / on-demand NLRP3 blockade pegged to anticipated mechanical exposure** becomes a candidate therapeutic strategy distinct from continuous prophylaxis. Relevant for the mRNA-IL-1Ra payload work referenced in [chassis-pending-interventions.md](./chassis-pending-interventions.md) — short-duration coverage timed to high-load events may be a cleaner use case than daily baseline coverage.

These are downstream implications conditional on the open questions resolving in favor of mechanical triggering. They are not load-bearing claims for the platform until the upstream evidence is in.

## References

- Wilcox WR, Khalaf AA. *Nucleation of monosodium urate crystals.* Ann Rheum Dis. 1975;34(4):332–339. PMID 242279. **In Vitro.** (Foundational primary source on mechanical effects on MSU nucleation.)
- Choi HK et al. *Nocturnal Risk of Gout Attacks.* Arthritis Rheumatol. 2015;67(2):555–562. PMC4360969. **Clinical / case-crossover, n=724.**
- Abhishek A et al. *Triggers of acute attacks of gout, does age of gout onset matter?* PLoS One. 2017;12(10):e0186096. PMC5638318. **Clinical / cross-sectional, n=550.**
- Chen K-J et al. *Risk Factors for Postsurgical Gout Flares after Thoracolumbar Spine Surgeries.* J Clin Med. 2022;11(13):3749. PMC9267449. **Clinical / retrospective, n=128.**
- Bougault C et al. *Stress-induced cartilage degradation does not depend on the NLRP3 inflammasome.* Arthritis Rheum. 2012;64(12):3972–3981. PMID 22933232. **Animal Model + In Vitro.**
- Jablonski K et al. *Physical activity prevents acute inflammation in a gout model by downregulation of TLR2 on circulating neutrophils.* PLoS One. 2020;15(9):e0237520. PMC7529261. **Animal Model + Clinical observational.**
- Ma W-J et al. *Beware of misdiagnosis and incorrect treatment of acute gout flare and postoperative infections after arthroscopic surgery for knee gouty arthritis.* Zhongguo Gu Shang. 2024. PMID 39104066. **Clinical / retrospective, n=235.** (Chinese-language original; English abstract on PubMed. No translation disagreement on load-bearing claims — the PubMed English abstract carries the n, timing, and event data.)
- Yang Y et al. *Risk of gout flares after vaccination: a prospective case-crossover study.* Ann Rheum Dis. 2019. PMC7184318. **Clinical / case-crossover, n=517.** Used here to characterize the structural limitations of case-crossover designs on detecting habitual-activity triggers. Non-vaccination trigger question wording is not reproduced in the published Methods.
- Flynn TJ et al. *Positive association of tomato consumption with serum urate: support for tomato consumption as an anecdotal trigger of gout flares.* BMC Musculoskelet Disord. 2015;16:196. PMC4541734. **Clinical / cross-sectional, n=2051.** Cited here only to note scope: the instrument asks "Do certain foods/drinks trigger your gout?" — food triggers only, no activity / exercise / injury question — so this study does not inform the mechanical-trigger question either direction.
- Li XD, Miao ZM, Liu YH, Cheng XY, Liu L, Li CG. *1713例痛风急性发作诱因分析* [Analysis of Trigger Factors in 1,713 Cases of Acute Gout Flares]. 山东医药 [Shandong Medical Journal]. 2012. **Clinical / case-series, n=1,713 (Qingdao cohort).** Senior author Li Changgui (李长贵), Affiliated Hospital of Qingdao University. Cited 13× per Google Scholar. Chinese-language only; not PubMed-indexed. **Primary abstract verified via cqvip 2026-05-20.** Verbatim Chinese abstract (objective/methods/results/conclusion structure): 目的分析痛风急性发作的诱因。方法根据不同年龄、尿酸水平及性别,对1 713例痛风急性发作的诱因进行分析比较。结果诱因为高嘌呤饮食839例、饮酒768例、受寒142例、劳累330例、情绪波动56例、高脂饮食101例、外伤及感染6例,无明显诱因410例。≥50岁者高嘌呤饮食、≥40岁者饮酒在各诱因中所占比例明显低于<30岁者(P<0.05);尿酸≥480μmol/L者高嘌呤饮食、尿酸≥420μmol/L者饮酒在各诱因中所占比例明显高于<300μmol/L者(P<0.05);明确的诱因中,男性高嘌呤饮食、饮酒和劳累居前3位,女性高嘌呤饮食、劳累和受寒居前3位。结论痛风急性发作的诱因包括高嘌呤饮食、饮酒、受寒、劳累、情绪波动、高脂饮食、外伤及感染等,其中最重要的诱因为高嘌呤饮食和饮酒,且存在一定的性别、年龄及尿酸水平差异。 Keywords (关键词): 痛风 (gout), 关节病 (arthropathy), 嘌呤饮食 (purine diet), 饮酒 (alcohol consumption), 诱发因素 (triggers). Translation cross-check applied per project protocol on category boundaries: 劳累 (fatigue/overwork) is semantically broader than 剧烈运动 (strenuous exercise) and the primary paper does NOT use the latter — secondary clinical-education venues conflated the two. Trauma (外伤) is grouped with infection at 6 cases total (0.35%).
- *Zhongyi Neikexue* (中医内科学) — standard TCM internal medicine textbook, 痹病 (Bi-disease) chapter. Names 劳累 (exertion/fatigue), 外伤 (trauma), and meteorological factors as discrete contributing triggers for 痹证, with metabolic-overload mechanism framing (organ-function depletion → 湿浊 / damp-turbid accumulation → joint obstruction). **TCM textbook / Mechanistic framing.** Source for candidate mechanism #5.
- Chhana A, Lee G, Dalbeth N. *Factors influencing the crystallization of monosodium urate: a systematic literature review.* BMC Musculoskelet Disord. 2015;16:296. PMC4606994. **Review.**
- Roddy E. *Revisiting the pathogenesis of podagra: why does gout target the foot?* J Foot Ankle Res. 2011;4:13. PMC3117776. **Review.**

*Mechanotransduction references for the Piezo1 → NLRP3 axis in OA contexts (Cao 2026; Chen S. 2025; Liu 2022) surfaced in the lit scan and informed the candidate-mechanism section above. Their specific PMIDs and DOIs are pending verification against primary source before being cited individually here; the page does not depend on their specific citations for any load-bearing claim.*

## Scan limitations

The multilingual scan covered Western (PubMed, Europe PMC, paperclip) + Chinese (mechanism-framed queries + traditional-pathology-framed queries via TCM Bi-syndrome ontology and Kampo) + Japanese (J-STAGE, CiNii) + Korean (KoreaMed Synapse) + German (DGRh guidelines, indexed PubMed) + Russian (PubMed) literatures, with two-pass query framing (mechanism-name + traditional-pathology variants) and translation cross-checks on load-bearing Japanese / Chinese passages.

Remaining limitations after that coverage:

- **Li XD et al. 2012 primary abstract retrieved and verified 2026-05-20** via cqvip from a network with China-region hosts allowlisted. Translation cross-check applied per project protocol. Two corrections to prior secondary-source summary documented inline above. **CNKI / WanFang / ChinaXiv full-article PDFs still gated** at the application layer (subscription / institutional auth) even with network reachability restored — but the abstract carried the load-bearing trigger-frequency table, so the page does not currently depend on full-PDF retrieval.
- **No primary biomechanics paper quantifying first-MTPJ peak loading vs other joints was surfaced** in any language; the claim is consistently asserted in podiatry reviews but the primary citation chain has not been verified. **[UNVERIFIED]** as flagged inline.
- **Peripheral-joint temperature (~29–32°C)** widely cited via secondary reviews in all languages scanned; primary measurement source not surfaced. **[UNVERIFIED]** as flagged inline.
- **Korean Bi-syndrome trigger ontology** incompletely covered — Dongui Bogam analysis paper (jikm.or.kr) timed out on full-text retrieval.
- **Kampo trigger-frequency cohort studies** not found in Japanese-language literature; possibly do not exist (Kampo is syndrome-pattern-based, not trigger-epidemiology-based).
- **No primary in vitro study** combining MSU-laden cartilage + cyclic compression + supernatant readout was surfaced in any language. The mechanism-native gap (open question #1) holds across all literatures scanned.
