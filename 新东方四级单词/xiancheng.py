 # -*- coding : 'utf-8' -*-
import requests
from lxml import etree
import re
import time
import threading
from queue import Queue
#queue队列将多任务分配给多线程，有奇效
#首次运行时间 34.839718
#为了提高效率，后添加了多线程

lock = threading.Lock()
exitFlag = False
html_q = Queue()

#得到单词页面的html文档
class thread_crawl(threading.Thread):
    def __init__(self,threadID,urlq):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.urlq = urlq
    def run(self):
        self.get_html()
        
    def get_html(self):
        while True:
            if self.urlq.empty():
                break
            else:
                try:
                    url = self.urlq.get()
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
                        }
                    req = requests.get(url,headers=headers)
                    html = etree.HTML(req.content)
                    html_q.put(html)
                except Exception as e:
                    print('get_html',e)
                    
class thread_parser(threading.Thread):
    def __init__(self,threadID,html_q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.html_q = html_q
        self.lock = lock
    def run(self):
        while not exitFlag:
            try:
                '''
                调用队列对象的get()方法从队头删除并返回一个项目。可选参数为block，默认为True。
                如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。
                如果队列为空且block为False，队列将引发Empty异常。
                '''
                html = self.html_q.get(False)
                self.get_content(html)
                self.html_q.task_done()
            except:
                pass
    def get_content(self,html):
        position = 5
        xp = '//div[@class="mt40"]/'+re.sub('\d',str(position),'p[position()>3]',)
        result = html.xpath(xp)
        for p in result:
            text = p.text.strip()
            #可以用format控制输出，效果更好
            print('     /'.join(re.split('[/\[\]]',text)))
            
#在初始URL下，得到所有单词页面的链接
def get_ht(url):
    try:
        req = requests.get(url)
        html = etree.HTML(req.content)
        return html
    except:
        return ""
def get_url(inti_url):
    global url_q
    url_q = Queue()
    html = get_ht(inti_url)
    #xpath返回的就是一个list，我还定义了一个u_list,去添加xpath的返回对象，导致后面出错。
    u_list = (html.xpath('//td[@height="30"]/a/@href'))
    #每个字母开头的单词不止一页，其他链接在单词页面中，也需提取，整合成一个完整的url_list
    for u in u_list:
        html = get_ht(u)
        result = html.xpath('//div[@class="pgbar pg"]/a/@href')[1:-2]
        for i in result:
            url_q.put(i)
    return url_q
def main():
    start = time.clock()
    inti_url = ('http://news.koolearn.com/20180312/1146258.html')
    url_qq = get_url(inti_url)
    crawlthreads = []
    crawl_list = ['thread1','thread2','thread3']
    for i in crawl_list:
        thread = thread_crawl(i,url_qq)
        thread.start()
        crawlthreads.append(thread)
    
    parserthreads = []
    parser_list = ['parser1','parser2','parser3']
    for i in parser_list:
        thread = thread_parser(i,html_q)
        thread.start()
        parserthreads.append(thread)
    
    for i in crawlthreads:
        i.join()
    
    global exitFlag
    exitFlag = True
    for i in parserthreads:
        i.join()
    
    print(html_q.qsize())
    end = time.clock()
    print('runtime %f'%(end-start))
        
if __name__=="__main__":
    main()
