# encoding:utf-8
"""
尝试搞定CSDN
这个也失败了，原因是滑动验证码的问题：没有解决
"""
import selenium
import selenium.webdriver
import time

driver = selenium.webdriver.Chrome(r"C:\Users\zuoyikeji\Desktop\chromedriver.exe")
driver.get("https://passport.csdn.net/login?code=public")
time.sleep(3)
# driver.switch_to.frame("login_frame")
elem = driver.find_element_by_xpath("//*[@class=\"main-select\"]/ul//li[2]/a")
elem.click()
time.sleep(2)

name_elem = driver.find_element_by_id("all")
name_elem.send_keys("xxxxxxx")
time.sleep(1)
pwd_elem = driver.find_element_by_id("password-number")
pwd_elem.send_keys("xxxxx")
time.sleep(1)
but_elem = driver.find_element_by_xpath("//*[@data-type=\"account\"]")
but_elem.click()
time.sleep(8)
logincenter = driver.find_element_by_xpath("//*[@class=\"loginCenter\"]/a")
logincenter.click()
time.sleep(3)

# 提取user信息
username = driver.find_element_by_xpath("//*[@class=\"nick\"]//span[1]").text
print(username)

driver.close()
"""
注意下这种写法：
driver.find_element_by_class_name("xxxxx").get_attribute("src")
"""