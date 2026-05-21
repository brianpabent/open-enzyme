#!/usr/bin/env python3
"""
comp-039 retrieval driver.

For each candidate's PubMed query frame, run a snapshot retrieval.
For East Asian sources, perform reachability probes via local_curl_fetch and
record provenance, but do not block on full-text fetch — they are evidence
discovery, not the only path to load-bearing evidence.

Writes:
  ../outputs/retrieval-probes.json
  ../outputs/<candidate>-pubmed-snapshot.json
"""

from pathlib import Path
import json
import sys
import time
import urllib.parse

HERE = Path(__file__).resolve().parent
LIB = HERE.parent.parent.parent / "wiki" / "etc" / "experiments" / "lib"
sys.path.insert(0, str(LIB))

from agentic_lit_synthesis import (  # noqa: E402
    fetch_pubmed_snapshot,
    local_curl_fetch,
    read_json,
    utc_now_iso,
    write_json,
)


OUT = HERE.parent / "outputs"
PROBES_RAW = OUT / "retrieval-probes-raw"


def run_probes(plan_artifact, candidate_key):
    """Run lightweight reachability probes on a small number of East Asian queries per candidate."""
    plan = plan_artifact["plan"]
    probes = []
    for framing in plan.get("framings", []):
        language = framing.get("language")
        if language not in ("zh", "ja"):
            continue
        # Hit one CNKI Overseas search URL per Chinese query (max first 4 per candidate)
        if language == "zh":
            queries = framing.get("queries", [])[:4]
            for q in queries:
                url = f"https://oversea.cnki.net/kns8s/defaultresult/index?kw={urllib.parse.quote(q)}"
                try:
                    prov = local_curl_fetch(url, PROBES_RAW, timeout_seconds=60)
                    probes.append({
                        "candidate": candidate_key,
                        "language": "zh",
                        "framing": framing.get("type"),
                        "query": q,
                        "url": url,
                        "ok": True,
                        "body_path": prov["body_path"],
                    })
                except Exception as exc:  # noqa: BLE001
                    probes.append({
                        "candidate": candidate_key,
                        "language": "zh",
                        "framing": framing.get("type"),
                        "query": q,
                        "url": url,
                        "ok": False,
                        "error": str(exc),
                    })
                time.sleep(0.5)
        if language == "ja":
            queries = framing.get("queries", [])[:3]
            for q in queries:
                # J-STAGE article search
                url = f"https://www.jstage.jst.go.jp/result/global/-char/en?globalSearchKey={urllib.parse.quote(q)}"
                try:
                    prov = local_curl_fetch(url, PROBES_RAW, timeout_seconds=60)
                    probes.append({
                        "candidate": candidate_key,
                        "language": "ja",
                        "framing": framing.get("type"),
                        "query": q,
                        "url": url,
                        "ok": True,
                        "body_path": prov["body_path"],
                    })
                except Exception as exc:  # noqa: BLE001
                    probes.append({
                        "candidate": candidate_key,
                        "language": "ja",
                        "framing": framing.get("type"),
                        "query": q,
                        "url": url,
                        "ok": False,
                        "error": str(exc),
                    })
                time.sleep(0.5)
    return probes


def run_pubmed_snapshot(plan_artifact, candidate_key):
    """Run only the Western frames against PubMed (mechanism-name queries).

    Native zh/ja queries are NOT routed through PubMed (zero coverage). They
    are routed through the East Asian academic allowlist via local_curl_fetch.
    """
    plan = plan_artifact["plan"]
    western_strategy = {
        "framings": [f for f in plan.get("framings", []) if f.get("language") == "en"],
    }
    snapshot = fetch_pubmed_snapshot(western_strategy, retmax_per_query=6, pause_seconds=0.34)
    snapshot["candidate"] = candidate_key
    snapshot["created_at_utc"] = utc_now_iso()
    return snapshot


def main():
    plans = read_json(HERE.parent / "inputs" / "per-candidate-query-plan.json")
    all_probes = []
    for candidate_key, payload in plans.items():
        print(f"--- {candidate_key} probes ---")
        probes = run_probes(payload, candidate_key)
        all_probes.extend(probes)
        ok = sum(1 for p in probes if p["ok"])
        print(f"  probes: {ok}/{len(probes)} ok")

        print(f"--- {candidate_key} PubMed snapshot ---")
        snap = run_pubmed_snapshot(payload, candidate_key)
        out_path = OUT / f"{candidate_key}-pubmed-snapshot.json"
        write_json(out_path, snap)
        print(f"  records: {len(snap.get('records', []))}")
        print(f"  wrote: {out_path}")

    write_json(OUT / "retrieval-probes.json", {
        "created_at_utc": utc_now_iso(),
        "probes": all_probes,
    })


if __name__ == "__main__":
    main()
