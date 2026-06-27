from bs4 import BeautifulSoup
import requests
import os
from urllib.parse import urlparse

url = "https://alternativeto.net/"

# Fix 1: Add browser-like headers so the server doesn't block the request
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}

response = requests.get(url, headers=headers)
# "Mozilla/5.0 (X11; Linux x86_64; rv:150.0) Gecko/20100101 Firefox/150.0"
print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

os.makedirs("images", exist_ok=True)

images = soup.find_all("img")
print(f"Found {len(images)} image tags")

count = 0
for img in images:
    img_url = img.get("src") or img.get("data-src")

    if not img_url:
        continue

    if img_url.startswith("data:") or not img_url.startswith("http"):
        continue

    try:
        img_response = requests.get(img_url, headers=headers, timeout=10)
        img_response.raise_for_status()

        # Fix 4: Use the correct extension from the URL
        path = urlparse(img_url).path
        ext = os.path.splitext(path)[-1]  # e.g. .jpg, .png, .gif
        if not ext or len(ext) > 5:
            ext = ".jpg"  # fallback

        count += 1
        filename = f"images/image_{count}{ext}"

        with open(filename, "wb") as file:
            file.write(img_response.content)

        print(f"Downloaded {filename}")

    except Exception as error:
        print("Error:", error)

print(f"\nDone. {count} images saved.")