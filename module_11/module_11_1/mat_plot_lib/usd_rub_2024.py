"""
Данный модуль отображает динамику курса USD/RUB с 09.09.2023 по 09.09.2024.
с использованием библиотек matplotlib и yfinance.
"""

import yfinance as yf
import matplotlib.pyplot as plt

ticker = 'RUB=X'

data = yf.download(ticker, start="2023-09-09", end="2024-09-09")

plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Close'], label="USD/RUB Exchange Rate")
plt.title("Курс доллара к рублю с 09.09.2023 по 09.09.2024")
plt.xlabel("Дата")
plt.ylabel("Курс USD/RUB")
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.show()
