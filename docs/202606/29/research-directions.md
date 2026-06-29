# 研究方向与二次创新路线 · 2026-06-29

- 生成时间：2026-06-29 22:18:16 UTC
- 当日论文数：27
- 方向数：4

## 生成提示

全量研究方向生成返回不可解析 JSON，已使用分批生成兜底。

## 质量门控提示

- batch 2 returned unparsable or schema-invalid JSON
- batch 3 returned unparsable or schema-invalid JSON

## 今日方向总览

| 方向 | 论文数 | 代表论文 |
|---|---:|---|
| 医疗与生物领域鲁棒视觉语言模型的评估与自适应防御 | 3 | Aloe-Vision: Robust Vision-Language Models for Healthcare<br>Benchmarking Vision-Language Models for Microscopic Plant Image Understanding<br>T-VSS: Test-Time Visual Subspace Steering for Adversarial Robustness of Vision-Language Models |
| 基于因果反事实推理与联合稀疏编码的弱监督病理图像分割 | 2 | C2RM-Seg: Causal Counterfactual Reasoning with Structural-Semantic Priors for Weakly Supervised Histopathological Tissue Segmentation<br>Steering Vision-Language Models with Joint Sparse Autoencoders |
| 视觉同质文档与4D动态场景的稠密检索与跟踪 | 2 | 4DVLT: Dynamic Scene Understanding with Worldline-Centered Vision-Language Tracking<br>Invoice Haystack: Benchmarking Document Retrieval and Visual Question Answering Under Strong Visual Homogeneity |
| 结构化视觉推理的几何感知与不确定性建模 | 3 | OmniSpace: Efficient Geometry Awareness for Autonomous Vehicles MLLMs<br>Modular Diffusion Models for Structured Visual Recognition<br>VISTA Architect: A graph database-oriented health AI system demonstrated in multidisciplinary tumor boards |

## 方向 1：医疗与生物领域鲁棒视觉语言模型的评估与自适应防御
现有医疗和生物显微领域的视觉语言模型面临数据稀缺、评估基准有限和对对抗扰动脆弱等共同挑战。Aloe-Vision构建了融合医疗与通用数据的大规模训练集和CareQA-Vision鲁棒评估基准，揭示了对对抗输入的脆弱性；PlantMicro提出了微观植物图像理解基准，发现细粒度识别和生物学推理能力差；T-VSS提出了测试时视觉子空间引导防御，直接修正被攻击的视觉特征。三者互补可形成鲁棒VLM的评估-防御闭环。

### 代表论文

- [Aloe-Vision: Robust Vision-Language Models for Healthcare](https://arxiv.org/abs/2606.27500v1)：针对医疗领域视觉-语言模型数据稀缺、鲁棒性不足和评估基准受限的问题，提出Aloe-Vision模型和Aloe-Vision-Data数据集，融合医疗与通用多模态数据，训练7B和72B参数模型，在多个基准上取得优异性能。同时提出CareQA-Vision基准用于可靠评估，并揭示模型在对抗性输入下的脆弱性。
- [Benchmarking Vision-Language Models for Microscopic Plant Image Understanding](https://arxiv.org/abs/2606.22497v1)：提出PlantMicro基准，包含超过5,000张显微镜图像和9,000多个VQA对，系统评估视觉语言模型在微观植物图像理解上的能力。
- [T-VSS: Test-Time Visual Subspace Steering for Adversarial Robustness of Vision-Language Models](https://arxiv.org/abs/2606.23132v1)：提出测试时视觉子空间引导（T-VSS）方法，通过构建样本特定的低秩子空间并在其中学习共享特征修正，直接调整被攻击的视觉特征，实现高效轻量的测试时自适应防御。

### 共同创新点
- 识别出医疗/生物VLM在对抗扰动和细粒度场景下的脆弱性
- 提供了领域特定的评估数据集和任务（Aloe-Vision的CareQA-Vision和PlantMicro的9K VQA对）
- 提出了轻量级测试时自适应机制（T-VSS）可直接在特征空间修复扰动

### 尚未解决的问题
- 缺乏统一的对抗鲁棒性评估协议，医疗和生物基准任务差异大
- 现有防御方法（如T-VSS）未在医疗VLM上验证，且依赖多视图增强的局部结构
- 植物显微场景下的细粒度对抗样本生成尚未研究

### 二次创新路线
#### 路线 1：跨领域鲁棒性迁移的测试时自适应方法
- 核心想法：将T-VSS的低秩子空间修正方法扩展至医疗和生物领域，并引入PlantMicro基准中发现的失败模式（如细胞器识别错误）作为先验，构建领域感知的子空间修正向量。
- 新问题定义：定义新任务：跨领域（医疗CT、显微植物）VLM的测试时对抗鲁棒性评估与自适应防御，要求模型在面对未知对抗扰动时通过少量领域内多视图残差进行特征修正。
- 机制来源：
  - Aloe-Vision揭示了医疗VLM在对抗输入下的脆弱性，并提供CareQA-Vision基准和Aloe-Vision-Data数据集，用于下游测试时自适应评估。
  - T-VSS提供了在视觉特征空间构建低秩子空间并学习共享修正向量的方法，通过SVD分解多视图特征残差，在子空间内优化熵损失。
  - PlantMicro提供了微观植物图像VQA任务，其细粒度识别（如病原类型、细胞器）的失败可指导T-VSS的可靠权重设计，避免不可靠视图破坏修正方向。
- 为什么值得做：T-VSS在通用数据集上有效，医疗领域有Aloe-Vision的扰动评估基线，PlantMicro提供了细粒度任务，三者结合可验证迁移性并提升弱场景下的鲁棒性。
- 理论/数学创新理由：
  - 数学对象：测试时特征修正的低秩子空间投影与最优化目标（可靠性加权的熵最小化）
  - 来源分解：Aloe-Vision评估了对抗扰动下VLM的预测退化，但未提出修正机制；T-VSS通过SVD分解R∈R^{V×d}得到子空间基U，并学习α∈R^m最小化熵损失H_l(·)；PlantMicro揭示了细粒度特征的脆弱性，与T-VSS的可靠性加权（基于局部邻域一致性）可结合得到关注细粒度的权重。
  - 新建模方式：将T-VSS的修正向量Δf=Uα优化为：α* = argmin_α Σ_v ω_v · H_l(f_v + Uα)，其中ω_v = exp(-λ·d(f_v, N(f_v))) 衡量视图v的细粒度一致性，d由PlantMicro中细粒度分类器在邻域上的方差度量。
  - 公式草图：设f_v为第v个视图的特征，N(f_v)为其最近邻集合，细粒度不适配度δ_v = Var({c(f_i) | f_i in N(f_v)})，其中c(·)为细粒度分类器输出。权重ω_v = exp(-λ δ_v)。最终修正优化：min_{α} Σ_v ω_v · (-log softmax(ŷ_v + W^T Uα)_c)，其中ŷ_v为对抗特征logit，W为分类权重。
  - 为什么可能有效：通过引入细粒度一致性权重，避免不可靠视图（如细胞器被错误识别）污染修正方向，使子空间修正向量更关注细粒度判别特征，从而提升在医疗和生物领域精细任务上的防御效果。
- 可验证实验：在Aloe-Vision的CareQA-Vision基准（医疗图像）和PlantMicro基准（微观植物图像）上，使用PGD和AutoAttack生成对抗样本，比较标准T-VSS与提出方法的防御后准确率。
- 主要风险：多视图增强在医疗图像（如MRI）上可能产生临床无关视图，导致残差矩阵结构性差；细粒度分类器在未见类别上表现不稳定。

## 方向 2：基于因果反事实推理与联合稀疏编码的弱监督病理图像分割
弱监督组织病理分割面临伪标签噪声问题，C2RM-Seg通过因果反事实推理去除染色等混淆因素，并融合结构-语义双路径分割；JSAE通过联合稀疏自编码器学习可解释的跨模态特征并实现双向干预。两者结合可进一步利用JSAE的稀疏特征引导分解因果因子，实现更准确的去偏。

### 代表论文

- [C2RM-Seg: Causal Counterfactual Reasoning with Structural-Semantic Priors for Weakly Supervised Histopathological Tissue Segmentation](https://arxiv.org/abs/2606.25508v1)：提出C2RM-Seg，通过因果反事实推理生成形态对齐的CAM伪标签，并融合ResNeSt结构特征与DINOV3语义先验的双路径分割架构，辅以不确定性门控边缘损失，实现弱监督组织病理组织分割的SOTA性能。
- [Steering Vision-Language Models with Joint Sparse Autoencoders](https://arxiv.org/abs/2606.25657v1)：提出联合稀疏自编码器（JSAE），通过显式对齐约束联合分解视觉和语言激活，得到可解释、可控的跨模态特征，用于引导视觉语言模型行为。

### 共同创新点
- 均采用特征分解策略（C2RM的因果因子分解和JSAE的稀疏潜在分解）
- 均涉及对特征的可控干预（C2RM的因果反事实减法，JSAE的加性引导与抑制）
- 均使用额外先验（C2RM使用DINOV3语义，JSAE使用文本辅助）

### 尚未解决的问题
- C2RM的因果结构矩阵假设为线性，不足以建模复杂病理特征交互
- JSAE操作在序列池化表示上，缺乏像素级或token级引导能力
- 两者均未在弱监督病理任务上联合应用

### 二次创新路线
#### 路线 1：联合稀疏因果因子分解的弱监督分割
- 核心想法：用JSAE的联合稀疏编码框架替代C2RM中简单的线性因果结构矩阵，通过显式对齐视觉和文本（如病理报告）的稀疏潜在表示，学习更有意义的因果因子，并利用文本侧的稀疏特征作为因果干预方向，提升去偏效果。
- 新问题定义：新任务：弱监督组织病理图像分割中的联合稀疏因果因子学习与反事实干预，使用图像-文本对（组织切片+诊断报告）训练JSAE，提取的稀疏因子作为因果变量，进行反事实干预生成去偏CAM伪标签。
- 机制来源：
  - C2RM-Seg提出了因果反事实推理模块（C2RM），通过结构因果矩阵A将特征分解为K个潜在因子，并去除混淆贡献生成反事实特征Z^cf，用于CAM去偏。但A为线性，且缺乏外部语义先验。
  - JSAE使用联合稀疏自编码器学习图像和文本的稀疏潜在表示，通过对齐约束（余弦相似度）使两者共享相同的稀疏维度，并可从文本解码器列提取跨模态引导方向。该机制可提供语义先验。
- 为什么值得做：JSAE通过文本引导获得语义丰富的跨模态特征，可辅助病理分割中染色与形态的分解，且稀疏表示天然适合因果因子发现。C2RM已证明因果去偏的有效性，结合后有望进一步提升伪标签质量。
- 理论/数学创新理由：
  - 数学对象：联合稀疏因果因子分解：优化稀疏性、重建性、对齐性和因果去偏的联合目标
  - 来源分解：C2RM的特征分解是硬分配给K个线性因子，缺乏稀疏性约束；JSAE的稀疏编码是过完备的（维度>特征维度），但未显式建模因果结构。二者互补：以JSAE的稀疏编码为隐空间，在其上叠加因果结构矩阵实现因子化。
  - 新建模方式：联合优化目标：L = L_recon + λ1 L_sparse + λ2 L_align + λ3 L_causal。其中L_recon为模态重建，L_sparse为L1正则，L_align为模态间余弦相似度，L_causal为反事实特征与原始特征的差异最小化（鼓励去偏）。在隐空间中，因果结构矩阵A施加于稀疏代码z_v和z_t，反事实代码z_v^cf = z_v - A z_v。
  - 公式草图：设图像编码器E_v，文本编码器E_t，输出全局特征h_v, h_t；JSAE编码器得到稀疏代码z_v = ReLU(W_enc_v h_v), z_t = ReLU(W_enc_t h_t)。因果结构矩阵A∈R^{d×d}（d为隐层维度），行softmax约束。反事实特征ĥ_v = Dec_v(z_v - A z_v)。分类损失使用ĥ_v生成CAM。联合损失：L = MSE(ĥ_v, h_v) + λ1 * (||z_v||_1 + ||z_t||_1) + λ2 * (1 - cos(z_v, z_t)) + λ3 * ||ĥ_v - h_v||_2^2。
  - 为什么可能有效：稀疏性迫使编码器选择少数因果因子，对齐项利用文本先验引导视觉因子与语义概念对应（如“染色”对应文字“hematoxylin”），因果结构矩阵则去除因子间的混淆路径，使反事实特征更专注于形态本身，从而生成更准确的伪标签。
- 可验证实验：在C2RM-Seg使用的GlaS和ColonHist数据集上，将JSAE预训练于配对的组织病理图像-报告数据（如来自TCGA），替换C2RM的原始分类器，比较伪标签质量（mIoU）和最终分割性能。
- 主要风险：需要大量可用的图像-文本对，病理报告非结构化；JSAE在序列池化层次，无法直接提供像素级引导，可能需要额外上采样；稀疏维度选择敏感。

## 方向 3：视觉同质文档与4D动态场景的稠密检索与跟踪
视觉高度同质文档检索面临嵌入坍缩问题，4D动态场景跟踪面临多视图、时间一致性和指令推理挑战。Invoice Haystack通过双流融合和VLM过滤缓解坍缩，4DVLT通过对象中心4D状态图和世界线解码实现精确跟踪。两者机制互补：4DVLT的图推理和路由机制可推广到文档检索中做结构化筛选，Invoice Haystack的VLM验证可增强4D跟踪的语义确认。

### 代表论文

- [4DVLT: Dynamic Scene Understanding with Worldline-Centered Vision-Language Tracking](https://arxiv.org/abs/2606.22631v1)：提出4DVLT任务和Instruct-4D基准，并设计4DTrack方法通过图条件世界线推理实现指令条件下的4D动态场景理解，在基准上超越最强基线19.62个点。
- [Invoice Haystack: Benchmarking Document Retrieval and Visual Question Answering Under Strong Visual Homogeneity](https://arxiv.org/abs/2606.25343v1)：提出Invoice Haystack基准和VL-RAG框架，通过融合文本与视觉嵌入并进行VLM验证过滤，解决视觉高度同质文档检索中的嵌入坍缩问题。

### 共同创新点
- 均处理视觉-语言检索/跟踪中的歧义性问题（文档嵌入坍缩，跟踪目标混淆）
- 均采用多源信息融合（Invoice Haystack:文本+视觉+VLM；4DVLT:外观+几何+运动学）
- 均包含一个验证或过滤步骤（VLM filter vs 物理校准统一输出）

### 尚未解决的问题
- Invoice Haystack的VLM验证增加推理成本，且只用于检索后过滤
- 4DVLT的前端检测质量有限，在严重遮挡下候选缺失
- 两者均未探索在线/增量设置

### 二次创新路线
#### 路线 1：基于世界线图推理的视觉同质文档检索
- 核心想法：将4DVLT中的对象中心4D状态图和路由收缩思想应用于文档检索：将文档集合中的每张发票视为一个状态，通过时间或序列顺序（如发票处理流程）构建状态转移图，利用查询条件进行度量引导路由选择子图，提升对同质文档的区分能力。
- 新问题定义：新任务：文档流检索，给定一组按时间或逻辑顺序排列的视觉同质文档（如发票流水线），通过自然语言查询检索目标文档，并输出其完整时间上下文（如前后文档）。要求利用状态图进行非时序推理。
- 机制来源：
  - Invoice Haystack揭示了视觉同质文档集（平均余弦相似度0.73）导致的嵌入坍缩，并提出融合文本+视觉+VLM验证的VL-RAG框架。其分数融合仅基于平均，缺乏结构上下文。
  - 4DVLT提出了对象中心4D状态图，将每个候选对象的状态（位置、外观、可见性）作为节点，时间转移为边，并通过度量引导路由（公式：ℓ_l,u = r_l,u + α*s_a_text_i + α_m*(-||δ_l,u||^2)等）收缩候选空间，再通过双向解码和物理校准输出一致性轨迹。
- 为什么值得做：Invoice Haystack表明同质文档嵌入坍缩难以通过单一嵌入区分，而4DVLT的图结构通过引入拓扑关系和物理约束增加了区分维度，可突破余弦相似度的局限。
- 理论/数学创新理由：
  - 数学对象：文档状态图上的路由logit和双向序列解码的联合优化
  - 来源分解：Invoice Haystack的检索仅依赖点状相似度，未建模文档间的相关结构（如同一发票的多个版本）；4DVLT的路由函数结合了全局语义相关性和度量偏移，但针对3D空间，不适用于文档。可借鉴其形式，将文档的OCR文本嵌入和视觉布局嵌入作为状态特征，文档间的顺序或引用关系作为边。
  - 新建模方式：定义文档状态图G=(V,E)，每个节点v有特征向量g_v（融合文本、视觉和布局）。对查询q，路由logit ℓ_v = r(q, g_v) + α·s_sem(q, v) + β·c_loc(v, N(v))，其中r为潜在查询与节点的相关性，s_sem为全局语义匹配，c_loc为局部邻域一致性（如与前后文档的字段连续性）。然后通过双向序列解码：p(W) = ∏_{t=1}^T p(w_t | w_{<t}, G, q)和反向，最终通过物理式约束（如发票金额总和匹配）选择最佳路径。
  - 公式草图：路由保留概率：π_v = softmax(ℓ_v) over V。构造子图Ĝ = {v ∈ V | π_v > τ} ∪ edges。双向解码：前向概率p_f(w_t | history) = softmax(MLP([h_t, e_t]))，后向p_b类似。最终路径得分：s_path = Σ_t log p_f(w_t) + Σ_t log p_b(w_t) + γ·E_physical(W)，其中E_physical为物理一致性（如金额误差的负对数）。
  - 为什么可能有效：通过引入文档间结构（顺序、引用）和物理约束（如金额字段的连续性），强制检索结果不仅相似度高，而且与上下文一致的路径，这能有效打破嵌入空间的噪声坍缩，因为只有真正匹配的文档才会在局部邻域中保持一致的语义和物理关系。
- 可验证实验：在Invoice Haystack的1500张发票基础上，模拟发票流水线（如添加时间戳、前后文档引用），构建DocFlow检索任务。比较VL-RAG、4DTrack风格图检索以及提出方法的MRR和Recall@1。
- 主要风险：构建文档状态图需要额外元数据（时间、顺序），增加标注成本；在无天然顺序的场景（如发票集合）中，边定义可能主观。

## 方向 4：结构化视觉推理的几何感知与不确定性建模
针对复杂视觉场景中的结构化预测任务，本方向融合几何感知与不确定性建模，通过跨论文机制互补实现更鲁棒的空间推理。OmniSpace利用极线约束和3D蒸馏提升多视图对应，但输出为确定性点估计；MDMs通过模块化扩散模型建模输出分布，但缺乏几何先验；VISTA Architect提供持久化知识图谱和时序抽象，增强结构化信息的可追溯性。三者结合可形成训练时几何蒸馏、推理时扩散采样的框架，并借助图结构保证输出一致性。

### 代表论文

- [OmniSpace: Efficient Geometry Awareness for Autonomous Vehicles MLLMs](https://arxiv.org/abs/2606.22617v1)：提出OmniSpace框架，通过摄像头姿态注入、多视图极线注意力和3D几何蒸馏，仅从2D观测实现高效几何感知空间推理，无需辅助3D模型，在自动驾驶规划、风险检测等任务上超越现有方法。
- [Modular Diffusion Models for Structured Visual Recognition](https://arxiv.org/abs/2606.22702v1)：提出模块化扩散模型（MDMs），通过将结构化输出分解为多个条件扩散模型并利用DAG定义依赖关系，实现对异质输出空间的不确定性建模，在目标检测、实例分割和场景图生成任务中取得优势。
- [VISTA Architect: A graph database-oriented health AI system demonstrated in multidisciplinary tumor boards](https://arxiv.org/abs/2606.22692v1)：针对电子健康记录中患者历史重建的挑战，提出VISTA Architect，一种基于图的AI架构，通过两阶段预处理（MEDS图保留原始结构，TOA用LLM合成时间线）生成持久知识图谱。在斯坦福胸科肿瘤委员会1180名患者中，15个变量准确率达96.4%，智能体接口将准备时间降至2.2分钟，优于RAG基线，且模块化设计可适配其他专科。

### 共同创新点
- 均采用条件建模思路：OmniSpace以相机位姿为条件，MDMs以图像和部分输出为条件，VISTA以EHR记录为条件
- 均设计模块化解耦机制：OmniSpace分离位姿注入和注意力约束，MDMs分解联合分布为条件扩散，VISTA分离MEDS图和TOA层
- 均追求轻量推理：OmniSpace推理无额外3D模型，MDMs组件独立采样，VISTA无需重复处理原始记录

### 尚未解决的问题
- 几何感知与不确定性建模未结合：OmniSpace输出确定性，MDMs未利用几何约束，导致不确定区间的空间定位不精确
- 结构化输出验证缺失：MDMs生成内容可能违反几何或语义约束，VISTA的图结构可提供校验但对视觉任务适配不够
- 时序动态场景支持不足：OmniSpace仅处理单时刻多视图，MDMs未建模时间依赖，VISTA虽有时序但非视觉推理

### 二次创新路线
#### 路线 1：几何约束扩散：融合极线注意力的结构化输出生成
- 核心想法：将MDMs的扩散解码器中的交叉注意力替换为OmniSpace的多视图极线注意力，使去噪过程在几何约束下进行，提升物体框和掩码的一致性与精度。
- 新问题定义：基于多视图图像的联合目标检测与实例分割任务，要求输出与真实3D投影一致，且能表达边界和遮挡的不确定性。
- 机制来源：
  - OmniSpace的Camera Pose Injector提供每帧精确位姿编码，解决了MDMs缺乏全局几何先验的问题
  - OmniSpace的Multi-view Epipolar Attention将跨视图交互限制在极线上，补足MDMs全局注意力可能引入几何不一致的缺陷
  - MDMs的动态查询生成与时间调制机制补足OmniSpace输出为确定性点估计、无法表达多模态的不足
- 为什么值得做：极线注意力可强制跨视图特征在对应极线上交互，避免噪声特征扰动，而扩散过程的迭代细化能自然处理遮挡和模糊，互补性强。
- 理论/数学创新理由：
  - 数学对象：条件扩散模型的变分下界与极线约束的联合优化目标
  - 来源分解：OmniSpace优化3D几何蒸馏损失L_geo=VGGT特征与学生特征L2距离；MDMs优化扩散ELBO L_diff= E[||epsilon - epsilon_theta||^2]。两者独立优化，未交互。
  - 新建模方式：定义联合损失 L = L_diff + λ * L_geo_constrained，其中L_geo_constrained在MDMs的去噪解码器交叉注意力中引入极线掩码，使注意力权重仅作用于对应极线区域，从而在生成过程中隐式满足几何约束。
  - 公式草图：设查询点像素坐标p_i，极线方程为l_j = F_{ij} * p_i，其中F_{ij}为基础矩阵。注意力掩码M_{ij} = 1 if distance(p_j', l_j) < τ，否则0。则极线注意力输出: Attn(Q,K,V) = softmax(QK^T / sqrt(d) + log(M)) V。联合损失: L = E_{t,epsilon} [||epsilon - epsilon_theta(z_t, t, I, pose)||^2] + β * Σ_{i,j} MSE(student_feat(i,j), teacher_feat(i,j)) * M_{ij}，其中z_t为噪声查询，I为图像特征，pose为位姿。
  - 为什么可能有效：极线掩码强制注意力聚焦于几何对应的区域，减少噪声注意力带来的虚假检测，使扩散过程朝向全局一致的结构输出；几何蒸馏补充了场景级别的深度和形状先验，有助于区分遮挡边界和真实轮廓，从而提升不确定性建模的可靠性。
- 可验证实验：在nuScenes数据集上搭建极线注意力扩散模型，以环视6路相机为输入，预测车辆和行人3D框与2D掩码。对比基线：①OmniSpace+MLLM确定性输出；②MDMs原始全局注意力；③本文极线注意力扩散。评估指标：mAP、mIoU、以及校准误差（ECE）和负对数似然（NLL）。
- 主要风险：极线注意力依赖精确标定的相机位姿，若位姿有噪声或动态变化，掩码可能错误排除有效对应，导致召回下降。可引入位姿不确定性建模或软掩码缓解。

#### 路线 2：知识图谱引导的扩散结果结构化校验与纠错
- 核心想法：利用VISTA Architect的MEDS图存储实体关系，在MDMs生成后通过图推理检查输出是否符合语义和几何常识，对不一致的样本进行条件重采样或梯度修正。
- 新问题定义：场景图生成任务，要求输出不仅包含物体框和关系三元组，还要满足预定义的常识规则（如“人在车外”）、几何规则（如“物体不嵌入”）。
- 机制来源：
  - VISTA的MEDS图保留原始EHR的实体与关系，可泛化为视觉常识图谱；其TOA层提供时序一致性答案，类比于视觉时序场景的连贯性
  - MDMs的模块化设计使得部分输出（如关系）可被替换或重置，便于注入外部约束进行修正
  - OmniSpace的几何蒸馏提供3D位置先验，可辅助判断几何合理性
- 为什么值得做：MDMs独立采样可能输出违反常识的物体布局（如重叠、悬浮），VISTA的持久化知识图谱可提供本体约束，将扩散过程从无约束生成变为约束满足生成。
- 理论/数学创新理由：
  - 数学对象：约束优化中的投影梯度法或马尔科夫链蒙特卡洛，目标为在扩散似然约束下满足硬/软规则。
  - 来源分解：MDMs仅最大化数据似然p(x|I)，未考虑规则一致性；VISTA构建知识图谱后仅用于检索，不参与生成。
  - 新建模方式：定义规则集R，每个规则为布尔函数r(x)∈{0,1}。在采样时，每步去噪后对输出x_t进行投影：x_t' = argmin_{x} ||x - x_t||^2 subject to r(x)=1（硬约束）或添加正则项λ * penalty(r(x))（软约束）。对于非凸约束，可采用MCMC接受/拒绝：若r(x_t)=0，则以概率exp(-β*penalty)接受，否则拒绝并重采样。
  - 公式草图：设采样过程从t=T到0，每一步得到预测x0_t。定义规则惩罚P(x0_t)= Σ_k φ(r_k(x0_t))。若P>0，则通过梯度下降修正x0_t：x0_t' = x0_t - η ∇_x P(x0_t)。用修正后的x0_t'重新计算噪声预测：epsilon_t' = (z_t - sqrt(αt_bar) * x0_t') / sqrt(1-αt_bar)。继续后续去噪步骤。其中φ为指示函数或平滑函数，η为步长。
  - 为什么可能有效：将知识图谱中的规则转化为可微的惩罚项，在扩散过程中间步骤纠正输出，可以避免最终采样结果违反常识，同时保持生成速度（无需重跑整个链）；投影步骤可以视为在数据流形上寻找最近有效点，提高输出可解释性。
- 可验证实验：在Visual Genome数据集上，预定义物体位置不重叠（IoU<0.5）、支持关系（如“on”要求接触）等规则。实验组：MDMs+规则修正；对照组：原始MDMs、Top-down知识图谱引导解码。评估规则违反率（%）、场景图召回率（SGRecall）、以及生成多样性（Distinct）。
- 主要风险：规则设计可能过强或过弱，过强会降低多样性，过弱无法滤除错误；梯度修正可能将输出推向非流形区域。需调整惩罚权重与步长，或使用可学习的软规则。
