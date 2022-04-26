import http
import requests
from bs4 import BeautifulSoup
import json
up=()
#url1="https://just-scrape-it.com/"
#url2="https://just-scrape-it.com/collections/hoodie-sweat"
# url3="https://just-scrape-it.com/collections/tshirt-t-shirt-tee-shirt"
# url4="https://just-scrape-it.com/products/cagoule-scrape-original"
# url5="https://just-scrape-it.com/collections/maillots-ete"
url6="https://just-scrape-it.com/collections/stickers"
response=requests.get(url6)
#r=response.json()
 
if response.ok:
    soup=BeautifulSoup(response.text,"html.parser")
    nom_mcat3 =soup.find('li', class_="site-nav--active")
    print("catégorie: ",nom_mcat3.text)
    sty=soup.find_all('li', class_="grid__item grid__item--collection-template small--one-half medium-up--one-quarter")
    verify=soup.find_all('div',class_="grid-view-item product-card")
    for(i,u) in enumerate(verify):
        print("----------------$$$$$$$$$$--------------")
        print("article: n°",i)
        sty2=u.find('a', class_="grid-view-item__link grid-view-item__image-container full-width-link")
        price=u.find('span', class_="price-item price-item--sale")
        imag=u.find('img')
        print("nom:"+ sty2.text)
        print("prix" +price.text)
        print("http:"+imag['src'])