# comp-038 Codex Synthesis Packet

Use this packet for the primary GPT-5.5/Codex synthesis role without spending OpenRouter tokens.

## Instructions

You are working on Open Enzyme, a Phase 0 research-and-design library.
Audience: PhD-level scientists. Be rigorous, source-aware, and direct.
Do not overclaim. Distinguish candidate evidence from verified evidence.
For load-bearing assay claims, PubMed abstracts alone are insufficient:
require full text, protocol PDFs, vendor validation docs, or method-comparison
data before recommending a GREEN verdict.

Run five independent synthesis trajectories mentally/analytically over the query plan and PubMed snapshot. Surface candidate Tier 2 butyrate assays, collapse consensus candidates, then produce a ranked audit. Do not assign GREEN unless full text, protocol PDFs, vendor validation docs, or GC-MS comparison data are present.

Required output shape:

```json
{
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
          "provisional_gc_ms_validation_status": ""
        }
      ],
      "red_flags": [],
      "trajectory_notes": ""
    }
  ],
  "consensus_candidates": [],
  "ranked_candidates": [],
  "overall_verdict": "GREEN | YELLOW | RED",
  "limitations": [],
  "recommended_next_step": ""
}
```

## Query Strategy

```json
{
  "scope": "Identify Tier 2 butyrate quantification assays (colorimetric / enzymatic / breath-hydrogen proxy / other low-cost intermediate methods) that can be validated against Tier 3 GC-MS reference. Microbiome-derived butyrate quantification in stool, blood, breath, and culture-supernatant matrices.",
  "natural_product_scope": false,
  "target_concentration_ranges": {
    "lumenal_butyrate": "10 uM to 100 mM (physiological gut range)",
    "serum_butyrate": "~1 to 10 uM (fasting and post-prandial human)",
    "culture_supernatant": "100 uM to 50 mM (in vitro fermentation)",
    "breath_hydrogen_proxy": "5 to 200 ppm (clinical breath-test range)"
  },
  "framings": [
    {
      "type": "assay-class-colorimetric",
      "queries": [
        "butyrate colorimetric assay validation GC-MS",
        "short chain fatty acid colorimetric quantification",
        "SCFA enzyme coupled colorimetric assay",
        "butyrate ester hydrolysis colorimetric"
      ],
      "rationale": "Colorimetric is the cheapest Tier 2 path; if a kit exists with published GC-MS validation it's the obvious first candidate."
    },
    {
      "type": "assay-class-enzymatic",
      "queries": [
        "butyrate kinase enzymatic assay quantification",
        "acyl-CoA synthetase butyrate enzymatic measurement",
        "NADH coupled butyrate assay",
        "butyryl-CoA dehydrogenase activity butyrate quantification"
      ],
      "rationale": "Enzymatic assays (NADH-readout, kinase-coupled) are standard Tier 2 path for fatty acid quantification in clinical chemistry; precedent exists for acetate, lactate, etc."
    },
    {
      "type": "assay-class-breath-hydrogen-proxy",
      "queries": [
        "breath hydrogen butyrate fermentation correlation",
        "lactulose breath test SCFA production proxy",
        "breath methane hydrogen colonic fermentation marker",
        "breath gas chromatography volatile fatty acids"
      ],
      "rationale": "Breath-hydrogen is established clinical proxy for colonic carbohydrate fermentation; the question is whether the correlation to specifically-butyrate (vs total SCFA / acetate / propionate) has been validated."
    },
    {
      "type": "assay-class-electrochemical-biosensor",
      "queries": [
        "butyrate biosensor electrochemical quantification",
        "SCFA microbial biosensor butyrate detection",
        "butyrate ion-selective electrode validation"
      ],
      "rationale": "Electrochemical and biosensor approaches are an emerging Tier 2 path; worth surveying even if Tier 2 readiness is unclear."
    },
    {
      "type": "validation-against-GC-MS",
      "queries": [
        "butyrate assay GC-MS comparison validation method correlation",
        "short chain fatty acid kit GC-MS cross-validation",
        "stool butyrate method comparison reference standard"
      ],
      "rationale": "The Tier 2 / Tier 3 bridge is the load-bearing criterion. Any candidate assay must have published GC-MS cross-validation (or such a study must be feasible) to count as a valid Tier 2 home for OE."
    },
    {
      "type": "application-context-stool",
      "queries": [
        "stool butyrate quantification clinical assay home test",
        "fecal SCFA self-administered measurement",
        "point-of-care SCFA stool analysis"
      ],
      "rationale": "OE's likely Tier 2 use cases are stool-matrix (microbiome interventions) and culture-supernatant (engineered LBP characterization). Stool-specific literature may surface kits not visible in generic SCFA searches."
    },
    {
      "type": "application-context-culture",
      "queries": [
        "in vitro fermentation butyrate quantification culture supernatant",
        "engineered probiotic SCFA production assay",
        "Faecalibacterium prausnitzii butyrate yield measurement"
      ],
      "rationale": "Specifically for engineered LBP / Faecalibacterium / Roseburia chassis characterization. Culture-supernatant matrices are simpler than stool and may have different optimal Tier 2 paths."
    },
    {
      "type": "commercial-kit-landscape",
      "queries": [
        "butyrate assay kit commercial Sigma Megazyme Cayman Cell Biolabs",
        "short chain fatty acid quantification kit catalog",
        "butyrate ELISA available commercial"
      ],
      "rationale": "A direct vendor/catalog scan complements the academic literature search. If a commercial kit with documented validation exists, it's the practical answer."
    }
  ],
  "deferred_framings": [
    {
      "type": "natural-product / non-English-corpus",
      "rationale": "Butyrate-assay literature is predominantly Western analytical chemistry. CNKI / J-STAGE / KISS scan is unlikely to surface novel Tier 2 candidates and is deferred unless Stage 1 returns are sparse."
    },
    {
      "type": "mass-spec-alternatives (non-GC-MS)",
      "rationale": "LC-MS, UPLC-MS, and capillary electrophoresis-MS are Tier 3 alternatives to GC-MS but do not lower the cost ladder. Deferred; the Tier 2 question is about NON-mass-spec methods specifically."
    }
  ],
  "output_format_expected": {
    "top_candidate_assays": "ranked list (1-5) via pairwise tournament across N=5 consensus trajectories",
    "per_candidate_fields": [
      "assay_name",
      "assay_class (colorimetric / enzymatic / breath-hydrogen / electrochemical / other)",
      "commercial_availability (kit / lab-built / both)",
      "cost_per_sample_estimate_usd",
      "GC_MS_validation_status (validated / partial / unvalidated)",
      "published_correlation_coefficient_with_GC_MS",
      "dynamic_range_butyrate",
      "matrix_compatibility (stool / serum / culture / breath)",
      "sample_prep_complexity (low / medium / high)",
      "key_publications (PMIDs)",
      "limitations_and_caveats",
      "consensus_statistic (N trajectories that surfaced this candidate)"
    ],
    "verdict": "GREEN (validated Tier 2 path exists, ready to adopt) / YELLOW (candidate exists but GC-MS validation is partial; OE-internal validation study required) / RED (no Tier 2 candidate with sufficient evidence; wet-lab development is the only path)"
  },
  "provenance": {
    "created": "2026-05-20",
    "created_by": "comp-038 scaffold (Claude on branch claude/review-gemini-science-PpAlm)",
    "methodology_reference": "operations/agentic-science-adoption.md \u2014 comp-038 scaffold section",
    "frozen_for_run": false
  }
}
```

## Model / Protocol Config

```json
{
  "openrouter": {
    "api_key_env": "OPENROUTER_API_KEY",
    "endpoint": "https://openrouter.ai/api/v1/chat/completions",
    "secret_location": "repo-root .env (gitignored) or shell environment"
  },
  "roles": {
    "query_strategist": {
      "model": "codex/gpt-5.5-in-session",
      "temperature": null,
      "notes": "Default when Codex runs the experiment locally; no OpenRouter call."
    },
    "synthesis": {
      "model": "codex/gpt-5.5-in-session",
      "temperature": null,
      "notes": "Primary synthesis role is performed by the current Codex session from outputs/codex-synthesis-packet.md."
    },
    "judge": {
      "model": "codex/gpt-5.5-in-session",
      "temperature": null,
      "notes": "Default judge/limitations pass when Codex is driving the run."
    },
    "verifier": {
      "model": "codex/gpt-5.5-in-session",
      "temperature": null,
      "notes": "Default source-evidence gate when Codex is driving the run."
    },
    "query_strategist_openrouter": {
      "env": "COMP038_QUERY_MODEL",
      "model": "deepseek/deepseek-chat",
      "temperature": 0.2
    },
    "synthesis_openrouter": {
      "env": "COMP038_SYNTHESIS_MODEL",
      "model": "openai/gpt-5.5",
      "temperature": 0.35
    },
    "judge_openrouter": {
      "env": "COMP038_JUDGE_MODEL",
      "model": "anthropic/claude-opus-4.7",
      "temperature": 0
    },
    "verifier_openrouter": {
      "env": "COMP038_VERIFIER_MODEL",
      "model": "anthropic/claude-opus-4.7",
      "temperature": 0
    }
  },
  "run": {
    "trajectories": 5,
    "consensus_threshold": 3,
    "budget_usd": 25,
    "max_candidates_for_full_pairwise": 6,
    "pubmed_retmax_per_query": 10,
    "final_green_requires_full_text_or_protocol_evidence": true
  },
  "translation": {
    "protocol": "two independent models from different vendors; preserve science-relevant disagreements inline rather than choosing one winner",
    "pairs": {
      "zh": {
        "model_a": {
          "env": "COMP038_TRANSLATION_ZH_MODEL_A",
          "model": "deepseek/deepseek-chat",
          "temperature": 0
        },
        "model_b": {
          "env": "COMP038_TRANSLATION_ZH_MODEL_B",
          "model": "openai/gpt-5.5",
          "temperature": 0
        },
        "referee": {
          "env": "COMP038_TRANSLATION_REFEREE_MODEL",
          "model": "anthropic/claude-opus-4.7",
          "temperature": 0
        }
      },
      "ja": {
        "model_a": {
          "env": "COMP038_TRANSLATION_JA_MODEL_A",
          "model": "anthropic/claude-opus-4.7",
          "temperature": 0
        },
        "model_b": {
          "env": "COMP038_TRANSLATION_JA_MODEL_B",
          "model": "openai/gpt-5.5",
          "temperature": 0
        },
        "referee": {
          "env": "COMP038_TRANSLATION_REFEREE_MODEL",
          "model": "anthropic/claude-opus-4.7",
          "temperature": 0
        }
      },
      "default": {
        "model_a": {
          "env": "COMP038_TRANSLATION_MODEL_A",
          "model": "openai/gpt-5.5",
          "temperature": 0
        },
        "model_b": {
          "env": "COMP038_TRANSLATION_MODEL_B",
          "model": "anthropic/claude-opus-4.7",
          "temperature": 0
        },
        "referee": {
          "env": "COMP038_TRANSLATION_REFEREE_MODEL",
          "model": "anthropic/claude-opus-4.7",
          "temperature": 0
        }
      }
    }
  },
  "provenance": {
    "created": "2026-05-20",
    "notes": [
      "Model names are non-secret and may be overridden by environment variables.",
      "OPENROUTER_API_KEY must never be committed.",
      "Default Codex roles make local runs use Brian's existing Codex/OpenAI subscription rather than OpenRouter spend.",
      "The *_openrouter roles are opt-in only and are used by analyze.py only with --run-openrouter."
    ]
  }
}
```

## PubMed Snapshot

Fetched at: 2026-05-20T15:06:05+00:00

```json
{
  "fetched_at_utc": "2026-05-20T15:06:05+00:00",
  "retmax_per_query": 10,
  "query_results": [
    {
      "framing": "assay-class-colorimetric",
      "query": "butyrate colorimetric assay validation GC-MS",
      "pmids": []
    },
    {
      "framing": "assay-class-colorimetric",
      "query": "short chain fatty acid colorimetric quantification",
      "pmids": [
        "41456648",
        "39503721",
        "28649044",
        "39126070",
        "37864505",
        "36436717",
        "27350657",
        "32319943",
        "38967859",
        "29224868"
      ]
    },
    {
      "framing": "assay-class-colorimetric",
      "query": "SCFA enzyme coupled colorimetric assay",
      "pmids": []
    },
    {
      "framing": "assay-class-colorimetric",
      "query": "butyrate ester hydrolysis colorimetric",
      "pmids": [
        "7082346",
        "33211958"
      ]
    },
    {
      "framing": "assay-class-enzymatic",
      "query": "butyrate kinase enzymatic assay quantification",
      "pmids": [
        "35839206",
        "29523768"
      ]
    },
    {
      "framing": "assay-class-enzymatic",
      "query": "acyl-CoA synthetase butyrate enzymatic measurement",
      "pmids": [
        "8002592"
      ]
    },
    {
      "framing": "assay-class-enzymatic",
      "query": "NADH coupled butyrate assay",
      "pmids": [
        "23223453",
        "34348140",
        "37370057",
        "41713389",
        "35752796",
        "41643453",
        "39436023",
        "34648892",
        "3503522",
        "6627675"
      ]
    },
    {
      "framing": "assay-class-enzymatic",
      "query": "butyryl-CoA dehydrogenase activity butyrate quantification",
      "pmids": []
    },
    {
      "framing": "assay-class-breath-hydrogen-proxy",
      "query": "breath hydrogen butyrate fermentation correlation",
      "pmids": [
        "31212318",
        "33671147"
      ]
    },
    {
      "framing": "assay-class-breath-hydrogen-proxy",
      "query": "lactulose breath test SCFA production proxy",
      "pmids": []
    },
    {
      "framing": "assay-class-breath-hydrogen-proxy",
      "query": "breath methane hydrogen colonic fermentation marker",
      "pmids": [
        "8049636",
        "1486849",
        "8253524",
        "41952402",
        "36221245",
        "27276436",
        "21712835",
        "16607150"
      ]
    },
    {
      "framing": "assay-class-breath-hydrogen-proxy",
      "query": "breath gas chromatography volatile fatty acids",
      "pmids": [
        "30699297",
        "36055216",
        "38503704",
        "40579210",
        "27341456",
        "41082646",
        "21386205",
        "5444347",
        "33765666",
        "27545394"
      ]
    },
    {
      "framing": "assay-class-electrochemical-biosensor",
      "query": "butyrate biosensor electrochemical quantification",
      "pmids": [
        "42041444",
        "41546892",
        "38823224"
      ]
    },
    {
      "framing": "assay-class-electrochemical-biosensor",
      "query": "SCFA microbial biosensor butyrate detection",
      "pmids": []
    },
    {
      "framing": "assay-class-electrochemical-biosensor",
      "query": "butyrate ion-selective electrode validation",
      "pmids": [
        "26999666"
      ]
    },
    {
      "framing": "validation-against-GC-MS",
      "query": "butyrate assay GC-MS comparison validation method correlation",
      "pmids": [
        "33509465",
        "26968013",
        "22105594"
      ]
    },
    {
      "framing": "validation-against-GC-MS",
      "query": "short chain fatty acid kit GC-MS cross-validation",
      "pmids": []
    },
    {
      "framing": "validation-against-GC-MS",
      "query": "stool butyrate method comparison reference standard",
      "pmids": []
    },
    {
      "framing": "application-context-stool",
      "query": "stool butyrate quantification clinical assay home test",
      "pmids": []
    },
    {
      "framing": "application-context-stool",
      "query": "fecal SCFA self-administered measurement",
      "pmids": [
        "39173973",
        "35276942",
        "40880079"
      ]
    },
    {
      "framing": "application-context-stool",
      "query": "point-of-care SCFA stool analysis",
      "pmids": [
        "33957773",
        "30649345",
        "39340210"
      ]
    },
    {
      "framing": "application-context-culture",
      "query": "in vitro fermentation butyrate quantification culture supernatant",
      "pmids": [
        "23542733"
      ]
    },
    {
      "framing": "application-context-culture",
      "query": "engineered probiotic SCFA production assay",
      "pmids": [
        "39546851",
        "35505080",
        "40350789",
        "32900799",
        "40735631",
        "40628054",
        "41478068",
        "41215008",
        "40921044",
        "37093514"
      ]
    },
    {
      "framing": "application-context-culture",
      "query": "Faecalibacterium prausnitzii butyrate yield measurement",
      "pmids": []
    },
    {
      "framing": "commercial-kit-landscape",
      "query": "butyrate assay kit commercial Sigma Megazyme Cayman Cell Biolabs",
      "pmids": []
    },
    {
      "framing": "commercial-kit-landscape",
      "query": "short chain fatty acid quantification kit catalog",
      "pmids": []
    },
    {
      "framing": "commercial-kit-landscape",
      "query": "butyrate ELISA available commercial",
      "pmids": [
        "38295385",
        "30716067",
        "39932071",
        "30416353",
        "24016248"
      ]
    }
  ],
  "records": [
    {
      "pmid": "1486849",
      "title": "Use of breath hydrogen and methane as markers of colonic fermentation in epidemiologic studies: circadian patterns of excretion.",
      "abstract": "Fermentation in the large bowel has been postulated to play a protective role against colon cancer. Hydrogen and methane are end products of this fermentation process and are absorbed into the bloodstream and excreted via expired air in the breath. Breath levels of hydrogen and, to a lesser extent, methane correlate strongly with colonic fermentation and may serve as useful biomarkers for this process. In a preliminary study to assess the usefulness of these two markers in epidemiologic studies, we followed the hourly excretion of the two gases in expired alveolar air for 48 hr in 20 healthy subjects, using a Quintron gas chromatograph equipped with a solid-state detector specific for reducing gases. All subjects excreted hydrogen, but 71% did not excrete methane. Possible atmospheric contamination of the samples was corrected for on the basis of breath carbon dioxide levels. A clear circadian pattern of excretion was observed for breath hydrogen, with a decrease during the early morning followed by a progressive increase during the rest of the day. Methane excretion was constant throughout the day. This study shows that four samples collected at convenient times (0600, 1300, 1800, and 2200 hr) are optimal to characterize individuals by their breath excretions of hydrogen and methane during a 24-hr period.",
      "journal": "Environmental health perspectives",
      "year": "1992",
      "doi": "10.1289/ehp.9298199",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/1486849/",
      "matched_queries": [
        "breath methane hydrogen colonic fermentation marker"
      ]
    },
    {
      "pmid": "16607150",
      "title": "High incidence of fermentation in the digestive tract in patients with reflux oesophagitis.",
      "abstract": "Because bacteria represent the sole source of gut hydrogen (H2) and methane (CH4), fasting breath H2 and CH4 gases have been used as markers of colonic fermentation. The presence of carbohydrates in the colonic lumen inhibits gastric and pancreatic secretions, and also influences lower oesophageal sphincter function in gastro-oesophageal reflux disease.\nStudies were performed in 793 consecutive patients undergoing oesophagogastroscopy (270 men and 523 women, aged 19-85 years). A fasting breath sample (20 ml) was collected before endoscopy. At endoscopy, we intubated the stomach without inflation by air, and 20 ml of intragastric gas was collected through the biopsy channel. Next, the tip of the endoscope was inserted into the second portion of the duodenum without inflation by air, and 20 ml of intraduodenal gas was collected. H2 and CH4 concentrations of each sample were measured by gas chromatography.\nReflux oesophagitis was found in 147 of the 793 patients. The mean values of the H2 and/or CH4 levels of samples taken from the stomach, duodenum and exhaled air were higher in patients with reflux oesophagitis than those without reflux oesophagitis. High H2 and/or CH4 levels were more frequently found in patients with reflux oesophagitis.\nWe concluded that the presence of fermentation in the digestive tract was considered to be a risk factor for developing reflux oesophagitis.",
      "journal": "European journal of gastroenterology & hepatology",
      "year": "2006",
      "doi": "10.1097/00042737-200605000-00013",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/16607150/",
      "matched_queries": [
        "breath methane hydrogen colonic fermentation marker"
      ]
    },
    {
      "pmid": "21386205",
      "title": "Extra-oral halitosis: an overview.",
      "abstract": "Halitosis can be subdivided into intra-oral and extra-oral halitosis, depending on the place where it originates. Most reports now agree that the most frequent sources of halitosis exist within the oral cavity and include bacterial reservoirs such as the dorsum of the tongue, saliva and periodontal pockets, where anaerobic bacteria degrade sulfur-containing amino acids to produce the foul smelling volatile sulfur compounds (VSCs), especially hydrogen sulfide (H(2)S) and methyl mercaptan (CH(3)SH). Tongue coating is considered to be the most important source of VSCs. Oral malodor can now be treated effectively. Special attention in this overview is given to extra-oral halitosis. Extra-oral halitosis can be subdivided into non-blood-borne halitosis, such as halitosis from the upper respiratory tract including the nose and from the lower respiratory tract, and blood-borne halitosis. The majority of patients with extra-oral halitosis have blood-borne halitosis. Blood-borne halitosis is also frequently caused by odorous VSCs, in particular dimethyl sulfide (CH3SCH3). Extra-oral halitosis, covering about 5-10% of all cases of halitosis, might be a manifestation of a serious disease for which treatment is much more complicated than for intra-oral halitosis. It is therefore of utmost importance to differentiate between intra-oral and extra-oral halitosis. Differences between intra-oral and extra-oral halitosis are discussed extensively. The importance of applying odor characterization of various odorants in halitosis research is also highlighted in this article. The use of the odor index, odor threshold values and simulation of bad breath samples is explained.",
      "journal": "Journal of breath research",
      "year": "2010",
      "doi": "10.1088/1752-7155/4/1/017003",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/21386205/",
      "matched_queries": [
        "breath gas chromatography volatile fatty acids"
      ]
    },
    {
      "pmid": "21712835",
      "title": "Inulin increases short-term markers for colonic fermentation similarly in healthy and hyperinsulinaemic humans.",
      "abstract": "Colonic fermentation of dietary fibre produces short-chain fatty acids (SCFAs), acetate, propionate and butyrate, which may protect against type 2 diabetes by reducing serum free-fatty acids (FFAs). Since hyperinsulinaemia is associated with insulin resistance and increased diabetes risk, the main objective was to compare markers of colonic fermentation after acute inulin ingestion in subjects with normal (<40\u2009 pmol/l, NI) and high (\u226540 \u2009pmol/l, HI) plasma insulin.\nOvernight fasted NI (n=9) and HI (n=9) subjects were studied for 4 \u2009h on two separate days after consuming 300 \u2009ml drinks containing 75 \u2009g glucose (Glucose) or 75 \u2009g glucose plus 24\u2009 g inulin (Inulin) using a randomized, single-blind, crossover design.\nInulin elicited a higher breath hydrogen and methane areas under the curve (AUC), but the increases in SCFA responses were not statistically significant. Mean serum-acetate concentration over the 4-h study period was higher in NI than in HI subjects (44.3 \u00b1 6.9 vs 22.5 \u00b1 3.7 \u2009\u03bcmol/l, P=0.001). The rate of rebound of FFA was reduced by Inulin, with FFA at 4\u2009 h being less after Inulin than Glucose, regardless of insulin status (0.310 \u00b1 0.028 vs 0.432 \u00b1 0.042 mEq/l, P=0.008).\nThis suggests that inulin increases short-term markers for colonic fermentation, but a longer study period may be necessary to observe differences in SCFA production. The reason for the lower serum acetate in HI is unclear but may be due to reduced absorption, increased clearance or decreased endogenous production. This suggests the need to compare acetate kinetics in normal and hyperinsulinaemic subjects.",
      "journal": "European journal of clinical nutrition",
      "year": "2011",
      "doi": "10.1038/ejcn.2011.116",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/21712835/",
      "matched_queries": [
        "breath methane hydrogen colonic fermentation marker"
      ]
    },
    {
      "pmid": "22105594",
      "title": "An enzymatic method to determine \u03b3-hydroxybutyric acid in serum and urine.",
      "abstract": "Gamma-hydroxybutyric acid (GHB) has become one of the most dangerous illicit drugs of abuse today. It is used as a recreational and date rape drug because of its depressant effect on the central nervous system, which may cause euphoria, amnesia, respiratory arrest, and coma. There is an urgent need for a simple, easy-to-use assay for GHB determination in urine and blood. In this article, a rapid enzymatic assay adapted to clinical chemistry analyzers for the detection of GHB is presented.\nThe described GHB enzymatic assay is based on a recombinant GHB dehydrogenase. The full validation of the assay was performed on a Konelab 30 analyzer (Thermo Fisher Scientific).\nThe analytical sensitivity was <1.5 mg/L, whereas the functional sensitivity was 4.5 mg/L in serum and 2.8 mg/L in urine. The total imprecision coefficient of variation (CV) was <9.8% in serum and <7.9% in urine. The within-run imprecision showed a CV of <3.8% in serum and <4.6% in urine. The assay was linear within the range 5-250 mg/L. Mean recoveries were 109% in serum and 105% in urine. No cross-reactivity was observed for tested GHB analogues and precursors. Comparison of GHB-positive samples showed an excellent correlation with ion chromatography, gas chromatography-mass spectrometry, and liquid chromatography associated to tandem mass spectrometry. Except for ethanol, no substantial interference from serum constituents and some drugs was observed.\nThis automated GHB assay is fully quantitative and allows the accurate measurement of GHB in serum and urine. It can be used as a rapid screening assay for the determination of GHB in intoxicated or overdosed patients.",
      "journal": "Therapeutic drug monitoring",
      "year": "2011",
      "doi": "10.1097/FTD.0b013e318239a41a",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/22105594/",
      "matched_queries": [
        "butyrate assay GC-MS comparison validation method correlation"
      ]
    },
    {
      "pmid": "23223453",
      "title": "Suppression of oxidative stress by \u03b2-hydroxybutyrate, an endogenous histone deacetylase inhibitor.",
      "abstract": "Concentrations of acetyl-coenzyme A and nicotinamide adenine dinucleotide (NAD(+)) affect histone acetylation and thereby couple cellular metabolic status and transcriptional regulation. We report that the ketone body d-\u03b2-hydroxybutyrate (\u03b2OHB) is an endogenous and specific inhibitor of class I histone deacetylases (HDACs). Administration of exogenous \u03b2OHB, or fasting or calorie restriction, two conditions associated with increased \u03b2OHB abundance, all increased global histone acetylation in mouse tissues. Inhibition of HDAC by \u03b2OHB was correlated with global changes in transcription, including that of the genes encoding oxidative stress resistance factors FOXO3A and MT2. Treatment of cells with \u03b2OHB increased histone acetylation at the Foxo3a and Mt2 promoters, and both genes were activated by selective depletion of HDAC1 and HDAC2. Consistent with increased FOXO3A and MT2 activity, treatment of mice with \u03b2OHB conferred substantial protection against oxidative stress.",
      "journal": "Science (New York, N.Y.)",
      "year": "2013",
      "doi": "10.1126/science.1227166",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/23223453/",
      "matched_queries": [
        "NADH coupled butyrate assay"
      ]
    },
    {
      "pmid": "23542733",
      "title": "Development of a HPLC-UV method for the quantitative determination of four short-chain fatty acids and lactic acid produced by intestinal bacteria during in vitro fermentation.",
      "abstract": "A rapid and sensitive HPLC-UV method for the quantitative determination of four short-chain fatty acids (SCFAs) and lactic acid (LA) produced during in vitro fermentation is presented. Extraction of SCFAs from supernatants of bacterial cultures is aggravated due to their polarity and volatility. Detection can only be performed at a short, non-selective UV wavelength (210nm), due to the lack of any significant chromophore. Therefore special attention was paid to the optimization of the sample preparation procedure and the HPLC-UV conditions. The final extraction procedure consisted of a liquid-liquid back extraction using diethylether. Prior to HPLC-UV analysis the samples were acidified (pH<2) in order to improve retention of the SCFA's and LA on the Hypersil Gold aQ column. Matrix-matched calibration graphs were prepared for all analytes of interest (range 0.5-50mM) and correlation and goodness-of-fit coefficients were between 0.9951-0.9993 and 3.88-8.27%, respectively. Limits of detection and quantification ranged from 0.13 to 0.33mM and 0.5 to 1.0mM, respectively. The results for the within-day and between-day precision and accuracy fell within the ranges specified. The reported validated method has been successfully used for the in vitro screening of supernatants of bacterial cultures for the presence of butyric acid, aiming to select for butyric acid-producing bacteria. In addition, the method has been used to determine the production pattern of selected fatty acids by bacterial species isolated from human feces and chicken caeca.",
      "journal": "Journal of pharmaceutical and biomedical analysis",
      "year": "2013",
      "doi": "10.1016/j.jpba.2013.02.032",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/23542733/",
      "matched_queries": [
        "in vitro fermentation butyrate quantification culture supernatant"
      ]
    },
    {
      "pmid": "24016248",
      "title": "The influence of statin-fibrate combination therapy on lipids profile and apolipoprotein A5 in patients with acute coronary syndrome.",
      "abstract": "Statin-fibrate combination therapy has been used to treat patients with acute coronary syndrome (ACS) complicated by elevated triglycerides (TG) and decreased high density lipoprotein cholesterol (HDL-C). The purpose of this study was to evaluate the influence of the combination therapy on lipids profile and apolipoprotein A5 (apoA5) level in patients with ACS.\nOne hundred and four patients with ACS were recruited and randomly assigned into two groups: one was statin group (n = 52), given atorvastatin (20 mg QN) or other statins with equivalent dosages; the other was combination group (n = 52), given the same dose of statin plus bezafibrate (200 mg BID). Follow-up visits were scheduled at the end of 6 and 12 weeks post treatment. Serum apoA5 levels were determined using a commercial available ELISA kit.\n(1) Compared with that of statin monotherapy, statin-bezafibrate combination treatment not only resulted in a significant reduction of TG, TC and LDL-C levels, (all p < 0.05), but also led to increases in HDL-C and apoA5 levels (p < 0.05).(2) The percentage changes of TC, TG, LDL-C and apoA5 levels in both groups were even bigger at 12 weeks after treatment than that at 6 weeks (all p < 0.05). Similarly, the rates of achieving lipid-control target were higher in statin-bezafibrate combination treatment group than those in statin monotherapy group (all p < 0.05).(3) Spearman rank correlation analysis showed that the pre-treatment apoA5 level was positively correlated with TG (r = 0.359, p = 0.009). However, a negative correlation was observed between apoA5 and TG (r = -0.329, p = 0.017) after 12 weeks treatment.\nStatin and fibrate combination therapy is more effective than statin alone in achieving a comprehensive lipid control for ACS patients. Serum apoA5 elevation after statin and fibrate combination treatment could be due to the synergistic effect of both drugs on hypertriglyceridemia control.",
      "journal": "Lipids in health and disease",
      "year": "2013",
      "doi": "10.1186/1476-511X-12-133",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/24016248/",
      "matched_queries": [
        "butyrate ELISA available commercial"
      ]
    },
    {
      "pmid": "26968013",
      "title": "Determination of GHB levels in breast milk and correlation with blood concentrations.",
      "abstract": "The sodium salt of GHB or sodium oxybate is approved and registered in some countries as a therapeutic substance (Xyrem(\u00ae)) for the treatment of narcolepsy-associated cataplexy. This study was designed to measure the GHB endogenous levels in blood and breast milk of 20 breastfeeding women. In addition, blood and breast milk samples of a 32-year-old narcoleptic nursing mother, who was on sodium oxybate treatment, were simultaneously collected at 0.5, 1, 3, 4 and 5h following a 4.5g GHB dose and analyzed, in order to establish the safety interval of time to breastfeed. A GC-MS method for the detection and quantification of GHB in blood and breast milk was developed and fully validated. The geometric mean of endogenous GHB levels in blood and breast milk detected at time 0 were 0.57mg/L; 95% Reference Interval (RI): 0.21-1.52mg/L and 0.36mg/L; 95% RI: 0.13-1.03mg/L, respectively. The geometric mean of the concentration of GHB in milk was 37% less (95% RI: from 14 to 53%) compared to that found in the blood. The analysis of blood and breast milk samples collected from the 32 years-old female showed the following results: GHB blood concentration 0.5h after medication intake was 80.10mg/L, reaching the peak 1h after the drug administration (108.34mg/L) and it steadily decreased to reach a level of 1.75mg/L, 5h after the medication intake. The GHB concentration found in breast milk followed the same pattern as for the blood, with the highest concentration being 23.19mg/L, 1h after sodium oxybate administration and the lowest 0.99mg/L, 5h after the medication's intake. The comparison between blood and breast milk GHB levels in the 32-year-old woman, showed significant lower GHB levels in milk at 0.5, 1 and 3h, ranging from 71 to 80% less. It is interesting to note that only at 4 and 5h the difference between blood and breast milk GHB levels fell within the 95% RI (14-53%) of endogenous levels. Taking into consideration the absence of reference values for endogenous GHB in milk, we suggest the following reference interval: 0.13-1.03mg/L. We would recommend, following these preliminary data, that nursing mothers under sodium oxybate treatment should breastfeed at least 5h after the last GHB administration. However, further studies are necessary in order to confirm these findings.",
      "journal": "Forensic science international",
      "year": "2016",
      "doi": "10.1016/j.forsciint.2016.02.020",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/26968013/",
      "matched_queries": [
        "butyrate assay GC-MS comparison validation method correlation"
      ]
    },
    {
      "pmid": "26999666",
      "title": "Functional and Biochemical Characterization of Alvinella pompejana Cys-Loop Receptor Homologues.",
      "abstract": "Cys-loop receptors are membrane spanning ligand-gated ion channels involved in fast excitatory and inhibitory neurotransmission. Three-dimensional structures of these ion channels, determined by X-ray crystallography or electron microscopy, have revealed valuable information regarding the molecular mechanisms underlying ligand recognition, channel gating and ion conductance. To extend and validate the current insights, we here present promising candidates for further structural studies. We report the biochemical and functional characterization of Cys-loop receptor homologues identified in the proteome of Alvinella pompejana, an extremophilic, polychaete annelid found in hydrothermal vents at the bottom of the Pacific Ocean. Seven homologues were selected, named Alpo1-7. Five of them, Alpo2-6, were unidentified prior to this study. Two-electrode voltage clamp experiments revealed that wild type Alpo5 and Alpo6, both sharing remarkably high sequence identity with human glycine receptor \u03b1 subunits, are anion-selective channels that can be activated by glycine, GABA and taurine. Furthermore, upon expression in insect cells fluorescence size-exclusion chromatography experiments indicated that four homologues, Alpo1, Alpo4, Alpo6 and Alpo7, can be extracted out of the membrane by a wide variety of detergents while maintaining their oligomeric state. Finally, large-scale purification efforts of Alpo1, Alpo4 and Alpo6 resulted in milligram amounts of biochemically stable and monodisperse protein. Overall, our results establish the evolutionary conservation of glycine receptors in annelids and pave the way for future structural studies.",
      "journal": "PloS one",
      "year": "2016",
      "doi": "10.1371/journal.pone.0151183",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/26999666/",
      "matched_queries": [
        "butyrate ion-selective electrode validation"
      ]
    },
    {
      "pmid": "27276436",
      "title": "Lactulose Breath Test Gas Production in Childhood IBS Is Associated With Intestinal Transit and Bowel Movement Frequency.",
      "abstract": "In adults with irritable bowel syndrome (IBS), bacterial gas production (colonic fermentation) is related to both symptom generation and intestinal transit. Whether gas production affects symptom generation, psychosocial distress, or intestinal transit in childhood IBS is unknown.\nChildren (ages 7-17 years) with pediatric Rome III IBS completed validated psychosocial questionnaires and a 2-week daily diary capturing pain and stooling characteristics. Stool form determined IBS subtype. Subjects then completed a 3-hour lactulose breath test for measurement of total breath hydrogen and methane production. Carmine red was used to determine whole intestinal transit time.\nA total of 87 children (mean age 13\u200a\u00b1\u200a2.6 [standard deviation] years) were enrolled, of whom 50 (57.5%) were girls. All children produced hydrogen and 51 (58.6%) produced methane. Hydrogen and methane production did not correlate with either abdominal pain frequency/severity or psychosocial distress. Hydrogen and methane production did not differ significantly by IBS subtype. Methane production correlated positively with whole intestinal transit time (r\u200a=\u200a0.31, P\u200a<\u200a0.005) and inversely with bowel movement frequency (r\u200a=\u200a-0.245, P\u200a<\u200a0.05). Methane production (threshold 3 ppm) as a marker for identifying IBS-C had a sensitivity of 60% and specificity of 42.9%.\nLactulose breath test total methane production may serve as a biomarker of whole intestinal transit time and bowel movement frequency in children with IBS. In children with IBS, lactulose breath test hydrogen and methane production did not, however, correlate with abdominal pain, IBS subtype, or psychosocial distress.",
      "journal": "Journal of pediatric gastroenterology and nutrition",
      "year": "2017",
      "doi": "10.1097/MPG.0000000000001295",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/27276436/",
      "matched_queries": [
        "breath methane hydrogen colonic fermentation marker"
      ]
    },
    {
      "pmid": "27341456",
      "title": "Breath gas monitoring during a glucose challenge by a combined PTR-QMS/GC\u00d7GC-TOFMS approach for the verification of potential volatile biomarkers.",
      "abstract": "Breath gas profiles, which reflect metabolic disorders like diabetes, are the subject of scientific focus. Nevertheless, profiling is still a challenging task that requires complex and standardized methods. This study was carried out to verify breath gas patterns that were obtained in previous proton-transfer reaction-quadrupole mass spectrometry (PTR-QMS) studies and that can be linked to glucose metabolism. An experimental setup using simultaneous PTR-QMS and complementary highly time-resolved needle trap micro extraction (NTME) combined with comprehensive 2D gas chromatography-time-of-flight mass spectrometry (GC\u00d7GC-TOFMS) was established for the analysis of highly polar volatile organic compounds (VOCs). The method was applied to the breath gas analysis of three volunteers during a glucose challenge, whereby subjects ingested a glucose solution orally. Challenge responsive PTR-QMS target VOCs could be linked to small n-carbonic (C2-C4) alcohols and short chain fatty acids (SCFA). Specific isomers could be identified by simultaneously applied NTME-GC\u00d7GC-TOFMS and further verified by their characteristic time profiles and concentrations. The identified VOCs potentially originate from bacteria that are found in the oral cavity and gastrointestinal tract. In this study breath gas monitoring enabled the identification of potential VOC metabolites that can be linked to glucose metabolism.",
      "journal": "Journal of breath research",
      "year": "2016",
      "doi": "10.1088/1752-7155/10/3/036003",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/27341456/",
      "matched_queries": [
        "breath gas chromatography volatile fatty acids"
      ]
    },
    {
      "pmid": "27350657",
      "title": "Identification and quantification of antifungal compounds produced by lactic acid bacteria and propionibacteria.",
      "abstract": "Fungal growth in bakery products represents the most frequent cause of spoilage and leads to economic losses for industrials and consumers. Bacteria, such as lactic acid bacteria and propionibacteria, are commonly known to play an active role in preservation of fermented food, producing a large range of antifungal metabolites. In a previous study (Le Lay et al., 2016), an extensive screening performed both in vitro and in situ allowed for the selection of bacteria exhibiting an antifungal activity. In the present study, active supernatants against Penicillium corylophilum and Aspergillus niger were analyzed to identify and quantify the antifungal compounds associated with the observed activity. Supernatant treatments (pH neutralization, heating and addition of proteinase K) suggested that organic acids played the most important role in the antifungal activity of each tested supernatant. Different methods (HPLC, mass spectrometry, colorimetric and enzymatic assays) were then applied to analyze the supernatants and it was shown that the main antifungal compounds corresponded to lactic, acetic and propionic acids, ethanol and hydrogen peroxide, as well as other compounds present at low levels such as phenyllactic, hydroxyphenyllactic, azelaic and caproic acids. Based on these results, various combinations of the identified compounds were used to evaluate their effect on conidial germination and fungal growth of P. corylophilum and Eurotium repens. Some combinations presented the same activity than the bacterial culture supernatant thus confirming the involvement of the identified molecules in the antifungal activity. The obtained results suggested that acetic acid was mainly responsible for the antifungal activity against P. corylophilum and played an important role in E. repens inhibition.",
      "journal": "International journal of food microbiology",
      "year": "2016",
      "doi": "10.1016/j.ijfoodmicro.2016.06.020",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/27350657/",
      "matched_queries": [
        "short chain fatty acid colorimetric quantification"
      ]
    },
    {
      "pmid": "27545394",
      "title": "Vacuum ultraviolet absorption spectroscopy in combination with comprehensive two-dimensional gas chromatography for the monitoring of volatile organic compounds in breath gas: A feasibility study.",
      "abstract": "Vacuum ultraviolet (VUV) absorption spectroscopy was recently introduced as a new detection system for one, as well as comprehensive two-dimensional gas chromatography (GC\u00d7GC) and successfully applied to the analysis of various analytes in several matrices. In this study, its suitability for the analysis of breath metabolites was investigated and the impact of a finite volume of the absorption cell and makeup gas pressure was evaluated for volatile analytes in terms of sensitivity and chromatographic resolution. A commercial available VUV absorption spectrometer was coupled to GC\u00d7GC and applied to the analysis of highly polar volatile organic compounds (VOCs). Breath gas samples were acquired by needle trap micro extraction (NTME) during a glucose challenge and analysed by the applied technique. Regarding qualitative and quantitative information, the VGA-100 is compatible with common GC\u00d7GC detection systems like FID and even TOFMS. Average peak widths of 300ms and LODs in the lower ng range were achieved using GC\u00d7GC-VUV. Especially small oxygenated breath metabolites show intense and characteristic absorption patterns in the VUV region. Challenge responsive VOCs could be identified and monitored during a glucose challenge. The new VUV detection technology might especially be of benefit for applications in clinical research.",
      "journal": "Journal of chromatography. A",
      "year": "2016",
      "doi": "10.1016/j.chroma.2016.08.024",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/27545394/",
      "matched_queries": [
        "breath gas chromatography volatile fatty acids"
      ]
    },
    {
      "pmid": "28649044",
      "title": "Quantification and speciation of volatile fatty acids in the aqueous phase.",
      "abstract": "This study lays great emphasis on establishing a reliable analytical platform to quantify and specify volatile fatty acids (VFAs) in the aqueous phase by derivatizing VFAs into their corresponding alkyl esters via thermally-induced rapid esterification (only 10\u00a0s reaction time). To this end, reaction conditions for the thermally-induced rapid esterification are optimized. A volumetric ratio of 0.5\u00a0at 400\u00a0\u00b0C for VFA/methanol is identified as the optimal reaction conditions to give \u223c90% volatile fatty acid methyl ester (VFAME) yield. To maintain a high yield of VFAMEs, this study suggests that dilution of the sample to an optimum concentration (\u223c500\u00a0ppm for each VFA) is required. Derivatization of VFAs into VFAMEs via the thermally-induced rapid esterification is more reliable to quantify and specify VFAs in the aqueous phase than conventional colorimetric method.",
      "journal": "Environmental pollution (Barking, Essex : 1987)",
      "year": "2017",
      "doi": "10.1016/j.envpol.2017.06.042",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/28649044/",
      "matched_queries": [
        "short chain fatty acid colorimetric quantification"
      ]
    },
    {
      "pmid": "29224868",
      "title": "Technical note: Validation of the BHBCheck blood \u03b2-hydroxybutyrate meter as a diagnostic tool for hyperketonemia in dairy cows.",
      "abstract": "Accurate cow-side blood \u03b2-hydroxybutyrate (BHB) detection meters are valuable tools for rapid diagnosis of hyperketonemia. The main objective of this study was to compare the blood BHB measured in whole blood by the BHBCheck meter (PortaCheck, Moorestown, NJ) to a previously validated meter, Precision Xtra meter (Abbott Laboratories, Abbott Park, IL) and a colorimetric laboratory assay. Samples (n = 426) were collected from postpartum primiparous and multiparous Holstein cows (n = 79 cows) enrolled in 1 of 2 experiments (Exp) with different sampling schedules (Exp 1: n = 39 cows, 58 samples; Exp 2: n = 40 cows, 368 samples). In both Exp, whole-blood samples were collected from the coccygeal vessels after morning milking, before morning feeding. Blood samples were used immediately for BHB quantification via the BHBCheck meter and the Precision Xtra meter. Blood was also collected into evacuated tubes containing no additive (Exp 1) or potassium oxalate/sodium fluoride (Exp 2), which were centrifuged for serum or plasma separation and stored at -20\u00b0C for subsequent analysis. Laboratory quantification of BHB concentration was done by the BHB LiquiColor Assay (EKF Diagnostics-Stanbio, Boerne, TX; certified for serum and plasma). Data were analyzed by UNIVARIATE, CORR, FREQ, REG, and LOGISTIC procedures of SAS 9.4 (SAS Institute Inc., Cary, NC). Within this sample set, average parity was 3.3 lactations and DIM was 14 d. The proportion of samples classified as hyperketonemia (BHB \u22651.2 mmol/L) was 25, 28, and 31% as determined by the colorimetric assay, BHBCheck meter, and Precision Xtra meter, respectively. The correlation for BHBCheck meter BHB concentration compared with the colorimetric assay concentrations was r = 0.96, with a sensitivity of 91% and specificity of 93%. Correlation, sensitivity, and specificity of the Precision Xtra meter concentrations were 0.97, 98%, and 92%, respectively. Bland-Altman plots demonstrated minimal bias for both meters. Area under the receiver operator characteristic curve suggests adequate diagnostic accuracy of both meters. Overall, accuracy, sensitivity, and specificity of the BHBCheck meter was similar to the Precision Xtra meter and laboratory assay, indicating the BHBCheck meter is appropriate for use as a cow-side diagnostic test for hyperketonemia in dairy cows.",
      "journal": "Journal of dairy science",
      "year": "2018",
      "doi": "10.3168/jds.2017-13583",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/29224868/",
      "matched_queries": [
        "short chain fatty acid colorimetric quantification"
      ]
    },
    {
      "pmid": "29523768",
      "title": "Protein Acetylation and Butyrylation Regulate the Phenotype and Metabolic Shifts of the Endospore-forming Clostridium acetobutylicum.",
      "abstract": "Clostridium acetobutylicum is a strict anaerobic, endospore-forming bacterium, which is used for the production of the high energy biofuel butanol in metabolic engineering. The life cycle of C. acetobutylicum can be divided into two phases, with acetic and butyric acids being produced in the exponential phase (acidogenesis) and butanol formed in the stationary phase (solventogenesis). During the transitional phase from acidogenesis to solventogenesis and latter stationary phase, concentration peaks of the metabolic intermediates butyryl phosphate and acetyl phosphate are observed. As an acyl group donor, acyl-phosphate chemically acylates protein substrates. However, the regulatory mechanism of lysine acetylation and butyrylation involved in the phenotype and solventogenesis of C. acetobutylicum remains unknown. In our study, we conducted quantitative analysis of protein acetylome and butyrylome to explore the dynamic change of lysine acetylation and butyrylation in the exponential phase, transitional phase, and stationary phase of C. acetobutylicum Total 458 lysine acetylation sites and 1078 lysine butyrylation sites were identified in 254 and 373 substrates, respectively. Bioinformatics analysis uncovered the similarities and differences between the two acylation modifications in C. acetobutylicum Mutation analysis of butyrate kinase and the central transcriptional factor Spo0A was performed to characterize the unique role of lysine butyrylation in the metabolic pathway and sporulation process of C. acetobutylicum Moreover, quantitative proteomic assays were performed to reveal the relationship between protein features (e.g. gene expression level and lysine acylation level) and metabolites in the three growth stages. This study expanded our knowledge of lysine acetylation and butyrylation in Clostridia and constituted a resource for functional studies on lysine acylation in bacteria.",
      "journal": "Molecular & cellular proteomics : MCP",
      "year": "2018",
      "doi": "10.1074/mcp.RA117.000372",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/29523768/",
      "matched_queries": [
        "butyrate kinase enzymatic assay quantification"
      ]
    },
    {
      "pmid": "30416353",
      "title": "The roles of valerenic acid on BDNF expression in the SH-SY5Y cell.",
      "abstract": "The roots of Valeriana officinalis L. (Valerianaceae) are used for treating sleep disorders and/or mild nerve tension. The effect of valerenic acid on brain-derived neurotrophic factor (BDNF) has not yet been studied, although it is known that gamma-amino butyric acid A (GABAA) receptor is regulated by BDNF, which modulates the depressive-like behavior and neurogenesis. The purpose of this study is to determine the effect of V. officinalis root extract (VO), its main constituents valerenic acid (VA) and acetoxy valerenic acid (AVA) as well as valerenic acid-free (VAF), acetoxy valerenic acid-free (AVAF) extracts and increasing amounts of valerenic acid containing extracts on the BDNF expression in SH-SY5Y cell lines. The effect of methanolic extracts of VO, VA, AVA, VAF, AVAF, and the extracts whose amount of VA were increased gradually, were tested using a Human BDNF ELISA kit with 17\u03b2-estradiol as a positive control. The VO and VA extracts caused a significant (p\u202f<\u202f0.001) increase in the BDNF expression in SH-SY5Y cells compared to control. This effect completely disappeared when cells were treated with VAF extract. AVA alone did not show any significant change in the BDNF levels. The extracts with increasing amount of VA led to a concentration- dependent effect on the cells. In conclusion, our findings suggest that the antidepressant-like effect of the VO extract is also related to BDNF expression, and that this is mainly due to the presence of VA in the extract. Removing VA from VO extract leads to a loss of activity. Moreover, the concentration of VA plays a role for BDNF expressions in SH-SY5Y cells, which demonstrates the importance of quality control on the commercially available products.",
      "journal": "Saudi pharmaceutical journal : SPJ : the official publication of the Saudi Pharmaceutical Society",
      "year": "2018",
      "doi": "10.1016/j.jsps.2018.05.005",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/30416353/",
      "matched_queries": [
        "butyrate ELISA available commercial"
      ]
    },
    {
      "pmid": "30649345",
      "title": "Effects of high inclusion of soybean hulls on apparent total tract macronutrient digestibility, fecal quality, and fecal fermentative end-product concentrations in extruded diets of adult dogs.",
      "abstract": "Soybean hulls (SBH) are a fiber-rich co-product of the soybean oil extraction process that corresponds to 8% of the soybean seed. Despite being readily available and priced competitively, SBH are underutilized in monogastric nutrition. Thus, the objective of this study was to evaluate SBH as a dietary fiber in canine diets. Four diets were formulated with either SBH, beet pulp (BP), or cellulose (CL) as the main source of dietary fiber (15% total dietary fiber [TDF]), with the control diet formulated with no supplemental fiber (NF). Animal procedures were approved by the University of Illinois Institutional Animal Care and Use Committee. Eight adult female Beagle (mean age = 4.6 \u00b1 0.6 yr; mean BW = 12.8 \u00b1 1.7 kg) were used in a replicated 4 \u00d7 4 Latin square design. Each period consisted of 14 d, with 10 d of diet adaptation followed by 4 d of total fecal and urine collections. At the end of each period, a blood sample was collected and analyzed for serum chemistry. Food was offered twice daily and fed to maintain body weight. Food intake (g/d) on a dry matter basis (DMB) did not differ among treatments. Fecal score was lower (P < 0.05) for dogs fed CL (2.0) in contrast with other dietary treatments (2.3), using a 5-point scale (1 = hard, dry pellets; 5 = diarrhea). Fecal as-is and DM output did not differ for dogs fed BP, CL, or SBH, and were approximately 50% greater (P < 0.05) than dogs fed NF. Apparent total tract digestibility (ATTD) of dry matter, organic matter, and gross energy were greater (P < 0.05) for dogs fed NF when compared with dogs fed BP, CL, or SBH. Dogs fed CL had greater (P < 0.05) AHF ATTD (94%) compared with all other treatments (mean = 91%). Dogs fed CL and NF had greater (P < 0.05) CP ATTD, 87% and 86%, respectively, while dogs fed SBH were intermediate (83%) and dogs fed BP were lowest (79%). Total short-chain fatty acid (SCFA) concentration was greatest in dogs fed BP (582.5 \u03bcmol/g) and SBH (479.7 \u03bcmol/g) when compared with NF and CL (267.0 and 251.1 \u03bcmol/g, respectively). Serum metabolites were within-reference ranges and dogs remained healthy throughout the study. In conclusion, SBH resulted in similar macronutrient ATTD when compared with BP and CL. Dogs fed SBH were also observed to have an increase in fecal SCFA concentration. In general, high level addition of SBH were well-utilized by the dog, resulting in no untoward effects on dog health, nutrient digestibility, or fecal characteristics.",
      "journal": "Journal of animal science",
      "year": "2019",
      "doi": "10.1093/jas/skz015",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/30649345/",
      "matched_queries": [
        "point-of-care SCFA stool analysis"
      ]
    },
    {
      "pmid": "30699297",
      "title": "Mass-Spectrometry Analysis of Mixed-Breath, Isolated-Bronchial-Breath, and Gastric-Endoluminal-Air Volatile Fatty Acids in Esophagogastric Cancer.",
      "abstract": "A noninvasive breath test has the potential to improve survival from esophagogastric cancer by facilitating earlier detection. This study aimed to investigate the production of target volatile fatty acids (VFAs) in esophagogastric cancer through analysis of the ex vivo headspace above underivatized tissues and in vivo analysis within defined anatomical compartments, including analysis of mixed breath, isolated bronchial breath, and gastric-endoluminal air. VFAs were measured by PTR-ToF-MS and GC-MS. Levels of VFAs (acetic, butyric, pentanoic, and hexanoic acids) and acetone were elevated in ex vivo experiments in the headspace above esophagogastric cancer compared with the levels in samples from control subjects with morphologically normal and benign conditions of the upper gastrointestinal tract. In 25 patients with esophagogastric cancer and 20 control subjects, receiver-operating-characteristic analysis for the cancer-specific VFAs butyric acid ( P < 0.001) and pentatonic acid ( P = 0.005) within in vivo gastric-endoluminal air gave an area under the curve of 0.80 (95% confidence interval of 0.65 to 0.93, P = 0.01). Compared with mixed- and bronchial-breath samples, all examined VFAs were found in highest concentrations within esophagogastric-endoluminal air. In addition, VFAs were higher in all samples derived from cancer patients compared with in the controls. Equivalence of VFA levels within the mixed and bronchial breath of cancer patients suggests that their origin within breath is principally derived from the lungs and, by inference, from the\u00a0systemic circulation as opposed to direct passage from the upper gastrointestinal tract. These findings highlight the potential to utilize VFAs for endoluminal-gas biopsies and noninvasive mixed-exhaled-breath testing for esophagogastric-cancer detection.",
      "journal": "Analytical chemistry",
      "year": "2019",
      "doi": "10.1021/acs.analchem.9b00148",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/30699297/",
      "matched_queries": [
        "breath gas chromatography volatile fatty acids"
      ]
    },
    {
      "pmid": "30716067",
      "title": "Neuroprotective effects of PPAR\u03b1 in retinopathy of type 1 diabetes.",
      "abstract": "Diabetic retinopathy (DR) is a common neurovascular complication of type 1 diabetes. Current therapeutics target neovascularization characteristic of end-stage disease, but are associated with significant adverse effects. Targeting early events of DR such as neurodegeneration may lead to safer and more effective approaches to treatment. Two independent prospective clinical trials unexpectedly identified that the PPAR\u03b1 agonist fenofibrate had unprecedented therapeutic effects in DR, but gave little insight into the physiological and molecular mechanisms of action. The objective of the present study was to evaluate potential neuroprotective effects of PPAR\u03b1 in DR, and subsequently to identify the responsible mechanism of action. Here we reveal that activation of PPAR\u03b1 had a robust protective effect on retinal function as shown by Optokinetic tracking in a rat model of type 1 diabetes, and also decreased retinal cell death, as demonstrated by a DNA fragmentation ELISA. Further, PPAR\u03b1 ablation exacerbated diabetes-induced decline of visual function as demonstrated by ERG analysis. We further found that PPAR\u03b1 improved mitochondrial efficiency in DR, and decreased ROS production and cell death in cultured retinal neurons. Oxidative stress biomarkers were elevated in diabetic Ppar\u03b1-/- mice, suggesting increased oxidative stress. Mitochondrially mediated apoptosis and oxidative stress secondary to mitochondrial dysfunction contribute to neurodegeneration in DR. Taken together, these findings identify a robust neuroprotective effect for PPAR\u03b1 in DR, which may be due to improved mitochondrial function and subsequent alleviation of energetic deficits, oxidative stress and mitochondrially mediated apoptosis.",
      "journal": "PloS one",
      "year": "2019",
      "doi": "10.1371/journal.pone.0208399",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/30716067/",
      "matched_queries": [
        "butyrate ELISA available commercial"
      ]
    },
    {
      "pmid": "31212318",
      "title": "Genetic parameters of plasma and ruminal volatile fatty acids in sheep fed alfalfa pellets and genetic correlations with enteric methane emissions1.",
      "abstract": "Animal-to-animal variation in methane (CH4) emissions determined in respiration chambers has a genetic basis, but rapid phenotyping methods that can be applied on-farm are required to enable increased genetic progress by the farming industry. Fermentation of carbohydrates in the rumen results in the formation of VFA with hydrogen (H2) as a byproduct that is used for CH4 formation. Generally, fermentation pathways leading to acetate are associated with the most H2 production, less H2 formation is associated with butyrate production, and propionate and valerate production are associated with reduced H2 production. Therefore, VFA may constitute a potential correlated proxy for CH4 emissions to enable high-throughput animal screening. The objective of the present study was to determine the genetic parameters for ruminal and plasma VFA concentrations in sheep fed alfalfa (Medicago sativa L.) pellets and their genetic (rg) and phenotypic (rp) correlations with CH4 emissions. Measurements of CH4 emissions in respiration chambers and ruminal (stomach tubing 18 h from last meal) and blood plasma (3 h post-feeding) VFA concentrations were made on 1,538 lambs from 5 birth years (2007 and 2009 to 2012) aged between 5 and 10 mo, while the animals were fed alfalfa pellets at 2.0 times maintenance requirements in 2 equal size meals (0900 and 1500 h). These measurements were repeated twice (rounds) 14 d apart. Mean (\u00b1 SD) CH4 production was 24.4 \u00b1 3.08 g/d, and the mean CH4 yield was 15.8 \u00b1 1.51 g/kg DMI. Mean concentration of total ruminal VFA was 52.2 mM, with concentrations of acetate, propionate and butyrate of 35.97, 8.83, and 4.02 mM, respectively. Ruminal total VFA concentration had heritability (h2) and repeatability estimates (\u00b1 SE) of 0.24 \u00b1 0.05 and 0.35 \u00b1 0.03, respectively, and similar estimates were found for acetate, propionate, and butyrate. Blood plasma concentrations of VFA had much lower estimates of h2 and repeatability than ruminal VFA. Genetic correlations with CH4 yield were greatest for total concentrations of ruminal VFA and acetate, with 0.54 \u00b1 0.12 and 0.56 \u00b1 0.12, respectively, which were much greater than their corresponding rp. The rp and rg of ruminal VFA proportions and blood VFAs with CH4 emissions were in general lower than for ruminal VFA concentrations. However, minor ruminal VFA proportions had also moderate rg with CH4 yield. Pre-feeding concentrations of total VFA and acetate were the strongest correlated proxies to select sheep that are genetically low CH4 emitters.",
      "journal": "Journal of animal science",
      "year": "2019",
      "doi": "10.1093/jas/skz162",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/31212318/",
      "matched_queries": [
        "breath hydrogen butyrate fermentation correlation"
      ]
    },
    {
      "pmid": "32319943",
      "title": "Analytical validation of a quantitative method for therapeutic drug monitoring on the Alinity\u00aec Abbott.",
      "abstract": "The aim of this study was to evaluate the analytical performance of the Alinity\u00aec Abbott compared to the Architect\u00ae immunoassay system for the determination of drugs having a narrow therapeutic index.\nValproic acid, amikacin, gentamicin, phenobarbital and vancomycin were analyzed using Particle-Enhanced Turbidimetric Inhibitor Immunoassay (Petinia), phenytoin and theophylline were analyzed using an immunoenzymatic method and a colorimetric method was performed to quantify lithium. The methods were validated according to the total error approach. Seven validation standards were analyzed in quintuplet during four days to establish the limits of the methods. Dilution integrity and interferences (hemolysis and high concentrations of bilirubin and lipids) were also tested. Depending on the analyte, the results obtained for twenty to forty patients on the Alinity\u00ae were compared to those obtained on the Architect\u00ae.\nThe bias and the coefficients of variation for repeatability and for intermediate precision were lower than 15% for all drugs. Accuracy profiles were acceptable (acceptance limits fixed at 30%) in the validated ranges. The lower limits of quantification (LLOQ) were similar to those determined by Abbott except for gentamicin for which we determined a LLOQ at 1.22 mg/L while Abbott determined it at 0.5 mg/L. All assays diluted linear and analyte concentrations were not affected by interferences. Concentrations obtained for real samples on the Alinity\u00aec are comparable to those obtained on the Architect\u00aeci.\nThe analytical validation of a method suitable for therapeutic drug monitoring of drugs on the Alinity\u00aec meets the requirements of European Medicines Agency.",
      "journal": "Annales de biologie clinique",
      "year": "2020",
      "doi": "10.1684/abc.2020.1535",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/32319943/",
      "matched_queries": [
        "short chain fatty acid colorimetric quantification"
      ]
    },
    {
      "pmid": "32900799",
      "title": "Prebiotics and Community Composition Influence Gas Production of the Human Gut Microbiota.",
      "abstract": "Prebiotics confer benefits to human health, often by promoting the growth of gut bacteria that produce metabolites valuable to the human body, such as short-chain fatty acids (SCFAs). While prebiotic selection has strongly focused on maximizing the production of SCFAs, less attention has been paid to gases, a by-product of SCFA production that also has physiological effects on the human body. Here, we investigate how the content and volume of gas production by human gut microbiota are affected by the chemical composition of the prebiotic and the community composition of the microbiota. We first constructed a linear system model based on mass and electron balance and compared the theoretical product ranges of two prebiotics, inulin and pectin. Modeling shows that pectin is more restricted in product space, with less potential for H2 but more potential for CO2 production. An ex vivo experimental system showed pectin degradation produced significantly less H2 than inulin, but CO2 production fell outside the theoretical product range, suggesting fermentation of fecal debris. Microbial community composition also impacted results: methane production was dependent on the presence of Methanobacteria, while interindividual differences in H2 production during inulin degradation were driven by a Lachnospiraceae taxon. Overall, these results suggest that both the chemistry of the prebiotic and the composition of the microbiota are relevant to gas production. Metabolic processes that are relatively prevalent in the microbiome, such as H2 production, will depend more on substrate, while rare metabolisms such as methanogenesis depend more strongly on microbiome composition.IMPORTANCE Prebiotic fermentation in the gut often leads to the coproduction of short-chain fatty acids (SCFAs) and gases. While excess gas production can be a potential problem for those with functional gut disorders, gas production is rarely considered during prebiotic design. In this study, we combined the use of theoretical models and an ex vivo experimental platform to illustrate that both the chemical composition of the prebiotic and the community composition of the human gut microbiota can affect the volume and content of gas production during prebiotic fermentation. Specifically, more prevalent metabolic processes such as hydrogen production were strongly affected by the oxidation state of the probiotic, while rare metabolisms such as methane production were less affected by the chemical nature of the substrate and entirely dependent on the presence of Methanobacteria in the microbiota.",
      "journal": "mBio",
      "year": "2020",
      "doi": "10.1128/mBio.00217-20",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/32900799/",
      "matched_queries": [
        "engineered probiotic SCFA production assay"
      ]
    },
    {
      "pmid": "33211958",
      "title": "Selective Butyrate Esterase Probe for the Rapid Colorimetric and Fluorogenic Identification of Moraxella catarrhalis.",
      "abstract": "Clinical identification of the pathogenic bacterium Moraxella catarrhalis in cultures relies on the detection of bacterial butyrate esterase (C4-esterase) using a coumarin-based fluorogenic substrate, 4-methylumbelliferyl butyrate. However, this classical probe may give false-positive responses because of its poor stability and lack of specificity. Here, we report a new colorimetric and fluorogenic probe design employing a meso-ester-substituted boron dipyrromethene (BODIPY) dye for the specific detection of C4-esterase activity expressed by M. catarrhalis. This new probe has resistance to nonspecific hydrolysis that is far superior to the classical probe and also selectively responds to esterase with rapid colorimetric and fluorescence signal changes and large \"turn-on\" ratios. The probe was successfully applied to the specific detection of M. catarrhalis with high sensitivity.",
      "journal": "Analytical chemistry",
      "year": "2020",
      "doi": "10.1021/acs.analchem.0c03671",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/33211958/",
      "matched_queries": [
        "butyrate ester hydrolysis colorimetric"
      ]
    },
    {
      "pmid": "33509465",
      "title": "Aroma characteristics of cloudy kiwifruit juices treated with high hydrostatic pressure and representative thermal processes.",
      "abstract": "The commercial kiwifruit juice is deficient in a theoretical basis for the control of aroma characteristics during sterilization. To investigate the different sterilization methods on the aroma of kiwifruit juice, three sterilized kiwifruit juice samples, including pasteurization (PS), high temperature short time (HTST) and high hydrostatic pressure (HHP) sterilization, were observed. Results showed that a total of 15 major aroma-active compounds were identified in fresh kiwifruit juice by combination of detection frequency (DF) analysis and odor activity value (OAV); while the changes of these aroma-active compounds during PS, HTST and HHP sterilization were further studied. Quantitative descriptive analysis (QDA) was applied to validate the sensory differences, showing fruity and grassy notes changed a lot after sterilization, and the HHP sample was similar to fresh sample (FS) in comparison of samples treated by other sterilization methods. Further partial least squares regression analysis (PLSR) coincided with the overall note. Among these aroma-active compounds, the decrease of C6 aldehydes and C6 alcohols such as hexanal, (E)-2-hexenal and 1-hexanol might result in the great change of grassy note while the change of fruity note might be well correlated with the decrease of esters such as methyl butyrate and ethyl butyrate during processing.",
      "journal": "Food research international (Ottawa, Ont.)",
      "year": "2021",
      "doi": "10.1016/j.foodres.2020.109841",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/33509465/",
      "matched_queries": [
        "butyrate assay GC-MS comparison validation method correlation"
      ]
    },
    {
      "pmid": "33671147",
      "title": "Resistant Starch Type 2 from Wheat Reduces Postprandial Glycemic Response with Concurrent Alterations in Gut Microbiota Composition.",
      "abstract": "The majority of research on the physiological effects of dietary resistant starch type 2 (RS2) has focused on sources derived from high-amylose maize. In this study, we conduct a double-blind, randomized, placebo-controlled, crossover trial investigating the effects of RS2 from wheat on glycemic response, an important indicator of metabolic health, and the gut microbiota. Overall, consumption of RS2-enriched wheat rolls for one week resulted in reduced postprandial glucose and insulin responses relative to conventional wheat when participants were provided with a standard breakfast meal containing the respective treatment rolls (RS2-enriched or conventional wheat). This was accompanied by an increase in the proportions of bacterial taxa Ruminococcus and Gemmiger in the fecal contents, reflecting the composition in the distal intestine. Additionally, fasting breath hydrogen and methane were increased during RS2-enriched wheat consumption. However, although changes in fecal short-chain fatty acid (SCFA) concentrations were not significant between control and RS-enriched wheat roll consumption, butyrate and total SCFAs were positively correlated with relative abundance of Faecalibacterium, Ruminoccocus, Roseburia, and Barnesiellaceae. These effects show that RS2-enriched wheat consumption results in a reduction in postprandial glycemia, altered gut microbial composition, and increased fermentation activity relative to wild-type wheat.",
      "journal": "Nutrients",
      "year": "2021",
      "doi": "10.3390/nu13020645",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/33671147/",
      "matched_queries": [
        "breath hydrogen butyrate fermentation correlation"
      ]
    },
    {
      "pmid": "33765666",
      "title": "Investigation of the relationship between skin-emitted volatile fatty acids and skin surface acidity in healthy participants-a pilot study.",
      "abstract": "Volatile organic compounds (VOCs) emitted from human skin are of great interest in general in research fields including disease diagnostics and comprise various compound classes including acids, alcohols, ketones and aldehydes. The objective of this research is to investigate the volatile fatty acid (VFA) emission as recovered from healthy participant skin VOC samples and to characterise its association with skin surface acidity. VOC sampling was performed via headspace-solid phase microextraction with analysis via gas chromatography-mass spectrometry. Several VFAs were recovered from participants, grouped based on gender and site (female forehead, female forearm, male forearm). Saturated VFAs (C9, C12, C14, C15, C16) and the unsaturated VFA C16:1 (recovered only from the female forehead) were considered for this study. VFA compositions and abundances are discussed in the context of body site and corresponding gland type and distribution, and their quantitative association with skin acidity investigated. Normalised chromatographic peak areas of the recovered VFAs were found to linearly correlate with hydrogen ion concentration measured at each of the different sites considered and is the first report to our knowledge to demonstrate such an association. Our observations are explained in terms of the free fatty acid content at the skin surface which is well-established as being a major contributor to skin surface acidity. Furthermore, it is interesting to consider that these VFA emissions from skin, governed by equilibrium vapour pressures exhibited at the skin surface, will be dependent on skin pH. It is proposed that these pH-modulated equilibrium vapour pressures of the acids could be resulting in an enhanced VFA emission sensitivity with respect to skin surface pH. To translate our observations made here for future wearable biodiagnostic applications, the measurement of skin surface pH based on the volatile emission was demonstrated using a pH indicator dye in the form of a planar colorimetric sensor, which was incorporated into a wearable platform and worn above the palm surface. As acidic skin surface pH is required for optimal skin barrier function and cutaneous antimicrobial defence, it is envisaged that these colorimetric volatile acid sensors could be deployed in robust wearable formats for monitoring health and disease applications in the future.",
      "journal": "Journal of breath research",
      "year": "2021",
      "doi": "10.1088/1752-7163/abf20a",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/33765666/",
      "matched_queries": [
        "breath gas chromatography volatile fatty acids"
      ]
    },
    {
      "pmid": "33957773",
      "title": "Sustained Dysbiosis and Decreased Fecal Short-Chain Fatty Acids after Traumatic Brain Injury and Impact on Neurologic Outcome.",
      "abstract": "Traumatic brain injury (TBI) alters microbial populations present in the gut, which may impact healing and tissue recovery. However, the duration and impact of these changes on outcome from TBI are unknown. Short-chain fatty acids (SCFAs), produced by bacterial fermentation of dietary fiber, are important signaling molecules in the microbiota gut-brain axis. We hypothesized that TBI would lead to a sustained reduction in SCFA producing bacteria, fecal SCFAs concentration, and administration of soluble SCFAs would improve functional outcome after TBI. Adult mice (n\u2009=\u200910) had the controlled cortical impact (CCI) model of TBI performed (6\u2009m/sec, 2-mm depth, 50-msec dwell). Stool samples were collected serially until 28 days after CCI and analyzed for SCFA concentration by high-performance liquid chromatography-mass spectrometry/mass spectrometry and microbiome analyzed by 16S gene sequencing. In a separate experiment, mice (n\u2009=\u200910/group) were randomized 2 weeks before CCI to standard drinking water or water supplemented with the SCFAs acetate (67.5\u2009mM), propionate (25.9\u2009mM), and butyrate (40\u2009mM). Morris water maze performance was assessed on post-injury Days 14-19. Alpha diversity remained stable until 72\u2009h, at which point a decline in diversity was observed without recovery out to 28 days. The taxonomic composition of post-TBI fecal samples demonstrated depletion of bacteria from Lachnospiraceae, Ruminococcaceae, and Bacteroidaceae families, and enrichment of bacteria from the Verrucomicrobiaceae family. Analysis from paired fecal samples revealed a reduction in total SCFAs at 24\u2009h and 28 days after TBI. Acetate, the most abundant SCFA detected in the fecal samples, was reduced at 7 days and 28 days after TBI. SCFA administration improved spatial learning after TBI versus standard drinking water. In conclusion, TBI is associated with reduced richness and diversity of commensal microbiota in the gut and a reduction in SCFAs detected in stool. Supplementation of soluble SCFAs improves spatial learning after TBI.",
      "journal": "Journal of neurotrauma",
      "year": "2021",
      "doi": "10.1089/neu.2020.7506",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/33957773/",
      "matched_queries": [
        "point-of-care SCFA stool analysis"
      ]
    },
    {
      "pmid": "34348140",
      "title": "Ketogenesis impact on liver metabolism revealed by proteomics of lysine \u03b2-hydroxybutyrylation.",
      "abstract": "Ketone bodies are bioactive metabolites that function as energy substrates, signaling molecules, and regulators of histone modifications. \u03b2-hydroxybutyrate (\u03b2-OHB) is utilized in lysine \u03b2-hydroxybutyrylation (Kbhb) of histones, and associates with starvation-responsive genes, effectively coupling ketogenic metabolism with gene expression. The emerging diversity of the lysine acylation landscape prompted us to investigate the full proteomic impact of Kbhb. Global protein Kbhb is induced in a tissue-specific manner by a variety of interventions that evoke \u03b2-OHB. Mass spectrometry analysis of the \u03b2-hydroxybutyrylome in mouse liver revealed 891 sites of Kbhb within 267 proteins enriched for fatty acid, amino acid, detoxification, and one-carbon metabolic pathways. Kbhb inhibits S-adenosyl-L-homocysteine hydrolase (AHCY), a rate-limiting enzyme of the methionine cycle, in parallel with altered metabolite levels. Our results illuminate the role of Kbhb in hepatic metabolism under ketogenic conditions and demonstrate a functional consequence of this modification on a central metabolic enzyme.",
      "journal": "Cell reports",
      "year": "2021",
      "doi": "10.1016/j.celrep.2021.109487",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/34348140/",
      "matched_queries": [
        "NADH coupled butyrate assay"
      ]
    },
    {
      "pmid": "34648892",
      "title": "Kinetic model of Clostridium beijerinckii's Acetone-Butanol-Ethanol fermentation considering metabolically diverse cell types.",
      "abstract": "Clostridium beijerinckii population branches into metabolically diverse cell types in batch cultures. Here, we present a new kinetic model of C. beijerinckii's Acetone-Butanol-Ethanol fermentation that considers three cell types: producers of acids (acidogenic), consumer of acids and producers of solvents (solventogenic), and spores cells. The model accurately recapitulates batch culture data. Also, the model estimates cell type-specific kinetic parameters, which can be helpful to improve the operation of the ABE fermentation and give a framework to study acidogenic and solventogenic metabolic pathways. To exemplify the latter, we used a constraint-based model to study how the ABE pathways are used among acidogenic and solventogenic cell types. We found that among both cell types, glycolytic production of ATP and consumption of NAD+ varies widely during the fermentation, with their maximum production/consumption rates happening when acidogenic and solventogenic growth rates were at their highest. However, acidogenic cells use the ABE pathway to contribute with an extra 12.5% of the total production of ATP, whereas solventogenic cell types use the ABE pathway to supply more than 75% of the demand for NAD+, alternating between the production of lactate and butyrate, being both coupled to the production of NAD+.",
      "journal": "Journal of biotechnology",
      "year": "2021",
      "doi": "10.1016/j.jbiotec.2021.09.021",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/34648892/",
      "matched_queries": [
        "NADH coupled butyrate assay"
      ]
    },
    {
      "pmid": "3503522",
      "title": "Bioluminescent assay of D-3-hydroxybutyrate in serum.",
      "abstract": "An enzymatic assay of D-3-hydroxybutyrate in which the hydroxybutyrate dehydrogenase reaction is coupled to the bacterial oxidoreductase-luciferase system is described. The bioluminescent assay is based on either, end-point, or on initial velocity measurements. This simple and rapid assay requires a single serum sample of 10 microliters. Its linear range covers two orders of magnitude from 10(-6) mol/l upwards. This assay is suitable for the routine determination of D-3-hydroxybutyrate in human blood with good accuracy.",
      "journal": "Journal of bioluminescence and chemiluminescence",
      "year": "1986",
      "doi": "10.1002/bio.1170010104",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/3503522/",
      "matched_queries": [
        "NADH coupled butyrate assay"
      ]
    },
    {
      "pmid": "35276942",
      "title": "Health Effects of Drinking Water Produced from Deep Sea Water: A Randomized Double-Blind Controlled Trial.",
      "abstract": "Global trends focus on a balanced intake of foods and beverages to maintain health. Drinking water (MIU; hardness = 88) produced from deep sea water (DSW) collected offshore of Muroto, Japan, is considered healthy. We previously reported that the DSW-based drinking water (RDSW; hardness = 1000) improved human gut health. The aim of this randomized double-blind controlled trial was to assess the effects of MIU on human health. Volunteers were assigned to MIU (n = 41) or mineral water (control) groups (n = 41). Participants consumed 1 L of either water type daily for 12 weeks. A self-administered questionnaire was administered, and stool and urine samples were collected throughout the intervention. We measured the fecal biomarkers of nine short-chain fatty acids (SCFAs) and secretory immunoglobulin A (sIgA), as well as urinary isoflavones. In the MIU group, concentrations of three major SCFAs and sIgA increased postintervention. MIU intake significantly affected one SCFA (butyric acid). The metabolic efficiency of daidzein-to-equol conversion was significantly higher in the MIU group than in the control group throughout the intervention. MIU intake reflected the intestinal environment through increased production of three major SCFAs and sIgA, and accelerated daidzein-to-equol metabolic conversion, suggesting the beneficial health effects of MIU.",
      "journal": "Nutrients",
      "year": "2022",
      "doi": "10.3390/nu14030581",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/35276942/",
      "matched_queries": [
        "fecal SCFA self-administered measurement"
      ]
    },
    {
      "pmid": "35505080",
      "title": "Probiotic supplementation for neonates with congenital gastrointestinal surgical conditions: guidelines for future research.",
      "abstract": "Our pilot RCT found that probiotic supplementation with the three-strain bifidobacterial product (B. breve M-16V, B. longum subsp. infantis M-63 and B. longum subsp. longum BB536) attenuates gut dysbiosis, increases stool short-chain fatty acid (SCFA) levels and improves the growth of head circumference in neonates with congenital gastrointestinal surgical conditions (CGISC). In this article, we have provided guidelines for designing future multicentre RCTs based on the experience gained from our pilot RCT. The recommendations include advice about sample size, potential confounders, outcomes of interest, probiotic strain selection, storage, dose, duration and microbial quality assurance, collection of stool samples, storage and analysis and reporting. Following these guidelines will increase the validity of future RCTs in this area and hence confidence in their results. IMPACT: Probiotic supplementation attenuates gut dysbiosis, increases stool short-chain fatty acid (SCFA) levels and improves the growth of head circumference in neonates with congenital gastrointestinal surgical conditions. The current review provides evidence-based guidelines to conduct adequately powered RCTs in this field.",
      "journal": "Pediatric research",
      "year": "2023",
      "doi": "10.1038/s41390-022-02087-8",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/35505080/",
      "matched_queries": [
        "engineered probiotic SCFA production assay"
      ]
    },
    {
      "pmid": "35752796",
      "title": "Model-based driving mechanism analysis for butyric acid production in Clostridium tyrobutyricum.",
      "abstract": "Butyric acid, an essential C4 platform chemical, is widely used in food, pharmaceutical, and animal feed industries. Clostridium tyrobutyricum is the most promising microorganism for industrial bio-butyrate production. However, the metabolic driving mechanism for butyrate synthesis was still not profoundly studied.\nThis study reports a first-generation genome-scale model (GEM) for C. tyrobutyricum, which provides a comprehensive and systematic analysis for the butyrate synthesis driving mechanisms. Based on the analysis in silico, an energy conversion system, which couples the proton efflux with butyryl-CoA transformation by two redox loops of ferredoxin, could be the main driving force for butyrate synthesis. For verifying the driving mechanism, a hydrogenase (HydA) expression was perturbed by inducible regulation and knockout. The results showed that HydA deficiency significantly improved the intracellular NADH/NAD+ rate, decreased acetate accumulation (63.6% in serum bottle and 58.1% in bioreactor), and improved the yield of butyrate (26.3% in serum bottle and 34.5% in bioreactor). It was in line with the expectation based on the energy conversion coupling driving mechanism.\nThis work show that the first-generation GEM and coupling metabolic analysis effectively promoted in-depth understanding of the metabolic driving mechanism in C. tyrobutyricum and provided a new insight for tuning metabolic flux direction in Clostridium chassis cells.",
      "journal": "Biotechnology for biofuels and bioproducts",
      "year": "2022",
      "doi": "10.1186/s13068-022-02169-z",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/35752796/",
      "matched_queries": [
        "NADH coupled butyrate assay"
      ]
    },
    {
      "pmid": "35839206",
      "title": "Enzymatic measurement of short-chain fatty acids and application in periodontal disease diagnosis.",
      "abstract": "Periodontal disease is a chronic inflammatory condition caused by periodontal pathogens in the gingival sulcus. Short-chain fatty acids (SCFAs) produced by causal bacteria are closely related to the onset and progression of periodontal disease and have been reported to proliferate in the periodontal sulcus of patients experiencing this pathology. In such patients, propionic acid (C3), butyric acid (C4), isobutyric acid (IC4), valeric acid (C5), isovaleric acid (IC5), and caproic acid (C6), henceforth referred to as [C3-C6], has been reported to have a detrimental effect, while acetic acid (C2) exhibits no detrimental effect. In this study, we established an inexpensive and simple enzymatic assay that can fractionate and measure these acids. The possibility of applying this technique to determine the severity of periodontal disease by adapting it to specimens collected from humans has been explored. We established an enzyme system using acetate kinase and butyrate kinase capable of measuring SCFAs in two fractions, C2 and [C3-C6]. The gingival crevicular fluid (GCF) and saliva of 10 healthy participants and 10 participants with mild and severe periodontal disease were measured using the established enzymatic method and conventional gas chromatography-mass spectrometry (GC-MS). The quantification of C2 and [C3-C6] in human GCF and saliva was well correlated when using the GC-MS method. Furthermore, both C2 and [C3-C6] in the GCF increased with disease severity. However, while no significant difference was observed between healthy participants and periodontal patients when using saliva, [C3-C6] significantly differed between mild and severe periodontal disease. The enzymatic method was able to measure C2 and [C3-C6] separately as well as using the GC-MS method. Furthermore, the C2 and [C3-C6] fractions of GCF correlated with disease severity, suggesting that this method can be applied clinically. In contrast, the quantification of C2 and [C3-C6] in saliva did not differ significantly between healthy participants and patients with periodontal disease. Future studies should focus on inflammation rather than on tissue destruction.",
      "journal": "PloS one",
      "year": "2022",
      "doi": "10.1371/journal.pone.0268671",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/35839206/",
      "matched_queries": [
        "butyrate kinase enzymatic assay quantification"
      ]
    },
    {
      "pmid": "36055216",
      "title": "Volatile composition of the morning breath.",
      "abstract": "We have measured the composition of volatile organic compounds (VOCs) in the morning breath of 30 healthy individuals before and after tooth brushing. The concentrations of VOCs in the breath samples were measured with proton-transfer-reaction time-of-flight mass spectrometry (MS) and further identification was performed with a combination of solid phase microextraction and offline gas chromatography-MS. We hypothesize that compounds, whose concentrations significantly decreased in the breath after tooth brushing are largely of microbial origin. In this study, we found 35 such VOCs. Out of these, 33 have been previously connected to different oral niches, such as salivary and subgingival bacteria. We also compared the concentrations of the 35 VOCs found in increased amounts in the morning breath to their respective odor thresholds to evaluate their ability to cause odor. Compounds that could contribute to the breath odor include many volatile sulfur compounds, such as methanethiol, hydrogen sulfide, dimethyl sulfide, and 2-methyl-1-propanethiol, but also other VOCs, such as acetic acid, butyric acid, valeric acid, acetaldehyde, octanal, phenol, indole, ammonia, isoprene, and methyl methacrylate.",
      "journal": "Journal of breath research",
      "year": "2022",
      "doi": "10.1088/1752-7163/ac8ec8",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/36055216/",
      "matched_queries": [
        "breath gas chromatography volatile fatty acids"
      ]
    },
    {
      "pmid": "36221245",
      "title": "Associations between postprandial symptoms, hydrogen and methane production, and transit time in irritable bowel syndrome.",
      "abstract": "Abnormal oroanal transit time (OATT) and visceral hypersensitivity are key pathophysiological factors in irritable bowel syndrome (IBS). The lactulose nutrient challenge test (LNCT) has been developed to assess the postprandial symptoms and gut microbial fermentation. We aimed to investigate associations between OATT, rectal sensitivity, and LNCT in IBS patients.\nWe included 263 IBS patients from two study cohorts, where the link between pathophysiology and symptoms was investigated. During the LNCT, severity of postprandial symptoms was graded, and breath hydrogen/methane concentrations were measured after ingestion of a combined lactulose nutrient drink every 15\u2009min for 4\u00a0h. The patients underwent rectal sensitivity (rectal barostat) and OATT (radiopaque markers) investigations. Comorbid conditions (functional dyspepsia, anxiety, depression, and somatization) were assessed with questionnaires.\nAfter controlling for comorbid conditions, rectal sensitivity was associated with abdominal pain (p\u2009<\u20090.05), and more rapid OATT was associated with higher severity of abdominal discomfort, rumbling, nausea, and urgency (p\u2009<\u20090.05 for all) both pre- and post-prandially. Postprandial nausea, urgency, and abdominal pain changed differently over time depending on OATT (p\u2009<\u20090.05 for all). OATT, but not rectal sensitivity, was associated with hydrogen and methane concentrations (p\u00a0=\u00a00.002 for both). Trajectories over time of postprandial symptoms and exhaled hydrogen/methane concentrations were correlated with different correlations depending on OATT.\nThis study highlights the importance of oroanal transit and hydrogen and methane production in the pathophysiology of IBS and increases our understanding of pathophysiological factors involved in postprandial symptom generation. Treatments targeting oroanal transit and hydrogen and methane production may improve specific postprandial symptoms.",
      "journal": "Neurogastroenterology and motility",
      "year": "2023",
      "doi": "10.1111/nmo.14482",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/36221245/",
      "matched_queries": [
        "breath methane hydrogen colonic fermentation marker"
      ]
    },
    {
      "pmid": "36436717",
      "title": "Antioxidant, anti-inflammatory and analgesic activity of Mimosa acutistipula (Mart.) Benth.",
      "abstract": "Medicinal plants belonging to the genus Mimosa, such as Mimosa tenuiflora, M. caesalpinifolia, and M. verrucosa are known for their popular use for asthma, bronchitis and fever. Ethnopharmacological studies report that Mimosa acutistipula is used to treat alopecia and pharyngitis, conditions that can be related to oxidative stress, inflammatory processes and painful limitations. However, there is no studies on its efficacy and mechanism of action.\nTo elucidate the antioxidant, anti-inflammatory, analgesic and antipyretic activity of M. acutistipula leaves.\nPhytochemical profile of M. acutistipula extracts was evaluated by several reaction-specific methods. Secondary metabolites such as tannins, phenols and flavonoids were quantified with colorimetric assays. In vitro antioxidant potential was evaluated using DPPH and ABTS\u00a0+\u00a0as free radical scavenging tests, FRAP and phosphomolybdenum as oxide-reduction assays, and anti-hemolytic for lipid peroxidation evaluation. In vivo anti-inflammatory evaluation was performed by paw edema, and peritonitis induced by carrageenan. Analgesic effect and its possible mechanisms were determined by acetic acid-induced abdominal writhing and the formalin test. Antipyretic activity was evaluated by yeast-induced fever.\nCyclohexane, chloroform, ethyl acetate and methanol extracts of leaves had presence of tannins, flavonoids, phenol, alkaloids, terpenes (except methanolic extract), and saponins (only for methanolic and chloroformic extracts). In phenols, flavonoids and tannins quantification, methanolic and ethyl acetate extract had higher amounts of this phytocompounds. Ethyl acetate extract, due to its more expressive quantity of phenols and flavonoids, was chosen for carrying out the in vivo tests. Due to the relationship between oxidative stress and inflammation, antioxidant tests were performed, showing that ethyl acetate extract had a high total antioxidant activity (70.18%), moderate activity in DPPH radical scavenging, and a moderate ABTS\u00a0+\u00a0radical inhibition (33.61%), and FRAP assay (112.32\u00a0\u03bcg Fe2+/g). M. acutistipula showed anti-inflammatory activity, with 54.43% of reduction in paw edema (50\u00a0mg/kg) when compared to the vehicle. In peritonitis test, a reduction in the concentration of NO could be seen, which is highly involved in the anti-inflammatory activity and is responsible for the increase in permeability. In the analgesic evaluation, most significant results in writhing test were seen at 100\u00a0mg/kg, with a 34.7% reduction of writhing. A dual mechanism of action was confirmed with the formalin test, both neurogenic and inflammatory pain were reduced, with a mechanism via opioid route. In the antipyretic test, results were significantly decreased at all concentrations tested.\nM. acutistipula leaves ethyl acetate extract showed expressive concentrations of phenolic compounds and antioxidant activity. It also exhibited anti-inflammatory and analgesic activity, besides its antipyretic effect. Thus, these results provide information regarding its popular use and might help future therapeutics involving this specimen.",
      "journal": "Journal of ethnopharmacology",
      "year": "2023",
      "doi": "10.1016/j.jep.2022.115964",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/36436717/",
      "matched_queries": [
        "short chain fatty acid colorimetric quantification"
      ]
    },
    {
      "pmid": "37093514",
      "title": "Pro-pre and Postbiotic\u00a0Fermentation of the Dietetic Dairy Matrix with Prebiotic Sugar Replacers.",
      "abstract": "In this study, bacterial growth, postbiotic short-chain fatty acids\u00a0(SCFAs) formation,\u00a0and gelation properties of sugar-free probiotic milk gels produced with stevia and inulin as a sugar replacer and synbiotic interactions were investigated with regard to prebiotic/bio-therapeutic potential and consumer preference. Lactobacillus acidophilus and Bifidobacterium animalis subsp. lactis cultures were used in the manufacture of dietetic milk gels. The addition of stevia and inulin promoted the viability of bacteria and enhanced milk gel firmness throughout its shelf life. The activity of the probiotic bacteria was identified to be within the potential prebiotic effects (>\u20098.30 log10 cfu mL-1) in\u00a0a food matrix. However, it was determined that especially stevia and stevia\u2009+\u2009inulin addition increased the survival rate of probiotic bacteria and in vitro total SCFA production with higher scores for consumers' preferences rather than with the addition of stevia alone. Yoghurts containing B. animalis subsp. lactis have improved the instrumental textural properties, whereas yoghurts containing L. acidophilus had higher scores for sensorial attributes.",
      "journal": "Probiotics and antimicrobial proteins",
      "year": "2024",
      "doi": "10.1007/s12602-023-10069-3",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/37093514/",
      "matched_queries": [
        "engineered probiotic SCFA production assay"
      ]
    },
    {
      "pmid": "37370057",
      "title": "Butyrate inhibits the mitochondrial complex \u0399 to mediate mitochondria-dependent apoptosis of cervical cancer cells.",
      "abstract": "Cervical cancer (CC) is a common gynecological malignancy with high morbidity worldwide. Butyrate, a short-chain fatty acid produced by intestinal flora, has been reported to inhibit cervical carcinogenesis. This study aimed to investigate the pro-apoptotic effects of butyrate on CC and the underlying mechanisms.\nHuman HeLa and Ca Ski cells were used in this study. Cell proliferation, cell migration and invasion were detected by CCK-8 and EdU staining, transwell and wound healing assay, respectively. Cell cycle, mitochondrial membrane potential and apoptosis were evaluated by flow cytometry. Western blot and RT-qPCR were carried out to examine the related genes and proteins to the mitochondrial complex \u0399 and apoptosis. Metabolite changes were analyzed by energy metabolomics and assay kits. The association between G protein-coupled receptor 41, 43, 109a and CC prognosis was analyzed using data from The Cancer Genome Atlas (TCGA).\nCCK-8 results showed significant inhibition of CC cell proliferation induced by butyrate treatment, which was confirmed by EdU staining and cell cycle detection. Data from the transwell and wound healing assay revealed that CC cell migration was dramatically reduced following butyrate treatment. Additionally, invasiveness was also decreased by butyrate. Western blot analysis showed that cleaved Caspase 3 and cleaved PARP, the enforcers of apoptosis, were increased by butyrate treatment. The results of Annexin V/PI staining and TUNEL also showed an increase in butyrate-induced apoptotic cells. Expression of Cytochrome C (Cytc), Caspase 9, Bax, but not Caspase 12 or 8, were up-regulated under butyrate exposure. Mechanistically, the decrease in mitochondrial NADH and NAD\u2009+\u2009levels after treatment with butyrate was observed by energy metabolomics and the NAD+/NADH Assay Kit, similar to the effects of the complex \u0399 inhibitor rotenone. Western blot results also demonstrated that the constituent proteins of mitochondrial complex \u0399 were reduced by butyrate. Furthermore, mitochondria-dependent apoptosis has been shown to be initiated by inhibition of the complex \u0399.\nCollectively, our results revealed that butyrate inhibited the proliferation, migration and invasion of CC cells, and induced mitochondrial-dependent apoptosis by inhibiting mitochondrial complex \u0399.",
      "journal": "BMC complementary medicine and therapies",
      "year": "2023",
      "doi": "10.1186/s12906-023-04043-3",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/37370057/",
      "matched_queries": [
        "NADH coupled butyrate assay"
      ]
    },
    {
      "pmid": "37864505",
      "title": "Cholesterol deficiency as a mechanism for autism: A valproic acid model.",
      "abstract": "Dysregulated cholesterol metabolism represents an increasingly recognized feature of autism spectrum disorder (ASD). Children with fetal valproate syndrome caused by prenatal exposure to valproic acid (VPA), an anti-epileptic and mood-stabilizing drug, have a higher incidence of developing ASD. However, the role of VPA in cholesterol homeostasis in neurons and microglial cells remains unclear. Therefore, we examined the effect of VPA exposure on regulation of cholesterol homeostasis in the human microglial clone 3 (HMC3) cell line and the human neuroblastoma cell line SH-SY5Y. HMC3 and SH-SY5Y cells were each incubated in increasing concentrations of VPA, followed by quantification of mRNA and protein expression of cholesterol transporters and cholesterol metabolizing enzymes. Cholesterol efflux was evaluated using colorimetric assays. We found that VPA treatment in HMC3 cells significantly reduced ABCA1 mRNA, but increased ABCG1 and CD36 mRNA levels in a dose-dependent manner. However, ABCA1 and ABCG1 protein levels were reduced by VPA in HMC3. Furthermore, similar experiments in SH-SY5Y cells showed increased mRNA levels for ABCA1, ABCG1, CD36, and 27-hydroxylase with VPA treatment. VPA exposure significantly reduced protein levels of ABCA1 in a dose-dependent manner, but increased the ABCG1 protein level at the highest dose in SH-SY5Y cells. In addition, VPA treatment significantly increased cholesterol efflux in SH-SY5Y, but had no impact on efflux in HMC3. VPA differentially controls the expression of ABCA1 and ABCG1, but regulation at the transcriptional and translational levels are not consistent and changes in the expression of these genes do not correlate with cholesterol efflux in vitro.",
      "journal": "Journal of investigative medicine : the official publication of the American Federation for Clinical Research",
      "year": "2024",
      "doi": "10.1177/10815589231210521",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/37864505/",
      "matched_queries": [
        "short chain fatty acid colorimetric quantification"
      ]
    },
    {
      "pmid": "38295385",
      "title": "In\u00a0Vivo Inhibition of Dipeptidyl Peptidase 4 Allows Measurement of GLP-1 Secretion in Mice.",
      "abstract": "Dipeptidyl peptidase 4 (DPP-4) and neprilysin (NEP) rapidly degrade glucagon-like peptide 1 (GLP-1) in mice. Commercially available sandwich ELISA kits may not accurately detect the degradation products, leading to potentially misleading results. We aimed to stabilize GLP-1 in mice, allowing reliable measurement with sensitive commercially available ELISA kits. Nonanesthetized male C57Bl/6JRj mice were subjected to an oral glucose tolerance test (OGTT; 2 g/kg glucose), and plasma total and intact GLP-1 were measured (Mercodia and Alpco ELISA kits, respectively). No GLP-1 increases were seen in samples taken beyond 15 min after the glucose load. Samples taken at 5 and 10 min after the OGTT showed a minor increase in total, but not intact, GLP-1. We then administered saline (control), or a DPP-4 inhibitor (valine pyrrolidide or sitagliptin) with or without an NEP-inhibitor (sacubitril), 30 min before the OGTT. In the inhibitor groups only, intact GLP-1 increased significantly during the OGTT. After injecting male C57Bl/6JRj mice with a known dose of GLP-1(7-36)NH2, peak GLP-1 levels were barely detectable after saline but were 5- to 10-fold higher during sitagliptin and the combination of sitagliptin/sacubitril. The half-life of the GLP-1 plasma disappearance increased up to sevenfold during inhibitor treatment. We conclude that reliable measurement of GLP-1 secretion is not possible in mice in\u00a0vivo with commercially available sandwich ELISA kits, unless degradation is prevented by inhibition of DPP-4 and perhaps NEP. The described approach allows improved estimates of GLP-1 secretion for future studies, although it is a limitation that these inhibitors additionally influence levels of insulin and glucagon.",
      "journal": "Diabetes",
      "year": "2024",
      "doi": "10.2337/db23-0848",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/38295385/",
      "matched_queries": [
        "butyrate ELISA available commercial"
      ]
    },
    {
      "pmid": "38503704",
      "title": "[Determination of organic acids and anions in exhaled breath by condensation collection-ion chromatography].",
      "abstract": "A non-invasive condensation collection-ion chromatography method was established for the determination of organic acids and anions including lactic acid, formic acid, acetic acid, pyruvic acid, chloride, nitrate, nitrite, and sulfate in the exhaled breath of humans. The breath exhaled was condensed and collected using a home-made exhaled breath condensation equipment. This equipment included a disposable mouthpiece as a blow-off port, one-way valve and flow meter, cold trap, disposable condensate collection tube placed in the cold trap, and gas outlet. A standard sampling procedure was used. Before collection, the collection temperature and sampling volume were set on the instrument control panel, and sampling was started when the cold-trap temperature dropped to the set value, while maintaining the balance. Subjects were required to gargle with pure water before sampling. During the sampling process, the subjects were required to inhale deeply until the lungs were full of gas and then exhale evenly through the air outlet. When the set volume was collected, the instrument made a prompt sound; then, the collection was immediately ended, the expiration time was recorded, and the average collection flow was calculated according to the expiration time and sampling volume. After collection, the disposable condensation collection tube was immediately taken out, sealed, and stored in the refrigerator at -20 \u2103 away from light, and immediately used for further testing. The organic acids and anions in exhaled breath condensation (EBC) were filtered through a 0.22 \u03bcm membrane filter before injection and detected by ion chromatography with conductivity detection. Factors such as collection temperature and collection flow rate during condensation collection were optimized. The optimal cooling temperature was set at -15 \u2103, and the optimal exhaled breath flow rate was set at 15 L/min. The mobile phase consisted of a mixture of sodium carbonate (1.5 mmol/L) and sodium bicarbonate (3 mmol/L). The flow rate was 0.8 mL/min, and the injection volume was 100 \u03bcL. An IC-SA3 column (250 mm\u00d74.0 mm) was used, and the temperature was set at 45 \u2103. An ICDS-40A electrodialysis suppressor was used, and the current was set at 150 mA. The linear ranges of the eight organic acids and anions were 0.1-10.0 mg/L; their correlation coefficients (r) were \u22650.9993. The limits of detection (LODs) for the eight organic acids and anions were 0.0017-0.0150 mg/L based on a signal-to-noise ratio of 3, and the limits of quantification (LOQs) were 0.0057-0.0500 mg/L based on a signal-to-noise ratio of 10. The intra-day precisions were 5.06%-6.33% (n=5), and the inter-day precisions were 5.37%-7.50% (n=5). This method was used to detect organic acids and anions in the exhaled breath of five healthy subjects. The contents of organic acids and anions in the exhaled breath were calculated. The content of lactic acid was relatively high, at 1.13-42.3 ng/L, and the contents of other seven organic acids and anions were 0.18-11.0 ng/L. During a 10 km-long run, the majority of organic acids and anions in the exhaled breath of five subjects first increased and then decreased. However, due to abnormal metabolism, the content changes of lactic acid, acetic acid, pyruvic acid and chloride in one subject were obviously different from others during exercise, showing a continuous rise. This method has the advantages of involving a simple sampling process and exhibiting good precision, few side effects, and no obvious discomfort or risk to the subjects. This study provides experimental ideas and a theoretical basis for future research on human metabolites.",
      "journal": "Se pu = Chinese journal of chromatography",
      "year": "2024",
      "doi": "10.3724/SP.J.1123.2023.07016",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/38503704/",
      "matched_queries": [
        "breath gas chromatography volatile fatty acids"
      ]
    },
    {
      "pmid": "38823224",
      "title": "Quantitative study on a simple electrochemical dsDNA-pregabalin biosensor; multi-spectroscopic, molecular docking and modelling studies.",
      "abstract": "Pregabalin (PGB) is a \u03b3-aminobutyric acid (GABA) alkylated analog prescribed to treat neuropathic pain, fibromyalgia, and postherpetic neuralgia. Using analytical, spectroscopic methods and molecular docking and molecular dynamics (MD) simulations, a detailed experimental and theoretical investigation was conducted into the binding process and interactions between PGB and double-stranded fish sperm deoxyribonucleic acid (dsDNA). It was evident from the collected experimental results that PGB binds with ds-DNA. PGB attaches to dsDNA via minor groove binding, as demonstrated by the results of electrochemical studies, UV-Vis absorption spectroscopy, and replacement study with ethidium bromide and Hoechst-32588. PGB's binding constant (Kb) with dsDNA, as determined by the Benesi-Hildebrand plot, is 2.41\u00d7104 \u00b1 0.30 at 298\u202fK. The fluorescence investigation indicates that PGB and dsDNA have a binding stoichiometry (n) of 1.21 \u00b1 0.09. Molecular docking simulations were used in the research to computational determination of the interactions between PGB and dsDNA. The findings demonstrated that minor groove binding was the mechanism by which PGB interacted with dsDNA. Based on the electrochemically responsive PGB-dsDNA biosensor, we developed a technique for low-concentration detection of PGB utilizing differential pulse voltammetry (DPV). The voltammetric analysis of the peak current decrease in the deoxyadenosine oxidation signals resulting from the association between PGB and dsDNA enabled a sensitive estimation of PGB in pH 4.80 acetate buffer. The deoxyguanosine oxidation signals exhibited a linear relationship between 2 and 16\u202f\u03bcM PGB. The values for the limit of detection (LOD) and limit of quantitation (LOQ) were 0.57\u202f\u03bcM and 1.91\u202f\u03bcM, respectively.",
      "journal": "Journal of pharmaceutical and biomedical analysis",
      "year": "2024",
      "doi": "10.1016/j.jpba.2024.116261",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/38823224/",
      "matched_queries": [
        "butyrate biosensor electrochemical quantification"
      ]
    },
    {
      "pmid": "38967859",
      "title": "Fabrication of Highly Sensitive and Selective Nitrite Colorimetric Sensor Based on the Enhanced Peroxidase Mimetic Activity of Using Acetic Acid Capped Zinc Oxide Nanosheets.",
      "abstract": "Nitrite ions (NO2-), as one of the leading type-A inorganic-anion, showing significant-effects in the aquatic environment and also to humans health. Whereas, the higher uptake causes detrimental threat to human health leading to various chronic diseases, thus demanding efficient, reliable and convenient method for its monitoring. For this purpose, in the present research study we have fabricated the mimetic nonozyme like catalyst based colorimetric nitrite sensor. The acetic acid capped Zinc Oxide (ZnO) nanosheets (NSs) were introduce as per-oxidase mimetic like catalyst which shows high efficiency towards the oxidative catalysis of colorless tetramethylbenzidine (TMB) to oxidized-TMB (blue color) in the presence of Hydrogen-peroxide (H2O2). The present nitrite ions will stimulate the as formed oxidized-TMB (TMBox), and will caused diazotization reaction (diazotized-TMBox), which will not only decreases the peak intensity of UV-visible peak of TMBox at 652\u00a0nm but will also produces another peak at 446\u00a0nm called as diazotized-TMBox peak, proving the catalytic reaction between the nitrite ions and TMBox. Further, the prepared colorimetric sensor exhibits better sensitivity with a wider range of concentration (1\u2009\u00d7\u200910-3-4.50\u2009\u00d7\u200910-1 \u00b5M), lowest limit of detection (LOD) of 0.22\u2009\u00b1\u20090.05 nM and small limit of quantification (LOQ) 0.78\u2009\u00b1\u20090.05 nM having R2 value of 0.998. Further, the colorimetric sensor also manifest strong selectivity towards NO2- as compared to other interference in drinking water system. Resultantly, the prepared sensor with outstanding repeatability, stability, reproducibility, re-usability and its practicability in real water samples also exploit its diverse applications in food safety supervision and environmental monitoring.",
      "journal": "Journal of fluorescence",
      "year": "2025",
      "doi": "10.1007/s10895-024-03830-6",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/38967859/",
      "matched_queries": [
        "short chain fatty acid colorimetric quantification"
      ]
    },
    {
      "pmid": "39126070",
      "title": "Assessment of 5-Hydroxymethylfurfural in Food Matrix by an Innovative Spectrophotometric Assay.",
      "abstract": "Foods contaminants pose a challenge for food producers and consumers. Due to its spontaneous formation during heating and storage, hydroxymethylfurfural (HMF) is a prevalent contaminant in foods rich in carbohydrates and proteins. Colorimetric assays, such as the Seliwanoff test, offer a rapid and cost-effective method for HMF quantification but require careful optimization to ensure accuracy. We addressed potential interference in the Seliwanoff assay by systematically evaluating parameters like incubation time, temperature, and resorcinol or hydrochloric acid concentration, as well as the presence of interfering carbohydrates. Samples were analyzed using a UV-Vis spectrophotometer in scan mode, and data obtained were validated using HPLC, which also enabled quantification of unreacted HMF for assessing the protocol's accuracy. Incubation time and hydrochloric acid percentage positively influenced the colorimetric assay, while the opposite effect was observed with the increase in resorcinol concentration. Interference from carbohydrates was eliminated by reducing the acid content in the working reagent. HPLC analyses corroborated the spectrophotometer data and confirmed the efficacy of the proposed method. The average HMF content in balsamic vinegar samples was 1.97 \u00b1 0.94 mg/mL. Spectrophotometric approaches demonstrated to efficiently determine HMF in complex food matrices. The HMF levels detected in balsamic vinegars significantly exceeded the maximum limits established for honey. This finding underscores the urgent need for regulations that restrict contaminant levels in various food products.",
      "journal": "International journal of molecular sciences",
      "year": "2024",
      "doi": "10.3390/ijms25158501",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/39126070/",
      "matched_queries": [
        "short chain fatty acid colorimetric quantification"
      ]
    },
    {
      "pmid": "39173973",
      "title": "Diet, Microbiome, and Inflammation Predictors of Fecal and Plasma Short-Chain Fatty Acids in Humans.",
      "abstract": "Gut microbes produce short-chain fatty acids (SCFAs), which are associated with broad health benefits. However, it is not fully known how diet and/or the gut microbiome could be modulated to improve SCFA production.\nThe objective of this study was to identify dietary, inflammatory, and/or microbiome predictors of SCFAs in a cohort of healthy adults.\nSCFAs were measured in fecal and plasma samples from 359 healthy adults in the United States Department of Agriculture Nutritional Phenotyping Study. Habitual and recent diet was assessed using a Food Frequency Questionnaire and Automated Self-Administered 24-h Dietary Assesment Tool dietary recalls. Markers of systemic and gut inflammation were measured in fecal and plasma samples. The gut microbiome was assessed using shotgun metagenomics. Using statistics and machine learning, we determined how the abundance and composition of SCFAs varied with measures of diet, inflammation, and the gut microbiome.\nWe show that fecal pH may be a good proxy for fecal SCFA abundance. A higher Healthy Eating Index for a habitual diet was associated with a compositional increase in fecal butyrate relative to acetate and propionate. SCFAs were associated with markers of subclinical gastrointestinal (GI) inflammation. Fecal SCFA abundance was inversely related to plasma lipopolysaccharide-binding protein. When we analyzed hierarchically organized diet and microbiome data with taxonomy-aware algorithms, we observed that diet and microbiome features were far more predictive of fecal SCFA abundances compared to plasma SCFA abundances. The top diet and microbiome predictors of fecal butyrate included potatoes and the thiamine biosynthesis pathway, respectively.\nThese results suggest that resistant starch in the form of potatoes and microbially produced thiamine provide a substrate and essential cofactor, respectively, for butyrate synthesis. Thiamine may be a rate-limiting nutrient for butyrate production in adults. Overall, these findings illustrate the complex biology underpinning SCFA production in the gut. This trial was registered at clinicaltrials.gov as NCT02367287.",
      "journal": "The Journal of nutrition",
      "year": "2024",
      "doi": "10.1016/j.tjnut.2024.08.012",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/39173973/",
      "matched_queries": [
        "fecal SCFA self-administered measurement"
      ]
    },
    {
      "pmid": "39340210",
      "title": "Changes in intestinal permeability and gut microbiota following diet-induced weight loss in patients with metabolic dysfunction-associated steatohepatitis and liver fibrosis.",
      "abstract": "Weight loss improves metabolic dysfunction-associated steatohepatitis (MASH). We investigated whether there were associated changes in intestinal permeability, short-chain fatty acids (SCFAs), and gut microbiota, which are implicated in the pathophysiology of MASH. Sixteen adults with MASH, moderate fibrosis, and obesity received a low-energy total diet replacement program for 12\u2009weeks and stepped food re-introduction over the following 12\u2009weeks (ISRCTN12900952). Intestinal permeability, fecal SCFAs, and fecal microbiota were assessed at 0, 12, and 24\u2009weeks. Data were analyzed using mixed-effects linear regression and sparse partial least-squares regression. Fourteen participants completed the trial, lost 15% (95% CI: 11.2-18.6%) of their weight, and 93% had clinically relevant reductions in liver disease severity markers. Serum zonulin concentrations were reduced at both 12 and 24\u2009weeks (152.0\u2009ng/ml, 95% CI: 88.0-217.4, p\u2009<\u20090.001). Each percentage point of weight loss was associated with a 13.2\u2009ng/mL (95% CI: 3.8-22.5, p\u2009<\u20090.001) reduction in zonulin. For every 10\u2009ng/mL reduction in zonulin, there was a 6.8% (95% CI: 3.5%-10.2, p\u2009<\u20090.001) reduction in liver fat. There were reductions in SCFA and alpha diversity evenness as well as increases in beta diversity of the gut microbiota at 12\u2009weeks, but the changes did not persist at 24\u2009weeks. In conclusion, substantial dietary energy restriction is associated with significant improvement in MASH markers alongside reduction in intestinal permeability. Changes in gut microbiota and SCFA were not maintained with sustained reductions in weight and liver fat, suggesting that microbiome modulation may not explain the relationship between weight loss and improvements in MASH.",
      "journal": "Gut microbes",
      "year": "2024",
      "doi": "10.1080/19490976.2024.2392864",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/39340210/",
      "matched_queries": [
        "point-of-care SCFA stool analysis"
      ]
    },
    {
      "pmid": "39436023",
      "title": "Computer-Aided Flexible Loops Engineering of Glutamate Dehydrogenase for Asymmetric Synthesis of Chiral Pesticides l-phosphinothricin.",
      "abstract": "The access to the enantiopure noncanonical amino acid l-phosphinothricin (l-PPT) by applying biocatalysts is highly appealing in organic chemistry. In this study, a NADH-dependent glutamate dehydrogenase from Lachnospiraceae bacterium (LbGluDH) was chosen for the asymmetric synthesis of l-PPT. Three flexible loops undergoing big conformational shifts during the catalysis were identified and rationally engineered following the initial mutagenesis. The enzyme's specific activity toward the key precursor of l-PPT, 2-oxo-4-[(hydroxy) (methyl) phosphinyl] butyric acid (PPO), was improved from negligible to 9 U/mg, and the Km value was reduced to 17 mM. The computational analysis showed that the modified loops broadened the enzyme's narrow tunnels, allowing the substrate to access the binding pocket and get closer to the crucial residue D165, thereby enhancing the catalytic process. Utilizing the variant as the catalyst, the preparation of l-PPT achieved a 100% conversion rate within 60 min, coupled with a stereoselectivity exceeding 99.9%, demonstrating its practical capacity for industrial application. Similar enhancement in catalytic activity was obtained applying the same strategy to a typical NADH-dependent GluDH from Pyrobaculum islandicum (PisGluDH), indicating the effectiveness of our strategy for the protein engineering of GluDHs targeted to the biosynthesis of unnatural compounds.",
      "journal": "Journal of agricultural and food chemistry",
      "year": "2024",
      "doi": "10.1021/acs.jafc.4c06294",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/39436023/",
      "matched_queries": [
        "NADH coupled butyrate assay"
      ]
    },
    {
      "pmid": "39503721",
      "title": "Enhanced biosynthesis of poly(3-hydroxybutyrate) in engineered strains of Pseudomonas putida via increased malonyl-CoA availability.",
      "abstract": "Malonyl-coenzyme A (CoA) is a key precursor for the biosynthesis of multiple value-added compounds by microbial cell factories, including polyketides, carboxylic acids, biofuels, and polyhydroxyalkanoates. Owing to its role as a metabolic hub, malonyl-CoA availability is limited by competition in several essential metabolic pathways. To address this limitation, we modified a genome-reduced Pseudomonas putida strain to increase acetyl-CoA carboxylation while limiting malonyl-CoA utilization. Genes involved in sugar catabolism and its regulation, the tricarboxylic acid (TCA) cycle, and fatty acid biosynthesis were knocked-out in specific combinations towards increasing the malonyl-CoA pool. An enzyme-coupled biosensor, based on the rppA gene, was employed to monitor malonyl-CoA levels in\u00a0vivo. RppA is a type III polyketide synthase that converts malonyl-CoA into flaviolin, a red-colored polyketide. We isolated strains displaying enhanced malonyl-CoA availability via a colorimetric screening method based on the RppA-dependent red pigmentation; direct flaviolin quantification identified four engineered strains had a significant increase in malonyl-CoA levels. We further modified these strains by adding a non-canonical pathway that uses malonyl-CoA as precursor for poly(3-hydroxybutyrate) biosynthesis. These manipulations led to increased polymer accumulation in the fully engineered strains, validating our general strategy to boost the output of malonyl-CoA-dependent pathways in P.\u2009putida.",
      "journal": "Microbial biotechnology",
      "year": "2024",
      "doi": "10.1111/1751-7915.70044",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/39503721/",
      "matched_queries": [
        "short chain fatty acid colorimetric quantification"
      ]
    },
    {
      "pmid": "39546851",
      "title": "Transplant of gut microbiota ameliorates metabolic and heart disorders in rats fed with a hypercaloric diet by modulating microbial metabolism and diversity.",
      "abstract": "Metabolic syndrome (MS) is a cluster of metabolic disorders which have a tight correlation with dysbiosis of gut microbiota (GM) that have to be treated to avoid higher risks for health. In this work, probiotics obtained from healthy cultured GM were provided to rats with metabolic syndrome (MSR) as therapy in treating MS through the correction of dysbiosis. MSR showed obesity, high blood pressure, abnormal blood chemistry parameters and high heart rate respect to control rats (CNTR). Cultivated GM from feces of MSR in media favoring anaerobic species, showed dysbiosis as judged by differences in the 16S rRNA metabarcoding analysis and by affected intermediary metabolism (methane and SCFA production, nutrients consumption and enzyme activities) compared to CNTR. The metabarcoding analysis of cultured healthy GM identified 211 species, which were further transplanted alive in MSR once a week for 9 weeks. Thereafter, in transplanted MSR the excess of Clostridium and Lactobacillus diminished, while Prevotella, Eubacterium, Faecalibacterium and methanogens, among others increased, leading to the recovery of the microbial metabolic capacity. The presence of butyric acid-producing bacteria in the transplanted GM correlated with increased levels of anti-inflammatory cytokines. Therefore, transplanted MSR recovered the normal levels of weight, blood glucose, triglycerides and
```

## Run Record

```json
{
  "run": {
    "timestamp_utc": "2026-05-20T15:09:12+00:00",
    "mode": "codex_synthesis_from_packet",
    "no_openrouter_model_calls": true,
    "source_packet": "outputs/codex-synthesis-packet.md",
    "pubmed_snapshot": "outputs/pubmed-snapshot.json",
    "pubmed_records": 74,
    "queries": 27,
    "model_role_note": "Primary synthesis performed in-session by Codex/GPT-5.5-equivalent role to avoid unnecessary OpenRouter spend.",
    "models": {
      "query_strategist": "codex/gpt-5.5-in-session",
      "synthesis": "codex/gpt-5.5-in-session",
      "judge": "codex/gpt-5.5-in-session",
      "verifier": "codex/gpt-5.5-in-session"
    },
    "input_sha256": {
      "query_strategy": "8abcc1b32acd8bcf2aae06105d9474d389e8c68771892a9e980925005ee87ec2",
      "model_config": "5803b0d82bd2b6f666471d5d99a38b76aca448f4839fc2ec006a976f681f8fb9"
    },
    "openrouter_policy": "Default Codex path makes no OpenRouter model calls; *_openrouter roles require explicit --run-openrouter."
  },
  "query_strategy_scope": "Identify Tier 2 butyrate quantification assays (colorimetric / enzymatic / breath-hydrogen proxy / other low-cost intermediate methods) that can be validated against Tier 3 GC-MS reference. Microbiome-derived butyrate quantification in stool, blood, breath, and culture-supernatant matrices.",
  "query_critique": {
    "coverage_verdict": "adequate_for_first_pass_with_vendor_followup_gap",
    "notes": "PubMed coverage was adequate to reject breath proxy and generic FFA kits and to surface HPLC-UV/electrochemical candidates. Vendor/protocol search remains necessary before wet-lab adoption because commercial kit validation rarely appears in PubMed."
  }
}
```
