import scrapy
from scrapy.exceptions import CloseSpider
import json

class EbooksSpider(scrapy.Spider):
    name = 'ebooks'
    allowed_domains = ['openlibrary.org']
    start_urls = ['https://openlibrary.org/subjects/fiction.json?limit=12&offset=0 ']

    # I observed that the offset url parameter determined which book index to start from on that page.
    # As it was displaying books in multiples of 12, initially it's set to 0, and then I increment it by 12.
    page_increment = 12
    offset = 0

    def parse(self, response):

        # Check if response receives an error because there is nothing left to scrape.
        if response.status == 500:
            raise CloseSpider("Reached final page!")

        # Turn response object into a JSON object that is easier to work with.
        resp = json.loads(response.body)
        ebooks = resp.get('works')
        for ebook in ebooks:
            yield {
                'Title': ebook.get('title'),
                'Main Subjects': ebook.get('subject')[:3]
            }

        # Increment offset before beginning to crawl subsequent page.
        self.offset += self.page_increment
        yield scrapy.Request(
            url=f"https://openlibrary.org/subjects/fiction.json?limit=12&offset={self.offset}",
            callback=self.parse
        )
