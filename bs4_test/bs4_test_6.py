# coding:utf-8

from bs4 import BeautifulSoup
import re

"""
bs4的select的使用方法
"""


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters;
and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- E
lsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie<
/a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tilli
e</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, "lxml")  # "lxml解析方式"
# print soup.select("title")  # 按照标签的名字进行查找
# print soup.select("a")  # 按照标签的名字进行查找,一次定位多个

# print soup.select(".sister")   # 按照class进行查找
# print soup.select("#link1")   # 按照id进行查找
# print soup.select("p #link1")   # p标签内部的id进行查找
"""
[<a class="sister" href="http://example.com/elsie" id="link1"><!-- E\nlsie --></a>]
"""

# print soup.select("head > title")  # 后代(层级关系)

# print soup.select("a[class=\"sister\"]")  # 标签为a的class=sister的元素
"""
[<a class="sister" href="http://example.com/elsie" id="link1"><!-- E\nlsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie&lt;\n/a&gt; and\n</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tilli\ne</a>]
"""

print(soup.select("title")[0].get_text())   # 获取标签之间的内容


