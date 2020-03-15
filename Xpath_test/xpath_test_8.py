# encoding:utf-8
import urllib2
import urllib

import lxml
import lxml.etree


def parse(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    data = response.read()
    html = lxml.etree.HTML(data)
    stocklist = html.xpath("//ul[@class=\"list-box\"]//li//div[@class=\"content\"]//text()")
    str_r = "".join(stocklist)
    print(str_r)

parse("http://www.haoduanzi.com/wen/")