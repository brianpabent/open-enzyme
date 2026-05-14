---
prompt_id: 05-rasburicase-ada-mechanism
task_type: mechanism-inference
provenance: synthetic-but-realistic (mechanism-inference around drug-induced ADA)
target_output_tokens: 700
notes: |
  Tests mechanism-inference in immunology. The question has multiple
  reasonable mechanisms (epitope exposure, PEG immunogenicity in pegylated
  variants, T-cell-dependent vs T-cell-independent responses, glycoprofile
  differences). Vendor priors likely to differ on which to foreground.
---

# Prompt

You are answering an immunogenicity-mechanism question for a working scientific wiki on engineered enzyme therapeutics. Audience: PhD-level scientists.

Context: Rasburicase (recombinant *A. flavus* uricase produced in *S. cerevisiae*) elicits anti-drug antibodies (ADAs) in approximately 60% of patients receiving repeated doses. Pegloticase (a PEGylated, mammalian-cell-produced uricase tetramer) elicits clinically significant ADAs in approximately 40% of patients in the phase-3 program, with substantial loss of efficacy in ADA-positive responders. Both are foreign (non-human) proteins, both contain the same uricase catalytic core, both are administered IV.

Question: Propose the dominant mechanism(s) by which these therapeutic uricases drive ADA formation in human patients. Specifically:

1. Identify the three most likely structural / pharmacological drivers of ADA against rasburicase
2. Identify how each driver compares for pegloticase (does PEGylation help, hurt, or change the dominant epitope class?)
3. Explain whether ADAs against rasburicase and pegloticase are expected to cross-neutralize (yes/no/partial, with reasoning)
4. Predict whether an oral uricase delivered in a fermented food matrix (no IV exposure, gut-lumen-only action, no systemic uptake) would face the same ADA risk, and the dominant reason for your prediction
5. Flag any mechanism step in your reasoning where the evidence base is thin enough that a careful reviewer might dispute it

State evidence levels and primary sources where you can.
