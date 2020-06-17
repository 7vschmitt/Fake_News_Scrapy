import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes' #name of spider
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    #variabes should not be changed, we can put in a list of urls

    #create a method: selfreference and the response containing the sourcecode of the website we want to scrape
    #classes, objects and inheritance: new object refer itself inside of a class we need the self argument, response (particular part of the source code)
    def pars(self, response):
        title = response.css('title::text').extract() #css. selector
        yield {'titletext': title} #dictionary key-value


#yield keyword: return keyword usually used inside of a method or function, generator is used by scrapy behind the scenes.

#use terminal to run spider:
#1. navigate to
# the scrapy_trial project
#2. scrapy crawl quotes (the name defined in the class)

#css selectors select tags from the website:
#1. open scrapy shell: type in the terminal: scrapy shell "website"
#2. get response with css selector: response.css("title::text").extract()/ or  response.css("title::text").extract_first() without brackets




