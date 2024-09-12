"""
Данный модуль, используя библиотеки requests, pandas и bs4 выводит:
топ 10 фильмов за последние 20 лет,
самого продуктивного режиссёра и самый популярный жанр за последние 20 лет.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

url = ("https://ru.wikipedia.org/wiki/250_%D0%BB%D1%83%D1%87%D1%88%D0%B8%D1%85_"
       "%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%D0%BE%D0%B2_%D0%BF%D0%BE_%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B8_IMDb")
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", class_="sortable")
data = []

for row in table.find_all("tr")[1:]:
    cells = row.find_all("td")
    position = cells[0].text.strip()
    title_cell = cells[1]
    title_link = title_cell.find("a")
    title = title_link.text.strip() if title_link else title_cell.text.strip()
    year = cells[2].text.strip()
    director = cells[3].text.strip()
    genre = cells[4].text.strip()
    data.append([title, year, director, genre])

df = pd.DataFrame(data, columns=["Название", "Год", "Режиссер", "Жанр"])

df["Год"] = pd.to_numeric(df["Год"], errors='coerce')

current_year = datetime.now().year
last_20_years = current_year - 20
recent_films = df[df["Год"] >= last_20_years]

top_10_recent_films = recent_films.sort_values("Год", ascending=False).head(10)
print("Топ 10 фильмов за последние 20 лет:")
print(top_10_recent_films[["Название", "Год", "Режиссер", "Жанр"]].to_string(index=False))

director_counts = recent_films["Режиссер"].value_counts()
most_productive_director = director_counts.idxmax()
most_productive_director_count = director_counts.max()
print(f"\nСамый продуктивный режиссер за последние 20 лет: {most_productive_director},"
      f" количество фильмов: {most_productive_director_count}")

most_common_genre_recent = recent_films["Жанр"].value_counts().idxmax()
print(f"\nСамый популярный жанр за последние 20 лет: {most_common_genre_recent}")
