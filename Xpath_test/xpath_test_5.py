# encoding:utf-8
import lxml
import lxml.etree

import urllib2
import urllib


"""
xpath结合urllib2进行网页数据提取实战
"""

def download(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    data = response.read()
    html = lxml.etree.HTML(data)
    e_html = html.xpath("//*[@class=\"emphasis\"]/text()")
    print(e_html)

download("https://www.autohome.com.cn/166/#pvareaid=3311284")