# encoding:utf-8
import selenium
import selenium.webdriver
import re
import time
import lxml
import lxml.etree

def getnumbers():
    url = "https://careers.tencent.com/search.html?index=2&keyword=python"
    driver = selenium.webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
    driver.get(url)
    time.sleep(3)
    page_source = driver.page_source
    html = lxml.etree.HTML(page_source)
    mylist = html.xpath("//div[@class=\"search-count\"]//text()")[0]
    print(mylist[9:12])
    driver.close()

getnumbers()