import importlib.util
import sys
import unittest
from pathlib import Path


def _load_module():
    root = Path(__file__).resolve().parents[1]
    src_dir = root / "src"
    if str(src_dir) not in sys.path:
        sys.path.insert(0, str(src_dir))
    src_path = root / "src" / "7.generate_innovation_brief.py"
    spec = importlib.util.spec_from_file_location("innovation_brief_mod", src_path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def _route():
    return {
        "route_name": "证据约束的不确定性路由",
        "idea": "把视觉证据定位和不确定性估计联合起来，形成可拒答的医学多模态推理系统。",
        "why_promising": "该路线能同时减少弱证据过度适配和无依据回答，适合真实临床场景。",
        "new_problem_definition": "定义一个需要同时输出诊断答案、证据区域和拒答概率的新评测任务。",
        "source_mechanisms": [
            "第一篇论文提供证据区域定位机制，用于约束模型只能依据相关图像区域推理。",
            "第二篇论文提供不确定性门控机制，用于在证据不足时降低更新或触发拒答。",
        ],
        "theoretical_rationale": {
            "math_object": "核心对象是条件风险函数、证据置信度和拒答代价。",
            "source_decomposition": "现有论文分别处理证据定位和不确定性估计，缺少统一风险目标。",
            "new_formulation": "构造联合目标，同时最小化诊断损失、证据一致性损失和拒答校准损失。",
            "formula_sketch": "L = L_cls + lambda * L_ground + beta * E[u(x) * C_wrong - r(x) * C_reject]",
            "why_it_may_work": "该目标把错误答案风险和证据缺失风险显式分开，能提升稳健性和可解释性。",
        },
        "possible_experiment": "在医学视觉问答和报告生成数据上比较答案准确率、证据一致性和拒答校准误差。",
        "risk": "主要风险是证据标注不足，需要用弱监督或人工小样本校准补充。",
    }


def _payload():
    return {
        "directions": [
            {
                "name": "证据约束的可靠医学多模态推理",
                "summary": "该方向结合证据定位、不确定性估计和拒答机制，面向高风险医学问答。",
                "paper_ids": ["2605.00001v1", "2605.00002v1"],
                "shared_innovations": ["共同创新在于把模型答案与可检查证据和风险估计绑定。"],
                "open_gaps": ["尚未统一评估答案正确性、证据一致性和拒答校准。"],
                "innovation_routes": [_route()],
            }
        ]
    }


class FakeClient:
    def __init__(self, responses):
        self.responses = list(responses)

    def chat_json(self, messages, max_tokens):
        if not self.responses:
            return None
        return self.responses.pop(0)


class InnovationResearchDirectionsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = _load_module()

    def _papers(self):
        return [
            {"paper_id": "2605.00001v1", "title": "A", "abstract": "medical evidence grounding"},
            {"paper_id": "2605.00002v1", "title": "B", "abstract": "medical uncertainty routing"},
            {"paper_id": "2605.00003v1", "title": "C", "abstract": "medical calibration"},
        ]

    def test_retries_in_batches_when_full_generation_is_unparsable(self):
        client = FakeClient([None, _payload()])
        result = self.mod.build_research_directions(client, self._papers(), {})

        self.assertEqual(len(result["directions"]), 1)
        self.assertIn("分批生成兜底", result["generation_warning"])

    def test_disabled_llm_warning_is_not_confused_with_parse_failure(self):
        result = self.mod.build_research_directions(None, self._papers(), {})

        self.assertEqual(result["directions"], [])
        self.assertIn("未启用 LLM", result["generation_warning"])


if __name__ == "__main__":
    unittest.main()
