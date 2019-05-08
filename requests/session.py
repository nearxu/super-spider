import requests

# 会话对象
# 如果你向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升
s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')

r = s.get("http://httpbin.org/cookies")

print(r.text)
