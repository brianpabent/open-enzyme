# Cross-vendor review — deepseek-on-2

**Model requested:** `deepseek/deepseek-v4-pro`
**Model returned:** `deepseek/deepseek-v4-pro-20260423`
**Latency:** 130.9s
**Usage:** {'prompt_tokens': 2569, 'completion_tokens': 6363, 'total_tokens': 8932, 'cost': 0.023263695, 'is_byok': False, 'prompt_tokens_details': {'cached_tokens': 0, 'cache_write_tokens': 0, 'audio_tokens': 0, 'video_tokens': 0}, 'cost_details': {'upstream_inference_cost': 0.023263695, 'upstream_inference_prompt_cost': 0.003907449, 'upstream_inference_completions_cost': 0.019356246}, 'completion_tokens_details': {'reasoning_tokens': 5743, 'image_tokens': 0, 'audio_tokens': 0}}

---

### Catch 1 — §2.5
**Claim under review:**  
> A parallel system, FARS (Fully Automated Research System), deployed publicly for 228 hours in March 2026 and produced 100 short machine-learning papers, optimizing for throughput rather than per-paper rigor.  
(Also the later assertion: “a single-vendor pipeline for FARS.”)

**Verdict:** Rejected  

**Reasoning:**  
No citation is provided for FARS, and the system is not among the 11 S2-verified papers. The specific details (228‑hour deployment, 100 papers) strongly suggest a model hallucination. A claim about an existing system of this nature cannot stand without a verifiable reference.  

**Suggested correction:**  
Drop the FARS sentence entirely, or supply a verified citation with the same level of support as the other referenced systems. If the system is real, the reference must be added to the citation pool and verified.

---

### Catch 2 — §2.5
**Claim under review:**  
> Yamada et al. (2025) extended the system with agentic tree search and reported the first fully AI-generated paper to pass workshop-level human peer review.

**Verdict:** Push-back  

**Reasoning:**  
The original AI Scientist (Lu et al. 2024) already reports AI-generated papers being accepted at a workshop-level venue (ICLR 2025 Tiny Papers track). Attributing the “first” such achievement to Yamada et al. (2025) is therefore factually incorrect and misrepresents the timeline.  

**Suggested correction:**  
Revise to something like:  
> Yamada et al. (2025) extended the system with agentic tree search and further demonstrated AI-generated papers passing workshop-level peer review.  
Or, if the Yamada et al. paper established a qualitatively different review threshold (e.g., a regular workshop track with full reviews), explicitly specify the distinction rather than claiming absolute primacy.

---

### Catch 3 — §2.5 (ancillary)
**Claim under review:**  
> Two structural features unite these systems … First, each is constructed within a single vendor’s model family — … a single-vendor pipeline for FARS.

**Verdict:** Rejected (follows from Catch 1)  

**Reasoning:**  
The characterization of FARS as “single-vendor” inherits the same unsupported status as the existence of the system itself. Without a verified citation the claim cannot be accepted.  

**Suggested correction:**  
Remove the FARS reference and rephrase the “single-vendor” statement to cover only the verified systems (AI Scientist, PaperOrchestra, and any other cited system). If a replacement is needed, ensure the new system appears in the verified citation pool.

---

*(No further catches. The remaining attribution of prior work, the cross‑vendor/within‑vendor distinction, the framing of PoLL, and the novelty claim are correctly handled.)*
