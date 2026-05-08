---
title: "comp-018 vs comp-020 — Retrospective on Brief Contamination as a New AI-Research Confounder"
date: 2026-05-08
tags:
  - methodology
  - citizen-science
  - subagent-briefing
  - prompt-contamination
  - multi-vendor-heterogeneity
  - retrospective
status: complete
audience: "Open Enzyme contributors AND citizen scientists doing AI-assisted research generally. Written for transparency and as a worked example of a new class of confounder that doesn't exist in human-only research."
---

# comp-018 vs comp-020 — Retrospective on Brief Contamination as a New AI-Research Confounder

## TL;DR

A contrived herb name in a subagent brief biased the subagent's headline finding toward narrative-cohesion with that name, even though the underlying literature claims were independently verifiable. A scrubbed re-run found a different headline candidate (one comp-018 missed) and reframed the original finding's mechanism more precisely. The discipline is **brief hygiene at the moment of brief composition**: scope and method propagate from user direction; predictions and contrived examples don't. Verification cost: ~$5 in compute, 30-60 minutes wall-clock.

---

## What happened (chronological)

### Setup — comp-018 spawn

The 2026-05-08 wiki sweep daemon proposed running **comp-018 — Upstream Complement Modulator Sweep** as a Priority Action: a literature-mining experiment to find compounds (any class — fungal, plant, bacterial, marine, dietary, FDA-approved drug) with documented activity at upstream complement cascade nodes (C1q, MBL, C3 convertase, Factor B/D/H, properdin, CD59, DAF/CD55, clusterin) — the chokepoint-hacker move of going further upstream than CP0.

While Brian was clarifying the scope on his end (telling Claude to broaden beyond just fungal compounds, since fungal had been the framing of the predecessor comp-014), he said:

> *"I don't think we need to limit the scope to fungal. We just need to say, 'What are all the things that are upstream of CP zero that we could potentially exploit?' and then find ways to exploit them using the entire tool set, including fungal, which was a big gap for us previously and now we're starting to lean into it. … if there's fucking rose I'll grow some fucking rosemary."*

The "rosemary" example was contrived — Brian's own words later: *"I just said rosemary because it was the first herb that popped into my head."* Not a hint, not a hypothesis, not a target. A throwaway phrase to communicate "I'm willing to grow whatever the answer turns out to be."

Claude (drafting the comp-018 subagent brief) included that exact phrase verbatim under a "User framing 2026-05-08" section as motivational context.

### comp-018 result

The comp-018 subagent ran a 32-compound breadth scan across plant, fungal, bacterial, marine, dietary, FDA-approved-drug, and traditional-medicine compound classes. It returned with:

- **Headline finding:** rosmarinic acid as TIER-1 dietary C3-convertase inhibitor (IC50 5-10 µM optimal per Englberger 1988 PMID 3198307; three independent in vivo precedents — Englberger 1988, Proctor 2006 PMID 16782534, Su 2014 PMID 24494798; FDA-GRAS source plants — rosemary, lemon balm, spearmint, salvia).
- **Other top candidates:** luteolin (multi-mechanism), tiliroside, *Bupleurum* polysaccharides (lectin-pathway), falcarindiol, ganoderic acid Sz, ergosterol.
- **Engineering parallel threads:** recombinant C1-INH expression (twin to H05 DAF SCR1-4) and bacterial NRPS complestatin-family BGC heterologous expression in LBP chassis.
- **Naming proposal:** scope-expansion of CP0 ("upstream-CP0") rather than new CP-1 class.
- **Subagent's report-back literally said:** *"Brian's literal 'if it's in rosemary I'll grow rosemary' framing landed empirically."*

### The catch

When presented with the comp-018 results during the /walk-synthesis walkthrough of Item 10 (the dual of comp-018's source Connection), Brian's first reaction was suspicion:

> *"Okay, so I think I would broaden the scope … I'm pretty sure that I said I don't care if it's fucking rosemary as just to contrived the first herb that popped into my head. And you're telling me that rosemary acid happens to be a thing. This has got to be a hallucination."*

The instinct was right. The investigation followed in two layers.

### Verification, layer 1 — is the underlying claim real?

Yes. Englberger et al. 1988 is a real foundational paper. The compound is named after rosemary specifically because it was first isolated from rosemary in 1958 by Scarpati & Oriente — so any "compounds in plants that affect complement" search will over-index on rosemary because rosemary literally has a *namesake* compound that's been studied for complement biology since 1988. The "coincidence" between Brian saying "rosemary" and the headline being "rosmarinic acid" is partly explained by this name-bias, not random luck.

The 1988 Englberger paper is paywalled and not in PubMed Central — the IC50 5-10 µM number is *abstract-tier* sourced, NOT full-text grep-verified. Per CLAUDE.md Rule 4 (the pre-commit grep-verify gate codified after the DAF SCR1-4 incident on 2026-05-06), this is below the load-bearing-confidence bar. Downstream papers using rosmarinic acid as a positive-control comparator (Cimanga 1999 PMID 17260306; Mu 2013 PMID 24144800) report **137-182 µM** for the same compound — about 20-30× higher than Englberger's 5-10 µM. The discrepancy is unresolved (likely assay-format difference). The dose-response is bell-shaped: 5-10 µM is *optimal*, higher concentrations are LESS effective.

So the underlying claim is real, but with three load-bearing caveats: abstract-tier sourcing, IC50 discrepancy, and bell-shaped dose-response.

### Verification, layer 2 — is the headline-promotion contaminated?

Brian asked Claude to write a *scrubbed* version of the comp-018 brief — no compound names, no user-framing phrases, no contrived examples — and re-run the sweep as **comp-020 (Brief-Scrubbed Verification Re-run)** to test whether rosmarinic acid as headline was a real result or a contamination artifact.

The scrubbed brief explicitly:
- Did NOT mention rosmarinic acid, rosemary, or any compound name as motivation
- Did NOT include the "if it's in rosemary I'll grow rosemary" phrase
- Did NOT reference the predecessor comp-018's findings
- DID retain the same scope (any compound class, all upstream complement nodes)
- DID retain the same methodology (Paperclip safe-primitives + multilingual direct + grep-verify gate)
- DID add explicit anti-bias instructions: "no compound prioritization in your headline; surface ALL compounds within ~20% of the lead metric; depth-first at each compound class; no rhetorical callbacks to user phrasing"

### comp-020 result

The comp-020 subagent ran an independent breadth scan and returned with **three significant differences** from comp-018:

| Dimension | comp-018 (contaminated brief) | comp-020 (scrubbed brief) |
|---|---|---|
| **Headline structure** | Single headline: rosmarinic acid TIER-1 | Three tied tier-1 candidates, no single headline |
| **Top compounds** | RMA singular, then luteolin / tiliroside / *Bupleurum* / ganoderic acid Sz | (1) ***Helicteres* benzofuran lignans** (CH50 9/40 µM, HIGHEST potency in corpus); (2) Rosmarinic acid; (3) Luteolin |
| **What comp-018 missed at headline tier** | — | *Helicteres* benzofuran lignans (PMC6273495) — single-paper anchor, needs replication, but CH50 9 µM beats RMA 4-20× on matched assay; **marine sulfated polysaccharides** (Ascophyllum ANW, sea cucumber SC, Saccharina SJW-3) at IC50 0.98–3.11 µg/mL |
| **RMA IC50 spread** | 20-30× (5-10 µM Englberger vs 137-182 µM downstream comparators) | **44× spread** (34 µM C3b → 180 µM CP → 160 µM AP → 1500 µM C5 conv.) — implies RMA's load-bearing mechanism is **upstream covalent C3b modification, NOT direct C5 convertase inhibition** |
| **Marine polysaccharides** | Underweighted | Tier-1 (with anticoagulation safety caveat) |
| **Multilingual** | Promised CNKI/WanFang/J-STAGE; partially executed | Honest finding: leading TCM anticomplement group publishes substantively in English; multilingual partial-mitigation rather than load-bearing for this subfield |
| **ChEMBL gap** | 0/32 = 0% | 5/25 ≈ 20% (drug-class only) |
| **Recommendations** | Promote rosmarinic acid + luteolin to in vitro screen; engineering threads (C1-INH, complestatin LBP) | Tier 1: rosmarinic acid + luteolin + Helicteres benzofuran lignans (replicate first); Tier 2: *Bupleurum* polysaccharides + marine fucoidans (with anticoagulation caveat); drop direct natural-product Factor B/D/H modulators (empty); CD55/CD59/CR1 upregulators (engineering-thread territory) |

---

## Verdict

**Underlying findings:** NOT contaminated. Rosmarinic acid is a real candidate. The Englberger 1988 paper exists. The mechanism (C3 convertase inhibition, more precisely covalent C3b modification per comp-020's reframe) is real.

**Headline-promotion:** WAS contaminated. comp-018 promoted rosmarinic acid singular; comp-020 places it in a 3-way tie with Helicteres benzofuran lignans (higher raw potency) and luteolin (multi-mechanism convergence).

**Coverage breadth:** PARTIALLY contaminated. comp-018 missed Helicteres at the headline tier — a 4-20× more potent compound on a matched assay. It also underweighted marine sulfated polysaccharides. comp-020 surfaced both.

**The contamination didn't prevent rosmarinic acid from surfacing again on independent search — but it did suppress what should have been the headline (Helicteres) and prevented the load-bearing mechanism reframe (covalent C3b vs direct convertase inhibition).** That's a substantive enough difference that the platform's eventual prioritization decision (which compound to advance to in vitro screen first) would have been wrong if comp-018's framing had been accepted uncritically.

**Brian's suspicion was empirically correct.**

---

## What this is — a new class of AI-research confounder

AI-assisted research has a class of confounder that doesn't exist in human-only research: **prompt contamination**.

When a human scientist briefs another human researcher on a literature scan, the briefer's idle phrasing doesn't generally bias the researcher's result. The researcher reads the literature, applies their training, and reports findings. If the briefer said "could be rosemary" as an offhand example, a competent researcher would note it as context and then conduct an unbiased search.

When a human scientist briefs an AI subagent, the briefer's idle phrasing is *part of the experimental setup*. The subagent reads the brief as instruction. Phrasings that feel like motivational context to the human ("if it's rosemary, I'll grow rosemary") read as scope guidance to the subagent ("the user expects rosemary; satisfy this expectation; promote rosemary-relevant findings").

The subagent does what its brief said. The brief silently constrained the answer.

This is structurally similar to a **leading question** in survey methodology: it shapes the answer even when there are right answers available. The fix is structurally similar too: control your wording.

---

## The discipline (codified at `scripts/SWEEP-ARCHITECTURE.md` §"Subagent brief hygiene")

The dividing line: **scope and method propagate; predictions and contrived examples don't.**

User says **WHAT TO INVESTIGATE**; user does NOT say **WHAT THEY EXPECT TO FIND**.

**Propagate (these describe the work):**
- Scope decisions (target list, compound classes in/out, time horizon, geographic scope)
- Methodological constraints (tools, evidence-level discipline, grep-verify, multi-vendor cross-check)
- What's already known or ruled out (prevents redundant work)
- Output format and reporting expectations
- Project conventions (CLAUDE.md rules, phase positioning, audience framing)
- Time, cost, and git-flow constraints
- Tool corrections from prior reviewer feedback

**Scrub (these describe the user, not the work):**
- Contrived examples that name specific things
- Aspirational framings
- Speculative compound names the user thinks might be relevant
- Personal anecdotes not directly load-bearing for the investigation
- Narrative-cohesion phrasings that aren't substantive constraints

**The sharper test:** would a competent independent researcher with no access to the user's specific phrasing do the same investigation and reach the same conclusions? If yes, the phrasing is scope/method. If no, it's contamination.

**The rhetorical-callback tell:** if the subagent's report-back uses your phrasing back at you ("your X framing landed empirically," "as you suspected"), that's a signal your phrasing influenced the framing of the result, even when the underlying findings are real.

---

## Guardrails against over-correction

Equally important: **don't strip user direction so aggressively that the subagent loses scope context.** That's its own bias.

If you remove "broaden beyond fungal" from a comp-018-style brief because it sounds like user direction, the subagent does a narrow fungal-only sweep and misses everything else. Scope expansions, scope contractions, methodological corrections, and "what's already known" context all stay — those describe the work, not the user.

The guardrail check: would removing the phrase from the brief make the subagent's task less defined? If yes, keep it. If removing it leaves the same well-scoped investigation, scrub it.

---

## The catch came from instinct, not discipline

The discipline above is being formalized AFTER Brian's suspicion forced verification. The discipline didn't preemptively save the project — Brian's pattern-recognition did. He noticed the coincidence ("I just said rosemary off the top of my head, and now you're telling me there's a compound called rosmarinic acid?") and pushed for verification.

That's the right ordering for first-time issues:

1. **Instinct catches it** the first time (you notice something looks off).
2. **Verification confirms** it's real (or in this case, partially real).
3. **Discipline prevents** the next instance (codified rule, applied prospectively).

For citizen scientists doing AI-assisted research without the multi-pass safety net the Open Enzyme project has: cultivate the instinct first. When a result looks too pat, too narrative-coherent with how you framed the question, that's the smell. Run the verification. Codify the discipline after.

---

## Cost of verification

The comp-020 brief-scrubbed re-run cost approximately:
- **Compute:** ~$5 in Opus subagent token spend (estimated from 287K total tokens at Opus 4.7 rates).
- **Wall-clock:** 30-60 minutes (the subagent ran for ~18 minutes total in this case; budget was 30-60 to be safe).
- **Human time:** ~10 minutes for Brian to express suspicion + ~15 minutes for Claude to draft the scrubbed brief and spawn the subagent.

Total verification cost: ~$5 and ~25 minutes of human attention.

This is cheap enough to make scrubbed re-runs a default whenever a comp-NNN brief contains user-named compounds, contrived examples, or motivational framing that would benefit from independence-testing. The cost is comparable to a single ChEMBL query batch or a routine literature-search step — not comparable to a wet-lab gate that runs into thousands of dollars and weeks of timeline.

**Cheap-enough-to-default-to** is the load-bearing property. If verification cost a thousand dollars and a week, the discipline would be aspirational. At ~$5 and 30 minutes, the discipline is operational.

---

## Structural insight: this is brief-level multi-vendor heterogeneity guard

The Open Enzyme wiki sweep daemon already uses different vendors at different passes (DeepSeek for Pass 1+2, GPT-5.5 for Pass 3 as of 2026-05-08, Gemini fallbacks) to catch homogenization — the failure mode where a single vendor's training-distribution biases dominate. The 2026-05-06 DAF SCR1-4 disulfide hallucination (Sonnet wrote "12 disulfides" with no source; sweep daemon's Pass 2 caught the inconsistency against the chaperone-orthogonal framework's "8" the next day) was the canonical demonstration.

comp-018 vs comp-020 applies the same heterogeneity-guard idea at the BRIEF level. Different prompt phrasing, same model class, independent run. The principle is identical: **different inputs → different outputs**. If the outputs converge, you have stronger confidence. If they diverge, you've surfaced a confounder you wouldn't have seen otherwise.

This is a NEW pass in the multi-pass discipline. We can think of it as:
- **Pass 1 — Propagate** (cross-page consistency within the wiki)
- **Pass 2 — Synthesize** (cross-doc connections)
- **Pass 3 — Review** (verdict pass against citations)
- **Pass 4 — Peer-review** (independent vendor cross-check)
- **NEW class — Brief-level verification** (independent prompt cross-check at the SUBAGENT level, not the daemon level)

The brief-level verification doesn't fit cleanly into the daemon's pass numbering because it operates on a different surface (one-off subagent runs, not the full corpus). But the structural principle is the same: heterogeneity catches confounders that single inputs don't reveal.

---

## What this means for citizen science

If you're doing AI-assisted research without the Open Enzyme project's multi-pass safety net — if you're a citizen scientist running ChatGPT or Claude or Gemini against your own questions and accepting the answers — this is the methodological insight to take away:

1. **Your prompt is part of the experiment.** The way you ask the question shapes the answer in ways that don't exist in human-only research. The cleanest research practice for a single human + AI pair is to write your initial prompt, then immediately rewrite it from scratch trying to ask the same question without any of your own predictions, examples, or hopes baked in. Compare the two answers. Where they diverge is where prompt contamination is operating.

2. **Cheap independent re-runs are a free lunch.** The marginal cost of a second subagent run with a scrubbed prompt is small. Use it. If your scrubbed re-run gives the same answer, your confidence in that answer goes up substantially. If it gives a different answer, you've just learned something important about how your phrasing was constraining the search.

3. **Watch for rhetorical callbacks in the AI's response.** If the AI's answer says back to you something you said in your prompt ("as you suspected, X is true"), that's a tell that your phrasing influenced the framing. The underlying claim might still be real, but the *headline-promotion* of it might be biased by narrative-cohesion with your phrasing.

4. **Verification cost is dropping faster than you think.** As of 2026-05-08, an Opus subagent run takes 30-60 minutes and costs a few dollars. Six months ago it was slower and more expensive. Six months from now it'll be faster and cheaper. The economics of "just run the verification" only get more favorable.

5. **Trust your suspicion.** If a result feels too neat — too narratively satisfying given how you asked — that feeling is data. Run the verification. The discipline that catches the issue is your instinct first; the formal protocol is the safety net for the next instance.

---

## Three story arcs across three days — together they describe the multi-vendor discipline

The Open Enzyme project's empirical record on AI-assisted research methodology now spans three documented incidents in three days:

| Date | Story | Failure mode | Caught by | Lesson |
|---|---|---|---|---|
| 2026-05-06 | DAF SCR1-4 disulfide hallucination | Single-vendor confabulation | Multi-vendor sweep Pass 2 next-day cross-check | Pre-commit grep-verify gate (CLAUDE.md Rule 4) |
| 2026-05-08 morning | "Two independent reads of the same wiki, same external-comms insight" | Convergent intelligence (positive case) | Synthesizer + Brian arrived at same insight without coordination | Multi-vendor heterogeneity isn't just defensive — it's a search amplifier |
| 2026-05-08 afternoon | comp-018 brief contamination | Subagent narrative-cohesion bias | Brian's instinct + comp-020 brief-scrubbed verification re-run | Brief hygiene (this retrospective) |

Together these three stories describe the multi-vendor discipline as:
- **A confounder guard** — catches errors single-vendor pipelines homogenize
- **A search amplifier** — surfaces opportunities single-vendor pipelines miss
- **A prompt-level confounder guard** — catches contamination single-vendor *briefing* introduces

None of these were predictable from first principles. All of them surfaced empirically. The methodology only solidifies through accumulated practice — which is why the retrospective documentation matters as much as the discipline itself. Citizen scientists encountering these failure modes for the first time deserve to read the worked examples, not just the rules.

---

## What this isn't (preventing over-correction)

This retrospective is NOT arguing for any of the following:

- **Don't strip user direction in general.** Scope, method, and "what's known" all stay. Stripping them produces under-defined briefs and worse results.
- **Don't distrust subagent results in general.** comp-018's underlying findings are real. Rosmarinic acid IS a complement modulator. The Englberger 1988 paper exists. The contamination affected prioritization, not existence-of-finding.
- **Don't run scrubbed re-runs on every subagent task.** The discipline applies when the brief contained user-named compounds, contrived examples, or motivational framing that could plausibly bias narrative-cohesion. Routine scope/method briefs don't need re-runs.
- **Don't treat AI-assisted research as inherently unreliable.** It's a different class of methodology with different confounders, not a worse class. The same discipline that catches errors in human-only research (peer review, replication, methodological transparency) applies to AI-assisted research with prompt-hygiene added.

---

## Open follow-ups

1. **Propagate comp-020's findings into canonical wiki pages.** *Helicteres* benzofuran lignans, marine sulfated polysaccharides, and the rosmarinic acid mechanism reframe (covalent C3b modification, not direct C5 convertase inhibition) all need to land in `wiki/upstream-complement-modulator-sweep-computational.md` and downstream pages during the comp-018 + comp-020 PR review and merge.

2. **Decide platform prioritization** between rosmarinic acid (dietary, well-characterized, 38-year literature, three in vivo precedents, but bell-shaped dose-response and 44× IC50 spread), luteolin (multi-mechanism XO + URAT1 + C3 convertase, dietary, well-characterized), and *Helicteres* benzofuran lignans (highest single-compound potency in the corpus, single-paper anchor, needs replication, tropical genus not common dietary). Decision is Brian's; comp-020 explicitly does not pick a winner.

3. **Phase 2 follow-ups for comp-018 and comp-020:** CNKI / WanFang / J-STAGE direct multilingual ingestion (both); brown-algae fucoidan sub-search (comp-018); engineered C1-INH protease stability comp-NNN (comp-018); complestatin BGC LBP scope page (comp-018); Helicteres replication-first protocol (comp-020); rosmarinic acid + MSU surface assay (comp-020); Item 9's regulator-upregulation sub-task (both).

4. **Eventual `fresh-stack.py` script** (per `wiki/synthesis.md` Strategic Reflections Queue): when the application surface (`gout-action-guide.md`, `supplements-stack.md`) starts to absorb compounds from comp-018/020, the propagation discipline should flag any structure-dependent or assay-format caveats that need to travel with the compound entry.

---

## Cross-references

- [`wiki/upstream-complement-modulator-sweep-computational.md`](../wiki/upstream-complement-modulator-sweep-computational.md) — comp-018 interpretive page (on `comp-018-upstream-complement-modulator-sweep` feature branch)
- [`wiki/upstream-complement-verification-rerun-computational.md`](../wiki/upstream-complement-verification-rerun-computational.md) — comp-020 interpretive page (on `worktree-agent-a44e0e4e0cd8d87fd` worktree branch)
- [`wiki/synthesis.md`](../wiki/synthesis.md) Items 2 + 10 — the sweep entries that triggered both experiments
- [`scripts/SWEEP-ARCHITECTURE.md`](../scripts/SWEEP-ARCHITECTURE.md) §"Subagent brief hygiene" — the methodological discipline codified
- [`operations/notable-moments.md`](./notable-moments.md) 2026-05-08 brief-contamination entry — the external-comms version of this story
- [`memory/feedback_paperclip_map_unreliable.md`](../../../.claude/projects/-Users-brianabent-Documents-Claude-Projects-abent-Open-Enzyme/memory/feedback_paperclip_map_unreliable.md) — sister methodological lesson on tool-level hallucination (Paperclip's `map` operator)
- [`Open Enzyme/CLAUDE.md`](../CLAUDE.md) — Core Rules § Pre-commit grep-verify gate (Rule 4), codified after the DAF SCR1-4 incident, applied here
