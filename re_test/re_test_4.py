# encoding:utf-8
import selenium
import selenium.webdriver
import re


def getnumberbyspace(space):
    url = "https://search.51job.com/list/" + space + ",000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    driver = selenium.webdriver.Chrome(r"C:\Users\19663\Desktop\chromedriver.exe")
    driver.get(url)
    pagesource = driver.page_source
    # 下面的部分不使用u会发生报错
    restr = '<div class="rt">([\s\S]*?)</div>' # 如果正则抓取失败，一般都是由于空白字符导致的
    """
    ([\s\S]*?) 的作用就是将给定的字符串的
    深圳 
        共4497条职位

    上海 
        共6804条职位

    北京 
        共3516条职位

    """
    regex = re.compile(restr, re.IGNORECASE)
    mylist = regex.findall(pagesource)
    newpagesource = mylist[0].strip()  # 去除前后的空白符
    newstr = "(\\d+)"
    newgex = re.compile(newstr, re.IGNORECASE)
    mylist = newgex.findall(newpagesource)
    driver.close()
    # 在我们得到的是字典或者列表的时候，我们需要保证其数据的正确性，在后面取数据的时候才不会出错
    if len(mylist) == 0:
        return "失败"
    else:
        return mylist[0]


spacedict = {"010000": "北京", "020000": "上海", "040000": "深圳"}
print(getnumberbyspace("010000"))
# for space in spacedict:
#     print spacedict[space], getnumberbyspace(space)
#     break


"""
对上面的方法进行解析：
    1.首先他并没有解决抓取中存在中文的问题，只是通过两次抓取的方式避开了
    2.学习的点：strip()方法去掉空格(多余字符的处理)，([\s\S]*?)使用非贪婪的模式进行匹配给定的字符串中所有的东西，包括多余字符
"""