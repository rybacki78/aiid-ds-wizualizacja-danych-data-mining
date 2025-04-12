import numpy as np

"""
np.array - argumenty rzutowany na tablicę (coś po czym można iterować) - warto sprawdzić rozmiar/kształt
"""

tab = np.array([2, -3, 4])
print(tab)
print("size:", tab.size)
tab2 = np.array((4, -3, 3, 2))  # to samo co tab
print(tab2)
print("size:", tab2.size)
tab3 = np.array({3, 3, 2, 5, 2})  # set - usuwa duplikaty, tylko jeden element
print(tab3)
print("size:", tab3.size)
tab4 = np.array({"pl": 344, "en": 22})  # słownik, tylko jeden element
print(tab4)
print("size:", tab4.size)

# tylko listy albo krotki przenosza sie do tablicy!

print("-" * 30)

"""
np.zeros - tworzy tablicę wypełnioną zerami
"""
tab = np.zeros(4)
print(tab)
print(tab.shape)
tab2 = np.zeros([2, 3])
print(tab2)
print(tab2.shape)
tab3 = np.zeros([2, 3, 4])
print(tab3)
print(tab3.shape)

print("-" * 30)

"""
np.ones - tworzy tablicę wypełnioną jedynkami (to nie odpowiednik macierzy jednostkowej!)
"""

tab = np.ones(4)
print(tab)
print(tab.shape)
tab2 = np.ones([2, 3])
print(tab2)
print(tab2.shape)
tab3 = np.ones([2, 3, 4])
print(tab3)
print(tab3.shape)

print("-" * 30)

"""
np.diag - tworzy tablicę odpowiadającą macierzy diagonalnej
"""

print("tab0")
tab0 = np.diag([3, 4, 5])
print(tab0)
print("tab1")
tab1 = np.array([[2, 3, 4], [3, -4, 5], [3, 4, -5]])
print(tab1)
tab2 = np.diag(tab1)
print("tab2")
print(tab2)
tab3 = np.diag(tab1, k=1)
print("tab3")
print(tab3)
print("tab4")
tab4 = np.diag(tab1, k=-2)
print(tab4)
print("tab5")
tab5 = np.diag(np.diag(tab1))
print(tab5)

print("-" * 30)

"""np.arange - tablica wypełniona równomiernymi wartościami

Składnia: numpy.arange([start, ]stop, [step, ]dtype=None)

Zasada działania jest podobna jak w funkcji range, ale dopuszczamy liczby “z ułamkiem”.
"""

a = np.arange(3)
print(a)
b = np.arange(3.0)
print(b)
c = np.arange(3, 7)
print(c)
d = np.arange(3, 11, 2)
print(d)
e = np.arange(0, 1, 0.1)
print(e)
f = np.arange(3, 11, 2, dtype=float)
print(f)
g = np.arange(3, 10, 2)
print(g)

print("-" * 30)

"""np.linspace - tablica wypełniona równomiernymi wartościami wg skali liniowej"""

a = np.linspace(2.0, 3.0, num=5)
print(a)
b = np.linspace(2.0, 3.0, num=5, endpoint=False)
print(b)
c = np.linspace(10, 20, num=4)
print(c)
d = np.linspace(10, 20, num=4, dtype=int)
print(d)

print("-" * 30)

"""np.logspace - tablica wypełniona wartościami wg skali logarytmicznej

Składnia: numpy.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0)"""

a = np.logspace(2.0, 3.0, num=4)
print(a)
b = np.logspace(2.0, 3.0, num=4, endpoint=False)
print(b)
c = np.logspace(2.0, 3.0, num=4, base=2.0)
print(c)

print("-" * 30)

"""np.empty - pusta (niezainicjowana) tablica - konkretne wartości nie są “gwarantowane”"""

a = np.empty(3)
print(a)
b = np.empty(3, dtype=int)
print(b)

print("-" * 30)

"""np.identity - tablica przypominająca macierz jednostkową

np.eye - tablica z jedynkami na przekątnej (pozostałe zera)"""

print("a")
a = np.identity(4)
print(a)
print("b")
b = np.eye(4, k=1)
print(b)
print("c")
c = np.eye(4, k=2)
print(c)
print("d")
d = np.eye(4, k=-1)
print(d)
