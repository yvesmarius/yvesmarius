import requests
import random
from bs4 import BeautifulSoup
from urllib.request import ProxyDigestAuthHandler
from pprint import pprint
import json
proxy_list = []
with open('proxxi.txt') as f:
    for line in f:
        proxy_list.append(line.strip())
# storing functional IPs in a list
working_proxies = []
for i in proxy_list:
    working_proxies.append(i)
    
for i in range(5):
    random_ip = random.choice(working_proxies)
    # rotating IPs from working_proxies
    proxy = {
        'http': 'http://' + random_ip,
        'https': 'http://' + random_ip
    }
    res = requests.get('https://www.fratmat.info/',proxies=proxy,timeout=10,)
    soup=BeautifulSoup(res.text,"html.parser")
    print(soup.json())
navigation=soup.find_all('div', class_="article-info")
for (i,u) in enumerate(navigation):
    press=u.find_all('div', class_="publishTime")
    print(press)
    # print(f"Request received from following IP:\n{res.text}")
saver={'http': 'http://51.38.191.151:80',
'http': 'http://51.91.157.66:80',
'http': 'http://54.36.26.122:80',
'http': 'http://151.106.17.126:1080',
'http': 'http://89.234.182.234:80',
'http': 'http://188.213.31.16:8000',
'http': 'http://137.74.93.21:1080',
'http': 'http://51.79.250.224:3128'}