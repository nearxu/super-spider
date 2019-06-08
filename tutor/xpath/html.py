
from bs4 import BeautifulSoup
from lxml import etree
import csv

def get_html():
    with open('html.txt','r') as f:
        return f.read()

def main():
    html_string = get_html()
    html_content = BeautifulSoup(html_string)

    htmls = html_content.select('.s_position_list .item_con_list .con_list_item')
     
    for html in htmls:
    # name = html.xpath('//a[@class="position_link"]/h3/text()')
    # job_request = html.xpath('//div[@class="li_b_l"]/text()')
    # salary = html.xpath('//div[@class="li_b_l"]/span/text()')
    # descript = html.xpath('//div[@class="industry"]/text()')
    # address = html.xpath('//span[@class="add"]/em/text()')
    # company = html.xpath('//div[@class="company_name"]/a/text()')
    # time = html.xpath('//span[@class="format-time"]/text()')
        # names = li.xpath('//a[@class="position_link"]/h3/text()')
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
                    'salary':salary,
                    'descript':descript,
                    'address':address,
                    'company':company,
                    'time':time,
                }
        write_csv(work)

def write_csv(item):
    with open('works.csv','wb',encoding='utf-8') as f:
        fieldnames = ['name', 'salary', 'descript', 'address','company','time']
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writerow(item)

main()

# def main1():
#     html = get_html()
#     html_content = etree.HTML(html,etree.HTMLParser())
#     htmls = html_content.xpath('//ul[@class="item_con_list"]/li')

#     for d in htmls:
#         print(d)
#         name = d.xpath('//a[@class="position_link"]/h3/text()')
#         print(name)

# main1()

