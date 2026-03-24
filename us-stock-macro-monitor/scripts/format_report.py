#!/usr/bin/env python3
"""
Format macro news and data into a structured Markdown report.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional


def format_indicator_table(indicators: Dict) -> str:
    """Format economic indicators as a markdown table."""
    rows = [
        "| 指标 | 当前值 | 日变化 | 解读 |",
        "|-----|-------|-------|------|",
    ]

    indicator_names = {
        "VIXCLS": "VIX 恐慌指数",
        "DTWEXBGS": "美元指数",
        "DGS10": "10年期美债收益率",
        "DGS2": "2年期美债收益率",
        "DFF": "联邦基金利率",
        "UNRATE": "失业率",
    }

    for series_id, data in indicators.items():
        name = indicator_names.get(series_id, data.get("name", series_id))
        value = data.get("value", "N/A")
        change = data.get("change")

        if change is not None:
            change_str = f"+{change:.2f}" if change > 0 else f"{change:.2f}"
        else:
            change_str = "-"

        # Simple interpretation
        interpretation = get_indicator_interpretation(series_id, data.get("current_value"))

        rows.append(f"| {name} | {value} | {change_str} | {interpretation} |")

    return "\n".join(rows)


def get_indicator_interpretation(indicator: str, value: Optional[float]) -> str:
    """Get a brief interpretation of the indicator value."""
    if value is None:
        return "数据不可用"

    if indicator == "VIXCLS":
        if value > 30:
            return "高波动性/恐慌"
        elif value > 20:
            return "中等波动"
        else:
            return "低波动/平静"
    elif indicator in ["DGS10", "DGS2"]:
        if value > 5:
            return "高利率环境"
        elif value > 3:
            return "中等利率"
        else:
            return "低利率环境"
    elif indicator == "DTWEXBGS":
        if value > 105:
            return "强势美元"
        elif value < 95:
            return "弱势美元"
        else:
            return "美元中性"
    elif indicator == "UNRATE":
        if value > 6:
            return "高失业率"
        elif value < 4:
            return "充分就业"
        else:
            return "就业稳定"

    return "-"


def format_fedwatch_table(probabilities: List[Dict]) -> str:
    """Format CME FedWatch probabilities."""
    if not probabilities:
        return "暂无 FedWatch 数据"

    rows = [
        "| 会议日期 | 维持利率 | 加息25bp | 降息25bp |",
        "|---------|---------|---------|---------|",
    ]

    for prob in probabilities[:5]:  # Show next 5 meetings
        date = prob.get("meeting_date", "-")
        hold = prob.get("hold_prob", "-")
        hike = prob.get("hike_prob", "-")
        cut = prob.get("cut_prob", "-")
        rows.append(f"| {date} | {hold} | {hike} | {cut} |")

    return "\n".join(rows)


def format_news_section(news_items: List[Dict], max_items: int = 5) -> str:
    """Format news items as markdown bullet points."""
    if not news_items:
        return "暂无相关新闻"

    lines = []
    for item in news_items[:max_items]:
        title = item.get("title", "")
        source = item.get("source", "")
        date = item.get("pub_date", "")
        description = item.get("description", "")
        link = item.get("link", "")

        # Clean up the description
        if description:
            description = description.strip()
            if len(description) > 200:
                description = description[:200] + "..."

        lines.append(f"- **{title}**")
        lines.append(f"  - 来源: {source} | {date}")
        if description:
            lines.append(f"  - {description}")
        if link:
            lines.append(f"  - [链接]({link})")
        lines.append("")

    return "\n".join(lines)


def generate_report(
    indicators: Dict,
    fedwatch: List[Dict],
    news: Dict[str, List[Dict]],
    title: Optional[str] = None,
) -> str:
    """Generate the full markdown report."""

    if title is None:
        title = f"美股宏观监控报告 - {datetime.now().strftime('%Y-%m-%d')}"

    sections = [
        f"# {title}",
        "",
        "## 关键指标速览",
        "",
        format_indicator_table(indicators),
        "",
        "## CME FedWatch 利率预测",
        "",
        format_fedwatch_table(fedwatch),
        "",
        "## 美联储动态",
        "",
        format_news_section(news.get("fed", [])),
        "",
        "## 通胀与就业",
        "",
        format_news_section(news.get("inflation", []) + news.get("employment", [])),
        "",
        "## 地缘政治与贸易政策",
        "",
        format_news_section(news.get("geopolitics", []) + news.get("trade", [])),
        "",
        "## 市场情绪",
        "",
        "_数据来源: TradingView, Polymarket_",
        "",
        "## 今日重点关注",
        "",
        "1. **请关注重要经济日历**",
        "   - 影响分析: 待更新",
        "   - 相关板块: 全市场",
        "",
        "2. **美联储官员讲话日程**",
        "   - 影响分析: 关注政策转向信号",
        "   - 相关板块: 金融、科技",
        "",
        "---",
        f"_报告生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_",
        "_免责声明: 本报告仅供参考，不构成投资建议_",
    ]

    return "\n".join(sections)


if __name__ == "__main__":
    # Example usage
    sample_indicators = {
        "VIXCLS": {"name": "VIX", "value": "18.50", "change": -1.2},
        "DTWEXBGS": {"name": "美元指数", "value": "102.30", "change": 0.5},
        "DGS10": {"name": "10年期美债", "value": "4.25%", "change": 0.05},
    }

    sample_news = {
        "fed": [
            {"title": "Fed signals potential rate cuts", "source": "Reuters", "pub_date": "Today"},
        ],
        "inflation": [
            {"title": "CPI data shows cooling inflation", "source": "Bloomberg", "pub_date": "Today"},
        ],
    }

    report = generate_report(sample_indicators, [], sample_news)
    print(report)
