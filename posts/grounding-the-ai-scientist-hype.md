---
title: Grounding the AI Scientist hype
date: 2026-05-08
status: draft
tags: [ai-augmented-research, methodology, citation-laundering, hypothesis-generation]
---

# Grounding the AI Scientist hype

An article crossed my desk this morning: *"[The AI scientist: now academic papers can be fully automated, what does this mean for the future of research?](https://theconversation.com/the-ai-scientist-now-academic-papers-can-be-fully-automated-what-does-this-mean-for-the-future-of-research-282161)"* It surveys three systems. The headline answer is roughly "a lot." The longer answer is more interesting.

I run [Open Enzyme](https://github.com/brianpabent/open-enzyme), an open-source biology project currently focused on gout, because I think better treatments are available if we just look. I've been iterating on an AI-first research methodology for the past couple months. I'm 2 weeks into an n of 1 experiment on myself. So I read the article with some specific questions: where do these tools sit relative to the workflow we've been running? Are other AI research projects making discoveries faster and cheaper? What can I learn from these projects?

Here's what I found.

## The three systems mentioned

**[Sakana AI's AI Scientist / AI Scientist-v2](https://sakana.ai/ai-scientist-nature/)**

**The claim**: The first comprehensive system for fully automatic scientific discovery.

End-to-end discovery workflow. Given a research direction, it generates ideas, writes and runs code, analyses results, and drafts a LaTeX manuscript. The headline result is that one of three submitted papers cleared peer review at an [ICLR 2025 workshop](https://arxiv.org/abs/2504.08066). Digging a little deeper: the workshop was *I Can't Believe It's Not Better* (ICBINB), explicitly a negative-results venue with a ~70% acceptance rate, and the authors withdrew the paper before publication. An [independent evaluation on arxiv](https://arxiv.org/abs/2502.14297) catalogues additional methodological concerns. ~$15 per paper. Real work. Real milestone. Lower bar than the headline implies.

**[Analemma's Fully Automated Research System (FARS)](https://analemma.ai/fars/)** 
**The claim**: Fully automated research.

Also end-to-end. A multi-agent system (Ideation, Planning, Experiment, Writing) that ran a [live public deployment](https://analemma.ai/blog/introducing-fars/) in early March and produced 100 short ML papers in 228 hours, [burning 11.4B tokens](https://eu.36kr.com/en/p/3696795271966336). The pitch is volume: one paper every 2.5 hours at a few dollars each. Peer review wasn't part of the deployment. They're optimizing for quantity over quality. The domain is ML, not wet lab. So 100 papers in 228 hours benchmarks the writing-and-coding loop. It says nothing about whether any of those papers contains a finding worth surviving expert review.

**[Google Cloud's PaperOrchestra](https://www.marktechpost.com/2026/04/08/google-ai-research-introduces-paperorchestra-a-multi-agent-framework-for-automated-ai-research-paper-writing/)** 
**The claim**: Submission-ready manuscripts from your raw experimental data. You do the science, it does the writing.

Explicitly *not* end-to-end. Given experimental logs and rough notes, its five agents (Outline, Plotting, Literature Review, Section Writing, Content Refinement) produce a submission-ready LaTeX manuscript with figures and citations. The Literature Review agent verifies cited papers exist via Semantic Scholar. ~40 minutes per paper. The benchmarks ([PaperWritingBench, 200 reverse-engineered CVPR/ICLR papers](https://yiwen-song.github.io/paper_orchestra/)) say it beats baselines 50–68% on lit-review quality and 14–38% on overall manuscript quality. Cool!

Three different positions on the value chain. AI Scientist and FARS automate the whole loop. PaperOrchestra automates only the writing and assumes the science is sound. Where each is useful follows from that.

## The gap

In research with wet-lab consequence, the bottleneck is forming hypotheses worth testing that hold up against primary sources and are cost-effective to run.

Months in, the pattern is consistent: AI is excellent at *enumerating* possibilities. Connections, mechanisms, candidate molecules, contradictions in the literature, branches of investigation. What it doesn't do is commit to a bet. Not yet, and not in the systems above. Pick the most-interesting thread. Name the riskiest assumption. Notice that two wiki pages, NLRP3 inhibition and gut barrier integrity, rhyme in a way no one has stated. That's what taste looks like in research. Vibe-coding has a name for this in software; vibe-science is the lab version.

The state of the art is closer to closing this gap than most people realize, but two of the three systems above are evidence we're not there yet. Neither generating 100 papers in a week nor clearing a 70%-accept negative-results workshop closes the gap. PaperOrchestra is the most honest: it doesn't claim to close the gap, just compresses the writing once a human has done the science. For Open Enzyme, it helps answer the question: We've done the research, now what?

## What we've been doing

AI prose fails in distinct ways. Our methodology layers six disciplines, each catching a failure mode the others miss.

**Vibe-Science (Interactive Layer).** Claude Code with bio plugins is where I do the work the daemon can't. Lead with curiosity, ask why and why not dozens of times, pick the threads worth pulling, name the load-bearing sub-claims, run cheap computational experiments before any wet-lab spend. The other five disciplines keep me honest AND feed back new synthesis into the loop.

**Multi-Vendor Adversarial Review.** Every substantive change to the wiki fires a three-pass daemon: Pass 1 propagates the finding into affected pages. Pass 2 reads the full corpus for unstated connections (currently ~650k tokens!). Pass 3 reviews each finding. With Claude Opus on the vibe-science layer above, DeepSeek in Pass 1 and 2, Gemini as a fallback in Pass 2 (DeepSeek can flake), and GPT-5.5 in Pass 3, that's three to four vendors across two layers. Different vendors guard against epistemic homogenization: three models from one vendor agree on the same wrong answer more often than three models from three different training pipelines.

**Shift Left.** Every load-bearing quantitative claim (IC50s, doses, cohort sizes, percentages, disulfide-bond counts) must be grep-verified against its primary source before the commit lands. This rule was codified two days ago, after a Sonnet subagent hallucinated "12 disulfide bonds" (the actual count is 8) in four places on a wiki page about a complement-system protein. The pipeline doesn't even count disulfides. The agent just wrote the number, and it propagated overnight into a downstream hypothesis page that used it to drive a chaperone-load calculation. The next day's sweep caught the inconsistency by cross-referencing two pages that disagreed on the count. The discipline is to verify before the commit, not after the propagation.

**Verification in Depth.** Yesterday's incident was different and more interesting. A multilingual lit scan on the *Eurycoma longifolia* (tongkat ali) corpus surfaced a "37% testosterone increase" figure that recurs across three "independent" RCTs from the supplement-marketing tier. First verification: the figure is real, from a single 2013 paper measuring *salivary* testosterone in a *mixed-sex moderately-stressed cohort*. The supplement industry has laundered it as serum free-T elevation in hypogonadal men for thirteen years(!). Second pass: a misattributed citation (a "Shin 2024" paper that doesn't exist; the actual paper is by different authors with a different PMID). Third pass: a computational re-run of an experiment depending on the trigger claim surfaced a third laundered claim, a mechanism attribution the cited primary papers don't establish, sourced again from supplement-industry summary tier. Three layers of citation laundering, on one wiki page, in one workday, each caught by a different stage of the discipline. None would have surfaced under a single-pass workflow.

**Evidence Tiering.** Every claim in the corpus is tagged Clinical Trial, Animal Model, In Vitro, or Mechanistic Extrapolation. Reviewers can tell at a glance whether they're reading a randomized human trial or a chain of reasoning across foundational biology.

**Multilingual by Default.** The AI substrate reads Chinese, Japanese, Korean, German, Russian, French, Spanish, Arabic, Hindi, and Portuguese natively. No translation step needed. Treating language as a barrier in 2026 is path-dependent narrowing. A compound with thin Western evidence but substantial Chinese clinical evidence has stronger empirical backing than the Western-only view shows. Two independent models from different vendors translate non-English sources, and rather than one translation 'winning', disagreements are documented inline. Nuance and precision matter in science.

None of these moves is groundbreaking, but I'm trying to make my foot not hurt. Doing good science is selfish for me.

## The hero is the discipline, not the AI

All three systems have impressive infrastructure. What they're missing, to varying degrees, is the layered verification discipline that catches AI prose's most common error: the confident-sounding load-bearing number with no primary source behind it.

PaperOrchestra is closest: its Semantic Scholar check verifies cited papers exist. Mine verifies cited *numbers* match the primary source. The first is necessary; the second is necessary and must be the standard.

This isn't the best system. There are gaps I haven't run into yet, and probably gaps Sakana, FARS, and PaperOrchestra have already solved that I'll rediscover painfully on my own. What I'd point at isn't any of the six disciplines as they stand. It's that they keep moving. The last substantial change to the daemon was two days ago. Another will likely land next week. Those three systems are optimizing for something I don't fully see, so I won't grade them. I know what I'm optimizing for: my foot.

I tried to start this project two or three years ago and couldn't. Context windows were too small, hallucinations too frequent, agents too expensive, literature locked down. All of that changed in the last year. I'm an engineer with a foot problem, not a biologist. The unlock isn't just for me and untrained vibe-scientists. Legacy science teams with deep expertise and actual budgets are going to produce remarkable and world-changing discoveries faster than they ever could. The thing I'm most excited about: scientific gatekeeping has collapsed. 

Which is why overhyping today's tools doesn't help. Honesty about what's still broken is how we get to the future we want faster.
