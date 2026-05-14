---
prompt_id: 04-koji-uricase-hypothesis-gen
prompt_sha256_12: 9dc91d95f2f9
vendor: deepseek
model_requested: deepseek/deepseek-v4-pro
model_served: deepseek/deepseek-v4-pro
model_served_raw: deepseek/deepseek-v4-pro-20260423
call_timestamp_utc: 2026-05-14T15:29:09.073351Z
latency_seconds: 84.42
input_tokens: 328
output_tokens: 4118
cost_usd: 0.0037
finish_reason: stop
response_sha256_12: 0269e14f1112
status: ok
---

**Assumptions**
- *A. flavus* uricase is naturally intracellular (peroxisomal); heterologous secretion represents a non-native topology that may challenge folding and disulfide bond formation in the secretory pathway.
- The α‑amylase secretion signal is the native signal peptide from *A. oryzae* AmyB and is cleaved by signal peptidase.
- The amyB promoter is constitutive and strong enough for the intended production, but its regulation under scale‑up conditions is not at issue here.
- *A. oryzae* is BSL‑1; all proposed work stays within BSL‑1.
- “Phase‑0 design‑stage” means no whole‑organism engineering of *A. oryzae* has yet been performed.

---

### 1. In silico – Signal peptide cleavage and pre‑protein structure assessment

**Question answered**  
Does the α‑amylase signal peptide–uricase junction generate a high‑probability signal peptidase cleavage site without occluding the uricase N‑terminus, and does the fusion create steric clashes that would prevent proper folding?

**Cost**  
~$0 (strictly computational, using web‑accessible tools)

**Timeline**  
2–3 days (sequence threading, molecular dynamics relaxation, consensus scoring)

**Decision informed**  
- If SignalP 6.0 (eukaryotic mode) returns a cleavage probability <0.5 or a non‑canonical cleavage site, **modify the signal peptide or introduce a flexible linker**.  
- If AlphaFold2 or ESMFold predicts the signal peptide sterically blocks the uricase active site or prevents tetramer assembly, **insert a structured linker or switch to a shorter secretion tag**.  
- If both predictions are favourable, **proceed** with the current cassette architecture.

**Biggest risk factor for uninterpretability**  
Predictors trained on generic eukaryotic data may not capture *A. oryzae*‑specific signal peptidase preferences or the influence of the filamentous fungal ER environment; a high‑confidence *in silico* score could still fail *in vivo*.

---

### 2. Low wet‑lab – Heterologous expression of uricase in *E. coli* and simulated gastrointestinal (GI) stability/activity assay

**Question answered**  
Is the *A. flavus* uricase (codon‑optimised for *A. oryzae*) intrinsically active, and can it withstand the pH, proteases, and bile salts it would encounter in the human GI tract?

**Cost**  
<$500 (gene synthesis, pET vector, Ni‑NTA purification, uric acid substrate, simulated gastric & intestinal fluid reagents)

**Timeline**  
3–4 weeks (cloning, small‑scale expression, IMAC purification, kinetic assay ± GI exposure)

**Decision informed**  
- If purified uricase has no detectable activity (k_cat < 1% of published uricases), **kill the design** – the enzyme is non‑functional.  
- If >50% activity is lost after 2 h in simulated gastric fluid (pH 2, pepsin) and not regained upon transfer to simulated intestinal fluid, **modify the delivery concept** (enteric coating required) or **kill the design** as a naked dietary supplement.  
- If the enzyme retains >30% residual activity under sequential gastric‑then‑intestinal conditions, **proceed** with the cassette.

**Biggest risk factor for uninterpretability**  
The *E. coli* cytoplasm is reducing and lacks eukaryotic chaperones; if uricase requires disulfide bonds or eukaryotic folding factors, the bacterially produced protein may be inactive regardless of its true potential in the *A. oryzae* secretory pathway, giving a false‑negative activity result.

---

### 3. Mid wet‑lab – Secretion competence test of the α‑amylase signal peptide–uricase fusion in *Saccharomyces cerevisiae*

**Question answered**  
Can the *A. oryzae* α‑amylase signal peptide direct efficient secretion of the heterologous uricase in a eukaryotic host, and is the secreted enzyme soluble and active?

**Cost**  
$500–5 000 (gene synthesis of the exact signal‑peptide–uricase fusion in a yeast episomal vector, yeast transformation, selection, micro‑scale culture, and uricase activity assay in supernatant vs. cell lysate)

**Timeline**  
6–8 weeks (shorter if in‑lab yeast systems are already established)

**Decision informed**  
- If >70% of total uricase activity is found in the culture supernatant, **proceed** – the signal peptide functions and the enzyme folds properly in a eukaryotic secretory pathway.  
- If activity is exclusively intracellular, **modify** the cassette: test alternative signal peptides (e.g., *A. niger* glucoamylase, synthetic pre‑pro sequences) or add an ER‑retention‑avoidance motif.  
- If no activity is detected anywhere, the uricase cannot fold in a eukaryotic secretome; **kill the design** or move to a non‑secreted intracellular strategy.

**Biggest risk factor for uninterpretability**  
The *A. oryzae* α‑amylase signal peptide may be inefficiently recognised by the yeast Sec61 translocon or processed incorrectly by yeast signal peptidase, leading to no secretion even though it would work perfectly in the homologous *A. oryzae* host – a false‑negative that could prematurely discard a viable cassette.

---

**Ordering justification (information‑per‑dollar, high → low)**  
1. **In silico** – zero cost, immediate feedback on the most fundamental sequence‑level compatibility; any severe defects here stop further investment.  
2. **E. coli GI assay** – <$500, answers the critical question of whether the therapeutic payload itself can survive the gut; if the enzyme is inherently GI‑labile, the entire approach is unsound regardless of secretion success.  
3. **Yeast secretion test** – $500–5 000, addresses the highest engineering risk (secretion of a non‑native protein) in a eukaryotic context, but is costlier and may yield a host‑specific false‑negative; its value is tempered by the lower confidence in directly predicting *A. oryzae* behaviour.
