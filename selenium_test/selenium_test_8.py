# encoding:utf-8


"""
操作js
driver.execute_script(js_str)
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("hello")
driver.find_element_by_id("kw").send_keys(Keys.RETURN)
time.sleep(5)
js = "window.scrollTo(200,550)"
driver.execute_script(js)
time.sleep(5)


driver.quit()