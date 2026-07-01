# 研究方向与二次创新路线 · 2026-07-01

- 生成时间：2026-07-01 22:23:00 UTC
- 当日论文数：36
- 方向数：5

## 生成提示

全量研究方向生成被质量门控过滤，已使用分批生成兜底。

## 质量门控提示

- batch 1 returned unparsable or schema-invalid JSON
- batch 2 returned unparsable or schema-invalid JSON
- batch 3 returned unparsable or schema-invalid JSON

## 今日方向总览

| 方向 | 论文数 | 代表论文 |
|---|---:|---|
| 机器人空间感知与多视图几何推理增强 | 3 | G$^3$VLA: Geometric inductive bias for Vision-Language-Action Models<br>Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics<br>TriViewBench: Controlled Complexity Scaling for Multi-View Structural Reasoning in MLLMs |
| 大视觉语言模型的自适应计算资源分配机制 | 3 | GeMoE: Gating Entropy is All You Need for Uncertainty-aware Adaptive Routing in MoE-based Large Vision-Language Models<br>Towards Fast and Effective Long Video Understanding of Multimodal Large Language Models via Adaptive Quasi-Gaussian Sampling<br>Toward Low-Latency Vision-Language Models with Doubly-Correct Predictions in Egocentric Visual Understanding |
| 面向医疗领域的高可靠RAG系统构建 | 2 | MedGuards: Multi-Agent System for Reliable Medical Error Detection and Correction<br>Reducing Redundancy in Whole-Slide Image Patching for Scalable Indexing and Retrieval |
| 多模态大模型效率优化与鲁棒性增强 | 2 | Spectral Evolution-Guided Token Pruning in Multimodal Large Language Models<br>Are We There Yet? Exploring the Capabilities of MLLMs in Assistive AI Applications |
| 几何先验注入与多任务分割 | 2 | Boosting Text-Driven Video Segmentation via Geometry-Aware Distillation<br>Intracranial Aneurysm Classification and Segmentation via Tri-Axial ROI and Multi-Task Learning |

## 方向 1：机器人空间感知与多视图几何推理增强
针对机器人操作和导航中空间理解不足的问题，结合几何偏置注入、语义建图和诊断性多视图基准，形成从感知到评估的闭环改进方向。

### 代表论文

- [G$^3$VLA: Geometric inductive bias for Vision-Language-Action Models](https://arxiv.org/abs/2606.24472v1)：针对VLA模型视觉标记缺乏几何信息的问题，提出G3VLA模块，通过内参射线嵌入、PRoPE和跨视图融合注入校准几何，无需额外传感器，在LIBERO、RoboCasa24等基准上显著提升空间和物体敏感任务性能。
- [Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics](https://arxiv.org/abs/2606.24814v1)：针对物流环境中机器人缺乏语义理解的问题，本文提出结合SLAM、SAM实例分割、聚类和VLM多视图推理的上下文语义建图流水线，零样本推断物体类别和可移动性，在语义分类和可移动性估计上分别达到98.93% mIoU和89.17% mAcc，并识别出主要瓶颈。
- [TriViewBench: Controlled Complexity Scaling for Multi-View Structural Reasoning in MLLMs](https://arxiv.org/abs/2606.26029v1)：提出TriViewBench，一个通过合成3D场景控制视觉复杂度的多视图结构推理基准，系统评估MLLMs在结构推理上的可扩展性瓶颈。

### 共同创新点
- G3VLA通过内参射线嵌入和PRoPE注入校准几何，解决VLA模型缺乏相机几何信息的问题
- 语义建图流水线融合SLAM几何与VLM语义，零样本推断物体可移动性
- TriViewBench显式分离局部决策、计数和全局恢复能力，揭示跨视图身份混淆失效机制

### 尚未解决的问题
- 现有几何注入与语义建图未有效融合，缺乏统一的几何-语义联合表示
- 多视图推理中的跨视图对应（身份混淆）缺乏显式解决机制
- 缺乏对静态场景操作和动态环境适应性的统一框架

### 二次创新路线
#### 路线 1：几何引导的跨视图语义对应与物体计数联合优化
- 核心想法：利用G3VLA的PRoPE提供跨视图位置对应线索，辅助语义建图的实例聚类，并直接修正TriViewBench中发现的过计数错误
- 新问题定义：在多视图机器人操作场景中，给定多张RGB图像及其相机内参和外参，要求模型同时输出每个视图中的物体实例分割、跨视图身份对应、全局物体计数以及每个物体的语义属性（类别、可移动性），实现几何-语义联合推理
- 机制来源：
  - G3VLA的PRoPE（投影位置编码）提供跨视图位置对应线索，解决了不同视图间同一物体如何关联的问题
  - 语义建图实例聚类利用多视图特征聚合形成物体实例，但缺乏几何约束导致身份混淆时可能错误合并或分裂
  - TriViewBench的跨视图身份混淆分析表明模型倾向于将同一物体在不同视角重复计数，几何线索可提供对应约束避免重复
- 为什么值得做：G3VLA已证明几何信息可提升空间敏感任务，语义建图依赖多视图一致性，TriViewBench精确量化了计数错误，三者联合有清晰的问题定义和互补机制
- 理论/数学创新理由：
  - 数学对象：跨视图几何对应损失与语义一致性联合优化目标
  - 来源分解：G3VLA的PRoPE提供了像素级几何对应映射（极线约束）；语义建图使用CLIP特征相似度进行实例关联；TriViewBench暴露了计数偏差，但未提供纠正方法
  - 新建模方式：联合最小化交叉熵计数损失、跨视图几何对应损失（基于PRoPE的对极距离）以及实例特征一致性损失，统一训练或后处理
  - 公式草图：L = L_count + λ1 * Σ_{(i,j)∈C} d_epipolar(PRoPE(p_i), PRoPE(p_j)) + λ2 * Σ_{(i,j)∈C} ||f_i - f_j||^2，其中C为跨视图对应集合，f为CLIP特征，d_epipolar为对极距离
  - 为什么可能有效：几何损失强制同一物体在不同视图的投影满足极线几何，抑制错误对应；特征一致性损失保留语义相似性；计数损失直接惩罚全局计数偏差，三者互补可同时改善定位、对应和计数精度
- 可验证实验：基于合成场景（如TriViewBench的1923个场景）构建几何-语义联合标注，比较基线（分别用G3VLA和语义建图）与联合模型在物体计数、实例分割mIoU和跨视图对应精度上的差异，消融各损失项
- 主要风险：联合训练需要多视图几何标注（深度/对应真值），合成场景容易生成但真实场景标注成本高；可能因损失权重调节困难导致性能负迁移

#### 路线 2：基于不确定性指导的动态视图选择与几何注入
- 核心想法：结合AdaQ的自适应采样思想和G3VLA的几何注入，构建一个根据任务不确定性动态选择最相关视图和注入几何信息的框架
- 新问题定义：在机器人持续感知场景中，面对多视角视频流，系统需实时决定当前时刻哪些视角应被激活和详细处理，并依据任务查询（如物体计数或空间关系）动态调整采样间隔和几何注入强度
- 机制来源：
  - AdaQ的3-σ规则根据全局/局部查询自适应确定帧采样区间，解决了固定采样导致的信息冗余或不足
  - G3VLA的PRoPE和跨视图融合需要多视图对齐，但未考虑视图选择，冗余视图增加计算量而无关视图引入噪声
- 为什么值得做：AdaQ通过准高斯分布自适应选择关键帧，与G3VLA的几何注入互补：前者决定哪些视图需要详细处理，后者决定如何注入几何，可减少冗余同时保持几何精度
- 理论/数学创新理由：
  - 数学对象：查询条件不确定性驱动的帧选择概率分布，结合几何编码的信息增益
  - 来源分解：AdaQ使用门控熵作为不确定性度量来确定帧区间，但未利用几何信息；G3VLA提供了几何编码但无自适应选择
  - 新建模方式：定义每个时刻t的视图重要性分数S(v_t) = α * H_gate(v_t) + β * I_geo(v_t; query)，其中H_gate为G3VLA门控熵（来自GeMoE思想），I_geo为几何信息增益（PRoPE与query的相关性），选择Top-K视图进行几何注入和融合
  - 公式草图：S(v) = α * (-Σ w_i log w_i) + β * sim(PRoPE(v), query_embedding)，其中w_i为v在G3VLA中的门控权重，sim为余弦相似度
  - 为什么可能有效：门控熵高表明该视图需要更多专家资源（复杂），几何信息增益高表明该视图与查询任务相关，联合选择可减少冗余并聚焦对任务最有价值的视图
- 可验证实验：在机器人操作模拟环境（如LIBERO）中，对比固定视图采样、AdaQ单独采样和联合不确定性采样的任务成功率、推理延迟和内存占用。使用G3VLA作为基础VLA模型
- 主要风险：需要实时计算门控熵和几何相似度，可能增加额外计算开销；query embedding的定义可能依赖任务先验

## 方向 2：大视觉语言模型的自适应计算资源分配机制
从模型结构、输入采样和参数剪枝三个层面协同优化MLLM的计算效率，通过不确定性感知实现自适应资源分配。

### 代表论文

- [GeMoE: Gating Entropy is All You Need for Uncertainty-aware Adaptive Routing in MoE-based Large Vision-Language Models](https://arxiv.org/abs/2606.26287v1)：提出GeMoE，通过门控熵代理MDL来动态调整每个token激活的专家数量，在保持性能的同时提升专家激活稀疏性。
- [Towards Fast and Effective Long Video Understanding of Multimodal Large Language Models via Adaptive Quasi-Gaussian Sampling](https://arxiv.org/abs/2606.24187v2)：针对多模态大模型处理长视频时计算成本高的问题，本文提出自适应准高斯采样方法AdaQ，无需训练，通过动态调整采样区间实现鲁棒帧选择。实验表明，仅用64帧即可使Qwen3-VL-8B平均性能超过GPT4o 15.8%，且仅需设置一个超参数。
- [Toward Low-Latency Vision-Language Models with Doubly-Correct Predictions in Egocentric Visual Understanding](https://arxiv.org/abs/2606.25160v1)：提出一种基于原理的剪枝策略（rationale-informed pruning），利用VLM自身的空间-时间依据指导非均匀剪枝，在降低计算开销的同时保持双重正确预测（既准确又证据充分）。

### 共同创新点
- GeMoE通过门控熵衡量token复杂性动态分配专家数，实现按需计算
- AdaQ通过准高斯采样自适应选择关键帧，降低视频输入冗余
- 剪枝策略利用模型自身原理热图指导非均匀剪枝，维持双重正确预测

### 尚未解决的问题
- 三种方法独立工作，缺乏联合决策或相互感知的机制
- 没有统一的复杂度度量同时指导专家分配、帧采样和剪枝比率
- 剪枝后模型可靠性（双重正确预测）在其他两种方法中未被考虑

### 二次创新路线
#### 路线 1：统一不确定性度量驱动的三层自适应资源分配框架
- 核心想法：提出一种共享的不确定性度量（基于门控熵和预测置信度），联合指导MoE专家数量、关键帧采样步长和剪枝掩码，使得在给定延迟预算下最大化性能
- 新问题定义：在资源受限的MLLM部署中，给定最大推理延迟T_max，模型需动态为每个任务分配：每token激活专家数k、每视频采样的帧数F、以及每层参数保留比率p，使得整体推理延迟≤T_max且性能最优
- 机制来源：
  - GeMoE的门控熵H(x)表明token的复杂性，可映射到所需专家数
  - AdaQ的3-σ区间与查询类型关联，但未利用更细粒度的token级不确定性
  - 剪枝策略的热图重要性用于非均匀剪枝，但重要性是基于静态的，未考虑输入动态
- 为什么值得做：GeMoE证明了门控熵与MDL的关系，AdaQ使用准高斯规则，剪枝使用热图重要性，三者本质上都在估计信息冗余或认知不确定性，统一度量可避免各自为政
- 理论/数学创新理由：
  - 数学对象：联合资源分配优化问题，目标为在延迟约束下最大化期望性能，不确定度作为资源分配调度器
  - 来源分解：GeMoE解决专家数分配问题；AdaQ解决帧数分配；剪枝解决参数分配；三者互不关联
  - 新建模方式：定义共享不确定性U = H(x) + τ * (1 - max(softmax(y_hat)))（预测熵与置信度）。延迟模型L(k, F, p) = c1*k + c2*F + c3*(1-p)。优化目标：max E[Accuracy] s.t. L ≤ T_max。决策变量通过轻量级预测器从U映射
  - 公式草图：k, F, p = f_θ(U)，其中f_θ为MLP，训练数据收集通过随机搜索在验证集上获得最优(k, F, p) tuples
  - 为什么可能有效：不确定性U整合了输入复杂度和模型置信度，高不确定性需要更多资源（更多专家/帧/参数）以提升性能，低不确定性可减少资源节省延迟，实现更细粒度的自适应
- 可验证实验：在长视频理解基准（如VideoMME）上，固定一个MLLM（如LLaVA-NeXT），嵌入GeMoE路由、AdaQ采样和剪枝方法，训练三层资源预测器，与单独优化及均匀分配对比，在相同延迟下比较准确率。消融U中不同成分
- 主要风险：联合优化需大量数据收集训练预测器，可能过拟合；延迟模型L线性近似可能不准确；需避免三层之间负交互

#### 路线 2：剪枝与动态路由协同：在MoE模型中保持双重正确预测
- 核心想法：将剪枝策略的热图重要性引入GeMoE的门控机制，使专家选择不仅考虑token的MDL，还考虑保持在剪枝后仍能输出正确证据的重要性
- 新问题定义：在已进行结构化剪枝的MoE VLM中，要求模型在推理时不仅预测正确标签，且其选择的专家和生成的原理热图能正确反映证据区域，即双重正确剪枝MoE
- 机制来源：
  - 剪枝策略的原理热图定位了与正确证据相关的参数，但未用于路由机制
  - GeMoE动态路由根据门控熵选择专家，但未考虑参数重要性差异
  - 剪枝后某些专家被剪掉，剩余专家的门控需要重新校准
- 为什么值得做：剪枝策略发现现有剪枝虽保留证据定位却损害准确性，而GeMoE仅考虑MDL未考虑证据；两者结合可使MoE在剪枝环境下仍维持双重正确
- 理论/数学创新理由：
  - 数学对象：证据感知的门控权重，结合参数重要性与MDL
  - 来源分解：剪枝策略提供每层参数的重要性热图I_param(l)；GeMoE提供门控熵H(x)和路由权重w_i(x)
  - 新建模方式：新的门控分数w'_i(x) = w_i(x) * exp(β * I_param(l_i))，其中l_i为第i个专家所在层，I_param为该层参数平均重要性（基于热图）。训练时同时优化交叉熵和证据对齐损失（剪枝策略中的双重正确损失）
  - 公式草图：L_joint = L_ce + γ1 * L_mono + γ2 * L_doublyCorrect，其中L_mono为GeMoE的单调性损失，L_doublyCorrect = ||attn_map - rationale_mask||^2（注意力与原理掩码的MSE）
  - 为什么可能有效：I_param引导路由优先激活对正确证据贡献大的专家，避免剪枝后路由到被证据削弱的专家；双重正确损失直接惩罚证据不对齐，维持可解释性
- 可验证实验：在自我中心视频理解数据集（如Ego4D）上，使用一个MoE VLM（如MoE-LLaVA）进行剪枝（50%参数），比较原始路由、GeMoE、剪枝+原始路由、剪枝+GeMoE、以及所提联合方法的双重正确准确率和平均精度。可视化路由偏差
- 主要风险：需要计算每层参数重要性，增加预计算开销；双重正确损失可能降低泛化能力；剪枝后专家数量减少导致路由灵活性下降

## 方向 3：面向医疗领域的高可靠RAG系统构建
针对临床环境中LLM的安全性和病理图像检索的效率问题，整合多智能体错误检测与病理索引压缩，形成端到端可靠RAG系统。

### 代表论文

- [MedGuards: Multi-Agent System for Reliable Medical Error Detection and Correction](https://arxiv.org/abs/2606.25651v2)：提出MedGuards框架，将医疗错误检测与纠正建模为多智能体上下文学习任务，通过专门智能体协作和置信度仲裁机制，无需额外训练即可显著提升性能，并引入KPCS评估指标。
- [Reducing Redundancy in Whole-Slide Image Patching for Scalable Indexing and Retrieval](https://arxiv.org/abs/2606.26157v1)：ARReST通过识别并移除跨类别中高度相似的冗余图块（对判别贡献小），在保持检索性能的同时显著压缩WSI索引存储。

### 共同创新点
- MedGuards通过多智能体协作和置信度仲裁检测纠正医疗文本错误，无需额外训练
- ARReST通过识别跨类别冗余图块压缩病理图像索引，降低存储同时保持检索精度

### 尚未解决的问题
- MedGuards仅处理文本错误，未利用图像信息；ARReST仅索引图像，未考虑文本生成可靠性
- 两者缺乏统一的数据流协同，无法在检索后自动纠正生成错误
- 缺少针对医疗RAG场景的端到端评估框架

### 二次创新路线
#### 路线 1：检索-生成-验证闭环：基于多智能体仲裁的病理查询系统
- 核心想法：在病理RAG中，先用ARReST压缩索引快速检索相关图块，再用LLM生成诊断描述，最后用MedGuards多智能体检测并纠正生成中的错误，形成闭环
- 新问题定义：构建一个端到端病理查询系统：输入WSI区域查询，系统输出依据检索证据生成的诊断文本，且文本必须经过多智能体验证纠正，保证正确性和可溯源性
- 机制来源：
  - ARReST的冗余仓库移除低判别性图块，压缩索引，解决了检索空间大、延迟高的问题
  - MedGuards的检测-定位-纠正流水线纠正生成的错误，解决了LLM输出不可靠问题
  - MedGuards的置信度仲裁机制可提供每个纠正的可信度评分
- 为什么值得做：ARReST压缩使检索更快，MedGuards确保生成正确，且MedGuards的检测智能体可以定位到具体句子，与检索结果交叉验证
- 理论/数学创新理由：
  - 数学对象：生成错误概率与检索相关性联合的贝叶斯风险最小化
  - 来源分解：ARReST降低了检索空间但未考虑检索结果的质量；MedGuards纠正错误但未使用检索证据的置信度
  - 新建模方式：构建检索相关性得分r(q, d)（来自ARReST）和纠正置信度c（来自MedGuards仲裁）。最终决策为：若c(corrected) - c(original) > δ且r(q, d) > τ，则接受纠正；否则输出原始。风险函数R = E[L(y, ŷ)]
  - 公式草图：ŷ = { y_orig if c_orig > c_corr + δ or r < τ; y_corr otherwise }，c_orig, c_corr分别为MedGuards对原始和纠正文本的置信度分数
  - 为什么可能有效：结合证据可靠性和纠正可信度避免过度纠正，降低假阳性率；ARReST确保检索到的证据与查询相关，使MedGuards能以高置信度纠正
- 可验证实验：在公开病理WSI数据集（如TCGA）上，构建问答集（问题+答案对），比较基线（直接LLM、RAG+LLM、RAG+LLM+MedGuards后处理）和所提闭环系统的准确率、纠正接受率和端到端延迟。消融置信度阈值δ和τ
- 主要风险：闭环可能引入延迟累积；置信度阈值需精细调参；多智能体系统在资源受限的临床部署中可能计算量过大

#### 路线 2：并行错误检测与图块检索：面向实时临床笔记支持系统
- 核心想法：将MedGuards的检测智能体与ARReST的检索智能体并行运行，检测到错误时自动触发相关图块检索作为辅助证据，帮助纠正智能体生成更准确的修正
- 新问题定义：实时临床笔记支持：医生输入文本的同时，系统并行检测潜在错误并检索相关WSI图块，当检测到错误时即时呈现检索结果和纠正建议，交互式保证安全
- 机制来源：
  - MedGuards的检测智能体能快速判断是否存在错误，并定位错误句子
  - ARReST的检索机制可在百万级图块中快速查询，且压缩后索引小
  - MedGuards的纠正智能体目前仅依靠文本，缺乏多模态证据
- 为什么值得做：MedGuards纠正时仅依赖文本内上下文，若结合检索到的病理图像证据可提升纠正准确性（如药物剂量错误可参考病理图像中的细胞形态）
- 理论/数学创新理由：
  - 数学对象：联合概率建模：错误概率P(error | text)与检索相关性P(relevant | error location)
  - 来源分解：MedGuards提供了错误检测的概率c_det；ARReST提供了查询与图块的相似度sim(q, patch)
  - 新建模方式：当c_det > threshold时，将错误句子作为查询q，通过ARReST检索Top-K图块，将图块特征输入纠正智能体作为附加上下文。纠正智能体输出条件概率p(s_corr | text, patches)
  - 公式草图：s_corr = argmax p(s | x, patches) where patches = ARReST(q), q = error_sentence
  - 为什么可能有效：病理图像提供与错误相关的视觉上下文（如正常细胞 vs 异常细胞），帮助纠正智能体判断正确术语，减少对单一文本的依赖
- 可验证实验：在医疗笔记数据集（如MedCoDi）上，构建包含病理图像参考的测试集（模拟临床场景），比较MedGuards单独、文本+静态图像、文本+ARReST动态检索纠正的准确率、纠正质量和延迟。控制检索时间
- 主要风险：并行系统需要协调文本和图像两个线程，可能增加系统复杂度；检索结果可能引入视觉噪声误导纠正；需要实时性要求高，对检索速度要求严格

## 方向 4：多模态大模型效率优化与鲁棒性增强
结合跨层频谱演化剪枝（论文1）与辅助AI评估（论文3），提出面向细粒度视觉感知的鲁棒性感知剪枝策略，在保证效率的同时维持模型对文本等细节的敏感度。

### 代表论文

- [Spectral Evolution-Guided Token Pruning in Multimodal Large Language Models](https://arxiv.org/abs/2606.24165v1)：提出基于跨层频谱演化（CLSE）的无训练视觉token剪枝框架，通过频域量化token在Transformer层间的语义演化强度来识别重要token，在减少计算开销的同时保持或提升多模态大语言模型性能。
- [Are We There Yet? Exploring the Capabilities of MLLMs in Assistive AI Applications](https://arxiv.org/abs/2606.25084v1)：系统评估了多模态大语言模型在货币识别、场景文本问答、多语言菜单阅读等真实辅助任务上的表现，构建了基于头戴GoPro的自我中心数据基准NetraLink，揭示了当前MLLMs在细粒度视觉感知和鲁棒性方面的优势与局限。

### 共同创新点
- 均关注多模态大模型的实际应用效果
- 均涉及token或特征的细粒度重要性评估

### 尚未解决的问题
- 当前剪枝方法未考虑下游任务对文本细节的需求
- 辅助AI场景下模型对小文本和低分辨率视觉信息处理不足

### 二次创新路线
#### 路线 1：语义感知频谱剪枝
- 核心想法：将CLSE的频谱演化得分与文本引导的注意力得分加权融合，保留对文本指令至关重要的视觉token。
- 新问题定义：面向文本密集型场景（如货币识别、菜单阅读）的多模态大模型效率优化问题——要求剪枝后模型文本识别准确率不下降。
- 机制来源：
  - 论文1解决如何通过频域跨层演化识别重要视觉token，但其得分仅基于视觉语义变化，未考虑文本需求
  - 论文3揭示当前MLLM对场景文本的细粒度识别不足，暗示需要保留文本相关token
- 为什么值得做：辅助AI任务依赖场景文本，CLSE剪枝可能丢弃包含文本的token；文本注意力可弥补。
- 理论/数学创新理由：
  - 数学对象：加权融合得分函数 S_i = α·S_i^CLSE + (1-α)·A_i^text，其中S_i^CLSE为频谱演化得分，A_i^text为token i与文本描述的注意力相关性。
  - 来源分解：论文1定义了S_i^CLSE = ||G⊙F(X_i^ℓ) - G⊙F(X_i^{ℓ+1})||_2的归一化；论文3评估了注意力权重与文本对齐的关系。
  - 新建模方式：新得分函数结合两种互补信息，保持高频变化和文本相关性。
  - 公式草图：S_i = β·norm(||G⊙F(X_i^ℓ) - G⊙F(X_i^{ℓ+1})||_2) + (1-β)·norm(∑_t A_{i,t}^text)，其中β为超参数，A_{i,t}^text为第t个文本token与视觉token i的注意力权重。
  - 为什么可能有效：频谱演化捕获视觉语义变化，文本注意力确保文本相关token不被剪除；融合后可能平衡计算效率与文本感知性能。
- 可验证实验：在NetraLink基准的货币和菜单任务上比较CLSE、随机剪枝、注意力剪枝与提出的语义感知剪枝，控制保留token比例（如10%），评估文本VQA准确率和推理时间。
- 主要风险：α需要手动调整；注意力机制在早期层可能不够准确。

#### 路线 2：鲁棒性引导的动态token保留
- 核心想法：根据输入图像的鲁棒性特征（如光照、尺度）动态调整剪枝保留比例，采用不确定性量化指导保留数量。
- 新问题定义：多模态大模型在非受控环境下的自适应剪枝问题——根据图像质量预测最优保留token数，保持下游任务性能稳定。
- 机制来源：
  - 论文1提出固定保留K个token的剪枝，缺乏对输入的适应性
  - 论文3指出光照、遮挡、小文本是性能瓶颈，暗示需要根据困难程度调整计算预算
- 为什么值得做：辅助AI场景中光照和遮挡变化大，统一定长剪枝可能导致鲁棒性下降；动态调整可适应性保留更多token。
- 理论/数学创新理由：
  - 数学对象：不确定性预测器 U = f_θ(x)，映射图像x到保留率r = g(U)，其中g为单调非增函数。
  - 来源分解：论文1的剪枝策略固定保留率；论文3分析了不同场景下MLLM的识别准确率差异。
  - 新建模方式：训练一个小型不确定性回归网络，以图像嵌入为输入，输出预测误差方差；方差大时增加保留token比例。
  - 公式草图：r = r_min + (r_max - r_min) * exp(-λ·U)，U = Var[ŷ]由数据不确定性估计得到；保留token数K = r * N。
  - 为什么可能有效：不确定性高的区域通常包含更多关键信息，增加保留token可提升鲁棒性；不确定性低的图像可大幅剪枝。
- 可验证实验：在NetraLink数据集上训练一个轻量CNN不确定性预测器，比较固定剪枝与动态剪枝在不同光照/遮挡条件下的ANLS得分。
- 主要风险：不确定性预测器需要额外训练数据，可能引入噪声。

## 方向 5：几何先验注入与多任务分割
融合几何感知蒸馏（论文2）与多任务学习框架（论文4），引入3D几何一致性先验提升医学图像多类分割的准确性和鲁棒性。

### 代表论文

- [Boosting Text-Driven Video Segmentation via Geometry-Aware Distillation](https://arxiv.org/abs/2606.24464v1)：提出GeoLaV两阶段框架，通过单目新视图合成预训练和几何感知蒸馏，将3D几何知识注入文本驱动视频分割，提升时空一致性与语言对齐。
- [Intracranial Aneurysm Classification and Segmentation via Tri-Axial ROI and Multi-Task Learning](https://arxiv.org/abs/2606.26706v1)：提出一个两阶段多任务框架，结合2D三轴ROI提取和3D多任务nnU-Net，实现13个解剖位置的动脉瘤分类、多类动脉瘤分割和多类血管分割，在RSNA 2025挑战中获得第二名。

### 共同创新点
- 均通过额外先验（几何知识/多任务）增强分割性能
- 均涉及多类分割任务和结构化输出

### 尚未解决的问题
- 论文2的几何蒸馏针对视频，未直接应用于3D医学图像
- 论文4的多任务学习未显式建模几何一致性

### 二次创新路线
#### 路线 1：几何感知的多任务颅内动脉瘤分割
- 核心想法：在论文4的多任务nnU-Net基础上，引入单目深度估计或三维重构损失作为几何约束，提升分割的3D结构一致性。
- 新问题定义：几何一致的多任务血管分割与分类——要求分割结果在三维空间中满足平滑性、连通性等几何先验。
- 机制来源：
  - 论文4解决多任务分割联合分类问题，但未利用几何信息
  - 论文2提出从单目图像学习几何一致表示，并通过蒸馏注入分割网络
- 为什么值得做：颅内血管具有复杂3D形态，几何先验可减少因视角变化导致的分割断裂或位置偏移。
- 理论/数学创新理由：
  - 数学对象：几何一致性损失 L_geo = ||D(∇S) - D_prior||，其中S为分割体素，D为深度预测函数，∇S为分割边界梯度。
  - 来源分解：论文4的损失为多任务Dice+CE和分类BCE；论文2使用新视图合成损失预训练几何编码器。
  - 新建模方式：在原多任务损失中加入几何正则项：L_total = L_mtl + λ·L_geo(S, I)，其中I为输入CT/MRI，L_geo通过预测深度图与分割边界对齐程度衡量。
  - 公式草图：L_geo = MSE(D(S_binary) - D_gt)，其中S_binary为动脉瘤二值掩膜，D(·)为单目深度估计网络（如论文2的π3模型）输出，D_gt可通过对空间坐标线性映射得到粗略深度。
  - 为什么可能有效：深度一致性能约束分割的几何结构，避免不连贯或异常的血管分割，尤其对细长动脉瘤有益。
- 可验证实验：在RSNA 2025数据集上，以论文4基线加入L_geo项，比较Dice分数和位置分类准确率。
- 主要风险：单目深度估计在医学图像上可能不准确，需要预训练或微调。

#### 路线 2：跨域几何蒸馏用于医学图像分割
- 核心想法：将论文2中从自然图像学到的几何感知蒸馏迁移到医学图像，利用大型3D几何模型（如VGGT）生成伪3D标注，蒸馏到医学分割网络。
- 新问题定义：跨域几何蒸馏——利用自然图像域预训练的3D几何模型增强医学图像分割的3D结构理解，无需配对医学数据。
- 机制来源：
  - 论文2提出从自然单目图像预训练几何表示并蒸馏到视频分割模型
  - 论文4的多任务网络可作为医学分割的强基线
- 为什么值得做：医学标注昂贵，自然图像几何知识可迁移，提升小样本分割性能。
- 理论/数学创新理由：
  - 数学对象：蒸馏损失：L_distill = MSE(f_proj(F_seg), f_geo(F_geo))，其中F_seg为分割网络特征，F_geo为预训练几何模型特征。
  - 来源分解：论文2使用投影头将记忆特征映射到VFM/3D特征空间计算余弦相似度；论文4使用跨注意力池化。
  - 新建模方式：沿用双分支蒸馏结构：分割网络特征经投影头与固定几何编码器特征对比，采用Hinge铰链损失稳定训练。
  - 公式草图：L_distill = max(0, cos(f_proj(z_seg), z_geo) - margin)，其中z_seg为分割网络瓶颈特征，z_geo为VGGT编码器特征。
  - 为什么可能有效：自然图像几何模型已学习通用3D结构先验，蒸馏后医学分割网络隐式获得几何感知，可能提升小样本下的分割质量。
- 可验证实验：在颅内动脉瘤数据集上，将论文4的nnU-Net替换为加入蒸馏分支的版本，与原始多任务模型比较分割Dice和长轴误差。
- 主要风险：域差异可能大，需要域适应或大量微调。
