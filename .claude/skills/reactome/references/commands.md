# Reactome CLI Commands

Run from the repository root.

```bash
python3 tools/reactome/reactome_analysis.py db-version --output /tmp/reactome-version.json
python3 tools/reactome/reactome_analysis.py search --query "tranilast" --output /tmp/reactome-search-tranilast.json
python3 tools/reactome/reactome_analysis.py query --id R-HSA-844456 --output /tmp/reactome-nlrp3.json
python3 tools/reactome/reactome_analysis.py contained-events --id R-HSA-844456 --output /tmp/reactome-nlrp3-events.json
python3 tools/reactome/reactome_analysis.py participants --id R-HSA-877178 --output /tmp/reactome-p2x7-atp-participants.json
python3 tools/reactome/reactome_analysis.py diagram --id R-HSA-168643 --highlight NLRP3 --output /tmp/reactome-nlr-signaling.png
```

Use `python3 -m json.tool <file> | sed -n '1,120p'` for quick inspection, and `jq` for targeted extraction.
