import pandas as pd
import numpy as np

# series
print("--series--")
s = pd.Series([3, -5, 7, 4])
print(s)
print("values:")
print(s.values)
print("shape:")
print(s.shape)
print("size:")
print(s.size)

# dataframe
print("--dataframe--")
import pandas as pd

data = {'Country': ['Belgium', 'India', 'Brazil'],
        'Capital': ['Brussels', 'New Delhi', 'Brasília'],
        'Population': [11190846, 1303171035, 207847528]}
frame = pd.DataFrame(data)
print(frame)
print("--")
df = pd.DataFrame(data, columns=['Country', 'Population', 'Capital'])
print(df)
print("--")
print("Shape:", df.shape)
print("--")
print("Index:", df.index)
print("--")
print("columns:", df.columns)
print("--")
df.info()
print("--")
print(df.count())

# ladowanie danych
print("--- ladowanie danych ---")
price = pd.read_excel("data-sets/ceny21.xlsx")
print(price)
print("--")
gastro = pd.read_csv("data-sets/gastro21.csv", header=None).T
gastro[1] = gastro[1].astype(int)
gastro[2] = gastro[2].astype(int)
print(gastro)
gastro.info()




