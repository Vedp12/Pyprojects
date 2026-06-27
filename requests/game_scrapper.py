from bs4 import BeautifulSoup
import requests 

url ="https://sandbox.oxylabs.io/products"
respond = requests.get(url)
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )
}
soup = BeautifulSoup(respond.text, "html.parser")
