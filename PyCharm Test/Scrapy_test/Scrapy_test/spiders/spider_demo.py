import scrapy


class SpiderDemoSpider(scrapy.Spider):
    name = 'spider_demo'
    # allowed_domains = ['www.w37fhy.cn']
    start_urls = ['https://www.w37fhy.cn/']

    def parse(self, response):
        print(response)
