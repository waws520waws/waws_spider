# enncoding:utf-8
"""
运行环境python2
在这里我们是对https的请求：
    1.对于这个页面是并没有任何影响
    2.假设我们用不了，抓取不到https的数据  解决办法ssl 忽略
    import ssl
    context = ssl._create_unverified_context()

"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import lxml.etree
import lxml
import urllib2
import urllib

def makeurllist():
    urllist = ["https://www.jb51.net/list/list_97_"+str(i+1)+".htm"for i in range(514)]
    return urllist

def parseurl(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    data = response.read()
    html = lxml.etree.HTML(data)
    title = html.xpath("//div[@class=\"artlist clearfix\"]//dl//dt//a//@title")
    detail_url_list = html.xpath("//div[@class=\"artlist clearfix\"]//dl//dt//a//@href")
    new_detail_url_list = ["https://www.jb51.net"+detail_url for detail_url in detail_url_list]
    return zip(title,new_detail_url_list)

if __name__ == '__main__':
    filepath = "./jiaobenzhijia.txt"
    j_file = open(filepath, "w+")
    urllist = makeurllist()
    for url in urllist:
        all = parseurl(url)
        for title, de_url in all:
            new_str = title + "\t\t" + de_url + "\n"
            j_file.write(new_str)
        print(url + "已经抓取完毕")

    j_file.close()

