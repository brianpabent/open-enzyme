---
prompt_id: 08-cordycepin-koji-feasibility
task_type: hypothesis-generation + mechanism
provenance: synthetic-but-realistic (mirrors a Pass 2 "novel cassette" inquiry)
target_output_tokens: 1000
notes: |
  Tests whether vendors agree on the feasibility profile of a multi-step
  metabolic-engineering proposal. The kind of task where vendors most
  diverge — one may push back hard, another may go enthusiastic, a third
  may hedge.
---

# Prompt

You are advising on metabolic-engineering feasibility for a working scientific wiki on engineered food-grade microbial therapeutics. Audience: PhD-level scientists. Be direct about feasibility and risk; do not soften pushback.

Proposal: A research project wants to engineer *Aspergillus oryzae* (koji) to heterologously produce **cordycepin** (3'-deoxyadenosine, the bioactive nucleoside from *Cordyceps militaris*) alongside a primary uricase + lactoferrin cassette. The cordycepin biosynthesis pathway in *C. militaris* uses two contiguous genes, cns1 + cns2 (Xia et al. 2017, Cell Chem Biol), to convert adenosine to cordycepin via a 3'-keto-adenosine intermediate. The pathway is cytosolic, bacterial-origin-style, and does not require ER processing or glycosylation.

Question: Evaluate the feasibility of co-expressing cns1 + cns2 in an *A. oryzae* strain already carrying a uricase + lactoferrin cassette. Specifically:

1. Predict whether cns1 + cns2 will compete with the existing uricase + lactoferrin cassette for cellular resources. For each resource (ER chaperones, codon usage, precursor pools, redox cofactors, ATP), state expected competition (none / mild / severe) and the mechanism for the prediction.

2. Identify the single biggest off-target metabolic risk of expressing cns1 + cns2 in *A. oryzae*. Cordycepin is a nucleoside analog and an ADA (adenosine deaminase) substrate concern; what does that imply for koji viability, fermentation stability, and product purity?

3. Estimate the cordycepin titer achievable in *A. oryzae* if the cassette is successfully integrated. State the assumptions your estimate rests on (precursor supply, promoter strength, product efflux). Note one published cordycepin titer from another heterologous host as a sanity check if you can recall one.

4. Identify the single in-silico or low-cost wet-lab experiment that would most cleanly de-risk this proposal. State its cost, timeline, and the decision it informs.

5. Push back on the proposal itself if you think the strategic rationale is weak — i.e., is co-expressing cordycepin in the same strain as uricase + lactoferrin actually the right strategy, or would a parallel mono-cassette strain make more biological sense? Be willing to recommend NOT pursuing this.
