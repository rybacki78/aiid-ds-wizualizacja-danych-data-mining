import pandas as pd

# sortowanie

# Przykładowa ramka danych
df = pd.DataFrame({
    'Name': ['Alice', 'Tom', 'Charlie'],
    'Age': [25, 42, 35],
    'Salary': [50000, 60000, 70000]
})

# Sortowanie po kolumnie 'Age'
s1= df.sort_values(by='Age')
print(s1)
# Sortowanie w odwrotnej kolejności
s2 = df.sort_values(by='Salary', ascending=False)
print(s2)
# Sortowanie według 'Age' rosnąco, a następnie 'Salary' malejąco
s3 = df.sort_values(by=['Age', 'Salary'], ascending=[True, False])
print(s3)

# Sortowanie inplace (zamiana istniejącej zmiennej)
df.sort_values(by='Age', inplace=True)
print(df)

# NaN
df2 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Dave'],
    'Age': [25, 30, None, 35],
    'Salary': [50000, None, 70000, 60000]
})

# Sortowanie z NaN na końcu
s2 = df2.sort_values(by='Age', na_position='last')
print(s2)
# Sortowanie z NaN na początku
s3 = df2.sort_values(by='Age', na_position='first')
print(s3)