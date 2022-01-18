import scrapy
from scrapy.selector import Selector
from twisted.internet import reactor
from scrapy. crawler import CrawlerRunner
from scrapy.http import Request

class PrSpider(scrapy.Spider):
    name ='snaphref'
    allowed_domains = ['snapdeal.com']
    start_urls = ['https://www.snapdeal.com/search?keyword=technology%20books&santizedKeyword=techology+books&catId=0&categoryId=0&suggested=false&vertical=p&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy']

    def parse(self, response):
        sel = Selector(response)
        #import pdb; pdb.set_trace()
        node=sel.xpath('//div//section//div/div[@class="product-tuple-description "]')

        for i in node :
            #import pdb; pdb.set_trace()
            link = ''.join(i.xpath('.//div/a/@href').extract()[0])
            
            print(link)          
            yield Request(link,callback = self.details)
    
    def details(self, response) :
        import pdb; pdb.set_trace()
        title = response.xpath('//div/h1[@class="pdp-e-i-head"]/text()').extract()
        price = response.xpath('//div//span[@itemprop="price"]//text()').extract()
        highlights = response.xpath('//div//div[@class="spec-body p-keyfeatures"]//text()').extract()       
        otherdetails = response.xpath('//div//table//table[@class="product-spec"]//text()').extract()
        description = response.xpath('//div/div[@class="detailssubbox"]//text()').extract()
        termsconditions = response.xpath('//section//div[@class="spec-section expanded"]//text()').extract()
        
        sel = Selector (response)


