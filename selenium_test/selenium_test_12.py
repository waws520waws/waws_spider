# encoding:utf-8
"""
模拟手机端的数据抓取
步骤：
    1.options = webdriver.ChromeOptions()
    2.options.add_experimental_option("mobileEmulation",{"deviceName":"iPhone X"})
    3.wevdriver.Chrome("path",chrome_options = options)
"""
from selenium import webdriver
import time

mobilesetting = {"deviceName":"iPhone X"}
options = webdriver.ChromeOptions()  # 选项
options.add_experimental_option("mobileEmulation",mobilesetting)  # 模拟手机

driver = webdriver.Chrome(r"C:\Users\zuoyikeji\Desktop\chromedriver.exe",chrome_options=options)
driver.set_window_size(500,1000)
driver.maximize_window()   # 全屏
driver.get("https://www.taobao.com")

time.sleep(10)

driver.save_screenshot("taobao.jpg")
driver.close()