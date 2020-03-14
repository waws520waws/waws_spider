# encoding:utf-8
import urllib2
import cookielib

"""
下面的这个程序将cookie信息保存起来
"""
filepath = "../cookie/cookie.txt"
cookie = cookielib.LWPCookieJar()
cookie.load(filepath,ignore_expires=True,ignore_discard=True)


header = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(header)
response = opener.open("http://www.renren.com/")
print(response.read())