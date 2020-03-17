# encoding:utf-8
"""
模拟登录CSDN
"""
import selenium
import selenium.webdriver
import selenium.webdriver.common.keys
import time


driver = selenium.webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
driver.get("https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fwww.cnblogs.com%2F")
elem = driver.find_element_by_id("LoginName")
elem.send_keys("*******")
elem2 = driver.find_element_by_id("Password")
elem2.send_keys("******")
time.sleep(3)
elem2.send_keys(selenium.webdriver.common.keys.Keys.RETURN)
time.sleep(10)
pagesource = driver.page_source
print(pagesource)


time.sleep(20)
driver.close()