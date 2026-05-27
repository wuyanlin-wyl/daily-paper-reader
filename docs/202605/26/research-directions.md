# 研究方向与二次创新路线 · 2026-05-26

- 生成时间：2026-05-27 09:30:46 UTC
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

- [Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence](https://arxiv.org/abs/2605.22414v1)：提出一个具有空间定位病灶证据的临床可解释眼科VQA基准FundusGround，通过ETDRS网格映射病灶，生成多格式问题，并验证病灶级视觉证据提升模型性能与透明度。
- [Towards Reliable Fetal Ultrasound Interpretation with Multi-Agent Collaboration](https://arxiv.org/abs/2605.25357v1)：提出FetUSAgents，一种工具增强的多智能体系统，通过双路径证据仲裁（DPEA）和检索增强证据库，实现可靠、可溯源的胎儿超声解读。
- [RAPTOR+: A Visually Grounded Vision-Language Framework to Improve Clinical Trust and Auditability in Automated Cancer Referral Processing](https://arxiv.org/abs/2605.25956v1)：针对紧急疑似结直肠癌转诊处理中手动审查的瓶颈，本文提出RAPTOR+多模态框架，通过微调视觉语言模型实现端到端转诊理解，并在223份临床转诊表单上评估。相比零样本模型和OCR管道，微调模型显著提升了阅读准确率（96.1%）和证据定位的严格安全性（60.6%），增强了临床可审计性。
- [MedFM-Robust: Benchmarking Robustness of Medical Foundation Models](https://arxiv.org/abs/2605.19027v3)：构建了一个包含40种扰动类型、覆盖八种成像模态的医疗基础模型鲁棒性基准，系统评估了视觉-语言模型和分割模型在不同微调策略下的表现，揭示了微调策略的主导作用及领域特定扰动的严重性。
- [RoboSurg-VQA: A Multimodal Benchmark for Surgical Segmentation-Aware Visual Question Answering](https://arxiv.org/abs/2605.23068v1)：提出了RoboSurg-VQA，一个通过重用公共手术分割数据集构建的分割感知视觉问答基准，配有一组固定的临床问题，并采用约束提示自动生成候选答案加人工审计以确保质量。
- [What Makes a Medical Checker Trainable? Diagnosing Signal Collapse and Reward Hacking in Checker-Guided RAG for Biomedical QA](https://arxiv.org/abs/2605.25988v1)：发现医学RAG中NLI检查器的输出分布而非准确率决定其作为强化学习奖励的可训练性，诊断了信号坍缩和奖励破解，并提出适度信号策略可提升模型质量。
- [BalanceRAG: Joint Risk Calibration for Cascaded Retrieval-Augmented Generation](https://arxiv.org/abs/2605.20084v1)：提出BalanceRAG，通过联合校准LLM-only和RAG两个分支的不确定性阈值，在二维网格上用序列图检验控制系统级错误率，提高覆盖率并减少不必要的检索调用。
- [VRXU-net: A Deep Learning Approach for Brain Ischemic Stroke Lesion Detection and Segmentation in T1W MRI](https://arxiv.org/abs/2605.21633v1)：提出一种结合改进VGG分类和残差U-Net分割的VRXU-net方法，通过三平面聚合和预分类器减少非病变切片处理，提高脑缺血性卒中病变检测和分割的准确率及Dice系数。
- [Med-R2: An Adversarial Benchmark for Evidence-Grounded Reasoning in Medical VLMs](https://arxiv.org/abs/2605.24492v1)：提出Med-R2 Bench基准，通过层级化对抗性评估来测试医学视觉语言模型是否基于视觉证据推理而非依赖虚假先验。
- [Thinking in Scales: Accelerating Gigapixel Pathology Image Analysis via Adaptive Continuous Reasoning](https://arxiv.org/abs/2605.19491v2)：提出PathCTM模型，通过自适应连续推理（动态尺度切换和早期停止）大幅提升全切片图像分析的效率，减少约96%的patch和推理时间，同时保持诊断准确率。
- [Cardiac fat segmentation using computed tomography and an image-to-image conditional generative adversarial neural network](https://arxiv.org/abs/2605.20064v1)：提出基于条件生成对抗网络pix2pix的自动分割方法，实现CT图像中心外膜和纵隔脂肪的高精度实时分割。

### 共同创新点
- 提出一个具有空间定位病灶证据的临床可解释眼科VQA基准FundusGround，通过ETDRS网格映射病灶，生成多格式问题，并验证病灶级视觉证据提升模型性能与透明度。
- 提出FetUSAgents，一种工具增强的多智能体系统，通过双路径证据仲裁（DPEA）和检索增强证据库，实现可靠、可溯源的胎儿超声解读。
- 针对紧急疑似结直肠癌转诊处理中手动审查的瓶颈，本文提出RAPTOR+多模态框架，通过微调视觉语言模型实现端到端转诊理解，并在223份临床转诊表单上评估。相比零样本模型和OCR管道，微调模型显著提升了阅读准确率（96.1%）和证据定位的严格安全性（60.6%），增强了临床可审计性。
- 构建了一个包含40种扰动类型、覆盖八种成像模态的医疗基础模型鲁棒性基准，系统评估了视觉-语言模型和分割模型在不同微调策略下的表现，揭示了微调策略的主导作用及领域特定扰动的严重性。

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

- [PrivFusion: A Privacy-preserving Multi-Agent Framework for Harmonizing Distributed Datasets](https://arxiv.org/abs/2605.24249v1)：提出PrivFusion，一个在联邦学习前自动协调多机构结构化数据集的隐私保护多智能体框架，通过本地数据分析和语义聚类减少人工干预。
- [Parameter-Efficient VLMs for Gastrointestinal Endoscopy: Medical Image Generation and Clinical Visual Question Answering](https://arxiv.org/abs/2605.24792v1)：提出双流水线PEFT模型，利用Florence-2和LoRA微调Stable Diffusion 2.1，同时解决胃肠内镜VQA和隐私保护合成图像生成问题。
- [ImPartial: Multi-channel Whole-Cell Segmentation using Partial Annotations](https://arxiv.org/abs/2605.24128v1)：提出ImPartial框架，利用稀疏涂鸦和自监督多通道量化插值，在部分标注下实现与全监督相当的细胞分割性能。

### 共同创新点
- 提出PrivFusion，一个在联邦学习前自动协调多机构结构化数据集的隐私保护多智能体框架，通过本地数据分析和语义聚类减少人工干预。
- 提出双流水线PEFT模型，利用Florence-2和LoRA微调Stable Diffusion 2.1，同时解决胃肠内镜VQA和隐私保护合成图像生成问题。
- 提出ImPartial框架，利用稀疏涂鸦和自监督多通道量化插值，在部分标注下实现与全监督相当的细胞分割性能。

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

- [Universal Boosts, Specific Suppressors: Sparse Autoencoder Steering of Medical Vision-Language Models](https://arxiv.org/abs/2605.24977v1)：提出一种基于稀疏自编码器的解码时残差引导方法，通过逐token因果干预（提升正确特征、抑制错误特征）改善医学视觉语言模型生成胸部X光报告的质量。

### 共同创新点
- 提出一种基于稀疏自编码器的解码时残差引导方法，通过逐token因果干预（提升正确特征、抑制错误特征）改善医学视觉语言模型生成胸部X光报告的质量。

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

- [EchoPilot: Training-Free Ultrasound Video Segmentation via Scale-Space Semantic Prompting and Reliability-Gated Memory](https://arxiv.org/abs/2605.25944v1)：EchoPilot提出一种无需训练的超声视频分割框架，通过尺度空间语义提示和可靠性门控记忆，仅需单点点击和类别名称即可实现高质量分割。

### 共同创新点
- EchoPilot提出一种无需训练的超声视频分割框架，通过尺度空间语义提示和可靠性门控记忆，仅需单点点击和类别名称即可实现高质量分割。

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

- [PromptRad: Knowledge-Enhanced Multi-Label Prompt-Tuning for Low-Resource Radiology Report Labeling](https://arxiv.org/abs/2605.20052v1)：提出PromptRad，一种知识增强的多标签提示调优方法，用于低资源放射学报告标注，将多标签分类转化为掩码语言建模并利用UMLS同义词扩展词汇表。

### 共同创新点
- 提出PromptRad，一种知识增强的多标签提示调优方法，用于低资源放射学报告标注，将多标签分类转化为掩码语言建模并利用UMLS同义词扩展词汇表。

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

- [Divide-and-Conquer Inference for Large-Scale Visual Recognition with Multimodal Large Language Models](https://arxiv.org/abs/2605.24799v1)：提出分而治之推理（DCI）策略，通过递归分解大规模分类任务并动态剪枝，缓解多模态大语言模型在长序列识别中的注意力稀释和性能崩溃问题，实现无训练加速和精度提升。

### 共同创新点
- 提出分而治之推理（DCI）策略，通过递归分解大规模分类任务并动态剪枝，缓解多模态大语言模型在长序列识别中的注意力稀释和性能崩溃问题，实现无训练加速和精度提升。

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
