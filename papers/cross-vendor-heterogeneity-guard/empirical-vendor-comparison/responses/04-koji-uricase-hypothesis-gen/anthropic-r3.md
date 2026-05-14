---
prompt_id: 04-koji-uricase-hypothesis-gen
prompt_sha256_12: 9dc91d95f2f9
vendor: anthropic
replicate: 3
model_requested: anthropic/claude-opus-4-7
model_served: anthropic/claude-4.7-opus
model_served_raw: anthropic/claude-4.7-opus-20260416
call_timestamp_utc: 2026-05-14T17:43:35.546221Z
latency_seconds: 56.64
input_tokens: 532
output_tokens: 3318
cost_usd: 0.2568
finish_reason: stop
response_sha256_12: 05fd2c418678
status: ok
---

# De-risking experiments for the *A. oryzae*::*A. flavus* uricase cassette

**Assumptions stated upfront:**
- Native *A. flavus* uricase (UniProt Q12553 / UoX) is peroxisomal in its source organism — it carries a C-terminal PTS1-like tripeptide (SKL or variant). The cassette as described does not mention deletion of this signal, so secretion competence is non-obvious.
- Uricase is a homotetramer (~135 kDa); folding/oligomerization in the ER/secretory pathway is a real liability versus its native cytosolic/peroxisomal folding environment.
- Uricase catalysis requires molecular O₂ and produces H₂O₂; activity at GI luminal pH (≈1.5 stomach → 6–7.4 small intestine → 5.5–7 colon) is the relevant performance envelope, not the pH 8–9 optimum used in clinical IV rasburicase assays.
- "Food-grade" implies no antibiotic selection markers in the final strain, but selection markers are acceptable at this design stage.

Ordered by expected information-per-dollar (highest first).

---

## Experiment 1 — In silico signal peptide / secretion compatibility and PTS1 conflict audit

1. **Name & question:** *Sequence-level secretion-competence audit.* Does the α-amylase SP cleave correctly when fused to the codon-optimized uricase N-terminus, and does the native C-terminal PTS1 motif (or any cryptic ER retention / N-glycosylation / GPI signals) actively oppose secretion?
   - Tools: SignalP 6.0 (eukaryotic), DeepLoc 2.0, PTS1 predictor (Neuberger), NetNGlyc/NetOGlyc, big-PI fungal predictor, and a Kozak/codon adaptation index check (CAI, %MinMax) against the *A. oryzae* highly-expressed gene set; AlphaFold2/3 fold of the SP-cleaved mature protein and the tetramer interface.
2. **Cost:** ~$0 (in silico).
3. **Timeline:** 2–4 days.
4. **Decision informed:**
   - If PTS1 is intact and predicted active → **modify** cassette to truncate or mutate the C-terminal tripeptide (e.g., SKL→SKL-stop+linker or deletion) before any cloning.
   - If SP cleavage probability at the designed junction is <0.7 or predicted to leave a non-native N-terminal residue that destabilizes the fold → **modify** the SP/propeptide junction or swap to a glaA or CBHI-derived SP.
   - If predicted N-glycosylation sites cluster at the tetramer interface → **modify** (consider N→Q mutations) or flag for empirical check.
   - Clean result → **proceed** to Experiment 2.
5. **Biggest interpretability risk:** SignalP/DeepLoc are trained predominantly on yeast/mammalian data; *Aspergillus* secretion idiosyncrasies (e.g., glaA carrier-protein dependence for heterologous secretion) are under-represented. A "pass" prediction does not rule out empirical failure, but a "fail" prediction is reasonably trustworthy.

---

## Experiment 2 — Cell-free expression + activity assay of the mature (post-cleavage) coding sequence

1. **Name & question:** *In vitro transcription/translation (IVTT) functional check.* Does the codon-optimized mature uricase polypeptide (SP removed in the construct used here) fold into catalytically active tetramer at all, independent of the host secretion pathway? This isolates the "is the protein functional after codon optimization and any silent engineering" question from the "does *A. oryzae* secrete it" question.
   - Use a eukaryotic CFE system (wheat germ or *Leishmania* LEXSY lysate preferred over *E. coli* S30 for a eukaryotic tetramer; rabbit reticulocyte is acceptable). Express mature ORF; assay uricase activity by uric acid absorbance loss at 293 nm in air-saturated buffer at pH 7.5 and pH 6.0 (small-intestinal proxy), and by Amplex Red for H₂O₂ generation. Run native PAGE / SEC for tetramer assembly.
2. **Cost:** Mid wet-lab, ~$1,500–3,000 (CFE kit + uric acid + Amplex Red + plasmid synthesis if not already in hand). If the lab already has a CFE pipeline, low wet-lab.
3. **Timeline:** 1.5–3 weeks including DNA template prep.
4. **Decision informed:**
   - No activity, no tetramer → **kill or major redesign**: revert codon optimization, try *A. flavus* native sequence, or switch to a better-characterized uricase chassis (e.g., *Candida utilis* / *Arthrobacter*).
   - Activity present but low specific activity vs. published rasburicase (~8 U/mg) → **modify** (likely revisit codon table / rare-codon clusters at folding-critical regions).
   - Activity comparable to literature → **proceed** to in-host expression.
5. **Biggest interpretability risk:** CFE systems lack the native peroxisomal redox/cofactor environment and may under-fold a tetramer that would fold fine in a cell. A negative result could be a CFE artifact rather than a true sequence defect. Mitigation: include a positive control (commercial rasburicase or a published functional uricase ORF) in the same CFE run.

---

## Experiment 3 — Small-scale shake-flask secretion test in a surrogate *A. oryzae* / RIB40 background with supernatant activity readout

1. **Name & question:** *Phase-0 secretion + luminal-condition activity screen.* When the full cassette is transformed into *A. oryzae* (e.g., RIB40 or a *pyrG* auxotroph, both BSL-1), does uricase appear in the culture supernatant at detectable specific activity, and does that activity survive simulated upper-GI conditions (simulated gastric fluid, SGF, pH 1.2 with pepsin for 30–60 min, then simulated intestinal fluid, SIF, pH 6.8 with pancreatin)?
   - Read-outs: supernatant uric acid degradation rate (A293 assay), Western blot against uricase, total secreted protein (BCA), and post-SGF/SIF residual activity. 3–5 transformants, two media (CD vs. DPY or maltose-induced), 50 mL shake flasks.
2. **Cost:** Mid wet-lab, ~$2,000–5,000 (transformation reagents, media, pepsin/pancreatin, blot consumables; assumes strain and basic mycology infrastructure on hand). Approaches the upper bound of the band.
3. **Timeline:** 4–6 weeks (transformation + purification of transformants + assay).
4. **Decision informed:**
   - No supernatant activity but intracellular activity present → **modify** secretion strategy: glaA carrier fusion, alternative SP, propeptide engineering, or *vps*/protease-deficient host.
   - Supernatant activity present but destroyed by SGF → **modify** product strategy (enteric encapsulation is now a hard requirement, not optional; or engineer pH/protease tolerance; or relocate activity to colonic delivery).
   - Supernatant activity present and ≥50% retained through SGF/SIF → **proceed** to full strain engineering and scale-up.
   - Activity present only after cell lysis with no secretion despite multiple SP variants → **kill** the secretion strategy; reconsider whole-cell (lysed koji) product format.
5. **Biggest interpretability risk:** *A. oryzae* secretes abundant proteases (especially in submerged culture with rich N source); a negative supernatant result could reflect proteolysis of correctly secreted uricase rather than a secretion failure. Mitigation: include protease inhibitor cocktail in one arm, and/or use a protease-reduced host (Δ*tppA* Δ*pepE* etc.) if available — but note this adds scope and pushes toward full engineering cycle.

---

## Justification of ordering (information-per-dollar)

1. **Exp 1 first** — at ~$0 and <1 week, a single in silico finding (intact PTS1, predicted SP miscleavage, severe rare-codon cluster) can redirect the entire cassette design before any DNA is ordered. The expected-value calculation is dominated by the asymmetry: small downside, potentially cassette-saving upside. Information density per dollar is effectively unbounded.
2. **Exp 2 second** — decouples "is the ORF functional" from "is the host competent," which is the most common confounder when a secreted heterologous fungal cassette fails. Spending $1.5–3k here prevents spending 4–6 weeks and $2–5k on Exp 3 only to be unable to attribute failure. CFE is ~10× cheaper than the equivalent answer obtained by building protease-null hosts or running intracellular vs. extracellular fractionation panels.
3. **Exp 3 last** — highest absolute cost and longest timeline, but it is the only one of the three that tests the actual product-relevant question (secreted + GI-stable activity). It is correctly ordered last because Exps 1 and 2 sharply increase the probability that Exp 3's result is interpretable and actionable rather than a multi-variable failure.

A reasonable stopping rule: if Exp 1 returns a clear structural problem (e.g., PTS1 intact, predicted strong peroxisomal targeting), do not run Exps 2–3 until the cassette is revised and Exp 1 re-run.
