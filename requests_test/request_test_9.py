# encoding:utf-8
import requests
"""
这个部分requests 和 session有关
使用cookie模拟登录配合session的步骤：
首先使用session.post登陆一个要登录的网站，因为是会话，所以会获取cookies信息
在下一次的get请求的时候，直接携带cookies的信息 
"""
session = requests.Session()  # 会话
mysession1 = session.get("http://httpbin.org/cookies/set/number/123456789")
mysession1 = session.get("http://httpbin.org/cookies")
print(mysession1.text)
"""
{
  "cookies": {
    "number": "123456789"
  }
}
"""

mysession2 = requests.get("http://httpbin.org/cookies/set/number/123456789")
mysession2 = requests.get("http://httpbin.org/cookies")
print(mysession2.text)

"""
{
  "cookies": {}
}
"""