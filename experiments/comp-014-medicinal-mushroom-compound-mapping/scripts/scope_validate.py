"""
comp-014 Phase 1 scope validation.

Validates the input JSON files are well-formed and emits outputs/scope-summary.md.
Stdlib only — no DB calls, no network, no external packages.

Phase 2+ will replace this with actual aggregation scripts. This script's purpose is to:
1. Sanity-check the scope JSONs parse and have the expected structure.
2. Emit a human-readable summary of what the experiment will do.
3. Serve as the reproducibility entry point: `python3 scope_validate.py` from the
   experiment folder produces the scope-summary.md artifact.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INPUTS = ROOT / "inputs"
OUTPUTS = ROOT / "outputs"


def load_json(path: Path):
    with path.open() as f:
        return json.load(f)


def validate_data_sources(d: dict) -> list[str]:
    issues = []
    for required_section in ("compound_databases", "bioactivity_target_databases", "literature_corpora", "phase_plan_summary"):
        if required_section not in d:
            issues.append(f"data-sources.json missing section: {required_section}")
    return issues


def validate_candidate_species(d: dict) -> list[str]:
    issues = []
    if "candidates" not in d:
        issues.append("candidate-species.json missing 'candidates' array")
        return issues
    for c in d["candidates"]:
        for required_field in ("scientific", "compound_classes_known", "rationale", "regulatory_class"):
            if required_field not in c:
                issues.append(f"candidate {c.get('scientific', '<unknown>')} missing field: {required_field}")
    return issues


def validate_chokepoint_targets(d: dict) -> list[str]:
    issues = []
    if "chokepoints" not in d:
        issues.append("chokepoint-targets.json missing 'chokepoints' object")
        return issues
    for name, cp in d["chokepoints"].items():
        if not isinstance(cp, dict):
            issues.append(f"chokepoint {name} is not an object")
            continue
        # Proposed chokepoints use rationale_for_inclusion; canonical use rationale.
        if "rationale" not in cp and "rationale_for_inclusion" not in cp:
            issues.append(f"chokepoint {name} missing 'rationale' or 'rationale_for_inclusion'")
    return issues


def render_summary(sources: dict, species: dict, chokepoints: dict) -> str:
    n_species = len(species["candidates"])
    n_chokepoints = len(chokepoints["chokepoints"])
    proposed_chokepoint_count = sum(1 for k in chokepoints["chokepoints"] if k.startswith("_PROPOSED"))

    n_compound_dbs = len(sources["compound_databases"])
    n_bioactivity_dbs = len(sources["bioactivity_target_databases"])
    n_lit_corpora = len(sources["literature_corpora"])

    lines = []
    lines.append("# comp-014 — Medicinal Mushroom Compound × Chokepoint Mapping")
    lines.append("")
    lines.append("**Status:** Phase 1 scope complete; Phase 2 starting.")
    lines.append("")
    lines.append("## Inventory")
    lines.append("")
    lines.append(f"- **Phase 5 anchor species (sanity-check):** {n_species}")
    lines.append(f"- **Open Enzyme chokepoint targets:** {n_chokepoints} ({proposed_chokepoint_count} proposed, not-yet-canonical)")
    lines.append(f"- **Compound databases planned:** {n_compound_dbs}")
    lines.append(f"- **Bioactivity / target databases planned:** {n_bioactivity_dbs}")
    lines.append(f"- **Multilingual literature corpora planned:** {n_lit_corpora}")
    lines.append("")
    lines.append("## Phase 5 anchor species (NOT the breadth gate — sanity-check only)")
    lines.append("")
    for c in species["candidates"]:
        flag = ""
        if c.get("redox_chokepoint_relevance") == "primary":
            flag = " — **redox chokepoint primary**"
        elif c.get("redox_chokepoint_relevance") == "secondary":
            flag = " — redox chokepoint secondary"
        lines.append(f"- *{c['scientific']}* ({c.get('common_name', '—')}){flag}")
    lines.append("")
    lines.append("## Chokepoint targets")
    lines.append("")
    lines.append("| Chokepoint | UniProt | Site | Priority signal |")
    lines.append("|---|---|---|---|")
    for name, cp in chokepoints["chokepoints"].items():
        if name.startswith("_"):
            continue
        uniprot = cp.get("uniprot", "—")
        if uniprot == "—" and "uniprot_oat1" in cp:
            uniprot = f"{cp['uniprot_oat1']} / {cp['uniprot_oat3']}"
        if uniprot == "—" and "uniprot_keap1" in cp:
            uniprot = f"{cp['uniprot_keap1']} / {cp['uniprot_nrf2']}"
        site = cp.get("site", "—")
        rationale = cp.get("rationale", "")
        # Truncate rationale to one sentence
        priority = rationale.split(".")[0] + "." if rationale else ""
        lines.append(f"| {name} | {uniprot} | {site} | {priority} |")
    lines.append("")
    lines.append("**Proposed (not-yet-canonical):**")
    lines.append("")
    for name, cp in chokepoints["chokepoints"].items():
        if not name.startswith("_PROPOSED"):
            continue
        lines.append(f"- **{cp['name']}** — {cp['_status']}")
    lines.append("")
    lines.append("## Phase plan")
    lines.append("")
    plan = sources["phase_plan_summary"]
    for phase_key in sorted(plan.keys()):
        lines.append(f"- **{phase_key}**: {plan[phase_key]}")
    lines.append("")
    lines.append("## Data sources (Phase 2-5 access plan)")
    lines.append("")
    lines.append("### Compound databases")
    for db_name, db in sources["compound_databases"].items():
        if isinstance(db, dict):
            lines.append(f"- **{db_name}** — {db.get('scope', '')}")
    lines.append("")
    lines.append("### Bioactivity / target databases")
    for db_name, db in sources["bioactivity_target_databases"].items():
        if isinstance(db, dict):
            lines.append(f"- **{db_name}** — {db.get('scope', '')}")
    lines.append("")
    lines.append("### Multilingual literature corpora")
    for corp_name, corp in sources["literature_corpora"].items():
        if isinstance(corp, dict):
            lines.append(f"- **{corp_name}** — {corp.get('scope', '')}")
    lines.append("")
    lines.append("## Reproducibility")
    lines.append("")
    lines.append("```bash")
    lines.append("cd experiments/comp-014-medicinal-mushroom-compound-mapping")
    lines.append("python3 scripts/scope_validate.py")
    lines.append("```")
    lines.append("")
    lines.append("Phase 2+ will add per-phase scripts. This Phase 1 script validates inputs and emits this summary.")
    lines.append("")
    return "\n".join(lines)


def main():
    sources = load_json(INPUTS / "data-sources.json")
    species = load_json(INPUTS / "phase-5-anchor-species.json")
    chokepoints = load_json(INPUTS / "chokepoint-targets.json")
    toxicity = load_json(INPUTS / "toxicity-filter.json")

    issues: list[str] = []
    issues += validate_data_sources(sources)
    issues += validate_candidate_species(species)
    issues += validate_chokepoint_targets(chokepoints)
    if "inclusion_lists" not in toxicity or "exclusion_lists" not in toxicity:
        issues.append("toxicity-filter.json missing inclusion_lists or exclusion_lists")

    if issues:
        print("VALIDATION ISSUES:")
        for i in issues:
            print(f"  - {i}")
        raise SystemExit(1)

    OUTPUTS.mkdir(exist_ok=True)
    summary = render_summary(sources, species, chokepoints)
    (OUTPUTS / "scope-summary.md").write_text(summary)
    print(f"OK. Validated {len(species['candidates'])} species, {len(chokepoints['chokepoints'])} chokepoint entries.")
    print(f"Wrote {OUTPUTS / 'scope-summary.md'}")


if __name__ == "__main__":
    main()
