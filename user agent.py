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
