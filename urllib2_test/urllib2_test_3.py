# encoding:utf-8

import urllib2

# 给Request增加headers参数，模拟浏览器

def download(url):
    headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url,headers = headers)
    # 发起请求，注意这里使用的已经不是urlopen,在这里可以这样记，request携带请求头，而urlopen只是打开网页
    # 构造请求，使用urlopen开启请求
    data = urllib2.urlopen(request).read()
    # 打开请求抓取数据
    return data

url = "https://www.lagou.com/jobs/list_python/p-city_2"
print(download(url))