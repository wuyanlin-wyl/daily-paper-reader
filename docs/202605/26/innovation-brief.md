# 创新点总结 · 2026-05-26

- 生成时间：2026-05-27 07:54:40 UTC
- 当日论文数：36

## 今日趋势
- 医学视觉语言模型（VQA）与可解释性：多篇工作聚焦于通过空间定位、证据基础、多智能体协作等提升VQA的可靠性与临床可用性。
- 参数高效与低资源学习：利用PEFT、LoRA、提示调优等方法降低计算和数据需求，推动医学AI在资源受限场景的应用。
- 隐私保护与数据协调：联邦学习框架与多智能体数据协调，实现分布式医疗数据的安全对齐。
- 鲁棒性与基准：系统构建针对医学基础模型鲁棒性的基准，涵盖领域特定扰动和多种模态。
- 无需训练或推理时干预：通过稀疏自编码器引导、分而治之推理等创新，实现轻量级性能提升。

## 最值得先读

| 论文 | 推荐理由 |
|---|---|
| [Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence](https://arxiv.org/abs/202605/26/2605.22414v1-towards-clinically-interpretable-ophthalmic-vqa-via-spatially-grounded-lesion-evidence) | 该论文提出了FundusGround基准，通过ETDRS网格空间定位病变证据，实现临床可解释的眼科VQA，为医学VQA的可解释性提供了关键框架和高质量数据集，具有重要的基准价值和临床意义。 |

## 单篇创新点

### 1. Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.22414v1-towards-clinically-interpretable-ophthalmic-vqa-via-spatially-grounded-lesion-evidence
- 一句话贡献：提出FundusGround基准，通过ETDRS网格空间定位病变证据，实现临床可解释的眼科VQA。
- 核心创新点：
  - 设计三阶段流水线收集10719张眼底图像并标注15595个病变，所有病变基于ETDRS网格映射到九个临床区域
  - 生成72706个四格式问题（开放/封闭/单选/多选）并构建双指标评估（答案准确性与病变级推理）
  - 将眼科VQA从单纯答案准确性扩展为需要空间定位病变证据的临床可解释任务
  - 实验证明引入病变级空间证据一致提升模型性能与推理透明度，突显空间定位的必要性
- 和已有工作的区别：现有眼科VQA基准缺乏显式视觉证据，而本工作首次提供标准化的空间定位病变标注以支撑临床可解释性。
- 阅读启发：空间定位的病变证据是构建可靠且可解释的眼科VQA系统的关键。
- 可信度：high

### 2. PrivFusion: A Privacy-preserving Multi-Agent Framework for Harmonizing Distributed Datasets
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24249v1-privfusion-a-privacy-preserving-multi-agent-framework-for-harmonizing-distributed-datasets
- 一句话贡献：提出PrivFusion框架，在联邦学习之前通过多智能体自动实现隐私保护的分布式数据协调，解决多机构数据异构性问题。
- 核心创新点：
  - 设计多智能体架构，每个站点运行本地智能体分析数据而不暴露原始信息
  - 基于语义相似性的跨站点特征聚类方法，自动识别可协调的字段
  - 迭代式转换建议机制，逐步调整数据格式直至全局对齐
  - 将数据协调作为联邦学习的必要前置步骤，而非假设数据集已统一
  - 针对多机构医疗数据的高度异构性提出自动化解决方案，替代手动协调
- 和已有工作的区别：现有联邦学习工作多关注模型聚合的隐私保护或非独立同分布问题，而忽略或假定数据已提前协调；本工作首次将数据协调本身作为隐私保护下的自动化任务，并利用多智能体协作实现。
- 阅读启发：联邦学习在多机构医疗场景中的成功不仅依赖算法，更需要高效的数据协调；自动化和隐私保护可兼得。
- 可信度：medium

### 3. Parameter-Efficient VLMs for Gastrointestinal Endoscopy: Medical Image Generation and Clinical Visual Question Answering
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24792v1-parameter-efficient-vlms-for-gastrointestinal-endoscopy-medical-image-generation-and-clinical-visual-question-answering
- 一句话贡献：提出参数高效的视觉语言模型双流水线，同时解决胃肠内镜中医疗视觉问答和隐私保护合成图像生成问题，显著降低计算成本并提升性能。
- 核心创新点：
  - 采用Florence-2视觉语言模型结合参数高效微调（PEFT）进行医疗VQA，降低训练计算成本并增强可解释性
  - 运用Low-Rank Adaptation (LoRA)微调Stable Diffusion 2.1生成高质量胃肠内镜图像，避免患者隐私泄露
  - 同时针对胃肠内镜AI中两个关键瓶颈：标注数据稀缺和隐私保护，提出统一的双流水线框架
  - 在医疗VQA任务中应用PEFT，替代传统全参数微调，解决临床部署中的计算和隐私限制
  - VQA在Kvasir-VQA数据集上达到ROUGE-1=0.92、ROUGE-L=0.91，BLEU从0.08提升至0.24
- 和已有工作的区别：现有工作分别处理VQA或图像生成，本文首次在胃肠内镜领域将PEFT应用于两个任务，并证明LoRA合成图像在图像-文本一致性上优于主流生成模型。
- 阅读启发：参数高效微调可有效缓解医学AI中数据与计算瓶颈，双流水线框架为内镜诊断的可靠性和可扩展性提供了实用方案。
- 可信度：high

### 4. Universal Boosts, Specific Suppressors: Sparse Autoencoder Steering of Medical Vision-Language Models
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24977v1-universal-boosts-specific-suppressors-sparse-autoencoder-steering-of-medical-vision-language-models
- 一句话贡献：提出一种基于稀疏自编码器的解码时残差引导方法，通过逐token因果干预（提升正确特征、抑制错误特征）改善医学VLM报告质量，无需权重更新。
- 核心创新点：
  - 使用Top-K稀疏自编码器在后期层进行逐token残差引导
  - 因果干预针对临床错误进行抑制/提升
  - 推理时干预无需训练，零样本迁移
  - 跨模型特征对齐发现通用提升方向与模型特定抑制方向
  - 首
- 和已有工作的区别：与依赖权重更新的微调方法不同，本文方法仅需推理时干预，无需额外训练；同时揭示了特征的可迁移性差异，为跨模型部署提供指导。
- 阅读启发：为VLM幻觉问题提供了一种轻量级、可迁移的推理时干预方法，并揭示了特征在模型间的通用与特定性质。
- 可信度：high

### 5. Towards Reliable Fetal Ultrasound Interpretation with Multi-Agent Collaboration
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.25357v1-towards-reliable-fetal-ultrasound-interpretation-with-multi-agent-collaboration
- 一句话贡献：提出FetUSAgents，一种工具增强的多智能体系统，通过双路径证据仲裁和检索增强证据库实现可靠的胎儿超声解读，在VQA任务上超越最强基线25%以上。
- 核心创新点：
  - 多智能体协作架构，通过LLM代理协调任务特定视觉工具完成从解剖识别到定量测量的子任务
  - 双路径证据仲裁(DPEA)，融合LLM推理性推理与结构化计算证据，提升可靠性与可溯源性
  - 检索增强证据库，整合中间发现支持临床可解释结论
  - 将胎儿超声解读定义为从视觉感知到临床理解的多步骤工作流，而非单一任务
  - 构建FetUS-VQA基准，包含1,892张图像和3,205个问答对，覆盖10项临床任务
- 和已有工作的区别：不同于“单任务单模型”范式及直接使用MLLM的局限，采用多智能体协作和工具增强，通过双路径仲裁解决领域特异性不足和幻觉问题。
- 阅读启发：提供了可扩展的证据驱动临床助手路线，用于产前成像的可靠自动解读。
- 可信度：high

### 6. EchoPilot: Training-Free Ultrasound Video Segmentation via Scale-Space Semantic Prompting and Reliability-Gated Memory
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.25944v1-echopilot-training-free-ultrasound-video-segmentation-via-scale-space-semantic-prompting-and-reliability-gated-memory
- 一句话贡献：提出无需训练的超声视频分割框架EchoPilot，仅需单点点击和类别名称，通过尺度空间语义提示和可靠性门控记忆实现高质量分割。
- 核心创新点：
  - 提出尺度空间语义提示（Scale-Space Semantic Prompting），包括参数自由的S.E.E.D.准则选择最优上下文视图，以及从基础特征合成几何精确的辅助点提示，无需额外用户交互
  - 提出可靠性门控记忆更新（Reliability-Gated Memory），根据预测不确定性选择性冻结提示视频分割器的记忆库，防止误差积累
  - 结合冻结的医学视觉语言模型（VLM）用于语义定位、视觉基础模型（VFM）用于密集几何特征提取、以及提示视频分割器用于掩码预测和传播，三者协同工作无需训练
  - 在稀疏交互设定下（仅第一帧单点点击和类别名称）实现无需训练的超声视频分割
  - 首次将冻结的医学视觉语言模型用于无训练超声视频分割
- 和已有工作的区别：之前的提示基础模型直接部署在超声中不可靠，因为单点提供空间上下文不足导致尺度模糊，且贪婪记忆更新放大早期错误导致严重时域漂移；EchoPilot通过尺度空间语义提示解决初始化模糊，通过可靠性门控记忆解决传播漂移。
- 阅读启发：本文展示了一种无需训练、仅需极稀疏交互的超声视频分割方案，通过巧妙结合多个预训练模型和创新的提示与记忆机制，有效应对超声图像的噪声、弱边界和快速变形挑战。
- 可信度：high

### 7. RAPTOR+: A Visually Grounded Vision-Language Framework to Improve Clinical Trust and Auditability in Automated Cancer Referral Processing
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.25956v1-raptor-a-visually-grounded-vision-language-framework-to-improve-clinical-trust-and-auditability-in-automated-cancer-referral-processing
- 一句话贡献：提出RAPTOR+多模态框架，通过微调视觉语言模型实现端到端的癌症转诊表单理解，并引入接地感知评估以提升可审计性。
- 核心创新点：
  - 使用视觉语言模型（VLM）替代OCR+LLM两阶段流水线，实现端到端文档理解，克服手写、布局变化和证据链接丢失问题
  - 提出接地感知评估框架，同时衡量提取准确性和证据定位能力，引入'严格安全性'指标量化可审计性
  - 聚焦紧急疑似结直肠癌转诊处理中的手动审查瓶颈，将多模态文档理解应用于临床操作流程
  - 强调视觉证据的链接和可审计性，而非仅关注结构化抽取，将临床信任作为设计目标
  - 微调后的Qwen3-VL-8B在223份临床表单上达到96.1%阅读准确率和60.6%严格安全性，而零样本Gemini 2.5 Flash准确率92.6%但严格安全性仅1.2%，揭示零样本模型的接地鸿沟
- 和已有工作的区别：原RAPTOR依赖独立OCR阶段，对笔迹和布局鲁棒性差且无法保留视觉证据；RAPTOR+端到端VLM直接处理图像，且首次在转诊任务中评估证据定位能力以支持临床审计
- 阅读启发：在医疗文档理解任务中，任务特定的VLM微调对实现可靠、可审计的提取至关重要，零样本模型即使准确率高也缺乏证据可验证性
- 可信度：high

### 8. MedFM-Robust: Benchmarking Robustness of Medical Foundation Models
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.19027v3-medfm-robust-benchmarking-robustness-of-medical-foundation-models
- 一句话贡献：首次系统构建包含40种扰动（28种医疗特定）的鲁棒性基准，全面评估医疗基础模型在多模态任务上的鲁棒性。
- 核心创新点：
  - 构建了包含40种扰动（12基础+28医疗特定）的鲁棒性基准，覆盖8种成像模态
  - 系统评估了5种视觉-语言模型（VQA、视觉定位、描述）和2种分割模型（5种微调策略）
  - 发现了微调策略对鲁棒性的主导作用，LoRA退化约两倍于全微调
  - 揭示了医疗特定扰动对分割任务的严重损害（15个最强扰动中9个为医疗特定）
  - 对比了通用与医疗专用VLM的鲁棒性差异，提出部署指南
- 和已有工作的区别：已有工作主要评估自然图像或单一医疗任务的鲁棒性，本文首次构建包含多模态任务和医疗特定扰动的系统基准，并比较不同微调策略的影响。
- 阅读启发：医疗AI部署需考虑领域特定扰动，优先选择全微调或Adapter策略，避免LoRA用于鲁棒性敏感任务；通用模型不适合医疗定位任务。
- 可信度：high

### 9. PromptRad: Knowledge-Enhanced Multi-Label Prompt-Tuning for Low-Resource Radiology Report Labeling
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.20052v1-promptrad-knowledge-enhanced-multi-label-prompt-tuning-for-low-resource-radiology-report-labeling
- 一句话贡献：提出PromptRad，一种知识增强的多标签提示调优方法，在低资源放射学报告标注中仅需少量标注数据即可取得优异性能。
- 核心创新点：
  - 将多标签分类重构为掩码语言建模任务，利用提示调优避免额外分类层，降低数据需求
  - 基于UMLS元词表构建多词词汇表，融入同义词以增强类别语义表示
  - 在仅32个标注样本的低资源场景下，性能超越字典方法和传统微调基线
  - 针对低资源放射学报告多标签标注问题，解决标注数据稀缺的临床困境
  - 探索提示调优在医疗文本多标签分类中的应用，而非传统全量微调
- 和已有工作的区别：传统规则方法难以应对多样表述，微调方法需要大量标注数据；PromptRad通过提示调优和知识增强，在低资源下实现了更好的标注效果。
- 阅读启发：提示调优结合领域知识（如UMLS）可有效解决低资源医疗文本分类问题，减少对大规模人工标注的依赖。
- 可信度：high

### 10. RoboSurg-VQA: A Multimodal Benchmark for Surgical Segmentation-Aware Visual Question Answering
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.23068v1-robosurg-vqa-a-multimodal-benchmark-for-surgical-segmentation-aware-visual-question-answering
- 一句话贡献：提出RoboSurg-VQA，首个融合分割感知的机器人手术视觉问答基准，通过复用分割数据并采用约束提示+人工审计标注，实现临床相关问题的标准化评估。
- 核心创新点：
  - 利用现有手术分割数据集，通过统一模式标注生成视觉问答对，实现分割感知的VQA基准构建。
  - 采用约束提示自动生成候选答案并辅以人工审计，确保标注的合理性与一致性。
  - 设计涵盖手术上下文、解剖结构、成像模式、伪影、图像质量等6类临床相关问题的固定问题集。
  - 首次将分割感知（segmentation-aware）引入手术VQA，解决传统VQA忽略像素级理解的问题。
  - 聚焦临床实际需求，模拟医生在手术中提出的语言问题（如视野遮挡、烟雾、出血等退化视图下的问答）。
- 和已有工作的区别：与现有手术VQA或分割任务不同，本工作将分割感知与VQA结合，并利用已有分割数据自动构建大规模、多类别、临床相关的问题集，大幅降低标注成本。
- 阅读启发：为机器人辅助手术中的视觉问答提供了首个分割感知基准，展示了如何有效复用分割数据生成高质量VQA标注。
- 可信度：high

### 11. What Makes a Medical Checker Trainable? Diagnosing Signal Collapse and Reward Hacking in Checker-Guided RAG for Biomedical QA
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.25988v1-what-makes-a-medical-checker-trainable-diagnosing-signal-collapse-and-reward-hacking-in-checker-guided-rag-for-biomedical-qa
- 一句话贡献：发现NLI检查器的输出分布而非准确率决定其在医学RAG强化学习中的可训练性，并诊断出信号坍缩与奖励破解问题，为验证器奖励系统设立边界条件。
- 核心创新点：
  - 系统比较四种NLI后端作为GRPO训练奖励，揭示LLM对数概率导致信号坍缩
  - 发现强信号检查器触发三步奖励破解级联（短回答、搜索避免、语言崩塌）
  - 提出信号强度策略依赖性，同一检查器在不同策略下表现不同
  - 首次从输出分布角度分析检查器在强化学习中的可训练性，而非依赖准确率
  - 聚焦医学RAG中检查器奖励的退化模式，填补了相关理论空白
- 和已有工作的区别：以往工作关注检查器准确率，本文揭示输出分布（中性标签比例）才是关键，并首次描述奖励破解三阶段级联
- 阅读启发：训练可微的验证器奖励时，应避免使用高偏斜的对数概率分布，选择校准度好的分类器；强信号未必更好，需警惕奖励破解。
- 可信度：high

### 12. BalanceRAG: Joint Risk Calibration for Cascaded Retrieval-Augmented Generation
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.20084v1-balancerag-joint-risk-calibration-for-cascaded-retrieval-augmented-generation
- 一句话贡献：提出BalanceRAG，通过二维网格上的序列图检验联合校准级联RAG中LLM-only和RAG分支的阈值，在控制系统级错误率的同时提高覆盖并减少不必要的检索调用。
- 核心创新点：
  - 将阈值对视为二维网格上的操作点，使用顺序图形测试识别安全操作点
  - 支持多风险校准，允许同时限制检索使用率与选择条件风险
  - 实现风险自适应的阈值校准，动态控制系统级错误率
  - 针对级联RAG中LLM-only和RAG分支的联合阈值校准问题，而非传统的逐阶段独立校准
  - 在三个开放域QA基准上，BalanceRAG满足预设风险水平，同时保留更多正确样本并提高覆盖率
- 和已有工作的区别：以往级联RAG的校准采用逐阶段进行，导致保守覆盖；BalanceRAG首次联合校准两个分支的阈值，实现了更优的风险-覆盖权衡。
- 阅读启发：级联RAG系统中联合阈值校准比逐阶段校准更有效，能够兼顾风险控制和覆盖性能。
- 可信度：high

### 13. VRXU-net: A Deep Learning Approach for Brain Ischemic Stroke Lesion Detection and Segmentation in T1W MRI
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.21633v1-vrxu-net-a-deep-learning-approach-for-brain-ischemic-stroke-lesion-detection-and-segmentation-in-t1w-mri
- 一句话贡献：提出VRXU-net，结合改进VGG检测与残差U-Net分割，通过三平面独立处理并融合结果，以及预分类器过滤非病变切片，实现T1W MRI中脑缺血性卒中病变的准确检测与分割。
- 核心创新点：
  - 构建VRXU-net架构，先使用改进VGG模型在2D切片上检测病变，再通过带残差块的U型网络进行分割
  - 独立处理轴向、矢状、冠状三个解剖平面，并聚合三平面分割结果以提升定位精度
  - 在分割前引入高性能分类器作为预过滤，减少非病变切片的无效分割，提高速度和准确性
  - 分割输出反馈给分类模型，用于降低假阳性预测
  - 针对T1W MRI中缺血性卒中病变与周围正常组织灰度相似、形状大小位置多变导致的检测和分割困难
- 和已有工作的区别：现有方法通常直接处理3D图像或单一平面，而本文通过将3D图像分解为2D切片并融合三平面信息，同时采用检测-分割流水线和预分类器策略，在降低模型复杂度的同时提高了分割精度和效率。
- 阅读启发：本文提供了一种新颖的流水线式深度学习方法，通过多平面融合和预过滤策略，有效解决了缺血性卒中病变在T1W MRI中的检测与分割难题，且方法具有一定的通用性和可扩展性。
- 可信度：medium

### 14. ImPartial: Multi-channel Whole-Cell Segmentation using Partial Annotations
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24128v1-impartial-multi-channel-whole-cell-segmentation-using-partial-annotations
- 一句话贡献：提出ImPartial框架，利用稀疏涂鸦和自监督多通道量化插值，以极少的标注达到与全监督相当的多通道细胞分割性能。
- 核心创新点：
  - 提出自监督多通道量化插值方法，将分割目标转化为分类任务，避免像素级重建
  - 利用跨通道信息进行量化插值，增强分割特征学习
  - 仅需稀疏涂鸦作为标注，结合有限监督训练
  - 针对低标注条件下的多通道细胞分割问题，尤其适应于新兴成像模态和变通道配置
  - 放宽了传统方法对密集像素级标注的依赖
- 和已有工作的区别：区别于需要完美像素重建或去噪的自监督方法，本方法直接优化与分割对齐的分类目标，且无需完整标注。
- 阅读启发：该方法大幅降低细胞分割的标注需求，为病理学图像分析在数据稀缺场景下的应用提供了实用方案。
- 可信度：high

### 15. Med-R2: An Adversarial Benchmark for Evidence-Grounded Reasoning in Medical VLMs
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24492v1-med-r2-an-adversarial-benchmark-for-evidence-grounded-reasoning-in-medical-vlms
- 一句话贡献：提出Med-R2 Bench，一个层级化、对抗性的基准，用于评估医学视觉语言模型在临床工作流中是否进行基于证据的推理而非依赖虚假先验。
- 核心创新点：
  - 构建了与临床工作流对齐的四阶段层级化基准，包含逐步问答任务以评估推理链的视觉证据根基
  - 引入对抗性扰动（如误导性提示）测试模型对错误线索的鲁棒性
  - 提出层级微调策略，利用层级化数据提升模型推理鲁棒性
  - 针对医学VLM在VQA中可能依赖虚假先验而非证据推理的问题，首次系统性地提出了对抗性评估框架
  - 定义了从临床检查、诊断、治疗到预后四个阶段的层级化推理评估
- 和已有工作的区别：现有基准多评估总体VQA准确率，而Med-R2专注于推理过程是否扎根于视觉证据，并通过对抗性设置暴露模型对虚假先验的依赖，同时与临床工作流深度结合。
- 阅读启发：该基准为评估和提升医学VLM的可靠推理能力提供了关键工具，强调了证据基础在医疗AI中的重要性。
- 可信度：high

### 16. Thinking in Scales: Accelerating Gigapixel Pathology Image Analysis via Adaptive Continuous Reasoning
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.19491v2-thinking-in-scales-accelerating-gigapixel-pathology-image-analysis-via-adaptive-continuous-reasoning
- 一句话贡献：提出PathCTM模型，通过自适应连续推理和置信度感知早停，在不损失准确率的前提下将WSI分析的计算开销降低约96%。
- 核心创新点：
  - 将诊断推理建模为动态顺序信息追求过程
  - 条件计算实现低倍到高倍动态尺度切换
  - 注意力引导的区域剪枝机制
  - 置信度感知的早停策略
  - 解决传统MIL处理所有高倍patch的计算冗余问题
- 和已有工作的区别：传统MIL需要固定处理所有高倍patch，而PathCTM通过动态尺度选择和早停，仅处理必要区域，实现数量级效率提升。
- 阅读启发：WSI分析可模拟病理医生先全局浏览再局部细看，通过智能早停大幅加速，为临床部署提供高效解决方案。
- 可信度：high

### 17. Cardiac fat segmentation using computed tomography and an image-to-image conditional generative adversarial neural network
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.20064v1-cardiac-fat-segmentation-using-computed-tomography-and-an-image-to-image-conditional-generative-adversarial-neural-network
- 一句话贡献：首次将条件生成对抗网络（pix2pix）应用于心脏CT图像中两种脂肪（心外膜和纵隔）的自动分割，实现高精度实时分割。
- 核心创新点：
  - 使用pix2pix条件GAN进行医学图像分割，开辟新应用场景
  - 同时分割心外膜和纵隔两种脂肪，利用生成对抗网络特性
  - 实现实时分割，速度优于现有方法
  - 将图像到图像的翻译任务直接应用于心脏脂肪分割，拓展pix2pix使用范围
  - 在CT数据集上达到99.08%准确率、98.73 F1（心外膜）和97.90%准确率、98.40 F1（纵隔），指标领先
- 和已有工作的区别：现有方法多采用传统分割或U-Net，本文首次采用条件GAN（pix2pix）进行心脏脂肪分割，且精度和速度均更优。
- 阅读启发：条件GAN在医学图像分割中具有潜力，尤其适用于需要同时分割多个结构且追求实时性的任务。
- 可信度：high

### 18. Divide-and-Conquer Inference for Large-Scale Visual Recognition with Multimodal Large Language Models
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24799v1-divide-and-conquer-inference-for-large-scale-visual-recognition-with-multimodal-large-language-models
- 一句话贡献：提出分而治之推理（DCI）策略，通过递归分解大规模视觉分类任务并动态剪枝，有效缓解MLLM在长序列识别中的性能崩溃问题，实现无需额外训练的推理加速与精度提升。
- 核心创新点：
  - 从信息论角度揭示长序列识别中注意力稀释与衰减导致性能崩溃的内在机理
  - 设计递归分解策略，将全局分类任务拆解为多个局部子问题，提升局部信噪比
  - 引入动态剪枝机制，压缩搜索空间，避免冗余计算
  - 实现接近线性的推理复杂度，替代传统自注意力二次复杂度
  - 首次定义并理论分析MLLM在大规模分类中的性能崩溃现象（Performance Collapse in Long Sequence Recognition）
- 和已有工作的区别：现有工作主要关注MLLM的通用能力或小规模任务，缺乏对大规模标签空间下性能退化的分析与有效解决方案；DCI首次将分治思想引入MLLM推理，并理论解释性能崩溃原因。
- 阅读启发：DCI是一种即插即用、模型无关的测试时扩展方法，可高效提升MLLM在大规模视觉识别任务中的准确率和速度，为部署轻量模型替代重型模型提供新范式。
- 可信度：high

### 19. Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.22414v1
- 一句话贡献：提出包含空间定位病灶证据的眼科VQA基准FundusGround，以提升临床可解释性。
- 核心创新点：
  - 提出三阶段流水线收集10,719张眼底图像，含15,595个图像级精细病灶标注
  - 采用ETDRS网格对所有病灶进行空间定位，实现标准化的九区域视网膜映射
  - 基于结构化病灶证据生成72,706个问题，涵盖开放、封闭、单选和多选四种格式
  - 引入双指标评估：答案准确性和病灶级推理能力
  - 首次将临床可解释性（空间定位病灶证据）作为眼科VQA的核心目标
- 和已有工作的区别：现有眼科VQA基准仅评估答案准确性，缺乏对视觉证据的空间定位和可解释性要求，本工作通过病灶级标注和ETDRS网格实现显式空间定位的推理。
- 阅读启发：空间定位病灶证据是构建可靠、可解释眼科VQA系统的关键，未来工作可在此基础上探索更多临床场景。
- 可信度：high

### 20. PrivFusion: A Privacy-preserving Multi-Agent Framework for Harmonizing Distributed Datasets
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.24249v1
- 一句话贡献：提出了一个隐私保护的多智能体框架PrivFusion，在联邦学习之前自动协调异构结构化数据集，显著减少手动工作量。
- 核心创新点：
  - 设计多智能体系统，每个站点运行本地智能体分析数据分布与特征语义
  - 跨站点聚类语义相似特征，自动生成转换建议
  - 迭代协调过程直到所有站点的数据对齐，无需共享原始数据
  - 首次将数据协调作为联邦学习的关键前置步骤，并实现自动化与隐私保护
  - 针对结构化临床数据集的异质性，提出通用协调框架
- 和已有工作的区别：现有联邦学习工作通常假设数据已协调或忽略异质性，PrivFusion首次提出自动化、隐私保护的数据协调方法作为联邦学习的预处理阶段。
- 阅读启发：该框架表明，通过多智能体协作可以在不泄露隐私的前提下自动解决多中心数据异质性，为联邦学习的实用部署铺平道路。
- 可信度：medium

### 21. Parameter-Efficient VLMs for Gastrointestinal Endoscopy: Medical Image Generation and Clinical Visual Question Answering
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.24792v1
- 一句话贡献：提出双管道PEFT模型，同时用于胃肠内镜临床VQA和隐私保护合成图像生成，显著降低计算成本并提升诊断可靠性。
- 核心创新点：
  - 采用Florence-2视觉语言模型结合PEFT进行医疗VQA，增强可解释性并降低训练计算成本。
  - 使用Low-Rank Adaptation (LoRA) 与Stable Diffusion 2.1生成高质量胃肠内镜图像，实现隐私保护的数据库扩充。
  - 通过双管道框架统一处理VQA和合成数据生成，两个任务相互促进。
  - 针对胃肠内镜AI中标注数据短缺、隐私政策严格和传统微调瓶颈的双重问题，首次提出同时解决VQA和数据生成的框架。
  - 利用合成数据增强训练集以改善私有数据集上的VQA性能，克服公开数据不足的限制。
- 和已有工作的区别：现有工作通常单独处理VQA或图像生成，且未采用参数高效微调；本文首次将PEFT应用于胃肠内镜领域，同时优化两个任务，并在合成质量上超越现有生成模型。
- 阅读启发：参数高效方法（如LoRA）在医学影像AI中极具潜力，能够以低成本实现高性能VQA和隐私保护数据生成，为临床部署提供可扩展方案。
- 可信度：high

### 22. Universal Boosts, Specific Suppressors: Sparse Autoencoder Steering of Medical Vision-Language Models
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.24977v1
- 一句话贡献：提出一种基于稀疏自编码器的解码时残差引导方法，无需权重更新即可抑制医学视觉语言模型的幻觉，并发现促进正确生成的特征跨模型通用而抑制幻觉的特征模型特异。
- 核心创新点：
  - 在解码阶段对每个token使用Top-K稀疏自编码器进行残差引导，通过因果干预抑制临床错误
  - 将引导向量分为促进正确（boost）和抑制错误（suppress）两类，并分别分析其跨模型迁移性
  - 提出根据模型特异性定制抑制向量，而共享促进向量的迁移策略
  - 首次将稀疏自编码器应用于医学视觉语言模型的推理时引导，解决报告生成中的幻觉问题
  - 关注跨模型迁移时引导向量的通用性与特异性差异，提出非对称迁移策略
- 和已有工作的区别：不同于以往需要微调或训练额外模块的方法，本工作仅通过解码时残差引导（SAE基）提升质量，且揭示了promote和suppress特征的不同迁移属性。
- 阅读启发：稀疏自编码器可有效操控模型内部表示来抑制幻觉，且促进正确生成的特征具有跨模型通用性，为轻量级模型诊断和修复提供了新思路。
- 可信度：high

### 23. Towards Reliable Fetal Ultrasound Interpretation with Multi-Agent Collaboration
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.25357v1
- 一句话贡献：提出FetUSAgents多智能体系统，通过工具增强、双路径证据仲裁和检索增强证据库，实现可靠且可溯源的胎儿超声全流程分析，在VQA任务上超越最强基线25%以上。
- 核心创新点：
  - 提出工具增强的多智能体协作框架，协调LLM与任务特定视觉工具（如分割、测量模型）进行超声图像分析
  - 设计Dual-Path Evidence Arbitration（DPEA）机制，融合基于LLM的深思推理与结构化计算证据，提升可靠性与可解释性
  - 构建检索增强的证据库，汇总中间结果并支持可溯源的临床结论生成
  - 在视觉问答中引入多步骤子任务分解，从解剖识别到定量测量逐步推理
  - 克服了传统'一个任务一个模型'范式在胎儿超声多步骤流程中缺乏系统性集成的问题
- 和已有工作的区别：现有工作依赖端到端MLLM或独立任务模型，缺乏多步骤协同与可验证证据链；本工作通过多智能体协作、双路径仲裁和证据库实现结构化、可溯源的超声解释。
- 阅读启发：多智能体+工具增强+双路径仲裁可有效提升医学影像分析中的可靠性与临床适用性，为构建证据驱动的临床助手提供了可扩展的路线。
- 可信度：high

### 24. EchoPilot: Training-Free Ultrasound Video Segmentation via Scale-Space Semantic Prompting and Reliability-Gated Memory
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.25944v1
- 一句话贡献：提出一种无需训练的超声视频分割框架EchoPilot，仅需单点点击和类别名称，通过尺度空间语义提示和可靠性门控记忆实现鲁棒分割。
- 核心创新点：
  - 提出Scale-Space Semantic Prompting方法：先通过参数自由的S.E.E.D.准则选择最优上下文视图，再从密集基础特征中合成几何精确的辅助点提示，无需额外用户交互。
  - 提出Reliability-Gated Memory更新机制：在预测不确定时选择性冻结分割器的记忆库，防止误差累积和时序漂移。
  - 首个动态胎儿胎盘超声视频分割数据集，包含671帧标注图像。
  - 在稀疏第一帧交互设置下进行超声视频分割，仅需单点点击和解剖类别名称，无需密集标注或训练。
  - 针对超声图像特有的散斑噪声、弱边界和快速形变挑战，提出无需训练的解决方案。
- 和已有工作的区别：现有可提示基础模型直接部署在超声中因单点空间上下文不足和贪婪记忆更新导致不可靠，本文通过尺度空间语义提示解决尺度歧义，通过可靠性门控记忆减少错误传播。
- 阅读启发：提供了一种结合冻结视觉语言模型和视觉基础模型的无需训练框架，有效应对超声视频分割的挑战，具有实用性和鲁棒性。
- 可信度：high

### 25. RAPTOR+: A Visually Grounded Vision-Language Framework to Improve Clinical Trust and Auditability in Automated Cancer Referral Processing
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.25956v1
- 一句话贡献：提出RAPTOR+，一个基于视觉语言模型的端到端多模态框架，将半结构化癌症转诊表单的提取与视觉证据链接起来，显著提升临床可审计性和安全性。
- 核心创新点：
  - 将原有OCR+LLM流水线替换为端到端视觉语言模型（VLM），直接处理图像输入，避免OCR中间步骤的误差和布局依赖
  - 引入接地感知评估框架，同时衡量提取准确性和证据定位能力（Strict Safety指标）
  - 微调Qwen3-VL-8B模型实现96.1% Reading Accuracy和60.6% Strict Safety，证明任务特定微调是可靠临床文档理解的关键
  - 针对癌症紧急转诊表单处理中的临床信任和可审计性问题，首次将视觉接地引入医疗文档提取任务
  - 揭示零样本VLM存在严重接地差距：Gemini 2.5 Flash虽有92.6%阅读准确率但Strict Safety仅1.2%
- 和已有工作的区别：现有RAPTOR系统依赖独立OCR步骤，难以处理手写、布局变化且丢失视觉证据链接；RAPTOR+通过VLM端到端理解并显式关联视觉证据，提升审计能力。
- 阅读启发：在临床文档理解中，仅靠高准确率不足以保证信任，必须通过任务特定微调实现视觉证据的可追溯定位。
- 可信度：high

### 26. MedFM-Robust: Benchmarking Robustness of Medical Foundation Models
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/2605.19027v3
- 一句话贡献：构建首个覆盖8种成像模态、40种扰动的医学基础模型鲁棒性基准，系统揭示微调策略与领域特定扰动对性能的影响规律。
- 核心创新点：
  - 提出包含12种基础扰动和28种医学特定扰动的鲁棒性评测体系
  - 设计跨模态（VQA、视觉定位、分割）的鲁棒性评估框架
  - 对比5种微调策略（全微调、LoRA、Adapter等）的鲁棒性影响
  - 首次系统评估医学基础模型在真实世界扰动下的鲁棒性
  - 聚焦医学特定扰动（如病理染色、扫描噪声）而非通用噪声
- 和已有工作的区别：现有工作仅评估通用鲁棒性或单一任务，本文首次构建多模态、多任务、多扰动的医学基础模型鲁棒性基准，并发现领域特定扰动的关键影响。
- 阅读启发：医学基础模型部署时应优先选择全微调或Adpater策略，避免LoRA；评估鲁棒性必须包含领域特定扰动，而非仅依赖通用图像噪声。
- 可信度：high

### 27. BalanceRAG: Joint Risk Calibration for Cascaded Retrieval-Augmented Generation
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/2605.20084v1
- 一句话贡献：提出BalanceRAG方法，通过联合校准LLM-only和RAG两个分支的不确定性阈值对，在控制系统级错误率的同时保留更多样本，并减少不必要的检索调用。
- 核心创新点：
  - 将级联RAG的阈值对视为二维网格上的操作点，使用序贯图形测试识别安全操作点
  - 实现风险自适应阈值校准，联合控制两个分支的不确定性阈值而非逐阶段校准
  - 扩展到多风险校准，同时限制检索使用率和选择条件风险
  - 针对级联RAG中分阶段校准过于保守的问题，提出联合风险校准框架
  - 定义了二维阈值格点上的安全操作点概念，解决多阈值联合优化问题
- 和已有工作的区别：现有级联RAG方法通常逐阶段校准阈值，而BalanceRAG联合考虑LLM-only和RAG两个分支的不确定性，利用序贯图形测试在二维空间找到最优阈值对，实现更高效的风险控制。
- 阅读启发：本文提供了一种可控制风险且高效的级联RAG校准策略，能显著减少不必要的检索调用，适用于对检索成本敏感的部署场景。
- 可信度：high

### 28. Thinking in Scales: Accelerating Gigapixel Pathology Image Analysis via Adaptive Continuous Reasoning
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/2605.19491v2
- 一句话贡献：提出PathCTM，通过动态尺度切换和自适应早停实现千兆像素病理图像的token高效连续推理，大幅降低计算成本同时保持诊断精度。
- 核心创新点：
  - 将诊断推理建模为从低倍到高倍的动态顺序信息追踪过程
  - 采用条件计算实现注意力引导的区域修剪，动态切换尺度
  - 引入置信度感知的早停机制，在证据充分时终止推理
  - 针对传统MIL方法对高倍率全块遍历计算昂贵的问题，提出token高效的尺度空间连续推理范式
  - 相比标准MIL方法，PathCTM减少95.95%所需图像块，缩短95.62%推理时间，且AUC不下降
- 和已有工作的区别：传统方法固定在高倍率处理所有补丁并聚合，而PathCTM自适应地在低倍全局和高倍局部间切换，仅处理必要区域。
- 阅读启发：PathCTM提供了一种高效、可扩展的病理图像分析新思路，使得千兆像素级WSI的实时推理成为可能。
- 可信度：high

### 29. PromptRad: Knowledge-Enhanced Multi-Label Prompt-Tuning for Low-Resource Radiology Report Labeling
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/2605.20052v1
- 一句话贡献：提出PromptRad，一种知识增强的多标签提示调优方法，在仅需32个标注样本的低资源设置下，显著提升放射学报告标注性能。
- 核心创新点：
  - 将多标签分类重新表述为掩码语言建模（MLM），利用提示调优避免额外分类层
  - 从UMLS Metathesaurus引入多词同义词动词化器，增强类别语义表示
  - 设计专门的提示模板和动词化策略，有效处理复杂否定模式
  - 聚焦低资源临床场景下放射学报告的多标签标注问题
  - 解决传统规则方法灵活性不足和微调方法对大量标注数据依赖的矛盾
- 和已有工作的区别：与基于规则或微调的方法不同，PromptRad通过提示调优融合外部医学知识（UMLS同义词），以极少标注数据实现高性能，且对否定表达更鲁棒。
- 阅读启发：提示调优结合领域知识是突破低资源医疗文本分类的有效范式，尤其适用于标注数据稀缺的临床场景。
- 可信度：high

### 30. VRXU-net: A Deep Learning Approach for Brain Ischemic Stroke Lesion Detection and Segmentation in T1W MRI
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/2605.21633v1
- 一句话贡献：提出了一种结合分类与分割的序贯框架，利用三平面2D切片分析和残差U-net结构实现脑缺血性卒中病灶的高效检测与分割。
- 核心创新点：
  - 提出先分类后分割的序贯框架，通过高精度分类器筛选非病灶切片，减少不必要的分割计算
  - 设计基于视觉特征、残差连接和U型网络的VRU-Net架构，融合修改的VGG分类器与残差块分割网络
  - 将3D MRI分解为轴向、矢状、冠状三个平面的2D切片分别处理，再聚合三平面分割结果提升定位精度
  - 分割输出反馈至分类模型，帮助减少假阳性预测
  - 针对T1W MRI中缺血性卒中病灶与周围脑组织相似、难以分割的问题，提出多平面2D切片分析策略
- 和已有工作的区别：与现有方法相比，本工作将病灶检测和分割分解为两步：先使用改进的VGG进行2D切片级分类判断是否包含病灶，再仅对有病灶的切片使用残差U-net分割，并且融合三个解剖平面的分割结果，同时利用分割结果反馈优化分类器，形成闭环提升。
- 阅读启发：该工作展示了在医学图像分割中，先分类后分割的序贯策略能有效提升效率与性能，多平面融合和反馈机制有助于提高分割精度。
- 可信度：high

### 31. Cardiac fat segmentation using computed tomography and an image-to-image conditional generative adversarial neural network
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/2605.20064v1
- 一句话贡献：首次将pix2pix（条件生成对抗网络）应用于CT图像中心脏脂肪（心外膜和纵隔脂肪）的自动分割和量化，实现了高精度（平均精度99.08%，F1 98.73）和实时分割。
- 核心创新点：
  - 采用pix2pix网络进行图像到图像翻译，实现了端到端的心脏脂肪分割
  - 将原本设计用于图像生成的GAN架构迁移至医学图像分割任务
  - 将心脏脂肪分割问题转化为条件图像生成问题
  - 首次针对两种心脏脂肪（心外膜和纵隔脂肪）同时进行自动分割
  - 实验结果表明分割精度达到99.08%（心外膜脂肪）和97.90%（纵隔脂肪），F1分数分别为98.73和98.40
- 和已有工作的区别：此前心脏脂肪分割主要依赖传统图像处理或U-Net等CNN，本研究首次尝试使用条件GAN（pix2pix）并证明其优越性（更高的F1和更快的运行时间）。
- 阅读启发：条件GAN能够有效用于医学图像分割任务，尤其对心脏脂肪这种边界模糊的目标，展现出高精度和实时性潜力。
- 可信度：high

### 32. RoboSurg-VQA: A Multimodal Benchmark for Surgical Segmentation-Aware Visual Question Answering
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/2605.23068v1
- 一句话贡献：提出了RoboSurg-VQA，首个将手术分割语义与视觉问答结合的多模态基准，通过复用分割数据集和自动化标注构建临床相关的问答对。
- 核心创新点：
  - 提出分割感知的VQA基准，将分割掩码作为视觉问答的输入之一
  - 设计统一的模式将多个公开手术分割数据集转化为VQA格式
  - 采用约束提示与自动有效性检查结合人工审核的半自动化标注方法
  - 首次定义手术场景下的分割感知视觉问答任务
  - 覆盖程序上下文、解剖结构、伪影、图像质量等临床相关维度
- 和已有工作的区别：现有手术分割或VQA工作独立进行，该基准首次将分割信息融入VQA，并针对手术特定降质条件设计问题集。
- 阅读启发：了解手术VQA新基准的构建方法、标注策略和评估难点，为后续研究提供基础。
- 可信度：high

### 33. ImPartial: Multi-channel Whole-Cell Segmentation using Partial Annotations
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/2605.24128v1
- 一句话贡献：提出ImPartial框架，利用稀疏涂鸦标注和自监督多通道量化插补，在低标注下实现与全监督相当的多通道全细胞分割。
- 核心创新点：
  - 自监督多通道量化插补：不进行像素级重建，而是引入分类目标以更好对齐分割目标
  - 利用稀疏涂鸦作为部分标注，显著降低标注成本
  - 适用于可变通道配置的多重成像数据集
  - 针对多通道全细胞分割中标注稀缺的问题，提出仅需稀疏涂鸦的低标注设定
  - 面向新兴生物成像模态和多重数据集的可变通道配置
- 和已有工作的区别：现有方法需要密集像素级标注或依赖图像重建/去噪，而ImPartial引入自监督分类目标，避免不必要的重建，更高效利用稀疏标注。
- 阅读启发：稀疏涂鸦结合自监督多通道量化插补是一种实用、高效的细胞分割策略，可大幅降低标注负担。
- 可信度：high

### 34. Divide-and-Conquer Inference for Large-Scale Visual Recognition with Multimodal Large Language Models
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/2605.24799v1
- 一句话贡献：提出一种无需训练、即插即用的分治推理策略（DCI），通过递归分解和动态剪枝解决MLLM在大规模图像分类中的性能崩溃问题，使轻量模型媲美闭源巨头。
- 核心创新点：
  - 发现MLLM在长序列识别中的性能崩溃现象，并从信息论角度揭示其根源为信息熵与注意力稀释/衰减的冲突
  - 提出Divide-and-Conquer Inference (DCI)，将全局分类递归分解为局部子问题，并引入动态剪枝压缩搜索空间
  - 通过提高局部信噪比和缓解注意力权重稀释，改善长序列推理中的模型精度
  - 相比传统自注意力的二次复杂度，DCI实现更优的缩放行为并加速大规模分类推理
  - 首次系统定义并解释MLLM在大标签空间分类中的'性能崩溃'问题
- 和已有工作的区别：现有工作多关注MLLM的预训练或微调，本文首次针对推理阶段提出分治策略来处理大规模标签空间，无需更改模型结构或参数。
- 阅读启发：DCI是一种简单高效的推理增强方法，可即插即用提升MLLM在大规模视觉识别中的性能，尤其适合轻量级模型。
- 可信度：high

### 35. What Makes a Medical Checker Trainable? Diagnosing Signal Collapse and Reward Hacking in Checker-Guided RAG for Biomedical QA
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/2605.25988v1
- 一句话贡献：发现训练时检查器的输出分布（而非验证集准确率）决定了其是否提供可训练梯度，并揭示了信号坍缩与奖励劫持机制。
- 核心创新点：
  - 提出信号坍缩是log-prob特有的，校准的MedNLI分类器可避免；
  - 发现中等信号优于强信号，避免奖励劫持级联；
  - 揭示信号强度策略依赖性。
  - 将NLI检查器作为GRPO训练医学RAG代理的过程奖励，对比四种检查器后端。
  - 在四个医学QA基准上，使用中等信号的局部分类器训练的模型BERTScore提升12%，无需GPT依赖；
- 和已有工作的区别：先前关注检查器的准确率，本文发现输出分布更重要；揭示了检查器作为奖励时的边界条件，如信号坍缩和奖励劫持。
- 阅读启发：设计可训练检查器时，应关注输出分布而非准确率；避免强信号引起的奖励劫持；注意信号强度的策略依赖性。
- 可信度：high

### 36. Med-R2: An Adversarial Benchmark for Evidence-Grounded Reasoning in Medical VLMs
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/2605.24492v1
- 一句话贡献：提出一个与临床工作流对齐的分层对抗基准Med-R2 Bench，系统评估医学视觉语言模型在视觉证据基础上的推理鲁棒性。
- 核心创新点：
  - 设计分阶段逐步问答任务，覆盖四个临床阶段，严格测试推理链是否基于视觉证据
  - 引入针对误导线索的对抗扰动，评估模型对虚假相关性或错误提示的鲁棒性
  - 构建大规模数据集（42,432张图像、31个任务类别、110,406个QA对）
  - 提出基于分层数据的逐步微调方法，显著提升推理鲁棒性
  - 将对抗鲁棒性与视觉接地联合评估，揭示模型是否依赖假相关性或正确提示
- 和已有工作的区别：现有医学VLM基准多关注整体问答准确率，而Med-R2首次从证据基础推理角度，结合对抗扰动和临床工作流分层，系统评估模型的鲁棒性与解释性缺陷。
- 阅读启发：医学视觉语言模型在推理链中容易依赖文本提示而非视觉证据，需通过分层对抗训练提升鲁棒性，才能更可靠地应用于临床决策。
- 可信度：high
