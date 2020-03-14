# encoding:utf-8
"""
下载图片

"""

# # python2
# import urllib
# # 下载图片
# urllib.urlretrieve("https://www.kuaidaili.com/doc/product/img/tps_intro.jpg","../img/sp_test_img/1.jpg")

# python3
import urllib.request
# 下载图片
urllib.request.urlretrieve("https://www.kuaidaili.com/doc/product/img/tps_intro.jpg","./1.jpg")