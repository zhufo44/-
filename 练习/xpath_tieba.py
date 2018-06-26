# -*- coding='utf-8' -*-

import requests
from lxml import etree
import json

url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB&fr=search'
req = requests.get(url)
print(req.status_code)

html = etree.HTML(req.content)
result = html.xpath('//ul[@id="thread_list"]/li[@data-field]')
print(len(result))

for li in result:
    item = {}
    title = li.xpath('.//a[@rel]')[0].text
    author = li.xpath('.//a[@rel]')[1].text
    text = li.xpath('.//div[@class="threadlist_abs threadlist_abs_onlyline "]')[0].text.strip()
    num = li.xpath('.//span[@class="threadlist_rep_num center_text"]')[0].text

    item['title'] = title
    item['author'] = author
    item['text'] = text
    item['num'] = num
    
    line = json.dumps(item,ensure_ascii=False)
    print(line)
 
