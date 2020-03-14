# encoding:utf-8
import urllib2
import urllib

"""
这个部分是Request中的data进行赋值，注意是字典类型，这个data赋值了，就代表是post请求了
"""


url = "https://umbra.nascom.nasa.gov/cgi-bin/eit-catalog.cgi"
values = {'obs_year':'2011','obs_month':'March',
                             'obs_day':'8','start_year':'2011'
                             ,'start_month':'March','start_day':'8'
                             ,'start_hour':'All Hours','stop_year':'2011'
                             ,'stop_month':'March','stop_day':'8'
                             ,'stop_hour':'All Hours','xsize':'All'
                             ,'ysize':'All','wave':'all'
                             ,'filter':'all','object':'all'
                             ,'xbin':'all','ybin':'all'
                             ,'highc':'all'}

data = urllib.urlencode(values)
request = urllib2.Request(url,data) # post类型,发起请求，传递data
print(urllib2.urlopen(request).read())