Web Scraper: Extract Website Titles

This Python script scrapes the latest headlines from the BBC News homepage.
You learned how to send HTTP requests, parse HTML structures, and extract useful data automatically.

🔧 Tools Used

requests — downloads webpage HTML

BeautifulSoup (bs4) — parses and navigates HTML

Python 3

📌 What the Script Does

Sends a request to https://www.bbc.com/news

Downloads the raw HTML of the homepage

Extracts all headline titles found in the page

Prints each headline cleanly in the terminal

▶️ How to Run the Script

Open your terminal and navigate to the project folder:

cd Day7_WebScraper


Then run:

python scrape_titles.py

📘 Example Output
Top Headlines:
- World leaders meet for global summit
- Market updates show rapid growth
- Scientists discover new species
...

🎯 Skills Learned

How HTTP web requests work

Understanding website HTML structure

Extracting elements with BeautifulSoup

Automation using external libraries

Basic web scraping techniques used in real-world projects
