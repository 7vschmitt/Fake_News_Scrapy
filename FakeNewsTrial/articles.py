# -*- coding: utf-8 -*-
# Spider 1: Scraping all the urls to the articles on one Fact Checker
# Fact Checker: FullFact (fullfact.org)
# Link to article: https://towardsdatascience.com/web-scraping-news-articles-to-build-an-nlp-data-pipeline-92ec6083da2

import scrapy
from scrapy.http import Request
from FakeNewsTrial.items import FakenewstrialItem

class ArticlesSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['fullfact.org']
    start_urls = ['http://fullfact.org/']

    def start_request(selfself):
    url ="https: //fullfact.org/" #not so sure why this is necessary
    link_urls = [url.format(i) for i in range(0, 500)]
    for link_url in link_urls:
        print(link_url)

    #HTML content:
    request=Request(link_url, cookies={'store_language':'en'}),
    callback=self.parse_main_pages)
    yield request #usually I get an error here (outside function, must be used inside function)

    def parse_main_pages(self,respone):
    item=FakenewstrialItem()

    #get HTML content where the article linkes are stored
    content=response.xpath('//dic[@id="items"]//div[@class="article-meta]')
    #here comes the tricky part: we need to define the tag = id and the attribute = article-meta with respect to the classes defined in the html code of the website
    #and the tags and attributes might differ among the different html code of the Fact Checker websites
    #the html code of the example news page used in the article has the well defined div class="article-meta", and also div id, so these are the two items we need to define regarding on the Fact Chekcer
    #sourcecode of example website: view-source:https://www.trtworld.com/

    #loop through each article link in HTML content
    for article_link in content.xpath('.//a'):
        item['article_url']=article_link.xpath('.//@href').extract_first()
        #this can be actually used like that here we extract the hrfs without the html code
    item['article_url']="https://fullfact.org/"+item['article_url']
    yield(item)

    def parse(selfself, response):
        pass