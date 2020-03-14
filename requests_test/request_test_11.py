import requests

"""
指定本地的证书用于SSL验证
"""
response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
print(response.status_code)