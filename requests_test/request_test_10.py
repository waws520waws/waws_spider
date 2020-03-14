# encoding:utf-8
import requests

# 下面两句话的作用是接触警告
from requests.packages import urllib3
urllib3.disable_warnings()

"""
这个部分主要完成的是关于request_ssl的处理的部分
"""

import json
# req = requests.get("https://www.12306.cn",verify = True)
"""
默认用证书，不安全报错/没有证书  verify = False 不会报错
"""
req = requests.get("https://www.baidu.com/",verify = False)
print(req)