---
name: x-tech-news
description: Fetch and summarize the latest tech news from x.com (Twitter), especially AI-related content. Use this skill when the user wants to get updates about technology trends, AI news, or social media tech discussions from X/Twitter. Triggers on phrases like "get X news", "Twitter tech updates", "latest AI news from X", "what's happening in tech on X", "x.com 科技动态", "推特 AI 新闻".
---

# X Tech News Fetcher

Fetch and summarize the latest technology and AI news from x.com (Twitter) using RSS feeds.

## How It Works

This skill uses RSS bridge services (like Nitter) to fetch public X/Twitter accounts' posts without requiring API keys.

## Supported RSS Sources

- **Nitter instances** - Primary RSS source for X/Twitter
  - nitter.net
  - nitter.cz
  - nitter.privacydev.net
  - (and other public instances)

## Usage

When user asks for X/Twitter tech news:

1. **Fetch RSS feeds** - Use the `scripts/fetch_x_news.py` script
2. **Parse and filter** - Extract tweets, filter by AI/tech keywords
3. **智能分类** - 自动按主题分类（模型发布、产品更新、研究进展、安全/对齐、行业动态）
4. **生成摘要** - 生成数据概览和热门话题
5. **翻译为中文** - 将所有推文内容翻译为中文简体，保留关键术语（如 GPT-5.4, Codex, API 等）不翻译
6. **Present** - Show formatted summary to user
7. **Save (optional)** - Save to file if requested

## Translation Guidelines

When translating tweets to Chinese:
- 保持技术术语英文：GPT-5.4, Claude, API, Codex, LLM 等
- 保持人名、公司名英文：OpenAI, Anthropic, Sam Altman 等
- 翻译口语化表达为自然中文
- 保留链接和引用标记
- 如果原文已经是中文或日文，保持原样

## Keywords for AI/Tech Filtering

AI-related: AI, artificial intelligence, machine learning, ML, LLM, GPT, ChatGPT, Claude, OpenAI, Anthropic, Gemini, Copilot, Midjourney, Stable Diffusion

Tech-related: tech, technology, startup, funding, product launch, API, software, hardware, silicon, chip, model release

## Auto-Categorization

Tweets are automatically categorized into:
- **模型发布** - New model releases (GPT, Claude, LLM updates)
- **产品更新** - Product features, ChatGPT, Codex, API updates
- **研究进展** - Research papers, studies, benchmarks
- **安全/对齐** - Safety, alignment, security evaluations
- **行业动态** - Funding, acquisitions, industry news
- **其他** - Uncategorized tech content

## Output Format

```markdown
# X Tech News Summary - [Date]

## AI/ML Highlights
- **[Account]**: [Summary of tweet and why it matters]
- **[Account]**: [Summary]

## Trending Topics
1. **[Topic]**: [Brief description with context]
2. **[Topic]**: [Brief description]

## Notable Discussions
- **[Account]**: "[Key quote or insight]"
  - [Engagement metrics if available]
```

## Implementation

Use the bundled script to fetch RSS:
```bash
python skills/x-tech-news/scripts/fetch_x_news.py [account1] [account2] ...
```

Or fetch RSS directly with WebFetch tool:
- Nitter RSS URL format: `https://nitter.net/[username]/rss`

## Default Accounts to Monitor

- @OpenAI
- @AnthropicAI
- @GoogleAI
- @DeepMind
- @OpenAIDevs
- @sama
- @ylecun
- @karpathy
- @DrJimFan
- @AndrewYNg

## Note

RSS bridge services may occasionally be rate-limited or unavailable. If one fails, try another Nitter instance or inform the user to try again later.
