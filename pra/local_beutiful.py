from bs4 import BeautifulSoup

with open("index.html", "r") as file:
    content = file.read()
    soup = BeautifulSoup(content, "html.parser")
    # print(soup.prettify())
    tags = soup.find_all("h2")
    for tag in tags:
        print(tag.text)
