
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())


# 首先选取的是href属性的值为link4.html的a标签,在找到这些a标签的父标签的class属性的值
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)

"""
另一种方式
使用parent:: 对父元素进行提取
from lxml import etree
 
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)

"""