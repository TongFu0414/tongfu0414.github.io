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
Building on this background, I am keen to explore a broad range of frontier AI research directions.

I am currently seeking **MPhil opportunities for Fall 2027**. Please feel free to [contact me](mailto:futong0414@163.com).

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
    <p class="project-card__summary">A training-free framework for multimodal reasoning through question-contrastive visual steering. It separates question-dependent signals from shared perturbation effects and selectively applies a bounded hidden-state update, with all model parameters frozen.</p>
    <figure class="project-media project-media--wide">
      <a href="{{ '/assets/research/qcvs-overview.png' | relative_url }}">
        <img src="{{ '/assets/research/qcvs-overview.png' | relative_url }}" width="1527" height="948" loading="lazy" decoding="async" alt="QCVS overview: matched visual controls and task-reference contrasts produce a direction; a gate selects a single bounded intervention">
      </a>
      <figcaption>QCVS: question-contrastive probing and selective inference-time steering.</figcaption>
    </figure>
    <details class="project-details">
      <summary>View project details</summary>
      <div class="project-details__content">
        <ul>
          <li><strong>Question-contrastive probing:</strong> Matched spatial controls are evaluated under a task question and a generic description reference. Their differential responses isolate the question-dependent interaction.</li>
          <li><strong>Selective intervention:</strong> Relative interaction strength and signal amplitude determine whether to apply one bounded update during a fresh prefix replay. Model parameters remain frozen.</li>
          <li><strong>Evaluation:</strong> The manuscript evaluates multimodal mathematical reasoning on DynaMath and We-Math, reporting accuracy alongside repair, damage, and intervention coverage.</li>
        </ul>
      </div>
    </details>
  </article>

  <article class="project-card">
    <header class="project-card__header">
      <h3 class="project-card__title">CFMS: A Coarse-to-Fine Multimodal Synthesis Framework for Enhanced Tabular Reasoning</h3>
      <p class="project-card__meta">PRCV 2026 (Main Track) · Accepted</p>
    </header>
    <p class="project-card__summary">CFMS combines an initial multimodal understanding of a table with a sequence of targeted symbolic operations. Visual, semantic, and statistical descriptions provide context for the subsequent reasoning process.</p>
    <figure class="project-media project-media--wide">
      <a href="{{ '/assets/research/cfms-overview.png' | relative_url }}">
        <img src="{{ '/assets/research/cfms-overview.png' | relative_url }}" width="1400" height="760" loading="lazy" decoding="async" alt="CFMS overview: coarse visual, semantic, and statistical descriptions guide fine-grained table operations">
      </a>
      <figcaption>CFMS: coarse knowledge synthesis followed by fine-grained table operations.</figcaption>
    </figure>
    <details class="project-details">
      <summary>View project details</summary>
      <div class="project-details__content">
        <ul>
          <li><strong>Coarse stage:</strong> Synthesize visual, semantic, and statistical information into a compact textual knowledge tuple.</li>
          <li><strong>Fine stage:</strong> Guide an LLM planner through table operations such as column creation, selection, grouping, and sorting before answer generation.</li>
          <li><strong>Evaluation:</strong> Assess table question answering on WikiTQ and table-based fact verification on TabFact.</li>
        </ul>
      </div>
    </details>
  </article>
</div>

## Experience {#experience}

<div class="experience-list" markdown="1">

- {% include experience-logos.html organizations="hikvision" %} **[Hikvision](https://www.hikvision.com/en/)**, Hangzhou, China<br>
  <span class="needs-confirmation">Jun. 2026 – Present</span><br>
  <strong class="needs-confirmation">Product Management Engineer, Industrial AI</strong><br>
  Focus: Industrial Multimodal AI / Smart-Factory Applications<br>
  <span class="needs-confirmation">Product requirements, model-evaluation criteria, and human-review workflows for visual inspection and process monitoring.</span>

- {% include experience-logos.html organizations="dptech" %} **[DPtech](https://www.dptech.com/)**, <span class="needs-confirmation">Hangzhou, China</span><br>
  <span class="needs-confirmation">Jul. 2024 – May 2026</span><br>
  <strong class="needs-confirmation">Product Manager, Network Security Products</strong><br>
  Focus: LLM/RAG-Based Security Applications / Data Classification<br>
  <span class="needs-confirmation">Product definition, data preparation, annotation workflows, and evaluation criteria in collaboration with domain experts and algorithm teams.</span>

- {% include experience-logos.html organizations="tyut" %} **[Taiyuan University of Technology (211)](https://english.tyut.edu.cn/)**, Shanxi, China<br>
  Sept. 2020 – Jul. 2024<br>
  **B.Eng. in Computer Science**<br>
  Excellent Engineer Education and Training Program<br>
  **Comprehensive Evaluation Rank:** Top 12.7% (24/189)

</div>

## Publications {#publications}

### Manuscripts Under Review

- **T. Fu**<sup>*</sup> et al., QCVS: Question-Contrastive Visual Steering for Multimodal Reasoning. *2027 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP 2027).* **Under review.**

### Accepted Papers

- Q. Huang<sup>*</sup>, H. Lin<sup>*</sup>, **T. Fu**, Y. Wang, Z. Fu, Q. Wang, Y. Sun<sup>†</sup>, and D. Zhang<sup>†</sup>, CFMS: A Coarse-to-Fine Multimodal Synthesis Framework for Enhanced Tabular Reasoning. *2026 Chinese Conference on Pattern Recognition and Computer Vision (PRCV 2026, Main Track).* **Accepted.**

<p class="publication-note"><sup>*</sup> Equal contribution. <sup>†</sup> Corresponding authors.</p>

## Honors and Awards {#awards}

- **Excellent Engineer Education and Training Program — Certificate of Completion**<br>
  Jun. 2024

- **Outstanding Communist Youth League Cadre**<br>
  2021

- **Academic Excellence Award**<br>
  Apr. 2021

- **Social Work Award**<br>
  Apr. 2021

- **DPtech Certified Product Technology Engineer**<br>
  Certification valid through Jul. 2026

## Skills {#skills}

{% include skills-mindmap.html %}

## Learning Resources {#resources}

{% include learning-resources.html %}

## CV and Contact {#contact}

[**Download academic CV (PDF)**]({{ '/assets/CV_TongFu.pdf' | relative_url }}?v={{ site.time | date: '%s' }})<br>
Email: [**futong0414@163.com**](mailto:futong0414@163.com) · [**GitHub**](https://github.com/TongFu0414)
