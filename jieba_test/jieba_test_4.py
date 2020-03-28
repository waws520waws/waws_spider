import jieba

"""
使用suggest_freq是建议分割还是合并，当我们使用元组的方式("A","B")进行操作时，是将原本捆绑在一起的词语分割开；
当我们使用"AB"，是将原本分割开的词语绑在一起
"""

print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
"""
如果/放到/post/中将/出错/。
"""


jieba.suggest_freq(('中', '将'), True)
print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
"""
如果/放到/post/中/将/出错/。
"""


print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))
"""
「/台/中/」/正确/应该/不会/被/切开
"""


jieba.suggest_freq('台中', True)
print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))
"""
「/台中/」/正确/应该/不会/被/切开
"""