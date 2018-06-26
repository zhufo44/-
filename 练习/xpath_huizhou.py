#-*- coding='utf-8' -*-
import requests
from lxml import etree
import json

def get_html(url):
    req = requests.get(url)
    print(req.status_code)
    html = etree.HTML(req.content)
    return html

def get_data(html):
    result = html.xpath('//div[@id="THE_RESULTS_Grid"]//tr')
    print(len(result))
    
def main():
    url = 'https://piaosanlang.gitbooks.io/spiders/03day/section3.3.html'
    html = get_html(url)
    get_data(html)

if __name__=='__main__':
    main()
    
