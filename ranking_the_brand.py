# -*- coding: utf-8 -*-
"""Ranking the brand.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L9SZxHxvpaqeZjj9d76iHLsFFnlJx5ep
"""

import requests
from bs4 import BeautifulSoup as bs

url="https://www.rankingthebrands.com/Brand-detail.aspx?brandID="
open("goodgleData.csv","w")
pageID=range(1,2)

for link in pageID:
  r=requests.get(url+str(link))
  if r.status_code!=200:
    print("url failed:",link)
    continue

print(url+str(link))
page=r.text
soup=bs(page,'html.parser')
titleSoup=soup.find_all('div',attrs=({'class':'pathLeft'}))[0]
title=titleSoup.find("span").text

awards=soup.find_all('div',attrs={'class':'rankingcell01'})

yearValue=soup.find_all('div',attrs={'class':'rankingcell02'})
year=[y for y in yearValue if yearValue.index(y)%2==0]
rank=[r for r in yearValue if yearValue.index(r)%2==1]

for ward in awards:
  i=awards.index(ward)
  data=[title,ward.text,year[i].text,rank[i].text]
  print(",".join(data),file=open("goodgleData.csv","a"))
  print(",".join(data))

