# encoding:utf-8
from bs4 import BeautifulSoup


"""
初始化步骤：构建soup对象，可以使用prettify()进行html代码格式规范化输出

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

soup = BeautifulSoup(html,"lxml")  #lxml解析方式
soup1 = BeautifulSoup(html,"html.parser")  #常规网页解析
soup2 = BeautifulSoup(html,"html5lib")  #html5解析方式

print(soup.prettify())
print("--"*40)
print(soup1.prettify())
print("--"*40)
print(soup2.prettify())