# encoding:utf-8
"""
这个部分主要说的是requests的异常处理
"""
import requests
try:
    url = "http://www.google.com/"
    response = requests.get(url,timeout = 3)
    # 连接+读取分离
    # response = requests.get(url,timeout = (5,11,30))
    # 永久等待
    # response = requests.get(url,timeout=None)
    # 永久等待
    # response = requests.get(url)
    print(response.text)
    print(response.status_code)
except Exception as e:
    print("get http://www.google.com/ failed")
print("over")