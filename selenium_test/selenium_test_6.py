# encoding:utf-8
import selenium
import selenium.webdriver
import time

"""
QQ空间
第一个问题：
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"[id="switcher_plogin"]"}

QQ空间并没有登陆成功
"""
path = r"C:\Users\19663\Desktop\chromedriver.exe"
driver = selenium.webdriver.Chrome(path)
driver.get("https://qzone.qq.com")
time.sleep(5)
driver.switch_to.frame("login_frame")
a_elem = driver.find_element_by_id("switcher_plogin")
a_elem.click()
time.sleep(1)
name_elem = driver.find_element_by_id("u")
name_elem.send_keys("xxxxxx")
pwd_elem = driver.find_element_by_id("p")
pwd_elem.send_keys("xxxxx")
button_elem = driver.find_element_by_id("login_button")
button_elem.click()
time.sleep(3)

print(driver.page_source)
# driver.close()