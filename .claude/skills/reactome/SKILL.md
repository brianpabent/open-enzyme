---
name: reactome
description: Query, inspect, audit, and contribute Reactome pathway data for Open Enzyme. Use when Codex or Claude Code needs Reactome pathway/reaction details, participant UniProt or ChEBI identifiers, contained events, parent pathways, diagrams, enrichment analysis, or a Reactome contribution gap analysis.
---

# Reactome

## Quick Start

Use the repository-local CLI:

```bash
python3 tools/reactome/reactome_analysis.py --help
python3 tools/reactome/reactome_analysis.py query --id R-HSA-844456 --output /tmp/reactome-nlrp3.json
python3 tools/reactome/reactome_analysis.py participants --id R-HSA-877178 --output /tmp/reactome-participants.json
```

The tool is self-contained and uses only Python 3.10+ standard library modules plus `tools/reactome/http_client.py`. Output parent directories are created automatically.

## Common Tasks

- Search Reactome: `python3 tools/reactome/reactome_analysis.py search --query "NLRP3 inflammasome" --output /tmp/search.json`
- Query a stable ID: `python3 tools/reactome/reactome_analysis.py query --id R-HSA-844456 --output /tmp/pathway.json`
- List sub-events: `python3 tools/reactome/reactome_analysis.py contained-events --id R-HSA-844456 --output /tmp/events.json`
- List ancestors: `python3 tools/reactome/reactome_analysis.py event-ancestors --id R-HSA-844456 --output /tmp/ancestors.json`
- Extract reaction participants: `python3 tools/reactome/reactome_analysis.py participants --id R-HSA-877178 --output /tmp/participants.json`
- Export diagrams: `python3 tools/reactome/reactome_analysis.py diagram --id R-HSA-168643 --highlight NLRP3 --output /tmp/nlr-diagram.png`
- Analyze a gene list: `python3 tools/reactome/reactome_analysis.py analyze --data "NLRP3,PYCARD,CASP1,IL1B" --output /tmp/enrichment.json`

Use `/tmp` for exploratory output. Use `reference/generated/reactome/` only when an export is durable provenance worth committing.

No-hit searches are meaningful during contribution audits. The CLI writes them as JSON with `notFound: true` so agents can distinguish "not present in Reactome search" from a tool failure.

## Research Discipline

Treat Reactome as curated pathway infrastructure, not primary evidence. Before editing `wiki/`, verify load-bearing claims against primary papers: PMIDs, DOIs, residue positions, ChEBI IDs, UniProt accessions, kinetic constants, dose-response numbers, and evidence tiers.

When auditing contribution opportunities, do not infer absence from a single text search. Check:

- Search results for compound and synonym names.
- The target pathway's `hasEvent` or `contained-events`.
- The target event's `regulatedBy`, `precedingEvent`, `followingEvent`, `literatureReference`, and participants.
- Whether Reactome already models the mechanism in a summation even if it lacks a separate reaction edge.

Classify candidates as `absent`, `present-only-in-other-context`, `already-modeled`, or `needs-curator-interpretation`.

## Contribution Dossiers

For Reactome submissions, keep proposals narrow and curator-friendly:

- Name the exact Reactome event(s) to update or regulate.
- Provide the proposed physical entity or regulation edge.
- Cite primary literature with verified PMID/DOI.
- State the evidence level and caveats.
- Avoid claims about authorship, DOI credit, or ORCID integration unless Reactome explicitly promises them.
