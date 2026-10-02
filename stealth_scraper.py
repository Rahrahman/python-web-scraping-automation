import json
import random
import time
import requests

def run_stealth_check():
    url = "https://httpbin.org/headers"

    # Realistic desktop Windows Chrome headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Sec-Ch-Ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1"
    }

    # Initialize session with custom headers
    session = requests.Session()
    session.headers.update(headers)

    # Random human-like delay
    delay = random.uniform(1.5, 3.0)
    print(f"Adding human-like delay of {delay:.2f} seconds before request...")
    time.sleep(delay)

    print(f"Sending GET request to {url}...")
    response = session.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    received_headers = data.get("headers", {})

    print("\n=== Header Verification Result ===")
    detected_user_agent = received_headers.get("User-Agent")
    print(f"Server-Detected User-Agent: {detected_user_agent}")
    print(f"Server-Detected Accept-Language: {received_headers.get('Accept-Language')}")
    print(f"Server-Detected Sec-Ch-Ua: {received_headers.get('Sec-Ch-Ua')}")

    # Export to stealth_check.json
    output_filename = "stealth_check.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"\nVerification payload saved to {output_filename}")

if __name__ == "__main__":
    run_stealth_check()
