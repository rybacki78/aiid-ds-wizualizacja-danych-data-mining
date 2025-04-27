import matplotlib.pyplot as plt
import numpy as np

daty = np.arange('2024-01', '2025-01', dtype='datetime64')

index = np.arange(len(daty))

y_1 = index
y_2 = index ** 2
y_3 = index ** 3

plt.plot(daty, y_1, label='Liniowa')
plt.plot(daty, y_2, label='Kwadratowa')
plt.plot(daty, y_3, label='Sześcienna')

plt.xlabel('Miesiąc (2024)')
plt.ylabel('Wartość')
plt.title("Funkcje w roku 2024")
plt.legend()
plt.grid(True)

plt.show()