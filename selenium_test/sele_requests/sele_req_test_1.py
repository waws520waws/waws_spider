# encoding:utf-8
"""
使用selenium实现cookie的抓取，登录不需要加密，抓取到cookie之后在使用requests库
携带着cookie对网页进行访问
——————作为网页登陆的最终解决方式

cookie的两个问题：
    1.时效性的问题
    2.有的时候是依靠着IP进行加密的
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import requests
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
driver.get("https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fsearch.jd.com%2FSearch%3Fkeyword%3Dvostro%25205370%26enc%3Dutf-8%26wq%3Dvostro%25205370%26pvid%3D1adb9739cb7c419bbe1bc39592bb5b2b")

WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.LINK_TEXT, u'账户登录')))
driver.find_element_by_link_text(u"账户登录").click()

WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.ID, 'loginname')))
driver.find_element_by_id("loginname").send_keys("xxxxxx")

WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.ID, 'nloginpwd')))
driver.find_element_by_id("nloginpwd").send_keys("xxxxxxx")

WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.ID, 'loginsubmit')))
driver.find_element_by_id("loginsubmit").click()

time.sleep(10)
"""
在这遇到的一个问题就是：在获取cookies的时候需要页面加载完成，否则获取不到完整cookie,在后面也就会出现session登录不上的问题
"""
cks = driver.get_cookies()
"""
拿下来的是列表形式：需要转化成字典的形式才能使用 
在session中，使用set对cookie进行构造
"""
session = requests.session()
for cookie in cks:
    session.cookies.set(cookie["name"],cookie["value"])

print(session.cookies)

session.headers.clear()
html = session.get("https://cart.jd.com/cart.action").text


soup = BeautifulSoup(html,"lxml")
print(soup.select(".item-msg .p-name a")[0].get_text().strip())
time.sleep(1)

driver.close()

