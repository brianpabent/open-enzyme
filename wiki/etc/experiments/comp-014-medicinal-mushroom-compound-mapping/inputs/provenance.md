# comp-014 — Input Provenance

**Phase 1 (this commit) registers the experiment scope. No external database queries have been executed.** Phase 2 will pull data; that pass will append per-source fetch dates, dump versions, and record counts to this file.

## inputs/data-sources.json

Hand-curated list of compound databases, bioactivity sources, and multilingual literature corpora planned for Phase 2-5. Each entry records URL, scope, access method, expected yield, and (where relevant) language and translation-protocol notes per `Open Enzyme/CLAUDE.md` §Translation protocol.

**Source for the source list:**
- LOTUS, NPAtlas, COCONUT, MIBiG: known public natural-product databases, URLs from the database home pages
- KNApSAcK, NPASS, TCMSP, TCMID, TCM Database@Taiwan, HIT, BATMAN-TCM: known East-Asian-hosted compound + target databases referenced in the natural products informatics literature; URLs are the maintainer-published canonical entry points
- ChEMBL, PubChem BioAssay, SwissTargetPrediction, STITCH: standard bioactivity / target-prediction sources
- CNKI, Wanfang, J-STAGE, CiNii, KISS, RISS: per `Open Enzyme/CLAUDE.md` global-multilingual-research rule, the canonical Chinese / Japanese / Korean primary-literature corpora

No fetches executed in Phase 1 — the source list is documentation of intent, not yet retrieval.

## inputs/candidate-species.json

15 medicinal fungi selected by the criteria in the file (substantive characterized chemistry + human-use precedent + regulatory tractability). Sources for the candidate selection:
- TCM materia medica references (Ganoderma, Cordyceps, Wolfiporia, Polyporus, Tremella, Auricularia, Phellinus traditional indications)
- Western medicinal-mushroom monographs (Hericium, Trametes, Inonotus, Grifola, Lentinula, Agaricus blazei, Pleurotus)
- Industrial-fungus precedent (Aspergillus oryzae as Open Enzyme chassis; Aspergillus terreus as lovastatin-original)
- Common-name and TCM-name fields filled from standard ethnomycology and TCM materia medica

NCBI Taxonomy IDs are canonical and will be the join key for fungal-species de-duplication across LOTUS / NPAtlas / KNApSAcK / TCMSP / MIBiG in Phase 2.

**Excluded** — three categories documented in the JSON: psychoactive (Schedule I), toxic (Amanita, Claviceps), and culinary-only (truffles).

## inputs/chokepoint-targets.json

Open Enzyme chokepoint targets to map fungal compounds against. Drawn directly from existing wiki pages:
- `wiki/modality-chokepoint-matrix.md` — canonical chokepoint inventory (rows × columns)
- `wiki/nlrp3-exploit-map.md` — NLRP3 sub-chokepoints (CP0–CP6)
- `wiki/abcg2-modulators.md` — transporter biology (URAT1, GLUT9, ABCG2, OAT1/3)
- `wiki/complement-c5a-gout.md` — CP0 complement layer (C5aR1, the platform-gap target)
- `wiki/gout-pathophysiology.md` — XO, NLRP3, transporter axis
- `wiki/spm-resolution-pathway.md`, `wiki/tnfsf14-gout-target.md` — Lp-PLA2 inflammation axis
- `wiki/food-grade-hdaci-screen-computational.md` (comp-007) — HDAC6 axis
- `wiki/supplements-stack.md` — Nrf2/KEAP1 axis

UniProt accessions used as the join key. Each accession is the canonical human entry; rest.uniprot.org is whitelisted for Phase 2 verification queries if any accession is suspect.

**One proposed addition** — `_PROPOSED_redox_disulfide_modulators` — is flagged as not-yet-canonical. Phase 5 deliverable is a confirm/reject decision based on whether the breadth pass surfaces enough fungal-compound coverage to warrant a formal chokepoint addition. Rejection criteria documented in the JSON.

## What Phase 1 does NOT include

- Actual compound records pulled from any database (Phase 2)
- Target-mapping output (Phase 3)
- Chokepoint intersection ranked candidate list (Phase 4)
- Multilingual primary-literature ingestion (Phase 5)
- Per-compound triage with comp-013-style methodology (Phase 6)

Reason: this is a phase-gated multi-pass experiment with material data-volume and translation-cost implications. Brian reviews the scope first; Phase 2+ executes after sign-off.
