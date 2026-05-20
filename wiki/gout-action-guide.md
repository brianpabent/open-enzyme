---
title: "Gout Action Guide — what to do, by situation"
date: 2026-05-08
tags: ["application-surface", "patient-guide", "gout", "stack-design", "decision-tree"]
related:
  - supplements-stack.md
  - gout-pathophysiology.md
  - etc/open-enzyme-vision.md
  - self-experiment-protocol.md
  - personal-genome-protocol.md
status: application-surface
audience: "Anyone arriving with 'I have gout, what do I do?' — patients, practitioners, curious laypeople. PhD-level mechanism details live in the research wiki; this page is the entry surface that gets you to the right action."
---

# Gout Action Guide — what to do, by situation

**This is the "I have gout, what do I do?" entry surface for Open Enzyme.** The research wiki has the depth — mechanisms, evidence levels, study citations, contradictions. This page surfaces what those findings *imply for action*: what to start today, what to build out over a month, what to plan for over a year.

> **Not medical advice.** Open Enzyme is Phase 0 (Research & Design). None of the engineered-strain interventions on this page are FDA-approved or clinically available. Everything in the "today / this month / this year" sections is over-the-counter or dietary; even so, work with a physician on anything that interacts with your medications or comorbidities. The point of this page is to translate research findings into actionable starting points, not to replace clinical care.

---

## Step 1 — Identify your situation

Pick the closest match. Each row links to a tailored section below.

| If you are… | Start here |
|---|---|
| **Male, mid-life, no genotype info, mostly diet-managed gout** | [Default path](#default-path) |
| **Androgen-elevated** (high endogenous T, on TRT, on Clomid/enclomiphene) | [Androgen-elevated path](#androgen-elevated-path) |
| **Q141K-positive ABCG2** (from 23andMe / genome sequencing) | [Q141K-positive path](#q141k-positive-path) |
| **In an active flare right now** | [Active flare](#active-flare) |
| **Already on allopurinol or febuxostat, looking for adjuncts** | [On a urate-lowering drug](#on-a-urate-lowering-drug) |
| **No flare yet, family history or borderline UA** | [Prevention path](#prevention-path) |

---

## Default path

Most readers. No genotype info, mostly diet-managed gout, want a sensible mechanism-grounded stack.

> **Calibration note (updated 2026-05-08 with comp-019 flux-model results):** the engineered-strain mechanism (gut-lumen uricase via koji) is predicted to work in non-Q141K males at the SAME or LARGER effect size than in Q141K-positive readers — not smaller. [comp-019](./uricase-abcg2-genotype-stratification-computational.md) (flux-model Monte Carlo, n=5000, 2026-05-08) found the gut-lumen uricase mechanism is **substrate-limited rather than ABCG2-capacity-limited**: WT/WT non-Q141K males get the LARGEST predicted ΔSUA (−0.83 mg/dL at 25 mg/day) because they have more urate flowing through the gut compartment for the engineered uricase to degrade. Q141K-het predicted −0.67 mg/dL; Q141K-hom −0.50 mg/dL. **The platform's primary-demographic positioning is supported by the in-silico flux model.** Caveat: this is in-silico, not human RCT. Clinical effect size remains unproven; the eventual Phase 2b RCT (typical-gout cohort, Q141K + Q126\* as stratification rather than enrichment, single 25 mg/day dose, pre-stratified by CKD stage) is what would actually settle this. **Practical implication:** the Default path's dietary + over-the-counter entries are genuinely broadly applicable today; the engineered-strain Future entries are predicted to apply broadly too, pending Phase 2b confirmation. **Genotyping yourself still matters** — but for adjacent clinical reasons (HLA-B\*58:01 carriers have high allopurinol-allergy / SCAR risk; SLC2A9 / URAT1 variants affect baseline UA handling; family-history risk stratification) rather than gut-lumen-sink-mechanism conditionality. See [personal-genome-protocol](./personal-genome-protocol.md). If you do test Q141K-positive, the [Q141K-positive path](#q141k-positive-path) still has tailored stack guidance for adjuvant interventions (sulforaphane, lactoferrin, EGCG) regardless of the engineered-strain mechanism's predicted effectiveness.

### Today (start in the next 24 hours)

- **Cut high-fructose corn syrup** — fructose drives PRPS-mediated purine biosynthesis upstream of XO (the enzyme allopurinol blocks). This is a single dietary change with real mechanistic backing. See [PRPS chokepoint](./prps-purine-biosynthesis-chokepoint.md), [fructose connection](./fructose-connection.md).
- **Hydrate aggressively** — >3L/day. Dilutes urate, supports renal excretion.
- **Cut the obvious dietary triggers** — organ meats, beer, sardines, anchovies. Moderate red meat. (Standard advice; documented in primary clinical literature.)
- **Tart cherry concentrate** — 8–12 oz/day OR 500–1500 mg/day dried-extract capsule. Lowers UA modestly + reduces flare frequency in observational data. Cheap, broadly tolerated. [Catalog →](./supplements-stack.md#cherry-extract-tart-cherry-concentrate)

### This month (build out)

- **Omega-3 (high EPA + DHA)** — 3–4 g/day. NLRP3-pathway resolution via specialized pro-resolving mediators (SPMs). DHA-derived MSU-gout animal evidence is strongest. [Catalog →](./supplements-stack.md#omega-3-high-epa--dha)
- **NAC (N-acetylcysteine)** — 600–1,200 mg/day split AM + evening. Glutathione/ROS axis suppresses NLRP3 priming. ~$15/month. [Catalog →](./supplements-stack.md#nac-n-acetyl-cysteine)
- **Lactoferrin (bovine)** — 100–300 mg/day commercial oral. Anti-inflammatory + Mechanistic Extrapolation toward ABCG2 derepression via TNFα suppression. [Catalog →](./supplements-stack.md#lactoferrin-bovine--new-cp5-entry)
- **Whole-fermentate Cordyceps + GLPP** *(speculative — wet-lab gate pending)* — emerging two-organism stack from the medicinal-mushroom-complement track. Targets ADA (adenosine deaminase) upstream of XO. Currently mechanism-grounded, not yet wet-lab confirmed at human dose. Reality check: typical fruiting-body extracts deliver only ~3–4 mg cordycepin per serving (sub-therapeutic by ~25–150×); a pure-cordycepin nutraceutical at 100–500 mg/day OR home Cordyceps fermentation is the only way to deliver a dose where the URAT1-inhibition mechanism is plausible. See [medicinal-mushroom-complement-track](./medicinal-mushroom-complement-track.md).

### This year (advanced)

- **Run the closed-loop n=1 pharmacogenomics workflow** — genotype → variant-informed compound selection → home/community-biolab production → Tier 2 batch QC → calibrated dose → biomarker tracking. The canonical user-facing entry point is [`genotype-informed-supplement-workflow.md`](./genotype-informed-supplement-workflow.md) — walks the five-step pipeline end-to-end with a Q141K worked example. The two prerequisite steps below feed into it.
- **Get genotyped via clinical-grade testing** — order ABCG2 Q141K (rs2231142), SLC2A9, URAT1 variants through a clinical-grade lab (e.g., via your rheumatologist or a direct-to-consumer clinical service that returns CLIA-grade results). Changes the stack design substantially. **Consumer panels (23andMe, AncestryDNA, etc.) are not recommended for any gout-stack-design decision** — see the canonical [Consumer SNP data-quality caveat](./gout-genetic-variants.md#consumer-snp-data-quality-caveat--canonical-statement) for the full reasoning. See [personal-genome-protocol](./personal-genome-protocol.md) for ordering paths. The unified variant index at [`gout-genetic-variants.md`](./gout-genetic-variants.md) is the canonical reference for which variants matter and what they do.
- **Self-experiment with rigor** — log SUA monthly, track flares, A/B test compounds. See [self-experiment-protocol](./self-experiment-protocol.md).
**Acute-flare-abort comparator table — choosing between prednisone / anakinra / canakinumab for an active flare.** Per-flare and cumulative-over-years framing for someone with recurrent gout:

| Option | Mechanism | Dosing for acute flare | Acute side effects | Cumulative burden (recurrent flares × decades) | Cost per flare | Access |
|---|---|---|---|---|---|---|
| **Prednisone taper** | Glucocorticoid receptor — system-wide | 30–40 mg/day × 5 days then taper over 7–10 days | Glucose spike, BP rise, sleep disruption, mood changes, immunosuppression | **Real, dose-dependent:** bone loss / osteoporosis, cataracts, adrenal suppression, glucose intolerance, weight gain | ~$10–30 (generic) | Any prescriber |
| **Anakinra (Kineret) SC** | IL-1R1 competitive antagonist (recombinant endogenous IL-1Ra) | 100 mg SC daily × 3 days, self-administered in thigh/abdomen. **~85–94% achieve good response across real-world series; meaningful pain reduction often within 24 h, full resolution by day 3–5** (Ottaviani 2013 PMC3978950, Jeria-Navarro 2023 PMC9877612, Saag 2021 anaGO RCT) | **Injection-site reactions in <2% of gout 3-day-protocol cohorts** (the 70% ISR rate widely quoted is from chronic-RA daily dosing where ISRs develop over first 4 weeks); immediate stinging at injection mostly resolves within seconds; modest infection-risk signal at 3-day acute use (~0.9% in flare arm vs 31.8% in long-term-anakinra populations — bracket the distinction sharply) | **Minimal known burden** — anakinra is recombinant version of body's endogenous IL-1Ra; no bone / glucose / adrenal effects; long-term concern is only infection masking under chronic use (not relevant for 3-day acute use × few flares/yr) | ~$300/dose × 3 = ~$900 | Rheumatologist (off-label for gout) |
| **Canakinumab (Ilaris) SC** | Anti-IL-1β monoclonal | 150 mg single SC | Same injection-site profile; longer half-life (~26 days) so chronic exposure window per dose | Same as anakinra's mechanism (no steroid burden); ADAs possible with chronic use but rare | **~$3,000/dose** (FDA-approved for gout but cost barrier) | Rheumatologist; insurance variable |
| **Colchicine + NSAID** (mild flares) | Microtubule inhibition + COX | 1.2 mg colchicine + NSAID at flare onset | GI (colchicine), GI bleed risk (NSAID), renal (NSAID) | NSAID: real renal burden over years; colchicine: minimal at acute-use dose | ~$20–50 | OTC or any prescriber |
| **Inhaled mRNA-IL-1RA** *(future, 5–10 yr horizon)* | Same as anakinra — pulmonary mRNA expression of IL-1Ra | Per [comp-036](./computational-experiments.md): BID × 4–14 days reaches **median 50–56% of flare window above 80% receptor occupancy** (best regimen tested); doesn't match anakinra Cmax but partial-suppression may be clinically meaningful vs prednisone burden | Pulmonary irritation; possible LNP innate immune activation; anti-PEG buildup over many lifetime exposures | TBD; in principle cleaner than steroid burden; chronic-LNP-exposure question is open | $25–200/flare projected | Doesn't exist yet (partner-tier development) |

**The decision frame:** if you flare 3–6× per year over decades, **cumulative prednisone burden is the load-bearing concern** (bone / glucose / mood / cataract effects compound). Anakinra SC is the cleanest acute-flare-abort option clinically available *today* — same chokepoint as canakinumab and inhaled mRNA, just SC route. Canakinumab has the longest half-life (one shot covers months) but cost is prohibitive without insurance. Colchicine + NSAID is the right tool for mild flares; inadequate for severe. The inhaled mRNA-IL-1RA route is on a 5–10 year development horizon (per [comp-033](./computational-experiments.md) + [comp-036](./computational-experiments.md)) and is what would change the economics if it lands — same mechanism as anakinra, much lower per-dose cost, different delivery format. **Head-to-head RCT evidence (added 2026-05-19, source: `logs/anakinra-3day-gout-patient-experience-2026-05-19.md`):** Saag 2021 (anaGO, n=165) found anakinra and a single IM triamcinolone shot produce essentially identical pain reduction at 24–72 h (−41.2 vs −39.4 on 0–100 VAS, p=0.688); Janssen 2019 (n=88) found anakinra non-inferior to free-choice standard care with more patients achieving ≥50% pain reduction by day 3 (OR 2.56, 95% CI 1.03–6.37, p=0.04). The case for anakinra over prednisone for a *single* flare is mostly about cumulative-steroid-burden avoidance over years, not single-flare pain control where the two are comparable.

**Relapse without a ULT/prophylaxis bridge (added 2026-05-19, load-bearing for recurrent-flare patients).** Real-world series consistently show that the 3-day anakinra course aborts the index flare but ~26% of patients relapse within ~2 weeks if no flare-prevention bridge therapy (allopurinol/febuxostat + low-dose colchicine prophylaxis) is in place — Ottaviani 2013 PMC3978950 reports relapse 70% in patients without prevention vs 20% with prevention (p=0.006). **Anakinra is an acute-abort tool, not a prophylactic.** Pair with ULT initiation or continuation. The combined-route flare protocols below assume this ULT bridge is being put in place at the same time the flare is being aborted.

- **Anakinra (Kineret) SC for acute flare — bridge while inhaled-mRNA pulse doesn't exist yet.** Off-label for acute gout flare, used in rheumatology practice when corticosteroids are contraindicated or undesirable (recurrent flares + steroid burden). **Route: subcutaneous injection in thigh or abdomen, 100 mg/day × 3 days** — same SC route as insulin, the patient self-administers with a prefilled syringe. **NOT** intra-articular (no needle into the gout joint itself; that's a totally different procedure used for IA corticosteroid injection or the chassis-pending IA uricase concept at [`chassis-pending-interventions.md` §6](./chassis-pending-interventions.md)). Mechanism: recombinant IL-1 receptor antagonist (IL-1Ra) competitively blocks IL-1β signaling — aborts flare within hours via the same CP5a chokepoint as canakinumab, but daily SC dosing vs canakinumab's monthly SC + ~100× lower cost. Side-effect profile: injection-site reactions (most common), low infection-risk signal at the 3-day acute-use protocol (label cautions about TB / fungal infection are for chronic immunosuppression-tier use). Vs prednisone 30-40 mg/day × 2-week taper: anakinra is **faster onset (hours vs days), narrower mechanism (single pathway block vs system-wide glucocorticoid receptor), cleaner cumulative side-effect burden over years of recurrent flares** (no bone loss, no glucose intolerance, no adrenal suppression, no mood / sleep / BP effects). Cost: ~$300/dose, ~$900/flare for the 3-day protocol; insurance coverage variable for off-label use. Access: rheumatologist or forward-thinking internist willing to prescribe off-label. **Bridge until the inhaled mRNA-IL-1RA modality exists** ([`chassis-pending-interventions.md` §4](./chassis-pending-interventions.md), 5–10 year development horizon per [comp-033](./computational-experiments.md) partner-tier analysis); anakinra is the same mechanism + same chokepoint, just SC delivery instead of pulmonary mRNA.
- **Compounding-pharmacy access (requires physician partner; not DIY)** — a 503A compounding pharmacy can prepare custom formulations along two distinct tracks. **(a) Discovery-engine repurposing candidates:** drugs not currently used for gout but identified as hitting gout chokepoints. **Disulfiram** (CP6b GSDMD blockade) is the highest-priority candidate; 503A-eligible via Tier 2 (component of FDA-approved drug); **dose modeling completed as [comp-027](./disulfiram-dose-modeling-computational.md) 2026-05-16 → YELLOW-leaning-GREEN: narrow sub-AUD window centered on 100 mg/day (range 75–125 mg/d), where parent DSF Cmax engages GSDMD at 1.3× IC50 while Me-DTC stays at DER hypotension threshold.** Two-phase compounding protocol: IR capsule 50→100 mg/d titration over 14 days, then ER lipid-matrix 100 mg QD chronic. Zileuton (CP6a 5-LOX), pentostatin (ADA), and lesinurad (URAT1, FDA-approved 2015, commercially withdrawn 2019 for business reasons — Tier 2 eligibility survives per 21 CFR 216.24) are all 503A-eligible via Tier 2 but have supplier-side bulk-API supply questions. **(b) Custom-dose formulations of established gout drugs:** allopurinol (pediatric/weight-based doses, liquid suspensions), colchicine (low-dose ER for prophylaxis, fixed-dose combos), probenecid (ER for QD dosing, combinations). These are 503A-eligible via Tier 1 (USP monograph) — no regulatory uncertainty; the question is whether a custom formulation clinically outperforms the commercial product. Full per-compound tier mapping at [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md). Path requires a rheumatology / functional-medicine prescriber.

### Future (Open Enzyme pipeline — none shipping yet, Phase 0)

- Engineered koji secreting uricase in the gut lumen ± lactoferrin → [koji-endgame-strain](./koji-endgame-strain.md)
- Engineered LBP probiotics → [engineered-lbp-chassis](./engineered-lbp-chassis.md)
- siRNA-URAT1 for genotype-targeted under-excretors → [sirna-urat1-modality](./sirna-urat1-modality.md)

---

## Androgen-elevated path

If you have high endogenous testosterone, are on TRT, or are taking Clomid/enclomiphene/anastrozole. Androgens upregulate URAT1 (the kidney transporter that reabsorbs urate from urine back into the blood) and may indirectly increase serum UA. The stack should include URAT1 countermeasures.

**Important context — the H07 reframe.** The Clomid-elevates-UA observation has a recent mechanistic update. The old model said "androgens directly suppress ABCG2 via the androgen receptor." Comp-016 + comp-017 + the H07 hypothesis card argue the actual mechanism is **estradiol-pathway antagonism** — Clomid blocks an estradiol → PI3K/Akt → ABCG2 induction signal that males largely lack at baseline. Implications for stack design:

- **Aromatase inhibitors (anastrozole, letrozole) and DIM are *more unfavorable* than the supplement-industry default suggests.** They reduce E2 substrate for the same pathway Clomid is already blocking — likely additive to UA elevation.
- **Direct urate-axis modulators (cordycepin, eurycomanone, butyrate, carnosine) are *more favorable*.** They bypass the ER pathway entirely.
- See [H07 clomid intestinal-ER antagonism](./hypotheses/H07-clomid-intestinal-er-antagonism.md) for the full mechanism.

### Today

All [Default path → Today](#today-start-in-the-next-24-hours) entries apply. Plus:

- **Avoid AIs and DIM** unless prescribed for other reasons. Estrogen-pathway suppression worsens the gout picture in this group.

### This month

- **Carnosine** — 500–1,000 mg/day oral L-carnosine (split doses preferred). URAT1 + GLUT9 downregulation in animal models; specific countermeasure for androgen-driven UA elevation. [Catalog →](./supplements-stack.md#carnosine-l-carnosine-β-alanyl-l-histidine--dual-ua--nlrp3)
- **Tongkat ali (Physta, standardized)** — 200 mg/day, standardized to 0.8–1.5% eurycomanone. PRPS-mediated purine-synthesis suppression (eurycomanol, PMID 34785103) + multi-target transporter modulation (URAT1↓, GLUT9↓, ABCG2↑, NPT1↑). 2021 RCT showed SUA ↓7–11% (n=105). The XO-inhibition claim circulating in supplement-industry summaries is a [citation-laundering artifact (comp-015 v2)](./t-axis-adjuvant-urate-mapping-computational.md) — the actual mechanism is transporter modulation + PRPS suppression. [Catalog →](./supplements-stack.md#tongkat-ali-eurycoma-longifolia--physta--lj100--dual-t-axis--ua-favorable)
- **Cordycepin (whole-fermentate Cordyceps OR pure-cordycepin nutraceutical at 100–500 mg/day)** — URAT1 downregulation. Reality check: standard fruiting-body extracts deliver only ~3–4 mg cordycepin per serving (sub-therapeutic). Use a pure-cordycepin product or commit to home Cordyceps fermentation. See [medicinal-mushroom-complement-track](./medicinal-mushroom-complement-track.md).

### This year

- Genotype yourself (ABCG2 Q141K is high-prevalence in this demographic and changes the stack — see [Q141K-positive path](#q141k-positive-path) if you test positive).
- Self-experiment with rigor — n=1 monthly SUA tracking is genuinely valuable to the field if you're willing to share the data.

---

## Q141K-positive path

If you've genotyped and you're heterozygous or homozygous for ABCG2 Q141K (rs2231142), your gut-lumen secretion pathway is partially compromised at baseline. The stack tilts toward **ABCG2-rescue compounds** alongside standard intervention.

> **Why this matters more than for the default path:** ABCG2 normally secretes ~30% of daily urate into the gut lumen. Q141K reduces that capacity. Compounds that *boost* ABCG2 expression or function become especially relevant; compounds that *antagonize* ABCG2 become especially harmful. See [abcg2-modulators](./abcg2-modulators.md) for the full ABCG2 axis discussion and [intestinal ABCG2 sex dimorphism (comp-017)](./intestinal-abcg2-sex-dimorphism-public-data-mining-computational.md) for the disease-state vs. baseline framing.

### Today

All [Default path → Today](#today-start-in-the-next-24-hours) entries.

### This month

- **Sulforaphane (broccoli sprouts)** — ~50 mg/day supplement, OR 100–150 g/day raw broccoli sprouts (must be raw/freshly chopped to preserve myrosinase). HDAC inhibitor at the food-grade level; partial Q141K rescue mechanism documented in vitro. [Catalog →](./supplements-stack.md#sulforaphane-broccoli-sprouts)
- **Lactoferrin** — direct relevance for Q141K because the lactoferrin → TNFα → ABCG2 derepression mechanism is especially valuable in a group with already-compromised baseline ABCG2.
- **EGCG (standardized green tea extract)** — 400–800 mg EGCG/day OR 3–5 cups matcha/day. Wide-spectrum NLRP3 + transporter modulation. Caveat: high-dose EGCG can be a functional ABCG2 *inhibitor* — start at the low end (400 mg) and watch SUA trajectory. [Catalog →](./supplements-stack.md#egcg-green-tea-catechin--widest-spectrum-natural-compound)

### This year

- Self-experiment with rigor — Q141K-positive responders are who Open Enzyme's gut-lumen-sink thesis depends on most, so good n=1 data here is genuinely valuable.
- Watch [comp-018 — upstream complement modulator sweep](./upstream-complement-modulator-sweep-computational.md) (Phase 1 complete 2026-05-08; **rosmarinic acid** + **luteolin** + **Bupleurum polysaccharides** as upstream-CP0 dietary candidates — note: a brief-scrubbed verification re-run as [comp-020](./upstream-complement-verification-rerun-computational.md) flagged that comp-018's headline-promotion of rosmarinic acid was contaminated by user phrasing in the brief; *Helicteres* benzofuran lignans actually beat rosmarinic acid 4-20× on matched-assay potency — see retrospective at `operations/comp-018-vs-comp-020-retrospective.md`) and [food-grade HDACi screen (comp-007)](./food-grade-hdaci-screen-computational.md) for new candidate ABCG2-rescue compounds.

---

## Active flare

You are in pain right now. **Standard medical care is the priority** — colchicine, NSAID, or steroid as your physician directs. The supplements below are *adjuncts*, not replacements.

### Today (during the flare)

- **Hydrate aggressively** — >4 L/day water.
- **Tart cherry concentrate** — push to 16–20 oz/day during flare. Strongest acute-flare evidence among supplements.
- **Omega-3** — push to 4–6 g/day during flare.
- **Topical CBD + THC (1:1 ratio, high-mg/oz formulation) applied to the affected joint, plus ice.** CB2 receptor activation on synovial macrophages and infiltrating neutrophils suppresses NLRP3 inflammasome assembly and reduces IL-1β release — same downstream chokepoint as colchicine (CP3/CP2), reached via a different receptor. Topical TRPV1 desensitization plus the cooling component (typically menthol / TRPM8 agonist) adds thermoreceptor-mediated pain reduction at the site. Beta-caryophyllene (CB2-selective agonist) and CBG have direct MSU-model evidence for inflammasome suppression — see [`cannabinoids-terpenes.md`](./cannabinoids-terpenes.md) §1 + §2 for the full mechanism and sourcing detail. Practical protocol: ice 10–15 min → apply topical 1:1 THC:CBD → ice again 30–60 min later. For more severe presentations or systemic effect, oral or inhaled THC:CBD adds systemic CB1/CB2 activation. **In recurrent-flare patients with significant cumulative steroid burden, this protocol may reduce or replace the need for prednisone dose escalation during a step-down rebound.** Cannabis is jurisdiction-dependent and requires medical-program access in many places. *[In Vitro / Animal Model — direct human gout-flare RCT evidence absent; mechanistic + indirect evidence base in cannabinoids-terpenes.md]*
- **Avoid:** ketogenic states, intermittent fasting, alcohol, organ meats, high-fructose foods. All transiently raise UA and can extend the flare.
- **Avoid BHB / exogenous ketones during a flare.** Ketosis competes with urate for renal MCT/URAT1 reabsorption — transient UA rise of 5–10% is documented and can compound the flare. **However, note (2026-05-19):** during an *untreated* active flare, the body's HPA axis is already engaged — 24h UFC rises ~58% above interval baseline, driving cortisol-mediated urate excretion that *lowers* serum UA via URAT1 downregulation + XOR induction (Zhang 2023, PMC9989260). So serum UA dynamics during an *untreated* flare are complex: inflammation-driven UA excretion ↓ SUA, ketone competition ↑ SUA, net direction depends on which effect dominates. The conservative recommendation (suspend BHB/ketosis during flare) remains right because the variance is high and adding a known UA-elevating intervention to an unstable system is risky. See [cortisol-fasting-glucocorticoid-inflammasome-lit-scan-2026-05-19](../logs/cortisol-fasting-glucocorticoid-inflammasome-lit-scan-2026-05-19.md) for the full evidence map.

### Combined-route flare protocols — mechanism-non-redundant stacking (added 2026-05-19)

Two named combined protocols for active flare. Both leverage **mechanism-non-redundant convergence on NLRP3** through independent receptor pathways and delivery compartments. *[Speculative; mechanism-composition logic, no human gout RCT for either combination as named.]*

**Protocol A — Colchicine + topical CBD:THC (for users on colchicine).** Two independent receptor pathways reaching the same chokepoint:
- **Oral colchicine** (1.2 mg + 0.6 mg at 1 hour per AGREE trial) → β-tubulin binding → CP3 ASC speck blockade + CP2 P2X7 pore inhibition (intracellular, systemic)
- **Topical 1:1 CBD:THC** on affected joint → CB2 GPCR on synovial macrophages → CP2 NLRP3 conformational suppression (plasma-membrane, local)
- The two arms hit CP2 via completely different molecular mechanisms (tubulin/P2X7 vs. CB2 Gαi-coupled signaling) and reach the joint via different compartments (oral systemic vs. transdermal local). Mechanism-non-redundant. Not a replacement for either arm alone; a layered acute-flare strategy. See [`colchicine.md`](./colchicine.md) §3.3.1 and [`cannabinoids-terpenes.md`](./cannabinoids-terpenes.md) §4a for the per-arm mechanism details.

**Protocol B — Prednisone + topical CBD:THC + inhaled cannabinoid + ice (four-route layered, n=1 anchor).** Brian's actual protocol used during a 2026-05 prodromal rebound after disc-golf overexertion. Mechanism layering:
- **Prednisone** (on existing taper) → systemic glucocorticoid receptor activation → NLRP3, IL-1β, NOS2, ACOD1 transrepression at CP1+CP2 (timing-aligned: per H2 lit scan [`logs/cortisol-fasting-glucocorticoid-inflammasome-lit-scan-2026-05-19.md`](../logs/cortisol-fasting-glucocorticoid-inflammasome-lit-scan-2026-05-19.md), GR works AFTER LPS priming, which is exactly the prodromal / mid-flare window)
- **Topical CBD:THC** → local CB2 → CP2 (transdermal local)
- **Inhaled cannabis** → systemic CB1/CB2 → CP2 (systemic) — different compartment than topical
- **Ice cycling** → TRPM8 nociceptive blunting + tissue temperature drop + cold-induced anti-inflammatory effect (local)
- Three layered interventions converging on CP1+CP2 via three distinct cellular compartments + one peripheral nociceptive intervention. See [`cannabinoids-terpenes.md`](./cannabinoids-terpenes.md) §4a for the n=1 observation anchor.

**Which protocol fits which user:** Protocol A is for users already on colchicine with no contraindications (renal function adequate, no statin/macrolide/cyclosporine drug-interaction surface). Protocol B is for users on prednisone (acute or taper) where the colchicine drug-interaction surface is unacceptable or where colchicine isn't part of the regimen. Both are layered onto whatever urate-lowering therapy is in place; both target acute-flare inflammation, not chronic hyperuricemia.

### Once the flare resolves (1–2 weeks)

- Return to maintenance stack from the path that fits your situation.
- **Log the flare** (date, suspected trigger, severity, duration). Pattern recognition is the highest-leverage thing you can do for yourself. See [self-experiment-protocol](./self-experiment-protocol.md).

---

## On a urate-lowering drug

You're already on allopurinol or febuxostat. The drug is doing the XO suppression; the supplement stack should target *complementary* mechanisms (NLRP3 inflammation, ABCG2 secretion, ROS, gut-lumen sink).

### Today

All [Default path → Today](#today-start-in-the-next-24-hours) entries — none antagonize allopurinol/febuxostat.

- **Avoid sustained heavy ketosis** if your UA is borderline-controlled — transient UA rise on top of the drug can still trigger a flare.

### This month

- **Lactoferrin** — TNFα-mediated ABCG2 derepression is mechanistically distinct from XO suppression, so it stacks cleanly.
- **Sulforaphane** — ABCG2-axis support (Mechanistic Extrapolation).
- **Omega-3 + NAC** — NLRP3 axis. You can have low UA on allopurinol and still flare from residual MSU crystals; these address the inflammatory side independently of UA level.

### This year

- **Genotype if you haven't** — HLA-B\*58:01 carriers have a high allopurinol allergy / SCAR risk. Clinically actionable. See [personal-genome-protocol](./personal-genome-protocol.md).
- Self-experiment under physician supervision to test whether the adjunct stack lets you reduce allopurinol dose.

---

## Prevention path

No flare yet. Family history, borderline UA, or just want to avoid the trajectory.

### Today

- Diet baseline (cut HFCS, hydrate, moderate purines).
- Tart cherry at maintenance dose.

### This month

- Omega-3 at maintenance dose (3–4 g/day).
- Add NAC if your stack tolerates it.
- Establish baseline: SUA every 6 months. Track your personal trajectory before something happens.

### This year

- Genotype to know your variant-driven risk.
- Watch this guide for updates as Open Enzyme's research pipeline matures.

---

## How this page stays fresh

This page is **not** auto-updated by the wiki sweep daemon. The sweep daemon propagates findings *between* research wiki pages; promotion to this application surface is currently a **manual review pass**.

The plan: a `fresh-stack.py` script (sibling to the existing `fresh-synthesis.py`) that scans the research wiki for findings that should be reflected here but aren't, surfaces them as a promotion-candidate report, and lets a human review and accept the propagation. Until that script exists, the propagation discipline is: research findings live in their canonical pages; this page is updated by hand whenever a finding crosses the maturity threshold for action recommendations.

If you find a finding in the research wiki that should be reflected here but isn't, that's a propagation gap — open an issue or a PR.

See [synthesis/strategic-reflections/](../synthesis/strategic-reflections/) for the platform-architecture reflection on whether the daemon should eventually grow a propagation-to-application-surface pass.

---

## Cross-references

- [Supplements stack catalog](./supplements-stack.md) — per-compound depth, dose, contraindications, drug interactions, stack-level antagonisms
- [Gout pathophysiology](./gout-pathophysiology.md) — multi-track urate transporter coverage map; mechanisms behind the actions on this page
- [Open Enzyme vision](./etc/open-enzyme-vision.md) — the platform's broader thesis and pipeline
- [Self-experiment protocol](./self-experiment-protocol.md) — how to run rigorous n=1 on yourself
- [Personal genome protocol](./personal-genome-protocol.md) — MinION-based pharmacogenomics + strain QC
- [Research index](../index.md) — full wiki dashboard with all concepts and primary research
