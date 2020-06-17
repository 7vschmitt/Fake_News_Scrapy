# -*- coding: utf-8 -*-
import scrapy


class ArticlesSpider(scrapy.Spider):
    name = 'articles'
    start_urls = ['http://fullfact.org/']

    def parse(self, response):
        pass
