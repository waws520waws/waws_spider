import requests

# 普通的代理
proxies = {"http":"http://139.129.116.46",
           "https":"http://139.129.116.46"}

print(requests.get("http://www.baidu.com",proxies=proxies).text)

# 需要认证的代理
proxies = {"http":"http://user:password@139.129.116.46:9999",
           "https":"http://user:password@139.129.116.46:9999"}

print(requests.get("http://www.baidu.com",proxies=proxies).text)

# socket5协议代理
"""
安装方式：'requests[socks]'
"""

import requests

proxies = {
    'http': 'socks5://user:password@host:port',
    'https': 'socks5://user:password@host:port'
}
requests.get("https://www.taobao.com", proxies=proxies)