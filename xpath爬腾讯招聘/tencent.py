# -*- coding='utf-8' -*-
from lxml import etree
import requests
import json

url = 'https://hr.tencent.com/position.php?&start=10'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}

output =open('tencent.json','w')
req = requests.get(url,headers=headers)
html = etree.HTML(req.content)

for tr in html.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
    item = {}

    name = tr.xpath('./td[1]/a')[0].text
    detaillink = tr.xpath('./td[1]/a')[0].attrib['href']
    catalog = tr.xpath('./td[2]')[0].text
    recruitnumber = tr.xpath('./td[3]')[0].text
    worklocation = tr.xpath('./td[4]')[0].text
    publishtime = tr.xpath('./td[5]')[0].text

    item['name'] = name
    item['detaillik'] = detaillink
    item['catalog'] = catalog
    item['recruitnumber'] = recruitnumber
    item['worklocation'] = worklocation
    item['publishtime'] = publishtime
    print(type(name))
    
    line = json.dumps(item,ensure_ascii=False)+'\n'
    print(line)
    output.write(line)

output.close()
