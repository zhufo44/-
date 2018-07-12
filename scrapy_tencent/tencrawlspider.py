# -*- coding=utf-8 -*-
#在原来的spider是基于basic，提取下一页的链接使用参数for循环判断，并且需要使用scrapy.Request重新发起请求
#基于CrawlSpider,rule对象可以自动实现链接跟进，发送request。
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class tencenttspider(CrawlSpider):
    name = "tencent"
    allowed_domains = ['centent.com']
    start_urls = ['']

    rules = [
            Rule(linkextractor(allow(),callback=tencentparse,follow=True)),
            ]

    def tencentspider(self,response):
        pass
