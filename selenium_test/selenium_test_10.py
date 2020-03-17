# encoding:utf-8

from selenium import webdriver
import time

"""
多个浏览器窗口
"""
driver = webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
driver.get("https://www.baidu.com")

time.sleep(3)
driver.find_element_by_link_text(u"登录").click()
time.sleep(3)
driver.find_element_by_link_text(u"立即注册").click()
firstwin = driver.current_window_handle
"""
在这里有个地方需要说明一下，就是我们在点击立即注册的时候，是打开了一个新页面
但是此时的窗体的主体仍然是登录的那个，所以后面的不等于/切换也就对的上了
"""
allwindows = driver.window_handles  # 所有的窗口

# 选择注册窗口
for win in allwindows:
    print(win)
    if win != firstwin:
        driver.switch_to.window(win)
        print("切换成功")
        driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("hello")
    time.sleep(3)

driver.close()   # 关闭当前

time.sleep(5)
driver.quit()    # 关闭所有的窗口