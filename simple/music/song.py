from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

def read_csv():
    with open('name.csv','r',encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            id,name = row
            if id is 'id':
                continue
            else :
                yield id,name

# def get_html_str(url):
#     # pass
#     driver = webdriver.Chrome()
#     driver.get(url)

#     driver.switch_to_frame('g_iframe')
#     time.sleep(3)

#     html = driver.page_source
#     driver.close()
#     return page_src

def parse_html_page(html):
    # pass
     # 这里是使用lxml解析器进行解析,lxml速度快,文档容错能力强,也能使用html5lib
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('span', 'txt')
    return items

def write_to_csv(items,artist_name):
    with open("songs.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["歌手名字", artist_name])

        for item in items:
            writer.writerow([item.a['href'].replace('/song?id=', ''), item.b['title']])

            print('歌曲id:', item.a['href'].replace('/song?id=', ''))
            song_name = item.b['title']
            print('歌曲名字:', song_name)

    csvfile.close()


def get_html_src(url):
    # 可以任意选择浏览器,前提是要配置好相关环境,更多请参考selenium官方文档
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(3)

    # driver.switch_to_frame('x-URS-iframe1557738750238.2686')
    iframe = driver.find_element_by_tag_name('iframe')
    driver.switch_to_frame(iframe)
    # 切换成frame
    # driver.switch_to_frame("g_iframe")
    # 休眠3秒,等待加载完成!
    time.sleep(3)
    page_src = driver.page_source
    driver.close()
    return page_src
    
def main():
    for csv in read_csv():
        print(csv)
        id,name = csv
        url = "https://music.163.com/#/artist?id=" + str(id)
        print("正在获取{}的热门歌曲...".format(name))
        html = get_html_src(url)
        items = parse_html_page(html)
        print("{}的热门歌曲获取完成!".format(name))
        print("开始将{}的热门歌曲写入文件".format(name))
        write_to_csv(items,name)
        print("{}的热门歌曲写入到本地成功!".format(name))

main()

