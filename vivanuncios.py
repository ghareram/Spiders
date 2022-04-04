import scrapy
import requests
from scrapy.http import Request
import pymysql as MySQLdb

import pymysql
conn = pymysql.connect


insert_query = "insert into vivanuncios(title, Estatus, MetrosCuadrados, Recámara, Baños, MedioBaños, Garage, AñodeConstruccion, SuperficieTotal, Entrega, Ubicación, longitude, latitude) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
conn = MySQLdb.connect(host='localhost', user='hare', password='Ram@1234', db='vivanuncios')
cursor = conn.cursor()

class PrSpider(scrapy.Spider):
    name = 'vivanuncios'
    start_urls = ['https://www.vivanuncios.com.mx/s-renta-inmuebles/v1c1098p1']

    def __int__(self, * args, **kwargs):
        super(PrSpider, self).__init__(*args, **kwargs)
        self.domain_url = 'https://www.vivanuncios.com.mx/'

    def parse(self,response) :
        #import pdb;pdb.set_trace()
        nodes =  response.xpath('//div//div[@class="tileV2 REAdTileV2 promoted listView"]/div/div').extract()

        for node in nodes :
            links = response.xpath('//div/div[@class="viewport-contents"]//@href').getall()
            for link in links:
                if 'http' not in link:
                    link2 = 'https://www.vivanuncios.com.mx' + link
                    yield Request(link2,callback=self.response)
        next_page = response.xpath('//div//span/a/@href').extract()

        if next_page:
            for i in next_page:
                next_page1 = 'https://www.vivanuncios.com.mx' + i
                print(next_page1)
                yield Request(next_page1, callback=self.parse)

    def response(self,response) :
        #import pdb;pdb.set_trace()
        title = ''.join(response.xpath('.//h1/div[@class="title"]/text()').extract())
        Estatus = ''.join(response.xpath('//span[contains(text(), "Estatus")]//following-sibling::span//text()').getall()).replace(':','')
        MetrosCuadrados = ''.join(response.xpath('//span[contains(text(), "Metros Cuadrados")]//following-sibling::span//text()').getall()).replace(':','')
        Recámara = ''.join(response.xpath('//span[contains(text(), "Recámara(s)")]//following-sibling::span//text()').getall()).replace(':','')
        Baños = ''.join(response.xpath('//span[contains(text(), "Baños") and not(contains(text(), "Medio Baños"))]//following-sibling::span//text()').getall()).replace(':','') 
        MedioBaños = ''.join(response.xpath('//span[contains(text(), "Medio Baños")]//following-sibling::span//text()').getall()).replace(':','') 
        Garage = ''.join(response.xpath('//span[contains(text(), "Garage")]//following-sibling::span//text()').getall()).replace(':','')
        AñodeConstruccion = ''.join(response.xpath('//span[contains(text(), "Año de Construccion")]//following-sibling::span//text()').getall()).replace(':','')
        SuperficieTotal = ''.join(response.xpath('//span[contains(text(), "Superficie Total")]//following-sibling::span//text()').getall()).replace(':','')
        Entrega = ''.join(response.xpath('//span[contains(text(), "Entrega")]//following-sibling::span//text()').getall()).replace(':','')
        Ubicación = ''.join(response.xpath('//div[@class="location-name"]/text()').extract()) 
        longitude = ''.join(response.xpath('substring-before(normalize-space(substring-after(//script[contains(., "longitude")]/text(),"latitude")), ",")').extract_first()).replace('":','')   
        latitude = ''.join(response.xpath('substring-before(normalize-space(substring-after(//script[contains(., "latitude")]/text(),"longitude")), ",")').extract_first()).replace('":','').replace('}','')

        values=(title, Estatus, MetrosCuadrados, Recámara, Baños, MedioBaños, Garage, AñodeConstruccion, SuperficieTotal, Entrega, Ubicación, longitude, latitude)
        print(values)
  
        cursor.execute(insert_query, values)
        conn.commit()
