buildings ={
"Buri khalifa": "United Arab Emirates",
"Shanghai Tower": "China",
"Abraj AL-Bait Clock Tower": "Saudi Arabia",
"Ping An Finance Center": "China",
"Latte Wortd Tower": "South Korea",
"One Wor ld Trade Center": "United States",
"Guangzhou CTF Finance Center": "China",
"Tianjin CTF Finance Center": "China",
"Zun Taipei": "Taiwan",
"Shanghai World Financial Čenter": "China",
"Centrat Park Tower": "United States",
"Lakhta Center" : "Russia",
"Landmark": "Vietnam",
"Changsha IFS Tower": "China",
"Petronas Tower 1": "Mataysia",
"Petronas Tower 2": "Melaysia",
"Zifeng Tower": "China",
"Suzhou IFS": "China",
"The Exchange": "Malaysia",
"Millis Tower": "United States"
}
country_buildings = {}

for key, value in buildings.items():
    if value not in country_buildings:
        country_buildings[value] = [key]
    else:
        country_buildings[value].append(key)

print(country_buildings)
for i,v in country_buildings.items():
    print(str(i) + ":" + str(v))
