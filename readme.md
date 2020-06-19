# Web crawler for scraping articles from different Fact Checkers


#Scrapy
Scrapy is based on building a DOM tree based on the HTML source and makes use of given CSS or XPATH selectors to find matches in the tree.

## Potential Chellenges:
1. Find appropriate selectors: when the structure of the DOM tree differs in different websites and the CSS and XPATH selectors are not existent on every website, then different spiders are necessary.
2. Often the news articles on a Fact Checker website are only represented by title and very short description. So scraping the article body is not possible from the original website. One solution might be, to create one spider to scrape the corresponding article hrefs and then create a second spider which scrapes the raw text information from all the article hrefs.

https://towardsdatascience.com/web-scraping-news-articles-to-build-an-nlp-data-pipeline-92ec6083da2

## Scrapy Selectors
https://docs.scrapy.org/en/latest/topics/selectors.html 


# Newspaper 
is a python library to extract and curate articles from newspapers and similar websites
(if you want to install it use pip install newspaper3k, otherwise you get the python 2 deprecated version)
https://newspaper.readthedocs.io/en/latest/ 

It has following features: 

 - Multi-threaded article download framework
 - News url identification
 - Text extraction from html
 - Top image extraction from html
 - All image extraction from html
 - Keyword extraction from text
 - Summary extraction from text
 - Author extraction from text
 - Google trending terms extraction

List of supported languages: 

| input code   | full name |
| ------------- | ------------- |
| nl  | Dutch  |
| zh  | Chinese |
| vi  | Vietnamese |
| no  | Norwegian |
| ar  | Arabic  |
| tr  | Turkish |
| sr  | Serbian |
| fr  | French |
| ru  | Russian  |
| en  | English |
| hi  | Hindi  |
| ja  | Japanese |
| sw  | Swahili  |
| pl  | Polish |
| fa  | Persian  |
| el  | Greek |
| sv  | Swedish |
| sl  | Slovenian |              
| de  | German |                           
| it  | Italian |                           
| pt  | Portuguese |                          
| he  | Hebrew |                           
| hr  | Croatian |                         
| et  | Estonian |                           
| id  | Indonesian |                          
| ro  | Romanian |                           
| es  | Spanish |                          
| ko  | Korean |                           
| hu  | Hungarian |                         
| da  | Danish |                           
| fi  | Finnish |                          
| bg  | Bulgarian |                           
| be  | Belarusian |  
| mk  | Macedonian |                           
| nb  | Norwegian (Bokmål) |                         
| uk  | Ukrainian |                           
                        
                    
 ## Potential Challenges: 
 
 it actually solves the problems of scrapy. Only the languages need to be stated explicitly in the scraper.py. So probably need to create different scripts for each language (?).
 
 ## Feedparser                  
 Nespaper can be used in combination with the feedparser library, which has one primary public function, parse. parse takes a number of arguments, but only one is required, and it can be a URL, a local filename, or a raw string containing feed data in any format.       
 Feedparser is somehow complementary to the selectors of Scrapy, but it is not necessary to look them up seperately for each html structure of different websites, it automatically detects the different items, which can be choosen beforehand in the Scraper.py script. 
 
 For example, the most commonly used elements in RSS feeds (regardless of version) are title, link, description, publication date, and entry ID                   
                        
                        

