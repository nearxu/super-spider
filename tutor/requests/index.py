import requests

url = 'http://www.baidu.com'

headers = {
  "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

params = {
  "kw":"hello"
}

response = requests.get(url,headers=headers)

html = response.text

print(type(html))

proxies = {
    'http:':'http://117.114.149.66:53281'
}

response_post = requests.post(url,headers=headers,data=params,proxies=proxies)

html_post = response.content.decode('utf-8')

print(type(html_post))

with open('baidu.txt','w',encoding='utf-8') as f:
    f.write(html)

