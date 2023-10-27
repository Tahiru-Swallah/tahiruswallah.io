import scrapy


class KfcSpider(scrapy.Spider):
    name = "kfc"
    start_urls = ["https://www.kfc.com.gh/?gclid=CjwKCAjw1t2pBhAFEiwA_-A-NLCUSIPWh_IWlRKHvyZnC2RhWpwQz5VG3NK546uccE5w-Rl7PVE5eRoCUd0QAvD_BwE"]

    headers = {
        "Accept": "application/json,text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        'Accept-Language': "en-US,en;q=0.9",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent":" Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36"
    }

    def parse(self, response):
        
        url = ""