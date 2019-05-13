import requests

class TiebaSpider():

    def __init__(self,word,max):
        self.max = max
        self.word = word
        self.url = "https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
        }

    def get_urls(self):
        urls = []
        for m in range(0,self.max,50):
            url = self.url.format(self.word,m)
            urls.append(url)
        return urls

    def get_content(self,url):

        response = requests.get(url,headers = self.header)
        return response

    def get_item(self,content):
        pass
    
    def run(self):
        urls_list = self.get_urls()

        for url in urls_list:
            content = self.get_content(url)
            print(content.text)


if __name__ == "__main__":
    spider = TiebaSpider('王者荣耀小鲁班',150)
    spider.run()