import json
import csv
from selenium import webdriver
from bs4 import BeautifulSoup


def init(url, word):
    url = url
    word = word
    driver = login(url)

    urls = get_urls(driver)

    print(urls, 'urls')


def login(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver


def get_urls(driver):

    page_number = int(driver.find_element_by_xpath(
        "//div[@class='content__pg']").get_attribute('data-totalpage'))

    urls = []

    url_single = get_list_urls_single(driver)
    urls += url_single

    urls = list(set(urls))

    return urls


def get_list_urls_single(driver):
    list_urls_single = []
    list_a = driver.find_element_by_xpath(
        "//a[@class='content__list--item--aside']")
    for i in list_a:
        list_urls_single.append(i.get_attribute('href'))
    return list_urls_single


if __name__ == "__main__":
    init(url='https://sz.zu.ke.com/zufang/', word='')
