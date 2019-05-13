from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv



def get_html_src(url):
    driver = webdriver.Chrome()
    driver.get(url)

    driver.implicitly_wait(3)

    # driver.switch_to_frame('x-URS-iframe1557738750238.2686')
    iframe = driver.find_element_by_tag_name('iframe')
    driver.switch_to_frame(iframe)

    page_src = driver.page_source

    driver.close()
    return page_src

def parse_html(html):
    soup = BeautifulSoup(html,'lxml')
    items = soup.find_all('span','txt')
    print(items)
    return items

def write_csv(items):
    with open('top.csv','a') as f:
       w = csv.writer(f)

       for item in items:
            w.writerow([item.a['href'].replace('/song?id=', ''), item.b['title']])
            print('歌曲id:', item.a['href'].replace('/song?id=', ''))
            song_name = item.b['title']
            print('歌曲名字:', song_name)
def main():
    url = 'https://music.163.com/#/discover/toplist?id=3778678'

    html = get_html_src(url)

    items = parse_html(html)

    write_csv(items)

main()
