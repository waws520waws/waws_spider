# encoding:utf-8

"""
打码识别
虚拟手机号
短信验证码

"""

from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("mobileEmulation",{"deviceName":"iPhone X"})
driver = webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe",chrome_options=options)

driver.get("https://www.jd.com")
time.sleep(2)
driver.find_element_by_id("msShortcutLogin").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@report-eventid=\"MLoginRegister_SMSVerification\"]").click()
time.sleep(3)
user_name = driver.find_element_by_id("username")
user_name.send_keys("xxxxx")
pwd = driver.find_element_by_id("pwd")
pwd.send_keys("xxxxx")
driver.find_element_by_xpath("//*[@report-eventid=\"MLoginRegister_Login\"]").click()
time.sleep(20)
driver.save_screenshot("jdhere.jpg")
driver.close()
