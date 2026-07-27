#!/usr/bin/env python3
"""comp-004: bounded supplement–ABCG2 assay-evidence audit.

Run from the repository root:
python3 wiki/etc/experiments/comp-004-supplement-abcg2-antagonism/analyze.py
"""

import json
import pathlib


ROOT = pathlib.Path(__file__).parent
INPUT = ROOT / "inputs" / "assay_evidence.json"
OUTPUTS = ROOT / "outputs"

EXPECTED_COMPOUNDS = {"Curcumin", "EGCG", "Quercetin"}
ALLOWED_EVIDENCE_LEVELS = {"In Vitro", "Animal Model", "In Vitro + Animal Model"}
ALLOWED_URATE_STATUSES = {
    "not_established_by_cited_record",
    "direct_intestinal_urate_flux_reported",
}
REQUIRED_FIELDS = {
    "compound",
    "evidence_level",
    "assay_context",
    "reported_substrates",
    "urate_evidence_status",
    "intestinal_model_tested",
    "source",
}


def require_nonempty_string(value, field, compound):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{compound}: {field} must be a non-empty string")
    return value.strip()


def load_records():
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 1:
        raise ValueError("unsupported input schema_version")

    evidence_set = payload.get("evidence_set")
    if not isinstance(evidence_set, dict):
        raise ValueError("evidence_set must be an object")
    for field in ("scope", "cutoff_date", "selection_rule"):
        require_nonempty_string(evidence_set.get(field), f"evidence_set.{field}", "input")

    records = payload.get("records")
    if not isinstance(records, list) or not records:
        raise ValueError("inputs/assay_evidence.json must contain a non-empty records list")

    seen = set()
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("every record must be an object")
        missing = REQUIRED_FIELDS - set(record)
        if missing:
            raise ValueError(
                f"{record.get('compound', '<unnamed>')} missing fields: {sorted(missing)}"
            )

        compound = require_nonempty_string(record["compound"], "compound", "record")
        normalized = compound.casefold()
        if normalized in seen:
            raise ValueError(f"duplicate compound record: {compound}")
        seen.add(normalized)

        evidence_level = require_nonempty_string(
            record["evidence_level"], "evidence_level", compound
        )
        if evidence_level not in ALLOWED_EVIDENCE_LEVELS:
            raise ValueError(f"{compound}: unsupported evidence_level {evidence_level!r}")
        require_nonempty_string(record["assay_context"], "assay_context", compound)

        substrates = record["reported_substrates"]
        if (
            not isinstance(substrates, list)
            or not substrates
            or any(not isinstance(item, str) or not item.strip() for item in substrates)
        ):
            raise ValueError(f"{compound}: reported_substrates must be non-empty strings")

        urate_status = require_nonempty_string(
            record["urate_evidence_status"], "urate_evidence_status", compound
        )
        if urate_status not in ALLOWED_URATE_STATUSES:
            raise ValueError(f"{compound}: unsupported urate_evidence_status {urate_status!r}")
        if not isinstance(record["intestinal_model_tested"], bool):
            raise ValueError(f"{compound}: intestinal_model_tested must be Boolean")

        source = record["source"]
        if not isinstance(source, dict):
            raise ValueError(f"{compound}: source must be an object")
        for field in ("citation", "pmid", "verified_location"):
            require_nonempty_string(source.get(field), f"source.{field}", compound)
        doi = source.get("doi")
        if doi is not None and (not isinstance(doi, str) or not doi.strip()):
            raise ValueError(f"{compound}: source.doi must be null or a non-empty string")

    if {record["compound"] for record in records} != EXPECTED_COMPOUNDS:
        raise ValueError(
            "records must contain exactly: " + ", ".join(sorted(EXPECTED_COMPOUNDS))
        )
    return evidence_set, records


def classify(record):
    """Map each cited record to a bounded evidence disposition."""
    if record["urate_evidence_status"] == "direct_intestinal_urate_flux_reported":
        return {
            **record,
            "disposition": "DIRECT_URATE_EVIDENCE_PRESENT_REVIEW_REQUIRED",
            "disposition_reasons": [
                "the cited record reports direct intestinal urate-flux evidence"
            ],
            "quantitative_risk_rank_allowed": False,
        }

    reasons = ["the cited record does not establish intestinal urate transport"]
    if record["intestinal_model_tested"] is False:
        reasons.append("the cited record does not use an intestinal model")
    reasons.append("the cited record supplies no applicable intestinal-urate parameter")
    return {
        **record,
        "disposition": "DIRECT_INTESTINAL_URATE_FLUX_ASSAY_REQUIRED",
        "disposition_reasons": reasons,
        "quantitative_risk_rank_allowed": False,
    }


def write_summary(output):
    lines = [
        "# comp-004: Supplement–ABCG2 Assay-Evidence Audit",
        "",
        "**Status:** the quantitative gut-lumen occupancy verdict is invalid for biological",
        "or clinical decision use.",
        "",
        "The model compared nominal bulk gut concentrations with ABCG2 IC50 values measured",
        "using drug substrates in other systems, then interpreted the ratio as percent",
        "inhibition of intestinal urate transport. Free segment-resolved exposure, substrate",
        "dependence, intestinal context, and urate flux were not measured. The ratio,",
        "percent-inhibition, and VERY_HIGH risk outputs do not survive.",
        "",
        "## Bounded evidence map",
        "",
        "| Compound | Evidence | Cited-record boundary | Disposition |",
        "|---|---|---|---|",
    ]
    for record in output["records"]:
        disposition = (
            "Direct evidence requires review"
            if record["disposition"] == "DIRECT_URATE_EVIDENCE_PRESENT_REVIEW_REQUIRED"
            else "Direct intestinal urate-flux assay required"
        )
        lines.append(
            f"| {record['compound']} | {record['evidence_level']} | "
            f"{record['assay_context']} | {disposition} |"
        )

    lines += [
        "",
        "## Bounded conclusion",
        "",
        "Within these three cited primary records, quercetin, curcumin, and EGCG each have an",
        "ABCG2/BCRP interaction signal in another experimental context. These records do not",
        "establish a quantitative intestinal urate-transport effect. This is not a literature",
        "census and does not rank intestinal-urate hazard, predict a clinical effect, or identify",
        "a favorable dose, formulation, exposure pattern, or genotype stratum.",
        "",
        "To resolve the question raised by this bounded evidence set, pair measured free parent",
        "compound and metabolites with ABCG2 protein and basolateral-to-apical urate flux across",
        "prespecified exposure times in an intestinal epithelial model.",
        "",
        "## Invalidated uses",
        "",
    ]
    lines.extend(f"- {item}" for item in output["invalidated_scope"])
    OUTPUTS.mkdir(exist_ok=True)
    (OUTPUTS / "summary.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


def main():
    evidence_set, source_records = load_records()
    records = [classify(record) for record in source_records]
    output = {
        "schema_version": 1,
        "experiment": "comp-004",
        "title": "Supplement–ABCG2 Assay-Evidence Audit",
        "status": "QUANTITATIVE_VERDICT_INVALID",
        "allowed_scope": (
            "Qualitative routing from the three cited primary records to a direct "
            "intestinal urate-flux experiment; not a literature census."
        ),
        "evidence_set": evidence_set,
        "decision_rule": (
            "If a cited record does not establish direct intestinal urate flux, route the "
            "compound to that experiment. If it does, stop default routing and require review. "
            "Never calculate percent inhibition, assign a quantitative risk tier, or infer "
            "clinical direction from nominal gut concentration."
        ),
        "invalidated_scope": [
            "The nominal occupancy ratios as biological decision metrics.",
            "The predicted ABCG2-inhibition percentages.",
            "The VERY_HIGH risk labels for quercetin and curcumin.",
            "Any patient, genotype, dosing, formulation, or clinical-risk inference.",
        ],
        "records": records,
    }
    OUTPUTS.mkdir(exist_ok=True)
    (OUTPUTS / "assay_evidence_audit.json").write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    write_summary(output)
    print("comp-004 complete. Bounded qualitative audit outputs written to outputs/.")


if __name__ == "__main__":
    main()
