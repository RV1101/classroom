import requests
from bs4 import BeautifulSoup
import os

os.makedirs("E:\jandan")
os.chdir("E:\jandan")
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
all_url = 'http://jandan.net/ooxx/'
start_html = requests.get(all_url,  headers=headers)
Soup = BeautifulSoup(start_html.text, 'lxml')
all_img = Soup.find('ol', class_='commentlist').find_all('img')
for img in all_img:
    src=img['src']
    src_url='http:'+src
    name = src_url[-9:-4]
    pic = requests.get(src_url, headers=headers)
    f = open(name+'.jpg', 'ab')
    f.write(pic.content)
    f.close()