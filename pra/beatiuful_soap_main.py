from bs4 import BeautifulSoup
from bs4.filter import SoupStrainer
import time, requests

# Target URL
target_url = "https://www.flipkart.com/clo/~cs-k4rzk1whgr/pr?sid=clo&collection-tab-name=Men%27s+Clothing&pageCriteria=default&p%5B%5D=facets.brand%255B%255D%3DWROGN&sort=recency_desc&param=321&BU=LifeStyle"

token = ""

api_url = f"http://api.scrape.do/?token={token}&url={target_url}"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

time.sleep(2)

try:
    session = requests.session()
    response = session.get(
        api_url,
        headers=headers,
    )

    if response.status_code == 200:
        with open("flipkart.html", "r", encoding="utf-8") as file:
            html = file.read()
            soup = BeautifulSoup(html, "html.parser")
            # print(soup.prettify())
            print(soup.title.text)
    else:
        print("Failed to fetch page ")

except Exception as e:
    print("Error:", e)
