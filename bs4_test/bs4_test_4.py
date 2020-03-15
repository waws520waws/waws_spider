#coding:utf-8

from bs4 import BeautifulSoup

"""
bs4的祖先节点，父节点，兄弟节点，儿子节点，子孙节点的使用，部分展示
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

soup=BeautifulSoup(html,"lxml") #"lxml解析方式"
# print soup.head.contents  # contents 返回一个元素下的所有的子节点，列表

"""
[<title>The Dormouse's story</title>]
"""

print(soup.a.contents)  # 按照标签的闭合进行分割，换行元素也算

"""
[u' E\nlsie ']
"""

# children
# for child in soup.body.children:
#     print child                # 其实就是闭合标签的节点分布


# for child in soup.body.descendants:
#     print child                   # 标签及标签下的内容

"""
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>   # body下的第一层
<b>The Dormouse's story</b>                                        # p拔掉的一层
The Dormouse's story                                               # b拔掉的一层

"""