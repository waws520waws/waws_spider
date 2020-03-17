# encoding:utf-8
"""
爬取快代理的所有的ip:port,并验证是否可用
"""
from selenium import webdriver
import urllib2
import time

for i in range(10):
    url = "https://www.kuaidaili.com/free/inha/"
    driver = webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
    url = url + str(i + 1) + "/"
    driver.get(url)
    time.sleep(1)
    data = driver.find_elements_by_xpath("//tbody//tr")
    http_list = []
    for da in data:
        ip = da.find_element_by_xpath("./td[1]").text
        port = da.find_element_by_xpath("./td[2]").text
        http = ip + ":" + port
        http_list.append(http)
    driver.close()
    for http in http_list:
        httpproxy = urllib2.ProxyHandler({"http": http})
        opener = urllib2.build_opener(httpproxy)
        request = urllib2.Request("https://www.baidu.com")
        try:
            response = opener.open(request, timeout=10)
            print(http + u"可以使用")
        except:
            print(http + u"无效")