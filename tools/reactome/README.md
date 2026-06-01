# Reactome Database CLI & Integration Tool
**Location:** `tools/reactome/`  
**Purpose:** A completely self-contained, zero-dependency Python utility enabling *any* agent (Claude Code, Codex, or custom shell scripts) to query, search, and analyze data in the Reactome pathway database.

---

## How to Use This Tool

This tool is designed to run anywhere with a standard **Python 3.10+** environment. It uses only the Python standard library plus the local `http_client.py` in this directory.

### Running via Plain Python

```bash
python3 tools/reactome/reactome_analysis.py <command> [options] --output <file>
```

### Running via `uv`

No external dependency resolution is required. If another agent prefers `uv`, it can still execute the script:

```bash
uv run tools/reactome/reactome_analysis.py <command> [options] --output <file>
```

---

## 📋 Common Commands Reference

All commands require the `--output <path>` argument to write structured JSON or image results to a file. Parent directories are created automatically.

### 1. Database Info
Check database status and connectivity:
```bash
python3 tools/reactome/reactome_analysis.py db-version --output /tmp/version.json
python3 tools/reactome/reactome_analysis.py db-name --output /tmp/name.json
```

### 2. Search the Knowledgebase
Search for a pathway, molecule, or drug in Reactome:
```bash
python3 tools/reactome/reactome_analysis.py search --query "NLRP3 inflammasome" --output /tmp/search.json
```
No-hit searches are written as structured JSON with `notFound: true` instead of failing, which is useful for curation-gap audits.

### 3. Mechanistic Queries (Stable IDs)
Query the detailed reaction equations, authors, orthologs, and summation for a specific Reactome ID (e.g. `R-HSA-844456`):
```bash
python3 tools/reactome/reactome_analysis.py query --id R-HSA-844456 --output /tmp/pathway.json
```

### 4. Reaction/Event Participants
Get the exact UniProt accessions, chemical compounds (ChEBI), and complexes involved in a specific step:
```bash
python3 tools/reactome/reactome_analysis.py participants --id R-HSA-877178 --output /tmp/participants.json
```

### 5. Diagram Export (PNG/SVG)
Export structural layout diagrams of pathways, with optional gene highlighting:
```bash
# Export the parent NLR signaling pathway with NLRP3 highlighted in the diagram
python3 tools/reactome/reactome_analysis.py diagram --id R-HSA-168643 --highlight NLRP3 --output /tmp/nlr_diagram.png
```

### 6. Batch Gene List Enrichment
Post a list of genes or proteins (separated by commas or newlines) to get a p-value ranked pathway hits report and a 7-day `summaryToken`:
```bash
python3 tools/reactome/reactome_analysis.py analyze --data "NLRP3,PYCARD,CASP1,IL1B" --output /tmp/enrichment.json
```

---

## Open Enzyme Research Discipline

Reactome is a curated pathway graph, not a substitute for primary literature. Use Reactome IDs, participants, summations, and `regulatedBy` edges to orient mechanistic work, then grep-verify any load-bearing numbers, residue positions, PMIDs, DOIs, or evidence-tier conclusions against primary sources before editing `wiki/`.

For durable generated exports, prefer `reference/generated/reactome/`. For scratch inspection, use `/tmp`.

---

## 🧩 Programmatic Python Import

You can import the robust, rate-limited `http_client` directly in other Python scripts within the workspace:

```python
import sys
sys.path.append("tools/reactome")
import http_client

# Initialize a rate-limited client for Reactome (1 request per second)
client = http_client.HttpClient("https://reactome.org/", qps=1)

# Fetch a query directly
response_json = client.fetch_json("ContentService/data/query/R-HSA-844456")
print(response_json.get("displayName"))
```
