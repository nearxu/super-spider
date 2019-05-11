# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy.selector import Selector
from demo.items import DemoItem
import time


class MoiveSpider(CrawlSpider):
    name = 'moive'
    allowed_domains = ['moive.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    # rules = (
    #     Rule(LinkExtractor(allow=(r'https://movie.douban.com/top250\?start=\d+.*'))),
    #     Rule(LinkExtractor(allow=(r'https://movie.douban.com/subject/\d+')),
    #          callback='parse_item'),
    # )

    def parse_item(self, response):
        print(response, 'response')
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        time.sleep(3)
        li_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for li in li_list:
            item = DemoItem()
            item['title'] = li.xpath(
                'div/div[2]/div[1]/a/span[1]/text()').extract_first()
            item['score'] = li.xpath(
                'div/div[2]/div[2]/div/span[2]/text()').extract_first()
            item['motto'] = li.xpath(
                'div/div[2]/div[2]/p[2]/span/text()').extract_first()
            yield item
