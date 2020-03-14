# encoding:utf-8
import urllib2

"""
使用网络上找到的免费的代理
ProxyHandler创建代理的函数，参数是一个字典，键http/https  值ip:port  或者yonghuming:mima@ip:port
在创建opener的时候将代理对象加入进去 opener = urllib2.build_opener(代理对象) 
"""
httpproxy = urllib2.ProxyHandler({"http":"49.70.64.148:9999"})  # 无密码验证代理的使用
# httpproxy = urllib2.ProxyHandler({"http":"wangwei:111111@49.70.64.148:9999"}) # 带密码的代理使用
# 出错的一个原因其实就是代理不好使
"""
nohttpproxy = urllib2.ProxyHandler({})  # 空代理的使用

opener = urllib2.build_opener(nohttpproxy) # 创建一个空代理打开器
"""

opener = urllib2.build_opener(httpproxy) # 创建一个打开器
"""
注意下面的url链接的完整性ttp://www.baidu.com/  斜杠
"""
request = urllib2.Request("https://www.kuaidaili.com/doc/")
response = opener.open(request) # 打开网页,内置代理服务器
print(response.read())