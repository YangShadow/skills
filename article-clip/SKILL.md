---
name: article-clip
description: 原文归档 skill。抓取文章完整原文（不做提炼），转换为 Markdown 存入 Obsidian inbox 目录。触发场景：用户调用 /article-clip，或说「帮我存这篇文章」「归档这个链接」「抓取原文」时。支持微信公众号、X/Twitter、YouTube、腾讯文档、通用网页。
---

# article-clip Skill

## 触发方式

```
/article-clip <URL>        # 抓取原文并归档
/article-clip              # 无 URL 时提示用户提供
```

## 目标

抓取目标 URL 的**完整原文**，转换为干净的 Markdown，写入 Obsidian inbox 目录。
**不做任何提炼、总结、改写**——保留原文全部内容，供后续二次处理使用。

## Step 1：加载 web-access skill 并抓取

必须加载 web-access skill 并遵循其指引，根据 URL 特征选择抓取策略：

| URL 特征 | 来源类型 | 抓取策略 |
|---------|---------|---------|
| mp.weixin.qq.com | 微信公众号 | CDP 模式（反爬，必须走浏览器） |
| x.com / twitter.com | X（推特）| CDP 模式；抓正文 + 完整线程 |
| youtube.com / youtu.be | YouTube | 优先官方字幕；无字幕则抓视频描述；标注「基于字幕/描述」 |
| docs.qq.com | 腾讯文档 | CDP 模式；全文提取 |
| 其他域名 | 通用网页 | WebFetch 或 Jina（r.jina.ai/ 前缀）；失败则 CDP |

抓取目标：
- 文章标题
- 正文全文（保留段落、标题层级、代码块、列表等结构）
- 发布日期（能抓到则记录，否则留空）
- 作者 / 来源账号（能抓到则记录）

图片、视频等媒体资源不需要下载，忽略即可。

## Step 2：转换为 Markdown

原文结构映射规则：
- 文章大标题 → `# 标题`
- 小节标题 → `##` / `###`（按原文层级）
- 正文段落 → 普通段落，保留原始分段
- 有序/无序列表 → Markdown 列表
- 代码块 → 代码块（保留语言标注）
- 引用 → `>` blockquote
- 加粗/斜体 → `**bold**` / `*italic*`
- 超链接 → `[文本](url)`
- 图片 → 跳过（不需要保留）
- 广告、评论区、推荐阅读等非正文内容 → 删除

## Step 3：写入 Obsidian

**目标路径：**
- 投资理财相关文章 → `/Users/seeing/Documents/Obsidian/01.投资理财/11.inbox/`
- 其他文章 → `/Users/seeing/Documents/Obsidian/11.inbox/`

判断依据：文章主题涉及股票/期权/美股/基金/宏观经济/投资/理财/财报时归入投资理财 inbox。

**文件命名：** `YYYY-MM-DD-标题关键词.md`
- 日期取今天（无法从文章获取时）或文章发布日期
- 标题取文章主题，去掉特殊字符，中英文均可，不超过 30 字

**文件格式：**

```markdown
---
date: YYYY-MM-DD
source: wechat | x.com | youtube | tencent-doc | web
url: <原文 URL>
author: <作者或来源账号，无则留空>
tags: []
status: inbox
---

# <文章原标题>

<正文原文，完整保留>
```

`status: inbox` 固定写死，表示待处理状态。

## Step 4：Git 同步

```bash
cd "/Users/seeing/Documents/Obsidian"
git add 11.inbox/ 01.投资理财/11.inbox/
git commit -m "clip: <文章标题> $(date +%Y-%m-%d)"
git pull --rebase origin main
git push origin main
```

push 失败时告知用户，不阻塞主流程。

## 常见问题

**微信公众号抓取失败**：微信会检测自动化，优先尝试 CDP 模式。若 CDP 也失败，告知用户手动粘贴原文内容，然后继续写入流程（跳过 Step 1）。

**YouTube 无字幕**：抓取视频描述 + 频道信息，在文件 frontmatter 中标注 `note: 基于视频描述，无字幕`。

**内容过长**：不截断，完整保留。Obsidian 无文件大小限制。
