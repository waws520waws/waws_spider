# encoding:utf-8
"""
·失败 —— 失败
这个程序失败的原因是：异步加载，我们请求回来的网页的数据并不是我们需要的数据
BAT的所有招聘网站的终极解决方法就是selenium 模拟浏览器，加载完成了，在从中提取出我们想要的数据
"""

import urllib
import urllib2
import re

import lxml
import lxml.etree

def getnumbers(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    data = response.read()
    print(data)
    restr = "<div data-v-288d7ecc="" class=\"search-count\">显示1-10,共(\\d+)职位</div>"
    regex = re.compile(restr,re.IGNORECASE)
    numlist = regex.findall(data)
    if len(numlist)>0:
        return numlist[0]
    else:
        return 0

def geturllist(num):
    urllist = []
    if num == 0:
        return urllist
    if num%10==0:
        urllist = ["https://careers.tencent.com/search.html?index="+str(i+1)+"&keyword=python" for i in range(num//10+1)]
    else:
        urllist = ["https://careers.tencent.com/search.html?index=" + str(i + 1) + "&keyword=python" for i in range(num // 10 + 2)]
    return urllist

def get_detail_urllist(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    data = response.read()
    html = lxml.etree.HTML(data)
    id_list = html.xpath("//div[@class=\"recruit-wrap recruit-margin\"]//div[@id=\"share-detail\"]//div//@id")
    urllist = ["https://careers.tencent.com/jobdesc.html?postId="+ id for id in id_list]
    return urllist

def parse_url(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    data = response.read()
    html = lxml.etree.HTML(data)
    duty_list = html.xpath("//div[@class=\"recruit-content\"]//div[@class=\"duty-text\"]//li//text()")
    duty_str = "".join(duty_list).strip()
    return duty_str


if __name__ == '__main__':
    filepath = "./Tencent_duty.txt"
    T_file = open(filepath,"w")
    origin_url = "https://careers.tencent.com/search.html?index=2&keyword=python"
    num = getnumbers(origin_url)
    print(num)
    urllist = geturllist(num)
    for url in urllist:
        detail_url_list = get_detail_urllist(url)
        for detail_url in detail_url_list:
            duty_str = parse_url(detail_url)
            T_file.write(duty_str+"\n")

    T_file.close()