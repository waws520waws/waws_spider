import requests
"""
requests的认证功能
"""

from requests.auth import HTTPBasicAuth
# 第一种繁琐写法
r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
print(r.status_code)

# 第二种简便写法
r = requests.get('http://localhost:5000', auth=('username', 'password'))
print(r.status_code)