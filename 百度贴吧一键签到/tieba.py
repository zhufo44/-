from selenium import webdriver
from time import sleep
from aip import AipOcr
import os,re

url = 'https://tieba.baidu.com/'

driver = webdriver.Firefox()
driver.get(url)
sleep(1)
driver.find_element_by_link_text('登录').click()
sleep(2)
driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
sleep(2)
driver.find_element_by_id('TANGRAM__PSP_10__userName').send_keys('帐号')
driver.find_element_by_id('TANGRAM__PSP_10__password').send_keys('密码')
#有时会出现验证码，try except 捕获异常。用screenshot验证码，百度api识别。
try:
    driver.find_element_by_id('TANGRAM__PSP_10__submit').click()
    if driver.find_element_by_id('TANGRAM__PSP_10__verifyCodeImg'):
        driver.find_element_by_id('TANGRAM__PSP_10__verifyCodeImg').screenshot('yz.jpg')
        yzm=''
        APP_ID ='11002301'
        API_KEY ='iWAltZkrgoaQ8OGFc52YG1dR'
        SECRET_KEY = '4IXjkArC5T3Kpbu9FBlVCgEBvaWg4xe2'

        client = AipOcr(APP_ID,API_KEY,SECRET_KEY)
        fp = open(r'yz.jpg','rb')
        img = fp.read()
        message = client.basicGeneral(img)

        for i in message.get('words_result'):
            print(i.get('words'),end='')
            yzm+=str(i.get('words'))
        driver.find_element_by_id('TANGRAM__PSP_10__verifyCode').send_keys(yzm)
        sleep(3)
        driver.find_element_by_id('TANGRAM__PSP_10__submit').click()
except  Exception as e:
    print(e)
finally:   
    sleep(3)
    driver.find_element_by_class_name('onekey_btn').click()
    sleep(1)
    driver.find_element_by_css_selector('a[class="j_sign_btn sign_btn sign_btn_nonmember"]').click()


