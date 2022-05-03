from weakref import proxy
import requests
from bs4 import BeautifulSoup
import random
user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]

for i in range(1,4):
    # Pick a random user agent
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
proxy={
'http': 'http://160.19.232.85:3128'	,
}

   
url=["https://www.fratmat.info/politique",
"https://www.fratmat.info/economie",
"https://www.fratmat.info/societe",
"https://www.fratmat.info/sports",
"https://www.fratmat.info/culture",
"https://www.fratmat.info/region"]
for i in url:
    response = requests.get(i,proxies=proxy,headers=headers)
    print(response.json())
    soup = BeautifulSoup(response.text,"html.parser")
    navigation=soup.find('div', class_="col-md-6 col-xs-12")
    print(navigation)
for (i,u) in enumerate(navigation):
    print("article:n",i)
    press1=u.find_all('div', class_="article-info")
for(i,u) in enumerate(press1):
    press2=u.find('a')
    print(press2.text) 
    
    
    # print('titre:',press1.text,'\t')
    # print('lien:',press1['href'],'\t')

      
    
    
    
#     proxy = {
#         'http': 'http://' + random_ip,         
#         'http': 'http://' + random_ip
#      }    

