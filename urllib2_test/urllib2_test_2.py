import urllib2

"""
主要看下response的方法
"""


url = "http://www.baidu.com"
response = urllib2.urlopen(url)
print(response.geturl())
print(response.getcode())
print(response.info())


"""
http://www.baidu.com

200

Bdpagetype: 1
Bdqid: 0xf3af2e8a00052fba
Cache-Control: private
Content-Type: text/html;charset=utf-8
Date: Sat, 14 Mar 2020 09:51:47 GMT
Expires: Sat, 14 Mar 2020 09:50:56 GMT
P3p: CP=" OTI DSP COR IVA OUR IND COM "
P3p: CP=" OTI DSP COR IVA OUR IND COM "
Server: BWS/1.1
Set-Cookie: BAIDUID=514C4C76B0DCAB10C9281CC026C93D45:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
Set-Cookie: BIDUPSID=514C4C76B0DCAB10C9281CC026C93D45; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
Set-Cookie: PSTM=1584179507; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
Set-Cookie: BAIDUID=514C4C76B0DCAB1058237D1ABBB623B7:FG=1; max-age=31536000; expires=Sun, 14-Mar-21 09:51:47 GMT; domain=.baidu.com; path=/; version=1; comment=bd
Set-Cookie: BDSVRTM=0; path=/
Set-Cookie: BD_HOME=1; path=/
Set-Cookie: H_PS_PSSID=30974_1440_21115_30842_30823_26350_30717; path=/; domain=.baidu.com
Traceid: 1584179507065569434617559304642381557690
Vary: Accept-Encoding
Vary: Accept-Encoding
X-Ua-Compatible: IE=Edge,chrome=1
Connection: close
Transfer-Encoding: chunked
"""