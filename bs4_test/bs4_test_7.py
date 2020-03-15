# encoding:utf-8
import urllib
import urllib2
import selenium
import selenium.webdriver
import time

"""
这个使用bs4的find_all配合selenium的方式进行职位数字的提取 
"""

from bs4 import BeautifulSoup

def download(url):
    driver = selenium.webdriver.Chrome(r"C:\Users\zuoyikeji\Desktop\chromedriver.exe")
    driver.get(url)
    time.sleep(3)
    pagesource = driver.page_source
    soup = BeautifulSoup(pagesource,"lxml")
    text = soup.find_all("div",class_="dw_tlc")[0].find("div",class_="rt").get_text().strip()
    driver.close()
    return text

print(download("https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&"
               "stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize="
               "99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0"
               "&address=&line=&specialarea=00&from=&welfare="))