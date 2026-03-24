---
name: us-stock-macro-monitor
description: 获取并汇总影响美股市场的宏观资讯，包括美联储政策、通胀就业数据、地缘政治、贸易政策等。当用户询问美股相关新闻、宏观监控、美联储动态、FOMC会议、CPI/PPI数据、非农就业、VIX指数、美元指数、利率预期、地缘政治风险、贸易战、关税政策时必须使用此技能。支持中英文关键词：美股宏观、market macro、美联储、Federal Reserve、CPI、通胀inflation、就业数据、非农就业、nonfarm payroll、地缘政治、geopolitics、美股监控、stock market monitor、Fed news、利率rate、加息hike、降息cut、VIX、美元指数DXY、美债收益率treasury yield、关税tariff、贸易战trade war。只要涉及美股投资决策相关的宏观经济因素，立即使用此技能。
---

# 美股宏观监控

获取并汇总影响美股市场的关键宏观资讯，自动翻译为简体中文输出。

## 监控范围

### 1. 美联储货币政策
- FOMC 会议纪要及声明
- 利率决策及 Powell 讲话
- CME FedWatch 利率预测概率

### 2. 通胀与就业数据
- CPI (消费者价格指数)
- PPI (生产者价格指数)
- 非农就业数据 (Nonfarm Payrolls)
- 失业率

### 3. 地缘政治与政策
- 白宫政策声明
- 美国贸易代表处 (USTR) 公告
- 国际关系及冲突动态

### 4. 市场情绪指标
- VIX 恐慌指数
- 美元指数
- 美债收益率
- Polymarket 事件预测市场

## 信息来源

### 官方数据源
| 来源 | 网址 | 数据类型 |
|-----|------|---------|
| 美联储 | federalreserve.gov | 利率决议、FOMC声明 |
| FRED | fred.stlouisfed.org | 经济指标数据 |
| 美国劳工统计局 | bls.gov | CPI、PPI、就业数据 |
| 白宫 | whitehouse.gov | 政策声明 |
| USTR | ustr.gov | 贸易政策 |

### 财经媒体
| 来源 | 网址 | 特点 |
|-----|------|------|
| Bloomberg | bloomberg.com | 全球财经新闻领导者 |
| Reuters | reuters.com | 快讯及深度分析 |
| Financial Times | ft.com | 国际视角 |
| CNBC | cnbc.com | 美股市场焦点 |
| Yahoo Finance | finance.yahoo.com | 市场数据及新闻 |
| Investing.com | investing.com | 全球市场覆盖 |

### 市场数据平台
| 来源 | 网址 | 用途 |
|-----|------|------|
| TradingView | tradingview.com | 技术分析、市场情绪 |
| CME FedWatch | cmegroup.com | 利率预测概率 |
| Polymarket | polymarket.com | 事件预测市场 |

## 使用方法

当用户请求美股宏观资讯时：

1. **确定时间范围**
   - "今天"/"最新" → 获取当天最新新闻
   - "日报"/"总结" → 获取过去24小时汇总

2. **获取数据**
   - 使用 WebFetch 抓取各来源 RSS/网页
   - 获取关键市场指标 (VIX、美元指数、美债收益率)
   - 获取 CME FedWatch 利率概率

3. **翻译内容**
   - 所有非简体中文内容自动翻译
   - 保留专业术语：Fed, CPI, PPI, FOMC, VIX, GDP
   - 保留人名和公司名英文

4. **生成报告**
   - 按类别组织信息
   - 突出显示对市场影响重大的新闻
   - 添加时间戳和来源

## 输出格式

```markdown
# 美股宏观监控报告 - [日期]

## 关键指标速览
| 指标 | 当前值 | 日变化 | 解读 |
|-----|-------|-------|------|
| VIX | XX.XX | +X.XX | 市场情绪... |
| 美元指数 | XX.XX | +X.XX | 美元强弱... |
| 10年期美债 | X.XX% | +Xbp | 利率预期... |
| 2年期美债 | X.XX% | +Xbp | 短期利率... |

## CME FedWatch 利率预测
| 会议日期 | 维持利率 | 加息25bp | 降息25bp |
|---------|---------|---------|---------|
| [日期] | XX% | XX% | XX% |

## 美联储动态
- **[标题]** - [来源] - [时间]
  [中文摘要内容...]

## 通胀与就业
- **[标题]** - [来源] - [时间]
  [中文摘要内容...]

## 地缘政治与贸易政策
- **[标题]** - [来源] - [时间]
  [中文摘要内容...]

## 市场情绪与预测
- **[Polymarket 事件]** - 当前概率: XX%
  [中文描述...]

## 今日重点关注
1. **[事件1]** ([时间])
   - 影响分析: ...
   - 相关板块: ...

2. **[事件2]** ([时间])
   - 影响分析: ...
   - 相关板块: ...

---
数据更新时间: [时间戳]
```

## 翻译指南

所有获取的英文内容必须翻译为简体中文：

**保留不翻译：**
- 专业术语: Fed, FOMC, CPI, PPI, GDP, NFP, VIX, ETF, IPO
- 人名: Jerome Powell, Joe Biden, Donald Trump
- 公司/机构名: Federal Reserve, Treasury, White House
- 代码/缩写: SPX, NDX, DJI, USD

**翻译原则：**
- 保持财经专业术语的准确性
- 使用简体中文（zh-CN）
- 保留原文链接

## RSS 源参考

```
Reuters Markets: https://www.reuters.com/markets/rss/
CNBC Finance:    https://www.cnbc.com/id/10000664/device/rss/rss.html
Yahoo Finance:   https://finance.yahoo.com/news/rssindex
Investing.com:   https://www.investing.com/rss/news.rss
```

## 注意事项

1. **数据来源限制**
   - Bloomberg、Reuters 可能有付费墙限制
   - 优先使用公开可访问的 RSS 源
   - 部分数据可能需要通过 WebFetch 直接抓取网页

2. **时效性**
   - 优先获取当天最新新闻
   - 关键经济数据发布时间（美东时间8:30）
   - FOMC 会议时间（每6周一次）

3. **准确性**
   - 标注新闻来源和时间
   - 区分事实报道和市场分析
   - 对预测性内容注明不确定性
