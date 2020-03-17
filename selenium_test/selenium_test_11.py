# encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

"""
selenium 模拟鼠标进行操作
"""
driver = webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.baidu.com")
above = driver.find_element_by_link_text(u"设置")
ActionChains(driver).move_to_element(above).perform()  # 悬浮，鼠标停留
time.sleep(4)
# ActionChains(driver).move_to_element(elem)  #移动
ActionChains(driver).move_to_element(above).context_click() # 单击
# ActionChains(driver).move_to_element(above).double_click() # 双击
# ActionChains(driver).move_to_element(above).drag_and_drop() # 拖放


time.sleep(5)
driver.close()