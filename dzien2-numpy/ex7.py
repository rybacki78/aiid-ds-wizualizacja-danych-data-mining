import numpy as np

# 1
a = np.array([[1, 4, 9, 16]])
print(np.sqrt(a))

# 2
b = np.array([[-1, -2, 3, -4]])
print(np.abs(b))

# 3
c = np.array([[0, np.pi / 2, np.pi, 3 * np.pi / 2]])
print(np.sin(c))
print(np.cos(c))
print(np.tan(c))
print(1 / np.tan(c))

# 4
d = np.array([[1, np.e, np.e**2]])
print(np.log(d))

# 5
f = np.array([[2, 4], [10, 20]])
sk = 5
print(np.power(f / 5, 2))

# 8
h = np.array([[10,100,1000]])
print(np.log10(h))
