---
name: knowledge-capture
description: 知识捕获 skill。从多种来源（x.com、微信公众号、YouTube、腾讯文档、外网）抓取内容，提炼结构化笔记，写入 Obsidian 并 git push。触发场景：用户调用 /knowledge-capture，或提供 URL 要求整理成笔记时。
---

# knowledge-capture Skill

## 触发方式

```
/knowledge-capture <URL>               # 自动识别来源和分类
/knowledge-capture <URL> --cat ai      # 强制指定分类（ai/books/skills/misc）
/knowledge-capture                     # 无URL时进入粘贴内容模式
```

## Step 1：来源识别与抓取策略

调用 web-access skill 抓取内容，根据 URL 域名选择策略：

| URL 特征 | 来源类型 | 抓取策略 |
|---------|---------|---------|
| x.com / twitter.com | X（推特）| 推文正文 + 完整线程 + 高赞回复（≥50赞）|
| mp.weixin.qq.com | 微信公众号 | 文章完整正文（处理跳转页）|
| youtube.com / youtu.be | YouTube | 优先抓官方字幕；无字幕则抓视频描述+高赞评论摘要；标注「基于字幕/描述」|
| docs.qq.com | 腾讯文档 | 文档全文提取 |
| 其他域名 | 通用网页 | 正文提取，过滤导航栏/广告/footer |

**粘贴内容模式（无URL）：**
用户直接粘贴文字内容时，跳过抓取步骤，直接进入 Step 2 内容分析。
询问：「请问这段内容来自哪里？（用于填写笔记来源字段）」

**注意：**
- 抓取前检查 web-access 的 CDP 依赖是否可用
- x.com / 微信公众号等反爬平台优先使用 CDP 模式
- 若抓取失败，告知用户并切换到粘贴内容模式

## Step 2：分类判断

**Auto-detect（关键词匹配，优先级从高到低）：**

| 匹配关键词 | 分类 | Obsidian 路径 |
|-----------|------|--------------|
| AI / 大模型 / LLM / Agent / GPT / Claude / 提示词 / Prompt / 机器学习 | ai | `/Users/seeing/Documents/Obsidian/02.知识库/01.AI学习/` |
| 书评 / 读书 / 读后感 / 作者 / 章节 / 书名 / 这本书 / 推荐书 | books | `/Users/seeing/Documents/Obsidian/02.知识库/02.读书笔记/` |
| 教程 / 方法论 / 技能 / 学习 / 指南 / How to / 实践 / 技巧 | skills | `/Users/seeing/Documents/Obsidian/02.知识库/05.skills/` |
| 其他 | misc | `/Users/seeing/Documents/Obsidian/02.知识库/04.杂项/` |

`--cat <分类>` 参数强制覆盖 auto-detect，直接使用指定分类。

分类判断后告知用户：「已分类为 [ai/books/skills/misc]，将保存到 知识库/xxx/。继续？」
用户可在此步骤修改分类。

## Step 3：内容提炼

**提炼规则（严格执行）：**
- 核心观点：≤5条，必须用自己的语言重新表达，禁止直接复制原文句子
- 为什么重要：从用户视角写，这个知识对程序员/投资人有什么具体价值
- 我的思考：若内容有明显争议点或延伸问题，给出1-2个引导性问题；若无，留空等用户填写
- 关联笔记：在 Obsidian Vault 的 知识库/ 目录下搜索标题相近的已有笔记，建立 `[[双链]]`

**提炼质量标准：**
- 读完笔记后无需再看原文也能理解核心内容
- 每条观点应是独立的、可行动的或可应用的知识点
- 避免：「文章说了A、B、C三点」这类描述性总结

## Step 4：写入 Obsidian

**文件命名规则：** `YYYY-MM-DD-标题关键词.md`（标题取原文主题，中英文均可，去掉特殊字符）

**笔记模板：**

```markdown
---
date: YYYY-MM-DD
source: x.com | wechat | youtube | tencent-doc | web
url: <原文URL>
category: ai | books | skills | misc
tags: []
---

# <标题>

> <原文一句话概括>（<作者/来源账号>，<平台>）

## 核心观点
1. <观点1，自己的语言>
2. <观点2>
3. <观点3>

## 为什么重要
<对我的具体价值，1-3句>

## 我的思考
<引导性问题或留空>

## 关联笔记
- [[<已有笔记标题>]]

## 原始来源
- [<标题或域名>](<url>) · YYYY-MM-DD
```

使用文件写入工具将笔记保存到对应 Obsidian 路径。

## Step 5：Git 同步

```bash
cd "/Users/seeing/Documents/Obsidian"
git add 02.知识库/
git commit -m "learn: <笔记标题> $(date +%Y-%m-%d)"
git pull --rebase origin main
git push origin main
```

push 失败时告知用户，不阻塞主流程。
