# coding:utf-8

from bs4 import BeautifulSoup
import re


"""
bs4的find_all的使用方法
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
# print soup.find("p")     # 找到第一个p标签
# print soup.find_all("p")     # 找到所有p标签，列表形式返回
# print soup.find_all("p")[2]     # 找到所有p标签，列表形式返回

# for tag in soup.find_all(re.compile("^b")):  # 使用正则的方式进行匹配
#     print tag.name

"""
<body>...</body>
<b>...</b>
"""

# print soup.find_all(["title","b"])  # 按照列表进行搜索，只要有一个符合就返回数据
"""
[<title>The Dormouse's story</title>, <b>The Dormouse's story</b>]
"""

# print soup.find_all(id="link2")

"""
[<a class="sister" href="http://example.com/lacie" id="link2">Lacie&lt;\n/a&gt; and\n</a>]
"""

print(soup.find_all(class_="sister")) # class特殊 使用class_
"""
[<a class="sister" href="http://example.com/elsie" id="link1"><!-- E\nlsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie&lt;\n/a&gt; and\n</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tilli\ne</a>]
"""
print(soup.find_all(text="The"))
print(soup.find_all(text="The Dormouse\'s story"))
"""
精确的等于才能完成匹配
[]
[u"The Dormouse's story", u"The Dormouse's story"]
"""

print(soup.find_all("a",class_="sister")) # 限定查找a标签的class属性为sister的元素数据
