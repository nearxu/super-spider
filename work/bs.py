

from bs4 import BeautifulSoup

source = '<div class="tag1 tag2" id="1"><!--这是注释--> Tag test <b>子标签</b></div>'

bs = BeautifulSoup(source,'lxml')

print(type(bs))

tag = bs.div
print(type(tag))

print(tag.attrs,tag['class'],tag['id'])


