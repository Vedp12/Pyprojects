from bs4 import BeautifulSoup
import time
import requests

# --- Config ---
TOKEN = "f60b533afb5547edb2687941afc65cb51c51af9d9f8"  # get from scrape.do
TARGET_URL = (
    "https://www.flipkart.com/clo/~cs-k4rzk1whgr/pr"
    "?sid=clo&collection-tab-name=Men%27s+Clothing"
    "&p%5B%5D=facets.brand%255B%255D%3DWROGN&sort=recency_desc"
)
API_URL = f"https://api.scrape.do/?token={TOKEN}&url={TARGET_URL}"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

def fetch_page():
    time.sleep(2)
    session = requests.Session()  # capital S in Session
    response = session.get(API_URL, headers=HEADERS, timeout=30)

    if response.status_code == 200:
        with open("flipkart.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("Page saved to flipkart.html")
        return response.text
    else:
        print(f"Failed: {response.status_code} — {response.text[:200]}")
        return None

def parse_products(html):
    soup = BeautifulSoup(html, "html.parser")

    # Flipkart product cards (class names may shift; inspect your saved HTML)
    products = soup.find_all("div", {"data-id": True})  # each product card has data-id

    if not products:
        print("No products found — Flipkart may have changed its HTML structure.")
        print("Open flipkart.html and inspect the class names.")
        return

    for p in products:
        name = p.find("a", class_="IRpwTa") or p.find("div", class_="KzDlHZ")
        price = p.find("div", class_="Nx9bqj")
        link_tag = p.find("a", href=True)

        print("---")
        print("Name :", name.get_text(strip=True) if name else "N/A")
        print("Price:", price.get_text(strip=True) if price else "N/A")
        print("Link :", "https://www.flipkart.com" + link_tag["href"] if link_tag else "N/A")

if __name__ == "__main__":
    html = fetch_page()
    if html:
        parse_products(html)