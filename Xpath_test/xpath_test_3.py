# encoding:utf-8
import lxml
import lxml.etree

html = lxml.etree.parse("1.html")
print(type(html))

res = html.xpath("//li")  # 是一个列表，包含所有元素
print(res)
"""
[<Element li at 0x1359f248>, <Element li at 0x1359f208>, <Element li at 0x1359cc08>, <Element li at 0x1359c208>, <Element li at 0x1359ac88>]
"""
print(type(res[0]))
"""
<type 'lxml.etree._Element'>
"""
print(html.xpath("//li/@class"))  # 取出li的所有结点的class名称
"""
将所有的lixia的class属性全部提取了出来
·若其中有的属性不存在，则跳过不显示
['item-0', 'item-1', 'item-inactive', 'item-1', 'item-0']
"""
print(html.xpath("//li/a/@href"))
"""
['link1.html', 'link2.html', 'link3.html', 'link4.html', 'link5.html']
"""
print(html.xpath("//li/a")) # li下面有5个节点，每个节点对应一个元素
print(html.xpath("//li/a/@href=\"link3.html\""))
"""
True
判断匹配出来的元素中是否有与"link3.html"相匹配的元素，若有则返回Ture
"""
print(html.xpath("//li//@class"))

"""
会将li下面的所有的class属性全部抓取出来
['item-0', 'hhh', 'item-1', 'item-inactive', 'item-1', 'item-0']
"""
print(html.xpath("//li"))
print(html.xpath("//li[1]"))
print(html.xpath("//li[last()]"))
print(html.xpath("//li[last()-1]"))
"""
第一个/最后一个
[<Element li at 0x1368a2c8>, <Element li at 0x1368a288>, <Element li at 0x13687c88>, <Element li at 0x13687288>, <Element li at 0x13685d08>]
[<Element li at 0x1368a2c8>]
[<Element li at 0x13685d08>]
[<Element li at 0x137ad288>]
"""
print(html.xpath("//li[last()-1]/a/@href"))
"""
['link4.html']
"""
print(html.xpath("//*[@href=\"link4.html\"]")) # 选取href="link4.html" 的元素
"""
[<Element a at 0x12f3d948>]
"""
print(html.xpath("//*[@href=\"link4.html\"]/text()")) # text() 取出标签之间的文本数据
"""
['fourth item']
"""
