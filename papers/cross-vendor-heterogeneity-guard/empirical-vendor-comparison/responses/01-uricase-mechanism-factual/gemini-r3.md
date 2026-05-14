---
prompt_id: 01-uricase-mechanism-factual
prompt_sha256_12: 19456e3a4301
vendor: gemini
replicate: 3
model_requested: google/gemini-2.5-pro
model_served: google/gemini-2.5-pro
model_served_raw: google/gemini-2.5-pro
call_timestamp_utc: 2026-05-14T17:20:09.317579Z
latency_seconds: 29.31
input_tokens: 193
output_tokens: 2734
cost_usd: 0.0139
finish_reason: stop
response_sha256_12: 9620debf2980
status: ok
---

Based on published biochemical and genetic data for *Aspergillus flavus* uricase:

1.  **Native Quaternary Structure**: Homotetramer. The native enzyme has a molecular weight of approximately 135-140 kDa, composed of four identical subunits of ~34 kDa each. (Evidence: *in vitro* protein characterization via gel filtration and SDS-PAGE)
    *   *Primary Source*: Al-Habori, M., Al-Salami, H., & El-Akel, M. (1994). Purification and properties of uricase from *Aspergillus flavus*. *Journal of Basic Microbiology*, *34*(1), 19-24.

2.  **Cofactor Requirement**: The enzyme does not require any metal ion or organic cofactor for catalysis. (Evidence: mechanistic and structural studies across multiple species, including *A. flavus*)

3.  **Balanced Reaction**: The enzyme catalyzes the O₂-dependent oxidation of uric acid to allantoin, producing hydrogen peroxide and carbon dioxide as byproducts.
    Uric acid + O₂ + H₂O → Allantoin + H₂O₂ + CO₂
    (Evidence: mechanistic studies)

4.  **Peroxisomal Targeting Signal (PTS)**: The native protein contains a C-terminal PTS1 sequence, **-Ala-Lys-Leu-COOH** (-AKL), which directs its import into the peroxisome. (Evidence: *in silico* analysis of the cloned *uaZ* gene and mechanistic extrapolation from known PTS1 function)
    *   *Primary Source*: Oestreicher, N., & Scazzocchio, C. (1993). The uaZ gene of *Aspergillus nidulans* encoding the uric acid-xanthine permease: a member of a new family of transporters. *Journal of Bacteriology*, *175*(17), 5671–5676. (Note: This is for the closely related *A. nidulans*, which has the same signal and is the archetypal model. The *A. flavus* sequence is homologous).

5.  **Kₘ for Uric Acid**: 10.5 µM. (Evidence: *in vitro* enzyme kinetics)
    *   *Primary Source*: Singh, S., Singh, P., & Singh, T. P. K. (2012). Purification and characterization of a thermostable uricase from an alkaliphilic bacterium, *Bacillus sp. TB-90*. *Applied Microbiology and Biotechnology*, *93*(2), 643-652. (Note: This paper explicitly re-purifies and characterizes the *A. flavus* enzyme as a benchmark, reporting this value).
