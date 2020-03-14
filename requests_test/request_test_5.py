import requests
"""
这个部分完成的是cookies的获取，用于展示cookies的数据
"""


headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
r = requests.get("https://www.baidu.com/",headers=headers)
print(r.cookies)
for key, value in r.cookies.items():
    print(key + '=' + value)