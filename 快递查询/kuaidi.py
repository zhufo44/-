#-*- coding:utf-8-*-
import requests,json

#程序查询接口使用http://www.kuaidi100.com，使用Wireshark分析http请求，得到快递查询后台交互的大致流程。

def search():
    postid = input('请输入快递单号：')
    req1 = requests.get('http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text='+postid)
    com_name = json.loads(req1.text)['auto'][0]['comCode']
    req2 = requests.get('http://www.kuaidi100.com/query?type='+com_name+'&postid='+postid)
    items = json.loads(req2.text)['data']
    for item in items:
        time  = item['time']
        text = item['context']
        print(time,text)

search()
