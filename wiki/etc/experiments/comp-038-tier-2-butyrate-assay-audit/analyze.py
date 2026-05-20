#!/usr/bin/env python3
"""
comp-038 — Tier 2 butyrate assay audit.

Lightweight OE-native agentic literature-synthesis runner.

Default live workflow for Codex sessions:
- fetch source snapshots locally;
- write a Codex synthesis packet;
- let the current Codex model perform the expensive synthesis in-session.

Optional OpenRouter workflow remains available for external model roles when
explicitly requested.
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR.parent / "lib"))

from agentic_lit_synthesis import (  # noqa: E402
    OpenRouterClient,
    extract_json_object,
    fetch_pubmed_snapshot,
    load_root_dotenv,
    read_json,
    role_model,
    utc_now_iso,
    write_json,
)


INPUTS = SCRIPT_DIR / "inputs"
OUTPUTS = SCRIPT_DIR / "outputs"
QUERY_STRATEGY = INPUTS / "query-strategy.json"
MODEL_CONFIG = INPUTS / "model-config.json"


SYSTEM = """You are working on Open Enzyme, a Phase 0 research-and-design library.
Audience: PhD-level scientists. Be rigorous, source-aware, and direct.
Do not overclaim. Distinguish candidate evidence from verified evidence.
For load-bearing assay claims, PubMed abstracts alone are insufficient:
require full text, protocol PDFs, vendor validation docs, or method-comparison
data before recommending a GREEN verdict."""


def sha256_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def compact_query_plan(query_strategy):
    lines = [query_strategy["scope"], ""]
    for framing in query_strategy["framings"]:
        lines.append(f"{framing['type']}:")
        for query in framing["queries"]:
            lines.append(f"- {query}")
    return "\n".join(lines)


def query_strategy_prompt(query_strategy):
    return f"""Review this butyrate-assay search strategy for blind spots.

Task: identify Tier 2 butyrate quantification assays that can be validated
against Tier 3 GC-MS for stool, serum, breath, and culture-supernatant matrices.

Current query plan:
{compact_query_plan(query_strategy)}

Return JSON only:
{{
  "missing_framings": [
    {{"type": "...", "queries": ["..."], "rationale": "..."}}
  ],
  "high_value_queries": ["..."],
  "likely_false_leads": ["..."],
  "coverage_verdict": "adequate | needs_revision",
  "notes": "short rationale"
}}"""


def synthesis_prompt(query_strategy, query_critique, pubmed_snapshot, trajectory_index):
    return f"""Trajectory {trajectory_index}: run an independent desk-audit plan
for Tier 2 butyrate assay discovery.

Use the committed query plan, PubMed title/abstract snapshot, and your
scientific prior to propose candidate assay classes, exact follow-up searches,
and evidence that must be retrieved before any final verdict. Favor specificity
over prose. Do not treat PubMed abstracts as full-text validation.

Committed query plan:
{json.dumps(query_strategy, indent=2)}

Query-strategy critique:
{json.dumps(query_critique, indent=2)}

PubMed title/abstract snapshot:
{json.dumps(pubmed_snapshot, indent=2)[:50000]}

Return JSON only:
{{
  "trajectory": {trajectory_index},
  "candidate_assays": [
    {{
      "assay_name": "...",
      "assay_class": "colorimetric | enzymatic | breath-hydrogen | electrochemical | other",
      "matrix_compatibility": ["stool", "serum", "culture", "breath"],
      "why_candidate": "...",
      "required_evidence_before_verdict": ["..."],
      "suggested_queries": ["..."],
      "likely_limitations": ["..."],
      "provisional_gc_ms_validation_status": "validated | partial | unvalidated | unknown"
    }}
  ],
  "red_flags": ["..."],
  "trajectory_notes": "..."
}}"""


def candidate_key(candidate):
    text = " ".join([
        candidate.get("assay_name", ""),
        candidate.get("assay_class", ""),
    ]).lower()
    text = "".join(ch if ch.isalnum() else " " for ch in text)
    tokens = [tok for tok in text.split() if tok not in {"assay", "butyrate", "scfa"}]
    return " ".join(tokens[:6]) or candidate.get("assay_name", "").lower()


def reduce_candidates(trajectory_outputs, threshold):
    buckets = {}
    for output in trajectory_outputs:
        trajectory = output["trajectory"]
        for candidate in output.get("candidate_assays", []):
            key = candidate_key(candidate)
            bucket = buckets.setdefault(key, {
                "key": key,
                "assay_name": candidate.get("assay_name", key),
                "assay_class": candidate.get("assay_class", "unknown"),
                "trajectories": [],
                "candidate_records": [],
            })
            bucket["trajectories"].append(trajectory)
            bucket["candidate_records"].append(candidate)

    consensus = [
        bucket for bucket in buckets.values()
        if len(set(bucket["trajectories"])) >= threshold
    ]
    consensus.sort(key=lambda item: (-len(set(item["trajectories"])), item["assay_name"]))
    return consensus, list(buckets.values())


def judge_prompt(consensus_candidates):
    return f"""Rank these consensus-surfaced Tier 2 butyrate assay candidates.

Use pairwise-judgment logic internally. Criteria:
1. Validation against GC-MS or feasibility of direct GC-MS cross-validation.
2. Cost / accessibility / kit availability.
3. Sample-prep complexity.
4. Dynamic range coverage: lumenal 10 uM-100 mM; serum ~1-10 uM;
   culture supernatant 100 uM-50 mM.
5. Matrix fit for OE's likely use cases: stool and culture supernatant.

Important: any GREEN verdict requires full-text/protocol/vendor validation
evidence. If evidence is not yet retrieved, use YELLOW or RED, not GREEN.

Candidates:
{json.dumps(consensus_candidates, indent=2)}

Return JSON only:
{{
  "ranked_candidates": [
    {{
      "rank": 1,
      "assay_name": "...",
      "assay_class": "...",
      "verdict": "GREEN | YELLOW | RED",
      "confidence": "high | medium | low",
      "rationale": "...",
      "must_verify_before_wet_lab": ["..."]
    }}
  ],
  "overall_verdict": "GREEN | YELLOW | RED",
  "limitations": ["..."],
  "recommended_next_step": "..."
}}"""


def write_summary(run_record):
    lines = [
        "# comp-038 — Tier 2 Butyrate Assay Audit",
        "",
        f"**Run timestamp:** {run_record['run']['timestamp_utc']}",
        f"**Mode:** {run_record['run']['mode']}",
        "",
        "## Model Roles",
        "",
    ]
    for role, model in run_record["run"]["models"].items():
        lines.append(f"- **{role}:** `{model}`")
    lines.extend([
        "",
        "## Query-Strategy Critique",
        "",
        f"**Coverage verdict:** {run_record.get('query_critique', {}).get('coverage_verdict', 'not run')}",
        "",
        run_record.get("query_critique", {}).get("notes", "Not run."),
        "",
        "## Consensus Candidates",
        "",
    ])
    for candidate in run_record.get("consensus_candidates", []):
        trajectories = sorted(set(candidate["trajectories"]))
        lines.append(
            f"- **{candidate['assay_name']}** ({candidate['assay_class']}) "
            f"surfaced in {len(trajectories)} trajectories: {trajectories}"
        )

    judged = run_record.get("judgment", {})
    if judged:
        lines.extend(["", "## Ranked Verdict", ""])
        lines.append(f"**Overall verdict:** **{judged.get('overall_verdict', 'UNKNOWN')}**")
        lines.append("")
        for item in judged.get("ranked_candidates", []):
            lines.append(
                f"{item.get('rank')}. **{item.get('assay_name')}** — "
                f"**{item.get('verdict')}** ({item.get('confidence')} confidence). "
                f"{item.get('rationale')}"
            )
        lines.extend(["", "## Limitations", ""])
        for limitation in judged.get("limitations", []):
            lines.append(f"- {limitation}")
        lines.extend(["", "## Recommended Next Step", "", judged.get("recommended_next_step", "")])
    else:
        lines.extend([
            "",
            "## Ranked Verdict",
            "",
            "Not run. Use `python3 analyze.py --prepare-codex` to fetch source snapshots "
            "and write a synthesis packet for Codex, or `python3 analyze.py --run-openrouter` "
            "only when external model spend is intentional.",
        ])

    lines.extend([
        "",
        "## Reproducibility",
        "",
        f"- `query-strategy.json` SHA256: `{run_record['run']['input_sha256']['query_strategy']}`",
        f"- `model-config.json` SHA256: `{run_record['run']['input_sha256']['model_config']}`",
        "- Secret material is not recorded. OpenRouter keys are only needed for `--run-openrouter`.",
        "",
    ])
    (OUTPUTS / "summary.md").write_text("\n".join(lines))


def role_config(model_config, role, openrouter=False):
    """
    Return the config block for a role.

    The default roles describe the no-spend Codex workflow. Explicit
    OpenRouter roles live under *_openrouter names so a local Codex run never
    silently implies an OpenRouter GPT-5.5 call.
    """
    if openrouter:
        openrouter_role = f"{role}_openrouter"
        if openrouter_role in model_config["roles"]:
            return model_config["roles"][openrouter_role]
    return model_config["roles"][role]


def configured_model(model_config, role, openrouter=False):
    wrapper = {"roles": {role: role_config(model_config, role, openrouter=openrouter)}}
    return role_model(wrapper, role)


def build_run_record(mode, query_strategy, model_config):
    use_openrouter_roles = mode == "openrouter"
    models = {
        "query_strategist": configured_model(model_config, "query_strategist", use_openrouter_roles),
        "synthesis": configured_model(model_config, "synthesis", use_openrouter_roles),
        "judge": configured_model(model_config, "judge", use_openrouter_roles),
        "verifier": configured_model(model_config, "verifier", use_openrouter_roles),
    }
    return {
        "run": {
            "timestamp_utc": utc_now_iso(),
            "mode": mode,
            "models": models,
            "parameters": model_config["run"],
            "input_sha256": {
                "query_strategy": sha256_file(QUERY_STRATEGY),
                "model_config": sha256_file(MODEL_CONFIG),
            },
        },
        "query_strategy_scope": query_strategy["scope"],
    }


def write_codex_packet(query_strategy, model_config, run_record, pubmed_snapshot):
    packet_path = OUTPUTS / "codex-synthesis-packet.md"
    lines = [
        "# comp-038 Codex Synthesis Packet",
        "",
        "Use this packet for the primary GPT-5.5/Codex synthesis role without spending OpenRouter tokens.",
        "",
        "## Instructions",
        "",
        SYSTEM,
        "",
        "Run five independent synthesis trajectories mentally/analytically over the query plan and PubMed snapshot. "
        "Surface candidate Tier 2 butyrate assays, collapse consensus candidates, then produce a ranked audit. "
        "Do not assign GREEN unless full text, protocol PDFs, vendor validation docs, or GC-MS comparison data are present.",
        "",
        "Required output shape:",
        "",
        "```json",
        json.dumps({
            "trajectory_outputs": [
                {
                    "trajectory": 1,
                    "candidate_assays": [
                        {
                            "assay_name": "",
                            "assay_class": "",
                            "matrix_compatibility": [],
                            "why_candidate": "",
                            "required_evidence_before_verdict": [],
                            "suggested_queries": [],
                            "likely_limitations": [],
                            "provisional_gc_ms_validation_status": "",
                        }
                    ],
                    "red_flags": [],
                    "trajectory_notes": "",
                }
            ],
            "consensus_candidates": [],
            "ranked_candidates": [],
            "overall_verdict": "GREEN | YELLOW | RED",
            "limitations": [],
            "recommended_next_step": "",
        }, indent=2),
        "```",
        "",
        "## Query Strategy",
        "",
        "```json",
        json.dumps(query_strategy, indent=2),
        "```",
        "",
        "## Model / Protocol Config",
        "",
        "```json",
        json.dumps(model_config, indent=2),
        "```",
        "",
        "## PubMed Snapshot",
        "",
        f"Fetched at: {pubmed_snapshot['fetched_at_utc']}",
        "",
        "```json",
        json.dumps(pubmed_snapshot, indent=2)[:120000],
        "```",
        "",
        "## Run Record",
        "",
        "```json",
        json.dumps(run_record, indent=2),
        "```",
        "",
    ]
    packet_path.write_text("\n".join(lines))
    return packet_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--prepare-codex",
        action="store_true",
        help="Fetch local source snapshots and write a Codex synthesis packet without model API spend.",
    )
    parser.add_argument(
        "--run-openrouter",
        action="store_true",
        help="Call OpenRouter models and spend API budget. Use only when external model roles are intentional.",
    )
    args = parser.parse_args()

    OUTPUTS.mkdir(exist_ok=True)
    load_root_dotenv(SCRIPT_DIR)

    query_strategy = read_json(QUERY_STRATEGY)
    model_config = read_json(MODEL_CONFIG)
    mode = "openrouter" if args.run_openrouter else ("codex-packet" if args.prepare_codex else "dry-run")
    run_record = build_run_record(mode, query_strategy, model_config)

    if not args.prepare_codex and not args.run_openrouter:
        expected = [
            OUTPUTS / "pubmed-snapshot.json",
            OUTPUTS / "codex-synthesis-packet.md",
            OUTPUTS / "results.json",
            OUTPUTS / "summary.md",
        ]
        missing = [path.relative_to(SCRIPT_DIR) for path in expected if not path.exists()]
        if missing:
            print("Dry-run artifact check failed. Missing:")
            for path in missing:
                print(f"- {path}")
            print("Use --prepare-codex to fetch source snapshots without model API spend.")
            sys.exit(1)
        print("Dry-run artifact check passed. Existing outputs preserved.")
        return

    pubmed_snapshot = fetch_pubmed_snapshot(
        query_strategy,
        retmax_per_query=model_config["run"].get("pubmed_retmax_per_query", 10),
    )
    write_json(OUTPUTS / "pubmed-snapshot.json", pubmed_snapshot)
    run_record["pubmed_snapshot"] = {
        "fetched_at_utc": pubmed_snapshot["fetched_at_utc"],
        "retmax_per_query": pubmed_snapshot["retmax_per_query"],
        "record_count": len(pubmed_snapshot["records"]),
        "artifact": "outputs/pubmed-snapshot.json",
    }

    if args.prepare_codex:
        run_record["query_critique"] = {
            "coverage_verdict": "pending_codex_synthesis",
            "notes": "Source packet prepared for Codex/GPT-5.5 in-session synthesis; no OpenRouter model calls made.",
        }
        run_record["consensus_candidates"] = []
        packet_path = write_codex_packet(query_strategy, model_config, run_record, pubmed_snapshot)
        run_record["codex_synthesis_packet"] = str(packet_path.relative_to(SCRIPT_DIR))
        write_json(OUTPUTS / "results.json", run_record)
        write_summary(run_record)
        print(f"Codex packet ready: {packet_path}")
        return

    client = OpenRouterClient(app_title="Open Enzyme comp-038")
    roles = {
        "query_strategist": role_config(model_config, "query_strategist", openrouter=True),
        "synthesis": role_config(model_config, "synthesis", openrouter=True),
        "judge": role_config(model_config, "judge", openrouter=True),
        "verifier": role_config(model_config, "verifier", openrouter=True),
    }

    query_response = client.chat(
        run_record["run"]["models"]["query_strategist"],
        [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": query_strategy_prompt(query_strategy)},
        ],
        temperature=roles["query_strategist"]["temperature"],
    )
    query_critique = extract_json_object(query_response["text"])
    run_record["query_critique"] = query_critique
    run_record["query_response_provenance"] = {
        "response_id": query_response["response_id"],
        "model": query_response["model"],
    }

    trajectory_outputs = []
    trajectories = model_config["run"]["trajectories"]
    for idx in range(1, trajectories + 1):
        response = client.chat(
            run_record["run"]["models"]["synthesis"],
            [
                {"role": "system", "content": SYSTEM},
                {"role": "user", "content": synthesis_prompt(query_strategy, query_critique, pubmed_snapshot, idx)},
            ],
            temperature=roles["synthesis"]["temperature"],
        )
        parsed = extract_json_object(response["text"])
        parsed["response_provenance"] = {
            "response_id": response["response_id"],
            "model": response["model"],
        }
        trajectory_outputs.append(parsed)

    threshold = model_config["run"]["consensus_threshold"]
    consensus, all_buckets = reduce_candidates(trajectory_outputs, threshold)
    run_record["trajectory_outputs"] = trajectory_outputs
    run_record["all_candidate_buckets"] = all_buckets
    run_record["consensus_candidates"] = consensus

    if consensus:
        judge_response = client.chat(
            run_record["run"]["models"]["judge"],
            [
                {"role": "system", "content": SYSTEM},
                {"role": "user", "content": judge_prompt(consensus)},
            ],
            temperature=roles["judge"]["temperature"],
        )
        run_record["judgment"] = extract_json_object(judge_response["text"])
        run_record["judgment_response_provenance"] = {
            "response_id": judge_response["response_id"],
            "model": judge_response["model"],
        }
    else:
        run_record["judgment"] = {
            "overall_verdict": "RED",
            "limitations": ["No candidate met the consensus threshold."],
            "recommended_next_step": "Inspect trajectory outputs and revise query strategy.",
        }

    write_json(OUTPUTS / "results.json", run_record)
    write_summary(run_record)
    print("Live run complete. Wrote outputs/results.json and outputs/summary.md")


if __name__ == "__main__":
    main()
