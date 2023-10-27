import scrapy

class ComputerScrapy(scrapy.Spider):
    name = "computer"
    start_urls = ['https://compughana.com/phones-tablets/tecno.html?product_list_limit=24']

    def parse(self, response):
        for products in response.css('div.product-item-info.type1'):
            try:
                yield {
                    'name': products.css('a.product-item-link::text').get(),
                    'price': products.css('span.price::text').get().replace('₵', ''),
                    'links': products.css('a.product-item-link').attrib['href'],
                    'Image_link': products.css('a img.product-image-photo.default_image.porto-lazyload').attrib['data-src'],
                } 
            except:
                yield {
                    'name': products.css('a.product-item-link::text').get(),
                    'price':'Sold out',
                    'links': products.css('a.product-item-link').attrib['href'],
                    'image_link': 'Image not found',
                }