import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_multipage_books():
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    all_books = []

    for page_num in range(1, 4):
        page_url = base_url.format(page_num)
        print(f"Scraping page {page_num}: {page_url}")

        response = requests.get(page_url)
        response.raise_for_status()
        response.encoding = "utf-8"

        soup = BeautifulSoup(response.text, "html.parser")
        product_pods = soup.find_all("article", class_="product_pod")

        for pod in product_pods:
            # Title (from h3 > a attribute 'title')
            title_tag = pod.select_one("h3 > a")
            title = title_tag.get("title") if title_tag else None

            # Price (from p.price_color)
            price_tag = pod.find("p", class_="price_color")
            price = price_tag.get_text(strip=True) if price_tag else None

            # Rating (from p.star-rating class name)
            rating_tag = pod.find("p", class_="star-rating")
            rating = None
            if rating_tag:
                rating_classes = [c for c in rating_tag.get("class", []) if c != "star-rating"]
                rating = rating_classes[0] if rating_classes else None

            # Availability (from p.instock.availability, stripped)
            avail_tag = pod.select_one("p.instock.availability")
            availability = avail_tag.get_text(strip=True) if avail_tag else None

            all_books.append({
                "Page_Number": page_num,
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Availability": availability
            })

        # Safety pause between requests
        time.sleep(1)

    df = pd.DataFrame(all_books)
    output_filename = "multipage_books_dataset.csv"
    df.to_csv(output_filename, index=False, encoding="utf-8")

    print(f"\nTotal books collected: {len(df)}")
    print(f"Dataset successfully saved to {output_filename}")

if __name__ == "__main__":
    scrape_multipage_books()
