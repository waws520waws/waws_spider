from lxml import etree

"""
contains的使用：应用于一个标签的属性有多个值的情况，如果我们还是用之前的相等的模式，是匹配不到值的
"""



text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)