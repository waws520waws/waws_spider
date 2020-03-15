# encoding:utf-8
import urllib
import urllib2

"""
urllib2配合bs4进行数据的提取
这个使用bs4的select配合urllib2的方式进行职位数字的提取 
注意没有这种形式：
select("a",class_="link") 这个是find_all的写法
"""

from bs4 import BeautifulSoup

def download(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    pagesource = response.read()
    soup = BeautifulSoup(pagesource,"lxml")
    # text = soup.select(".dw_tlc")[0].select(".rt")[0].get_text().strip()
    text = soup.select("div .dw_tlc")[0].select("div .rt")[0].get_text().strip()


    return text

print(download("https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c"
               "&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99"
               "&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0"
               "&address=&line=&specialarea=00&from=&welfare="))