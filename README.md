# Python Web Scraping & Automated Data Extraction Portfolio

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Chromium-green.svg)](https://playwright.dev/)
[![BeautifulSoup](https://img.shields.io/badge/Parser-BeautifulSoup4-orange.svg)](https://www.crummy.com/software/BeautifulSoup/)
[![Pandas](https://img.shields.io/badge/Data-Pandas-150458.svg)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Build-Production--Ready-brightgreen.svg)]()

> **Comprehensive showcase of production-grade web scraping, browser automation, anti-bot circumvention, and automated ETL pipelines engineered in Python.**

---

## 📌 Executive Summary

Modern web scraping demands far more than basic HTTP requests—it requires handling complex JavaScript SPAs, dodging sophisticated bot defenses, parsing paginated catalogs at scale, and turning unstructured web DOMs into clean, actionable business intelligence.

This portfolio highlights **5 specialized projects** covering the complete web scraping and data automation lifecycle:
1. **Static DOM Data Mining** (Requests, BeautifulSoup4)
2. **Paginated Catalog Extraction with Rate-Limiting** (Session Loops, Defensive Throttling)
3. **Dynamic SPA & Client-Side JavaScript Rendering** (Playwright Headless Chromium)
4. **Anti-Scraping Evasion & Header Spoofing** (Requests Session, TLS/Client Fingerprint Simulation)
5. **Post-Scrape Analytics & Automated Notification Pipeline** (Pandas Aggregation, Automated Alerts)

---

## 🚀 Projects Showcase

### 1. Static E-Commerce Scraper
*High-precision DOM element parsing and tabular normalization.*

- **Script**: [`ecommerce_scraper.py`](ecommerce_scraper.py)
- **Deliverable**: [`books_sample.csv`](books_sample.csv)
- **Target**: `http://books.toscrape.com/`
- **Key Capabilities**:
  - Targets containerized card layouts (`article.product_pod`) using CSS selectors.
  - Safely extracts nested title attributes, price points, availability indicators, and mapped star ratings.
  - Automatically handles response character encoding to eliminate Unicode mojibake (e.g., preserving `£` currency symbols).
  - Normalizes clean dictionary structures into a structured Pandas DataFrame.

---

### 2. Multi-Page Paginated Catalog Pipeline
*Reliable multi-page crawling engineered with ethical rate-limiting.*

- **Script**: [`multipage_books_scraper.py`](multipage_books_scraper.py)
- **Deliverable**: [`multipage_books_dataset.csv`](multipage_books_dataset.csv)
- **Target**: `http://books.toscrape.com/catalogue/page-{N}.html`
- **Key Capabilities**:
  - Traverses sequential paginated URL routes dynamically with automated route formatting.
  - Features defensive pauses (`time.sleep(1)`) between HTTP requests to respect host server bandwidth and eliminate IP rate-limiting risks.
  - Appends contextual crawl metadata (`Page_Number`) to ensure end-to-end data lineage.
  - Aggregates multi-batch scrapes into a unified 60-record dataset ready for analytical modeling.

---

### 3. Dynamic SPA & JS Automation Scraper
*Full browser automation for JavaScript-rendered DOMs that standard HTTP libraries cannot fetch.*

- **Script**: [`dynamic_scraper.py`](dynamic_scraper.py)
- **Deliverable**: [`dynamic_quotes.csv`](dynamic_quotes.csv)
- **Target**: `http://quotes.toscrape.com/js/`
- **Key Capabilities**:
  - Leverages `playwright.sync_api` to orchestrate an authentic headless Chromium browser.
  - Implements explicit selector waiting (`page.wait_for_selector("div.quote")`) ensuring zero race conditions with asynchronous DOM hydration.
  - Extracts asynchronously populated text and author elements straight from the live JavaScript execution context.
  - Enforces graceful browser context disposal to prevent memory leaks in production scrapers.

---

### 4. Anti-Scraping Bypass & Header Spoofer
*Simulating genuine browser TLS and HTTP signatures to bypass WAFs and bot filters.*

- **Script**: [`stealth_scraper.py`](stealth_scraper.py)
- **Deliverable**: [`stealth_check.json`](stealth_check.json)
- **Target Service**: `https://httpbin.org/headers`
- **Key Capabilities**:
  - Spoofs authentic desktop Windows 10 Chrome 124 browser signatures (`User-Agent`, `Sec-Ch-Ua`, `Accept-Language`, `Sec-Fetch-*`).
  - Employs persistent connection pooling via `requests.Session`.
  - Injects randomized human-like jitter delays (`random.uniform(1.5, 3.0)`) before execution.
  - Verifies server-perceived headers via JSON telemetry to validate that bot-detection heuristics are circumvented.

---

### 5. Automated Data Processing & Notification Flow
*Turning raw crawled datasets into executive summaries and threshold-based alerts.*

- **Script**: [`automation_pipeline.py`](automation_pipeline.py)
- **Deliverables**: 
  - Filtered High-Value CSV: [`top_rated_books.csv`](top_rated_books.csv)
  - Executive Alert Report: [`automated_report.txt`](automated_report.txt)
- **Input Source**: [`multipage_books_dataset.csv`](multipage_books_dataset.csv)
- **Key Capabilities**:
  - Ingests scraped CSV datasets, strips currency notations, and casts financial values to native floats.
  - Calculates real-time analytics: total volume, mean catalog price (£35.00), min/max spread, and quality ratios.
  - Filters high-priority items (`Rating == 'Five'`) and stores them in a dedicated target file.
  - Generates an executive dispatch-ready report with formatted KPIs, ready for automated email or webhook delivery.

---

## 🛠️ Technical Competencies

| Competency Area | Technologies & Methods |
|---|---|
| **Web Crawling & Parsing** | Requests, BeautifulSoup4 (`html.parser`, `lxml`), CSS Selectors, XPath |
| **Browser Automation & SPAs** | Playwright (Chromium, Firefox, WebKit), Headless Navigation, Explicit Waits |
| **Stealth & Anti-Bot Protection** | User-Agent Rotation, Header Spoofing, `requests.Session`, Randomized Delays |
| **Data Processing & ETL** | Pandas, Data Cleaning, Type Normalization, Unicode & UTF-8 Encoding Safeguards |
| **Export Formats & Delivery** | CSV, JSON, TXT Executive Summaries, Automated Reporting Workflows |

---

## 📂 Repository Structure

```
├── ecommerce_scraper.py           # Single-page e-commerce target scraper
├── books_sample.csv               # Scraped book sample dataset (20 records)
├── multipage_books_scraper.py     # Multi-page paginated scraper with rate-limiting
├── multipage_books_dataset.csv    # Aggregated 3-page catalog dataset (60 records)
├── dynamic_scraper.py             # Playwright headless browser JS-rendered scraper
├── dynamic_quotes.csv             # Scraped dynamic SPA quotes dataset (10 records)
├── stealth_scraper.py             # Browser spoofing & stealth headers validator
├── stealth_check.json             # Server-verified headers response payload
├── automation_pipeline.py         # Automated analytics, CSV filter & report generator
├── top_rated_books.csv            # Filtered 5-star rated books dataset (14 records)
├── automated_report.txt           # Dispatch-ready executive summary notification
└── README.md                      # Professional project portfolio documentation
```

---

## ⚡ Quickstart & Installation

### 1. Environment Setup
Install required Python packages and the Playwright Chromium browser binary:
```bash
pip install requests beautifulsoup4 pandas playwright
playwright install chromium
```

### 2. Running the Pipeline
Run any component individually:
```bash
# Project 1: Single-page static scraper
python ecommerce_scraper.py

# Project 2: Multi-page paginated scraper
python multipage_books_scraper.py

# Project 3: Playwright dynamic SPA scraper
python dynamic_scraper.py

# Project 4: Stealth headers & anti-bot check
python stealth_scraper.py

# Project 5: Automated analytics & alert generator
python automation_pipeline.py
```

---

## 💼 Why Choose These Solutions for Your Project?
- **Zero Breakage**: Robust selector querying with fallback null-handling.
- **Enterprise-Grade Cleanliness**: Clean data outputs without corrupt encoding or messy whitespace.
- **Scalable Architecture**: Modular functions that integrate into Cron jobs, Celery workers, or AWS Lambda pipelines.
- **Polite & Ethical**: Built-in rate limits to safeguard your target domains from downtime.
