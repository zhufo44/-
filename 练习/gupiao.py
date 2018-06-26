#-*- coding='utf-8' -*-
import requests
from lxml import etree
import threading
from queue import Queue

class thread_crawl(threading.Thread):
    def __init__(self,threadID,url_q,data_q):
        threading.Thread.__init(self)
        self.threadID = threadID
        self.url_q = url_q
        self.data_q = data_q
    def run(self):
        url = self.url_q.get()
        req = requests.get(url)
        self.data_q.put(req.content)
        print('线程%s进行HTML文档爬取'%self.threadID)

class url_thread(threading.Thread):
    def __init__(self,inti_url,url_q):
        threading.Thread.__init__(self)
        self.inti_url = inti_url
        self.url_q = url_q
    def run(self):
        req = requests.get(self.inti_url)
        html = etree.HTML(req.content)
        u_list = html.xpath('//td[@height="30"]/a/@href')
        for u in u_list:
            req = requests.get(u)
            html = etree.HTML(req.content)
            result = html.xpath('//div[@class="pgbar pg"]/a/@href')[1:-2]
            self.url_q.put(result)
def main():
    inti_url = 'http://news.koolearn.com/20180312/1146258.html'
    url_q = Queue()
    data_q = Queue()

    thread1 = url_thread(inti_url,url_q)
    thread1.start()
    thread1.join()
    print(url_q.qsize())
if __name__ == '__main__':
    main()
