from lxml import etree
"""
xpath中轴的使用

"""

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
print(result)
"""
第一个li的所有祖先
[<Element html at 0x2b3be050dc8>, <Element body at 0x2b3be181b88>, <Element div at 0x2b3be181bc8>, <Element ul at 0x2b3be181c08>]
"""


result = html.xpath('//li[1]/ancestor::div')
print(result)
"""
第一个li的所有div祖先
[<Element div at 0x2b3be181bc8>]
"""


result = html.xpath('//li[1]/attribute::*')
print(result)
"""
第一个li的所有属性的值
['item-0']
"""

result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
"""
第一个li的直接子节点中标签为a且href属性值为link1.html的元素
[<Element a at 0x2b3be181b88>]
"""


result = html.xpath('//li[1]/descendant::span')
print(result)
"""
第一个li的所有子孙节点中标签为span的元素
[<Element span at 0x2b3be181bc8>]
"""


result = html.xpath('//li[1]/following::*[2]')
print(result)
"""
第一个li的following轴，可以获取当前节点之后的所有节点，这里我们虽然使用的是*匹配，但又加了索引选择，所以只获取了第二个后续节点
[<Element a at 0x2b3be181c08>]
"""


result = html.xpath('//li[1]/following-sibling::*')
print(result)
"""
第一个li的following-sibling轴，可以获取当前节点的所有兄弟节点
[<Element li at 0x29526521e48>, <Element li at 0x29526521d48>, <Element li at 0x29526521a88>, <Element li at 0x29526521c48>]
"""
