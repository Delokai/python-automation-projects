import requests
from bs4 import BeautifulSoup

def scrape_bbc():
    url = "https://www.bbc.com/news"

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    headlines = soup.find_all("h2")

    print("BBC News Headlines:\n")
    for h in headlines[:10]:  # show only first 10
        print("-", h.get_text(strip=True))

scrape_bbc()
