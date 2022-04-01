import scrapy
import requests
from scrapy.http import Request
import pymysql as MySQLdb

class PrSpider(scrapy.Spider):
    name = 'vivanuncios'
    start_urls = ['https://www.vivanuncios.com.mx/']

    def __int__(self, * args, **kwargs):
        super(PrSpider, self).__init__(*args, **kwargs)
        self.domain_url = 'https://www.vivanuncios.com.mx/'

    def parse(self, response):
        link1 = ''.join(response.xpath('//head/link[@rel="next"]/@href').extract())
        url = https://www.vivanuncios.com.mx + link1
        yield Request (url, callback=self.parse_categories)

    def parse_categories(self,response) :
        nodes =  response.xpath('//div//div[@class="tileV2 REAdTileV2 promoted listView"]/div/div').extract()

        for node in nodes :
            link = ''.join(response.xpath('//div/div[@class="viewport-contents"]//@href').getall())
            if 'http' not in link:
                link2 = 'https://www.vivanuncios.com.mx' + link
                yield Request(link2,callback=self.response)
        next_page = response.xpath
