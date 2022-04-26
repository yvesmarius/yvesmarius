import requests
from bs4 import BeautifulSoup
import json
up=()
#url1="https://just-scrape-it.com/"
#url2="https://just-scrape-it.com/collections/hoodie-sweat"
# url3="https://just-scrape-it.com/collections/tshirt-t-shirt-tee-shirt"
url4="https://just-scrape-it.com/products/cagoule-scrape-original"
# url5="https://just-scrape-it.com/collections/maillots-ete"
# url6="https://just-scrape-it.com/collections/"
response=requests.get(url4)
#r=response.json()
 
if response.ok:
    soup=BeautifulSoup(response.text,"html.parser")
    nom_mcat3=soup.find('a', href="/products/cagoule-scrape-original", class_="site-nav__link site-nav__link--main site-nav__link--active")
    pricec=soup.find('span', class_="gf_product-price money")
    cimg=soup.find('div', class_="module gf_module-center gf_module-center-lg gf_module--md gf_module--sm gf_module--xs")
    tyc=soup.find('h1', itemprop="name")
    
    #typ=soup<span class="site-nav__label"
    print("----------------$$$$$$$$$$--------------")
    
    print("la categorie: ",nom_mcat3.text,"\n")
    
    for (i,u) in enumerate (cimg):
        cimg2=u.find('img')
        print("nom :"+ tyc.text)
        print("le prix est :",pricec.text,"\n") 
        print("https:" + cimg2['src'],"\n")
           
    print("----------------*******-------------")    
        #print(cimg2)
    
