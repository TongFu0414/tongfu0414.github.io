---
permalink: /
seo_title: "Tong Fu"
description: "Tong Fu: multimodal reasoning, vision-language models, and reliable AI. Seeking MPhil opportunities for Fall 2027."
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
I studied **Computer Science and Technology** at [Taiyuan University of Technology](https://english.tyut.edu.cn/) from 2020 to 2024. My research interests lie in **multimodal reasoning**, **vision-language models**, and **reliable AI**.

My research includes question-contrastive visual steering and coarse-to-fine tabular reasoning. I am interested in how models use visual evidence, when inference-time interventions help, and how evaluation can reveal both improvements and failure cases.<br>
I am seeking **MPhil opportunities starting in Fall 2027**. Please feel free to [contact me](mailto:futong0414@163.com).

## Research Interests {#research-interest}

**Multimodal Reasoning:** visual evidence, mathematical reasoning, and structured-data understanding;<br>
**Inference-Time Methods:** activation steering and selective intervention in frozen models;<br>
**Reliable AI:** model evaluation, failure analysis, and industrial applications.

## Selected Research {#research}

<div class="project-list">
  <article class="project-card">
    <header class="project-card__header">
      <h3 class="project-card__title">QCVS: Question-Contrastive Visual Steering for Multimodal Reasoning</h3>
      <p class="project-card__meta">First author · Submitted to ICASSP 2027</p>
    </header>
    <p class="project-card__summary">How can a vision-language model receive useful inference-time guidance without disturbing predictions it already gets right? QCVS separates question-specific visual signals from shared perturbation effects and applies a bounded hidden-state update selectively.</p>
    <figure class="project-media project-media--wide">
      <a href="{{ '/assets/research/qcvs-overview.png' | relative_url }}">
        <img src="{{ '/assets/research/qcvs-overview.png' | relative_url }}" width="1527" height="948" loading="lazy" decoding="async" alt="QCVS overview: matched visual controls and task-reference contrasts produce a direction; a gate selects a single bounded intervention">
      </a>
      <figcaption>QCVS overview, extracted from the supplied research manuscript.</figcaption>
    </figure>
    <details class="project-details">
      <summary>View research details</summary>
      <div class="project-details__content">
        <ul>
          <li><strong>Question-contrastive probing:</strong> Matched spatial controls are evaluated under a task question and a generic description reference. Their differential responses isolate the question-dependent interaction.</li>
          <li><strong>Selective intervention:</strong> Relative interaction strength and signal amplitude determine whether to apply one bounded update during a fresh prefix replay. Model parameters remain frozen.</li>
          <li><strong>Evaluation:</strong> The manuscript evaluates multimodal mathematical reasoning on DynaMath and We-Math, reporting accuracy alongside repair, damage, and intervention coverage.</li>
        </ul>
        <p class="needs-confirmation"><strong>My specific contributions:</strong> Please confirm the division of method design, implementation, experiments, and writing.</p>
      </div>
    </details>
  </article>

  <article class="project-card">
    <header class="project-card__header">
      <h3 class="project-card__title">CFMS: A Coarse-to-Fine Multimodal Synthesis Framework for Enhanced Tabular Reasoning</h3>
      <p class="project-card__meta">Third author · Accepted at PRCV 2026 (Main Track)</p>
    </header>
    <p class="project-card__summary">CFMS combines an initial multimodal understanding of a table with a sequence of targeted symbolic operations. Visual, semantic, and statistical descriptions provide context for the subsequent reasoning process.</p>
    <figure class="project-media project-media--wide">
      <a href="{{ '/assets/research/cfms-overview.png' | relative_url }}">
        <img src="{{ '/assets/research/cfms-overview.png' | relative_url }}" width="1400" height="760" loading="lazy" decoding="async" alt="CFMS overview: coarse visual, semantic, and statistical descriptions guide fine-grained table operations">
      </a>
      <figcaption>CFMS framework, extracted from the supplied research manuscript. The table is an illustrative example.</figcaption>
    </figure>
    <details class="project-details">
      <summary>View research details</summary>
      <div class="project-details__content">
        <ul>
          <li><strong>Coarse stage:</strong> Synthesize visual, semantic, and statistical information into a compact textual knowledge tuple.</li>
          <li><strong>Fine stage:</strong> Guide an LLM planner through table operations such as column creation, selection, grouping, and sorting before answer generation.</li>
          <li><strong>Evaluation:</strong> Assess table question answering on WikiTQ and table-based fact verification on TabFact.</li>
        </ul>
        <p class="needs-confirmation"><strong>My specific contributions:</strong> Please confirm the modules, experiments, and manuscript work I personally completed.</p>
      </div>
    </details>
    <p class="project-card__source"><a href="#publications">Publication details</a> · <span class="needs-confirmation">Final proceedings citation, DOI, and public paper/code links to confirm.</span></p>
  </article>
</div>

## Experience {#experience}

<div class="experience-list" markdown="1">

- **[Hikvision](https://www.hikvision.com/en/)**<br>
  <span class="needs-confirmation">Jun. 2026 – Present · Hangzhou, China · Product Management Engineer, Industrial AI — provisional role and dates.</span><br>
  <span class="needs-confirmation">Provisional scope from the existing experience draft: industrial multimodal applications, visual inspection, defect detection, false-alarm analysis, and human-in-the-loop evaluation. Exact responsibilities and implementation ownership require confirmation.</span>

- **[DPtech](https://www.dptech.com/)**<br>
  <span class="needs-confirmation">Jul. 2024 – May 2026 · Hangzhou, China · Product Manager, Network Security Products — provisional role and dates.</span><br>
  <span class="needs-confirmation">Provisional scope from the existing experience draft: LLM/RAG-based security applications, structured-data classification, annotation workflows, and evaluation criteria. Exact responsibilities and outcome measurements require confirmation.</span>

- **[Taiyuan University of Technology](https://english.tyut.edu.cn/)**<br>
  Sept. 2020 – Jul. 2024<br>
  **Computer Science and Technology**<br>
  Undergraduate studies; completed the coursework of the Excellent Engineer Education and Training Program.<br>
  <span class="needs-confirmation">Official degree title and award details to be checked against the degree certificate.</span>

</div>

## Publications {#publications}

### Submitted Manuscript

- **Tong Fu** et al. **QCVS: Question-Contrastive Visual Steering for Multimodal Reasoning.** Submitted to ICASSP 2027; submission confirmed on Sept. 14, 2026.<br>

### Accepted Paper

- Qixian Huang<sup>*</sup>, Hongqiang Lin<sup>*</sup>, **Tong Fu**, Yingsen Wang, Zhenghui Fu, Qirui Wang, Yiding Sun<sup>†</sup>, and Dongxu Zhang<sup>†</sup>. **CFMS: A Coarse-to-Fine Multimodal Synthesis Framework for Enhanced Tabular Reasoning.** Accepted at PRCV 2026 (Main Track).<br>
  <span class="needs-confirmation">Final publication citation, DOI, and accessible paper link to confirm.</span>

<p class="publication-note"><sup>*</sup> Equal contribution. <sup>†</sup> Corresponding authors. Author markers above follow the supplied CFMS manuscript.</p>

## Honors and Awards {#awards}

- **Academic Excellence Award (学业优秀奖)**, Taiyuan University of Technology<br>
  First semester of the 2020–2021 academic year; certificate issued in Apr. 2021.

- **Social Service Award (社会工作奖)**, Taiyuan University of Technology<br>
  First semester of the 2020–2021 academic year; certificate issued in Apr. 2021.

- **Outstanding Communist Youth League Student Cadre (优秀共青团干部)**, Taiyuan University of Technology<br>
  2020–2021 academic year; certificate issued in May 2021.

- **Excellent Engineer Education and Training Program — Coursework Completion**<br>
  Taiyuan University of Technology; certificate issued in Jun. 2024.

## Skills {#skills}

<p class="review-note">Research topics are grounded in the manuscripts above. <span class="needs-confirmation">Red nodes marked “confirm” identify individual skills or tools that still need confirmation.</span></p>

{% include skills-mindmap.html %}

## Related Learning Resources {#resources}

Selected reference resources for the research topics above.

{% include learning-resources.html %}

## CV and Contact {#contact}

[**Download academic CV (PDF)**]({{ '/assets/CV_TongFu.pdf' | relative_url }}?v={{ site.time | date: '%s' }})<br>
For research discussions or MPhil opportunities starting in Fall 2027, please contact [**futong0414@163.com**](mailto:futong0414@163.com). You can also find me on [**GitHub**](https://github.com/TongFu0414).
