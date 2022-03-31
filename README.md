# Scraping-APIs

I use Scrapy to crawl https://openlibrary.org/, but by using its API found by inspecting network requests to and from the page.
Crawling APIs could save effort, but could also be trickier. I had to analyse how the URL parameters on the API requests were formatted, then work with changing those to get different pages.

Path to Spider:
Scraping-APIs > demo_api > spiders > ebooks.py

Path to JSON data:
Scraping-APIs > ebooks_fiction_data.json
