---
prompt_id: 04-koji-uricase-hypothesis-gen
prompt_sha256_12: 9dc91d95f2f9
vendor: deepseek
replicate: 3
model_requested: deepseek/deepseek-v4-pro
model_served: deepseek/deepseek-v4-pro
model_served_raw: deepseek/deepseek-v4-pro-20260423
call_timestamp_utc: 2026-05-14T17:39:17.085756Z
latency_seconds: 131.62
input_tokens: 328
output_tokens: 4084
cost_usd: 0.0037
finish_reason: stop
response_sha256_12: 41717a2a72f2
status: ok
---

## Assumptions
- The *A. oryzae* codon optimisation table is appropriate for the host strain and growth conditions (e.g., submerged culture on defined medium).  
- The α‑amylase secretion signal (AmyB SP) from *A. oryzae* is functional in closely related aspergilli and can direct secretion of a heterologous passenger.  
- Uricase from *A. flavus* is a soluble, active enzyme that does not require unusual post‑translational modifications present only in the native host.  
- The final product will be a lyophilised concentrate of culture supernatant; enzyme stability in the GI tract is a primary efficacy determinant.  
- “Phase‑0 design‑stage” means we have not yet built the *A. oryzae* expression vector; all experiments must be computational or use surrogate hosts / cell‑free systems, and must stay at BSL‑1.

---

## Experiment 1 (highest information‑per‑dollar)
### In silico sequence‑ and structure‑based cassette audit
**Question answered:** Does the codon‑optimised coding sequence harbour cryptic features (mRNA secondary structure blocking translation initiation, internal ribosome entry sites, rare codons, hidden splice sites, or fortuitous promoter/terminator elements) that would impair expression in *A. oryzae*, and is the AmyB signal peptide predicted to be cleaved efficiently?

**Estimated cost:** ~$0 (computational)  
**Estimated timeline:** 1–2 days  
**Decision informed:**  
- If SignalP 6.0 (eukaryotic mode) gives a cleavage probability <0.5, or if the mRNA folding free energy of the region –30 to +30 nt around the start codon (ΔG) is weaker than –10 kcal/mol (i.e., too stable), **modify** the signal peptide or re‑optimise the first 10–15 codons.  
- If cryptic *Saccharomyces*‑like splice sites (branch point + 3′ splice site) or fungal‑like polyadenylation signals are found, **revise** the codon optimisation.  
- If all metrics are within accepted thresholds, **proceed** to wet‑lab validation.

**Biggest risk factor for uninterpretable output:**  
Prediction algorithms are trained primarily on mammalian/yeast data; the secretory translocon and mRNA‑unwinding machinery of *A. oryzae* may deviate enough to generate false positives or false negatives. A “clean” in silico profile does not guarantee in vivo performance.

---

## Experiment 2 (second‑highest information‑per‑dollar)
### Cell‑free coupled transcription‑translation with microsomal membranes
**Question answered:** Can the full pre‑pro‑uricase fusion (AmyB SP + *A. flavus* uricase, codon‑optimised for *A. oryzae*) be translocated into endoplasmic reticulum‑derived vesicles, have its signal peptide cleaved, and yield active uricase?

**Estimated cost:** <$500 (low wet‑lab)  
- Gene synthesis of a linear template: T7 promoter – AmyB SP – uricase (A. oryzae codon usage) – T7 terminator ≈ $200  
- Rabbit reticulocyte lysate with canine pancreatic microsomes, plus uricase activity assay reagents ≈ $300  
**Estimated timeline:** 2–3 weeks (gene synthesis + 1 day for the assay)  
**Decision informed:**  
- If translocated, cleaved protein shows uricase activity (decrease in A₂₉₀), **proceed** with confidence that the signal peptide functions and the mature enzyme is active.  
- If no activity or no cleavage, **modify** the signal peptide (e.g., try a different *Aspergillus* secretion signal, or adjust the linker between SP and uricase) and re‑test; a complete failure would **kill** the cassette design.

**Biggest risk factor for uninterpretable output:**  
Canine microsomes lack fungal‑specific chaperones (e.g., BiP orthologues, protein disulfide isomerase isoforms) and may not support efficient folding of a fungal oxidase. A negative result could be a false negative due to incompatible translocation machinery rather than an intrinsic flaw in the cassette.

---

## Experiment 3 (third‑highest information‑per‑dollar)
### Heterologous expression in *E. coli* and simulated GI‑tract stability assay
**Question answered:** Is the *A. flavus* uricase polypeptide (without signal peptide) intrinsically active and sufficiently resistant to the pH, proteases, and bile salts encountered during oral delivery to the intestinal lumen?

**Estimated cost:** $500–5,000 (mid wet‑lab)  
- Gene synthesis of *E. coli*‑codon‑optimised uricase (no SP, with N‑terminal His₆ tag) + cloning into pET vector ≈ $300  
- Small‑scale expression, Ni‑NTA purification, and activity/stability assays in simulated gastric fluid (pH 2.0 + pepsin, 2 h) and simulated intestinal fluid (pH 6.8 + trypsin/chymotrypsin + bile salts, 3 h) ≈ $1,500–4,000  
**Estimated timeline:** 4–6 weeks  
**Decision informed:**  
- If ≥50% activity remains after sequential gastric + intestinal challenge, **proceed**; the enzyme is likely robust enough for luminal uricolysis.  
- If activity is lost rapidly (e.g., <10% after gastric phase), **kill** the current enzyme choice or **modify** by engineering acid‑resistant variants (e.g., surface charge redesign) before committing to *A. oryzae* strain engineering.

**Biggest risk factor for uninterpretable output:**  
Uricase produced in *E. coli* cytoplasm may lack any post‑translational modifications (e.g., acetylation, glycosylation) that occur in *A. oryzae* and could influence conformational stability or protease resistance. In vitro GI simulations also omit the protective effect of food matrices and mucus, potentially overestimating inactivation.

---

## Ordering justification (information‑per‑dollar)
1. **In silico audit** – zero cost, days of effort; eliminates cassettes with obvious sequence‑level defects before any money is spent.  
2. **Cell‑free translocation/activity** – low cost (<$500) and only 2–3 weeks; simultaneously tests the two most uncertain elements (signal peptide cleavage and uricase activity) in a single experiment, yielding high‑density information.  
3. **E. coli expression + GI stability** – higher cost and longer timeline, but addresses the ultimate functional requirement (GI survival) that determines whether the entire product concept is viable. It is placed last because the first two experiments can kill the cassette before this larger investment is made.
