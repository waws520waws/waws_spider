# encoding:utf-8
"""
selenium的使用

"""
import selenium
import urllib
import selenium.webdriver
import selenium.webdriver.common.keys
import time

"""
步骤：
    1.开启webdriver对象
    2.get获取网页信息
    3.通过元素定位想要的位置信息
    4.send_keys输入想要输入的信息
    5.按键进行操作
"""

driver = selenium.webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
driver.get("http://www.baidu.com")
elem = driver.find_element_by_id("kw")


elem.send_keys("python")
time.sleep(3)
elem.send_keys(selenium.webdriver.common.keys.Keys.RETURN)


time.sleep(20)
driver.close()
