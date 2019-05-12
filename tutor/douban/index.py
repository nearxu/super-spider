import requests

import json 
import time
# https://movie.douban.com/explore#!type=movie&tag=热门&sort=recommend&page_limit=20&page_start=0

url = 'https://movie.douban.com/explore#!'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}

for page_start in range(0,100,20):
    params = {
        "type": "movie",
        "tag": "热门",
        "sort": "recommend",
        "page_limit": "20",
        "page_start": page_start
    }

    time.sleep(1)
    response = requests.get(
        url=url,
        headers=headers,
        params=params
    )

    # result = response.json()

    # pyhton_result = result.load()
    # 获取字节串
    content = response.content
    # 转换成字符串
    string = content.decode('utf-8')
    # 把字符串转成python数据类型
    results = json.loads(string)

    for moive in pyhton_result['subjects']:
        write_moive(moive)

def write_moive(item):
    with open('moive.json','w') as f:
        f.write(item)
