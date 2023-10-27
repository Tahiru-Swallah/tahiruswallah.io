from scrapy.spiders import CrawlSpider, Rule

from scrapy.linkextractors import LinkExtractor

class BookScrapy(CrawlSpider):
    name = 'book'
    allowed_domains = ['toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(allow='catalogue/category')),
        Rule(LinkExtractor(allow='catalogue', deny='category'), callback='parse_item')
    )


    def parse_item(self, response):
        if response.css('.product_main h1::text').get() == None:
            avail = response.css('.instock.availability::text')[1].get().replace('\n','').replace(' ', '')
            yield {
                'title': 'Title not found',
                'price': response.css('.price_color::text').get().replace('£', ''),
                'availability': avail[avail.index('('):].replace('(','').replace(')','').replace('available', ''),
            }
        else:
            avail = response.css('.instock.availability::text')[1].get().replace('\n','').replace(' ', '')
            yield {
                'title': response.css('.product_main h1::text').get(),
                'price': response.css('.price_color::text').get().replace('£', ''),
                'availability': avail[avail.index('('):].replace('(','').replace(')','').replace('available', ''),
            }