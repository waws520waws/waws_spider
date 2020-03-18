# encoding:utf-8
"""
智联招聘job的正则的提取方式
"""

import re
mystr = '<span title="大数据分析工程师" class="jobTitle over-length \
                listsimple__content__item__box__jobname__span \
                listsimple__content__item__box__jobname__span__title">大数据分析工程师</span>'


restr = ">\\W+<"
# 不带有括号的话，会匹配上所有的数据
restr1 = ">(\\W+)<"
# 带有括号只会匹配上括号中的数据

# 为什么要进行预编译：加快运行速度
regex = re.compile(restr,re.IGNORECASE)

# 注意这里的写法：使用的是regex编译后的结果的findall方法
mylist = regex.findall(mystr)
print(mylist)
# 运行结果：['\xe5\xa4\xa7\xe6\x95\xb0\xe6\x8d\xae\xe5\x88\x86\xe6\x9e\x90\xe5\xb7\xa5\xe7\xa8\x8b\xe5\xb8\x88']
print(mylist[0])
# 运行结果：大数据分析工程师