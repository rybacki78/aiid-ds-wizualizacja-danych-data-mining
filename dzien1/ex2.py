import numpy as np


a = np.array([[1, 2, 3], [4, 5, 6]])

print("typ:", type(a))
print("shape:", a.shape)
print("size:", a.size)
print("ndim:", a.ndim)
print("nbytes:", a.nbytes)
print("dtype:", a.dtype)

print("-" * 30)

b = np.array([[7, 8], [9, 10], [11, 12]])
print("typ:", type(b))
print("shape:", b.shape)
print("size:", b.size)
print("ndim:", b.ndim)
print("nbytes:", b.nbytes)
print("dtype:", b.dtype)

print("-" * 30)

c = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])

print("typ:", type(c))
print("shape:", c.shape)
print("size:", c.size)
print("ndim:", c.ndim)
print("nbytes:", c.nbytes)
print("dtype:", c.dtype)
