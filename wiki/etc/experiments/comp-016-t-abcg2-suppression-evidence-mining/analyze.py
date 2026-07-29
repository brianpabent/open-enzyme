#!/usr/bin/env python3
"""Validate and render the fixed COMP-016 evidence inventory."""

import json
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
INPUT_PATH = HERE / "inputs" / "studies.json"
OUTPUT_DIR = HERE / "outputs"

ALLOWED_TEST_CLASSES = {"in_vivo", "in_vitro", "adjacent", "unresolved"}
ALLOWED_OUTCOMES = {"decrease", "increase", "no_difference", "not_tested"}
ALLOWED_VERIFICATION = {
    "primary_full_text",
    "official_publisher_abstract",
    "primary_database_abstract",
    "legacy_search_summary",
    "unresolved_legacy_placeholder",
}
DIRECT_OUTCOME_VERIFICATION = {
    "primary_full_text",
    "official_publisher_abstract",
    "primary_database_abstract",
}


def load_inventory():
    with INPUT_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def validate_inventory(data):
    if data.get("schema_version") != 2:
        raise ValueError("schema_version must equal 2")
    records = data.get("records")
    if not isinstance(records, list) or len(records) != 17:
        raise ValueError("the fixed inventory must contain exactly 17 records")

    seen = set()
    for record in records:
        record_id = record.get("id")
        if not record_id or record_id in seen:
            raise ValueError(f"missing or duplicate record id: {record_id!r}")
        seen.add(record_id)

        test_class = record.get("test_class")
        outcome = record.get("target_outcome")
        verification = record.get("verification_tier")
        if test_class not in ALLOWED_TEST_CLASSES:
            raise ValueError(f"{record_id}: invalid test_class {test_class!r}")
        if outcome not in ALLOWED_OUTCOMES:
            raise ValueError(f"{record_id}: invalid target_outcome {outcome!r}")
        if verification not in ALLOWED_VERIFICATION:
            raise ValueError(
                f"{record_id}: invalid verification_tier {verification!r}"
            )
        for field in (
            "citable",
            "androgen_manipulated",
            "intestinal_abcg2_measured",
            "same_context_target_outcome",
        ):
            if type(record.get(field)) is not bool:
                raise ValueError(f"{record_id}: {field} must be a strict Boolean")
        if test_class in {"in_vivo", "in_vitro"}:
            if not record["androgen_manipulated"]:
                raise ValueError(f"{record_id}: direct test must manipulate androgen")
            if not record["intestinal_abcg2_measured"]:
                raise ValueError(
                    f"{record_id}: direct test must measure intestinal ABCG2"
                )
            if not record["same_context_target_outcome"]:
                raise ValueError(
                    f"{record_id}: direct outcome must be linked to the same "
                    "androgen-manipulation and intestinal-ABCG2 context"
                )
            if not record["citable"]:
                raise ValueError(f"{record_id}: direct test must be citable")
            if verification not in DIRECT_OUTCOME_VERIFICATION:
                raise ValueError(
                    f"{record_id}: {verification!r} cannot support a direct outcome"
                )
            if outcome == "not_tested":
                raise ValueError(f"{record_id}: direct test requires a target outcome")
        else:
            if record["same_context_target_outcome"]:
                raise ValueError(
                    f"{record_id}: adjacent/unresolved record cannot assert a "
                    "same-context target outcome"
                )
            if outcome != "not_tested":
                raise ValueError(
                    f"{record_id}: adjacent/unresolved record cannot carry target outcome"
                )
        if record["citable"] and verification == "unresolved_legacy_placeholder":
            raise ValueError(f"{record_id}: unresolved placeholder cannot be citable")

    return records


def analyze(records):
    direct_in_vivo = [r for r in records if r["test_class"] == "in_vivo"]
    direct_in_vitro = [r for r in records if r["test_class"] == "in_vitro"]
    direct_tests = direct_in_vivo + direct_in_vitro
    direct_suppression = [
        r for r in direct_tests if r["target_outcome"] == "decrease"
    ]
    result_code = (
        "DIRECT_SUPPRESSION_DEMONSTRATED_IN_FIXED_INVENTORY"
        if direct_suppression
        else "NOT_DEMONSTRATED_IN_FIXED_INVENTORY"
    )
    if direct_suppression:
        bounded_interpretation = (
            "The fixed 17-record inventory contains at least one direct target "
            "test recording decreased intestinal ABCG2 under androgen "
            f"manipulation: {', '.join(r['id'] for r in direct_suppression)}. "
            "This demonstrates suppression only within those recorded model "
            "contexts; it does not establish a physiological human effect, "
            "healthy-human baseline, population rule, or literature-wide result."
        )
        scope_conclusion = (
            "The result can support only a direct-suppression statement within "
            "the identified tested model contexts. It does not establish "
            "physiological-human magnitude or discard the need for direct "
            "apical-protein and urate-flux measurement."
        )
    else:
        bounded_interpretation = (
            "No record in the fixed 17-record inventory demonstrates "
            "androgen-driven intestinal ABCG2 suppression. This does not "
            "establish a universal literature absence, the opposite mechanism, "
            "a healthy-human null, or a male-specific export ceiling."
        )
        scope_conclusion = (
            "The result rejects only use of direct androgen suppression of "
            "intestinal ABCG2 as an established premise from this scan. It "
            "preserves the broader mechanistic question and routes it to a "
            "direct apical-protein and urate-flux measurement."
        )
    return {
        "inventory_size": len(records),
        "citable_records": sum(bool(r["citable"]) for r in records),
        "unresolved_records": [r["id"] for r in records if not r["citable"]],
        "counts_by_test_class": dict(
            sorted(Counter(r["test_class"] for r in records).items())
        ),
        "counts_by_verification_tier": dict(
            sorted(Counter(r["verification_tier"] for r in records).items())
        ),
        "direct_in_vivo_test_ids": [r["id"] for r in direct_in_vivo],
        "direct_in_vitro_test_ids": [r["id"] for r in direct_in_vitro],
        "direct_suppression_ids": [r["id"] for r in direct_suppression],
        "direct_test_outcomes": {
            r["id"]: r["target_outcome"] for r in direct_tests
        },
        "result_code": result_code,
        "bounded_interpretation": bounded_interpretation,
        "scope_conclusion": scope_conclusion,
    }


def build_results(data, records, analysis):
    corrected_findings = [
        {
            "id": record["id"],
            "citation": record["citation"],
            "evidence_level": record["evidence_level"],
            "verification_tier": record["verification_tier"],
            "retained_finding": record["retained_finding"],
            "boundary": record["boundary"],
        }
        for record in records
        if record.get("retained_finding")
    ]
    classifications = [
        {
            "id": record["id"],
            "citation": record["citation"],
            "test_class": record["test_class"],
            "target_outcome": record["target_outcome"],
            "citable": record["citable"],
            "boundary": record["boundary"],
        }
        for record in records
    ]
    return {
        "schema_version": 2,
        "inventory_date": data["inventory_date"],
        "repair_date": data["repair_date"],
        "question": data["question"],
        "decision_rule": data["decision_rule"],
        "analysis": analysis,
        "corrected_source_findings": corrected_findings,
        "record_classifications": classifications,
        "forbidden_inferences": data["forbidden_inferences"],
    }


def render_summary(data, records, analysis):
    lines = [
        "# COMP-016 — bounded evidence-inventory result",
        "",
        f"**Inventory date:** {data['inventory_date']}",
        "",
        f"**Result:** `{analysis['result_code']}`",
        "",
        analysis["bounded_interpretation"],
        "",
        "## Direct-test accounting",
        "",
        f"- Fixed inventory: {analysis['inventory_size']} records.",
        f"- Citable records: {analysis['citable_records']}.",
        (
            "- Direct in-vivo androgen × intestinal ABCG2 tests: "
            f"{len(analysis['direct_in_vivo_test_ids'])}."
        ),
        (
            "- Direct in-vitro androgen × intestinal ABCG2 tests: "
            f"{len(analysis['direct_in_vitro_test_ids'])}"
            + (
                f" ({', '.join(analysis['direct_in_vitro_test_ids'])})."
                if analysis["direct_in_vitro_test_ids"]
                else "."
            )
        ),
        (
            "- Direct tests recording intestinal ABCG2 decrease: "
            f"{len(analysis['direct_suppression_ids'])}."
        ),
        "",
        "### Direct-test records",
        "",
    ]
    direct_records = [
        record
        for record in records
        if record["test_class"] in {"in_vivo", "in_vitro"}
    ]
    if direct_records:
        for record in direct_records:
            lines.append(
                f"- **{record['id']} — {record['citation']}**: "
                f"`{record['target_outcome']}` in `{record['test_class']}`. "
                f"{record['boundary']}"
            )
    else:
        lines.append("- None.")
    lines.extend(["", "## Corrected source anchors", ""])
    for record in records:
        if record.get("retained_finding"):
            lines.extend(
                [
                    f"- **{record['id']} — {record['citation']}** "
                    f"({record['evidence_level']}; "
                    f"`{record['verification_tier']}`): "
                    f"{record['retained_finding']} **Boundary:** "
                    f"{record['boundary']}",
                ]
            )

    lines.extend(
        [
            "",
            "## Complete fixed-inventory classification",
            "",
            "| ID | Citation | Test class | Direct target outcome | "
            "Verification | Boundary |",
            "|---|---|---|---|---|---|",
        ]
    )
    for record in records:
        citation = record["citation"].replace("|", "/")
        boundary = record["boundary"].replace("|", "/")
        lines.append(
            f"| {record['id']} | {citation} | {record['test_class']} | "
            f"{record['target_outcome']} | {record['verification_tier']} | "
            f"{boundary} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation boundary",
            "",
            "Adjacent human hormone/urate cohorts remain relevant to the broader "
            "androgen–urate prior, but they do not isolate intestinal ABCG2. "
            "Animal genotype effects, healthy-rat baseline comparisons, renal "
            "transporter studies, and non-intestinal cancer-cell mechanisms "
            "remain separate contexts.",
            "",
            analysis["scope_conclusion"],
            "",
            "## Forbidden inferences",
            "",
        ]
    )
    lines.extend(f"- {item}" for item in data["forbidden_inferences"])
    lines.extend(
        [
            "",
            "## Reproduction boundary",
            "",
            "`analyze.py` performs no retrieval. A new search, newly identified "
            "study, or changed source classification requires a new reviewed "
            "result-bearing lifecycle.",
            "",
        ]
    )
    return "\n".join(lines)


def main():
    data = load_inventory()
    records = validate_inventory(data)
    analysis = analyze(records)
    results = build_results(data, records, analysis)
    summary = render_summary(data, records, analysis)

    OUTPUT_DIR.mkdir(exist_ok=True)
    with (OUTPUT_DIR / "results.json").open(
        "w", encoding="utf-8", newline="\n"
    ) as handle:
        json.dump(results, handle, indent=2, ensure_ascii=False, sort_keys=True)
        handle.write("\n")
    with (OUTPUT_DIR / "summary.md").open(
        "w", encoding="utf-8", newline="\n"
    ) as handle:
        handle.write(summary)

    print(f"result_code={analysis['result_code']}")
    print(f"inventory_size={analysis['inventory_size']}")
    print(f"direct_in_vivo={len(analysis['direct_in_vivo_test_ids'])}")
    print(f"direct_in_vitro={len(analysis['direct_in_vitro_test_ids'])}")
    print(f"direct_suppression={len(analysis['direct_suppression_ids'])}")


if __name__ == "__main__":
    main()
