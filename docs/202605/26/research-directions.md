# 研究方向与二次创新路线 · 2026-05-26

- 生成时间：2026-05-27 08:17:39 UTC
- 当日论文数：36
- 方向数：2

## 今日方向总览

| 方向 | 论文数 | 代表论文 |
|---|---:|---|
| vlmmed | 18 | Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence<br>PrivFusion: A Privacy-preserving Multi-Agent Framework for Harmonizing Distributed Datasets<br>Parameter-Efficient VLMs for Gastrointestinal Endoscopy: Medical Image Generation and Clinical Visual Question Answering |
| ['keyword:VLMMed' | 18 | Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence<br>PrivFusion: A Privacy-preserving Multi-Agent Framework for Harmonizing Distributed Datasets<br>Parameter-Efficient VLMs for Gastrointestinal Endoscopy: Medical Image Generation and Clinical Visual Question Answering |

## 方向 1：vlmmed
该方向包含 18 篇论文，建议结合单篇创新点进一步细分子问题。

### 代表论文

- [Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence](https://arxiv.org/abs/202605/26/2605.22414v1-towards-clinically-interpretable-ophthalmic-vqa-via-spatially-grounded-lesion-evidence)：提出FundusGround基准，通过引入基于ETDRS网格的空间定位病变证据，实现临床可解释的眼科视觉问答。
- [PrivFusion: A Privacy-preserving Multi-Agent Framework for Harmonizing Distributed Datasets](https://arxiv.org/abs/202605/26/2605.24249v1-privfusion-a-privacy-preserving-multi-agent-framework-for-harmonizing-distributed-datasets)：提出PrivFusion，首个隐私保护多智能体框架，在联邦学习前自动协调异构医疗数据集，减少人工干预。
- [Parameter-Efficient VLMs for Gastrointestinal Endoscopy: Medical Image Generation and Clinical Visual Question Answering](https://arxiv.org/abs/202605/26/2605.24792v1-parameter-efficient-vlms-for-gastrointestinal-endoscopy-medical-image-generation-and-clinical-visual-question-answering)：提出双流水线PEFT框架，同时解决了胃肠内镜领域医疗VQA精度低和隐私保护合成数据生成两大难题，显著降低计算成本并提升性能。
- [Universal Boosts, Specific Suppressors: Sparse Autoencoder Steering of Medical Vision-Language Models](https://arxiv.org/abs/202605/26/2605.24977v1-universal-boosts-specific-suppressors-sparse-autoencoder-steering-of-medical-vision-language-models)：提出基于稀疏自编码器的解码时残差引导方法，通过逐token因果干预（提升正确特征、抑制错误特征）减少医学视觉语言模型的幻觉，无需权重更新，并发现提升方向跨模型通用、抑制方向模型特有。
- [Towards Reliable Fetal Ultrasound Interpretation with Multi-Agent Collaboration](https://arxiv.org/abs/202605/26/2605.25357v1-towards-reliable-fetal-ultrasound-interpretation-with-multi-agent-collaboration)：提出FetUSAgents，一种工具增强的多智能体系统，通过双路径证据仲裁（DPEA）和检索增强证据库实现可靠的胎儿超声解读，在VQA任务上超越最强基线25%以上。
- [EchoPilot: Training-Free Ultrasound Video Segmentation via Scale-Space Semantic Prompting and Reliability-Gated Memory](https://arxiv.org/abs/202605/26/2605.25944v1-echopilot-training-free-ultrasound-video-segmentation-via-scale-space-semantic-prompting-and-reliability-gated-memory)：EchoPilot提出一种无需训练的超声视频分割框架，通过尺度空间语义提示和可靠性门控记忆，仅需单点点击和类别名称即可实现高质量分割，并在三个数据集上达到最优性能。
- [RAPTOR+: A Visually Grounded Vision-Language Framework to Improve Clinical Trust and Auditability in Automated Cancer Referral Processing](https://arxiv.org/abs/202605/26/2605.25956v1-raptor-a-visually-grounded-vision-language-framework-to-improve-clinical-trust-and-auditability-in-automated-cancer-referral-processing)：提出RAPTOR+，一种利用微调视觉语言模型实现端到端癌症转诊表单理解与视觉证据定位的多模态框架，显著提升临床可审计性。
- [MedFM-Robust: Benchmarking Robustness of Medical Foundation Models](https://arxiv.org/abs/202605/26/2605.19027v3-medfm-robust-benchmarking-robustness-of-medical-foundation-models)：构建了医疗基础模型鲁棒性评估基准，涵盖40种扰动、8种模态，系统评估了5个VLM和2个分割模型，揭示了微调策略和领域特定扰动对鲁棒性的关键影响。
- [PromptRad: Knowledge-Enhanced Multi-Label Prompt-Tuning for Low-Resource Radiology Report Labeling](https://arxiv.org/abs/202605/26/2605.20052v1-promptrad-knowledge-enhanced-multi-label-prompt-tuning-for-low-resource-radiology-report-labeling)：提出PromptRad，一种知识增强的多标签提示调优方法，在低资源情况下将放射学报告标注转化为掩码语言建模，利用UMLS同义词丰富类别表示，仅需少量标注数据即可达到优异性能。
- [RoboSurg-VQA: A Multimodal Benchmark for Surgical Segmentation-Aware Visual Question Answering](https://arxiv.org/abs/202605/26/2605.23068v1-robosurg-vqa-a-multimodal-benchmark-for-surgical-segmentation-aware-visual-question-answering)：提出了 RoboSurg-VQA，一个面向机器人辅助手术的、分割感知的视觉问答基准，通过重用公共手术分割数据集并设计临床问题集与自动标注流水线，填补了该领域缺乏标准评估平台的空白。
- [What Makes a Medical Checker Trainable? Diagnosing Signal Collapse and Reward Hacking in Checker-Guided RAG for Biomedical QA](https://arxiv.org/abs/202605/26/2605.25988v1-what-makes-a-medical-checker-trainable-diagnosing-signal-collapse-and-reward-hacking-in-checker-guided-rag-for-biomedical-qa)：发现医学RAG中NLI检查器的输出分布而非准确率决定其作为RL奖励的可训练性，并诊断了信号坍缩和奖励破解问题。
- [BalanceRAG: Joint Risk Calibration for Cascaded Retrieval-Augmented Generation](https://arxiv.org/abs/202605/26/2605.20084v1-balancerag-joint-risk-calibration-for-cascaded-retrieval-augmented-generation)：提出BalanceRAG，通过二维网格上的序列图检验联合校准LLM-only和RAG分支的不确定度阈值，在控制系统级错误率的同时保留更多样本，并支持多风险校准。
- [VRXU-net: A Deep Learning Approach for Brain Ischemic Stroke Lesion Detection and Segmentation in T1W MRI](https://arxiv.org/abs/202605/26/2605.21633v1-vrxu-net-a-deep-learning-approach-for-brain-ischemic-stroke-lesion-detection-and-segmentation-in-t1w-mri)：提出VRXU-net，通过级联分类与分割、残差块、三平面融合及反馈机制，实现了T1W MRI中脑缺血性卒中病变的高效检测与分割。
- [ImPartial: Multi-channel Whole-Cell Segmentation using Partial Annotations](https://arxiv.org/abs/202605/26/2605.24128v1-impartial-multi-channel-whole-cell-segmentation-using-partial-annotations)：提出ImPartial框架，利用稀疏涂鸦部分标注和自监督多通道量化插值，在低标注场景下实现与全监督相当的细胞分割性能，大幅减少标注需求。
- [Med-R2: An Adversarial Benchmark for Evidence-Grounded Reasoning in Medical VLMs](https://arxiv.org/abs/202605/26/2605.24492v1-med-r2-an-adversarial-benchmark-for-evidence-grounded-reasoning-in-medical-vlms)：提出Med-R2 Bench基准，通过层级化对抗性评估揭示医学视觉语言模型在临床推理中依赖虚假先验而非视觉证据的问题，并提供层级微调方法提升推理鲁棒性。
- [Thinking in Scales: Accelerating Gigapixel Pathology Image Analysis via Adaptive Continuous Reasoning](https://arxiv.org/abs/202605/26/2605.19491v2-thinking-in-scales-accelerating-gigapixel-pathology-image-analysis-via-adaptive-continuous-reasoning)：提出PathCTM模型，通过自适应连续推理和早停机制，大幅减少全切片图像分析所需的patch数和推理时间，同时保持诊断精度。
- [Cardiac fat segmentation using computed tomography and an image-to-image conditional generative adversarial neural network](https://arxiv.org/abs/202605/26/2605.20064v1-cardiac-fat-segmentation-using-computed-tomography-and-an-image-to-image-conditional-generative-adversarial-neural-network)：提出将条件生成对抗网络(pix2pix)首次应用于心脏CT图像中两种脂肪(心外膜和纵隔)的自动分割，实现高精度与实时处理。
- [Divide-and-Conquer Inference for Large-Scale Visual Recognition with Multimodal Large Language Models](https://arxiv.org/abs/202605/26/2605.24799v1-divide-and-conquer-inference-for-large-scale-visual-recognition-with-multimodal-large-language-models)：提出分而治之推理（DCI），通过递归分解和动态剪枝，解决多模态大语言模型在大规模分类中的性能崩溃问题，提升准确率和推理速度。

### 共同创新点
- 提出FundusGround基准，通过引入基于ETDRS网格的空间定位病变证据，实现临床可解释的眼科视觉问答。
- 提出PrivFusion，首个隐私保护多智能体框架，在联邦学习前自动协调异构医疗数据集，减少人工干预。
- 提出双流水线PEFT框架，同时解决了胃肠内镜领域医疗VQA精度低和隐私保护合成数据生成两大难题，显著降低计算成本并提升性能。
- 提出基于稀疏自编码器的解码时残差引导方法，通过逐token因果干预（提升正确特征、抑制错误特征）减少医学视觉语言模型的幻觉，无需权重更新，并发现提升方向跨模型通用、抑制方向模型特有。

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

## 方向 2：['keyword:VLMMed'
该方向包含 18 篇论文，建议结合单篇创新点进一步细分子问题。

### 代表论文

- [Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence](https://arxiv.org/abs/2605.22414v1)：提出FundusGround基准，通过空间定位的病灶证据实现临床可解释的眼科VQA，并证明病灶级视觉证据能提升模型性能与透明度。
- [PrivFusion: A Privacy-preserving Multi-Agent Framework for Harmonizing Distributed Datasets](https://arxiv.org/abs/2605.24249v1)：提出PrivFusion，一个隐私保护的多智能体框架，在联邦学习前自动协调结构化的多站点异构数据集，减少人工标注和数据映射工作。
- [Parameter-Efficient VLMs for Gastrointestinal Endoscopy: Medical Image Generation and Clinical Visual Question Answering](https://arxiv.org/abs/2605.24792v1)：提出双管道PEFT框架，同时解决内窥镜临床VQA和隐私保护合成图像生成，显著降低计算成本并提升性能。
- [Universal Boosts, Specific Suppressors: Sparse Autoencoder Steering of Medical Vision-Language Models](https://arxiv.org/abs/2605.24977v1)：提出一种无需权重更新的解码时间残差导向方法，基于稀疏自编码器对医学视觉语言模型进行推理时干预，有效减少幻觉并提升报告质量，且发现增强方向可跨模型迁移而抑制方向需特定于模型。
- [Towards Reliable Fetal Ultrasound Interpretation with Multi-Agent Collaboration](https://arxiv.org/abs/2605.25357v1)：Automated fetal ultrasound interpretation requires a workflow from visual perception, including plane recognition and anatomical segmentation, to clinical understanding, including biometric measurement and diagnostic re...
- [EchoPilot: Training-Free Ultrasound Video Segmentation via Scale-Space Semantic Prompting and Reliability-Gated Memory](https://arxiv.org/abs/2605.25944v1)：提出无需训练的超声视频分割框架EchoPilot，仅需单点点击和类别名，通过尺度空间语义提示和可靠性门控记忆实现SOTA性能。
- [RAPTOR+: A Visually Grounded Vision-Language Framework to Improve Clinical Trust and Auditability in Automated Cancer Referral Processing](https://arxiv.org/abs/2605.25956v1)：提出RAPTOR+，利用微调视觉语言模型实现端到端的癌症转诊表单理解，并通过grounding感知评估框架证明其相比于零样本模型和OCR流水线在证据可定位性上的显著提升。
- [MedFM-Robust: Benchmarking Robustness of Medical Foundation Models](https://arxiv.org/abs/2605.19027v3)：提出了首个涵盖多模态、多扰动类型的医学基础模型鲁棒性基准，系统揭示了微调策略和医学特定扰动对性能的关键影响。
- [BalanceRAG: Joint Risk Calibration for Cascaded Retrieval-Augmented Generation](https://arxiv.org/abs/2605.20084v1)：提出BalanceRAG，通过联合校准LLM-only和RAG的阈值对，实现级联RAG系统的风险自适应控制，在保证错误率的前提下提升覆盖率和正确示例数，并减少不必要的检索。
- [Thinking in Scales: Accelerating Gigapixel Pathology Image Analysis via Adaptive Continuous Reasoning](https://arxiv.org/abs/2605.19491v2)：提出PathCTM模型，将全切片病理图像分析转化为动态连续推理过程，通过自适应尺度切换和置信度早停，大幅减少计算开销且不损失精度。
- [PromptRad: Knowledge-Enhanced Multi-Label Prompt-Tuning for Low-Resource Radiology Report Labeling](https://arxiv.org/abs/2605.20052v1)：提出PromptRad，一种知识增强的多标签提示调优方法，在低资源下将放射学报告标注重构为掩码语言建模，利用UMLS同义词丰富类别表示，仅需32个标注样本即超越传统方法。
- [VRXU-net: A Deep Learning Approach for Brain Ischemic Stroke Lesion Detection and Segmentation in T1W MRI](https://arxiv.org/abs/2605.21633v1)：提出一种结合VGG分类器、残差U-Net和多平面聚合的序贯框架，用于T1W MRI中缺血性脑卒中病灶的检测与分割。
- [Cardiac fat segmentation using computed tomography and an image-to-image conditional generative adversarial neural network](https://arxiv.org/abs/2605.20064v1)：提出将图像到图像的条件生成对抗网络pix2pix用于心脏脂肪自动分割，实现了高精度和实时分割。
- [RoboSurg-VQA: A Multimodal Benchmark for Surgical Segmentation-Aware Visual Question Answering](https://arxiv.org/abs/2605.23068v1)：提出了RoboSurg-VQA，首个结合分割感知的视觉问答基准，用于机器人辅助和微创手术场景，通过复用公共分割数据集并设计临床相关问题集与自动标注流程构建。
- [ImPartial: Multi-channel Whole-Cell Segmentation using Partial Annotations](https://arxiv.org/abs/2605.24128v1)：提出ImPartial框架，利用稀疏涂鸦标注和自监督多通道量化插补，在低标注条件下实现与全监督相当的细胞分割性能。
- [Divide-and-Conquer Inference for Large-Scale Visual Recognition with Multimodal Large Language Models](https://arxiv.org/abs/2605.24799v1)：提出一种无需训练的测试时缩放策略DCI，通过递归分解分类任务并动态剪枝，克服MLLM在长序列推理中的性能崩溃，提升大规模视觉识别精度与速度。
- [What Makes a Medical Checker Trainable? Diagnosing Signal Collapse and Reward Hacking in Checker-Guided RAG for Biomedical QA](https://arxiv.org/abs/2605.25988v1)：发现医学RAG中NLI检查器的输出分布（而非准确率）决定其是否提供可训练梯度，并识别出信号坍缩和奖励黑客两种训练失败模式。
- [Med-R2: An Adversarial Benchmark for Evidence-Grounded Reasoning in Medical VLMs](https://arxiv.org/abs/2605.24492v1)：提出了一个层次化的对抗基准Med-R2，系统评估医学视觉语言模型在临床推理中是否真正基于视觉证据，并发现模型依赖提示而非视觉线索，同时验证了逐步微调能提升鲁棒性。

### 共同创新点
- 提出FundusGround基准，通过空间定位的病灶证据实现临床可解释的眼科VQA，并证明病灶级视觉证据能提升模型性能与透明度。
- 提出PrivFusion，一个隐私保护的多智能体框架，在联邦学习前自动协调结构化的多站点异构数据集，减少人工标注和数据映射工作。
- 提出双管道PEFT框架，同时解决内窥镜临床VQA和隐私保护合成图像生成，显著降低计算成本并提升性能。
- 提出一种无需权重更新的解码时间残差导向方法，基于稀疏自编码器对医学视觉语言模型进行推理时干预，有效减少幻觉并提升报告质量，且发现增强方向可跨模型迁移而抑制方向需特定于模型。

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
