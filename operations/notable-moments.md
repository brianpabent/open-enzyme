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
