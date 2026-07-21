# 研究方向与二次创新路线 · 2026-07-21

- 生成时间：2026-07-21 20:38:52 UTC
- 当日论文数：34
- 方向数：5

## 今日方向总览

| 方向 | 论文数 | 代表论文 |
|---|---:|---|
| 视觉语言模型高效推理与视觉令牌压缩 | 4 | CRISP: Pre-LLM Yet Text-Driven Visual Token Pruning for Efficient LVLM Inference<br>VisCo: Leveraging Large Language Models as Intrinsic Encoders for Visual Token Compression<br>Gaussian Mixture Modeling for Event-Aware Visual Allocation in Long Video Understanding |
| 视觉语言模型空间感知与物理策略推理 | 4 | SportD: Can VLMs Physically Strategize?<br>DM-KG: A Novel Method for Boosting Spatial Cognition of Vision-Language Models in Street View Imagery<br>See like a Robot: Robot-Centric Pointmaps for Vision-Language-Action Models |
| 医学图像分割与半监督/无监督学习 | 4 | Localization-Infused Vision-Language Semantic Fusion for Text-Guided Medical Image Segmentation<br>OFD-Net: Teacher-Free Reliable Semi-supervised Medical Image Segmentation with Orthogonal Feature Disentanglement Net of Foreground-Background<br>Memory-Supported Synergistic Adaptation for Training-Free Test-Time Medical Image Segmentation |
| 医学视觉语言模型的检索增强与证据推理 | 3 | NGM-RAG: Neural Graph Matching based Retrieval-Augmented Generation<br>MamaBench: Benchmarking LLM Robustness in Maternal and Child Health Diagnosis through Counterfactual Clinical Perturbation<br>Cost-Pragmatic Quality Gating and Selection-Fusion Multi-Model Combiners for BioASQ Phases A+ and B |
| 视觉语言表示学习与少样本泛化 | 4 | AspectCLIP: Optimizing CLIP Representation Space via Aspect-Guided Consistency Regularization<br>PRiSM: Prototype Regularization for Few-Shot VLMs<br>Can Experts Adapt Without Training? On Test-Time Modality Generalization in MVLMs |

## 方向 1：视觉语言模型高效推理与视觉令牌压缩
针对VLM中视觉令牌数量庞大导致推理开销高的问题，结合多篇论文的互补机制，设计新的令牌压缩与分配策略，在保持性能的同时大幅降低计算量。

### 代表论文

- [CRISP: Pre-LLM Yet Text-Driven Visual Token Pruning for Efficient LVLM Inference](https://arxiv.org/abs/2607.16326v1)：大型视觉语言模型（LVLM）推理时需处理大量视觉token，现有剪枝方法存在缺陷。本文提出CRISP，一种在LLM之前但文本驱动的视觉token剪枝框架，通过两阶段流水线（先识别文本对齐token，再增强上下文完整性），在激进剪枝下保持高达99.5%准确率，同时降低推理成本和延迟2倍以上。
- [VisCo: Leveraging Large Language Models as Intrinsic Encoders for Visual Token Compression](https://arxiv.org/abs/2607.12756v1)：提出VisCo，一种训练高效的视觉token压缩框架，通过参数共享自编码器重用预训练VLM自身作为内在压缩器，使用记忆token实现视觉信息压缩。
- [Gaussian Mixture Modeling for Event-Aware Visual Allocation in Long Video Understanding](https://arxiv.org/abs/2607.12557v1)：提出GMM-EVA，一种无需训练、即插即用的关键帧分配方法，通过高斯混合模型对帧级相关性分数进行事件级建模，并对每个事件差异化分配高分辨率主关键帧和低分辨率辅关键帧，在仅用约一半视觉token预算的情况下达到或超越均匀采样和现有方法的性能。
- [Attention-Free and Lightweight Token Reduction for Efficient Vision-Language Models](https://arxiv.org/abs/2607.13500v1)：针对视觉语言模型在边缘设备上计算开销大的问题，提出了一种轻量级、无需注意力的令牌缩减框架。该框架通过信息熵评估令牌重要性，并利用变换一致性实现多样性选择，在保持性能的同时显著加速推理。

### 共同创新点
- 利用文本指令或查询相关性引导视觉令牌的筛选与加权
- 采用自编码或记忆令牌结构实现轻量级压缩
- 通过事件或语义感知分配预算，而非均匀处理

### 尚未解决的问题
- 现有方法在极端压缩比下对细粒度空间关系保留不足
- 多阶段流水线增加延迟，难以实现端到端优化
- 缺少对动态输入复杂度自适应调整压缩率的机制

### 二次创新路线
#### 路线 1：查询引导的层级式视觉令牌自适应压缩
- 核心想法：将CRISP的文本驱动预LLM剪枝与VisCo的参数共享自编码器结合，先通过查询相关性标记关键区域，再利用记忆令牌压缩次要区域，实现层级式自适应压缩。
- 新问题定义：提出查询引导的视觉令牌自适应压缩任务：给定图像和查询，输出一组压缩后的视觉令牌，使得在后续LLM推理中，对于查询相关的空间和语义信息保持高保真度，而无关区域被高度压缩。
- 机制来源：
  - CRISP（2607.16326v1）解决了文本相关视觉令牌的识别问题，但其剪枝后仅保留文本对齐令牌，丢失了场景上下文。
  - VisCo（2607.12756v1）通过记忆令牌和自编码器实现了高质量压缩，但未区分令牌对查询的重要性。
  - 本路线融合两者：先用CRISP的文本对齐度量筛选出高相关令牌，对剩余令牌用VisCo的记忆令牌压缩，同时保留部分上下文令牌以维持场景完整性。
- 为什么值得做：CRISP仅做早剪枝但丢失全局上下文，VisCo压缩质量高但未利用查询信息。两者互补可同时兼顾效率与质量。
- 理论/数学创新理由：
  - 数学对象：信息瓶颈与率失真优化目标
  - 来源分解：CRISP提供了基于文本相关性的重要性得分函数s(x_i)=cos(v_i, t_q)，VisCo提供了自编码重构损失L_recon=||x_i - Dec(Enc(x_i))||^2。
  - 新建模方式：联合优化目标：min_{M, θ} Σ_{i∈H} L_recon(Enc(x_i)) + λ Σ_{i∈H} s(x_i) + γ Σ_{i∈L} L_recon(Enc(x_i))，其中H为高相关令牌集，L为低相关令牌集，通过稀疏约束控制总令牌数。
  - 公式草图：设视觉令牌集合V={v_1,...,v_N}，查询文本嵌入t_q。定义相关性得分r_i=cos(v_i, t_q)。选择阈值τ，令H={i|r_i≥τ}，L=V\H。总令牌预算B，则目标为：min Σ_{i∈H} ||v_i - Dec(Enc(v_i))||^2 + λ Σ_{i∈L} ||v_i - Dec(Enc(v_i))||^2，满足|H|+|L'|≤B，其中L'为L中经过记忆令牌编码后的压缩表示。
  - 为什么可能有效：通过查询相关性指导预算分配，高相关令牌保留完整信息，低相关令牌被高度压缩，可以有效减少冗余token的干扰，同时保证关键信息的完整性，从而在压缩率较大时仍保持下游任务性能。
- 可验证实验：在LLaVA-1.5模型上，基于COCO Caption和VQAv2数据集，比较不同压缩率下与CRISP、VisCo的性能差异，评估FID、准确率和推理时间。
- 主要风险：高相关令牌选择可能过于依赖CLIP度量，若查询-图像语义偏移（如医学图像）可能失效；记忆令牌质量受限于预训练分布。

## 方向 2：视觉语言模型空间感知与物理策略推理
结合运动策略评估、街景空间图谱、机器人坐标对齐和布局推理，构建统一的空间感知增强框架，提升VLM在真实场景中的物理推理与决策能力。

### 代表论文

- [SportD: Can VLMs Physically Strategize?](https://arxiv.org/abs/2607.14616v1)：提出SportD基准，通过价值驱动评分评估VLMs在足球比赛中的物理策略推理能力。
- [DM-KG: A Novel Method for Boosting Spatial Cognition of Vision-Language Models in Street View Imagery](https://arxiv.org/abs/2607.12319v1)：针对视觉语言模型在街景图像中存在的空间语义幻觉问题，提出DM-KG方向度量知识图谱框架，通过全景分割与度量深度估计提取实体3D空间坐标，构建JSON格式知识图作为显式几何先验，注入VLM引导空间推理。在公共空间问答基准上，距离估计MAE降低31.1%，方向判断平均角度误差降低65.8%，同时保持高问答成功率。
- [See like a Robot: Robot-Centric Pointmaps for Vision-Language-Action Models](https://arxiv.org/abs/2607.11498v1)：提出机器人中心点地图（robot-centric pointmaps），将场景点在机器人坐标系中的3D坐标编码为图像像素，以消除VLA模型中观察帧（相机帧）与动作帧（机器人帧）之间的不匹配问题。
- [Think, Plan, Paint: Layout-Aware Reasoning for Controllable Image Generation in Unified Models](https://arxiv.org/abs/2607.16409v1)：提出ATLAS框架，通过'思考-规划-绘制'范式和强化学习布局对齐，实现统一多模态大模型中的可控图像生成，显著提升复杂空间指令遵循能力。

### 共同创新点
- 将空间几何信息显式编码为结构化表示（如点图、知识图谱、布局）
- 引入价值模型或度量标准定量评估空间决策质量
- 通过中间表示（坐标、距离、方向）桥接观察与动作空间

### 尚未解决的问题
- 现有方法各自针对特定场景，缺乏统一的VLM空间推理框架
- 空间表示与语言指令的对齐依赖外部标注或预训练模型
- 多步空间推理的误差累积和鲁棒性不足

### 二次创新路线
#### 路线 1：基于统一空间知识图谱的VLM物理推理增强
- 核心想法：将DM-KG的方向-距离图、SportD的价值模型和机器人中心点地图融合为统一空间知识图谱，作为VLM的显式空间先验，提升跨场景的物理策略推理能力。
- 新问题定义：定义统一空间增强的物理推理任务：给定任务文本指令和视觉输入，VLM需要构建或利用一个包含物体3D位置、方向、距离以及动作价值的空间知识图谱，并基于此生成最优动作序列（如足球传球、导航指令）。
- 机制来源：
  - DM-KG（2607.12319v1）解决了街景中物体方向-距离的显式抽取，但其格式为JSON图，缺少动作价值信息。
  - SportD（2607.14616v1）提供了基于VAEP的动作价值评估，但依赖已知场景结构，无法泛化到新场景。
  - 机器人中心点地图（2607.11498v1）将3D坐标对齐到机器人坐标系，但未与语言指令深度耦合。
  - 本路线将DM-KG的图结构作为骨架，注入SportD的价值模型计算每个空间关系的决策效用，并利用点地图的3D坐标进行几何校准，形成一张带权重的空间知识图谱。
- 为什么值得做：DM-KG提供静态空间关系，SportD提供动态决策价值，点地图提供机器人帧几何信息，三者互补可覆盖从静态到动态、从观察到动作的完整空间推理。
- 理论/数学创新理由：
  - 数学对象：加权空间图与价值迭代
  - 来源分解：DM-KG构建了节点（物体）和边（方向、距离）的无权重图G；SportD提供了动作价值函数V(s,a)；点地图提供了坐标转换矩阵T。
  - 新建模方式：定义图G'= (V, E, W)，其中节点v_i包含3D坐标p_i，边e_ij包含方向d_ij和距离l_ij，权重w_ij = V(s, a_ij)/max_a V(s,a)实现归一化价值。VLM输入为视觉+指令，先通过DM-KG的提取方法得到G'，再通过图神经网络编码，最后结合价值进行动作选择。
  - 公式草图：令节点特征h_i^0 = f_v(visual_region_i)，边特征e_ij = [d_ij, l_ij]；价值权重w_ij = softmax(V(s, a_ij))。图卷积：h_i^{(k+1)} = ReLU(Σ_{j∈N(i)} w_ji W_k [h_j^{(k)} || e_ji])。最终动作概率p(a_ij) = softmax(MLP(h_i^{(K)}))。
  - 为什么可能有效：通过价值权重引导图信息传播，使模型关注高价值空间关系，同时结合3D坐标实现不同视角下的几何不变性，从而提升空间推理的准确性和泛化性。
- 可验证实验：在SportD足球决策基准和DM-KG街景问答上联合评估，比较与单独使用各模块的性能，测量最优动作准确率和空间关系错误率。
- 主要风险：图构建依赖预训练模型（如分割、深度估计），在遮挡或光照极差场景可能引入噪声；价值模型需领域适配。

## 方向 3：医学图像分割与半监督/无监督学习
结合文本引导、正交特征解耦、测试时记忆与多智能体协同，构建鲁棒的医学图像分割框架，在标注稀缺和分布偏移下提升性能。

### 代表论文

- [Localization-Infused Vision-Language Semantic Fusion for Text-Guided Medical Image Segmentation](https://arxiv.org/abs/2607.16327v1)：提出LoG框架，通过联合多尺度目标定位任务实现三级定位引导的语义融合，解决文本引导医学图像分割中目标位置信息未被显式利用和融合策略单一的问题。
- [OFD-Net: Teacher-Free Reliable Semi-supervised Medical Image Segmentation with Orthogonal Feature Disentanglement Net of Foreground-Background](https://arxiv.org/abs/2607.16705v1)：提出无教师单网络框架OFD-Net，通过正交特征解耦模块（OFDM）分离前景-背景表示，利用解耦引导模块（DGM）注入结构先验，并设计可靠性感知伪标签学习机制，解决半监督医学图像分割中伪标签质量低导致误差累积和确认偏差的问题。
- [Memory-Supported Synergistic Adaptation for Training-Free Test-Time Medical Image Segmentation](https://arxiv.org/abs/2607.17693v1)：针对测试时自适应（TTA）中基于视觉-语言模型（VLM）的医学图像分割任务，现有微调方法因噪声更新常损害预训练特征。提出无训练记忆支持的协同自适应（MSSA）框架，通过在线记忆动态选择可靠跨模态预测作为语义先验，并结合跨图像结构对齐实现鲁棒自适应。在多个医学分割基准上，MSSA一致提升VLM分割模型，超越现有时序微调方法，DSC提升最高达12.2%，mIoU提升11.7%。
- [Understanding From Human Perspective: A Multi-agent System for Interactive Egocentric Medical Image Segmentation](https://arxiv.org/abs/2607.17341v1)：提出第一个用于交互式自我中心医学图像分割的多智能体系统EgoMed-Agent，通过目标确认和定位引导传播两个工作流解决语义模糊和视觉变异挑战。

### 共同创新点
- 利用文本或临床参数作为语义先验引导分割
- 通过特征解耦或记忆库维护内部结构化参考
- 引入交互式确认机制或协同适应策略增强鲁棒性

### 尚未解决的问题
- 多模态融合中文本和图像对齐精度不足
- 半监督学习对极端外观变化的伪标签质量仍不可靠
- 测试时适应方法在连续分布漂移下的稳定性有限

### 二次创新路线
#### 路线 1：文本引导的可靠伪标签与特征解耦协同框架
- 核心想法：将LoG的三级定位融合约束与OFD-Net的正交特征解耦结合，利用文本提取定位信息作为解耦的结构先验，提升半监督医学图像分割的伪标签可靠性。
- 新问题定义：提出文本引导的半监督医学图像分割问题：给定少量有标注图像（含文本描述）和大量无标注图像（可能无文本），利用文本中的定位信息辅助特征解耦，生成可靠伪标签以训练分割模型。
- 机制来源：
  - LoG（2607.16327v1）解决了文本位置信息未被显式利用的问题，通过多尺度定位任务输出定位图。
  - OFD-Net（2607.16705v1）提出了正交前景-背景特征解耦，并基于解耦一致性评估伪标签可靠性。
  - 本路线将LoG的定位图作为OFD-Net中解耦模块的辅助信号，使其前景-背景分离更准确；同时利用解耦一致性进一步过滤不可靠的伪标签。
- 为什么值得做：LoG提供文本定位先验，OFD-Net提供前景-背景正交解耦，两者结合可生成更准确的伪标签并减少确认偏差。
- 理论/数学创新理由：
  - 数学对象：定位增强的正交约束与加权伪标签损失
  - 来源分解：LoG的定位损失L_loc = KL(定位图 || 预测掩膜)；OFD-Net的正交损失L_orth = ||F_fg^T F_bg||_F^2 和可靠性权重w=Dice(Pred, P_fg)。
  - 新建模方式：联合训练时，对无标注数据引入定位引导的正交损失L_orth_loc = ||(F_fg⊙M_loc)^T (F_bg⊙(1-M_loc))||_F^2，其中M_loc为LoG预测的定位图。伪标签损失L_pseudo = Σ_i w_i * Dice(pred_i, pseudo_i)，其中w_i = Dice(pred_i, P_fg_i) * Dice(pred_i, M_loc_i)。
  - 公式草图：定义定位图M_loc ∈ [0,1]^{H×W}来自LoG定位模块。正交损失变为：L_orth_loc = Σ ||(F_fg ⊙ M_loc)^T (F_bg ⊙ (1-M_loc))||_F^2。总损失L = L_sup + λ1 L_orth_loc + λ2 L_pseudo。
  - 为什么可能有效：定位图作为软注意力，约束前景-背景解耦更加关注文本描述区域，避免背景噪声干扰；结合定位一致性的伪标签权重可进一步减少错误累积。
- 可验证实验：在ACDC和MSCI数据集上，使用10%标注，对比LoG、OFD-Net和本路线，计算Dice和HD95。
- 主要风险：文本描述需要专家标注，增加成本；定位图质量依赖文本特征提取，弱描述可能导致误导。

## 方向 4：医学视觉语言模型的检索增强与证据推理
结合图匹配RAG、证据锚定RAG和成本实用检索策略，提升医学VLM在多跳推理和反事实诊断中的鲁棒性和事实准确性。

### 代表论文

- [NGM-RAG: Neural Graph Matching based Retrieval-Augmented Generation](https://arxiv.org/abs/2607.11159v1)：提出NGM-RAG框架，通过图构建、神经图匹配和自适应加权策略，将文本匹配与图神经网络结合，提升多跳推理和长上下文问答的检索增强生成性能。
- [MamaBench: Benchmarking LLM Robustness in Maternal and Child Health Diagnosis through Counterfactual Clinical Perturbation](https://arxiv.org/abs/2607.14385v2)：提出MamaBench反事实基准和证据锚定RAG（EA-RAG）方法，揭示LLMs在母婴健康诊断中的鲁棒性差距，并通过临床参数提取、覆盖审计与对比子查询降低偏差陷阱率。
- [Cost-Pragmatic Quality Gating and Selection-Fusion Multi-Model Combiners for BioASQ Phases A+ and B](https://arxiv.org/abs/2607.13551v1)：提出成本实用的质量门控重检索策略和选择-融合多模型组合分解方法，在BioASQ任务上降低重检索成本12%并提升列表F1，通过选择/融合分解预测并验证了不同组合器在指标上的优势差异。

### 共同创新点
- 引入图结构或证据覆盖度量替代传统相似度检索
- 设计反事实或质量门控机制确保检索结果的诊断相关性
- 通过多模型组合或同步融合提升答案可靠性

### 尚未解决的问题
- 图构建依赖LLM，在医学领域可能引入知识错误
- 反事实鲁棒性在领域泛化中仍存在显著差距
- 多模型组合的预算和延迟在实际部署中需优化

### 二次创新路线
#### 路线 1：医学图增强反事实RAG框架
- 核心想法：将NGM-RAG的神经图匹配结构与EA-RAG的反事实覆盖审计结合，构建医学诊断的鲁棒检索框架，显式建模临床逻辑关系并抵抗诊断焦点偏差。
- 新问题定义：定义医学图增强反事实RAG任务：给定患者临床叙事，系统需构建医学知识图谱（包含症状、检查、疾病、治疗的关系），利用图匹配检索相关证据，并特别评估反事实扰动下的检索鲁棒性，最终生成诊断和建议。
- 机制来源：
  - NGM-RAG（2607.11159v1）解决了多跳推理中关系图匹配问题，但其检索只基于静态知识库，未考虑反事实扰动。
  - EA-RAG（2607.14385v2）通过证据覆盖审计对比子查询增强反事实鲁棒性，但未利用图结构进行关系推理。
  - 本路线将NGM-RAG的图构建与图匹配作为基础检索，再引入EA-RAG的覆盖审计模块对每个临床参数进行覆盖度检查，对覆盖不足的参数生成基于图结构的对比子查询。
- 为什么值得做：NGM-RAG擅长多跳关系推理，EA-RAG擅长反事实鲁棒性，两者互补可同时提升复杂推理和对抗移位能力。
- 理论/数学创新理由：
  - 数学对象：图结构上的证据覆盖优化与反事实对比学习
  - 来源分解：NGM-RAG提供图匹配得分S_GNN = cos(GNN(q), GNN(d))，EA-RAG提供覆盖度度量C(e_j) = max_{b∈B} cos(e_j, b)以及反事实检索子查询生成。
  - 新建模方式：对每个临床参数e_j，其图节点表示为h_j，检索块b_i的图节点表示为g_i。联合得分S(e_j, b_i) = α cos(h_j, g_i) + (1-α) 1_{C(e_j) < τ} cos(h_j, g_i')，其中g_i'为反事实子查询的节点。总目标为最大化覆盖度总和Σ_j C(e_j)同时最小化图匹配损失。
  - 公式草图：定义覆盖度C(e_j) = max_i cos(h_j, g_i)。若C(e_j)<τ，则生成子查询向量q_sub_j = MLP([h_j, Δ])，计算补充覆盖S_sub_j = max_i cos(q_sub_j, g_i)。最终检索得分R = Σ_{e_j} (C(e_j) + β * S_sub_j * 1_{C(e_j)<τ})。
  - 为什么可能有效：图匹配提供结构化关系，覆盖审计确保所有关键参数被检索，反事实子查询针对参数缺口定向补充，从而在复杂临床推理和反事实扰动下保持高召回率和准确率。
- 可验证实验：在MamaBench和MedQA数据集上，对比NGM-RAG、EA-RAG和本路线，评估BTR、F1和推理延迟。
- 主要风险：图构建开销大，医学实体关系抽取错误会传播；反事实子查询生成依赖LLM，可能引入hallucination。

## 方向 5：视觉语言表示学习与少样本泛化
结合方面感知正则化、原型正则化、测试时贝叶斯适应和统一表示框架，提升VLM在数据不平衡、模态偏移下的泛化能力。

### 代表论文

- [AspectCLIP: Optimizing CLIP Representation Space via Aspect-Guided Consistency Regularization](https://arxiv.org/abs/2607.13805v1)：提出AspectCLIP，通过方面感知语义聚类和方面引导的一致性正则化，优化CLIP表示空间以尊重图文信息不对称，提升下游任务性能。
- [PRiSM: Prototype Regularization for Few-Shot VLMs](https://arxiv.org/abs/2607.17820v1)：提出PRiSM，一种类原型正则化方法，通过最大化类间距离、支持特征对齐和原型保真度的多目标损失，结合块Majorize-Minimize优化器，有效缓解少样本视觉语言模型在类别不平衡和高类别数下的性能下降。
- [Can Experts Adapt Without Training? On Test-Time Modality Generalization in MVLMs](https://arxiv.org/abs/2607.16726v1)：提出一种完全免优化的测试时模态泛化框架MoBE，通过熵引导动态路由和专家贝叶斯适应，无需梯度更新即可实现鲁棒的模态泛化。
- [Let RGB Be the Language of Vision](https://arxiv.org/abs/2607.12450v1)：提出RINO框架，将各种视觉信息统一表示为RGB图像，视觉任务转化为RGB到RGB的图像编辑问题，通过共享编码解码架构，无需任务微调即可零样本迁移。

### 共同创新点
- 引入结构化的先验（方面簇、原型、专家）指导表示学习
- 测试时免优化适应机制应对分布偏移
- 统一多模态表示为RGB或共享空间降低模态鸿沟

### 尚未解决的问题
- 方面聚类静态固定，无法适应训练过程表示变化
- 原型正则化对极端不平衡场景的鲁棒性不足
- 测试时适应在连续多步分布漂移中衰减

### 二次创新路线
#### 路线 1：动态方面感知的测试时原型适应框架
- 核心想法：将AspectCLIP的动态聚类更新思想与MoBE的测试时贝叶斯适应结合，在测试阶段在线调整方面簇原型，实现无需训练的分布偏移适应。
- 新问题定义：提出测试时方面感知原型适应任务：在测试阶段，模型接收未标注的测试流，利用其与预训练方面簇的原型相似度动态调整原型向量，并通过贝叶斯更新实现无参数适应，提升下游分类或检索性能。
- 机制来源：
  - AspectCLIP（2607.13805v1）解决了图文信息不对称导致的表示空间扭曲，通过静态文本聚类定义方面簇。
  - MoBE（2607.16726v1）提出了免优化的测试时适应框架，通过熵路由和贝叶斯更新调整专家输出。
  - 本路线将AspectCLIP的方面簇作为MoBE中专家的原型，在测试时根据当前批次嵌入的熵值动态调整簇原型（指数移动平均），并利用贝叶斯公式更新类别先验。
- 为什么值得做：AspectCLIP通过方面感知正则化优化表示空间，MoBE在测试时动态路由专家，两者结合可在测试时自适应调整表示空间以匹配目标分布。
- 理论/数学创新理由：
  - 数学对象：动态原型更新与贝叶斯后验估计
  - 来源分解：AspectCLIP提供静态聚类质心μ_c，MoBE提供贝叶斯更新公式P(y|x) ∝ P(u|x) * π(y)。
  - 新建模方式：测试时，对每个批次，计算图像嵌入v_i，分配方面簇c_i = argmax_c cos(v_i, μ_c)。更新簇原型：μ_c ← (1-γ)μ_c + γ * mean({v_i: c_i = c})。类别先验π(y)初始为均匀分布，随着高置信度样本积累，π(y) ← (1-η)π(y) + η * 1_{y=argmax P(y|x)}。最终预测通过贝叶斯融合。
  - 公式草图：令μ_c^{(t)} = (1-γ)μ_c^{(t-1)} + γ * mean({v_i: argmax_j cos(v_i, μ_j^{(t-1)}) = c})。后验概率P(y|x) = softmax(τ v_i^T W_y) ⊙ π(y) / Σ_y softmax(...)，其中π(y)用指数移动平均更新。
  - 为什么可能有效：动态原型更新能在测试时捕获新数据的分布特征，贝叶斯机制融合先验和似然，对于类别不平衡或模态偏移具有自适应性，且无需反向传播，适合在线场景。
- 可验证实验：在领域偏移数据集（如ImageNet-R、CIFAR-10-C）上，与AspectCLIP和MoBE对比，评估分类准确率和原型更新稳定性。
- 主要风险：动态原型可能受批次噪声影响，在极端小批量下不稳定；贝叶斯更新对错误积累敏感。
