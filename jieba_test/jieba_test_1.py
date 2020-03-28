import jieba

str_list = ["我来到北京清华大学","乒乓球拍卖完了","中国科学技术大学"]

# 全模式
# for str_1 in str_list:
#     seg_list = jieba.cut(str_1,cut_all=True)
#     print("Full Mode:"+"/".join(list(seg_list)))
#     """
#     Full Mode:我/来到/北京/清华/清华大学/华大/大学
#     Full Mode:乒乓/乒乓球/乒乓球拍/球拍/拍卖/卖完/了
#     Full Mode:中国/科学/科学技术/技术/大学
#     """


# 精确模式
seg_list = jieba.cut("我来到北京清华大学",cut_all=False)
print("Default Mode:"+"/".join(list(seg_list)))

"""
Default Mode:我/来到/北京/清华大学
"""

# 默认使用的就是精确模式
seg_list = jieba.cut("我来到北京清华大学")
print("None Params Mode:"+"/".join(list(seg_list)))
"""
None Params Mode:我/来到/北京/清华大学
"""


# 搜索引擎模式
seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")
print("Search Mode:"+"/".join(list(seg_list)))
"""
Search Mode:小明/硕士/毕业/于/中国/科学/学院/科学院/中国科学院/计算/计算所/，/后/在/日本/京都/大学/日本京都大学/深造
"""