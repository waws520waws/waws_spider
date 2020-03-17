# encoding:utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

import requests

driver = webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
driver.get("https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d9k2HYu9&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F")

WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.ID, 'J_Quick2Static')))
driver.find_element_by_id("J_Quick2Static").click()

WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.ID, 'TPL_username_1')))
driver.find_element_by_id("TPL_username_1").send_keys("xxxxx")
time.sleep(2)

WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.ID, 'TPL_password_1')))
driver.find_element_by_id("TPL_password_1").send_keys("xxxxxxx")
time.sleep(2)

WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'J_SubmitStatic')))
driver.find_element_by_id("J_SubmitStatic").click()

time.sleep(5)

"""
淘宝的滑动验证码比较厉害，需要其他方式破解
没有成功
"""

cookies = driver.get_cookies()

session = requests.session()
for cookie in cookies:
    session.cookies.set(cookie["name"],cookie["value"])

session.headers.clear()
data = {"buyerNick":"","dateBegin":0,"dateEnd":0,"lastStartRow":"","logisticsService":"","options":0,"orderStatus":"","pageNum":5,"pageSize":15,"queryBizType":"","queryOrder":"desc","rateStatus":"","refund":"","sellerNick":"","prePageNo":4}
store_json = session.post("https://buyertrade.taobao.com/trade/itemlist/asyncBought.htm?action=itemlist/BoughtQueryAction&event_submit_do_query=1&_input_charset=utf8",data = data).text
json_data = json.loads(store_json)

print(json_data)