import numpy as np

# 1
print("a")
a = np.arange(1,7)
print(a.reshape(2,3))

# 2
print("b")
b = np.array([[1,2],[3,4],[5,6]])
print(b.flatten())

# 3
print("d")
d = np.array([[1,2,3],[4,5,6]])
print(d.T)

# 4
print("e")
e1 = np.array([1,2,3])
e2 = np.array([4,5,6])
print(np.hstack((e1,e2)))

# 5
print("f")
f1 = np.array([[1,2,3]])
f2 = np.array([[4,5,6]])
print(np.concatenate((f1.T,f2.T), axis=1))