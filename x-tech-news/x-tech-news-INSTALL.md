# X Tech News Skill 安装指南

## 📦 安装方法

### 方法一：直接解压安装

1. 将 `x-tech-news.skill` 文件复制到 Claude Code 的 skills 目录：
   ```bash
   # macOS/Linux
   mkdir -p ~/.claude/skills
   unzip x-tech-news.skill -d ~/.claude/skills/x-tech-news/
   ```

2. 或者在项目目录中直接使用：
   ```bash
   unzip x-tech-news.skill -d ./skills/x-tech-news/
   ```

### 方法二：使用 Claude Code 命令（如果支持）

```bash
claude skills add ./x-tech-news.skill
```

---

## 🔧 系统要求

- **Python**: 3.7 或更高版本
- **网络**: 需要访问 Nitter RSS 服务（可能需要 VPN）
- **依赖**: 仅使用 Python 标准库，无需额外安装

---

## 🚀 使用方法

### 在 Claude Code 中使用

激活 skill 的方式：
```
获取 x.com 上最新的 AI 新闻
```

或：
```
Twitter 上有什么科技热点？
```

### 命令行直接使用

```bash
# 进入 skill 目录
cd skills/x-tech-news

# 获取最新 AI 新闻（英文）
python scripts/fetch_x_news.py -f -o news.md

# 限制每个账号的推文数量
python scripts/fetch_x_news.py -f -l 5 -o news.md

# 获取特定账号
python scripts/fetch_x_news.py OpenAI AnthropicAI -f

# 输出为 JSON 格式
python scripts/fetch_x_news.py -f -j
```

---

## 📋 功能特性

### 自动监控的账号（16个）

**AI Labs:**
- @OpenAI, @AnthropicAI, @GoogleAI, @GoogleDeepMind, @OpenAIDevs

**AI 领袖:**
- @sama (Sam Altman), @ylecun (Yann LeCun)
- @karpathy (Andrej Karpathy), @AndrewYNg (吴恩达)

**研究人员:**
- @DrJimFan, @goodside, @hardmaru, @bindureddy

**科技媒体:**
- @newsycombinator (Hacker News)
- @TechCrunch, @verge

### 智能分类系统

推文自动归类到以下类别：
1. **模型发布** - GPT, Claude, LLM 等新模型发布
2. **产品更新** - ChatGPT, Codex, API 功能更新
3. **研究进展** - 论文、实验、benchmark
4. **安全/对齐** - Safety, alignment, 评估
5. **行业动态** - 融资、收购、公司新闻
6. **其他** - 未分类内容

### 输出示例

```markdown
# X 科技动态摘要 - 2026年03月24日

> 共获取 118 条相关动态 | 主要来自: @OpenAI(10条)... | 热门话题: gpt, claude, api

---

## 模型发布
**@OpenAI** GPT-5.4 mini 今天在 ChatGPT、Codex 和 API 中可用。
针对编程、计算机使用、多模态理解和子代理进行了优化。

## 产品更新
...
```

---

## ⚠️ 注意事项

1. **RSS 服务稳定性**: Nitter 是第三方 RSS 桥接服务，可能偶尔不可用
2. **访问限制**: 某些地区可能需要 VPN 才能访问 Nitter
3. **翻译**: 当前版本抓取英文内容，建议由 Claude 翻译成中文
4. **频率限制**: 请勿过于频繁地抓取，建议间隔 5 分钟以上

---

## 📝 自定义配置

### 修改监控账号

编辑 `scripts/fetch_x_news.py`，修改 `DEFAULT_ACCOUNTS` 列表：

```python
DEFAULT_ACCOUNTS = [
    "OpenAI",
    "AnthropicAI",
    "你的自定义账号",
    # ...
]
```

### 添加关键词过滤

编辑 `scripts/fetch_x_news.py` 中的 `AI_KEYWORDS` 和 `TECH_KEYWORDS` 列表。

---

## 🔗 相关文件

打包后的 skill 文件包含：
- `SKILL.md` - Skill 定义和使用指南
- `README.md` - 详细文档
- `scripts/fetch_x_news.py` - 核心抓取脚本
- `scripts/__init__.py` - 包初始化文件

---

## 📄 许可证

MIT License - 可自由使用和修改

---

## 🤝 问题反馈

如有问题或建议，欢迎反馈！
