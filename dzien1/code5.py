# indeksowanie, "krojenie"

import numpy as np

a = np.array([2, 5, -2, 4, -7, 8, 9, 11, -23, -4, -7, 16, 1])
print("1:", a[5])  # Dostęp do elementu o indeksie 5.
print("2:", a[-2])  # Dostęp do elementu drugiego od tyłu.
print(
    "3:", a[3:6]
)  # Dostęp do elementów o indeksach od 3 do 5 (włącznie) - zasada przedziałów lewostronnie domkniętych, prawostronnie otwartych.
print("4:", a[:])  # Dostęp do wszystkich elementów.
print("5:", a[0:-1])  # Dostęp do wszystkich elementów z wyłączeniem ostatniego.
print("6:", a[:5])  # Dostęp od początku do elementu o indeksie 4.
print("1:", a[4:])  # Dostęp do elementów od indeksu 4 do końca.
print("2:", a[4:-1])  # Dostęp do elementów od indeksu 4 do końca bez ostatniego.
print(
    "3:", a[4:10:2]
)  # Dostęp do elementów o indeksach stanowiących ciąg arytmetyczny od 4 do 10 (z czwórką, ale bez dziesiątki) z krokiem równym 2
print("4:", a[::-1])  # Dostęp do elementów od tyłu do początku.
print("5:", a[::2])  # Dostęp do elementów o indeksach parzystych od początku.
print(
    "6:", a[::-2]
)  # Dostęp do elementów o indeksach “nieparzystych ujemnych” od początku.

print("-" * 30)

# tablica dwuwymiarowa
a = np.array([[3, 4, 5], [-3, 4, 8], [3, 2, 9]])
b = a[:2, 1:]
print(b)
print(np.shape(b))
c = a[1]
print(c)
print(np.shape(c))
d = a[1, :]
print(d)
print(np.shape(d))

print("-" * 30)

a = np.array([[3, 4, 5], [-3, 4, 8], [3, 2, 9]])
e = a[1:2, :]
print(e)
print(np.shape(e))
f = a[:, :2]
print(f)
print(np.shape(f))
g = a[1, :2]
print(g)
print(np.shape(g))
h = a[1:2, :2]
print(h)
print(np.shape(h))

print("-" * 30)

# zmienne a i b sa połączone, b to jest widok a
a = np.array([[3, 4, 5], [-3, 4, 8], [3, 2, 9]])
b = a[1:2, 1:]
print(b)
a[1][1] = 9
print(a)
print(b)
b[0][0] = -11
print(a)
print(b)

print("-" * 30)

# rozłączenie widoku
a = np.array([[3, 4, 5], [-3, 4, 8], [3, 2, 9]])
b = a[1:2, 1:].copy()
print(b)
a[1][1] = 9
print(a)
print(b)
b[0][0] = -11
print(a)
print(b)

print("-" * 30)

# Indeksowanie logiczne (fancy indexing, maski boolowskie)

a = np.array([2, 5, -2, 4, -7, 8, 9, 11, -23, -4, -7, 8, 1])
b = a[np.array([1, 3, 7])]
print(b)
c = a[[1, 3, 7]]
print(c)

a = np.array([2, 5, -2, 4, -7, 8, 9, 11, -23, -4, -7, 8, 1])
b = a > 0
print(b)
c = a[a > 0]
print(c)
d = a[(a > 5) & (a % 2 != 0)]  # znak & odpowiada za AND
print(d)
e = a[(a > 5) | (a % 2 != 0)]  # znak | odpowiada za OR
print(e)
f = a[(a > 5) ^ (a % 2 != 0)]  # znak ^ odpowiada za XOR
print(f)
g = a[~(a > 0)]
print(g)

# indeksowanie logiczne nie tworzy widoku!

a = np.array([2, 5, -2, 4, -7, 8, 9, 11, -23, -4, -7, 8, 1])
b = a[a > 0]
print(b)
b[0] = -5
print(a)
print(b)
a[1] = 20
print(a)
print(b)
