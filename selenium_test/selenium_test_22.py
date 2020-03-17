# encoding:utf-8
"""
爬取快代理的所有的ip:port
"""
from selenium import webdriver
import time

for i in range(100):
    url = "https://www.kuaidaili.com/free/inha/"
    driver = webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
    url = url + str(i+1) + "/"
    driver.get(url)
    time.sleep(1)
    data = driver.find_elements_by_xpath("//tbody//tr")
    for da in data:
        ip = da.find_element_by_xpath("./td[1]").text
        port = da.find_element_by_xpath("./td[2]").text
        print(ip + ":" + port)
    print("第" + str(i+1) + "页下载完成")
    driver.close()
    break