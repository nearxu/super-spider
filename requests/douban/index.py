import requests

from bs4 import BeautifulSoup

import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}


def create_url(start):
    url = 'https://movie.douban.com/subject/27102569/comments?start=' + \
        start + '&limit=20&sort=new_score&status=P'
    return url


def open_url(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        print(e)
        return None


def parse_html(html):
    soup = BeautifulSoup(html, features='html.parser')
    comments = soup.find_all(class_='comment-item')

    global number
    for comment in comments:
        user = comment.find('a').attrs['title']
        sp = comment.findAll('span')
        types = sp[3].text
        try:
            rate = comment.find('span', class_='rating').attrs['title']
        except AttributeError:
            rate = 'no rate'
        time = comment.find('span', class_='comment-time').attrs['title']
        desc = comment.find('span', class_='short').text

        yield {
            'index': number,
            'user': user,
            'type': types,
            'rate': rate,
            'time': time,
            'desc': desc
        }

        number += 1


def write_csv(item):
    with open('comment.csv', 'a', encoding='utf_8_sig', newline='') as f:
        fieldnames = ['index', 'user', 'type', 'rate', 'time', 'desc']
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writerow(item)


def main():
    global number
    number = 1
    while True:
        if number == 1:
            start = '00'
        else:
            start = str(number-1)
        url = create_url(start)
        html = open_url(url)
        if html:
            print(url)
            for item in parse_html(html):
                write_csv(item)
        else:
            print('end')
            break


if __name__ == "__main__":
    main()
