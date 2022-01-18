import scrapy
from scrapy.selector import Selector
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner

class PrSpider(scrapy.Spider):
    name = 'flipkart'
    allowed_domains = ['flipkart.com']
    start_urls = ['https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi'
                ]
    def parse(self, response):
        #import pdb;pdb.set_trace()
        title=response.xpath('//div[@class="_4rR01T"]/text()').extract()
        Price = response.xpath('//div[@class="_30jeq3 _1_WHN1"]/text()').extract()
        ratings= response.xpath('//span[@class="_2_R_DZ"]//span/text()').extract()
        description = response.xpath('//div/ul[@class="_1xgFaf"]/li/text()').extract()

        row_data = zip(title, Price,ratings,description)
        for item in row_data:
            import pdb; pdb.set_trace()
            # create dictionary for storing the scraped info
            scraped_info = {
                # key:value
                'title': item[1],
                'Price': item[1],
                'ratings': item[1],
                'description' : item[1],
               }

