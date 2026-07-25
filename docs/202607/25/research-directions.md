# 研究方向与二次创新路线 · 2026-07-25

- 生成时间：2026-07-25 20:46:56 UTC
- 当日论文数：25
- 方向数：4

## 质量门控提示

- 视觉语言模型的安全性与鲁棒性 / 基于因果干预的VLM复合安全防御框架: theoretical_rationale.new_formulation is not predominantly Chinese
- 视觉语言模型的可解释性与诊断评估 / 基于失败机制分析的VLM组合推理纠正训练: theoretical_rationale.new_formulation is not predominantly Chinese

## 今日方向总览

| 方向 | 论文数 | 代表论文 |
|---|---:|---|
| 视觉语言模型的安全性与鲁棒性 | 3 | One Modality to Forget Them All: Enhancing Cross-Modal Unlearning in Vision-Language Models<br>MissingBench-Verified: Probing Vision-Language Models' Inability to Detect Missing Object Parts<br>Dual Adversarial Fine-tuning for Enhancing Robustness of Large Vision Language Model |
| 视觉语言模型的高效推理与表示压缩 | 3 | Searching for Task-Specific Vision Paths: Evolutionary Block Pruning Across Vision-Language Models<br>Modularized Dynamic-Granularity Video LLM for Multi-Event Long Video Understanding<br>Efficient Frame Selection for Long Videos at Test Time with Attention-Based MLLM Selectors |
| 视觉语言模型的可解释性与诊断评估 | 3 | Attention-Guided Saliency Maps for Interpreting Visualization Literacy in VLMs<br>How Do VLMs Fail? Vision-Operation Misalignment in Compositional VQA<br>PathReportEval: A Systematic Benchmark for Pathology Report Generation |
| 视觉语言模型在医学领域应用 | 4 | Induce to Empower: Improving Lightweight Baselines via Foundation Model Induction for Generalized Polyp Segmentation<br>Toward Generalizable Cognitive Impairment Detection with Speech-Based Multimodal Large Language Models<br>HTT-Net: Hierarchical Text-guided Transition Modeling for Surgical Video Phase Recognition |

## 方向 1：视觉语言模型的安全性与鲁棒性
研究VLM在遗忘、缺失部件和对抗攻击下的脆弱性，并提出跨模态遗忘检测、缺失部件基准和双对抗微调等方法。

### 代表论文

- [One Modality to Forget Them All: Enhancing Cross-Modal Unlearning in Vision-Language Models](https://arxiv.org/abs/2607.16442v1)：本文首次系统研究视觉语言模型(VLM)中跨模态遗忘的转移，发现不对称且易被排版攻击恢复的漏洞，并提出CrossInf方法通过影响引导聚焦Transformer模块，将转移差距减半并实现近零攻击成功率。
- [MissingBench-Verified: Probing Vision-Language Models' Inability to Detect Missing Object Parts](https://arxiv.org/abs/2607.18673v1)：提出MissingBench-Verified基准，揭示当前VLMs在检测物体缺失部件时的系统性缺陷，且现有策略（工具辅助验证、自主视觉推理、增加推理时间、微调等）无法缓解。
- [Dual Adversarial Fine-tuning for Enhancing Robustness of Large Vision Language Model](https://arxiv.org/abs/2607.18958v1)：提出双对抗微调框架DAFT，联合视觉和语义监督信号，通过替换CLIP视觉编码器即可提升大型视觉语言模型在零样本分类、图像描述和VQA任务上的鲁棒性。

### 共同创新点
- 首次系统研究VLM的跨模态遗忘转移和缺失部件检测问题
- 提出对抗攻击下的多任务鲁棒性微调框架
- 揭示了VLM在不同安全威胁下的共性脆弱性

### 尚未解决的问题
- 缺乏统一的安全评估基准，涵盖遗忘、缺失、对抗等多种威胁
- 现有方法仅针对单一威胁，难以应对复合攻击
- 缺少对VLM内部机制与安全漏洞之间关联的深入分析

### 二次创新路线
#### 路线 1：基于缺失部件检测的VLM鲁棒性增强预训练
- 核心想法：利用MissingBench-Verified（2607.18673v1）中部件缺失检测任务作为预训练数据，结合双对抗微调（2607.18958v1）的语义监督，增强VLM对部件缺失的鲁棒性。
- 新问题定义：定义部件缺失鲁棒分类任务：在测试时图像中物体部件可能被移除或遮挡，模型需正确识别物体并检测缺失部件。
- 机制来源：
  - 2607.18673v1构建了缺失部件基准，发现VLM对此类输入系统性失败，但未提供解决方案。
  - 2607.18958v1的双对抗微调利用标题语义监督保持特征鲁棒，但未针对部件缺失。
  - 本路线将MissingBench的图像作为对抗样本（实际是自然缺失），用双分支方法微调，使模型学会利用上下文而非依赖局部部件。
- 为什么值得做：部件缺失检测揭示了VLM对物体完整性的依赖，而语义监督能保持对抗下的语义一致性，两者结合可提升对异常输入的鲁棒性。
- 理论/数学创新理由：
  - 数学对象：对比损失L_contrastive = -log(exp(sim(z, t+)/τ) / Σ exp(sim(z, t_i)/τ))，其中z为图像特征（含缺失部件），t+为正文本标题，t_i为负样本。
  - 来源分解：MissingBench提供了缺失部件数据和评估协议；DAFT提供了语义监督的对抗训练框架；本路线将缺失部件视为一种特殊对抗扰动，利用标题对齐恢复语义。
  - 新建模方式：L_total = L_cls + λ L_contrastive，其中L_cls为标准分类损失，z = F_θ(x_missing)，x_missing为缺失部件图像。训练时，对每个图像生成描述其内容的标题（如“一只没有耳朵的猫”），作为正文本。
  - 公式草图：L = CE(y, p(y|x_missing)) + λ * InfoNCE(F_img(x_missing), T_text(caption))
  - 为什么可能有效：对比损失迫使视觉特征与语义描述对齐，即使缺失部件，模型也能通过整体上下文和标题线索正确识别；同时，标题中包含缺失信息，帮助模型推理。
- 可验证实验：在MissingBench-Verified上训练，在原始测试集和缺失部件测试集上测试分类准确率，并与直接微调比较。
- 主要风险：需要生成描述性标题，可能引入噪声；预训练可能使模型过度依赖标题线索，降低对真实世界完整物体的泛化。

## 方向 2：视觉语言模型的高效推理与表示压缩
研究如何在不降低性能或仅小幅降低的前提下，通过块跳过、动态粒度编码和注意力帧选择等方法减少VLM的计算开销。

### 代表论文

- [Searching for Task-Specific Vision Paths: Evolutionary Block Pruning Across Vision-Language Models](https://arxiv.org/abs/2607.17052v1)：提出一种源平衡进化搜索方法，在不微调的情况下为视觉语言模型固定预算地选择可跳过的视觉块路线，并比较共享路线与能力特定路线的效果。
- [Modularized Dynamic-Granularity Video LLM for Multi-Event Long Video Understanding](https://arxiv.org/abs/2607.15778v1)：提出MoD-VLLM，一种通过正负片段定位和模块化动态粒度反射实现迭代自反思的多事件长视频理解框架。
- [Efficient Frame Selection for Long Videos at Test Time with Attention-Based MLLM Selectors](https://arxiv.org/abs/2607.15689v1)：提出DAFS（Dynamic Attention-based Budget-aware Frame Selection），利用多模态大模型选定层的交叉注意力作为帧相关性信号，无需训练，并通过动态规划优化候选池大小和每帧token预算。

### 共同创新点
- 均致力于在推理阶段减少计算量，无需或仅需少量微调
- 利用模型内部信号（注意力、损伤）指导压缩策略
- 在不同任务（分类、问答、视频理解）上验证有效性

### 尚未解决的问题
- 现有方法通常针对特定架构或任务设计，缺乏通用压缩框架
- 动态调整计算预算的方法尚不成熟，难以自适应输入难度
- 块级剪枝与帧级选择之间的协同优化未探索

### 二次创新路线
#### 路线 1：联合进化剪枝与注意力帧选择的计算自适应框架
- 核心想法：将进化块剪枝（2607.17052v1）与注意力帧选择（2607.15689v1）结合，在视频理解中同时优化跳过的视觉块数量和关键帧数量，实现总计算预算下的最优性能。
- 新问题定义：定义联合计算预算分配问题：给定总FLOPs约束，同时决定每个视频帧中跳过的视觉块和保留的帧数，最小化任务性能损失。
- 机制来源：
  - 2607.17052v1的进化搜索可跳过固定数量的视觉块，但不考虑帧间变化。
  - 2607.15689v1的DAFS利用注意力得分选择帧，但未考虑帧内块压缩。
  - 本路线将跳过块数作为每帧的参数，纳入DAFS的优化目标，扩展进化搜索的搜索空间。
- 为什么值得做：两者都使用进化/搜索方法优化计算预算，且针对不同层面（块和帧），联合优化可提供更灵活的压缩。
- 理论/数学创新理由：
  - 数学对象：离散优化问题：max_{S, F} Utility(S, F) s.t. Cost(S, F) ≤ B，其中S为跳过块策略，F为帧选择策略。
  - 来源分解：进化剪枝评估每个块的损伤，DAFS评估每帧的注意力相关性；本路线将两者结合为联合效用函数U = Σ_{k∈F} (att_score_k * acc_drop(S_k))，其中att_score_k来自DAFS，acc_drop(S_k)来自进化搜索对帧k的损伤估计。
  - 新建模方式：U = Σ_{k∈F} α·φ_j(k) - β·μ(S_k)，其中φ_j(k)为DAFS的帧相关性分数，μ(S_k)为跳过块的平均损伤。约束：Σ_{k∈F} c(S_k) ≤ B。
  - 公式草图：max_{S,F} Σ_{k∈F} (α·s_k - β·d_k) s.t. Σ_{k∈F} c_k ≤ B
  - 为什么可能有效：联合优化能全局权衡帧重要性和块重要性，避免单独优化时次优解；通过调整α和β可适应不同任务偏好。
- 可验证实验：在长视频问答数据集（如NExT-QA）上，比较联合优化与分别优化的性能（准确率、FLOPs、推理时间）。
- 主要风险：搜索空间增大可能导致进化算法收敛慢；需要设计高效的效用函数估计方法。

#### 路线 2：基于动态粒度反射的视频LLM自适应令牌分配
- 核心想法：结合MoD-VLLM（2607.15778v1）的正负片段定位和动态粒度分配，与DAFS（2607.15689v1）的注意力帧选择，实现更细粒度的令牌预算分配。
- 新问题定义：定义细粒度令牌预算分配任务：给定总令牌预算，同时确定保留哪些帧以及每帧使用哪种粒度编码（细/粗），以最大化多事件理解准确率。
- 机制来源：
  - 2607.15778v1通过定位模块区分正负片段，并对正片段用细粒度、负片段用粗粒度，但未优化帧级选择。
  - 2607.15689v1的DAFS通过注意力选择帧，但所有选中帧使用相同粒度。
  - 本路线将DAFS的帧选择结果作为MoD-VLLM的输入，并进一步允许选中帧内动态粒度（对关键子片段细粒度，其他粗粒度）。
- 为什么值得做：MoD-VLLM处理长视频时分配不同粒度给正负片段，DAFS选择关键帧，两者可协同：先选帧，再对选中帧分配不同粒度。
- 理论/数学创新理由：
  - 数学对象：层次优化：上层选择帧集F，下层对每个帧分配粒度g∈{fine, coarse}，目标最大化信息保留。
  - 来源分解：MoD-VLLM提供正负片段判断和粒度调度器；DAFS提供帧级注意力分数；本路线将注意力分数作为帧的重要性权重，再结合MoD的粒度选择。
  - 新建模方式：total_info = Σ_{k∈F} w_k * I(g_k)，其中w_k为DAFS注意力分数，I(g_k)为粒度g_k的信息量（如细粒度=1,粗粒度=0.5）。约束：Σ_{k∈F} cost(g_k) ≤ B。
  - 公式草图：max_{F,{g_k}} Σ_{k∈F} w_k·I(g_k) s.t. Σ_{k∈F} cost(g_k) ≤ B
  - 为什么可能有效：通过联合优化，在预算内优先对重要帧且关键子片段分配细粒度，次要部分粗粒度，实现信息最大化。
- 可验证实验：在MEventBench基准上，比较本方法与MoD-VLLM和DAFS单独使用的准确率和令牌使用效率。
- 主要风险：层次优化可能增加推理延迟；粒度cost估计需准确否则预算超支。

## 方向 3：视觉语言模型的可解释性与诊断评估
提出可解释性方法（注意力显著图）和诊断框架（组合VQA失败分析、病理报告评估），揭示VLM内部工作机制和失败模式。

### 代表论文

- [Attention-Guided Saliency Maps for Interpreting Visualization Literacy in VLMs](https://arxiv.org/abs/2607.16105v1)：提出一种轻量级、无梯度的注意力显著图方法，通过聚合语言模型所有层和头的注意力权重并映射回图像patch，实现VLM在图表问答中每个生成token与图像区域的直接对齐，并用删除指标验证了因果忠实性。
- [How Do VLMs Fail? Vision-Operation Misalignment in Compositional VQA](https://arxiv.org/abs/2607.16094v1)：提出操作中心机制框架，通过因果干预将VLM在组合VQA中的失败分解为四种类型（grounding、reasoning、attribute extraction、language prior），并发现各失败类型与特定内部计算路径（MLP、注意力等）的因果关系。
- [PathReportEval: A Systematic Benchmark for Pathology Report Generation](https://arxiv.org/abs/2607.18448v1)：提出PathReportEval标准化基准和临床报告质量分数（CRQS），解决病理报告生成评估标准不统一、传统NLG指标忽略临床错误的问题。

### 共同创新点
- 均致力于解释或诊断VLM的行为，不依赖额外标注
- 提供细粒度的分析（token级、操作级、临床属性级）
- 开发了标准化评估工具（显著图、失败模式分类、CRQS）

### 尚未解决的问题
- 可解释性方法未直接用于模型改进，缺乏闭环
- 失败分析仅针对特定数据集和架构，通用性不足
- 临床评估指标CRQS依赖结构化提取，误差可能累积

### 二次创新路线
#### 路线 1：基于临床事实评估的病理报告生成优化
- 核心想法：利用CRQS指标（2607.18448v1）作为强化学习奖励信号，训练病理报告生成模型直接优化临床事实准确性，而非传统词级指标。
- 新问题定义：定义临床奖励强化学习任务：在病理报告生成中，以CRQS（包括CFC、KIR、HR、CDS）作为奖励，使用策略梯度优化生成模型。
- 机制来源：
  - 2607.18448v1提供了CRQS指标的计算方法，包括结构化提取和四个子指标，但仅用于评估，未用于训练。
  - 本路线将CRQS作为奖励函数，结合策略梯度（如PPO）优化生成模型，直接提升临床质量。
- 为什么值得做：CRQS直接从临床属性角度评估报告质量，比BLEU/ROUGE更符合实际需求，用作奖励可减少幻觉和遗漏。
- 理论/数学创新理由：
  - 数学对象：策略梯度目标J(θ) = E_{y∼π_θ}[R(y, y*)]，其中R为CRQS分数，y*为参考报告。
  - 来源分解：CRQS的子指标分别评估覆盖、召回、幻觉和矛盾，本路线用其加权和作为奖励，引导模型学习平衡这些方面。
  - 新建模方式：R = w1*CFC + w2*KIR + w3*(1-HR) + w4*(1-CDS)，权重沿用默认或自适应。策略梯度更新：θ ← θ + α ∇_θ log π_θ(y|x) R。
  - 公式草图：∇_θ J ≈ E[ (CRQS(y, y*) - baseline) * ∇_θ log π_θ(y|x) ]
  - 为什么可能有效：直接优化临床指标避免词级偏差，减少幻觉和遗漏；结构化提取确保奖励计算可靠；策略梯度可处理不可微奖励。
- 可验证实验：在TCGA病理报告数据集上，训练基于LLaVA的生成模型，用CRQS作为奖励进行强化学习，比较与标准SFT的CRQS分数和临床错误率。
- 主要风险：需要实时计算CRQS，可能增加训练时间；奖励可能不平稳，需要合理的基线降低方差。

## 方向 4：视觉语言模型在医学领域应用
将VLM应用于息肉分割、认知障碍检测、手术阶段识别和病理报告生成等医学任务，利用预训练知识提升泛化性和效率。

### 代表论文

- [Induce to Empower: Improving Lightweight Baselines via Foundation Model Induction for Generalized Polyp Segmentation](https://arxiv.org/abs/2607.17208v1)：提出Lite-Polyp Inductor框架，通过生成基础模型原型表示并借助重建监督进行语义对齐，再通过Transformer融合突出息肉相关特征，显著提升轻量基线模型在息肉分割任务上的泛化性能，且计算开销小。
- [Toward Generalizable Cognitive Impairment Detection with Speech-Based Multimodal Large Language Models](https://arxiv.org/abs/2607.21496v1)：提出基于开源大语言模型（Qwen2-Audio和Qwen3）的多模态框架，通过融合语音音频嵌入和自动转录文本嵌入进行认知障碍检测，在ADReSS20和ADReSSo21上达到92.4%准确率，并具有跨数据集泛化能力。
- [HTT-Net: Hierarchical Text-guided Transition Modeling for Surgical Video Phase Recognition](https://arxiv.org/abs/2607.16787v1)：本文提出HTT-Net，通过构建分层手术语义记忆（包括阶段内描述、阶段间过渡描述和细粒度语义单元），并设计过渡感知片段构建（TAS-Con）和过渡感知片段校准（TAS-Calib）模块，利用结构化语义知识增强手术视频阶段识别的准确性和时间一致性。
- [PathReportEval: A Systematic Benchmark for Pathology Report Generation](https://arxiv.org/abs/2607.18448v1)：提出PathReportEval标准化基准和临床报告质量分数（CRQS），解决病理报告生成评估标准不统一、传统NLG指标忽略临床错误的问题。

### 共同创新点
- 利用预训练VLM或基础模型医学化，克服小样本和领域漂移
- 进行多模态融合（图像+文本/语音）以增强诊断能力
- 提出轻量化方案以适配临床实时需求

### 尚未解决的问题
- 医学标注成本高，多数方法仍需少量标注数据
- 跨数据集泛化仍面临挑战，不同医院分布差异大
- 缺乏统一的可信度评估和临床决策集成框架

### 二次创新路线
#### 路线 1：基于不确定性感知的医学VLM主动学习框架
- 核心想法：结合Bayesian不确定性估计（2607.20582v1）与基础模型诱导（2607.17208v1），设计主动学习策略，在少量标注下最大化分割性能。
- 新问题定义：定义不确定性驱动的主动学习任务：在息肉分割中，从未标注池中选择最不确定的样本进行标注，以最小化标注预算达到目标性能。
- 机制来源：
  - 2607.20582v1提出MC dropout不确定性信号，可检测易错样本。
  - 2607.17208v1利用多个基础模型诱导轻量模型，提升泛化。
  - 本路线使用MC dropout估计每个未标注样本的不确定性，选择高不确定性样本由专家标注，而后用基础模型诱导微调。
- 为什么值得做：不确定性可指导标注，减少无用标注；基础模型诱导提供强先验，两者结合可高效利用标注预算。
- 理论/数学创新理由：
  - 数学对象：主动采集函数a(x) = H(p(y|x)) + λ Var(p(y|x))，其中H为熵，Var为MC dropout方差。
  - 来源分解：不确定性估计提供样本选择准则；基础模型诱导提供训练增强；本路线迭代进行标注-训练。
  - 新建模方式：在每轮主动学习中，选取使a(x)最大的k个样本，标注后加入训练集，更新诱导模块。最终目标是最小化期望分割损失。
  - 公式草图：x* = argmax_{x∈U} ( H(p_θ(y|x)) + λ * Var_{T}(p_θ_t(y|x)) )
  - 为什么可能有效：主动选择高不确定性样本避免无效标注，基础模型诱导使得少量数据即可学到泛化特征，降低标注成本。
- 可验证实验：在息肉分割数据集（Kvasir-SEG、CVC-ClinicDB等）上模拟主动学习，比较随机选择、熵选择和本方法的标注效率（达到目标Dice所需的标注比例）。
- 主要风险：MC dropout需要多次前向传播增加计算；基础模型诱导需要预先提取特征，可能限制实时性。

#### 路线 2：跨模态医学摘要与报告一致性增强
- 核心想法：结合病理报告生成（2607.18448v1）的CRQS指标和语音认知障碍检测（2607.21496v1）的多模态框架，构建多模态医学摘要系统，统一图像和语音信息生成结构化报告，并用CRQS保证事实一致性。
- 新问题定义：定义多模态医学摘要任务：输入为病理WSI图像和患者语音描述，输出结构化报告，同时评估事实准确性和临床一致性。
- 机制来源：
  - 2607.18448v1提供病理报告生成的评估指标CRQS和生成基线。
  - 2607.21496v1利用Qwen2-Audio和Qwen3提取语音和文本特征。
  - 本路线融合语音嵌入和图像嵌入，使用Transformer解码生成报告，并用CRQS奖励进行强化学习。
- 为什么值得做：两个任务互补：病理报告生成处理图像，认知障碍检测处理语音，合并可处理更丰富的多模态输入。
- 理论/数学创新理由：
  - 数学对象：多模态融合特征z = [E_image(x)；E_speech(a)]，生成似然p(y|z) = ∏ p(y_t|z, y_{<t})，优化目标包括CE和CRQS奖励。
  - 来源分解：病理报告生成提供了文本解码器和评估；语音特征提取提供了音频编码；本路线将两者拼接作为输入，并用CRQS作为奖励。
  - 新建模方式：L = L_CE + λ L_RL，L_RL = -E[CRQS(y, y*)]。训练时先预训练融合模块，再强化学习微调。
  - 公式草图：L_total = -log p(y|x, a) + λ * (baseline - CRQS(y, y*)) * log p(y|x, a)
  - 为什么可能有效：结合语音描述可提供额外上下文（如患者主诉），增强报告相关性和完整性；CRQS奖励直接优化临床事实，减少幻觉。
- 可验证实验：在真实或模拟多模态医学数据集上（如同时包含WSI和语音描述的病例），比较单模态与多模态报告生成的CRQS分数和临床专家评分。
- 主要风险：多模态数据获取困难；不同模态编码器对齐需大量训练；CRQS的结构化提取可能不适应口语化描述。
