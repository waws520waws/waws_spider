# encoding:utf-8
import re


#网页屏蔽
# 我并没有遇到视频中讲解的那种502的屏蔽方式，出现502的屏蔽的方式说明网站将我们的python的库拒之门外，可以使用selenium库进行模拟用户操作的方式 获取网页


# def download(url):
#     return urllib2.urlopen(url).read()
#
# url = "https://sou.zhaopin.com/?jl=530&kw=python&kt=3"
# print download(url)


import selenium
import selenium.webdriver
import time

# 因为智联招聘的改版，从新使用拉钩信息
def getnumberbyname(searchname):
    url = "https://sou.zhaopin.com/?jl=530&kw="+searchname+"&kt=3"
    # 注意我们在这个地方进行调用chrome的时候需要用到chromedriver_win32驱动，需要下载并配置指定的路径进行使用
    driver = selenium.webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")  # 调用chrome浏览器
    driver.get(url)
    pagesource = driver.page_source  # 抓取网页源代码
    restr = '">(\\W+)</span>'
    # 带有括号只会匹配上括号中的数据

    # 为什么要进行预编译：加快运行速度
    regex = re.compile(restr, re.IGNORECASE)

    # 注意这里的写法：使用的是regex编译后的结果的findall方法
    mylist = regex.findall(pagesource)
    time.sleep(2)
    driver.close()
    return mylist

for name in getnumberbyname("python"):
    print(name)
