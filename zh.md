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
<span class="intro-highlight">我希望探索更广泛的人工智能前沿研究方向。</span>

我目前正在寻找 <strong class="intro-highlight">2027 年秋季入学的 MPhil 研究机会</strong>，欢迎联系我（[CV]({{ '/assets/CV_TongFu.pdf' | relative_url }}?v={{ site.time | date: '%s' }}) &nbsp; <a href="#email-modal" data-dialog-open="email-modal" aria-controls="email-modal" aria-haspopup="dialog">邮箱</a> &nbsp; <a href="#wechat-modal" data-dialog-open="wechat-modal" aria-controls="wechat-modal" aria-haspopup="dialog">微信</a>）。

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
    <p class="project-card__summary">面向视觉数学推理的免训练推理时方法，在 Qwen3.5 2B–9B 三档模型上将 DynaMath 准确率提升 <strong>1.76–2.52 个百分点</strong>，仅对 <strong>22%–30% 的输入</strong>施加干预。</p>
    <figure id="qcvs-overview" class="project-media project-media--wide">
      <a href="{{ '/assets/research/qcvs-overview.png' | relative_url }}">
        <img src="{{ '/assets/research/qcvs-overview.png' | relative_url }}" width="1527" height="948" loading="lazy" decoding="async" alt="QCVS 方法概览：匹配视觉控制与任务、参考提示的差分构造干预方向，经门控后进行单次有界干预">
      </a>
      <figcaption>QCVS：问题对比探测与选择性推理时引导。</figcaption>
    </figure>
    <details class="project-details">
      <summary>查看项目细节</summary>
      <div class="project-details__content">
        <p><strong>项目背景：</strong>视觉扰动会同时改变视觉语言模型中的问题相关证据和通用空间响应。沿混合信号进行引导，可能在修复错误答案的同时损伤原本正确的预测。QCVS 围绕两个相互关联的问题展开：如何提取与当前问题有关的干预方向，以及何时值得应用这一方向。</p>
        <ul>
          <li><strong>匹配视觉控制与双重差分探测：</strong>仅编码一次图像，通过重排互不重叠的 2 × 2 视觉 token 块构造两个控制条件，保留 token 向量集合、数量及块内结构。任务问题与固定的“Describe the visible content”参考提示使用相同的控制。在最后一个助手前缀 token 处，分别计算原始输入与控制输入的激活差，再用任务响应减去参考响应，对两个控制取均值，提取问题相关交互。整个过程需要六次前缀计算，无需生成答案，也不依赖真实答案标签或输出置信度。</li>
          <li><strong>双阈值门控与单点干预：</strong>分别衡量交互信号相对于扰动响应的强度、相对于原始任务状态的幅度，仅在两个阈值同时通过时执行更新。独立校准集确定幅度阈值及范数的第 5–95 百分位边界，验证集选择目标层、引导系数和相对强度阈值。对选中的输入，重新计算未扰动的任务前缀，在指定层、指定 token 处注入一次有界更新，重建后续生成需要的状态；未选中的输入沿保留的原始任务状态继续解码，模型权重始终冻结。</li>
          <li><strong>多规模评测与跨骨干迁移：</strong>在 DynaMath、We-Math 上与 Base、VCD、VISTA 和 Task-only 引导比较。Qwen3.5-2B、4B、9B 的 DynaMath 准确率分别提升 2.52、1.92、1.76 个百分点；9B 模型在两个基准上分别达到 85.35% 和 77.43%。采用各模型独立校准后，DeepSeek-VL2-Tiny、Small 的 DynaMath 准确率分别由 45.01% 提升至 47.13%、由 55.01% 提升至 56.95%。评测同时记录基线错误被修复的比例、原本正确答案被损伤的比例、干预覆盖率和生成 token 数。</li>
          <li><strong>控制覆盖率的方向与门控消融：</strong>在 Qwen3.5-4B / DynaMath 上，QCVS 以 25.01% 的覆盖率提升 1.92 个百分点，修复 13.98% 的基线错误，损伤 0.50% 的原本正确答案。在相同覆盖率下改用 Task-only 方向，增益降至 0.84 个百分点；随机方向、反向方向分别带来 −0.88、−1.86 个百分点的变化。移除门控、对全部输入干预后，净增益同样仅为 0.84 个百分点，损伤率升至 3.55%，从而区分方向构造与干预选择各自的作用。</li>
        </ul>
        <p><strong>核心结果：</strong>三档 Qwen3.5 的 DynaMath 准确率提升 <strong>1.76–2.52 个百分点</strong>；Qwen3.5-9B 在 DynaMath、We-Math 上分别达到 <strong>85.35%</strong>、<strong>77.43%</strong>；干预覆盖率约 <strong>22%–30%</strong>，无需微调模型。</p>
      </div>
    </details>
  </article>

  <article class="project-card">
    <header class="project-card__header">
      <h3 class="project-card__title">CFMS: A Coarse-to-Fine Multimodal Synthesis Framework for Enhanced Tabular Reasoning</h3>
      <p class="project-card__meta">PRCV 2026 主会 · 已录用</p>
    </header>
    <p class="project-card__summary">将多模态知识综合与迭代表格操作结合的两阶段框架。在 GPT-4 / GPT-4V 粗粒度阶段辅助下，使用 GPT-3.5 规划器，达到 <strong>81.37% 的 TabFact 准确率</strong>和 <strong>61.42% 的 WikiTQ 答案准确率</strong>。</p>
    <figure id="cfms-overview" class="project-media project-media--wide">
      <a href="{{ '/assets/research/cfms-overview.png' | relative_url }}">
        <img src="{{ '/assets/research/cfms-overview.png' | relative_url }}" width="1400" height="760" loading="lazy" decoding="async" alt="CFMS 框架：粗粒度的视觉、语义和统计描述，引导细粒度表格操作与答案生成">
      </a>
      <figcaption>CFMS：粗粒度知识综合与细粒度表格操作。</figcaption>
    </figure>
    <details class="project-details">
      <summary>查看项目细节</summary>
      <div class="project-details__content">
        <p><strong>项目背景：</strong>将表格序列化为文本容易弱化行列关系、趋势与异常值等整体信息，而在多步推理中反复处理视觉输入又会增加开销。CFMS 将一次性的表格整体理解与回答问题、验证陈述所需的精确符号操作分离，形成由粗到细的推理过程。</p>
        <ul>
          <li><strong>一次性的视觉、语义与统计知识综合：</strong>为输入表格生成并执行可视化代码，再由 GPT-4V 描述所得图表的整体模式；同时由 GPT-4 补充实体语义背景和数值摘要，包括关键列、最大值、最小值与均值。将三类描述合并为文本知识元组，在细粒度阶段持续复用，使规划器在处理原始结构化数据时保留全局视角。</li>
          <li><strong>带状态的符号规划与表格演化：</strong>规划器在每一步结合问题、当前表格、操作历史与粗粒度知识，选择新增计算列、选择列、筛选行、分组、排序等操作及其参数，执行后得到下一张表。例如，营收与研发投入比的问题需要先新增比值列，再筛选第二季度数据并识别最高比值。规划器输出 END 后，结合最终表格、问题与知识元组生成答案。</li>
          <li><strong>表格问答与事实验证：</strong>采用少样本上下文学习，在 WikiTQ 上评估答案准确率（denotation accuracy），在 TabFact 上评估二分类准确率。GPT-3.5-Turbo 规划器配合 GPT-4 / GPT-4V 粗粒度阶段，分别达到 81.37%、61.42%，较 Chain-of-Table 的 80.20%、59.94% 提升 1.17、1.48 个百分点。保留外部粗粒度阶段辅助、将规划器替换为 LLaMA-2-13B-Chat 后，两个基准的结果分别为 68.53%、43.89%。</li>
          <li><strong>大表格稳健性与模块消融：</strong>在超过 4,000 token 的 WikiTQ 大表格上，CFMS 达到 46.92% 准确率，Dater 为 34.62%。移除粗粒度阶段后，WikiTQ 整体准确率由 61.42% 降至 55.18%；移除细粒度阶段后降至 56.44%。操作池消融进一步显示精确表格操作的作用：移除分组操作后，WikiTQ 准确率降至 55.02%；移除行筛选后，TabFact 准确率由 81.37% 降至 76.79%。</li>
          <li><strong>明确的模型调用预算：</strong>论文的 WikiTQ 对比中，每个问题最多调用模型 15 次，包括粗粒度知识综合 4 次、细粒度规划最多 10 次、最终回答 1 次；对比配置中的 Binder、Dater 分别为 50、100 次。该指标衡量调用次数，粗粒度阶段使用的较强模型具有更高的单次调用成本。</li>
        </ul>
        <p><strong>核心结果：</strong>GPT-4 / GPT-4V 辅助的 GPT-3.5 规划器在 TabFact、WikiTQ 上分别达到 <strong>81.37%</strong>、<strong>61.42%</strong>，较 Chain-of-Table 提升 <strong>1.17 / 1.48 个百分点</strong>；WikiTQ 大表格准确率为 <strong>46.92%</strong>。</p>
      </div>
    </details>
  </article>
</div>

## 经历 {#experience}

<div class="experience-list" markdown="1">

- {% include experience-logos.html organizations="hikvision" %} **[海康威视](https://www.hikvision.com/)**，中国杭州<br>
  2026 年 6 月至今<br>
  **工业 AI 产品管理工程师**<br>
  方向：工业多模态 AI / 智慧工厂应用<br>
  围绕工业视觉检测与生产过程监控，开展产品需求、模型评测标准与人工复核流程相关工作。

- {% include experience-logos.html organizations="dptech" %} **[迪普科技](https://www.dptech.com/)**，中国杭州<br>
  2024 年 7 月至 2026 年 5 月<br>
  **网络安全产品经理**<br>
  方向：LLM/RAG 安全应用 / 数据分类<br>
  与领域专家及算法团队协作，开展产品与数据需求、标注流程和评测标准相关工作。

- {% include experience-logos.html organizations="tyut" %} **[太原理工大学（211）](https://www.tyut.edu.cn/)**，中国山西<br>
  2020 年 9 月至 2024 年 7 月<br>
  **计算机科学与技术，工学学士**<br>
  卓越工程师教育培养计划<br>
  **综合测评排名：**前 12.7%（24/189） [\[证明材料\]]({{ '/assets/evidence/Evidence_Comprehensive_Evaluation_Rank.pdf' | relative_url }})

</div>

## 论文 {#publications}

### 在审稿件

- **T. Fu**<sup>&#42;</sup> 等，[QCVS: Question-Contrastive Visual Steering for Multimodal Reasoning](#qcvs-overview)。*2027 IEEE International Conference on Acoustics, Speech and Signal Processing（ICASSP 2027）。* **审稿中。**

### 已录用论文

- Q. Huang<sup>&#42;</sup>, H. Lin<sup>&#42;</sup>, **T. Fu**, Y. Wang, Z. Fu, Q. Wang, Y. Sun<sup>†</sup>, and D. Zhang<sup>†</sup>，[CFMS: A Coarse-to-Fine Multimodal Synthesis Framework for Enhanced Tabular Reasoning](#cfms-overview)。*2026 Chinese Conference on Pattern Recognition and Computer Vision（PRCV 2026，主会）。* **已录用。**

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

## 联系方式 {#contact}

学术 CV：[**Tong Fu (付彤)**]({{ '/assets/CV_TongFu.pdf' | relative_url }}?v={{ site.time | date: '%s' }})<br>
邮箱：[**futong0414@163.com**](mailto:futong0414@163.com)<br>
微信：Ft_Be_admitted_to
