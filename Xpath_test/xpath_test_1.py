# encoding:utf-8

import lxml
import lxml.etree

"""
主要是将html_str构造成体

"""





text = """
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
     </ul>
 </div>
"""

html = lxml.etree.HTML(text)    # 处理文本
print(type(html))
print(html)
"""
<type 'lxml.etree._Element'>
<Element html at 0x134072c8>
"""

print(lxml.etree.tostring(html))

"""
<html><body><div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a> # &#230;&#179;&#168;&#230;&#132;&#143;&#239;&#188;&#140;&#230;&#173;&#164;&#229;&#164;&#132;&#231;&#188;&#186;&#229;&#176;&#145;&#228;&#184;&#128;&#228;&#184;&#170; </li> &#233;&#151;&#173;&#229;&#144;&#136;&#230;&#160;&#135;&#231;&#173;&#190;
     </ul>
 </div>
</body></html>

"""