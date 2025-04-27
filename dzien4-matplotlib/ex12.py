import pandas as pd
import matplotlib.pyplot as plt

dane = pd.read_csv('../data-sets/temp_ols_2023.csv', sep=",")
dane['miesiac'] = pd.to_datetime(dane['miesiac'])

plt.plot(dane['miesiac'], dane['srednia'], label='Średnia')
plt.plot(dane['miesiac'], dane['maks'], label='Maks', linestyle='--')
plt.plot(dane['miesiac'], dane['min'], label='Min', linestyle='--')

plt.xlabel('Miesiąc (2024)')
plt.ylabel('Wartość')
plt.title("Temperatura w roku 2024")
plt.legend()
plt.grid(True)

plt.show()
