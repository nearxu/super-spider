import requests
from lxml import etree

class Login(object):
    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Referer': 'https://github.com/',
            'Host': 'github.com'
        }

        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.session = requests.Session()

    def login(self):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.get_token(),
            'login': self.email,
            'password': self.password
        }
        response = self.session.post(self.post_url,data=post_data,headers = self.headers)

        if response.status_code == 200:
            print('login success')
        else :
            print('fail')
        return response.text

    def get_token(self):
        response = self.session.get(self.login_url,headers=self.headers)

        html = etree.HTML(response.content.decode())
        token = html.xpath('//input[@name="authenticity_token"]/@value')[0]

        return token

if __name__ == "__main__":
    email = input('input email')
    password = input('input password')
    spider = Login(email,password)

    text = spider.login()

