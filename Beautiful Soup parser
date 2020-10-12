import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
html=urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Lowri.html').read()
soup=BeautifulSoup(html,'html.parser')
tags=soup('a')
links=list()
for tag in tags:
    links.append(tag.get('href',None))
print(links[17])

reps=0
while reps<6:
    reps=reps+1
    html=urllib.request.urlopen(links[17]).read()
    soup=BeautifulSoup(html,'html.parser')
    tags=soup('a')
    links=list()
    for tag in tags:
        links.append(tag.get('href',None))
    print(links[17])
