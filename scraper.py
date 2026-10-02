import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_quotes():
    url = 'http://quotes.toscrape.com/'
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes_data = []

    quote_elements = soup.find_all('div', class_='quote')
    for quote_div in quote_elements:
        text_elem = quote_div.find('span', class_='text')
        author_elem = quote_div.find('small', class_='author')

        if text_elem and author_elem:
            quotes_data.append({
                'Quote': text_elem.get_text(strip=True),
                'Author': author_elem.get_text(strip=True)
            })

    df = pd.DataFrame(quotes_data, columns=['Quote', 'Author'])
    df.to_csv('quotes.csv', index=False, encoding='utf-8')
    print(f"Successfully scraped {len(df)} quotes and saved to quotes.csv")

if __name__ == '__main__':
    scrape_quotes()
