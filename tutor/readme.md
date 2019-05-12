### some tutor from

https://github.com/CriseLYJ/Python-crawler-tutorial-starts-from-zero/blob/master/JSON%20数据提取.md


### json and python

object dict

array list

string unicode

number int

true True

null None

json string => json.loads()  python dict 

json string <= json.dumps()  python

json object => json.load() python

json object <= json.dump() python

### request

response 常用属性
response.text 返回响应内容，响应内容为 str 类型
respones.content 返回响应内容,响应内容为 bytes 类型
response.status_code 返回响应状态码
response.request.headers 返回请求头
response.headers 返回响应头
response.cookies 返回响应的 RequestsCookieJar 对象
response.content 转换 str 类型


##### 获取字节数据
content = response.content
##### 转换成字符串类型
html = content.decode('utf-8')


