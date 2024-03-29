import requests
from bs4 import BeautifulSoup

page_to_scrape = requests.get("https://terraria.wiki.gg/wiki/Ranged_weapons")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
# boost_gear_span = soup.find("span", class_="mw-headline", id="Boost_gear")
# print(boost_gear_span)

td_tags_weapon_name = soup.find_all("td", attrs={"class": "il2c"})
a_tags_weapon_name = []

for td in td_tags_weapon_name:
    a_tags_in_td = td.find_all('a', href=True, title=True)
    a_tags_weapon_name.extend(a_tags_in_td)

data_to_write = "\n".join([a.text for a in a_tags_weapon_name])

with open("ranged_weapons.txt", "w", encoding='utf-8') as file:
    file.write(data_to_write)

####### Alternative Option #########
weapon_list = []
for row in soup.find_all("tr"):
    if len(row.find_all('td')) != 6:
        continue
    else:
        name = row.find_all('td')[1].text.replace('\n', '')
        damage = row.find_all('td')[3].text.replace('\n', '')
        source = row.find_all('td')[4].text.replace('\n', '')
        notes = row.find_all('td')[5].text.replace('\n', '')
        weapon = name, damage, source, notes
        weapon_list.append(weapon)

for weapon in weapon_list:
    print("Weapon Name: ", weapon[0], "\n Damage: ", weapon[1], "\n Source: " , weapon[2],   "\n Notes: ", weapon[3], "\n")
