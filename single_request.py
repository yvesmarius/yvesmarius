from weakref import proxy
import requests
from bs4 import BeautifulSoup
proxy={'http': 'http://51.79.50.22 :9300',
    }
url=['https://www.fratmat.info/politique','https://www.fratmat.info/sociéte',
'https://www.fratmat.info/sport','https://www.fratmat.info/culture','https://www.fratmat.info/économie']
for i in url:
    response = requests.get(i,proxies=proxy)
soup=BeautifulSoup(response.text,"html.parser")
navigation=soup.find_all('div', class_="article-info")
for (i,u) in enumerate(navigation):
    print("article:n",i)
    press1=u.find('a')
    press2=u.find('div', class_="publishTime")
    print(press1['href'])
    print(press1.text)
    

