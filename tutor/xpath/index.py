from lxml import etree
from bs4 import BeautifulSoup
import re
text = '''
<div>
    <ul>
         <li class="item"><a href="link1.html">first item</a></li>
         <li class="item"><a href="link2.html">second item</a></li>
         <li class="item"><a href="link3.html">third item</a></li>
         <li class="item"><a href="link4.html">fourth item</a></li>
         <li class="item"><a href="link5.html">fifth item</a>
     </ul>
 </div>
 '''

# html = etree.HTML(text,etree.HTMLParser())

# result = etree.tostring(html)
# print(result.decode('utf-8'))
# lis = html.xpath('//ul/li')

# for li in lis:
#     name = li.xpath('//a/text()')
#     print(name)

soup = BeautifulSoup(text)

print(soup)

# find_all tagname attrs
lis = soup.find_all('li',class_="item")

#css
csss = soup.select('.item')

# div css

divs = soup.select('li[class="item"]')

for tag in divs:
    print(tag)
