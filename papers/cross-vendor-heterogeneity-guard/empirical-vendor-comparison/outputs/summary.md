# Empirical vendor-comparison summary

- Prompts: 8
- Vendors: deepseek, gemini, openai, anthropic
- Total cost: $2.2022
- Per-vendor responses: {'deepseek': 8, 'gemini': 8, 'openai': 8, 'anthropic': 7}
- Per-vendor refusals: {'deepseek': 0, 'gemini': 0, 'openai': 0, 'anthropic': 1}
- Per-vendor empties (other): {'deepseek': 0, 'gemini': 0, 'openai': 0, 'anthropic': 0}

## Pairwise mean agreement rate (across all prompts with claim coding)

| Vendor A | Vendor B | n_prompts | mean agreement |
|---|---|---|---|
| deepseek | gemini | 8 | 79.6% |
| deepseek | openai | 8 | 88.7% |
| gemini | openai | 8 | 77.1% |
| deepseek | anthropic | 7 | 85.6% |
| gemini | anthropic | 7 | 83.6% |
| openai | anthropic | 7 | 76.7% |

## By task type

| Task type | n data points | mean agreement | min | max |
|---|---|---|---|---|
| factual | 3 | 63.3% | 50.0% | 80.0% |
| factual-quantitative | 6 | 97.6% | 85.7% | 100.0% |
| mechanism-inference | 12 | 80.7% | 66.7% | 100.0% |
| hypothesis-generation | 6 | 67.5% | 50.0% | 100.0% |
| synthesis | 6 | 87.5% | 75.0% | 100.0% |
| adversarial-review | 6 | 78.6% | 66.7% | 100.0% |
| hypothesis-generation + mechanism | 6 | 89.7% | 75.0% | 100.0% |

## Per-prompt breakdown

### 01-uricase-mechanism-factual  (task: factual)
- Claims loaded: True  (6 claims)
  - deepseek: status=ok, cost=$0.0051, latency=184.3s, body_chars=1679
  - gemini: status=ok, cost=$0.0198, latency=39.5s, body_chars=1957
  - openai: status=ok, cost=$0.0647, latency=114.1s, body_chars=2363
  - anthropic: status=EMPTY, cost=$0.0000, latency=0.0s, body_chars=16
  - deepseek_vs_gemini: agreement=50.0%  (agree=3, disagree=3, refusals=0)
  - deepseek_vs_openai: agreement=80.0%  (agree=4, disagree=1, refusals=0)
  - deepseek_vs_anthropic: agreement=n/a  (agree=0, disagree=0, refusals=6)
  - gemini_vs_openai: agreement=60.0%  (agree=3, disagree=2, refusals=0)
  - gemini_vs_anthropic: agreement=n/a  (agree=0, disagree=0, refusals=6)
  - openai_vs_anthropic: agreement=n/a  (agree=0, disagree=0, refusals=6)

### 02-abcg2-q141k-factual-quant  (task: factual-quantitative)
- Claims loaded: True  (7 claims)
  - deepseek: status=ok, cost=$0.0033, latency=68.6s, body_chars=2908
  - gemini: status=ok, cost=$0.0180, latency=39.4s, body_chars=5347
  - openai: status=ok, cost=$0.0917, latency=157.1s, body_chars=3259
  - anthropic: status=ok, cost=$0.1261, latency=27.9s, body_chars=3762
  - deepseek_vs_gemini: agreement=100.0%  (agree=6, disagree=0, refusals=0)
  - deepseek_vs_openai: agreement=100.0%  (agree=6, disagree=0, refusals=0)
  - deepseek_vs_anthropic: agreement=85.7%  (agree=6, disagree=1, refusals=0)
  - gemini_vs_openai: agreement=100.0%  (agree=6, disagree=0, refusals=0)
  - gemini_vs_anthropic: agreement=100.0%  (agree=6, disagree=0, refusals=0)
  - openai_vs_anthropic: agreement=100.0%  (agree=6, disagree=0, refusals=0)

### 03-nlrp3-mechanism-inference  (task: mechanism-inference)
- Claims loaded: True  (6 claims)
  - deepseek: status=ok, cost=$0.0040, latency=73.8s, body_chars=8022
  - gemini: status=ok, cost=$0.0242, latency=49.2s, body_chars=9327
  - openai: status=ok, cost=$0.0972, latency=191.5s, body_chars=7421
  - anthropic: status=ok, cost=$0.2217, latency=44.8s, body_chars=7142
  - deepseek_vs_gemini: agreement=80.0%  (agree=4, disagree=1, refusals=0)
  - deepseek_vs_openai: agreement=100.0%  (agree=3, disagree=0, refusals=0)
  - deepseek_vs_anthropic: agreement=75.0%  (agree=3, disagree=1, refusals=0)
  - gemini_vs_openai: agreement=66.7%  (agree=2, disagree=1, refusals=0)
  - gemini_vs_anthropic: agreement=100.0%  (agree=4, disagree=0, refusals=0)
  - openai_vs_anthropic: agreement=66.7%  (agree=2, disagree=1, refusals=0)

### 04-koji-uricase-hypothesis-gen  (task: hypothesis-generation)
- Claims loaded: True  (6 claims)
  - deepseek: status=ok, cost=$0.0037, latency=84.4s, body_chars=5732
  - gemini: status=ok, cost=$0.0212, latency=42.0s, body_chars=6946
  - openai: status=ok, cost=$0.0779, latency=146.3s, body_chars=10352
  - anthropic: status=ok, cost=$0.2469, latency=56.9s, body_chars=8173
  - deepseek_vs_gemini: agreement=60.0%  (agree=3, disagree=2, refusals=0)
  - deepseek_vs_openai: agreement=75.0%  (agree=3, disagree=1, refusals=0)
  - deepseek_vs_anthropic: agreement=100.0%  (agree=5, disagree=0, refusals=0)
  - gemini_vs_openai: agreement=60.0%  (agree=3, disagree=2, refusals=0)
  - gemini_vs_anthropic: agreement=50.0%  (agree=3, disagree=3, refusals=0)
  - openai_vs_anthropic: agreement=60.0%  (agree=3, disagree=2, refusals=0)

### 05-rasburicase-ada-mechanism  (task: mechanism-inference)
- Claims loaded: True  (6 claims)
  - deepseek: status=ok, cost=$0.0023, latency=121.0s, body_chars=11257
  - gemini: status=ok, cost=$0.0220, latency=48.4s, body_chars=9756
  - openai: status=ok, cost=$0.0887, latency=176.0s, body_chars=14405
  - anthropic: status=ok, cost=$0.2147, latency=48.5s, body_chars=7128
  - deepseek_vs_gemini: agreement=80.0%  (agree=4, disagree=1, refusals=0)
  - deepseek_vs_openai: agreement=80.0%  (agree=4, disagree=1, refusals=0)
  - deepseek_vs_anthropic: agreement=80.0%  (agree=4, disagree=1, refusals=0)
  - gemini_vs_openai: agreement=80.0%  (agree=4, disagree=1, refusals=0)
  - gemini_vs_anthropic: agreement=80.0%  (agree=4, disagree=1, refusals=0)
  - openai_vs_anthropic: agreement=80.0%  (agree=4, disagree=1, refusals=0)

### 06-cross-document-synthesis  (task: synthesis)
- Claims loaded: True  (6 claims)
  - deepseek: status=ok, cost=$0.0052, latency=92.5s, body_chars=5694
  - gemini: status=ok, cost=$0.0310, latency=65.0s, body_chars=9187
  - openai: status=ok, cost=$0.0662, latency=100.6s, body_chars=12209
  - anthropic: status=ok, cost=$0.2065, latency=38.1s, body_chars=5991
  - deepseek_vs_gemini: agreement=100.0%  (agree=5, disagree=0, refusals=0)
  - deepseek_vs_openai: agreement=75.0%  (agree=3, disagree=1, refusals=0)
  - deepseek_vs_anthropic: agreement=100.0%  (agree=5, disagree=0, refusals=0)
  - gemini_vs_openai: agreement=75.0%  (agree=3, disagree=1, refusals=0)
  - gemini_vs_anthropic: agreement=100.0%  (agree=5, disagree=0, refusals=0)
  - openai_vs_anthropic: agreement=75.0%  (agree=3, disagree=1, refusals=0)

### 07-self-demonstrating-review  (task: adversarial-review)
- Claims loaded: True  (5 claims)
  - deepseek: status=ok, cost=$0.0049, latency=167.3s, body_chars=2821
  - gemini: status=ok, cost=$0.0152, latency=32.6s, body_chars=2387
  - openai: status=ok, cost=$0.0150, latency=20.5s, body_chars=3331
  - anthropic: status=ok, cost=$0.1324, latency=23.8s, body_chars=4739
  - deepseek_vs_gemini: agreement=66.7%  (agree=2, disagree=1, refusals=0)
  - deepseek_vs_openai: agreement=100.0%  (agree=4, disagree=0, refusals=0)
  - deepseek_vs_anthropic: agreement=75.0%  (agree=3, disagree=1, refusals=0)
  - gemini_vs_openai: agreement=75.0%  (agree=3, disagree=1, refusals=0)
  - gemini_vs_anthropic: agreement=75.0%  (agree=3, disagree=1, refusals=0)
  - openai_vs_anthropic: agreement=80.0%  (agree=4, disagree=1, refusals=0)

### 08-cordycepin-koji-feasibility  (task: hypothesis-generation + mechanism)
- Claims loaded: True  (6 claims)
  - deepseek: status=ok, cost=$0.0062, latency=151.1s, body_chars=6161
  - gemini: status=ok, cost=$0.0280, latency=58.0s, body_chars=9499
  - openai: status=ok, cost=$0.0607, latency=93.0s, body_chars=12206
  - anthropic: status=ok, cost=$0.2777, latency=56.3s, body_chars=8908
  - deepseek_vs_gemini: agreement=100.0%  (agree=5, disagree=0, refusals=0)
  - deepseek_vs_openai: agreement=100.0%  (agree=4, disagree=0, refusals=0)
  - deepseek_vs_anthropic: agreement=83.3%  (agree=5, disagree=1, refusals=0)
  - gemini_vs_openai: agreement=100.0%  (agree=4, disagree=0, refusals=0)
  - gemini_vs_anthropic: agreement=80.0%  (agree=4, disagree=1, refusals=0)
  - openai_vs_anthropic: agreement=75.0%  (agree=3, disagree=1, refusals=0)
