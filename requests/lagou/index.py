import json
import requests
import time
import csv

proxies = {
    "http": "http://123.183.19.67:8118",
}


def parse_json(response):
    result = response.json()
    print(result, 'result')
    if result:
        info = result['content']['positionResult']['result']
        for job in info:
            if job:
                yield {
                    '岗位id': job['positionId'],
                    '公司全名': job['companyFullName'],
                    '福利待遇': job['companyLabelList'],
                    '工作地点': job['district'],
                    '学历要求': job['education'],
                    '工作类型': job['firstType'],
                    '发布时间': job['formatCreateTime'],
                    '职位名称': job['positionName'],
                    '薪资': job['salary'],
                    '工作年限': job['workYear']
                }
    else:
        return None


def get_json(url, datas):
    my_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?city=%E4%B8%8A%E6%B5%B7&cl=false&fromSearch=true&labelWords=&suginput=',
    }
    cookies = {
        'Cookie': '_ga=GA1.2.1874976523.1544007181; user_trace_token=20181205185345-09812c8b-f87c-11e8-8ce2-5254005c3644; LGUID=20181205185345-0981324f-f87c-11e8-8ce2-5254005c3644; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22168dc353e2b24d-084eac6449f41b-b781636-2304000-168dc353e2cb88%22%2C%22%24device_id%22%3A%22168dc353e2b24d-084eac6449f41b-b781636-2304000-168dc353e2cb88%22%7D; LG_LOGIN_USER_ID=f657e34e2aba35ab96c633a4decfb21900511087396b9f6a; JSESSIONID=ABAAABAAADEAAFI619C8FE6DCD8BF3131FAB894E3C1DAFF; _gid=GA1.2.1308081911.1557389790; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1555384609,1557389791; LGSID=20190509161634-c294c033-7232-11e9-9ee2-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_hotsearch; X_HTTP_TOKEN=3e0a2006364e5b140089837551b62946723d89c2ec; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1557389796; LGRID=20190509161640-c5bda3a1-7232-11e9-9ee2-5254005c3644; SEARCH_ID=6cc0f10585ce406381182d7a3787c9a5'
    }
    time.sleep(4)
    try:

        response = requests.post(url=url, headers=my_headers,
                                 cookies=cookies, data=datas, proxies=proxies)
        if response.status_code == 200:
            result = response.json()
            info = result['content']['positionResult']['result']
            for job in info:
                if job:
                    yield {
                        '岗位id': job['positionId'],
                        '公司全名': job['companyFullName'],
                        '福利待遇': job['companyLabelList'],
                        '工作地点': job['district'],
                        '学历要求': job['education'],
                        '工作类型': job['firstType'],
                        '发布时间': job['formatCreateTime'],
                        '职位名称': job['positionName'],
                        '薪资': job['salary'],
                        '工作年限': job['workYear']
                    }
        else:
            return None
    except Exception as e:
        print(e)
        return None


def write_csv(item):
    with open('lagou.csv', 'a', encoding='utf_8_sig', newline='') as f:
        fieldnames = ['岗位id', '公司全名', '福利待遇', '工作地点',
                      '学历要求', '工作类型', '发布时间', '职位名称', '薪资', '工作年限']
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writerow(item)


def main():
    page = 50
    key = 'web前端'
    city = '深圳'

    # info_result = []
    # title = ['岗位id','公司全名','福利待遇','工作地点','学历要求','工作类型','发布时间','职位名称','薪资','工作年限']
    # info_result.append(title)

    for x in range(1, page):
        url = 'https://www.lagou.com/jobs/positionAjax.json?&needAddtionalResult=false'
        datas = {
            'first': True,
            'pn': x,
            'kd': key,
            'city': city
        }
        info = get_json(url, datas)
        if info:
            for item in info:
                write_csv(item)
        else:
            print('end')
            break


if __name__ == "__main__":
    main()
