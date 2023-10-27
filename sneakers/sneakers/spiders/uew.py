import scrapy


class UewSpider(scrapy.Spider):
    name = "uew"
    start_urls = ["https://www.uew.edu.gh/"]

    def parse(self, response):
        for link in response.css('li.leaf'):
            yield {
                'Quick Access': link.css('a::text').get(),
                'Links': link.css('a').attrib['href']
            }
 