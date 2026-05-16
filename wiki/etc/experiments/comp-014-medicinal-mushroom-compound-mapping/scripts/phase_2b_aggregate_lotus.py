"""
Phase 2b: Aggregate LOTUS raw responses into a deduplicated compound × species table.

Reads outputs/_lotus_raw/*.json (created by phase_2b_lotus_pull.sh) and produces:
- outputs/phase-2b-lotus-fungal-compounds.json — species → compound list
- outputs/phase-2b-compounds-by-inchikey.json — compound → species attributions
- outputs/phase-2b-lotus-fungal-compounds.md — human-readable summary

stdlib only (json, pathlib, collections).
"""
import json
from pathlib import Path
from collections import defaultdict


BASE = Path(__file__).resolve().parent.parent / "outputs"
RAW = BASE / "_lotus_raw"


def main():
    compounds = {}
    by_species_inchikeys = defaultdict(set)
    raw_files = sorted(RAW.glob("*.json"))
    total_records = 0

    for f in raw_files:
        try:
            d = json.loads(f.read_text())
        except Exception as e:
            print(f"skip {f.name}: parse error {e}")
            continue
        nps = d.get("naturalProducts", []) if isinstance(d, dict) else []
        for c in nps:
            ik = c.get("inchikey") or c.get("inchikey2D") or c.get("lotus_id")
            if not ik:
                continue
            total_records += 1
            if ik not in compounds:
                compounds[ik] = {
                    "inchikey": c.get("inchikey", ""),
                    "inchikey2D": c.get("inchikey2D", ""),
                    "lotus_id": c.get("lotus_id", ""),
                    "name": c.get("traditional_name") or c.get("iupac_name", "")[:100],
                    "molecular_formula": c.get("molecular_formula", ""),
                    "molecular_weight": c.get("molecular_weight"),
                    "smiles": c.get("smiles", ""),
                    "wikidata_id": c.get("wikidata_id", ""),
                    "species": set(),
                }
            orgs = c.get("organisms", []) or c.get("taxa", [])
            attached = False
            for org in orgs:
                sp = None
                if isinstance(org, dict):
                    sp = org.get("name") or org.get("scientificName") or org.get("organism")
                elif isinstance(org, str):
                    sp = org
                if sp and isinstance(sp, str):
                    compounds[ik]["species"].add(sp)
                    by_species_inchikeys[sp].add(ik)
                    attached = True
            if not attached:
                query_hint = f.stem.replace("_", " ")
                compounds[ik]["species"].add(f"[query-hint] {query_hint}")
                by_species_inchikeys[f"[query-hint] {query_hint}"].add(ik)

    for ik, c in compounds.items():
        c["species"] = sorted(c["species"])

    species_counts = {sp: len(iks) for sp, iks in by_species_inchikeys.items()}
    sorted_species = sorted(species_counts.items(), key=lambda x: -x[1])

    result = {
        "_meta": {
            "date": "2026-05-06",
            "phase": "2b",
            "source": "LOTUS REST API (https://lotus.naturalproducts.net/api/search/simple)",
            "queries_run": len(raw_files),
            "total_records_seen": total_records,
            "unique_compounds_by_inchikey": len(compounds),
            "unique_species_attributions": len(by_species_inchikeys),
        },
        "_summary": {
            "top_30_species_by_compound_count": dict(sorted_species[:30]),
        },
        "by_species": {sp: sorted(list(iks))[:200] for sp, iks in by_species_inchikeys.items()},
        "compound_count_by_species": dict(sorted_species),
    }

    (BASE / "phase-2b-lotus-fungal-compounds.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False)
    )
    (BASE / "phase-2b-compounds-by-inchikey.json").write_text(
        json.dumps(compounds, indent=2, ensure_ascii=False)
    )

    md = ["# Phase 2b — LOTUS fungal-compound aggregation", ""]
    md.append("**Source:** LOTUS REST API (https://lotus.naturalproducts.net/api/search/simple)")
    md.append("**Date:** 2026-05-06")
    md.append(f"**Queries run:** {len(raw_files)} fungal genera/species")
    md.append(f"**Total records seen:** {total_records:,}")
    md.append(f"**Unique compounds (by InChIKey):** {len(compounds):,}")
    md.append(f"**Unique species/taxa with compound attributions:** {len(by_species_inchikeys):,}")
    md.append("")
    md.append("## Top 30 species by compound count")
    md.append("")
    md.append("| Rank | Species/taxon | Compound count |")
    md.append("|---:|---|---:|")
    for i, (sp, n) in enumerate(sorted_species[:30], 1):
        md.append(f"| {i} | *{sp}* | {n:,} |")
    md.append("")
    md.append("## Notable findings")
    md.append("")
    md.append("- The `[query-hint]` prefixed records are compounds where LOTUS did not attach explicit organism metadata in the search/simple response; we attribute by the query name. To upgrade these to canonical species attributions, query the per-compound LOTUS endpoint or use the LOTUS Zenodo bulk dump.")
    md.append("- Per-InChIKey full compound table at `phase-2b-compounds-by-inchikey.json` — Phase 3 target mapping reads from this.")
    md.append("- Phase 5 anchor sanity-check: every species in `phase-5-anchor-species.json` should appear with non-zero compound count. Verify before promoting Phase 2 to complete.")
    md.append("")
    md.append("## Caveats")
    md.append("")
    md.append("- LOTUS aggregates upstream sources (NPAtlas, Wikidata-fed, etc.); some compounds may have weak species-of-origin evidence in the underlying primary literature.")
    md.append("- 200-records-per-query limit may have truncated very-rich species (Ganoderma lucidum returned 28MB raw, suggesting query saturation).")
    md.append("- No toxicity filter applied yet — that's the next discrete step (apply toxicity-filter.json to the species list).")
    md.append("- KNApSAcK / NPASS / TCMSP / HIT pulls not yet executed — LOTUS-only result is one slice of the breadth pass; the East-Asian-hosted DBs likely surface additional species and compounds beyond what LOTUS captures.")
    md.append("")

    (BASE / "phase-2b-lotus-fungal-compounds.md").write_text("\n".join(md))

    print(f"Wrote: {BASE / 'phase-2b-lotus-fungal-compounds.json'}")
    print(f"Wrote: {BASE / 'phase-2b-compounds-by-inchikey.json'}")
    print(f"Wrote: {BASE / 'phase-2b-lotus-fungal-compounds.md'}")
    print(f"\nTotal: {total_records:,} records, {len(compounds):,} unique compounds, {len(by_species_inchikeys):,} unique species")


if __name__ == "__main__":
    main()
