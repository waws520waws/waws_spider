# encoding:utf-8
import urllib2
import urllib


"""
使用request对象的各种方法
"""

def downloadasAndroid(url):
    headers = {"User-Agent": "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"}
    request = urllib2.Request(url,headers = headers)
    request.add_header("Connection","keep-alive")
    print(request.get_full_url())  # 整个网页的链接
    print(request.get_host())      # 服务器域名/ip
    print(request.get_method())    # 请求方法
    print(request.get_header("Connection"))  # http/ftp/https
    print(request.get_type())

    response = urllib2.urlopen(request)
    print(response.code)        # 状态码
    print(response.info())     # 网页详细信息
    print(response.read())      # 网页源代码


downloadasAndroid("http://www.baidu.com")