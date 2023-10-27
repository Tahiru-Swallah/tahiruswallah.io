import scrapy



class FrankoSpider(scrapy.Spider):
    name = "Franko"
    start_urls = ["https://frankotrading.com/product-category/laptops-desktops/?v=6848ae6f8e78"]

    def parse(self, response):
        
        for product in response.css('div.product-loop-wrapper'):
            try:
                yield {
                    'Name': product.css("h2.woocommerce-loop-product__title a::text").get(),
                    "Price": product.css("span.woocommerce-Price-amount.amount::text").get(),
                    "Image-link": product.css("a.woocommerce-LoopProduct-link.woocommerce-loop-product__link img").attrib['src'],
                    'Links': product.css('a').attrib['href']
                }

            except :
                yield {
                    'Name': 'Name not found',
                    "Price": 'Price not found',
                    "Image-link": 'Image not found',
                    'Links': 'Link not found'
                }


        next_page = response.css('a.next.page-numbers').attrib['href']

        if next_page is not None:
            nex_page = response.follow(next_page, callback=self.parse)

            yield nex_page