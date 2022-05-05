

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

    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
proxyR=['160.19.232.85:3128',
'41.65.163.86:1981',
'85.25.111.162:5566',
'109.195.23.223:34031',
'64.201.163.133:80',
'50.217.22.108:80',
'50.206.25.107:80',
'50.202.210.119:80']
for i in range(10000):
    proxyR2=random.choice(proxyR)
    proxies = {
         'http': 'http://' + proxyR2,         
         'http': 'http://' + proxyR2}
   
url=['https://www.fratmat.info/morearticles/politique?pgno=1','https://www.fratmat.info/morearticles/conomie?pgno=1','https://www.fratmat.info/morearticles/societe?pgno=1','https://www.fratmat.info/morearticles/sports?pgno=1','https://www.fratmat.info/morearticles/culture?pgno=1',
'https://www.fratmat.info/morearticles/regions','https://www.fratmat.info/morearticles/tranger?pgno=1']
for i in url:
    response = requests.get(i,proxies=proxies,headers=headers)
    soup = BeautifulSoup(response.text,"html.parser")
    # children = soup.select_one('.col-md-6:nth-child(1)')
    final=soup.select('.fratmat-more-articles .article-info')
    final2=soup.select('.fratmat-more-articles .layout-ratio')
    final3=soup.select('.fratmat-more-articles')
    final4=soup.select('element.style')
    for span in final4:
        print(span.text)  
    for i in (final3):
        tilte3=i.find('a')   
    for (i,u) in enumerate (final):
        print("----------------$$$$$$$$$$--------------")
        print("article: n°",i)
        print(tilte3.text)
        title=u.find_all('a',class_="article-title fontSize23Height81")
        
        for i in (final2):
            title2=u.find('img')
        for a in title:
            print('titre:',a.text.strip())
            print('lien:',a['href'])
            print('image:',title2['src'],'\n')
             
              
    # for a in children1:
    #     print(a.text)
    #     print(a['href'])
       
# for (i,u) in enumerate(children2):
#     print('article n°:',i)
#     t=u.select('.article-title')
#     images=u.select('.layout-ratio img')
#     print(images['src'])
#     print('le titre :',t.text)
#     print('lien :',t['href'])
    
    
    # print('titre:',press1.text,'\t')
    # print('lien:',press1['href'],'\t')

      
    
    
    
#     proxy = {
#         'http': 'http://' + random_ip,         
#         'http': 'http://' + random_ip
#      }    

