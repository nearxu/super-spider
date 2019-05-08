import requests

headers = {'user-agent': 'my-app/0.0.1'}

url = 'https://api.github.com/some/endpoint'

r = requests.get(url, headers=headers)

print(r.status_code)

print(r.text)
