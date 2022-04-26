import requests
from bs4 import BeautifulSoup
import json
up=()
#url1="https://just-scrape-it.com/"
#url2="https://just-scrape-it.com/collections/hoodie-sweat"
# url3="https://just-scrape-it.com/collections/tshirt-t-shirt-tee-shirt"
# url4="https://just-scrape-it.com/products/cagoule-scrape-original"
url5="https://just-scrape-it.com/collections/maillots-ete"
# url6="https://just-scrape-it.com/collections/"
response=requests.get(url5)
#r=response.json()
 
if response.ok:
    soup=BeautifulSoup(response.text,"html.parser")
    nom_mcat3 =soup.find('div',class_="section-header text-center")
    print(nom_mcat3.text)
    art= soup.find_all('li',class_="grid__item grid__item--collection-template small--one-half medium-up--one-quarter")
    for (i, u) in enumerate(art):
        print("----------------$$$$$$$$$$--------------")
        print("article: n°",i)
        arttt =u.find('div',class_="h4 grid-view-item__title product-card__title")
        priceart=u.find('span',class_="price-item price-item--sale")
        imageart=u.find('img')
        
        er=print("nom: ",arttt.text)
        print("le prix est: ",priceart.text)
        print("https:" + imageart['src'],'\n')
        