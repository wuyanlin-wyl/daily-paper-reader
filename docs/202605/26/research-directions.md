# 研究方向与二次创新路线 · 2026-05-26

- 生成时间：2026-05-27 08:49:16 UTC
- 当日论文数：18
- 方向数：6

## 今日方向总览

| 方向 | 论文数 | 代表论文 |
|---|---:|---|
| 医学 VLM 可解释性与视觉证据定位 | 11 | Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence<br>Towards Reliable Fetal Ultrasound Interpretation with Multi-Agent Collaboration<br>RAPTOR+: A Visually Grounded Vision-Language Framework to Improve Clinical Trust and Auditability in Automated Cancer Referral Processing |
| 医学多智能体与可靠推理 | 3 | PrivFusion: A Privacy-preserving Multi-Agent Framework for Harmonizing Distributed Datasets<br>Parameter-Efficient VLMs for Gastrointestinal Endoscopy: Medical Image Generation and Clinical Visual Question Answering<br>ImPartial: Multi-channel Whole-Cell Segmentation using Partial Annotations |
| 医学视觉语言模型 | 1 | Universal Boosts, Specific Suppressors: Sparse Autoencoder Steering of Medical Vision-Language Models |
| 医学图像分割与低标注学习 | 1 | EchoPilot: Training-Free Ultrasound Video Segmentation via Scale-Space Semantic Prompting and Reliability-Gated Memory |
| 大规模视觉识别与高效推理 | 1 | PromptRad: Knowledge-Enhanced Multi-Label Prompt-Tuning for Low-Resource Radiology Report Labeling |
| 医学基础模型鲁棒性与评测基准 | 1 | Divide-and-Conquer Inference for Large-Scale Visual Recognition with Multimodal Large Language Models |

## 方向 1：医学 VLM 可解释性与视觉证据定位
该方向包含 11 篇论文，建议结合单篇创新点进一步细分子问题。

### 代表论文

- [Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence](https://arxiv.org/abs/2605.22414v1)：提出FundusGround基准，通过ETDRS网格空间定位病变证据，提升眼科VQA的可解释性和准确性。
- [Towards Reliable Fetal Ultrasound Interpretation with Multi-Agent Collaboration](https://arxiv.org/abs/2605.25357v1)：提出FetUSAgents，一种工具增强的多智能体系统，通过双路径证据仲裁和检索增强证据库，实现可靠的胎儿超声解读，在VQA等任务上显著优于现有方法。
- [RAPTOR+: A Visually Grounded Vision-Language Framework to Improve Clinical Trust and Auditability in Automated Cancer Referral Processing](https://arxiv.org/abs/2605.25956v1)：提出RAPTOR+，一种基于视觉语言模型的多模态框架，通过微调VLM实现端到端癌症转诊表单理解，显著提升阅读准确率和视觉证据定位的严格安全性，增强临床可审计性。
- [MedFM-Robust: Benchmarking Robustness of Medical Foundation Models](https://arxiv.org/abs/2605.19027v3)：构建了涵盖40种扰动、8种成像模态的医疗基础模型鲁棒性基准，系统评估了VLM和分割模型在不同微调策略下的性能退化，揭示了微调策略与领域特定扰动对鲁棒性的主导作用。
- [RoboSurg-VQA: A Multimodal Benchmark for Surgical Segmentation-Aware Visual Question Answering](https://arxiv.org/abs/2605.23068v1)：提出一个面向机器人辅助手术的分割感知视觉问答基准RoboSurg-VQA，通过重用公共分割数据集、设计临床问题集和约束提示自动标注+人工审计，为手术视觉理解提供标准化评估平台。
- [What Makes a Medical Checker Trainable? Diagnosing Signal Collapse and Reward Hacking in Checker-Guided RAG for Biomedical QA](https://arxiv.org/abs/2605.25988v1)：发现医学RAG中NLI检查器的输出分布（而非准确率）决定其作为RL奖励的可训练性，诊断出信号坍缩和奖励破解两种现象，并证明适度信号检查器训练出的模型优于强信号检查器。
- [BalanceRAG: Joint Risk Calibration for Cascaded Retrieval-Augmented Generation](https://arxiv.org/abs/2605.20084v1)：提出BalanceRAG方法，通过二维网格上的序列图检验联合校准LLM-only和RAG分支的不确定性阈值，在控制系统级错误率的同时保留更多样本，并可扩展至多风险校准。
- [VRXU-net: A Deep Learning Approach for Brain Ischemic Stroke Lesion Detection and Segmentation in T1W MRI](https://arxiv.org/abs/2605.21633v1)：提出一种结合预分类器与三平面融合残差U-Net的VRXU-net方法，用于脑缺血性卒中病变检测与分割，在ATLAS数据集上提升准确率和Dice系数。
- [Med-R2: An Adversarial Benchmark for Evidence-Grounded Reasoning in Medical VLMs](https://arxiv.org/abs/2605.24492v1)：提出Med-R2 Bench，一个层级化对抗性基准，系统评估医学视觉语言模型在临床推理中是否真正基于视觉证据而非虚假相关性。
- [Thinking in Scales: Accelerating Gigapixel Pathology Image Analysis via Adaptive Continuous Reasoning](https://arxiv.org/abs/2605.19491v2)：提出PathCTM模型，实现token高效的尺度空间连续推理，大幅减少计算开销而不损失性能。
- [Cardiac fat segmentation using computed tomography and an image-to-image conditional generative adversarial neural network](https://arxiv.org/abs/2605.20064v1)：首次将pix2pix条件生成对抗网络应用于CT图像中心外膜和纵隔脂肪的自动分割，实现高精度和实时分割。

### 共同创新点
- 提出FundusGround基准，通过ETDRS网格空间定位病变证据，提升眼科VQA的可解释性和准确性。
- 提出FetUSAgents，一种工具增强的多智能体系统，通过双路径证据仲裁和检索增强证据库，实现可靠的胎儿超声解读，在VQA等任务上显著优于现有方法。
- 提出RAPTOR+，一种基于视觉语言模型的多模态框架，通过微调VLM实现端到端癌症转诊表单理解，显著提升阅读准确率和视觉证据定位的严格安全性，增强临床可审计性。
- 构建了涵盖40种扰动、8种成像模态的医疗基础模型鲁棒性基准，系统评估了VLM和分割模型在不同微调策略下的性能退化，揭示了微调策略与领域特定扰动对鲁棒性的主导作用。

### 尚未解决的问题
- 现有工作之间的评测协议、数据集和临床适用边界可能尚未统一。
- 需要进一步确认方法在真实场景、跨中心数据或外部验证集上的稳定性。

### 二次创新路线
#### 路线 1：统一评测与误差分解
- 核心想法：把同方向论文放到统一任务、统一指标和统一错误类型下比较，寻找稳定短板。
- 为什么值得做：同方向论文往往各自验证，统一评测能暴露可继续推进的真实问题。
- 可验证实验：复现或复用公开结果，构建共享测试集，按失败类型进行分层统计。
- 主要风险：不同论文的数据和任务定义不一致，可能需要较多人工清洗。

#### 路线 2：方法组合与轻量增强
- 核心想法：抽取该方向中互补的模块，例如解释、校准、隐私、效率或多智能体协作，组合成更完整方案。
- 为什么值得做：单篇论文通常只优化一个环节，模块组合可能带来更强的系统效果。
- 可验证实验：选择一个强基线，逐步加入互补模块并做消融实验。
- 主要风险：模块叠加可能增加复杂度，收益未必线性增长。

## 方向 2：医学多智能体与可靠推理
该方向包含 3 篇论文，建议结合单篇创新点进一步细分子问题。

### 代表论文

- [PrivFusion: A Privacy-preserving Multi-Agent Framework for Harmonizing Distributed Datasets](https://arxiv.org/abs/2605.24249v1)：提出PrivFusion框架，通过多智能体自动协调分布式医疗数据集，减少人工干预，提高联邦学习前的数据一致性。
- [Parameter-Efficient VLMs for Gastrointestinal Endoscopy: Medical Image Generation and Clinical Visual Question Answering](https://arxiv.org/abs/2605.24792v1)：提出双流水线参数高效微调（PEFT）模型，同时解决胃肠内镜中隐私保护合成图像生成和临床视觉问答问题。
- [ImPartial: Multi-channel Whole-Cell Segmentation using Partial Annotations](https://arxiv.org/abs/2605.24128v1)：提出ImPartial框架，利用稀疏部分标注和自监督多通道量化插值，实现与全监督相当的细胞分割性能，大幅减少标注需求。

### 共同创新点
- 提出PrivFusion框架，通过多智能体自动协调分布式医疗数据集，减少人工干预，提高联邦学习前的数据一致性。
- 提出双流水线参数高效微调（PEFT）模型，同时解决胃肠内镜中隐私保护合成图像生成和临床视觉问答问题。
- 提出ImPartial框架，利用稀疏部分标注和自监督多通道量化插值，实现与全监督相当的细胞分割性能，大幅减少标注需求。

### 尚未解决的问题
- 现有工作之间的评测协议、数据集和临床适用边界可能尚未统一。
- 需要进一步确认方法在真实场景、跨中心数据或外部验证集上的稳定性。

### 二次创新路线
#### 路线 1：统一评测与误差分解
- 核心想法：把同方向论文放到统一任务、统一指标和统一错误类型下比较，寻找稳定短板。
- 为什么值得做：同方向论文往往各自验证，统一评测能暴露可继续推进的真实问题。
- 可验证实验：复现或复用公开结果，构建共享测试集，按失败类型进行分层统计。
- 主要风险：不同论文的数据和任务定义不一致，可能需要较多人工清洗。

#### 路线 2：方法组合与轻量增强
- 核心想法：抽取该方向中互补的模块，例如解释、校准、隐私、效率或多智能体协作，组合成更完整方案。
- 为什么值得做：单篇论文通常只优化一个环节，模块组合可能带来更强的系统效果。
- 可验证实验：选择一个强基线，逐步加入互补模块并做消融实验。
- 主要风险：模块叠加可能增加复杂度，收益未必线性增长。

## 方向 3：医学视觉语言模型
该方向包含 1 篇论文，建议结合单篇创新点进一步细分子问题。

### 代表论文

- [Universal Boosts, Specific Suppressors: Sparse Autoencoder Steering of Medical Vision-Language Models](https://arxiv.org/abs/2605.24977v1)：提出一种基于稀疏自编码器的解码时残差引导方法，通过逐token因果干预（提升正确特征、抑制错误特征），在不更新权重的情况下显著减少医学视觉语言模型在胸部X光报告生成中的幻觉，并发现提升方向跨模型通用而抑制方向模型特异。

### 共同创新点
- 提出一种基于稀疏自编码器的解码时残差引导方法，通过逐token因果干预（提升正确特征、抑制错误特征），在不更新权重的情况下显著减少医学视觉语言模型在胸部X光报告生成中的幻觉，并发现提升方向跨模型通用而抑制方向模型特异。

### 尚未解决的问题
- 现有工作之间的评测协议、数据集和临床适用边界可能尚未统一。
- 需要进一步确认方法在真实场景、跨中心数据或外部验证集上的稳定性。

### 二次创新路线
#### 路线 1：统一评测与误差分解
- 核心想法：把同方向论文放到统一任务、统一指标和统一错误类型下比较，寻找稳定短板。
- 为什么值得做：同方向论文往往各自验证，统一评测能暴露可继续推进的真实问题。
- 可验证实验：复现或复用公开结果，构建共享测试集，按失败类型进行分层统计。
- 主要风险：不同论文的数据和任务定义不一致，可能需要较多人工清洗。

#### 路线 2：方法组合与轻量增强
- 核心想法：抽取该方向中互补的模块，例如解释、校准、隐私、效率或多智能体协作，组合成更完整方案。
- 为什么值得做：单篇论文通常只优化一个环节，模块组合可能带来更强的系统效果。
- 可验证实验：选择一个强基线，逐步加入互补模块并做消融实验。
- 主要风险：模块叠加可能增加复杂度，收益未必线性增长。

## 方向 4：医学图像分割与低标注学习
该方向包含 1 篇论文，建议结合单篇创新点进一步细分子问题。

### 代表论文

- [EchoPilot: Training-Free Ultrasound Video Segmentation via Scale-Space Semantic Prompting and Reliability-Gated Memory](https://arxiv.org/abs/2605.25944v1)：提出一种无需训练的超声视频分割框架EchoPilot，通过尺度空间语义提示和可靠性门控记忆，仅需单点点击和类别名称即可实现高质量分割，并在多个数据集上达到最优性能。

### 共同创新点
- 提出一种无需训练的超声视频分割框架EchoPilot，通过尺度空间语义提示和可靠性门控记忆，仅需单点点击和类别名称即可实现高质量分割，并在多个数据集上达到最优性能。

### 尚未解决的问题
- 现有工作之间的评测协议、数据集和临床适用边界可能尚未统一。
- 需要进一步确认方法在真实场景、跨中心数据或外部验证集上的稳定性。

### 二次创新路线
#### 路线 1：统一评测与误差分解
- 核心想法：把同方向论文放到统一任务、统一指标和统一错误类型下比较，寻找稳定短板。
- 为什么值得做：同方向论文往往各自验证，统一评测能暴露可继续推进的真实问题。
- 可验证实验：复现或复用公开结果，构建共享测试集，按失败类型进行分层统计。
- 主要风险：不同论文的数据和任务定义不一致，可能需要较多人工清洗。

#### 路线 2：方法组合与轻量增强
- 核心想法：抽取该方向中互补的模块，例如解释、校准、隐私、效率或多智能体协作，组合成更完整方案。
- 为什么值得做：单篇论文通常只优化一个环节，模块组合可能带来更强的系统效果。
- 可验证实验：选择一个强基线，逐步加入互补模块并做消融实验。
- 主要风险：模块叠加可能增加复杂度，收益未必线性增长。

## 方向 5：大规模视觉识别与高效推理
该方向包含 1 篇论文，建议结合单篇创新点进一步细分子问题。

### 代表论文

- [PromptRad: Knowledge-Enhanced Multi-Label Prompt-Tuning for Low-Resource Radiology Report Labeling](https://arxiv.org/abs/2605.20052v1)：提出一种知识增强的多标签提示调优方法PromptRad，在低资源放射学报告标注中仅需少量标注数据即可超越传统方法并与GPT-4性能相当。

### 共同创新点
- 提出一种知识增强的多标签提示调优方法PromptRad，在低资源放射学报告标注中仅需少量标注数据即可超越传统方法并与GPT-4性能相当。

### 尚未解决的问题
- 现有工作之间的评测协议、数据集和临床适用边界可能尚未统一。
- 需要进一步确认方法在真实场景、跨中心数据或外部验证集上的稳定性。

### 二次创新路线
#### 路线 1：统一评测与误差分解
- 核心想法：把同方向论文放到统一任务、统一指标和统一错误类型下比较，寻找稳定短板。
- 为什么值得做：同方向论文往往各自验证，统一评测能暴露可继续推进的真实问题。
- 可验证实验：复现或复用公开结果，构建共享测试集，按失败类型进行分层统计。
- 主要风险：不同论文的数据和任务定义不一致，可能需要较多人工清洗。

#### 路线 2：方法组合与轻量增强
- 核心想法：抽取该方向中互补的模块，例如解释、校准、隐私、效率或多智能体协作，组合成更完整方案。
- 为什么值得做：单篇论文通常只优化一个环节，模块组合可能带来更强的系统效果。
- 可验证实验：选择一个强基线，逐步加入互补模块并做消融实验。
- 主要风险：模块叠加可能增加复杂度，收益未必线性增长。

## 方向 6：医学基础模型鲁棒性与评测基准
该方向包含 1 篇论文，建议结合单篇创新点进一步细分子问题。

### 代表论文

- [Divide-and-Conquer Inference for Large-Scale Visual Recognition with Multimodal Large Language Models](https://arxiv.org/abs/2605.24799v1)：提出分而治之推理（DCI）策略，通过递归分解大规模分类任务并动态剪枝，克服MLLM在长序列推理中的性能崩溃，实现即插即用的测试时扩展。

### 共同创新点
- 提出分而治之推理（DCI）策略，通过递归分解大规模分类任务并动态剪枝，克服MLLM在长序列推理中的性能崩溃，实现即插即用的测试时扩展。

### 尚未解决的问题
- 现有工作之间的评测协议、数据集和临床适用边界可能尚未统一。
- 需要进一步确认方法在真实场景、跨中心数据或外部验证集上的稳定性。

### 二次创新路线
#### 路线 1：统一评测与误差分解
- 核心想法：把同方向论文放到统一任务、统一指标和统一错误类型下比较，寻找稳定短板。
- 为什么值得做：同方向论文往往各自验证，统一评测能暴露可继续推进的真实问题。
- 可验证实验：复现或复用公开结果，构建共享测试集，按失败类型进行分层统计。
- 主要风险：不同论文的数据和任务定义不一致，可能需要较多人工清洗。

#### 路线 2：方法组合与轻量增强
- 核心想法：抽取该方向中互补的模块，例如解释、校准、隐私、效率或多智能体协作，组合成更完整方案。
- 为什么值得做：单篇论文通常只优化一个环节，模块组合可能带来更强的系统效果。
- 可验证实验：选择一个强基线，逐步加入互补模块并做消融实验。
- 主要风险：模块叠加可能增加复杂度，收益未必线性增长。
