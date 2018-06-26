# -*- coding : 'utf-8' -*-
import requests
from lxml import etree
import re
import time
#首次运行时间 133.513033

#得到单词页面的html文档
def get_html(url):
    try:
        req = requests.get(url)
        req.raise_for_status()
        html = etree.HTML(req.content)
        return html
    except:
        return ""

#在初始URL下，得到所有单词页面的链接    
def get_url(inti_url):
    html = get_html(inti_url)
    #xpath返回的就是一个list，我还定义了一个u_list,去添加xpath的返回对象，导致后面出错。
    u_list = (html.xpath('//td[@height="30"]/a/@href'))
    url_list = []
    #每个字母开头的单词不止一页，其他链接在单词页面中，也需提取，整合成一个完整的url_list
    for u in u_list:
        html = get_html(u)
        result = html.xpath('//div[@class="pgbar pg"]/a/@href')[1:-2]
        for i in result:
            url_list.append(i)
    return url_list

#对单词页面进行数据提取       
def get_content(html,position=3):
    #在详细单词页，发现有两种规则模式，故添加位置参数，进行转换
    xp = '//div[@class="mt40"]/'+re.sub('\d',str(position),'p[position()>3]',)
    result = html.xpath(xp)
    for p in result:
        text = p.text.strip()
        #可以用format控制输出，效果更好
        print('     /'.join(re.split('[/\[\]]',text)))

def main():
    start = time.clock()
    inti_url = ('http://news.koolearn.com/20180312/1146258.html')
    url_list = get_url(inti_url)
    print(len(url_list))
    count = 0
    #发现规则模式在两种模式中跳转，故添加循环控制
    while count<len(url_list):
        try:
            for url in url_list[count:]:
                html = get_html(url)
                get_content(html)
                count+=1
        except:
            print('捕获异常，模式跳转')
        try:
            for url in url_list[count:]:
                count+=1
                html = get_html(url)
                get_content(html,5)
        except:
            print('捕获异常，模式跳转')
    end = time.clock()
    print('runtime %f'%(end-start))
        
if __name__=="__main__":
    main()
