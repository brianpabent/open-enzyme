---
title: Grounding the AI Scientist hype
date: 2026-05-08
status: draft
tags: [ai-augmented-research, methodology, citation-laundering, hypothesis-generation]
---

# Grounding the AI Scientist hype

An article crossed my desk this morning with the headline *"The AI scientist: now academic papers can be fully automated, what does this mean for the future of research?"* It surveys three systems. The headline answer is roughly "a lot." The longer answer, once you actually look at what each system does and what it doesn't, is more interesting and more useful.

I run a small open-source biology project — engineered food-grade microbes producing therapeutic enzymes, currently focused on gout. I've been building an AI-augmented research methodology around it for the past few months. So I read the article with a specific question in my head: where do these tools sit relative to the workflow we've actually been running, and what's still load-bearing on a human?

Here's what I found.

## The three systems

**[Sakana AI's AI Scientist / AI Scientist-v2](https://sakana.ai/ai-scientist-nature/).** End-to-end. Given a research direction, it generates ideas, writes and runs code, analyses results, and drafts a LaTeX manuscript. The headline result is that one of three submitted papers cleared peer review at an [ICLR 2025 workshop](https://arxiv.org/abs/2504.08066). The caveats matter: the workshop was *I Can't Believe It's Not Better* (ICBINB), explicitly a negative-results venue with a ~70% acceptance rate, and the authors withdrew the paper before publication. An [independent evaluation on arxiv](https://arxiv.org/abs/2502.14297) catalogues additional methodological concerns. ~$15 per paper. Real work. Real milestone. Lower bar than the headline implies.

**[Analemma's Fully Automated Research System (FARS)](https://analemma.ai/fars/).** Also end-to-end. A multi-agent system (Ideation, Planning, Experiment, Writing) that ran a [live public deployment](https://analemma.ai/blog/introducing-fars/) in early March and produced 100 short ML papers in 228 hours, [burning 11.4B tokens](https://eu.36kr.com/en/p/3696795271966336). The pitch is volume — one paper every 2.5 hours at a few dollars each. Peer review wasn't part of the deployment. This is a generation-rate play, not a quality play.

**[Google Cloud's PaperOrchestra](https://www.marktechpost.com/2026/04/08/google-ai-research-introduces-paperorchestra-a-multi-agent-framework-for-automated-ai-research-paper-writing/).** Explicitly *not* end-to-end. You give it your raw experimental logs and rough notes; it gives you back a submission-ready LaTeX manuscript with figures and citations. Five agents (Outline, Plotting, Literature Review, Section Writing, Content Refinement). The Literature Review agent uses the Semantic Scholar API to verify cited papers actually exist before including them. ~40 minutes per paper. The benchmarks ([PaperWritingBench, 200 reverse-engineered CVPR/ICLR papers](https://yiwen-song.github.io/paper_orchestra/)) say it beats baselines 50–68% on lit-review quality and 14–38% on overall manuscript quality.

The three systems sit in three different positions on the value chain. AI Scientist and FARS automate the whole loop. PaperOrchestra automates only the writing and assumes a human did the science. The honest assessment of where each is useful follows directly from that distinction.

## The honest gap

Here's the thing the article doesn't quite name: in research that has any wet-lab consequence, the bottleneck isn't writing papers. The bottleneck is forming hypotheses worth testing — the kind that survive contact with primary sources and that point at experiments cheap enough to run.

I've been doing this dance with my AI collaborator for months now. The pattern is consistent: the AI is excellent at *enumerating* possibilities. Connections, mechanisms, candidate molecules, contradictions in the literature, branches of investigation. What it doesn't do — at least not yet, at least not in the systems above — is *commit to a bet*. Pick the one most-interesting thread. Name the riskiest assumption underlying the current direction. Look at a wiki page about NLRP3 inhibition and a separate wiki page about gut barrier integrity and notice they rhyme in a way nobody has stated out loud. That last one in particular is what taste looks like in research, and it's currently mine to provide. I steer; the AI surfaces.

I think the state of the art is closer to closing this gap than people realize, and I think two of the three systems above are evidence we're not there yet. Generating 100 papers in a week is not closing the gap. Clearing a 70%-accept negative-results workshop is not closing the gap. The closer-to-honest position is PaperOrchestra's, which doesn't claim to close it at all — it just compresses the writing once a human has done the science.

## What we've been doing instead

The methodology my project runs on isn't a single tool. It's a multi-pass discipline.

**Multi-vendor adversarial review.** Each substantive change to our research wiki triggers a four-pass sweep: a Claude propagation pass (find affected pages, fold in the new finding), a Gemini synthesis pass (read the full corpus, find connections nobody has stated), a Claude review pass (critique the synthesis, prepend findings to a queue I review manually), and a DeepSeek peer-review pass (a fourth model from a fourth vendor, looking for things the first three missed). The vendors are deliberately heterogeneous because the failure mode we're guarding against is epistemic homogenization — three Anthropic models will agree on the same wrong answer more often than three models from three different training pipelines.

**Pre-commit grep-verify gate.** Every load-bearing quantitative claim — every IC50, every dose, every percentage, every cohort size, every disulfide-bond count — must be grep-verified against its primary source *before* the commit lands. Not "verify if the sweep flags it." Verify before the content ships into the corpus. This rule was codified two days ago, after a Sonnet subagent hallucinated "12 disulfide bonds" in four places of fluent prose on a wiki page about a complement-system protein. The pipeline that produced the page doesn't even count disulfides. The agent just wrote the number, confidently, in scientific tone, and the number propagated overnight into a downstream hypothesis page that used it to drive a chaperone-load calculation. The next day's sweep caught the inconsistency by cross-referencing two pages that disagreed on the count. UniProt's canonical entry settled the question (the actual count is 8, not 12). The number is grep-verifiable. The verification is no more than a primary-source query. The discipline is to do it before the commit, not after the propagation.

**Multi-stage verification, including verification-of-verification.** Yesterday's incident was structurally different and arguably more interesting. A multilingual lit scan on the *Eurycoma longifolia* (tongkat ali) corpus surfaced a "37% testosterone increase" figure that recurs in lockstep across three "independent" RCTs from the supplement-marketing tier. A first verification subagent with PubMed access found that the figure is real — it's from a single 2013 paper, and it measures *salivary* testosterone in a mixed-sex moderately-stressed cohort. The supplement industry has been laundering it as if it were serum free-T elevation in hypogonadal men for thirteen years. A second verification pass on the parent page surfaced a separate misattributed citation (a "Shin 2024" paper that doesn't exist; the actual paper fitting the description is by different authors with a different PMID). A third pass — a computational re-run of an experiment that depended on the trigger claim — surfaced a third laundered claim (a mechanism attribution that the cited primary papers don't actually establish, sourced again from supplement-industry summary tier). Three layers of citation laundering, on one wiki page, in one workday, each caught by a different stage of the discipline. None would have surfaced under a single-pass workflow. The full incident is documented in [`operations/notable-moments.md`](../operations/notable-moments.md).

**Evidence tiering.** Every claim in the corpus is tagged Clinical Trial, Animal Model, In Vitro, or Mechanistic Extrapolation. Reviewers can tell at a glance whether they're reading a piece of the wiki that derives from a randomized human trial or from a chain of reasoning across foundational biology.

**Multilingual by default.** The AI substrate reads Chinese, Japanese, Korean, German, Russian, French, Spanish, Arabic, Hindi, Portuguese — natively, no translation step needed. Treating language as a barrier in 2026 is path-dependent narrowing. A compound with thin Western evidence but substantial Chinese clinical evidence has stronger empirical backing than the Western-only view shows. When non-English sources are ingested, two independent models from different vendors translate, and disagreements are surfaced inline rather than collapsed silently.

None of these moves is exotic. None requires new research. Each addresses a specific failure mode that I've watched a fluent AI produce in plausible-sounding prose and that would have shipped, undetected, into a research corpus that PhD-level readers are supposed to be able to trust.

## The hero is the discipline, not the AI

What the three systems in the article have in common is impressive infrastructure. What they're missing — to varying degrees — is the layered verification discipline that catches the kind of error AI fluent prose produces *most* easily, which is the confident-sounding load-bearing number with no primary source behind it. PaperOrchestra's citation-existence check via Semantic Scholar is a step in this direction. It's a weaker version of what we need: theirs verifies that a cited paper exists. Ours verifies that a cited *number* matches the primary source. The first is necessary; the second is necessary and not yet standard.

A reasonable person can read all of the above and conclude different things. You might think automated paper generation is closer than I'm giving it credit for, and that the discipline I'm describing will be folded into the next generation of these systems within a year. You might think the opposite — that the gap I'm naming is the gap, and the systems above are mostly automating the parts of research that don't need automating. I have my own read, but the point of writing this isn't to land mine on you. It's to give you the data to land on yours.

---

*Written 2026-05-08. The tongkat ali three-layer citation-laundering incident referenced above is documented in full at [`operations/notable-moments.md`](../operations/notable-moments.md). The DAF disulfide-count incident from 2026-05-06 is in the same file. Both are worked examples of the verification discipline catching specific classes of error, with cost and time-to-detection numbers attached.*
