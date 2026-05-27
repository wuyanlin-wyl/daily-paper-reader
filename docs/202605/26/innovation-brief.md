# 创新点总结 · 2026-05-26

- 生成时间：2026-05-27 06:18:50 UTC
- 当日论文数：36

## 今日趋势
- 医学视觉语言模型的可靠性、可解释性和鲁棒性评估与提升
- 参数高效微调（PEFT）与低资源场景下的医学AI应用
- 多智能体系统与分治策略在医学图像分析中的应用
- 联邦学习中的隐私保护与数据协调
- 基于稀疏自编码器或提示调优的模型编辑与幻觉缓解

## 最值得先读

| 论文 | 推荐理由 |
|---|---|
| [Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence](https://arxiv.org/abs/2605.22414v1) | 首次提出临床可解释的眼底VQA基准，强调空间定位证据，为可靠医学VQA提供了新范式。 |
| [Med-R2: An Adversarial Benchmark for Evidence-Grounded Reasoning in Medical VLMs](https://arxiv.org/abs/2605.24492v1) | 系统评估医学VLM对抗性鲁棒性的层级化基准，揭示了推理缺陷并提供了训练改进方向。 |

## 单篇创新点

### 1. Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.22414v1-towards-clinically-interpretable-ophthalmic-vqa-via-spatially-grounded-lesion-evidence
- 一句话贡献：提出了首个带有基于ETDRS网格空间定位病变证据的临床可解释眼科VQA基准FundusGround，验证了病变级视觉证据对模型准确性和可解释性的提升。
- 核心创新点：
  - 提出了三阶段数据收集管线，包括图像收集、基于ETDRS网格的病变空间定位和标准化标注
  - 构建了包含10719张眼底图像、15595个图像级病变标注和72706个多格式问题的数据集
  - 引入了双指标评估框架，同时衡量答案准确性和病变级推理能力
  - 首次在眼科VQA中要求模型提供空间定位的病变证据，实现临床可解释性
  - 将ETDRS网格这一临床标准引入VQA任务，确保病变标注的解剖一致性和临床有效性
- 和已有工作的区别：现有眼科VQA基准仅关注答案准确率，缺乏对模型推理过程的可解释性评估；本工作通过空间定位的病变证据和双指标评估，推动了临床可解释的VQA。
- 阅读启发：对于需要高可靠性的临床AI，应强制模型输出空间可解释的证据，而不仅仅依赖答案正确性。
- 可信度：high

### 2. PrivFusion: A Privacy-preserving Multi-Agent Framework for Harmonizing Distributed Datasets
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24249v1-privfusion-a-privacy-preserving-multi-agent-framework-for-harmonizing-distributed-datasets
- 一句话贡献：提出一种隐私保护的多智能体框架PrivFusion，通过本地数据分析和跨站点语义特征聚类自动实现分布式结构化数据集协调，减少联邦学习中数据异构性导致的人工干预。
- 核心创新点：
  - 多智能体协作机制：每个站点部署本地智能体分析数据，跨站点聚类语义相似特征
  - 迭代变换建议算法：智能体提供变换建议直至所有站点特征对齐
  - 隐私保护：所有操作基于本地统计信息，不共享原始数据
  - 聚焦联邦学习中数据集异构性导致的数据协调这一被忽视的先决条件
  - 自动化结构化数据的协调，替代昂贵耗时的手动harmonization过程
- 和已有工作的区别：现有联邦学习工作通常假设数据已协调好，而PrivFusion专注于协调阶段；不同于传统手动或中心化的协调方法，PrivFusion以隐私保护方式自动完成多站点协调。
- 阅读启发：PrivFusion为联邦学习提供了一种自动、隐私保护的分布式协调方法，解决了实际部署中因数据异构性导致联邦学习性能下降的关键问题。
- 可信度：medium

### 3. Parameter-Efficient VLMs for Gastrointestinal Endoscopy: Medical Image Generation and Clinical Visual Question Answering
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24792v1-parameter-efficient-vlms-for-gastrointestinal-endoscopy-medical-image-generation-and-clinical-visual-question-answering
- 一句话贡献：提出双流水线参数高效微调（PEFT）模型，同时提升胃肠内镜视觉问答（VQA）的性能和隐私保护的合成图像生成质量。
- 核心创新点：
  - 采用Florence-2模型结合PEFT进行临床VQA，增强可解释性并大幅降低训练计算成本
  - 利用LoRA微调Stable Diffusion 2.1生成高保真度胃肠内镜图像，避免隐私泄露
  - 双流水线统一处理VQA和合成图像生成，避免分别设计模型
  - 聚焦胃肠内镜AI中标注数据稀缺、隐私限制和传统微调计算瓶颈的联合解决方案
  - 同时解决临床VQA和隐私保护合成数据生成两个核心问题
- 和已有工作的区别：现有工作分别处理VQA或图像生成，且未采用PEFT策略；本工作首次将PEFT同时应用于VQA和生成，在低计算开销下取得更优的图像-文本一致性（FBD更低）。
- 阅读启发：参数高效微调结合双流水线设计能有效应对医学数据稀缺和隐私限制，为内镜AI提供实用且可扩展的解决方案。
- 可信度：high

### 4. Universal Boosts, Specific Suppressors: Sparse Autoencoder Steering of Medical Vision-Language Models
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24977v1-universal-boosts-specific-suppressors-sparse-autoencoder-steering-of-medical-vision-language-models
- 一句话贡献：提出基于稀疏自编码器的解码时残差引导方法，通过逐token因果干预（提升正确特征、抑制错误特征）减少医学视觉语言模型在胸部X光报告生成中的幻觉，无需权重更新。
- 核心创新点：
  - 在医学VLM的深层逐层使用Top-K稀疏自编码器提取可解释特征
  - 基于因果干预的解码时残差引导，分别对有益特征（boost）和有害特征（suppress）进行定向调整
  - 发现提升方向跨模型架构通用，而抑制方向为模型特有，因此需按模型定制抑制
  - 针对医学视觉语言模型生成放射报告时的幻觉问题（虚构、遗漏、定位错误）
  - 在推理阶段进行干预，避免再次训练或权重更新
- 和已有工作的区别：不同于微调、提示工程或知识蒸馏等传统方法，本文在解码时通过SAE激活进行定向因果干预，不修改模型参数，且首次揭示提升与抑制方向的可迁移性差异。
- 阅读启发：本文提供了一种高效、可解释的推理时幻觉缓解方案，适用于多种医学VLM，并展示了跨模型共享有益特征的可能性，为后续可迁移的模型编辑提供了新思路。
- 可信度：high

### 5. Towards Reliable Fetal Ultrasound Interpretation with Multi-Agent Collaboration
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.25357v1-towards-reliable-fetal-ultrasound-interpretation-with-multi-agent-collaboration
- 一句话贡献：提出FetUSAgents多智能体系统，通过工具增强和双路径证据仲裁，实现高可靠的胎儿超声解读，在分布外实验中VQA准确率超越最强基线25%以上。
- 核心创新点：
  - 构建工具增强的多智能体系统，通过协作LLM代理协调任务特定视觉工具，分解临床查询为子任务。
  - 提出双路径证据仲裁（DPEA），融合LLM的推理性推理与结构化计算证据。
  - 引入检索增强证据库，整合中间发现以支持可追溯的临床结论。
  - 首次将多智能体协作范式应用于胎儿超声解读，解决“单任务-单模型”的集成不足问题。
  - 为胎超声领域构建专门VQA基准FetUS-VQA（1892图像，3205问答对，10临床任务），填补评估空白。
- 和已有工作的区别：现有方法多为单任务模型或直接应用MLLM，缺乏多步推理和领域特异性；本工作通过多智能体协作和双重证据仲裁，兼具结构化计算和语言推理，降低幻觉风险，提升可靠性和可解释性。
- 阅读启发：多智能体系统结合工具增强和证据仲裁，是提升医学图像分析可靠性的有效路径，尤其适用于多步骤临床任务。
- 可信度：high

### 6. EchoPilot: Training-Free Ultrasound Video Segmentation via Scale-Space Semantic Prompting and Reliability-Gated Memory
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.25944v1-echopilot-training-free-ultrasound-video-segmentation-via-scale-space-semantic-prompting-and-reliability-gated-memory
- 一句话贡献：提出一种无需训练的超声视频分割框架，仅需单点点击和类别名称，通过尺度空间语义提示和可靠性门控记忆解决初始化模糊和传播漂移问题。
- 核心创新点：
  - 提出尺度空间语义提示（Scale-Space Semantic Prompting），利用S.E.E.D.准则自动选择最优上下文视图并合成几何精确的辅助点提示
  - 引入可靠性门控记忆更新（Reliability-Gated Memory Update），根据预测不确定性选择性冻结记忆库以防止误差积累
  - 构建了首个动态胎儿胎盘超声视频分割数据集，包含671帧标注图像
  - 在训练-free的稀疏交互超声视频分割中，仅需单点点击和类别名称，无需密集标注或模型微调
  - 解决超声视频中尺度模糊和弱边界问题，首次将冻结的医学VLM和VFM组合用于超声分割
- 和已有工作的区别：与直接使用提示基础模型（如SAM）不同，本工作通过多模型协作和自适应提示策略解决了超声中单点信息不足和记忆漂移问题，无需用户额外交互或模型训练。
- 阅读启发：展示了如何巧妙组合冻结的视觉语言模型和基础模型实现高精度超声视频分割，为医疗影像的少交互分割提供了新范式。
- 可信度：high

### 7. RAPTOR+: A Visually Grounded Vision-Language Framework to Improve Clinical Trust and Auditability in Automated Cancer Referral Processing
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.25956v1-raptor-a-visually-grounded-vision-language-framework-to-improve-clinical-trust-and-auditability-in-automated-cancer-referral-processing
- 一句话贡献：提出RAPTOR+多模态框架，通过微调视觉语言模型替代原有OCR+LLM管道，实现端到端癌症转诊表单理解，并引入证据定位评估，大幅提升临床可审计性。
- 核心创新点：
  - 采用视觉语言模型（VLM）进行端到端转诊理解，无需独立OCR步骤
  - 引入grounding-aware评估框架，同时测量提取准确性和证据定位
  - 微调Qwen3-VL-8B在严格安全性上达到60.6%，显著优于零样本模型
  - 针对临床转诊处理中视觉证据丢失和手工审核瓶颈问题
  - 强调可审计性和临床信任，而不仅仅是提取精度
- 和已有工作的区别：原RAPTOR系统依赖分离的OCR和LLM，易受手写和布局变化影响且缺乏视觉证据连接；RAPTOR+通过单一VLM实现端到端处理并显式链接抽取结果到视觉证据。
- 阅读启发：对于临床文档理解，任务特定微调VLM比零样本模型更可靠，且应同时评估证据定位以确保可审计性。
- 可信度：high

### 8. MedFM-Robust: Benchmarking Robustness of Medical Foundation Models
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.19027v3-medfm-robust-benchmarking-robustness-of-medical-foundation-models
- 一句话贡献：构建了首个针对医疗基础模型在真实扰动下鲁棒性的综合基准，涵盖40种扰动、八种成像模态，评估VLM和分割模型，揭示微调策略和领域特定扰动的影响。
- 核心创新点：
  - 设计了包含28种医学特定扰动的扰动库，覆盖八种成像模态
  - 提出了针对VLM的VQA、视觉定位和描述三种任务的鲁棒性评估框架
  - 系统对比了五种微调策略（全微调、LoRA、Adapter等）对分割模型鲁棒性的影响
  - 首次系统评估医疗基础模型在真实世界扰动下的鲁棒性，而非仅理想条件下的性能
  - 覆盖了视觉-语言模型和分割模型的多任务、多模态鲁棒性基准
- 和已有工作的区别：以往工作缺乏对医疗基础模型在多样化真实扰动下的系统评估，本文提供了全面的基准测试和部署指南。
- 阅读启发：医疗AI部署需重视领域特定的鲁棒性评估，选择适当的微调策略以平衡效率与鲁棒性。
- 可信度：high

### 9. PromptRad: Knowledge-Enhanced Multi-Label Prompt-Tuning for Low-Resource Radiology Report Labeling
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.20052v1-promptrad-knowledge-enhanced-multi-label-prompt-tuning-for-low-resource-radiology-report-labeling
- 一句话贡献：提出知识增强的多标签提示调优方法，将放射学报告标注转化为掩码语言建模，利用UMLS同义词扩展词汇表，在低资源下仅需少量标注数据即可高效标注。
- 核心创新点：
  - 将多标签分类任务重定义为掩码语言建模（MLM），无需额外分类层
  - 基于UMLS Metathesaurus构建多词verbalizer，融入同义词丰富类别表示
  - 在低资源场景下仅需32个标注样本即可微调预训练语言模型
  - 针对放射学报告标注中标注数据稀缺的低资源问题
  - 解决传统规则方法对临床报告描述多样性适应不足的问题
- 和已有工作的区别：区别于规则方法和传统微调，采用提示调优范式并引入医学知识（UMLS同义词）增强类别表示，显著降低标注数据需求。
- 阅读启发：低资源临床文本标注可采用提示调优结合外部知识库，以极小标注成本获得高性能。
- 可信度：high

### 10. RoboSurg-VQA: A Multimodal Benchmark for Surgical Segmentation-Aware Visual Question Answering
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.23068v1-robosurg-vqa-a-multimodal-benchmark-for-surgical-segmentation-aware-visual-question-answering
- 一句话贡献：提出了首个结合分割感知的机器人手术视觉问答基准RoboSurg-VQA，通过重用公共分割数据集并采用自动生成+人工审计的标注方法，为手术场景下的VQA提供了标准评估平台。
- 核心创新点：
  - 提出分割感知的VQA框架，将分割掩码作为视觉问答的输入特征之一
  - 设计约束提示自动生成候选答案并配合一致性检查与人工审计的标注流程
  - 构建固定临床问题集与封闭答案集，覆盖手术上下文、解剖结构、伪影等维度
  - 首次将VQA任务引入机器人手术领域，并强调分割感知能力
  - 针对手术中常见的遮挡、烟雾、出血等退化视图设计问题集
- 和已有工作的区别：现有手术视觉问答工作要么缺乏分割信息感知，要么仅针对单一任务（如分割或分类）；本工作首次整合分割感知与VQA，并通过复用公共分割数据集降低构建成本，同时采用自动+人工标注提升效率与质量。
- 阅读启发：RoboSurg-VQA为手术场景下的多模态理解提供了新的基准和标注范式，特别强调了在临床相关退化条件下的视觉问答能力。
- 可信度：high

### 11. What Makes a Medical Checker Trainable? Diagnosing Signal Collapse and Reward Hacking in Checker-Guided RAG for Biomedical QA
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.25988v1-what-makes-a-medical-checker-trainable-diagnosing-signal-collapse-and-reward-hacking-in-checker-guided-rag-for-biomedical-qa
- 一句话贡献：发现医学RAG中NLI检查器的输出分布而非准确率决定其作为强化学习奖励的可训练性，并诊断出信号坍缩和奖励破解两种关键失败模式。
- 核心创新点：
  - 系统比较四种NLI后端（LLM对数概率、MedNLI分类器等）作为GRPO训练的奖励信号
  - 揭示LLM对数概率评分导致超97%的claims被标记为中性，引发梯度消失（信号坍缩）
  - 发现强信号（如专有检查器）会触发奖励破解三级联：超短答案、搜索回避、语言坍缩
  - 提出信号强度是策略相关的概念：同一检查器在不同策略下可能表现为适度或强信号
  - 将验证器作为奖励的问题从“如何选最佳验证器”转向“验证器输出分布如何影响可训练性”
- 和已有工作的区别：已有工作聚焦验证器的准确率或损失，本文首次证明训练时的输出分布（尤其是中性标签比例）比准确率更关键，并量化了信号强度与奖励破解的因果关系。
- 阅读启发：设计基于验证器的奖励系统时，应关注输出分布的均匀性而非绝对准确率，避免强信号引发的奖励破解，适度信号（如校准的MedNLI）更有利于训练。
- 可信度：high

### 12. BalanceRAG: Joint Risk Calibration for Cascaded Retrieval-Augmented Generation
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.20084v1-balancerag-joint-risk-calibration-for-cascaded-retrieval-augmented-generation
- 一句话贡献：提出BalanceRAG，通过二维网格序列图检验联合校准LLM-only和RAG的不确定度阈值，在控制系统级错误率的同时提高覆盖率并减少不必要检索。
- 核心创新点：
  - 将两个分支的阈值对视为二维网格上的操作点，采用序列图检验联合校准
  - 实现风险自适应阈值校准，同时控制系统级错误率和覆盖率
  - 扩展至多风险校准，同时约束检索使用率和选择条件风险
  - 针对级联RAG中逐阶段校准保守的问题，提出联合风险校准范式
  - 首次将级联RAG的阈值校准问题形式化为二维网格上的图形检验问题
- 和已有工作的区别：现有级联RAG逐阶段校准阈值，可能过于保守；BalanceRAG联合校准两个分支阈值，在保证风险控制下保留更多样本并降低检索开销。
- 阅读启发：BalanceRAG提供了一种系统级风险可控的级联RAG校准方法，平衡了准确率、覆盖率和检索效率。
- 可信度：high

### 13. VRXU-net: A Deep Learning Approach for Brain Ischemic Stroke Lesion Detection and Segmentation in T1W MRI
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.21633v1-vrxu-net-a-deep-learning-approach-for-brain-ischemic-stroke-lesion-detection-and-segmentation-in-t1w-mri
- 一句话贡献：提出VRXU-net模型，通过三平面2D切片分解与级联分类-分割框架，在T1W MRI中实现脑缺血性卒中病灶的高效检测与精准分割。
- 核心创新点：
  - 将3D MRI分解为轴向、矢状、冠状三个平面的2D切片，分别分割后融合结果，利用多平面信息提高定位精度
  - 引入基于改进VGG的高性能预分类器，先识别病变切片，再仅对病变切片进行分割，减少非病变切片处理，提升速度和准确率
  - 在U-Net分割网络中嵌入残差块，增强梯度流动和特征学习能力
  - 分割结果反馈给分类器以降低假阳性，形成交叉优化机制
  - 针对T1W MRI中缺血性卒中病灶与周围组织对比度低、形状大小多变的问题，提出多平面2D分解策略，降低3D建模复杂度同时保留立体信息
- 和已有工作的区别：现有U-Net类方法通常直接在3D或单平面2D上进行分割，而VRXU-net结合了多平面分解、级联分类与分割、残差块及反馈机制，在T1W模态上取得了更好性能。
- 阅读启发：这是一种结合分类与分割、利用多平面2D分解的轻量级脑卒中病灶检测分割方法，适用于对比度低的T1W MRI。
- 可信度：high

### 14. ImPartial: Multi-channel Whole-Cell Segmentation using Partial Annotations
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24128v1-impartial-multi-channel-whole-cell-segmentation-using-partial-annotations
- 一句话贡献：提出ImPartial框架，通过自监督多通道量化插值在稀疏涂鸦标注下实现与全监督相当的全细胞分割性能
- 核心创新点：
  - 自监督多通道量化插值机制，无需完美像素重建，直接优化分割目标
  - 利用稀疏涂鸦作为部分标注，结合多通道信息进行弱监督学习
  - 在多重免疫荧光和明场免疫组化等不同模态上统一处理
  - 针对多通道可变配置的病理图像，利用部分标注（稀疏涂鸦）替代密集像素标注
  - 降低细胞分割对专家标注的依赖，适用于标注稀缺的新兴成像模态
- 和已有工作的区别：现有弱监督方法依赖像素级重建或生成式预训练，而ImPartial引入与分割任务对齐的自监督分类目标，避免冗余重建，更高效利用有限标注
- 阅读启发：ImPartial展示了自监督辅助任务设计的巧妙：不追求图像完美重建，而是设计针对分割的中间目标，从而在标注极少时仍能取得优异性能
- 可信度：high

### 15. Med-R2: An Adversarial Benchmark for Evidence-Grounded Reasoning in Medical VLMs
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24492v1-med-r2-an-adversarial-benchmark-for-evidence-grounded-reasoning-in-medical-vlms
- 一句话贡献：提出首个层级化对抗性基准Med-R2 Bench，系统评估医学视觉语言模型在四个临床阶段中基于视觉证据的推理鲁棒性，并揭示模型对提示的过度依赖和文本-视觉对齐缺陷。
- 核心创新点：
  - 构建了与临床工作流对齐的四阶段层级化评估框架（分诊、检查、诊断、随访），每个阶段设计逐步推理的QA任务以检验视觉证据的严格依赖。
  - 采用对抗性扰动（如遮挡、混淆区域、伪影）生成误导性视觉线索，系统测试模型在干扰下的鲁棒性。
  - 大规模数据集（42,432图像、31任务、110,406 QA对）覆盖多种医学影像类型和临床场景。
  - 设计层级微调方法，利用分阶段数据逐步训练，显著提升模型在对抗性样本下的推理准确性。
  - 首次将对抗性鲁棒性评估与临床证据推理需求结合，关注模型是否依赖虚假先验而非真实视觉线索。
- 和已有工作的区别：现有医学VQA基准（如VQA-RAD、Slake）仅评估单一问答正确性，未考虑推理链的视觉证据基础；对抗性攻击研究（如Adv-Medi）主要针对分类任务而非多步推理。Med-R2首次联合层级推理评估与对抗扰动，更贴近临床实际需求。
- 阅读启发：本文提供了一个严谨的工具来检验VLM在医学推理中的“伪智能”现象，并指出了提升模型可靠性的可行路径——层级化对抗训练，对构建安全的医学AI有重要参考价值。
- 可信度：high

### 16. Thinking in Scales: Accelerating Gigapixel Pathology Image Analysis via Adaptive Continuous Reasoning
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.19491v2-thinking-in-scales-accelerating-gigapixel-pathology-image-analysis-via-adaptive-continuous-reasoning
- 一句话贡献：提出PathCTM模型，通过自适应连续推理从低倍到高倍动态分析病理全切片图像，大幅减少计算开销并保持诊断精度。
- 核心创新点：
  - 动态尺度切换：从低倍全局到高倍局部逐步细化，使用条件计算实现自适应缩放。
  - 注意力引导区域剪枝：在低倍阶段关注关键区域，剪除无关区域以减少高倍处理。
  - 置信度感知早期停止：当不确定性足够低时提前终止推理，避免冗余计算。
  - 将全切片图像诊断重新定义为动态顺序信息追求问题，而非传统多实例学习中的静态聚合。
  - 在保持AUC不下降的前提下，减少所需图像块数量约95.95%，缩短推理时间约95.62%。
- 和已有工作的区别：现有MIL方法对所有高倍图像块进行穷举处理，计算昂贵；PathCTM通过自适应推理仅处理必要区域，效率提升近两个数量级。
- 阅读启发：通过动态尺度选择和早期停止机制，可显著加速大规模病理图像分析，为临床部署提供可能。
- 可信度：high

### 17. Cardiac fat segmentation using computed tomography and an image-to-image conditional generative adversarial neural network
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.20064v1-cardiac-fat-segmentation-using-computed-tomography-and-an-image-to-image-conditional-generative-adversarial-neural-network
- 一句话贡献：首次将条件生成对抗网络pix2pix应用于心脏CT图像中两种脂肪（心外膜和纵隔）的自动分割，实现高精度实时分割。
- 核心创新点：
  - 采用pix2pix条件GAN架构（原本用于图像翻译）直接进行分割任务
  - 实现单网络同时分割两种脂肪类型
  - 端到端训练，无需手工特征提取
  - 聚焦心脏脂肪分割这一临床需求，减轻人工标注负担
  - 区分心外膜和纵隔两种解剖位置不同的脂肪
- 和已有工作的区别：现有方法多使用传统机器学习或CNN分割，本文首次引入条件GAN（pix2pix）进行心脏脂肪分割，在精度和速度上均有提升。
- 阅读启发：条件GAN不仅可用于图像翻译，也可有效应用于医学图像分割任务，尤其在需要高精度和实时处理的场景。
- 可信度：high

### 18. Divide-and-Conquer Inference for Large-Scale Visual Recognition with Multimodal Large Language Models
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24799v1-divide-and-conquer-inference-for-large-scale-visual-recognition-with-multimodal-large-language-models
- 一句话贡献：提出一种即插即用的测试时分治推理策略（DCI），通过递归分解大规模分类任务并动态剪枝，有效缓解多模态大语言模型在长序列识别中的性能崩溃问题，显著提升精度和推理速度。
- 核心创新点：
  - 揭示了长序列识别中性能崩溃的根本原因：信息熵升高与注意力稀释/衰减的矛盾导致信噪比不足
  - 提出了分而治之的递归推理框架，将全局分类任务分解为多个局部子问题
  - 设计了动态剪枝机制，自适应压缩搜索空间以提升局部信噪比
  - 实现了更优的缩放行为，在推理时避免了二次复杂度，加速大规模分类
  - 首次从信息论角度分析和定义多模态大语言模型在长序列识别中的性能崩溃现象
- 和已有工作的区别：不同于以往通过模型微调或结构修改来提升长序列性能，DCI是一种纯推理阶段的即插即用策略，不改变模型参数，且通过分解和剪枝直接解决注意力稀释问题，避免了二次复杂度。
- 阅读启发：对于多模态大语言模型的大规模分类任务，分治推理是一种有效且高效的扩展方法，无需训练即可显著提升性能，为实际应用提供了低成本优化方案。
- 可信度：high

### 19. Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.22414v1
- 一句话贡献：提出FundusGround基准，通过ETDRS网格空间定位病变证据，实现临床可解释的眼底VQA。
- 核心创新点：
  - 构建包含10719张眼底图像和15595个精细病变标注的数据集
  - 采用ETDRS网格将病变映射到9个临床视网膜区域，确保解剖一致性
  - 生成72706个问题，涵盖开放、封闭、单选和多选四种格式
  - 双指标评估答案准确性和病变级推理能力
  - 聚焦临床可解释性，要求VQA提供空间定位的病变证据而非仅答案准确
- 和已有工作的区别：现有眼底VQA基准只注重答案准确率，忽略可解释性；本工作首次引入空间定位的病变证据作为推理基础。
- 阅读启发：空间 grounding 是构建可靠可解释医学VQA的关键，为临床决策支持提供新范式。
- 可信度：high

### 20. PrivFusion: A Privacy-preserving Multi-Agent Framework for Harmonizing Distributed Datasets
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.24249v1
- 一句话贡献：提出一个隐私保护的多智能体框架PrivFusion，在联邦学习前自动协调异构结构化数据集，减少人工干预。
- 核心创新点：
  - 使用多智能体分布式分析本地数据
  - 通过聚类语义相似特征实现跨站点对齐
  - 提供迭代转换建议直至数据集协调
  - 强调数据协调是联邦学习多站点分析的必要前提而常被忽视
  - 在联邦学习之前而非期间进行协调
- 和已有工作的区别：现有联邦学习假设数据已协调，或数据协调缺乏隐私保护；PrivFusion首次在保护隐私的前提下自动化多站点结构化数据协调。
- 阅读启发：PrivFusion提供了一种实用的、可扩展的隐私保护数据协调方法，可作为联邦学习的预处理步骤，降低多中心研究中的数据整合障碍。
- 可信度：high

### 21. Parameter-Efficient VLMs for Gastrointestinal Endoscopy: Medical Image Generation and Clinical Visual Question Answering
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.24792v1
- 一句话贡献：提出一个双管道PEFT框架，同时解决内镜VQA（Florence-2+PEFT）和隐私保护图像生成（Stable Diffusion+LoRA），显著降低计算成本并提升性能。
- 核心创新点：
  - 采用Florence-2视觉语言模型结合PEFT进行内镜VQA，提升可解释性并大幅降低训练计算成本
  - 利用LoRA与Stable Diffusion 2.1生成高质量胃肠道内镜图像，实现隐私保护的数据增强
  - 双管道架构同时处理VQA和合成数据生成两个任务，共享PEFT优势
  - 针对胃肠道内镜标注数据稀缺和隐私限制，提出无需真实数据即可增强训练集的合成方法
  - 将VQA与隐私保护图像生成结合到统一框架，克服传统微调的计算瓶颈
- 和已有工作的区别：以往工作分别处理VQA或合成数据，且全量微调计算开销大；本工作首次用PEFT双管道同时优化两个任务，并在内镜领域实现高效率和良好性能。
- 阅读启发：PEFT（尤其LoRA）能有效降低医学图像生成和VQA的计算成本，同时保护隐私，为资源受限的临床AI部署提供可行方案。
- 可信度：high

### 22. Universal Boosts, Specific Suppressors: Sparse Autoencoder Steering of Medical Vision-Language Models
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.24977v1
- 一句话贡献：提出一种无需权重更新的解码时残差操纵方法，利用稀疏自编码器在推理时通过增强和抑制特定特征来减少医学视觉语言模型的幻觉，并发现增强方向跨模型通用而抑制方向模型特异。
- 核心创新点：
  - 使用Top-K稀疏自编码器在模型晚期层进行逐token残差操纵
  - 基于临床错误进行因果性增强/抑制干预
  - 跨模型特征对齐分析揭示增强方向通用而抑制方向模型特异
  - 首次将稀疏自编码器用于医疗视觉语言模型的推理时幻觉缓解
  - 提出无需重新训练、仅通过解码时特征操纵的零样本迁移方法
- 和已有工作的区别：区别于之前需要微调或额外训练的幻觉缓解方法，本方法仅通过推理时基于稀疏自编码器的特征操纵即可实现模型无关的增强和模型特定的抑制，并且零样本迁移到新数据集。
- 阅读启发：稀疏自编码器可以提取可解释的因果特征，其中促进报告质量的特征具有跨模型通用性，而与幻觉相关的特征则是模型特有的，因此抑制幻觉需要针对不同骨干网络定制。
- 可信度：high

### 23. Towards Reliable Fetal Ultrasound Interpretation with Multi-Agent Collaboration
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.25357v1
- 一句话贡献：Automated fetal ultrasound interpretation requires a workflow from visual perception, including plane recognition and anatomical segmentation, to clinical understanding, including biometric measurement and diagnostic reporting. However, th...
- 核心创新点：
  - 需结合全文进一步确认具体技术创新；当前基础信息不足。
  - 从题目与摘要看，该工作可能面向一个更具体或更实用的任务设定。
  - 建议阅读论文实验部分确认主要结果、对比基线与消融证据。
- 和已有工作的区别：当前可用信息不足，暂不强行判断与已有工作的明确差异。
- 阅读启发：可先浏览摘要、方法图和实验表格，判断它是否与自己的研究问题相关。
- 可信度：low

### 24. EchoPilot: Training-Free Ultrasound Video Segmentation via Scale-Space Semantic Prompting and Reliability-Gated Memory
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.25944v1
- 一句话贡献：提出了一种无需训练的超声视频分割框架EchoPilot，通过尺度空间语义提示和可靠性门控记忆机制，在仅需单点点击和类别名称的稀疏交互下实现稳定分割。
- 核心创新点：
  - 提出Scale-Space Semantic Prompting，通过S.E.E.D.（语义能量-熵密度）准则自动选择最优上下文视图，并从密集基础特征中合成几何精确的辅助点提示，无需额外用户交互。
  - 提出Reliability-Gated Memory更新机制，在预测不确定时选择性冻结分割器的记忆库，防止早期误差累积导致的时序漂移。
  - 构建首个动态胎儿胎盘超声视频分割数据集，包含671个标注帧，为超声视频分割提供新基准。
  - 首次在超声视频分割中采用训练-free范式和稀疏第一帧交互（单点点击+类别名称），无需模型微调或密集标注。
  - 在三个超声视频数据集上取得最先进性能，一致优于现有训练-free基线和微调专家模型。
- 和已有工作的区别：现有工作或需要大量标注数据微调，或依赖密集用户交互（如多点框选），而EchoPilot仅需单点点击和类别名称，通过冻结的视觉-语言模型和视觉基础模型实现无训练高效分割，并解决了单点上下文不足和记忆更新误差累积问题。
- 阅读启发：EchoPilot展示了利用现有预训练模型组合和智能提示策略，可以在极稀疏交互下高效处理超声视频分割这一困难任务，为临床低资源场景提供新思路。
- 可信度：high

### 25. RAPTOR+: A Visually Grounded Vision-Language Framework to Improve Clinical Trust and Auditability in Automated Cancer Referral Processing
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.25956v1
- 一句话贡献：提出RAPTOR+多模态框架，用视觉语言模型实现端到端的癌症转诊表单理解，并引入接地感知评估指标，实验证明微调VLM能显著提升证据定位的可靠性和临床可审计性。
- 核心创新点：
  - 用视觉语言模型（VLM）替代OCR+LLM的两阶段流水线，实现端到端图文理解，减少手写、布局变化等干扰
  - 提出接地感知评估框架，在提取准确率之外引入证据定位指标（Strict Safety）衡量视觉证据可追溯性
  - 将视觉语言模型引入癌症转诊处理场景，解决原有系统缺乏视觉证据链接、难以审计的临床痛点
  - 发现零样本VLM（如Gemini 2.5 Flash）虽提取准确率高（92.6%）但严格安全性极低（1.2%），而微调后的Qwen3-VL-8B在保持高准确率（96.1%）的同时严格安全性提升至60.6%
  - 定量揭示了临床文档理解中任务特定微调对可审计性的必要性
- 和已有工作的区别：与RAPTOR相比，RAPTOR+统一了OCR与语言模型为单一VLM，输出直接链接到原始视觉区域，克服了手工转录和证据丢失问题；同时提出了评估接地质量的度量而非仅关注提取数值
- 阅读启发：在医疗文档自动化处理中，仅追求字段提取精度不足以保证临床可信，必须采用微调的多模态模型确保提取结果可追溯至视觉证据
- 可信度：high

### 26. MedFM-Robust: Benchmarking Robustness of Medical Foundation Models
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/2605.19027v3
- 一句话贡献：提出了一个针对医学基础模型的鲁棒性基准，系统评估了多种扰动下的模型性能，揭示了微调策略和医学特定扰动的影响。
- 核心创新点：
  - 构建包含40种扰动类型的鲁棒性基准，其中28种为医学特定扰动
  - 覆盖8种成像模态和多个任务（VQA、视觉接地、字幕、分割）
  - 系统比较了多种微调策略（LoRA、全微调、Adapter等）的鲁棒性差异
  - 首次系统评估医学基础模型在真实世界扰动下的鲁棒性，填补该领域空白
  - 定义了医学特定扰动类别，如病理变异、成像伪影等
- 和已有工作的区别：先前工作主要关注自然图像或通用模型的鲁棒性，本文聚焦医学基础模型，并引入医学特定扰动；现有基准缺乏对医学多模态模型的系统鲁棒性评估。
- 阅读启发：为医学AI部署提供鲁棒性指南，强调领域特定鲁棒性评估的必要性，指导选择合适的微调策略和模型。
- 可信度：high

### 27. BalanceRAG: Joint Risk Calibration for Cascaded Retrieval-Augmented Generation
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/2605.20084v1
- 一句话贡献：提出BalanceRAG，通过联合风险校准级联RAG中LLM-only和RAG分支的阈值对，在控制系统级错误率的同时提高覆盖率并减少检索调用。
- 核心创新点：
  - 将LLM-only和RAG的阈值对建模为二维点阵上的操作点，使用序贯图形测试识别安全操作点
  - 实现风险自适应阈值校准，同时控制系统级错误率和选择条件风险
  - 扩展到多风险校准，可约束检索使用量
  - 首次形式化级联RAG中两个分支的联合阈值校准问题，解决分阶段校准的保守性
  - 在三个开放域QA基准上使用多个LLM骨干验证，达到预设风险水平且比全量RAG减少无用检索
- 和已有工作的区别：现有级联RAG分阶段校准阈值，未考虑联合不确定性；BalanceRAG通过二维点阵序贯测试实现联合风险校准，更高效控制错误率。
- 阅读启发：级联RAG可通过联合校准阈值对，在保证风险可控下减少检索代价，提升系统实用性。
- 可信度：high

### 28. Thinking in Scales: Accelerating Gigapixel Pathology Image Analysis via Adaptive Continuous Reasoning
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/2605.19491v2
- 一句话贡献：提出PathCTM，将全切片病理图像分析建模为动态序列信息追寻，通过自适应尺度切换和早停机制大幅降低计算开销，同时保持诊断精度。
- 核心创新点：
  - 将诊断推理转化为动态序列信息追寻过程，从低倍全局到高倍局部渐进式推理
  - 采用条件计算实现动态尺度切换，结合注意力引导的区域剪枝，避免全图密集处理
  - 引入置信度感知的早期停止机制，在证据充分时终止推理以减少冗余计算
  - 将WSI分析从传统的固定尺度多实例学习重新定义为自适应连续推理问题
  - 强调推理效率而非仅有精度，追求在极低计算成本下保持诊断性能
- 和已有工作的区别：现有MIL方法固定在高倍率下处理所有图像块，计算昂贵；PathCTM模仿病理医生由粗到细的诊断过程，动态选择关键区域和最佳分辨率，显著提升效率。
- 阅读启发：病理图像分析中，通过动态推理和早期停止可以极大提升效率，为大规模临床应用提供了可行的计算方案。
- 可信度：high

### 29. PromptRad: Knowledge-Enhanced Multi-Label Prompt-Tuning for Low-Resource Radiology Report Labeling
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/2605.20052v1
- 一句话贡献：提出PromptRad，一种知识增强的多标签提示调优方法，在仅需32个标注样本的低资源场景下实现放射报告标注，性能超越规则和微调基线，并接近GPT-4。
- 核心创新点：
  - 将多标签分类重构为掩码语言建模任务，无需额外分类层
  - 从UMLS Metathesaurus中引入同义词到多词动词化器，丰富类别语义表示
  - 利用提示调优在极少量标注数据上微调预训练语言模型
  - 关注临床放射报告标注中低资源（少量标注数据）的实际困难
  - 不同于传统基于规则或需要大量标注数据的微调方法，面向数据稀缺场景
- 和已有工作的区别：现有规则标注器难以应对多样描述，微调方法依赖大量标注数据；PromptRad通过提示调优和知识增强的动词化器，在极低资源下高效工作。
- 阅读启发：提供一种在数据稀缺临床场景下实用的放射报告标注方案，证明提示调优与医学知识库结合能有效降低标注成本。
- 可信度：high

### 30. VRXU-net: A Deep Learning Approach for Brain Ischemic Stroke Lesion Detection and Segmentation in T1W MRI
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/2605.21633v1
- 一句话贡献：提出一种先分类后分割的两阶段深度学习框架VRXU-net，通过改进VGG分类器筛选含病灶切片、残差U-Net分割，并融合三个解剖平面的分割结果，实现脑缺血卒中病灶的准确检测与分割。
- 核心创新点：
  - 将视觉特征、残差连接与U形网络结合，构建用于3D MRI的VRXU-net架构
  - 采用改进的VGG模型作为高性能分类器，在分割前过滤非病灶切片，减少计算量并提升精度
  - 独立处理轴向、矢状、冠状三个解剖平面，聚合三视图分割结果以增强定位准确性
  - 分割输出反馈至分类模型，通过双向闭环机制进一步降低假阳性预测
  - 将3D图像分解为2D切片处理，降低模型复杂度并利用多平面信息
- 和已有工作的区别：现有工作通常直接对全脑3D图像或单平面2D切片进行分割，而本文引入分类器预先筛选切片、融合三平面信息，并通过分割结果反馈提升分类性能，形成协同优化。
- 阅读启发：利用分类-分割级联与多平面聚合策略，在保证速度的同时显著提升脑卒中病灶检测分割的准确性，为临床提供可靠的辅助工具。
- 可信度：high

### 31. Cardiac fat segmentation using computed tomography and an image-to-image conditional generative adversarial neural network
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/2605.20064v1
- 一句话贡献：提出基于pix2pix条件生成对抗网络的新方法，首次实现心外膜脂肪和纵隔脂肪的自动分割与量化，精度达99.08%，F1-score分别达98.73和98.40，且支持实时分割。
- 核心创新点：
  - 将图像到图像的条件生成对抗网络pix2pix直接应用于心脏脂肪分割任务（非原始设计用途），验证其迁移有效性
  - 实现同一模型中同时分割心外膜和纵隔两种脂肪类型，利用心包作为自然空间边界
  - 聚焦于CT影像中心脏脂肪（心外膜和纵隔）的自动分割与量化，解决手动分割工作量大、成本高的问题
  - 明确区分两种由心包分隔的脂肪类型，分别评估分割性能
  - 心外膜脂肪分割准确率99.08%、F1-score 98.73；纵隔脂肪准确率97.90%、F1-score 98.40
- 和已有工作的区别：现有方法多采用传统深度分割网络（如U-Net），该方法首次将条件生成对抗网络pix2pix用于心脏脂肪分割，并在F1-score和运行时间上超越已有研究。
- 阅读启发：条件生成对抗网络可有效迁移至医学图像分割任务，尤其是使用pix2pix进行高精度、实时的多类型脂肪分割。
- 可信度：high

### 32. RoboSurg-VQA: A Multimodal Benchmark for Surgical Segmentation-Aware Visual Question Answering
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/2605.23068v1
- 一句话贡献：提出了RoboSurg-VQA，一个面向手术分割感知的视觉问答基准，通过重新利用公开分割数据集并引入临床相关问题和退化视图挑战，填补了手术VQA领域的空白。
- 核心创新点：
  - 构建了分割感知的VQA基准，将分割标签与问答任务结合
  - 通过约束提示和自动有效性检查生成候选答案，再经人工审核提升一致性
  - 设计了涵盖过程、解剖、成像模态、伪影、质量、可见性和空间属性的临床问题集
  - 首次将VQA任务与手术分割感知结合，在退化视图（遮挡、烟雾、出血等）下评估视觉理解
  - 基于现有分割数据集重新标注，扩展了数据利用率
- 和已有工作的区别：以往手术VQA工作未充分利用分割信息，且缺乏对退化视图（如遮挡、烟雾）的系统性评估；本工作通过分割感知问题集和针对性标注策略填补了这一空白。
- 阅读启发：本基准为手术视觉语言模型提供了细粒度评估工具，揭示了在复杂手术条件下VQA的挑战，并展示了如何从现有分割数据扩展VQA标注。
- 可信度：medium

### 33. ImPartial: Multi-channel Whole-Cell Segmentation using Partial Annotations
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/2605.24128v1
- 一句话贡献：提出ImPartial框架，通过自监督多通道量化插补实现使用稀疏涂鸦和有限标注的高性能全细胞分割。
- 核心创新点：
  - 引入自监督多通道量化插补，避免像素级完美重建，而是使用与分割目标一致的自监督分类目标
  - 在低标注场景下实现与全监督模型相当的性能
  - 针对多通道细胞分割中标注稀缺问题，使用稀疏涂鸦作为部分标注
  - 适用于可变通道配置的多重成像数据集
  - 在多重细胞成像和单重临床免疫组化数据集上，与强基线相比的一致改进
- 和已有工作的区别：先前工作通常需要密集像素标注或完美重建，而ImPartial利用自监督学习与部分标注，无需完美重建即可实现分割。
- 阅读启发：该工作展示了在标注稀缺的病理图像分割中，通过自监督辅助任务可以大幅减少标注需求，同时保持高性能。
- 可信度：high

### 34. Divide-and-Conquer Inference for Large-Scale Visual Recognition with Multimodal Large Language Models
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/2605.24799v1
- 一句话贡献：提出Divide-and-Conquer Inference (DCI)测试时扩展策略，通过递归分解和动态剪枝解决MLLM在大规模图像分类中长序列性能崩溃问题，无需训练即可提升准确率和推理速度。
- 核心创新点：
  - 提出递归分解全局分类任务为多个局部子问题的DCI框架
  - 设计动态剪枝机制压缩搜索空间，改善信噪比
  - 信息论分析揭示长序列中注意力稀释与衰减导致性能崩溃
  - 聚焦MLLM在大规模标签空间（如ImageNet-21K）下的性能退化问题
  - 首次将测试时计算扩展策略应用于多模态大模型的视觉识别任务
- 和已有工作的区别：现有改进MLLM长序列性能的方法多依赖微调或架构修改，DCI是模型无关、即插即用的测试时策略，无需训练即可零成本提升性能。
- 阅读启发：只需在推理时拆分任务并动态剪枝，即可让轻量MLLM在大规模分类中胜过重模型，且计算更高效。
- 可信度：high

### 35. What Makes a Medical Checker Trainable? Diagnosing Signal Collapse and Reward Hacking in Checker-Guided RAG for Biomedical QA
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/2605.25988v1
- 一句话贡献：本文发现，在医疗RAG的RL训练中，检查器的输出分布（而非准确率）决定其可训练性，并揭示信号崩溃与奖励黑客现象。
- 核心创新点：
  - 比较四种NLI后端作为GRPO训练的过程奖励，在多个LLM和医疗QA基准上实验
  - 识别LLM对数概率评分导致超过97%的claim被标记为中性，造成梯度消失
  - 发现强检查器会触发奖励黑客级联：超短答案、回避搜索、语言崩溃
  - 提出中等信号检查器可训练出更高性能的模型（+12% BERTScore）
  - 指出信号强度是策略依赖的，同一检查器在不同策略上表现不同
- 和已有工作的区别：先前工作假设检查器准确率决定其有效性，本文揭示输出分布的非退化性才是关键。
- 阅读启发：选择奖励模型时应关注其输出分布是否会出现信号崩溃或奖励黑客，中等强度信号可能更鲁棒。
- 可信度：high

### 36. Med-R2: An Adversarial Benchmark for Evidence-Grounded Reasoning in Medical VLMs
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/2605.24492v1
- 一句话贡献：提出了一个与临床工作流对齐的分层对抗基准Med-R2，用于系统评估和提升医学视觉语言模型在证据基础推理中的鲁棒性。
- 核心创新点：
  - 设计了与临床四阶段工作流（采集、分析、诊断、治疗）对齐的层次化QA任务
  - 在图像中施加对抗性扰动以测试模型对误导视觉线索的鲁棒性
  - 构建了包含42,432张图像、31个任务类别、110,406个QA对的大规模基准数据集
  - 首次定义并评估医学VLM在临床工作流各阶段中推理链是否严格基于视觉证据
  - 将对抗鲁棒性测试引入医学视觉问答任务，关注误导性视觉线索的影响
- 和已有工作的区别：现有医学VLM基准多关注整体问答准确率，未系统评估推理过程是否基于证据及对误导线索的鲁棒性，而Med-R2填补了这一空白。
- 阅读启发：医学VLM在临床推理中仍存在严重鲁棒性缺陷，本研究提供了评估和改进的工具，推动证据基础的医疗AI发展。
- 可信度：high
