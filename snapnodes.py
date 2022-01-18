import scrapy
from scrapy.selector import Selector
from twisted.internet import reactor
from scrapy. crawler import CrawlerRunner

class PrSpider(scrapy.Spider):
    name ='snapdeal'
    allowed_domains = ['snapdeal.com']
    start_urls = ['https://www.snapdeal.com/search?keyword=technology%20books&santizedKeyword=techology+books&catId=0&categoryId=0&suggested=false&vertical=p&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy']

    def parse(self, response):
        sel = Selector(response)
        import pdb; pdb.set_trace()
        node=sel.xpath('//div//section//div/div[@class="product-tuple-description "]') 

        for i in node :
            #import pdb; pdb.set_trace()
            title = i.xpath('.//div/a/p[@class="product-title"]/text()').extract()
            price = i.xpath('.//div/span[@class="lfloat product-price"]/text()').extract()
            author = i.xpath('.//div/a/p[@class="product-author-name"]/text()').extract()

            values = [title,price,offer]
            print(values)

