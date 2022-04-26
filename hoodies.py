import requests
from bs4 import BeautifulSoup
import json

#url1="https://just-scrape-it.com/"
url2="https://just-scrape-it.com/collections/hoodie-sweat"
# url3="https://just-scrape-it.com/collections/tshirt-t-shirt-tee-shirt"
# url4="https://just-scrape-it.com/products/cagoule-scrape-original"
# url5="https://just-scrape-it.com/collections/maillots-ete"
# url6="https://just-scrape-it.com/collections/"
response=requests.get(url2)
#r=response.json()
 
if response.ok:
    soup=BeautifulSoup(response.text,"html.parser")
    nom_mcat3 =soup.find('li', class_="site-nav--active")
    

    ul_article =soup.find('ul',class_="grid grid--uniform grid--view-items")
    art= soup.find_all('li',class_="grid__item grid__item--collection-template small--one-half medium-up--one-quarter")
    final=soup.find_all('span', class_="price-item price-item--regular")
    verify=soup.find_all('div',class_="grid-view-item product-card")
    print("catégorie: ",nom_mcat3.text)
    for (i, u) in enumerate(art):
        
        # arttt =u.find('div',class_="grid-view-item product-card")
        priceart=u.find('span',class_="price-item price-item--sale")
        imageart=u.find('img')
        final0=u.find('span', class_="price-item price-item--regular")

        # print("nom: ",arttt.text)
        
        for (i,u) in enumerate (verify):
            print("----------------$$$$$$$$$$--------------")
            print("article: n°",i)
            verify2=u.find('div',class_="h4 grid-view-item__title product-card__title")
            priceart=u.find('span',class_="price-item price-item--sale")
            imageart=u.find('img')
            print(verify2.text)
            print("le prix est: ",priceart.text)
            print("https:" + imageart['src'],'\n')
        
            
    print("----------------*******-------------")
    

    # with open("save.json","r", encoding='utf-8') as f:
    #     data=json.load(f)
    #     data["categorie:"]=nom_mcat.text.split()
    # up={"categorie:":nom_mcat.text.split(),"nom:":arttt.text}    
    # data.append("le prix est:"+priceart.text) 
    # data.append("https:" + imageart['src'])  
    # up.update(data)
    up=[]      
    # with open("save.json","w", encoding='utf-8') as f:
    #     up.append(nom_mcat3.text)
    #     # up.append(arttt.text)
    #     up.append(imageart)
    #     json.dump(up,f,indent=4)

   
    