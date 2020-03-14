# encoding:utf-8
import urllib2
import cookielib

"""
下面的这个程序将cookie信息保存起来
"""
filepath = "../cookie/cookie.txt"
cookie = cookielib.LWPCookieJar(filepath)  # 设定路径
header = urllib2.HTTPCookieProcessor(cookie)  # 设定cookie,与网站有关
opener = urllib2.build_opener(header)
response = opener.open("http://www.renren.com/")

cookie.save(ignore_expires=True,ignore_discard=True)
