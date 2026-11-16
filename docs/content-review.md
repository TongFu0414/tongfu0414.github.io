# Content and source notes

The current homepage follows the user-designated CV. Both languages should be updated together. Per the user's latest instructions, paper review notes are kept off the public page and the LLM-focused skills map has no confirmation labels.

| Item | What to confirm |
| --- | --- |
| Profile | The latest user-provided avatar is `images/me.jpg`; the user states Hangzhou as the profile location and requests a WeChat modal showing `Ft_Be_admitted_to`. These supersede the earlier GitHub-avatar choice. |
| QCVS | The latest user-designated CV states under review in ICASSP 2027 and co-first author. The user authorized the supplied manuscript's public PDF on 2026-11-16; its complete final author list and individual contributions remain internal source notes rather than public review prompts. |
| CFMS | Final proceedings citation and DOI, code links, and individual contributions remain to confirm. Current wording is accepted at PRCV 2026 Main Track. The user authorized the supplied manuscript's public PDF on 2026-11-16. |
| Hikvision experience | The current CV and supplied experience draft agree on Product Management Engineer, Industrial AI, June 2026 to present, in Hangzhou. The user authorizes normal display after this local cross-check. Copy focuses on requirements, model evaluation and human-review workflows; no independent employment letter was supplied. |
| DPtech experience | The current CV and supplied experience draft agree on Product Manager, Network Security Products, July 2024 to May 2026, in Hangzhou. The user authorizes normal display after this local cross-check. Copy focuses on product/data requirements, annotation and evaluation; unsubstantiated accuracy or labor-saving figures are omitted. |
| Education | The latest CV states B.Eng. in Computer Science without a review highlight; the homepage follows it. A separate degree certificate has not been inspected. School and study dates have transcript support; rank is explicitly comprehensive evaluation, not GPA rank. |
| Skills | Drafted as authorized by the user, grouped around LLM foundations, multimodal models, inference, applications, evaluation, and basic development tools. No proficiency score is inferred. |
| English | The user requests TOEFL Certificate in the language branch and states that the score meets the school's English language requirement; the CV includes that parenthetical statement. No score, test date, validity, or downloadable certificate has been supplied. |
| CV | The user-designated application PDF is the canonical CV. `assets/CV_TongFu.pdf` is an unchanged copy for download. Do not generate a separate website CV or replace the user-designated source. Contact links now match its email address. |

The user authorizes certificate Evidence links. Public assets use cropped, correctly oriented, redacted and flattened copies; source originals remain private. Submission credentials, raw transcripts, and internal work documents are excluded from public assets. The local materials contain no TOEFL certificate file, so its skills entry has no Evidence link.

## Public evidence copies

| Evidence | Public PDF |
| --- | --- |
| Academic Excellence Award, 2021 | `assets/evidence/Evidence_Academic_Excellence_Award_2021.pdf` |
| Outstanding Youth League Cadre, 2021 | `assets/evidence/Evidence_Outstanding_Youth_League_Cadre_2021.pdf` |
| Social Work Award, 2021 | `assets/evidence/Evidence_Social_Work_Award_2021.pdf` |
| Excellent Engineer program coursework completion, 2024 | `assets/evidence/Evidence_Excellent_Engineer_Program_2024.pdf` |
| DPtech product technology engineer certification | `assets/evidence/Evidence_DPtech_Certification.pdf` |
| Comprehensive evaluation rank | `assets/evidence/Evidence_Comprehensive_Evaluation_Rank.pdf` |

Names, certificate wording, dates, and issuer signatures/stamps are preserved. Personal identification, student and certificate numbers are removed where present; the public PDFs embed only sanitized flattened images, with no original hidden image or text layer. The rank proof is comprehensive evaluation, not GPA rank. The program certificate is coursework completion, not a degree certificate. DPtech validity remains through July 2026 and is not presented as a current renewal.

Official wordmarks and the university seal are used unchanged; their source URLs are in `_data/experience_logos.yml`. The university's 211 designation is supported by its [official profile](https://www.tyut.edu.cn/xxgk1/xxjj.htm), checked 2026-11-15.

The 27 Foundations resources retain the reference list's titles, links, order, and source metadata. They are shown under Inspiring Articles / 受启发的文章, without category headings or collapsed panels, with two cards per row.

## Research detail provenance — 2026-11-16

The expanded English and Chinese project descriptions follow the reference homepage's background, technical modules and core-results structure, checked at `https://ryannnice.github.io/` on 2026-11-16. Technical content and numbers come from the supplied local manuscripts, not the reference author's projects. They describe the research methods and reported results without assigning unconfirmed implementation responsibilities to Tong Fu. The user subsequently authorized publishing the two complete manuscripts unchanged at `assets/papers/QCVS.pdf` and `assets/papers/CFMS.pdf`, with paper-title links to the repository's GitHub PDF pages. Submission screenshots and access credentials remain private.

| Public detail | Local source and interpretation |
| --- | --- |
| QCVS controls and direction | `icassp2027一作.pdf`, §§3.1–3.2, pp. 1–2: one visual encoding, two matched 2 × 2 block permutations, six task/reference prefix evaluations, paired clean–control subtraction and averaging. Controls preserve token content and within-block structure; they are feature perturbations, not semantic counterfactuals. |
| QCVS gate and execution | §§3.3–3.4, pp. 2–3: joint relative-strength/amplitude thresholds, separate calibration and validation roles, 5th–95th percentile norm bounds, one edit at a chosen layer/prefix token, fresh prefix replay for selected inputs. Frozen weights do not mean zero inference overhead; the six probes are prefix evaluations, not six generated answers. |
| QCVS main results | Table 1, p. 3: Qwen3.5 2B/4B/9B DynaMath gains +2.52/+1.92/+1.76 percentage points; Qwen3.5-9B DynaMath 85.35%, We-Math 77.43%; coverage about 22%–30%. Repair is conditional on baseline errors; damage is conditional on baseline-correct answers. Neither denominator is all test inputs. |
| QCVS transfer and ablations | Tables 2–3, p. 4: DeepSeek-VL2-Tiny 45.01% → 47.13%, Small 55.01% → 56.95%, with model-specific calibration. Qwen3.5-4B/DynaMath at 25.01% coverage: +1.92 pp, repair 13.98%, damage 0.50%; Task-only +0.84 pp, random −0.88 pp, reversed −1.86 pp. Ungated uses 100% coverage, +0.84 pp and 3.55% damage. |
| CFMS synthesis and planning | `paper_id_三作.pdf`, §§3.2–3.4, pp. 5–7: generated chart → visual description, semantic context and numerical summary → reusable knowledge tuple; current table, question, history and tuple guide symbolic operations until END. The revenue-to-R&D example is an illustrative reasoning case, not an additional benchmark result. |
| CFMS backbone conditions and main results | §4.1 and Table 1, pp. 8–9: GPT-4/GPT-4V coarse-stage assistance remains present with either GPT-3.5-Turbo or LLaMA-2-13B-Chat as fine-stage planner. TabFact uses binary classification accuracy; WikiTQ uses denotation accuracy. GPT-3.5 results are 81.37%/61.42%, versus Chain-of-Table 80.20%/59.94% (+1.17/+1.48 pp). LLaMA results are 68.53%/43.89%. The p. 9 prose mistakenly associates 68.53% with WikiTQ; the homepage follows the table's TabFact column. |
| CFMS large tables and ablations | Tables 2, 4–5, pp. 9, 11–12: WikiTQ tables >4,000 tokens, CFMS 46.92% vs Dater 34.62%. Removing coarse/fine stages yields WikiTQ 55.18%/56.44% from 61.42%. Removing grouping yields WikiTQ 55.02%; removing row selection yields TabFact 76.79% from 81.37%. |
| CFMS query budget | Table 3 and efficiency analysis, pp. 10–11: ≤15 model calls = 4 coarse + ≤10 fine + 1 answer, versus Binder 50 and Dater 100 in the manuscript's configurations. This is a query-count comparison; no equal-cost, latency or wall-clock speedup claim is made. |
