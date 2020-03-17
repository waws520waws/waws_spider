# encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
driver.get("https://www.baidu.com")

driver.implicitly_wait(10)
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("kw").send_keys(Keys.RETURN)

if driver.find_element_by_class_name("nums").is_displayed():
    print(driver.find_element_by_class_name("nums").text)


driver.close()