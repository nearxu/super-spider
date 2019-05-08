import requests

import lxml.etree

import os

import telnetlib

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}


def get_proxy(page):
    response = requests.get(
        'http://www.xicidaili.com/nn/{}'.format(page), headers=headers)
    print('response type:', type(response))

    proxy_list = []

    selector = lxml.etree.HTML(response.text)
    rows = selector.xpath('//*[@id="ip_list"]//tr')
    rows_total = len(rows)
    row_xpath_head = '//*[@id="ip_list"]//tr['
    row_ip_xpath_tail = ']/td[2]/text()'
    row_port_xpath_tail = ']/td[3]/text()'
    for i in range(1, rows_total):
        ip_xpath = row_xpath_head + str(i+1) + row_ip_xpath_tail
        port_xpath = row_xpath_head + str(i+1) + row_port_xpath_tail
        ip = selector.xpath(ip_xpath)[0]
        port = selector.xpath(port_xpath)[0]
        ip_port = ip + ':' + port
        print(ip_port, 'ip-port')
        proxy_list.append(ip_port)
    print(proxy_list, 'list')
    return proxy_list


def test_ip(proxy_ip):
    ip_port = proxy_ip.split(':')
    ip = ip_port[0]
    port = ip_port[1]

    try:
        telnetlib.Telnet(ip, port, timeout=10)
    except:
        return False
    else:
        return True

# write


def write_txt(ip):
    with open('ip.txt', 'a') as f:
        f.write(ip+'\n')

# delete


def del_file():
    file_path = './ip.txt'
    if os.path.exists(file_path):
        os.remove(file_path)


def run():
    del_file
    proxy_ip_port_list = []
    for i in range(1, 2):
        proxy_ip_port_list += get_proxy(i)
    for x in range(100):
        proxy_ip_port = proxy_ip_port_list[x]
        is_valid = test_ip(proxy_ip_port)
        # is_valid = True
        print(is_valid, 'wether is valid')
        if is_valid:
            write_txt(proxy_ip_port)


if __name__ == "__main__":
    run()
