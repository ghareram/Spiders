import scrapy
import requests
from scrapy.http import Request
import pymysql as MySQLdb

import pymysql
conn = pymysql.connect


insert_query = "insert into ussecurity(date,video_running_time,description) values(%s, %s, %s)"
conn = MySQLdb.connect(host='localhost', user='hare', password='Ram@1234', db='dbussecurity')
cursor = conn.cursor()


class PrSpider(scrapy.Spider):
    name = 'ussecurities'
    #allowed_domains = ['sec.gov']
    start_urls = ['https://www.sec.gov/page/news']

    def __init__(self, *args, **kwargs):
        super(PrSpider, self).__init__(*args, **kwargs)
        self.domain_url = 'https://www.sec.gov/page/news'
	

    def parse(self, response):
        #import pdb;pdb.set_trace()
        link = ''.join(response.xpath("//li[@class='menu__item is-active is-leaf leaf ']/a[contains(@href,'videos')]/@href").extract())
        url = 'https://sec.gov' + link
        yield Request(url, callback=self.parse_categories) 

    def parse_categories(self, response):
        #import pdb;pdb.set_trace()
        nodes = response.xpath('//div[@class="views-view-grid horizontal cols-3 clearfix"]/div/div')
        next_page = response.xpath('//ul//li[@class="pager__item"]/a/@href').getall()
        
        for node in nodes:
            date = ''.join(node.xpath('.//time[@class="datetime"]/text()').extract())
            video_running_time = ''.join(node.xpath('.//span[@class="field-content-runtime"]/text()').extract())
            description = ''.join(node.xpath('.//div[@class="field-content"]/a/text()').extract())
            #video_running_time = ''.join(response.xpath('//div/span[@class="field-content-runtime"]/text()').getall())
            #video_details = ''.join(response.xpath('//div/p/text()').getall())

            values = (date,video_running_time,description)
            print(values)

            cursor.execute(insert_query, values)
            conn.commit()

        if next_page:
            for i in next_page:
                #import pdb;pdb.set_trace()
                next_page1 = 'https://www.sec.gov/news/sec-videos' + i
                print(next_page1)
                yield Request(next_page1, callback=self.parse_categories) 
        """if next_page2:
            for j in next_page2:
                next_page3 = 'https://www.sec.gov' + j
                print(next_page2)
                yield Request(next_page3, callback=self.parse_categories)"""
