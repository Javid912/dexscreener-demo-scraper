from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
import time
import csv

def scrape_dexscreener():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        context = browser.new_context()
        page = context.new_page()

        print("Navigating to Dexscreener...")
        page.goto("https://dexscreener.com/new-pairs/")
        page.wait_for_load_state("networkidle")

        rows = []
        for attempt in range(5):
            try:
                print(f"Attempt {attempt+1} - waiting for rows...")
                page.wait_for_selector("a.ds-dex-table-row-new", timeout=20000, state="visible")
                rows = page.query_selector_all("a.ds-dex-table-row-new")
                if rows:
                    break
            except PlaywrightTimeout:
                print("⚠️ Timeout - scrolling and retrying...")
                page.mouse.wheel(0, 2000)
                time.sleep(3)

        if not rows:
            print("❌ No rows found after retries.")
            browser.close()
            return []

        print(f"✅ Found {len(rows)} rows")
        data = []
        for row in rows:
            try:
                token = row.query_selector(".ds-dex-table-row-base-token-symbol").inner_text()
                price = row.query_selector(".ds-dex-table-row-col-price").inner_text()
                volume = row.query_selector(".ds-dex-table-row-col-volume").inner_text()
                market_cap = row.query_selector(".ds-dex-table-row-col-market-cap").inner_text()
                link = row.get_attribute("href")

                data.append({
                    "token": token,
                    "price": price,
                    "volume": volume,
                    "market_cap": market_cap,
                    "link": f"https://dexscreener.com{link}"
                })
            except Exception as e:
                print(f"⚠️ Error parsing row: {e}")

        browser.close()
        return data


if __name__ == "__main__":
    results = scrape_dexscreener()
    if results:
        filename = "dexscreener_data.csv"
        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
        print(f"💾 Data saved to {filename}")
