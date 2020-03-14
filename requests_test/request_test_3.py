# encoding:utf-8

"""
requests 的POST方法
注意post方式中传递的参数是data,而get 是params
"""

import requests
data = {"user":"admin","pwd":"admin"}
headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
url = "https://httpbin.org/post"
req = requests.post(url,data=data,headers=headers)
print(req.content.decode("utf8","ignore"))