import requests

r = requests.get('*', auth=('*', '*'))

print(r.status_code)

print(r.text, 'text')

print(r.json())

text = r.text

with open('use.txt', 'w') as f:
    w = f.write(text)
    print('write over', w)
