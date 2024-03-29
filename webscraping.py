import requests
from bs4 import BeautifulSoup

page_to_scrape = requests.get("https://terraria.wiki.gg/wiki/Ranged_weapons")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
# boost_gear_span = soup.find("span", class_="mw-headline", id="Boost_gear")
# print(boost_gear_span)

td_tags = soup.find_all("td", attrs={"class": "il2c"})
a_tags = []

for td in td_tags:
    a_tags_in_td = td.find_all('a', href=True, title=True)
    a_tags.extend(a_tags_in_td)

data_to_write = "\n".join([a.text for a in a_tags])

with open("ranged_weapons.txt", "w", encoding='utf-8') as file:
    file.write(data_to_write)
