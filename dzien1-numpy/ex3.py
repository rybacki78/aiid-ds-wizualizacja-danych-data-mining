import numpy as np

a = np.arange(1, 6)
a.shape = (1,5)
print(a)

b = np.arange(1,5)
b.shape = (2,2)
print(b)

c = np.arange(10)
print(c)

d = np.arange(10, 31, 5)
print(d)

e = np.linspace(0, 1, num=5)
print(e)

f = np.zeros([2, 3])
print(f)

j = np.identity(4)
print(j)
