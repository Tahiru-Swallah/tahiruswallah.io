import scrapy
import json


class SunSpider(scrapy.Spider):
    name = "sun"
    start_urls = ["https://www.sunglasshut.com/wcs/resources/plp/10152/byCategoryId/3074457345626651837?isProductNeeded=true&isChanelCategory=false&pageSize=18&responseFormat=json&currency=USD&viewTaskName=CategoryDisplayView&storeId=10152&pageView=image&catalogId=20602&top=Y&beginIndex=0&h5e=dec71031a9a88ccf5c15fec0d26c912d&langId=-1&categoryId=3074457345626651837&cid=CM-ENL_20231016-SGHNATrendSheerShades2_22551425&orderBy=default&currentPage=1"]

    def parse(self, response):
        raw_data = response.body
        data = json.loads(raw_data)

        for k in data['plpView']['products']['products']['product']:
            yield {
                'name': k['name']
                }

        next_page = data["plpView"]['nextPageURL']

        if next_page != None:
            next_page = response.urljoin(next_page)

            requests = scrapy.Request(next_page, callback=self.parse)

            yield requests


        