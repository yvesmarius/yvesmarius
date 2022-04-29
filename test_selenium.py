import json
import requests
from bs4 import BeautifulSoup
url1="https://just-scrape-it.com/"
response=requests.get(url1)
up=[]
if response.ok:
    soup=BeautifulSoup(response.text,"html.parser")
    applink=soup.find_all('li', class_="mobile-nav__item border-bottom")  
for i in applink:
    link=i.find('a')
    print(link['href'])          
with open("save.json",'w') as f:
    up.append(link['href'])
    j=json.dumps(up)
    f.write(j)