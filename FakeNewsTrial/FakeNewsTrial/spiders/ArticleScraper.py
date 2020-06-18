# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class ArticlescraperSpider(CrawlSpider):
    name = 'ArticleScraper'
    allowed_domains = ['fullfact.org']
    start_urls = ['http://fullfact.org/']
    rules = (
            Rule(LinkExtractor(), callback='parse_item', follow=True),
        )

    def parse_item(self, response):
        filename = response.url.split("/")[-2] + '.html'
        text = response.xpath('//body//p//text()').extract()
        with open(filename, 'wb') as f:
            #f.write(response.body)
            f.write(text)