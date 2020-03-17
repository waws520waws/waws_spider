"""
ajax实战完整代码
"""
import requests
from urllib.parse import urlencode
import time
from multiprocessing import Pool


def parse_data(data):
    posts = data["Data"]["Posts"]
    for post in posts:
        categoryname = post.get("CategoryName","")
        LastUpdateTime = post.get("LastUpdateTime","")
        LocationName = post.get("LocationName","")
        PostURL = post.get("PostURL","")
        RecruitPostName = post.get("RecruitPostName","")
        Responsibility = post.get("Responsibility","")
        info = {
                    "categoryname":categoryname,
                    "LastUpdateTime":LastUpdateTime,
                    "LocationName":LocationName,
                    "PostURL":PostURL,
                    "RecruitPostName":RecruitPostName,
                    "Responsibility":Responsibility,
        }
        print(info)



def download(pageIndex):
    timestamp = int(float(time.time()) * 1000)
    base_url = "https://careers.tencent.com/tencentcareer/api/post/Query?"
    headers = {
        "referer": "https://careers.tencent.com/search.html?keyword=python",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    params = {
        "timestamp": timestamp,
        "countryId":"",
        "cityId":"",
        "bgIds":"",
        "productId":"",
        "categoryId":"",
        "parentCategoryId":"",
        "attrId":"",
        "keyword":"python",
        "pageIndex":pageIndex,
        "pageSize":"10",
        "language":"zh-cn",
        "area":"cn",
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            print("{0},already downloaded".format(url))
            data = response.json()
            parse_data(data)
    except:
        print("{0},download failed".format(url))




if __name__ == '__main__':
    pool = Pool()
    page_list = [i for i in range(1,81)]
    pool.map(download,page_list)
    pool.close()
    pool.join()