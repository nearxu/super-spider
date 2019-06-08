import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}


def open_url():
    url = 'https://qq.yh31.com/zjbq/'

    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        else :
            return None
    except Exception as e:
        print(e)
        return None

def parse_html(html):
    print(html,'html')
    soup = BeautifulSoup(html,features='html.parser')
    title_pages = soup.find_all(id="qh_con1")
    return title_pages



if __name__ == "__main__":
    html = open_url()
    content = parse_html(html)
    print(content)
