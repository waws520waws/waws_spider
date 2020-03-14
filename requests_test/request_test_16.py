# encoding:utf-8
import requests
import chardet

"""
这个部分可以查看网页的编码
"""
response = requests.get("http://www.baidu.cn")
# 注意这里使用text会报错
print(chardet.detect(response.content))

# 设置编码(检测网页编码)
response.encoding = chardet.detect(response.content)
# print response.text
print(response.history)  # 指的是跳转历史
print(response.url)      # 最终响应的url http://www.baidu.cn--->http://www.baidu.com/

"""
{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
[<Response [302]>]
http://www.baidu.com/
"""