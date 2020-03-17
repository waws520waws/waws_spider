# encoding:utf-8
from selenium import webdriver
import time

"""
前进/后退操作
"""

options = webdriver.ChromeOptions()
options.add_experimental_option("mobileEmulation",{"deviceName":"iPhone X"})
driver = webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe",chrome_options=options)
# driver.set_window_position(500,1000)
driver.maximize_window()
driver.get("https://www.taobao.com")

time.sleep(5)
driver.get("https://www.jd.com")
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.close()