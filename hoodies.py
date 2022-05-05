import requests
from bs4 import BeautifulSoup
import json

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
        nom_mcat3 =soup.find('li', class_="site-nav--active")
        ul_article =soup.find('ul',class_="grid grid--uniform grid--view-items")
        art= soup.find_all('li',class_="grid__item grid__item--collection-template small--one-half medium-up--one-quarter")
        final=soup.find_all('span', class_="price-item price-item--regular")
        verify=soup.find_all('div',class_="grid-view-item product-card")
        #cagoule////
        cimg=soup.find('div', class_="module gf_module-center gf_module-center-lg gf_module--md gf_module--sm gf_module--xs")
        pricec=soup.find('span', class_="gf_product-price money")
        print("catégorie: ",nom_mcat3.text)
    # for (i, u) in enumerate(art):
        
    #     # arttt =u.find('div',class_="grid-view-item product-card")
    #     priceart=u.find('span',class_="price-item price-item--sale")
    #     imageart=u.find('img')
    #     final0=u.find('span', class_="price-item price-item--regular")

        # print("nom: ",arttt.text)    
    for(i,u) in enumerate (verify):
        print("----------------$$$$$$$$$$--------------")
        print("article: n°",i)
        verify2=u.find('div',class_="h4 grid-view-item__title product-card__title")
        priceart=u.find('span',class_="price-item price-item--sale")
        imageart=u.find('img')
        print(verify2.text)
        print("le prix est: ",priceart.text)
        print("https:" + imageart['src'],'\n')    
        #cagoule//////
        
    

    # with open("save.json","r", encoding='utf-8') as f:
    #     data=json.load(f)
    #     data["categorie:"]=nom_mcat.text.split()
    # up={"categorie:":nom_mcat.text.split(),"nom:":arttt.text}    
    # data.append("le prix est:"+priceart.text) 
    # data.append("https:" + imageart['src'])  
    # up.update(data)
    # up=[]      
    # with open("save.json","w", encoding='utf-8') as f:
    #     up.append(nom_mcat3.text)
    #     # up.append(arttt.text)
    #     up.append(imageart)
    #     json.dump(up,f,indent=4)

   
    