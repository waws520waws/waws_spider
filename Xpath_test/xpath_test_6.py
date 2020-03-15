# encoding:utf-8

"""
在这里我们解析得到的数据中中文无法正常的显示，主要是python2的原因，但是我们可以使用python3的方式进行处理
使用python3进行处理需要注意(实战遇坑)：
    1.import urllib.request
    2.使用urllib.request.urlopen()的时候，不能加入headers

除了使用python3,进行解决 我们还可以使用python2的解码方式进行问题的解决

"""

# import lxml
# import lxml.etree
#
# import urllib.request
#
# def parse(url):
#     response = urllib.request.urlopen(url)
#     data = response.read()
#     html = lxml.etree.HTML(data)
#     print(html.xpath("//div[@class=\"dw_tlc\"]/div[@class=\"rt\"]/text()")[0].strip())
#
# parse("https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=")


"""
python2版本
"""
import lxml
import lxml.etree

import urllib2

def parse(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url,headers =headers)
    response =urllib2.urlopen(request)
    data = response.read()
    html = lxml.etree.HTML(data)
    print(html.xpath("//div[@class=\"dw_tlc\"]/div[@class=\"rt\"]/text()")[0].strip())

parse("https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=")




