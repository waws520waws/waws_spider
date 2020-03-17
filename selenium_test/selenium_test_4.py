# encoding:utf-8
import selenium
import selenium.webdriver
import time

# driver = selenium.webdriver.Chrome("C:\Users\zuoyikeji\Desktop\chromedriver.exe")
# driver1 = selenium.webdriver.Firefox("../driver/geckodriver.exe")
# driver2 = selenium.webdriver.Ie("../driver/IEDriverServer.exe")
"""
selenium登录博客园的程序：自动判断登录成功还是失败
"""

def login(username,password):
    driver = selenium.webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
    driver.get("https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fwww.cnblogs.com%2F")
    time.sleep(3)
    name_elem = driver.find_element_by_id("LoginName")
    pwd_elem = driver.find_element_by_id("Password")
    name_elem.send_keys(username)
    pwd_elem.send_keys(password)
    time.sleep(3)
    button_elem = driver.find_element_by_id("submitBtn")
    button_elem.click()
    time.sleep(10)
    pagesource = driver.page_source
    return pagesource.find(u"退出") != -1

print(login("xxx","xxxxx"))