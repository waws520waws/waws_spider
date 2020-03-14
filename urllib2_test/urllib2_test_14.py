# encoding:utf-8
import urllib2
import ssl

"""
解决https加密的问题
使用传统的http的处理方式对https并不适用
"""
import ssl
context = ssl._create_unverified_context() # 忽略安全
headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
url = "https://www.baidu.com"
request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request,context = context)
print(response.read())