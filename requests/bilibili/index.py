import requests
import json
import random
import sys
import datetime
import time
import csv
from multiprocessing.dummy import Pool as ThreadPool
head = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://space.bilibili.com/45388',
    'Origin': 'http://space.bilibili.com',
    'Host': 'space.bilibili.com',
    'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
}

# proxies = {
#     'http':'http://121.31.145.235:8123',
#     'http':'http://112.85.129.106:9999',
# }


def load_user_agent():
    uas = []
    with open('C:/Users/nearxu/Desktop/super-spider/requests/bilibili/user_agent.txt', 'r') as f:
        for ua in f.readlines():
            if ua:
                uas.append(ua.strip())
    random.shuffle(uas)
    return uas


uas = load_user_agent()


def datetime_to_timestamp_in_milliseconds():     
    return int(round(time.time() * 1000))

# 521400 521500
# 521500 521600
# for r ub range(521400, 521410):

# for r in range(5214, 5215):
user_ids = []
for i in range(521400, 521856):
    user_ids.append(str(i))

def get_page(user_id):
    url = 'https://space.bilibili.com/' + user_id
    payload = {
        '_': datetime_to_timestamp_in_milliseconds(),
        'mid': user_id
    }

    ua = random.choice(uas)
    print(ua)

    head = {
        'User-Agent': ua,
        'Referer': 'https://space.bilibili.com/'+user_id +'?from=search&seid=' + str(random.randint(10000, 50000))
    }

    response = requests.session().post(
        'http://space.bilibili.com/ajax/member/GetInfo',
        headers=head,
        data=payload).text

    try:
        jsonDict = json.loads(response)
        status = jsonDict['status'] if 'status' in jsonDict.keys(
        ) else False
        print(status , 'status')
        if status == True:
            if 'data' in jsonDict.keys():
                jsData = jsonDict['data']
                mid = jsData['mid']
                name = jsData['name']
                sex = jsData['sex']
                rank = jsData['rank']
                face = jsData['face']
                regtimestamp = jsData['regtime']
                regtime_local = time.localtime(regtimestamp)
                regtime = time.strftime(
                    "%Y-%m-%d %H:%M:%S", regtime_local)
                spacesta = jsData['spacesta']
                birthday = jsData['birthday'] if 'birthday' in jsData.keys(
                ) else 'nobirthday'
                sign = jsData['sign']
                level = jsData['level_info']['current_level']
                OfficialVerifyType = jsData['official_verify']['type']
                OfficialVerifyDesc = jsData['official_verify']['desc']
                vipType = jsData['vip']['vipType']
                vipStatus = jsData['vip']['vipStatus']
                toutu = jsData['toutu']
                toutuId = jsData['toutuId']
                coins = jsData['coins']

                print('success get user info')

                # try:
                #     res = requests.get(
                #         'https://api.bilibili.com/x/relation/stat?vmid=' +
                #         str(mid) + '&jsonp=jsonp'
                #     ).text()
                #     viewinfo = requests.get(
                #         'https://api.bilibili.com/x/space/upstat?mid=' + str(mid) + '&jsonp=jsonp').text

                #     js_fans_data = json.loads(res)
                #     js_viewdata = json.loads(viewinfo)
                #     following = js_fans_data['data']['following']
                #     fans = js_fans_data['data']['follower']
                #     archiveview = js_viewdata['data']['archive']['view']
                #     article = js_viewdata['data']['article']['view']
                # except:
                #     following = 0
                #     fans = 0
                #     archiveview = 0
                #     article = 0

            else:
                print('no data')

            try:
                # "following":following, "fans":fans, "archiveview":archiveview, "article":article
                write_csv({"mid":mid, "name":name,"sex":sex, "rank":rank, "face":face, "regtime":regtime, "spacesta":spacesta, "birthday":birthday, "sign":sign, "level":level, "OfficialVerifyType":OfficialVerifyType, "OfficialVerifyDesc":OfficialVerifyDesc, "vipType":vipType, "vipStatus":vipStatus,
                          "toutu":toutu, "toutuId":toutuId, "coins":coins}
                          )
            except Exception as e:
                print(e)
                print('write error')
        else:
            print('error', url)
    except Exception as e:
        print(e)
        pass


def write_csv(item):
    # 'following','fans','archiveview','article'
    with open('comment.csv', 'a', encoding='utf_8_sig', newline='') as f:
        fieldnames = ['mid', 'name', 'sex', 'rank', 'face', 'regtime','spacesta','birthday',
        'sign','level','OfficialVerifyType','OfficialVerifyDesc','vipType','vipStatus','toutu',
        'toutuId','coins']
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writerow(item)


if __name__ == "__main__":
    # pool = ThreadPool(1)
    # try:
    #     # results = pool.map(get_page, urls)
    # except Exception as e:
    #     print(e)

    for user_id in user_ids:
      get_page(user_id)
      time.sleep(1)