#!/usr/bin/env python3
"""
Fetch macro news from various financial sources.
Supports RSS feeds and direct web scraping.
"""

import json
import re
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from urllib.parse import urljoin
import xml.etree.ElementTree as ET

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    requests = None
    BeautifulSoup = None


# RSS Feed sources
RSS_SOURCES = {
    "reuters_markets": "https://www.reuters.com/markets/rss/",
    "cnbc_finance": "https://www.cnbc.com/id/10000664/device/rss/rss.html",
    "yahoo_finance": "https://finance.yahoo.com/news/rssindex",
    "investing_news": "https://www.investing.com/rss/news.rss",
}

# Keywords for categorization
KEYWORDS = {
    "fed": ["fed", "federal reserve", "fomc", "interest rate", "powell", "rate cut", "rate hike"],
    "inflation": ["cpi", "ppi", "inflation", "deflation", "price index", "consumer price", "producer price"],
    "employment": ["jobs", "employment", "unemployment", "payroll", "nfp", "nonfarm", "labor market"],
    "geopolitics": ["war", "conflict", "sanctions", "trade war", "tariff", "diplomatic", "biden", "trump", "white house"],
    "trade": ["trade", "import", "export", "ustr", "trade agreement", "wto"],
}


def fetch_rss_feed(url: str) -> List[Dict]:
    """Fetch and parse RSS feed."""
    if requests is None:
        return []

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        # Parse RSS
        root = ET.fromstring(response.content)

        items = []
        # Handle both RSS 2.0 and Atom formats
        for item in root.iter("item"):
            title = item.find("title")
            link = item.find("link")
            pub_date = item.find("pubDate")
            description = item.find("description")

            items.append({
                "title": title.text if title is not None else "",
                "link": link.text if link is not None else "",
                "pub_date": pub_date.text if pub_date is not None else "",
                "description": description.text if description is not None else "",
            })

        return items
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []


def categorize_news(title: str, description: str = "") -> List[str]:
    """Categorize news based on keywords."""
    text = (title + " " + description).lower()
    categories = []

    for category, keywords in KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            categories.append(category)

    return categories if categories else ["general"]


def fetch_all_news() -> Dict[str, List[Dict]]:
    """Fetch news from all sources."""
    all_news = {
        "fed": [],
        "inflation": [],
        "employment": [],
        "geopolitics": [],
        "trade": [],
        "general": [],
    }

    for source_name, url in RSS_SOURCES.items():
        items = fetch_rss_feed(url)

        for item in items:
            categories = categorize_news(item["title"], item.get("description", ""))
            item["source"] = source_name

            for category in categories:
                if category in all_news:
                    all_news[category].append(item)

    return all_news


def deduplicate_news(news_list: List[Dict]) -> List[Dict]:
    """Remove duplicate news based on title similarity."""
    seen = set()
    unique = []

    for item in news_list:
        # Use first 50 chars of normalized title as key
        key = re.sub(r'\W+', '', item["title"].lower())[:50]
        if key not in seen:
            seen.add(key)
            unique.append(item)

    return unique


if __name__ == "__main__":
    news = fetch_all_news()

    # Deduplicate each category
    for category in news:
        news[category] = deduplicate_news(news[category])

    # Output as JSON
    print(json.dumps(news, ensure_ascii=False, indent=2))
