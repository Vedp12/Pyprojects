import requests
response = requests.get('https://httpbin.org/get')
print(response.status_code)  # Outputs: 200
print(response.json())        # Outputs: JSON response

url = "https://books.toscrape.com/"
headers = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64; rv:150.0) Gecko/20100101 Firefox/150.0"
    )
}
response = requests.get(url)
