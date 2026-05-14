---
prompt_id: 04-koji-uricase-hypothesis-gen
task_type: hypothesis-generation
provenance: synthetic-but-realistic (matches daemon Pass 2 "experiment" emit type)
target_output_tokens: 1000
notes: |
  Open-ended hypothesis-generation. Tests whether vendors propose
  meaningfully different follow-up experiments given identical context.
  Expected: high divergence — this is exactly the task where vendor
  priors most differ.
---

# Prompt

You are advising on experimental design for a working scientific wiki on engineered food-grade microbial therapeutics. Audience: PhD-level scientists. No marketing language. State assumptions explicitly.

Context: A research project is engineering *Aspergillus oryzae* (koji) to express the *A. flavus* uricase gene heterologously, with secretion to the medium for downstream concentration into an oral dietary supplement intended to degrade luminal uric acid in the GI tract. A first-pass cassette is in design: native A. flavus uricase coding sequence, *A. oryzae*-codon-optimized, under the constitutive amyB promoter, with an N-terminal α-amylase secretion signal peptide.

Question: Propose three follow-up computational or low-cost wet-lab experiments that would de-risk this cassette before committing to the full strain-engineering + scale-up cycle. For each experiment:

1. Name the experiment precisely and the question it answers
2. Estimate cost (in silico = ~$0, low wet-lab = <$500, mid wet-lab = $500-5000)
3. Estimate timeline (days, weeks)
4. State the decision the experiment would inform (kill the design, modify a specific parameter, proceed)
5. Identify the single biggest risk factor for each experiment that could make its output uninterpretable

Order the three experiments by expected information-per-dollar. Briefly justify the ordering.

Do not propose experiments that require BSL-2+, animal models, or human subjects — this is a Phase-0 design-stage exercise.
