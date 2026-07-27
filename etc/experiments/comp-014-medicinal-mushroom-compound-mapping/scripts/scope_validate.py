"""
comp-014 Phase 1 scope validation.

Validates the input JSON files are well-formed and emits outputs/scope-summary.md.
Stdlib only — no DB calls, no network, no external packages.

This is the only retained runnable script. Its purpose is to:
1. Sanity-check the scope JSONs parse and have the expected structure.
2. Emit a human-readable summary of the retained scope.
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
        issues.append("phase-5-anchor-species.json missing 'candidates' array")
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
    rendered_chokepoints = [
        (name, cp)
        for name, cp in chokepoints["chokepoints"].items()
        if not name.startswith("_")
    ]
    proposed_chokepoints = [
        (name, cp)
        for name, cp in chokepoints["chokepoints"].items()
        if name.startswith("_PROPOSED")
    ]
    n_chokepoints = len(rendered_chokepoints)

    n_compound_dbs = len(sources["compound_databases"])
    n_bioactivity_dbs = len(sources["bioactivity_target_databases"])
    n_lit_corpora = len(sources["literature_corpora"])

    lines = []
    lines.append("# comp-014 — Medicinal Mushroom Compound × Chokepoint Mapping")
    lines.append("")
    lines.append(
        "**Status:** Breadth aggregation and target mapping are retained as a "
        "lead inventory. Historical rank and priority fields have no current "
        "decision authority; the former Phase 6 occupancy/feasibility triage is retired."
    )
    lines.append("")
    lines.append("## Inventory")
    lines.append("")
    lines.append(f"- **Phase 5 anchor species (sanity-check):** {n_species}")
    lines.append(f"- **Rendered historical target entries:** {n_chokepoints}")
    lines.append(f"- **Compound databases recorded:** {n_compound_dbs}")
    lines.append(f"- **Bioactivity / target databases recorded:** {n_bioactivity_dbs}")
    lines.append(f"- **Multilingual literature corpora recorded:** {n_lit_corpora}")
    lines.append("")
    lines.append("## Historical anchor species (sanity-check set, not priorities)")
    lines.append("")
    for c in species["candidates"]:
        lines.append(f"- *{c['scientific']}* ({c.get('common_name', '—')})")
    lines.append("")
    lines.append("## Chokepoint targets")
    lines.append("")
    lines.append("| Chokepoint | UniProt | Site | Scope rationale |")
    lines.append("|---|---|---|---|")
    for name, cp in rendered_chokepoints:
        uniprot = cp.get("uniprot", "—")
        if uniprot == "—" and "uniprot_oat1" in cp:
            uniprot = f"{cp['uniprot_oat1']} / {cp['uniprot_oat3']}"
        if uniprot == "—" and "uniprot_keap1" in cp:
            uniprot = f"{cp['uniprot_keap1']} / {cp['uniprot_nrf2']}"
        site = cp.get("site", "—")
        scope_rationale = cp.get("rationale", "").replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {name} | {uniprot} | {site} | {scope_rationale} |")
    lines.append("")
    if proposed_chokepoints:
        lines.append("**Proposed (not-yet-canonical):**")
        lines.append("")
        for _, cp in proposed_chokepoints:
            lines.append(f"- **{cp['name']}** — {cp['_status']}")
        lines.append("")
    lines.append("## Recorded phase scope")
    lines.append("")
    plan = sources["phase_plan_summary"]
    for phase_key in sorted(plan.keys()):
        lines.append(f"- **{phase_key}**: {plan[phase_key]}")
    lines.append("")
    lines.append("## Historical data-source inventory")
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
        else:
            lines.append(f"- **{db_name}** — {db}")
    lines.append("")
    lines.append("### Multilingual literature corpora")
    for corp_name, corp in sources["literature_corpora"].items():
        if isinstance(corp, dict):
            lines.append(f"- **{corp_name}** — {corp.get('scope', '')}")
    lines.append("")
    lines.append("## Reproducibility")
    lines.append("")
    lines.append("```bash")
    lines.append("cd wiki/etc/experiments/comp-014-medicinal-mushroom-compound-mapping")
    lines.append("python3 scripts/scope_validate.py")
    lines.append("```")
    lines.append("")
    lines.append(
        "This scope validator checks the current input structure and emits this summary. "
        "It does not reproduce the database pulls, later joins, historical rankings, "
        "or retired Phase 6."
    )
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
    rendered_target_count = sum(
        1 for name in chokepoints["chokepoints"] if not name.startswith("_")
    )
    print(
        f"OK. Validated {len(species['candidates'])} species, "
        f"{rendered_target_count} rendered historical target entries."
    )
    print(f"Wrote {OUTPUTS / 'scope-summary.md'}")


if __name__ == "__main__":
    main()
