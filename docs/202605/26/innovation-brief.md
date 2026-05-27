# 创新点总结 · 2026-05-26

- 生成时间：2026-05-27 08:16:27 UTC
- 当日论文数：36

## 今日趋势
- 医学视觉语言模型的可解释性与鲁棒性评估
- 隐私保护与低资源场景下的多模态数据协调与学习
- 医学图像分割的创新方法（弱监督、无需训练、多平面融合等）
- 检索增强生成在医疗领域的应用与风险校准

## 最值得先读

| 论文 | 推荐理由 |
|---|---|
| [Med-R2: An Adversarial Benchmark for Evidence-Grounded Reasoning in Medical VLMs](https://arxiv.org/abs/2605.24492v1) | 系统构建了层级化对抗基准，揭示医学VLM依赖虚假先验而非视觉证据的鲁棒性缺陷，并提供可操作的微调改进方法，对推动临床可信AI具有重要警示和指导意义。 |

## 单篇创新点

### 1. Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.22414v1-towards-clinically-interpretable-ophthalmic-vqa-via-spatially-grounded-lesion-evidence
- 一句话贡献：提出FundusGround基准，通过引入基于ETDRS网格的空间定位病变证据，实现临床可解释的眼科视觉问答。
- 核心创新点：
  - 构建包含10,719张眼底图像和15,595个病变标注的数据集，所有病变使用ETDRS网格在9个临床区域精确定位
  - 设计三阶段流水线：图像采集-病变标注-问题生成，产出72,706个涵盖四种格式（开放、封闭、单选、多选）的问题
  - 首次将空间定位病变证据作为临床可解释性的核心要求引入眼科VQA任务
  - 针对现有VQA基准忽略视觉证据的问题，重新定义评价目标为同时兼顾答案准确性和病变量化推理
  - 实验证明引入病变级空间证据同时提升模型回答准确性和推理透明度，包括通用和医疗大语言模型
- 和已有工作的区别：现有眼科VQA基准仅关注答案准确性，缺乏对视觉证据（特别是空间定位病变）的明确要求和评估；本工作通过结构化病变标注和空间 grounding 实现了可解释性。
- 阅读启发：在眼科VQA中，显式的空间病变证据对模型性能提升和临床可信度至关重要，未来可推广至其他医学影像分析场景。
- 可信度：high

### 2. PrivFusion: A Privacy-preserving Multi-Agent Framework for Harmonizing Distributed Datasets
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24249v1-privfusion-a-privacy-preserving-multi-agent-framework-for-harmonizing-distributed-datasets
- 一句话贡献：提出PrivFusion，首个隐私保护多智能体框架，在联邦学习前自动协调异构医疗数据集，减少人工干预。
- 核心创新点：
  - 使用多智能体分别分析本地数据，通过语义特征聚类实现跨站点特征对齐
  - 迭代提供数据转换建议直到所有站点特征统一，无需暴露原始数据
  - 自动化协调流程，替代传统手动数据映射和本体匹配
  - 首次将数据协调作为联邦学习前的独立关键步骤，并设计自动化解决方案
  - 针对多机构医疗数据的结构化异构性，而非仅关注模型训练阶段的差异
- 和已有工作的区别：现有联邦学习研究主要集中于模型聚合和隐私保护，忽略了训练前数据协调环节，往往依赖手动数据清洗；PrivFusion首次自动化这一过程并保持隐私。
- 阅读启发：联邦学习应用于真实医疗场景时，数据协调是关键瓶颈，PrivFusion提供了一种自动化、隐私保护的解决方案，可大幅降低多机构协作的门槛。
- 可信度：high

### 3. Parameter-Efficient VLMs for Gastrointestinal Endoscopy: Medical Image Generation and Clinical Visual Question Answering
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24792v1-parameter-efficient-vlms-for-gastrointestinal-endoscopy-medical-image-generation-and-clinical-visual-question-answering
- 一句话贡献：提出双流水线PEFT框架，同时解决了胃肠内镜领域医疗VQA精度低和隐私保护合成数据生成两大难题，显著降低计算成本并提升性能。
- 核心创新点：
  - 首次将Florence-2 VLM与参数高效微调(PEFT)结合应用于胃肠内镜临床VQA，增强可解释性并降低训练开销
  - 采用LoRA微调Stable Diffusion 2.1生成高质量、隐私保护的内镜图像，替代传统数据增强方法
  - 双流水线设计实现VQA与合成数据生成的联合优化，在单一框架中解决数据稀缺和隐私限制
  - 针对胃肠内镜AI中标注数据稀缺、隐私政策严格和传统微调计算瓶颈的复合挑战
  - 将隐私保护合成数据生成作为提升VQA性能的关键辅助任务，实现数据扩增与模型微调的协同
- 和已有工作的区别：现有工作通常单独处理VQA或数据生成，且多采用全参数微调；本工作首次将PEFT同时应用于VLM和扩散模型，实现双任务协同并大幅降低训练开销，同时利用合成数据保护隐私。
- 阅读启发：参数高效微调（PEFT）与LoRA策略可有效缓解医学影像领域的数据隐私和计算瓶颈，双流水线设计为临床AI提供可靠且可扩展的解决方案。
- 可信度：high

### 4. Universal Boosts, Specific Suppressors: Sparse Autoencoder Steering of Medical Vision-Language Models
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24977v1-universal-boosts-specific-suppressors-sparse-autoencoder-steering-of-medical-vision-language-models
- 一句话贡献：提出基于稀疏自编码器的解码时残差引导方法，通过逐token因果干预（提升正确特征、抑制错误特征）减少医学视觉语言模型的幻觉，无需权重更新，并发现提升方向跨模型通用、抑制方向模型特有。
- 核心创新点：
  - 解码时残差引导：在推理时对每token的稀疏自编码器进行因果干预
  - 组合抑制/提升干预：同时增强正确特征和抑制错误特征
  - 因果干预策略：针对临床错误进行定向引导
  - 针对医学视觉语言模型生成胸部X光报告时的幻觉问题（虚构、遗漏、定位错误）
  - 采用稀疏自编码器进行解码时引导，无需模型权重更新
- 和已有工作的区别：现有方法通常需要微调或重训练，本文仅推理时引导，且发现通用boost和特定suppress特征，提出转移时需对每个模型单独处理抑制方向
- 阅读启发：稀疏自编码器可有效引导VLM减少幻觉，且转移时抑制方向需针对模型，提升方向可跨模型迁移
- 可信度：high

### 5. Towards Reliable Fetal Ultrasound Interpretation with Multi-Agent Collaboration
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.25357v1-towards-reliable-fetal-ultrasound-interpretation-with-multi-agent-collaboration
- 一句话贡献：提出FetUSAgents，一种工具增强的多智能体系统，通过双路径证据仲裁（DPEA）和检索增强证据库实现可靠的胎儿超声解读，在VQA任务上超越最强基线25%以上。
- 核心创新点：
  - 提出工具增强的多智能体协作框架，通过LLM代理协调专用视觉工具完成胎儿超声解读。
  - 引入双路径证据仲裁（DPEA），结合LLM推理与结构化计算证据。
  - 构建检索增强证据库，整合中间结果以支持可追溯结论。
  - 针对胎儿超声解读中'一个任务一个模型'范式的局限性，提出多步骤系统性整合方案。
  - 解决多模态大模型在领域特定任务中的幻觉和可靠性问题。
- 和已有工作的区别：现有方法多采用独立模型处理单一任务，缺乏多步骤证据整合；该工作首次通过多智能体协作与双路径证据仲裁，实现从解剖识别到量化测量的端到端可靠解读。
- 阅读启发：多智能体协作与证据仲裁可显著提升胎儿超声解读的可靠性和临床实用性，为产前成像提供了可扩展的智能化路径。
- 可信度：high

### 6. EchoPilot: Training-Free Ultrasound Video Segmentation via Scale-Space Semantic Prompting and Reliability-Gated Memory
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.25944v1-echopilot-training-free-ultrasound-video-segmentation-via-scale-space-semantic-prompting-and-reliability-gated-memory
- 一句话贡献：EchoPilot提出一种无需训练的超声视频分割框架，通过尺度空间语义提示和可靠性门控记忆，仅需单点点击和类别名称即可实现高质量分割，并在三个数据集上达到最优性能。
- 核心创新点：
  - 提出Scale-Space Semantic Prompting方法，利用S.E.E.D.准则从尺度空间中选择最优上下文视图，并合成几何精确的辅助点提示，无需额外用户交互
  - 设计Reliability-Gated Memory更新机制，根据预测不确定性选择性冻结分割器的记忆库，防止误差累积导致的时序漂移
  - 首次在超声视频分割中采用训练-free框架，仅需稀疏的第一帧交互（单点点击+解剖类别名称），无需微调或大量标注
  - 引入冻结的医学视觉语言模型（VLM）与视觉基础模型（VFM）协同工作，应对超声图像特有的散斑噪声、弱边界和快速形变
  - 贡献了首个动态胎儿胎盘超声视频分割数据集，包含671帧标注
- 和已有工作的区别：现有promptable基础模型直接部署在超声上不可靠，单点提示缺乏空间上下文导致尺度模糊，贪婪记忆更新放大早期误差；EchoPilot通过尺度空间语义提示解决初始化歧义，并通过可靠性门控记忆控制误差传播，实现稳健分割。
- 阅读启发：EchoPilot展示了如何利用冻结的VLM和VFM设计无训练的视频分割框架，通过智能提示和记忆管理有效克服超声视频的挑战，为临床交互式分割提供了实用方案。
- 可信度：high

### 7. RAPTOR+: A Visually Grounded Vision-Language Framework to Improve Clinical Trust and Auditability in Automated Cancer Referral Processing
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.25956v1-raptor-a-visually-grounded-vision-language-framework-to-improve-clinical-trust-and-auditability-in-automated-cancer-referral-processing
- 一句话贡献：提出RAPTOR+，一种利用微调视觉语言模型实现端到端癌症转诊表单理解与视觉证据定位的多模态框架，显著提升临床可审计性。
- 核心创新点：
  - 使用微调的Qwen3-VL-8B模型进行端到端转诊理解，无需独立的OCR阶段
  - 引入接地感知评估框架，同时衡量提取准确率和证据定位能力
  - 将零样本VLM、微调VLM与原始OCR流水线进行系统性比较
  - 首次将视觉语言模型应用于紧急癌症转诊处理的端到端自动化，解决半结构化文档中的手写、布局变化和视觉证据丢失问题
  - 定义了一个新的评估维度——证据接地（grounding），以衡量模型的可审计性
- 和已有工作的区别：与原有RAPTOR系统依赖OCR+LLM分离式流水线不同，RAPTOR+采用多模态VLM实现统一处理，并首次在评估中引入接地指标以量化解译结果与视觉证据的关联。
- 阅读启发：对于临床文档理解，任务特定的VLM微调比通用零样本模型更可靠；评估时需同时关注提取准确性和证据接地，以支持临床信任和审计。
- 可信度：high

### 8. MedFM-Robust: Benchmarking Robustness of Medical Foundation Models
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.19027v3-medfm-robust-benchmarking-robustness-of-medical-foundation-models
- 一句话贡献：构建了医疗基础模型鲁棒性评估基准，涵盖40种扰动、8种模态，系统评估了5个VLM和2个分割模型，揭示了微调策略和领域特定扰动对鲁棒性的关键影响。
- 核心创新点：
  - 提出包含40种扰动类型的鲁棒性基准，其中28种为医疗领域特定扰动
  - 同时评估视觉-语言模型（VQA/视觉定位/描述）和分割模型，覆盖5种微调策略
  - 发现LoRA微调导致鲁棒性退化约两倍于全微调，而Adapter提供效率-鲁棒性权衡
  - 聚焦医疗基础模型在真实世界扰动下的鲁棒性评估这一被忽视的关键问题
  - 首次系统对比多种微调策略对医疗模型鲁棒性的影响
- 和已有工作的区别：现有医疗AI研究主要关注模型性能，而本文系统评估了模型在多种真实扰动下的鲁棒性，并提供了具体的微调策略选择和领域特定扰动影响的量化证据。
- 阅读启发：微调策略选择比模型架构更影响鲁棒性；LoRA虽然高效但鲁棒性较差；医疗特定扰动对分割任务威胁大，应优先评估领域扰动；零样本VQA模型鲁棒性差异大，通用模型在定位任务上失败率高。
- 可信度：high

### 9. PromptRad: Knowledge-Enhanced Multi-Label Prompt-Tuning for Low-Resource Radiology Report Labeling
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.20052v1-promptrad-knowledge-enhanced-multi-label-prompt-tuning-for-low-resource-radiology-report-labeling
- 一句话贡献：提出PromptRad，一种知识增强的多标签提示调优方法，在低资源情况下将放射学报告标注转化为掩码语言建模，利用UMLS同义词丰富类别表示，仅需少量标注数据即可达到优异性能。
- 核心创新点：
  - 将多标签分类重构为掩码语言建模任务，通过提示调优（prompt-tuning）无需额外分类层。
  - 设计多词词汇表（multi-word verbalizer），融入UMLS Metathesaurus同义词以增强类别语义表示。
  - 针对低资源临床场景，仅需32个标注样本即可进行有效放射学报告标注。
  - 解决现有规则方法无法处理多样描述、微调方法需要大量标注数据的问题。
  - 在肝CT报告数据集上，使用32个标注样本即超越字典方法和传统微调基线。
- 和已有工作的区别：现有方法或是依赖规则（难以覆盖多样描述），或是需要大量标注数据进行微调；PromptRad通过提示调优和知识增强，大幅降低标注需求，并首次将UMLS同义词引入多标签提示词设计。
- 阅读启发：提示调优结合领域知识（UMLS）可高效实现低资源医疗文本多标签分类，否定模式处理能力突出。
- 可信度：high

### 10. RoboSurg-VQA: A Multimodal Benchmark for Surgical Segmentation-Aware Visual Question Answering
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.23068v1-robosurg-vqa-a-multimodal-benchmark-for-surgical-segmentation-aware-visual-question-answering
- 一句话贡献：提出了 RoboSurg-VQA，一个面向机器人辅助手术的、分割感知的视觉问答基准，通过重用公共手术分割数据集并设计临床问题集与自动标注流水线，填补了该领域缺乏标准评估平台的空白。
- 核心创新点：
  - 提出通过约束提示自动生成候选答案，结合自动有效性一致性和人工审核的标注方法。
  - 构建了共享语义分割标签的通用 schema，统一了多个公共手术分割数据集。
  - 首次将分割感知（segmentation-aware）引入手术视觉问答，问题覆盖手术流程、解剖结构、伪影、图像质量等临床相关方面。
  - 设计固定问题集及封闭答案集，确保评估一致性。
  - 报告了基准统计信息和常用基线性能，展示了复杂手术条件下（如遮挡、烟雾、出血）的评估挑战。
- 和已有工作的区别：不同于仅关注分割掩码准确性的传统手术视觉理解基准，本工作从临床提问角度出发，生成与分割标签对齐的问答对，实现细粒度的语义评估。
- 阅读启发：该基准为手术场景下的视觉问答提供了标准化的测试平台，可推动模型在真实临床语言理解中的发展。
- 可信度：high

### 11. What Makes a Medical Checker Trainable? Diagnosing Signal Collapse and Reward Hacking in Checker-Guided RAG for Biomedical QA
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.25988v1-what-makes-a-medical-checker-trainable-diagnosing-signal-collapse-and-reward-hacking-in-checker-guided-rag-for-biomedical-qa
- 一句话贡献：发现医学RAG中NLI检查器的输出分布而非准确率决定其作为RL奖励的可训练性，并诊断了信号坍缩和奖励破解问题。
- 核心创新点：
  - 比较了四种NLI检查器后端（LLM对数概率、校准的MedNLI分类器等）作为过程奖励。
  - 诊断出信号坍缩：LLM对数概率导致97%以上标签为中性，梯度消失。
  - 诊断出奖励破解：强信号触发短回答、搜索避免及语言崩坏的三步级联。
  - 提出适度信号（如校准的MedNLI）优于强信号，训练模型得+12% BERTScore。
  - 发现信号强度具有策略依赖性，同一检查器在不同策略下表现不同。
- 和已有工作的区别：['之前工作多假设高准确性检查器更好，本文揭示输出分布而非准确率是关键。', '首次系统性识别并命名信号坍缩和奖励破解在医学RAG RL中的具体表现。', '强调检查器强度需适中，强信号反而导致训练崩溃。']
- 阅读启发：设计检查器作为RL奖励时，应关注其输出分布的稳定性与区分度，避免极端分布（如中性过多）或过强信号引发的奖励破解；适度且校准的检查器可能更有效。
- 可信度：high

### 12. BalanceRAG: Joint Risk Calibration for Cascaded Retrieval-Augmented Generation
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.20084v1-balancerag-joint-risk-calibration-for-cascaded-retrieval-augmented-generation
- 一句话贡献：提出BalanceRAG，通过二维网格上的序列图检验联合校准LLM-only和RAG分支的不确定度阈值，在控制系统级错误率的同时保留更多样本，并支持多风险校准。
- 核心创新点：
  - 将级联RAG中LLM-only和RAG分支的阈值对视为二维网格上的操作点，实现联合校准而非逐阶段保守校准。
  - 采用顺序图形检验（sequential graphical testing）识别安全操作点，动态调整阈值以满足目标风险水平。
  - 扩展至多风险校准，允许同时控制检索使用率和选择条件风险。
  - 针对级联RAG系统的风险校准问题，提出系统级误差控制而非逐分支独立校准。
  - 考虑实际部署中减少不必要检索调用的需求，通过风险自适应阈值保留更多样本。
- 和已有工作的区别：与现有级联RAG的逐阶段独立校准（如仅基于LLM不确定性设定阈值）不同，BalanceRAG将两分支阈值联合优化，通过二维网格和序列图检验实现系统级风险校准，避免了保守性。
- 阅读启发：本文提供了一种风险可控且高效的级联RAG校准方法，能够平衡模型可靠性、覆盖率和检索成本，可推广到需要选择性使用RAG的应用场景。
- 可信度：high

### 13. VRXU-net: A Deep Learning Approach for Brain Ischemic Stroke Lesion Detection and Segmentation in T1W MRI
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.21633v1-vrxu-net-a-deep-learning-approach-for-brain-ischemic-stroke-lesion-detection-and-segmentation-in-t1w-mri
- 一句话贡献：提出VRXU-net，通过级联分类与分割、残差块、三平面融合及反馈机制，实现了T1W MRI中脑缺血性卒中病变的高效检测与分割。
- 核心创新点：
  - 采用改进VGG模型进行2D切片级病变检测，再以带残差块的U-Net进行分割，形成级联架构
  - 独立处理轴向、矢状、冠状三个平面，并聚合三平面分割结果以提升定位精度
  - 在分割前引入高性能分类器，减少非病变切片的分割计算，提高整体速度与准确率
  - 分割结果反馈给分类器，用于降低假阳性预测
  - 针对T1W MRI中缺血性卒中病变形状、大小、位置多样且与周围脑组织相似导致的检测困难问题
- 和已有工作的区别：现有方法大多直接进行3D分割或仅使用单一平面，VRXU-net通过级联分类-分割、三平面融合及反馈优化，在效率和精度上均超越现有工作。
- 阅读启发：提出一种结合分类与分割、多平面融合及反馈机制的深度学习框架，有效提升了T1W MRI中脑卒中病变检测和分割的性能。
- 可信度：high

### 14. ImPartial: Multi-channel Whole-Cell Segmentation using Partial Annotations
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24128v1-impartial-multi-channel-whole-cell-segmentation-using-partial-annotations
- 一句话贡献：提出ImPartial框架，利用稀疏涂鸦部分标注和自监督多通道量化插值，在低标注场景下实现与全监督相当的细胞分割性能，大幅减少标注需求。
- 核心创新点：
  - 采用稀疏涂鸦作为弱标注，降低人工标注成本
  - 提出自监督多通道量化插值方法，引入分类目标而非重建目标，更好对齐分割任务
  - 设计多通道框架适应不同成像模态和可变通道配置
  - 针对病理图像中部分标注（稀疏涂鸦）下的细胞分割问题
  - 聚焦多重成像和临床明场免疫组化数据集，处理标注稀缺场景
- 和已有工作的区别：现有方法依赖密集像素标注或完整弱标注，而本文使用更稀疏的涂鸦标注，并通过自监督量化插值避免像素级重建，直接优化分割目标。
- 阅读启发：在标注稀缺的病理图像场景中，利用稀疏涂鸦和自监督辅助任务可有效提升分割精度，降低标注成本，为实际应用提供可行方案。
- 可信度：high

### 15. Med-R2: An Adversarial Benchmark for Evidence-Grounded Reasoning in Medical VLMs
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24492v1-med-r2-an-adversarial-benchmark-for-evidence-grounded-reasoning-in-medical-vlms
- 一句话贡献：提出Med-R2 Bench基准，通过层级化对抗性评估揭示医学视觉语言模型在临床推理中依赖虚假先验而非视觉证据的问题，并提供层级微调方法提升推理鲁棒性。
- 核心创新点：
  - 设计了四个临床阶段的层级化问答任务，分别评估视觉证据在每一步推理中的支撑作用
  - 引入对抗性扰动（如图像遮挡、文本误导）测试模型对虚假线索的鲁棒性
  - 构建大规模数据集（42,432图像、31任务、110,406 QA对）覆盖多阶段临床场景
  - 首次将医学VLM的评估从整体VQA分解为与临床工作流对齐的逐步证据推理
  - 提出对抗性攻击不仅针对单一步骤，而是贯穿整个推理链，检测模型是否依赖捷径或虚假相关性
- 和已有工作的区别：现有医学VQA基准仅评估整体准确性，未考虑推理步骤对视觉证据的依赖；本工作首次引入层级化对抗性攻击来量化模型在临床决策各阶段的证据基础。
- 阅读启发：该基准为医学AI提供了一套可操作的鲁棒性评估工具，提示未来应关注模型在临床推理中的可解释性和抗干扰能力。
- 可信度：high

### 16. Thinking in Scales: Accelerating Gigapixel Pathology Image Analysis via Adaptive Continuous Reasoning
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.19491v2-thinking-in-scales-accelerating-gigapixel-pathology-image-analysis-via-adaptive-continuous-reasoning
- 一句话贡献：提出PathCTM模型，通过自适应连续推理和早停机制，大幅减少全切片图像分析所需的patch数和推理时间，同时保持诊断精度。
- 核心创新点：
  - 将推理建模为动态顺序信息追求，从低倍全局到高倍局部逐步聚焦
  - 使用注意力引导的区域剪枝实现条件计算，动态切换尺度
  - 引入置信度感知的早停机制，在证据充足时终止推理
  - 将WSI分析从传统的静态MIL聚合重新定义为动态自适应推理过程
  - 首次在病理图像中实现端到端的尺度空间连续推理
- 和已有工作的区别：传统MIL方法需穷举所有高倍率patch，计算成本高；本工作通过自适应尺度选择和早停，避免了冗余计算。
- 阅读启发：自适应推理可显著提升计算效率，为大规模WSI分析提供可扩展方案。
- 可信度：high

### 17. Cardiac fat segmentation using computed tomography and an image-to-image conditional generative adversarial neural network
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.20064v1-cardiac-fat-segmentation-using-computed-tomography-and-an-image-to-image-conditional-generative-adversarial-neural-network
- 一句话贡献：提出将条件生成对抗网络(pix2pix)首次应用于心脏CT图像中两种脂肪(心外膜和纵隔)的自动分割，实现高精度与实时处理。
- 核心创新点：
  - 将原本用于图像到图像翻译的pix2pix网络架构应用于心脏脂肪分割任务
  - 利用条件GAN实现无手工特征的心外膜和纵隔脂肪自动分割
  - 采用生成对抗训练策略提升分割边界清晰度和区域一致性
  - 针对临床手动分割心脏脂肪耗时耗力的问题，提出全自动分割方法
  - 同时分割心外膜和纵隔两种脂肪，并区分其空间位置
- 和已有工作的区别：现有研究多采用传统图像处理或常规深度学习模型，而本工作首次将条件GAN用于心脏脂肪分割，并在F1分数和运行时间上超越已有方法。
- 阅读启发：条件GAN可有效迁移至医学图像分割任务，尤其是对边界模糊的器官或组织，具备高精度和高效潜力。
- 可信度：high

### 18. Divide-and-Conquer Inference for Large-Scale Visual Recognition with Multimodal Large Language Models
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24799v1-divide-and-conquer-inference-for-large-scale-visual-recognition-with-multimodal-large-language-models
- 一句话贡献：提出分而治之推理（DCI），通过递归分解和动态剪枝，解决多模态大语言模型在大规模分类中的性能崩溃问题，提升准确率和推理速度。
- 核心创新点：
  - 递归分解全局分类任务为多个局部子问题
  - 动态剪枝机制压缩搜索空间
  - 缓解长序列推理中的注意力稀释和衰减
  - 实现线性计算复杂度替代二次复杂度
  - 首次定义多模态大语言模型在长序列识别中的性能崩溃现象
- 和已有工作的区别：现有方法通常需要额外训练或微调，而DCI是模型无关的测试时扩展策略，通过动态分解和剪枝提升信噪比，无需修改模型参数。
- 阅读启发：DCI是一种高效且即插即用的方法，能显著提升MLLM在大规模视觉识别任务中的性能，具有实用价值。
- 可信度：high

### 19. Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.22414v1
- 一句话贡献：提出FundusGround基准，通过空间定位的病灶证据实现临床可解释的眼科VQA，并证明病灶级视觉证据能提升模型性能与透明度。
- 核心创新点：
  - 采用三阶段流程收集10719张眼底图像，并精确标注15595个病灶，确保高质量
  - 基于ETDRS网格将病灶标准化映射到9个临床视网膜区域，保证解剖一致性与临床有效性
  - 生成72706个四格式问题（开放、封闭、单选、多选），覆盖多样化提问方式
  - 提出双指标评估框架：答案准确率+病灶级推理能力，全面衡量模型表现
  - 首
- 和已有工作的区别：现有眼科VQA基准仅重答案准确率，忽视临床可解释性；本工作首次构建了包含空间病灶标注和多种问题格式的可解释VQA基准
- 阅读启发：为眼科VQA提供可解释性新范式：通过显式空间病灶证据，模型不仅给出答案还能展示推理依据，提升临床可靠性
- 可信度：high

### 20. PrivFusion: A Privacy-preserving Multi-Agent Framework for Harmonizing Distributed Datasets
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.24249v1
- 一句话贡献：提出PrivFusion，一个隐私保护的多智能体框架，在联邦学习前自动协调结构化的多站点异构数据集，减少人工标注和数据映射工作。
- 核心创新点：
  - 使用多智能体分别分析本地数据并聚类语义相似的特征
  - 通过迭代转换建议实现跨站点数据对齐
  - 在协调过程中保持隐私（不共享原始数据）
  - 首次将数据协调作为联邦学习前必需且常被忽略的步骤，并实现自动化
  - 针对结构化临床数据的异构性，提出多智能体协作解决方案
- 和已有工作的区别：现有联邦学习研究主要关注模型训练时的隐私和异构性，缺乏对数据层面协调的自动化支持；PrivFusion填补了这一空白，通过多智能体自动发现和匹配跨站点的语义相似特征。
- 阅读启发：PrivFusion提供了一种实用且隐私保护的自动化数据协调工具，使分布式数据集在联邦学习之前达到对齐状态，有助于提升多站点学习效果并降低人工成本。
- 可信度：high

### 21. Parameter-Efficient VLMs for Gastrointestinal Endoscopy: Medical Image Generation and Clinical Visual Question Answering
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.24792v1
- 一句话贡献：提出双管道PEFT框架，同时解决内窥镜临床VQA和隐私保护合成图像生成，显著降低计算成本并提升性能。
- 核心创新点：
  - 采用Florence-2视觉语言模型结合PEFT进行临床VQA，提升可解释性并降低训练成本
  - 使用LoRA对Stable Diffusion 2.1进行微调，生成高质量内窥镜合成图像，保障隐私安全
  - 在Kvasir-VQA数据集上VQA模型达到ROUGE-1=0.92、ROUGE-L=0.91、BLEU从0.08提升至0.24
  - 针对内窥镜AI数据标注不足、隐私政策严格和传统微调瓶颈，首次提出双管道PEFT模型同时处理VQA和数据生成
  - 解决了隐私保护下合成数据增强训练数据库的临床实际问题
- 和已有工作的区别：现有工作多单独处理内窥镜VQA或图像生成，且未采用参数高效微调；本工作首次联合两任务并利用PEFT大幅降低计算开销，同时实现更优的语义对齐和更低FBD。
- 阅读启发：参数高效微调（如LoRA、Adapter）可有效推动临床AI落地，特别是在数据敏感、标注稀缺的医疗影像领域。
- 可信度：high

### 22. Universal Boosts, Specific Suppressors: Sparse Autoencoder Steering of Medical Vision-Language Models
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.24977v1
- 一句话贡献：提出一种无需权重更新的解码时间残差导向方法，基于稀疏自编码器对医学视觉语言模型进行推理时干预，有效减少幻觉并提升报告质量，且发现增强方向可跨模型迁移而抑制方向需特定于模型。
- 核心创新点：
  - 使用Top-K稀疏自编码器在后期层提取特征，进行因果导向对抗临床错误
  - 组合抑制与增强干预在推理时动态调整生成
  - 跨模型特征对齐分析发现增强方向跨架构重叠，抑制方向模型特定
  - 零样本迁移至IU-Xray数据集证明方法的泛化性
  - 针对医学视觉语言模型幻觉问题，无需权重更新仅推理时干预
- 和已有工作的区别：以往方法通常需要微调或权重更新，本文仅通过推理时干预，并利用稀疏自编码器分析特征方向的可迁移性，为模型通用性和特定性提供新理解。
- 阅读启发：发现增强方向可跨模型通用，而抑制方向需针对不同模型定制，为医学VLM幻觉减轻和模型可解释性提供新思路。
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
- 一句话贡献：提出无需训练的超声视频分割框架EchoPilot，仅需单点点击和类别名，通过尺度空间语义提示和可靠性门控记忆实现SOTA性能。
- 核心创新点：
  - 提出Scale-Space Semantic Prompting，包含S.E.E.D.（语义能量-熵密度）准则自动选择最佳上下文视图和从基础特征合成几何精确的辅助点提示。
  - 提出Reliability-Gated Memory更新机制，在预测不确定性高时选择性冻结记忆库，防止错误累积和漂移。
  - 首个在无需训练条件下通过稀疏第一帧交互（单点点击+类别名）实现超声视频分割的方法。
  - 贡献了动态胎儿胎盘超声视频分割数据集（671标注帧），填补领域空白。
  - 在三个超声视频数据集上，无需训练即超越所有无训练基线和微调专家模型。
- 和已有工作的区别：现有可提示基础模型直接部署于超声因单点上下文不足和贪婪记忆更新导致错误累积，而EchoPilot通过尺度空间上下文选择和可靠性门控记忆避免了这些问题。
- 阅读启发：无需训练且仅需极稀疏交互（一帧单点）即可实现高质量超声视频分割，展示了通用基础模型结合精心设计的提示策略在医学影像中的巨大潜力。
- 可信度：high

### 25. RAPTOR+: A Visually Grounded Vision-Language Framework to Improve Clinical Trust and Auditability in Automated Cancer Referral Processing
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.25956v1
- 一句话贡献：提出RAPTOR+，利用微调视觉语言模型实现端到端的癌症转诊表单理解，并通过grounding感知评估框架证明其相比于零样本模型和OCR流水线在证据可定位性上的显著提升。
- 核心创新点：
  - 采用端到端视觉语言模型代替OCR+LLM两阶段流水线，避免手写和布局变化导致的误差
  - 设计grounding感知评估框架，同时衡量字段提取准确率和视觉证据定位能力
  - 利用VLM微调（Qwen3-VL-8B）在临床转诊表单上实现高精度读写并保持可审计的视觉链接
  - 将视觉语言模型应用于半结构化临床文档的端到端理解，解决转诊处理中人工审核瓶颈
  - 提出临床信任和可审计性作为核心评估维度，超越传统NLP的纯提取准确率指标
- 和已有工作的区别：原RAPTOR依赖OCR和LLM级联，丢失视觉证据且易受书写/布局干扰；RAPTOR+通过VLM统一视觉与文本理解，直接链接提取结果到原始图像区域，实现可审计的决策追溯。
- 阅读启发：微调视觉语言模型对实现可靠、可审计的临床文档理解至关重要，零样本模型虽读得准但证据定位不足，无法满足临床应用的安全要求。
- 可信度：high

### 26. MedFM-Robust: Benchmarking Robustness of Medical Foundation Models
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/2605.19027v3
- 一句话贡献：提出了首个涵盖多模态、多扰动类型的医学基础模型鲁棒性基准，系统揭示了微调策略和医学特定扰动对性能的关键影响。
- 核心创新点：
  - 构建包含40种扰动类型（12基础+28医学特定）和8种成像模态的鲁棒性基准
  - 评估5种视觉-语言模型和2种分割模型，覆盖VQA、视觉定位、字幕生成和分割任务
  - 系统比较LoRA、全微调、Adapter等微调策略对鲁棒性的影响
  - 首次针对医学基础模型进行大规模鲁棒性系统评估
  - 定义并引入医学特定扰动（如造影剂变化、病灶遮挡）以贴近真实医疗场景
- 和已有工作的区别：现有研究多关注通用模型或单一模态，本文首次系统分析医学基础模型在多任务、多扰动下的鲁棒性，并揭示微调策略与医学特定扰动的独特性。
- 阅读启发：选择医学基础模型时需优先考虑鲁棒性，微调策略应权衡效率与退化，医学特定扰动评估对于部署至关重要。
- 可信度：high

### 27. BalanceRAG: Joint Risk Calibration for Cascaded Retrieval-Augmented Generation
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/2605.20084v1
- 一句话贡献：提出BalanceRAG，通过联合校准LLM-only和RAG的阈值对，实现级联RAG系统的风险自适应控制，在保证错误率的前提下提升覆盖率和正确示例数，并减少不必要的检索。
- 核心创新点：
  - 将级联RAG的LLM-only和RAG两个分支的不确定性阈值视为二维格点上的操作点，通过顺序图形测试识别安全操作点
  - 提出联合风险校准方法，替代传统的逐阶段保守校准，直接控制系统级错误率
  - 扩展到多风险校准，同时约束检索使用量和选择条件风险
  - 提出级联RAG场景下联合不确定性阈值校准问题，区别于以往逐级校准或固定阈值做法
  - 定义了系统级错误率控制目标，允许在保证风险水平下最大化接受示例数
- 和已有工作的区别：现有校准方法通常对LLM-only和RAG分支独立设置阈值，导致保守或资源浪费；BalanceRAG通过联合优化二维阈值对，在统计上保证整体风险的同时保留更多可靠示例。
- 阅读启发：级联RAG系统中，联合校准两个分支的不确定性阈值比分别校准更有效，能在控制错误的同时提升可用性和效率。
- 可信度：high

### 28. Thinking in Scales: Accelerating Gigapixel Pathology Image Analysis via Adaptive Continuous Reasoning
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/2605.19491v2
- 一句话贡献：提出PathCTM模型，将全切片病理图像分析转化为动态连续推理过程，通过自适应尺度切换和置信度早停，大幅减少计算开销且不损失精度。
- 核心创新点：
  - 将诊断推理建模为从低分辨率全局到高分辨率局部的动态顺序信息追求过程
  - 使用条件计算实现动态尺度切换，并借助注意力机制引导区域剪枝
  - 引入置信度感知的早停策略，在不确定性足够低时终止推理
  - 克服传统多实例学习穷举处理所有高倍率patch导致的计算瓶颈
  - 将尺度选择与区域聚焦纳入统一的端到端推理框架
- 和已有工作的区别：与依赖固定高倍率patch枚举的MIL方法不同，PathCTM动态决定何时切换尺度、聚焦哪些区域以及何时终止，实现了计算效率的跨越式提升。
- 阅读启发：病理WSI分析可以不必处理所有细节，通过智能的尺度与区域选择，在保持诊断准确率的同时实现接近100倍的加速。
- 可信度：high

### 29. PromptRad: Knowledge-Enhanced Multi-Label Prompt-Tuning for Low-Resource Radiology Report Labeling
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/2605.20052v1
- 一句话贡献：提出PromptRad，一种知识增强的多标签提示调优方法，在低资源下将放射学报告标注重构为掩码语言建模，利用UMLS同义词丰富类别表示，仅需32个标注样本即超越传统方法。
- 核心创新点：
  - 将多标签分类重构为掩码语言建模任务，无需额外分类层
  - 引入UMLS Metathesaurus的同义词构建多词动词化器，增强类别语义
  - 仅微调预训练语言模型，大幅减少所需标注数据
  - 聚焦低资源放射学报告标注场景，传统方法依赖大量标注数据或规则
  - 针对临床报告中描述多样性及复杂否定模式提出解决方案
- 和已有工作的区别：不同于基于规则标注和全模型微调，PromptRad通过提示调优和知识增强的动词化器，在极少标注数据下实现高效多标签分类，且无需额外分类器。
- 阅读启发：知识增强的提示调优能有效缓解医疗领域标注数据稀缺问题，为低资源临床报告自动标注提供可行方案。
- 可信度：high

### 30. VRXU-net: A Deep Learning Approach for Brain Ischemic Stroke Lesion Detection and Segmentation in T1W MRI
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/2605.21633v1
- 一句话贡献：提出一种结合VGG分类器、残差U-Net和多平面聚合的序贯框架，用于T1W MRI中缺血性脑卒中病灶的检测与分割。
- 核心创新点：
  - 将U-Net与残差块结合形成VRU-Net架构
  - 采用改进的VGG模型在2D切片上预分类，仅对阳性切片进行分割以降低计算量
  - 在轴向、矢状、冠状三个平面独立处理并聚合分割结果
  - 利用分割输出反馈优化分类模型，减少假阳性预测
  - 针对T1W MRI中缺血性卒中病灶的自动检测与分割，病灶形状、大小、位置多变且与正常组织对比度低
- 和已有工作的区别：现有方法多直接进行3D分割或2D分割，本文提出先分类后分割的序贯策略，并利用多平面信息聚合，同时引入残差连接改进U-Net结构。
- 阅读启发：该方法通过序贯框架和多平面聚合，在保持较低模型复杂度的同时提升了病灶检测分割的准确性和鲁棒性。
- 可信度：high

### 31. Cardiac fat segmentation using computed tomography and an image-to-image conditional generative adversarial neural network
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/2605.20064v1
- 一句话贡献：提出将图像到图像的条件生成对抗网络pix2pix用于心脏脂肪自动分割，实现了高精度和实时分割。
- 核心创新点：
  - 首次将pix2pix网络应用于心脏脂肪分割任务，而非传统分割网络
  - 利用条件GAN实现端到端的图像到分割掩码的直接映射
  - 网络设计支持实时分割，显著降低运行时间
  - 针对心外膜和纵隔两种脂肪的联合分割，二者由心包膜自然分隔
  - 解决手动分割工作量大、成本高的问题，提供自动化定量分析
- 和已有工作的区别：以往工作多采用传统分割网络或手工特征，本文首次将用于图像翻译的pix2pix条件GAN用于心脏脂肪分割，展现更高的精度和实时性。
- 阅读启发：条件生成对抗网络可有效迁移至医学图像分割任务，尤其是对边界模糊的脂肪组织，具有潜力替代传统分割方法。
- 可信度：high

### 32. RoboSurg-VQA: A Multimodal Benchmark for Surgical Segmentation-Aware Visual Question Answering
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/2605.23068v1
- 一句话贡献：提出了RoboSurg-VQA，首个结合分割感知的视觉问答基准，用于机器人辅助和微创手术场景，通过复用公共分割数据集并设计临床相关问题集与自动标注流程构建。
- 核心创新点：
  - 利用公共手术分割数据集，通过统一的语义模式重新标注，生成带分割感知的VQA数据
  - 采用约束提示（constrained prompting）结合自动有效性检查与一致性校验，再经人工审计，半自动化地扩展标注规模
  - 首次将分割感知任务与视觉问答结合，聚焦手术场景中临床医生提出的程序上下文、可见性、伪影、解剖结构等实际问题
  - 针对手术常见挑战（遮挡、烟雾、出血、镜面高光）下的退化视图设计VQA问题
  - 报告了基准统计信息及多个基线方法的性能，并分析了在挑战性手术条件下的评估困难
- 和已有工作的区别：以往工作要么是纯分割基准，要么是通用VQA基准。RoboSurg-VQA弥合了分割与VQA的鸿沟，专门为手术领域设计，问题集涵盖临床关注点，且标注方法结合了自动化与人工审核。
- 阅读启发：本文提供了一个新的多模态基准，可推动手术场景下细粒度视觉理解与语言交互的研究，并为低质量图像下的VQA评估提供参考。
- 可信度：high

### 33. ImPartial: Multi-channel Whole-Cell Segmentation using Partial Annotations
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/2605.24128v1
- 一句话贡献：提出ImPartial框架，利用稀疏涂鸦标注和自监督多通道量化插补，在低标注条件下实现与全监督相当的细胞分割性能。
- 核心创新点：
  - 引入自监督多通道量化插补目标，避免像素级重建，更适配分割任务
  - 设计稀疏涂鸦标注下的弱监督学习策略，大幅减少标注成本
  - 利用多通道信息进行跨通道自监督学习，提升分割鲁棒性
  - 针对新兴生物成像模态和多通道数据集标注匮乏的问题
  - 在低标注场景（稀疏涂鸦）下追求全监督分割性能
- 和已有工作的区别：现有弱监督方法多依赖像素级重建或大量手工调参，ImPartial通过自监督分类目标替代重建，并利用多通道量化插补，更高效利用稀疏标注。
- 阅读启发：稀疏涂鸦加自监督学习可在细胞分割中大幅降低标注需求，值得在类似低标注场景推广。
- 可信度：high

### 34. Divide-and-Conquer Inference for Large-Scale Visual Recognition with Multimodal Large Language Models
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/2605.24799v1
- 一句话贡献：提出一种无需训练的测试时缩放策略DCI，通过递归分解分类任务并动态剪枝，克服MLLM在长序列推理中的性能崩溃，提升大规模视觉识别精度与速度。
- 核心创新点：
  - 发现并定义MLLM在长序列识别中的性能崩溃现象（Performance Collapse）
  - 从信息论角度揭示性能崩溃源于信息熵与注意力稀释/衰减的冲突
  - 提出Divide-and-Conquer Inference（DCI）递归分解全局分类为多个局部子问题
  - 设计动态剪枝机制压缩搜索空间，提升信噪比并缓解注意力稀释
  - DCI具有更优的扩展行为，加速大规模分类推理
- 和已有工作的区别：现有工作多关注模型架构或训练数据规模，而DCI是首个面向MLLM大规模视觉识别的测试时递归分解与动态剪枝范式，且模型无关即插即用。
- 阅读启发：DCI为MLLM用于大规模识别提供了一种高效、无训练的推理加速与精度提升方案，揭示了长序列性能瓶颈的本质。
- 可信度：high

### 35. What Makes a Medical Checker Trainable? Diagnosing Signal Collapse and Reward Hacking in Checker-Guided RAG for Biomedical QA
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/2605.25988v1
- 一句话贡献：发现医学RAG中NLI检查器的输出分布（而非准确率）决定其是否提供可训练梯度，并识别出信号坍缩和奖励黑客两种训练失败模式。
- 核心创新点：
  - 在GRPO框架下训练医学RAG代理，以NLI检查器作为过程奖励
  - 对比四种NLI后端（LLM log-prob、校准分类器等）作为奖励信号的效果
  - 发现log-prob评分导致97%以上样本中性标签，引发梯度消失
  - 将NLI检查器从验证工具重新定义为RL训练中的过程奖励函数
  - 研究检查器输出分布而非准确率对可训练性的影响
- 和已有工作的区别：现有工作注重检查器准确率或评估指标，本文首次关注其在RL训练中的输出分布特性及对梯度可训练性的决定性作用，并系统揭示奖励黑客现象。
- 阅读启发：设计可训练的检查器奖励时，应避免输出分布过于集中（如中性主导）或过强导致黑客行为，需校准信号强度与策略匹配。
- 可信度：high

### 36. Med-R2: An Adversarial Benchmark for Evidence-Grounded Reasoning in Medical VLMs
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/2605.24492v1
- 一句话贡献：提出了一个层次化的对抗基准Med-R2，系统评估医学视觉语言模型在临床推理中是否真正基于视觉证据，并发现模型依赖提示而非视觉线索，同时验证了逐步微调能提升鲁棒性。
- 核心创新点：
  - 设计了与临床四阶段工作流对齐的层次化逐步QA任务，评估推理链的视觉证据支撑
  - 引入对抗性图像扰动和文本误导，测试模型对欺骗性线索的鲁棒性
  - 构建了包含42,432张图像、31个任务类别和110,406个QA对的大规模基准数据集
  - 首次将医学VLM的推理鲁棒性评估与临床工作流（从初步观察到诊断）紧密结合
  - 明确了现有模型可能依赖虚假先验而非视觉证据的问题，并提供了量化评估方法
- 和已有工作的区别：现有医学VLM基准多关注整体问答准确率，未系统考察推理链的证据基础和对欺骗性线索的脆弱性；Med-R2则从临床工作流出发，通过层次化对抗设计深入评估模型是否真正基于视觉证据。
- 阅读启发：医学VLM在看似准确的回答背后可能依赖捷径，需要专门的对抗鲁棒性评估来推动可信的临床推理发展。
- 可信度：high
