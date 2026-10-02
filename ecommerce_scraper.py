import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books():
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    product_pods = soup.find_all("article", class_="product_pod")

    for pod in product_pods:
        # Title (from h3 > a attribute 'title')
        title_tag = pod.select_one("h3 > a")
        title = title_tag.get("title") if title_tag else None

        # Price (from p.price_color)
        price_tag = pod.find("p", class_="price_color")
        price = price_tag.get_text(strip=True) if price_tag else None

        # Rating (from p.star-rating class name, e.g., 'One', 'Two', 'Three')
        rating_tag = pod.find("p", class_="star-rating")
        rating = None
        if rating_tag:
            rating_classes = [c for c in rating_tag.get("class", []) if c != "star-rating"]
            rating = rating_classes[0] if rating_classes else None

        # Availability (from p.instock.availability, stripped of whitespace)
        avail_tag = pod.select_one("p.instock.availability")
        availability = avail_tag.get_text(strip=True) if avail_tag else None

        books.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })

    df = pd.DataFrame(books)

    # Export to books_sample.csv
    df.to_csv("books_sample.csv", index=False, encoding="utf-8")

    # Print first 5 records and total count
    print("First 5 records:")
    print(df.head(5))
    print(f"\nTotal books scraped: {len(df)}")

if __name__ == "__main__":
    scrape_books()
