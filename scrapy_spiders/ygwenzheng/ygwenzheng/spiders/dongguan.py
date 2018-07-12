# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ygwenzheng.items import YgwenzhengItem
import re

class DongguanSpider(CrawlSpider):
    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/sheqing?page=0']

    rules = (
        Rule(LinkExtractor(allow=r'show\?id=\d+'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'page=\d+'))
    )

    def parse_item(self, response):
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        item = YgwenzhengItem()
        
        u1 = response.xpath('//td[@valign="bottom"]/text()').extract()[0]
        u2 = re.split(r'[\],:]',u1)
        item['title'] = u2[2]
        item['num'] = u2[1]
        item['text'] = response.xpath('//td[@id="content1"]/text()').extract()[0].strip('\xa0')
        item['link'] = response.url
        
        yield item
