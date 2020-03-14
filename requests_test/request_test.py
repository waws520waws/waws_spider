# encoding:utf-8

"""
介绍requests的基础信息

"""


import requests
r = requests.get("http://www.baidu.com")

print(type(r))
print(r.status_code)
print(r.url)
print(r.headers)
print(r.cookies)
print(r.content) # 网页内容
print(type(r.content))
print(r.text)   # 网页内容
print(type(r.text))
print(r.history)
print(r.encoding)
print(r.is_redirect)  # 是否重定向
print(r.links)    # 子链接