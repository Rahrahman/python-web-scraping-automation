from playwright.sync_api import sync_playwright
import pandas as pd

def scrape_dynamic_quotes():
    url = "http://quotes.toscrape.com/js/"
    quotes_data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print(f"Navigating to {url}...")
        page.goto(url)

        # Explicitly wait for JavaScript-rendered quote elements
        page.wait_for_selector("div.quote")

        quote_elements = page.query_selector_all("div.quote")
        for q in quote_elements:
            text_elem = q.query_selector("span.text")
            author_elem = q.query_selector("small.author")

            quote_text = text_elem.inner_text().strip() if text_elem else None
            author_text = author_elem.inner_text().strip() if author_elem else None

            if quote_text and author_text:
                quotes_data.append({
                    "Quote": quote_text,
                    "Author": author_text
                })

        browser.close()

    df = pd.DataFrame(quotes_data, columns=["Quote", "Author"])
    output_file = "dynamic_quotes.csv"
    df.to_csv(output_file, index=False, encoding="utf-8")

    print("\nExtracted Records:")
    print(df)
    print(f"\nTotal quotes extracted: {len(df)}")
    print(f"Saved to {output_file}")

if __name__ == "__main__":
    scrape_dynamic_quotes()
