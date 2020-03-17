# encoding:utf-8
"""
提取网页的所有文本
"""
from selenium import webdriver
import time

url = "https://www.51shucheng.net/guanchang/erhaoshouzhang/erhaoshouzhang1/1730.html"
driver = webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
driver.get(url)
time.sleep(1)
data = driver.find_elements_by_xpath("/*")

for tag in data:
    print(tag.text)

driver.quit()