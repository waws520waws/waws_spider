# requests库的使用(代码的集合)

参考博客：

基本用法：https://cuiqingcai.com/5517.html

高级用法：https://cuiqingcai.com/5523.html

[toc]



## 基本功法

### Get方法

#### 基本用法

**前提说明：我们主要访问的是链接为[http://httpbin.org/get](http://epub.ituring.com.cn/article/edit/[http://httpbin.org/get)，该网站会判断如果客户端发起的是GET请求的话，它返回相应的请求信息**

```python
# encoding:utf-8

"""
介绍requests的基础信息
"""
import requests
r = requests.get("http://www.baidu.com")

print(type(r))
print r.status_code
print r.url
print r.headers
print r.cookies
print r.content # 网页内容
print(type(r.content))
print r.text   # 网页内容
print(type(r.text))
print r.history
print r.encoding
print r.is_redirect  # 是否重定向
print r.links    # 子链接
```

得到的结果如下：

```python
<class 'requests.models.Response'>
200
http://www.baidu.com/
{'Content-Encoding': 'gzip', 'Transfer-Encoding': 'chunked', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Keep-Alive': 'timeout=58', 'Server': 'bfe/1.0.8.18', 'Last-Modified': 'Mon, 23 Jan 2017 13:28:11 GMT', 'Pragma': 'no-cache', 'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Date': 'Fri, 13 Mar 2020 22:53:20 GMT', 'Content-Type': 'text/html'}
<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
<!DOCTYPE html>
<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer><link rel=stylesheet type=text/css href=http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css><title>百度一下，你就知道</title></head> <body link=#0000cc> <div id=wrapper> <div id=head> <div class=head_wrapper> <div class=s_form> <div class=s_form_wrapper> <div id=lg> <img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129> </div> <form id=form name=f action=//www.baidu.com/s class=fm> <input type=hidden name=bdorz_come value=1> <input type=hidden name=ie value=utf-8> <input type=hidden name=f value=8> <input type=hidden name=rsv_bp value=1> <input type=hidden name=rsv_idx value=1> <input type=hidden name=tn value=baidu><span class="bg s_ipt_wr"><input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus></span><span class="bg s_btn_wr"><input type=submit id=su value=百度一下 class="bg s_btn"></span> </form> </div> </div> <div id=u1> <a href=http://news.baidu.com name=tj_trnews class=mnav>新闻</a> <a href=http://www.hao123.com name=tj_trhao123 class=mnav>hao123</a> <a href=http://map.baidu.com name=tj_trmap class=mnav>地图</a> <a href=http://v.baidu.com name=tj_trvideo class=mnav>视频</a> <a href=http://tieba.baidu.com name=tj_trtieba class=mnav>贴吧</a> <noscript> <a href=http://www.baidu.com/bdorz/login.gif?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2f%3fbdorz_come%3d1 name=tj_login class=lb>登录</a> </noscript> <script>document.write('<a href="http://www.baidu.com/bdorz/login.gif?login&tpl=mn&u='+ encodeURIComponent(window.location.href+ (window.location.search === "" ? "?" : "&")+ "bdorz_come=1")+ '" name="tj_login" class="lb">登录</a>');</script> <a href=//www.baidu.com/more/ name=tj_briicon class=bri style="display: block;">更多产品</a> </div> </div> </div> <div id=ftCon> <div id=ftConw> <p id=lh> <a href=http://home.baidu.com>关于百度</a> <a href=http://ir.baidu.com>About Baidu</a> </p> <p id=cp>&copy;2017&nbsp;Baidu&nbsp;<a href=http://www.baidu.com/duty/>使用百度前必读</a>&nbsp; <a href=http://jianyi.baidu.com/ class=cp-feedback>意见反馈</a>&nbsp;京ICP证030173号&nbsp; <img src=//www.baidu.com/img/gs.gif> </p> </div> </div> </div> </body> </html>

<type 'str'>
<!DOCTYPE html>
<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer><link rel=stylesheet type=text/css href=http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css><title>ç¾åº¦ä¸ä¸ï¼ä½ å°±ç¥é</title></head> <body link=#0000cc> <div id=wrapper> <div id=head> <div class=head_wrapper> <div class=s_form> <div class=s_form_wrapper> <div id=lg> <img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129> </div> <form id=form name=f action=//www.baidu.com/s class=fm> <input type=hidden name=bdorz_come value=1> <input type=hidden name=ie value=utf-8> <input type=hidden name=f value=8> <input type=hidden name=rsv_bp value=1> <input type=hidden name=rsv_idx value=1> <input type=hidden name=tn value=baidu><span class="bg s_ipt_wr"><input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus></span><span class="bg s_btn_wr"><input type=submit id=su value=ç¾åº¦ä¸ä¸ class="bg s_btn"></span> </form> </div> </div> <div id=u1> <a href=http://news.baidu.com name=tj_trnews class=mnav>æ°é»</a> <a href=http://www.hao123.com name=tj_trhao123 class=mnav>hao123</a> <a href=http://map.baidu.com name=tj_trmap class=mnav>å°å¾</a> <a href=http://v.baidu.com name=tj_trvideo class=mnav>è§é¢</a> <a href=http://tieba.baidu.com name=tj_trtieba class=mnav>è´´å§</a> <noscript> <a href=http://www.baidu.com/bdorz/login.gif?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2f%3fbdorz_come%3d1 name=tj_login class=lb>ç»å½</a> </noscript> <script>document.write('<a href="http://www.baidu.com/bdorz/login.gif?login&tpl=mn&u='+ encodeURIComponent(window.location.href+ (window.location.search === "" ? "?" : "&")+ "bdorz_come=1")+ '" name="tj_login" class="lb">ç»å½</a>');</script> <a href=//www.baidu.com/more/ name=tj_briicon class=bri style="display: block;">æ´å¤äº§å</a> </div> </div> </div> <div id=ftCon> <div id=ftConw> <p id=lh> <a href=http://home.baidu.com>å³äºç¾åº¦</a> <a href=http://ir.baidu.com>About Baidu</a> </p> <p id=cp>&copy;2017&nbsp;Baidu&nbsp;<a href=http://www.baidu.com/duty/>ä½¿ç¨ç¾åº¦åå¿è¯»</a>&nbsp; <a href=http://jianyi.baidu.com/ class=cp-feedback>æè§åé¦</a>&nbsp;äº¬ICPè¯030173å·&nbsp; <img src=//www.baidu.com/img/gs.gif> </p> </div> </div> </div> </body> </html>

<type 'unicode'>
[]
ISO-8859-1    # 这个猜测的不一定对
False
{}
```

**这里面有个问题就是content和text的区别，从返回的结果来说并没有什么区别?**

```python
@property
    def content(self):
        """Content of the response, in bytes."""

@property
    def text(self):
        """Content of the response, in unicode.

        If Response.encoding is None, encoding will be guessed using
        ``chardet``.

        The encoding of the response content is determined based solely on HTTP
        headers, following RFC 2616 to the letter. If you can take advantage of
        non-HTTP knowledge to make a better guess at the encoding, you should
        set ``r.encoding`` appropriately before accessing this property.
        """
```

其实一个是返回的bytes的响应数据，而另一个返回的是unicode的类型的响应数据，因为text中有这样的一段话If Response.encoding is None, encoding will be guessed using chardet 猜测使用的编码方式，所以很大概率得到的数据是乱码，所以以后写代码的统一方式是：在解析网页的时候，先看一下网页的编码是什么<meta http-equiv="Content-Type" content="text/html;charset=utf-8">，然后使用content配合decode的方式进行请求数据的获得

> **resp.text返回的是Unicode型的数据。**
> **resp.content返回的是bytes型也就是二进制的数据**
>
> 常见**文本类型用text，图片、文件类型用contexnt**

```python
# 规范化写法
import requests
r = requests.get("http://www.baidu.com")
print(r.content.decode("utf8","ignore"))    # ignore忽略字符的解析的问题
```

#### 查询参数

两种方式

* 方式1

```python
import requests
req = requests.get("http://httpbin.org/get?name=waws&age=18")
```

* 方式2
  * ==最常见的方式**params**参数，将要传递的查询参数放在字典中==

```python
import requests

data = {"name":"waws","age":18}
headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
url = "http://httpbin.org/get"
req = requests.get(url,params=data,headers=headers)
print req.content.decode("utf8","ignore")
```

请求信息打印

```python
{
  "args": {
    "age": "18", 
    "name": "waws"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);", 
    "X-Amzn-Trace-Id": "Root=1-5e6c1454-574b9d2cca12bee5fd2f69bb"
  }, 
  "origin": "47.56.119.204", 
  "url": "http://httpbin.org/get?age=18&name=waws"
}
```

#### json()

```python
import requests

data = {"name":"waws","age":18}
headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
url = "http://httpbin.org/get"
req = requests.get(url,params=data,headers=headers)
print(req.json())
print(type(req.json()))
```

结果：

```python
{u'origin': u'1.62.147.226', u'headers': {u'X-Amzn-Trace-Id': u'Root=1-5e6c179d-19ab945adf592a23f802718b', u'Host': u'httpbin.org', u'Accept-Encoding': u'gzip, deflate', u'Accept': u'*/*', u'User-Agent': u'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);'}, u'args': {u'age': u'18', u'name': u'waws'}, u'url': u'http://httpbin.org/get?age=18&name=waws'}
<type 'dict'>
```
但需要注意的是，如果返回结果不是JSON格式，便会出现解析错误，抛出**json.decoder.JSONDecodeError**异常
#### headers

与`urllib.request`一样，我们也可以通过`headers`参数来传递头信息,其中最重要的头部信息是**User-Agent**,可以模拟浏览器，一般的反爬虫的措施中最简单的策略就是判断是否是浏览器端进行的请求，则我们需要在头部加上User-Agent进行伪装,还有一个东西也比较有用，可能成为反爬虫的判断之一，就是**Referer**，从哪个网站跳转过来的，需要注意

```python
import requests

data = {"name":"waws","age":18}
headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
url = "http://httpbin.org/get"
req = requests.get(url,params=data,headers=headers)   # 添加参数headers=headers
```

### Post方式

**一般用于登录的使用**

==需要注意的是调用post方法的时候，参数变成了data,而get方法的参数是params==

```python
"""
requests 的POST方法
注意post方式中传递的参数是data,而get 是params
"""
import requests
data = {"user":"admin","pwd":"admin"}
headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
url = "https://httpbin.org/post"
req = requests.post(url,data=data,headers=headers)
print req.content.decode("utf8","ignore")
```

结果展示：

```python
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "pwd": "admin", 
    "user": "admin"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "20", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);", 
    "X-Amzn-Trace-Id": "Root=1-5e6c1cc6-ad4bd0f88bdb8b0c5c98ec13"
  }, 
  "json": null, 
  "origin": "1.62.147.226", 
  "url": "https://httpbin.org/post"
}
```

### 响应

通过比较返回码和内置的成功的返回码，来保证请求得到了正常响应，输出成功请求的消息，否则程序终止，这里我们用`requests.codes.ok`得到的是成功的状态码200

* 带有requests.codes完整代码

```python
import requests

r = requests.get('http://www.jianshu.com')
if not r.status_code == requests.codes.ok:
    print('Request Failed')
else:
    print('Request Successfully')
```

返回码和相对应的代表字符串

```python
# 信息性状态码
100: ('continue',),
101: ('switching_protocols',),
102: ('processing',),
103: ('checkpoint',),
122: ('uri_too_long', 'request_uri_too_long'),
 
# 成功状态码
200: ('ok', 'okay', 'all_ok', 'all_okay', 'all_good', '\\o/', '✓'),
201: ('created',),
202: ('accepted',),
203: ('non_authoritative_info', 'non_authoritative_information'),
204: ('no_content',),
205: ('reset_content', 'reset'),
206: ('partial_content', 'partial'),
207: ('multi_status', 'multiple_status', 'multi_stati', 'multiple_stati'),
208: ('already_reported',),
226: ('im_used',),
 
# 重定向状态码
300: ('multiple_choices',),
301: ('moved_permanently', 'moved', '\\o-'),
302: ('found',),
303: ('see_other', 'other'),
304: ('not_modified',),
305: ('use_proxy',),
306: ('switch_proxy',),
307: ('temporary_redirect', 'temporary_moved', 'temporary'),
308: ('permanent_redirect',
      'resume_incomplete', 'resume',), # These 2 to be removed in 3.0
 
# 客户端错误状态码
400: ('bad_request', 'bad'),
401: ('unauthorized',),
402: ('payment_required', 'payment'),
403: ('forbidden',),
404: ('not_found', '-o-'),
405: ('method_not_allowed', 'not_allowed'),
406: ('not_acceptable',),
407: ('proxy_authentication_required', 'proxy_auth', 'proxy_authentication'),
408: ('request_timeout', 'timeout'),
409: ('conflict',),
410: ('gone',),
411: ('length_required',),
412: ('precondition_failed', 'precondition'),
413: ('request_entity_too_large',),
414: ('request_uri_too_large',),
415: ('unsupported_media_type', 'unsupported_media', 'media_type'),
416: ('requested_range_not_satisfiable', 'requested_range', 'range_not_satisfiable'),
417: ('expectation_failed',),
418: ('im_a_teapot', 'teapot', 'i_am_a_teapot'),
421: ('misdirected_request',),
422: ('unprocessable_entity', 'unprocessable'),
423: ('locked',),
424: ('failed_dependency', 'dependency'),
425: ('unordered_collection', 'unordered'),
426: ('upgrade_required', 'upgrade'),
428: ('precondition_required', 'precondition'),
429: ('too_many_requests', 'too_many'),
431: ('header_fields_too_large', 'fields_too_large'),
444: ('no_response', 'none'),
449: ('retry_with', 'retry'),
450: ('blocked_by_windows_parental_controls', 'parental_controls'),
451: ('unavailable_for_legal_reasons', 'legal_reasons'),
499: ('client_closed_request',),
 
# 服务端错误状态码
500: ('internal_server_error', 'server_error', '/o\\', '✗'),
501: ('not_implemented',),
502: ('bad_gateway',),
503: ('service_unavailable', 'unavailable'),
504: ('gateway_timeout',),
505: ('http_version_not_supported', 'http_version'),
506: ('variant_also_negotiates',),
507: ('insufficient_storage',),
509: ('bandwidth_limit_exceeded', 'bandwidth'),
510: ('not_extended',),
511: ('network_authentication_required', 'network_auth', 'network_authentication')
```

## 高阶功法

### 上传文件

```python
# encoding:utf-8
import json
"""
这个部分完成的是使用request 上传文件
注意我们使用   files = **  这里面的files是一个打开的文件对象
"""
import requests
url = "http://httpbin.org/post?a=Ok"

textfile = {"file":open("request_test.py","rb")} # 一般打开的文件对象

response2 = requests.post(url,files=textfile)
print(response2.text)
```

结果：

```python
{
  "args": {
    "a": "Ok"
  }, 
  "data": "", 
  "files": {
    "file": "# encoding:utf-8\r\n\r\n\"\"\"\r\n\u4ecb\u7ecdrequests\u7684\u57fa\u7840\u4fe1\u606f\r\n\r\n\"\"\"\r\n\r\n\r\nimport requests\r\nr = requests.get(\"http://www.baidu.com\")\r\n\r\nprint(type(r))\r\nprint(r.status_code)\r\nprint(r.url)\r\nprint(r.headers)\r\nprint(r.cookies)\r\nprint(r.content) # \u7f51\u9875\u5185\u5bb9\r\nprint(type(r.content))\r\nprint(r.text)   # \u7f51\u9875\u5185\u5bb9\r\nprint(type(r.text))\r\nprint(r.history)\r\nprint(r.encoding)\r\nprint(r.is_redirect)  # \u662f\u5426\u91cd\u5b9a\u5411\r\nprint(r.links)    # \u5b50\u94fe\u63a5"
  }, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "584", 
    "Content-Type": "multipart/form-data; boundary=f6dfdba37d39fcd6c3e51bffb9da9bb2", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.23.0", 
    "X-Amzn-Trace-Id": "Root=1-5e6c2a5c-f317508c8cee0ffc086c26b0"
  }, 
  "json": null, 
  "origin": "1.62.147.226", 
  "url": "http://httpbin.org/post?a=Ok"
}
```

注意这里面的files字段是一个单独的字段，独立于form之外的存在，路径参数的展示是args,form表单参数的展示是form,上传文件的展示是files.

### ==Cookies==

* cookie的==**获取**==
  * 响应对象的cookies属性

```python
import requests

headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
r = requests.get("https://www.baidu.com/",headers=headers)
print(r.cookies)
for key, value in r.cookies.items():
    print(key + '=' + value)
```

结果

这里我们首先调用`cookies`属性即可成功得到Cookies，可以发现它是`RequestCookieJar`类型。然后用`items()`方法将其转化为元组组成的列表，遍历输出每一个Cookie的名称和值，实现Cookie的遍历解析

```python
<RequestsCookieJar[<Cookie BAIDUID=845842F77144CF02730B6A10BBDAF1F7:FG=1 for .baidu.com/>, <Cookie BIDUPSID=845842F77144CF023943DAB7D50F0F0A for .baidu.com/>, <Cookie H_PS_PSSID=30970_1422_21080_30839_30824_26350_30717 for .baidu.com/>, <Cookie PSTM=1584147541 for .baidu.com/>, <Cookie BDSVRTM=0 for www.baidu.com/>, <Cookie BD_HOME=1 for www.baidu.com/>]>
BAIDUID=845842F77144CF02730B6A10BBDAF1F7:FG=1
BIDUPSID=845842F77144CF023943DAB7D50F0F0A
H_PS_PSSID=30970_1422_21080_30839_30824_26350_30717
PSTM=1584147541
BDSVRTM=0
BD_HOME=1
```

* 使用cookie==**模拟登录**==(一般短期有效,可适用,不行再换用其他方法)
  * 其实就是将登录之后的cookie粘贴下来，然后作为请求头的一部分存在

```python
import requests
 
headers = {
    'Cookie': 'q_c1=31653b264a074fc9a57816d1ea93ed8b|1474273938000|1474273938000; d_c0="AGDAs254kAqPTr6NW1U3XTLFzKhMPQ6H_nc=|1474273938"; __utmv=51854390.100-1|2=registration_date=20130902=1^3=entry_date=20130902=1;a_t="2.0AACAfbwdAAAXAAAAso0QWAAAgH28HQAAAGDAs254kAoXAAAAYQJVTQ4FCVgA360us8BAklzLYNEHUd6kmHtRQX5a6hiZxKCynnycerLQ3gIkoJLOCQ==";z_c0=Mi4wQUFDQWZid2RBQUFBWU1DemJuaVFDaGNBQUFCaEFsVk5EZ1VKV0FEZnJTNnp3RUNTWE10ZzBRZFIzcVNZZTFGQmZn|1474887858|64b4d4234a21de774c42c837fe0b672fdb5763b0',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)
```

* cookies的==**设置**==
  * 在请求的参数中添加cookies,参数是一个字典
  * 在get中传递cookie,网络请求中会使用这个cookie，但是并不会将其存储变成 requests的cookie

```python
# encoding:utf-8

import requests
import time

"""
这个部分主要是request和cookie相关的操作
在get中传递cookie,网络请求中会使用这个cookie，但是并不会将其存储变成 requests的cookie
"""
mycookie = dict(BDSID="zhadu")
# req = requests.get("http://www.baidu.com",cookies = mycookie)

req = requests.get("http://httpbin.org/cookies",cookies = mycookie)
time.sleep(3)
print(req.cookies)
print(req.text)
```

结果：

```python
<RequestsCookieJar[]>
{
  "cookies": {
    "BDSID": "zhadu"
  }
}
```

从网上粘贴下来的大量的cookie的处理，使用RequestsCookieJar对象处理

```python
import requests
 
cookies = 'q_c1=31653b264a074fc9a57816d1ea93ed8b|1474273938000|1474273938000; d_c0="AGDAs254kAqPTr6NW1U3XTLFzKhMPQ6H_nc=|1474273938"; __utmv=51854390.100-1|2=registration_date=20130902=1^3=entry_date=20130902=1;a_t="2.0AACAfbwdAAAXAAAAso0QWAAAgH28HQAAAGDAs254kAoXAAAAYQJVTQ4FCVgA360us8BAklzLYNEHUd6kmHtRQX5a6hiZxKCynnycerLQ3gIkoJLOCQ==";z_c0=Mi4wQUFDQWZid2RBQUFBWU1DemJuaVFDaGNBQUFCaEFsVk5EZ1VKV0FEZnJTNnp3RUNTWE10ZzBRZFIzcVNZZTFGQmZn|1474887858|64b4d4234a21de774c42c837fe0b672fdb5763b0'
jar = requests.cookies.RequestsCookieJar()
headers = {
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
r = requests.get("http://www.zhihu.com", cookies=jar, headers=headers)
print(r.text)
```

### Session

**它通常用于模拟登录成功之后再进行下一步的操作**

> 在requests中，如果直接利用`get()`或`post()`等方法的确可以做到模拟网页的请求，但是这实际上是相当于不同的会话，也就是说相当于你用了两个浏览器打开了不同的页面。
>
> 设想这样一个场景，第一个请求利用`post()`方法登录了某个网站，第二次想获取成功登录后的自己的个人信息，你又用了一次`get()`方法去请求个人信息页面。实际上，这相当于打开了两个浏览器，是两个完全不相关的会话，能成功获取个人信息吗？那当然不能。
>
> 其实解决这个问题的主要方法就是维持同一个会话，也就是相当于打开一个新的浏览器选项卡而不是新开一个浏览器。但是我又不想每次设置`cookies`，那该怎么办呢？这时候就有了新的利器——`Session`对象。

```python
session = requests.Session()  # 会话
mysession = session.get("http://httpbin.org/cookies/set/number/123456789")
mysession = session.get("http://httpbin.org/cookies")
print mysession.text
"""
{
  "cookies": {
    "number": "123456789"
  }
}
"""

mysession = requests.get("http://httpbin.org/cookies/set/number/123456789")
mysession = requests.get("http://httpbin.org/cookies")
print mysession.text

"""
{
  "cookies": {}
}
"""
```

分析上面的两段代码：

* 第一段是开启了一个session对话，当我们进行不同的页面的请求的时候实际上都在同一个对话中，信息共享，cookies共享，然后第一次设置的cookie，在重新获取新网页的时候依旧使用之前设置的cookie;
* 第二段代码是分属于两个对话相当于开启了两个浏览器，这样信息不能共享，第一部设置了cookie,但是在获取新页面的时候并不能获取到之前设置好的cookie

### SSL证书验证

> requests还提供了证书验证的功能。当发送HTTP请求的时候，它会检查SSL证书，我们可以使用`verify`参数控制是否检查此证书。其实如果不加`verify`参数的话，默认是`True`，会自动验证

```python
import requests

"""
这个部分主要完成的是关于request_ssl的处理的部分
"""

import json
# req = requests.get("https://www.12306.cn",verify = True)
"""
默认用证书，不安全报错/没有证书  verify = False 不会报错
"""
req = requests.get("https://www.baidu.com/",verify = False)
print(req)
```

```python
# 注意下这个错误，说明和证书检验有关
requests.exceptions.SSLError: ("bad handshake: Error([('SSL routines', 'tls_process_server_certificate', 'certificate verify failed')],)",)
```

指定本地的证书进行验证

```python
import requests

"""
指定本地的证书用于SSL验证
"""
response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
print(response.status_code)
```

### 代理

* 需要注意两点：
  * 第一个就是proxies是一个字典，键http/https,值代理部分
  * 第二个就是种类两种http代理/socket代理

```python
import requests

# 普通的代理
proxies = {"http":"http://139.129.116.46",
           "https":"http://139.129.116.46"}

print(requests.get("http://www.baidu.com",proxies=proxies).text)

# 需要认证的代理
proxies = {"http":"http://user:password@139.129.116.46:9999",
           "https":"http://user:password@139.129.116.46:9999"}

print(requests.get("http://www.baidu.com",proxies=proxies).text)

# socket5协议代理
"""
安装方式：'requests[socks]'
"""

import requests

proxies = {
    'http': 'socks5://user:password@host:port',
    'https': 'socks5://user:password@host:port'
}
requests.get("https://www.taobao.com", proxies=proxies)
```

### 超时

> 在本机网络状况不好或者服务器网络响应太慢甚至无响应时，我们可能会等待特别久的时间才可能收到响应，甚至到最后收不到响应而报错。为了防止服务器不能及时响应，应该设置一个超时时间，即超过了这个时间还没有得到响应，那就报错。这需要用到timeout参数。这个时间的计算是发出请求到服务器返回响应的时间

```python
# encoding:utf-8
"""
这个部分主要说的是requests的异常处理
"""
import requests
try:
    url = "http://www.google.com/"
    response = requests.get(url,timeout = 3)
    # 连接+读取分离
    # response = requests.get(url,timeout = (5,11,30))
    # 永久等待
    # response = requests.get(url,timeout=None)
    # 永久等待
    # response = requests.get(url)
    print(response.text)
    print(response.status_code)
except Exception as e:
    print("get http://www.google.com/ failed")
print("over")
```

### 身份认证

> 出现以下的情景会需要用到认证的功能
>
> ![3-9](https://github.com/waws520waws/waws_spider/blob/master/image/3-9.jpg)

```python
import requests
"""
requests的认证功能
"""

from requests.auth import HTTPBasicAuth
# 第一种繁琐写法
r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
print(r.status_code)

# 第二种简便写法
r = requests.get('http://localhost:5000', auth=('username', 'password'))
print(r.status_code)
```

### 构造Request对象

```python
from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
```

结果和使用post方法请求一样

```python
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "name": "germey"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "11", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-5e6c3dbc-28c8c2badd6f23ee83a234a4"
  }, 
  "json": null, 
  "origin": "1.62.147.226", 
  "url": "http://httpbin.org/post"
}
```

> **为什么和post方法一样但是比post方法繁琐的多，还要介绍**：
>
> > 有了`Request`这个对象，就可以将请求当作独立的对象来看待，这样在进行队列调度时会非常方便。后面我们会用它来构造一个`Request`队列

## 小点记录

### 字符编码的检测

* 使用chardet的detect方法可以检测网页的编码

```python
# encoding:utf-8
import requests
import chardet

"""
这个部分可以查看网页的编码
"""
response = requests.get("http://www.baidu.cn")
# 注意这里使用text会报错
print(chardet.detect(response.content))

# 设置编码(检测网页编码)
response.encoding = chardet.detect(response.content)
# print response.text
print(response.history)  # 指的是跳转历史
print(response.url)      # 最终响应的url http://www.baidu.cn--->http://www.baidu.com/

"""
{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
[<Response [302]>]
http://www.baidu.com/
"""
```

