import requests

import time
from urllib.parse import urlencode

import matplotlib.pyplot as plt
import numpy as np

host = 'm.weibo.cn'
base_url = 'https://%s/api/container/getIndex?' % host
user_agent = 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 wechatdevtools/0.7.0 MicroMessenger/6.3.9 Language/zh_CN webview/0'

headers = {
    'Host': host,
    'Referer': 'https://m.weibo.cn/u/5680339910',
    'User-Agent': user_agent
}

CK = {
    'type': 'uid',
    'value': 5680339910,  # 陈珂
    'containerid': 1005055680339910
}
HCY = {
    'type': 'uid',
    'value': 6371457043,
    'containerid': 1005056371457043
}
LJP = {
    'type': 'uid',
    'value': 5680339910,
    'containerid': 1005055681828458
}
XCW = {
    'type': 'uid',
    'value': 6375473647,
    'containerid': 1005056375473647
}
XHL = {
    'type': 'uid',
    'value': 6519204388,
    'containerid': 1005056519204388
}
ZQY = {
    'type': 'uid',
    'value': 5886585193,
    'containerid': 1005055886585193
}
LSS = {
    'type': 'uid',
    'value': 6372319982,
    'containerid': 1005056372319982
}
ZAJ = {
    'type': 'uid',
    'value': 5787334703,
    'containerid': 1005055787334703
}
ZYX = {
    'type': 'uid',
    'value': 6224125612,
    'containerid': 1005056224125612
}
LHY = {
    'type': 'uid',
    'value': 5886586996,
    'containerid': 1005055886586996
}
GYJ = {
    'type': 'uid',
    'value': 5685467003,
    'containerid': 1005055685467003
}
LKJ = {
    'type': 'uid',
    'value': 6375457642,
    'containerid': 1005056375457642
}
LZ = {
    'type': 'uid',
    'value': 6195974151,
    'containerid': 1005056195974151
}
CJH = {
    'type': 'uid',
    'value': 6226275725,
    'containerid': 1005056226275725
}
XLL = {
    'type': 'uid',
    'value': 5786332015,
    'containerid': 1005055786332015
}
CJY = {
    'type': 'uid',
    'value': 6221966810,
    'containerid': 1005056221966810
}
LJ = {
    'type': 'uid',
    'value': 6535125009,
    'containerid': 1005056535125009
}
YSQ = {
    'type': 'uid',
    'value': 6729713146,
    'containerid': 1005056729713146
}
YQY = {
    'type': 'uid',
    'value': 5786337946,
    'containerid': 1005055786337946
}
FBB = {
    'type': 'uid',
    'value': 6376516458,
    'containerid': 1005056376516458
}
LQJ = {
    'type': 'uid',
    'value': 5681479865,
    'containerid': 1005055681479865
}

nameG={'CK','HCY','LJP','XCW','XHL','ZQY','LSS','ZAJ','ZYX','LHY','GYJ','LKJ','LZ','CJH','XLL','CJY','LJ','YSQ','YQY','FBB','LQJ'}
dict_name={'CK':0,'HCY':0,'LJP':0,'XCW':0,'XHL':0,'ZQY':0,'LSS':0,'ZAJ':0,'ZYX':0,'LHY':0,'GYJ':0,'LKJ':0,'LZ':0,'CJH':0,'XLL':0,'CJY':0,'LJ':0,'YSQ':0,'YQY':0,'FBB':0,'LQJ':0}
dict_fans={'CK':0,'HCY':0,'LJP':0,'XCW':0,'XHL':0,'ZQY':0,'LSS':0,'ZAJ':0,'ZYX':0,'LHY':0,'GYJ':0,'LKJ':0,'LZ':0,'CJH':0,'XLL':0,'CJY':0,'LJ':0,'YSQ':0,'YQY':0,'FBB':0,'LQJ':0}


def get_fan_page(params):
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(e)
        return None

def parse_fan_page(json):
  items = json.get('data').get('userInfo')
  num = items['followers_count']
  username = items['screen_name'] 
  return username,num 

Gmembers_nums = 21

if __name__ == "__main__":
    for name in nameG:
        json = get_fan_page(eval(name))
        member,fan_nums = parse_fan_page(json)
        dict_name[name] = member
        dict_fans[name] = fan_nums
        time.sleep(0.5)
    
    # sort
    dict_order = sorted(dict_fans.items(),key = lambda x:x[1],reverse = True)

    values = []
    xname = []

    for i  in range(Gmembers_nums):
        # 包含每个柱子下标的序列
        xname.append((dict_name[dict_order[i][0]]))
        # 包含每个柱子对应值的序列
        values.append(dict_order[i][1]) 
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['font.family']='sans-serif'

    index= 2*np.arange(Gmembers_nums)
    p2 = plt.bar(index,values , 0.5, label="粉丝数", color="#87CEFA")

    # show
    for x,y in zip(index,values):
      plt.text(x,y+0.1,'%d' %y,ha='center',va='bottom')
    # 添加纵横轴的刻度
    plt.xticks(index, xname,rotation=60)

    plt.show()