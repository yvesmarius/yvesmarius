from selenium import webdriver
from selenium.webdriver.chrome.options import Options
browser = webdriver.chrome('chromedriver')
browser.get("https://just-scrape-it.com/collections/hoodie-sweat")
if browser.ok:
    browser2=browser.find_elements('a',class_="grid-view-item__link grid-view-item__image-container full-width-link")
    up=[]
    gt=browser2.text
    up.append(gt)
    print(up)