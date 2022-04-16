import scrapy
from scrapy.http import FormRequest, Request
from scrapy.selector import Selector
from scrapy.spiders import Spider
from scrapy.utils.response import open_in_browser
import requests
import json
import pymysql as MySQLdb


class PrSpider(scrapy.Spider):
    name = 'lamudifp'
    allowed_domains = ['lamudi.com.mx']
    start_urls = ['https://www.lamudi.com.mx/for-sale/']

    def parse(self,response) :
        sel = Selector(response)
        #import pdb;pdb.set_trace()
        #node = sel.xpath('//div/div[@class="row ListingCell-row ListingCell-agent-redesign"]')
        #node = sel.xpath('//div[@class="row ListingCell-row ListingCell-agent-redesign"]')
        node = sel.xpath('//div/div[@class="small-12 columns card ListingCell-content js-MainListings-container  ListingCell-wrapper"]')

        for i in node :
            address = ''.join(i.xpath('.//div/h1//text()').extract()).replace('\n','').replace(',','').replace('      ','')
            title = ''.join(i.xpath('.//div/h2[@class="ListingCell-KeyInfo-title"]/text()').get()).replace('\n','').replace('    ','')


            values = [title,address]
            print(values)


       
