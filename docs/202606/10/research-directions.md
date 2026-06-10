# 研究方向与二次创新路线 · 2026-06-10

- 生成时间：2026-06-10 21:58:29 UTC
- 当日论文数：17
- 方向数：4

## 质量门控提示

- 医疗智能体进化与推理对齐 / 对齐引导的技能记忆效用加权: formula_sketch does not look like a formula

## 今日方向总览

| 方向 | 论文数 | 代表论文 |
|---|---:|---|
| 医疗智能体进化与推理对齐 | 3 | Baichuan-M4: A Clinical-Grade Medical Agent System for Continuous Care<br>Experience Makes Skillful: Enabling Generalizable Medical Agent Reasoning via Self-Evolving Skill Memory<br>The Consistency Illusion: How Multi-Agent Debate Hides Reasoning Misalignment |
| 高效多模态表示与推理优化 | 6 | DALE-CT: Depth-Aware Foundation Models for Computed Tomography<br>Late-Layer Fusion is Enough: Dual-Path Vision Token Routing for Multimodal Large Language Models under Visual Saturation<br>DyCo-RL: Dynamic Cross-Modal Coordination for Visual Reasoning |
| 联邦与增量医学图像分割 | 4 | Shift-Dependent Asymmetry: Orthogonal Inverse Low-Rank Adaptation for Federated Medical Segmentation<br>vesselFM-CT: Segmenting All Blood Vessels in CT Images for System-Level Cardiovascular Analysis<br>Multi-planar 2D-U-Net Segmentation of 3D-CT Abdominal Organs augmented by Spatial Occurrence Maps |
| 多模型协同与证据融合 | 3 | One Stone, Three Birds: Self-adaptive Optimal Transport for Multi-VLM Selection, Adaptation, and Ensembling<br>Constrained Dominant Sets for Multimodal Document Question Answering<br>QCFuse: Query-Aware Cache Fusion via Compressed View for Efficient RAG Serving |

## 方向 1：医疗智能体进化与推理对齐
将连续护理强化学习框架、后部署技能记忆进化与跨智能体推理对齐度量相结合，形成可自我监督、持续改进的医疗智能体系统，提升长期决策的可靠性与一致性。

### 代表论文

- [Baichuan-M4: A Clinical-Grade Medical Agent System for Continuous Care](https://arxiv.org/abs/2606.08982v2)：提出临床级医疗智能体系统Baichuan-M4，通过统一运行时、连续护理强化学习推理模型和临床工具层三大支柱，面向连续护理而非单轮问答，在多项医学评估中取得领先并降低幻觉率至3.3%。
- [Experience Makes Skillful: Enabling Generalizable Medical Agent Reasoning via Self-Evolving Skill Memory](https://arxiv.org/abs/2606.09365v1)：提出SkeMex，一种无需更新模型权重的后部署自我进化框架，通过将交互轨迹蒸馏为结构化技能并利用环境反馈估计效用指导检索和治理，实现医疗智能体的通用推理。
- [The Consistency Illusion: How Multi-Agent Debate Hides Reasoning Misalignment](https://arxiv.org/abs/2606.08457v1)：提出CARA指标族量化多智能体LLM系统的跨推理链对齐，发现答案一致下推理不一致的"一致性幻觉"，并通过接地辩论协议（GDP）显著改善对齐。

### 共同创新点
- Baichuan-M4提供连续护理RL框架和工具层，SkeMex提供非参数化技能记忆进化，CARA提供推理对齐诊断与接地辩论协议。
- 三者均面向医疗智能体的长期交互与决策，互补地解决奖励设计、经验积累和推理一致性问题。

### 尚未解决的问题
- 技能记忆的效用估计与推理对齐度量尚未统一，可能导致不一致技能被误用。
- 多智能体场景下，对齐度量随智能体数量增加计算开销大。
- 联邦环境下技能库的隐私保护与分布式治理缺乏机制。

### 二次创新路线
#### 路线 1：跨智能体推理链蒸馏与技能合并
- 核心想法：利用CARA检测多智能体间高对齐推理链，通过SkeMex的蒸馏引擎将其转化为技能，并通过治理模块合并相似技能，减少冗余。
- 新问题定义：在多智能体医疗系统中，如何从多轮辩论中提取可复用的、内部一致的推理模式，并整合为单一智能体的结构化技能。
- 机制来源：
  - Baichuan-M4的工具层：支持多智能体协调与辩论。
  - SkeMex的蒸馏引擎：将轨迹转化为技能；治理模块：合并/删除技能。
  - CARA的对齐度量：提供高对齐链的筛选标准。
- 为什么值得做：多智能体辩论产生多样化推理，但冗余和噪声多；对齐度量可筛选高质量链，蒸馏为紧凑技能，提升技能库效率。
- 理论/数学创新理由：
  - 数学对象：最小化联合推理熵的同时最大化技能压缩率
  - 来源分解：Baichuan-M4产生多智能体轨迹；SkeMex蒸馏但缺乏筛选标准；CARA提供对齐分数但未用于蒸馏。
  - 新建模方式：定义技能筛选阈值τ，仅保留CARA-HYB > τ的链；对候选技能计算互信息MI(skill_i, skill_j)，若MI > η则合并为泛化技能。蒸馏损失加入对齐正则项：L = L_distill + γ * (1 - A_avg)。
  - 公式草图：设S为候选技能集，保留S' = {s | CARA-HYB(s, ref) > τ}；对s_i, s_j ∈ S'，若I(s_i; s_j) > η，则合并为s_k = (s_i ∪ s_j)/2。蒸馏时，新技能s_k使得链集合的KL散度最小。
  - 为什么可能有效：对齐阈值过滤低质量链，互信息合并减少冗余，γ正则项鼓励技能内部一致性，形成紧凑且可靠的技能库。
- 可验证实验：在Baichuan-M4多智能体系统上运行MedQA-USMLE辩论，收集轨迹并应用该方法，评估技能库大小与下游准确率。
- 主要风险：阈值τ和η需经验设定；合并可能丢失细微差异，导致泛化下降。

## 方向 2：高效多模态表示与推理优化
从自监督表示学习到推理优化，通过深度感知预训练、视觉令牌路由、跨模态协调强化学习和可学习稀疏化，突破医疗VLM的计算瓶颈与表示质量问题，并结合污染审计确保基准可信。

### 代表论文

- [DALE-CT: Depth-Aware Foundation Models for Computed Tomography](https://arxiv.org/abs/2606.07775v1)：本文提出DALE-CT，一种基于2D切片架构的CT基础模型，从零使用LeJEPA自监督学习训练，通过引入3D深度感知预训练策略和密集辅助监督，在无文本监督下达到与SOTA 3D视觉语言模型接近的性能。
- [Late-Layer Fusion is Enough: Dual-Path Vision Token Routing for Multimodal Large Language Models under Visual Saturation](https://arxiv.org/abs/2606.09131v1)：提出DPVR-LF，通过在视觉令牌饱和点将其路由至单层侧分支，文本单独经过深层堆栈，仅在最后层融合，以约3%可训练参数保持竞争力，挑战了视觉令牌必须遍历所有深层的假设。
- [DyCo-RL: Dynamic Cross-Modal Coordination for Visual Reasoning](https://arxiv.org/abs/2606.08035v1)：提出 DyCo-RL，通过 Fisher-Rao 测地距离动态分配令牌视觉/文本角色并基于注意力对齐优势加权，解决多模态大模型推理中跨模态协调失败问题。
- [Cosine Misleads: Auxiliary Losses Reshape Vision Language Models, Not Their Latents](https://arxiv.org/abs/2606.05753v1)：揭示视觉语言模型中潜在视觉推理的余弦对齐损失与准确率负相关，提出PRISM诊断方法证明监督潜在变量被绕过，辅助损失通过共享参数重塑语言模型。
- [Learnable Token Sparsification for Efficient Gigapixel Whole Slide Image Reasoning](https://arxiv.org/abs/2606.08641v1)：针对十亿像素全切片图像视觉令牌过多问题，提出可学习令牌稀疏化方法，通过解耦路由架构和SparseLearn组件（含可微Soft Top-K与对角注意力去噪器）实现端到端训练，推理时仅保留32个令牌（0.78%原始长度），在SlideBench上达到73.32%准确率，显著优于基线方法，并具备强零样本泛化能力。
- [A Controlled Audit of Pretraining Contamination in Public Medical Vision-Language Benchmarks](https://arxiv.org/abs/2606.10066v1)：本研究通过四种检测器（图像侧近邻重叠、规范顺序可交换性、队列相对Min-K%++尾富集、跨模型前K重叠）系统审计了医学视觉语言模型在公共基准上的预训练污染，发现图像侧存在分布重叠而非像素级重复，队列相对检测器在小型医学VLM队列中不可靠。

### 共同创新点
- DALE-CT的深度感知自监督框架与DPVR-LF的视觉令牌路由共同关注2D/3D上下文与计算效率。
- DyCo-RL的跨模态协调RL与Cosine Misleads的诊断方法分别从优化和评估角度提升推理质量。
- Learnable Token Sparsification可减少视觉令牌，与DPVR-LF互补。
- Controlled Audit提供预训练污染检测，保障评估可信度。

### 尚未解决的问题
- 视觉令牌饱和点固定，缺乏自适应路由机制。
- 辅助损失（如余弦对齐）与推理准确率负相关，需要新损失设计。
- 多模态RL中令牌级角色分配计算开销较大。
- 污染审计未结合模型内部表示进行记忆化检测。

### 二次创新路线
#### 路线 1：自适应视觉令牌路由与动态饱和检测
- 核心想法：结合DPVR-LF的视觉饱和发现和DALE-CT的深度感知，设计一个基于层间注意力动态检测饱和点的路由模块，并利用Learnable Token Sparsification进一步稀疏已路由的视觉令牌。
- 新问题定义：在多模态大模型中，如何根据输入图像动态决定视觉令牌何时以及如何被路由和稀疏化，以最小化计算开销同时保持下游性能。
- 机制来源：
  - DPVR-LF的层间注意力分析：发现文本到图像注意力下降模式，用于识别饱和点。
  - DALE-CT的深度感知：提供2D切片与3D位置关联，辅助注意力距离度量。
  - Learnable Token Sparsification的可学习稀疏：通过SparseLearn组件学习保留哪些令牌。
- 为什么值得做：固定饱和点可能不适用于不同任务和图像；动态检测可适应输入变化；稀疏化进一步降低计算。
- 理论/数学创新理由：
  - 数学对象：动态路由阈值θ(t)和稀疏比率ρ
  - 来源分解：DPVR-LF使用固定层索引路由；DALE-CT使用固定的12mm slab；Learnable Token Sparsification固定稀疏比率。
  - 新建模方式：定义注意力衰减率α(l) = (A_vis2txt(l) - A_vis2txt(l-1)) / A_vis2txt(l-1)，当α(l)<ε时触发路由。在侧分支后，使用可学习稀疏模块输出保留掩码M，使得||M||_0 / N = ρ，且通过Soft Top-K可微。
  - 公式草图：设l=0,...,L-1，计算δ(l)=A_vis2txt(l-1)-A_vis2txt(l)，当δ(l)>τ时在l层路由。路由后视觉令牌序列V'通过单层侧分支，然后输入SparseLearn模块：M = SoftTopK(score(V'; θ), ρ)，最终保留V'_sel = V' ⊙ M。
  - 为什么可能有效：动态路由适应不同输入；稀疏化在轻量侧分支后进一步减少令牌，两者结合在保持精度的前提下大幅降低计算。
- 可验证实验：在LLaVA-1.5和CT-RATE数据集上测试动态路由与稀疏化，与DPVR-LF和固定稀疏对比，测量FLOPs和V*Bench准确率。
- 主要风险：动态检测可能不稳定，需设计稳定阈值；稀疏化可能丢失关键视觉证据。

#### 路线 2：跨模态协调的令牌级对齐与辅助损失重设计
- 核心想法：基于Cosine Misleads的发现（余弦对齐与准确率负相关），借助DyCo-RL的Fisher-Rao距离分配令牌角色，设计新的辅助损失，使潜在变量真正参与推理。
- 新问题定义：在视觉语言模型的潜在视觉推理中，如何设计训练损失使得中间潜在变量不仅是视觉目标的压缩编码，而且因果性地参与答案生成。
- 机制来源：
  - Cosine Misleads的PRISM诊断：发现潜在变量被绕过，余弦对齐无意义。
  - DyCo-RL的Fisher-Rao角色分配：动态分配视觉/文本角色，并基于注意力对齐加权优势。
  - DALE-CT的密集辅助监督头：提供解剖和异常级密集目标。
- 为什么值得做：现有辅助损失（MSE/余弦）导致模型绕过潜在变量；新损失通过角色对齐和因果约束，强制潜在变量承载答案信息。
- 理论/数学创新理由：
  - 数学对象：因果对齐损失 L_causal
  - 来源分解：Cosine Misleads指出现有LVR损失只压缩不利用；DyCo-RL使用对齐加权但未针对潜在变量；DALE-CT使用密集监督但未见用于推理。
  - 新建模方式：定义潜在变量z的因果重要性得分ψ(z) = |Δacc| from PRISM corruption。训练时加入L_causal = ||ψ(z) - 1||^2，鼓励z对答案有高因果贡献。同时，角色对齐损失L_role = Σ (cos(attn_vis, attn_ref) - role_label)^2，role_label来自Fisher-Rao。
  - 公式草图：在PRISM扰动测试中，对潜在变量z添加噪声η，计算准确率变化Δacc = |acc(z) - acc(z+η)|。ψ(z) = Δacc。训练时总损失L = L_task + β L_causal + γ L_role，其中L_task为交叉熵。
  - 为什么可能有效：L_causal迫使z直接贡献答案，避免被绕过；L_role确保角色分配与注意力一致，增强跨模态协调性。
- 可验证实验：在V*Bench和MMVP上训练LVR变体，测量PRISM ψ值和准确率，对比标准LVR和Cosine Misleads基线。
- 主要风险：L_causal需要扰动计算，增加训练开销；ψ可能不稳定，需要合理归一化。

## 方向 3：联邦与增量医学图像分割
针对医学图像分割中的联邦异构、全血管分割和弱监督增量场景，融合逆非对称微调、血管感知损失、多平面先验和语义锚点，实现鲁棒且高效的分割框架。

### 代表论文

- [Shift-Dependent Asymmetry: Orthogonal Inverse Low-Rank Adaptation for Federated Medical Segmentation](https://arxiv.org/abs/2606.08687v1)：提出逆非对称微调（IAT）与子空间正交正则化器（SOR），解决联邦医学分割中编码器-解码器不对称导致的异构性耦合问题，实现无需额外通信的高效联邦微调。
- [vesselFM-CT: Segmenting All Blood Vessels in CT Images for System-Level Cardiovascular Analysis](https://arxiv.org/abs/2606.09400v1)：提出vesselFM-CT模型，通过多步迭代训练和TubeLoss损失函数，首次实现从大血管到微小血管的全分割，性能优于基线。
- [Multi-planar 2D-U-Net Segmentation of 3D-CT Abdominal Organs augmented by Spatial Occurrence Maps](https://arxiv.org/abs/2606.07717v1)：提出一种基于2D-U-Net的多平面分割框架，通过空间出现图（SOM）增强，实现大视野3D CT腹部器官的轻量级精确分割。
- [Weakly Supervised Incremental Segmentation via Semantic Anchors and Spatial Arbitration](https://arxiv.org/abs/2606.04060v1)：提出SASA框架，通过刚性语义锚点、弹性残差令牌和空间标签仲裁，在弱监督增量分割中抑制特征漂移和类覆盖。

### 共同创新点
- IAT处理联邦场景下编码器-解码器不对称，vesselFM-CT提供血管专用损失和迭代训练，Multi-planar 2D-U-Net提供多平面集成和空间先验，SASA解决弱监督增量中的特征漂移。
- 四者分别关注联邦、困难结构、多平面集成和增量学习，互补形成全面的分割解决方案。

### 尚未解决的问题
- 联邦场景下外观偏移与监督偏移的量化分离仍需手动超参数。
- 全血管分割依赖迭代训练和人工校正，自动化不足。
- 多平面融合未考虑各平面权重自适应。
- SASA的锚点数量随增量线性增长，存储开销大。

### 二次创新路线
#### 路线 1：联邦全血管分割的逆非对称微调与血管损失
- 核心想法：将IAT的逆非对称微调应用于vesselFM-CT的分割模型，使编码器和解码器分别处理外观偏移和监督偏移，同时使用TubeLoss解决血管内外部不平衡。
- 新问题定义：在联邦医学分割中，针对血管结构具有极大尺度变化且客户端异构严重的情况，如何设计参数分配和损失函数使得模型高效适应各站点。
- 机制来源：
  - IAT：编码器共享B、本地A吸收外观偏移；解码器共享A、本地B吸收监督偏移。
  - vesselFM-CT的TubeLoss：基于半径加权并添加边界假阳性惩罚，解决类不平衡。
- 为什么值得做：联邦场景下血管分割面临严重外观差异（CT厂商）和标注差异；IAT解耦异质性，TubeLoss关注小血管，结合可提升泛化。
- 理论/数学创新理由：
  - 数学对象：联邦聚合中的非对称参数更新与TubeLoss的加权Dice
  - 来源分解：IAT提供结构解耦，但仅处理分割通用任务；vesselFM-CT提供血管专用损失，但未考虑联邦场景。
  - 新建模方式：在IAT框架中，TubeLoss替换标准Dice/CE：L_local = λ_Dice L_Dice^w + λ_CE L_CE^w，其中权重w基于半径倒数。在联邦聚合时，编码器的B矩阵全局平均，A矩阵不聚合；解码器的A全局平均，B不聚合。SOR正则化器加入本地损失以防止泄漏。
  - 公式草图：L_local = λ_Dice · 2*sum(w·y_hat·y)/sum(w·(y_hat+y)) + λ_CE · sum(w·CE(y_hat,y)) + λ_SOR · (||P_sh · P_lo||_F^2 + ||Q_sh · Q_lo||_F^2)，其中w为TubeLoss权重。
  - 为什么可能有效：非对称参数分配使模型分离外观和监督偏差；TubeLoss强调小血管和边界，减少漏检；SOR防止共享因子被本地漂移污染，三者协同提升联邦分割精度。
- 可验证实验：在多个CT血管分割数据集上模拟联邦客户端（不同扫描仪），对比IAT+TubeLoss与单独IAT和单独vesselFM-CT。
- 主要风险：超参数λ_SOR需调谐；解码器共享A可能限制监督偏移适应能力。

#### 路线 2：弱监督增量分割中的多平面空间先验与锚点蒸馏
- 核心想法：将Multi-planar 2D-U-Net的空间出现图(SOM)作为SASA中语义锚点的初始化先验，并在增量学习时通过SOM约束空间标签仲裁(SLA)，减少伪标签噪声。
- 新问题定义：在弱监督增量分割中，如何利用训练集的全局空间分布先验辅助语义锚点初始化，并在每步伪标签生成中利用空间几何约束抑制噪声。
- 机制来源：
  - Multi-planar 2D-U-Net的空间出现图：从训练集统计类条件体素概率，提供3D位置先验。
  - SASA的语义锚点：可学习类级刚性表示，但初始化为随机；空间标签仲裁(SLA)：基于对象掩码和几何权重。
- 为什么值得做：SOM提供解剖位置统计先验，可增强锚点的空间特异性；SLA利用SOM的几何权重可更合理过滤矛盾标签。
- 理论/数学创新理由：
  - 数学对象：锚点初始化分布P_anchor和SLA中几何权重w_geo
  - 来源分解：Multi-planar提供SOM作为先验，但仅用于多通道输入；SASA的锚点随机初始化，SLA使用高斯权重但未利用全局先验。
  - 新建模方式：锚点A_c初始化为SOM中类c的空间中心：A_c = argmax_x SOM_c(x)。在SLA中，几何权重w_geo改为SOM引导权重：w_p = SOM_c(p) · exp(-||p - μ||^2/σ^2)。
  - 公式草图：A_c^0 = μ_c = ∫ x · SOM_c(x) dx / ∫ SOM_c(x) dx。在SLA中，对像素p，权重w_p = SOM_c(p) · exp(-||p - μ_c||^2 / (2σ^2))，其中c为当前候选类。
  - 为什么可能有效：先验初始化加速锚点收敛；SOM引导权重优先选择位于器官典型区域的像素，减少背景噪声，提升伪标签质量。
- 可验证实验：在腹部CT增量分割任务上（逐步加入新器官），对比原始SASA和使用SOM初始化的SASA，评估每步分割Dice。
- 主要风险：SOM可能因训练集偏差导致偏差放大；锚点初始化为固定点可能缺乏灵活性。

## 方向 4：多模型协同与证据融合
利用最优运输和约束主导集实现无训练的多VLM选择、适配与集成，以及文档问答中证据的鲁棒选择，结合RAG缓存融合加速，形成高效的多源证据处理框架。

### 代表论文

- [One Stone, Three Birds: Self-adaptive Optimal Transport for Multi-VLM Selection, Adaptation, and Ensembling](https://arxiv.org/abs/2606.08126v1)：提出OSTB框架，利用自适应最优运输从多候选VLM中估计共识样本-类别结构，无需训练即可同时实现模型选择、目标域适配和预测集成。
- [Constrained Dominant Sets for Multimodal Document Question Answering](https://arxiv.org/abs/2606.07252v1)：针对长多模态文档问答中相似度检索器因内容重复而忽略互补证据的问题，本文提出基于约束主导集(CDS)的无训练检索方法。通过在查询增强的亲和图上应用复制定理进行全局均衡选择，自动平衡相关性与冗余度。结合Qwen3-VL-32B阅读器，CDS在VisDoMBench上平均66.99，比无检索基线提升37.1分，在MMLongBench-Doc上提升4.8分，达到新最优。
- [QCFuse: Query-Aware Cache Fusion via Compressed View for Efficient RAG Serving](https://arxiv.org/abs/2606.05875v1)：QCFuse提出一种压缩视图查询感知选择器，通过块锚点查询探测和关键层分析，在RAG缓存融合中实现高效预填充加速，同时保持全预填充质量。

### 共同创新点
- OSTB提出基于自适应最优运输的共识结构，同时实现模型选择、适配和集成。
- CDS利用约束主导集从多相似项中选择互补证据，避免重复。
- QCFuse通过压缩视图选择器加速RAG缓存融合。
- 三者均面向多源证据或模型，采用结构化方法优化选择与融合。

### 尚未解决的问题
- OSTB的运输计划计算随类别数增加复杂度高。
- CDS需要构建全图，对超大规模文档库扩展性差。
- QCFuse依赖离线关键层分析，对动态模型变化敏感。

### 二次创新路线
#### 路线 1：基于共识运输的约束主导集证据选择
- 核心想法：将OSTB的共识运输计划作为CDS中亲和图的边权重先验，使证据选择不仅考虑相似性还考虑可靠性，并从多文档中挑出共识证据。
- 新问题定义：在多文档多模态VQA中，如何利用多个VLM的共识信号引导证据选择，避免单一模型偏见导致的证据遗漏。
- 机制来源：
  - OSTB的共识运输计划：通过最优运输估计算法统一样本-类别匹配结构。
  - CDS的约束主导集：在查询增强的亲和图上选择互补证据。
- 为什么值得做：CDS仅基于相似度，忽略模型可靠性；OSTB共识计划可编码多模型一致性，作为先验可提升选择鲁棒性。
- 理论/数学创新理由：
  - 数学对象：共识加权亲和图G'的拉普拉斯与主导集
  - 来源分解：OSTB输出运输计划矩阵P，其中P[i][c]表示样本i属于类别c的共识概率；CDS构建原始亲和图G基于特征相似度。
  - 新建模方式：定义新亲和度矩阵A' = α A_orig + (1-α) P·P^T，其中P·P^T捕获样本间共识类别一致性。然后在A'上运行CDS算法，将查询作为硬约束，选出互补证据。
  - 公式草图：设A_orig基于特征相似度，P为运输计划，A' = α A_orig + (1-α) P P^T。CDS求解：max_{x} x^T A' x，s.t. x_i ∈ {0,1}, ∑ x_i = k, x_q = 1（查询）。
  - 为什么可能有效：共识项P·P^T引导选择与多数模型一致的证据，减少单模型偏差；α平衡相似度与共识，使选择既相关又可靠。
- 可验证实验：在VisDoMBench上，使用多个VLM（如LLaVA、Qwen-VL）生成特征，对比原始CDS、OSTB+CDS，评估证据多样性（冗余度）和问答准确率。
- 主要风险：P·P^T可能过于平滑，损失细粒度差异；α调优需验证集。

#### 路线 2：压缩视图的查询感知与关键层联动缓存融合
- 核心想法：将QCFuse的压缩视图选择器与OSTB的共识计划结合：在缓存融合时，不仅考虑查询-块相关性，还考虑块间共识度，优先融合多个模型都认为重要的块。
- 新问题定义：在多模型RAG服务中，如何利用多个模型的共识信号指导缓存块的选取与重计算，减少冗余计算同时保证证据质量。
- 机制来源：
  - QCFuse的块锚点查询探测和关键层K状态选择。
  - OSTB的共识运输计划，可提供跨模型块重要性评分。
- 为什么值得做：QCFuse仅基于单模型查询探测，可能选到模型偏见块；OSTB共识计划可跨模型筛选重要块，提升缓存命中效率。
- 理论/数学创新理由：
  - 数学对象：共识加权重计算代价函数
  - 来源分解：QCFuse单独使用查询-块相似度及关键层K状态；OSTB输出共识计划，但未与缓存集成。
  - 新建模方式：定义块j的共识得分s_j = (1/M) Σ_m P_m(j, c)，其中M为模型数，P_m为模型m的运输计划。缓存选择时，结合QCFuse的得分q_j和共识得分：总得分score_j = β q_j + (1-β) s_j。重计算集合P = {j | score_j > γ}。
  - 公式草图：score_j = β · QCFuse_score(j; query, cache) + (1-β) · (1/M) Σ_m P_m(j, c*)，其中c*为查询预测类别。重计算比率ρ限制|P|/N ≤ ρ。
  - 为什么可能有效：共识得分过滤掉仅单模型高度相关的块，减少缓存污染；β调节平衡，可适应不同模型一致性程度。
- 可验证实验：在医疗VQA数据集上部署多个VLM（如LLaVA-Med, Qwen-VL-Med），测量缓存命中率、预填充时间及准确率，对比QCFuse和QCFuse+共识。
- 主要风险：共识得分计算需运行多个模型，增加在线延迟；跨模型存储开销大。
