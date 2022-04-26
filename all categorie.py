import requests
from bs4 import BeautifulSoup
import json
up=()
url1="https://just-scrape-it.com/"
url2="https://just-scrape-it.com/collections/hoodie-sweat"
url3="https://just-scrape-it.com/collections/tshirt-t-shirt-tee-shirt"
url4="https://just-scrape-it.com/products/cagoule-scrape-original"
url5="https://just-scrape-it.com/collections/maillots-ete"
url6="https://just-scrape-it.com/collections/stickers"
response2=requests.get(url2)
response3=requests.get(url3)
response4=requests.get(url4)
response5=requests.get(url5)
response6=requests.get(url6)
#r=response.json()
 
if response2.ok:
    soup=BeautifulSoup(response2.text,"html.parser")
    nom_mcat2 =soup.find('div',class_="section-header text-center")
    print(nom_mcat2.text)
if response3.ok:
    soup=BeautifulSoup(response3.text,"html.parser")
    nom_mcat3 =soup.find('div',class_="section-header text-center")
    print(nom_mcat3.text)
if response4.ok:
    soup=BeautifulSoup(response4.text,"html.parser")
    nom_mcat4=soup.find('a', href="/products/cagoule-scrape-original", class_="site-nav__link site-nav__link--main site-nav__link--active")
    print("collection:"+nom_mcat4.text)
if response5.ok:
    soup=BeautifulSoup(response5.text,"html.parser")
    nom_mcat5 =soup.find('div',class_="section-header text-center")
    print(nom_mcat5.text)
if response6.ok:
    soup=BeautifulSoup(response6.text,"html.parser")
    nom_mcat6 =soup.find('div', class_="collection-hero__title-wrapper")
    print(nom_mcat6.text)                