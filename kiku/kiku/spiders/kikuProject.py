import scrapy
import json

for i in range(1,6):
    pages = i

class KikukScrapy(scrapy.Spider):
    name = "kiku"
    start_urls = ['https://m.kikuu.com/search/result?belongCategory=814607&kw=Jumpsuits%20&%20Rompers']

    headers = {
            'Accept': '*/*',
            "Accept-Encoding" : 'gzip, deflate, br',
            "Accept-Language" : "en-US,en;q=0.9",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36"
        }


    def parse(self, response):
        for i in range(1, 6):
            url = f'https://www.kikuu.com/api/marketing/products/search?page={i}&pagesize=20&highestPrice=&lowestPrice=&caAttribute=&searchSwitches=&keyWord=Jumpsuits%20&searchSortType=1001&belongCategory=-1&searchOptionItems='
                    
            request = scrapy.Request(url, callback=self.parse_api, headers=self.headers)

            yield request

    def parse_api(self, response):
        raw_data = response.body
        data = json.loads(raw_data)
        
        for name in data["obj"]:
            try:
                yield {
                    'name' : name['productName'],
                    'price' : name['priceUnionShow'],
                    'rating' : name['productScore'],
                    'image-link' : name['productImg0Show']
                }
            except KeyError as e:
                yield {
                    'name' : name['productName'],
                    'price' : name['priceUnionShow'],
                    'rating' : "No rate found",
                    'image-link' : name['productImg0Show']
                }

        
