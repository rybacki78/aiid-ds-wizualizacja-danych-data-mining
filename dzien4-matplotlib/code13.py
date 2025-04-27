import pandas as pd
import matplotlib.pyplot as plt


data = {
    'product_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'price': [19.99, 29.99, 14.99, 49.99, 9.99, 39.99, 24.99, 34.99, 44.99, 15.99],
    'units_sold': [150, 85, 200, 50, 300, 75, 120, 95, 60, 180],
    'rating': [4.5, 4.2, 4.8, 3.9, 4.6, 4.1, 4.3, 4.0, 3.8, 4.7],
    'discount': [0.1, 0.05, 0.15, 0.0, 0.2, 0.1, 0.05, 0.08, 0.0, 0.12]
}

df = pd.DataFrame(data)
x_values = df['price']
y_values = df['units_sold']
colors = df['rating']
sizes = df['discount'] * 1000 + 50

plt.scatter(x_values, y_values, s=sizes, c=colors, alpha=0.7, cmap='viridis')

plt.colorbar(label='Ocena produktu')

plt.xlabel('Cena produktu (PLN)')
plt.ylabel('Liczba sprzedanych sztuk')
plt.title('Analiza sprzedaży')

plt.grid(True, alpha=0.3)

plt.show()