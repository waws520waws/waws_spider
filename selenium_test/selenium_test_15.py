# encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

"""
跳转到提示框
switch_to.alert.accept()
"""

driver = webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
driver.get("https://www.baidu.com")
time.sleep(3)
above = driver.find_element_by_link_text(u"设置")
ActionChains(driver).move_to_element(above).perform()
time.sleep(1)
driver.find_element_by_link_text("搜索设置").click()
time.sleep(1)
driver.find_element_by_id("sh_1").click()
driver.find_element_by_link_text(u"保存设置").click()

time.sleep(2)

# 这个功能暂时性并没有测通过
driver.switch_to.alert.accept()
time.sleep(10)

driver.close()