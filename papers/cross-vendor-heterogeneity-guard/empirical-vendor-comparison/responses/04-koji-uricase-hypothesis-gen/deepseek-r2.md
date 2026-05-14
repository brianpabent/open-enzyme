---
prompt_id: 04-koji-uricase-hypothesis-gen
prompt_sha256_12: 9dc91d95f2f9
vendor: deepseek
replicate: 2
model_requested: deepseek/deepseek-v4-pro
model_served: deepseek/deepseek-v4-pro
model_served_raw: deepseek/deepseek-v4-pro-20260423
call_timestamp_utc: 2026-05-14T17:12:00.151517Z
latency_seconds: 59.60
input_tokens: 328
output_tokens: 3997
cost_usd: 0.0036
finish_reason: stop
response_sha256_12: 32d57ce274d9
status: ok
---

**Assumptions**
- The *A. flavus* uricase coding sequence is available and has been codon-optimised for *A. oryzae* using a standard algorithm (e.g., GeneOptimizer, IDT codon optimisation).  
- The amyB promoter and α-amylase secretion signal are well‑characterised parts; a vector backbone containing them (e.g., pPTR, pNAN) is accessible.  
- Uricase activity can be measured spectrophotometrically by monitoring uric acid degradation at 292 nm.  
- All wet-lab work is performed at BSL‑1 (food‑grade *A. oryzae* is BSL‑1; *A. flavus* DNA sequences do not confer pathogenicity).  
- “Low wet-lab” assumes in‑house cloning/expression capability; “mid wet‑lab” includes gene synthesis, custom cloning, and small‑scale fungal cultivation.

---

### Experiment 1 (ordered first)
**Name:** *In silico* sequence‑ and structure‑based manufacturability audit of the expression cassette.  
**Question answered:** Does the designed coding sequence contain any computationally predictable features that would severely impair transcription, mRNA stability, translation, secretion, or enzymatic activity?  
**Cost:** ~$0 (in silico).  
**Timeline:** 2–3 days.  
**Decision informed:**  
- **Kill/modify** if any of the following are found: strong cryptic splice sites; very low codon adaptation index (<0.6); stable 5′ mRNA secondary structure (ΔG < −15 kcal/mol) obstructing ribosome access; SignalP probability of cleavage <0.5; predicted signal peptide hydrophobicity incompatible with ER translocation; or AlphaFold‑predicted misfolding of the mature uricase domain (pLDDT <70 in catalytic core).  
- **Proceed** to Experiment 2 if no high‑risk flags are raised.  
**Biggest risk factor for uninterpretability:** Predictive algorithms have false‑positive/negative rates; a clean *in silico* profile does not guarantee success, and a flagged feature may be tolerated *in vivo*, leaving the design in an ambiguous “grey zone” without wet‑lab data.

---

### Experiment 2 (ordered second)
**Name:** Cell‑free expression and activity assay of the mature uricase domain (signal peptide omitted).  
**Question answered:** Can the codon‑optimised mature uricase polypeptide fold into an enzymatically active conformation in the absence of fungal post‑translational machinery?  
**Cost:** Low wet‑lab (<$500) — PCR‑amplify the mature uricase coding sequence from the synthesised gene, add T7 promoter/RBS by overlap extension, express in an *E. coli*‑based cell‑free system (e.g., PURExpress), and assay uricase activity.  
**Timeline:** 1–2 weeks (primer design, PCR, cell‑free reaction, activity assay).  
**Decision informed:**  
- **Kill the design** if no uricase activity is detected (specific activity <5% of a positive control).  
- **Modify** (re‑optimise codons, change uricase orthologue) if activity is present but very low (<20% of control).  
- **Proceed** to Experiment 3 if robust activity confirms the core enzyme sequence is functional.  
**Biggest risk factor for uninterpretability:** Cell‑free systems lack chaperones and a redox‑optimised folding environment; a false‑negative may occur if the enzyme aggregates or requires a co‑factor not supplied (though most fungal uricases are cofactor‑independent). A negative result therefore cannot definitively rule out activity in the fungal ER.

---

### Experiment 3 (ordered third)
**Name:** Transient secretion test in *A. oryzae* using an AMA1‑based autonomously replicating plasmid.  
**Question answered:** Does the full cassette (amyB promoter, α‑amylase signal peptide, codon‑optimised uricase) drive secretion of active uricase into the culture medium in the target host?  
**Cost:** Mid wet‑lab ($500–5 000) — gene synthesis of the complete cassette, cloning into an AMA1 vector, protoplast/PEG transformation of a uricase‑deficient *A. oryzae* host, shake‑flask cultivation (50 mL), and uricase activity assay of the supernatant.  
**Timeline:** 3–4 weeks.  
**Decision informed:**  
- **Kill the design** if no extracellular activity is detected.  
- **Modify a specific parameter** (signal peptide, promoter strength, culture conditions) if activity is low or secretion efficiency is poor.  
- **Proceed** to stable chromosomal integration and scale‑up if secreted activity exceeds a predefined threshold (e.g., >10 U/L).  
**Biggest risk factor for uninterpretability:** AMA1 plasmids are mitotically unstable and show high copy‑number variation; an absence of activity could be due to plasmid loss rather than cassette failure. Rigorous selection pressure and multiple biological replicates are essential to avoid a false‑negative conclusion.

---

### Ordering justification (information‑per‑dollar)
1. **In silico audit** – zero cost, rapid, and can immediately eliminate designs with catastrophic sequence‑level flaws (e.g., a non‑cleavable signal peptide). Highest information‑per‑dollar because it filters out non‑starters before any reagent is purchased.  
2. **Cell‑free activity test** – low cost, answers the most fundamental biochemical question: is the uricase sequence capable of folding into an active enzyme? A negative result here saves the cost and time of any fungal work.  
3. **Transient *A. oryzae* secretion** – higher cost and longer timeline, but it integrates host‑specific secretion machinery and is the minimal test of the complete cassette in the target organism. Only warranted once the uricase moiety itself has been validated.
