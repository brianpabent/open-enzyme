#!/usr/bin/env python3
"""Build the corrected COMP-017 qualitative evidence-audit outputs.

This run did not extract healthy-human, sex-stratified intestinal ABCG2 values
from GTEx or HPA. It therefore cannot test the preregistered 1.5-fold Part A
threshold. The executable work is limited to deterministic schema validation,
source-boundary classification, and rendering of the committed evidence
extracts.

The legacy input filename and ``full_text_extract`` field are retained for
checkout compatibility. Each record carries its own verification tier.
"""

import json
from collections import OrderedDict
from pathlib import Path


HERE = Path(__file__).resolve().parent
INPUTS = HERE / "inputs"
OUTPUTS = HERE / "outputs"
PART_A_THRESHOLD_FOLD = 1.5
EXPECTED_PAPER_IDS = ("P01", "P02", "P03", "P04")
ALLOWED_EVIDENCE_LEVELS = {
    "Animal Model",
    "In Vitro",
    "Mechanistic Extrapolation",
}


def load_json(name):
    with (INPUTS / name).open(encoding="utf-8") as handle:
        return json.load(handle)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def aggregate_part_a(gtex, hpa):
    """Report whether the direct healthy-human question can be tested."""
    gtex_values = gtex.get("raw_per_tissue_sex_stratified_TPM")
    hpa_result = hpa.get("sex_stratified_protein_data_at_this_tier", {}).get(
        "result"
    )
    require(gtex.get("status") == "NOT EXTRACTED", "GTEx status drift")
    require(gtex_values is None, "GTEx values require a new reviewed model")
    require(
        bool(gtex.get("original_run_access_note")),
        "missing original GTEx access trace",
    )
    require(hpa.get("status") == "NOT EXTRACTED", "HPA status drift")
    require(
        hpa_result == "NOT DIRECTLY EXTRACTED",
        "HPA values require a new reviewed model",
    )

    return OrderedDict(
        [
            ("decision_threshold_fold", PART_A_THRESHOLD_FOLD),
            ("gtex_direct_sex_stratified_values", gtex_values),
            ("hpa_direct_sex_stratified_protein", hpa_result),
            ("direct_values_available", False),
            ("decision", "DIRECT_HUMAN_BASELINE_UNRESOLVED"),
            (
                "reason",
                "No healthy-human, sex-stratified intestinal ABCG2 values "
                "were extracted; the 1.5-fold population threshold was not tested.",
            ),
            ("original_run_access_note", gtex["original_run_access_note"]),
            (
                "qualitative_context",
                "Rat intestinal baseline evidence and adjacent-tissue or disease-state "
                "evidence may motivate a human analysis, but cannot substitute for it.",
            ),
        ]
    )


def aggregate_part_b(source_extracts):
    """Normalize the four committed source records without upgrading provenance."""
    table = []
    papers = source_extracts.get("papers")
    require(isinstance(papers, list), "papers must be a list")
    ids = tuple(paper.get("id") for paper in papers)
    require(ids == EXPECTED_PAPER_IDS, f"expected paper IDs {EXPECTED_PAPER_IDS}")

    for paper in papers:
        require(bool(paper.get("verification_tier")), f"{paper['id']} missing tier")
        require(
            paper.get("evidence_level") in ALLOWED_EVIDENCE_LEVELS,
            f"{paper['id']} invalid evidence level",
        )
        extract = paper.get("full_text_extract", {})
        require(bool(extract.get("method")), f"{paper['id']} missing method")
        require(
            bool(extract.get("exact_quantitative_findings")),
            f"{paper['id']} missing findings",
        )
        difference = paper.get("abstract_vs_fulltext_difference")
        require(
            isinstance(difference, list) and difference,
            f"{paper['id']} missing correction notes",
        )

        table.append(
            OrderedDict(
                [
                    ("id", paper["id"]),
                    ("study", paper.get("study")),
                    ("title", paper.get("title")),
                    ("journal", paper.get("journal")),
                    ("year", paper.get("year")),
                    ("pmid", paper.get("pmid")),
                    ("doi", paper.get("doi")),
                    ("verification_tier", paper["verification_tier"]),
                    ("evidence_level", paper["evidence_level"]),
                    ("method_described", extract.get("method")),
                    (
                        "key_reported_findings",
                        extract.get("exact_quantitative_findings", []),
                    ),
                    ("correction_or_gain", difference),
                    ("scope_notes", paper.get("scope_notes", [])),
                ]
            )
        )

    return table


def assemble_evidence_boundaries(source_extracts):
    """Load the single input-owned boundary set and fail closed on schema drift."""
    boundaries = source_extracts.get("evidence_boundaries")
    require(isinstance(boundaries, list) and boundaries, "missing boundaries")
    for index, boundary in enumerate(boundaries):
        require(bool(boundary.get("question")), f"boundary {index} missing question")
        require(bool(boundary.get("status")), f"boundary {index} missing status")
        require(bool(boundary.get("boundary")), f"boundary {index} missing text")
        require(
            boundary.get("evidence_level") in ALLOWED_EVIDENCE_LEVELS,
            f"boundary {index} invalid evidence level",
        )
    return boundaries


def assemble_overall_verdict(source_extracts):
    synthesis = source_extracts.get("cross_paper_synthesis", {})
    require(
        synthesis.get("direct_human_baseline", "").startswith("UNRESOLVED:"),
        "direct-human boundary drift",
    )
    require(
        synthesis.get("evidence_level") == "Mechanistic Extrapolation",
        "qualitative prior must be Mechanistic Extrapolation",
    )
    return {
        "code": "DIRECT_HUMAN_BASELINE_UNRESOLVED",
        "label": (
            "Direct healthy-human intestinal ABCG2 sex-stratification remains unresolved"
        ),
        "rationale": (
            "The run extracted no sex-stratified GTEx intestinal distribution and no "
            "sex-stratified HPA intestinal protein values, so it did not test the "
            "preregistered 1.5-fold population threshold."
        ),
        "qualitative_prior": synthesis["qualitative_prior"],
        "qualitative_prior_evidence_level": synthesis["evidence_level"],
    }


def build_summary_md(results):
    lines = [
        f"# {results['title']}",
        "",
        f"**Experiment:** {results['experiment_id']}  ",
        f"**Original extraction:** {results['original_extraction_date']}  ",
        f"**Correction verification and artifact run:** {results['correction_verification_date']}  ",
        f"**Output schema:** {results['schema_version']}  ",
        "",
        "## Verdict",
        "",
        f"**{results['overall_verdict']['label']}.**",
        "",
        results["overall_verdict"]["rationale"],
        "",
        (
            f"**{results['overall_verdict']['qualitative_prior_evidence_level']}:** "
            f"{results['overall_verdict']['qualitative_prior']}"
        ),
        "",
        "## Part A — direct healthy-human dataset question",
        "",
        (
            f"- **Decision rule:** test a prespecified "
            f"{results['part_a']['decision_threshold_fold']:.1f}× population difference."
        ),
        f"- **GTEx values extracted:** {results['part_a']['gtex_direct_sex_stratified_values']}",
        f"- **HPA sex-stratified protein:** {results['part_a']['hpa_direct_sex_stratified_protein']}",
        f"- **Decision:** `{results['part_a']['decision']}`",
        f"- **Reason:** {results['part_a']['reason']}",
        f"- **Original access trace:** {results['part_a']['original_run_access_note']}",
        "",
        "## Part B — four-paper mixed-tier evidence correction",
        "",
        "| ID | Evidence | Source | Correction or scope gain |",
        "|---|---|---|---|",
    ]

    for row in results["part_b"]:
        notes = row.get("correction_or_gain", [])
        note = notes[0] if notes else "No additional correction recorded."
        if len(note) > 240:
            note = note[:237] + "..."
        cite = f"{row.get('study')} — {row.get('journal')}"
        lines.append(
            f"| {row['id']} | **{row['evidence_level']}** | {cite} | {note} |"
        )

    lines.extend(["", "### Source-specific extracts", ""])
    for row in results["part_b"]:
        lines.extend(
            [
                f"#### {row['id']} — {row.get('study')}",
                "",
                f"- **Title:** {row.get('title')}",
                f"- **PMID:** {row.get('pmid') or '—'}; **DOI:** {row.get('doi') or '—'}",
                f"- **Evidence level:** **{row.get('evidence_level')}**",
                f"- **Verification tier:** {row.get('verification_tier')}",
                f"- **Method described:** {row.get('method_described') or '—'}",
                "",
                "**Reported findings retained in the committed extract:**",
            ]
        )
        for finding in row.get("key_reported_findings", []):
            lines.append(f"- {json.dumps(finding, ensure_ascii=False)}")
        lines.extend(["", "**Correction or scope gain:**"])
        for note in row.get("correction_or_gain", []):
            lines.append(f"- {note}")
        lines.extend(["", "**Scope notes:**"])
        for note in row.get("scope_notes", []):
            lines.append(f"- {note}")
        lines.append("")

    lines.extend(["## Evidence boundaries", ""])
    for boundary in results["evidence_boundaries"]:
        lines.extend(
            [
                f"### {boundary['question']}",
                "",
                f"- **Status:** `{boundary['status']}`",
                f"- **Evidence level:** **{boundary['evidence_level']}**",
                f"- **Boundary:** {boundary['boundary']}",
                "",
            ]
        )

    lines.extend(
        [
            "## Reproduction boundary",
            "",
            (
                "This script deterministically validates and renders the committed "
                "inputs. It does not retrieve literature, reconstruct missing GTEx/HPA "
                "values, or upgrade any record beyond its stated verification tier."
            ),
            "",
        ]
    )
    return "\n".join(lines)


def main():
    gtex = load_json("gtex_data.json")
    hpa = load_json("hpa_data.json")
    source_extracts = load_json("full_text_extract.json")

    results = OrderedDict(
        [
            ("schema_version", 2),
            (
                "schema_note",
                "Intentional incompatible replacement of the historical COMP-017 output schema.",
            ),
            ("experiment_id", "comp-017"),
            ("title", "Intestinal ABCG2 sex-difference evidence audit"),
            (
                "original_extraction_date",
                source_extracts["original_extraction_date"],
            ),
            (
                "correction_verification_date",
                source_extracts["correction_verification_date"],
            ),
            (
                "artifact_run_date",
                source_extracts["correction_verification_date"],
            ),
            ("overall_verdict", assemble_overall_verdict(source_extracts)),
            ("part_a", aggregate_part_a(gtex, hpa)),
            ("part_b", aggregate_part_b(source_extracts)),
            (
                "evidence_boundaries",
                assemble_evidence_boundaries(source_extracts),
            ),
        ]
    )

    OUTPUTS.mkdir(parents=True, exist_ok=True)
    with (OUTPUTS / "results.json").open("w", encoding="utf-8") as handle:
        json.dump(results, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    with (OUTPUTS / "summary.md").open("w", encoding="utf-8") as handle:
        handle.write(build_summary_md(results))


if __name__ == "__main__":
    main()
