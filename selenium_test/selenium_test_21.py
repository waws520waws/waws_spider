# encoding:utf-8
from selenium import webdriver
import time

"""
file_down 文件的下载
"""
import os


options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting.popups":0,"download.default_directory":"./"}
options.add_experimental_option("prefs",prefs)
"""
已经下载了：只不过目录不是我们指定的目标目录
下载到了google浏览器自己的默认目录中了：r"C:\\Users\\19663\\Downloads"
"""


driver = webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
driver.get("https://pypi.org/project/selenium/#files")
driver.find_element_by_link_text("selenium-3.141.0.tar.gz").click()
time.sleep(10)
driver.close()