# encoding:utf-8
import urllib2
from bs4 import BeautifulSoup

"""
stockstar的综合案例
"""




def download(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    data = response.read()
    return data

def parse(data):
    """
    在这里有一个注意的地方就是解析的soup可以指定编码的格式，我们可以通过head标签中meta中找到charset,保持一致即可
    :param data:
    :return:
    """
    soup = BeautifulSoup(data,"lxml",from_encoding="gb2312")
    tr_list = soup.select(".tbody_right")[1].select("tr")
    all_stock_text = []

    for tr in tr_list:
        td_list = tr.select("td")
        stock_text = []
        for td in td_list:
            # text = td.get_text()
            text = td.string
            stock_text.append(text)
        all_stock_text.append(stock_text)
    return all_stock_text


if __name__ == '__main__':
    data = download("https://quote.stockstar.com/fund/open.shtml")
    for text in parse(data):
        for i in text:
            print(i)