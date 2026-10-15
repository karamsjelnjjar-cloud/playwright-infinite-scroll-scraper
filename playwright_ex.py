import pandas as pd
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser (Chromium)
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://quotes.toscrape.com/scroll')

    # Wait for initial load
    page.wait_for_timeout(2000)

    # Scroll down loop
    scroll_pause_time = 1000
    last_height = page.evaluate("document.body.scrollHeight")

    while True:
        page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
        page.wait_for_timeout(scroll_pause_time)

        new_height = page.evaluate("document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Extract all quotes
    quotes_elements = page.query_selector_all('.quote')
    all_quotes_data = []

    for quote in quotes_elements:
        text = quote.query_selector('.text').inner_text()
        author = quote.query_selector('.author').inner_text()

        tag_elements = quote.query_selector_all('.tag')
        tags = ', '.join([tag.inner_text() for tag in tag_elements])

        all_quotes_data.append({
            'Quote': text,
            'Author': author,
            'Tags': tags
        })

    browser.close()

# Export to Excel
df = pd.DataFrame(all_quotes_data)
df.to_excel('playwright_quotes.xlsx', index=False)

print("Export completed successfully using Playwright!")