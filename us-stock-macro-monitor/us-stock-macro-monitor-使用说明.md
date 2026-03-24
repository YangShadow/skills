# 美股宏观监控技能使用说明

## 📌 简介

**us-stock-macro-monitor** 是一个 Claude Code 技能，用于获取和汇总影响美股市场的关键宏观资讯，包括美联储政策、通胀就业数据、地缘政治、贸易政策等。所有内容自动翻译为简体中文输出。

---

## 🚀 安装方法

### 方法一：安装到 Claude Code（推荐）

1. **复制技能文件到 Claude Code 技能目录**
   ```bash
   cp us-stock-macro-monitor.skill ~/.claude/skills/
   ```

2. **重启 Claude Code** 或运行以下命令刷新技能列表
   ```bash
   claude skills refresh
   ```

3. **验证安装**
   ```bash
   claude skills list | grep us-stock-macro-monitor
   ```

### 方法二：当前项目使用

如果你在当前项目中使用，技能已经位于 `skills/us-stock-macro-monitor/` 目录下，Claude Code 会自动检测并使用。

---

## 💬 使用方法

安装完成后，直接在对话中使用以下任意方式触发技能：

### 触发关键词

| 中文关键词 | 英文关键词 |
|-----------|-----------|
| 美股宏观 / 美股监控 | market macro / stock market monitor |
| 美联储 / Fed / FOMC | Federal Reserve / Fed news |
| CPI / PPI / 通胀数据 | inflation / CPI data |
| 就业数据 / 非农就业 | employment / nonfarm payroll / NFP |
| 地缘政治 | geopolitics / geopolitical risk |
| 利率 / 加息 / 降息 | interest rate / rate hike / rate cut |
| VIX / 恐慌指数 | VIX / volatility index |
| 美元指数 / DXY | US Dollar Index / DXY |
| 美债收益率 | treasury yield / bond yield |
| 关税 / 贸易战 | tariff / trade war |

### 使用示例

#### 1. 获取完整宏观日报
```
"给我一份美股宏观监控日报"
"获取今天影响美股的重要新闻"
"总结一下美股市场的宏观情况"
```

#### 2. 专注特定主题
```
"查看美联储最新动态和利率预期"
"最近有什么通胀数据和CPI消息"
"关注一下地缘政治风险"
"看一下CME FedWatch的利率预测"
```

#### 3. 组合查询
```
"总结一下最近的通胀数据和地缘政治风险"
"美联储政策和就业数据有什么新消息"
"VIX指数和美债收益率怎么样"
```

---

## 📊 输出内容

技能会生成一份结构化的 Markdown 报告，包含以下部分：

### 1. 关键指标速览
| 指标 | 说明 |
|-----|------|
| VIX | 恐慌指数，反映市场情绪 |
| 美元指数 (DXY) | 美元强弱程度 |
| 10年期美债 | 长期利率预期 |
| 2年期美债 | 短期利率预期 |

### 2. CME FedWatch 利率预测
- 下次FOMC会议利率概率
- 未来几次会议的利率路径预期

### 3. 美联储动态
- FOMC会议决议
- Powell讲话要点
- 美联储官员观点

### 4. 通胀与就业
- CPI/PPI最新数据
- 非农就业数据
- 失业率变化

### 5. 地缘政治与贸易政策
- 国际冲突动态
- 贸易谈判进展
- 关税政策变化
- 白宫政策声明

### 6. 市场情绪
- Polymarket预测市场数据
- TradingView情绪指标

### 7. 今日重点关注
- 重要经济数据发布时间
- 关键事件提醒
- 影响分析及相关板块

---

## 📡 数据来源

### 官方数据源
- **美联储** (federalreserve.gov) - 利率决议、FOMC声明
- **FRED** (fred.stlouisfed.org) - 经济指标数据
- **美国劳工统计局** (bls.gov) - CPI、PPI、就业数据
- **白宫** (whitehouse.gov) - 政策声明
- **USTR** (ustr.gov) - 贸易政策

### 财经媒体
- **Reuters** - 全球财经新闻
- **Bloomberg** - 市场快讯
- **Financial Times** - 国际视角
- **CNBC** - 美股市场焦点
- **Yahoo Finance** - 市场数据及新闻
- **Investing.com** - 全球市场覆盖

### 市场数据平台
- **TradingView** - 技术分析、市场情绪
- **CME FedWatch** - 利率预测概率
- **Polymarket** - 事件预测市场

---

## ⚙️ 高级用法

### 手动运行脚本

如果需要自定义数据获取，可以直接运行脚本：

```bash
# 进入技能目录
cd skills/us-stock-macro-monitor/

# 1. 获取宏观新闻
python scripts/fetch_macro_news.py

# 2. 获取美联储数据
python scripts/fetch_fed_data.py

# 3. 格式化报告
python scripts/format_report.py
```

### 自定义 RSS 源

编辑 `scripts/fetch_macro_news.py` 文件中的 `RSS_SOURCES` 字典，添加或修改新闻源：

```python
RSS_SOURCES = {
    "source_name": "https://example.com/rss/feed.xml",
    # ... 其他源
}
```

### 添加监控关键词

编辑 `scripts/fetch_macro_news.py` 文件中的 `KEYWORDS` 字典，添加新的监控类别：

```python
KEYWORDS = {
    "fed": ["fed", "federal reserve", "fomc", ...],
    "inflation": ["cpi", "ppi", "inflation", ...],
    # 添加你的自定义类别
    "custom": ["keyword1", "keyword2", ...],
}
```

---

## 📝 输出示例

```markdown
# 美股宏观监控报告 - 2026年3月24日

## 关键指标速览
| 指标 | 当前值 | 日变化 | 解读 |
|-----|-------|-------|------|
| VIX | 26.15 | +1.2 | 市场恐慌情绪上升 |
| 美元指数 | 99.15 | +0.5 | 美元反弹 |
| 10年期美债 | 4.26% | +5bp | 收益率上升 |

## CME FedWatch 利率预测
| 会议日期 | 维持利率 | 降息25bp | 加息25bp |
|---------|---------|---------|---------|
| 2026年5月 | 75% | 25% | <5% |

## 美联储动态
- **美联储维持利率不变** - Reuters - 今天
  联邦基金利率目标区间维持在3.50%-3.75%...

## 通胀与就业
- **2月CPI同比增长2.4%** - Bloomberg - 今天
  核心CPI环比上涨0.2%，住房成本仍是主要推手...

## 地缘政治与贸易政策
- **中东局势紧张** - Reuters - 今天
  霍尔木兹海峡航运受阻，油价飙升...

## 今日重点关注
1. **3月CPI数据发布** (4月10日 8:30 ET)
   - 影响分析: 若CPI跳升可能改变降息预期
   - 相关板块: 利率敏感板块、银行股

---
数据更新时间: 2026-03-24
_免责声明: 本报告仅供参考，不构成投资建议_
```

---

## 🔧 故障排除

### 技能没有触发
- 确保使用了触发关键词（见上文列表）
- 检查技能是否正确安装：`claude skills list`
- 尝试更明确地表达，如"使用美股宏观监控技能获取..."

### 数据获取失败
- 某些数据源可能有访问限制或需要API密钥
- 检查网络连接
- 查看脚本输出的错误信息

### 翻译不完整
- 技能使用 Claude 进行翻译，确保 Claude 服务正常
- 部分专业术语会保留英文原文（如 Fed, CPI, VIX 等）

---

## 📅 更新计划

- [ ] 添加更多数据源（WSJ、MarketWatch等）
- [ ] 支持定时自动推送（Cron任务）
- [ ] 添加历史数据对比功能
- [ ] 支持自定义报告模板

---

## ⚠️ 免责声明

本技能提供的所有信息仅供参考，不构成投资建议。投资有风险，决策需谨慎。请根据自身情况独立判断。

---

## 🐛 问题反馈

如遇到问题或有改进建议，请：
1. 检查本使用说明是否已解答你的问题
2. 查看技能目录下的 `references/data_sources.md` 了解更多技术细节
3. 联系技能开发者

---

**版本**: v1.0
**创建日期**: 2026-03-24
**适用平台**: Claude Code
