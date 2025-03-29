import numpy as np

"""
Podstawowym bytem w bibliotece NumPy jest N-wymiarowa tablica zwana ndarray. Każdy element na tablicy traktowany jest jako typ dtype.

numpy.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)

    object - to co ma być wrzucone do tablicy
    dtype - typ
    copy - czy obiekty mają być skopiowane, domyślne True
    order - sposób układania: C (rzędy), F (kolumny), A, K
    subok - realizowane przez podklasy (jeśli True), domyślnie False
    ndmin - minimalny rozmiar (wymiar) tablicy
    like - tworzenie na podstawie tablic referencyjnej
"""

a = np.array([1, 2, 3])  # Standardowe domyślne.
print("a:", a)
print("typ a:", type(a))  # Sprawdzenie typu
b = np.array(
    [1, 2, 3.0]
)  # Jeden z elementów jest innego typu. Tu następuje zatem rozszerzenie do typu “największego”.
print("b:", b)
c = np.array([[1, 2], [3, 4]])  # Tu otrzymamy tablicę 2x2.
print("c:", c)
d = np.array([1, 2, 3], ndmin=2)  # W tej linijce otrzymana będzie tablica 2x1.
print("d:", d)
e = np.array([1, 2, 3], dtype=complex)  # Ustalenie innego typu - większego.
print("e:", e)
f = np.array(np.asmatrix("1 2; 3 4"))  # Skorzystanie z podtypu macierzowego.
print("f:", f)
g = np.array(np.asmatrix("1 2; 3 4"), subok=True)  # Zachowanie typu macierzowego.
print("g:", g)
print(type(g))
