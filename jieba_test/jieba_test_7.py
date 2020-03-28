import sys
sys.path.append('../')

import jieba
import jieba.analyse
from optparse import OptionParser

USAGE = "usage:    python extract_tags_idfpath.py [file name] -k [top k]"

parser = OptionParser(USAGE)
parser.add_option("-k", dest="topK")
opt, args = parser.parse_args()


if len(args) < 1:
    print(USAGE)
    sys.exit(1)

file_name = args[0]

if opt.topK is None:
    topK = 10
else:
    topK = int(opt.topK)

content = open(file_name, 'rb').read()

# 关键词提取所使用逆向文件频率（IDF）文本语料库可以切换成自定义语料库的路径
jieba.analyse.set_idf_path("../extra_dict/idf.txt.big")

tags = jieba.analyse.extract_tags(content, topK=topK)

print(",".join(tags))