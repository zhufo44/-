# -*- coding: utf-8 -*-
import scrapy
from Douban.items import DoubanItem

class DbmoviesSpider(scrapy.Spider):
    name = 'dbmovies'
    allowed_domains = ['movie.douban.com']
    url = 'https://movie.douban.com/top250?start='
    offset = 0
    start_urls = [url+str(offset)]

    def parse(self, response):
        item = DoubanItem()
        for li in response.xpath('//div[@class="item"]'):

            item['rank'] = li.xpath('div[@class="pic"]/em/text()').extract()[0]
            item['name'] = li.xpath('div/div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score'] = li.xpath('div/div[@class="bd"]/div[@class="star"]/span[2]/text()').extract()[0]
            abstract = li.xpath('div/div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            
            if len(abstract)!=0:
                item['abstract'] = abstract[0]
            yield item
        if self.offset <225 :
            self.offset+=25
    
        yield scrapy.Request(self.url+str(self.offset),callback=self.parse)
