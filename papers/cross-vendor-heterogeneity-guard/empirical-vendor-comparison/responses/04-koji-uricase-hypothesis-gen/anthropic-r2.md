---
prompt_id: 04-koji-uricase-hypothesis-gen
prompt_sha256_12: 9dc91d95f2f9
vendor: anthropic
replicate: 2
model_requested: anthropic/claude-opus-4-7
model_served: anthropic/claude-4.7-opus
model_served_raw: anthropic/claude-4.7-opus-20260416
call_timestamp_utc: 2026-05-14T17:16:00.018909Z
latency_seconds: 47.72
input_tokens: 532
output_tokens: 2694
cost_usd: 0.2100
finish_reason: stop
response_sha256_12: 2dabe25ddb45
status: ok
---

# Phase-0 De-risking Experiments for A. oryzae Uricase Cassette

## Assumptions stated upfront
- Uricase referred to is *A. flavus* uricase (uaZ / uricase, ~302 aa, peroxisomal in native host — **note: native enzyme is peroxisomal, not secreted**, which is the central design tension this cassette is fighting).
- "Food-grade" implies final strain must be GRAS-compatible; *A. flavus* sequences in *A. oryzae* are acceptable to many regulators because the two species are taxonomically near-identical, but residual aflatoxin-cluster sequences should be confirmed absent from the cloned region — assumed already verified.
- Target site of action is GI lumen (pH ~1.5 stomach → ~6–7.4 small intestine → ~5.5–7 colon). Uricase requires O₂ and produces H₂O₂; cofactor/oxygen availability in lumen is **not** addressed by any cassette-level experiment and is flagged as out-of-scope here.
- "Low-cost wet-lab" assumes existing lab infrastructure (qPCR, plate reader, SDS-PAGE); reagent-only costing.

---

## Experiment 1 (highest information/$): *In silico* signal-peptide compatibility and secretion-pathway audit

1. **Name & question.** SignalP 6.0 / DeepSig / TargetP-2.0 prediction on the chimeric α-amylase-SP::uricase fusion, combined with PTS1/PTS2 motif scan (e.g., PredPlantPTS1 adapted, or manual C-terminal -SKL/-AKL/-SRL screen) on the mature uricase sequence. **Question: does the fusion predict cleavage at the intended site, and does the mature protein still carry a peroxisomal targeting signal that will compete with ER/secretory routing?**
2. **Cost:** ~$0 (in silico).
3. **Timeline:** 1–2 days including manual curation.
4. **Decision informed:**
   - If SP cleavage probability <0.7 or predicted cleavage site is shifted → redesign SP (try glaA SP, or test ≥3 SP variants in Exp. 3).
   - If C-terminal PTS1 (-SKL-like tripeptide) is present on *A. flavus* uricase → **kill this exact cassette design**; the protein will be co-translationally routed but still tagged for peroxisome, producing mis-sorting. Requires C-terminal extension/tag to mask PTS1 before proceeding.
   - All clean → proceed to Exp. 2 and 3.
5. **Biggest interpretability risk:** SignalP and PTS predictors are trained predominantly on yeast/mammalian/plant data; *Aspergillus*-specific cleavage fidelity is under-represented, so a "pass" is weaker evidence than a "fail." False negatives on PTS1 (non-canonical variants) are the dominant failure mode.

---

## Experiment 2: Codon-optimization QC and mRNA structure check around the SP-CDS junction

1. **Name & question.** Compute CAI/tAI against an *A. oryzae* highly-expressed reference set (amyB, glaA, gpdA), GC% sliding window, and predict mRNA secondary structure (RNAfold / mfe) for the −30 to +90 nt window around the start codon, including the SP-mature junction. **Question: does the codon-optimized cassette introduce a 5′ structural element or rare-codon cluster that will throttle translation initiation or cause SP misprocessing?**
2. **Cost:** ~$0.
3. **Timeline:** 1 day.
4. **Decision informed:**
   - ΔG of 5′ UTR + first 45 nt more negative than ~−10 kcal/mol → modify synonymous codons in the first ~15 codons to reduce structure (cheap fix, no redesign).
   - Rare-codon cluster (>3 consecutive codons <10% usage) in SP region → re-optimize SP separately from mature CDS.
   - Otherwise proceed.
5. **Biggest interpretability risk:** CAI/tAI poorly predict absolute expression in filamentous fungi; published *A. oryzae* codon tables are biased toward a handful of secreted hydrolases, so "optimized" can mean "optimized for amylase-like expression specifically" — which may actually be fine here since amyB promoter is used, but the metric is internally circular.

---

## Experiment 3 (most expensive, most direct): Heterologous small-scale secretion test in *Pichia pastoris* or *S. cerevisiae* as a surrogate host

1. **Name & question.** Synthesize the mature uricase CDS (codon-optimized for the surrogate), fuse to α-factor or native SP in a standard episomal vector, transform into *P. pastoris* GS115 or *S. cerevisiae* BY4741, induce, and assay (a) supernatant uricase activity (uric acid → allantoin, A₂₉₃ decrease, standard assay) and (b) supernatant vs. lysate partitioning by activity and Western. **Question: is *A. flavus* uricase fundamentally secretion-competent when its native peroxisomal context is removed, independent of *A. oryzae*-specific factors?**
2. **Cost:** mid wet-lab, ~$1,500–3,000 (gene synthesis ~$200–400, vector + transformation reagents, uric acid + buffers, anti-His or anti-uricase antibody if Western used).
3. **Timeline:** 3–4 weeks (synthesis lead time dominates; cloning + transformation + induction ~1.5 weeks).
4. **Decision informed:**
   - Activity detectable in supernatant at >10% of total → strong green light; *A. oryzae* cassette likely works; proceed to strain engineering.
   - Activity intracellular only, supernatant null → uricase folds but does not secrete; predicts *A. oryzae* will also fail. Redesign: try fusion partners (e.g., glaA carrier protein fusion) before committing.
   - No activity anywhere → folding/cofactor problem (uricase is a homotetramer requiring proper assembly); kill secreted-format design, consider intracellular expression + cell-wall display or lysis-based formulation instead.
5. **Biggest interpretability risk:** *Pichia*/*Saccharomyces* secretion machinery, glycosylation patterns, and peroxisomal sorting differ enough from *Aspergillus* that a negative result in yeast does not robustly predict failure in *A. oryzae* — yeasts hyperglycosylate and have stricter ER QC. A **positive** result is highly informative; a **negative** is ambiguous. Consider this asymmetric evidence.

---

## Ordering justification (information per dollar)

1. **Exp. 1 > Exp. 2 > Exp. 3.** Exp. 1 can outright kill the cassette (PTS1 conflict is a single-residue-level dealbreaker that no amount of promoter or SP tuning will rescue) for zero cost and one day. Highest expected information per dollar by a wide margin.
2. **Exp. 2** is also free, but its outputs are tuning parameters rather than go/no-go calls — lower decision-leverage per unit time than Exp. 1, but still ~$0 so it ranks second.
3. **Exp. 3** is the only one producing empirical activity data and is by far the most decision-relevant if positive, but it costs ~$2k and 3–4 weeks, and its negative result is ambiguous (asymmetric evidence problem). It belongs last on info/$ grounds despite being the most "real" experiment.

Note that Exp. 1 should gate Exp. 3: there is no point spending $2k on a surrogate-host secretion test if the in silico audit reveals an unmasked PTS1, because the surrogate test would then be testing the wrong question.
