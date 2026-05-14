---
prompt_id: 04-koji-uricase-hypothesis-gen
prompt_sha256_12: 9dc91d95f2f9
vendor: openai
replicate: 3
model_requested: openai/gpt-5.5
model_served: openai/gpt-5.5
model_served_raw: openai/gpt-5.5-20260423
call_timestamp_utc: 2026-05-14T17:42:38.907002Z
latency_seconds: 162.10
input_tokens: 334
output_tokens: 6470
cost_usd: 0.0786
finish_reason: stop
response_sha256_12: 52845b79ee37
status: ok
---

## Assumptions

1. Costs exclude personnel, existing incubators, qPCR/plate-reader access, and routine consumables already present in a fungal molecular biology lab.  
2. The parental *A. oryzae* strain is handled under BSL-1 conditions and is available for non-recombinant culture tests.  
3. “amyB promoter constitutive” is treated as an unverified design assumption; amylase promoters in *Aspergillus* are often carbon-source regulated.  
4. The goal at this stage is to de-risk the cassette and product premise, not to optimize production titer.  
5. No animal, human-subject, or BSL-2+ work is proposed.

---

| Order | Experiment | Question answered | Cost | Timeline | Decision informed | Biggest risk to interpretability |
|---:|---|---|---|---|---|---|
| 1 | **In silico cassette and secretory-pathway liability audit** | Does the proposed amyB–α-amylase signal peptide–*A. flavus* uricase cassette contain obvious design liabilities before synthesis/integration? | In silico, ~$0 | 1–3 days | **Proceed** if no major liabilities; **modify** if specific liabilities are found; **kill/rethink** if multiple independent liabilities converge | Prediction tools are not calibrated well for *A. oryzae* secreted heterologous enzymes, so absence of flagged liabilities is not evidence of secretion competence |
| 2 | **Parental-strain amyB promoter-regime validation under intended production media** | Is the amyB promoter actually active under the media/feed regime envisioned for enzyme production? | Low wet-lab, <$500 | ~1 week | **Proceed with amyB** if strongly active; **modify medium/induction regime** or **switch promoter** if repressed/weak | Endogenous amyB expression may not predict activity of the isolated promoter fragment in an engineered cassette/locus |
| 3 | **Surrogate uricase luminal-compatibility assay by urate depletion in simulated GI matrices** | Is unformulated fungal uricase activity plausibly compatible with the intended GI compartment? | Low wet-lab, <$500 if purified uricase and plate-reader access are available | 2–5 days | **Proceed** if activity survives relevant intestinal conditions; **add formulation requirement** if gastric exposure is destructive; **change enzyme/design** if activity is poor at target pH | Commercial/purified surrogate uricase may not match the secreted, glycosylated *A. flavus* uricase product |

---

## 1. In silico cassette and secretory-pathway liability audit

**Precise experiment:**  
Run an integrated computational review of the complete designed expression unit: amyB promoter context if sequence is defined, 5′ UTR, α-amylase signal peptide, signal-peptide/uricase junction, codon-optimized uricase ORF, 3′ UTR/terminator, and mature uricase structure.

**Question answered:**  
Does the cassette contain avoidable liabilities that would make expression, secretion, folding, or activity unlikely?

**Analyses to include:**

- **Codon-usage and translation features**
  - CAI/tAI against highly expressed *A. oryzae* secreted proteins.
  - Extreme GC windows, homopolymers, repeats, unwanted restriction sites if relevant.
  - Strong predicted mRNA secondary structure near the start codon/signal-peptide region.

- **Fungal transcript-processing liabilities**
  - Cryptic splice donor/acceptor motifs.
  - Premature polyadenylation-like motifs.
  - Internal TATA-like or transcriptional terminator-like motifs if the ORF is heavily optimized.

- **Secretion-signal assessment**
  - SignalP/Phobius-style prediction of signal peptide cleavage.
  - Whether the predicted mature N-terminus matches a plausible active uricase N-terminus.
  - Whether the α-amylase signal peptide–uricase junction creates a problematic charged/hydrophobic motif.
  - Whether a short linker or alternate secretion signal should be considered.

- **Subcellular targeting conflicts**
  - Scan for C-terminal peroxisomal targeting motifs, because many uricases are naturally peroxisomal.
  - Scan for ER-retention-like motifs.
  - If a strong peroxisomal targeting signal remains, consider whether it should be removed or neutralized in the secreted construct.

- **Mature enzyme structural liabilities**
  - AlphaFold/ColabFold model of the mature uricase, preferably compared with known uricase structures.
  - Conservation of catalytic residues and tetramerization interface.
  - Predicted N-glycosylation motifs and whether they fall near active-site entrances, oligomer interfaces, or structurally buried regions.
  - Surface-exposed protease-sensitive loops, especially in regions likely exposed after secretion.

**Cost:**  
In silico, approximately $0.

**Timeline:**  
1–3 days.

**Decision informed:**

- **Proceed:** no major red flags; signal cleavage and mature enzyme look plausible.
- **Modify specific parameter:**  
  - Change signal peptide or add/remove junction residues if cleavage is ambiguous.  
  - Remove/alter a peroxisomal targeting motif if present and judged problematic.  
  - Adjust codon optimization if extreme local GC, repeats, or RNA structures are introduced.  
  - Consider N-glycosylation-site mutation only if a site is strongly predicted to obstruct active site/interface.
- **Kill/rethink:** multiple independent analyses suggest poor secretion/folding or disrupted catalytic architecture.

**Single biggest risk factor:**  
Computational predictors may miss host-specific secretion bottlenecks in *A. oryzae*; a “clean” audit is necessary but not sufficient.

---

## 2. Parental-strain amyB promoter-regime validation under intended production media

**Precise experiment:**  
Culture the non-engineered parental *A. oryzae* strain under candidate production/feed conditions and measure endogenous amyB expression or secreted α-amylase activity as a proxy for amyB promoter activity.

**Question answered:**  
Will the amyB promoter be active in the actual process conditions, or is the cassette relying on a promoter that is repressed under the intended medium?

**Readouts:**  
Use one or both low-cost readouts:

- Endogenous **amyB transcript abundance** by RT-qPCR.
- Secreted **amylase activity** in culture supernatant as a functional proxy.

Include media conditions that bracket the intended production process, especially different carbon sources if relevant, because amyB-family promoters are commonly starch/maltose induced and glucose repressed.

**Cost:**  
Low wet-lab, <$500.

**Timeline:**  
Approximately 1 week, including culture, sampling, and readout.

**Decision informed:**

- **Proceed with amyB:** strong amyB activity under intended production conditions.
- **Modify production regime:** promoter is active only under specific induction/feed conditions.
- **Switch promoter:** amyB is weak, delayed, or strongly repressed in the desired medium. Candidate alternatives could include other validated *A. oryzae* promoters selected for the intended carbon source and process mode.

**Single biggest risk factor:**  
Endogenous amyB behavior may not fully predict the isolated promoter fragment in an engineered cassette, particularly after genomic integration, copy-number variation, or chromatin-position effects.

---

## 3. Surrogate uricase luminal-compatibility assay by urate depletion in simulated GI matrices

**Precise experiment:**  
Test purified fungal uricase, ideally *A. flavus* uricase if available or the closest obtainable fungal uricase, for urate-depletion activity after exposure to simplified gastric and intestinal matrices.

**Question answered:**  
Is the intended enzyme activity plausibly compatible with the GI compartment where luminal uric acid degradation is expected to occur?

**Suggested comparison conditions, kept at a screening level:**

- Neutral to mildly alkaline buffer approximating small-intestinal pH.
- Acidic gastric-like condition.
- Intestinal-like condition with bile salts and digestive proteases if available.
- Uric acid substrate-only control.
- Heat-inactivated enzyme or no-enzyme control.

Read out urate depletion spectrophotometrically or with a commercial uric acid assay.

**Cost:**  
Low wet-lab, <$500 if enzyme, assay kit/substrate, and plate-reader access are available.

**Timeline:**  
2–5 days.

**Decision informed:**

- **Proceed with cassette as product-relevant:** enzyme activity is retained under the intended intestinal-like conditions.
- **Modify formulation assumption:** enzyme is active at intestinal pH but destroyed by gastric-like exposure, implying enteric protection or targeted release should be required before scale-up.
- **Modify enzyme choice/cassette:** enzyme has poor activity or stability even under intestinal-like conditions, suggesting a different uricase homolog, engineered variant, or product concept should be considered before investing in *A. oryzae* strain construction.
- **Kill design:** no meaningful activity under any plausible luminal condition and no clear formulation workaround.

**Single biggest risk factor:**  
The purified surrogate may not represent the final secreted *A. oryzae* product, especially if the final enzyme is glycosylated, proteolytically processed, or oligomerized differently.

---

## Justification of ordering by expected information-per-dollar

1. **In silico cassette audit** is first because it costs essentially nothing and can identify hard design failures: bad signal-peptide cleavage, introduced transcript-processing motifs, problematic glycosylation sites, or retained peroxisomal targeting signals.

2. **amyB promoter-regime validation** is second because it cheaply tests a central cassette assumption. If amyB is inactive under the intended medium, full strain construction would likely fail for a preventable reason.

3. **surrogate GI compatibility testing** is third because it is still inexpensive and product-critical, but less directly tied to the cassette. Its main limitation is transferability from purified/surrogate enzyme to the eventual secreted *A. oryzae* glycoform.
