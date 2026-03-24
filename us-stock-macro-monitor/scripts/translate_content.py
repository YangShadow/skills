#!/usr/bin/env python3
"""
Translate content to Simplified Chinese.
Preserves English technical terms, names, and acronyms.
"""

import re
from typing import List, Dict

# Terms to preserve in English
PRESERVE_TERMS = {
    # Fed/Monetary Policy
    "Fed", "FOMC", "Federal Reserve", "Fed Funds Rate",
    # Economic Indicators
    "CPI", "PPI", "GDP", "NFP", "Nonfarm Payrolls",
    "PCE", "Core PCE", "Inflation", "Deflation",
    # Market Terms
    "VIX", "SPX", "NDX", "DJI", "S&P 500", "Nasdaq", "Dow",
    "ETF", "Futures", "Options", "IPO",
    # Rates/Currency
    "USD", "DXY", "Treasury", "Yield", "Basis Points", "bps",
    # Institutions
    "Treasury", "White House", "USTR", "BLS", "Commerce Department",
    # Common names (will be matched case-insensitively)
    "Powell", "Biden", "Trump", "Yellen",
    # Other
    "AI", "API", "LLM", "GPT", "FedWatch",
}

# Create regex pattern for preserved terms (sorted by length, longest first)
sorted_terms = sorted(PRESERVE_TERMS, key=len, reverse=True)
PRESERVE_PATTERN = re.compile(
    r'\b(' + '|'.join(re.escape(term) for term in sorted_terms) + r')\b',
    re.IGNORECASE
)

# Simple translation dictionary for common financial phrases
# In production, this would call a translation API
SIMPLE_TRANSLATIONS = {
    "Federal Reserve": "美联储",
    "interest rate": "利率",
    "rate hike": "加息",
    "rate cut": "降息",
    "inflation": "通胀",
    "deflation": "通缩",
    "unemployment": "失业",
    "employment": "就业",
    "payroll": "就业人口",
    "trade war": "贸易战",
    "tariff": "关税",
    "sanctions": "制裁",
    "stock market": "股市",
    "bull market": "牛市",
    "bear market": "熊市",
    "recession": "衰退",
    "expansion": "扩张",
}


def detect_language(text: str) -> str:
    """Detect if text is primarily Chinese or English."""
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', text))
    total_chars = len(re.sub(r'\s', '', text))

    if total_chars == 0:
        return "unknown"

    ratio = chinese_chars / total_chars
    if ratio > 0.3:
        return "zh"
    return "en"


def translate_text(text: str) -> str:
    """
    Translate text to Simplified Chinese.
    This is a placeholder that marks text for translation.
    In actual use, Claude would perform the translation.
    """
    if not text:
        return text

    lang = detect_language(text)
    if lang == "zh":
        # Already Chinese, check if simplified
        return text

    # Mark for translation - actual translation done by Claude
    # Return with marker for post-processing
    return f"[TRANSLATE_TO_ZH]{text}[/TRANSLATE_TO_ZH]"


def translate_news_item(item: Dict) -> Dict:
    """Translate a news item to Chinese."""
    translated = item.copy()

    # Translate title and description
    if "title" in item:
        translated["title"] = translate_text(item["title"])
    if "description" in item:
        translated["description"] = translate_text(item["description"])

    return translated


def batch_translate(news_list: List[Dict]) -> List[Dict]:
    """Translate a list of news items."""
    return [translate_news_item(item) for item in news_list]


if __name__ == "__main__":
    # Test translation
    test_text = "Fed signals potential rate cuts amid cooling inflation"
    print(f"Original: {test_text}")
    print(f"Translated: {translate_text(test_text)}")
