# encoding:utf-8

import urllib2
"""
使用Request对象的方法add_header，在请求头中增加信息
还有方法 add_data(data)   add_header(key,value)   add_unredirected_header(key,value)
get_data()   get_full_url()    get_header()   get_host()   get_method()   get_origin_req_host()
"""


def download(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url,headers = headers)
    request.add_header("Connection","keep-alive")  # 额外添加header信息
    # 通过调用Request.get_header()来查看header消息
    request.get_header(header_name="Connection")
    response = urllib2.urlopen(request)
    print(response.code)     # 查看状态码
    data = response.read()
    return data


url = "https://www.lagou.com/jobs/list_python/p-city_2"
print(download(url))