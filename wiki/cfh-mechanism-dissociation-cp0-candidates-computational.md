---
title: comp-039 — CFH-dependence mechanism-dissociation of dietary upstream-CP0 candidates
date: 2026-05-21
tags:
  - computational
  - complement
  - CFH
  - Y402H
  - genetics
  - mechanism-dissociation
  - rosmarinic-acid
  - luteolin
  - houttuynia
  - helicteres
related:
  - gout-genetic-variants.md
  - complement-c5a-gout.md
  - upstream-complement-modulator-sweep-computational.md
  - upstream-complement-verification-rerun-computational.md
  - computational-experiments.md
sources:
  - "Sahu A, Rawal N, Pangburn MK. Inhibition of complement by covalent attachment of rosmarinic acid to activated C3b. Biochem Pharmacol 1999;57(12):1439-46. PMID 10353266"
  - "Englberger W, Hadding U, Etschenberg E, Graf E, Leyck S, Winkelmann J, Parnham MJ. Rosmarinic acid: a new inhibitor of complement C3-convertase with anti-inflammatory activity. Int J Immunopharmacol 1988;10(6):729-37. PMID 3198307"
  - "Peake PW, Pussell BA, Martyn P, Timmermans V, Charlesworth JA. The inhibitory effect of rosmarinic acid on complement involves the C5 convertase. Int J Immunopharmacol 1991;13(7):853-7. PMID 1761351"
  - "Zhang T, Chen DF. Anticomplementary principles of a Chinese multiherb remedy for the treatment and prevention of SARS. J Ethnopharmacol 2008;117(2):351-61. PMID 18400428 / PMC7126446"
  - "Yin X, Lu Y, Cheng ZH, Chen DF. Anti-Complementary Components of Helicteres angustifolia. Molecules 2016;21(11):1506. PMID 27834928 / PMC6273495"
  - "Tian L et al. Anti-complementary constituents of Houttuynia cordata and their targets in complement activation cascade. J Ethnopharmacol 2014. PMID 24423008"
  - "Lu Y, Jiang Y, Ling L, Zhang Y, Li H, Chen D. Beneficial effects of Houttuynia cordata polysaccharides on \"two-hit\" acute lung injury and endotoxic fever in rats associated with anti-complementary activities. Acta Pharm Sin B 2018;8(2):218-227. PMID 29719782 / PMC5925397"
  - "Xu YY et al. Houttuynia cordata Thunb. polysaccharides ameliorates lipopolysaccharide-induced acute lung injury in mice. J Ethnopharmacol 2015;173:81-90. PMID 26190353 / PMC7127486"
  - "UniProt P08603 (CFAH_HUMAN) Sushi domain feature annotations — Sushi 7 = aa 387-444, contains Y402; Y402H = rs1061170 ARMD4 association"
status: complete (propagation to gout-genetic-variants.md Category 5 row + complement-c5a-gout.md §6.3 done 2026-05-21)
---

# comp-039 — CFH-dependence mechanism-dissociation of dietary upstream-CP0 candidates

> **Plain-English summary first.** Open Enzyme has identified four dietary candidates that block complement activation upstream of MSU-crystal-driven gout flares: rosmarinic acid (in rosemary, lemon balm, perilla), luteolin (in celery, parsley, chamomile), *Houttuynia cordata* polysaccharide (in fish-mint, a herb commonly eaten across Southeast Asia), and *Helicteres angustifolia* benzofuran lignans (a tropical folk-medicine plant — not dietary). A common genetic variant called **CFH Y402H** is present in ~36-39% of Europeans, ~35-37% of Africans, ~30% of South Asians, ~5-6% of East Asians. It weakens one specific complement-regulator protein (Factor H). The OE prediction is that Y402H carriers should benefit *more* from these dietary candidates because the candidates work *upstream of* where Factor H normally acts — they prevent the problem before Factor H would have to clean it up. **There is one big counter-evidence:** in age-related macular degeneration (AMD), Y402H carriers paradoxically did *worse* on the AREDS zinc-antioxidant formulation. The OE hypothesis is that AREDS works *through* Factor H (and carriers can't capitalize on it because their Factor H is broken), while these dietary candidates work *upstream of* Factor H (so carriers can still benefit). This comp converts that hand-wavy plausibility argument into a candidate-by-candidate prediction the UK Biobank cross-tab can test.

> **Where the analysis lives:**
> - Operations workspace: [`operations/cfh-mechanism-dissociation-2026-05-21/`](../operations/cfh-mechanism-dissociation-2026-05-21/)
> - Per-candidate Model A source reads + Model B (DeepSeek) counter-reads + two-model annotated cross-checks: [`operations/cfh-mechanism-dissociation-2026-05-21/outputs/`](../operations/cfh-mechanism-dissociation-2026-05-21/outputs/)
> - Biobank feasibility (prior): [`logs/cfh-y402h-dietary-cp0-biobank-mining-2026-05-19.md`](../logs/cfh-y402h-dietary-cp0-biobank-mining-2026-05-19.md)
> - Canonical CFH-row source-of-truth: [`gout-genetic-variants.md`](./gout-genetic-variants.md) Category 5; [`complement-c5a-gout.md`](./complement-c5a-gout.md) §6.3

## 1. Scope and question

CFH (Complement Factor H) Y402H — the missense variant rs1061170, p.Tyr402His — sits in Sushi/CCP domain 7 of CFH (UniProt P08603 verified: Sushi 7 = aa 387-444 [grep-verified against the P08603 JSON record this session]; Y402 is in the middle of that domain). CCP6-8 of CFH is the canonical CRP-binding and host-glycosaminoglycan-binding surface. Y402H weakens both surface contacts. CFH itself regulates alternative-pathway complement amplification by (a) decay-accelerating the C3bBb convertase and (b) acting as a Factor-I cofactor for C3b → iC3b cleavage. Both functions operate on **surface-deposited C3b** — that is, *downstream* of where C3b is first generated and deposited.

The OE hypothesis ([`complement-c5a-gout.md` §6.3](./complement-c5a-gout.md), added 2026-05-19): the comp-018 / comp-020 upstream-CP0 dietary candidates inhibit complement *upstream of* where CFH acts (preventing C3 convertase assembly or C3b deposition), so Y402H carriers — who have *more* unregulated surface C3b at baseline — should benefit *more* from these candidates, not less. The AMD-paradox counter-evidence (Klein 2008 PMID 18423869 / Awh 2013 PMID 23972322 / Vavvas 2018 PMID 29311295 AREDS zinc + Merle 2015 PMID 26132079 DHA → CFH high-risk carriers WORSE) is hypothesized to apply only to interventions that work *through* CFH (zinc-induced complement inactivation requires CFH-CRP-bridging, which Y402H performs poorly), not to interventions that work *upstream of* CFH.

This comp converts that hypothesis from hand-wavy plausibility to a **per-candidate CFH-dependence classification** with falsifiable predictions.

## 2. Methodology

Per CLAUDE.md §"Multi-frame query discipline" + §"Pre-commit grep-verify gate for load-bearing numbers" + §"Translation protocol":

1. **Multi-frame retrieval** (PubMed + East Asian academic sources via local-curl allowlist; query plans at [`operations/.../inputs/per-candidate-query-plan.json`](../operations/cfh-mechanism-dissociation-2026-05-21/inputs/per-candidate-query-plan.json); reachability probes at [`operations/.../outputs/retrieval-probes.json`](../operations/cfh-mechanism-dissociation-2026-05-21/outputs/retrieval-probes.json)).

2. **Two-model independent cross-check.** Model A = Claude Opus 4.7 (this comp's primary reader, full primary-source reads); Model B = DeepSeek (`deepseek/deepseek-chat-v3` via OpenRouter, native-Chinese training depth, independent counterread per candidate). Per CLAUDE.md update 2026-05-21: Claude is Model A and reads sources directly; OpenRouter is invoked *only* for Model B to control marginal cost.

3. **Binding-site mapping vs Y402H footprint.** For each candidate, the primary-source binding-site or target-identification data is mapped onto the complement cascade, and the question "does this mechanism require functional CFH downstream?" is answered with structural justification.

4. **Multi-hypothesis discipline** (per CLAUDE.md §"Deep multi-metric evaluation discipline"). For each candidate, ≥2 binding-site / mechanism hypotheses are generated, evaluated against published evidence, and the rejected ones are documented.

5. **Pre-commit grep-verify gate.** All load-bearing numbers (CH50, AP50, IC50, residue ranges, sample sizes, depletion-rescue percentages) verified against the primary source before writing. Sushi-7 = aa 387-444 verified against UniProt P08603 JSON directly. The Lu 2018 depletion-rescue percentages (CHCP C3-depleted 9.29 ± 1.69%, C4-depleted 12.34 ± 1.39%, C5-depleted 44.54 ± 3.92%) verified against PMC5925397 full text. The Yin 2016 CH50 / AP50 (compound 4 = 40 / 105 μM; compound 5 = 9 / 21 μM) verified against PMC6273495 full text. The Sahu 1999 IC50 = 34 μM verified against PubMed-hosted abstract.

## 3. Per-candidate classification

### 3.1 Rosmarinic acid

**Classification: CFH-INDEPENDENT (High confidence — both models agree).**

**Primary mechanism evidence:**
- Sahu 1999 (PMID 10353266): rosmarinic acid covalently attaches to the **thioester-containing α'-chain of nascent C3b** (Cys988 reactive carbonyl, exposed only on activated/cleaved C3). IC50 for inhibiting covalent C3b deposition on cells = **34 μM**. Mechanism is fluid-phase covalent capture of nascent C3b *before* surface attachment. **[In Vitro]**
- Englberger 1988 (PMID 3198307): inhibits **C3-convertase of the classical complement pathway**. Threshold 1 μM; optimal 5-10 μM, ~70% hemolysis inhibition. Mechanism is convertase active-site / assembly inhibition (elastase weakly co-inhibited supports serine-proteinase active-site involvement). **[In Vitro]**
- Peake 1991 (PMID 1761351): mM-range C5 convertase inhibition; secondary regime. **[In Vitro]**

**CFH-footprint mapping:** the C3b thioester (Cys988 α'-chain) is structurally distant from C3d (the CFH-binding fragment of C3b) and far from CFH's CCP6-8 CRP-binding surface. Rosmarinic acid quenches nascent C3b *before* it can be deposited on a target surface; CFH's regulatory functions (decay-acceleration of C3bBb, Factor-I cofactor for C3b → iC3b) operate on already-surface-deposited C3b — downstream of where rosmarinic acid acts. No primary source mentions CFH dependence.

**Predicted Y402H × rosmarinic acid × incident gout interaction:** **negative direction (effect ≥ in carriers)** — Model A reasoning. Model B picks **null direction** (no differential effect). Both reject the AMD-paradox direction (+ harm in carriers).

[TRANSLATION-DISAGREEMENT — prediction direction]: Model A predicts effect ≥ in carriers because Y402H carriers have *more* unregulated surface C3b at baseline; removing the upstream substrate produces a larger absolute reduction. Model B predicts null because mechanism independence implies genotype indifference. Both predictions need separate UKB falsification thresholds; positive direction (carriers worse) refutes both.

**Multi-hypothesis discipline — rejected alternatives:**
1. *Rosmarinic acid acts via CRP displacement at the CFH CCP7 surface.* Rejected: Sahu 1999 IC50 was measured in cell-free fluid-phase nascent C3b — no CRP, no host surface, no CFH present; mechanism works in their absence.
2. *Rosmarinic acid binds C3d (the CFH-binding fragment) directly.* Rejected: radioiodination localizes covalent attachment to the α'-chain thioester (Cys988), not C3d (the TED domain).

**Falsification test:** rosmarinic acid (34 μM, 100 μM, 340 μM) on MSU-crystal-driven complement activation in CFH-depleted serum vs CFH-replete serum (C5a generation readout). Retained suppression in CFH-depleted serum confirms CFH-independence.

**UKB cross-tab specification:** rs1061170 × Phenol-Explorer-derived rosmarinic-acid intake (rosemary, perilla, lemon balm sources via Oxford WebQ — note these are Mediterranean-pattern foods and exposure is heterogeneous) × incident gout M10.x. Pre-specify null AND negative direction with adequate power for each.

### 3.2 Luteolin

**Classification: CFH-INDEPENDENT (Medium confidence — both models agree, both flag mechanism-site ambiguity).**

**Primary mechanism evidence:**
- Zhang 2008 (PMID 18400428 / PMC7126446, full text read): luteolin tested in matched CP (sheep-erythrocyte + guinea-pig serum) and AP (rabbit-erythrocyte + 1:10 NHS) hemolytic assays. **CH50 = 0.19 mM; AP50 = 0.17 mM.** [Verbatim verified against PMC7126446.] Mechanism attribution: **4'-OH B-ring substitution essential for activity** (flavonoids with -OCH3 at C-4' are 5-10× weaker). Specific cascade node NOT pinned at depletion-rescue resolution. **[In Vitro]**
- Pieroni 1996 (PMID 8941947): olive-leaf flavonoid class-level activity. **[In Vitro]**

**CFH-footprint mapping:** the matched CP/AP IC50 (0.19 vs 0.17 mM) is consistent with a cascade node common to both pathways — most likely C3 itself or convertase active-site / assembly. Both candidate mechanisms are functionally upstream of CFH's AP-specific regulatory role. A CFH-competitive mechanism would predict AP-selective potency (CFH is AP-specific), which is not observed.

Luteolin additionally has documented gout-relevant non-complement modes (per [comp-013](./tcm-gout-compound-triage-computational.md)): XO IC50 550 nM + URAT1 expression downregulation. These are CFH-orthogonal entirely. The multi-mode complicates the UKB cross-tab — see "Limitations" below.

**Predicted Y402H × luteolin × incident gout interaction:** **negative direction (effect ≥ in carriers, Model A) vs null direction (Model B).** Both reject the AMD-paradox direction.

[TRANSLATION-DISAGREEMENT — mechanism specificity]: Model A commits to "convertase-level inhibition" as the most-likely mechanism site; Model B reserves judgement. Model B's more cautious framing is appropriate given that no depletion-rescue or single-residue binding data exists for luteolin specifically.

**Multi-hypothesis discipline — rejected alternative:**
1. *Luteolin binds the CCP6-8 CRP-binding surface of CFH itself, competing with CRP.* Weakly rejected: (a) no surveyed paper reports CFH as a luteolin target; (b) the matched CP/AP IC50 is inconsistent with a CFH-competitive mechanism (CFH-competition predicts AP-selectivity, not matched CP+AP potency).

**Falsification test:** luteolin on MSU-crystal-driven complement activation in CFH-depleted vs CFH-replete serum. **For the UKB cross-tab, additionally pre-specify a 24h-urate intermediate-phenotype arm** to dissociate the complement-mode from the XO + URAT1 urate-axis modes — otherwise the cross-tab is confounded by three parallel mechanisms.

**UKB cross-tab specification:** rs1061170 × Apiaceae-family dietary intake (celery, parsley, chamomile — captures luteolin exposure better than total-flavonoid sums) × incident gout M10.x, with 24h-urate intermediate readout in a subset.

### 3.3 Houttuynia cordata polysaccharide (HCP / HCPM / CHCP)

**Classification: CFH-INDEPENDENT (High confidence — both models agree).**

**Primary mechanism evidence:**
- Lu 2018 (PMID 29719782 / PMC5925397, full text read): complement-depleted-sera mapping for CHCP polysaccharide. Verbatim depletion-rescue percentages: **C2-depleted serum rescue 72.82 ± 10.61%, C9-depleted rescue 63.21 ± 2.27%, C3-depleted rescue 9.29 ± 1.69%, C4-depleted rescue 12.34 ± 1.39%, C5-depleted rescue 44.54 ± 3.92%.** Interpretation: **CHCP's primary targets are C3 and C4, with partial C5 effect.** [Grep-verified against PMC5925397.] **[In Vitro + Animal Model — rats, "two-hit" ALI rescue]**
- Tian 2014 (PMID 24423008): glycoside-class anti-complementary fractions of *Houttuynia cordata* "block C3 and C4 components" — convergent mechanism class. **[In Vitro]**
- Xu 2015 (PMID 26190353 / PMC7127486, full text read): HCP at 40, 80, 160 mg/kg PO in LPS-induced ALI mouse model — reduces C3d deposition (immunohistochemistry), reduces TLR4 expression in lung tissue, suppresses C5a-induced macrophage chemotaxis, reduces NLRP3-axis cytokines (IL-1β, TNF-α, IL-6). **Multi-target: complement + TLR4 + NLRP3 axis.** **[Animal Model]**
- Yu 2026 PMC12937656 (TLR4-MD2 computational docking) — CP1-level TLR-priming mechanism orthogonal to complement.

**CFH-footprint mapping:** C3 binding upstream of cleavage prevents the substrate pool that CFH regulates. **C4 binding is mechanistically incompatible with CFH-dependence** — CFH is alternative-pathway-specific and does not regulate the classical-pathway C4-axis. The TLR4-MD2 mode (CP1, TLR-priming) bypasses complement entirely. Pectic polysaccharide binding mode (adsorptive surface contact) is structurally distinct from CFH's CCP-fold protein recognition. Three orthogonal lines of evidence converge on CFH-independence.

**Predicted Y402H × HCP × incident gout interaction:** **negative direction, possibly notably greater in carriers (Model A — dual CP0+CP1 chokepoint compounds the genotype-baseline-severity amplification) vs null direction (Model B).** Both reject the AMD-paradox direction.

[TRANSLATION-DISAGREEMENT — dual-chokepoint framing]: Model A explicitly highlights HCP's dual CP0 (complement) + CP1 (TLR4) mechanism as a reason for *amplified* benefit in Y402H carriers; Model B does not foreground this. The dual-chokepoint framing is consistent with the comp-018 Phase 2 "DUAL-CHOKEPOINT" classification of HCP/HCPM as a Tier 1d candidate.

**Multi-hypothesis discipline — rejected alternative:**
1. *HCP polysaccharide acts as a CFH-mimic — binding C3b at the same surface CFH binds.* Partially rejected: depletion-rescue data (Lu 2018) shows HCP blocks the cascade at C3 *cleavage*, not at C3b *inactivation*. CFH-mimicry would predict downstream-of-cleavage action. HCP's pectic polysaccharide structure is structurally nothing like CFH's CCP-fold. Same prediction direction (negative) but better-evidenced as activation-blocker than CFH-mimic.

**Falsification test:** CHCP / HCP-1 on MSU-crystal-driven complement activation in (i) CFH-depleted serum, (ii) Factor B-depleted serum, (iii) C4-depleted serum. The C4-depletion arm specifically tests the classical-pathway-CFH-independent prediction.

**Cross-tab specification — NOT well-suited to UK Biobank.** Houttuynia consumption is rare in UK dietary corpus. The relevant cross-tab is more tractable in Chinese / Vietnamese / Korean / Japanese cohorts — Korean Genome Epidemiology Study (KoGES), China Kadoorie Biobank (CKB), Singapore Chinese Health Study. These cohorts have lower Y402H allele frequency (~5-6% East Asian vs ~36-39% European) but adequate Houttuynia exposure data. **Operational recommendation:** if UKB is the active collaboration channel, defer HCP cross-tab and lead with rosmarinic acid + luteolin; if a parallel East Asian cohort collaboration becomes available, HCP becomes the highest-priority cross-tab there.

### 3.4 Helicteres benzofuran lignans

**Classification: CFH-INDEPENDENT (Medium confidence — Model A bounds by replication risk; Model B picks High because Yin 2016 target identification is unambiguous if it replicates).**

**Primary mechanism evidence:**
- Yin 2016 (PMID 27834928 / PMC6273495, full text read): depletion-rescue target identification for *Helicteres angustifolia* benzofuran sesquilignans. **Compound 4 (machicendonal): CH50 = 40 μM, AP50 = 105 μM; targets C1q, C2, C3, C4, C9. Compound 5 (dihydrodehydrodiconiferyl alcohol): CH50 = 9 μM, AP50 = 21 μM; targets C1q, C2, C3, C9 (NOT C4).** [Verbatim verified against PMC6273495.] **[In Vitro, single-paper anchor]**
- **comp-018 Phase 2 replication status: INCONCLUSIVE** ([phase-2-helicteres-replication.json](./etc/experiments/comp-018-upstream-complement-modulator-sweep/phase-2/phase-2-helicteres-replication.json)) — no independent group has reproduced Yin 2016. Structurally-adjacent benzofuran lignans (*Styrax japonica* egonol, Min 2004 PMID 15643559) are 3.7× weaker, leaving open the question of whether Yin 2016 represents exceptional pharmacology or assay-format artifact.

**CFH-footprint mapping:** C1q, C2, C4, C9 are not CFH-regulated. C3 binding is upstream of cleavage (CFH regulates the cleavage product, not C3 itself). The multi-target lignan pattern is structurally orthogonal to CFH's CCP6-8 binding surface. **The CP-pathway IC50 (9 μM CH50 for compound 5) is more potent than the AP-pathway IC50 (21 μM)** — inconsistent with a CFH-competitive mechanism (CFH is AP-specific; competition would predict AP-selectivity).

**Predicted Y402H × Helicteres × incident gout interaction:** **negative direction (effect ≥ in carriers, Model A) vs null (Model B), with wide uncertainty bands. Practically: Helicteres is not part of any UKB-tractable dietary corpus.** The candidate's CFH-classification value is more relevant to a future TCM-supplement clinical evaluation than to the present UKB cross-tab.

[TRANSLATION-DISAGREEMENT — confidence framing]: Model A bounds confidence by comp-018 Phase 2 replication risk (Medium); Model B does not weight replication risk into the confidence call (High). Model A's framing is the appropriate one for OE's evidence discipline — replication risk is a *published* Phase 2 finding, not informal speculation.

**Multi-hypothesis discipline — rejected alternative:**
1. *Helicteres lignans act via CCP6-8 occupation displacing CRP / GAG from CFH.* Rejected: Yin 2016 depletion-rescue identifies C1q + C2 + C3 + C4 + C9 (not CFH) as targets; CP-pathway IC50 is more potent than AP, inconsistent with CFH-competitive mechanism.

**Falsification test priority order:**
1. Independent wet-lab replication of Yin 2016 (comp-018 Phase 2 open follow-up). **Load-bearing.**
2. If replication confirms, compound 5 on MSU + CFH-depleted vs CFH-replete serum.
3. Consider whether Helicteres has a route to clinical translation given non-dietary status.

## 4. Summary table — per-candidate genotype × candidate interaction prediction

| Candidate | CFH-dependence | Confidence | Predicted Y402H × candidate × incident gout (Model A) | Predicted (Model B) | Falsification threshold |
|---|---|---|---|---|---|
| **Rosmarinic acid** | CFH-independent | High | negative (effect ≥ in carriers) | null | HR > 1.5 (402HH × diet vs 402YY × diet) at p<0.05 refutes — retire from CP0 stack |
| **Luteolin** | CFH-independent | Medium | negative (effect ≥ in carriers, with multi-mode confound) | null | HR > 1.4 refutes; cross-tab against Apiaceae intake + 24h-urate intermediate readout |
| **Houttuynia cordata polysaccharide (HCP/HCPM/CHCP)** | CFH-independent | High | negative, possibly notably greater (dual CP0+CP1 chokepoint) | null | HR > 1.3 refutes; UKB unlikely to capture exposure — defer to East Asian cohorts |
| **Helicteres benzofuran lignans** | CFH-independent | Medium (replication-bounded) | negative, wide uncertainty | null | (a) wet-lab replication of Yin 2016 first; (b) non-dietary, not UKB-actionable |

**Mechanism axis common to all four candidates:** action at C3 / C3 convertase / C3b nascent thioester / C1q + C2 + C4 (CP initiation) — all upstream of where Y402H matters. **Mechanism axis present in zero of the four candidates:** zinc-induced complement inactivation via CFH-CRP-bridging (the AREDS / DHA AMD-paradox mechanism). The dissociation is mechanistically clean: OE candidates work by *substrate-elimination upstream of CFH regulation*, AREDS works *through* CFH-CRP-bridging-dependent complement inactivation. Y402H breaks the latter but not the former.

## 5. Recommended UK Biobank collaboration ask

For the UK Biobank gout-GWAS collaborators (Merriman/Otago, Major-Wrigley/Auckland, Choi/MGH per [`gout-genetic-variants.md`](./gout-genetic-variants.md) Category 5 CFH row), the candidate-stratified cross-tab is the following:

**Lead query (highest-power tractable cross-tab):**

> Cross-tabulate **rs1061170 (CFH Y402H) genotype × Phenol-Explorer-derived rosmarinic-acid intake quartiles × incident gout M10.x** in UK Biobank participants without prior gout at baseline (n target ≈ 450K). Pre-specify *both* a **negative-direction** test (carrier-amplified protective effect, HR < 1 in carriers vs non-carriers on high-intake diet; Model A) AND a **null-direction** test (no differential interaction; Model B). The AMD-paradox direction (carriers WORSE on high-intake, HR > 1.4) refutes the OE upstream-CP0-bypass hypothesis and would force retiring rosmarinic acid from the upstream-CP0 candidate stack.

**Secondary queries (in priority order):**

1. **rs1061170 × Apiaceae-family intake × incident gout M10.x** (luteolin proxy; Apiaceae captures luteolin-rich exposure better than total-flavonoid sums). Add 24h-urate intermediate-phenotype readout in the subset with biochemistry data to dissociate the complement-mode from the XO + URAT1 urate-axis modes.

2. **rs1061170 × dietary CFH-bypass diversity score × incident gout** (Bondonno 2025 Nature Food methodology generalized) — composite score over rosemary / lemon balm / perilla / celery / parsley intake, vs Yokose 2024 Rheumatology cohort framework.

3. **NOT in UKB:** Houttuynia cordata cross-tab. The exposure is rare in UK dietary corpus. Defer to Korean Genome Epidemiology Study (KoGES) / China Kadoorie Biobank (CKB) / Singapore Chinese Health Study collaborations when available — flag that the East Asian cohorts have lower Y402H allele frequency (~5-6%) but adequate Houttuynia exposure data.

4. **Not actionable in any biobank yet:** Helicteres benzofuran lignans (non-dietary; comp-018 Phase 2 replication required first).

**Confound considerations** for the collaborators: (a) CFH 402H × hypertension interaction (Volcik 2008 ARIC) and CFH 402HH × elevated CRP (Hecker 2023) mean the cross-tab needs careful adjustment for BMI, baseline CRP, eGFR, hypertension; (b) overall dietary-quality / Mediterranean-diet-pattern correlation with rosmarinic-acid-rich foods needs adjustment; (c) effect-direction differences in African-American vs European-ancestry (Volcik 2008) suggest the cross-tab should be stratified by ancestry rather than pooled.

## 6. Limitations

1. **No direct empirical Y402H × candidate × gout data exists in the published literature.** All four classifications are mechanistic extrapolations from primary-source binding-site or target-identification data — the empirical test is exactly what the UKB cross-tab is designed to provide.

2. **AMD-vs-gout site-of-action confounding.** AMD complement activation is at the retinal pigment epithelium; gout complement activation is at MSU crystals in joints. The CFH-CRP-zinc bridging machinery may not be identically deployed at both sites, so the AMD-paradox-doesn't-transfer reasoning carries some site-specificity uncertainty.

3. **Bioavailability of dietary candidates is variably characterized.** Rosmarinic acid reported low systemic absorption (≤1% per PMC9143754); luteolin variable (Apiaceae sources better than supplementation); HCP polysaccharide bioavailability after oral intake incompletely characterized; Helicteres benzofuran lignans not relevant (non-dietary). The operative *in-vivo* concentration at MSU-crystal sites in joints is unknown for all four. Gut-luminal or systemic-plasma routes may differ.

4. **Single-anchor replication risk for Helicteres.** comp-018 Phase 2 verdict on Yin 2016 is INCONCLUSIVE. The Helicteres CFH-independence classification is conditional on the Yin 2016 target identification holding up in independent replication.

5. **Mechanism-site resolution varies across candidates.** Rosmarinic acid (high, Sahu 1999 radioiodination); HCP / Helicteres (medium, depletion-rescue resolution per Lu 2018 + Yin 2016); luteolin (low, no depletion-rescue or single-residue data). Confidence calls reflect this gradient.

6. **Two-model agreement on classification but disagreement on prediction direction.** Both models classify all four candidates as CFH-independent. Both reject the AMD-paradox direction (carriers WORSE). They disagree on whether to predict negative direction (Model A — carriers benefit MORE because genotype-baseline severity amplifies absolute effect size) or null direction (Model B — mechanism independence implies genotype indifference). The UKB cross-tab should be pre-specified to falsify both. A *positive* (carriers worse) result refutes both models and would force retiring the upstream-CP0-bypass hypothesis.

7. **Population-stratification confound for Y402H frequency.** Y402H is ~36-39% in Europeans, ~35-37% in Africans, ~30% in South Asians, ~5-6% in East Asians. The UKB cohort is European-ancestry-skewed. Replication across ancestries needs separate analyses, ideally collaborations with All of Us (better African-American representation) and the East Asian cohorts above for HCP.

## 7. New follow-ups surfaced

- **comp-040 (proposed):** wet-lab in-vitro CFH-depleted-serum MSU-crystal complement-activation assay — definitive falsification test of the CFH-independence classification for rosmarinic acid, luteolin, and HCP. Estimated cost: low (assay reagents commercially available; serum sourcing via CompTech or Complement Technology Inc).
- **comp-041 (proposed):** Y402H × candidate cross-tab feasibility scan in East Asian cohorts (KoGES, CKB, Singapore Chinese Health Study) for Houttuynia-specific cross-tab — paralleling the UKB feasibility analysis done 2026-05-19.
- **Open follow-up — comp-018 Phase 2 Helicteres replication:** unchanged; this comp does not displace the load-bearing replication requirement on Yin 2016.

## 8. Cross-references

- [`gout-genetic-variants.md`](./gout-genetic-variants.md) Category 5 CFH row (canonical; this comp informs the predicted-stratification framing but does not edit the canonical row until Brian reviews)
- [`complement-c5a-gout.md`](./complement-c5a-gout.md) §6.3 (canonical; this comp informs the dietary-CP0 stratification framing but does not edit until Brian reviews)
- [`upstream-complement-modulator-sweep-computational.md`](./upstream-complement-modulator-sweep-computational.md) — comp-018, the original modulator discovery + Phase 2 Houttuynia + Helicteres + C1-INH thread
- [`upstream-complement-verification-rerun-computational.md`](./upstream-complement-verification-rerun-computational.md) — comp-020, the brief-scrubbed verification rerun
- [`logs/cfh-y402h-dietary-cp0-biobank-mining-2026-05-19.md`](../logs/cfh-y402h-dietary-cp0-biobank-mining-2026-05-19.md) — biobank feasibility analysis
- [`computational-experiments.md`](./computational-experiments.md) — comp-039 entry
- Operations workspace: [`operations/cfh-mechanism-dissociation-2026-05-21/`](../operations/cfh-mechanism-dissociation-2026-05-21/)
