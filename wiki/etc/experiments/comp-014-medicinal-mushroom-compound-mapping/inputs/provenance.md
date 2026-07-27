# comp-014 — Input provenance

The Phase 1 inputs register a bounded source and target scope. Later pulls and joins exist in the artifact, but the retained scope validator does not reproduce them. Their rows are retrieval leads, not current ranks or biological verdicts.

## inputs/data-sources.json

Hand-curated list of compound databases, bioactivity sources, and multilingual literature corpora recorded for Phases 2–5. Each entry records URL, scope, access method, expected yield, and (where relevant) language and translation-protocol notes under the top-level [`CLAUDE.md`](../../../../../CLAUDE.md) translation protocol.

**Source for the source list:**
- LOTUS, NPAtlas, COCONUT, MIBiG: known public natural-product databases, URLs from the database home pages
- KNApSAcK, NPASS, TCMSP, TCMID, TCM Database@Taiwan, HIT, BATMAN-TCM: known East-Asian-hosted compound + target databases referenced in the natural products informatics literature; URLs are the maintainer-published canonical entry points
- ChEMBL, PubChem BioAssay, SwissTargetPrediction, STITCH: standard bioactivity / target-prediction sources
- CNKI, Wanfang, J-STAGE, CiNii, KISS, RISS: regional Chinese, Japanese, and Korean literature corpora recorded under the project's multilingual-research rule

No fetches were executed by the Phase 1 scope step. The source list documents the intended coverage; it is not proof that every source was successfully queried.

## inputs/phase-5-anchor-species.json

The file contains 18 historical anchor species used as retrieval and pipeline-coverage leads, not as a current candidate ranking. Sources recorded for that selection included:
- TCM materia medica references (Ganoderma, Cordyceps, Wolfiporia, Polyporus, Tremella, Auricularia, Phellinus traditional indications)
- Western medicinal-mushroom monographs (Hericium, Trametes, Inonotus, Grifola, Lentinula, Agaricus blazei, Pleurotus)
- Industrial-fungus precedent (Aspergillus oryzae as Open Enzyme chassis; Aspergillus terreus as lovastatin-original)
- Common-name and TCM-name fields filled from standard ethnomycology and TCM materia medica

NCBI Taxonomy IDs are canonical and will be the join key for fungal-species de-duplication across LOTUS / NPAtlas / KNApSAcK / TCMSP / MIBiG in Phase 2.

**Excluded** — three categories documented in the JSON: psychoactive (Schedule I), toxic (Amanita, Claviceps), and culinary-only (truffles).

## inputs/chokepoint-targets.json

Open Enzyme chokepoint targets to map fungal compounds against. Drawn directly from existing wiki pages:
- [`modality-chokepoint-matrix.md`](../../../../modality-chokepoint-matrix.md) — chokepoint inventory
- [`nlrp3-exploit-map.md`](../../../../nlrp3-exploit-map.md) — NLRP3 sub-chokepoints
- [`abcg2-modulators.md`](../../../../abcg2-modulators.md) — transporter biology
- [`complement-c5a-gout.md`](../../../../complement-c5a-gout.md) — complement layer
- [`gout-pathophysiology.md`](../../../../gout-pathophysiology.md) — XO, NLRP3, and transporter context
- [`spm-resolution-pathway.md`](../../../../spm-resolution-pathway.md) and [`tnfsf14-gout-target.md`](../../../../tnfsf14-gout-target.md) — Lp-PLA2 context
- [`food-grade-hdaci-screen-computational.md`](../../../../food-grade-hdaci-screen-computational.md) — HDAC6 context
- [`supplements-stack.md`](../../../../supplements-stack.md) — Nrf2/KEAP1 context

UniProt accessions used as the join key. Each accession is the canonical human entry; rest.uniprot.org is whitelisted for Phase 2 verification queries if any accession is suspect.

The redox/disulfide entry is retained only as a historical lead container. It is not a proposed, admitted, preliminary, or rejected chokepoint. Any compound–target pair from that container requires primary-source rehydration and mechanism-matched testing.

## Raw source captures left unchanged

This cleanup does not modify source payloads under:

- `outputs/_chembl_raw/*.json`
- `outputs/_lotus_raw/*.json`
- `outputs/_npatlas_raw/*.json`
- `outputs/_knapsack_raw/*.html`

It also leaves the historical identifier caches and target lookup intermediate unchanged. These files preserve retrieval provenance; derived summaries, ranks, and recommendations do not inherit authority from them.

## What Phase 1 does NOT include

- Actual compound records pulled from any database (Phase 2)
- Target-mapping output (Phase 3)
- Chokepoint-intersection rows suitable for current ranking (historical rank fields have no current decision authority)
- Complete multilingual primary-literature ingestion
- Per-compound viability ranking. The former comp-013-style Phase 6 method is retired; any successor must preserve effect polarity and require relevant exposure plus mechanism-matched function.

The sole retained execution step is `scripts/scope_validate.py`; no later phase has a current sign-off or runnable reproduction path in this artifact.
