# encoding:utf-8
import urllib2

"""
Request的data的添加方法
"""

data = "first=true&p=1&kd=python"
headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
request = urllib2.Request("https://www.lagou.com/lbs/getAllCitySearchLabels.json",headers = headers)
request.add_data(data)
print(urllib2.urlopen(request).read())