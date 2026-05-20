---
title: Open Enzyme — Notable Moments Log
date: 2026-05-05
status: active
---

# Notable Moments Log

Append-only log of moments in the project that are worth external communication — blog post, LinkedIn post, conference talk, podcast soundbite, whatever. The bar isn't "every commit" or "every finding." The bar is **"something a non-OE-native reader would find genuinely interesting or surprising."** Often these are inflection-point moments where a long-held assumption breaks, or where a methodology produces a non-trivial result, or where AI-assisted research velocity does something a human-only workflow couldn't.

Each entry has: **date**, **headline** (one-line, scan-friendly), **what happened** (substantive but accessible — CTO not PhD framing per `CLAUDE.md`), **why it matters** (for the external-audience reader, not for the OE corpus), and **external-comms angle** (suggested framing for a post/talk).

This log is **public** (operations/ folder is in the public repo) — same posture as the rest of the project. Radical transparency is a feature; readers seeing the working state is the point.

---

## 2026-05-20 — "NLRP3 is empty in fungi" was query-framing-empty, not biology-empty. The AI substrate's multilingual + traditional-formula competence was being silently underused for two weeks before the audit caught it.

**What happened.** Two weeks ago a computational experiment (comp-014) systematically mapped 6,798 fungal compounds against 24 inflammation-axis targets to find candidates for the medicinal-mushroom-complement track. The verdict for NLRP3, ASC, and caspase-1 (the central inflammasome chokepoints that drive gout flares) came back: **empty in fungi.** Zero compounds at curated-activity tiers. That verdict propagated into [`medicinal-mushroom-compound-mapping-computational.md`](../wiki/medicinal-mushroom-compound-mapping-computational.md), routed downstream into the chassis-pending interventions framework, and sat there. The implicit logical conclusion: mushroom polysaccharide chemistry doesn't engage the central inflammasome pathway at gout-relevant potency, so the cultivation track can't directly close the NLRP3 chokepoint and the koji-engineering track is where NLRP3 coverage has to come from.

**Yesterday's retrospective audit found that verdict was wrong.** The 2026-05-19 [lit-scan query-framing retrospective](../logs/lit-scan-query-framing-retrospective-audit-2026-05-19.md) walked back through every prior comp-NNN that touched non-Western compound classes and asked: *did the seed query actually search for what's in the literature, or did it search for what's in ChEMBL?* The pattern was visible after a couple of items: ChEMBL is Western-curated medicinal-chemistry data. Seeding compound lists from ChEMBL pure-compound activity columns and then mapping to PubMed catches Western-published natural-product chemistry. It misses entire subfields of non-Western traditional-medicine literature where the paper is anchored against a species name, a traditional-formula name, or a traditional-pathology term — not against a curated Western target column.

**The species-name + traditional-formula re-scans surfaced what the original framing had missed.** Three [parallel re-scans](../logs/) on 2026-05-19 hit the medicinal-mushroom corpus from species-anchored angles, the URAT1 chokepoint via classical Chinese gout formulas (Bai Hu Jia Gui Zhi Tang, Si Miao San, Wu Ling San), and the xanthine-oxidase chokepoint via classical Chinese herbal formulas (Huo Xiang Zheng Qi, Wu Mei Wan, etc.). The recovery rate was substantial:

- **NLRP3 axis in fungi: not empty.** ≥18 fungal sub-form × NLRP3-axis papers in PubMed under species-name + traditional-pathology framing, ≥5 at the gout indication itself (MSU + HUA rodent models). The strongest single-species fit was *Phellinus igniarius* (桑黄, sang huang), which covers four chokepoints simultaneously — XO + NLRP3 + URAT1 + bile-acid axis — across four independent papers. *Cordyceps militaris* in a 2023 head-to-head puts NLRP3 (not URAT1 alone) as the primary anti-MSU mechanism. *Antrodia camphorata* has an NLRP3-selective triterpenoid (Antcin-H). *Ganoderma lucidum* sub-fractions (spore-powder S-GLSP and pentapeptide GLP4) hit NLRP3 by routes distinct from the bulk triterpenoid / polysaccharide chemistry.
- **The chokepoint isn't fungal-empty; it was query-framing-empty.** Same biology, different lens.
- **Falsifying counter-finding preserved:** lentinan (the polysaccharide most associated with shiitake) was explicitly tested against MSU and came back **negative on NLRP3**. Shiitake's anti-inflammatory contribution travels via the AIM2 inflammasome and cardiovascular eritadenine, not via NLRP3. Reframing the chokepoint as "not empty" didn't collapse into "all mushrooms work" — the discipline preserves the negative result.
- **Bonus recovery on the ABCG2 chokepoint:** *Wolfiporia cocos* (茯苓, Fu Ling — a canonical ingredient of the Si Miao San gout formula) elevates intestinal ABCG2 mRNA + protein in hyperuricemic mice with effect magnitude **exceeding benzbromarone** (the gold-standard uricosuric drug used as positive control). This was missed by comp-014's Phase 3 because Poria triterpenes are outside ChEMBL's curated activity table.
- **comp-013 (TCM gout compound triage) ten-item correction batch.** Mangiferin / Zhi Mu (Anemarrhena asphodeloides — cardinal herb of the Bai Hu Jia Gui Zhi Tang ChiCTR-registered RCT) added as tier-1 URAT1. Coix seed oil mechanism upgraded from "atractylenolide I = unclear" to four-transporter coverage (URAT1 + GLUT9 + OAT1 + ABCG2) at 73–87% SUA reduction. Plantago seed attribution corrected from aucubin to acteoside + apigenin + geniposidic acid via PPAR. Multiple other separations and reframes.

**The discipline upgrade.** The 4-framing seed-query matrix is now codified at four operational layers:

1. **Project rule** in [`CLAUDE.md`](../CLAUDE.md) §"Global-multilingual research by default" — every comp-NNN scan touching natural products / TCM / Kampo / Ayurveda must seed from (a) Western mechanism-name, (b) species-name + original-language characters, (c) traditional formula composition, (d) traditional pathology term.
2. **Daemon prompt** in [`scripts/sweep-prompt-2-synthesize.md`](../scripts/sweep-prompt-2-synthesize.md) — Pass 2 synthesis flags chokepoints showing "empty" status from mechanism-only scans as candidates for query-framing re-scan rather than confirmed empty.
3. **Manual lit-mining discipline** in [`wiki/etc/manual-literature-mining.md`](../wiki/etc/manual-literature-mining.md) §"Query-framing for non-Western compound classes" — minimum 4-framing matrix with explicit interaction with the existing pre-commit grep-verify gate.
4. **New-comp-experiment skill** at [`.claude/skills/new-comp-experiment/SKILL.md`](../.claude/skills/new-comp-experiment/SKILL.md) — every new experiment now writes its query strategy to `inputs/query-strategy.json` so future re-scans can detect query-framing gaps mechanically rather than via closure-annotation audit.

**Why this matters.** This is the third entry in the multi-vendor AI-assisted research methodology series ([DAF SCR1-4 disulfide hallucination](#2026-05-06--an-ai-agent-invented-a-number-nobody-asked-it-to-invent-the-next-days-process-found-it-heres-exactly-what-happened-and-what-discipline-catches-this), [brief contamination → scrubbed re-run](#2026-05-08--brief-contamination-is-real-a-contrived-if-its-in-rosemary-ill-grow-rosemary-example-landed-verbatim-in-the-subagent-brief-and-biased-the-headline-finding-a-scrubbed-re-run-found-something-better)). The earlier entries were about *false positives* — the AI invented a number, or the user's framing biased the headline finding. This one is about *false negatives* — the AI didn't invent anything; it correctly reported what its query found. The query just didn't look at the right surface of the literature.

The AI substrate is fluent in Mandarin, Japanese, Korean, classical Chinese formula composition, and the traditional pathology vocabulary that anchors a huge fraction of the natural-product literature. None of that fluency is automatically activated by a Western-default mechanism-name query. ChEMBL is Western-curated. PubMed indexing has Western-language bias even on Chinese-group publications. A seed list that starts from those sources will produce a list shaped by those sources, and the AI substrate's multilingual + traditional-formula competence sits dormant unless the prompt explicitly invokes it.

**The 2026 marginal-cost asymmetry makes this more embarrassing, not less.** Reading a Chinese-language paper in 2026 costs $0 of additional compute — the model already knows the language, the script, the classical formula references, the pharmacopoeia. The "language barrier" framing that justified ignoring non-English literature in pre-AI research is gone. Yet the default query habits were still treating ChEMBL + English-language PubMed as the universe. Two weeks of "NLRP3 is empty in fungi" was the cost of not noticing the asymmetry sooner.

The fix is mechanical: a 4-framing seed-query matrix and a `query-strategy.json` artifact. The discipline is now upstream of the next comp-NNN. The pattern generalizes well beyond gout/NLRP3 — any pharma research touching non-Western traditional medicine has the same exposure to this failure mode.

**Honest framing on how we found it.** The audit didn't fire because the daemon flagged the empty verdict as suspicious. It fired because Brian was working through the synthesis queue, noticed that comp-018 Phase 2 had identified citation-network insularity + traditional-formula-name framing as the diagnosis at the complement chokepoint, and asked: *what other comp-NNN experiments would have the same exposure?* That question triggered the retrospective. The discipline is now codified so the next comp-NNN doesn't depend on the same kind of cross-experiment intuition firing — but credit where due: the catch came from human pattern-matching across walkthrough closure annotations, not from any individual daemon pass. Instinct first, discipline after. Same ordering as the brief-contamination entry, same lesson: the multi-vendor + multi-pass infrastructure is the floor, not the ceiling, on what catches errors.

**External-comms angle.** This is a clean third-in-a-series methodology post: hallucination → contamination → query framing. Each is a structural failure mode of AI-assisted research that doesn't exist (or doesn't exist in the same shape) in human-only research. The arc:

- **DAF SCR1-4 disulfide hallucination (2026-05-06):** AI invented a number. Multi-vendor sweep caught it the next day. *Lesson: cross-vendor heterogeneity catches single-model confabulation.*
- **Brief contamination → rosmarinic acid (2026-05-08):** User framing biased the headline finding. Scrubbed re-run produced a better answer. *Lesson: prompts are part of the experimental setup; control for prompt-level variables the way you control for any other.*
- **Query-framing reversal (2026-05-20, this entry):** Western-default query habits silently filtered out entire subfields of non-Western literature. 4-framing seed-query matrix recovered the missing evidence. *Lesson: the AI substrate's multilingual + multi-framing competence is a strength your default queries probably aren't using; you have to invoke it explicitly.*

The post writes itself if Brian wants to write it. The audience that benefits most is citizen scientists, independent researchers, and pharma research groups that touch any non-Western traditional medicine — same audience as the brief-contamination piece. For that audience, the actionable takeaway is the 4-framing matrix itself, which is short enough to fit in a tweet and concrete enough to apply tomorrow.

For pharma research groups specifically, the implicit invitation is to audit their own seed-list construction practices. If a current "we systematically scanned X chokepoint and found no candidates" verdict was produced by a ChEMBL-anchored mechanism-name query, the 4-framing re-scan is cheap enough (~$5 in compute, hours of wall-clock, no wet-lab cost) to be the default audit move.

The full per-scan retrospectives live at [`logs/lit-scan-query-framing-retrospective-audit-2026-05-19.md`](../logs/lit-scan-query-framing-retrospective-audit-2026-05-19.md) and the three triggered re-scans ([mushroom traditional-name](../logs/mushroom-traditional-name-nlrp3-rescan-2026-05-19.md), [URAT1 classical-formula](../logs/urat1-classical-formula-rescan-2026-05-19.md), [XO classical-formula](../logs/xo-classical-formula-rescan-2026-05-19.md)).

Notable for: AI-assisted research methodology, non-Western traditional medicine in pharma R&D, the structural property that default query habits are baked-in research-bias the AI substrate is positioned to escape *if* the prompt explicitly invokes the escape.

---

## 2026-05-08 — Brief contamination is real: a contrived "if it's in rosemary I'll grow rosemary" example landed verbatim in the subagent brief and biased the headline finding. A scrubbed re-run found something better.

**What happened.** Today's wiki sweep proposed running comp-018 (Upstream Complement Modulator Sweep) — a literature-mining experiment to find compounds that interfere with the complement cascade upstream of C5a. While Brian was clarifying the scope on his end (telling Claude to broaden beyond just fungal compounds), he said *"if the answer is rosemary, I'll grow some fucking rosemary"* — meant as a contrived example, the first herb that popped into his head, not as an actual hint about what to look for.

Claude (drafting the comp-018 subagent brief) included that exact phrase verbatim as motivational framing. The subagent then ran a 32-compound breadth scan and came back with **rosmarinic acid** (the active compound in rosemary, lemon balm, and spearmint, named after rosemary because it was first isolated from rosemary in 1958) as the singular headline finding — TIER-1 dietary C3-convertase inhibitor, IC50 5-10 µM optimal, three independent in vivo precedents, FDA-GRAS source plants, and the subagent's report-back literally said *"Brian's literal 'if it's in rosemary I'll grow rosemary' framing landed empirically."*

Brian's first reaction was suspicion: *"This has got to be a hallucination — I just said rosemary because it was the first herb that popped into my head, and now you're telling me there's a compound called rosmarinic acid that does this exact thing?"* That suspicion was the catch.

**Verification, layer 1:** the underlying claim is real. Englberger et al. 1988 (PMID 3198307) is a real foundational paper titled literally *"Rosmarinic acid: a new inhibitor of complement C3-convertase with anti-inflammatory activity."* Two follow-on in vivo precedents (Proctor 2006 PMID 16782534; Su 2014 PMID 24494798) extended the evidence. Rosemary is FDA GRAS. Rosmarinic acid is *the* most well-characterized natural-product upstream complement modulator in the published literature. Not a hallucination. The "coincidence" between Brian saying rosemary and the headline being rosmarinic acid is partly explained by name-bias: rosmarinic acid is named after rosemary specifically because rosemary is where it was first isolated, so any complement-related compound found in plants will over-index in rosemary.

**Verification, layer 2 (the actually-noteworthy part):** Brian asked Claude to write a *scrubbed* version of the subagent brief — no compound names, no user-framing phrases, no contrived examples — and re-run the sweep as comp-020 to test whether rosmarinic acid as headline was a real result or a contamination artifact.

The comp-020 (scrubbed) re-run came back with three significant differences from comp-018:

1. **No singular headline.** Three tier-1 candidates tied within 20%: *Helicteres* benzofuran lignans (CH50 9/40 µM — the highest-potency single hit in the corpus, single-paper anchor PMC6273495, needs replication), rosmarinic acid (still real, still tier-1, but not singular), and luteolin (a dietary flavonoid with three independent gout-relevant mechanisms across the OE corpus).

2. **comp-018 missed Helicteres entirely at the headline tier.** *Helicteres* benzofuran lignans beat rosmarinic acid by 4-20× on a matched CH50 hemolytic assay. comp-018's brief contamination apparently nudged the subagent toward narrative-cohesion with the user's "rosemary" framing strongly enough that Helicteres got buried.

3. **comp-018 underweighted marine sulfated polysaccharides** (Ascophyllum ANW, sea cucumber SC, Saccharina SJW-3) — IC50 0.98-3.11 µg/mL, with the caveat that they have anticoagulation safety considerations.

4. **The rosmarinic acid IC50 spread is wider than comp-018 reported** — 44× across assays (34 µM C3b deposition vs. 1500 µM C5 convertase), which implies RMA's load-bearing mechanism is upstream covalent C3b modification rather than direct C5 convertase inhibition. comp-018 framed it less precisely.

**Verdict on the contamination:** underlying findings were NOT contaminated (rosmarinic acid IS real and surfaced again on independent search). Headline-promotion WAS contaminated (comp-018 promoted it singular; comp-020 places it in a 3-way tie). Coverage breadth was PARTIALLY contaminated (comp-018 missed Helicteres at headline tier and underweighted marine polysaccharides; comp-020 surfaced both).

**Brian's suspicion was empirically correct.**

**Why it matters.** AI-assisted research has a class of confounder that doesn't exist in human-only research: **prompt contamination**. If the user's phrasing ends up in the subagent brief — through carelessness, motivational framing, or just unconsidered handover — the subagent can be biased toward narrative-cohesion with the user's framing without ever overtly hallucinating. The subagent does what its brief said; the brief silently constrained the answer.

The fix is upstream of the subagent: **brief hygiene at the moment of brief composition.** Scope and method propagate from user direction (those describe the work). Predictions and contrived examples don't (those describe the user's hopes about the work). Independent re-run with scrubbed framing — at ~$5 in compute and 30-60 minutes wall-clock — is cheap enough to make a default whenever a brief contains user-named compounds or phrases.

For citizen scientists doing AI-assisted research without the multi-pass safety net the Open Enzyme project has: **this is a category of error you should know about. Your prompt is part of the experiment. Control for it.**

**The catch came from Brian's instinct, not the discipline.** The discipline is being formalized AFTER the suspicion forced verification. That's the right ordering for first-time issues — instinct catches it once, discipline prevents the next instance.

**External-comms angle.** Builds on yesterday's DAF SCR1-4 disulfide-hallucination story (single-AI confabulation caught by multi-vendor sweep) and on this morning's "two independent reads of the same wiki, same day, same insight" story (multi-vendor convergent intelligence). Today's story is the third in the series: **brief-level multi-vendor heterogeneity guard**. Different prompt → different output. The same multi-pass discipline that catches model-level errors also catches prompt-level contamination, but you have to apply it explicitly.

The full retrospective with side-by-side comparison and recommendations for citizen-science workflows lives at [`operations/comp-018-vs-comp-020-retrospective.md`](./comp-018-vs-comp-020-retrospective.md). The methodological discipline is codified at [`scripts/SWEEP-ARCHITECTURE.md`](../scripts/SWEEP-ARCHITECTURE.md) §"Subagent brief hygiene." Three story arcs across three days — homogenization (DAF SCR1-4), convergent insight (DAF retrospective post), and brief contamination (this entry) — together describe the multi-vendor discipline as a search amplifier, an opportunity surface, AND a confounder guard. None of these were predictable from first principles; all of them surfaced empirically.

Notable for: AI-assisted research methodology, citizen-science workflow design, the structural property that subagent briefs are part of the experimental setup and not just project-management overhead.

---

## 2026-05-08 — Two independent reads of the same wiki, same day, same external-comms insight: multi-vendor heterogeneity catching opportunities, not just errors

**What happened.** This morning Brian published [Grounding the AI Scientist Hype](https://0xbpa.substack.com/p/grounding-the-ai-scientist-hype) on Substack — a public case study using the DAF SCR1-4 disulfide-count incident (logged 2026-05-06 in this same file) as the canonical example of how AI-assisted scientific research catches its own hallucinations through multi-vendor verification, not by avoiding them. The post went live before the day's wiki sweep daemon ran.

Later the same day, the sweep daemon fired on commit `e842754`. The synthesizer (Gemini 2.5 Pro) independently surfaced as a Pass 2 finding: *"Write up the DAF SCR1-4 incident as a mini case study … a potent, concrete case study that validates the entire linter-and-sweep approach."* The Pass 3 reviewer (GPT-5.5, freshly swapped into this slot this morning, replacing Claude Opus 4.7) pushed back: "the wiki already documents the loop-closure." Narrowly true — `manual-literature-mining.md` §"The DAF SCR1-4 incident" and the 2026-05-06 entry in this file both have the wiki coverage. But the synthesizer wasn't suggesting wiki coverage. It was suggesting **public communication**, which had already happened, on a surface the daemon by design cannot see (the personal blog repo is private; the public sweep daemon must not read private siblings, by the umbrella's one-way privacy gradient).

So: the synthesizer was right about what to do. Brian had already done it six hours earlier. The reviewer couldn't verify the external action because the daemon's scope is correctly bounded to the wiki.

**Why it matters.** The original framing of multi-vendor heterogeneity in this project was *defensive* — different vendors cross-checking each other to catch errors that single-vendor pipelines would homogenize. The DAF SCR1-4 incident itself was the canonical demonstration: Sonnet hallucinated a number, the multi-vendor sweep caught it the next day.

What happened today is *generative*. Two completely independent reads of the same substrate — a Gemini-based wiki synthesizer running unattended, and a human writer drafting a blog post over coffee — converged on the same external-comms angle without coordination. The same multi-vendor heterogeneity that catches wrong numbers also catches valuable opportunities. That's a different and more interesting validation of the multi-model thesis than the original framing anticipated.

There's also a structural property worth naming, separate from any specific model's calibration: the wiki sweep daemon is a **closed-system tool**. It operates on the wiki, by design and by the project's privacy gradient. So when the synthesizer points outside the closed system — at external comms, sibling-repo work, application surfaces — the reviewer's "already covered" verdict is necessarily scoped to *the wiki*. Coordination of work outside the daemon's scope stays a human responsibility. That's not a defect; it's the correct architecture for a public daemon. It just means Pass 3 verdicts of "already covered" carry an implicit "in the wiki" qualifier.

**External-comms angle.** The previous DAF SCR1-4 post framed multi-vendor heterogeneity as an error-correction discipline. The natural follow-on — this entry — is about the *generative* property: when you have multiple competent agents reading the same substrate independently, they don't just catch each other's mistakes, they converge on the same valuable angles. Three things stack: the original homogenization risk (DAF SCR1-4) → multi-vendor catches the error; the convergent-insight moment today → multi-vendor surfaces the same opportunity; and the closed-system property (the daemon is by-design wiki-scoped, so external action is by-design human-coordinated). Story arc: heterogeneity isn't just a safety net, it's a search amplifier.

Notable for: open-source-research workflow design, AI-assisted science methodology, the tension between agent-driven discovery and human-driven editorial judgment, the structural property that public-facing daemons are correctly scope-limited.

---

## 2026-05-07 — The "37% testosterone increase" figure all over the tongkat ali supplement market is salivary T in a mixed-sex stressed cohort. Verification gate caught the laundering.

**What happened.** Today's lit-scan task: a multilingual literature review of natural alternatives to Clomid (clomiphene citrate) for free-testosterone elevation, framed for the gout-comorbid male on SERM therapy. (The trigger was a specific n=1 self-experiment situation; the page itself is genericized in `wiki/androgen-natural-modulation.md`.) Among the seven sub-investigations, *Eurycoma longifolia* (tongkat ali) showed up as the best-evidenced herbal candidate — there's a real RCT corpus.

The lit-scan subagent, drafting from working memory without live PubMed access, flagged a suspicious pattern: the headline figure **"~37% testosterone elevation"** recurred across three "independent" Physta-extract RCTs (George 2014, Talbott 2013, Tambi 2012) in suspicious lockstep. Either consistent biology — or a marketing-cycle copy-paste contaminating the corpus. The draft was committed with `[VERIFICATION-PENDING]` markers per the project's pre-commit grep-verify gate (CLAUDE.md Rule 4, codified yesterday after the DAF SCR1-4 incident).

**The verification, performed by a follow-up subagent with PubMed access:**

The "37%" figure is genuinely from Talbott 2013 (*J Int Soc Sports Nutr*, PMID 23705671). But:

1. It's **salivary T**, not serum free T or total T.
2. The cohort is **n=63 mixed-sex** moderately-stressed adults — not hypogonadal men.
3. The intervention was Physta 200 mg/d × 4 weeks, ostensibly for cortisol/stress modulation, with T as a secondary endpoint.

The supplement-industry copy-paste pattern across George 2014 (which is itself a *narrative review*, not a fresh RCT — it's *citing* Talbott) and downstream marketing materials uses the figure as if it were generalizable serum free-T elevation in hypogonadal men. **It isn't.** A salivary-T headline number from a mixed-sex stressed cohort is not the same claim as a serum-free-T elevation in low-T men, and the supplement industry has been treating it as if they were interchangeable for a decade.

The same verification pass caught a stack of related errors in the draft, all consistent with the supplement-industry citation laundering pattern:

- "Leitão" systematic review attribution → actually **Leisegang 2022** (PMID 36013514), with subgroup analysis showing no significant T elevation in eugonadal baseline; the supplement marketing tier elides this caveat.
- "Tsukamoto 2002 / Tsujimura 2005" Hochu-ekki-to citations → don't appear in PubMed; actual papers are Ishikawa 1992 (PMID 1519556) and Tsujimura 2010 (PMID 20143961). Wrong year and wrong author on both.
- "Maggio 2014" magnesium-T cohort study → actually **Maggio 2011** (PMID 21675994, CHIANTI cohort n=399). 2014 is a review citing the 2011 cohort; the marketing cited the review.
- Yakubu group (fadogia testicular toxicity) at "Ahmadu Bello University, Zaria" → actually **University of Ilorin**.
- Henkel & Wang 2014 dose: drafted as 200 mg/d, actual is **400 mg/d × 5 weeks**.
- Cinar 2011 magnesium dose: drafted as fixed mg/d, actual is **10 mg/kg/d**.
- Hochu-ekki-to drafted as containing epimedium → it doesn't.
- Wu Zi Yan Zong Wan composition drafted with cistanche/epimedium/cordyceps → actual five-seed formulation is *Lycium / Cuscuta / Rubus / Schisandra / Plantago*.

Eleven specific factual errors caught in a single verification pass on a single page. Most of them inherited from the supplement-industry citation tier rather than originating in the AI subagent's confabulation. The AI didn't invent the "37%" figure — **the supplement industry did, decades ago, and the AI's training corpus reflects that contamination.**

**Update later the same day: the story has three layers, not one.**

Subsequent verification work today on the same page surfaced two more citation-laundering instances, each caught by a different stage of the multi-pass discipline:

**Layer 2 — "Shin KH 2024 enclomiphene vs clomiphene pharmacology" doesn't exist.** A parallel verification subagent running on the parent page (`wiki/androgen-urate-axis.md`) found the citation can't be located in PubMed. The actual paper fitting the description is **Saffati G et al. 2024, PMID 39434750**, *Translational Andrology and Urology*: n=66 patients, enclomiphene +166 vs. clomiphene +98 ng/dL T, fewer adverse events. The same misattribution had propagated to BOTH the parent and daughter pages — the laundering wasn't a single-page issue but corpus-wide contamination. Caught by: cross-vendor parent-page verification sweep, paired with Sci-Hub-tier paywalled-paper access for confirmation.

**Layer 3 — "Eurycomanone is a xanthine oxidase inhibitor" is wrong; the actual mechanism is multi-target transporter modulation + purine-synthesis suppression.** A Sci-Hub-second-pass verification subagent surfaced what looked like a clean mechanism finding — the supplement-industry summary attributed direct XO inhibition to two PMIDs (31920654, 34785103). That triggered a v2 re-run of comp-015 (the T-axis-adjuvant urate-target mapping experiment) with XO added as the 5th target. **The v2 subagent, reading the primary papers' actual full text, found those PMIDs don't establish XO inhibition at all.** They establish: (1) eurycomanone directly modulates URAT1, GLUT9, ABCG2, NPT1 — a multi-target transporter mechanism, strong gout-favorable; (2) eurycomanol suppresses PRPS-driven purine biosynthesis, a separate gout-favorable mechanism. The "XO inhibitor" attribution was supplement-industry summary contamination — same shape as Layer 1, but inheriting through a different review-paper chain. Caught by: a computational experiment forcing primary-source verification of every load-bearing claim used to motivate it.

**The three layers in one workday on one wiki page:**

| Layer | The laundered claim | What's actually there | Caught by |
|---|---|---|---|
| 1 | "37% T elevation from tongkat ali" | Salivary T in mixed-sex moderately-stressed cohort (Talbott 2013 PMID 23705671) | First verification subagent reading the primary paper |
| 2 | "Shin KH 2024 enclomiphene paper" | Paper doesn't exist; the actual paper is Saffati G et al. 2024 (PMID 39434750) | Parent-page parallel verification subagent + Sci-Hub-tier confirmation |
| 3 | "Eurycomanone is an XO inhibitor" | Multi-target transporter modulation (PMID 31920654) + PRPS purine-synthesis suppression (PMID 34785103); NOT XO | comp-015 v2 computational experiment forcing primary-source verification of the trigger claim |

**The deeper pattern.** All three layers are the same shape from a verification-gate perspective: a load-bearing quantitative or mechanistic claim entered the corpus by inheritance from supplement-industry summary tier, not from primary-source verification. **Different stages of the discipline caught different instances of the same contamination.** No single verification step caught all three:

- Layer 1 surfaced because the first subagent had PubMed full-text access for the most-cited tongkat ali RCTs.
- Layer 2 surfaced because the parent-page sweep ran in parallel on the same misattributed citation appearing in both parent and daughter — cross-page consistency-checking caught what neither single-page sweep would have caught alone.
- Layer 3 surfaced because the computational experiment forced primary-source verification of even the trigger that motivated the re-run — verification-of-verification.

**The recursive lesson.** In supplement-industry-adjacent literature corpora, **even the verification process can inherit upstream laundering.** The Sci-Hub pass that surfaced Layer 3's trigger honestly reported what the secondary literature said about eurycomanone-XO. The computational experiment (Layer 3 catch) verified against the primary papers and found the secondary literature had laundered a claim that wasn't in the primary text. **Verification-of-verification is not paranoia; it's how multi-stage cross-checking actually catches multi-layer corpus contamination.**

The yield from a single workday on a single wiki page: **3 distinct citation-laundering layers, ~13 specific factual corrections, one direction-of-effect reversal (eurycomanone v1 GOUT-UNFAVORABLE → v2 GOUT-FAVORABLE) that materially shifts platform recommendations.** Cost: roughly $3-4 in subagent tokens across four parallel passes. The cost of skipping the verification stack: a wiki indistinguishable from any health-content blog post.

**Why it matters.** The DAF SCR1-4 incident yesterday was an AI hallucinating a number nobody asked for. Today's tongkat ali finding is structurally different and arguably more interesting: **the AI faithfully reproduced a number the supplement industry has been laundering for years.** The training data was contaminated; the AI inherited the contamination; only the multi-pass verification gate (per-claim primary-source check) surfaces the error.

This generalizes. Anyone running an AI-assisted lit scan on supplement / nutraceutical / "natural" anything is going to inherit the same citation laundering. The specific names will differ (boron Naghii 2011 is the entire evidentiary base for "boron raises T," n=8, never replicated in 14 years; that's a separate finding from the same pass). The pattern is constant: a single small study, a hyperbolic interpretation, decades of citation drift, and a corpus that looks rich but rests on a thin and often wrongly-described primary literature.

**The verification discipline that catches it:** for every effect-size, dose, sample-size, p-value, or direction-of-effect claim in newly-authored content, grep-verify against the primary source before commit. Use a different model in a different vendor for verification than the one that drafted the original. Flag what can't be verified inline (`[VERIFICATION-PENDING — searched PubMed 2026-05-07; primary not freely accessible]`) rather than fabricating.

The cost of the verification pass on this page: ~$1 in subagent tokens, ~9 minutes wall-clock, eleven factual corrections landed. The cost of skipping the verification pass: a wiki page that confidently misrepresents a salivary number as a serum claim, propagating into downstream synthesis, indistinguishable from any other supplement-industry blog post.

**External-comms angle.** Strong blog material with a deliberately funny edge — title-tier candidates:

- *"The supplement industry has been quoting a salivary testosterone number as if it were a serum number for 13 years. AI-assisted lit scans inherit the laundering. Here's the gate that catches it."*
- *"Your tongkat ali bottle says '37% testosterone increase.' Here's where that number actually came from."*
- *"How an AI agent's lit scan caught the supplement industry quoting saliva like it was blood."*
- *(Meta-angle, for the three-layer version of the story)*: *"In one workday on one wiki page, we caught three distinct layers of supplement-industry citation laundering. Each was caught by a different stage of the verification discipline. None would have surfaced under a single-pass workflow. Here's the architecture, with concrete examples of what each layer looked like and what caught it."*

Tone: dry, evidence-driven, faintly amused. **Don't shame the supplement industry directly** — the laundering is structural (small-study finding → simplified citation → marketing copy → derivative marketing copy → AI training corpus → AI summary → consumer), and naming the structure is more useful than naming bad actors. The hero of the story is the verification gate, not the AI catching it; the lesson is that anyone running AI-assisted health-content research needs the gate.

Adjacent post angles from the same verification pass: the boron Naghii 2011 single-study problem ("a 14-year-old n=8 study is the entire evidentiary base for the supplement industry's boron-T-elevation claim"); the fadogia agrestis Huberman-popularization vs zero-human-RCTs gap; the tendency for "kidney yang tonic" Chinese RCTs to elide UA as a tracked endpoint despite being relevant. Each is its own post; together they're a series on supplement-industry citation hygiene.

**The continuity with yesterday's DAF entry:** that one was an AI inventing a number. Today's is the AI inheriting an industry's bad number. **Both are the same class of problem from the verification-gate perspective** — a load-bearing quantitative claim entered the corpus without being grep-verified against a primary source — and both fail the same way absent the gate. The discipline isn't model-specific; it's claim-specific.

---

## 2026-05-06 — An AI agent invented a number nobody asked it to invent. The next day's process found it. Here's exactly what happened and what discipline catches this.

**What happened.** Yesterday (2026-05-05), an AI subagent was asked to write up a computational experiment on a complement-system protein called DAF/CD55 (specifically a truncated version called SCR1-4, relevant to the project's CP0 chokepoint closure thesis). The experiment itself was a protease-stability analysis — does the protein survive being cooked into the koji-fermentation environment? The AI's analysis pipeline used AlphaFold-predicted protein structure to score how exposed each protease cleavage site is. The experiment is well-defined and reproducible.

The pipeline does NOT count disulfide bonds. The page itself, in its own Limitations section, says explicitly: *"Disulfide bonds not modelled."*

But the AI agent, while writing the page, asserted in 4 places of prose narrative that the protein contains "3 conserved disulfide bonds per SCR domain → 12 total disulfides." Nobody asked it for that number. The pipeline didn't compute it. There was no source attached to the claim. The agent just wrote it confidently, in flowing scientific prose, in multiple spots.

The number then propagated overnight into a related "falsification card" page (the project's pre-registered hypothesis-tracking discipline) which used "12 disulfides" to derive a downstream calculation: "12 + 17 = 29 total disulfide bonds across the proposed three-cassette engineered strain — a real but not catastrophic increase." That 29 number then drove a chaperone-load synergy analysis predicting the strain might be at risk of folding-pathway saturation.

Today (2026-05-06), the project's wiki sweep daemon (a multi-pass system that uses Gemini, Claude, and DeepSeek across different vendors to cross-check every wiki edit for inconsistencies) flagged the discrepancy: the chaperone-orthogonal stacking framework page had "8 disulfides (4 SCRs × 2 disulfides each)," while the comp-012 page and the H05 stub said "12." Two pages disagreed on a load-bearing structural number.

**The verification, performed live during the walkthrough:** queried UniProt directly for the canonical human DAF/CD55 entry (P08174) and pulled the disulfide-bond feature annotations. The result:

```
FT   DISULFID        36..81    ┐ SCR1: 2 disulfides
FT   DISULFID        65..94    ┘
FT   DISULFID        98..145   ┐ SCR2: 2 disulfides
FT   DISULFID        129..158  ┘
FT   DISULFID        163..204  ┐ SCR3: 2 disulfides
FT   DISULFID        190..220  ┘
FT   DISULFID        225..267  ┐ SCR4: 2 disulfides
FT   DISULFID        253..283  ┘
```

**Eight disulfide bonds, not twelve.** Two per SCR domain, four domains, total of eight. This is the canonical sushi/CCP fold (Cys1–Cys3 + Cys2–Cys4 motif) — textbook complement biology. The chaperone framework page happened to have used the textbook number; the comp-012 + H05 pages had been fabricated.

The fix landed within ~30 minutes: corrected numbers in 5 places of comp-012 + 2 places of H05, anchored every reference to the UniProt feature annotations, added a "Correction note" to the comp-012 page documenting the error and how it was caught, and codified the missing discipline (a pre-commit grep-verify gate for every load-bearing quantitative claim in newly-authored wiki content) into the project's CLAUDE.md and the canonical methodology page.

**The downstream good news from the correction:** 8 disulfides instead of 12 means the proposed three-cassette engineered strain has a total disulfide load of 25 (17 lactoferrin + 8 DAF) instead of 29. The "can the cell fold all this in its protein-folding factory" question is meaningfully easier than yesterday's pages reflected — glucoamylase has 2, lactoferrin 17, 8 sits comfortably between. The CP0-closure engineering thesis is in better shape than the wrong numbers had suggested.

**Why it matters.** This is the citizen-science-with-AI dynamic in concrete form, with a happy ending and an instructive lesson.

The reassuring part: **the multi-pass cross-vendor process worked as designed.** The wiki sweep is built on the assumption that no single AI model should be trusted to be its own backstop. Different vendors (Gemini, Claude, DeepSeek) have different training distributions, different failure modes, different blind spots. When one model writes the substrate and a different model reads it for synthesis, inconsistencies surface that single-vendor workflows would miss. The DAF disulfide count is exactly the kind of error a single-model loop would propagate happily — but with cross-vendor synthesis on top, it surfaces as a flagged inconsistency within 24 hours.

The unreassuring part: **24 hours is too late.** The wrong number was already in the corpus. It had already been ingested into downstream synthesis (the chaperone-load triple-cassette analysis). It had propagated to a second page (H05). If the sweep daemon had been delayed by a week, the wrong number would have shaped multiple subsequent decisions before being caught. The sweep is a backstop, not a gate — and a backstop is the wrong place to catch fabricated coefficients.

The right place to catch this class of error is **before the content commits.** That's now codified as a project rule (CLAUDE.md Rule 4 + the canonical statement in `wiki/manual-literature-mining.md` §"Pre-commit verification gate"): every load-bearing quantitative claim must be grep-verified against its primary source before the commit lands. UniProt accession + feature annotation. PMID + section. ChEMBL ID + bioactivity record. NCT trial ID + endpoint. The verification takes 30 seconds; the propagation cost of skipping it is days of downstream re-work.

**The general lesson for citizen-science-with-AI work:**

1. **AI models will write confident-sounding scientific prose containing fabricated numbers,** even on tasks where the analysis pipeline didn't compute those numbers. The fabrication is not malicious — it's a side effect of the model trying to produce coherent-feeling explanatory narrative. "3 disulfides per SCR domain" is the kind of number that *sounds* like a textbook fact; it isn't.

2. **Single-model workflows will not catch this on their own.** A single AI loop tends to be internally consistent because it's drawing from one training distribution. Inconsistencies surface when a *different* model reads what the first one wrote and notices the math doesn't work.

3. **Cross-vendor multi-pass review is cheap and worth it.** OpenRouter routes calls to any of a dozen vendors at ~constant marginal cost. Running synthesis through Gemini, then critique through Claude, then peer-review through DeepSeek catches things any single one would miss. The wiki sweep daemon's full cycle costs ~$0.65 and runs in ~9-12 minutes — affordable for a one-person research project.

4. **Cross-vendor review is still a backstop, not a gate.** The right defense is verifying numbers at the moment they enter the corpus. Grep-verify every load-bearing number against a named primary source. Cite line-anchored. If you can't verify, don't ship — write a placeholder and come back to it. "Verify after the fact when the sweep flags it" is a worse posture than "verify before the commit."

5. **Document the discipline in the project's own canon, not just in the heads of the people running it.** The DAF incident is now in two places that future Claude sessions will read: the project CLAUDE.md (which is loaded into every session) and the methodology wiki page (which the sweep daemon ingests). The next subagent that authors a comp-NNN page will be briefed with the verification protocol baked in. A discipline that lives only in someone's head fades; one that lives in the project's instructions persists.

**The interesting community framing:** AI-assisted citizen-science research is going to grow rapidly. The tooling is good enough now (Claude Code + an MCP for literature + access to UniProt/ChEMBL/PubMed APIs + git for version control + a $20/month OpenAI or Anthropic subscription) that one person can run a real research operation. The thing that distinguishes work that contributes to the scientific record from work that fills it with confident-sounding noise is **the verification discipline.** Not the model quality, not the workflow speed, not the tool stack — the verification discipline. The DAF incident is one specific instance of a generalizable lesson: **the AI will hallucinate; the question is whether your process catches it before or after the corpus is contaminated.**

Open Enzyme's working answer is multi-pass cross-vendor sweep + pre-commit grep-verify gate + falsification cards with pre-registered thresholds + line-anchored citation + the manual-literature-mining methodology page that documents all of this. It's not unique to this project — it's a kit of disciplines that any small AI-assisted research operation can adopt. Most of it is documented in this repo's `wiki/` and `scripts/SWEEP-ARCHITECTURE.md`; the rest is in the CLAUDE.md and the falsification cards under `wiki/hypotheses/`.

**External-comms angle.** Strong blog-post material, framed as a case study in AI-research-rigor disciplines, NOT as a "Claude is broken" post. The headline is the verification discipline, not the hallucination. Suggested title: *"An AI agent invented a number on a research project. Here's how the next day's process caught it, and the discipline that prevents the next one."*

Tone: honest about the failure (the model wrote a confident-sounding hallucination, that's a real failure mode, naming it clearly is more useful than minimizing it), generous about the catch (multi-pass cross-vendor architecture worked as designed; the discipline matters more than the model brand), forward-looking (here's the protocol, here's the canonical methodology page, here's the project rule that codifies it — anyone running an AI-assisted research project can adopt this kit).

The substantive value the post offers a thoughtful reader: a concrete checklist they can adapt for their own projects. Not "AI is unreliable" (a non-actionable claim) and not "Claude/Gemini/DeepSeek is great" (a marketing claim) — but "here is the multi-pass architecture, here is the per-claim verification micro-protocol, here is what each component catches that the others miss."

**Three engagement opportunities:**

1. **Other AI-assisted research projects** — the kit of disciplines (multi-pass cross-vendor sweep + pre-commit grep-verify + falsification cards + line-anchored citation) is open and adoptable. If you're running an AI-assisted research operation and your verification posture is "trust the model and hope," this is the upgrade path. The full architecture is documented in this repo: `scripts/SWEEP-ARCHITECTURE.md`, `wiki/manual-literature-mining.md`, `CLAUDE.md`. Clone, adapt, contribute back.

2. **AI-research-tooling vendors** — the failure mode this caught is generic to LLM-authored scientific prose (not specific to any one model). A general "do your tools have a verification gate before content enters a knowledge base" question is worth asking across the major AI-research-tool vendors. The DAF case is a concrete example to point at.

3. **Citizen-science / open-science methodology workshops** — the kit-of-disciplines framing composes well with broader conversations about how AI changes research rigor. The Open Enzyme stack (chokepoint mapping + falsification cards + multi-pass sweep + pre-commit verification) is one specific instance of a methodology that could be generalized, written up, and shared as a workshop or methods paper if anyone wants to organize one.

**The reciprocal invitation, which is the headline of why this entry is in a public log at all:** Open Enzyme is published in public for exactly the same reason as Paperclip — so that other people can find OUR mistakes and make us better. The DAF disulfide-count incident is in this log not because we've solved AI hallucinations (we haven't) but because we want the failure mode and the discipline that catches it to be visible and adoptable. The verification rules we apply to other people's tools (grep every number, anchor identity to canonical metadata, cross-check every claim, line-anchored citation) apply equally to anyone auditing this corpus. We hope readers grep our numbers, find the next fabricated coefficient hiding somewhere we haven't looked, push back on our evidence-tier tags, surface the chokepoint claims we haven't documented honestly enough. **If you find a mistake in this corpus, please tell us. That's the deal we're trying to participate in.**

**Reference:** [`wiki/manual-literature-mining.md`](../wiki/manual-literature-mining.md) §"Pre-commit verification gate" — canonical statement of the discipline. [`wiki/daf-cd55-scr14-truncated-computational.md`](../wiki/daf-cd55-scr14-truncated-computational.md) §1.5 — correction note documenting the specific incident. [`CLAUDE.md`](../CLAUDE.md) §"Core Rules" Rule 4 — the project-level rule that applies to every AI session in this repo. [`scripts/SWEEP-ARCHITECTURE.md`](../scripts/SWEEP-ARCHITECTURE.md) — the multi-pass cross-vendor sweep that caught the inconsistency.

---

## 2026-05-05 — A guy and a laptop found a reliability problem in a well-funded Stanford research tool

**What happened.** Paperclip is the biomedical literature-indexing MCP tool from Stanford's GXL group — well-funded, well-publicized, full-text index across PubMed / bioRxiv / medRxiv / arXiv (~11M papers), the tool everyone in the AI-for-bio space has been excited about. We started using it for OE literature scans earlier in this project's life. In a session a few weeks back, the `map` operator (Paperclip's convenience-aggregation primitive — "give me a summary across N papers matching this query") returned outputs that, when grep-verified against the source papers, contained:

- **Wrong organisms** named in mechanism descriptions (the source papers actually studied a different organism)
- **Fabricated kinetic numbers** — specific IC50 / Km values that did not appear in any of the cited source papers
- **Made-up author affiliations** in citations

In other words, the convenience operator was doing model-side aggregation that filled in plausible-sounding details that weren't actually in the source documents. The `search`, `cat`, `head`, `grep`, `scan` primitives don't exhibit this — they return raw paper content, line-anchored, verifiable. The failure mode is specific to the aggregation step.

The open-source response (today, 2026-05-05): codified a five-rule verification discipline as [`wiki/manual-literature-mining.md`](../wiki/manual-literature-mining.md):

1. Use safe primitives only (search/cat/head/grep/scan); ban `map`/`reduce` from automated workflows
2. Anchor identity to `meta.json` (cite from canonical metadata, not inferred from paper body)
3. Grep-verify all numbers before they enter the wiki
4. Never propagate `map`/`reduce` summaries (treat as un-validated, re-derive from safe primitives)
5. Cite line-anchored, with the project's existing citation format

Plus a memory record (`feedback_paperclip_map_unreliable.md`) so future Claude sessions don't re-discover the failure the hard way. Plus the global-multilingual-search rule + translation-protocol disciplines that combine with this for non-English sources.

**Why it matters.** This is the open-science flywheel working as intended.

Paperclip is a genuinely powerful tool — full-text indexing across ~11M biomedical papers with line-anchored citation surfaces is a real research enablement. Stanford GXL built it and made it usable enough that a downstream project could integrate it via MCP and put it to work. That's the whole premise of open research tooling: build it openly, let people use it, and the ecosystem audits + improves it together.

The five-rule verification discipline isn't a "Paperclip is broken" finding — it's the kind of usage protocol that emerges naturally when a tool gets enough downstream adoption that someone runs into its edges. Every research tool has edges. The valuable thing the open ecosystem can do is document them clearly enough that future users either avoid the edge case or contribute fixes. That's how open infrastructure compounds.

There's also a smaller meta-observation worth naming: **rigor discipline is cheap.** The verification rules (grep every number, anchor identity to metadata, cite line-anchored, never propagate aggregation summaries) don't require headcount or compute — they require attention. A small project that explicitly bakes verification into its workflow can find usage edges that high-velocity research workflows miss. This isn't a critique of high-velocity work; it's an argument for *sometimes* slowing down enough to grep the actual source. The CP0 closure path earlier today was driven by the same discipline — multi-vendor cross-check, falsification cards, every claim verified against named primary sources. The Paperclip finding and the CP0 finding are products of the same epistemic move applied to different problems.

**The interesting community ask:** other research tools probably have analogous aggregation-primitive edges that nobody's documented yet. A community-level audit of "which AI-research-tool primitives are reliable for which use cases" would be valuable infrastructure for everyone building in this space. Open Enzyme's five-rule protocol could be one input to that broader effort.

**Three concrete engagement opportunities:**

1. **Paperclip team / Stanford GXL** — happy to share the specific queries and outputs that surfaced the `map`-operator hallucinations. If the team wants to either fix the operator, restrict it to reliable use cases, or document the edge prominently, the test cases we have would be useful input. This is exactly the kind of feedback loop open research tooling is supposed to enable. If anyone reading this is connected to the GXL group, an introduction would be welcome.
2. **Other AI-bio research projects using Paperclip** — the five-rule protocol in [`wiki/manual-literature-mining.md`](../wiki/manual-literature-mining.md) is open-source and reusable. If your project uses Paperclip for serious synthesis, the verification discipline matters; if you've run into similar or different edge cases, those findings would compose well with ours into a broader usage-protocol document.
3. **The broader AI-for-research-rigor methodology question** — this is one specific instance of a pattern: convenience-aggregation primitives in research tools tend to over-promise relative to their underlying primitive operations. A community-level audit across the major tools would produce real infrastructure value. Worth a workshop / meta-paper / shared document if anyone wants to organize one.

**External-comms angle.** Strong LinkedIn / blog-post material, **framed as the open-science feedback loop working** — not as a competitive finding. The interesting story is:

> "Open research infrastructure is amazing because it lets small downstream users like us audit the tools we depend on, find the edge cases, and share them back. Here's a usage protocol we built for Paperclip after running into its `map`-operator edge. The protocol is open; the test cases are available; we'd love for the Paperclip team to either incorporate the findings or tell us we got it wrong. This kind of small mutual contribution is what makes the open-research-tooling ecosystem actually work."

Tone: grateful (Paperclip is genuinely useful — that's why we built workflow on top of it), collaborative (sharing back so the tool gets better, not gotcha), substantive (concrete query patterns + verification protocol, not vague "it's unreliable"), forward-looking (community audit of similar primitives across other tools as the bigger opportunity). Close with the protocol link + the explicit "happy to share test cases with the Paperclip team."

**And the explicit reciprocal invitation, which is the headline:** Open Enzyme is published in public for exactly the same reason. Every wiki page, every comp-NNN experiment, every falsification card, every chokepoint claim — everything is open and inspectable specifically so that other people can find OUR mistakes and make us better. The five-rule verification protocol we built for ourselves applies equally to anyone auditing what we've done. We hope people grep our numbers, cross-check our citations, push back on our evidence-tier tags, and surface the edges we haven't named yet. Mutual audit is the whole point — Stanford's tool got audited because it's open; ours is open for the same reason. **If you find a mistake in this corpus, please tell us. That's the deal we're trying to participate in.**

**Reference:** [`wiki/manual-literature-mining.md`](../wiki/manual-literature-mining.md) — the formal verification protocol. Memory record: `feedback_paperclip_map_unreliable.md` (memory file, not wiki; documents the failure history).

---

## 2026-05-05 — Patent landscape on the koji-endgame architecture: clean FTO + a lapsed Novozymes patent that quietly validates the design

**What happened.** Asked an Opus subagent to do an exhaustive patent-landscape deep-dive on *Aspergillus oryzae* dual-heterologous-cassette expression — across Espacenet, Google Patents, USPTO, Lens.org, JPlatPat (Japan), CNIPA (China), DPMA (Germany). The motivation: H01 Killshot #1 (the academic-literature pass that ran earlier today) flagged ~30% probability of unpublished industrial IP from Novonesis (formerly Novozymes), DSM-Firmenich, or Genencor that could either validate the architecture, kill it, or block freedom-to-operate.

**Result: CONFIRMS NOVELTY** — no patent in any database discloses two heterologous proteins co-expressed in *A. oryzae* solid-state rice koji at therapeutic-grade titers, in any language. The §1.9 architecture remains genuinely first-in-class on the heterologous × solid-state × dual-cassette × therapeutic-titer axis.

**The interesting side finding:** **WO2017211803 (Novozymes 2017) directly claims dual-heterologous co-expression in filamentous fungi including *A. oryzae*. Status: ceased 2018-12-07 — architecture is now in public domain.** Examples in the patent are *A. niger* shake flask, not *A. oryzae* solid-state, but the fact that Novozymes filed it and let it lapse suggests they had internal proof-of-concept the architecture works in filamentous fungi but chose not to commercially pursue it. Industrial-IP residual risk dropped from ~30% (Killshot #1) to <10% (Killshot #1.5). Clean FTO profile for §1.9.

Plus: all foundational patents are expired — Ward 1995 lactoferrin (US5571697), Novozymes EP0238023, Genencor US5364770. The architecture stack is fully open to build on.

H01 status: survival count 1→2, survival score 0.3→0.45.

**Why it matters.** Patent-landscape due-diligence is the most boring and most often-skipped step in academic-style biotech projects. Almost all academic papers presume "if it's not in PubMed, no one's done it" — which silently misses the entire industrial IP corpus. Today's check confirmed that the architecture isn't trapped under active IP, AND that a major industrial player (Novozymes) had the architecture working in shake flask before letting it lapse — useful confidence about feasibility.

**Three places where outside expertise would tighten this further:**
1. **Authenticated Espacenet / Lens.org / Derwent search** — institutional access (e.g., Emory library, IP counsel) would tighten the residual industrial-IP risk from <10% to <5%. The 13 patents this scope found are best-effort via the unauthenticated web; institutional databases catch the corner cases.
2. **Direct trade-secret-side conversation with a Novozymes / Novonesis alumni or DSM-Firmenich alumni** — the residual <10% is unrecoverable from patent corpus alone (trade secrets aren't filed). One conversation with the right ex-engineer would close it.
3. **Read of the Senoo et al. 2024 (PMID 38242757) industrial *A. oryzae* AOK11 work** in detail — closest published precedent (3-4 enzymes co-expressed in solid-state, but self-cloning not heterologous). Brackets the H01 cell from another direction.

**External-comms angle.** **LinkedIn post (~150-300 words):** "Patent due diligence is the boring step nobody does. Here's what we found." Show the WO2017211803 lapsed-Novozymes finding. Frame it as an "open-source biotech compounding effect" — a major industrial player's architecture work falls into the public domain, and an academic-style open-source project picks it up. End with H01 status + the soft ask for institutional patent-database access.

**Reference:** [`wiki/hypotheses/H01-ward-dual-cassette.md`](../wiki/hypotheses/H01-ward-dual-cassette.md) — Killshot #1.5 Findings section has the 13-patent table + assumption-stack delta.

---

## 2026-05-05 — comp-011: don't pick — run BOTH uricase variants in parallel at ~$200 extra cost

**What happened.** comp-010 ([cassette compatibility for the dual-cassette koji endgame strain](../wiki/cassette-compatibility-computational.md)) had verified LOW design risk for *Aspergillus flavus* uricase + lactoferrin in the Ward 1995 architecture — that was the design we'd been planning. But the wiki's [`uricase-variant-selection.md`](../wiki/uricase-variant-selection.md) had documented an industry-revealed preference for ***Candida utilis* uricase** instead — three independent commercial programs (Allena/ALLN-346 + two others) had picked *C. utilis* over *A. flavus* for oral delivery. comp-010's LOW verdict didn't transfer automatically: *C. utilis* uricase has a different sequence, different disulfide profile, different KEX2 site profile, different codon-usage profile.

A Sonnet subagent ran comp-011 (the same seven-analysis pipeline, on *C. utilis* uricase). **Result: MODERATE risk vs. *A. flavus* LOW.** Three drivers:
1. **Codon burden 2.3× heavier** (CAI 0.65 vs 1.51) — full codon-optimized gene synthesis mandatory
2. **4 free cysteines** in *C. utilis* (vs. 0 in *A. flavus*) — risk of aberrant ER disulfide formation; mitigation via non-reducing SDS-PAGE QC
3. **2 internal KR sites** (positions 130, 138) — non-load-bearing for direct-secretion design

But the killer recommendation: **don't pick. Run BOTH variants in §1.9 as parallel direct-secretion cassettes** at ~$200–400 in additional gene synthesis cost and $0 additional fermentation cost. The empirical wet-lab comparison resolves the *A. flavus* vs. *C. utilis* platform decision in the same fermentation run.

**Bonus: an accession correction.** P15296 (which the brief had cited as the *C. utilis* uricase) is a defunct/reassigned accession that now returns a Drosophila transposable element protein. Correct canonical entry is **P78609 (URIC_CYBJA)**, verified by taxon search.

**Why it matters.** "Don't pick — run both" is a structurally underused move in early-stage biotech engineering. The cost of choosing wrong (months of wet-lab on the worse variant) is much higher than the cost of running both in parallel ($200 in gene synthesis). The chokepoint methodology naturally surfaces this kind of recommendation because it's not committed in advance to a particular candidate — the framework asks "which variants meet the spec?" rather than "is variant X the right one?"

**Where outside expertise would help:** anyone with experience on *C. utilis* heterologous protein expression in *Aspergillus*. The bioavailability + protease-resistance reasons for the industry's revealed preference are documented; what's missing is published *C. utilis* uricase secretion data in fungal hosts. Could be a Paperclip search-and-grep task using the new [`manual-literature-mining.md`](../wiki/manual-literature-mining.md) discipline.

**Reference:** [`wiki/c-utilis-uricase-cassette-compatibility-computational.md`](../wiki/c-utilis-uricase-cassette-compatibility-computational.md).

---

## 2026-05-05 — CP0 went from "honest platform gap" to "active fermentable engineering candidate" in 6 hours

**What happened.** The wiki had explicitly named complement priming (CP0) as the project's only "honest platform gap" — the one chokepoint in the gout cascade where no fermentable molecule was on the table, and the platform's official stance was "avacopan (a prescription pharma drug) as permanent adjunct." A 2026-04-27 computational scan of natural-product C5aR1 antagonists across ChEMBL / NPASS / LOTUS / Open Targets had returned zero validated hits — that was the prior result.

In one ~6-hour working session today (2026-05-05), the chokepoint methodology + AI-assisted research substrate moved CP0 from "pharma-only territory" to "in silico-validated stalk-truncated DAF/CD55 SCR1-4 construct, structurally comparable to uricase, with a concrete wet-lab proposal." Trace:

| Step | Time | Outcome |
|---|---|---|
| Scoped engineered soluble complement regulators (sCR1 / Factor H / DAF/CD55) as exploration vector | morning | DAF/CD55 ectodomain identified as most tractable candidate |
| comp-006: protease stability of full DAF ectodomain | midday | HIGH risk — disordered Ser/Thr stalk drives all the exposed sites |
| Sweep daemon's Pass 2 (DeepSeek V4-Pro) found the truncation hypothesis explicitly | afternoon | "A construct truncated at SCR4 would remove all exposed sites" |
| comp-012: protease stability of SCR1-4 truncated (aa 35-285) | evening | **LOW (0.039) — identical to uricase** |

The platform's CP0 status shifted from **"avacopan dependency"** to **"fermentable candidate identified, computationally validated, three known wet-lab unknowns"** — in a single session.

**Why it matters.** Gout research has treated complement priming as pharma-only territory because (a) C5a is a hard target for natural-product antagonism, (b) the FDA-approved compound (avacopan) is mechanically clean but commercially expensive ($60K+/year in some indications), (c) heterologous expression of human soluble complement regulators in food-grade GRAS organisms simply hadn't been seriously scoped for any indication. The path that opened — engineered DAF/CD55 SCR1-4 in *A. oryzae* — is genuinely first-in-class, even with three remaining unknowns.

**The deeper meta-story:** this is what the discovery-engine methodology produces when given AI-assisted research velocity. Six hours from "platform gap" to "actionable engineering plan" would have been months in a human-only workflow — literature triage + computational protease analysis + multi-vendor cross-checked synthesis + falsification-card discipline applied at every step. None of the individual moves was magic; the speed of compounding was.

**Three places we genuinely need help — these are the unknowns that will determine whether the engineering path is real or only computationally elegant.** If you work in any of these areas, get in touch — the questions are concrete enough that a substantive conversation can happen quickly.

1. **Disulfide folding / protein expression** — wet-lab *A. oryzae* expression of the truncated DAF SCR1-4 construct (aa 35–285). Does it fold correctly with all 12 disulfide bonds (3 per SCR domain × 4 SCRs)? Does it secrete? Does it survive solid-state koji fermentation in practice (vs. the in silico prediction)? **Who can help:** *A. oryzae* engineering labs with protease-deletion host access (NSlD-ΔP10 ideal, RIB40 acceptable for first-pass), filamentous-fungus protein expression CROs. The Maruyama lab at Tokyo University is the strain-source contact (their adalimumab-in-*A. oryzae* paper is the foundational reference for this whole architecture).
2. **Functional complement-regulatory activity** — does the truncated SCR1-4 fragment, expressed soluble (no GPI anchor), retain C3b/C4b binding and decay-accelerating function? Native DAF uses all four SCR domains plus the membrane GPI anchor for proper geometry. A soluble truncated form changes the geometry. **Who can help:** complement biologists with C3b deposition / C5a generation assays, anyone with experience on soluble-DAF or sCR1 / Factor H truncated-construct activity work. Even a literature deep-dive of published soluble-DAF activity profiles would be valuable; we're not aware of an aa 35–285 boundary specifically being tested.
3. **Mucosal-surface delivery geometry** — even if the protein is functional and shio-koji-stable, does luminal-side DAF SCR1-4 actually engage the submucosal-macrophage CP0 priming step? The macrophages doing the priming are submucosal; whether luminal DAF can reach them, or only acts on bacterial complement-priming at the mucus interface, is unresolved. **Who can help:** mucosal immunologists, gut-luminal complement-activation researchers, anyone who's quantified epithelial transit of soluble proteins in this size range.

Each unknown is real. Honest framing: not "CP0 closed," more like **"CP0 has a real candidate in active engineering investigation, with three specific gating questions where outside expertise would be valuable."** That's the recruiting hook — the unknowns are the invitation.

**External-comms angle.** Two natural formats:

- **LinkedIn post (~150-300 words):** Lead with the headline. Show the 6-hour timeline. Name the methodology (chokepoint mapping + AI-assisted research velocity + falsification card discipline). End with "three known unknowns before this closes — wet lab is the gating step." Close with a link to the comp-012 page (`https://brianpabent.github.io/open-enzyme/daf-cd55-scr14-truncated-computational/`). Tone: direct, no over-claim, "here's the working state, not a victory lap."
- **Blog post / longer technical piece (~800-1500 words):** Same arc but with the deeper methodology story. Highlight the multi-vendor sweep architecture (Gemini Pass 2 + Claude Pass 3 + DeepSeek peer-review for synthesis). Show the chain of computational experiments (comp-006 → sweep finding → comp-012). Cite the in silico verdicts with the "Mechanistic Extrapolation" evidence-tier honesty. Open-source angle: every step is committed, anyone can clone the repo and re-run the analyses.

**Reference for either format:** the synthesis log [`logs/v4-synthesis-2026-05-05-487fad3.md`](../logs/v4-synthesis-2026-05-05-487fad3.md) shows the exact moment the daemon surfaced the truncation hypothesis as a wet-lab proposal; the comp-012 page shows the in silico validation that landed within the same session. Concrete, citable, reproducible.

---

## How to add to this log

Append new entries at the TOP (most-recent-first chronological). Each entry uses the structure above:
- Date in ISO format (`YYYY-MM-DD`)
- Headline in `## YYYY-MM-DD — <one-line>` form
- Sections: What happened / Why it matters / External-comms angle
- Cross-link to canonical wiki sources

When an entry is actually used externally (a post lands, a talk gets given), append a "Used in:" line at the bottom of the entry with the URL/venue + date. Keep the entry — the log is also a record of what's been said publicly about the project.
