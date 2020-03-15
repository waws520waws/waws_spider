#coding:utf-8

"""
极其常见：
    1.标签
    2.name,attrs
    3.string

"""


from bs4 import BeautifulSoup
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

soup=BeautifulSoup(html,"lxml") #"lxml解析方式"
# soup1=BeautifulSoup(html,"html.parser") #常规网页解析，
# soup=BeautifulSoup(html,"html5lib") #HTML5解析 ,只是解析方法不一样，结果一样


# 提取标签的类型为Tag类型

# print soup.title #提取标签
"""
<title>The Dormouse's story</title>
"""
# print soup.head  #提取标签全部内容
# print soup.body
# print soup.a  #多个标签提取第一个
"""
<a class="sister" href="http://example.com/elsie" id="link1"><!-- E
lsie --></a>
"""
# print soup.p
#

# print soup.name
"""
[document]
"""
# print soup.title.name  #name就是标签的名字
"""
title
"""

# print soup.head.name
#
# print soup.title.attrs
"""
{}
"""
# print soup.p.attrs  #标签内部的属性
"""
{'class': ['title'], 'name': 'dromouse'}
"""

# print soup.p["class"] #取出标签的内部属性
"""
['title']
"""

# print soup.p["name"]
"""
dromouse
"""

"""
属性不存在的时候，就会报错
"""
#
print(soup.title.string) #取出标签之间的内容

"""
The Dormouse's story
"""