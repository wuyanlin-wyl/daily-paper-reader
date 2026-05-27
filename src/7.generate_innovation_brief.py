#!/usr/bin/env python

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from typing import Any, Dict, List

import requests


SCRIPT_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

CONFIG_FILE = os.path.join(ROOT_DIR, "config.yaml")
TODAY_STR = str(os.getenv("DPR_RUN_DATE") or "").strip() or datetime.now(timezone.utc).strftime("%Y%m%d")
RANGE_DATE_RE = re.compile(r"^(\d{8})-(\d{8})$")

BLT_API_KEY = os.getenv("BLT_API_KEY")
BLT_MODEL = os.getenv("BLT_SUMMARY_MODEL") or os.getenv("SUMMARY_MODEL") or "gemini-3-flash-preview"
DEFAULT_BASE_URL = "https://api.bltcy.ai/v1"


def log(message: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {message}", flush=True)


def load_config() -> Dict[str, Any]:
    if not os.path.exists(CONFIG_FILE):
        return {}
    try:
        import yaml  # type: ignore
    except Exception:
        return {}
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        return data if isinstance(data, dict) else {}
    except Exception as exc:
        log(f"[WARN] failed to read config.yaml: {exc}")
        return {}


def resolve_docs_dir() -> str:
    config = load_config()
    setting = (config.get("arxiv_paper_setting") or {}) if isinstance(config, dict) else {}
    raw = str(setting.get("docs_dir") or "docs").strip() or "docs"
    if os.path.isabs(raw):
        return raw
    return os.path.join(ROOT_DIR, raw)


def resolve_mode() -> str:
    config = load_config()
    setting = (config.get("arxiv_paper_setting") or {}) if isinstance(config, dict) else {}
    raw = str(setting.get("mode") or "standard").strip() or "standard"
    return raw.split(",", 1)[0].strip() or "standard"


def format_date(date_str: str) -> str:
    text = str(date_str or "").strip()
    if RANGE_DATE_RE.match(text):
        start, end = text.split("-", 1)
        return f"{start[:4]}-{start[4:6]}-{start[6:]} ~ {end[:4]}-{end[4:6]}-{end[6:]}"
    if re.match(r"^\d{8}$", text):
        return f"{text[:4]}-{text[4:6]}-{text[6:]}"
    return text


def day_dir_for(docs_dir: str, date_str: str) -> str:
    if RANGE_DATE_RE.match(date_str):
        return os.path.join(docs_dir, date_str)
    return os.path.join(docs_dir, date_str[:6], date_str[6:])


def resolve_latest_date_token(docs_dir: str) -> str:
    candidates: List[tuple[str, str]] = []
    if not os.path.isdir(docs_dir):
        return TODAY_STR

    for name in os.listdir(docs_dir):
        top_path = os.path.join(docs_dir, name)
        if not os.path.isdir(top_path):
            continue
        if RANGE_DATE_RE.match(name):
            meta_path = os.path.join(top_path, "papers.meta.json")
            readme_path = os.path.join(top_path, "README.md")
            if os.path.exists(meta_path) or os.path.exists(readme_path):
                _, end = name.split("-", 1)
                candidates.append((end, name))
            continue
        if not re.match(r"^\d{6}$", name):
            continue
        for day in os.listdir(top_path):
            if not re.match(r"^\d{2}$", day):
                continue
            token = f"{name}{day}"
            day_path = os.path.join(top_path, day)
            meta_path = os.path.join(day_path, "papers.meta.json")
            readme_path = os.path.join(day_path, "README.md")
            if os.path.exists(meta_path) or os.path.exists(readme_path):
                candidates.append((token, token))

    if not candidates:
        return TODAY_STR
    candidates.sort(key=lambda item: item[0], reverse=True)
    return candidates[0][1]


def read_json(path: str, default: Any) -> Any:
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as exc:
        log(f"[WARN] failed to read json: {path}: {exc}")
        return default


class SimpleLLMClient:
    def __init__(self, api_key: str, model: str) -> None:
        self.api_key = api_key
        self.model = model
        self.base_urls = self._resolve_base_urls()

    @staticmethod
    def _resolve_base_urls() -> List[str]:
        candidates = [
            os.getenv("LLM_PRIMARY_BASE_URL"),
            os.getenv("BLT_PRIMARY_BASE_URL"),
            os.getenv("BLT_API_BASE"),
            os.getenv("SUMMARY_BASE_URL"),
            DEFAULT_BASE_URL,
        ]
        output: List[str] = []
        for item in candidates:
            text = str(item or "").strip().rstrip("/")
            if text and text not in output:
                output.append(text)
        return output

    @staticmethod
    def _chat_url(base_url: str) -> str:
        base = str(base_url or "").strip().rstrip("/")
        if base.lower().endswith("/chat/completions"):
            return base
        if re.search(r"/v\d+$", base, flags=re.IGNORECASE):
            return f"{base}/chat/completions"
        return f"{base}/v1/chat/completions"

    @staticmethod
    def _strip_json_wrappers(text: str) -> str:
        cleaned = str(text or "").strip()
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r"\s*```$", "", cleaned)
        return cleaned.strip()

    @classmethod
    def _parse_json(cls, text: str) -> Dict[str, Any] | None:
        cleaned = cls._strip_json_wrappers(text)
        if not cleaned:
            return None
        try:
            parsed = json.loads(cleaned)
            return parsed if isinstance(parsed, dict) else None
        except Exception:
            pass

        match = re.search(r"\{.*\}", cleaned, flags=re.DOTALL)
        if not match:
            return None
        try:
            parsed = json.loads(match.group(0))
            return parsed if isinstance(parsed, dict) else None
        except Exception:
            return None

    def chat_json(self, messages: List[Dict[str, str]], max_tokens: int) -> Dict[str, Any] | None:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.2,
            "max_tokens": int(max_tokens),
            "response_format": {"type": "json_object"},
        }

        last_error: Exception | None = None
        for base_url in self.base_urls:
            try:
                resp = requests.post(self._chat_url(base_url), headers=headers, json=payload, timeout=120)
                if resp.status_code in {400, 404, 415, 422}:
                    # Some OpenAI-compatible gateways do not support response_format.
                    payload.pop("response_format", None)
                    resp = requests.post(self._chat_url(base_url), headers=headers, json=payload, timeout=120)
                resp.raise_for_status()
                data = resp.json()
                choices = data.get("choices") or []
                if not choices:
                    raise RuntimeError("LLM response missing choices")
                message = choices[0].get("message") or {}
                content = message.get("content") or ""
                if isinstance(content, list):
                    content = "\n".join(str(x.get("text") or x.get("content") or x) for x in content)
                return self._parse_json(str(content))
            except Exception as exc:
                last_error = exc
                continue

        if last_error is not None:
            raise last_error
        return None


def normalize_paper_id(value: Any) -> str:
    text = str(value or "").strip()
    if not text:
        return ""
    if text.startswith("http"):
        text = text.rstrip("/").rsplit("/", 1)[-1]
    if text.lower().startswith("arxiv:"):
        text = text.split(":", 1)[1].strip()
    return text


def clean_text(value: Any, max_len: int = 0) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    if max_len and len(text) > max_len:
        return text[: max_len - 1].rstrip() + "..."
    return text


def collect_recommend_papers(date_str: str, mode: str) -> Dict[str, Dict[str, Any]]:
    recommend_path = os.path.join(
        ROOT_DIR,
        "archive",
        date_str,
        "recommend",
        f"arxiv_papers_{date_str}.{mode}.json",
    )
    payload = read_json(recommend_path, {})
    papers: Dict[str, Dict[str, Any]] = {}
    for section, key in (("deep", "deep_dive"), ("quick", "quick_skim")):
        for item in payload.get(key) or []:
            if not isinstance(item, dict):
                continue
            pid = normalize_paper_id(item.get("id") or item.get("paper_id") or item.get("link"))
            if not pid:
                continue
            merged = dict(item)
            merged["section"] = section
            papers[pid] = merged
    return papers


def collect_meta_papers(docs_dir: str, date_str: str) -> List[Dict[str, Any]]:
    meta_path = os.path.join(day_dir_for(docs_dir, date_str), "papers.meta.json")
    payload = read_json(meta_path, {})
    papers = (payload.get("papers") if isinstance(payload, dict) else []) or []
    return [p for p in papers if isinstance(p, dict)]


def merge_paper_records(meta_papers: List[Dict[str, Any]], recommend_by_id: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    seen: set[str] = set()
    for meta in meta_papers:
        pid = normalize_paper_id(meta.get("paper_id") or meta.get("id"))
        if not pid:
            continue
        merged = dict(recommend_by_id.get(pid) or {})
        merged.update({k: v for k, v in meta.items() if v not in (None, "")})
        merged["paper_id"] = pid
        records.append(merged)
        seen.add(pid)

    for pid, rec in recommend_by_id.items():
        if pid in seen:
            continue
        item = dict(rec)
        item["paper_id"] = pid
        records.append(item)

    return records


INNOVATION_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "one_sentence_contribution": {"type": "string"},
        "technical_innovations": {"type": "array", "items": {"type": "string"}},
        "problem_setting_innovation": {"type": "array", "items": {"type": "string"}},
        "evidence_or_result_innovation": {"type": "array", "items": {"type": "string"}},
        "difference_from_prior_work": {"type": "string"},
        "reader_takeaway": {"type": "string"},
        "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
    },
    "required": [
        "one_sentence_contribution",
        "technical_innovations",
        "problem_setting_innovation",
        "evidence_or_result_innovation",
        "difference_from_prior_work",
        "reader_takeaway",
        "confidence",
    ],
}


DAILY_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "daily_trends": {"type": "array", "items": {"type": "string"}},
        "most_worth_reading": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "paper_id": {"type": "string"},
                    "reason": {"type": "string"},
                },
                "required": ["paper_id", "reason"],
            },
        },
    },
    "required": ["daily_trends", "most_worth_reading"],
}


DIRECTIONS_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "directions": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "name": {"type": "string"},
                    "summary": {"type": "string"},
                    "paper_ids": {"type": "array", "items": {"type": "string"}},
                    "shared_innovations": {"type": "array", "items": {"type": "string"}},
                    "open_gaps": {"type": "array", "items": {"type": "string"}},
                    "innovation_routes": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": False,
                            "properties": {
                                "route_name": {"type": "string"},
                                "idea": {"type": "string"},
                                "why_promising": {"type": "string"},
                                "possible_experiment": {"type": "string"},
                                "risk": {"type": "string"},
                            },
                            "required": [
                                "route_name",
                                "idea",
                                "why_promising",
                                "possible_experiment",
                                "risk",
                            ],
                        },
                    },
                },
                "required": [
                    "name",
                    "summary",
                    "paper_ids",
                    "shared_innovations",
                    "open_gaps",
                    "innovation_routes",
                ],
            },
        }
    },
    "required": ["directions"],
}


def build_paper_prompt(paper: Dict[str, Any]) -> List[Dict[str, str]]:
    title = clean_text(paper.get("title_en") or paper.get("title"), 500)
    abstract = clean_text(paper.get("abstract_en") or paper.get("abstract"), 3000)
    tldr = clean_text(paper.get("tldr") or paper.get("summary"), 1000)
    evidence = clean_text(paper.get("evidence") or paper.get("reason"), 1000)
    tags = clean_text(paper.get("tags"), 500)
    return [
        {
            "role": "system",
            "content": (
                "你是论文创新点分析助手。请用中文输出，聚焦'这篇论文新在哪里'，"
                "避免泛泛复述摘要。只基于输入信息，证据不足时降低 confidence。"
            ),
        },
        {
            "role": "user",
            "content": (
                f"标题：{title}\n"
                f"摘要：{abstract}\n"
                f"已有速览/TLDR：{tldr}\n"
                f"推荐证据：{evidence}\n"
                f"标签：{tags}\n\n"
                "请提炼该论文的创新点，保持短句、可读、具体。"
            ),
        },
    ]


def call_structured(client: SimpleLLMClient, messages: List[Dict[str, str]], schema_name: str, schema: Dict[str, Any], max_tokens: int) -> Dict[str, Any] | None:
    schema_hint = {
        "role": "system",
        "content": (
            f"请只返回一个 JSON object，schema_name={schema_name}。"
            "不要输出 Markdown，不要输出解释文字。JSON 字段必须符合："
            + json.dumps(schema, ensure_ascii=False)
        ),
    }
    return client.chat_json([schema_hint, *messages], max_tokens=max_tokens)


def fallback_innovation(paper: Dict[str, Any]) -> Dict[str, Any]:
    title = clean_text(paper.get("title_en") or paper.get("title"), 160)
    tldr = clean_text(paper.get("tldr") or paper.get("evidence") or paper.get("abstract_en") or paper.get("abstract"), 240)
    base = tldr or f"围绕「{title}」提出新的研究方案或实验观察。"
    return {
        "one_sentence_contribution": base,
        "technical_innovations": ["需结合全文进一步确认具体技术创新；当前基础信息不足。"],
        "problem_setting_innovation": ["从题目与摘要看，该工作可能面向一个更具体或更实用的任务设定。"],
        "evidence_or_result_innovation": ["建议阅读论文实验部分确认主要结果、对比基线与消融证据。"],
        "difference_from_prior_work": "当前可用信息不足，暂不强行判断与已有工作的明确差异。",
        "reader_takeaway": "可先浏览摘要、方法图和实验表格，判断它是否与自己的研究问题相关。",
        "confidence": "low",
    }


def summarize_paper(client: SimpleLLMClient | None, paper: Dict[str, Any]) -> Dict[str, Any]:
    if client is None:
        return fallback_innovation(paper)
    try:
        parsed = call_structured(client, build_paper_prompt(paper), "paper_innovation", INNOVATION_SCHEMA, 1800)
        if parsed:
            return parsed
    except Exception as exc:
        log(f"[WARN] LLM innovation summary failed for {paper.get('paper_id')}: {exc}")
    return fallback_innovation(paper)


def build_daily_synthesis(client: SimpleLLMClient | None, papers: List[Dict[str, Any]], innovations: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    if not papers:
        return {"daily_trends": [], "most_worth_reading": []}
    if client is None:
        top = []
        for paper in papers[:5]:
            pid = str(paper.get("paper_id") or "")
            if pid:
                top.append({"paper_id": pid, "reason": "基础版按推荐顺序列出，建议优先阅读。"})
        return {"daily_trends": ["本日创新趋势需要配置 LLM 后进行横向综合。"], "most_worth_reading": top}

    brief_items = []
    for paper in papers:
        pid = str(paper.get("paper_id") or "")
        innov = innovations.get(pid) or {}
        brief_items.append(
            {
                "paper_id": pid,
                "title": clean_text(paper.get("title_en") or paper.get("title"), 240),
                "contribution": clean_text(innov.get("one_sentence_contribution"), 300),
                "technical_innovations": innov.get("technical_innovations") or [],
                "takeaway": clean_text(innov.get("reader_takeaway"), 240),
            }
        )
    messages = [
        {
            "role": "system",
            "content": "你是研究趋势编辑。请用中文总结当天论文的共同创新方向，并选出最值得读的论文。",
        },
        {
            "role": "user",
            "content": (
                "下面是当天论文的创新点 JSON。请输出当天趋势和最值得读的论文，"
                "不要编造输入之外的信息。\n\n"
                + json.dumps(brief_items, ensure_ascii=False, indent=2)
            ),
        },
    ]
    try:
        parsed = call_structured(client, messages, "daily_innovation_synthesis", DAILY_SCHEMA, 1600)
        if parsed:
            return parsed
    except Exception as exc:
        log(f"[WARN] LLM daily synthesis failed: {exc}")
    return build_daily_synthesis(None, papers, innovations)


def paper_compact_item(paper: Dict[str, Any], innovations: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    pid = str(paper.get("paper_id") or "").strip()
    innov = innovations.get(pid) or {}
    return {
        "paper_id": pid,
        "title": clean_text(paper.get("title_en") or paper.get("title"), 240),
        "abstract": clean_text(paper.get("abstract_en") or paper.get("abstract"), 800),
        "tags": clean_text(paper.get("tags"), 240),
        "contribution": clean_text(innov.get("one_sentence_contribution"), 260),
        "technical_innovations": innov.get("technical_innovations") or [],
        "problem_setting_innovation": innov.get("problem_setting_innovation") or [],
        "reader_takeaway": clean_text(innov.get("reader_takeaway"), 220),
    }


def fallback_research_directions(papers: List[Dict[str, Any]], innovations: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    if not papers:
        return {"directions": []}

    groups: Dict[str, List[Dict[str, Any]]] = {}
    for paper in papers:
        tags = clean_text(paper.get("tags"))
        label = "综合医学 AI 方向"
        if tags:
            label = re.split(r"[,;，；]\s*", tags)[0].strip() or label
            label = re.sub(r"^(query|source|topic):", "", label, flags=re.IGNORECASE).strip() or label
        groups.setdefault(label, []).append(paper)

    directions: List[Dict[str, Any]] = []
    for label, items in groups.items():
        paper_ids = [str(p.get("paper_id") or "").strip() for p in items if str(p.get("paper_id") or "").strip()]
        contributions = [
            clean_text((innovations.get(pid) or {}).get("one_sentence_contribution"), 180)
            for pid in paper_ids
        ]
        contributions = [x for x in contributions if x]
        directions.append(
            {
                "name": label,
                "summary": f"该方向包含 {len(items)} 篇论文，建议结合单篇创新点进一步细分子问题。",
                "paper_ids": paper_ids,
                "shared_innovations": contributions[:4] or ["当前信息不足，需结合摘要和论文正文进一步归纳共同创新。"],
                "open_gaps": [
                    "现有工作之间的评测协议、数据集和临床适用边界可能尚未统一。",
                    "需要进一步确认方法在真实场景、跨中心数据或外部验证集上的稳定性。",
                ],
                "innovation_routes": [
                    {
                        "route_name": "统一评测与误差分解",
                        "idea": "把同方向论文放到统一任务、统一指标和统一错误类型下比较，寻找稳定短板。",
                        "why_promising": "同方向论文往往各自验证，统一评测能暴露可继续推进的真实问题。",
                        "possible_experiment": "复现或复用公开结果，构建共享测试集，按失败类型进行分层统计。",
                        "risk": "不同论文的数据和任务定义不一致，可能需要较多人工清洗。",
                    },
                    {
                        "route_name": "方法组合与轻量增强",
                        "idea": "抽取该方向中互补的模块，例如解释、校准、隐私、效率或多智能体协作，组合成更完整方案。",
                        "why_promising": "单篇论文通常只优化一个环节，模块组合可能带来更强的系统效果。",
                        "possible_experiment": "选择一个强基线，逐步加入互补模块并做消融实验。",
                        "risk": "模块叠加可能增加复杂度，收益未必线性增长。",
                    },
                ],
            }
        )
    return {"directions": directions}


def build_research_directions(client: SimpleLLMClient | None, papers: List[Dict[str, Any]], innovations: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    if not papers:
        return {"directions": []}
    if client is None:
        return fallback_research_directions(papers, innovations)

    items = [paper_compact_item(paper, innovations) for paper in papers]
    messages = [
        {
            "role": "system",
            "content": (
                "你是科研选题顾问。请把当天论文自动划分成若干研究方向，"
                "并在每个方向内进行二次创新路线开发。请用中文，避免空泛，"
                "每条路线都要包含想法、为什么有潜力、可做实验和风险。"
            ),
        },
        {
            "role": "user",
            "content": (
                "下面是当天论文和单篇创新点。请完成：\n"
                "1. 自动划分 2-8 个研究方向；论文少时可以少于 2 个。\n"
                "2. 每篇论文归入最相关的方向，必要时可少量交叉，但不要过度重复。\n"
                "3. 每个方向给出共同创新、未解决问题和 2-4 条二次创新路线。\n\n"
                + json.dumps(items, ensure_ascii=False, indent=2)
            ),
        },
    ]
    try:
        parsed = call_structured(client, messages, "research_directions", DIRECTIONS_SCHEMA, 5000)
        if parsed and isinstance(parsed.get("directions"), list):
            return parsed
    except Exception as exc:
        log(f"[WARN] LLM research directions failed: {exc}")
    return fallback_research_directions(papers, innovations)


def md_escape_table(text: Any) -> str:
    return clean_text(text).replace("|", "\\|")


def paper_link(paper: Dict[str, Any]) -> str:
    pid = normalize_paper_id(paper.get("paper_id") or paper.get("id"))
    source = str(paper.get("source") or "").strip().lower()
    if source == "biorxiv":
        return str(paper.get("pdf") or "").strip() or f"https://www.biorxiv.org/content/{pid}"
    if pid:
        return f"https://arxiv.org/abs/{pid}"
    return str(paper.get("pdf") or "").strip()


def render_markdown(date_str: str, papers: List[Dict[str, Any]], innovations: Dict[str, Dict[str, Any]], synthesis: Dict[str, Any]) -> str:
    label = format_date(date_str)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines: List[str] = [
        f"# 创新点总结 · {label}",
        "",
        f"- 生成时间：{generated_at}",
        f"- 当日论文数：{len(papers)}",
        "",
    ]

    if not papers:
        lines.extend(["## 今日趋势", "今日无新推荐，暂未生成创新点总结。", ""])
        return "\n".join(lines).rstrip() + "\n"

    trends = [clean_text(x, 220) for x in synthesis.get("daily_trends") or [] if clean_text(x)]
    lines.append("## 今日趋势")
    if trends:
        lines.extend([f"- {item}" for item in trends])
    else:
        lines.append("- 今日论文较少，暂无稳定趋势判断。")
    lines.append("")

    worth = synthesis.get("most_worth_reading") or []
    worth_by_id = {normalize_paper_id(item.get("paper_id")): clean_text(item.get("reason"), 180) for item in worth if isinstance(item, dict)}
    if worth_by_id:
        lines.extend(["## 最值得先读", "", "| 论文 | 推荐理由 |", "|---|---|"])
        by_id = {str(p.get("paper_id") or ""): p for p in papers}
        for pid, reason in worth_by_id.items():
            paper = by_id.get(pid)
            if not paper:
                continue
            title = md_escape_table(paper.get("title_en") or paper.get("title") or pid)
            link = paper_link(paper)
            title_md = f"[{title}]({link})" if link else title
            lines.append(f"| {title_md} | {md_escape_table(reason)} |")
        lines.append("")

    lines.append("## 单篇创新点")
    lines.append("")
    for idx, paper in enumerate(papers, start=1):
        pid = str(paper.get("paper_id") or "")
        innov = innovations.get(pid) or fallback_innovation(paper)
        title = clean_text(paper.get("title_en") or paper.get("title") or pid)
        link = paper_link(paper)
        section = str(paper.get("section") or "").strip()
        score = clean_text(paper.get("score") or paper.get("llm_score"))
        meta_parts = [part for part in [f"区域：{section}" if section else "", f"分数：{score}" if score else ""] if part]

        lines.append(f"### {idx}. {title}")
        if meta_parts:
            lines.append(f"- {'；'.join(meta_parts)}")
        if link:
            lines.append(f"- 原文链接：{link}")
        lines.append(f"- 一句话贡献：{clean_text(innov.get('one_sentence_contribution'), 260)}")
        lines.append("- 核心创新点：")
        tech = [clean_text(x, 180) for x in innov.get("technical_innovations") or [] if clean_text(x)]
        setting = [clean_text(x, 180) for x in innov.get("problem_setting_innovation") or [] if clean_text(x)]
        evidence = [clean_text(x, 180) for x in innov.get("evidence_or_result_innovation") or [] if clean_text(x)]
        for item in (tech + setting + evidence)[:5]:
            lines.append(f"  - {item}")
        lines.append(f"- 和已有工作的区别：{clean_text(innov.get('difference_from_prior_work'), 260)}")
        lines.append(f"- 阅读启发：{clean_text(innov.get('reader_takeaway'), 260)}")
        lines.append(f"- 可信度：{clean_text(innov.get('confidence')) or 'medium'}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_research_directions_markdown(
    date_str: str,
    papers: List[Dict[str, Any]],
    innovations: Dict[str, Dict[str, Any]],
    directions_payload: Dict[str, Any],
) -> str:
    label = format_date(date_str)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    directions = [d for d in directions_payload.get("directions") or [] if isinstance(d, dict)]
    paper_by_id = {str(p.get("paper_id") or "").strip(): p for p in papers}

    lines: List[str] = [
        f"# 研究方向与二次创新路线 · {label}",
        "",
        f"- 生成时间：{generated_at}",
        f"- 当日论文数：{len(papers)}",
        f"- 方向数：{len(directions)}",
        "",
    ]

    if not papers:
        lines.extend(["## 今日方向总览", "今日无新推荐，暂未生成研究方向。", ""])
        return "\n".join(lines).rstrip() + "\n"

    lines.extend(["## 今日方向总览", "", "| 方向 | 论文数 | 代表论文 |", "|---|---:|---|"])
    for direction in directions:
        name = md_escape_table(direction.get("name") or "未命名方向")
        paper_ids = [normalize_paper_id(x) for x in direction.get("paper_ids") or []]
        titles = []
        for pid in paper_ids[:3]:
            paper = paper_by_id.get(pid)
            if paper:
                titles.append(md_escape_table(paper.get("title_en") or paper.get("title") or pid))
        lines.append(f"| {name} | {len([pid for pid in paper_ids if pid])} | {'<br>'.join(titles) or '-'} |")
    lines.append("")

    for idx, direction in enumerate(directions, start=1):
        name = clean_text(direction.get("name") or f"方向 {idx}")
        summary = clean_text(direction.get("summary"), 500)
        paper_ids = [normalize_paper_id(x) for x in direction.get("paper_ids") or [] if normalize_paper_id(x)]
        lines.append(f"## 方向 {idx}：{name}")
        if summary:
            lines.append(summary)
            lines.append("")

        lines.extend(["### 代表论文", ""])
        if paper_ids:
            for pid in paper_ids:
                paper = paper_by_id.get(pid)
                if not paper:
                    continue
                title = clean_text(paper.get("title_en") or paper.get("title") or pid)
                link = paper_link(paper)
                contribution = clean_text((innovations.get(pid) or {}).get("one_sentence_contribution"), 220)
                title_md = f"[{title}]({link})" if link else title
                if contribution:
                    lines.append(f"- {title_md}：{contribution}")
                else:
                    lines.append(f"- {title_md}")
        else:
            lines.append("- 暂无明确归属论文。")
        lines.append("")

        shared = [clean_text(x, 260) for x in direction.get("shared_innovations") or [] if clean_text(x)]
        lines.append("### 共同创新点")
        if shared:
            lines.extend([f"- {item}" for item in shared])
        else:
            lines.append("- 暂无稳定共同创新点。")
        lines.append("")

        gaps = [clean_text(x, 260) for x in direction.get("open_gaps") or [] if clean_text(x)]
        lines.append("### 尚未解决的问题")
        if gaps:
            lines.extend([f"- {item}" for item in gaps])
        else:
            lines.append("- 需要结合全文和实验设置进一步判断。")
        lines.append("")

        routes = [r for r in direction.get("innovation_routes") or [] if isinstance(r, dict)]
        lines.append("### 二次创新路线")
        if not routes:
            lines.append("- 暂无可用路线。")
            lines.append("")
            continue
        for route_idx, route in enumerate(routes, start=1):
            route_name = clean_text(route.get("route_name") or f"路线 {route_idx}", 120)
            lines.append(f"#### 路线 {route_idx}：{route_name}")
            idea = clean_text(route.get("idea"), 360)
            why = clean_text(route.get("why_promising"), 300)
            experiment = clean_text(route.get("possible_experiment"), 320)
            risk = clean_text(route.get("risk"), 260)
            if idea:
                lines.append(f"- 核心想法：{idea}")
            if why:
                lines.append(f"- 为什么值得做：{why}")
            if experiment:
                lines.append(f"- 可验证实验：{experiment}")
            if risk:
                lines.append(f"- 主要风险：{risk}")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def insert_link_into_day_readme(day_readme: str) -> bool:
    if not os.path.exists(day_readme):
        return False
    try:
        with open(day_readme, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return False
    link_lines = [
        "- [今日创新点总结](innovation-brief.md)",
        "- [研究方向与二次创新路线](research-directions.md)",
    ]
    missing = [line for line in link_lines if line not in content]
    if not missing:
        return False
    marker = "## 今日简报（AI）"
    insert_text = "\n".join(missing)
    if marker in content:
        updated = content.replace(marker, f"{insert_text}\n\n{marker}", 1)
    else:
        lines = content.splitlines()
        if lines and lines[0].startswith("# "):
            lines.insert(1, "")
            for offset, line in enumerate(missing):
                lines.insert(2 + offset, line)
            updated = "\n".join(lines) + ("\n" if content.endswith("\n") else "")
        else:
            updated = insert_text + "\n\n" + content
    with open(day_readme, "w", encoding="utf-8") as f:
        f.write(updated)
    return True


def sidebar_href_for_date_token(date_token: str) -> str:
    if RANGE_DATE_RE.match(date_token):
        return f"#/{date_token}/innovation-brief"
    return f"#/{date_token[:6]}/{date_token[6:]}/innovation-brief"


def directions_href_for_date_token(date_token: str) -> str:
    if RANGE_DATE_RE.match(date_token):
        return f"#/{date_token}/research-directions"
    return f"#/{date_token[:6]}/{date_token[6:]}/research-directions"


def collect_existing_innovation_briefs(docs_dir: str) -> List[Dict[str, str]]:
    entries: List[Dict[str, str]] = []
    if not os.path.isdir(docs_dir):
        return entries

    for name in os.listdir(docs_dir):
        top_path = os.path.join(docs_dir, name)
        if not os.path.isdir(top_path):
            continue
        if RANGE_DATE_RE.match(name):
            brief_path = os.path.join(top_path, "innovation-brief.md")
            if os.path.exists(brief_path):
                directions_path = os.path.join(top_path, "research-directions.md")
                entries.append(
                    {
                        "token": name,
                        "label": format_date(name),
                        "href": sidebar_href_for_date_token(name),
                        "directions_href": directions_href_for_date_token(name),
                        "has_directions": "1" if os.path.exists(directions_path) else "",
                    }
                )
            continue
        if not re.match(r"^\d{6}$", name):
            continue
        for day in os.listdir(top_path):
            if not re.match(r"^\d{2}$", day):
                continue
            token = f"{name}{day}"
            brief_path = os.path.join(top_path, day, "innovation-brief.md")
            if os.path.exists(brief_path):
                directions_path = os.path.join(top_path, day, "research-directions.md")
                entries.append(
                    {
                        "token": token,
                        "label": format_date(token),
                        "href": sidebar_href_for_date_token(token),
                        "directions_href": directions_href_for_date_token(token),
                        "has_directions": "1" if os.path.exists(directions_path) else "",
                    }
                )

    entries.sort(key=lambda item: item["token"], reverse=True)
    return entries


def ensure_sidebar_innovation_links(docs_dir: str) -> bool:
    entries = collect_existing_innovation_briefs(docs_dir)
    if not entries:
        return False

    sidebar_path = os.path.join(docs_dir, "_sidebar.md")
    if os.path.exists(sidebar_path):
        with open(sidebar_path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
    else:
        lines = [
            '* <a class="dpr-sidebar-root-link" href="#/">首页</a>',
            "* Daily Papers",
        ]

    changed = False
    original_lines = list(lines)

    def line_date_token(line: str) -> str:
        text = line.strip()
        if not text.startswith("* "):
            return ""
        marker = re.search(r"<!--\s*dpr-date:(\d{8}(?:-\d{8})?)\s*-->", text)
        if marker:
            return marker.group(1)
        label = text[2:].strip()
        label = re.sub(r"\s*<!--.*?-->\s*", "", label).strip()
        range_match = re.match(r"^(\d{4})-(\d{2})-(\d{2})\s+~\s+(\d{4})-(\d{2})-(\d{2})$", label)
        if range_match:
            y1, m1, d1, y2, m2, d2 = range_match.groups()
            return f"{y1}{m1}{d1}-{y2}{m2}{d2}"
        single_match = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", label)
        if single_match:
            y, m, d = single_match.groups()
            return f"{y}{m}{d}"
        return ""

    def is_date_line(line: str) -> bool:
        return bool(line_date_token(line))

    def date_label_from_line(line: str) -> str:
        text = line.strip()
        if not text.startswith("* "):
            return ""
        text = re.sub(r"\s*<!--.*?-->\s*", "", text[2:]).strip()
        return text

    def make_date_line(entry: Dict[str, str]) -> str:
        token = entry["token"]
        return f"  * {entry['label']} <!--dpr-date:{token}-->"

    def indent_level(line: str) -> int:
        return len(line) - len(line.lstrip(" "))

    def is_section_heading(line: str) -> bool:
        stripped = line.strip()
        return stripped in {"* 精读区", "* 速读区"} and indent_level(line) >= 4

    def is_empty_innovation_date_block(idx: int, current_lines: List[str]) -> bool:
        if not current_lines[idx].startswith("  * ") or not is_date_line(current_lines[idx]):
            return False
        next_idx = idx + 1
        if next_idx >= len(current_lines) or not current_lines[next_idx].startswith("    * "):
            return False
        if "innovation-brief" not in current_lines[next_idx]:
            return False
        after_idx = next_idx + 1
        return after_idx >= len(current_lines) or not current_lines[after_idx].startswith("    * ")

    def has_child(idx: int, current_lines: List[str]) -> bool:
        return idx + 1 < len(current_lines) and current_lines[idx + 1].startswith("    * ")

    # Rebuild custom entries each run. This avoids duplicate date blocks and
    # keeps old innovation links after the upstream sidebar is regenerated.
    lines = [
        line
        for line in lines
        if "innovation-brief" not in line and "research-directions" not in line
    ]
    tokens_with_children = {
        line_date_token(line)
        for idx, line in enumerate(lines)
        if line.startswith("  * ") and line_date_token(line) and has_child(idx, lines)
    }
    pruned: List[str] = []
    for idx, line in enumerate(lines):
        token = line_date_token(line)
        if (
            line.startswith("  * ")
            and token
            and not has_child(idx, lines)
            and token in tokens_with_children
        ):
            changed = True
            continue
        pruned.append(line)
    lines = pruned
    if lines != original_lines:
        changed = True

    if not any(line.strip() == "* Daily Papers" for line in lines):
        lines.append("* Daily Papers")
        changed = True

    def find_date_line(label: str) -> int:
        target_token = ""
        for entry in entries:
            if entry["label"] == label:
                target_token = entry["token"]
                break
        candidates: List[int] = []
        for idx, line in enumerate(lines):
            if line.startswith("  * ") and line_date_token(line) == target_token:
                candidates.append(idx)
        if not candidates:
            target = f"  * {label}"
            for idx, line in enumerate(lines):
                if re.sub(r"\s*<!--.*?-->\s*", "", line).rstrip() == target:
                    candidates.append(idx)
        if not candidates:
            return -1
        for idx in candidates:
            if has_child(idx, lines) and not is_empty_innovation_date_block(idx, lines):
                return idx
        return candidates[0]

    daily_idx = next((idx for idx, line in enumerate(lines) if line.strip() == "* Daily Papers"), len(lines) - 1)

    for entry in entries:
        label = entry["label"]
        href = entry["href"]
        link_lines = [f'    * <a class="dpr-sidebar-item-link" href="{href}">创新点总结</a>']
        if entry.get("has_directions"):
            link_lines.append(
                f'    * <a class="dpr-sidebar-item-link" href="{entry["directions_href"]}">研究方向与路线</a>'
            )

        date_idx = find_date_line(label)
        if date_idx < 0:
            insert_idx = daily_idx + 1
            lines.insert(insert_idx, make_date_line(entry))
            for offset, line in enumerate(link_lines):
                lines.insert(insert_idx + 1 + offset, line)
            changed = True
            continue

        insert_idx = date_idx + 1
        while insert_idx < len(lines) and lines[insert_idx].startswith("    * ") and is_section_heading(lines[insert_idx]):
            # Keep the innovation brief before section headings like 精读区.
            break
        for offset, line in enumerate(link_lines):
            lines.insert(insert_idx + offset, line)
        changed = True

    if changed:
        with open(sidebar_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines).rstrip() + "\n")
    return changed


def main() -> None:
    parser = argparse.ArgumentParser(description="Step 7: generate daily innovation brief.")
    parser.add_argument("--date", type=str, default=TODAY_STR, help="date string YYYYMMDD, range token, or latest.")
    parser.add_argument("--mode", type=str, default=None, help="recommend mode.")
    parser.add_argument("--docs-dir", type=str, default=None, help="override docs dir.")
    parser.add_argument("--no-llm", action="store_true", help="generate fallback brief without calling LLM.")
    args = parser.parse_args()

    mode = args.mode or resolve_mode()
    docs_dir = args.docs_dir or resolve_docs_dir()
    date_arg = str(args.date or "").strip()
    date_str = resolve_latest_date_token(docs_dir) if date_arg.lower() == "latest" else (date_arg or TODAY_STR)
    target_dir = day_dir_for(docs_dir, date_str)
    os.makedirs(target_dir, exist_ok=True)

    recommend_by_id = collect_recommend_papers(date_str, mode)
    meta_papers = collect_meta_papers(docs_dir, date_str)
    papers = merge_paper_records(meta_papers, recommend_by_id)

    client = None
    if not args.no_llm and BLT_API_KEY:
        client = SimpleLLMClient(api_key=BLT_API_KEY, model=BLT_MODEL)
    elif not args.no_llm:
        log("[WARN] 未配置 BLT_API_KEY，使用基础版创新点总结。")

    innovations: Dict[str, Dict[str, Any]] = {}
    for index, paper in enumerate(papers, start=1):
        pid = str(paper.get("paper_id") or "").strip()
        if not pid:
            continue
        log(f"[INFO] innovation summary {index}/{len(papers)}: {pid}")
        innovations[pid] = summarize_paper(client, paper)

    synthesis = build_daily_synthesis(client, papers, innovations)
    markdown = render_markdown(date_str, papers, innovations, synthesis)
    directions_payload = build_research_directions(client, papers, innovations)
    directions_markdown = render_research_directions_markdown(
        date_str,
        papers,
        innovations,
        directions_payload,
    )

    out_path = os.path.join(target_dir, "innovation-brief.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(markdown)
    log(f"[OK] innovation brief saved: {out_path}")

    directions_path = os.path.join(target_dir, "research-directions.md")
    with open(directions_path, "w", encoding="utf-8") as f:
        f.write(directions_markdown)
    log(f"[OK] research directions saved: {directions_path}")

    day_readme = os.path.join(target_dir, "README.md")
    if insert_link_into_day_readme(day_readme):
        log(f"[OK] day README linked: {day_readme}")
    if ensure_sidebar_innovation_links(docs_dir):
        log(f"[OK] sidebar innovation links updated: {os.path.join(docs_dir, '_sidebar.md')}")


if __name__ == "__main__":
    main()
