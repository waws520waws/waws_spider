# encoding:utf-8



"""
解决编码问题：
    有的浏览器不支持中文，必须要将中文转化成编码后的字符格式才能完成搜索功能
    统一规范，编码解码
"""

# python2
import urllib
word = {"kw":"王伟"}
print(urllib.urlencode(word))
print(urllib.unquote(urllib.urlencode(word)))

"""
kw=%E7%8E%8B%E4%BC%9F
kw=王伟
"""

# python3
import urllib.parse
word = {"kw":"王伟"}
print(urllib.parse.urlencode(word))
print(urllib.parse.unquote(urllib.parse.urlencode(word)))