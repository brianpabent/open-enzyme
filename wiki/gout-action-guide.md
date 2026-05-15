---
title: "Gout Action Guide — what to do, by situation"
date: 2026-05-08
tags: ["application-surface", "patient-guide", "gout", "stack-design", "decision-tree"]
related:
  - supplements-stack.md
  - gout-pathophysiology.md
  - open-enzyme-vision.md
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

- **Get genotyped via clinical-grade testing** — order ABCG2 Q141K (rs2231142), SLC2A9, URAT1 variants through a clinical-grade lab (e.g., via your rheumatologist or a direct-to-consumer clinical service that returns CLIA-grade results). Changes the stack design substantially. Consumer panels (23andMe, AncestryDNA, etc.) are not recommended here — the raw SNP data quality is uneven for the specific variants gout stack design depends on, and the terms-of-service surrounding consumer-genomics data ownership are worth reading before submitting. See [personal-genome-protocol](./personal-genome-protocol.md) for ordering paths.
- **Self-experiment with rigor** — log SUA monthly, track flares, A/B test compounds. See [self-experiment-protocol](./self-experiment-protocol.md).
- **Compounding-pharmacy access (requires physician partner; not DIY)** — a 503A compounding pharmacy can prepare custom formulations along two distinct tracks. **(a) Discovery-engine repurposing candidates:** drugs not currently used for gout but identified as hitting gout chokepoints. **Disulfiram** (CP6b GSDMD blockade) is the highest-priority candidate; 503A-eligible via Tier 2 (component of FDA-approved drug); off-label dose modeling queued as [comp-027](./computational-experiments.md). Zileuton (CP6a 5-LOX), pentostatin (ADA), and lesinurad (URAT1, FDA-approved 2015, commercially withdrawn 2019 for business reasons — Tier 2 eligibility survives per 21 CFR 216.24) are all 503A-eligible via Tier 2 but have supplier-side bulk-API supply questions. **(b) Custom-dose formulations of established gout drugs:** allopurinol (pediatric/weight-based doses, liquid suspensions), colchicine (low-dose ER for prophylaxis, fixed-dose combos), probenecid (ER for QD dosing, combinations). These are 503A-eligible via Tier 1 (USP monograph) — no regulatory uncertainty; the question is whether a custom formulation clinically outperforms the commercial product. Full per-compound tier mapping at [`compounding-pharmacy-track.md`](./compounding-pharmacy-track.md). Path requires a rheumatology / functional-medicine prescriber.

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
- **Avoid:** ketogenic states, intermittent fasting, alcohol, organ meats, high-fructose foods. All transiently raise UA and can extend the flare.
- **Avoid BHB / exogenous ketones during a flare.** Ketosis competes with urate for renal MCT/URAT1 reabsorption — transient UA rise of 5–10% is documented and can compound the flare.

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
- [Open Enzyme vision](./open-enzyme-vision.md) — the platform's broader thesis and pipeline
- [Self-experiment protocol](./self-experiment-protocol.md) — how to run rigorous n=1 on yourself
- [Personal genome protocol](./personal-genome-protocol.md) — MinION-based pharmacogenomics + strain QC
- [Research index](../index.md) — full wiki dashboard with all concepts and primary research
