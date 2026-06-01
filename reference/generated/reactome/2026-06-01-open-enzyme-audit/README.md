# Reactome Open Enzyme Audit Outputs

Generated: 2026-06-01

These files are the durable subset of the Reactome CLI scratch run used for the Open Enzyme Reactome pathway audit. The full scratch run lived at `/tmp/reactome-audit-run/` and can be regenerated with `tools/reactome/reactome_analysis.py`.

The committed subset keeps the provenance needed for wiki and operations claims without committing every exploratory query result.

## Files

- `search-summary.json` - compact summary of all pathway and molecule searches.
- `events-complement-cascade.json` - contained events for `R-HSA-166658` Complement cascade.
- `search-factor-h.json`, `search-factor-i.json`, `search-cd55.json`, `search-SERPING1.json` - complement regulator searches used to separate clean Reactome anchors from noisy/context-only hits.
- `low-pathways-ABCG2.json` - low-level pathways containing Reactome ABCG2 entity `R-HSA-917929`.
- `events-purine-catabolism.json` - contained events for `R-HSA-74259` Purine catabolism.
- `events-pyroptosis.json` - contained events for `R-HSA-5620971` Pyroptosis.
- `low-pathways-NFE2L2.json` - low-level pathways containing Reactome NFE2L2 entity `R-HSA-201566`.
- `low-pathways-TLR4.json` - low-level pathways containing Reactome TLR4 entity `R-HSA-2201285`.
- `events-digestion.json` - contained events for `R-HSA-8935690` Digestion.
- `events-bile-acid.json` - contained events for `R-HSA-194068` Bile acid and bile salt metabolism.
- `search-*.json` - molecule-level searches used to classify contribution candidates versus already-modeled drug interactions.

## Interpretation Discipline

Reactome IDs are pathway graph anchors, not primary evidence. Any quantitative, residue-level, PMID, DOI, clinical, or evidence-tier claim derived from these anchors still needs the normal Open Enzyme pre-commit verification gate against primary sources.
