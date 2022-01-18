import scrapy
from scrapy.http import FormRequest, Request
from scrapy.selector import Selector
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.response import open_in_browser
import requests
import json
import pymysql as MySQLdb

import pymysql
conn = pymysql.connect

insert_query = "insert into dbflipkart(title,price,ratings,description) values(%s, %s, %s, %s)"

conn = MySQLdb.connect(host='localhost', user='hare', password='Ram@1234',
                       db='flipkart')
cursor = conn.cursor()


class PrSpider(scrapy.Spider):
    name = 'dbflip'
    allowed_domains = ['flipkart.com']
    start_urls = ['https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi']

    def parse(self, response):
       sel = Selector(response)
       node = sel.xpath('//div[@class="_1YokD2 _3Mn1Gg"]//div[@class="_1AtVbE col-12-12"]')

       for i in node:
           #import pdb; pdb.set_trace()
           title = i.xpath('//div[@class="_4rR01T"]/text()').extract()
           price = i.xpath('//div[@class="_30jeq3 _1_WHN1"]/text()').extract()
           ratings = i.xpath('//span[@class="_2_R_DZ"]//span/text()').extract()
           description = i.xpath('//div/ul[@class="_1xgFaf"]/li/text()').extract()

           values = (title, price, ','.join(ratings), ','.join(description))
           print(values)

           cursor.execute(insert_query, values)
           conn.commit()

