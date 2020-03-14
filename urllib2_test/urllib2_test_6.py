# encoding:utf-8

import urllib
import urllib2

"""
路径参数详细的使用爬取网页的代码urllib.urlencode()的使用
"""

headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
url = "http://www.baidu.com/"
word = {"wd":"尹成"}
kw = urllib.urlencode(word)
newurl = url + "?" + kw
request = urllib2.Request(newurl,headers = headers)
print(urllib2.urlopen(request).read())



# 多参数的书写方式
"""
# encoding:utf-8
import urllib2
import urllib


def download(url,addr,mytype):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    addr = urllib.urlencode({"jl":addr})
    mytype = urllib.urlencode({"kw":mytype})
    url = url + "?" + addr + "&" + mytype + "kt=3"

    request = urllib2.Request(url,headers = headers)
    request.add_header("Connection","keep-alive")
    response = urllib2.urlopen(request)
    print response.code
    data = response.read()
    return data

addr = "530"
mytype = "python"
url = "https://sou.zhaopin.com/"
print download(url,addr,mytype)

"""