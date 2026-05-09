# comp-020 query strategy

## Independence statement

This is a brief-scrubbed verification re-run. Per the mission spec:

- **No prior comp-018 (or comp-019) findings were consulted.** The compound list emerges from the lit-scan, anchored to target nodes only.
- Compound-class breadth applied: fungal, plant (phenolic / flavonoid / terpenoid / polysaccharide / lignan / alkaloid), bacterial, marine, dietary, FDA-approved, TCM, Kampo, Ayurvedic — all with equal initial weight.
- Multilingual default: PubMed + CNKI + WanFang + J-STAGE + KISS / RISS where queries support it.
- Paperclip MCP `map` operator NOT used per memory feedback (hallucinates organisms + numbers).

## Per-node anchor queries

For each upstream complement node, the search pattern is:

```
"<node-name>" AND ("inhibitor" OR "antagonist" OR "modulator" OR "natural product" OR "extract")
```

with refinements per compound class. Multi-vendor cross-check applied to non-English claims when a load-bearing IC50 is involved.

### Initiation
- C1q binding inhibitors / C1q deposition modulators
- MBL pathway inhibitors / MASP-1 / MASP-2 inhibitors
- Alternative-pathway C3 tickover modulators

### Convertase
- C3 convertase inhibitors (broad)
- C5 convertase inhibitors

### Soluble factors
- Factor B inhibitors / Bb formation
- Factor D inhibitors (iptacopan-like / ACH-4471 ancestor / natural)
- Factor H upregulators / mimetics / stabilizers
- Properdin inhibitors
- Clusterin modulators

### Membrane regulators
- CD55 / DAF expression upregulators
- CD59 expression upregulators
- CR1 modulators

### Total-complement (CH50/AP50) screens
Anti-complement total assays catch broad inhibitors that aren't node-specific in the literature.

## Assay-format heterogeneity flag

For any compound with multiple reported IC50 values, document the assay format:
- CH50 (sheep erythrocyte hemolysis, classical pathway readout)
- AP50 (rabbit erythrocyte hemolysis, alternative pathway readout)
- Direct enzymatic convertase assay
- ELISA-based deposition assay (Wieslab-style)
- Cell-based vs. cell-free
- Serum-source heterogeneity (human vs. guinea pig vs. rabbit)

If IC50 spans >5x across the literature, flag and document.

## Translation cross-check protocol

Non-English source with load-bearing claim -> two independent models. For Chinese sources, one Western-trained (Claude / Gemini) + one Chinese-vendor (DeepSeek / Qwen). Surface disagreements as `{Model A: ... | Model B: ...}` inline annotations.

## Tool order

1. Paperclip MCP search (PMC + bioRxiv + medRxiv full-text + OpenAlex abstracts).
2. PubMed via WebSearch / WebFetch for English depth pass.
3. CNKI / WanFang / J-STAGE direct queries via WebSearch — read sources in original where possible.
4. ChEMBL coverage check per top compound (anticomplement assays sparsely curated; document the gap).
5. DrugBank / RxNorm for FDA-approved repurposing surface.
