---
prompt_id: 01-uricase-mechanism-factual
task_type: factual
provenance: synthetic-but-realistic (mirrors daemon Pass 1 factual-lookup style)
target_output_tokens: 600
notes: |
  Tests whether vendors converge on standard biochemistry facts that are
  widely documented in the public literature. Low expected disagreement.
  Baseline for the other prompts.
---

# Prompt

You are answering a focused biochemistry question for a working scientific wiki on engineered microbial therapeutics. Audience: PhD-level scientists. No marketing language. State evidence levels (in vitro / animal / clinical / mechanistic extrapolation) when relevant.

Question: For *Aspergillus flavus* uricase (urate oxidase, EC 1.7.3.3), give the following with primary-source citation where possible:

1. Native quaternary structure (subunit count and approximate molecular weight)
2. Whether the enzyme requires any metal or organic cofactor
3. The full balanced reaction it catalyzes (including byproducts)
4. The peroxisomal targeting signal sequence on the native protein and its position
5. One published Km value for uric acid (with units and source)

Be concise. If you don't know a fact at the precision asked, say "uncertain" or "not from primary recall" — do not confabulate.
