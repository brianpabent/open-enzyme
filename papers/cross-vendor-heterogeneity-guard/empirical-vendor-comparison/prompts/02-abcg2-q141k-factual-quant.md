---
prompt_id: 02-abcg2-q141k-factual-quant
task_type: factual-quantitative
provenance: synthetic-but-realistic (factual literature-mining test)
target_output_tokens: 600
notes: |
  Quantitative factual recall on the ABCG2 Q141K polymorphism and its
  hyperuricemia association. Tests whether vendors agree on numbers
  (allele frequency, hazard ratio, fractional contribution to urate excretion).
  Quantitative factual prompts are where the heterogeneity-guard paper
  expects vendor disagreement to most directly bite, because each vendor's
  numerical recall is independently noisy.
---

# Prompt

You are answering a focused human-genetics + transporter-biology question for a working scientific wiki. Audience: PhD-level scientists. State evidence level when relevant and cite primary sources where possible.

Question: For the ABCG2 transporter and the c.421C>A (Q141K, rs2231142) polymorphism, provide:

1. The approximate fraction of total uric acid excretion that ABCG2 mediates in healthy humans (with primary-source citation)
2. The functional consequence of Q141K on transporter activity (percent reduction relative to wild-type, with source if possible)
3. The approximate minor-allele frequency of Q141K in (a) East Asian and (b) European populations
4. One published odds ratio or hazard ratio for hyperuricemia or gout associated with the Q141K variant (heterozygous or homozygous, specify which, with source)
5. Whether the gut or the kidney is the dominant site of ABCG2-mediated uric acid excretion (and the evidence underlying that assignment)

Be precise. If you don't have a number to a useful precision, say "uncertain" rather than confabulate.
