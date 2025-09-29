# Dexscreener Demo Scraper

A simple **Python Playwright scraper** that extracts the latest pairs from [Dexscreener](https://dexscreener.com/new-pairs/) and outputs structured data.

## Features
- Scrapes live token data (chain, name, symbol, age, buys, sells, volume, liquidity, market cap).
- Headless browser automation with **Playwright**.
- Configurable retry logic for stable scraping.
- CSV export (easy integration with analysis pipelines).
- Runs on Linux VPS (can be scheduled with cron for 5-min intervals).

## Example Output
```python
{'token': 'SPARK', 'price': '$0.0008177', 'volume': '$7.4M', 'market_cap': '$809K', 'link': 'https://dexscreener.com/plasma/0xf5ef5e0f99d0be34b30332bdfbb639241be4c309'}
