
from selenium import webdriver
# 用于 add_argument('--headless') 等选项设置
from selenium.webdriver.chrome.options import Options
# 显示等待
from selenium.webdriver.support.ui import WebDriverWait
# 设置等待执行语句
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# 结束等待
from selenium.common.exceptions import TimeoutException
# 对搜索关键词进行 URL 编码

import requests

import random

import time
from lxml import etree

# 对搜索关键词进行 URL 编码
from urllib.parse import quote

import csv


class LagouSpider():
    def __init__(self, search_word, city):
        if city in ['全国站', '全国', '']:
            self.url = "https://www.lagou.com/jobs/list_%s?labelWords=&fromSearch=true&suginput=" \
                % (quote(search_word))
        else:
            self.url = "https://www.lagou.com/jobs/list_%s?city=%s&cl=false&fromSearch=true&labelWords=&suginput=" \
                % (quote(search_word), quote(city))

        self.all_links = []

    def start_browser(self):
        driver_path = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('log-level=3')  # 不显示--headless时的日志信息
        self.driver = webdriver.Chrome(
            driver_path, chrome_options=chrome_options)

    def run2(self, ten_links):
        # self.start_browser()

        for link in ten_links:
            try:
                time.sleep(1)
                self.request_page(link)
            except TimeoutError:
                time.sleep(1)
                try:
                    self.request_page(link)
                except TimeoutError:
                    print('error url', link)
        self.driver.quit()

    def request_page(self, url):
        try:
            # 在当前窗口中同步执行javascript打开新窗口访问url
            # 执行后打开新页面（句柄追加一个新元素）
            self.driver.execute_script("window.open('%s')" % url)
            # driver.switch_to.window：将焦点切换到指定的窗口
            # driver.window_handles：返回当前会话中所有窗口的句柄
            # 切换到新打开的窗口，即第2个--index==1
            self.driver.switch_to.window(self.driver.window_handles[1])
            # 显式等待5s直到职位名称节点出现（解决打开页面空白无内容、长时间等待问题）
            WebDriverWait(self.driver, timeout=5).until(
                EC.presence_of_element_located((By.XPATH, "//span[@class='name']")))
            # 获取并解析详情页的网页源代码
            source = self.driver.page_source
            item = self.parse_page(source)

            print(item, 'item')
            self.write_csv(item)
        except TimeoutError:
            print('error driver:', url)

    def parse_page(self, source):
        html = etree.HTML(source)
        # 对html用xpath语法找到职位名称所在节点的文本，即position_name
        position_name = html.xpath("//span[@class='name']/text()")[0]
        # 对html用xpath语法找到职位id所在的节点，提取获得position_id
        position_id = html.xpath(
            "//link[@rel='canonical']/@href")[0].split('/')[-1].replace('.html', '')

        # 找到职位标签，依次获取：薪资、城市、年限、受教育程度、全职or兼职
        job_request_spans = html.xpath('//dd[@class="job_request"]//span')
        salary = job_request_spans[0].xpath(
            './/text()')[0].strip()         # 列表索引0==xpath第1个节点
        # city = job_request_spans[1].xpath(
        #     './/text()')[0].strip().replace("/", "").strip()
        work_year = job_request_spans[2].xpath(
            './/text()')[0].strip("/").strip()
        education = job_request_spans[3].xpath(
            './/text()')[0].strip("/").strip()

        # 找到公司标签，获取company_short_name
        company_short_name = html.xpath(
            '//dl[@class="job_company"]//em/text()')[0].replace("\n", "").strip()
        # 找到公司标签中的industry_field和finance_stage
        # company_infos = html.xpath(
        #     '//dl[@class="job_company"]//li')   # 注意该节点下的text()索引0和2是空的
        # industry_field = company_infos[0].xpath(
        #     './/text()')[1].replace("\n", "").strip()
        # finance_stage = company_infos[1].xpath(
        #     './/text()')[1].replace("\n", "").strip()

        # 找到工作地址所在的区
        district = html.xpath(
            '//div[@class="work_addr"]/a[2]/text()')[0].strip()

        # 找到职位诱惑，获取position_advantage
        position_advantage = html.xpath(
            '//dd[@class="job-advantage"]//p/text()')[0].strip("/").strip().replace("，", ",")
        # 找到所有职位标签，用","连接成字符串
        # position_labels = ",".join(html.xpath(
        #     '//li[@class="labels"]//text()')).strip()

        formatCreateTime = html.xpath('//span[@class="format-time"]//text()')

        return {
            '岗位id': position_id,
            '公司全名': company_short_name,
            '福利待遇': position_advantage,
            '工作地点': district,
            '学历要求': education,
            '发布时间': formatCreateTime,
            '职位名称': position_name,
            '薪资': salary,
            '工作年限': work_year
        }

    def write_csv(self, item):
        with open('lagou.csv', 'a', encoding='utf_8_sig', newline='') as f:
            fieldnames = ['岗位id', '公司全名', '福利待遇', '工作地点',
                          '学历要求', '发布时间', '职位名称', '薪资', '工作年限']
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writerow(item)

    def run1(self):
        self.start_browser()
        self.driver.get(self.url)
        count_page = 1

        while True:
            source = self.driver.page_source

            self.get_all_links(source)

            next_btn = self.driver.find_element_by_xpath(
                '//div[@class="pager_container"]/span[last()]')

            return list(set(self.all_links))

            # if "pager_next_disabled" in next_btn.get_attribute("class"):
            #     self.driver.quit()
            #     return list(set(self.all_links))
            # else:
            #     next_btn.click()
            #     count_page += 1
            #     time.sleep(random.randint(2, 4))

            time.sleep(random.randint(3, 5))

    def get_all_links(self, source):
        html = etree.HTML(source)

        links = html.xpath('//a[@class="position_link"]/@href')
        self.all_links += links


def main(word, city):
    start_time = time.time()

    spider = LagouSpider(word, city)
    needed_all_links = spider.run1()

    print(needed_all_links, 'needed_all_links')

    # 将所有职位详情url以10位单位拆分成嵌套列表
    # nested_all_links = [needed_all_links[i:i + 10]
    #                     for i in range(0, len(needed_all_links), 10)]

    count = 10
    for ten_link in needed_all_links:
        spider.run2(ten_link)
        print('Have fetched %s positions.\n' % str(count))
        # count计数调整间隔时间，避免请求过多弹出登录
        time.sleep(random.randint(6, 12) * (count // 100 + 1))
        count += 10

    # 记录项目结束时间
    end_time = time.time()
    print('\n【项目完成】\n【总共耗时：%.2f分钟】' % ((end_time - start_time) / 60))


if __name__ == "__main__":
    main(word='web前端', city='深圳')
