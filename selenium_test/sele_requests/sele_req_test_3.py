# encoding:utf-8
"""
selenium 配合 requests 做12306的抢票程序
"""
# encoding:utf-8

"""
登录12306 获取个人信息

浏览器的关闭可能会导致cookie失效
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

import requests

driver = webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
driver.get("https://kyfw.12306.cn/otn/resources/login.html")

WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.LINK_TEXT, u'账号登录')))
driver.find_element_by_link_text(u"账号登录").click()

WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.ID, 'J-userName')))
driver.find_element_by_id("J-userName").send_keys("xxxxxx")

WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.ID, 'J-password')))
driver.find_element_by_id("J-password").send_keys("xxxxxxx")
time.sleep(5)

WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.LINK_TEXT, u'立即登录')))
driver.find_element_by_link_text(u'立即登录').click()

time.sleep(15)



cookies = driver.get_cookies()

session = requests.session()
for cookie in cookies:
    session.cookies.set(cookie["name"],cookie["value"])

session.headers.clear()

train = session.get("https://kyfw.12306.cn/otn/view/information.html",verify = False).content.decode("utf-8","ignore")

print(train)