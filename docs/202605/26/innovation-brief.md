# 创新点总结 · 2026-05-26

- 生成时间：2026-05-27 07:29:18 UTC
- 当日论文数：36

## 今日趋势
- 医学视觉语言模型在VQA和分割中的可解释性与证据推理
- 隐私保护与参数高效微调在医疗AI中的实际应用
- 多智能体协作框架提升临床决策的可靠性和审计性
- 鲁棒性基准和对抗性评估推动医疗模型可信部署

## 最值得先读

| 论文 | 推荐理由 |
|---|---|
| [Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence](https://arxiv.org/abs/202605/26/2605.22414v1-towards-clinically-interpretable-ophthalmic-vqa-via-spatially-grounded-lesion-evidence) | 首次提出空间定位病变证据的眼科VQA基准FundusGround，显著提升模型可解释性和准确性。 |
| [MedFM-Robust: Benchmarking Robustness of Medical Foundation Models](https://arxiv.org/abs/202605/26/2605.19027v3-medfm-robust-benchmarking-robustness-of-medical-foundation-models) | 系统构建医疗基础模型鲁棒性基准，揭示LoRA微调导致鲁棒性退化等关键发现，对模型部署有重要指导意义。 |
| [EchoPilot: Training-Free Ultrasound Video Segmentation via Scale-Space Semantic Prompting and Reliability-Gated Memory](https://arxiv.org/abs/202605/26/2605.25944v1-echopilot-training-free-ultrasound-video-segmentation-via-scale-space-semantic-prompting-and-reliability-gated-memory) | 提出无需训练的超声视频分割框架，巧妙组合冻结预训练模型，解决了初始化歧义和漂移问题，为弱监督医学图像分析提供新范式。 |

## 单篇创新点

### 1. Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.22414v1-towards-clinically-interpretable-ophthalmic-vqa-via-spatially-grounded-lesion-evidence
- 一句话贡献：提出了首个具有空间定位病变证据的眼科VQA基准FundusGround，包含10,719张眼底图像、15,595个ETDRS网格标注病变和72,706个多格式问题，实验证明病变级空间证据可提升模型准确性与可解释性。
- 核心创新点：
  - 构建了三阶段标注流水线：图像收集、基于ETDRS网格的病变空间定位、多格式问题生成
  - 采用ETDRS网格将病变标准化映射到9个临床意义视网膜区域，确保解剖一致性
  - 生成四类问题（开放、封闭、单选、多选），覆盖更多临床场景
  - 设计双指标评估体系：答案准确率+病变级推理能力
  - 首次将空间可解释性引入眼科VQA问题设定，要求模型不仅给出答案还需定位病灶证据
- 和已有工作的区别：以往眼科VQA基准仅评估答案准确率，忽略视觉证据；FundusGround强制要求空间化病变定位，并首次引入ETDRS网格标准化标注，使模型推理更符合临床实践。
- 阅读启发：空间化病灶证据是提升眼科VQA可靠性和可解释性的关键，未来工作应重视视觉证据的显式建模。
- 可信度：high

### 2. PrivFusion: A Privacy-preserving Multi-Agent Framework for Harmonizing Distributed Datasets
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24249v1-privfusion-a-privacy-preserving-multi-agent-framework-for-harmonizing-distributed-datasets
- 一句话贡献：提出一个隐私保护的多智能体框架 PrivFusion，自动协调异构分布式数据集的特征对齐，减少联邦学习中人工协调工作。
- 核心创新点：
  - 使用多智能体分析本地数据并聚类语义相似特征
  - 提供迭代转换建议实现数据对齐，无需暴露原始数据
  - 聚焦联邦学习中被忽视的数据协调步骤，提出自动化方案
  - 在四个真实 COVID-19 数据集上验证了有效性和高效性
- 和已有工作的区别：现有工作多关注联邦学习中的模型聚合或差分隐私，而本文首次提出针对训练前数据协调的自动化隐私保护多智能体框架。
- 阅读启发：数据协调是联邦学习中的关键瓶颈，PrivFusion 的自动化方法可显著减少人工干预，提升多机构数据联合建模的可行性。
- 可信度：high

### 3. Parameter-Efficient VLMs for Gastrointestinal Endoscopy: Medical Image Generation and Clinical Visual Question Answering
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24792v1-parameter-efficient-vlms-for-gastrointestinal-endoscopy-medical-image-generation-and-clinical-visual-question-answering
- 一句话贡献：提出双流水线PEFT模型，同时解决胃肠内镜中VQA和隐私保护合成图像生成问题，大幅降低计算成本并提升诊断可靠性。
- 核心创新点：
  - 采用Florence-2 VLM结合PEFT进行临床VQA，显著减少训练计算成本并增强可解释性
  - 利用LoRA微调Stable Diffusion 2.1生成高质量胃肠内镜图像，实现隐私保护的数据增强，计算成本降低约90%
  - 在合成图像评估中引入Frechet BiomedCLIP Distance (FBD)指标，更准确衡量图像-文本语义一致性
  - 首次将参数高效微调（PEFT）统一应用于胃肠内镜的两个关键任务：VQA和生成式数据增强
  - 针对医疗数据隐私严格限制，设计了无需原始数据的合成图像生成方案，绕过隐私壁垒
- 和已有工作的区别：现有工作通常分别处理VQA或图像生成，且多采用全微调或昂贵数据标注；本文首次将PEFT串联两个流水线，在极低计算成本下同时提升两者性能，并专门针对医疗图像生成提出语义对齐评估指标FBD。
- 阅读启发：参数高效微调（PEFT）可有效打破医疗AI中数据与计算瓶颈，双流水线设计为隐私敏感场景提供实用方案，且FBD指标更适用于医学图像合成评估。
- 可信度：high

### 4. Universal Boosts, Specific Suppressors: Sparse Autoencoder Steering of Medical Vision-Language Models
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24977v1-universal-boosts-specific-suppressors-sparse-autoencoder-steering-of-medical-vision-language-models
- 一句话贡献：提出基于稀疏自编码器的解码时残差引导方法，通过因果干预提升方向（通用）和抑制方向（模型特有）减少医学VLM报告幻觉
- 核心创新点：
  - 使用Top-K稀疏自编码器进行逐token残差引导，无需权重更新
  - 结合因果干预同时提升正确特征和抑制错误特征
  - 通过跨模型特征对齐分析揭示提升方向跨架构通用、抑制方向模型特有
  - 将幻觉问题分解为特征提升和特征抑制两个子问题
  - 利用稀疏自编码器的可解释性进行针对性干预
- 和已有工作的区别：现有工作多全模型微调或提示工程，本文首次使用稀疏自编码器进行解码时残差引导，无需训练仅推理时干预，发现通用提升特征和模型特异抑制特征
- 阅读启发：稀疏自编码器可作为无参数干预工具引导模型行为，存在通用提升方向但抑制幻觉需针对模型定制
- 可信度：high

### 5. Towards Reliable Fetal Ultrasound Interpretation with Multi-Agent Collaboration
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.25357v1-towards-reliable-fetal-ultrasound-interpretation-with-multi-agent-collaboration
- 一句话贡献：提出FetUSAgents，一种结合多智能体协作与双路径证据仲裁的胎儿超声解读系统，显著提升了分布外场景下的VQA准确率。
- 核心创新点：
  - 设计多智能体协作框架，通过LLM代理协调多个任务专用视觉工具
  - 引入双路径证据仲裁（DPEA），融合LLM推理性证据与结构化计算证据
  - 构建检索增强的证据库，整合中间发现以支持可追溯的临床结论
  - 将胎儿超声解读从单一任务模型扩展为多智能体协作流程，覆盖从平面识别到诊断报告的完整临床工作流
  - 构建FetUS-VQA基准，包含1892张图像和3205个问答对，覆盖10种临床任务
- 和已有工作的区别：区别于以往‘一个任务一个模型’的孤立范式，本文通过多智能体系统整合视觉感知与临床推理，并利用双路径仲裁机制缓解多模态大模型的领域幻觉。
- 阅读启发：本文展示了通过工具增强的多智能体协作和结构化证据仲裁，能够有效提升医学图像分析中复杂临床任务的可靠性和泛化能力。
- 可信度：high

### 6. EchoPilot: Training-Free Ultrasound Video Segmentation via Scale-Space Semantic Prompting and Reliability-Gated Memory
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.25944v1-echopilot-training-free-ultrasound-video-segmentation-via-scale-space-semantic-prompting-and-reliability-gated-memory
- 一句话贡献：提出了一个无需训练的超声视频分割框架EchoPilot，仅需单次第一帧点击和类别名称，结合尺度空间语义提示和可靠性门控记忆，在多个数据集上达到最优性能。
- 核心创新点：
  - 提出尺度空间语义提示（Scale-Space Semantic Prompting），通过参数自由的S.E.E.D.（Semantic Energy-Entropy Density）准则自动选择最优上下文视图。
  - 从冻结的视觉基础模型（VFM）的密集特征中合成几何精确的辅助点提示，无需额外用户交互。
  - 提出可靠性门控记忆更新（Reliability-Gated Memory），在不确定预测时选择性冻结分割器的记忆库，防止误差累积。
  - 首次构建动态胎儿胎盘超声视频分割数据集，包含671帧标注图像。
  - 在稀疏交互（仅单点点击+类别名）的超声视频分割任务中，无需训练直接使用预训练模型。
- 和已有工作的区别：与现有依赖密集交互或需要任务特定微调的超声分割方法不同，EchoPilot是首个结合冻结的医学视觉语言模型（VLM）和视觉基础模型（VFM）的无训练框架，仅需极稀疏的交互且无需训练即可实现高精度视频分割。
- 阅读启发：本文展示了如何巧妙组合多个冻结的预训练模型（VLM、VFM、视频分割器）并通过零训练的方式解决超声视频分割中的初始化歧义和漂移问题，为医学图像分析中的少交互、无训练方法提供了新思路。
- 可信度：high

### 7. RAPTOR+: A Visually Grounded Vision-Language Framework to Improve Clinical Trust and Auditability in Automated Cancer Referral Processing
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.25956v1-raptor-a-visually-grounded-vision-language-framework-to-improve-clinical-trust-and-auditability-in-automated-cancer-referral-processing
- 一句话贡献：提出RAPTOR+，一个基于视觉语言模型的多模态框架，实现端到端的疑似结直肠癌转诊表单理解，并引入接地感知评估，显著提升证据可追溯性和临床可审计性。
- 核心创新点：
  - 将OCR+LLM流水线替换为端到端VLM（如Qwen3-VL-8B），直接处理半结构化表单，减少对手写和布局变化的敏感性
  - 提出接地感知评估框架，同时度量字段提取准确性和视觉证据定位能力
  - 通过任务特定微调使VLM输出与表单中原有视觉区域对齐，提升严格安全性（Strict Safety）
  - 首次将视觉语言模型全流程应用于癌症紧急转诊处理这一临床操作瓶颈问题
  - 解决了原有系统因依赖OCR而无法保持视觉证据链接、影响审计性的痛点
- 和已有工作的区别：相比原RAPTOR系统（OCR+LLM两阶段），RAPTOR+采用单一VLM端到端处理，无需独立OCR步骤，可直接关联抽取结果与表单中的视觉证据，提升系统鲁棒性和可审计性。
- 阅读启发：在临床文档理解任务中，视觉语言模型的零样本能力不足以支撑可靠证据定位，任务特定微调是实现安全、可审计自动化的关键。
- 可信度：high

### 8. MedFM-Robust: Benchmarking Robustness of Medical Foundation Models
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.19027v3-medfm-robust-benchmarking-robustness-of-medical-foundation-models
- 一句话贡献：构建了首个针对医疗基础模型鲁棒性的系统基准，包含40种扰动（12种通用+28种医学特有）覆盖8种成像模态，评估5个VLM和2个分割模型及5种微调策略。
- 核心创新点：
  - 提出包含40种扰动类型的医疗模型鲁棒性基准，其中28种为医学领域特有扰动
  - 系统评估VLM在VQA、视觉定位和描述三类任务上的鲁棒性
  - 比较5种微调策略（全微调、LoRA、Adapter等）对分割模型鲁棒性的影响
  - 发现LoRA微调导致近两倍于全微调的鲁棒性退化
  - 填补医疗基础模型在真实世界扰动下鲁棒性评估的空白
- 和已有工作的区别：现有工作多评估通用模型在标准噪声下的鲁棒性，本文聚焦医疗领域，构建领域特定扰动集，并系统比较多种任务和微调策略，为部署提供可操作指南。
- 阅读启发：医疗AI部署时微调策略选择至关重要，LoRA虽高效但鲁棒性差，推荐全微调或Adapter；医学特定扰动评估不可替代通用噪声测试；不同任务鲁棒性差异显著，需根据应用场景选择模型。
- 可信度：high

### 9. PromptRad: Knowledge-Enhanced Multi-Label Prompt-Tuning for Low-Resource Radiology Report Labeling
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.20052v1-promptrad-knowledge-enhanced-multi-label-prompt-tuning-for-low-resource-radiology-report-labeling
- 一句话贡献：提出PromptRad，利用知识增强的多标签提示调优，将多标签分类转化为掩码语言建模并整合UMLS同义词，仅需32个标注样本即可在低资源放射学报告标注中超越字典法和微调基线，性能与GPT-4相当。
- 核心创新点：
  - 将多标签分类任务重新构造为掩码语言建模，无需额外分类层。
  - 设计多词词汇表，利用UMLS Metathesaurus中的同义词丰富类别表示。
  - 在低资源设置下微调预训练语言模型，仅需少量标注数据。
  - 聚焦低资源放射学报告标注场景，解决数据稀缺问题。
  - 同时处理多标签分类，适应临床文本中多种发现共存的现实。
- 和已有工作的区别：现有基于规则的方法难以处理多样化描述，传统微调需要大量标注数据，而PromptRad通过提示调优和知识增强大大降低了对标注数据的依赖。
- 阅读启发：提示调优结合领域知识（如UMLS）是解决医学文本低资源标注问题的有效途径。
- 可信度：high

### 10. RoboSurg-VQA: A Multimodal Benchmark for Surgical Segmentation-Aware Visual Question Answering
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.23068v1-robosurg-vqa-a-multimodal-benchmark-for-surgical-segmentation-aware-visual-question-answering
- 一句话贡献：提出了首个融合手术分割感知的视觉问答基准RoboSurg-VQA，通过重用公共分割数据集和约束提示自动生成答案，覆盖临床相关的多维度问题。
- 核心创新点：
  - 构建了分割感知的VQA基准，每帧配有一组固定临床问题，涵盖程序上下文、解剖结构、图像质量等。
  - 利用约束提示自动生成候选答案，并设计有效性和一致性检查，再经人工审计提高准确性。
  - 通过共享模式重用多个公共手术分割数据集，统一标注格式，实现多任务联合。
  - 首次将VQA任务与手术分割感知结合，回答临床语境下的语言问题。
  - 聚焦手术中常见的退化视图（遮挡、烟雾、出血等）下的视觉问答能力。
- 和已有工作的区别：现有手术VQA基准多基于通用图像或简单问答，缺乏对分割感知（如区域、空间关系）和临床退化视图的针对性设计；本文首次将分割标签与临床VQA问题系统关联。
- 阅读启发：RoboSurg-VQA为手术视觉理解提供了更贴近临床实践的评估平台，推动VQA模型在复杂手术场景中的鲁棒性研究。
- 可信度：high

### 11. What Makes a Medical Checker Trainable? Diagnosing Signal Collapse and Reward Hacking in Checker-Guided RAG for Biomedical QA
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.25988v1-what-makes-a-medical-checker-trainable-diagnosing-signal-collapse-and-reward-hacking-in-checker-guided-rag-for-biomedical-qa
- 一句话贡献：发现训练过程中检查器的输出分布（而非准确率）决定其提供可训练梯度的能力，并诊断了信号坍缩和奖励破解两种故障模式。
- 核心创新点：
  - 比较四种NLI检查器后端（LLM log-prob、MedNLI等）作为GRPO训练奖励
  - 发现LLM log-prob导致97%以上标签中性（信号坍缩）
  - 揭示强信号触发三步奖励破解级联（超短回答、避免搜索、语言崩溃）
  - 适度信号的MedNLI分类器训练出更高性能模型（+12% BERTScore，无GPT依赖）
  - 发现信号强度具有策略依赖性
- 和已有工作的区别：以往研究注重检查器的准确率或校准，本文发现训练中输出分布才是关键，且强信号会反直觉地导致性能下降。
- 阅读启发：设计基于检查器奖励的RAG系统时，应优先选择输出分布非退化、信号强度适中的检查器，并警惕信号坍缩和奖励破解。
- 可信度：high

### 12. BalanceRAG: Joint Risk Calibration for Cascaded Retrieval-Augmented Generation
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.20084v1-balancerag-joint-risk-calibration-for-cascaded-retrieval-augmented-generation
- 一句话贡献：提出BalanceRAG，通过二维网格上的序列图检验联合校准级联RAG中LLM-only和RAG分支的不确定性阈值，在控制系统级错误率的同时保留更多样本，并可扩展至多风险校准以限制检索使用量。
- 核心创新点：
  - 将两个分支的不确定性阈值对视为二维网格上的操作点，通过序列图检验识别安全操作点，实现联合风险校准
  - 支持多风险校准，同时控制选择条件风险与检索使用量
  - 风险自适应阈值校准，在满足系统级错误率前提下最大化覆盖率和正确样本数
  - 针对级联RAG系统中逐阶段校准过于保守的问题，首次提出联合不确定性阈值校准方法
  - 将级联RAG的校准问题形式化为在二维阈值空间中寻找安全操作点
- 和已有工作的区别：现有级联RAG校准方法对LLM-only和RAG分支分别设置阈值（逐阶段），导致保守；BalanceRAG联合考虑两个分支的不确定性，通过二维网格序列图检验在相同风险水平下保留更多样本，并支持多风险目标约束检索使用。
- 阅读启发：BalanceRAG提供了一种风险可控的级联RAG部署方式，可以在不牺牲太多准确性的情况下显著降低检索开销，适用于对成本和事实性有平衡要求的场景。
- 可信度：high

### 13. VRXU-net: A Deep Learning Approach for Brain Ischemic Stroke Lesion Detection and Segmentation in T1W MRI
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.21633v1-vrxu-net-a-deep-learning-approach-for-brain-ischemic-stroke-lesion-detection-and-segmentation-in-t1w-mri
- 一句话贡献：提出VRXU-net，结合改进VGG检测、带残差块的U形分割与三平面聚合，并引入预分类器减少非病变切片处理，在T1W MRI缺血性脑卒中病灶检测分割上取得优于现有方法的准确率和Dice系数。
- 核心创新点：
  - 提出VRXU-net架构，融合视觉特征、残差连接和U型网络
  - 采用改进VGG模型先对2D切片进行病灶检测，再用带残差块的U形网络分割
  - 分别处理轴向、矢状、冠状三个解剖平面并将分割结果聚合
  - 引入高性能预分类器，在分割前滤除非病变切片，降低计算复杂度并提升准确率
  - 利用分割输出反馈优化分类模型，减少假阳性预测
- 和已有工作的区别：现有方法多直接对3D图像进行端到端分割，或仅使用单一平面信息；本工作创新性地将检测与分割分离，先通过轻量级分类器筛选切片，再对三个正交平面分别分割并聚合，既提高效率又增强准确性。
- 阅读启发：分离检测与分割、多平面信息融合以及预分类策略可有效解决病灶形态多变、对比度低的脑卒中病变分割难题。
- 可信度：high

### 14. ImPartial: Multi-channel Whole-Cell Segmentation using Partial Annotations
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24128v1-impartial-multi-channel-whole-cell-segmentation-using-partial-annotations
- 一句话贡献：提出ImPartial框架，利用稀疏涂鸦标注和自监督多通道量化插值，在仅需部分标注的情况下实现与全监督模型相当的细胞分割性能。
- 核心创新点：
  - 引入自监督多通道量化插值（self-supervised multi-channel quantized imputation）作为辅助任务
  - 放弃像素级完美重建/去噪，改用分类目标对齐分割任务
  - 在多重成像和可变通道配置的低标注场景下使用稀疏scribble标注
  - 针对新兴生物成像模态和多重数据集（可变通道配置）中标注稀缺的问题
  - 定义在低标注（partial annotation）条件下实现全监督级别分割的任务
- 和已有工作的区别：现有方法需要密集像素级标注或依赖图像重建/去噪，而ImPartial通过自监督量化插值避免不必要重建，直接优化分割目标，且适用于多通道可变配置。
- 阅读启发：部分标注结合精心设计的自监督任务可大幅降低细胞分割的标注成本，同时保持高性能，适用于多模态成像场景。
- 可信度：high

### 15. Med-R2: An Adversarial Benchmark for Evidence-Grounded Reasoning in Medical VLMs
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24492v1-med-r2-an-adversarial-benchmark-for-evidence-grounded-reasoning-in-medical-vlms
- 一句话贡献：提出了一个层级化、对抗性的医学视觉语言模型证据推理基准（Med-R2），模拟临床工作流评估模型的视觉证据依赖性和鲁棒性。
- 核心创新点：
  - 设计了与临床四阶段（检查、诊断、治疗、预后）对齐的层级化问答任务，严格评估推理链对视觉证据的依赖
  - 在图像和文本上施加对抗扰动，测试模型对误导性线索的鲁棒性
  - 构建了大规模数据集（42,432张图像、31个任务类别、110,406个QA对）
  - 提出层级微调策略，利用分级数据显著提升推理鲁棒性
  - 首次聚焦医学VLM推理是否基于视觉证据而非虚假先验，并设计专门基准进行量化评估
- 和已有工作的区别：现有医学VLM基准多关注整体问答准确率，缺乏对推理过程是否基于视觉证据的细粒度评估；本工作首次引入层级化对抗性评估，直接测试模型对误导信息的抵抗能力和证据依赖程度。
- 阅读启发：医学VLM在临床推理中易受虚假先验影响，需要更严格的证据基础评估；提出的Med-R2基准和层级微调方法为提升模型鲁棒性和可信度提供了有效工具。
- 可信度：high

### 16. Thinking in Scales: Accelerating Gigapixel Pathology Image Analysis via Adaptive Continuous Reasoning
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.19491v2-thinking-in-scales-accelerating-gigapixel-pathology-image-analysis-via-adaptive-continuous-reasoning
- 一句话贡献：提出PathCTM模型，通过自适应连续推理实现从低倍到高倍动态尺度转换和早期停止，大幅减少全切片图像分析的计算开销，同时保持诊断精度。
- 核心创新点：
  - 将诊断推理建模为动态序列信息追踪，从低倍全局到高倍局部渐进式过渡
  - 条件计算机制实现动态尺度切换，结合注意力引导的无关区域自动剪枝
  - 置信度感知的早期停止策略，在不确定性有效约束时终止推理
  - 挑战传统MIL方法在全切片图像分析中固定的高倍处理范式，提出尺度空间连续推理新设定
  - 在多个病理数据集上，相比标准MIL方法减少95.95%所需图像块和95.62%推理时间，AUC无下降
- 和已有工作的区别：现有MIL方法对所有区域均采用高倍率处理，计算冗余；PathCTM则根据诊断需求动态调整分辨率，并通过早期停止避免无效计算。
- 阅读启发：PathCTM表明，通过模拟医生逐步聚焦的推理过程，可以在不牺牲精度的前提下将全切片分析效率提升约20倍。
- 可信度：high

### 17. Cardiac fat segmentation using computed tomography and an image-to-image conditional generative adversarial neural network
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.20064v1-cardiac-fat-segmentation-using-computed-tomography-and-an-image-to-image-conditional-generative-adversarial-neural-network
- 一句话贡献：首次将条件生成对抗网络(pix2pix)应用于心脏CT图像中心外膜和纵隔脂肪的自动分割，实现了高精度和实时性能。
- 核心创新点：
  - 采用pix2pix网络架构进行图像到图像的翻译任务，实现心脏脂肪的自动分割
  - 该方法不需要预先训练的分割模型，直接通过条件GAN学习分割映射
  - 针对心外膜和纵隔脂肪两种类型进行联合分割，两者由心包膜分隔
  - 将本非为分割设计的pix2pix网络成功应用于医学图像分割任务
  - 心外膜脂肪分割平均准确率99.08%，F1分数98.73
- 和已有工作的区别：与现有心脏脂肪分割方法相比，该方法在F1分数和运行时间上均表现更优，且能同时分割两种脂肪。
- 阅读启发：条件生成对抗网络在心脏脂肪分割中具有巨大潜力，可作为高效、准确的自动分割工具。
- 可信度：high

### 18. Divide-and-Conquer Inference for Large-Scale Visual Recognition with Multimodal Large Language Models
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24799v1-divide-and-conquer-inference-for-large-scale-visual-recognition-with-multimodal-large-language-models
- 一句话贡献：提出分而治之推理（DCI）方法，通过递归分解任务和动态剪枝，解决多模态大语言模型在大规模分类中的性能崩溃问题，实现无训练即插即用的测试时扩展。
- 核心创新点：
  - 提出DCI递归分解全局分类任务为多个局部子问题，并动态剪枝搜索空间
  - 揭示了长序列推理中注意力稀释和衰减导致性能崩溃的信息论原因
  - 实现了更优的复杂度扩展行为，加速推理过程
  - 首次定义并分析多模态大语言模型在长序列识别中的性能崩溃现象
  - 将测试时扩展策略应用于大规模视觉识别，无需额外训练
- 和已有工作的区别：此前工作主要集中于模型训练或微调，而DCI是一种模型无关的测试时推理策略，不修改模型参数，通过分治和剪枝提升长序列分类性能。
- 阅读启发：DCI为多模态大模型在大规模分类任务中提供了一种高效、即插即用的性能提升方法，且无需重新训练。
- 可信度：high

### 19. Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.22414v1
- 一句话贡献：提出FundusGround基准，通过空间定位的病灶证据增强眼科VQA的临床可解释性。
- 核心创新点：
  - 构建三阶段管道采集10719张眼底图像并标注15595个病灶
  - 采用ETDRS网格将病灶标准化映射到9个临床视网膜区域
  - 生成四种格式（开放、封闭、单选、多选）共72706个问题
  - 设计双指标评估答案准确性和病灶级推理
  - 现有眼科VQA基准忽略视觉证据用于解释性，本文通过空间定位病灶弥补
- 和已有工作的区别：以往眼科VQA仅关注答案准确性，本文首次引入空间定位病灶作为可解释性依据。
- 阅读启发：明确的空间病灶定位对于可靠和可解释的眼科VQA至关重要。
- 可信度：high

### 20. PrivFusion: A Privacy-preserving Multi-Agent Framework for Harmonizing Distributed Datasets
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.24249v1
- 一句话贡献：提出一个隐私保护的多智能体框架，在联邦学习前自动协调异构结构化数据集，减少手动工作。
- 核心创新点：
  - 使用本地智能体分析数据隐私，跨站点聚类语义相似特征
  - 迭代生成转换建议直至数据对齐
  - 将数据协调与联邦学习分离，作为预处理步骤
  - 关注联邦学习中常被忽略的数据协调问题
  - 针对多站点结构化数据异质性提出自动化协调方案
- 和已有工作的区别：现有联邦学习工作假设数据已协调或需要手动处理，本工作首次自动化隐私保护的数据协调。
- 阅读启发：联邦学习前的数据协调可以通过多智能体框架自动且隐私保护地完成，提升模型训练效果。
- 可信度：high

### 21. Parameter-Efficient VLMs for Gastrointestinal Endoscopy: Medical Image Generation and Clinical Visual Question Answering
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.24792v1
- 一句话贡献：提出双管道PEFT框架，同时解决内窥镜视觉问答和隐私保护合成数据生成，显著降低计算成本并提升性能。
- 核心创新点：
  - 采用Florence-2结合PEFT进行内窥镜视觉问答，增强可解释性并降低训练成本
  - 使用LoRA对Stable Diffusion 2.1进行微调，生成高质量内窥镜图像，实现隐私保护数据增强
  - 双管道架构同时处理VQA和合成图像生成两个任务
  - 首次将参数高效微调(PEFT)同时应用于内窥镜VQA和医学图像生成
  - 解决内窥镜AI中数据标注不足、隐私限制和传统微调瓶颈三大问题
- 和已有工作的区别：相比单独使用全微调或传统生成模型，本工作通过PEFT统一了VQA和图像生成，在更低计算成本下实现了更好的图像-文本一致性（FBD更低）。
- 阅读启发：PEFT（特别是LoRA）可有效应用于医学内窥镜领域，同时提升VQA准确率和合成数据质量，为隐私保护和资源受限场景提供可行方案。
- 可信度：high

### 22. Universal Boosts, Specific Suppressors: Sparse Autoencoder Steering of Medical Vision-Language Models
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.24977v1
- 一句话贡献：提出基于稀疏自编码器的解码时残差引导方法，无需权重更新即可有效抑制医学视觉语言模型的幻觉，并发现质量提升方向跨模型通用而抑制方向模型特定。
- 核心创新点：
  - 在解码时对每个token的稀疏自编码器进行残差引导，结合后层Top-K SAE和因果引导
  - 推理时组合抑制与增强干预，无需重新训练模型
  - 跨模型特征对齐揭示质量提升方向可迁移、抑制方向需针对每个主干单独处理
  - 针对医学视觉语言模型生成报告时的幻觉问题（捏造、遗漏、定位错误），提出无需权重更新的推理时干预方法
  - 在MIMIC-CXR上对三个模型（RadVLM、LLaVA-Rad、CheXOne）临床综合指标相对提升5.4%~17.0%
- 和已有工作的区别：现有方法多需微调或额外训练，本文首次利用稀疏自编码器在解码时进行残差引导，无需权重更新即可抑制幻觉，并发现可迁移性与特异性在不同方向上的分布差异。
- 阅读启发：医学视觉语言模型的幻觉可通过推理时稀疏自编码器引导有效缓解，且促进质量的特征可跨模型迁移，但抑制特征需针对模型定制，为零样本跨模型干预提供了新思路。
- 可信度：high

### 23. Towards Reliable Fetal Ultrasound Interpretation with Multi-Agent Collaboration
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.25357v1
- 一句话贡献：提出FetUSAgents多智能体系统，通过工具协作与双路径证据仲裁实现可靠、可追溯的胎儿超声全流程自动解释。
- 核心创新点：
  - 设计多智能体协作框架，协调任务特定视觉工具（如分割、测量）完成复杂临床查询。
  - 提出Dual-Path Evidence Arbitration (DPEA)，融合LLM的推理证据与视觉工具的量化计算结果。
  - 构建检索增强证据库，存储中间发现并支持临床结论的溯源。
  - 开源FetUS-VQA基准：包含1892张图像和3205个问答对，覆盖10项临床任务。
  - 首次将多智能体系统用于胎儿超声全流程（从平面识别到报告生成），突破“一个任务一个模型”的孤立范式。
- 和已有工作的区别：与依赖单一多模态大模型的端到端方法不同，本工作通过多智能体解耦任务，将LLM的推理能力与专用视觉工具的精确计算结合，并引入证据仲裁机制确保结论可追溯、减少幻觉。
- 阅读启发：本文展示了一种构建可靠临床AI辅助系统的可扩展路线：用小模型工具保证基础能力，用多智能体协作实现复杂推理，并用证据库和仲裁机制增强可信度。
- 可信度：high

### 24. EchoPilot: Training-Free Ultrasound Video Segmentation via Scale-Space Semantic Prompting and Reliability-Gated Memory
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.25944v1
- 一句话贡献：提出EchoPilot，一种无需训练的超声视频分割框架，仅需单一点击和类别名称，通过尺度空间语义提示和可靠性门控记忆实现高性能。
- 核心创新点：
  - Scale-Space Semantic Prompting：提出S.E.E.D.准则自动选择最优上下文视图，并从基础特征合成几何精确的辅助点提示。
  - Reliability-Gated Memory：根据预测不确定性选择性冻结记忆库，防止错误累积和时序漂移。
  - 在
  - 稀
  - 疏
- 和已有工作的区别：现有方法直接部署可提示基础模型不可靠（单点尺度不足、贪心记忆导致漂移），EchoPilot通过自动多尺度提示和门控记忆机制克服这些局限。
- 阅读启发：展示了如何有效组合冻结的VLMs和VFMs实现无需训练的鲁棒超声视频分割，为弱监督医学图像分析提供新思路。
- 可信度：high

### 25. RAPTOR+: A Visually Grounded Vision-Language Framework to Improve Clinical Trust and Auditability in Automated Cancer Referral Processing
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.25956v1
- 一句话贡献：提出RAPTOR+，一个基于视觉语言模型的端到端框架，用于半结构化癌症转诊文档的理解，实现提取决策与视觉证据的链接，提升临床信任和可审计性。
- 核心创新点：
  - 使用视觉语言模型（VLM）替代OCR+LLM分离架构，实现端到端文档理解
  - 引入grounding-aware评估框架，同时衡量提取准确性和证据定位能力
  - 解决原RAPTOR系统因OCR分离对手写、布局变化敏感及丢失视觉证据链接的问题
  - 微调后的Qwen3-VL-8B在阅读准确率（96.1%）和严格安全性（60.6%）上显著优于零样本模型及原始OCR流水线
- 和已有工作的区别：原RAPTOR使用LLM+OCR两步处理，而RAPTOR+采用VLM端到端处理，并实现提取结果到视觉证据的可追溯链接。
- 阅读启发：任务特定微调对于构建可靠、可审计的临床文档理解系统至关重要，尤其是需要证据追溯的场景。
- 可信度：high

### 26. MedFM-Robust: Benchmarking Robustness of Medical Foundation Models
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/2605.19027v3
- 一句话贡献：系统性构建了医学基础模型鲁棒性基准，揭示了微调策略、医学特定扰动等关键因素对模型鲁棒性的影响。
- 核心创新点：
  - 提出包含40种扰动类型（12种基础+28种医学特定）的鲁棒性基准
  - 在8种成像模态上评估5个VLM和2个分割模型
  - 系统比较多种微调策略（全微调、LoRA、Adapter等）
  - 聚焦医学基础模型在真实世界扰动下的鲁棒性评估，以往未充分探讨
  - LoRA微调退化接近全微调两倍
- 和已有工作的区别：与仅评估标准精度的工作不同，本工作系统评估了多种扰动类型和任务，并给出部署指南。
- 阅读启发：部署医学基础模型时，应优先考虑全微调或Adapter（而非LoRA），并针对医学特定扰动进行鲁棒性测试；通用VLM在VQA上准确度高但视觉定位能力弱。
- 可信度：high

### 27. BalanceRAG: Joint Risk Calibration for Cascaded Retrieval-Augmented Generation
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/2605.20084v1
- 一句话贡献：提出BalanceRAG，通过二维格点序贯图形测试实现级联RAG系统中LLM-only和RAG两支路的联合风险校准，在控制错误率的同时提高覆盖率并减少不必要的检索。
- 核心创新点：
  - 将每个阈值对视为二维格点上的操作点，使用序贯图形测试识别安全操作点
  - 实现风险自适应的阈值校准，控制系统级错误率
  - 扩展到多风险校准，可以同时约束检索使用率和选择条件风险
  - 针对级联RAG中逐阶段校准过于保守的问题，提出联合风险校准框架
  - 将LLM-only和RAG的不确定性阈值进行联合优化，而非独立设置
- 和已有工作的区别：现有工作通常级联地逐阶段校准阈值，忽略联合效应对最终效用的影响；BalanceRAG首次联合校准两个分支的阈值，通过二维格点搜索和序贯测试实现风险控制。
- 阅读启发：联合校准两级不确定性阈值可以有效平衡风险、覆盖率和检索成本，为级联RAG系统提供实用的风险可控方案。
- 可信度：high

### 28. Thinking in Scales: Accelerating Gigapixel Pathology Image Analysis via Adaptive Continuous Reasoning
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/2605.19491v2
- 一句话贡献：提出PathCTM，通过自适应连续推理和条件计算，在保持诊断精度的同时将WSI分析所需图像块减少95.95%，推理时间缩短95.62%。
- 核心创新点：
  - 提出动态序贯信息追求机制，从低倍全局到高倍局部渐进式推理
  - 采用条件计算实现动态尺度切换，并耦合注意力引导的区域剪枝
  - 引入置信度感知的早期停止策略，在不确定性充分降低时终止推理
  - 将WSI诊断重新定义为可动态终止的序贯信息追求问题
  - 突破传统MIL方法需穷举处理所有高倍率图像块的限制
- 和已有工作的区别：传统方法固定使用最高倍率所有块，而PathCTM自适应地在低倍率上快速筛选区域，仅在高倍率处理关键位置，实现了数量级的计算节省。
- 阅读启发：PathCTM展示了通过动态推理路径设计，可以显著提升千兆像素病理图像分析的效率，同时不牺牲准确性。
- 可信度：high

### 29. PromptRad: Knowledge-Enhanced Multi-Label Prompt-Tuning for Low-Resource Radiology Report Labeling
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/2605.20052v1
- 一句话贡献：提出PromptRad，一种结合UMLS知识增强的多标签提示调优方法，在低资源场景下仅需少量标注样本即可高效完成放射学报告标注。
- 核心创新点：
  - 将多标签分类重构为掩码语言建模任务，利用提示调优无需额外分类层
  - 从UMLS Metathesaurus中提取同义词构建多词verbalizer，丰富类别语义表示
  - 在仅32个标注样本下微调预训练语言模型，显著降低标注数据需求
  - 聚焦低资源放射学报告标注，解决规则方法和传统微调在数据稀缺时性能不佳的问题
  - 将临床同义词知识引入提示学习，提升类别表示的鲁棒性
- 和已有工作的区别：相比规则方法（依赖固定模式）和全微调（需大量标注数据），PromptRad通过知识增强提示调优在极低资源下取得突破，且不增加模型复杂度。
- 阅读启发：PromptRad展示了知识增强提示调优在医疗文本少样本标注中的有效性，为数据稀缺的临床场景提供了实用方案。
- 可信度：high

### 30. VRXU-net: A Deep Learning Approach for Brain Ischemic Stroke Lesion Detection and Segmentation in T1W MRI
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/2605.21633v1
- 一句话贡献：提出VRXU-net，通过两阶段分类-分割框架结合三平面聚合实现T1W MRI中脑缺血中风病变的精准检测与分割。
- 核心创新点：
  - 先使用改进的VGG模型对2D切片进行缺血性卒中分类，再通过带有残差块的U型网络分割病变，形成顺序处理流程
  - 对轴向、矢状、冠状三个解剖平面独立处理并聚合结果，利用多平面信息提升定位准确性
  - 在分割前加入高性能分类器，减少对非病变切片的不必要分割，提高整体处理速度和精度
  - 针对T1W MRI中缺血性卒中病变形状、大小、位置多变且与周围组织灰度相似难以分割的问题
  - 将3D图像分解为2D切片处理，降低模型复杂度同时保留三维空间信息
- 和已有工作的区别：现有方法通常直接进行3D分割或使用单一平面2D分割，而该方法通过两阶段（先分类后分割）和多平面聚合，结合残差块与VGG改进，并利用分割结果反馈优化分类，实现了更高效准确的检测。
- 阅读启发：一种结合分类与分割、多平面聚合的端到端深度学习框架，有效提升缺血性中风病灶在T1W MRI中的检测和分割性能。
- 可信度：high

### 31. Cardiac fat segmentation using computed tomography and an image-to-image conditional generative adversarial neural network
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/2605.20064v1
- 一句话贡献：提出将pix2pix条件生成对抗网络应用于心脏CT图像中心外膜和纵隔脂肪的全自动分割，实现高精度和实时分割。
- 核心创新点：
  - 首次将原本用于图像到图像翻译的pix2pix网络用于心脏脂肪分割任务
  - 实现心外膜脂肪和纵隔脂肪两种类型脂肪的同时自动分割与量化
  - 分割速度达到实时，显著优于传统方法
  - 针对心脏脂肪分割中手动标注工作量大、耗时长的问题，提出全自动深度学习解决方案
  - 关注两种 spatially separated 的脂肪类型（心外膜和纵隔），并分别评估性能
- 和已有工作的区别：现有研究多采用传统分割网络如U-Net等，本文首次将条件生成对抗网络pix2pix应用于心脏脂肪分割，且能同时处理两种脂肪类型，并实现了实时分割速度。
- 阅读启发：pix2pix网络可有效迁移到医学图像分割任务中，尤其适合边界模糊的心脏脂肪区域，为临床自动化脂肪定量提供新思路。
- 可信度：high

### 32. RoboSurg-VQA: A Multimodal Benchmark for Surgical Segmentation-Aware Visual Question Answering
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/2605.23068v1
- 一句话贡献：提出了RoboSurg-VQA，一个结合手术分割感知的视觉问答基准，通过复用公共分割数据集并引入临床相关固定问题集与自动化标注管道，推动手术视觉理解评估。
- 核心创新点：
  - 将公共手术分割数据集重新标注为VQA格式，实现分割与问答的跨任务整合
  - 设计了一套包含程序上下文、解剖结构、图像质量等6类临床问题的固定问答框架
  - 采用约束提示生成候选答案，结合自动有效性检查和人工审核的标注流程
  - 首次定义‘分割感知’的VQA任务，要求模型在回答问题时同时理解分割掩码和视觉内容
  - 覆盖手术中常见的退化条件（遮挡、烟雾、出血等），挑战模型在恶劣场景下的鲁棒性
- 和已有工作的区别：不同于以往手术VQA数据集（如EndoVis-18-VQA）仅关注单一任务或缺乏分割信息，本工作系统性地融合分割标签与临床相关问答，并针对手术特有退化场景设计评估。
- 阅读启发：认识到构建手术VQA基准需要兼顾临床问题实用性、分割感知能力以及多模态标注的扩展性，本文提供了一个可复用的范式。
- 可信度：high

### 33. ImPartial: Multi-channel Whole-Cell Segmentation using Partial Annotations
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/2605.24128v1
- 一句话贡献：提出ImPartial框架，利用自监督多通道量化插补从稀疏涂鸦和有限标注中实现与全监督相当的多通道细胞分割。
- 核心创新点：
  - 引入自监督多通道量化插补目标，代替像素级重建，与分割目标更一致
  - 在多通道可变配置下利用稀疏涂鸦进行弱监督分割
  - 集成量化插补与分割任务，降低标注需求
  - 针
  - 对
- 和已有工作的区别：现有方法通常依赖密集像素标注或复杂重建，本文通过自监督量化插补避免不必要的重建，更高效地利用稀疏标注。
- 阅读启发：在标注资源有限的多通道细胞分割任务中，可采用自监督量化插补策略，显著减少标注成本而不牺牲精度。
- 可信度：high

### 34. Divide-and-Conquer Inference for Large-Scale Visual Recognition with Multimodal Large Language Models
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/2605.24799v1
- 一句话贡献：提出Divide-and-Conquer Inference (DCI)测试时缩放策略，通过递归分解分类任务和动态剪枝，解决MLLMs在大规模分类中的性能崩溃问题，无需额外训练即可提升精度和速度。
- 核心创新点：
  - 揭示Performance Collapse现象，从信息论角度归因于注意力稀释和衰减导致信噪比下降
  - 提出递归分解全局分类为局部子问题的分治推理框架
  - 设计动态剪枝机制压缩搜索空间，改善局部信噪比
  - 实现更优的推理复杂度缩放，避免传统自注意力的二次复杂度
  - 首次系统研究MLLMs在大规模标签空间分类时的性能退化问题
- 和已有工作的区别：现有工作主要关注模型架构或训练改进，而DCI是一种模型无关的测试时推理策略，通过分治和剪枝应对长序列注意力瓶颈，且不依赖额外训练或微调。
- 阅读启发：DCI为大规模视觉识别提供了一种高效、即插即用的推理增强方法，揭示了注意力机制在长序列下的根本限制并给出实用解决方案。
- 可信度：high

### 35. What Makes a Medical Checker Trainable? Diagnosing Signal Collapse and Reward Hacking in Checker-Guided RAG for Biomedical QA
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/2605.25988v1
- 一句话贡献：发现医疗核查器在训练中的输出分布（而非保留准确率）决定其是否提供可训练梯度，并诊断出信号坍缩和奖励黑客两种失败模式。
- 核心创新点：
  - 系统比较四种NLI检查器作为GRPO训练医疗RAG智能体的过程奖励
  - 提出信号强度概念并发现中等信号比强信号更优
  - 首次在医疗RAG的强化学习训练中系统分析检查器输出分布的影响
  - 揭示检查器信号强度与策略的依赖关系
  - 发现LLM对数概率评分导致超过97%的claim被判为中性，造成梯度坍塌
- 和已有工作的区别：以往工作关注检查器的准确率，本文发现训练中的输出分布和信号强度才是关键，且强信号反而导致奖励黑客。
- 阅读启发：训练可用的检查器需避免信号坍缩并保持适度信号强度，设计验证器-as-奖励系统应考虑边界条件。
- 可信度：high

### 36. Med-R2: An Adversarial Benchmark for Evidence-Grounded Reasoning in Medical VLMs
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/2605.24492v1
- 一句话贡献：提出了Med-R2 Bench，一个分层对抗性基准，用于评估医学视觉语言模型在临床推理中是否真正基于视觉证据，而非虚假的先验知识。
- 核心创新点：
  - 设计了与临床工作流对齐的分层分步QA任务，覆盖四个临床阶段
  - 引入对抗性扰动（如误导性文本/图像线索）测试模型鲁棒性
  - 构建了大规模数据集（42,432图像、31任务、110,406 QA对）
  - 首次将医学VLM的推理过程分解为临床工作流中的四个阶段进行逐级评估
  - 关注证据基础推理（evidence-grounded reasoning）而非单纯问答准确性
- 和已有工作的区别：现有医学VLM基准主要评估整体问答精度，而Med-R2 Bench专门测试模型是否基于视觉证据进行逐步推理，而非利用统计捷径或虚假关联。
- 阅读启发：医学VLM在证据基础推理上存在明显脆弱性，通过分层对抗性训练可以改善，未来研究应关注推理过程的可解释性和鲁棒性。
- 可信度：high
