# encoding:utf-8
import urllib2
import urllib

"""
ajax的请求方式是:post
因为使用的是python的库的方式，返回状态码为418，触发了反扒机制
添加上headers,模拟浏览器即可
"""

url = "https://movie.douban.com/j/chart/top_list?type=10&interval_id=100%3A90&action"
headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
formdata = {"limit":"20","start":"0"}

data = urllib.urlencode(formdata)
request = urllib2.Request(url,data = data,headers=headers)
print(urllib2.urlopen(request).read())
