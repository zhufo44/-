import requests
from lxml import etree

headers = {'Cookie': '_zap=0c12594a-0be8-41cb-94e4-dac7b4114706; q_c1=79a0621a33404eeab310d18dee3244f1|1508574740000|1508574740000; d_c0="AACC276XkAyPTslzEy-xuar-ipUMDvJ1YUI=|1508641885"; z_c0=Mi4xV3JmMkJBQUFBQUFBQUlMYnZwZVFEQmNBQUFCaEFsVk45Y2FNV3dBSW1WMWJrWER3LW9RSHpjanFqWUJONENxelJ3|1520400629|9a3b3c48dccf231486d386321ddccb6bd332b8c4; __DAYU_PP=iq6b2ZbQjjzqV6Zb3ibE7cc61072bc54; q_c1=79a0621a33404eeab310d18dee3244f1|1523418316000|1508574740000; aliyungf_tc=AQAAALxE/24pxAkA1hiTb8XwyL7nkZIS; _xsrf=77fbf582-0dd3-466f-81ab-d7ce66b2617f; __utma=51854390.519137210.1524231653.1524231653.1524231653.1; __utmb=51854390.0.10.1524231653; __utmc=51854390; __utmz=51854390.1524231653.1.1.utmcsr=testclass.net|utmccn=(referral)|utmcmd=referral|utmcct=/crawler/selenium_crawler/; __utmv=51854390.100--|2=registration_date=20170515=1^3=entry_date=20170515=1','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
req = requests.get('https://www.zhihu.com/explore',headers=headers)

html = etree.HTML(req.content)
result = html.xpath('//a[@class="question_link"]')
for i in result:
    text = i.text.strip()
    href = 'https://www.zhihu.com'+i.attrib['href']
    print(text,href)
