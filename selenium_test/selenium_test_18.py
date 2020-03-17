# encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait      # 等待一个元素加载完成
from selenium.webdriver.support import expected_conditions as EC
import time

"""
解决页面加载慢的问题
"""
driver = webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
driver.get("https://www.baidu.com")

"""
函数解析：
5：代表5秒超时
presence_of_all_elements_located接收的参数是一个元组
By.ID，等同于 find...by_id 
"""

driver.implicitly_wait(10)  # 控制操作时间在10s以内

elem = WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.ID,"kw")))
# 最多等15s,直到元素加载

"""
注意这里返回的是一个list
"""
elem[0].send_keys("python")
time.sleep(2)
elem[0].send_keys(Keys.CONTROL,"a")
time.sleep(1)

driver.close()