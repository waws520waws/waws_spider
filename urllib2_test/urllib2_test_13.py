# encoding:utf-8

# import urllib2
# response = urllib2.urlopen("http://www.baidu.cn")
# print response.geturl() == "http://www.baidu.cn"
"""
False
上面的代码可以判断出来是否发生了重定向
"""
import urllib2
class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        res = urllib2.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)
        res.status = code
        res.newurl = res.geturl()
        print(res.newurl)
        return res

opener = urllib2.build_opener(RedirectHandler)
opener.open("http://www.baidu.cn")

"""
http://www.baidu.com/
302:代表重定向
301:返回的是重定向后的url
"""