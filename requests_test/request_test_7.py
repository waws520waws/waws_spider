# encoding:utf-8

import requests
import time

"""
这个部分主要是request和cookie相关的操作
在get中传递cookie,网络请求中会使用这个cookie，但是并不会将其存储变成 requests的cookie
"""
mycookie = dict(BDSID="zhadu")
# req = requests.get("http://www.baidu.com",cookies = mycookie)

req = requests.get("http://httpbin.org/cookies",cookies = mycookie)
time.sleep(3)
print(req.cookies)
print(req.text)