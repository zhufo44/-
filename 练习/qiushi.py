# -*- coding="utf-8" -*-
import requests
from lxml import etree

def get_html(url):
    try:
        req = requests.get(url)
        req.raise_for_status()
        html = etree.HTML(req.content)
        return html
    except:
        return ""

def get_content(html):
    result = html.xpath('//div[contains(@class,"article block")]//div[@class="content"]/span')
    for i in result:
        text = i.xpath('string(.)').strip()
        print(text)

def main():
    inti_url = 'https://www.qiushibaike.com/8hr/page/1/'
    for i in range(2,10):
        url = inti_url+str(i)
        html = get_html(url)
        get_content(html)

if __name__=="__main__":
    main()
    
