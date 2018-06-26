import requests
from bs4 import BeautifulSoup
import bs4

def get_html(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
    req = requests.get(url,headers=headers)
    print(req.status_code)
    req.encoding = req.apparent_encoding
    soup = BeautifulSoup(req.text,'html.parser')
    with open('maoyan.txt','a') as f:
        for item in soup.select('.board-wrapper')[0].children:
            if type(item) == bs4.element.Tag:
                rank = item.i.string
                name = item.a['title']
                time = item.select('p[class="releasetime"]')[0].string
                f.write('{:<4}\t{:<{4}10}\t{:<8}{}'.format(rank,name,time,'\n',chr(12288)))

def main():
    for i in range(0,91,10):
        url = 'http://www.maoyan.com/board/4?offset='+str(i)
        get_html(url)
if __name__=='__main__':
    main()
