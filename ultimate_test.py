import requests
from bs4 import BeautifulSoup
import json

from soupsieve import select

url2="https://just-scrape-it.com/"
l="collections/hoodie-sweat","collections/tshirt-t-shirt-tee-shirt","collections/maillots-ete","collections/stickers"
up=[]
for i in l:
    links=url2+i
    up.append(links)
print(up)
# enlever les caracteres bizzare dans fichier json
# data_links=json.dump(données,f,ensure_ascii=False,indent=4)
     
    # print(link.attrs['href'])
for i in up: 
    response=requests.get(i)
    if response.ok:    
        soup=BeautifulSoup(response.text,"html.parser")
        test=soup.select('.product-card')
        for (i,u) in enumerate (test):
            test2=u.find_all('span', class_="visually-hidden")
            for span in test2:
                print(span.text)
        # for (i,u) in enumerate(test):
        #     df=u.find('.product-card__title')
        #     print(df.text)    
        # for div in df:
        #     print(div.text)
        # for div in test2:
        #     print(div.text)
# for (i,u) in enumerate (test):
#     test2=u.find('li', class_="grid__item grid__item--collection-template small--one-half medium-up--one-quarter")
#     print(test2)