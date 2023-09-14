from urllib.request import urlopen
# pip install beautifulsoup4
from bs4 import BeautifulSoup 

html = urlopen("https://kurs.onliner.by/")
soup = BeautifulSoup(html, features="html.parser")
tags = soup.find_all("p", {'class':"value rise"})

print(f"{tags[0].text}, {tags[1].text}, {tags[2].text}")