# 研究方向与二次创新路线 · 2026-07-05

- 生成时间：2026-07-05 21:30:09 UTC
- 当日论文数：34
- 方向数：4

## 今日方向总览

| 方向 | 论文数 | 代表论文 |
|---|---:|---|
| 医学视觉语言模型中的幻觉缓解与可靠性优化 | 3 | FADE: Mitigating Hallucinations by Reducing Language-Prior Dominance in Large Vision-Language Models<br>Reliability-Prioritized Fine-Grained Generation in Multimodal Large<br>Do Multimodal Large Language Models Need Reasoning to Classify Dementia from Speech? |
| 医学图像分割与表示学习中的域适应与结构先验 | 4 | Does Your ViT Still Need U-Net for Segmentation?<br>PSP: Harnessing Position and Shape Priors for Cross-Domain Few-Shot Medical Image Segmentation<br>Learning from Acquisition: Metadata-driven Multimodal Pre-training for Cardiac MRI |
| 医学报告生成与检索中的结构化知识融合 | 4 | Prior-Anchored Debiasing for Long-Tailed Multi-Organ Pathology Report Generation<br>Spatio-Temporal and Clinical Conditioning for Fine-Grained Radiology Report Retrieval<br>Discrete Diffusion Language Models for Interactive Radiology Report Drafting |
| 视觉语言模型的效率与自适应推理 | 4 | On Test-Time Scaling for Vision-Language Models<br>Fast Enough to Act: Spatio-Temporal Visual Token Merging for Low-Latency Robotic VLMs and VLAs<br>AB-RAG: Adaptive Budgeted Retrieval-Augmented Generation for Reliable Question Answering |

## 方向 1：医学视觉语言模型中的幻觉缓解与可靠性优化
本方向聚焦于多模态大语言模型在医学影像分析中生成不可靠或幻觉内容的问题，通过机制分析、可靠性优先优化和内部表示利用三种互补策略，旨在提升模型在细粒度描述和诊断任务中的可信度。

### 代表论文

- [FADE: Mitigating Hallucinations by Reducing Language-Prior Dominance in Large Vision-Language Models](https://arxiv.org/abs/2606.29431v1)：通过机制分析发现LVLM中关键层FFN是语言先验源，提出无训练方法FADE衰减FFN输出以缓解幻觉。
- [Reliability-Prioritized Fine-Grained Generation in Multimodal Large](https://arxiv.org/abs/2606.29573v2)：提出了一个粒度感知基准GranFact、层次感知评估算法和可靠性优先的偏好优化方法（RP-DPO），以解决多模态大语言模型细粒度视觉描述生成中的可靠性-粒度权衡问题。
- [Do Multimodal Large Language Models Need Reasoning to Classify Dementia from Speech?](https://arxiv.org/abs/2607.00260v1)：提出DeTAiL框架，通过利用推理MLLMs的内部表示而非依赖文本推理，改进了自动痴呆分类的准确性和迁移性。

### 共同创新点
- 从信息流角度揭示了语言先导（FFN）与视觉证据（注意力）的冲突机制
- 提出了可靠性优先的偏好优化框架，通过回滚构造保证粒度与正确性平衡
- 证明了内部隐藏表示比文本推理更可靠地编码诊断信息

### 尚未解决的问题
- 现有方法分别优化模型不同阶段（推理时、训练时、后适配），未形成统一框架
- 缺乏同时处理文本推理幻觉和内部表示偏移的联合策略
- 可靠性度量未与临床诊断权重结合

### 二次创新路线
#### 路线 1：语言先导衰减与可靠性优先DPO联合训练框架
- 核心想法：将FADE的FFN衰减机制嵌入到RP-DPO的训练过程中，在模型生成时动态抑制语言先导，同时用可靠性优先的偏好优化训练模型学会在早期步骤纠正错误推理，从而在训练和推理两个阶段阻断幻觉传递。
- 新问题定义：针对医学VQA，定义联合训练-推理的幻觉抑制问题：在训练时用RP-DPO优化生成策略，在推理时自动检测并衰减关键层FFN输出，确保最终回答既可靠又细粒度。
- 机制来源：
  - FADE（2606.29431v1）提供了FFN衰减机制，通过logit lens识别关键层（层16-22）并衰减因子(1-α)抑制语言先导，保留视觉证据
  - RP-DPO（2606.29573v2）提供了可靠性优先的偏好优化方法，通过回滚构造可靠性正负样本和DPO训练，强制模型优先保证正确性再追求细粒度
- 为什么值得做：FADE证明FFN是语言先导来源，但需手动确定关键层和衰减强度；RP-DPO从训练角度优化可靠性，但未干预推理时的动态。两者结合可实现从训练到推理的完整幻觉防护链。
- 理论/数学创新理由：
  - 数学对象：联合优化目标包含训练阶段的DPO损失和推理阶段的衰减函数
  - 来源分解：FADE处理推理时FFN输出的衰减因子，RP-DPO处理训练时偏好对的损失函数
  - 新建模方式：训练阶段：L = L_DPO(π_θ) + λ * L_aux，其中L_aux惩罚生成早期token的FFN输出与视觉证据的差异。推理阶段：对关键层l∈L_crit，输出修正为h_l' = (1-α) * FFN(h_{l-1}) + α * h_{l-1}，α由置信度动态调节
  - 公式草图：设模型为π_θ，生成序列y=(y_1,...,y_T)。定义关键层集合L_crit，推理时对每一层l，衰减后表示h_l' = (1-β_l) * h_l^{attn} + β_l * h_l^{ffn}，其中β_l由该层FFN贡献的符号决定。训练时使用RP-DPO损失：L_RP = -E[log σ(β_rel * (r(y_w) - r(y_l)))]，其中r(y)为可靠性评分
  - 为什么可能有效：通过训练时提前惩罚早期FFN偏差，模型在推理自然生成更可靠的推理链；推理时动态衰减则进一步抑制突发性语言先导，双重机制互补降低幻觉率
- 可验证实验：在医学VQA数据集（如PathVQA、Slake）上对比FADE、RP-DPO及联合方法的幻觉率、正确率和细粒度F1。使用GranFact的层次评估指标。
- 主要风险：衰减强度α和训练权重λ需联合调参，可能在不同数据集上敏感；联合训练可能增加收敛难度

#### 路线 2：隐藏表示引导的可靠性优先解码
- 核心想法：结合DeTAiL的隐藏表示优势和GranFact的可靠性优先思想，在解码阶段利用MLLM内部隐藏状态计算可靠性分数，动态决定是否回滚到更粗粒度描述，而非依赖文本推理。
- 新问题定义：定义隐藏表示驱动的自适应细粒度解码问题：对于每个生成token，计算其隐藏状态与视觉证据的兼容性得分，当得分低于阈值时自动替换为粗粒度类别，实现无需外部解析的可靠性优先生成。
- 机制来源：
  - DeTAiL（2607.00260v1）提供使用隐藏表示进行分类的方法，通过训练MLP适配器从MLLM最后一层隐藏状态中提取诊断相关信息，避免文本推理幻觉
  - GranFact（2606.29573v2）提供了回滚机制和层次评估框架，通过替换为最近祖先类别实现可靠性优先
- 为什么值得做：DeTAiL证明隐藏表示比文本推理更鲁棒；GranFact的回滚机制需要LLM解析，容易出错。用隐藏表示直接指导回滚可避免解析误差，同时保留可靠性优先。
- 理论/数学创新理由：
  - 数学对象：隐藏状态空间中的可靠性度量与自适应回滚函数
  - 来源分解：DeTAiL使用隐藏状态均值训练MLP分类器；GranFact使用LLM解析文本后回滚至祖先类别
  - 新建模方式：定义可靠性分数R(h) = sim(h, v_vis)，其中h为当前步隐藏状态，v_vis为视觉特征。若R(h) < τ，则将当前预测y替换为argmax_{c'∈ancestors(y)} p(c'|h)。整体损失为加权交叉熵：L = -log p(y_gt) + γ * max(0, τ - R(h))
  - 公式草图：设隐藏状态h_t，视觉特征池V={v_i}。计算注意力加权视觉上下文c = ∑ α_i v_i，α_i = softmax(h_t^T v_i)。定义置信度s = σ(MLP([h_t; c]))。若s < 0.5，则将当前预测类别y替换为最近祖先类别y' = parent(y)。最终损失L = -log p(y_gt) + β * (1 - s)
  - 为什么可能有效：隐藏状态直接编码了多模态对齐信息，比文本推理更鲁棒；自适应回滚避免了生成过于具体的错误描述，同时保持粒度优先原则
- 可验证实验：在GranFact数据集上比较隐藏表示引导的回滚与LLM解析回滚的正确率、粒度得分和延迟。使用层次感知评估。
- 主要风险：隐藏状态可靠性阈值的设定需要验证集调优；对于需要长链推理的任务，隐藏状态可能不包含完整语义

## 方向 2：医学图像分割与表示学习中的域适应与结构先验
本方向利用多种结构先验（位置、形状、元数据、细胞检测）来提升医学图像分割和表示学习在跨模态、少样本和不同尺度下的泛化能力与效率。

### 代表论文

- [Does Your ViT Still Need U-Net for Segmentation?](https://arxiv.org/abs/2607.00223v1)：证明现代ViT骨干下U-Net解码器对医学图像分割不再必要，并提出纯编码器分割框架EoSeg，采用多级查询建模与可学习块融合实现高效分割。
- [PSP: Harnessing Position and Shape Priors for Cross-Domain Few-Shot Medical Image Segmentation](https://arxiv.org/abs/2606.28799v1)：提出PSP框架，利用位置和形状先验作为跨域不变特征，通过PCE、SPM、HPP三个模块实现跨模态少样本医学图像分割，显著优于现有方法。
- [Learning from Acquisition: Metadata-driven Multimodal Pre-training for Cardiac MRI](https://arxiv.org/abs/2606.28991v1)：提出MetaCLIP-CMR，利用心脏MRI采集元数据生成文本，通过软标签对比学习预训练图像编码器，在模态/视图分类和分割任务上优于ImageNet和掩码重建，且仅需不到1%的大规模模型预训练图像量即可达到可比性能。
- [CellDETR: A Detection-Guided Framework for Scalable Cell Representation Learning from Histopathology Images](https://arxiv.org/abs/2606.29463v1)：提出CellDETR框架，基于Deformable DETR，通过位置特征解耦和框约束注意力实现可扩展的细胞级表示学习，在监督分类和跨数据集迁移上达到最优。

### 共同创新点
- 通过显式编码位置、形状或元数据等域不变特征减少对纹理的依赖
- 从不同粒度（像素、细胞、器官）引入结构约束以提高表达效率
- 利用检测引导或查询机制实现更精准的局部特征提取

### 尚未解决的问题
- 不同先验（位置、形状、元数据）尚未在统一框架下融合
- 现有方法在极低数据量下仍需足够支撑掩码或元数据标注
- 细胞级表示与器官级分割之间的跨尺度知识迁移未探索

### 二次创新路线
#### 路线 1：位置-形状-元数据三重先验引导的跨模态分割框架
- 核心想法：将PSP的位置坐标嵌入和形状原型调制与MetaCLIP-CMR的元数据文本监督相结合，利用元数据作为弱标签指导位置-形状原型的学习，实现无需人工标注的跨模态少样本分割。
- 新问题定义：定义零/少标注的跨模态医学图像分割问题：给定一个源模态的少量标注和大量目标模态的未标注图像（仅含元数据），利用元数据自动生成文本描述，指导位置-形状原型的提取和调制，实现目标模态的少样本分割。
- 机制来源：
  - PSP（2606.28799v1）提供位置坐标嵌入（PCE）和形状原型调制（SPM），利用显式位置和形状先验解耦结构与纹理
  - MetaCLIP-CMR（2606.28991v1）提供元数据到文本的自动转换和软标签对比学习，利用采集参数生成弱监督信号
- 为什么值得做：PSP依赖手工标注的支撑掩码获取形状先验，MetaCLIP-CMR证明元数据可自动生成文本监督。两者结合可在无掩码条件下学习形状先验，大幅降低标注成本。
- 理论/数学创新理由：
  - 数学对象：元数据引导的形状原型学习与位置增强特征
  - 来源分解：PSP使用支撑掩码计算几何和频谱形状先验；MetaCLIP-CMR使用元数据模板生成文本并对比学习
  - 新建模方式：将元数据文本嵌入e_meta与形状先验向量v_spec进行对齐：L_align = ||e_meta - MLP(v_spec)||^2。同时利用元数据文本作为查询，从支撑图像中通过注意力提取形状相关特征，替代手工掩码。最终分割损失为交叉熵与对齐损失的加权和
  - 公式草图：设支撑图像I_s及其元数据m_s，生成文本t_s = template(m_s)。通过文本编码器得到e_txt。从I_s中提取特征F_s，通过PCE得到位置增强特征F̂_s。计算形状先验v_shape = SPM(F̂_s, e_txt) (将e_txt作为条件)。对齐损失L_align = MSE(e_txt, MLP(v_shape))。最终预测采用PSP的HPP模块
  - 为什么可能有效：元数据提供了域不变的语义线索（如模态、视图），与位置-形状先验天然互补。文本对齐约束使得形状原型学习不再依赖精确掩码，从而在未标注目标域上也可提取鲁棒形状特征
- 可验证实验：在MRI-CT跨模态分割任务上，使用元数据（模态类型、扫描参数）替换支撑掩码，对比PSP基线、MetaCLIP-CMR线和联合方法在Dice和HD95上的表现。
- 主要风险：元数据的丰富程度影响对齐质量；若元数据描述与形状关联弱（如不同生产商的扫描参数），可能引入噪声

#### 路线 2：检测引导的编码器-only细胞级与器官级联合分割
- 核心想法：结合CellDETR的检测引导表示学习和EoSeg的纯编码器分割框架，提出一个无需解码器的多尺度联合分割模型，先通过检测提取细胞级嵌入，再通过查询机制聚合为器官级分割。
- 新问题定义：定义多粒度医学图像分割问题：输入全视野图像，同时输出细胞级检测框和器官级分割掩码，所有任务共享一个纯编码器ViT骨干，通过多级查询建模实现不同粒度的输出。
- 机制来源：
  - EoSeg（2607.00223v1）提供多级查询建模和可学习块融合，利用ViT不同层级特征图通过交叉注意力提取分割查询
  - CellDETR（2606.29463v1）提供位置特征解耦和框约束注意力，利用Deformable DETR进行细胞级检测和表示学习
- 为什么值得做：EoSeg证明ViT骨干下可摒弃U-Net解码器，但缺乏局部细节；CellDETR擅长细胞级检测但依赖DETR解码器。两者结合可实现从细胞到器官的端到端分割，共享编码器降低计算量。
- 理论/数学创新理由：
  - 数学对象：共享查询的多任务联合优化目标，包含分割损失和检测损失
  - 来源分解：EoSeg使用类别级查询进行分割；CellDETR使用可变形注意力进行细胞检测
  - 新建模方式：设计两组查询：器官级查询Q_seg（类别数）和细胞级查询Q_cell（可学习，数量等于最大细胞数）。两者共享ViT编码器特征。器官级通过多级查询建模得到分割图；细胞级通过可变形注意力得到检测框和嵌入。联合损失L = L_seg + L_det + λ * L_consist，其中L_consist约束细胞嵌入与器官掩码的区域一致性
  - 公式草图：设ViT输出特征图{F_l}。器官查询Q_seg与{F_l}交叉注意力得S = MLP(Z_seg)，其中Z_seg = CrossAttn(Q_seg, F_l)。细胞查询Q_cell通过可变形注意力采样点特征得Z_cell = DeformAttn(Q_cell, F_l)。检测头输出框b和类别c。一致性损失：L_consist = -log sim(Z_cell[in], S[b])，其中in表示框b落入器官区域
  - 为什么可能有效：共享编码器使细胞和器官特征相互增强；器官级分割为细胞检测提供上下文约束，细胞级检测为分割提供精确边缘信息，双向促进
- 可验证实验：在PanNuke数据集（细胞核分割+类型标注）上构建细胞级检测和器官级（组织类型）分割任务，对比CellDETR+U-Net、EoSeg+检测头和联合模型的多任务性能。
- 主要风险：细胞查询数量需预设，可能不适用于细胞密度变化大的场景；联合训练需平衡任务权重

## 方向 3：医学报告生成与检索中的结构化知识融合
本方向利用层次分类法、解剖区域、元报告模板等结构化知识，结合扩散模型的交互式生成能力，提升医学报告生成的层次一致性、长尾覆盖率和编辑灵活性。

### 代表论文

- [Prior-Anchored Debiasing for Long-Tailed Multi-Organ Pathology Report Generation](https://arxiv.org/abs/2607.00499v2)：提出Prior-Anchored Debiasing框架，通过视觉原型锚定瓶颈和元报告锚定库缓解长尾视觉和文本偏差，实现多器官病理报告生成。
- [Spatio-Temporal and Clinical Conditioning for Fine-Grained Radiology Report Retrieval](https://arxiv.org/abs/2607.02024v1)：提出STAR3框架，通过解剖区域检测、纵向时间建模和临床指示条件化，实现细粒度放射学报告检索，在MIMIC-CXR上超越现有检索方法。
- [Discrete Diffusion Language Models for Interactive Radiology Report Drafting](https://arxiv.org/abs/2607.01436v1)：本文系统比较了扩散语言模型（DiffusionGemma-26B）与自回归语言模型（Gemma-4-26B）在医学视觉问答和放射报告起草中的性能，发现扩散模型在同等规模下匹配或超越自回归性能，解码速度快3.5-4.4倍，并提供自回归模型不具备的任意顺序填充能力，适合交互式报告起草。
- [TaxoMIL: Taxonomy-Constrained Learning for Hierarchical Whole Slide Image Analysis](https://arxiv.org/abs/2606.31100v1)：提出TaxoMIL，一个受临床分类法约束的框架，将全切片图像分析重新表述为多粒度文本生成任务，通过双头Transformer解码器和分类法引导的目标实现层次一致的诊断预测。

### 共同创新点
- 将报告生成建模为结构化预测（区域级、层次标签、元模板）而非自由文本
- 利用临床先验（分类法、解剖位置、历史报告）减少数据稀疏影响
- 探索离散扩散模型的双向去噪能力实现交互式报告起草

### 尚未解决的问题
- 结构化知识（分类法、区域）与生成模型（扩散、自回归）的深度融合机制不明确
- 现有方法分别处理检索、生成和约束，未形成统一的可交互报告系统
- 长尾分布的器官或病变缺乏足够的结构化先验

### 二次创新路线
#### 路线 1：分类法约束的扩散模型用于交互式层次报告起草
- 核心想法：将TaxoMIL的分类法引导标签嵌入与DiffusionGemma的任意顺序填充能力结合，构建一个可在粗到细层次上双向编辑的报告起草系统，允许医生先在粗粒度层级修改，再自动细化。
- 新问题定义：定义层次交互式报告生成问题：给定WSI图像和初始粗粒度诊断（如器官级），用户可交互修改任一层次节点，扩散模型在保持下层与上层一致的前提下双向更新其他相关节点，最终输出完整层次化报告。
- 机制来源：
  - TaxoMIL（2606.31100v1）提供分类法引导的双头解码器和层次对比损失，保证粗-细标签的层次一致性
  - DiffusionGemma（2607.01436v1）提供离散扩散语言模型和任意顺序填充机制，在固定部分上下文后双向去噪生成剩余部分
- 为什么值得做：TaxoMIL提供层次约束确保诊断一致性；DiffusionGemma支持双向填充，两者结合可实现层次化的交互式编辑，即医生修改父类后，模型自动调整子类描述。
- 理论/数学创新理由：
  - 数学对象：层次约束的扩散采样目标，包含层次对比损失和双向去噪交叉熵
  - 来源分解：TaxoMIL使用层次对比损失约束标签嵌入空间；DiffusionGemma使用uniform-state扩散目标进行双向生成
  - 新建模方式：定义扩散过程：采样噪声n，模型预测原始token。加入层次约束：对属于同一父类的子类token，强制其去噪概率分布接近（KL散度正则）。交互编辑时，固定用户修改的token x_F，对空闲位置x_U进行条件采样：p(x_U|x_F) ∝ p(x_U|x_F) * exp(-λ * L_hier(x_F, x_U))，其中L_hier为层次一致性损失
  - 公式草图：设层次树T，节点v有祖先a(v)和后代d(v)。扩散模型参数θ，目标分布p_θ(x_0|x_T)。训练损失：L = -E[log p_θ(x_0)] + γ * ∑_v KL(p_θ(x_v|x_T) || p_θ(x_a(v)|x_T))。推理时固定部分x_F，对空闲部分进行step-wise去噪，每步施加层次约束
  - 为什么可能有效：层次约束确保生成文本在不同粒度间一致；扩散模型的双向性允许局部编辑后全局调整，符合医生修改报告的习惯
- 可验证实验：在TaxoMIL的WSI数据集（如TCGA）上构建交互式报告起草场景：模拟医生修改粗粒度诊断，评估自动生成子类描述的准确率和层次一致性（父-子类标签矛盾率）。
- 主要风险：扩散模型需要预设去噪步数，交互式编辑可能带来延迟；层次约束可能限制生成多样性

#### 路线 2：时空区域检索与元报告模板融合的层次化报告生成
- 核心想法：整合STAR3的区域级时空检索和PriOrGen的元报告锚定库，先通过STAR3检索前后片对应区域的句子，再利用PriOrGen的元报告模板作为检索后融合的模板，实现长尾感知的时序报告生成。
- 新问题定义：定义长尾时序医学报告生成问题：给定当前和先前的多器官WSI图像，通过区域级时空检索获取候选句子，利用元报告模板加权融合，输出覆盖头部和尾部器官的时序一致性报告。
- 机制来源：
  - STAR3（2607.02024v1）提供区域级时间建模（MHA）和临床条件模块，通过多任务解剖dropout选择报告相关区域并检索句子
  - PriOrGen（2607.00499v2）提供视觉原型锚定瓶颈（VPAB）压缩冗余补丁，以及元报告锚定库（MRAB）提供器官特定文本先验
- 为什么值得做：STAR3擅长利用纵向信息检索区域级句子，但受限于固定检索库；PriOrGen的元报告模板覆盖长尾器官，但未利用时间信息。两者结合可同时考虑时序动态和长尾分布。
- 理论/数学创新理由：
  - 数学对象：加权的检索-模板融合目标，包含时序一致性正则和长尾重加权
  - 来源分解：STAR3使用时序注意力融合前后片区域特征并检索句子；PriOrGen使用元报告模板嵌入作为先验
  - 新建模方式：对每个区域k，STAR3输出检索句子s_k^ret和置信度c_k。同时从MRAB中检索对应器官的元报告模板s_k^meta。融合句子：s_k = α_k * s_k^ret + (1-α_k) * s_k^meta，其中α_k = c_k / (c_k + β)，β为常数。长尾权重w_k = 1/(freq(organ_k)+1)。整体损失：L = ∑_k w_k * (L_cross_entropy(s_k, gt_k) + λ * L_consist(s_k, s_k_prev))，其中L_consist为当前句与前后片句子的语义一致性正则
  - 公式草图：令o_k为器官k。从MRAB取模板嵌入e_meta(o_k)，从STAR3取检索嵌入e_ret(k)。融合嵌入e_k = w_k * e_ret(k) + (1-w_k) * e_meta(o_k)，其中w_k = σ(MLP([e_ret; e_meta]))。解码器生成句子y_k = Dec(e_k)。时序一致性：L_temp = ||e_k - e_k_prev||^2
  - 为什么可能有效：对于高频器官，检索句子更可靠；对于低频器官，模板先验弥补数据不足。时序正则确保报告随时间连续，符合临床记录习惯
- 可验证实验：在MIMIC-CXR（带时间戳的胸片报告）上模拟长尾分布（只保留少数器官类别），对比STAR3、PriOrGen和联合方法的BLEU、ROUGE和长尾器官的F1。
- 主要风险：检索置信度与模板权重的融合策略需要调参；模板可能过于模板化导致多样性下降

## 方向 4：视觉语言模型的效率与自适应推理
本方向关注如何在不重新训练模型的前提下，通过动态调整推理时的计算资源（视觉token数量、检索预算、上下文长度、测试时计算）来平衡效率与性能，适应不同难度和资源约束。

### 代表论文

- [On Test-Time Scaling for Vision-Language Models](https://arxiv.org/abs/2606.28864v1)：首次全面研究LVLM的测试时缩放方法，发现小模型受益最大（性能提升30%），视觉信息仅在推理早期起关键作用。
- [Fast Enough to Act: Spatio-Temporal Visual Token Merging for Low-Latency Robotic VLMs and VLAs](https://arxiv.org/abs/2606.29350v1)：提出ST-Merge框架，在视觉编码阶段通过3D时空坐标的多队列并行匹配和加权聚合合并冗余视觉Token，并引入合并后位置校正机制，实现低延迟机器人VLM/VLA推理加速。
- [AB-RAG: Adaptive Budgeted Retrieval-Augmented Generation for Reliable Question Answering](https://arxiv.org/abs/2606.29090v1)：提出AB-RAG，一种无需训练、与骨干模型无关的自适应预算检索增强生成框架，通过结合模型确定性、答案与证据一致性及检索分数方差三个信号估计置信度，并决定是否继续检索，以在固定预算下平衡计算与准确性。
- [StochasT: Learning with Stochastic Turn Depth for Visual Instruction Tuning](https://arxiv.org/abs/2607.00465v1)：提出StochasT方法，通过随机裁剪多轮对话的历史上下文来训练LVLM，实现单轮和多轮场景下的鲁棒性能，并引入基于平衡拉丁方的评估机制。

### 共同创新点
- 利用轻量级信号（置信度、相似度、随机深度）指导自适应决策
- 在推理阶段而非训练阶段进行资源动态分配，保持模型通用性
- 从多个维度（token、检索、上下文、计算步数）探索自适应机制

### 尚未解决的问题
- 现有自适应策略各自独立，未形成统一的资源调度框架
- 缺乏跨任务、跨模型的自适应迁移能力
- 在保证性能的同时，自适应引入的额外决策开销可能抵消收益

### 二次创新路线
#### 路线 1：置信度驱动的视觉token合并与检索预算联合调度
- 核心想法：将AB-RAG的置信度估计和自适应检索决策与ST-Merge的视觉token合并结合，在推理早期根据置信度决定是否需要更多检索和更精细的视觉token，实现端到端的计算资源调度。
- 新问题定义：定义联合自适应计算问题：给定视觉问题和一个总计算预算（如总FLOPs或延时），模型自动决定视觉token合并率（保留比例）和检索深度（检索段落数），使得在预算内最大化答案准确性。
- 机制来源：
  - ST-Merge（2606.29350v1）提供3D时空坐标的多队列并行匹配和加权聚合，在视觉编码阶段合并冗余token，减少送入LLM的token数
  - AB-RAG（2606.29090v1）提供多信号置信度估计（模型确定性、检索分数方差等）和自适应检索决策循环，决定是否增加检索量
- 为什么值得做：AB-RAG擅长通过多信号估计答案置信度，但未利用视觉token效率优化；ST-Merge通过合并冗余token减少LLM输入量，但未考虑任务难度。两者结合可根据问题难度动态决定视觉细节程度和检索深度，避免在简单问题上浪费计算。
- 理论/数学创新理由：
  - 数学对象：预算约束下的联合优化问题，目标为最大化期望置信度
  - 来源分解：ST-Merge控制视觉token数量T_vis；AB-RAG控制检索段落数K。两者通过置信度信号联合决策
  - 新建模方式：定义状态s = (T_vis, K, c_conf)，其中c_conf为当前置信度。动作a = (ΔT_vis, ΔK)表示调整token合并度和检索深度。奖励r = accuracy(s) - α * cost(T_vis, K)。使用轻量级代理模型（如线性回归）学习最优策略π(a|s)。决策循环：初始T_vis=所有token，K=1；计算c_conf，若c_conf < τ且预算未耗，则选择(T_vis减半, K加1)等动作
  - 公式草图：定义置信度c = σ(MLP([d_model, e_cons, v_ret]))，其中d_model为模型输出token概率均值，e_cons为答案-证据一致性，v_ret为检索分数方差。动作空间：a ∈ {增加K, 减少T_vis, 不调整}。收益函数：J = E[∑ γ^t (acc_t - λ * (T_vis/ T_max + K/ K_max))]
  - 为什么可能有效：简单问题通常高置信度，可减少token和检索量加速；复杂问题低置信度时，增加视觉细节和外部知识可弥补。联合调度比独立优化更高效，避免重复计算
- 可验证实验：在VQA-v2和OK-VQA上模拟固定预算场景（如总FLOPs上限），对比ST-Merge、AB-RAG、联合方法的准确率和计算节约比例。
- 主要风险：决策循环本身可能引入延迟，需轻量级代理确保额外成本可控；置信度阈值和动作空间需跨数据集验证

#### 路线 2：测试时缩放与随机上下文深度的鲁棒性增强
- 核心想法：将StochasT的随机上下文深度的训练策略与测试时缩放（如Self-Consistency）结合，使模型在训练时接触多样化上下文长度，推理时利用自一致性投票获得更鲁棒的答案，特别是对于上下文依赖敏感的任务。
- 新问题定义：定义上下文鲁棒的多模态问答问题：模型在训练时通过随机上下文深度学习，推理时使用测试时自一致性采样，要求在任意上下文长度（包括单轮和多轮）下都能输出稳定准确的答案。
- 机制来源：
  - StochasT（2607.00465v1）提供随机轮次深度训练，通过采样父节点构建对话树，使模型适应不同历史长度
  - 测试时缩放（2606.28864v1）提供Self-Consistency方法，通过多次采样和多数投票提升答案稳定性
- 为什么值得做：StochasT解决多轮训练与单轮评估的差距，但推理时仍需面对不同上下文；测试时缩放中的Self-Consistency通过多次采样提高稳定性。两者结合可训练模型对上下文长度鲁棒，并在推理时通过多次采样进一步消除随机性。
- 理论/数学创新理由：
  - 数学对象：随机上下文训练与多次采样投票的期望风险最小化
  - 来源分解：StochasT在训练时随机化上下文长度；Self-Consistency在推理时多次采样
  - 新建模方式：训练时，对每个图像的多轮对话，以概率p∈[0,1]选择随机父节点（从根或前序轮次），构建注意力掩码，训练模型最大化条件概率。推理时，对输入（图像+上下文），采样b次得到答案集{y_i}，通过多数投票得到最终答案。目标：min E[1 - max_j freq(y_j)/b]
  - 公式草图：训练损失：L = -∑_{n=1}^N log p(y_n | X, y_{<n}, context_tree)，其中context_tree由StochasT采样父节点决定。推理时：对于输入x，采样b次得到{y_i}，计算众数y* = argmax count(y_i)，输出y*。若需置信度，可用count(y*)/b作为估计
  - 为什么可能有效：StochasT使模型在训练时见过各种上下文，不会过拟合特定长度；Self-Consistency在推理时通过多次采样平滑概率分布，两者结合让模型在任意上下文长度下都能稳定输出，特别适应对话式医疗问诊等场景
- 可验证实验：在医疗对话VQA数据集（如MedVQA）上构造多轮版本，比较基线、StochasT、StochasT+Self-Consistency的准确率和置信度校准曲线。
- 主要风险：Self-Consistency增加推理计算量b倍，需权衡；StochasT的超参数αβ需调整以避免模式崩溃
