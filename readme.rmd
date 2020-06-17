# Web crawler for scraping articles from different Fact Checkers

Scrapy is based on building a DOM tree based on the HTML source and makes use of given CSS or XPATH selectors to find matches in the tree.

## Potential Chellenges:
1. Find appropriate selectors: when the structure of the DOM tree differs in different websites and the CSS and XPATH selectors are not existent on every website, then different spiders are necessary.
2. Often the news articles on a Fact Checker website are only represented by title and very short description. So scraping the article body is not possible from the original website. One solution might be, to create one spider to scrape the corresponding article hrefs and then create a second spider which scrapes the raw text information from all the article hrefs.

https://towardsdatascience.com/web-scraping-news-articles-to-build-an-nlp-data-pipeline-92ec6083da2