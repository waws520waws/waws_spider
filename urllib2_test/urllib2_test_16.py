# encoding:utf-8
import urllib2
import cookielib

"""
下面的这个程序完成的是从响应中将cookie信息提取出来
"""


# 创建一个对象存储cookie
cookie = cookielib.CookieJar()

# 自动提取
header = urllib2.HTTPCookieProcessor(cookie)

# 处理cookie
opener = urllib2.build_opener(header)
response = opener.open("http://www.renren.com/")
cookies = ""
for data in cookie:
    cookies = cookies + data.name + "=" + data.value + "\r\n"

print(cookies)