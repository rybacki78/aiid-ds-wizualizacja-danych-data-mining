import numpy as np

"""
Atrybut     Opis
shape 	    krotka z informacją o liczbie elementów dla każdego z wymiarów
size 	    liczba elementów w tablicy (łączna)
ndim 	    liczba wymiarów tablicy
nbytes 	    liczba bajtów jaką tablica zajmuje w pamięci
dtype 	    typ danych
"""

tab1 = np.array([2, -3, 4, -8, 1])
print("typ:", type(tab1))
print("shape:", tab1.shape)
print("size:", tab1.size)
print("ndim:", tab1.ndim)
print("nbytes:", tab1.nbytes)
print("dtype:", tab1.dtype)

print("-" * 30)

tab2 = np.array([[2, -3], [4, "-8"]])
print("typ:", type(tab2))
print("shape:", tab2.shape)
print("size:", tab2.size)
print("ndim:", tab2.ndim)
print("nbytes:", tab2.nbytes)
print("dtype:", tab2.dtype)

print("-" * 30)

"""
NumPy nie wspiera postrzępionych tablic! Poniższy kod wygeneruje błąd:
"""
tab3 = np.array([[2, -3], [4, -8, 5], [3]])
