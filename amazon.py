import scrapy
from scrapy.selector import Selector
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from datetime import datetime




class PrSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.in']
    start_urls = ['https://www.amazon.in/s?k=inspirational+books&crid=1DMU0AE9X9O70&sprefix=inspirational%2Caps%2C480&ref=nb_sb_ss_ts-doa-p_1_13' ]

    def parse(self, response):
        
        import pdb;pdb.set_trace()
        title=response.xpath('//span[@class="a-size-medium a-color-base a-text-normal"]/text()').extract()
        price = response.xpath('//span/span[@class="a-price-whole"]/text()').extract()
        author = response.xpath('//div/a[@class="a-size-base a-link-normal s-link-style"]/text()').extract()
        released = response.xpath('//div/span[@class="a-size-base a-color-secondary a-text-normal"]/text()').extract()

        row_data = zip(title, rice,author,released)
        for item in row_data:
            import pdb; pdb.set_trace()
            # create dictionary for storing the scraped info
            scraped_info = {
                # key:value
                'title': item[1],
                'price': item[1],
                'author': item[1],
                'released' : item[1],
               }
