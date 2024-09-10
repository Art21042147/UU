"""
Данный модуль составляет круговую диаграмму населения крупнейших стран
с применением библиотек requests и matplotlib.
"""

import requests
import matplotlib.pyplot as plt


def get_country_wikidata_id(country_name):
    url = "https://www.wikidata.org/w/api.php"
    params = {
        "action": "wbsearchentities",
        "search": country_name,
        "language": "ru",
        "format": "json"
    }
    response = requests.get(url, params=params)
    data = response.json()
    if len(data['search']) > 0:
        return data['search'][0]['id']
    else:
        return None


def get_population_by_wikidata_id(wikidata_id):
    url = "https://www.wikidata.org/w/api.php"
    params = {
        "action": "wbgetentities",
        "ids": wikidata_id,
        "format": "json",
        "props": "claims"
    }
    response = requests.get(url, params=params)
    data = response.json()
    entities = data['entities'][wikidata_id]

    population_data = entities['claims'].get('P1082')

    if population_data:
        latest_population = population_data[-1]['mainsnak']['datavalue']['value']['amount']
        return int(latest_population)
    else:
        return None


countries = ['Россия', 'США', 'Китай', 'Индия', 'Бразилия', 'Индонезия',
             'Пакистан', 'Бангладеш', 'Мексика']

countries_population = {}

for country in countries:
    wikidata_id = get_country_wikidata_id(country)
    if wikidata_id:
        population = get_population_by_wikidata_id(wikidata_id)
        if population:
            countries_population[country] = population


labels = countries_population.keys()
sizes = countries_population.values()

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Население крупнейших стран мира')
plt.show()
