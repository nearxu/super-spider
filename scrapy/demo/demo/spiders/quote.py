import scrapy
import json


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):

        for quote in response.css('div.quote'):
            item = {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

            # dict => str
            data = json.dumps(item)

            # str => json

            # json.loads(str)
            print(data)
            with open('quote.txt', 'w', encoding='utf-8') as fp:
                w = fp.write(data)
