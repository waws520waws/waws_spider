# encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

"""
下拉菜单的实践
Select(sel).select_by_index(2)
"""

driver = webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
driver.get("https://www.baidu.com")
time.sleep(3)
above = driver.find_element_by_link_text(u"设置")
ActionChains(driver).move_to_element(above).perform()
time.sleep(1)
driver.find_element_by_link_text("搜索设置").click()
time.sleep(1)

sel = driver.find_element_by_id("nr")

Select(sel).select_by_index(2)

time.sleep(2)
driver.close()