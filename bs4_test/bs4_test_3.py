# encoding:utf-8
from bs4 import BeautifulSoup

"""
基本属性，标签，文字的获取
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

soup = BeautifulSoup(html,"lxml")

print(soup.title.string)
print(type(soup.name))  # 编码
print(soup.name)
print(soup.attrs)

print(soup.a)
print(soup.a.string)  # 清理注释  显示注释的信息
print(type(soup.a.string))
"""

<class 'bs4.element.Comment'>
"""
