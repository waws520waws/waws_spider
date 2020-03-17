# encoding:utf-8
import selenium
import selenium.webdriver
import time

"""
无界面浏览器
作用：我们在前台开放太多的浏览器资源并不是一个明智的选择，这样可以使用无界面浏览器进行替代
"""
path = "../driver/phantomjs.exe"
driver = selenium.webdriver.PhantomJS(path)
driver.get("http://www.qq.com")
time.sleep(3)
driver.save_screenshot("qq.jpg")
print(driver.title)
print(driver.page_source)
driver.close()