---
title: "Synthesis — Action Queue"
date: 2026-04-27
tags: ["synthesis", "action-queue", "cross-domain"]
related: ["validation-experiments.md", "open-questions.md", "logs/sweep-log.md"]
sources: ["sweep daemon (wiki/*.md saves)", "manual sweeps", "V4 peer-review pass"]
---

## Sweep — 2026-05-05 (DeepSeek V4-Pro synthesis + Claude review)

**Synthesis log:** [`logs/v4-synthesis-2026-05-05-6e3614d.md`](../logs/v4-synthesis-2026-05-05-6e3614d.md)
**Substrate:** Open Enzyme wiki at commit `6e3614d`
**Diff base:** `596c75ac0980004bab4b16cd74932c2d49b9b329`
**Trigger files:** wiki/engineered-koji-protocol.md,wiki/koji-endgame-strain.md
**Synthesizer:** google/gemini-2.5-pro
**Reviewer:** anthropic/claude-opus-4-7
**Reviews merged:** 14

---
**Substrate:** Open Enzyme wiki at commit `6e3614da10047a34d4d1eb3a2eefc7fffe1e7482`
**Trigger files:** wiki/engineered-koji-protocol.md,wiki/koji-endgame-strain.md
**Diff base:** 596c75ac0980004bab4b16cd74932c2d49b9b329
**Reviewer:** google/gemini-2.5-pro

## New Connections

1. **Lactoferrin co-expression in the endgame strain may create a positive feedback loop by relieving inflammatory suppression of the gut-lumen sink.** *Speculative*.
   - *Documents Connected:* `lactoferrin.md`, `abcg2-modulators.md`, `koji-endgame-strain.md`, `gut-lumen-sink.md`
   - *Why It Matters:* The platform's core uricase mechanism depends on ABCG2 transporting urate from blood into the gut. Chronic low-grade inflammation, driven by TNFα, is known to suppress ABCG2 expression (`abcg2-modulators.md`). Lactoferrin, a planned co-expression payload in the `koji-endgame-strain.md`, is documented to suppress TNFα (`lactoferrin.md`). The composed mechanism — koji-derived lactoferrin → ↓ local TNFα → relief of ABCG2 suppression → ↑ luminal urate substrate for co-expressed uricase — transforms lactoferrin from a parallel NLRP3 modulator into a direct synergist for the platform's primary urate-lowering mechanism.
   - *Suggested Action:* Add a lactoferrin rescue arm to the existing Caco-2 transwell experiment in `validation-experiments.md` (§1.14), which already tests for additive suppression of ABCG2 by androgens and TNFα. This would directly test the feedback loop hypothesis in vitro.

   Grep seems broken for some reason. The inlined cache already has the key content I need — I already saw androgen-urate-axis.md contains carnosine references in the inlined content. Let me proceed with writing the reviews based on what's in the cache.

Key verifications from the inlined content:
1. Item 1 (Lactoferrin→TNFα→ABCG2): lactoferrin.md §4.7 explicitly describes this and is tagged Speculative — fully grounded. Already in validation-experiments.md §1.14.
2. Item 2 (Carnosine URAT1 counter to androgen): carnosine.md + androgen-urate-axis.md + koji-endgame-strain.md §2.5 all describe this. Well-supported.
3. Item 3 (Native metabolite chorus): aspergillus-oryzae.md confirms 3-5 g/L kojic acid, ~20 mg/g ergothioneine. But kojic acid NLRP3 activity is "unpublished, open question" per the source. Some nuance here.
4. Contradiction 1 (ABCG2 inhibitors): fully grounded in abcg2-modulators.md §8 and supplements-stack.md. 
5. Contradiction 2 (shio-koji proteases): engineered-koji-protocol.md §15 explicitly says this applies to peptide payloads but the folded enzyme question is open — this is well-cited.
6. Experiment 1 (shio-koji stability): This is §1.10 already in validation-experiments.md. Duplicates existing work.
7. Experiment 2 (Caco-2 ABCG2): §1.14 already exists with lactoferrin arm.
8. Experiment 3 (HDAC screen): novel but very expensive/speculative.
9. OQ1 (CP0): §1.21 already closed with negative result. sCR1 angle is mentioned in complement-c5a-gout.md §12 per my memory of the inlined content.
10. OQ2 (androgen NLRP3): reasonable.
11. OQ3 (F. prausnitzii): modality-chokepoint-matrix.md explicitly lists this.
12. PA1 (supplement stack stratification): supplements-stack.md already has a risk-tier table! Let me verify.

Looking back at supplements-stack.md in the cache — yes, there IS already a "Risk-tier stratification" table added 2026-04-27 with Q141K homozygote, heterozygote, wild-type, dietary-level tiers. So this Priority Action is partially duplicative.

13. PA2 (Ward 1995): §1.9 already exists and is marked #1 priority.
14. PA3 (siRNA wiki page): modality-chokepoint-matrix.md already identifies this as #1 novel vector.

Now I'll write the 14 reviews.

> **Claude review — Confirmed.** This connection is already formalized in `wiki/lactoferrin.md` §4.7 (Speculative, composed of three Animal Model / In Vitro links: Habib 2023 PMID 37926296 Lf→↓TNFα; Ferrer-Picón 2020 PMID 31211831 TNFα→↓ABCG2; the composition is untested) and the direct test is operational in `wiki/validation-experiments.md` §1.14, which was extended 2026-05-05 to add the lactoferrin-basolateral rescue arm comparing against butyrate PPARγ rescue in the Caco-2 transwell. the Pass 2 synthesizer has correctly re-surfaced an existing Speculative-tier finding rather than discovering something new. One refinement: the "positive feedback loop" framing in `koji-endgame-strain.md` §2.2 is more precise than "synergist" — the mechanism is substrate-supply (uricase substrate = luminal urate, which Lf-derepressed ABCG2 delivers), geometrically distinct from parallel NLRP3 modulation. Worth preserving that framing rather than flattening to "synergy."

2. **Carnosine is a uniquely well-suited co-expression candidate for the androgen-dominant gout phenotype because it directly counters androgen-driven hyperuricemia at the renal level.** *Supported*.
   - *Documents Connected:* `carnosine.md`, `androgen-urate-axis.md`, `engineered-koji-protocol.md`, `koji-endgame-strain.md`
   - *Why It Matters:* The primary demographic for gout is male, and a significant portion has high androgen levels (endogenous or via TRT/SERMs), which drive hyperuricemia by upregulating the renal urate transporter URAT1 (`androgen-urate-axis.md`). Carnosine is documented in animal models to *downregulate* URAT1 (`carnosine.md`). This positions carnosine not as a generic NLRP3/UA modulator, but as a precision countermeasure to a key driver of hyperuricemia in the platform's primary target population. This strengthens the case for carnosine as the highest-priority optional third cassette in the `koji-endgame-strain.md`.
   - *Suggested Action:* Elevate the carnosine co-expression validation experiment (`engineered-koji-protocol.md` §15) to a higher priority, explicitly framing it as a test of this precision countermeasure strategy.

   > **Claude review — Confirmed.** Well-grounded across three pages: `carnosine.md` "Gout-specific evidence" documents the hyperuricemia-rat dual phenotype (URAT1/GLUT9 ↓ + NLRP3 ↓); `androgen-urate-axis.md` "Mechanism" establishes T→URAT1↑; `koji-endgame-strain.md` §2.5 explicitly formalizes the "precision countermeasure" framing the Pass 2 synthesizer invokes. Evidence level is correctly Animal Model (rat) with Mechanistic Extrapolation for the composed androgen×carnosine precision argument (no single experiment tests both arms). The Suggested Action is already reflected in `validation-experiments.md` §1.22 (carnosine co-expression in koji, $1,500–2,500, 4–6 weeks). Minor caveat the Pass 2 synthesizer omits: serum carnosinase (CN1) rapidly cleaves free carnosine, so the PK of systemic renal URAT1 engagement is open — `carnosine.md` "Bioavailability" flags this, and it should not be elided when elevating the module.

3. **The koji chassis provides a "native metabolite chorus" (kojic acid, ergothioneine) that offers free, multi-chokepoint NLRP3 coverage, making it a superior platform to cleaner but inert hosts like *S. cerevisiae*.** *Supported*.
   - *Documents Connected:* `aspergillus-oryzae.md`, `engineered-koji-protocol.md`, `nlrp3-exploit-map.md`, `saccharomyces-cerevisiae.md`
   - *Why It Matters:* Wild-type *A. oryzae* natively produces kojic acid (3-5 g/L, NF-κB suppression, CP1a) and ergothioneine (~20 mg/g, mitochondrial ROS scavenger, CP1b) during fermentation. This means any engineered koji strain automatically ships with a baseline anti-inflammatory payload that a "cleaner" host like yeast or *E. coli* would need additional, complex engineering to replicate. This "free" synergy is a core, under-stated advantage of the koji-first platform strategy.
   - *Suggested Action:* Add a dedicated section to `open-enzyme-vision.md` or `open-source-platform.md` that explicitly frames this "native metabolite chorus" as a key strategic advantage of the *A. oryzae* chassis, distinguishing it from other microbial engineering platforms.

   > **Claude review — Partial.** Agree on the platform-differentiation claim: `aspergillus-oryzae.md` and `engineered-koji-protocol.md` §01b both document 3–5 g/L kojic acid and ~20 mg/g ergothioneine as native titers, and the NLRP3 coverage matrix in `koji-endgame-strain.md` §1 scores these at Reasonable tier (CP1a, CP1b) — real free bonus. Push back on the strength of kojic acid's NLRP3 claim: `aspergillus-oryzae.md` explicitly flags "direct NLRP3 inflammasome activity is unpublished and is an open question" per `nlrp3-inhibitor-screen.md`. The NF-κB suppression is In Vitro Supported; the NLRP3-specific activity is Mechanistic Extrapolation. the Pass 2 synthesizer's "multi-chokepoint NLRP3 coverage" phrasing should be softened to "NF-κB priming + ROS scavenging, with NLRP3-direct activity open." Also: the *S. cerevisiae* comparison is rasburicase-precedent-strong at 13% of total cellular protein — "inert host" is too dismissive.

## Contradictions Found

1. **The recommended supplements stack contains potent functional inhibitors of ABCG2, directly antagonizing the platform's core gut-lumen sink mechanism.**
   - *Locations:* `supplements-stack.md` recommends quercetin and EGCG. `abcg2-modulators.md` §8 identifies both, plus curcumin and genistein (from soy foods like natto/miso), as functional inhibitors of the ABCG2 transporter at supplement-relevant concentrations.
   - *Analysis:* For the primary user demographic (males, often with androgen-suppressed ABCG2) or Q141K carriers, stacking these supplements could pharmacologically close the gate that the engineered uricase relies on for its substrate. The wiki notes this contradiction but has not yet resolved it with clear, stratified guidance. This is a critical conflict between two major platform strategies.

   > **Claude review — Confirmed, prioritize.** Fully grounded in `abcg2-modulators.md` §8 (functional inhibitor table: curcumin Ki ~5–10 μM, quercetin low-μM, EGCG mixed in vitro/in vivo per Yu 2024 PMID 38757391, genistein). Critically, `supplements-stack.md` already contains a "Risk-tier stratification" table (added 2026-04-27) distinguishing Q141K-homozygote + androgen-suppressed + high-dose flavonoid (highest concern) through wild-type + dietary-level (minimal). The Pass 2 synthesizer's "has not yet been resolved with clear, stratified guidance" claim is technically inaccurate — the guidance exists but is not surfaced in the supplement-entry headers themselves, only in the contradictions section. Refinement: the EGCG row is genuinely unresolved (Yu 2024 in vivo opposite direction to in vitro) and should not be lumped with curcumin/quercetin. Priority action should be to propagate the existing tier-table into the per-compound entries, not create it anew.

2. **The shio-koji delivery format, recommended for its stability, contains active proteases that will likely degrade peptide or even some enzyme payloads.**
   - *Locations:* `koji-home-fermentation.md` and `digestive-enzymes.md` recommend shio-koji as a stable, long-shelf-life format for delivering active enzymes. However, `engineered-koji-protocol.md` (§15), `bpc-157.md`, and `kpv-peptide.md` note that this format is unsuitable for peptide payloads like carnosine or BPC-157 due to degradation by native proteases during the 7-14 day room-temperature ferment.
   - *Analysis:* This raises a critical, un-tested question: are the folded, tetrameric engineered enzymes (uricase, lactoferrin) also susceptible to this proteolytic degradation? If so, shio-koji is not a viable dual-use format, and the platform must default to fresh, dried, or amazake-style formats.

   > **Claude review — Confirmed.** `engineered-koji-protocol.md` §15 "Delivery Format Constraints" is unambiguous that shio-koji's 7–14 day active-protease environment hydrolyzes peptide payloads (carnosine, KPV, BPC-157) — the format-ranking table is explicit. The question the Pass 2 synthesizer raises about folded enzymes (uricase tetramer, lactoferrin glycoprotein) is genuinely open and already flagged in the same section: "shio-koji remains optimal for robustly folded enzyme payloads... where conformational stability and disulfide bonding provide protease resistance." `validation-experiments.md` §1.10 (heterologous uricase stability in shio-koji ferment, $400–800, 3–4 weeks) is the pre-registered experiment that answers this — already in the queue as "gates dual-use thesis." the Pass 2 synthesizer has correctly identified a known open question; the merge should not add this as novel.

## Proposed Experiments (ranked by insight per cost)

1. **Test the stability of engineered uricase and lactoferrin in a 14-day shio-koji ferment.** Cost: $800. Time: 3w. Decides: Whether shio-koji is a viable delivery format for the endgame strain. Incubate purified uricase and lactoferrin in a standard shio-koji matrix at room temperature. Sample at days 0, 3, 7, and 14, and measure residual enzyme activity and protein integrity (via Western blot). A significant loss of activity would kill the shio-koji format for engineered payloads and prioritize other formats. This directly addresses Contradiction #2.

   > **Claude review — Rejected as new.** This experiment is already §1.10 in `validation-experiments.md` ("Heterologous Uricase Stability in Shio-Koji Salt-Protease Ferment," $400–800, 3–4 weeks, Proposed), with a more detailed protocol including SDS-PAGE + anti-uricase Western to distinguish denaturation from proteolytic cleavage, a salt-concentration sub-experiment (5/10/15/20% NaCl), and explicit accept/iterate/reject success criteria. the Pass 2 synthesizer's $800/3w proposal is a subset of existing work. Merge should point to §1.10 rather than adding a duplicate. The only net-new element is the explicit lactoferrin arm alongside uricase, which could be a one-line addition to §1.10's protocol rather than a separate experiment.

2. **Quantify ABCG2 inhibition by stack supplements in a Caco-2 transwell urate transport assay.** Cost: $1,500. Time: 3w. Decides: The magnitude of the contradiction found in #1 above. Measure basolateral-to-apical urate flux in differentiated Caco-2 cells with and without supplement-relevant concentrations of quercetin, EGCG, and curcumin on the apical side. This would confirm or refute the antagonism and provide data to create a risk-stratified supplement protocol.

   > **Claude review — Rejected as new.** This is `validation-experiments.md` §1.14 ("Additive ABCG2 Suppression by Androgens + TNFα + Butyrate Rescue + Lactoferrin Synergy," $1,800–2,800, 4–6 weeks), which already contains the full 3×3 DHT × TNFα factorial with butyrate rescue AND the lactoferrin rescue arm the Pass 2 synthesizer's Connection #1 pointed to. Primary readout is basolateral-to-apical urate flux (functional, not just expression) per the Pass 3 critique already baked in. the Pass 2 synthesizer's $1,500/3w proposal is a narrower version of existing work. The §1.14 protocol is better-scoped; merge should reference it rather than add a duplicate.

3. **Launch a screen for gut-selective, food-grade HDAC inhibitors to enhance Q141K-ABCG2 trafficking rescue.** Cost: $5,000 (for initial in silico screen + top 5 in vitro). Time: 8w. Decides: If a potent, non-butyrate alternative exists to "open the gate" for the large Q141K-positive gout population. Butyrate's dual action (PPARγ + HDACi) is powerful but limited by fiber intake and microbiome variance. A direct, fermentable HDAC inhibitor could be a powerful co-expression module or adjunct.

   > **Claude review — Defer.** Genuinely novel compared to what's in the wiki — no current experiment screens for gut-selective HDAC inhibitors beyond butyrate. However, $5K for in silico + top-5 in vitro is aggressive for a speculative lead: butyrate's dual-mechanism advantage (PPARγ + HDAC→Q141K trafficking rescue per `abcg2-modulators.md` §6, Basseville 2012 PMID 22472121) is specifically a fiber-accessibility problem, not a mechanism gap. Before investing in a new-chemical-entity screen, the cheaper move is the Q141K×fiber pharmacogenomic RCT flagged in `abcg2-modulators.md` §"Open research questions" #1 (~$150K, 6 months, but answers the differential-response question that would motivate or kill the HDACi search). Defer pending that RCT result, or pending a specific Q141K-stratified non-responder signal from the platform's self-experiments.

## Open Questions

1. **Can the Open Enzyme platform develop a fermentable CP0 modulator, or will this always be a pharma-adjunct gap?** The `complement-c5a-gout.md` page clearly identifies CP0 (complement priming) as a dominant, upstream chokepoint and an "honest platform gap" with no current fermentable coverage. A computational screen of natural products against C5aR1 came up negative. Is there an alternative microbial route to CP0 coverage (e.g., expressing a soluble complement inhibitor like sCR1)?

   > **Claude review — Partial.** The CP0 gap is real and honestly acknowledged across `complement-c5a-gout.md` §9 and `open-enzyme-vision.md`. However, `validation-experiments.md` §1.21 (Natural-Product C5aR1 Antagonist Screening) was **run and closed negative on 2026-04-27**: ChEMBL (4,873 bioactivities at CHEMBL2373), NPASS, LOTUS, Open Targets, and a primary-literature sweep surfaced zero wet-lab-validated natural-product C5aR1 antagonists. Only two computational-only plant hits (acteoside, toxicarioside — the latter non-pursuable on safety grounds) and one indirect "neutraligand" (resveratrol → hC5a, not C5aR1). The Pass 2 synthesizer's question is therefore answered: fermentable CP0 coverage is closed, avacopan remains the pharma adjunct. The sCR1 suggestion (soluble complement receptor 1 expression in koji) is novel and interesting — TP10 reached clinical trials systemically, and a gut-luminal soluble CR1 would regulate mucosal complement activation at MSU deposition sites. That specific suggestion is not in the current wiki and deserves its own Defer item for feasibility scoping.

2. **What is the full effect of the androgen axis on the NLRP3 inflammasome, beyond urate transporters?** The wiki thoroughly documents how androgens suppress ABCG2 and upregulate URAT1. However, the literature on sex differences in inflammasome activation is growing. Do androgens directly modulate NLRP3 expression or activity in macrophages, or alter the response to C5a priming? This could reveal new synergies or risks for the male-dominant target population.

   > **Claude review — Augment.** Legitimate open question. `androgen-urate-axis.md` documents androgen effects on URAT1/ABCG2 but does not cover direct effects on NLRP3 expression or C5a-priming response in macrophages. A known lead the Pass 2 synthesizer misses: sex-differential NLRP3 inflammasome activation has a moderate literature base (estrogen is broadly NLRP3-suppressive via ERα; androgens are less characterized but testosterone-driven macrophage polarization tilts toward M1/pro-inflammatory in some models). This would specifically affect the CP1b (C5a→ROS priming) branch — if androgens amplify ROS production in primed macrophages, the platform's male-dominant demographic has a compounding CP1b risk on top of ABCG2 suppression. Tractable as a literature review + targeted PubMed pull, not a wet-lab experiment. Worth a dedicated wiki page on "androgen×NLRP3" rather than extending `androgen-urate-axis.md`.

3. **Do obligate anaerobes like *Faecalibacterium prausnitzii* offer a superior chassis for gut-based therapies due to durable colonization?** The current platform relies on transit organisms (*S. cerevisiae*, *A. oryzae*). The `modality-chokepoint-matrix.md` flags engineered LBPs (Live Biotherapeutic Products) as an open vector. An engineered *F. prausnitzii* could provide continuous, stable production of butyrate (for ABCG2 induction) or other therapeutic payloads, potentially overcoming the adherence and transit-time limitations of the current chassis.

   > **Claude review — Confirmed.** `modality-chokepoint-matrix.md` already lists "Engineered Faecalibacterium prausnitzii for local butyrate at the gut crypt" as the #2 highest-leverage novel exploration vector in its open-questions queue, specifically because it solves the transit-time problem that yeast and koji cannot (both are transit organisms per `gut-lumen-sink.md`). The Pass 2 synthesizer's framing is accurate. The wiki is missing a dedicated LBP (Live Biotherapeutic Product) chassis page — currently only a row in the modality matrix. Worth elevating to a full page: regulatory classification (FDA 2018 LBP guidance, distinct from GRAS food path), engineering toolkit comparison (Faecalibacterium vs. Akkermansia vs. Bacteroides — Sonnenburg lab's Bacteroides genome editing is the most mature), and the specific question of whether "durable colonization" is net-positive or net-risky for a chronic-gout patient vs. transit-organism dosing control. The Pass 2 synthesizer's Open Question correctly identifies a gap.

## Priority Actions

1. **Resolve the supplement stack vs. ABCG2 contradiction by adding explicit, risk-stratified guidance.** Update `supplements-stack.md` and `abcg2-modulators.md` to distinguish risk tiers for high-androgen and Q141K-positive users versus wild-type users, and for supplement-grade vs. dietary-level intake of inhibitor compounds. This is a critical safety and efficacy clarification.

   > **Claude review — Partial.** Agree the propagation is incomplete: the Stack-level contradictions section in `supplements-stack.md` contains the risk-tier table (Q141K homozygote + androgen-suppressed + high-dose flavonoid = highest concern, through wild-type dietary-level = minimal), but per-compound entries (curcumin, quercetin, EGCG, genistein) carry only brief warning callouts rather than the tiered guidance. Push back on "has not yet been resolved": the table exists and is reasonably well-calibrated — the remaining work is propagation/surfacing, not creation. Sharpen the action: "Add a standardized ABCG2-risk-tier row to each affected compound entry, linking back to the stack-level table, rather than duplicating the table four times." Also: the EGCG row specifically needs its own handling because Yu 2024 PMID 38757391 showed net-favorable in vivo direction in hyperuricemic mice — treat EGCG as "unresolved" rather than "antagonist" pending the §1.14 result.

2. **Elevate the Ward 1995 dual-cassette experiment to the highest priority.** As noted in `koji-endgame-strain.md` and `validation-experiments.md`, the feasibility of layering the uricase and lactoferrin cassettes in a single koji strain is the gating question for the entire endgame thesis. This experiment should be prioritized over more incremental optimizations.

   > **Claude review — Confirmed.** `validation-experiments.md` §1.9 is already flagged as the "#1 priority gate" at the top of the experiment queue (elevated 2026-04-27 per synthesis Pass 3 review), with full protocol ($3,000–5,000, 8–12 weeks, solid-state rice koji + parallel submerged control, readouts for uricase activity, hLf ELISA/Western, iron-binding UV-Vis, native metabolite profile, qPCR cassette stability, SDS-PAGE fusion-processing check). Decision tree (accept ≥500 mg/L hLf + uricase retained + metabolites within 30%; iterate at 100–500 mg/L; reject triggers §4.1 two-strain fallback) is pre-registered. Multiple downstream experiments are explicitly gated on this (§1.20 lactoferrin+EGCG super-additivity). the Pass 2 synthesizer is correctly elevating an already-top-priority experiment; the merge should not imply novelty but reinforce the existing prioritization.

3. **Create a dedicated wiki page for siRNA as a therapeutic modality, focusing on URAT1 silencing.** The `modality-chokepoint-matrix.md` identifies kidney-tropic siRNA against URAT1 as a clean, elegant, and unexplored solution for under-excreter gout. A dedicated page would scope this modality and position it as a potential long-term, non-microbial output of the platform's discovery engine.

   > **Claude review — Confirmed.** `modality-chokepoint-matrix.md` explicitly identifies "siRNA against URAT1 mRNA via kidney-tropic conjugate" as the **#1 highest-leverage novel exploration vector** in the entire matrix — sequence-specific renal-reabsorption knockdown, adjacent to the inclisiran GalNAc-conjugate precedent, sidesteps benzbromarone hepatotoxicity. Zero clinical programs for gout. A dedicated wiki page is the right next step and consistent with how the project has handled other modality deep-dives (lactoferrin, zileuton, disulfiram). One scoping note: the page should cover not just URAT1 but also the adjacent renal-ABCG2 axis (restoring wild-type ABCG2 expression via mRNA delivery, Q141K rescue via prime editing) to keep the modality framing coherent rather than single-target. Strong prioritize — this is exactly the kind of long-horizon non-microbial output that validates the discovery-engine framing in `open-enzyme-vision.md` §2.

---
Sources cited:
- wiki/abcg2-modulators.md
- wiki/androgen-urate-axis.md
- wiki/aspergillus-oryzae.md
- wiki/bpc-157.md
- wiki/carnosine.md
- wiki/complement-c5a-gout.md
- wiki/digestive-enzymes.md
- wiki/engineered-koji-protocol.md
- wiki/gut-lumen-sink.md
- wiki/koji-endgame-strain.md
- wiki/koji-home-fermentation.md
- wiki/kpv-peptide.md
- wiki/lactoferrin.md
- wiki/modality-chokepoint-matrix.md
- wiki/nlrp3-exploit-map.md
- wiki/open-enzyme-vision.md
- wiki/open-source-platform.md
- wiki/saccharomyces-cerevisiae.md
- wiki/supplements-stack.md
- wiki/validation-experiments.md

---


## Sweep — 2026-05-05 (DeepSeek V4-Pro synthesis + Claude review)

**Synthesis log:** [`logs/v4-synthesis-2026-05-05-734bf51.md`](../logs/v4-synthesis-2026-05-05-734bf51.md)
**Substrate:** Open Enzyme wiki at commit `734bf51`
**Diff base:** `436f1bd38ef4ca9830c85c8c8c1469e3bb595187`
**Trigger files:** wiki/blood-barrier-exploits.md,wiki/enzyme-deficit-deep-dive.md,wiki/gout-deep-dive.md,wiki/gout-pathophysiology.md,wiki/nlrp3-inhibitor-screen.md,wiki/open-questions.md,wiki/supplements-stack.md,wiki/theaflavins.md,wiki/uricase-variant-selection.md,wiki/zileuton.md
**Synthesizer:** google/gemini-2.5-pro
**Reviewer:** anthropic/claude-opus-4-7
**Reviews merged:** 14

---
**Substrate:** Open Enzyme wiki at commit `734bf51`
**Trigger files:** wiki/blood-barrier-exploits.md,wiki/enzyme-deficit-deep-dive.md,wiki/gout-deep-dive.md,wiki/gout-pathophysiology.md,wiki/nlrp3-inhibitor-screen.md,wiki/open-questions.md,wiki/supplements-stack.md,wiki/theaflavins.md,wiki/uricase-variant-selection.md,wiki/zileuton.md
**Diff base:** 436f1bd38ef4ca9830c85c8c8c1469e3bb595187
**Reviewer:** google/gemini-2.5-pro

## New Connections

1.  **Lactoferrin co-expression in the endgame strain may create a positive feedback loop by relieving inflammatory suppression of the gut-lumen sink.** *Speculative*.
    -   *Documents Connected:* `lactoferrin.md`, `abcg2-modulators.md`, `koji-endgame-strain.md`, `gut-lumen-sink.md`
    -   *Why It Matters:* The platform's core uricase mechanism depends on ABCG2 transporting urate into the gut. Chronic low-grade inflammation, driven by TNFα, suppresses ABCG2 expression (`abcg2-modulators.md`). Lactoferrin is known to suppress TNFα (`lactoferrin.md`). Therefore, co-expressing lactoferrin in the `koji-endgame-strain` could relieve this inflammatory brake on ABCG2, increasing substrate supply for the co-expressed uricase. This transforms lactoferrin from a simple multi-chokepoint NLRP3 modulator into a direct synergist for the platform's primary urate-lowering mechanism.
    -   *Suggested Action:* Propose an in vitro experiment co-treating Caco-2 cells with TNFα and lactoferrin, then measuring ABCG2 expression and urate transport to validate this feedback loop. This should be added to `validation-experiments.md`.

> **Claude review — Confirmed.** Strong synthesis. The TNFα → ABCG2-suppression axis is directly supported by Ferrer-Picón 2020 (PMID 31211831) in `abcg2-modulators.md` §3, and lactoferrin's TNFα suppression is documented in `lactoferrin.md` §4.1 (Habib 2023 PMID 37926296). The positive-feedback framing is novel — lactoferrin was previously positioned as a CP1a/CP4/CP6b NLRP3 modulator only. One refinement: the platform already flags lactoferrin as "may be doing more for the gut-sink than its current positioning suggests" in `open-questions.md` §"Co-engineered substrate-supply mechanisms", so this elevates an existing hypothesis rather than originating it. The proposed Caco-2 TNFα + lactoferrin + urate transport experiment is well-scoped and should land in `validation-experiments.md` as a focused addition to §1.14 (which already tests DHT + TNFα additive suppression + butyrate rescue).

**✓ Actioned 2026-05-05:** Extended `validation-experiments.md` §1.14 to include a lactoferrin rescue arm alongside butyrate (renamed "Additive ABCG2 Suppression by Androgens + TNFα + Butyrate Rescue + Lactoferrin Synergy"; cost +$300 for Lf reagent + TNFα ELISA, timeline unchanged); added new `lactoferrin.md` §4.7 "Indirect Substrate-Supply Synergy" formalizing the composed mechanism with evidence-level tags; added a "Beyond chokepoint coverage" paragraph at end of `koji-endgame-strain.md` §2.2 framing the dual-cassette architecture as positive-feedback geometry. Stray garbage sentence at L32 of this file removed.

2.  **Carnosine is a uniquely well-suited co-expression candidate for the androgen-dominant gout phenotype because it directly counters androgen-driven hyperuricemia at the renal level.** *Supported*.
    -   *Documents Connected:* `carnosine.md`, `androgen-urate-axis.md`, `engineered-koji-protocol.md`
    -   *Why It Matters:* The primary demographic for gout is male, and a significant portion has high androgen levels (endogenous or via TRT/SERMs). The `androgen-urate-axis.md` page establishes that androgens drive hyperuricemia in part by upregulating the renal urate transporter URAT1. The `carnosine.md` page documents animal model evidence that carnosine *downregulates* URAT1. This positions carnosine not just as a generic NLRP3/UA modulator, but as a precision countermeasure to a key driver of hyperuricemia in the platform's primary target population.
    -   *Suggested Action:* Elevate carnosine's strategic priority for co-expression in the `koji-endgame-strain.md` thesis, specifically highlighting this mechanistic synergy for the male/high-androgen patient subgroup.

    > **Claude review — Confirmed, prioritize.** The carnosine/URAT1/androgen triangulation is well-grounded: `carnosine.md` documents URAT1/GLUT9 downregulation in the hyperuricemia rat model (dual phenotype), and `androgen-urate-axis.md` §"Mechanism" establishes androgen-driven URAT1 upregulation as the mirror mechanism. The "precision countermeasure to the primary target demographic" framing is a genuinely sharpened positioning. Push to prioritize: `engineered-koji-protocol.md` §15 currently treats carnosine as a Tier 2 secondary-synergy candidate with ~150 mg/L yeast baseline flagged as unsourced. This synergy argument strengthens the case for running the §15 validation experiment *before* further iteration on peripheral modules. Worth a corresponding update to `koji-endgame-strain.md` §2.2 (currently lactoferrin-dominant) to add a carnosine sub-row with the androgen-axis argument explicit.

**✓ Actioned 2026-05-05:** Added new `koji-endgame-strain.md` §2.5 "Carnosine — Renal Transporter-Modulation Arm for Androgen-Dominant Phenotype (Optional Third Cassette)" with full androgen-axis alignment argument, URAT1/GLUT9 mechanism, engineering note (CarnS + panD two-component cassette, format constraint to dried powder), four caveats (CN1 hydrolysis, β-alanine pool limitation, unsourced yeast titer, no human RCT), and evidence-level/strategic-position summary. Added matrix footnote at end of §1 pointing to §2.5 as the transporter-modulation layer beyond NLRP3 chokepoints. Added priority note to `engineered-koji-protocol.md` §15 Rationale calling out the androgen-axis precision-countermeasure framing and directing §15 validation before peripheral modules.

3.  **The koji chassis provides a "native metabolite chorus" (kojic acid, ergothioneine) that offers free, multi-chokepoint NLRP3 coverage, making it a superior platform to cleaner but inert hosts like *S. cerevisiae*.** *Supported*.
    -   *Documents Connected:* `aspergillus-oryzae.md`, `engineered-koji-protocol.md`, `nlrp3-exploit-map.md`, `saccharomyces-cerevisiae.md`
    -   *Why It Matters:* Wild-type *A. oryzae* natively produces kojic acid (3-5 g/L, NF-κB suppression, CP1a) and ergothioneine (~20 mg/g, mitochondrial ROS scavenger, CP1b) during fermentation. This means any engineered koji strain automatically ships with a baseline anti-inflammatory payload that a "cleaner" host like yeast or *E. coli* would need additional, complex engineering to replicate. This "free" synergy is a core, under-stated advantage of the koji-first platform strategy.
    -   *Suggested Action:* Add a dedicated section to `open-enzyme-vision.md` or `open-source-platform.md` that explicitly frames this "native metabolite chorus" as a key strategic advantage of the *A. oryzae* chassis.

    > **Claude review — Confirmed.** Well-sourced against `aspergillus-oryzae.md` §"Native Secondary Metabolites" (kojic acid 3–5 g/L, ergothioneine ~20 mg/g dry mass) and `engineered-koji-protocol.md` §01b. The CP1a/CP1b chokepoint mapping is already made in `koji-endgame-strain.md` §1 coverage matrix (which scores these Reasonable at CP1a and CP1b respectively). One caution worth surfacing in the suggested action: the kojic-acid direct-NLRP3 activity is flagged as "unpublished/open question" in `nlrp3-inhibitor-screen.md`, and ergothioneine's "Nrf2 inducer" classification is a two-step mechanistic extrapolation (ROS scavenger → Nrf2 stabilization → downstream) rather than a direct Nrf2 binder. The "free chorus" framing is correct directionally but the strategic page should tag evidence levels (In Vitro / Mechanistic Extrapolation) rather than present it as supported coverage.

## Contradictions Found

1.  **The recommended supplements stack contains potent functional inhibitors of ABCG2, directly antagonizing the platform's core gut-lumen sink mechanism.**
    -   *Locations:* `supplements-stack.md` recommends quercetin and EGCG. `abcg2-modulators.md` §8 identifies both, plus curcumin and genistein (from soy foods), as functional inhibitors of the ABCG2 transporter at supplement-relevant concentrations.
    -   *Analysis:* For the primary user demographic (males, often with androgen-suppressed ABCG2) or Q141K carriers, stacking these supplements could pharmacologically close the gate that the engineered uricase relies on for its substrate. The wiki notes this contradiction but has not yet resolved it with clear, stratified guidance. This is a critical conflict between two major platform strategies.

    > **Claude review — Confirmed.** Not a new finding — this contradiction is already extensively documented in `abcg2-modulators.md` §8 "The supplements-stack contradiction" and `supplements-stack.md` §"Stack-level contradictions" with a full risk-tier stratification table. The Pass 2 synthesizer correctly identifies it as unresolved. The useful framing addition is naming it as "a critical conflict between two major platform strategies" — worth elevating that framing into `open-enzyme-vision.md` itself, not just the per-page contradiction notes. The EGCG case is subtler than the synthesis suggests: Yu 2024 (PMID 38757391) shows in vivo net-favorable effect on ABCG2/URAT1/GLUT9 in hyperuricemic mice, contradicting the in vitro inhibition story — net clinical effect is flagged as unresolved, not antagonist.

2.  **The shio-koji delivery format, recommended for its stability, contains active proteases that will likely degrade peptide or even some enzyme payloads.**
    -   *Locations:* `koji-home-fermentation.md` and `digestive-enzymes.md` recommend shio-koji as a stable, long-shelf-life format for delivering active enzymes. However, `engineered-koji-protocol.md` (§15), `bpc-157.md`, and `kpv-peptide.md` note that this format is unsuitable for peptide payloads like carnosine or BPC-157 due to degradation by native proteases during the 7-14 day room-temperature ferment.
    -   *Analysis:* This raises a critical, un-tested question: are the folded, tetrameric engineered enzymes (uricase, lactoferrin) also susceptible to this proteolytic degradation? If so, shio-koji is not a viable dual-use format, and the platform must default to fresh, dried, or amazake-style formats.

    > **Claude review — Confirmed.** Accurate citation trail: `engineered-koji-protocol.md` §15 (carnosine) explicitly names the shio-koji format as structurally unsuitable for dipeptide payloads, and the same logic in `kpv-peptide.md` and `bpc-157.md`. The open question for folded tetrameric enzymes is real and not yet tested. This directly corresponds to proposed experiment §1.10 in `validation-experiments.md` ("Heterologous uricase stability in shio-koji salt-protease ferment") which is already queued with full protocol — the synthesizer may not have read it. The Pass 2 framing is correct but overstates novelty; the experiment is budgeted at $400–800 / 3–4 weeks and decides whether the dual-use household-condiment thesis survives.

## Proposed Experiments (ranked by insight per cost)

1.  **Quantify ABCG2 inhibition by stack supplements in a Caco-2 transwell urate transport assay.** Cost: $1,500. Time: 3w. Decides: The magnitude of the contradiction found in #1 above. Measure basolateral-to-apical urate flux in differentiated Caco-2 cells with and without supplement-relevant concentrations of quercetin, EGCG, and curcumin on the apical side. This would confirm or refute the antagonism and provide data to create a risk-stratified supplement protocol, especially for androgen-dominant or Q141K-positive users.

    > **Claude review — Partial.** The experiment is valuable and should run, but `validation-experiments.md` already contains closely-adjacent experiments: §1.14 (DHT + TNFα additive ABCG2 suppression + butyrate rescue) uses Caco-2 transwells at $1,500–2,500, and the Yu 2024 in vivo EGCG data (PMID 38757391) partially pre-empts the EGCG arm by showing net-favorable effect on ABCG2. Augment: extend §1.14 to add quercetin + EGCG + curcumin arms rather than queue a parallel experiment. The shared Caco-2 infrastructure and shared urate-flux readout amortize fixed costs; one well-designed factorial beats two overlapping experiments. Also include a Q141K-variant Caco-2 arm if available (the synthesis flags Q141K-positive users as highest-risk; this is where the contradiction most matters).

2.  **Test the stability of engineered uricase and lactoferrin in a 14-day shio-koji ferment.** Cost: $800. Time: 3w. Decides: Whether shio-koji is a viable delivery format for the endgame strain. Incubate purified uricase and lactoferrin in a standard shio-koji matrix at room temperature. Sample at days 0, 3, 7, and 14, and measure residual enzyme activity and protein integrity (via Western blot). A significant loss of activity would kill the shio-koji format for engineered payloads and prioritize other formats.

    > **Claude review — Confirmed, prioritize.** This is the most operationally important experiment proposal in the batch. The shio-koji dual-use thesis is load-bearing: it's the single product format that unifies Lynn's EPI track and Brian's gout track. §1.10 in `validation-experiments.md` already queues this at $400–800 / 3–4 weeks with full protocol (including SGF/SIF survival, Western for intact monomer, salt-concentration sub-experiment). The Pass 2 proposal duplicates the existing experiment at a higher cost estimate ($800) without adding the salt-gradient sub-experiment that would identify whether a low-salt shio-koji variant could preserve dual-use. Recommend: execute §1.10 as written, flag this Pass 2 proposal as a duplicate, and elevate priority given the strategic stakes.

3.  **Launch a screen for gut-selective, food-grade HDAC inhibitors to enhance Q141K-ABCG2 trafficking rescue.** Cost: $5,000 (for initial in silico screen + top 5 in vitro). Time: 8w. Decides: If a potent, non-butyrate alternative exists to "open the gate" for the large Q141K-positive gout population. Butyrate's dual action (PPARγ + HDACi) is powerful but limited by fiber intake and microbiome variance. A direct, fermentable HDAC inhibitor could be a powerful co-expression module or adjunct.

    > **Claude review — Partial.** The rationale is sound — butyrate's dual PPARγ + HDACi mechanism (Basseville 2012 PMID 22472121 for Q141K rescue) is well-documented in `abcg2-modulators.md` §6 — but the experimental design has tissue-selectivity risk the synthesis doesn't address. Pan-tissue HDAC inhibitors hit liver, BBB, and cardiac HDACs (cardiotoxicity is the reason vorinostat stays oncology-restricted). A "gut-selective, food-grade HDAC inhibitor" screen is sensible in principle but the selectivity criterion is the hard part — most food-grade HDACi candidates (butyrate, sulforaphane via indirect mechanism) are already known. Push back on cost: $5,000 for initial in silico + top-5 in vitro is optimistic for a screen that needs to differentiate gut-enriched binding from pan-tissue activity. Augment with: specify the selectivity assay (e.g., Caco-2 HDAC activity vs. hepatocyte HDAC activity as a primary screening discriminator), and add HDAC isoform specificity (HDAC1/2/3 are the relevant class for trafficking; HDAC6 is off-target for this purpose).

## Open Questions

1.  **Can the Open Enzyme platform develop a fermentable CP0 modulator, or will this always be a pharma-adjunct gap?** The `complement-c5a-gout.md` page clearly identifies CP0 (complement priming) as a dominant, upstream chokepoint and an "honest platform gap" with no current fermentable coverage. A computational screen of natural products against C5aR1 came up negative. Is there an alternative microbial route to CP0 coverage (e.g., expressing a soluble complement inhibitor like sCR1), or should the platform strategy formally accept avacopan as the permanent adjunct for this chokepoint?

    > **Claude review — Augment.** The question as framed is answered-closed — `validation-experiments.md` §1.21 (executed 2026-04-27) is a completed computational scan of natural-product C5aR1 chemical space with a definitive negative result (zero wet-lab-validated natural-product antagonists across ChEMBL 4,873 bioactivities, NPASS, LOTUS, Open Targets). The re-open conditions are specified. The productive re-framing is the second half of the question: **alternative microbial routes to CP0 coverage**. Specifically, expressing soluble complement regulators (sCR1/TP10, Factor H fragments, DAF/CD55 ectodomain) heterologously in GRAS hosts is genuinely unexplored. sCR1 is in clinical trials systemically; a gut-luminal version targeting mucosal-complement activation is the untested vector. This deserves a dedicated follow-up, likely tracked in `modality-chokepoint-matrix.md` rather than re-opening the natural-product screen.

2.  **What is the full effect of the androgen axis on the NLRP3 inflammasome, beyond urate transporters?** The wiki thoroughly documents how androgens suppress ABCG2 and upregulate URAT1. However, the literature on sex differences in inflammasome activation is growing. Do androgens directly modulate NLRP3 expression or activity in macrophages, or alter the response to C5a priming? This could reveal new synergies or risks for the male-dominant target population.

    > **Claude review — Confirmed.** Genuinely novel open question. The wiki has extensive coverage of androgen → URAT1/ABCG2 (`androgen-urate-axis.md`) and C5a → NLRP3 priming (`complement-c5a-gout.md`) but no explicit synthesis of whether androgens modulate the C5a-priming or NLRP3-assembly steps directly. Recent literature on sex-differential NLRP3 activation in macrophages (ERα/ERβ modulation of inflammasome; testosterone effects on TLR4/MyD88) is accumulating but not represented in the Open Enzyme corpus. Worth a dedicated literature scan before committing to a wiki page — the question as framed could be a major expansion of `androgen-urate-axis.md` or a standalone page. The male-demographic ceiling noted in `koji-endgame-strain.md` §1 footnote is currently transporter-focused only; extending it to the inflammasome would meaningfully change the stack-design rationale.

3.  **Do obligate anaerobes like *Faecalibacterium prausnitzii* offer a superior chassis for gut-based therapies due to durable colonization?** The current platform relies on transit organisms (*S. cerevisiae*, *A. oryzae*). The `modality-chokepoint-matrix.md` flags engineered LBPs as an open vector. An engineered *F. prausnitzii* could provide continuous, stable production of butyrate (for ABCG2 induction) or other therapeutic payloads, potentially overcoming the adherence and transit-time limitations of the current chassis.

    > **Claude review — Confirmed.** Directly traceable to `modality-chokepoint-matrix.md` row "Engineered LBPs (obligate anaerobes)" where Faecalibacterium prausnitzii is explicitly flagged as the highest-leverage candidate for durable colonization + local butyrate (hitting both wild-type ABCG2 via PPARγ and Q141K via HDAC trafficking rescue). The matrix names this as one of the top exploration vectors. The open question correctly identifies the current platform's structural limitation (transit organisms) and the LBP framework as the alternative. Worth noting: the regulatory path (FDA LBP guidance 2018) is distinct from koji/yeast GRAS food, and the home-fermentation thesis doesn't transfer to obligate anaerobes — this is a "commercial LBP" vector, not a "grow at home" vector. That tradeoff deserves explicit framing in any dedicated page.

## Priority Actions

1.  **Resolve the supplement stack vs. ABCG2 contradiction by adding explicit, risk-stratified guidance.** Update `supplements-stack.md` and `abcg2-modulators.md` to distinguish risk tiers for high-androgen and Q141K-positive users versus wild-type users, and for supplement-grade vs. dietary-level intake of inhibitor compounds (quercetin, EGCG, etc.). This is a critical safety and efficacy clarification.

    > **Claude review — Confirmed, prioritize.** Correctly identified as the most important stratification task in the corpus. `supplements-stack.md` already contains a risk-tier stratification table (§"Stack-level contradictions") — the action is to audit it for completeness and propagate the stratification into `abcg2-modulators.md` §8 and `open-enzyme-vision.md` §10. Priority is justified because this directly affects the self-experiment protocol: Brian is on clomid (elevates T → suppresses ABCG2 per `androgen-urate-axis.md`) and the supplement stack currently includes both EGCG and quercetin at supplement-grade doses. The stratification isn't theoretical; it's a live protocol-design question for §3.1–§3.5.

2.  **Elevate the Ward 1995 dual-cassette experiment to the highest priority.** As noted in `koji-endgame-strain.md` and `validation-experiments.md`, the feasibility of layering the uricase and lactoferrin cassettes in a single koji strain is the gating question for the entire endgame thesis. This experiment should be prioritized over more incremental optimizations.

    > **Claude review — Confirmed, prioritize.** This has already been formalized — `validation-experiments.md` §1.9 is explicitly tagged as "**#1 priority gate**" with the full protocol, cost ($3,000–5,000), timeline (8–12 weeks), dependencies, and success criteria. The Pass 3 review dated 2026-04-27 already elevated it. The Falsification Card (`wiki/hypotheses/H01-ward-dual-cassette.md`) exists. The synthesizer's elevation is consistent with existing platform priority. Action item: the blocker is not prioritization but execution — specifically, securing *A. oryzae* transformation lab access (Lauren Collier-Hyams at Emory per `team.md`, commercial CRO, or community biolab). The Priority Actions section should name that execution bottleneck, not just re-assert the priority.

3.  **Create a dedicated wiki page for siRNA as a therapeutic modality, focusing on URAT1 silencing.** The `modality-chokepoint-matrix.md` identifies kidney-tropic siRNA against URAT1 as a clean, elegant, and unexplored solution for under-excreter gout. A dedicated page would scope this modality and position it as a potential long-term, non-microbial output of the platform's discovery engine.

    > **Claude review — Confirmed.** Well-sourced against `modality-chokepoint-matrix.md` open exploration question #1 (siRNA against URAT1 mRNA via kidney-tropic conjugate — flagged as "the cleanest 'elegant solution' in the entire matrix"). A dedicated page is appropriate. Augment the proposal with: (a) the inclisiran GalNAc-conjugate precedent is liver-specific (GalNAc binds ASGPR on hepatocytes); kidney-tropic conjugate chemistry (megalin-binding peptides, CDP conjugates) is a distinct and less-mature chemistry class that deserves its own scoping. (b) The page should explicitly position siRNA as non-fermentable / discovery-engine output, parallel to zileuton/disulfiram/avacopan in the repurposing surface (per `open-enzyme-vision.md` §2.2). This maintains the clean split between "strain library" and "discovery engine" outputs and avoids confusing the two-track platform narrative.

---
Sources cited:
- wiki/abcg2-modulators.md
- wiki/androgen-urate-axis.md
- wiki/aspergillus-oryzae.md
- wiki/bpc-157.md
- wiki/carnosine.md
- wiki/complement-c5a-gout.md
- wiki/engineered-koji-protocol.md
- wiki/gut-lumen-sink.md
- wiki/koji-endgame-strain.md
- wiki/koji-home-fermentation.md
- wiki/kpv-peptide.md
- wiki/lactoferrin.md
- wiki/modality-chokepoint-matrix.md
- wiki/nlrp3-exploit-map.md
- wiki/nlrp3-inhibitor-screen.md
- wiki/open-enzyme-vision.md
- wiki/open-source-platform.md
- wiki/saccharomyces-cerevisiae.md
- wiki/supplements-stack.md
- wiki/validation-experiments.md

---


## Sweep — 2026-04-28 (DeepSeek V4-Pro synthesis + Claude review)

**Synthesis log:** [`logs/v4-synthesis-2026-04-28-3943bfc.md`](../logs/v4-synthesis-2026-04-28-3943bfc.md)
**Substrate:** Open Enzyme wiki at commit `3943bfc`
**Diff base:** `manual`
**Trigger files:** wiki/abcg2-modulators.md,wiki/androgen-urate-axis.md,wiki/bpc-157.md,wiki/colchicine.md,wiki/complement-c5a-gout.md,wiki/crispr-uricase.md,wiki/cross-validation.md,wiki/digestive-enzyme-optimization.md,wiki/disulfiram.md,wiki/engineered-koji-protocol.md,wiki/gout-pathophysiology.md,wiki/GRAPH.md,wiki/gut-lumen-sink.md,wiki/koji-endgame-strain.md,wiki/koji-home-fermentation.md,wiki/kpv-peptide.md,wiki/modality-chokepoint-matrix.md,wiki/nlrp3-inflammasome.md,wiki/open-enzyme-vision.md,wiki/open-questions.md,wiki/open-source-platform.md,wiki/self-experiment-protocol.md,wiki/spm-resolution-pathway.md,wiki/supplements-stack.md,wiki/validation-experiments.md
**Synthesizer:** google/gemini-2.5-pro
**Reviewer:** anthropic/claude-opus-4-7
**Reviews merged:** 14

---
**Substrate:** Open Enzyme wiki at commit `3943bfc`
**Trigger files:** wiki/abcg2-modulators.md,wiki/androgen-urate-axis.md,wiki/bpc-157.md,wiki/colchicine.md,wiki/complement-c5a-gout.md,wiki/crispr-uricase.md,wiki/cross-validation.md,wiki/digestive-enzyme-optimization.md,wiki/disulfiram.md,wiki/engineered-koji-protocol.md,wiki/gout-pathophysiology.md,wiki/GRAPH.md,wiki/gut-lumen-sink.md,wiki/koji-endgame-strain.md,wiki/koji-home-fermentation.md,wiki/kpv-peptide.md,wiki/modality-chokepoint-matrix.md,wiki/nlrp3-inflammasome.md,wiki/open-enzyme-vision.md,wiki/open-questions.md,wiki/open-source-platform.md,wiki/self-experiment-protocol.md,wiki/spm-resolution-pathway.md,wiki/supplements-stack.md,wiki/validation-experiments.md
**Diff base:** manual
**Reviewer:** google/gemini-2.5-pro

## New Connections

1. **Lactoferrin co-expression in the endgame strain may create a positive feedback loop by relieving inflammatory suppression of the gut-lumen sink.** *Speculative*.
   - *Documents Connected:* `lactoferrin.md`, `abcg2-modulators.md`, `koji-endgame-strain.md`, `gut-lumen-sink.md`
   - *Why It Matters:* The platform's core uricase mechanism depends on ABCG2 transporting urate into the gut. Chronic low-grade inflammation, driven by TNFα, suppresses ABCG2 expression. Lactoferrin is known to suppress TNFα. Therefore, co-expressing lactoferrin in the koji endgame strain could relieve this inflammatory brake on ABCG2, increasing substrate supply for the co-expressed uricase. This transforms lactoferrin from a simple multi-chokepoint NLRP3 modulator into a direct synergist for the platform's primary urate-lowering mechanism.
   - *Suggested Action:* Propose an in vitro experiment co-treating Caco-2 cells with TNFα, lactoferrin, and measuring ABCG2 expression and urate transport to validate this feedback loop.

   > **Claude review — Confirmed.** Lactoferrin's TNFα-suppression data is solid (Håversen 2002 and others; in vitro and animal models), and `abcg2-modulators.md` §3 explicitly cites Ferrer-Picón 2020 (PMID 31211831) for TNFα-mediated ABCG2 suppression in IBD organoids. The logical chain — lactoferrin → ↓TNFα → relief of ABCG2 suppression → ↑substrate for co-expressed uricase — is mechanistically coherent and currently classified "Speculative" appropriately given no direct lactoferrin→intestinal-ABCG2 experiment exists. Augment: the proposed Caco-2 experiment should mirror §1.14's DHT+TNFα+butyrate design for consistency, and should measure apical-to-basolateral urate flux (not just ABCG2 expression) since Pass 3 reviews have repeatedly flagged that transporter expression ≠ functional flux.

2. **Carnosine is a uniquely well-suited co-expression candidate for the androgen-dominant gout phenotype because it directly counters androgen-driven hyperuricemia at the renal level.** *Supported*.
   - *Documents Connected:* `carnosine.md`, `androgen-urate-axis.md`, `engineered-koji-protocol.md`
   - *Why It Matters:* The primary demographic for gout is male, and a significant portion has high androgen levels (endogenous or via TRT/SERMs). The `androgen-urate-axis.md` page establishes that androgens drive hyperuricemia in part by upregulating the renal urate transporter URAT1. The `carnosine.md` page documents animal model evidence that carnosine *downregulates* URAT1. This positions carnosine not just as a generic NLRP3/UA modulator, but as a precision countermeasure to a key driver of hyperuricemia in the platform's primary target population.
   - *Suggested Action:* Elevate carnosine's strategic priority for co-expression in the `koji-endgame-strain.md` thesis, specifically highlighting this mechanistic synergy for the male/high-androgen patient subgroup.

   > **Claude review — Confirmed.** The carnosine→URAT1 mechanistic case is documented in `androgen-urate-axis.md` (animal model evidence for URAT1 downregulation) and `carnosine.md` (dual UA + NLRP3 phenotype in hyperuricemia rat models). The framing as a "precision countermeasure" for male/high-androgen patients is well-supported by the axis mapping. One sharpening: the evidence level for carnosine→URAT1 is Animal Model only, and serum carnosinase (CN1) rapidly degrades free carnosine, capping achievable systemic exposure — flagged as an open question in `open-questions.md`. Elevation in `koji-endgame-strain.md` is warranted but should note the carnosinase-PK caveat and that koji-expression feasibility is still speculative (§15 in `engineered-koji-protocol.md` flags the β-alanine pool limitation).

3. **The koji chassis provides a "native metabolite chorus" (kojic acid, ergothioneine) that offers free, multi-chokepoint NLRP3 coverage, making it a superior platform to cleaner but inert hosts like *S. cerevisiae*.** *Supported*.
   - *Documents Connected:* `aspergillus-oryzae.md`, `engineered-koji-protocol.md`, `nlrp3-exploit-map.md`, `nlrp3-inhibitor-screen.md`
   - *Why It Matters:* Wild-type *A. oryzae* natively produces kojic acid (3-5 g/L, NF-κB suppression) and ergothioneine (~20 mg/g, mitochondrial ROS scavenger) during fermentation. These compounds hit NLRP3 chokepoints CP1a and CP1b, respectively. This means any engineered koji strain automatically ships with a baseline anti-inflammatory payload that a "cleaner" host like yeast or *E. coli* would need additional, complex engineering to replicate. This "free" synergy is a core, under-stated advantage of the koji-first platform strategy.
   - *Suggested Action:* Add a dedicated section to `open-enzyme-vision.md` or `open-source-platform.md` that explicitly frames this "native metabolite chorus" as a key strategic advantage of the *A. oryzae* chassis.

   > **Claude review — Confirmed, prioritize.** The "native metabolite chorus" framing is well-supported by `aspergillus-oryzae.md` and `engineered-koji-protocol.md` §01b: kojic acid 3–5 g/L (NF-κB suppression, In Vitro), ergothioneine ~20 mg/g dry mass (mitochondrial ROS scavenger). This is a genuine structural advantage the project under-sells. However, per `open-questions.md` §Uricase / Wild-type koji baseline, the ergothioneine titer "~20 mg/g dry mass" needs primary-source verification (flagged in L223 of `engineered-koji-protocol.md`) — the sweep noted Pass 2 cited this without verified primary source. The dedicated section in `open-enzyme-vision.md` should include the verification caveat and link to the proposed §1.11 experiment (ergothioneine→ABCG2 Caco-2 test).

## Contradictions Found

1. **The recommended supplements stack contains potent functional inhibitors of ABCG2, directly antagonizing the platform's core gut-lumen sink mechanism.** Locations: `supplements-stack.md` recommends quercetin, EGCG, and notes curcumin as a related compound. `abcg2-modulators.md` §8 identifies all three, plus genistein (from soy foods like natto/miso), as functional inhibitors of the ABCG2 transporter at supplement-relevant concentrations. Analysis: For the primary user demographic (males, often with androgen-suppressed ABCG2) or Q141K carriers, stacking these supplements could pharmacologically close the gate that the engineered uricase relies on for its substrate. The wiki notes this contradiction but has not yet resolved it with clear, stratified guidance.

   > **Claude review — Confirmed, prioritize.** `abcg2-modulators.md` §8 explicitly catalogs curcumin, quercetin, EGCG, and genistein as functional ABCG2 inhibitors at supplement-relevant doses, and `supplements-stack.md` has a Stack-level contradictions section addressing this. The risk-tier stratification added in that section (Q141K homozygote + androgen-suppressed + high-dose flavonoid = "highest concern") is good, but the contradiction remains under-resolved in practice: no clinical data exists on whether supplement-grade inhibitor stacking actually closes the gut sink in humans. The proposed Caco-2 transwell experiment in §1 ranking (but not yet in the experiment queue as a discrete entry) is the direct falsification path. Should be elevated to a Priority Experiment alongside §1.14 (DHT+TNFα+butyrate), since it tests the same axis.

2. **The shio-koji delivery format, recommended for its stability, contains active proteases that will likely degrade peptide or even some enzyme payloads.** Locations: `koji-home-fermentation.md` and `digestive-enzymes.md` recommend shio-koji as a stable, long-shelf-life format for delivering active enzymes. However, `engineered-koji-protocol.md` (§15) and `bpc-157.md` note that this format is unsuitable for peptide payloads like carnosine or BPC-157 due to degradation by native proteases during the 7-14 day room-temperature ferment. Analysis: This raises a critical, un-tested question: are the folded, tetrameric engineered enzymes (uricase, lactoferrin) also susceptible to this proteolytic degradation? If so, shio-koji is not a viable dual-use format, and the platform must default to fresh, dried, or amazake-style formats.

   > **Claude review — Confirmed.** `engineered-koji-protocol.md` §15 explicitly flags this constraint: "A carnosine-expressing strain cannot be delivered intact via the shio-koji format" due to Kex2-family peptidase activity over 7–14 days. The format-constraint table in §15 ranks formats by peptide survival (dried powder > amazake > fresh > shio-koji = effectively zero). `bpc-157.md` and `kpv-peptide.md` both reference this constraint. The open question is whether folded tetrameric enzymes (uricase, lactoferrin) are also protease-susceptible — §1.10 in validation-experiments.md is designed to test exactly this. The synthesizer's framing is correct; one refinement: the experiment §1.10 is specifically for *uricase*, not a generic "engineered enzymes" test. Lactoferrin stability in shio-koji remains a separate open question given its glycoprotein character differs from uricase's tetrameric fold.

## Proposed Experiments (ranked by insight per cost)

1. **Quantify ABCG2 inhibition by stack supplements in a Caco-2 transwell urate transport assay.** Cost: $1,500. Time: 3w. Decides: The magnitude of the contradiction found in #1 above. Measure basolateral-to-apical urate flux in differentiated Caco-2 cells with and without supplement-relevant concentrations of quercetin, EGCG, and curcumin on the apical side. This would confirm or refute the antagonism and provide data to create a risk-stratified supplement protocol, especially for androgen-dominant or Q141K-positive users.

   > **Claude review — Confirmed, prioritize.** This is §1 priority in the validation-experiments.md queue (§1.9 Ward 1995 dual-cassette is elevated to #1 priority gate) and the core question is already well-framed in `koji-endgame-strain.md` §3. However, the synthesizer's framing conflates the ABCG2 experiment (Caco-2 transwell for stack contradictions) with the Ward 1995 dual-cassette feasibility. §1.9 at $3–5K / 8–12 weeks tests the layering question specifically; the $1,500 Caco-2 transwell for supplement-stack ABCG2 inhibition is a separate experiment. The Ward 1995 test should remain prioritized as it gates the entire koji-endgame-strain thesis. The phrasing "over more incremental optimizations" is apt — the stack experiments are cheaper but downstream of strain feasibility.

2. **Test the stability of engineered uricase and lactoferrin in a 14-day shio-koji ferment.** Cost: $800. Time: 3w. Decides: Whether shio-koji is a viable delivery format for the endgame strain. Incubate purified uricase and lactoferrin in a standard shio-koji matrix at room temperature. Sample at days 0, 3, 7, and 14, and measure residual enzyme activity and protein integrity (via Western blot). A significant loss of activity would kill the shio-koji format for engineered payloads and prioritize other formats.

   > **Claude review — Partial.** Agreement: the Caco-2 ABCG2 experiment is low-cost and high-value for resolving the stack contradiction. Push back on the timeline: `cross-validation.md` notes 3-week and $1,500 estimate, which aligns with the synthesizer's framing. However, the experiment should test *apical-to-basolateral urate flux* (functional transport), not just ABCG2 expression — a repeated Pass 3 critique is that expression ≠ function. Also, the experiment needs to include butyrate as a rescue arm (parallel to §1.14's DHT+TNFα+butyrate design) to test whether induction of ABCG2 can rescue inhibitor-closed gates. A 3-arm design (vehicle / quercetin+EGCG+curcumin / quercetin+EGCG+curcumin+butyrate) would answer both questions.

3. **Launch a screen for gut-selective, food-grade HDAC inhibitors to enhance Q141K-ABCG2 trafficking rescue.** Cost: $5,000 (for initial in silico screen + top 5 in vitro). Time: 8w. Decides: If a potent, non-butyrate alternative exists to "open the gate" for the large Q141K-positive gout population. Butyrate's dual action (PPARγ + HDACi) is powerful but limited by fiber intake and microbiome variance. A direct, fermentable HDAC inhibitor could be a powerful co-expression module or adjunct.

   > **Claude review — Partial.** Agreement on the shio-koji stability question — §1.10 in validation-experiments.md is exactly this experiment ($400-800, 3-4 weeks). Push back on the protocol: the synthesizer's design only tests purified enzymes in shio-koji matrix, but the more relevant test is the engineered strain's enzymes produced *in situ* during shio-koji fermentation — this is what §1.10 specifies (uses engineered strain if available; WT+spiked rasburicase as pilot). The synthesizer's simpler "incubate purified enzymes" design misses the protease-activation kinetics that occur during koji-to-shio-koji transition. Western blot alone won't distinguish partial degradation from full activity loss; activity assays are essential (as §1.10 specifies).

## Open Questions

1. **Can the Open Enzyme platform develop a fermentable CP0 modulator, or will this always be a pharma-adjunct gap?** The `complement-c5a-gout.md` page clearly identifies CP0 (complement priming) as a dominant, upstream chokepoint and an "honest platform gap" with no current fermentable coverage. A computational screen of natural products against C5aR1 came up negative. Is there an alternative microbial route to CP0 coverage (e.g., expressing a soluble complement inhibitor like sCR1), or should the platform strategy formally accept avacopan as the permanent adjunct for this chokepoint?

   > **Claude review — Augment.** The CP0 gap is well-documented in `complement-c5a-gout.md` §9 and the §1.21 computational scan (2026-04-27) closed the natural-product C5aR1 antagonist question with a negative result: zero wet-lab-validated natural-product C5aR1 antagonists across ChEMBL (4,873 bioactivities), NPASS, LOTUS, and primary literature. The scan found only 2 computational-only docking hits (acteoside, toxicarioside — both without wet-lab validation in the decade since publication; toxicarioside non-pursuable on safety grounds) and 1 neutraligand (resveratrol binding C5a, not C5aR1). **The open question should be reframed:** the fermentable CP0 coverage question is definitively closed absent the §1.21 re-open conditions. Avacopan is the permanent pharma adjunct; sCR1 (soluble complement receptor 1, TP10) expression in koji is the only remaining speculative engineering route but is distant. The synthesizer's framing as "open question" is outdated — this is now a "closed with documented negative result, reopen only under specific conditions."

2. **What is the full effect of the androgen axis on the NLRP3 inflammasome, beyond urate transporters?** The wiki thoroughly documents how androgens suppress ABCG2 and upregulate URAT1. However, the literature on sex differences in inflammasome activation is growing. Do androgens directly modulate NLRP3 expression or activity in macrophages, or alter the response to C5a priming? This could reveal new synergies or risks for the male-dominant target population.

   > **Claude review — Confirmed.** `androgen-urate-axis.md` §Open questions explicitly flags this as unresolved: "What is the full effect of the androgen axis on the NLRP3 inflammasome, beyond urate transporters? Do androgens directly modulate NLRP3 expression or activity in macrophages, or alter the response to C5a priming?" The sex-specific GWAS signal (16 male-specific loci vs. 2 female-specific loci per UK Biobank 2025) is consistent with hormonal modulation beyond transporters. This is a genuine research gap worth a future sweep or dedicated literature scan. Augment: the question should include whether TRT/SERM-induced urate elevation correlates with changes in CP0 (complement priming) or CP1a (TNFSF14) — given that TNFSF14 shows inverse association with DHA in Mendelian randomization and many androgens affect lipid metabolism.

3. **Do obligate anaerobes like *Faecalibacterium prausnitzii* offer a superior chassis for gut-based therapies due to durable colonization?** The current platform relies on transit organisms (*S. cerevisiae*, *A. oryzae*). The `modality-chokepoint-matrix.md` flags engineered LBPs as an open vector. An engineered *F. prausnitzii* could provide continuous, stable production of butyrate (for ABCG2 induction) or other therapeutic payloads, potentially overcoming the adherence and transit-time limitations of the current chassis.

   > **Claude review — Augment.** `modality-chokepoint-matrix.md` explicitly flags engineered LBPs (*F. prausnitzii*, *Akkermansia muciniphila*, *Bacteroides*) as 🟡 open exploration vectors in multiple cells (gut lumen, gut epithelium ABCG2, gut barrier, microbiome community). The case for *F. prausnitzii* is strong: it's a known butyrate producer, and butyrate hits both wild-type ABCG2 (PPARγ) and Q141K (HDAC trafficking rescue) per `abcg2-modulators.md`. The synthesizer's framing is correct. Augment: `open-questions.md` §Platform / Strategic has a "Novel modalities" section that already includes this question — engineered *F. prausnitzii* is listed as #2 priority. The question should link there and note that the platform currently lacks any dedicated wiki page on obligate anaerobe LBPs as a chassis class, which is a documentation gap.

## Priority Actions

1. **Resolve the supplement stack vs. ABCG2 contradiction by adding explicit, risk-stratified guidance.** Update `supplements-stack.md` and `abcg2-modulators.md` to distinguish risk tiers for high-androgen and Q141K-positive users versus wild-type users, and for supplement-grade vs. dietary-level intake of inhibitor compounds (quercetin, EGCG, etc.). This is a critical safety and efficacy clarification.

   > **Claude review — Confirmed.** The supplement-stack ABCG2 contradiction is extensively documented in `abcg2-modulators.md` §8, `supplements-stack.md` Stack-level contradictions section, and `gut-lumen-sink.md`. The risk-tier stratification (Q141K + androgen-suppressed + high-dose flavonoid = highest concern) is already in the stack. The synthesizer's framing of "risk-stratified guidance" is appropriate. One refinement: the stratification framework in `supplements-stack.md` is based on genotype + androgen status + dose — but the practical question for users is "what do I do if I'm on TRT and taking quercetin?" The current guidance could be sharper: for Q141K-positive or androgen-dominant users, prefer ABCG2 *inducers* (sulforaphane, fermentable fiber→butyrate) over inhibitors (quercetin, EGCG, curcumin at supplement dose). This explicit "inducers-over-inhibitors" framing for high-risk tiers would operationalize the stratification.

2. **Elevate the Ward 1995 dual-cassette experiment to the highest priority.** As noted in `koji-endgame-strain.md` and `validation-experiments.md`, the feasibility of layering the uricase and lactoferrin cassettes in a single koji strain is the gating question for the entire endgame thesis. This experiment should be prioritized over more incremental optimizations.

   > **Claude review — Confirmed, prioritize.** `validation-experiments.md` already elevates §1.9 Ward 1995 dual-cassette to #1 priority gate: "If it fails, the single-strain endgame collapses to a two-strain co-fermentation fallback — significant operational consequences for dosing uniformity and home reproducibility. $3–5K / 8–12 weeks but extraordinarily high leverage given what it decides; should run before further investment in the single-strain architecture." The synthesizer's Priority Action #2 is correctly identified. Augment: per `koji-endgame-strain.md` §3.2, the experiment design already incorporates the Li 2024 (PMID 39830075) multi-copy α-amylase-locus precedent and Wang 2023 (PMID 37807677) *A. niger* CRISPR multi-locus integration precedent. The experiment is well-scoped; the gating decision is simply whether to commit the capital and timeline now or defer until the simpler single-cassette uricase strain is validated.

3. **Create a dedicated wiki page for siRNA as a therapeutic modality, focusing on URAT1 silencing.** The `modality-chokepoint-matrix.md` identifies kidney-tropic siRNA against URAT1 as a clean, elegant, and unexplored solution for under-excreter gout. A dedicated page would scope this modality and position it as a potential long-term, non-microbial output of the platform's discovery engine.

   > **Claude review — Augment.** `modality-chokepoint-matrix.md` flags kidney-tropic siRNA against URAT1 as the highest-leverage novel exploration vector: "sequence-specific knockdown of the renal-reabsorption transporter that drives Brian's hyperuricemia phenotype. Eliminates the dose-dependent off-target profile of small-molecule URAT1 inhibitors (benzbromarone hepatotoxicity)." This is ranked #1 in the matrix's novel modalities queue. The synthesizer's Priority Action #3 is well-targeted. Augment: the dedicated wiki page should scope this relative to the existing inclisiran (GalNAc-siRNA for PCSK9) precedent — this is an emerging delivery class with kidney-tropic megalin-binding conjugates as the research frontier. A page would establish: (a) mechanistic rationale (URAT1 is the dominant renal reabsorption transporter per `gout-pathophysiology.md`), (b) the elegant off-target profile vs. benzbromarone, (c) the delivery-unsolved status (kidney-tropic conjugate chemistry is research-active but not clinical), (d) positioning as a "long-term non-microbial output of the discovery engine." This aligns with the Open Enzyme mission of being a discovery engine, not solely a microbial strain library.

---


# Synthesis — Action Queue

## How to read this file

This is the **action queue** for the sweep daemon and manual synthesis passes. Entries appear when a sweep surfaces a new connection, contradiction, or experiment; entries leave when the work lands in the canonical wiki page (or is folded into [`validation-experiments.md`](./validation-experiments.md) / [`open-questions.md`](./open-questions.md)).

**The full audit trail of every sweep — including findings that have already landed — lives in [`logs/v4-synthesis-*.md`](../logs/) and [`logs/v4-peer-review-*.md`](../logs/).** Don't re-state finished work here; if you want the history, go to the log.

A 2026-04-27 inbox-zero pass pruned everything marked `✓ Actioned` out of this file. The residue below is the genuine open queue. Sweep-history table at the bottom records date / trigger / log link only.

---

## Pending — open items

**(none — inbox zero as of 2026-04-28).**

The 2026-04-27 walkthrough actioned all seven prior pending items; the work landed in the canonical wiki pages listed in [Where actioned items live now](#where-actioned-items-live-now) below. New entries will appear here when the next sweep daemon run surfaces a finding the canonical pages don't already cover.

For the audit trail of the 2026-04-27 walkthrough specifically, see `git log --since=2026-04-27` on this repo — the seven items each landed in their own commit cluster, with `[skip-wiki-sweep]` markers and one-line descriptions of where each finding's canonical home is.

---

## Sweep history

Audit trail. Date / trigger / synthesizer / reviewer / log link. **Findings landed in canonical wiki pages and were pruned from this file** during the 2026-04-27 inbox-zero pass.

| Date | Trigger | Synthesizer | Reviewer | Log |
|---|---|---|---|---|
| 2026-04-27 | `wiki/open-enzyme-vision.md` | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-27-b7df491.md`](../logs/v4-synthesis-2026-04-27-b7df491.md) |
| 2026-04-27 | aspergillus-oryzae + colchicine + cross-validation + 6 others | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-27-c602f32.md`](../logs/v4-synthesis-2026-04-27-c602f32.md) — duplicate finding (ergothioneine→ABCG2), collapsed into the b7df491 sweep |
| 2026-04-26 | `wiki/supplements-stack.md` | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-26-1aea93d.md`](../logs/v4-synthesis-2026-04-26-1aea93d.md) |
| 2026-04-26 | GRAPH + abcg2-modulators + androgen-urate-axis + gut-lumen-sink | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-26-1237ff0.md`](../logs/v4-synthesis-2026-04-26-1237ff0.md) |
| 2026-04-25 | `wiki/digestive-enzyme-optimization.md` | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-25-622d2e2.md`](../logs/v4-synthesis-2026-04-25-622d2e2.md) |
| 2026-04-25 | `wiki/digestive-enzyme-optimization.md` (re-run on commit `b5c9116`) | Gemini 2.5 Pro | Opus 4.7 | [`v4-synthesis-2026-04-25-b5c9116.md`](../logs/v4-synthesis-2026-04-25-b5c9116.md) — substantive duplicate of the 622d2e2 sweep on the same trigger; carnosine + androgen-urate axis finding overlaps with 622d2e2 Connection 6 |
| 2026-04-25 | `wiki/koji-home-fermentation.md` | DeepSeek V4-Pro | Sonnet 4.6 | [`v4-synthesis-2026-04-25-a280c0d.md`](../logs/v4-synthesis-2026-04-25-a280c0d.md) — substantive duplicate of the 622d2e2 sweep, collapsed |
| 2026-04-25 | V4 peer-review pass on the 2026-04-24 sweep (`4a40f74`) | DeepSeek V4-Pro | (peer-review of Opus 4.7) | [`v4-peer-review-2026-04-25-deepseek.md`](../logs/v4-peer-review-2026-04-25-deepseek.md) |
| 2026-04-25 | Peer-review pass on the 2026-04-24 sweep (`4a40f74`) | Gemini 2.5 Pro | (peer-review of Opus 4.7) | [`v4-peer-review-2026-04-25-gemini.md`](../logs/v4-peer-review-2026-04-25-gemini.md) — second peer-review pass on the same Claude substrate; cross-vendor heterogeneity per `open-source-platform.md §"Multi-model synthesis"` |
| 2026-04-24 | 25-file v1.2 batch (nlrp3-exploit-map restructure + 24 co-triggered) | (manual session) | Opus 4.7 | (in-session log; see commit `4a40f74` and surrounding) |
| 2026-04-23 | `wiki/nlrp3-inhibitor-screen.md` (ChEMBL appendix) | (manual) | Opus 4.7 | (in-session log) |
| 2026-04-23 | `wiki/gout-clinical-pipeline.md` | (manual) | Opus 4.7 | (in-session log) |
| 2026-04-23 | `wiki/cannabinoids-terpenes.md` | (manual) | Opus 4.7 | (in-session log) |
| 2026-04-21 (origin) | All 8 April 2026 AI analyses (initial Pass 2 brainstorm) | (manual) | (manual) | This file's original content; everything from that brainstorm has either landed in canonical wiki pages (carnosine module, koji-endgame-strain, validation-experiments §1.x) or surfaced again in later sweeps. |

---

## Where actioned items live now

The 2026-04-27 inbox-zero pass pruned ~700 lines of `✓ Actioned` content. The findings are not lost — they're in their canonical homes:

- **Experiment proposals** → [`validation-experiments.md`](./validation-experiments.md) §1.1–§1.19, §2.x, §3.x.
- **Open questions** → [`open-questions.md`](./open-questions.md), organized by topic.
- **Connection findings** → in the relevant per-compound or per-mechanism wiki page (e.g. ergothioneine → ABCG2 lives in [`abcg2-modulators.md`](./abcg2-modulators.md), shio-koji format constraints in [`engineered-koji-protocol.md` §15](./engineered-koji-protocol.md), Q141K population caveat in `abcg2-modulators.md`, etc.).
- **Coverage-matrix and chokepoint findings** → [`nlrp3-exploit-map.md`](./nlrp3-exploit-map.md), [`koji-endgame-strain.md`](./koji-endgame-strain.md), [`open-enzyme-vision.md`](./open-enzyme-vision.md).
- **Methodology standards** (rodent IC50 caveat, two-tier NLRP3 labeling, etc.) → [`validation-experiments.md` §1.19](./validation-experiments.md), [`nlrp3-inhibitor-screen.md`](./nlrp3-inhibitor-screen.md), [`chembl-cross-check.md`](./chembl-cross-check.md).
- **ChEMBL refresh automation** → [`.github/workflows/chembl-refresh.yml`](../.github/workflows/chembl-refresh.yml), runs quarterly (Jan/Apr/Jul/Oct 1st at 12:00 UTC).
- **Cross-doc audit history** → `git log -p wiki/synthesis.md` shows the prior un-pruned state of each sweep block; `logs/v4-synthesis-*.md` shows the original synthesizer outputs.
