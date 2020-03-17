# encoding:utf-8
import pyvirtualdisplay
import selenium.webdriver

"""
一些网站会禁止使用那个无界面浏览器，所以这个部分就是来解决这个问题的，我们可以隐藏浏览器
"""

options= selenium.webdriver.ChromeOptions()
options.add_argument("--disable-extensions")  # 禁止外部插件
options.add_argument("--profile-directory=Defalt")
options.add_argument("--incongnito")
options.add_argument("--disable-plugins-discovery")
options.add_argument("--start-maxmined")


display = pyvirtualdisplay.Display()
display.start()
"""
课上演示有问题/并没有解决
直接使用这种方式的话会造成一个错误 easyprocess.EasyProcessError:
使用浏览器配置选项进行解决
Chromeoptions的在网络上直接搜用法大全，可以详解
"""


driver = selenium.webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe",chrome_options=options)
driver.delete_all_cookies()
driver.set_window_size(800,800)
driver.set_window_position(0,0)
print("OK")

driver.get("http://www.baidu.com")
print(driver.page_source)
driver.close()