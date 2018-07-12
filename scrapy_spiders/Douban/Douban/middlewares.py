# -*- coding:utf-8 -*-

from Douban.settings import Useragents,Proxies
import random
import base64

class RandomUseragentMiddleware(object):
    
    def __init__(self):
        self.useragent = random.choice(Useragents)
    
    def process_request(self,request,spider):
        request.headers.setdefault('User-Agent',self.useragent)
        return request

class RandomProxyMiddleware(object):
    
    def __init__(self):
        self.proxy = random.choice(Proxies)
    
    def process_request(self,request,spider):
        if self.proxy['user_passwd'] is None:
            request.meta['proxy'] = 'http://'+self.proxy['ip_port']
        else:
            b64userpd = base64.b64encode(self.proxy['user_passwd'])
            request.meta['proxy'] = 'http://'+self.proxy['ip_port']
            request.headers['Proxy_Authorization'] = 'Basic'+b64userpd
