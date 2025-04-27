import pandas as pd
import matplotlib.pyplot as plt

sprz = pd.read_csv('../data-sets/sprzedaz_polrocze_2024.csv', sep=",")

plt.plot(sprz['miesiac'], sprz['sprzedaz'], label='Sprzedaż', marker='o')
plt.plot(sprz['miesiac'], sprz['koszty'], label='Koszty', linestyle='--', marker='o')
plt.plot(sprz['miesiac'], sprz['zysk'], label='Zysk', linestyle='--', marker='o')

plt.xlabel('Miesiąc')
plt.ylabel('[PLN]')
plt.title("Sprzedaż pierwsze półrocze 2024")
plt.legend()
plt.grid(True)

plt.show()