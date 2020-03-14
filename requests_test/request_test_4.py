# encoding:utf-8
import json
"""
这个部分完成的是使用request 上传文件
注意我们使用   files = **  这里面的files是一个打开的文件对象
"""
import requests
url = "http://httpbin.org/post?a=Ok"

textfile = {"file":open("request_test.py","rb")} # 一般

response2 = requests.post(url,files=textfile)
print(response2.text)