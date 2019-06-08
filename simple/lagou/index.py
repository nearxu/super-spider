from selenium import webdriver

import re
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv
from bs4 import BeautifulSoup
from lxml import etree

class Spider():
    def __init__(self):
        self.url  = 'https://www.lagou.com/jobs/list_web%E5%89%8D%E7%AB%AF?px=default&city=%E6%B7%B1%E5%9C%B3&district=%E5%8D%97%E5%B1%B1%E5%8C%BA#filterBox'
        self.driver = webdriver.Chrome()
        self.works = []
    def run(self):

        self.driver.get(self.url)

        while True:
            source = self.driver.page_source
            self.parse_page(source)
            try:
                next_btn = self.driver.find_element_by_xpath('//div[@class="pager_container"]/span[last()]')
                if "pager_next_disabled" in next_btn.get_attribute("class"):
                    print('no next page')
                    self.driver.close()
                    break
                else:
                    next_btn.click()
            except Exception as e:
                print(e)

            time.sleep(2)
            
    def write_csv(self,item):
        with open('work.csv', 'a', encoding='utf_8_sig', newline='') as f:
            fieldnames = ['name', 'salary', 'descript', 'address','company','time']
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writerow(item)

    def parse_page(self,source):
        # html_content = BeautifulSoup(source)
        html_content = BeautifulSoup(source)

        htmls = html_content.select('.s_position_list .item_con_list .con_list_item')

        # html_content = etree.HTML(source,etree.HTMLParser())
        # with open('html.txt','a',encoding='utf-8') as f:
        #     f.write(source)
            
        # htmls = html_content.xpath('//ul[@class="item_con_list"]/li')
        for html in htmls :
            try:

                name = html.select('.position_link h3')[0].string
                # job_request = html.select('.li_b_l')[0].string
                salary = html.select('.li_b_l span')[0].string
                descript = html.select('.industry')[0].string
                address = html.select('.add em')[0].string
                company = html.select('.company_name a')[0].string
                time = html.select('.format-time')[0].string  
                work = {
                    'name':name,
                    # 'job_request':job_request,
                    'salary':re.sub('[\s/]', '', salary),
                    'descript':re.sub('[\s/]', '', descript),
                    'address':re.sub('[\s/]', '', address),
                    'company':re.sub('[\s/]', '', company),
                    'time':re.sub('[\s/]', '', time),
                }
                self.write_csv(work)
            except Exception as e:
                print(e)


if __name__ == "__main__":
    spider = Spider()

    spider.run()


