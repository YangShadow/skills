# 数据源参考

## RSS 源

### 财经新闻

| 来源 | RSS URL | 说明 |
|-----|---------|------|
| Reuters Markets | https://www.reuters.com/markets/rss/ | 市场新闻快讯 |
| CNBC Finance | https://www.cnbc.com/id/10000664/device/rss/rss.html | 美股市场新闻 |
| Yahoo Finance | https://finance.yahoo.com/news/rssindex | 综合财经新闻 |
| Investing.com | https://www.investing.com/rss/news.rss | 全球市场新闻 |

### 美联储

| 来源 | URL | 说明 |
|-----|-----|------|
| FOMC Calendar | https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm | 会议日程 |
| Fed Speeches | https://www.federalreserve.gov/newsevents/speeches.htm | 官员讲话 |

## API 接口

### FRED (St. Louis Fed)

**Base URL:** `https://api.stlouisfed.org/fred/`

**主要指标:**
- `DFF` - 联邦基金有效利率
- `CPIAUCSL` - 消费者价格指数
- `PPIACO` - 生产者价格指数
- `UNRATE` - 失业率
- `PAYEMS` - 非农就业人数
- `VIXCLS` - VIX 波动率指数
- `DTWEXBGS` - 美元指数
- `DGS10` - 10年期国债收益率
- `DGS2` - 2年期国债收益率

**请求示例:**
```
https://api.stlouisfed.org/fred/series/observations?series_id=VIXCLS&file_type=json
```

### CME FedWatch

**URL:** https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html

可以通过网页抓取获取利率概率表格数据。

## 网页数据源

### 白宫
- **URL:** https://www.whitehouse.gov/briefing-room/
- **内容:** 政策声明、行政命令

### USTR
- **URL:** https://ustr.gov/about-us/policy-offices/press-office/press-releases
- **内容:** 贸易政策、关税公告

### BLS
- **URL:** https://www.bls.gov/news.release/cpi.nr0.htm
- **内容:** CPI、PPI、就业数据发布

## 付费/受限来源

### Bloomberg
- 大部分内容需要订阅
- 可通过 RSS 获取摘要

### Financial Times
- 有阅读限制
- 可通过 RSS 获取部分文章

## 数据抓取注意事项

1. **尊重 robots.txt**
2. **添加合适的 User-Agent**
3. **控制请求频率**
4. **处理反爬虫机制**
5. **缓存结果避免重复请求**
