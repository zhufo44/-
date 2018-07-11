# -*- coding:utf-8 -*-

from scrapy import Spider,Field
from TenCent.items import TencentItem

class TenPosition(Spider):
    name = 'tenposition'
    allowed_domains = ['tencent.com']

    url = 'https://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [url+str(offset)]

    def parse(self,response):

        for tr in response.xpath('//tr/@class="even" | //tr/@class="odd"'):
            item = TencentItem()
            item[posit_name] = tr.xpath('td[1]/a/text()').extract()[0]
            item[posit_link] = tr.xpath('td[1]/a/@href').extract()[0]
            if tr.xpath('td[2]/text()').extract()[0]:
                item[posit_type] = tr.xpath('td[2]/text()').extract()[0]
            else:
                item[posit_type] = None
            item[people_num] = tr.xpath('td[3]/text()').extract()[0]
            item[location] = tr.xpath('td[4]/text()').extract()[0]
            item[pub_time] = tr.xpath('td[5]/text()').extract()[0]

            yield item
        if self.offset < 3740:
            self.offset+=1

        yield scrapy.Request(self.url+str(self.offset),callback=self.parse)
