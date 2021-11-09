import requests
from bs4 import BeautifulSoup
import tkinter
#Ladányi Bertold Web_Scrape (2/3)
#2021.11.09

#URL kettébontás továbbfejlesztése
url =("https://www.mmk.hu/kereses/tagok?elem=10&tagozat=&iranyito_szam=&submit=Keres%C3%A9s&szakterulet_22=&szakmaiCim=&megye=1&darab=1000&kamarai_szam=&tanusitvany=&kamarai_szam2=&oldal={n}&nev=&szakterulet2=&telepules=&szakterulet3=0")
aurl = url[0:180]
burl = url[183:]

n = 1
while n < 101:
    hackedurl = (aurl + str(n) + burl)
    print(hackedurl)
    n += 1
