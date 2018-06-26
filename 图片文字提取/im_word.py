from aip import AipOcr
import re
import os
#使用百度ai接口从图片中提取文字
APP_ID ='11002301'
API_KEY ='iWAltZkrgoaQ8OGFc52YG1dR'
SECRET_KEY = '4IXjkArC5T3Kpbu9FBlVCgEBvaWg4xe2'

client = AipOcr(APP_ID,API_KEY,SECRET_KEY)
fp = open(r'捕获.PNG','rb')
img = fp.read()
message = client.basicGeneral(img)

for i in message.get('words_result'):
    print(i.get('words'),end= '')
    
