#!/usr/bin/env python3
"""
Phase 2 — Sequential Semantic Scholar verification.

Reads a list of candidate (cluster, title) pairs, queries S2 sequentially
(1 QPS rate limit), applies Levenshtein > 0.70 title-match check, requires
non-empty abstract and year <= cutoff_date, and writes verified records
to citation_pool.json.

Run from this workspace dir:
    python3 run_verify.py
"""
import json
import os
import subprocess
import time
from pathlib import Path

try:
    from Levenshtein import ratio
except ImportError:
    from rapidfuzz.distance import Levenshtein
    def ratio(a, b):
        return 1 - Levenshtein.distance(a, b) / max(len(a), len(b), 1)

WORKSPACE = Path(__file__).parent
S2_SCRIPT = Path.home() / "paper-orchestra/skills/literature-review-agent/scripts/s2_search.py"
CUTOFF_YEAR = 2026  # research cutoff per conference_guidelines.md = 2026-05-01

# Candidates: (cluster, query_title)
CANDIDATES = [
    ("multiagent_debate", "Improving Factuality and Reasoning in Language Models through Multiagent Debate"),
    ("self_refine", "Self-Refine: Iterative Refinement with Self-Feedback"),
    ("reflexion", "Reflexion: Language Agents with Verbal Reinforcement Learning"),
    ("llm_jury", "Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models"),
    ("constitutional_ai", "Constitutional AI: Harmlessness from AI Feedback"),
    ("rlaif", "RLAIF: Scaling Reinforcement Learning from Human Feedback with AI Feedback"),
    ("ai_scientist", "The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery"),
    ("ai_scientist_v2", "The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search"),
    ("paper_orchestra", "PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing"),
    ("model_collapse", "AI models collapse when trained on recursively generated data"),
    ("curse_recursion", "The Curse of Recursion: Training on Generated Data Makes Models Forget"),
]

env = os.environ.copy()
env["SSL_CERT_FILE"] = subprocess.check_output(
    ["python3", "-c", "import certifi;print(certifi.where())"], text=True
).strip()


def query_s2(title: str) -> dict | None:
    """Run s2_search.py for one title; return top hit dict or None."""
    result = subprocess.run(
        [
            "python3", str(S2_SCRIPT),
            "--query", title,
            "--fields", "title,abstract,year,authors,venue,externalIds",
            "--limit", "5",
        ],
        capture_output=True, text=True, env=env, timeout=60,
    )
    if result.returncode != 0:
        print(f"WARN: s2 failed for '{title[:60]}': {result.stderr[:200]}")
        return None
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError as e:
        print(f"WARN: bad JSON for '{title[:60]}': {e}")
        return None
    hits = data.get("data") or []
    if not hits:
        print(f"WARN: 0 results for '{title[:60]}'")
        return None
    return hits[0]


def verify(candidate_title: str, hit: dict) -> tuple[bool, str]:
    """Apply paper's verification rules. Returns (ok, reason_if_not)."""
    s2_title = hit.get("title", "")
    r = ratio(candidate_title.lower(), s2_title.lower())
    if r < 0.70:
        return False, f"Levenshtein {r:.2f} < 0.70 ({s2_title!r})"
    abstract = hit.get("abstract") or ""
    if not abstract.strip():
        return False, "empty abstract"
    year = hit.get("year")
    if year is None or year > CUTOFF_YEAR:
        return False, f"year {year} > cutoff {CUTOFF_YEAR}"
    return True, ""


def main():
    pool: dict[str, dict] = {}  # paperId -> record
    cluster_map: dict[str, list[str]] = {}

    for i, (cluster, title) in enumerate(CANDIDATES):
        if i > 0:
            time.sleep(1.0)  # 1 QPS
        hit = query_s2(title)
        if hit is None:
            print(f"[{cluster}] MISS (no result)")
            continue
        ok, reason = verify(title, hit)
        if not ok:
            print(f"[{cluster}] REJECTED: {reason}")
            continue
        pid = hit.get("paperId")
        if pid in pool:
            print(f"[{cluster}] DUP (paperId already in pool)")
            cluster_map.setdefault(cluster, []).append(pid)
            continue
        pool[pid] = {
            "paperId": pid,
            "title": hit.get("title"),
            "year": hit.get("year"),
            "venue": hit.get("venue"),
            "authors": [a.get("name") for a in (hit.get("authors") or [])],
            "abstract": (hit.get("abstract") or "")[:500],  # truncate for storage
            "externalIds": hit.get("externalIds", {}),
            "clusters": [cluster],
        }
        cluster_map.setdefault(cluster, []).append(pid)
        print(f"[{cluster}] OK '{hit.get('title','')[:70]}' ({hit.get('year')})")

    # Merge cluster lists into pool records
    for pid, rec in pool.items():
        rec["clusters"] = []
    for cluster, pids in cluster_map.items():
        for pid in pids:
            if pid in pool:
                pool[pid]["clusters"].append(cluster)

    out_path = WORKSPACE / "citation_pool.json"
    out_path.write_text(json.dumps(list(pool.values()), indent=2))
    print(f"\nWrote {len(pool)} verified records to {out_path}")


if __name__ == "__main__":
    main()
