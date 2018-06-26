import bs4
from bs4 import BeautifulSoup
import requests,lxml
import re

url_list =[]
def get_index_html(url):
    req = requests.get(url)
    req.encoding = req.apparent_encoding
    soup = BeautifulSoup(req.text,'lxml')
    question = ''.join(list(soup.select('.question_text')[0].pre.stripped_strings))
    answer = ''.join(list(soup.select('.answer_text')[0].span.stripped_strings))
    time = soup.select('span[class="time mr10"]')[0].string
    print('时间：%s 问题：%s\n优秀回答：%s'%(time,question,answer))

def get_url(url1):
    req = requests.get(url1)
    req.encoding = req.apparent_encoding
    soup = BeautifulSoup(req.text,'lxml')

    for i in soup.select('.list-group')[0].children:
        if isinstance(i,bs4.element.Tag):
            url_list.append(i.select('.question-title')[0].a['href'])
    return url_list

url1 = 'https://iask.sina.com.cn/c/74-all-1-new.html'
#get_url(url1)
#for i in url_list:
    #url = 'https://iask.sina.com.cn'+i
    #get_index_html(url)
get_index_html('https://iask.sina.com.cn/b/iRq5uli3CL6Z.html')
