from bs4 import BeautifulSoup
from lxml import html
import requests
# Ladányi Bertold - Autodidakta Web Scraping tanulás

# Név elérése
html_text = requests.get('https://www.mmk.hu/nevjegyzek?id=63726').text
soup = BeautifulSoup(html_text, 'lxml')
adatok = soup.find(id="content")
nev = adatok.find(id="title").text
print(f"Kontakt Neve:\n{nev}")

# Telefon és egyéb adatok
for match in soup.find_all('div', class_ = 'detail')[2:]: #A második class-tól listáz
    ujadat = match.text.rstrip() #Kiveszi a felesleges enter-eket
    ujadat2 = ujadat.replace(' ', '')
    print(ujadat2)

# Valamennyi új sor
print('\n\n')

# Az strip helyett a Prettify-al is megszépítheném az eredményt
