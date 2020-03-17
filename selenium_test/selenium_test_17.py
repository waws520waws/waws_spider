# encoding:utf-8

from selenium import webdriver
import time



"""
cookie的相关操作
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("hello")
driver.find_element_by_id("kw").send_keys(Keys.RETURN)
time.sleep(5)

driver.add_cookie({"name":"hahah","value":"babba"})

cks = driver.get_cookies()
print(cks)
driver.quit()