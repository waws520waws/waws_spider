# encoding:utf-8
import selenium
import selenium.webdriver
import re
import time

def getnumberbyspace(space):
    url = "https://www.lagou.com/jobs/list_python%20测试/p-city_2?px=default&district=海淀区&bizArea="+space+"#filterBox"
    driver = selenium.webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
    driver.get(url)
    time.sleep(5)
    pagesource = driver.page_source
    """
    在这里延申两个知识点：
        1.我们的匹配的字符串中如果有中文的话，一般匹配不上，建议前面带一个u
        2.我们的括号的匹配需要使用\( 的方式，而针对分组的括号则不做任何处理
    """
    restr = u'职位 \( <span>(\\d+)</span> \)'
    regex = re.compile(restr,re.IGNORECASE)
    mylist = regex.findall(pagesource)

    driver.close()
    return mylist[0]


spacelist = ["马连洼","海淀黄庄","西二旗","香山","航天桥"]

for space in spacelist:
    print(space,getnumberbyspace(space))