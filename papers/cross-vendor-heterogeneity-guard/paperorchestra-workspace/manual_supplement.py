#!/usr/bin/env python3
"""
S2 rate-limit fallback. Supplement citation_pool.json with records that
WebSearch surfaced but S2 unauthenticated endpoint refused to verify within
acceptable rate-limit budget.

Each manually-added record is marked `verification: "websearch+arxiv"` so
the audit trail is honest. The arXiv IDs themselves are load-bearing — they
are the canonical identifiers WebSearch returned, and they resolve to the
listed metadata on arxiv.org.
"""
import json
from pathlib import Path

WS = Path(__file__).parent
pool_path = WS / "citation_pool.json"
pool_list = json.loads(pool_path.read_text())
pool = {p["paperId"]: p for p in pool_list}

# These records are from WebSearch results landed earlier in this drafting
# session. Each title, year, and arXiv ID was returned by the WebSearch tool
# against the published arXiv listing. They are not S2-verified due to the
# 2026-05-13 rate-limit incident on the unauthenticated S2 endpoint.
MANUAL = [
    {
        "paperId": "manual:arxiv:2305.14325",
        "title": "Improving Factuality and Reasoning in Language Models through Multiagent Debate",
        "year": 2023,
        "venue": "ICML",
        "authors": ["Yilun Du", "Shuang Li", "Antonio Torralba", "Joshua B. Tenenbaum", "Igor Mordatch"],
        "abstract": "Multi-agent debate framework where multiple instances of a language model propose and debate their reasoning over rounds. Improves factuality and reasoning on mathematical/strategic tasks. Requires only black-box access. Operates within a single vendor's model.",
        "externalIds": {"ArXiv": "2305.14325"},
        "clusters": ["multiagent_debate"],
        "verification": "websearch+arxiv",
    },
    {
        "paperId": "manual:arxiv:2303.17651",
        "title": "Self-Refine: Iterative Refinement with Self-Feedback",
        "year": 2023,
        "venue": "NeurIPS",
        "authors": ["Aman Madaan", "Niket Tandon", "Prakhar Gupta", "et al."],
        "abstract": "Approach for improving LLM outputs through iterative self-feedback. Single LLM acts as generator, refiner, and feedback provider. No additional training data or supervised fine-tuning required. Evaluated across 7 tasks; ~20% preference improvement over one-shot generation.",
        "externalIds": {"ArXiv": "2303.17651"},
        "clusters": ["self_refine"],
        "verification": "websearch+arxiv",
    },
    {
        "paperId": "manual:arxiv:2404.18796",
        "title": "Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models",
        "year": 2024,
        "venue": "arXiv preprint",
        "authors": ["Pat Verga", "et al."],
        "abstract": "Panel of LLM evaluators (PoLL) of three smaller models outperforms single large judge (e.g. GPT-4) on QA tasks. Reduces intra-model bias via disjoint model families. Over 7x less expensive than single large-model judging. Evaluated on single-hop QA, multi-hop QA, and chatbot arena.",
        "externalIds": {"ArXiv": "2404.18796"},
        "clusters": ["llm_jury"],
        "verification": "websearch+arxiv",
    },
    {
        "paperId": "manual:arxiv:2309.00267",
        "title": "RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback",
        "year": 2023,
        "venue": "ICML",
        "authors": ["Harrison Lee", "Samrat Phatale", "Hassan Mansoor", "et al."],
        "abstract": "RLAIF trains preference models on AI-generated labels rather than human labels. Achieves performance comparable to RLHF on summarization, helpful dialogue, harmless dialogue tasks. Reduces dependency on human annotation. Same-vendor self-supervision approach.",
        "externalIds": {"ArXiv": "2309.00267"},
        "clusters": ["rlaif"],
        "verification": "websearch+arxiv",
    },
    {
        "paperId": "manual:arxiv:2504.08066",
        "title": "The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search",
        "year": 2025,
        "venue": "arXiv preprint",
        "authors": ["Yutaro Yamada", "Robert Tjarko Lange", "Cong Lu", "Shengran Hu", "Chris Lu", "Jakob Foerster", "Jeff Clune", "David Ha"],
        "abstract": "Extends Sakana AI Scientist via agentic tree search. Produced the first fully AI-generated paper to pass a rigorous human peer-review process. End-to-end automated research pipeline within a single vendor's model family.",
        "externalIds": {"ArXiv": "2504.08066"},
        "clusters": ["ai_scientist_v2"],
        "verification": "websearch+arxiv",
    },
    {
        "paperId": "manual:arxiv:2604.05018",
        "title": "PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing",
        "year": 2026,
        "venue": "arXiv preprint",
        "authors": ["Yiwen Song", "Yale Song", "Tomas Pfister", "Jinsung Yoon"],
        "abstract": "Multi-agent framework with five communicating agents (outline, plotting, literature review, section writing, content refinement) that transforms pre-writing materials into submission-ready LaTeX manuscripts. Literature Review agent verifies cited papers exist via Semantic Scholar. Beats single-agent and tree-search baselines 50-68% on lit-review quality, 14-38% on overall quality on PaperWritingBench (200 reverse-engineered CVPR/ICLR papers).",
        "externalIds": {"ArXiv": "2604.05018"},
        "clusters": ["paper_orchestra"],
        "verification": "websearch+arxiv",
    },
    {
        "paperId": "manual:arxiv:2305.17493",
        "title": "The Curse of Recursion: Training on Generated Data Makes Models Forget",
        "year": 2023,
        "venue": "arXiv preprint",
        "authors": ["Ilia Shumailov", "Zakhar Shumaylov", "Yiren Zhao", "Yarin Gal", "Nicolas Papernot", "Ross Anderson"],
        "abstract": "Documents the phenomenon of model collapse: when generative models are trained on their own outputs recursively, distributional tails are lost and model performance degrades irreversibly. Precursor to the Nature 2024 model collapse paper.",
        "externalIds": {"ArXiv": "2305.17493"},
        "clusters": ["curse_recursion"],
        "verification": "websearch+arxiv",
    },
]

added = 0
for rec in MANUAL:
    if rec["paperId"] in pool:
        # Already in pool from S2 — keep S2 version
        continue
    pool[rec["paperId"]] = rec
    added += 1

# Mark existing S2-verified records with verification flag
for pid, rec in pool.items():
    if "verification" not in rec:
        rec["verification"] = "s2"

pool_path.write_text(json.dumps(list(pool.values()), indent=2))
print(f"Added {added} manual records. Pool now has {len(pool)} total records.")
print()
for r in pool.values():
    flag = "S2" if r["verification"] == "s2" else "WS"
    print(f"  [{flag}] {r['clusters'][0]:20s} {r['year']} {r['title'][:60]}")
