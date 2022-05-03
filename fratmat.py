import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
url="https://www.fratmat.info/"
l={"POLITIQUE","ÉCONOMIES","SOCIÉTÉ","SPORTS","CULTURE","RÉGIONS"}
ml=[]
for i in l:
    link=url+i
    ml.append(link)
with open("save.json",'w',encoding='utf8') as f:
    data_links=json.dump(ml,f,ensure_ascii=False,indent=4)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}    



  
response = requests.get('https://www.fratmat.info/',headers=headers)
soup=BeautifulSoup(response.text,"html.parser")
navigation=soup.find_all('div', class_="article-info")
for (i,u) in enumerate(navigation):
    press=u.find_all('a')
    print(press['href'])

    