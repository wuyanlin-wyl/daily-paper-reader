# 创新点总结 · 2026-05-26

- 生成时间：2026-05-27 06:56:51 UTC
- 当日论文数：36

## 今日趋势
- 本日创新趋势需要配置 LLM 后进行横向综合。

## 最值得先读

| 论文 | 推荐理由 |
|---|---|
| [Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence](https://arxiv.org/abs/202605/26/2605.22414v1-towards-clinically-interpretable-ophthalmic-vqa-via-spatially-grounded-lesion-evidence) | 基础版按推荐顺序列出，建议优先阅读。 |
| [PrivFusion: A Privacy-preserving Multi-Agent Framework for Harmonizing Distributed Datasets](https://arxiv.org/abs/202605/26/2605.24249v1-privfusion-a-privacy-preserving-multi-agent-framework-for-harmonizing-distributed-datasets) | 基础版按推荐顺序列出，建议优先阅读。 |
| [Parameter-Efficient VLMs for Gastrointestinal Endoscopy: Medical Image Generation and Clinical Visual Question Answering](https://arxiv.org/abs/202605/26/2605.24792v1-parameter-efficient-vlms-for-gastrointestinal-endoscopy-medical-image-generation-and-clinical-visual-question-answering) | 基础版按推荐顺序列出，建议优先阅读。 |
| [Universal Boosts, Specific Suppressors: Sparse Autoencoder Steering of Medical Vision-Language Models](https://arxiv.org/abs/202605/26/2605.24977v1-universal-boosts-specific-suppressors-sparse-autoencoder-steering-of-medical-vision-language-models) | 基础版按推荐顺序列出，建议优先阅读。 |
| [Towards Reliable Fetal Ultrasound Interpretation with Multi-Agent Collaboration](https://arxiv.org/abs/202605/26/2605.25357v1-towards-reliable-fetal-ultrasound-interpretation-with-multi-agent-collaboration) | 基础版按推荐顺序列出，建议优先阅读。 |

## 单篇创新点

### 1. Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.22414v1-towards-clinically-interpretable-ophthalmic-vqa-via-spatially-grounded-lesion-evidence
- 一句话贡献：提出FundusGround基准，通过ETDRS网格空间定位病变证据，首次在眼科VQA中实现临床可解释的视觉问答。
- 核心创新点：
  - 设计三阶段管道收集10,719张眼底图像并注释15,595个病变，基于ETDRS网格将病变标准映射到9个临床视网膜区域
  - 生成72,706个涵盖开放、封闭、单选、多选四种格式的问题，构建大规模多格式问答数据集
  - 引入病变级空间证据作为模型输入，提升答案准确性和推理透明度
  - 将眼科VQA问题从单纯答案准确性转向临床可解释性，要求模型提供空间定位的病变证据
  - 首次定义并标准化了眼科VQA中的可解释性标准，即病变区域的空间接地
- 和已有工作的区别：现有眼科VQA基准（如FAMOUS、OphthoVQA）只关注答案准确性，缺乏显式视觉证据；本文首次引入ETDRS网格空间定位的病变证据，可解释性成为核心优化目标。
- 阅读启发：空间显式接地（如ETDRS病变定位）是实现可靠、可解释眼科VQA的关键，未来工作应重视视觉证据的结构化标注。
- 可信度：high

### 2. PrivFusion: A Privacy-preserving Multi-Agent Framework for Harmonizing Distributed Datasets
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24249v1-privfusion-a-privacy-preserving-multi-agent-framework-for-harmonizing-distributed-datasets
- 一句话贡献：提出PrivFusion，一个隐私保护的多智能体框架，在联邦学习前自动协调异构结构化数据集，减少人工干预。
- 核心创新点：
  - 使用多智能体分别分析本地数据，进行语义特征聚类
  - 基于聚类结果迭代提供转换建议直至特征对齐
  - 在隐私保护下实现跨机构数据自动协调
  - 将数据协调作为联邦学习的前置关键步骤，解决被忽视的异构性问题
  - 针对多机构结构化医疗数据，自动化协调替代传统手工操作
- 和已有工作的区别：现有联邦学习工作通常假设数据已协调或依赖大量人工协调，PrivFusion首次提出自动化、隐私保护的协调框架。
- 阅读启发：自动化数据协调是联邦学习成功的重要前提，多智能体框架可有效解决异构性问题并保护隐私。
- 可信度：high

### 3. Parameter-Efficient VLMs for Gastrointestinal Endoscopy: Medical Image Generation and Clinical Visual Question Answering
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24792v1-parameter-efficient-vlms-for-gastrointestinal-endoscopy-medical-image-generation-and-clinical-visual-question-answering
- 一句话贡献：提出双流水线PEFT模型，同时实现胃肠内镜临床VQA和隐私保护合成图像生成，显著降低计算成本并提升性能。
- 核心创新点：
  - 采用Florence-2作为VQA基础模型，结合PEFT增强可解释性并大幅降低训练计算成本
  - 使用LoRA微调Stable Diffusion 2.1生成高质量胃肠内镜图像，保护患者隐私
  - 双流水线架构同时处理VQA和图像生成两个任务
  - 针对胃肠内镜AI面临的标注数据稀缺、隐私政策严格、传统微调瓶颈三大限制
  - 解决医疗场景中隐私保护合成数据生成与临床VQA的联合需求
- 和已有工作的区别：现有工作通常依赖大量标注数据和全参数微调，而本文采用参数高效方法（PEFT+LoRA）在保持性能的同时大幅降低资源消耗，并首次将隐私保护生成与VQA结合于胃肠内镜。
- 阅读启发：参数高效微调（PEFT）在医疗低资源场景下极具潜力，可同时实现高性能与隐私保护，为临床AI部署提供可行路径。
- 可信度：high

### 4. Universal Boosts, Specific Suppressors: Sparse Autoencoder Steering of Medical Vision-Language Models
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24977v1-universal-boosts-specific-suppressors-sparse-autoencoder-steering-of-medical-vision-language-models
- 一句话贡献：提出基于稀疏自编码器的解码时残差引导方法，通过逐token因果干预（提升正确特征、抑制错误特征）有效减少医学视觉语言模型在胸部X光报告生成中的幻觉，且发现提升方向跨模型通用、抑制方向模型特有。
- 核心创新点：
  - 在解码阶段使用每token的稀疏自编码器进行残差引导，无需权重更新
  - 采用因果干预策略，分别对正确特征进行提升、对错误特征进行抑制
  - 结合提升和抑制操作在推理时组合干预
  - 针对医学视觉语言模型生成报告时的特定幻觉问题（虚构、遗漏、定位错误）
  - 无需重新训练或微调模型，仅通过推理时干预改善报告质量
- 和已有工作的区别：现有工作多通过微调或重训练解决幻觉，本方法首次利用解码时稀疏自编码器引导实现无需权重更新的推理时干预，且发现提升与抑制特征的不同跨模型泛化特性
- 阅读启发：稀疏自编码器可用于引导大语言模型解码行为，且提升特征具有跨模型通用性，为高效迁移提供新思路
- 可信度：high

### 5. Towards Reliable Fetal Ultrasound Interpretation with Multi-Agent Collaboration
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.25357v1-towards-reliable-fetal-ultrasound-interpretation-with-multi-agent-collaboration
- 一句话贡献：提出FetUSAgents，一种工具增强的多智能体系统，通过双路径证据仲裁（DPEA）协调LLM推理与专用视觉工具，实现可靠的胎儿超声全面解读，并在分布外VQA任务中大幅超越基线。
- 核心创新点：
  - 提出工具增强的多智能体系统FetUSAgents，通过协作LLM代理协调多个任务特定的视觉工具
  - 引入双路径证据仲裁（DPEA），融合LLM的推理性思考与专用视觉工具的结构化计算证据
  - 构建检索增强的证据银行，整合中间结果以支持可溯源且临床可靠的结论
  - 将胎儿超声解读从单一模型处理单任务扩展到多智能体协作的完整工作流
  - 针对MLLM在胎儿超声分析中的领域知识不足和幻觉风险，提出结合工具证据的系统方案
- 和已有工作的区别：不同于以往‘一个任务一个模型’的范式，FetUSAgents通过多智能体协作和双路径证据仲裁，将视觉感知与临床理解系统整合，显著提升了跨任务泛化能力和可解释性。
- 阅读启发：该工作为医疗影像分析提供了一种可扩展的、证据驱动的多智能体协作范式，有望提高胎儿超声解读的可靠性。
- 可信度：high

### 6. EchoPilot: Training-Free Ultrasound Video Segmentation via Scale-Space Semantic Prompting and Reliability-Gated Memory
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.25944v1-echopilot-training-free-ultrasound-video-segmentation-via-scale-space-semantic-prompting-and-reliability-gated-memory
- 一句话贡献：EchoPilot提出了一种无需训练的超声视频分割框架，仅需单点点击和类别名称，通过尺度空间语义提示和可靠性门控记忆实现高质量分割。
- 核心创新点：
  - 提出Scale-Space Semantic Prompting，通过S.E.E.D.准则自动选择最优上下文视图并合成辅助点提示，无需额外用户交互。
  - 设计Reliability-Gated Memory更新机制，在预测不确定时冻结分割器记忆库，防止误差累积与时间漂移。
  - 利用冻结的医学视觉语言模型与视觉基础模型联合进行语义定位与几何特征提取，实现训练-free分割。
  - 首个针对超声视频的稀疏交互分割框架，仅需第一帧的一个点点击和类别名称作为输入。
  - 贡献了首个动态胎儿胎盘超声视频分割数据集，包含671帧标注。
- 和已有工作的区别：现有方法或依赖大量标注进行训练，或直接部署提示模型于超声时因尺度模糊和错误记忆累积导致性能不佳；EchoPilot通过自动选择上下文视图和选择性记忆冻结解决了这些不足。
- 阅读启发：提供了一种高效、无需训练的超声视频分割范式，证明冻结的通用模型通过巧妙提示设计即可胜任医学影像任务。
- 可信度：high

### 7. RAPTOR+: A Visually Grounded Vision-Language Framework to Improve Clinical Trust and Auditability in Automated Cancer Referral Processing
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.25956v1-raptor-a-visually-grounded-vision-language-framework-to-improve-clinical-trust-and-auditability-in-automated-cancer-referral-processing
- 一句话贡献：提出RAPTOR+多模态框架，通过微调视觉语言模型实现端到端转诊单理解与视觉证据定位，显著提升癌症转诊处理的临床可审计性。
- 核心创新点：
  - 用视觉语言模型（VLM）替代OCR+LLM分阶段流程，实现端到端转诊理解，避免手写体、版式变化和视觉证据丢失问题
  - 提出grounding-aware评估框架，同时度量提取准确率和证据定位的严格安全性
  - 针对紧急疑似结直肠癌转诊处理中手动审查和转录瓶颈，首次将多模态VLM用于半结构化临床文档的端到端理解
  - 聚焦临床信任和可审计性，而非仅提高提取准确率
  - 发现零样本VLM存在严重grounding gap（如Gemini 2.5 Flash 92.6%阅读准确率但仅1.2%严格安全性）
- 和已有工作的区别：原RAPTOR依赖OCR预处理，无法处理手写体与布局变化且丧失视觉证据链接；RAPTOR+将视觉理解与结构化提取统一在VLM中，并首创兼顾准确性与证据定位的评估。
- 阅读启发：将VLM微调应用于临床转诊单可同时实现高精度提取和可追溯的视觉证据，是构建可信医疗AI系统的可行路径。
- 可信度：high

### 8. MedFM-Robust: Benchmarking Robustness of Medical Foundation Models
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.19027v3-medfm-robust-benchmarking-robustness-of-medical-foundation-models
- 一句话贡献：提出了首个面向医学基础模型鲁棒性的综合基准，包含40种扰动类型（12基础+28医学特定），覆盖八种成像模态，系统评估了五个视觉-语言模型和两个分割模型，揭示了微调策略、医学特定扰动和模型类型对鲁棒性的不同影响。
- 核心创新点：
  - 构建了包含40种扰动类型的鲁棒性基准，其中28种为医学特定扰动（如病理染色变化、设备噪声等）。
  - 覆盖八种医学成像模态（X光、CT、MRI、超声等），评估了五种视觉-语言模型（VQA、视觉定位、描述）和两种分割模型（五种微调策略）的鲁棒性。
  - 揭示了LoRA微调相比全微调导致近两倍的性能退化，而SAM-Med2D的Adapter实现了效率与鲁棒性的平衡。
  - 发现医学特定扰动对分割模型的损害尤为显著（9/15最严重扰动为领域特定）。
  - 首次系统性地评估医学基础模型在真实世界扰动下的鲁棒性，填补了该领域评估缺失的空白。
- 和已有工作的区别：现有工作主要关注医学基础模型在干净数据上的性能，缺乏对真实世界扰动的系统评估。本工作构建了首个跨模态、多任务、多扰动的鲁棒性基准，并提供了细粒度的部署指南。
- 阅读启发：医学基础模型的鲁棒性高度依赖于微调策略和任务类型，选择合适微调方法（如全微调或SAM-Med2D的Adapter）和模型（如MedGemma）可提升实际部署的可靠性；医学特定扰动应成为评估标准的一部分。
- 可信度：high

### 9. PromptRad: Knowledge-Enhanced Multi-Label Prompt-Tuning for Low-Resource Radiology Report Labeling
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.20052v1-promptrad-knowledge-enhanced-multi-label-prompt-tuning-for-low-resource-radiology-report-labeling
- 一句话贡献：提出PromptRad，一种知识增强的多标签提示调优方法，通过将多标签分类转化为掩码语言建模并利用UMLS同义词增强词汇表，在低资源放射学报告标注中仅需少量标注数据即可取得优异性能。
- 核心创新点：
  - 将多标签分类重新表述为掩码语言建模任务，无需附加分类层
  - 引入UMLS Metathesaurus中的同义词构建多词verbalizer，增强类别表示
  - 在低资源设置下通过提示调优微调预训练语言模型，显著降低标注数据需求
  - 针对放射学报告标注中标注数据稀缺的低资源场景
  - 现有规则方法和微调方法分别受限于描述多样性和数据需求大的问题
- 和已有工作的区别：与现有基于规则或传统微调的方法不同，PromptRad通过提示调优无需额外分类层，且利用UMLS医学知识库构建多词verbalizer，在极少标签数据下仍能有效进行多标签分类。
- 阅读启发：PromptRad展示了在数据稀缺的临床场景中，通过知识增强的提示调优可以高效地实现放射学报告多标签标注，且性能可与大型模型媲美。
- 可信度：high

### 10. RoboSurg-VQA: A Multimodal Benchmark for Surgical Segmentation-Aware Visual Question Answering
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.23068v1-robosurg-vqa-a-multimodal-benchmark-for-surgical-segmentation-aware-visual-question-answering
- 一句话贡献：提出RoboSurg-VQA，首个融合分割感知的机器人手术视觉问答基准，通过重用公共分割数据集和约束提示自动标注，实现临床相关问题的标准化评估。
- 核心创新点：
  - 设计分割感知的VQA任务，将分割掩码融入问答过程
  - 通过约束提示自动生成候选答案并辅以人工审计，实现高效标注
  - 构建统一的模式将多个公共手术分割数据集转化为VQA格式
  - 首次定义手术场景下分割感知的视觉问答问题设置
  - 涵盖程序上下文、解剖结构、成像方式、伪影、图像质量等临床相关问题类别
- 和已有工作的区别：现有手术VQA工作未利用分割信息，且依赖人工标注；本工作通过重用分割数据集和自动标注，实现了更大规模、更全面的临床问题覆盖。
- 阅读启发：RoboSurg-VQA为手术视觉理解提供了标准化基准，强调了分割感知在VQA中的重要性，并展示了自动标注的有效性。
- 可信度：high

### 11. What Makes a Medical Checker Trainable? Diagnosing Signal Collapse and Reward Hacking in Checker-Guided RAG for Biomedical QA
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.25988v1-what-makes-a-medical-checker-trainable-diagnosing-signal-collapse-and-reward-hacking-in-checker-guided-rag-for-biomedical-qa
- 一句话贡献：发现医学RAG中NLI检查器的输出分布而非准确率决定其作为GRPO奖励的可训练性，并诊断出信号坍缩与奖励破解两种失效模式。
- 核心创新点：
  - 对比四种NLI后端（LLM对数概率、MedNLI分类器等）作为过程奖励，揭示其训练梯度差异
  - 定义并诊断信号坍缩：LLM对数概率标签>97%为中性，导致梯度归零
  - 发现奖励破解的三步级联：强信号→超短答案→搜索回避→语言崩溃
  - 提出适度信号（校准分类器）优于强信号，提升12% BERTScore且无GPT依赖
  - 将NLI检查器从评估工具转为GRPO训练中的过程奖励，解决医学RAG的事实一致性强化学习问题
- 和已有工作的区别：以往研究关注检查器的准确率对下游任务的影响，本文首次揭示训练中输出分布（而非准确率）决定其可训练性，并系统分析信号坍缩与奖励破解两种失效机制。
- 阅读启发：设计奖励模型时，应优先考虑输出分布是否产生有信息量的梯度，避免过度追求信号强度，并注意策略对信号强度的调节作用。
- 可信度：high

### 12. BalanceRAG: Joint Risk Calibration for Cascaded Retrieval-Augmented Generation
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.20084v1-balancerag-joint-risk-calibration-for-cascaded-retrieval-augmented-generation
- 一句话贡献：提出BalanceRAG，通过二维网格序列图检验联合校准级联RAG中LLM-only和RAG分支的不确定度阈值，在控制系统级错误率的同时提高覆盖率并减少不必要的检索调用。
- 核心创新点：
  - 将级联RAG的两个分支不确定度阈值视为二维网格上的操作点，使用序列图检验联合校准
  - 从逐阶段风险校准扩展到多风险校准，同时约束检索使用率和选择条件风险
  - 采用风险自适应阈值对，在满足预设风险水平下最大化接受样本数
  - 首次将级联RAG的校准问题定义为两个分支阈值的联合风险校准，而非逐阶段独立校准
  - 提出控制系统级错误率（而非分支级错误率）的校准框架
- 和已有工作的区别：现有级联RAG采用逐阶段独立校准（保守且可能过度拒绝），本文首次提出联合校准阈值对，通过2D序列图检验实现系统级风险控制，且支持多风险约束。
- 阅读启发：学习了一种可证明的风险自适应级联RAG校准方法，有效权衡LLM-only与RAG的使用，降低检索成本而不牺牲可靠性。
- 可信度：high

### 13. VRXU-net: A Deep Learning Approach for Brain Ischemic Stroke Lesion Detection and Segmentation in T1W MRI
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.21633v1-vrxu-net-a-deep-learning-approach-for-brain-ischemic-stroke-lesion-detection-and-segmentation-in-t1w-mri
- 一句话贡献：提出VRXU-net，通过改进VGG检测切片级病灶、残差U-Net分割、三平面融合及预分类器过滤，在T1W MRI上实现高精度脑缺血性卒中病变检测与分割。
- 核心创新点：
  - 使用改进VGG模型对2D切片进行病灶检测，筛选出包含病变的切片，减少无效分割。
  - 采用带残差块的U形网络对每个切片进行分割，提高特征提取能力。
  - 独立处理轴向、矢状、冠状三平面，融合三平面分割结果以提升定位准确性。
  - 分割模型输出反馈给分类模型，降低假阳性预测。
  - 将3D MRI分解为2D切片处理，降低模型复杂度并利用多平面信息。
- 和已有工作的区别：现有方法通常直接对3D图像进行分割或使用单一平面信息，VRXU-net创新性地结合了切片级检测、残差U-Net分割、三平面融合以及分类-分割反馈循环，有效应对病变多样性并提升效率。
- 阅读启发：该工作展示了如何通过两阶段框架和多平面融合策略，在数据有限且病变特征模糊的医学影像分析任务中取得显著性能提升。
- 可信度：high

### 14. ImPartial: Multi-channel Whole-Cell Segmentation using Partial Annotations
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24128v1-impartial-multi-channel-whole-cell-segmentation-using-partial-annotations
- 一句话贡献：提出ImPartial框架，利用稀疏涂鸦和自监督多通道量化插值，仅需部分标注即可实现与全监督相当的多通道细胞分割性能。
- 核心创新点：
  - 提出自监督多通道量化插值目标，替代像素级重建，更好地对齐分割目标
  - 利用稀疏涂鸦作为部分标注，结合有限监督训练
  - 针对多通道可变配置的细胞成像数据，解决标注稀缺问题
  - 适用于低标注场景下的整体细胞分割
  - 在多重成像和单通道明场免疫组化数据集上，仅用部分标注达到与全监督相当的SOTA性能
- 和已有工作的区别：现有方法依赖密集像素标注，而ImPartial仅需稀疏涂鸦即可达到同等性能，并通过自监督量化插值增强分割目标。
- 阅读启发：展示了在医学图像分割中利用部分标注和自监督学习的有效性，显著降低标注成本。
- 可信度：high

### 15. Med-R2: An Adversarial Benchmark for Evidence-Grounded Reasoning in Medical VLMs
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24492v1-med-r2-an-adversarial-benchmark-for-evidence-grounded-reasoning-in-medical-vlms
- 一句话贡献：提出Med-R2 Bench，首个层级化对抗性基准，系统评估医学VLM在四个临床阶段中基于视觉证据的推理鲁棒性。
- 核心创新点：
  - 设计四级临床工作流（如影像获取、病灶检测、诊断、治疗）对应的层级化QA任务，评估推理链是否严格依赖视觉证据
  - 引入对抗性扰动（如添加误导性视觉线索）测试模型对虚假先验的抵抗能力
  - 构建大规模数据集：42,432张图像、31个任务类别、110,406个问答对
  - 提出Stepwise Fine-tuning方法，利用层级数据渐进微调提升推理鲁棒性
  - 首次聚焦医学VLM的基于证据的推理（而非简单VQA准确率），揭示模型是否依赖虚假先验
- 和已有工作的区别：现有基准多关注通用VQA或单任务性能，而Med-R2 Bench强调推理链的视觉证据约束，并通过层级化和对抗性设计深入分析模型弱点。
- 阅读启发：读者应认识到当前医学VLM在基于证据推理上的脆弱性，以及层级化对抗性数据微调是提升鲁棒性的有效方向。
- 可信度：high

### 16. Thinking in Scales: Accelerating Gigapixel Pathology Image Analysis via Adaptive Continuous Reasoning
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.19491v2-thinking-in-scales-accelerating-gigapixel-pathology-image-analysis-via-adaptive-continuous-reasoning
- 一句话贡献：提出PathCTM模型，通过从低倍到高倍的动态自适应连续推理和证据足够时的早停机制，大幅减少病理图像分析的计算开销，同时保持诊断精度。
- 核心创新点：
  - 将诊断推理建模为动态序列信息追求，渐进式从低倍全局到高倍局部转换
  - 使用条件计算和注意力引导的区域剪枝实现动态尺度切换
  - 引入置信度感知的早停机制，在不确定性充分降低时终止推理
  - 针对传统MIL方法穷举高倍patch处理导致计算效率低下的问题，提出无需穷举所有patch的连续推理范式
  - 在保持AUC不下降的前提下，减少95.95%的所需图像patch
- 和已有工作的区别：与标准MIL方法不同，PathCTM不预先固定高倍patch提取，而是动态决定何时切换到高倍、何时终止，实现token高效利用。
- 阅读启发：提供了一种可扩展的gigapixel病理图像分析新思路，通过自适应连续推理显著提升效率，有助于大规模临床部署。
- 可信度：high

### 17. Cardiac fat segmentation using computed tomography and an image-to-image conditional generative adversarial neural network
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.20064v1-cardiac-fat-segmentation-using-computed-tomography-and-an-image-to-image-conditional-generative-adversarial-neural-network
- 一句话贡献：首次将图像到图像的条件生成对抗网络pix2pix应用于心脏CT图像中两种类型脂肪（心外膜和纵隔）的自动分割，实现了高精度和实时处理。
- 核心创新点：
  - 采用pix2pix条件生成对抗网络进行心脏脂肪分割，该网络原本用于图像翻译任务，而非医学分割，作者验证了其在分割任务上的有效性
  - 实现同时分割心外膜脂肪和纵隔脂肪两种类型，被心包隔开
  - 将条件GAN引入心脏脂肪分割任务，替代传统手工或基于规则的方法，减少医生工作量
  - 聚焦于两种空间分离的脂肪类型，提升了分割的精细度
  - 心外膜脂肪分割准确率99.08%、F1分数98.73；纵隔脂肪准确率97.90%、F1分数98.40
- 和已有工作的区别：与现有心脏脂肪分割方法相比，本方法在F1分数和运行时间上表现更优，且能同时处理两种脂肪类型，而非单一类型。
- 阅读启发：条件GAN（如pix2pix）可用于医学图像分割任务，并在心脏脂肪分割上取得高精度和实时性能，为临床量化分析提供高效工具。
- 可信度：high

### 18. Divide-and-Conquer Inference for Large-Scale Visual Recognition with Multimodal Large Language Models
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/202605/26/2605.24799v1-divide-and-conquer-inference-for-large-scale-visual-recognition-with-multimodal-large-language-models
- 一句话贡献：提出分而治之推理（DCI），一种无需额外训练、即插即用的测试时扩展策略，通过递归分解和动态剪枝解决多模态大语言模型在长序列识别中的性能崩溃问题。
- 核心创新点：
  - 揭示多模态大语言模型在长序列识别中的性能崩溃现象，并从信息论角度归因于注意力稀释和衰减
  - 提出Divide-and-Conquer Inference (DCI)，递归将全局分类任务分解为多个简单的局部子问题
  - 设计动态剪枝机制压缩搜索空间，提升局部信噪比
  - 实现模型无关、即插即用的测试时扩展，无需额外训练或微调
  - 首次系统性研究多模态大语言模型在大规模图像分类中随着标签空间扩展的性能退化问题
- 和已有工作的区别：现有工作通常针对短序列或小规模类别优化，DCI是首个面向大规模长序列场景的测试时分治推理策略，直接缓解注意力稀释导致的性能崩溃。
- 阅读启发：本工作提供了一种高效、通用的测试时扩展方法，使轻量级多模态大语言模型无需训练即可在大规模分类任务上达到先进水平，强调了通过推理策略创新突破模型容量瓶颈的潜力。
- 可信度：medium

### 19. Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.22414v1
- 一句话贡献：提出FundusGround基准，通过空间定位的病变证据实现临床可解释的眼科VQA。
- 核心创新点：
  - 构建三阶段流水线收集10,719张眼底图像并精确标注15,595个病变
  - 使用ETDRS网格将病变空间定位到九个临床视网膜区域
  - 生成涵盖四种格式的72,706个问题（开放/封闭/单选/多选）
  - 设计双指标评估：答案准确性和病变级推理能力
  - 首次将空间定位的病变证据作为VQA的显式视觉线索，提升临床可解释性
- 和已有工作的区别：现有眼科VQA基准只关注答案准确性，而本工作强调提供空间定位的病变证据以实现可解释性。
- 阅读启发：将病变空间定位融入VQA是构建可靠、可解释眼科AI辅助系统的关键。
- 可信度：high

### 20. PrivFusion: A Privacy-preserving Multi-Agent Framework for Harmonizing Distributed Datasets
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.24249v1
- 一句话贡献：提出PrivFusion，一个隐私保护的多智能体框架，在联邦学习前自动协调异质数据集，减少手动工作。
- 核心创新点：
  - 使用多智能体分析本地数据并聚类跨站点的语义相似特征
  - 迭代提供转换建议直至数据对齐
  - 将数据协调作为联邦学习的隐私保护前置步骤
  - 明确将结构化数据集的协调视为联邦学习的必要前置条件
  - 针对联邦学习中数据集异质性问题提出自动化解决方案
- 和已有工作的区别：现有联邦学习工作通常忽略数据协调或依赖手动操作，PrivFusion首次提出自动化、隐私保护的协调框架。
- 阅读启发：自动数据协调可大幅降低联邦学习中数据异质性的障碍，提升多站点分析可行性。
- 可信度：high

### 21. Parameter-Efficient VLMs for Gastrointestinal Endoscopy: Medical Image Generation and Clinical Visual Question Answering
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.24792v1
- 一句话贡献：提出双管道PEFT模型，结合Florence-2进行医学VQA和LoRA Stable Diffusion生成隐私保护合成内窥镜图像，显著降低计算成本并提升性能。
- 核心创新点：
  - 采用PEFT微调Florence-2模型实现高可解释性医学VQA，计算成本大幅降低
  - 使用LoRA技术微调Stable Diffusion 2.1生成高质量合成GI内窥镜图像，保护患者隐私
  - 双管道框架同时优化VQA和合成数据生成任务
  - 针对GI内窥镜AI面临的数据标注不足、隐私政策和微调效率瓶颈
  - 同时解决医学VQA和隐私保护合成数据生成两个关键问题
- 和已有工作的区别：区别于传统全参数微调的高计算开销，本文采用PEFT实现高效微调；相比其他合成图像方法（如FLUX），本文通过LoRA获得更优的图像-文本对齐（更低FBD），同时确保隐私保护。
- 阅读启发：PEFT和LoRA能够高效应用于医学内窥镜领域，缓解数据隐私和标注短缺，同时提升VQA性能，为临床AI实用化提供可行方案。
- 可信度：high

### 22. Universal Boosts, Specific Suppressors: Sparse Autoencoder Steering of Medical Vision-Language Models
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.24977v1
- 一句话贡献：提出基于稀疏自编码器的推理时残差引导方法，通过抑制和增强特定特征来减少医疗视觉语言模型的幻觉，且增强方向跨模型通用，抑制方向需模型特化。
- 核心创新点：
  - 首次将Top-K稀疏自编码器应用于医疗视觉语言模型的解码时引导
  - 提出基于因果临床错误的token级残差干预，无需权重更新
  - 发现增强（boost）方向在多个架构间高度重叠，而抑制（suppress）方向为模型特有
  - 针对医疗VLM报告生成中的幻觉问题，采用推理时引导而非训练或微调
  - 定义并识别出通用增强特征和模型特定抑制特征，指导不同模型的迁移策略
- 和已有工作的区别：现有工作多通过训练或微调缓解幻觉，本方法仅需推理时干预；且先前引导技术通常假设方向可迁移，本文揭示了抑制方向具有模型特异性，为迁移提供新见解。
- 阅读启发：稀疏自编码器可以有效分离医疗VLM中的通用增强特征和模型特定抑制特征，从而实现轻量级、可迁移的幻觉缓解。
- 可信度：high

### 23. Towards Reliable Fetal Ultrasound Interpretation with Multi-Agent Collaboration
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.25357v1
- 一句话贡献：提出FetUSAgents，一个工具增强的多智能体系统，通过多智能体协作和双路径证据仲裁实现可靠的胎儿超声自动解释，并构建了专用的FetUS-VQA基准。
- 核心创新点：
  - 提出Dual-Path Evidence Arbitration (DPEA)，整合LLM deliberative推理与结构化计算证据
  - 设计检索增强的证据银行，汇聚中间发现以支持可追溯的临床结论
  - 构建多智能体协作框架，通过协调任务特定视觉工具分解临床查询为子任务
  - 从单任务单模型转向多智能体协作范式，解决多步骤超声解释中的系统集成问题
  - 针对胎儿超声分析中MLLM的领域知识不足和幻觉风险，提出证据驱动的可靠方案
- 和已有工作的区别：不同于以往的“单任务单模型”范式，本文提出多智能体协作系统，通过工具增强和双路径证据仲裁克服MLLM在特定领域的限制，实现更可靠且可解释的胎儿超声分析。
- 阅读启发：多智能体协作框架结合结构化证据与LLM推理可显著提高医疗影像分析的可信度和准确性，为开发临床级智能助手提供可扩展方案。
- 可信度：high

### 24. EchoPilot: Training-Free Ultrasound Video Segmentation via Scale-Space Semantic Prompting and Reliability-Gated Memory
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.25944v1
- 一句话贡献：提出EchoPilot，一个无需训练的超声视频分割框架，仅需单点点击和类别名称，通过尺度空间语义提示和可靠性门控记忆实现高精度分割。
- 核心创新点：
  - 提出Scale-Space Semantic Prompting，利用S.E.E.D.准则从VLM自动选择最佳上下文视图，并从VFM密集特征合成几何精确的辅助点提示，无需额外用户交互。
  - 引入Reliability-Gated Memory更新机制，根据预测不确定性选择性冻结记忆库，防止误差累积导致时序漂移。
  - 首个在稀疏首帧交互（单点点击+类别名称）设定下解决超声视频分割中的尺度模糊和时序漂移问题。
  - 贡献了第一个动态胎儿胎盘超声视频分割数据集，包含671个标注帧。
  - 在三个超声视频数据集上，EchoPilot在稀疏交互设定下达到SOTA，持续优于无需训练的基线和微调专家模型。
- 和已有工作的区别：现有可提示基础模型直接部署于超声分割不可靠，单点缺乏空间上下文导致尺度模糊，贪婪记忆更新放大早期错误；EchoPilot通过冻结VLM/VFM进行语义定位和几何特征提取，并选择性冻结记忆，解决了这些问题。
- 阅读启发：提供了一种无需训练即可利用现有视觉语言模型和基础模型进行鲁棒超声视频分割的有效范式，且新数据集可推动后续研究。
- 可信度：high

### 25. RAPTOR+: A Visually Grounded Vision-Language Framework to Improve Clinical Trust and Auditability in Automated Cancer Referral Processing
- 区域：deep；分数：9.0
- 原文链接：https://arxiv.org/abs/2605.25956v1
- 一句话贡献：提出RAPTOR+，利用视觉-语言模型实现临床转诊表格的端到端理解，并引入接地感知评估框架，显著提升可验证证据定位能力。
- 核心创新点：
  - 使用VLM替代OCR+LLM管道，实现端到端的临床文档理解，消除对单独OCR阶段的依赖
  - 引入接地感知评估框架，同时衡量提取准确性和证据定位（Strict Safety指标）
  - 对开源VLM进行任务特定微调，在真实临床表格上实现高精度与高证据可溯性
  - 针对癌症紧急转诊处理中半结构化文档的视觉证据丢失问题，提出多模态解决方案
  - 定义且解决了零样本VLM在临床场景下的'接地鸿沟'（高读取准确率但低严格安全性）
- 和已有工作的区别：相比原RAPTOR系统（OCR+LLM）和现有零样本VLM方法，RAPTOR+通过端到端VLM微调与接地评估，首次实现了临床转诊处理中提取决策与视觉证据的可审计链接。
- 阅读启发：对于临床文档理解等高风险场景，任务特定微调VLM是获得可靠、可审计结果的关键，零样本模型在证据定位上严重不足。
- 可信度：high

### 26. MedFM-Robust: Benchmarking Robustness of Medical Foundation Models
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/2605.19027v3
- 一句话贡献：构建首个涵盖40种扰动（含28种医学特定）的医学基础模型鲁棒性基准，揭示微调策略比模型架构更影响鲁棒性，并发现医学特定扰动对分割任务破坏性最大。
- 核心创新点：
  - 提出28种医学特定扰动类型（如病灶遮挡、造影剂变化等），覆盖8种成像模态
  - 设计包含VQA、视觉定位、分割、描述的多任务鲁棒性评估框架
  - 系统对比5种VLM和2种分割模型的5种微调策略的鲁棒性差异
  - 首次聚焦医学基础模型在真实世界扰动下的鲁棒性，而非仅关注干净数据性能
  - 定义医学特定扰动分类（成像参数、解剖变异、临床操作等），填补领域空白
- 和已有工作的区别：现有基准（如ImageNet-C）仅关注自然图像通用扰动，本文首次系统评估医学领域特定扰动对预训练基础模型的影响，并揭示微调策略的关键作用。
- 阅读启发：部署医学基础模型时需优先选择鲁棒微调策略（如Adapter），并针对具体任务进行医学特定扰动测试，不能直接迁移自然图像的鲁棒性结论。
- 可信度：high

### 27. BalanceRAG: Joint Risk Calibration for Cascaded Retrieval-Augmented Generation
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/2605.20084v1
- 一句话贡献：提出BalanceRAG方法，实现级联RAG系统中LLM-only和RAG分支的联合风险校准，通过二维格点序列图形测试识别安全阈值对，在控制系统级错误率的同时提高覆盖率和检索效率。
- 核心创新点：
  - 将级联RAG的两个分支的不确定性阈值视为二维格点上的操作点，利用序列图形测试识别满足风险水平的安全阈值对
  - 提出风险自适应阈值校准方法，控制系统级错误率（接受的样本中的错误比例），同时保留更多样本
  - 扩展到多风险校准，同时约束检索使用率和选择条件风险
  - 针对级联RAG系统（先尝试LLM-only，不确定时再使用RAG）中传统的逐阶段保守校准问题，提出联合校准视角
  - 将阈值校准建模为二维操作点的选择问题，而非独立优化每个阶段的阈值
- 和已有工作的区别：之前的工作通常独立设置LLM-only和RAG阶段的阈值（如基于置信度或熵），导致逐阶段保守决策；本工作首次联合优化两个分支的阈值，通过二维空间中的统计测试实现系统级风险控制。
- 阅读启发：级联RAG可以通过联合风险校准显著提升效率与可靠性的平衡，为实际部署提供一种自适应、可量化的阈值调节方法。
- 可信度：high

### 28. Thinking in Scales: Accelerating Gigapixel Pathology Image Analysis via Adaptive Continuous Reasoning
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/2605.19491v2
- 一句话贡献：提出PathCTM，一种通过自适应连续尺度推理实现gigapixel病理图像高效分析的token高效方法，大幅降低计算开销而不损失精度。
- 核心创新点：
  - 将诊断推理建模为动态序列信息追求，从低倍全局到高倍局部渐进过渡。
  - 条件计算驱动的动态尺度切换与注意力引导区域剪枝，只处理关键区域。
  - 置信度感知的提前停止机制，在证据充分时自适应终止推理。
  - 首次将WSI分析从静态特征聚合转变为动态连续推理，模拟病理医生由粗到细的诊断过程。
  - 相比标准MIL方法，所需的图像块数量减少95.95%，推理时间缩短约95.62%，同时AUC无下降。
- 和已有工作的区别：传统MIL方法需对所有高倍patch进行穷举处理，PathCTM通过动态尺度选择和提前终止实现高效推理，计算量降低两个数量级。
- 阅读启发：PathCTM为超大病理图像分析提供了高效新范式，显著降低计算需求，有望推动临床实时应用。
- 可信度：high

### 29. PromptRad: Knowledge-Enhanced Multi-Label Prompt-Tuning for Low-Resource Radiology Report Labeling
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/2605.20052v1
- 一句话贡献：提出PromptRad，一种将多标签分类重构为掩码语言建模并融合UMLS同义词知识的低资源放射学报告标注方法，仅需32个标注样本即可超越基线和接近GPT-4性能。
- 核心创新点：
  - 将多标签分类问题转化为掩码语言建模任务，无需额外分类层
  - 设计多词动词化器，整合UMLS元词表中的同义词以丰富类别语义表示
  - 利用提示调优在低资源场景下高效微调预训练语言模型
  - 聚焦低资源放射学报告标注，仅需少量标注数据（如32个样本）
  - 解决传统规则方法难以应对临床多样化描述以及微调PLM需要大量标注数据的矛盾
- 和已有工作的区别：不同于传统微调需要大量标注数据和额外分类头，以及基于规则方法无法处理多样描述，PromptRad通过提示调优和UMLS知识增强实现低资源高效标注。
- 阅读启发：提示调优结合医学知识库（如UMLS同义词）可以显著降低放射学报告标注对标注数据的需求，为数据稀缺的临床场景提供实用解决方案。
- 可信度：high

### 30. VRXU-net: A Deep Learning Approach for Brain Ischemic Stroke Lesion Detection and Segmentation in T1W MRI
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/2605.21633v1
- 一句话贡献：提出VRXU-net，通过先分类后分割的序列框架和多平面聚合策略，实现T1W MRI中缺血性卒中病灶的高效准确检测与分割。
- 核心创新点：
  - 设计VRXU-net架构，融合视觉特征、残差连接和U型网络。
  - 采用先分类后分割的序列化框架：用改进VGG分类器筛选非病灶切片，再由带残差块的U型分割模型处理，减少无效计算并提升速度。
  - 独立处理轴向、矢状、冠状三个解剖平面的2D切片，然后聚合三个平面的分割结果，提升定位精度。
  - 利用分割输出反馈优化分类模型，减少假阳性预测。
  - 针对T1W MRI中缺血性卒中病灶形状、大小、位置多变且与周围脑组织相似导致的检测分割难题。
- 和已有工作的区别：与直接进行3D分割或单平面分割的方法不同，本文采用先分类后分割的序列框架，仅在确认存在病灶的切片上进行分割，并结合多平面聚合，提高了效率和准确性。
- 阅读启发：本文展示了一种结合分类与分割、多平面聚合的端到端流程，可有效克服病灶多样性带来的挑战，为临床缺血性卒中病灶分割提供了实用且高效的解决方案。
- 可信度：high

### 31. Cardiac fat segmentation using computed tomography and an image-to-image conditional generative adversarial neural network
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/2605.20064v1
- 一句话贡献：将原本用于图像翻译的pix2pix条件生成对抗网络应用于心脏脂肪（心外膜和纵隔）的自动分割，实现了高精度和实时处理。
- 核心创新点：
  - 首次将pix2pix网络应用于心脏脂肪分割任务，该网络原本设计用于图像到图像翻译
  - 提出了端到端的深度学习框架，无需手工特征或传统分割步骤
  - 实现了心外膜和纵隔两种类型脂肪的同步分割与量化
  - 针对心脏脂肪分割任务，将问题建模为条件图像生成，而非传统的像素分类或U-Net分割
  - 解决了手动分割耗时且缺乏自动化的问题，提出实时分割的可能性
- 和已有工作的区别：现有方法多基于U-Net等传统分割网络，而本研究首次采用条件GAN（pix2pix）进行心脏脂肪分割，无需手工设计特征，且同时处理两种脂肪类型，性能更优且速度更快。
- 阅读启发：条件生成对抗网络不仅可以用于图像翻译，也可有效迁移至医学图像分割任务，尤其是当分割目标具有明确空间结构时，能获得高精度和实时推理。
- 可信度：high

### 32. RoboSurg-VQA: A Multimodal Benchmark for Surgical Segmentation-Aware Visual Question Answering
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/2605.23068v1
- 一句话贡献：提出了首个融合分割感知的机器人手术视觉问答基准RoboSurg-VQA，通过复用公共分割数据集并设计临床动机的多维度问答任务，解决了手术场景中退化视图下的可靠性评估问题。
- 核心创新点：
  - 基于现有手术分割数据集，通过统一模式自动构建结构化VQA数据对，降低标注成本
  - 设计包含程序上下文、解剖结构、成像模态、手术伪影、图像质量等6类临床相关问题的固定问答集
  - 采用约束提示生成候选答案，结合自动有效性检查和人工审核的混合标注流水线
  - 首次将语义分割信息显式融入手术VQA任务，提出分割感知的VQA基准
  - 覆盖遮挡、烟雾、出血、镜面高光等退化视图条件，贴近临床实际
- 和已有工作的区别：以往手术VQA工作多基于通用场景或小规模标注数据，缺乏对语义分割的显式利用和对退化视图的系统评估；本工作通过复用分割数据集并设计针对性问答任务，在数据效率和临床相关性上实现突破。
- 阅读启发：RoboSurg-VQA为手术视觉理解提供了一个结构化、可扩展、临床驱动的评估工具，同时展示了利用已有分割数据进行零样本标注VQA的可行路径。
- 可信度：high

### 33. ImPartial: Multi-channel Whole-Cell Segmentation using Partial Annotations
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/2605.24128v1
- 一句话贡献：提出了ImPartial框架，使用稀疏涂鸦部分标注实现多通道细胞分割，性能与全监督相当。
- 核心创新点：
  - 引入自监督多通道量化插补（self-supervised multi-channel quantized imputation）机制，避免像素级重建，通过分类目标增强分割。
  - 在低标注条件下，结合稀疏涂鸦和有限监督，实现与全监督相当的分割性能。
  - 针对多通道可变配置的病理图像，提出在部分标注（稀疏涂鸦）下进行细胞分割的新问题设定。
  - 在多个基准数据集（多通道细胞成像和单通道临床IHC）上，仅需少量标注即达到全监督水平，并持续优于强基线。
  - 提供了公开基准数据集和代码。
- 和已有工作的区别：现有方法依赖密集像素级标注，而ImPartial利用稀疏涂鸦和自监督量化插补，无需完美重建或去噪，降低标注成本。
- 阅读启发：在标注稀缺的生物医学影像场景中，自监督量化插补是一种有效的部分监督策略，可显著减少人工标注需求而不牺牲精度。
- 可信度：high

### 34. Divide-and-Conquer Inference for Large-Scale Visual Recognition with Multimodal Large Language Models
- 区域：quick；分数：6.0
- 原文链接：https://arxiv.org/abs/2605.24799v1
- 一句话贡献：提出一种分治推理（DCI）策略，通过递归分解和动态剪枝，在不训练微调的情况下缓解MLLM在大规模分类中的性能崩溃，提升准确率和推理速度。
- 核心创新点：
  - 识别了MLLM在长序列识别中的Performance Collapse现象，并通过信息论分析揭示其源于注意力稀释与衰减导致信噪比不足
  - 提出Divide-and-Conquer Inference (DCI)测试时缩放策略，将全局分类递归分解为多个局部子问题
  - 引入动态剪枝机制压缩搜索空间，提高局部信噪比并加速推理
  - 首次系统研究MLLM在大规模标签空间下的性能退化问题，定义为Performance Collapse
  - 将分治思想应用于MLLM推理阶段，无需额外训练即可提升大尺度视觉识别能力
- 和已有工作的区别：现有工作多关注MLLM的预训练或微调，而DCI是模型无关的即插即用推理策略，通过测试时动态分解与剪枝解决长序列注意力稀释问题。
- 阅读启发：分治推理是一种高效、无需训练的大规模视觉识别增强手段，可缓解长上下文中注意力退化的问题。
- 可信度：high

### 35. What Makes a Medical Checker Trainable? Diagnosing Signal Collapse and Reward Hacking in Checker-Guided RAG for Biomedical QA
- 区域：quick；分数：8.0
- 原文链接：https://arxiv.org/abs/2605.25988v1
- 一句话贡献：发现医疗RAG中NLI检查器的输出分布而非准确率决定其训练梯度是否有效，并诊断出信号崩溃、奖励黑客和策略依赖性三种现象。
- 核心创新点：
  - 区分了检查器输出分布（log概率）与精度的作用，发现log概率分布均匀性决定梯度可用性
  - 提出信号崩溃现象：LLM log概率打分导致超过97%的样本为中性，梯度消失
  - 发现奖励黑客三级级联：超短答案、回避搜索、语言崩溃，由强信号检查器触发
  - 揭示信号强度的策略依赖性：同一检查器在不同策略模型下表现不同，可能避免奖励黑客级联
  - 将NLI检查器作为过程奖励用于GRPO训练医疗RAG，而非仅做最终验证
- 和已有工作的区别：以往工作多关注检查器的准确率或直接用作奖励，本文首次诊断检查器输出分布特性（信号强度）对训练可用的关键影响，并发现强信号反而导致奖励黑客的悖论。
- 阅读启发：设计可训练检查器时，应关注输出log概率的退化情况而非仅准确率，中等信号更稳健；同一检查器在不同基座模型上效果可能迥异。
- 可信度：high

### 36. Med-R2: An Adversarial Benchmark for Evidence-Grounded Reasoning in Medical VLMs
- 区域：quick；分数：7.0
- 原文链接：https://arxiv.org/abs/2605.24492v1
- 一句话贡献：提出Med-R2 Bench，首个与临床工作流对齐的分层对抗性基准，系统评估医学视觉语言模型在视觉证据基础上的推理鲁棒性。
- 核心创新点：
  - 构建了包含42,432张图像、31个任务类别和110,406个问答对的分层基准，覆盖四个临床阶段。
  - 设计了逐步QA任务和对抗性扰动，专门测试推理链是否严格基于视觉证据而非虚假关联。
  - 通过评估14个模型揭示了四阶段临床工作流中的性能逐级退化现象。
  - 定义了与临床工作流对齐的逐步证据基础推理任务，填补了医学VLM在对抗环境下推理鲁棒性评估的空白。
  - 发现模型严重依赖提示词猜测答案，即使提供明确视觉线索也难以精确对齐文本描述。
- 和已有工作的区别：不同于现有仅关注整体问答准确率的基准，Med-R2专注于对抗性环境下的视觉证据基础推理链评估，并与临床工作流深度对齐。
- 阅读启发：医学VLM在对抗性环境下存在严重的证据依赖缺陷，分层逐步微调是提升鲁棒性的有效策略。
- 可信度：high
