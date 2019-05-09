import requests
import json
import time
import random
import csv

count = 1

limit = 30

movieId = '248906'

offset = 0
ts = 0

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}


def get_url():
    global offset
    url = 'http://m.maoyan.com/review/v2/comments.json?movieId=' + movieId + '&userId=-1&offset=' + str(
          offset) + '&limit=' + str(limit) + '&ts=' + str(ts) + '&type=3'
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


def parse_json(data):
    global count
    global offset
    global limit
    global ts

    res = json.loads(data)
    comments = res['data']['comments']

    for comment in comments:
        comment_time = comment['time']
        if ts == 0:
            ts = comment_time
            ts_duration = comment_time
        if comment_time != ts and ts == ts_duration:
            ts_duration = comment_time
        if comment_time != ts_duration:
            ts = ts_duration
            offset = 0
            return get_url()

        else:
            content = comment['content'].strip().replace('\n', '。')
            write_csv(time.strftime("%Y-%m-%d %H:%M:%S",
                                    time.localtime(comment_time/1000)), content)

    if res['paging']['hasMore']:
        offset += limit
        return get_url()
    else:
        return None


def write_csv(datetime, comment):
    with open('comment.csv', 'a', encoding='utf_8_sig', newline='') as f:
        # fieldnames = ['index', 'user', 'type', 'rate', 'time', 'desc']
        # w = csv.DictWriter(f, fieldnames=fieldnames)
        w = csv.writer(f, delimiter=';')
        w.writerow([datetime, comment])


if __name__ == "__main__":
    url = get_url()
    while True:
        try:
            data = open_url(url)
            if data:
                url = parse_json(data)
                if not url:
                    break
        except Exception as e:
            print(e)
            time.sleep(random.random()*3)
