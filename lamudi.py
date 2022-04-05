iimport scrapy
import requests
from scrapy.http import Request
import pymysql as MySQLdb


class PrSpider(scrapy.Spider):
    name = 'lamudi'
    start_urls = ['https://www.lamudi.com.mx/for-rent']

    def __int__(self, * args, **kwargs):
        super(PrSpider, self).__init__(*args, **kwargs)
        self.domain_url = 'https://www.lamudi.com.mx/'

    def parse(self,response) :
        nodes =  response.xpath('').extract()


