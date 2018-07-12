# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo 
import json
class DoubanPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        sheetname = settings['MONGODB_SHEETNAME']
        #self.filename = open('douban.json','w')        
        
        self.client = pymongo.MongoClient(host=host,port=port)
        self.db = self.client[dbname]
        self.post = self.db[sheetname]
                
    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        #data = json.dumps(dict(item),ensure_ascii=False)+'\n'
        #self.filename.write(data)
        return item
