# encoding:utf-8
"""
requests 的get方法的使用
"""
import requests

data = {"name":"waws","age":18}
headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
url = "http://httpbin.org/get"
req = requests.get(url,params=data,headers=headers)
# 标准解析格式
print(req.content.decode("utf8","ignore"))

# json解析获得字典
print(req.json())
print(type(req.json()))




