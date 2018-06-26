from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://qzone.qq.com')
sleep(1)
driver.switch_to_frame('login_frame')
sleep(1)
driver.find_element_by_id('switcher_plogin').click()
sleep(1)
driver.find_element_by_id('u').send_keys('')
driver.find_element_by_id('p').send_keys('')
sleep(1)
driver.find_element_by_id('login_button').click()
    
