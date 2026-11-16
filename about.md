---
permalink: /
seo_title: "Tong Fu"
description: "Tong Fu, a Taiyuan University of Technology (211) graduate in Computer Science, seeking MPhil opportunities for Fall 2027."
lang: en
locale: en_US
alternate_url: /zh/
alternate_lang: zh-CN
language_switch_label: 中文
language_switch_aria_label: Switch to Chinese
author_profile: true
hide_title: true
homepage: true
skills_mindmap: true
redirect_from:
  - /about/
  - /about.html
---

# Tong Fu (付彤)
---

Nice to meet you here!<br>
I graduated in **Computer Science** from [Taiyuan University of Technology (211)](https://english.tyut.edu.cn/) in 2024.

My research experience focuses on **multimodal reasoning**, **inference-time steering**, and **structured-data understanding**.<br>
<span class="intro-highlight">I am keen to explore a broad range of frontier AI research directions.</span>

I am currently seeking <strong class="intro-highlight">MPhil opportunities for Fall 2027</strong>. Please feel free to contact me（[CV]({{ '/assets/CV_TongFu.pdf' | relative_url }}?v={{ site.time | date: '%s' }}) &nbsp; <a href="#email-modal" data-dialog-open="email-modal" aria-controls="email-modal" aria-haspopup="dialog">Email</a> &nbsp; <a href="#wechat-modal" data-dialog-open="wechat-modal" aria-controls="wechat-modal" aria-haspopup="dialog">WeChat</a>）.

## Research Interests {#research-interest}

**Artificial Intelligence:** multimodal learning, vision-language models, and inference-time methods;<br>
**AI Applications:** structured-data reasoning, industrial inspection, and security applications.

## Selected Research Projects {#research}

<div class="project-list">
  <article class="project-card">
    <header class="project-card__header">
      <h3 class="project-card__title">QCVS: Question-Contrastive Visual Steering for Multimodal Reasoning</h3>
      <p class="project-card__meta">ICASSP 2027 · Under review</p>
    </header>
    <p class="project-card__summary">A training-free inference method for visual mathematical reasoning, improving DynaMath accuracy by <strong>1.76–2.52 percentage points</strong> across Qwen3.5 2B–9B while intervening on only <strong>22%–30% of inputs</strong>.</p>
    <figure id="qcvs-overview" class="project-media project-media--wide">
      <a href="{{ '/assets/research/qcvs-overview.png' | relative_url }}">
        <img src="{{ '/assets/research/qcvs-overview.png' | relative_url }}" width="1527" height="948" loading="lazy" decoding="async" alt="QCVS overview: matched visual controls and task-reference contrasts produce a direction; a gate selects a single bounded intervention">
      </a>
      <figcaption>QCVS: question-contrastive probing and selective inference-time steering.</figcaption>
    </figure>
    <details class="project-details">
      <summary>View project details</summary>
      <div class="project-details__content">
        <p><strong>Project Background:</strong> Visual perturbations change both question-relevant evidence and generic spatial responses inside a vision-language model. Steering with this mixed signal can repair an incorrect answer while also damaging an initially correct prediction. QCVS addresses two connected questions: how to isolate a question-specific direction, and when that direction warrants an intervention.</p>
        <ul>
          <li><strong>Matched Visual Controls and Double-Differential Probing:</strong> Encode the image once, then construct two controls by permuting non-overlapping 2 × 2 visual-token blocks while preserving the token vectors, token count and within-block structure. Apply the same controls under the task question and a fixed “Describe the visible content” reference. At the last assistant-prefix token, subtract each reference clean–control response from its task counterpart and average the two differences to isolate the question-dependent interaction. The six prefix evaluations require no answer generation, ground-truth labels or output-confidence scores.</li>
          <li><strong>Dual-Threshold Gating and Single-Site Intervention:</strong> Measure interaction strength relative to the perturbation responses and signal amplitude relative to the clean task state. Both thresholds must pass before an edit is applied. A separate calibration set supplies the amplitude threshold and 5th–95th percentile norm bounds; validation selects the target layer, steering multiplier and relative-strength threshold. Selected inputs receive one bounded update at one layer and prefix token during a fresh clean-prefix replay, rebuilding the states needed for continuation. Unselected inputs continue from the retained clean task state, with all model weights frozen.</li>
          <li><strong>Multi-Scale Evaluation and Cross-Backbone Transfer:</strong> Compare with Base, VCD, VISTA and Task-only steering on DynaMath and We-Math. DynaMath gains are +2.52, +1.92 and +1.76 percentage points for Qwen3.5-2B, 4B and 9B, respectively; the 9B model reaches 85.35% on DynaMath and 77.43% on We-Math. With model-specific calibration, DeepSeek-VL2-Tiny and Small improve from 45.01% to 47.13% and from 55.01% to 56.95% on DynaMath. Evaluation also tracks the fraction of baseline errors repaired, initially correct answers damaged, intervention coverage and generated-token counts.</li>
          <li><strong>Controlled Direction and Gating Ablations:</strong> On Qwen3.5-4B/DynaMath at 25.01% coverage, QCVS gains 1.92 percentage points, repairs 13.98% of baseline errors and damages 0.50% of initially correct answers. Replacing its direction with Task-only steering reduces the gain to 0.84 points under the same coverage; random and reversed directions yield −0.88 and −1.86 points. Removing gating also leaves only a 0.84-point gain at 100% coverage and raises damage to 3.55%, separating the value of direction construction from intervention selection.</li>
        </ul>
        <p><strong>Core Results:</strong> DynaMath accuracy gains of <strong>1.76–2.52 percentage points</strong> across three Qwen3.5 sizes; <strong>85.35%</strong> DynaMath and <strong>77.43%</strong> We-Math accuracy with Qwen3.5-9B; selective intervention at approximately <strong>22%–30% coverage</strong>, without model fine-tuning.</p>
      </div>
    </details>
  </article>

  <article class="project-card">
    <header class="project-card__header">
      <h3 class="project-card__title">CFMS: A Coarse-to-Fine Multimodal Synthesis Framework for Enhanced Tabular Reasoning</h3>
      <p class="project-card__meta">PRCV 2026 (Main Track) · Accepted</p>
    </header>
    <p class="project-card__summary">A two-stage framework combining multimodal knowledge synthesis with iterative table operations. With GPT-4/GPT-4V coarse-stage assistance and a GPT-3.5 planner, it achieves <strong>81.37% TabFact accuracy</strong> and <strong>61.42% WikiTQ denotation accuracy</strong>.</p>
    <figure id="cfms-overview" class="project-media project-media--wide">
      <a href="{{ '/assets/research/cfms-overview.png' | relative_url }}">
        <img src="{{ '/assets/research/cfms-overview.png' | relative_url }}" width="1400" height="760" loading="lazy" decoding="async" alt="CFMS overview: coarse visual, semantic, and statistical descriptions guide fine-grained table operations">
      </a>
      <figcaption>CFMS: coarse knowledge synthesis followed by fine-grained table operations.</figcaption>
    </figure>
    <details class="project-details">
      <summary>View project details</summary>
      <div class="project-details__content">
        <p><strong>Project Background:</strong> Serializing a table into text can obscure its row–column relationships, trends and outliers, while repeatedly processing visual inputs adds cost to multi-step reasoning. CFMS separates a one-time, holistic understanding of the table from the precise symbolic operations needed to answer a question or verify a claim.</p>
        <ul>
          <li><strong>One-Time Visual, Semantic and Statistical Synthesis:</strong> Generate and execute visualization code for the input table, then use GPT-4V to describe the resulting chart’s patterns. In parallel, GPT-4 supplies entity-level semantic context and numerical summaries, including key columns, maxima, minima and averages. Combine these three descriptions into a textual knowledge tuple that is reused throughout the fine stage, giving the planner a global view alongside the original structured data.</li>
          <li><strong>Stateful Symbolic Planning and Table Evolution:</strong> At each step, the planner conditions on the question, current table, operation history and coarse knowledge. It selects an operation and arguments from column creation, column selection, row filtering, grouping and sorting; execution produces the next table state. For example, a revenue-to-R&amp;D question can require adding a ratio column, filtering Q2 rows and identifying the highest ratio. Planning continues until an END decision, after which the final table, question and knowledge tuple support answer generation.</li>
          <li><strong>Question Answering and Fact Verification:</strong> Evaluate WikiTQ with denotation accuracy and TabFact with binary classification accuracy, using few-shot, in-context inference. With the GPT-3.5-Turbo planner and GPT-4/GPT-4V coarse stage, CFMS reaches 81.37% on TabFact and 61.42% on WikiTQ, exceeding Chain-of-Table’s 80.20% and 59.94% by 1.17 and 1.48 percentage points. A LLaMA-2-13B-Chat planner, retaining the external coarse-stage assistance, reaches 68.53% and 43.89%, respectively.</li>
          <li><strong>Large-Table Robustness and Component Ablations:</strong> On WikiTQ tables exceeding 4,000 tokens, CFMS reaches 46.92% accuracy versus Dater’s 34.62%. Removing the coarse stage reduces overall WikiTQ accuracy from 61.42% to 55.18%; removing the fine stage reduces it to 56.44%. Operation-level ablations further show the importance of structured manipulation: removing grouping lowers WikiTQ accuracy to 55.02%, while removing row selection lowers TabFact accuracy from 81.37% to 76.79%.</li>
          <li><strong>Explicit Query Budget:</strong> The paper’s WikiTQ comparison reports at most 15 model calls per question: four for coarse synthesis, up to ten for fine-stage planning and one for the final answer, versus 50 for Binder and 100 for Dater in the reported configurations. This measures call count; the stronger coarse-stage models carry a higher per-call cost.</li>
        </ul>
        <p><strong>Core Results:</strong> <strong>81.37%</strong> TabFact accuracy and <strong>61.42%</strong> WikiTQ denotation accuracy with GPT-4/GPT-4V assistance and a GPT-3.5 planner; gains of <strong>1.17 / 1.48 percentage points</strong> over Chain-of-Table; <strong>46.92%</strong> accuracy on large WikiTQ tables.</p>
      </div>
    </details>
  </article>
</div>

## Experience {#experience}

<div class="experience-list" markdown="1">

- {% include experience-logos.html organizations="hikvision" %} **[Hikvision](https://www.hikvision.com/en/)**, Hangzhou, China<br>
  Jun. 2026 – Present<br>
  **Product Management Engineer, Industrial AI**<br>
  Focus: Industrial Multimodal AI / Smart-Factory Applications<br>
  Product requirements, model-evaluation criteria, and human-review workflows for industrial visual inspection and process monitoring.

- {% include experience-logos.html organizations="dptech" %} **[DPtech](https://www.dptech.com/)**, Hangzhou, China<br>
  Jul. 2024 – May 2026<br>
  **Product Manager, Network Security Products**<br>
  Focus: LLM/RAG-Based Security Applications / Data Classification<br>
  Product and data requirements, annotation workflows, and evaluation criteria in collaboration with domain experts and algorithm teams.

- {% include experience-logos.html organizations="tyut" %} **[Taiyuan University of Technology (211)](https://english.tyut.edu.cn/)**, Shanxi, China<br>
  Sept. 2020 – Jul. 2024<br>
  **B.Eng. in Computer Science**<br>
  Excellent Engineer Education and Training Program<br>
  **Comprehensive Evaluation Rank:** Top 12.7% (24/189) [\[Evidence\]]({{ '/assets/evidence/Evidence_Comprehensive_Evaluation_Rank.pdf' | relative_url }})

</div>

## Publications {#publications}

### Manuscripts Under Review

- **T. Fu**<sup>&#42;</sup> et al., [QCVS: Question-Contrastive Visual Steering for Multimodal Reasoning](#qcvs-overview). *2027 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP 2027).* **Under review.**

### Accepted Papers

- Q. Huang<sup>&#42;</sup>, H. Lin<sup>&#42;</sup>, **T. Fu**, Y. Wang, Z. Fu, Q. Wang, Y. Sun<sup>†</sup>, and D. Zhang<sup>†</sup>, [CFMS: A Coarse-to-Fine Multimodal Synthesis Framework for Enhanced Tabular Reasoning](#cfms-overview). *2026 Chinese Conference on Pattern Recognition and Computer Vision (PRCV 2026, Main Track).* **Accepted.**

<p class="publication-note"><sup>&#42;</sup> Equal contribution. <sup>†</sup> Corresponding authors.</p>

## Honors and Awards {#awards}

- **Excellent Engineer Education and Training Program — Certificate of Completion**<br>
  Jun. 2024 [\[Evidence\]]({{ '/assets/evidence/Evidence_Excellent_Engineer_Program_2024.pdf' | relative_url }})

- **Outstanding Communist Youth League Cadre**<br>
  2021 [\[Evidence\]]({{ '/assets/evidence/Evidence_Outstanding_Youth_League_Cadre_2021.pdf' | relative_url }})

- **Academic Excellence Award**<br>
  Apr. 2021 [\[Evidence\]]({{ '/assets/evidence/Evidence_Academic_Excellence_Award_2021.pdf' | relative_url }})

- **Social Work Award**<br>
  Apr. 2021 [\[Evidence\]]({{ '/assets/evidence/Evidence_Social_Work_Award_2021.pdf' | relative_url }})

- **DPtech Certified Product Technology Engineer**<br>
  Certification valid through Jul. 2026 [\[Evidence\]]({{ '/assets/evidence/Evidence_DPtech_Certification.pdf' | relative_url }})

## Skills {#skills}

{% include skills-mindmap.html %}

## Inspiring Articles {#resources}

{% include learning-resources.html %}

## Contact {#contact}

Academic CV：[**Tong Fu (付彤)**]({{ '/assets/CV_TongFu.pdf' | relative_url }}?v={{ site.time | date: '%s' }})<br>
Email: [**futong0414@163.com**](mailto:futong0414@163.com)<br>
WeChat：Ft_Be_admitted_to
