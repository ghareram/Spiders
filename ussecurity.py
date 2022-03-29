import scrapy
import requests
from scrapy.http import Request
import pymysql as MySQLdb
from datetime import datetime
from datetime import timedelta

import pymysql
conn = pymysql.connect


insert_query = "insert into ussecurity(date,video_running_time,description,video_details,image_url,video_url) values(%s, %s, %s, %s, %s, %s)"
conn = MySQLdb.connect(host='localhost', user='hare', password='Ram@1234', db='dbussecurity')
cursor = conn.cursor()


class PrSpider(scrapy.Spider):
    name = 'ussecurity'
    #allowed_domains = ['sec.gov']
    start_urls = ['https://www.sec.gov/page/news']

    def __init__(self, *args, **kwargs):
        super(PrSpider, self).__init__(*args, **kwargs)
        self.domain_url = 'https://www.sec.gov/page/news'


    def parse(self, response):
        #import pdb;pdb.set_trace()
        link1 = ''.join(response.xpath("//li[@class='menu__item is-active is-leaf leaf ']/a[contains(@href,'videos')]/@href").extract())
        url = 'https://sec.gov' + link1
        yield Request(url, callback=self.parse_categories)

    def parse_categories(self, response):
        #import pdb;pdb.set_trace()
        nodes = response.xpath('//div[@class="views-view-grid horizontal cols-3 clearfix"]/div/div')
        
        for node in nodes:
            #import pdb;pdb.set_trace()
            link = ''.join(node.xpath('.//div/a/@href').getall())
            if 'http' not in link:
                link2 = 'https://www.sec.gov' + link
                yield Request(link2,callback=self.response)
        next_page = response.xpath('//ul//li[@class="pager__item"]/a/@href').getall()
        if next_page:
            for i in next_page:
                #import pdb;pdb.set_trace()
                next_page1 = 'https://www.sec.gov/news/sec-videos' + i
                print(next_page1)
                yield Request(next_page1, callback=self.parse_categories) 


    def response(self,response):
        #import pdb;pdb.set_trace()
        date = ''.join(response.xpath('//div[@class="article-publishdate"]//span/text()').extract()).replace('Publish Date','')
        video_running_time = ''.join(response.xpath('//div[@class="article-info"]//span/text()').extract()).replace('Video Running Time','')
        description = ''.join(response.xpath('.//h1/text()').extract())
        video_details = ''.join(response.xpath('.//div/p/text()').getall())
        image_url = ''.join(response.xpath('.//div[@class="field_remote_video_url"]//div/iframe/@src').extract())
        video_url = ''.join(response.xpath('.//div[@class="video-embed-field-provider-youtube video-embed-field-responsive-video"]/iframe/@src').extract())
        
        values = (date,video_running_time,description,video_details,image_url,video_url)
        print(values)

        cursor.execute(insert_query, values)
        conn.commit()

