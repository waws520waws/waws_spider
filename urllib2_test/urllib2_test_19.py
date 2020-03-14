# encoding:utf-8
import urllib2
import urllib
import cookielib

# 创建一个对象存储cookie
cookie = cookielib.CookieJar()

# 创建一个链接对象使用cookie
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

# 打开器，使用cookie
opener = urllib2.build_opener(cookie_handler)

# 增加一个浏览器模拟
opener.addheaders = [("User-Agent","Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);")]
url = "http://www.renren.com/PLogin.do"
data = {"email":"16601203140","password":"709103wei"}
data = urllib.urlencode(data)
request = urllib2.Request(url,data) # post请求登录，抓取cookie
response = opener.open(request)
response_index = opener.open("http://www.renren.com/914824554/profile")
print(response_index.read())

"""
分解步骤记忆如下：首先我们先找一个东西cookielib.CookieJar()，将我们获取到的cookie记录下来，要想记录，这个东西必须在链接中使用，
只有请求和响应的链接中才有cookie信息，所以将东西放入到urllib2.HTTPCookieProcessor(cookie)中，然后创建一个打开器（将cookie链接
处理器放在里面），目的完成请求和响应，实际上就是post请求，只不过是用opener的形式完成的，在这个过程中，那个东西记录了cookie信息
所以下一次再用这个打开器访问页面的时候，其实就携带这那个cookie信息。
"""
