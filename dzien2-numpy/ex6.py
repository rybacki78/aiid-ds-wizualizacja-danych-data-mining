import numpy as np

# 1
a = np.array([[1, 2, 3]])
k = 10
print("a + k:", a + k)
print("a - k:", a - k)
print("a * k:", a * k)
print("a / k:", a / k)

# 2
b1 = np.array([[1, 2, 3]])
b2 = np.array([[4, 5, 6]])
print("b1 + b2:", b1 + b2)
print("b1 - b2:", b1 - b2)
print("b1 * b2:", b1 * b2)
print("b1 / b2:", b1 / b2)

# 8
h1 = np.array([[1, 2, 3]])
h2 = np.array([[10, 20, 30]]).T
print(h1 + h2)
print(h1 * h2)
