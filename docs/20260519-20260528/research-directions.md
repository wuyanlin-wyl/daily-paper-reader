# 研究方向与二次创新路线 · 2026-05-19 ~ 2026-05-28

- 生成时间：2026-05-28 11:45:55 UTC
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

- [A Human-in-the-Loop Framework for Efficient Prompt Selection in Microscopy Vision-Language Models](https://arxiv.org/abs/2605.20495v1)：提出一种人机协同框架，通过目标驱动的主动学习策略选择优先标注的显微镜图像，以最少专家验证的示例构建提示集，达到分类性能目标。
- [Claim-Selective Certification for High-Risk Medical Retrieval-Augmented Generation](https://arxiv.org/abs/2605.21949v1)：提出声明选择性认证方法，将RAG回答分解为可验证声明，通过关系评分和意图感知选择器映射到四种动作（full/partial/conflict/abstain），实现高风险医疗场景下混合证据的细粒度决策。
- [Case-Aware Medical Image Classification with Multimodal Knowledge Graphs and Reliability-Guided Refinement](https://arxiv.org/abs/2605.22547v2)：提出一种基于多模态知识图谱和可靠性引导细化的案例感知推理框架MKG-CARE，用于医学图像分类，显式利用相似历史案例和结构化知识。
- [Evi-Steer: Learning to Steer Biomedical Vision-Language Models through Efficient and Generalizable Evidential Tuning](https://arxiv.org/abs/2605.26292v1)：提出Evi-Steer，一种基于证据推理的低维表征引导框架，通过仅更新0.11%参数实现生物医学视觉语言模型的不确定性感知高效微调，在少样本学习和域泛化设置下显著优于现有方法。
- [MedVol-R1: Reward-Driven Evidence Grounding for Volumetric Reasoning Segmentation](https://arxiv.org/abs/2605.26621v1)：提出MedVol-R1，一个基于GRPO强化学习的框架，将体素推理分割解耦为可验证的2D证据锚点（关键切片+边界框）和由冻结MedSAM2传播的3D掩码，无需链式思维标注。
- [OphIn-500K: Curating Web-Scale Visual Instructions for Scaling Ophthalmic Multimodal Large Language Models](https://arxiv.org/abs/2605.27916v1)：提出OphIn-Engine管线从网络眼科视频自动构建大规模指令数据OphIn-500K（50万+实例、15万+独特图像），并训练眼科专用多模态大语言模型OphIn-VL，在多项任务上超越通用医疗和专科模型。
- [Concept-Guided Noisy Negative Suppression for Zero-Shot Classification and Grounding of Chest X-Ray Findings](https://arxiv.org/abs/2605.19374v1)：提出概念引导的噪声负抑制框架CoNNS，利用层次概念本体和跨病人对重标策略，结合概念感知NCE损失，解决胸片零样本分类和定位中对比学习的噪声负样本问题。
- [Gaze into the Details: Locality-Sensitive Enhancement for OCTA Retinal Vessel Segmentation](https://arxiv.org/abs/2605.20651v1)：提出LSENet，通过补丁级局部信息增强（PIE）、多尺度特征融合（MFF）和连通性细化解码器（CRD）三个模块，有效解决OCTA视网膜血管分割中的低对比度导致的血管不连续和细节丢失问题，在三个公开数据集上以更少参数取得最优性能。
- [Pixel Wised Lesion Prediction on COVID-19 CT Imagery: A Comparative Analysis of Automated Image Segmentation Architectures](https://arxiv.org/abs/2605.20459v1)：本文通过综合评估四种深度学习分割架构（UNet、PSPNet、Linknet、FPN）与六种预训练编码器（VGG19、DenseNet121、Inception ResNet V2、MobileNet V2、SeresNet 101、EfficientNet B0）在三个COVID-19 CT数据集上的二分类和多分类分割性能，提供了标准化比较基准。
- [What Does the Caption Really Say? Counterfactual Phrase Intervention for Compositional Data Selection in Vision-Language Pretraining](https://arxiv.org/abs/2605.22651v1)：提出反事实短语干预（CPI）框架，通过受控非词替换生成短语敏感性分数，用于CLIP式对比预训练中组合性数据的筛选，仅用50%数据提升组合泛化指标。

### 共同创新点
- 提出一种人机协同框架，通过目标驱动的主动学习策略选择优先标注的显微镜图像，以最少专家验证的示例构建提示集，达到分类性能目标。
- 提出声明选择性认证方法，将RAG回答分解为可验证声明，通过关系评分和意图感知选择器映射到四种动作（full/partial/conflict/abstain），实现高风险医疗场景下混合证据的细粒度决策。
- 提出一种基于多模态知识图谱和可靠性引导细化的案例感知推理框架MKG-CARE，用于医学图像分类，显式利用相似历史案例和结构化知识。
- 提出Evi-Steer，一种基于证据推理的低维表征引导框架，通过仅更新0.11%参数实现生物医学视觉语言模型的不确定性感知高效微调，在少样本学习和域泛化设置下显著优于现有方法。

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

- [Benchmarking Convolutional, Transformer, Hybrid, and Vision Language Models for Multi Disease Retinal Screening](https://arxiv.org/abs/2605.26283v1)：本研究系统比较了卷积神经网络、视觉Transformer、混合CNN-Transformer及视觉语言模型在视网膜多疾病筛查中的性能。使用RFMiD数据集进行二分类和28类多标签分类，标准化训练与评估。结果表明注意力模型（如SwinTiny、混合CoAtNet0/MaxViTTiny）在二分类和多标签任务中表现最优，AUC超84%；视觉语言模型与CNN基线相当但未超越最优模型。外部验证Messidor-2上混合和Transformer...
- [WBCAtt+: Fine-Grained Pixel-Level Morphological Annotations for White Blood Cell Images](https://arxiv.org/abs/2605.19692v1)：提出WBCAtt+数据集，首次为白细胞图像提供11种细粒度形态属性和5类像素级分割标注，并构建利用分割信息提升属性识别性能的基线模型。

### 共同创新点
- 本研究系统比较了卷积神经网络、视觉Transformer、混合CNN-Transformer及视觉语言模型在视网膜多疾病筛查中的性能。使用RFMiD数据集进行二分类和28类多标签分类，标准化训练与评估。结果表明注意力模型（如SwinTiny、混合CoAtNet0/MaxViTTiny）在二分类和多标签任务中表现最优，AUC超84%；视觉语言模型与CNN基线...
- 提出WBCAtt+数据集，首次为白细胞图像提供11种细粒度形态属性和5类像素级分割标注，并构建利用分割信息提升属性识别性能的基线模型。

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

- [SpineContextResUNet: A Computationally Efficient Residual UNet for Spine CT Segmentation](https://arxiv.org/abs/2605.20760v1)：提出一种计算高效的3D残差U-Net (SpineContextResUNet)，通过轻量级上下文块（并行多膨胀卷积）捕获长程依赖，在资源受限硬件上实现脊柱CT分割，达到与大规模模型可比的精度。
- [Radiuma: A Unified Zero-Code Executable Graphical Workflow Generator for Reproducible and Shareable Medical Image Analysis and Machine Learning](https://arxiv.org/abs/2605.24201v1)：Radiuma是一个零代码图形工作流生成器，通过整合图像处理与机器学习模块并支持工作流保存共享，实现可重复和可共享的医学图像分析。
- [D-Convexity: A Unified Differentiable Convex Shape Prior via Quasi-Concavity for Data-driven Image Segmentation](https://arxiv.org/abs/2605.19210v1)：从拟凹性出发，提出无阈值的可微凸性先验，通过零阶、一阶、二阶条件将全局凸形状约束转化为局部可微不等式，并设计凸梯度投影模块(CGPM)集成到分割网络。
- [X-Ray cardiac angiographic vessel segmentation based on pixel classification using machine learning and region growing](https://arxiv.org/abs/2605.20073v1)：提出一种结合像素分类和区域增长的X射线心脏造影血管分割方法，通过提取多类纹理特征并使用随机森林分类器和ELEMENT迭代机制，达到95.48%准确率，优于现有无监督方法。

### 共同创新点
- 提出一种计算高效的3D残差U-Net (SpineContextResUNet)，通过轻量级上下文块（并行多膨胀卷积）捕获长程依赖，在资源受限硬件上实现脊柱CT分割，达到与大规模模型可比的精度。
- Radiuma是一个零代码图形工作流生成器，通过整合图像处理与机器学习模块并支持工作流保存共享，实现可重复和可共享的医学图像分析。
- 从拟凹性出发，提出无阈值的可微凸性先验，通过零阶、一阶、二阶条件将全局凸形状约束转化为局部可微不等式，并设计凸梯度投影模块(CGPM)集成到分割网络。
- 提出一种结合像素分类和区域增长的X射线心脏造影血管分割方法，通过提取多类纹理特征并使用随机森林分类器和ELEMENT迭代机制，达到95.48%准确率，优于现有无监督方法。

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

- [VISTA: Validation-Guided Integration of Spatial and Temporal Foundation Models with Anatomical Decoding for Rare-Pathology VCE Event Detection -- after competition results](https://arxiv.org/abs/2605.22096v1)：提出VISTA框架，融合EndoFM-LV时态模型与DINOv3帧级视觉模型，通过多样头集成、验证引导加权融合和解剖感知时序解码，解决胶囊内镜罕见病理事件检测中稀疏、异质和事件级评估的挑战。
- [Rotation-Aligned Key Channel Pruning for Efficient Vision-Language Model Inference](https://arxiv.org/abs/2605.19218v1)：提出旋转对齐关键通道剪枝框架RotateK，通过在线PCA旋转将token相关通道重要性对齐到共享低维子空间，实现结构化头维度剪枝，并使用融合Triton注意力核加速解码，在固定KV缓存预算下显著提升视觉语言模型推理效率。

### 共同创新点
- 提出VISTA框架，融合EndoFM-LV时态模型与DINOv3帧级视觉模型，通过多样头集成、验证引导加权融合和解剖感知时序解码，解决胶囊内镜罕见病理事件检测中稀疏、异质和事件级评估的挑战。
- 提出旋转对齐关键通道剪枝框架RotateK，通过在线PCA旋转将token相关通道重要性对齐到共享低维子空间，实现结构化头维度剪枝，并使用融合Triton注意力核加速解码，在固定KV缓存预算下显著提升视觉语言模型推理效率。

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
