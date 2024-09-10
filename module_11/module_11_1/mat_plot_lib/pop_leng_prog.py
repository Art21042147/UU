"""
Данный модуль выводит диаграмму популярности языков программирования
за последние 10 лет с использованием библиотек matplotlib и numpy.
"""

import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2014, 2024)
popularity = {
    "Python": [10, 12, 14, 16, 18, 21, 25, 28, 31, 34],
    "Java": [20, 19, 18, 17, 16, 15, 14, 13, 12, 11],
    "C++": [15, 16, 17, 18, 18, 17, 16, 15, 14, 13],
    "JavaScript": [17, 18, 19, 20, 21, 23, 25, 26, 27, 28],
    "C#": [13, 14, 15, 15, 16, 16, 16, 15, 14, 13]
}

fig, ax = plt.subplots(figsize=(10, 6))

width = 0.15
offset = np.linspace(-2*width, 2*width, len(popularity))

for i, (language, values) in enumerate(popularity.items()):
    ax.bar(years + offset[i], values, width, label=language)

ax.set_xlabel('Год')
ax.set_ylabel('Популярность (%)')
ax.set_title('Популярность языков программирования (2014-2023)')
ax.set_xticks(years)
ax.legend()

plt.show()
