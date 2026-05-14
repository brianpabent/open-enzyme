---
prompt_id: 04-koji-uricase-hypothesis-gen
prompt_sha256_12: 9dc91d95f2f9
vendor: openai
replicate: 2
model_requested: openai/gpt-5.5
model_served: openai/gpt-5.5
model_served_raw: openai/gpt-5.5-20260423
call_timestamp_utc: 2026-05-14T17:15:12.299957Z
latency_seconds: 140.93
input_tokens: 334
output_tokens: 5979
cost_usd: 0.0728
finish_reason: stop
response_sha256_12: 2dfdef6c2be1
status: ok
---

## Assumptions

- Work is Phase-0 only; no animal, human, or BSL-2+ work is considered.
- *A. oryzae* work, if any, is with non-engineered food-grade/BSL-1 material unless explicitly stated otherwise.
- Cost estimates exclude personnel time and assume access to standard molecular biology equipment, a plate reader or spectrophotometer, and routine bioinformatics tools.
- “amyB promoter” is treated as the promoter intended for the cassette, but I would explicitly verify its regulatory behavior, because native *A. oryzae amyB* promoters are often carbon-source regulated rather than truly constitutive.
- The desired product is secreted uricase recovered from culture medium, not delivery of viable engineered fungi.

---

## 1. In-silico secretory-expression developability audit of the `amyB–α-amylase signal peptide–A. flavus uricase` cassette

**Question answered**  
Does the current cassette have predictable liabilities for transcription, translation, secretion, maturation, glycosylation, oligomerization, or enzymatic function before any DNA is built?

This should include, at minimum:

- Codon-optimization sanity check against *A. oryzae* codon usage and tRNA availability.
- Scan for cryptic splice sites, premature polyadenylation-like motifs, repetitive elements, problematic GC/AT windows, and strong mRNA secondary structure around the start codon.
- Verification of the α-amylase signal peptide cleavage site and the exact predicted mature uricase N-terminus.
- Prediction of ER retention/mislocalization motifs.
- N- and O-glycosylation prediction on the mature uricase sequence.
- Structural mapping of predicted glycosylation sites, protease-sensitive loops, active-site residues, and tetramerization interfaces using AlphaFold/ColabFold or available homologous uricase structures.
- Check whether secretion would expose normally cytosolic/peroxisomal uricase motifs to fungal secretory processing that could impair activity.
- Promoter-context review: whether the chosen *amyB* promoter fragment is actually constitutive under the planned production medium.

**Estimated cost**  
In silico: approximately $0, assuming existing compute access.

**Estimated timeline**  
1–3 days.

**Decision informed**

- **Proceed** if no major red flags are found and the mature secreted protein is predicted to preserve active-site geometry, tetramerization, and secretion compatibility.
- **Modify specific parameters** if issues are found, e.g.:
  - choose a different secretion signal;
  - alter the signal peptide–uricase junction;
  - add/remove a short spacer or processing site;
  - revise codon optimization;
  - replace the promoter if *amyB* is not constitutive under intended culture conditions;
  - mutate non-conserved predicted N-glycosylation sites if they map near the active site or oligomer interface.
- **Kill the current design** if the mature secreted form is predicted to be intrinsically incompatible with activity, e.g. unavoidable glycosylation or cleavage at residues essential for catalysis or oligomerization.

**Single biggest risk factor for interpretability**  
Secretory-processing and glycosylation predictors are imperfect for filamentous fungi; a clean in-silico result can miss host-specific secretion or proteolysis failures.

---

## 2. Non-engineered *A. oryzae* conditioned-medium uricase spike-in stability/activity assay

**Question answered**  
Would extracellular uricase survive the proteolytic and chemical environment of an *A. oryzae* production supernatant long enough to be recovered as an active secreted product?

Conceptually, this is a non-GMO assay: grow non-engineered *A. oryzae* under media conditions approximating the intended production state, collect cell-free conditioned medium, spike in purified uricase, and monitor retention of uricolytic activity and gross protein integrity over time. Ideally the spiked enzyme would be purified *A. flavus* uricase; if unavailable, use the closest commercially available fungal or microbial uricase and interpret conservatively.

**Estimated cost**  
Low wet-lab: <$500 if using available *A. oryzae* strain, standard media, and a colorimetric or UV uric acid depletion assay. Could become mid-cost if custom purified *A. flavus* uricase is needed.

**Estimated timeline**  
Several days to ~1 week.

**Decision informed**

- **Proceed** if uricase activity is retained in conditioned medium over a time window compatible with harvest and downstream concentration.
- **Modify specific parameters** if activity decays:
  - alter production pH or medium composition;
  - shorten harvest time;
  - use a lower-protease host background;
  - screen alternative secretion signals or fusion partners;
  - add a purification capture step immediately post-harvest;
  - consider intracellular production followed by extraction rather than secretion.
- **Kill the secretion-first cassette concept** if uricase is rapidly and irreversibly degraded in relevant *A. oryzae* supernatants and the likely mitigations would defeat the intended low-cost production process.

**Single biggest risk factor for interpretability**  
The spiked enzyme may not faithfully represent the actual secreted cassette product, especially if the real product would be glycosylated, partially processed, misfolded, or present at much higher local concentration during secretion.

---

## 3. Cell-free or microscale heterologous expression/activity test of the predicted mature *A. flavus* uricase ORF

**Question answered**  
Does the mature uricase protein sequence encoded by the cassette, including the exact N-terminus expected after signal peptide cleavage, fold into an active soluble enzyme independent of the full *A. oryzae* strain-engineering cycle?

This can be framed as a small expression test of the predicted mature uricase sequence, optionally comparing:

- native mature N-terminus versus the N-terminus predicted after α-amylase signal peptide cleavage;
- one or two junction variants if the in-silico audit flags uncertainty;
- codon-optimized versus non-optimized coding sequence only if the expression system makes that comparison meaningful.

Readout should be simple: soluble protein detection plus uric acid degradation activity. The goal is not process development; it is to catch obvious “the designed mature protein is inactive or insoluble” failures before stable fungal engineering.

**Estimated cost**  
Mid wet-lab: ~$500–5000, depending on whether the DNA is already available and whether a commercial cell-free/eukaryotic expression system or a small BSL-1 microbial expression format is used.

**Estimated timeline**  
~1–3 weeks, largely driven by DNA procurement and expression setup.

**Decision informed**

- **Proceed** if the predicted mature uricase is soluble and active.
- **Modify specific parameters** if activity depends strongly on the N-terminal junction:
  - redesign the signal peptide cleavage junction;
  - add a short neutral spacer;
  - test an alternative secretion signal;
  - preserve the native mature uricase N-terminus more precisely.
- **Modify or kill the uricase ORF choice** if the protein is consistently inactive or insoluble in small expression formats, especially if this agrees with structural predictions.
- **Proceed with caution** if soluble active enzyme is obtained only in a non-secretory context, because the fungal secretory pathway may still introduce glycosylation or proteolysis liabilities.

**Single biggest risk factor for interpretability**  
Cell-free or non-*A. oryzae* microscale expression does not reproduce the fungal ER/Golgi secretion environment; therefore it can give both false reassurance and false negatives regarding folding, glycosylation, processing, and secretion-associated degradation.

---

## Ordering by expected information-per-dollar

1. **In-silico cassette/protein audit** — highest information per dollar because it is essentially free, fast, and can catch design-level errors that would otherwise propagate into every downstream experiment: wrong promoter assumption, bad signal peptide junction, cryptic processing motifs, problematic glycosylation, or structural incompatibility.

2. **Non-engineered *A. oryzae* conditioned-medium spike-in assay** — inexpensive and directly addresses a major risk specific to a secreted fungal production strategy: extracellular loss of uricase activity in the host secretome. It does not require building the engineered strain, yet it can strongly inform whether secretion into medium is a viable product-recovery route.

3. **Microscale expression/activity test of mature uricase** — more expensive and less host-representative than the first two, but it provides orthogonal wet-lab evidence that the designed mature uricase sequence can be active before committing to stable *A. oryzae* engineering. Its information-per-dollar is lower because a positive result still does not prove secretion success, while a negative result may reflect the surrogate expression system rather than the cassette itself.
