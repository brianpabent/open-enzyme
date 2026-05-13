## Problem Statement

AI-assisted literature synthesis is becoming a load-bearing component of how
scientific research is conducted. Research groups across biotechnology,
chemistry, physics, and the life sciences are deploying frontier language
models to read primary literature, propose connections across papers, draft
hypotheses, and maintain working knowledge graphs that span hundreds or
thousands of source documents. The pattern is no longer experimental; it is
operational infrastructure.

This shift introduces a new class of failure that does not exist in
traditional human-only research. When a single AI model is the sole
synthesizer of a long-lived knowledge corpus, the corpus accumulates that
model's blind spots and biases over time. We call this drift **epistemic
homogenization**. Epistemic homogenization is structurally distinct from
per-output hallucination: it is a property of the corpus as a whole,
compounding across hundreds of internally-coherent edits, no single output
obviously wrong, the cumulative drift invisible without an outside reference.

## Core Hypothesis

We propose that **cross-vendor heterogeneity** — models trained by different
companies, on different data corpora, with different reinforcement-learning-
from-human-feedback (RLHF) procedures and different alignment objectives —
is the right granularity for guarding against epistemic homogenization.
Multi-model heterogeneity *within* a single vendor (GPT-4o + GPT-4 + GPT-3.5;
or Sonnet + Opus) is insufficient, because all those models share the same
training-distribution prior, the same alignment procedure, and the same
characteristic failure modes.

Cross-vendor heterogeneity exploits the independence of training pipelines
across different companies. A blind spot in Anthropic's RLHF is unlikely to
appear in the same form in Google's, or DeepSeek's, or OpenAI's. The
cross-vendor pattern is a special case of ensemble methods, applied at the
vendor abstraction level for AI-assisted scientific synthesis.

## Proposed Methodology (High-Level Technical Approach)

We describe an operational deployment of cross-vendor heterogeneity — the
**Open Enzyme wiki-sweep daemon** — that maintains an ~80-page biotechnology
research wiki via a three-pass pipeline routed across three different vendor
models:

1. **Pass 1 — Propagate (Anthropic Claude Sonnet 4.6).** Reads edited files,
   identifies affected concepts, updates cross-referenced wiki pages inline
   with new findings. Includes evidence-level tagging and inline provenance.

2. **Pass 2 — Synthesize (DeepSeek V4-Pro, with Google Gemini 2.5 Pro
   fallback).** Reads the full corpus (~650k tokens) and emits cross-document
   synthesis: new connections, contradictions, open questions.

3. **Pass 3 — Review (Anthropic Claude Opus 4.7, or OpenAI GPT-5.5
   alternative configuration).** Critiques each synthesized finding with a
   fixed verdict vocabulary; has read-only tool access for primary-source
   spot-checks.

A separate **episodic peer-review pass** by an independent-vendor model is
run when major architectural changes land or when a class of synthesis
output is suspect. The seminal instance of this pass — DeepSeek V4-Pro
reviewing Claude Opus 4.7 output on 2026-04-25 — surfaced the very
homogenization risk that motivated formalizing the cross-vendor daemon,
demonstrating the principle by working.

## Expected Contribution

1. A formal definition of **epistemic homogenization** as a corpus-level
   failure mode distinct from per-output hallucination.
2. The cross-vendor heterogeneity guard as an explicit architectural pattern,
   with the argument that vendor-level (not model-level) heterogeneity is the
   right granularity.
3. An operational deployment (Open Enzyme wiki-sweep daemon) demonstrating
   the pattern at production scale, with four representative catches from
   ~3 weeks of operation:
   - Within-vendor cascade (DAF SCR1-4 disulfide-count hallucination)
   - Upstream-of-subagent contamination (comp-018 framing bias)
   - External-tool reliability test (Paperclip MCP `map` operator probe)
   - Cross-vendor catches methodological risk (DeepSeek Connection 7 self-
     flag, the seminal motivating catch)
4. A reflexive demonstration: the manuscript is drafted using the
   methodology it describes, with cross-vendor review applied at section
   boundaries and catches logged in a revisions appendix.

## Position vs. existing multi-agent AI literature

Existing multi-agent AI literature (debate, self-refine, jury-of-LLMs,
Constitutional AI, automated-research systems) operates almost exclusively
**within a single vendor**: multiple instances of the same company's model,
or multiple sizes of the same family. The cross-vendor regime — different
companies, different training corpora, different RLHF — is under-explored.
This paper develops the cross-vendor regime as an explicit architectural
pattern and presents the first operational demonstration we are aware of.
