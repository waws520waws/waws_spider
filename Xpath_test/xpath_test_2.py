# encoding:utf-8
import lxml

"""
lxml.etree.HTML()   处理文本字符串
lxml.etree.parse()   处理的是文件内容

"""


import lxml.etree

html = lxml.etree.parse("1.html")  # 处理文件
print(html)
print(type(html))
print(lxml.etree.tostring(html))

"""
报错：
lxml.etree.XMLSyntaxError: Opening and ending tag mismatch: meta line 4 and head, line 6, column 8
这个主要是标签不匹配的原因，将html中的meta标签去掉即可

"""

"""
知识点：lxml.etree.parse(html_file_path,解析器)，使用tostring()得到的数据是bytes类型的，decode解码查看
from lxml import etree
 
html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))

"""