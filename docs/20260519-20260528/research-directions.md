# 研究方向与二次创新路线 · 2026-05-19 ~ 2026-05-28

- 生成时间：2026-05-28 22:07:52 UTC
- 当日论文数：18
- 方向数：4

## 今日方向总览

| 方向 | 论文数 | 代表论文 |
|---|---:|---|
| 医学 VLM 可解释性与视觉证据定位 | 10 | A Human-in-the-Loop Framework for Efficient Prompt Selection in Microscopy Vision-Language Models<br>Claim-Selective Certification for High-Risk Medical Retrieval-Augmented Generation<br>Case-Aware Medical Image Classification with Multimodal Knowledge Graphs and Reliability-Guided Refinement |
| 医学多智能体与可靠推理 | 2 | Benchmarking Convolutional, Transformer, Hybrid, and Vision Language Models for Multi Disease Retinal Screening<br>WBCAtt+: Fine-Grained Pixel-Level Morphological Annotations for White Blood Cell Images |
| 医学图像分割与低标注学习 | 4 | SpineContextResUNet: A Computationally Efficient Residual UNet for Spine CT Segmentation<br>Radiuma: A Unified Zero-Code Executable Graphical Workflow Generator for Reproducible and Shareable Medical Image Analysis and Machine Learning<br>D-Convexity: A Unified Differentiable Convex Shape Prior via Quasi-Concavity for Data-driven Image Segmentation |
| 医学基础模型鲁棒性与评测基准 | 2 | VISTA: Validation-Guided Integration of Spatial and Temporal Foundation Models with Anatomical Decoding for Rare-Pathology VCE Event Detection -- after competition results<br>Rotation-Aligned Key Channel Pruning for Efficient Vision-Language Model Inference |

## 方向 1：医学 VLM 可解释性与视觉证据定位
该方向包含 10 篇论文，建议结合单篇创新点进一步细分子问题。

### 代表论文

- [A Human-in-the-Loop Framework for Efficient Prompt Selection in Microscopy Vision-Language Models](https://arxiv.org/abs/2605.20495v1)：提出一种人类在环的主动学习框架，通过目标驱动的提示集构建策略，以最少专家标注图像达到显微镜图像分类的目标性能。
- [Claim-Selective Certification for High-Risk Medical Retrieval-Augmented Generation](https://arxiv.org/abs/2605.21949v1)：提出声明选择性认证方法，将RAG回答分解为可验证声明，通过关系评分和意图感知选择器映射到四种动作（完整/部分/冲突/放弃），在弱标签协议下实现零UCCR和高PAU。
- [Case-Aware Medical Image Classification with Multimodal Knowledge Graphs and Reliability-Guided Refinement](https://arxiv.org/abs/2605.22547v2)：提出一种基于多模态知识图谱的案例感知推理框架，通过检索相似历史案例并注入视觉特征，同时用可靠性引导的决策细化机制校准预测，实现可解释的医学图像分类。
- [Evi-Steer: Learning to Steer Biomedical Vision-Language Models through Efficient and Generalizable Evidential Tuning](https://arxiv.org/abs/2605.26292v1)：提出Evi-Steer，一个基于证据学习的跨模态低维引导框架，通过仅更新0.11%参数实现不确定性感知的BiomedCLIP参数高效微调，在15个生物医学数据集上超越现有方法。
- [MedVol-R1: Reward-Driven Evidence Grounding for Volumetric Reasoning Segmentation](https://arxiv.org/abs/2605.26621v1)：本文针对三维医学图像中基于自由形式临床查询的体素推理分割任务，提出MedVol-R1框架。该方法通过强化学习将语言模型的临床推理解耦为可验证的二维证据锚点（关键轴向切片和边界框），再由冻结的MedSAM2模块传播为一致的三维掩码。采用冷启动监督微调结合GRPO训练，多组件奖励引导证据选择、空间定位和跨切片一致性。在三个公共数据集上取得最优性能，显著优于基线方法。
- [OphIn-500K: Curating Web-Scale Visual Instructions for Scaling Ophthalmic Multimodal Large Language Models](https://arxiv.org/abs/2605.27916v1)：提出OphIn-Engine自动数据流水线，从网络视频构建眼科指令数据集OphIn-500K（50万+实例），并训练眼科MLLM OphIn-VL，性能优于现有通用医疗和专科模型。
- [Concept-Guided Noisy Negative Suppression for Zero-Shot Classification and Grounding of Chest X-Ray Findings](https://arxiv.org/abs/2605.19374v1)：提出概念引导的噪声负抑制框架CoNNS，通过层次概念本体、跨患者对重标策略和概念感知NCE损失，解决胸片零样本分类和定位中对比学习噪声负样本导致的语义模糊问题。
- [Gaze into the Details: Locality-Sensitive Enhancement for OCTA Retinal Vessel Segmentation](https://arxiv.org/abs/2605.20651v1)：提出LSENet，通过在U-Net中引入Patch Information Enhance (PIE)、Multiscale Feature Fusion (MFF)和Connectivity Refinement Decoder (CRD)三个模块，解决OCTA视网膜血管分割中低局部对比度导致的血管不连续和细节丢失问题。
- [Pixel Wised Lesion Prediction on COVID-19 CT Imagery: A Comparative Analysis of Automated Image Segmentation Architectures](https://arxiv.org/abs/2605.20459v1)：综合评估4种分割架构（Unet、PSPNet、Linknet、FPN）与6种预训练编码器（VGG19、DenseNet121、Inception ResNet V2、MobileNet V2、SeresNet 101、EfficientNet B0）在COVID-19 CT图像二分类和多分类病变分割上的性能，并建立标准化比较基准。
- [What Does the Caption Really Say? Counterfactual Phrase Intervention for Compositional Data Selection in Vision-Language Pretraining](https://arxiv.org/abs/2605.22651v1)：提出反事实短语干预（CPI）框架，通过受控替换生成短语敏感性分数，用于视觉-语言对比预训练中的数据筛选，仅用50%数据即可提升组合泛化指标。

### 共同创新点
- 提出一种人类在环的主动学习框架，通过目标驱动的提示集构建策略，以最少专家标注图像达到显微镜图像分类的目标性能。
- 提出声明选择性认证方法，将RAG回答分解为可验证声明，通过关系评分和意图感知选择器映射到四种动作（完整/部分/冲突/放弃），在弱标签协议下实现零UCCR和高PAU。
- 提出一种基于多模态知识图谱的案例感知推理框架，通过检索相似历史案例并注入视觉特征，同时用可靠性引导的决策细化机制校准预测，实现可解释的医学图像分类。
- 提出Evi-Steer，一个基于证据学习的跨模态低维引导框架，通过仅更新0.11%参数实现不确定性感知的BiomedCLIP参数高效微调，在15个生物医学数据集上超越现有方法。

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
该方向包含 2 篇论文，建议结合单篇创新点进一步细分子问题。

### 代表论文

- [Benchmarking Convolutional, Transformer, Hybrid, and Vision Language Models for Multi Disease Retinal Screening](https://arxiv.org/abs/2605.26283v1)：系统比较了四类视觉模型（CNN、混合CNN-Transformer、Transformer、视觉语言模型）在多疾病视网膜筛查中的性能，通过标准化训练、校准和评估协议，为模型选择提供可重复的基准。
- [WBCAtt+: Fine-Grained Pixel-Level Morphological Annotations for White Blood Cell Images](https://arxiv.org/abs/2605.19692v1)：提出了WBCAtt+数据集，包含11种形态属性和5类像素级细胞组件的密集标注（113k图像级标签、10k分割图），并设计融入细胞组成结构的属性识别模型，提升了属性识别性能。

### 共同创新点
- 系统比较了四类视觉模型（CNN、混合CNN-Transformer、Transformer、视觉语言模型）在多疾病视网膜筛查中的性能，通过标准化训练、校准和评估协议，为模型选择提供可重复的基准。
- 提出了WBCAtt+数据集，包含11种形态属性和5类像素级细胞组件的密集标注（113k图像级标签、10k分割图），并设计融入细胞组成结构的属性识别模型，提升了属性识别性能。

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

## 方向 3：医学图像分割与低标注学习
该方向包含 4 篇论文，建议结合单篇创新点进一步细分子问题。

### 代表论文

- [SpineContextResUNet: A Computationally Efficient Residual UNet for Spine CT Segmentation](https://arxiv.org/abs/2605.20760v1)：提出 SpineContextResUNet，一种计算高效的 3D 残差 U-Net，通过轻量级上下文块（并行多膨胀卷积）捕获长程依赖，在脊柱 CT 分割中实现高精度与低资源需求。
- [Radiuma: A Unified Zero-Code Executable Graphical Workflow Generator for Reproducible and Shareable Medical Image Analysis and Machine Learning](https://arxiv.org/abs/2605.24201v1)：Radiuma是一个统一的零代码可执行图形化工作流生成器，将医学图像分析（读取、配准、融合、分割、特征提取）与机器学习（分类、回归、聚类）集成在一个模块化平台中，支持工作流的保存、共享和重放，以提高可重现性。
- [D-Convexity: A Unified Differentiable Convex Shape Prior via Quasi-Concavity for Data-driven Image Segmentation](https://arxiv.org/abs/2605.19210v1)：提出一种基于拟凹性的可微凸性先验，通过约束网络输出掩膜的所有超水平集为凸，将全局形状约束转化为局部可微不等式，并设计凸梯度投影模块（CGPM）实现端到端分割。
- [X-Ray cardiac angiographic vessel segmentation based on pixel classification using machine learning and region growing](https://arxiv.org/abs/2605.20073v1)：提出一种结合像素分类与ELEMENT区域生长控制策略的X射线心脏造影血管分割方法，采用随机森林分类器和多种纹理特征，在公开数据集上达到95.48%的准确率，优于现有无监督方法。

### 共同创新点
- 提出 SpineContextResUNet，一种计算高效的 3D 残差 U-Net，通过轻量级上下文块（并行多膨胀卷积）捕获长程依赖，在脊柱 CT 分割中实现高精度与低资源需求。
- Radiuma是一个统一的零代码可执行图形化工作流生成器，将医学图像分析（读取、配准、融合、分割、特征提取）与机器学习（分类、回归、聚类）集成在一个模块化平台中，支持工作流的保存、共享和重放，以提高可重现性。
- 提出一种基于拟凹性的可微凸性先验，通过约束网络输出掩膜的所有超水平集为凸，将全局形状约束转化为局部可微不等式，并设计凸梯度投影模块（CGPM）实现端到端分割。
- 提出一种结合像素分类与ELEMENT区域生长控制策略的X射线心脏造影血管分割方法，采用随机森林分类器和多种纹理特征，在公开数据集上达到95.48%的准确率，优于现有无监督方法。

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

## 方向 4：医学基础模型鲁棒性与评测基准
该方向包含 2 篇论文，建议结合单篇创新点进一步细分子问题。

### 代表论文

- [VISTA: Validation-Guided Integration of Spatial and Temporal Foundation Models with Anatomical Decoding for Rare-Pathology VCE Event Detection -- after competition results](https://arxiv.org/abs/2605.22096v1)：提出VISTA框架，融合EndoFM-LV时态模型与DINOv3帧级视觉模型，通过多样头集成、验证引导加权融合和解剖感知时序解码，提升胶囊内镜罕见病理事件检测精度，并在竞赛后通过全局阈值搜索优化获得第二名。
- [Rotation-Aligned Key Channel Pruning for Efficient Vision-Language Model Inference](https://arxiv.org/abs/2605.19218v1)：视觉语言模型推理时KV缓存压力大，现有方法通过token剪枝导致细粒度任务性能下降。本文提出旋转对齐关键通道剪枝（RotateK），通过在线PCA旋转将token相关通道重要性对齐到低维子空间，实现结构化剪枝，同时使用融合Triton注意力核加速解码。实验表明RotateK在准确率和延迟上均优于先前方法，联合token-通道剪枝进一步提升了KV缓存效率。

### 共同创新点
- 提出VISTA框架，融合EndoFM-LV时态模型与DINOv3帧级视觉模型，通过多样头集成、验证引导加权融合和解剖感知时序解码，提升胶囊内镜罕见病理事件检测精度，并在竞赛后通过全局阈值搜索优化获得第二名。
- 视觉语言模型推理时KV缓存压力大，现有方法通过token剪枝导致细粒度任务性能下降。本文提出旋转对齐关键通道剪枝（RotateK），通过在线PCA旋转将token相关通道重要性对齐到低维子空间，实现结构化剪枝，同时使用融合Triton注意力核加速解码。实验表明RotateK在准确率和延迟上均优于先前方法，联合token-通道剪枝进一步提升了KV缓存效率。

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
