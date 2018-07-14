# -*- coding: utf-8 -*-
import scrapy
import os
from xinlang.items import XinlangItem

class ActiclesSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide']

    def parse(self, response):
        
        items = []

        #所有大类的url和标题
        parent_title = response.xpath('//h3[@class="tit02"]/a/text()').extract()
        parent_url = response.xpath('//h3[@class="tit02"]/a/@href').extract()

        #所有小类的url和标题
        sub_title = response.xpath('//ul[@class="list01"]/li/a/text()').extract()
        sub_url = response.xpath('//ul[@class="list01"]/li/a/@href').extract()
        
        #构建大类的文件夹
        for i in range(0,len(parent_title)):
            parentpath = './Data/'+parent_title[i]
            if (not os.path.exists(parentpath)):
                os.makedirs(parentpath)
            
            #构造小类的文件夹,并将有关参数保存至item容器
            for j in range(0,len(sub_title)):
                item = XinlangItem()
                item['parent_url'] = parent_url[i]
                item['parent_title'] = parent_title[i]
                flag = sub_url[j].startswith(parent_url[i])

                if flag:
                    article_filepath = parentpath+'/'+sub_title[j]
                    if (not os.path.exists(article_filepath)):
                        os.makedirs(article_filepath)
                        
                    item['sub_url'] = sub_url[j]
                    item['sub_title'] = sub_title[j]
                    item['sub_filepath']  = article_filepath
                    items.append(item)

            for item in items:
                yield scrapy.Request(url=item['sub_url'],meta={'meta1':item},callback=self.second_parse)

    #文章详情页提取，对于下一个解析函数用不到的item字段，其实可以不必赋值。
    def second_parse(self,response):
        meta1 = response.meta['meta1']
        items = []
        article_url = response.xpath('//a/@href').extract()
        for i in range(0,len(article_url)):

            flag = (article_url[i].endswith('shtml') and article_url[i].startswith(meta1['parent_url']))
            if flag:
                item = XinlangItem()
                item['parent_url'] = meta1['parent_url']
                item['parent_title'] = meta1['parent_title']
                item['sub_url'] = meta1['sub_url']
                item['sub_title'] = meta1['sub_title']
                item['sub_filepath'] = meta1['sub_filepath']
                item['article_url'] = article_url[i]

                items.append(item)

        for item in items:
            yield scrapy.Request(url=item['article_url'],meta={'meta2':item},callback=self.detailparse)

    def detailparse(self,response):
        item = response.meta['meta2']
        content = ''
        head = response.xpath('//h1[@id="main_title"]/text()').extract()
        content_list = response.xpath('//div[@id="artibody"]/p/text()').extract()

        for text in content_list:
            content += text.strip('\u3000')

        item['head'] = head
        item['content'] = content

        yield item
