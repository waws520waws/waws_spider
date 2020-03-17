# encoding:utf-8
import selenium
import selenium.webdriver
import selenium.webdriver.common.keys
import time
driver = selenium.webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
driver.get("https://talent.baidu.com/external/baidu/index.html#/social/2/python")
time.sleep(5)
for i in range(10):
    # elem = driver.find_element_by_class_name("next")
    """
    相较于by_class_name的不确定性，使用by_xpath更能很好的定位元素的位置,by_xpath是最后的杀手锏
    """
    elem = driver.find_element_by_xpath("//*[@class=\"pagination\"]/ul//li[last()]/a")
    print(elem)
    time.sleep(3)

    elem.click()
    pagesource = driver.page_source
    print(pagesource)
    print("--"*40)

time.sleep(40)
driver.close()