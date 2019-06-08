import random
import urllib.request

def download_image(url):
    name = random.randrange(1,10000)
    full_name = str(name) + '.jpg'
    print(full_name)

    urllib.request.urlretrieve(url,full_name)

download_image('https://pic3.zhimg.com/50/v2-1109c1eb8bfb4eb3de613774237f511a_b.jpg')