# encoding:utf-8
import time
from selenium import webdriver
import urllib2
"""
使用selenium 和 urllib2 进行登录京东
csdn 没有搞定
还有一个问题就是：我们down下来的网页出现乱码----待解决 
"""



from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import lxml.etree

driver = webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
driver.get("https://passport.jd.com/uc/login?ltype=logout")

WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.LINK_TEXT, u'账户登录')))
driver.find_element_by_link_text(u"账户登录").click()

WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.ID, 'loginname')))
driver.find_element_by_id("loginname").send_keys("16601203140")

WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.ID, 'nloginpwd')))
driver.find_element_by_id("nloginpwd").send_keys("709103wei")

time.sleep(5)
WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class=\"login-btn\"]/a")))
driver.find_element_by_xpath("//div[@class=\"login-btn\"]/a").click()


time.sleep(10)
cookies = driver.get_cookies()
print(cookies)
cookie_content = ""
for cookie in cookies:
    cookie_content = cookie_content+";"+cookie["name"] +"=" +cookie["value"]

headers = {"Cookie":cookie_content}
request = urllib2.Request("https://cart.jd.com/cart.action",headers = headers)
response = urllib2.urlopen(request)
new_page = response.read()

print(new_page)

driver.close()