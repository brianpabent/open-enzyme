# Within-vendor agreement summary

- Vendors: deepseek, gemini, openai, anthropic
- Replicates configured: [1, 2, 3]
- Cells with at least 2 codable replicates: 32
- **Headline within-vendor mean agreement rate: 90.8%**
- Headline cross-vendor mean agreement rate (pilot, for comparison): 82.3%
- Within-vendor minus cross-vendor: +8.4%

## Partition of cross-vendor disagreement
- Cross-vendor disagreement rate: 17.7%
- Within-vendor disagreement rate (temperature noise): 9.2%
- Residual cross-vendor heterogeneity signal: 8.4% (48% of total cross-vendor disagreement)

## Per-vendor stability

| Vendor | Within-vendor | Cross-vendor | Delta |
|---|---|---|---|
| deepseek | 90.7% | 84.6% | +6.1% |
| gemini | 89.9% | 80.8% | +9.1% |
| openai | 88.3% | 81.9% | +6.4% |
| anthropic | 94.0% | 81.9% | +12.1% |

## By task type

| Task type | Within-vendor | Cross-vendor |
|---|---|---|
| adversarial-review | 87.6% | 78.6% |
| factual | 87.2% | 70.0% |
| factual-quantitative | 95.2% | 97.6% |
| hypothesis-generation | 87.5% | 67.5% |
| hypothesis-generation + mechanism | 100.0% | 89.7% |
| mechanism-inference | 86.1% | 80.7% |
| synthesis | 96.3% | 87.5% |

## Per-cell breakdown

| Prompt | Vendor | Task type | Cell mean | Pairs |
|---|---|---|---|---|
| 01-uricase-mechanism-factual | deepseek | factual | 88.9% | r1_vs_r2=67%; r1_vs_r3=100%; r2_vs_r3=100% |
| 01-uricase-mechanism-factual | gemini | factual | 77.8% | r1_vs_r2=83%; r1_vs_r3=67%; r2_vs_r3=83% |
| 01-uricase-mechanism-factual | openai | factual | 82.2% | r1_vs_r2=80%; r1_vs_r3=100%; r2_vs_r3=67% |
| 01-uricase-mechanism-factual | anthropic | factual | 100.0% | r1_vs_r2=100%; r1_vs_r3=100%; r2_vs_r3=100% |
| 02-abcg2-q141k-factual-quant | deepseek | factual-quantitative | 95.2% | r1_vs_r2=100%; r1_vs_r3=86%; r2_vs_r3=100% |
| 02-abcg2-q141k-factual-quant | gemini | factual-quantitative | 100.0% | r1_vs_r2=100%; r1_vs_r3=100%; r2_vs_r3=100% |
| 02-abcg2-q141k-factual-quant | openai | factual-quantitative | 100.0% | r1_vs_r2=100%; r1_vs_r3=100%; r2_vs_r3=100% |
| 02-abcg2-q141k-factual-quant | anthropic | factual-quantitative | 85.7% | r1_vs_r2=86%; r1_vs_r3=86%; r2_vs_r3=86% |
| 03-nlrp3-mechanism-inference | deepseek | mechanism-inference | 77.8% | r1_vs_r2=67%; r1_vs_r3=100%; r2_vs_r3=67% |
| 03-nlrp3-mechanism-inference | gemini | mechanism-inference | 66.7% | r1_vs_r2=60%; r1_vs_r3=80%; r2_vs_r3=60% |
| 03-nlrp3-mechanism-inference | openai | mechanism-inference | 77.8% | r1_vs_r2=67%; r1_vs_r3=67%; r2_vs_r3=100% |
| 03-nlrp3-mechanism-inference | anthropic | mechanism-inference | 100.0% | r1_vs_r2=100%; r1_vs_r3=100%; r2_vs_r3=100% |
| 04-koji-uricase-hypothesis-gen | deepseek | hypothesis-generation | 100.0% | r1_vs_r2=100%; r1_vs_r3=100%; r2_vs_r3=100% |
| 04-koji-uricase-hypothesis-gen | gemini | hypothesis-generation | 75.0% | r1_vs_r2=75%; r1_vs_r3=75%; r2_vs_r3=75% |
| 04-koji-uricase-hypothesis-gen | openai | hypothesis-generation | 75.0% | r1_vs_r2=75%; r1_vs_r3=75%; r2_vs_r3=75% |
| 04-koji-uricase-hypothesis-gen | anthropic | hypothesis-generation | 100.0% | r1_vs_r2=100%; r1_vs_r3=100%; r2_vs_r3=100% |
| 05-rasburicase-ada-mechanism | deepseek | mechanism-inference | 83.3% | r1_vs_r2=100%; r1_vs_r3=75%; r2_vs_r3=75% |
| 05-rasburicase-ada-mechanism | gemini | mechanism-inference | 100.0% | r1_vs_r2=100%; r1_vs_r3=100%; r2_vs_r3=100% |
| 05-rasburicase-ada-mechanism | openai | mechanism-inference | 100.0% | r1_vs_r2=100%; r1_vs_r3=100%; r2_vs_r3=100% |
| 05-rasburicase-ada-mechanism | anthropic | mechanism-inference | 83.3% | r1_vs_r2=75%; r1_vs_r3=75%; r2_vs_r3=100% |
| 06-cross-document-synthesis | deepseek | synthesis | 100.0% | r1_vs_r2=100%; r1_vs_r3=100%; r2_vs_r3=100% |
| 06-cross-document-synthesis | gemini | synthesis | 100.0% | r1_vs_r2=100%; r1_vs_r3=100%; r2_vs_r3=100% |
| 06-cross-document-synthesis | openai | synthesis | 85.0% | r1_vs_r2=100%; r1_vs_r3=75%; r2_vs_r3=80% |
| 06-cross-document-synthesis | anthropic | synthesis | 100.0% | r1_vs_r2=100%; r1_vs_r3=100%; r2_vs_r3=100% |
| 07-self-demonstrating-review | deepseek | adversarial-review | 80.6% | r1_vs_r2=67%; r1_vs_r3=100%; r2_vs_r3=75% |
| 07-self-demonstrating-review | gemini | adversarial-review | 100.0% | r1_vs_r2=100%; r1_vs_r3=100%; r2_vs_r3=100% |
| 07-self-demonstrating-review | openai | adversarial-review | 86.7% | r1_vs_r2=80%; r1_vs_r3=80%; r2_vs_r3=100% |
| 07-self-demonstrating-review | anthropic | adversarial-review | 83.3% | r1_vs_r2=100%; r1_vs_r3=75%; r2_vs_r3=75% |
| 08-cordycepin-koji-feasibility | deepseek | hypothesis-generation + mechanism | 100.0% | r1_vs_r2=100%; r1_vs_r3=100%; r2_vs_r3=100% |
| 08-cordycepin-koji-feasibility | gemini | hypothesis-generation + mechanism | 100.0% | r1_vs_r2=100%; r1_vs_r3=100%; r2_vs_r3=100% |
| 08-cordycepin-koji-feasibility | openai | hypothesis-generation + mechanism | 100.0% | r1_vs_r2=100%; r1_vs_r3=100%; r2_vs_r3=100% |
| 08-cordycepin-koji-feasibility | anthropic | hypothesis-generation + mechanism | 100.0% | r1_vs_r2=100%; r1_vs_r3=100%; r2_vs_r3=100% |