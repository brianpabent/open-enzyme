#!/usr/bin/env python3
"""Retry the 8 papers that hit S2 rate limit, with 8s spacing."""
import json
import os
import subprocess
import time
from pathlib import Path

WORKSPACE = Path(__file__).parent
S2_SCRIPT = Path.home() / "paper-orchestra/skills/literature-review-agent/scripts/s2_search.py"
CUTOFF_YEAR = 2026

# Papers that failed last run plus the self-refine/reflexion/jury we never got
RETRY_CANDIDATES = [
    ("self_refine", "Self-Refine: Iterative Refinement with Self-Feedback"),
    ("reflexion", "Reflexion: Language Agents with Verbal Reinforcement Learning"),
    ("llm_jury", "Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models"),
    ("rlaif", "RLAIF: Scaling Reinforcement Learning from Human Feedback with AI Feedback"),
    ("ai_scientist_v2", "The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search"),
    ("paper_orchestra", "PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing"),
    ("multiagent_debate", "Improving Factuality and Reasoning in Language Models through Multiagent Debate"),
    ("curse_recursion", "The Curse of Recursion: Training on Generated Data Makes Models Forget"),
]

try:
    from Levenshtein import ratio
except ImportError:
    from rapidfuzz.distance import Levenshtein
    def ratio(a, b):
        return 1 - Levenshtein.distance(a, b) / max(len(a), len(b), 1)

env = os.environ.copy()
env["SSL_CERT_FILE"] = subprocess.check_output(
    ["python3", "-c", "import certifi;print(certifi.where())"], text=True
).strip()

# Load existing pool
pool_path = WORKSPACE / "citation_pool.json"
pool_list = json.loads(pool_path.read_text()) if pool_path.exists() else []
pool: dict[str, dict] = {p["paperId"]: p for p in pool_list}

def query_s2(title):
    result = subprocess.run(
        ["python3", str(S2_SCRIPT), "--query", title,
         "--fields", "title,abstract,year,authors,venue,externalIds", "--limit", "5"],
        capture_output=True, text=True, env=env, timeout=120,
    )
    if result.returncode != 0:
        return None, result.stderr[:300]
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        return None, "bad JSON"
    hits = data.get("data") or []
    return (hits[0] if hits else None), None

for i, (cluster, title) in enumerate(RETRY_CANDIDATES):
    if i > 0:
        time.sleep(8.0)  # be polite — 8s between requests
    hit, err = query_s2(title)
    if hit is None:
        print(f"[{cluster}] FAIL: {err}")
        continue
    r = ratio(title.lower(), hit.get("title", "").lower())
    if r < 0.70:
        print(f"[{cluster}] LEV {r:.2f}<0.70 ({hit.get('title','')!r})")
        continue
    if not (hit.get("abstract") or "").strip():
        print(f"[{cluster}] EMPTY ABSTRACT")
        continue
    year = hit.get("year")
    if not year or year > CUTOFF_YEAR:
        print(f"[{cluster}] YEAR {year} > {CUTOFF_YEAR}")
        continue
    pid = hit.get("paperId")
    if pid in pool:
        pool[pid]["clusters"].append(cluster)
        print(f"[{cluster}] DUP merged")
        continue
    pool[pid] = {
        "paperId": pid,
        "title": hit.get("title"),
        "year": year,
        "venue": hit.get("venue"),
        "authors": [a.get("name") for a in (hit.get("authors") or [])],
        "abstract": (hit.get("abstract") or "")[:500],
        "externalIds": hit.get("externalIds", {}),
        "clusters": [cluster],
    }
    print(f"[{cluster}] OK '{hit.get('title','')[:70]}' ({year})")

pool_path.write_text(json.dumps(list(pool.values()), indent=2))
print(f"\nPool now has {len(pool)} verified records")
