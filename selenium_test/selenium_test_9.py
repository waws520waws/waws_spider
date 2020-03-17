# encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

"""
selenium 模拟键盘进行操作
"""
driver = webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("hello")
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
time.sleep(5)

# 发送组合键,ctrl+a  完成全选功能
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"a")

# 全选+回退--完成清空功能
time.sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)


time.sleep(5)
driver.close()