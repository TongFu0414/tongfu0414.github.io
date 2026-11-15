---
permalink: /zh/
seo_title: "付彤 Tong Fu"
description: "付彤的个人主页：多模态推理、视觉语言模型与可靠人工智能，申请 2027 年秋季入学的 MPhil。"
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
我于 2020–2024 年在[太原理工大学](https://www.tyut.edu.cn/)学习**计算机科学与技术**，研究兴趣包括**多模态推理**、**视觉语言模型**与**可靠人工智能**。

我的研究涉及问题对比视觉引导与粗到细的表格推理。我关注模型如何使用视觉证据、何时应在推理阶段进行干预，以及怎样通过评测同时识别性能提升和失败情况。<br>
我正在寻求 **2027 年秋季入学的 MPhil 机会**，欢迎通过[邮箱](mailto:futong4024@163.com)交流。

<p class="review-note"><span class="needs-confirmation">红色高亮表示需要本人确认的信息，或仍需补充的资料。</span></p>

## 研究兴趣 {#research-interest}

**多模态推理：**视觉证据、数学推理与结构化数据理解；<br>
**推理时方法：**冻结模型中的激活引导与选择性干预；<br>
**可靠人工智能：**模型评测、失败分析及产业应用。

## 精选研究 {#research}

<div class="project-list">
  <article class="project-card">
    <header class="project-card__header">
      <h3 class="project-card__title">QCVS: Question-Contrastive Visual Steering for Multimodal Reasoning</h3>
      <p class="project-card__meta">第一作者 · 已投稿 ICASSP 2027</p>
    </header>
    <p class="project-card__summary">如何在推理时向视觉语言模型提供有效引导，同时减少对原本正确预测的干扰？QCVS 将问题相关的视觉信号与共享扰动效应分离，并选择性地施加有界隐状态更新。</p>
    <figure class="project-media project-media--wide">
      <a href="{{ '/assets/research/qcvs-overview.png' | relative_url }}">
        <img src="{{ '/assets/research/qcvs-overview.png' | relative_url }}" width="1527" height="948" loading="lazy" decoding="async" alt="QCVS 方法概览：匹配视觉控制与任务、参考提示的差分构造干预方向，经门控后进行单次有界干预">
      </a>
      <figcaption>QCVS 方法概览，提取自提供的论文稿件。</figcaption>
    </figure>
    <details class="project-details">
      <summary>查看研究细节</summary>
      <div class="project-details__content">
        <ul>
          <li><strong>问题对比探测：</strong>在任务问题与通用图像描述提示下使用相同的空间控制，通过差分响应提取与问题相关的交互信号。</li>
          <li><strong>选择性干预：</strong>根据相对交互强度与信号幅度，决定是否在重新计算的干净前缀上施加一次有界更新，模型参数保持冻结。</li>
          <li><strong>评测：</strong>稿件在 DynaMath 与 We-Math 上评估多模态数学推理，同时报告准确率、修复率、损伤率和干预覆盖率。</li>
        </ul>
        <p class="needs-confirmation"><strong>本人具体贡献：</strong>方法设计、代码实现、实验和论文写作的分工待本人确认。</p>
      </div>
    </details>
    <p class="project-card__source"><a href="#publications">论文信息</a> · <span class="needs-confirmation">最新审稿状态、最终作者列表以及公开论文、代码链接待确认。</span></p>
  </article>

  <article class="project-card">
    <header class="project-card__header">
      <h3 class="project-card__title">CFMS: A Coarse-to-Fine Multimodal Synthesis Framework for Enhanced Tabular Reasoning</h3>
      <p class="project-card__meta">第三作者 · PRCV 2026 主会已录用</p>
    </header>
    <p class="project-card__summary">CFMS 先从多个模态和视角理解表格，再执行一系列有针对性的符号操作。视觉、语义与统计描述为后续推理提供整体上下文。</p>
    <figure class="project-media project-media--wide">
      <a href="{{ '/assets/research/cfms-overview.png' | relative_url }}">
        <img src="{{ '/assets/research/cfms-overview.png' | relative_url }}" width="1400" height="760" loading="lazy" decoding="async" alt="CFMS 框架：粗粒度的视觉、语义和统计描述，引导细粒度表格操作与答案生成">
      </a>
      <figcaption>CFMS 框架，提取自提供的论文稿件；图中表格为方法示例。</figcaption>
    </figure>
    <details class="project-details">
      <summary>查看研究细节</summary>
      <div class="project-details__content">
        <ul>
          <li><strong>粗粒度阶段：</strong>将视觉、语义和统计信息综合为紧凑的文本知识元组。</li>
          <li><strong>细粒度阶段：</strong>引导大语言模型规划器逐步执行新增列、选择、分组和排序等表格操作，随后生成答案。</li>
          <li><strong>评测：</strong>在 WikiTQ 上评估表格问答，在 TabFact 上评估基于表格的事实验证。</li>
        </ul>
        <p class="needs-confirmation"><strong>本人具体贡献：</strong>负责模块、实验及论文工作待本人确认。</p>
      </div>
    </details>
    <p class="project-card__source"><a href="#publications">论文信息</a> · <span class="needs-confirmation">正式出版引用、DOI 以及公开论文、代码链接待确认。</span></p>
  </article>
</div>

## 经历 {#experience}

<div class="experience-list" markdown="1">

- **[海康威视](https://www.hikvision.com/)**<br>
  <span class="needs-confirmation">2026 年 6 月至今 · 中国杭州 · 工业 AI 产品管理工程师——岗位与任职日期为待核实草稿。</span><br>
  <span class="needs-confirmation">现有工作经历稿涉及工业多模态应用、视觉检测、缺陷识别、误报分析及人工复核评测。个人实际职责、负责模块与实现范围待确认。</span>

- **[迪普科技](https://www.dptech.com/)**<br>
  <span class="needs-confirmation">2024 年 7 月至 2026 年 5 月 · 中国杭州 · 网络安全产品经理——岗位与任职日期为待核实草稿。</span><br>
  <span class="needs-confirmation">现有工作经历稿涉及 LLM/RAG 安全应用、结构化数据分类、标注流程及评测标准。个人实际职责与成果数字口径待确认。</span>

- **[太原理工大学](https://www.tyut.edu.cn/)**<br>
  2020 年 9 月至 2024 年 7 月<br>
  **计算机科学与技术**<br>
  本科阶段学习；修完“卓越工程师教育培养计划”课程。<br>
  <span class="needs-confirmation">正式学位名称与授予情况待学位证核对。</span>

</div>

## 论文 {#publications}

### 已投稿稿件

- **Tong Fu** 等. **QCVS: Question-Contrastive Visual Steering for Multimodal Reasoning.** 已投稿 ICASSP 2027，投稿确认日期为 2026 年 9 月 14 日。<br>
  <span class="needs-confirmation">最终完整作者列表、单位、最新审稿状态及公开稿件链接待确认。</span>

### 已录用论文

- Qixian Huang<sup>*</sup>, Hongqiang Lin<sup>*</sup>, **Tong Fu**, Yingsen Wang, Zhenghui Fu, Qirui Wang, Yiding Sun<sup>†</sup>, and Dongxu Zhang<sup>†</sup>. **CFMS: A Coarse-to-Fine Multimodal Synthesis Framework for Enhanced Tabular Reasoning.** PRCV 2026 主会已录用。<br>
  <span class="needs-confirmation">正式出版引用、DOI 及可访问论文链接待确认。</span>

<p class="publication-note"><sup>*</sup> 共同第一作者。<sup>†</sup> 通讯作者。上述标记依据提供的 CFMS 稿件。</p>

## 荣誉与奖励 {#awards}

- **学业优秀奖**，太原理工大学<br>
  2020–2021 学年第一学期；证书颁发于 2021 年 4 月。

- **社会工作奖**，太原理工大学<br>
  2020–2021 学年第一学期；证书颁发于 2021 年 4 月。

- **优秀共青团干部**，太原理工大学<br>
  2020–2021 学年；证书颁发于 2021 年 5 月。

- **“卓越工程师教育培养计划”课程合格证书**<br>
  太原理工大学，2024 年 6 月。

## 技术能力 {#skills}

<p class="review-note">研究主题来自上述论文。<span class="needs-confirmation">标有“待确认”的红色节点表示个人技能或工具使用情况仍需确认。</span></p>

{% include skills-mindmap.html %}

## 相关学习资料 {#resources}

与上述研究主题相关的参考资源。

{% include learning-resources.html %}

## CV 与联系方式 {#contact}

[**下载英文学术 CV（草稿，PDF）**]({{ '/assets/CV_TongFu.pdf' | relative_url }})<br>
<span class="needs-confirmation">此稿依据现有材料整理，红色文字表示仍待本人确认的内容。</span><br>
欢迎就多模态推理或 2027 年秋季 MPhil 机会交流：[**futong4024@163.com**](mailto:futong4024@163.com)。也可以访问我的 [**GitHub**](https://github.com/TongFu0414)。
