#!/usr/bin/env python3
"""
Fetch tech/AI news from X/Twitter via Nitter RSS feeds and translate to Chinese.
"""

import argparse
import json
import sys
import re
from datetime import datetime, timedelta
from xml.etree import ElementTree as ET
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
import time
import subprocess
import tempfile
import os

# Default tech/AI accounts to monitor
DEFAULT_ACCOUNTS = [
    "OpenAI",
    "AnthropicAI",
    "GoogleAI",
    "GoogleDeepMind",  # Fixed: was "DeepMind"
    "OpenAIDevs",
    "sama",
    "ylecun",
    "karpathy",
    "DrJimFan",
    "AndrewYNg",
    "goodside",  # AI researcher
    "bindureddy",  # AI founder
    "hardmaru",  # AI researcher
    "newsycombinator",  # Hacker News official
    "TechCrunch",  # Tech news
    "verge",  # Tech news
]

# Nitter instances to try (in order)
NITTER_INSTANCES = [
    "https://nitter.net",
    "https://nitter.cz",
    "https://nitter.privacydev.net",
    "https://nitter.space",
    "https://nitter.poast.org",
]

# Keywords for filtering AI/tech content
AI_KEYWORDS = [
    "AI", "artificial intelligence", "machine learning", "ML", "LLM", "GPT",
    "ChatGPT", "Claude", "OpenAI", "Anthropic", "Gemini", "Copilot",
    "Midjourney", "Stable Diffusion", "DALL-E", "model", "training",
    "fine-tuning", "inference", "token", "parameter", "neural",
]

TECH_KEYWORDS = [
    "tech", "technology", "startup", "funding", "product launch", "API",
    "software", "hardware", "silicon", "chip", "GPU", "TPU", "release",
    "announcement", "update", "beta", "launch", "ship",
]


def fetch_rss(nitter_instance: str, username: str, timeout: int = 30) -> str:
    """Fetch RSS feed for a given username from a Nitter instance."""
    url = f"{nitter_instance}/{username}/rss"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.0"
    }

    try:
        req = Request(url, headers=headers)
        with urlopen(req, timeout=timeout) as response:
            return response.read().decode("utf-8")
    except (HTTPError, URLError) as e:
        raise Exception(f"Failed to fetch {url}: {e}")


def parse_rss(rss_content: str, username: str) -> list:
    """Parse RSS XML content and extract tweets."""
    tweets = []

    try:
        root = ET.fromstring(rss_content)

        # RSS 2.0 format
        for item in root.findall(".//item"):
            title = item.findtext("title", "")
            link = item.findtext("link", "")
            pub_date = item.findtext("pubDate", "")
            description = item.findtext("description", "")

            tweets.append({
                "username": username,
                "content": title,
                "link": link,
                "published": pub_date,
                "description": description,
            })
    except ET.ParseError as e:
        print(f"Error parsing RSS for {username}: {e}", file=sys.stderr)

    return tweets


def is_tech_or_ai_related(tweet: dict) -> bool:
    """Check if tweet is related to AI or tech."""
    content = tweet.get("content", "").lower()
    all_keywords = [k.lower() for k in AI_KEYWORDS + TECH_KEYWORDS]

    return any(keyword in content for keyword in all_keywords)


def categorize_tweets(tweets: list) -> dict:
    """Categorize tweets by topic."""
    categories = {
        "模型发布": [],
        "产品更新": [],
        "研究进展": [],
        "安全/对齐": [],
        "行业动态": [],
        "其他": []
    }

    # Category keywords
    model_keywords = ["gpt", "claude", "llm", "model", "release", "launch", "available", "发布", "推出", "模型"]
    product_keywords = ["chatgpt", "codex", "api", "feature", "product", "app", "功能", "产品", "更新"]
    research_keywords = ["research", "paper", "study", "arxiv", "benchmark", "研究", "论文", "实验"]
    safety_keywords = ["safety", "alignment", "security", "guardrails", "eval", "安全", "对齐", "评估"]
    industry_keywords = ["funding", "startup", "acquisition", "raised", "million", "billion", "收购", "融资", "投资"]

    for tweet in tweets:
        content = tweet.get("content", "").lower()

        if any(kw in content for kw in model_keywords):
            categories["模型发布"].append(tweet)
        elif any(kw in content for kw in product_keywords):
            categories["产品更新"].append(tweet)
        elif any(kw in content for kw in research_keywords):
            categories["研究进展"].append(tweet)
        elif any(kw in content for kw in safety_keywords):
            categories["安全/对齐"].append(tweet)
        elif any(kw in content for kw in industry_keywords):
            categories["行业动态"].append(tweet)
        else:
            categories["其他"].append(tweet)

    # Remove empty categories
    return {k: v for k, v in categories.items() if v}


def generate_summary(tweets: list) -> str:
    """Generate a brief summary of the tweets."""
    if not tweets:
        return "暂无相关动态。"

    # Count by account
    account_counts = {}
    for t in tweets:
        acc = t.get("username", "Unknown")
        account_counts[acc] = account_counts.get(acc, 0) + 1

    top_accounts = sorted(account_counts.items(), key=lambda x: x[1], reverse=True)[:3]

    # Find trending topics (simple word frequency)
    all_text = " ".join(t.get("content", "").lower() for t in tweets)
    topic_keywords = ["gpt", "claude", "openai", "anthropic", "model", "ai", "research", "code", "api"]
    trending = [kw for kw in topic_keywords if kw in all_text]
    trending = list(set(trending))[:5]  # Unique, max 5

    summary_parts = [
        f"共获取 {len(tweets)} 条相关动态",
        f"主要来自: {', '.join(f'@{acc}({cnt}条)' for acc, cnt in top_accounts)}",
    ]
    if trending:
        summary_parts.append(f"热门话题: {', '.join(trending)}")

    return " | ".join(summary_parts)


def fetch_with_fallback(username: str, max_retries: int = 3) -> list:
    """Try multiple Nitter instances until one works."""
    errors = []

    for instance in NITTER_INSTANCES:
        for attempt in range(max_retries):
            try:
                rss_content = fetch_rss(instance, username)
                tweets = parse_rss(rss_content, username)
                return tweets
            except Exception as e:
                errors.append(f"{instance}: {e}")
                if attempt < max_retries - 1:
                    time.sleep(1)  # Brief delay before retry
                continue

    # All instances failed
    print(f"Failed to fetch {username} from all instances:", file=sys.stderr)
    for error in errors:
        print(f"  {error}", file=sys.stderr)
    return []


def main():
    parser = argparse.ArgumentParser(
        description="Fetch tech/AI news from X/Twitter via Nitter RSS"
    )
    parser.add_argument(
        "accounts",
        nargs="*",
        help="X/Twitter accounts to fetch (default: built-in list)",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output file (default: stdout)",
    )
    parser.add_argument(
        "--filter",
        "-f",
        action="store_true",
        help="Filter for AI/tech related tweets only",
    )
    parser.add_argument(
        "--limit",
        "-l",
        type=int,
        default=50,
        help="Maximum tweets per account (default: 50)",
    )
    parser.add_argument(
        "--days",
        "-d",
        type=int,
        default=1,
        help="Only include tweets from last N days (default: 1)",
    )
    parser.add_argument(
        "--json",
        "-j",
        action="store_true",
        help="Output as JSON instead of markdown",
    )
    parser.add_argument(
        "--translate",
        "-t",
        action="store_true",
        help="Add translation markers for Claude to translate content",
    )

    args = parser.parse_args()

    accounts = args.accounts if args.accounts else DEFAULT_ACCOUNTS

    all_tweets = []

    for account in accounts:
        print(f"Fetching {account}...", file=sys.stderr)
        tweets = fetch_with_fallback(account)

        if tweets:
            all_tweets.extend(tweets[:args.limit])
            print(f"  Got {len(tweets[:args.limit])} tweets", file=sys.stderr)
        else:
            print(f"  No tweets fetched", file=sys.stderr)

    # Filter for AI/tech content if requested
    if args.filter:
        all_tweets = [t for t in all_tweets if is_tech_or_ai_related(t)]

    # Output results
    if args.json:
        output = json.dumps(all_tweets, indent=2, ensure_ascii=False)
    else:
        # Generate intelligent markdown summary
        categories = categorize_tweets(all_tweets)
        summary = generate_summary(all_tweets)

        lines = [
            f"# X 科技动态摘要 - {datetime.now().strftime('%Y年%m月%d日')}",
            "",
            f"> {summary}",
            "",
            f"**数据来源**: {', '.join(f'@{a}' for a in accounts)}",
            "",
            "---",
            "",
        ]

        # Add categorized sections
        for category, tweets in categories.items():
            if tweets:
                lines.append(f"## {category}")
                lines.append("")

                for tweet in tweets[:10]:  # Limit to 10 per category
                    lines.append(f"**@{tweet['username']}**  {tweet['content'][:200]}{'...' if len(tweet['content']) > 200 else ''}")
                    if tweet.get('link'):
                        lines.append(f"[查看原文]({tweet['link']})")
                    lines.append("")

        output = "\n".join(lines)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"\nSaved to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
