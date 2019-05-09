
import requests
import json
import csv
from bs4 import BeautifulSoup
from time import sleep
import random

count = 1

url = 'https://www.zhihu.com/api/v4/questions/28997505/answers'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}


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

# json.loads() change to dict


def parse_json(data):
    res = json.loads(data)

    print(res, 'res')

    global count

    for an in res['data']:
        if an['type'] == 'answer':
            # question = an['question']['title']
            # soup = BeautifulSoup(an['content'],
            #                      features='html.parser')

            # answer = soup.text.strip().replace('\n', '。')
            # vote = an['target']['voteup_count']

            # get user
            name = an['author']['name']
            headline = an['author']['headline']
            gender = an['author']['gender']
            write_user_csv(
                {'name': name, 'headline': headline, 'gender': gender})
            count += 1

    return get_next_url(res)


def get_next_url(res):
    try:
        if not res['paging']['is_end']:
            url = res['paging']['next']
            write_url_csv(res['paging'])
            return url
        else:
            return None
    except Exception as e:
        print(e)
        return None


def write_url_csv(item):
    with open('url.csv', 'a', encoding='utf_8_sig', newline='') as f:
        fieldnames = ['is_start', 'is_end', 'previous', 'next', 'totals']
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writerow(item)


def write_user_csv(item):
    with open('user.csv', 'a', encoding='utf_8_sig', newline='') as f:
        fieldnames = ['name', 'headline', 'gender']
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writerow(item)


if __name__ == "__main__":
    count = 1

    while True:
        try:
            data = open_url(url)
            if data:
                url = parse_json(data)
                if not url:
                    print('end')
                    break
        except Exception as e:
            print(e)
            sleep(random.random()*3)
