import os
from bs4 import BeautifulSoup
import requests
html = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
bsObj = BeautifulSoup(html.content, "html.parser")
print(bsObj.title.string)
print(bsObj.findAll("a"))
for link in bsObj.findAll("a"):
       print(link.get('href') )