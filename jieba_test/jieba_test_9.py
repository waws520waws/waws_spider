import jieba

"""
标注划分的起止位置
"""
# 默认模式
# result = jieba.tokenize(u'永和服装饰品有限公司')
# for tk in result:
#     print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))

"""
word 永和		 start: 0 		 end:2
word 服装		 start: 2 		 end:4
word 饰品		 start: 4 		 end:6
word 有限公司		 start: 6 		 end:10
"""

# 搜索模式
result = jieba.tokenize(u'永和服装饰品有限公司', mode='search')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))


"""
word 永和		 start: 0 		 end:2
word 服装		 start: 2 		 end:4
word 饰品		 start: 4 		 end:6
word 有限		 start: 6 		 end:8
word 公司		 start: 8 		 end:10
word 有限公司		 start: 6 		 end:10
"""