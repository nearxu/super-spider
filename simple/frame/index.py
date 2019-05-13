from selenium import webdriver

url = 'https://mail.163.com/'

def main():
    driver = webdriver.Chrome()

    driver.get(url)

    driver.implicitly_wait(3)

    # driver.switch_to_frame('x-URS-iframe1557738750238.2686')
    iframe = driver.find_element_by_tag_name('iframe')
    driver.switch_to_frame(iframe)
    driver.find_element_by_name('email').send_keys('123')
    driver.find_elements_by_name('password').send_keys('456')

main()