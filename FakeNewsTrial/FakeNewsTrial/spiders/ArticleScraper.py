# -*- coding: utf-8 -*-
import scrapy


class ArticlescraperSpider(scrapy.Spider):
    name = 'ArticleScraper'
    allowed_domains = ['fullfact.org']
    start_urls = ['http://fullfact.org/']

    def parse(self, response):
        pass
