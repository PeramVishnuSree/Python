import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup
html=urllib.request.urlopen('http://python-data.dr-chuck.net/comments_581818.html').read()
soup=BeautifulSoup(html,'html.parser')
tags=soup('span')
lst=list()

for tag in tags:
    line=str(tag)
    numbers=re.findall('[0-9.]+',line)
    for i in numbers:
        lst.append(int(i))
print(sum(lst))
