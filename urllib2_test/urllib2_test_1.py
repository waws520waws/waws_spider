# encoding:utf-8
import urllib2

"""
主要的工作是urlopen()的到的是一个类似于文件的对象，可以使用文件读取内容的几种方法

"""

def download1(url):
    return urllib2.urlopen(url).read()  # 读取全部网页


def download2(url):
    return urllib2.urlopen(url).readlines()  # 读取每一行的网页数据，压入一个列表


def download3(url):
    response = urllib2.urlopen(url)  # 网页抽象为一个文件
    while True:
        line = response.readline()  # 读取一行
        if not line:
            break
        print(line)


url = "http://www.baidu.com"  #urlopen只能处理http,不可以处理https
# print download1(url)
# print download2(url)
print(download3(url))

"""
# read 的返回结果：行式文件类型
# readline 相当于文件中的一行一行读取,需要循环配合
# readlines 的返回结果：列表
"""

