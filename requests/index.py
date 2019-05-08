import requests

r = requests.get('https://api.github.com/user', auth=('nearxu', 'xsp3833858'))

print(r.status_code)

print(r.text, 'text')

print(r.json())

text = r.text

with open('use.txt', 'w') as f:
    w = f.write(text)
    print('write over', w)
