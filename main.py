


from bs4 import BeautifulSoup
f = open("recette.html","r") 
html_content=f.read()
f.close()
soup = BeautifulSoup(html_content,"html.parser")
search_h1 = soup.find("h1")

search_p = soup.find("div",class_="ingredients")
search_p2 = search_p.find_all("p")
print(search_p2[1])    
# for i, in search_p2:

print("le titre est: ",search_h1.text)



