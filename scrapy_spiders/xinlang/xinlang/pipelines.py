# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XinlangPipeline(object):
    def process_item(self, item, spider):
        article_url = item['article_url']
        filename = article_url[7:-6].replace("/",'_')
        filename += ".txt"

        f = open(item['sub_filepath']+'/'+filename,'w')
        f.write(item['content'])
        f.close()
        
        return item
