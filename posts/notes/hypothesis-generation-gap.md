---
title: Hypothesis-generation gap — working notes
date: 2026-05-08
status: working-note
tags: [methodology, hypothesis-generation, sweep-daemon, curiosity, taste]
---

# Hypothesis-generation gap

Working notes, not a post. Captures the conversation on 2026-05-08 about where AI-augmented research currently stops being load-bearing on the AI and starts being load-bearing on the human, and what we might do about it without waiting for the state of the art to catch up.

## What the gap is

The wiki sweep daemon (and all the lit-scan / comp-NNN subagents around it) is excellent at *enumeration*: connections, contradictions, candidate molecules, branches of investigation, mechanism mappings. What it doesn't do — and what Brian has been doing manually in every walkthrough — is *commit to a bet*. Specifically:

1. **Forced ranking.** Of N surfaced threads, *which one* is most worth the next experiment slot. Not "here are five interesting things." One.
2. **Counterfactual / riskiest-assumption.** What's the single load-bearing belief in the current platform thesis that's least supported by the corpus, such that its failure would most invalidate the direction.
3. **Cross-domain bridge-building.** Notice when two pages that don't cite each other rhyme in a way that hasn't been stated. The daemon's Phase B already aims at this ("weakly-connected page pairs"), but the discipline is on linking, not on the deeper move of "this NLRP3 chokepoint pattern is structurally the same as that gut-barrier pattern."
4. **Revealed-preference inference.** Look at which synthesis items Brian actioned vs. ignored over time. That's information about taste — what threads tend to get pursued vs. dropped — and it's currently unused.
5. **Evidence-anchored commitment.** Before a hypothesis is named, point at (a) the specific evidence in the corpus that supports it, (b) the specific evidence that would refute it, (c) the cheapest experiment that would discriminate. This is the take-equivalent of the grep-verify gate: forcing the model to ground a proposition in the corpus before committing.

## Why we think state of the art isn't quite there

Of the three AI-paper systems surveyed in [`grounding-the-ai-scientist-hype.md`](../grounding-the-ai-scientist-hype.md), two automate the whole loop and one automates only the writing. None of the three is trying to solve the curiosity / steering problem head-on — Sakana's AI Scientist generates *novel* ideas via tree search but doesn't appear to commit to a single bet with corpus-anchored support; FARS optimizes for throughput, which is the opposite move. PaperOrchestra explicitly leaves the science to humans. The gap is real and not yet productized.

Brian's read: we're close. We should be working on this now rather than waiting.

## The cheap version we're going to try

Add a final section to the existing Pass 2 / Pass 3 sweep prompts (the synthesis pass — the one that reads the full corpus for new ideas and connections). Two new top-level sections, each *forcing a single answer*, not a list:

- **Riskiest assumption.** Single paragraph naming the most load-bearing under-supported belief in the current platform thesis. Anchor to specific wiki page(s) and specific evidence (or absence thereof).
- **Most curious thread.** Single paragraph picking the *one* thread the model would spend the next experiment slot on. Must include: corpus evidence supporting the hunch, corpus evidence that would refute it, cheapest experiment that would discriminate. Multi-vendor signal: explicitly flag whether this is likely a convergent pick or an idiosyncratic one.

These run inside the existing sweep, no new pass, no new infrastructure. Marginal cost: roughly zero (one extra section in an existing prompt). The model already reads the full corpus for the rest of Pass 2; we're asking it to commit to a single answer at the end.

## The richer version, if the cheap one shows signal

A dedicated **Pass 4: Curiosity** that runs after Pass 3 review. Inputs:

1. Current state of the wiki corpus (already loaded).
2. Current platform thesis (top of `index.md` and `wiki/open-enzyme-vision.md`).
3. Recent `wiki/synthesis.md` actioned-vs-ignored history (revealed-preference signal — git log of `**✓ Actioned`-tagged items vs. items that aged out without being actioned).
4. Recent comp-NNN experiment results (what the corpus has *learned*, not just what it claims).

Outputs: 1–3 forced-rank hypotheses with the structure above, multi-vendor cross-checked. If Claude and DeepSeek and Gemini independently land on the same hypothesis, that's signal worth weighting. If only one model produces it, more skepticism warranted — same heterogeneity guard as the existing sweep.

Whether to build the rich version is a function of whether the cheap version actually surfaces useful output. Cheap-first.

## The take-equivalent of grep-verify

The grep-verify gate addresses confident-sounding hallucinated *numbers*. The hypothesis-generation gap is the same failure mode at a higher level: confident-sounding hallucinated *takes*. The same discipline applies. Before committing to a hypothesis, the model should be required to point at line-anchored support in the corpus — not "the literature suggests" but "wiki/page-X.md, the section on Y" — and to name the specific evidence that would refute the hypothesis. That last piece is the falsifiability anchor and it's what stops "interesting hunch" from drifting into "confident bet without grounding."

The cheap-version Pass 2 addendum should include this discipline in the prompt. The richer Pass 5 should formalize it as a structured output: each hypothesis gets a `[CORPUS-SUPPORT: file.md §section]` and `[REFUTATION-EVIDENCE: what would have to be true for this to be wrong]` tag, the same way Pass 2 already requires `[CHAIN-DEPTH]` and `[PHASE-A-MATCH]` tags.

## Open questions

- **Is forced-rank actually what we want?** Or do we want N=2-3 ranked picks with explicit "and here's why I rank them this way"? The forcing function is the commitment. A ranked list of 3 might be a reasonable middle ground.
- **What's the right reference frame for "platform thesis"?** Currently it's the top of `index.md`. As the project evolves, this drifts. Worth thinking about whether the sweep should pin to a specific commit's thesis or always read the latest.
- **How do we evaluate output quality?** The cheap version is easy to A/B (run it, see if Brian finds the surfaced "riskiest assumption" useful). The richer version is harder — a curiosity pass produces speculative outputs by design, and "did it pay off" is observable only after the experiment runs. Could be a manual annotation: when a curiosity-pass hypothesis gets promoted to a comp-NNN or to a synthesis-actioned item, log that. Track conversion rate over time.
- **Is multi-vendor convergence really the right signal?** It's the heuristic we already use elsewhere. But for *curiosity* specifically, divergence might be more interesting — if one model proposes something the others don't, that could be the most novel angle, not the least credible one. Worth thinking about more carefully.

## What's NOT in scope (yet)

- **Replacing human steering.** The point isn't to remove Brian from the loop; it's to give him better-curated single-answer options to react to, faster. He still picks.
- **A separate "AI scientist" system.** We're explicitly not trying to be Sakana / Analemma / Google. The methodology contribution we're making is the *layered verification discipline*. Hypothesis surfacing is a subordinate move inside that discipline, not a replacement for it.
- **Auto-promoting curiosity-pass hypotheses to comp-NNN experiments.** Manual promotion only. The whole point of forced-rank is to surface, not to act.

## Next concrete step

Edit `scripts/sweep-prompt-2-synthesize.md` to add the two new sections. See companion commit landing alongside this note.
