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
````

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/dexscreener-demo-scraper.git
cd dexscreener-demo-scraper
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
```

## Usage

Run the scraper:

```bash
python3 dexscreener_demo.py
```

Output is printed in the terminal.
To save to CSV, run:

```bash
python3 dexscreener_demo.py --csv
```

## Deployment

On a Linux VPS you can automate scraping every 5 minutes with a cron job:

```bash
*/5 * * * * /path/to/.venv/bin/python3 /path/to/dexscreener_demo.py --csv >> scraper.log 2>&1
```

---

## Tech Stack

* Python 3.9+
* Playwright
* Headless Chromium
* Linux / macOS / Windows

---

### Why this project?

This demo was created as part of a freelancing project proposal. It demonstrates:

* Fast prototyping of real-world scrapers.
* Clean project structure for easy extension.
* Integration-ready CSV output for further analytics.

---

💡 Want to use this as a base? Fork it and extend!

````

---

### 3. Add requirements.txt
Inside the project folder, create a `requirements.txt`:  
```txt
playwright==1.36.0
````
