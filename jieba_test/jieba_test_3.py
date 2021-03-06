import jieba


test_sent = (
"李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
"例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
"「台中」正確應該不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。"
)
words = jieba.cut(test_sent)
print('/'.join(words))



# -------------加载自定义词典----------------
# import jieba
# jieba.load_userdict("userdict.txt")
# import jieba.posseg as pseg
#
# jieba.add_word('石墨烯')
# jieba.add_word('凱特琳')
# jieba.del_word('自定义词')
#
# test_sent = (
# "李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
# "例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
# "「台中」正確應該不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。"
# )
# words = jieba.cut(test_sent)
# print('/'.join(words))
# --------------加载自定义词典结束-------------

"""
<不使用自定义词典进行分割>
李小福/是/创新/办/主任/也/是/云/计算/方面/的/专家/;/ /什么/是/八/一双/鹿/
/例如/我/输入/一个/带/“/韩玉/赏鉴/”/的/标题/，/在/自定义词/库中/也/增加/了/此/词为/N/类/
/「/台/中/」/正確/應該/不會/被/切開/。/mac/上/可/分出/「/石墨/烯/」/；/此時/又/可以/分出/來凱/特琳/了/。

<使用自定义词典进行分割>
李小福/是/创新办/主任/也/是/云计算/方面/的/专家/;/ /什么/是/八一双鹿/
/例如/我/输入/一个/带/“/韩玉赏鉴/”/的/标题/，/在/自定义/词库/中/也/增加/了/此/词为/N/类/
/「/台中/」/正確/應該/不會/被/切開/。/mac/上/可/分出/「/石墨烯/」/；/此時/又/可以/分出/來/凱特琳/了/。

从上面的两个对比中可以看出来 "创新办"，"云计算"，"凯特琳","石墨烯","韩玉鉴赏"，"台中"等都被完整的切分出来了
"""