---
permalink: /zh/
seo_title: "付彤 Tong Fu"
description: "付彤，太原理工大学（211）计算机科学与技术专业毕业，正在寻找 2027 年秋季入学的 MPhil 研究机会。"
lang: zh-CN
locale: zh_CN
alternate_url: /
alternate_lang: en
language_switch_label: English
language_switch_aria_label: Switch to English
author_profile: true
hide_title: true
homepage: true
skills_mindmap: true
---

# Tong Fu（付彤）
---

很高兴与你在这里相遇！<br>
我于 2024 年毕业于[太原理工大学（211）](https://www.tyut.edu.cn/)，专业为**计算机科学与技术**。

我的研究经历涉及**多模态推理**、**推理时引导**与**结构化数据理解**。<br>
在此基础上，我也希望探索更广泛的人工智能前沿研究方向。

我目前正在寻找 **2027 年秋季入学的 MPhil 研究机会**，欢迎通过[邮箱](mailto:futong0414@163.com)交流。

## 研究兴趣 {#research-interest}

**人工智能：**多模态学习、视觉语言模型与推理时方法；<br>
**AI 应用：**结构化数据推理、工业检测与网络安全应用。

## 精选研究项目 {#research}

<div class="project-list">
  <article class="project-card">
    <header class="project-card__header">
      <h3 class="project-card__title">QCVS: Question-Contrastive Visual Steering for Multimodal Reasoning</h3>
      <p class="project-card__meta">ICASSP 2027 · 审稿中</p>
    </header>
    <p class="project-card__summary">通过问题对比视觉引导改进多模态推理的免训练框架。QCVS 将问题相关信号与共享扰动效应分离，在模型参数保持冻结的条件下，选择性地施加有界隐状态更新。</p>
    <figure class="project-media project-media--wide">
      <a href="{{ '/assets/research/qcvs-overview.png' | relative_url }}">
        <img src="{{ '/assets/research/qcvs-overview.png' | relative_url }}" width="1527" height="948" loading="lazy" decoding="async" alt="QCVS 方法概览：匹配视觉控制与任务、参考提示的差分构造干预方向，经门控后进行单次有界干预">
      </a>
      <figcaption>QCVS：问题对比探测与选择性推理时引导。</figcaption>
    </figure>
    <details class="project-details">
      <summary>查看项目细节</summary>
      <div class="project-details__content">
        <ul>
          <li><strong>问题对比探测：</strong>在任务问题与通用图像描述提示下使用相同的空间控制，通过差分响应提取与问题相关的交互信号。</li>
          <li><strong>选择性干预：</strong>根据相对交互强度与信号幅度，决定是否在重新计算的干净前缀上施加一次有界更新，模型参数保持冻结。</li>
          <li><strong>评测：</strong>稿件在 DynaMath 与 We-Math 上评估多模态数学推理，同时报告准确率、修复率、损伤率和干预覆盖率。</li>
        </ul>
      </div>
    </details>
  </article>

  <article class="project-card">
    <header class="project-card__header">
      <h3 class="project-card__title">CFMS: A Coarse-to-Fine Multimodal Synthesis Framework for Enhanced Tabular Reasoning</h3>
      <p class="project-card__meta">PRCV 2026 主会 · 已录用</p>
    </header>
    <p class="project-card__summary">CFMS 先从多个模态和视角理解表格，再执行一系列有针对性的符号操作。视觉、语义与统计描述为后续推理提供整体上下文。</p>
    <figure class="project-media project-media--wide">
      <a href="{{ '/assets/research/cfms-overview.png' | relative_url }}">
        <img src="{{ '/assets/research/cfms-overview.png' | relative_url }}" width="1400" height="760" loading="lazy" decoding="async" alt="CFMS 框架：粗粒度的视觉、语义和统计描述，引导细粒度表格操作与答案生成">
      </a>
      <figcaption>CFMS：粗粒度知识综合与细粒度表格操作。</figcaption>
    </figure>
    <details class="project-details">
      <summary>查看项目细节</summary>
      <div class="project-details__content">
        <ul>
          <li><strong>粗粒度阶段：</strong>将视觉、语义和统计信息综合为紧凑的文本知识元组。</li>
          <li><strong>细粒度阶段：</strong>引导大语言模型规划器逐步执行新增列、选择、分组和排序等表格操作，随后生成答案。</li>
          <li><strong>评测：</strong>在 WikiTQ 上评估表格问答，在 TabFact 上评估基于表格的事实验证。</li>
        </ul>
      </div>
    </details>
  </article>
</div>

## 经历 {#experience}

<div class="experience-list" markdown="1">

- {% include experience-logos.html organizations="hikvision" %} **[海康威视](https://www.hikvision.com/)**，中国杭州<br>
  <span class="needs-confirmation">2026 年 6 月至今</span><br>
  <strong class="needs-confirmation">工业 AI 产品管理工程师</strong><br>
  方向：工业多模态 AI / 智慧工厂应用<br>
  <span class="needs-confirmation">围绕视觉检测与生产过程监控，开展产品需求、模型评测标准与人工复核流程相关工作。</span>

- {% include experience-logos.html organizations="dptech" %} **[迪普科技](https://www.dptech.com/)**，<span class="needs-confirmation">中国杭州</span><br>
  <span class="needs-confirmation">2024 年 7 月至 2026 年 5 月</span><br>
  <strong class="needs-confirmation">网络安全产品经理</strong><br>
  方向：LLM/RAG 安全应用 / 数据分类<br>
  <span class="needs-confirmation">与领域专家及算法团队协作，开展产品定义、数据准备、标注流程和评测标准相关工作。</span>

- {% include experience-logos.html organizations="tyut" %} **[太原理工大学（211）](https://www.tyut.edu.cn/)**，中国山西<br>
  2020 年 9 月至 2024 年 7 月<br>
  **计算机科学与技术，工学学士**<br>
  卓越工程师教育培养计划<br>
  **综合测评排名：**前 12.7%（24/189） [\[证明材料\]]({{ '/assets/evidence/Evidence_Comprehensive_Evaluation_Rank.pdf' | relative_url }})

</div>

## 论文 {#publications}

### 在审稿件

- **T. Fu**<sup>&#42;</sup> 等，QCVS: Question-Contrastive Visual Steering for Multimodal Reasoning. *2027 IEEE International Conference on Acoustics, Speech and Signal Processing（ICASSP 2027）。* **审稿中。**

### 已录用论文

- Q. Huang<sup>&#42;</sup>, H. Lin<sup>&#42;</sup>, **T. Fu**, Y. Wang, Z. Fu, Q. Wang, Y. Sun<sup>†</sup>, and D. Zhang<sup>†</sup>，CFMS: A Coarse-to-Fine Multimodal Synthesis Framework for Enhanced Tabular Reasoning. *2026 Chinese Conference on Pattern Recognition and Computer Vision（PRCV 2026，主会）。* **已录用。**

<p class="publication-note"><sup>&#42;</sup> 共同第一作者。<sup>†</sup> 通讯作者。</p>

## 荣誉与奖励 {#awards}

- **“卓越工程师教育培养计划”课程合格证书**<br>
  2024 年 6 月 [\[证明材料\]]({{ '/assets/evidence/Evidence_Excellent_Engineer_Program_2024.pdf' | relative_url }})

- **优秀共青团干部**<br>
  2021 年 [\[证明材料\]]({{ '/assets/evidence/Evidence_Outstanding_Youth_League_Cadre_2021.pdf' | relative_url }})

- **学业优秀奖**<br>
  2021 年 4 月 [\[证明材料\]]({{ '/assets/evidence/Evidence_Academic_Excellence_Award_2021.pdf' | relative_url }})

- **社会工作奖**<br>
  2021 年 4 月 [\[证明材料\]]({{ '/assets/evidence/Evidence_Social_Work_Award_2021.pdf' | relative_url }})

- **迪普科技产品技术工程师认证**<br>
  证书有效期至 2026 年 7 月 [\[证明材料\]]({{ '/assets/evidence/Evidence_DPtech_Certification.pdf' | relative_url }})

## 技术能力 {#skills}

{% include skills-mindmap.html %}

## 受启发的文章 {#resources}

{% include learning-resources.html %}

## CV 与联系方式 {#contact}

[**下载英文学术 CV（PDF）**]({{ '/assets/CV_TongFu.pdf' | relative_url }}?v={{ site.time | date: '%s' }})<br>
邮箱：[**futong0414@163.com**](mailto:futong0414@163.com) · [**GitHub**](https://github.com/TongFu0414)
