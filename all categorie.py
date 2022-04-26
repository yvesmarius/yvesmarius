

import requests
from bs4 import BeautifulSoup
import json
up=[]

#url="https://just-scrape-it.com/collection/"

url2=["https://just-scrape-it.com/collections/hoodie-sweat","https://just-scrape-it.com/collections/tshirt-t-shirt-tee-shirt",
"https://just-scrape-it.com/products/cagoule-scrape-original","https://just-scrape-it.com/collections/maillots-ete",
"https://just-scrape-it.com/collections/stickers"]
for i  in url2:
    response=requests.get(i)
    soup=BeautifulSoup(response.text,"html.parser")
    nom_mcat3 =soup.find('li', class_="site-nav--active")
    print("catégorie: ",nom_mcat3.text)
# response=requests.get(url3)
# response=requests.get(url4)
# response=requests.get(url5)
# response=requests.get(url6)
# #r=response.json()
# if response2.ok:
    
# nom_mcat3= nom_mcat2.find_all('li')
# nom_mcat4= nom_mcat3.find_all('a',href="/collections/tshirt-t-shirt-tee-shirt")
# print(nom_mcat4)
# "/collections/tshirt-t-shirt-tee-shirt"

# if response3.ok:
#     soup=BeautifulSoup(response3.text,"html.parser")
#     nom_mcat3 =soup.find('div',class_="section-header text-center")
#     print(nom_mcat3.text)
# if response4.ok:
#     soup=BeautifulSoup(response4.text,"html.parser")
#     nom_mcat4=soup.find('a', href="/products/cagoule-scrape-original", class_="site-nav__link site-nav__link--main site-nav__link--active")
#     print("collection:"+nom_mcat4.text)
# if response5.ok:
#     soup=BeautifulSoup(response5.text,"html.parser")
#     nom_mcat5 =soup.find('div',class_="section-header text-center")
#     print(nom_mcat5.text)
# if response6.ok:
#     soup=BeautifulSoup(response6.text,"html.parser")
#     nom_mcat6 =soup.find('div', class_="collection-hero__title-wrapper")
#     print(nom_mcat6.text)                