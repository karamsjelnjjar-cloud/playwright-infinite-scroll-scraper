# 🔄 Dynamic Infinite Scroll Scraper with Playwright

A robust and advanced web scraping tool built with Python and **Playwright** that handles dynamic pages with infinite scrolling, extracts structured data (Quotes, Authors, and Tags), processes it using Pandas, and exports it to an Excel file.

## 🚀 Features
- **Browser Automation (Playwright):** Launches a Chromium browser instance to interact with JavaScript-heavy and dynamic web applications.
- **Infinite Scroll Handling:** Implements an intelligent scrolling loop that evaluates document height dynamically (`scrollHeight`) until all hidden content is fully loaded.
- **Granular Data Extraction:** Extracts multi-attribute data including quote text, authors, and associated categorization tags.
- **Structured Data Export:** Cleans, organizes, and exports the final dataset seamlessly into an Excel file (`playwright_quotes.xlsx`).

## 🛠️ Built With
- **Python 3.x**
- **Playwright (Sync API)** (Dynamic Web Scraping & Automation)
- **Pandas** (Data Processing & Exporting)

## ⚙️ How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/karamsjelnjjar-cloud/playwright-infinite-scroll-scraper.git](https://github.com/karamsjelnjjar-cloud/playwright-infinite-scroll-scraper.git)
