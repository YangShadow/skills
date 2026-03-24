# X Tech News Skill

Fetch and summarize the latest AI and technology news from X (Twitter) using RSS feeds.

## Features

- **智能分类** - 自动将推文按主题分类（模型发布、产品更新、研究进展、安全/对齐、行业动态）
- **智能摘要** - 生成数据概览和热门话题统计
- **多源聚合** - 14个默认 AI/tech 账号
- **关键词过滤** - 自动筛选 AI/tech 相关内容
- **多实例容错** - 自动切换多个 Nitter 实例
- **中英文支持** - 输出格式为中英混合，适合中文用户

## Default Accounts

- **AI Labs**: @OpenAI, @AnthropicAI, @GoogleAI, @GoogleDeepMind, @OpenAIDevs
- **Leaders**: @sama, @ylecun, @karpathy, @AndrewYNg
- **Researchers**: @DrJimFan, @goodside, @hardmaru
- **Industry**: @bindureddy, @newsycombinator, @TechCrunch, @verge

## Usage in Claude Code

Activate the skill by asking:
- "获取 x.com 上最新的 AI 新闻"
- "Twitter 上有什么科技热点？"
- "看看 OpenAI 和 Anthropic 今天在 X 上说了什么"

## Script Usage

```bash
# Fetch from default accounts (AI/tech filtered)
python scripts/fetch_x_news.py -f -o news.md

# Fetch specific accounts
python scripts/fetch_x_news.py OpenAI AnthropicAI karpathy -f

# Limit tweets per account
python scripts/fetch_x_news.py -f -l 10

# Output as JSON
python scripts/fetch_x_news.py -j
```

## Output Format

```markdown
# X 科技动态摘要 - 2026年03月24日

> 共获取 149 条相关动态 | 主要来自: @OpenAI(15条)... | 热门话题: gpt, claude, ai...

**数据来源**: @OpenAI, @AnthropicAI...

---

## 模型发布
**@OpenAI**  GPT-5.4 mini is available today...
[查看原文](https://nitter.net/...)

## 产品更新
...

## 研究进展
...
```

## Notes

- RSS bridge services (Nitter) may occasionally be rate-limited
- The skill automatically tries multiple Nitter instances if one fails
- Some instances may require VPN in certain regions
- Tweet categorization is keyword-based and may not be 100% accurate
